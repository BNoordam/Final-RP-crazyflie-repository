# Standard deviation for 46 measurements at a single grid location

import numpy as np
import pandas as pd

# numbert of measurements
i=1
iter=46

all_data = []  # Initialize an empty list to store data from each iteration

while i <= iter:
    # Call for the file names for each value of i
    csv_filename = f'logged_data_kalman_46x0-1.5_{i}.csv'
    
    # Read data from the CSV file
    data = pd.read_csv(csv_filename, header=0, delimiter=',', skiprows=0, usecols=[2, 3, 4])
    
    # Convert the data to a NumPy array and append it to the list
    all_data.append(data.values)

    i += 1

# Concatenate all the arrays in the list into a single NumPy array
data_array = np.concatenate(all_data, axis=0)
print('standard deviation')
std_dev_x = np.std(data_array[:, 0])
print(std_dev_x)
std_dev_y = np.std(data_array[:, 1])
print(std_dev_y)
std_dev_z = np.std(data_array[:, 2])
print(std_dev_z)
print('average error')
average_x = np.mean(np.abs(data_array[:, 0]-1.5))
print(average_x)
average_y = np.mean(np.abs(data_array[:, 1]))
print(average_y)
average_z = np.mean(np.abs(data_array[:, 2]))
print(average_z)
print('median error')
mean_x = np.abs(np.median(data_array[:, 0]-1.5))
print(mean_x)
mean_y = np.abs(np.median(data_array[:, 1]))
print(mean_y)
mean_z = np.abs(np.median(data_array[:, 2]))
print(mean_z)
np.savetxt('combined_data[0-1.5].csv', data_array, delimiter=',')
