import time
import pandas as pd

import cflib.crtp
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm
from cflib.crazyflie.syncLogger import SyncLogger
from cflib.crazyflie.mem import MemoryElement
from cflib.crazyflie.mem import Poly4D

import os

class Uploader:
    def __init__(self):
        self._is_done = False
        self._sucess = True

    def upload(self, trajectory_mem):
        print('Uploading data')
        trajectory_mem.write_data(self._upload_done,
                                  write_failed_cb=self._upload_failed)

        while not self._is_done:
            time.sleep(0.2)

        return self._sucess

    def _upload_done(self, mem, addr):
        print('Data uploaded')
        self._is_done = True
        self._sucess = True

    def _upload_failed(self, mem, addr):
        print('Data upload failed')
        self._is_done = True
        self._sucess = False

def wait_for_position_estimator(scf):
    print('Waiting for estimator to find position...')

    log_config = LogConfig(name='Kalman Variance', period_in_ms=500)
    log_config.add_variable('kalman.varPX', 'float')
    log_config.add_variable('kalman.varPY', 'float')
    log_config.add_variable('kalman.varPZ', 'float')

    var_y_history = [1000] * 10
    var_x_history = [1000] * 10
    var_z_history = [1000] * 10

    threshold = 0.001

    with SyncLogger(scf, log_config) as logger:
        for log_entry in logger:
            data = log_entry[1]

            var_x_history.append(data['kalman.varPX'])
            var_x_history.pop(0)
            var_y_history.append(data['kalman.varPY'])
            var_y_history.pop(0)
            var_z_history.append(data['kalman.varPZ'])
            var_z_history.pop(0)

            min_x = min(var_x_history)
            max_x = max(var_x_history)
            min_y = min(var_y_history)
            max_y = max(var_y_history)
            min_z = min(var_z_history)
            max_z = max(var_z_history)

            # print("{} {} {}".
            #       format(max_x - min_x, max_y - min_y, max_z - min_z))

            if (max_x - min_x) < threshold and (
                    max_y - min_y) < threshold and (
                    max_z - min_z) < threshold:
                break


def reset_estimator(scf):
    cf = scf.cf
    cf.param.set_value('kalman.resetEstimation', '1')
    time.sleep(0.1)
    cf.param.set_value('kalman.resetEstimation', '0')
    wait_for_position_estimator(scf)


def activate_high_level_commander(scf):
    scf.cf.param.set_value('commander.enHighLevel', '1')


def activate_mellinger_controller(scf):
    scf.cf.param.set_value('stabilizer.controller', '2')

#set to 1 for robust tdoa
def activate_robust_tdoa(cf):
    cf.param.set_value('kalman.robustTdoa', '0')


data1 = pd.read_csv("yaw20_cf1.csv", header=None, delimiter=',', skiprows=1)
data2 = pd.read_csv("yaw20_cf2.csv", header=None, delimiter=',', skiprows=1)
# Convert the DataFrame to a list of lists
traject1 = data1.values.tolist()
traject2 = data2.values.tolist()

def upload_trajectory(cf, trajectory_id, trajectory):
    trajectory_mem = cf.mem.get_mems(MemoryElement.TYPE_TRAJ)[0]

    total_duration = 0
    for row in trajectory:
        duration = row[0]
        x = Poly4D.Poly(row[1:9])
        y = Poly4D.Poly(row[9:17])
        z = Poly4D.Poly(row[17:25])
        yaw = Poly4D.Poly(row[25:33])
        trajectory_mem.poly4Ds.append(Poly4D(duration, x, y, z, yaw))
        total_duration += duration

    upload_result = Uploader().upload(trajectory_mem)
    if not upload_result:
        print('Upload failed, aborting!')
        sys.exit(1)
    cf.high_level_commander.define_trajectory(trajectory_id, 0,
                                              len(trajectory_mem.poly4Ds))
    return total_duration

# _______________________________
# Essential Functions
# _______________________________

# TAKE OFF
DEFAULT_HEIGHT = 0.3
SPACING = 0.25
def take_off(scf):
    cf = scf.cf
    commander = cf.high_level_commander

    # Take off
    commander.takeoff(DEFAULT_HEIGHT, 2.0)
    time.sleep(3.0)

def position_callback(timestamp, data, logconf):
    global log_positions  # Add a global flag
    if log_positions:  # Check if logging is enabled
        x = data['stateEstimate.x']
        y = data['stateEstimate.y']
        z = data['stateEstimate.z']
        yaw = data['stateEstimate.yaw']

        file_path = 'traject20_log2_Robust_Mellinger.csv'
        file_exists = os.path.exists(file_path)

        # Write headers only if the file doesn't exist
        with open(file_path, 'a', newline='') as file:
            df = pd.DataFrame({'timestamp': [timestamp], 'stateEstimate.x': [x], 'stateEstimate.y': [y], 'stateEstimate.z': [z], 'stateEstimate.yaw': [yaw]})
            df.to_csv(file, index=False, header=not file_exists, mode='a')

def start_position_printing(scf):
    global log_positions  # Add a global flag
    log_positions = False  # Initialize the flag to False

    #log_conf = LogConfig(name='Kalman', period_in_ms=100)
    #log_conf.add_variable('kalman.stateX', 'float')
    #log_conf.add_variable('kalman.stateY', 'float')
    #log_conf.add_variable('kalman.stateZ', 'float')
    #log_conf.add_variable('kalman.stateD2', 'float')

    log_conf = LogConfig(name='Stabilizer', period_in_ms=100)
    log_conf.add_variable('stateEstimate.x', 'float')
    log_conf.add_variable('stateEstimate.y', 'float')
    log_conf.add_variable('stateEstimate.z', 'float')
    log_conf.add_variable('stateEstimate.yaw', 'float')

    scf.cf.log.add_config(log_conf)
    log_conf.data_received_cb.add_callback(position_callback)
    log_conf.start()

def run_shared_sequence(scf, seq_args):
    global log_positions
    cf = scf.cf

    commander = cf.high_level_commander
    trajectory_id = 1

    # Take off
    duration = upload_trajectory(cf, trajectory_id, seq_args)
    relative = False

    time.sleep(2)

    # Execute trajectory
    commander.start_trajectory(trajectory_id, 1.0, relative)
    log_positions = True
    time.sleep(duration) 
    log_positions = False
    time.sleep(6)

    # Go back to initial position and land again
    commander.land(0.0, 2.0)
    time.sleep(2)
    commander.stop()

URI1 = 'radio://0/1/2M/E7E7E7E7E7'
URI2 = 'radio://0/1/2M/E7E7E7E7E8'

# URIS of swarm
uris = {
    URI1,
    URI2,
    # Add more URIs if you want more copters in the swarm
}

# Parameters of Swarm
seq_args = {
    URI1: [traject1],
    URI2: [traject2],
}

if __name__ == '__main__':
    cflib.crtp.init_drivers()
    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:

        # Activate HL commander and reset estimator
        swarm.parallel_safe(activate_high_level_commander)
        swarm.parallel_safe(activate_mellinger_controller)
        swarm.parallel_safe(activate_robust_tdoa)
        swarm.parallel_safe(reset_estimator)
        swarm.parallel_safe(start_position_printing)

        swarm.parallel_safe(take_off)

        input("enter to continue")

        swarm.parallel_safe(run_shared_sequence, args_dict=seq_args)
