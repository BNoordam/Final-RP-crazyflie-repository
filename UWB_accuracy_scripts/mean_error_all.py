import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('MAE.csv', header=0, delimiter=',', skiprows=0, usecols=[2, 3, 4, 5])
datalist = data.values.tolist()
# Convert figure8 to a NumPy array
data_array = np.array(datalist)
#data_array = data_array[data_array[:, 0] != 0]
# Your data
average_x = data_array[:, 0]
average_y = data_array[:, 1]
average_z = data_array[:, 2]
average_xy = data_array[:, 3]
#average_xy = np.delete(average_xy, 45)
print('MAE1')
mean_error_x = np.mean(average_x)
print(mean_error_x)
mean_error_y = np.mean(average_y)
print(mean_error_y)
mean_error_z = np.mean(average_z)
print(mean_error_z)
mean_error_xy = np.mean(average_xy)
print(mean_error_xy)

data2 = pd.read_csv('MAE2.csv', header=0, delimiter=',', skiprows=0, usecols=[2, 3, 4, 5])
datalist2= data2.values.tolist()
# Convert figure8 to a NumPy array
data_array2 = np.array(datalist2)
#data_array = data_array[data_array[:, 0] != 0]
# Your data
average_x2 = data_array2[:, 0]
average_y2 = data_array2[:, 1]
average_z2 = data_array2[:, 2]
average_xy2 = data_array2[:, 3]
#average_xy = np.delete(average_xy, 45)
print('MAE2')
mean_error_x2 = np.mean(average_x2)
print(mean_error_x2)
mean_error_y2 = np.mean(average_y2)
print(mean_error_y2)
mean_error_z2 = np.mean(average_z2)
print(mean_error_z2)
mean_error_xy2 = np.mean(average_xy2)
print(mean_error_xy2)

data3 = pd.read_csv('MAE3_z.csv', header=0, delimiter=',', skiprows=0, usecols=[2, 3, 4, 5, 6])
datalist3= data3.values.tolist()
# Convert figure8 to a NumPy array
data_array3 = np.array(datalist3)
#data_array = data_array[data_array[:, 0] != 0]
# Your data
average_x3 = data_array3[:, 0]
average_y3 = data_array3[:, 1]
average_z3 = data_array3[:, 2]
average_xy3 = data_array3[:, 3]
average_xyz3 = data_array3[:, 4]
#average_xy = np.delete(average_xy, 45)
print('MAE3_z')
mean_error_x3 = np.mean(average_x3)
print(mean_error_x3)
mean_error_y3 = np.mean(average_y3)
print(mean_error_y3)
mean_error_z3 = np.mean(average_z3)
print(mean_error_z3)
mean_error_xy3 = np.mean(average_xy3)
print(mean_error_xy3)
mean_error_xyz3 = np.mean(average_xyz3)
print(mean_error_xyz3)

data4 = pd.read_csv('MAE4_z.csv', header=0, delimiter=',', skiprows=0, usecols=[2, 3, 4, 5, 6])
datalist4= data4.values.tolist()
# Convert figure8 to a NumPy array
data_array4 = np.array(datalist4)
#data_array = data_array[data_array[:, 0] != 0]
# Your data
average_x4 = data_array4[:, 0]
average_y4 = data_array4[:, 1]
average_z4 = data_array4[:, 2]
average_xy4 = data_array4[:, 3]
average_xyz4 = data_array4[:, 4]
#average_xy = np.delete(average_xy, 45)

print('MAE4_z')
mean_error_x4 = np.mean(average_x4)
print(mean_error_x4)
mean_error_y4 = np.mean(average_y4)
print(mean_error_y4)
mean_error_z4 = np.mean(average_z4)
print(mean_error_z4)
mean_error_xy4 = np.mean(average_xy4)
print(mean_error_xy4)
mean_error_xyz4 = np.mean(average_xyz4)
print(mean_error_xyz4)

data5 = pd.read_csv('MAE_P.csv', header=0, delimiter=',', skiprows=0, usecols=[2, 3, 4, 5])
datalist5 = data5.values.tolist()
# Convert figure8 to a NumPy array
data_array5 = np.array(datalist5)
#data_array = data_array[data_array[:, 0] != 0]
# Your data
average_x5 = data_array5[:, 0]
average_y5 = data_array5[:, 1]
average_z5 = data_array5[:, 2]
average_xy5 = data_array5[:, 3]
#average_xy = np.delete(average_xy, 45)
print('MAE_P')
mean_error_x5 = np.mean(average_x5)
print(mean_error_x5)
mean_error_y5 = np.mean(average_y5)
print(mean_error_y5)
mean_error_z5 = np.mean(average_z5)
print(mean_error_z5)

mean_error_xy5 = np.mean(average_xy5)
print(mean_error_xy5)

data6 = pd.read_csv('MAE_P2_z.csv', header=0, delimiter=',', skiprows=0, usecols=[2, 3, 4, 5, 6])
datalist6= data6.values.tolist()
# Convert figure8 to a NumPy array
data_array6 = np.array(datalist6)
#data_array = data_array[data_array[:, 0] != 0]
# Your data
average_x6 = data_array6[:, 0]
average_y6 = data_array6[:, 1]
average_z6 = data_array6[:, 2]
average_xy6 = data_array6[:, 3]
average_xyz6 = data_array6[:, 4]
#average_xy = np.delete(average_xy, 45)

print('MAE_P2')
mean_error_x6 = np.mean(average_x6)
print(mean_error_x6)
mean_error_y6 = np.mean(average_y6)
print(mean_error_y6)
mean_error_z6 = np.mean(average_z6)
print(mean_error_z6)
mean_error_xy6 = np.mean(average_xy6)
print(mean_error_xy6)
mean_error_xyz6 = np.mean(average_xyz6)
print(mean_error_xyz6)