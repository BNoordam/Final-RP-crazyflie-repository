import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
import pandas as pd
import math

# Loading and converting the trajectories to plot
data = pd.read_csv('traject13_log17C_Robust_Mellinger_cf8.csv', header=0, delimiter=',', skiprows=0, usecols=[1, 2, 3, 4])
datalist = data.values.tolist()
data_array = np.array(datalist)

x = data_array[:, 0]
y = data_array[:, 1]
z = data_array[:, 2]
yaw = data_array[:, 3]

data2 = pd.read_csv('traject13_log6C_Robust_Mellinger_cf8.csv', header=0, delimiter=',', skiprows=0, usecols=[1, 2, 3, 4])
datalist2 = data2.values.tolist()
data_array2 = np.array(datalist2)

data3 = pd.read_csv('traject13_log8T_Robust_Mellinger_cf8.csv', header=0, delimiter=',', skiprows=0, usecols=[1, 2, 3, 4])
datalist3 = data3.values.tolist()
data_array3 = np.array(datalist3)

data4 = pd.read_csv('traject13_log9C_Robust_Mellinger_cf8.csv', header=0, delimiter=',', skiprows=0, usecols=[1, 2, 3, 4])
datalist4 = data4.values.tolist()
data_array4 = np.array(datalist4)

data5 = pd.read_csv('traject13_log16C_Robust_Mellinger_cf8.csv', header=0, delimiter=',', skiprows=0, usecols=[1, 2, 3, 4])
datalist5 = data5.values.tolist()
data_array5 = np.array(datalist5)

data6 = pd.read_csv('traject13_log18C_Robust_Mellinger_cf8.csv', header=0, delimiter=',', skiprows=0, usecols=[1, 2, 3, 4])
datalist6 = data6.values.tolist()
data_array6 = np.array(datalist6)

# calculation of the mean and standard deviation
matrix_x=np.column_stack((data_array[:, 0], data_array2[:, 0], data_array3[:, 0], data_array4[:, 0], data_array5[:, 0], data_array6[:, 0]))
mean_x = np.mean(matrix_x, axis=1)
std_x = np.std(matrix_x, axis=1)

matrix_y=np.column_stack((data_array[:, 1], data_array2[:, 1], data_array3[:, 1], data_array4[:, 1], data_array5[:, 1], data_array6[:, 1]))
mean_y = np.mean(matrix_y, axis=1)
std_y = np.std(matrix_y, axis=1)

matrix_z=np.column_stack((data_array[:, 2], data_array2[:, 2], data_array3[:, 2], data_array4[:, 2], data_array5[:, 2], data_array6[:, 2]))
mean_z = np.mean(matrix_z, axis=1)
std_z = np.std(matrix_z, axis=1)

matrix_yaw=np.column_stack((data_array[:, 3], data_array2[:, 3], data_array3[:, 3], data_array4[:, 3], data_array5[:, 3], data_array6[:, 3]))
mean_yaw = np.mean(matrix_yaw, axis=1)
std_yaw = np.std(matrix_yaw, axis=1)


dataR = pd.read_csv('timed_waypoints_yaw13.csv', header=0, delimiter=',', skiprows=0)
datalistR = dataR.values.tolist()
data_arrayR = np.array(datalistR)

t = data_arrayR[:, 0]
xR = data_arrayR[:, 1]
yR = data_arrayR[:, 2]
zR = data_arrayR[:, 3]

Ref_yaw = data_arrayR[:, 4]/math.pi*180

# Function to convert yaw
def convert_degrees(degrees):
    degrees %= 360
    
    if degrees <= 180:
        return degrees
    else:
        return degrees - 360

yawR = np.vectorize(convert_degrees)(Ref_yaw)


if __name__ == "__main__":
  # Plotting the data
  gs = gridspec.GridSpec(6, 1)
  fig = plt.figure()

  ax = plt.subplot(gs[1, 0]) # row 0
  ax.plot(mean_x)
  ax.plot(xR)
  ax.fill_between(range(len(mean_x)), mean_x - std_x, mean_x + std_x, color='red', alpha=0.4, label='Standard Deviation')
  ax.set_ylabel("x [meter]")
  plt.title('20 seconds, 30 pieces, Mellinger controller trajectory')


  ax = plt.subplot(gs[2, 0]) # row 2
  ax.plot(mean_y)
  ax.plot(yR)
  ax.fill_between(range(len(mean_y)), mean_y - std_y, mean_y + std_y, color='red', alpha=0.4, label='Standard Deviation')
  ax.set_ylabel("y [meter]")

  ax = plt.subplot(gs[3, 0]) # row 3
  ax.plot(mean_z)
  ax.plot(zR)
  ax.fill_between(range(len(mean_z)), mean_z - std_z, mean_z + std_z, color='red', alpha=0.4, label='Standard Deviation')
  ax.set_ylabel("z [meter]")

  ax = plt.subplot(gs[4, 0]) # row 4
  ax.plot(mean_yaw, label='mean')
  ax.plot(yawR, label='reference')
  ax.fill_between(range(len(mean_yaw)), mean_yaw - std_yaw, mean_yaw + std_yaw, color='red', alpha=0.4, label='Standard Deviation')
  ax.set_ylabel("yaw [degree]")
  ax.set_xlabel("time [ms]")
  ax.set_ylim(-200, 200)
  ax.set_yticks([-180, 0, 180])
  ax.legend(loc='lower right')

  plt.show()

  #MAE yaw
  MAE_yaw = np.mean(np.abs(data_array[:, 3]-yawR))
  MAE_yaw2 = np.mean(np.abs(data_array2[:, 3]-yawR))
  MAE_yaw3 = np.mean(np.abs(data_array3[:, 3]-yawR))
  MAE_yaw4 = np.mean(np.abs(data_array4[:, 3]-yawR))
  MAE_yaw5 = np.mean(np.abs(data_array5[:, 3]-yawR))
  MAE_yaw6 = np.mean(np.abs(data_array6[:, 3]-yawR))
  print(MAE_yaw)
  print(MAE_yaw2)
  print(MAE_yaw3)
  print(MAE_yaw4)
  print(MAE_yaw5)
  print(MAE_yaw6)

  average_MAE = (MAE_yaw+MAE_yaw2+MAE_yaw3+MAE_yaw4+MAE_yaw5+MAE_yaw6)/6
  print(average_MAE)