import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('MAE4_z.csv', header=0, delimiter=',', skiprows=0, usecols=[0, 1, 2])
datalist = data.values.tolist()
# Convert figure8 to a NumPy array
data_array = np.array(datalist)

# Your data
true_x = data_array[:, 0]
true_y = data_array[:, 1]
average_xy = data_array[:, 2]
#average_xy[4] = 0.27

true_x = np.insert(true_x, 0, 0)
true_y = np.insert(true_y, 0, 0)
average_xy = np.insert(average_xy, 0, max(average_xy))

true_x = np.insert(true_x, 42, 0)
true_y = np.insert(true_y, 42, 3.5)
average_xy = np.insert(average_xy, 42, max(average_xy))
#average_xy[42] = 0.29

# Create a meshgrid
X, Y = np.meshgrid(np.unique(true_x), np.unique(true_y))

# Reshape average_xy to match the shape of X and Y
Z = np.array(average_xy).reshape(X.shape)

# Create a heatmap
plt.imshow(Z, cmap='magma', origin='lower', extent=[min(true_x)-0.25, max(true_x)+0.25, min(true_y)-0.25, max(true_y)+0.25])

# Add labels and a colorbar
plt.xlabel('x [meter]')
plt.ylabel('y [meter]')
plt.title('Positional MAE in the x-direction')
#plt.title('2D Positional MAE')
plt.colorbar(label='MAE [meter]')

# Show the plot
plt.show()
#plt.savefig('Heatmap1_XY_png.png')
#plt.savefig("Heatmap1_XY(-outlier).svg")