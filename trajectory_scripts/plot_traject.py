import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('timed_waypoints_yaw20_cf1.csv', header=0, delimiter=',', skiprows=0, usecols=[1, 2, 3])
datalist = data.values.tolist()
# Convert to a NumPy array
data_array = np.array(datalist)

# Your data
x = data_array[:, 0]
y = data_array[:, 1]
z = data_array[:, 2]

#ax = plt.figure().add_subplot(projection='3d')

#ax.plot(x, y, z, label='3D measured trajectory')

data2 = pd.read_csv('timed_waypoints_yaw20_cf2.csv', header=0, delimiter=',', skiprows=0, usecols=[0, 1, 2, 3])
datalist2 = data2.values.tolist()
# Convert to a NumPy array
data_array2 = np.array(datalist2)


x2 = data_array2[:, 1]
y2 = data_array2[:, 2]
z2 = data_array2[:, 3]

ax = plt.figure().add_subplot(projection='3d')
ax.plot(x, y, z, label='3D trajectory 1')
ax.plot(x2, y2, z2, label='3D trajectory 2')       
ax.legend()

ax.set_title('Mirrored Trajectories for swarm flight')

plt.show()