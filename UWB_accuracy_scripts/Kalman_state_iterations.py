import logging
import time
from threading import Timer

import cflib.crtp  # noqa
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.utils import uri_helper

uri = uri_helper.uri_from_env(default='radio://0/1/2M/E7E7E7E7E7')

logging.basicConfig(level=logging.ERROR)

# number of measurements
i=1
iter=46

class LoggingExample:
  
    def __init__(self, link_uri):
        """ Initialize and run the example with the specified link_uri """

        self._cf = Crazyflie(rw_cache='./cache')

        # Connect some callbacks from the Crazyflie API
        self._cf.connected.add_callback(self._connected)
        self._cf.disconnected.add_callback(self._disconnected)
        self._cf.connection_failed.add_callback(self._connection_failed)
        self._cf.connection_lost.add_callback(self._connection_lost)

        print('Connecting to %s' % link_uri)

        # Try to connect to the Crazyflie
        self._cf.open_link(link_uri)

        # Variable used to keep main loop occupied until disconnect
        self.is_connected = True

        self.logged_data=[]

    def _connected(self, link_uri):
        """ This callback is called form the Crazyflie API when a Crazyflie
        has been connected and the TOCs have been downloaded."""
        print('Connected to %s' % link_uri)

        # The definition of the logconfig can be made before connecting
        self._lg_kalm = LogConfig(name='kalman', period_in_ms=10)
        self._lg_kalm.add_variable('kalman.stateX', 'float')
        self._lg_kalm.add_variable('kalman.stateY', 'float')
        self._lg_kalm.add_variable('kalman.stateZ', 'float')

        # Adding the configuration cannot be done until a Crazyflie is
        # connected, since we need to check that the variables we
        # would like to log are in the TOC.
        try:
            self._cf.log.add_config(self._lg_kalm)
            # This callback will receive the data
            self._lg_kalm.data_received_cb.add_callback(self._kalm_log_data)
            # This callback will be called on errors
            self._lg_kalm.error_cb.add_callback(self._kalm_log_error)
            # Start the logging
            self._lg_kalm.start()
        except KeyError as e:
            print('Could not start log configuration,'
                  '{} not found in TOC'.format(str(e)))
        except AttributeError:
            print('Could not add Stabilizer log config, bad configuration.')

        # Start a timer to disconnect in 10s
        t = Timer(10, self._cf.close_link)
        t.start()
        #time.sleep(5)
        #self._cf.close_link()

    def _kalm_log_error(self, logconf, msg):
        """Callback from the log API when an error occurs"""
        print('Error when logging %s: %s' % (logconf.name, msg))

    def _kalm_log_data(self, timestamp, data, logconf):
        """Callback from a the log API when data arrives"""
        log_entry = {'timestamp': timestamp, 'log_name': logconf.name}
        log_entry.update(data)
        self.logged_data.append(log_entry)
        print(f'[{timestamp}][{logconf.name}]: ', end='')
        for name, value in data.items():
            print(f'{name}: {value:3.3f} ', end='')
        print()

    def _connection_failed(self, link_uri, msg):
        """Callback when connection initial connection fails (i.e no Crazyflie
        at the specified address)"""
        print('Connection to %s failed: %s' % (link_uri, msg))
        self.is_connected = False

    def _connection_lost(self, link_uri, msg):
        """Callback when disconnected after a connection has been made (i.e
        Crazyflie moves out of range)"""
        print('Connection to %s lost: %s' % (link_uri, msg))

    def _disconnected(self, link_uri):
        """Callback when the Crazyflie is disconnected (called in all cases)"""
        print('Disconnected from %s' % link_uri)
        self.is_connected = False

    def save_to_csv(self, filename):
        import csv

        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['timestamp', 'log_name', 'kalman.stateX', 'kalman.stateY', 'kalman.stateZ']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for entry in self.logged_data:
                writer.writerow(entry)


if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    while i<=iter:
        # Generate a new CSV filename based on the iteration
        csv_filename = f'power_logged_data_kalman2_z_{i}.csv'

        le = LoggingExample(uri)

        # The Crazyflie lib doesn't contain anything to keep the application alive,
        # so this is where your application should do something. In our case we
        # are just waiting until we are disconnected.
        while le.is_connected:
            time.sleep(1)

        # Save data to the generated CSV file
        le.save_to_csv(filename=csv_filename)
        print('move')

        i+=1

        # Sleep for 13 seconds before restarting
        time.sleep(13)

