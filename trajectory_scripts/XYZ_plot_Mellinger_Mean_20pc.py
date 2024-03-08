import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
import pandas as pd
import math

data = pd.read_csv('traject12_log2C_Robust_Mellinger_cf8.csv', header=0, delimiter=',', skiprows=0, usecols=[1, 2, 3, 4])
datalist = data.values.tolist()
# Convert figure8 to a NumPy array
data_array = np.array(datalist)

x = data_array[:, 0]
y = data_array[:, 1]
z = data_array[:, 2]
yaw = data_array[:, 3]

data2 = pd.read_csv('traject12_log6C_Robust_Mellinger_cf8.csv', header=0, delimiter=',', skiprows=0, usecols=[1, 2, 3, 4])
datalist2 = data2.values.tolist()
# Convert figure8 to a NumPy array
data_array2 = np.array(datalist2)

data3 = pd.read_csv('traject12_log3C_Robust_Mellinger_cf8.csv', header=0, delimiter=',', skiprows=0, usecols=[1, 2, 3, 4])
datalist3 = data3.values.tolist()
# Convert figure8 to a NumPy array
data_array3 = np.array(datalist3)

data4 = pd.read_csv('traject12_log4C_Robust_Mellinger_cf8.csv', header=0, delimiter=',', skiprows=0, usecols=[1, 2, 3, 4])
datalist4 = data4.values.tolist()
# Convert figure8 to a NumPy array
data_array4 = np.array(datalist4)

data5 = pd.read_csv('traject12_log5C_Robust_Mellinger_cf8.csv', header=0, delimiter=',', skiprows=0, usecols=[1, 2, 3, 4])
datalist5 = data5.values.tolist()
# Convert figure8 to a NumPy array
data_array5 = np.array(datalist5)

matrix_x=np.column_stack((data_array[:, 0], data_array2[:, 0], data_array3[:, 0], data_array4[:, 0], data_array5[:, 0]))
mean_x = np.mean(matrix_x, axis=1)
max_x = np.max(matrix_x, axis=1)
min_x = np.min(matrix_x, axis=1)


matrix_y=np.column_stack((data_array[:, 1], data_array2[:, 1], data_array3[:, 1], data_array4[:, 1], data_array5[:, 1]))
mean_y = np.mean(matrix_y, axis=1)
max_y = np.max(matrix_y, axis=1)
min_y = np.min(matrix_y, axis=1)

matrix_z=np.column_stack((data_array[:, 2], data_array2[:, 2], data_array3[:, 2], data_array4[:, 2], data_array5[:, 2]))
mean_z = np.mean(matrix_z, axis=1)
max_z = np.max(matrix_z, axis=1)
min_z = np.min(matrix_z, axis=1)

matrix_yaw=np.column_stack((data_array[:, 3], data_array2[:, 3], data_array3[:, 3], data_array4[:, 3], data_array5[:, 3]))
mean_yaw = np.mean(matrix_yaw, axis=1)
max_yaw = np.max(matrix_yaw, axis=1)
min_yaw = np.min(matrix_yaw, axis=1)

dataR = pd.read_csv('timed_waypoints_yaw16.csv', header=0, delimiter=',', skiprows=0)
datalistR = dataR.values.tolist()
# Convert figure8 to a NumPy array
data_arrayR = np.array(datalistR)

t = data_arrayR[:, 0]
xR = data_arrayR[:, 1]
yR = data_arrayR[:, 2]
zR = data_arrayR[:, 3]

Ref_yaw = data_arrayR[:, 4]/math.pi*180

# Function to convert degrees to the desired format
def convert_degrees(degrees):
    # Convert to range [0, 360)
    degrees %= 360
    
    # Convert to the desired format
    if degrees <= 180:
        return degrees
    else:
        return degrees - 360

# Apply the conversion function to each element in the dataset
yawR = np.vectorize(convert_degrees)(Ref_yaw)


if __name__ == "__main__":
  # Create 3x1 sub plots
  gs = gridspec.GridSpec(6, 1)
  fig = plt.figure()

  ax = plt.subplot(gs[1, 0]) # row 0
  ax.plot(mean_x)
  ax.plot(xR)
  ax.fill_between(range(len(mean_x)), min_x, max_x, color='red', alpha=0.4, label='Maximum-minimum')
  ax.set_ylabel("x [meter]")
  plt.title('40 seconds, 10 pieces Mean trajectory')


  ax = plt.subplot(gs[2, 0]) # row 2
  ax.plot(mean_y)
  ax.plot(yR)
  ax.fill_between(range(len(mean_y)), min_y, max_y, color='red', alpha=0.4, label='Maximum-minimum')
  ax.set_ylabel("y [meter]")

  ax = plt.subplot(gs[3, 0]) # row 3
  ax.plot(mean_z)
  ax.plot(zR)
  ax.fill_between(range(len(mean_z)), min_z, max_z, color='red', alpha=0.4, label='Maximum-minimum')
  ax.set_ylabel("z [meter]")

  ax = plt.subplot(gs[4, 0]) # row 4
  ax.plot(mean_yaw, label='Mean')
  ax.plot(yawR, label='Reference')
  ax.fill_between(range(len(mean_yaw)), min_yaw, max_yaw, color='red', alpha=0.4, label='Maximum-minimum')
  ax.set_ylabel("yaw [degree]")
  ax.set_xlabel("time [ms]")
  ax.set_ylim(-200, 200)
  ax.set_yticks([-180, 0, 180])
  ax.legend(loc='lower right')

  plt.show()

  #ax = plt.subplot(gs[5, 0]) # row 5
  #ax.plot(t, np.degrees(evals[:,12]))
  #ax.set_ylabel("yaw [deg]")

  #ax = plt.subplot(gs[6, 0]) # row 5
  #ax.plot(ts, np.degrees(evals[:,13]))
  #ax.set_ylabel("roll [deg]")

  #ax = plt.subplot(gs[7, 0]) # row 5
  #ax.plot(ts, np.degrees(evals[:,14]))
  #ax.set_ylabel("pitch [deg]")
    
    
    #plt.plot(y, label='Desired X Position', marker='o')
    #plt.plot(y2, label='Measured X Position', marker='x')

    # Adding labels and title
    ##plt.xlabel('Time')
    #plt.ylabel('X Position')
    #plt.title('Measured vs Desired X Position over Time')

    # Adding legend
    #plt.legend()

    # Display the plot
    #plt.show()