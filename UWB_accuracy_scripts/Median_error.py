#Median

import numpy as np
import pandas as pd


i=1
iter=46

true_x=np.array([0.5,1,1.5,2,2.5]+[0,0.5,1,1.5,2,2.5]*6+[0.5,1,1.5,2,2.5])
true_y=np.array([0]*5+[0.5]*6+[1]*6+[1.5]*6+[2]*6+[2.5]*6+[3]*6+[3.5]*5)

# Create an empty DataFrame to store the averages
result_list = []

while i<=iter:
    # Call for the file names for each value of i
    file_name = f"logged_data_kalman4_{i}.csv"
    # Read CSV
    data = pd.read_csv(file_name, header=0, delimiter=',', skiprows=0, usecols=[2, 3, 4])
    datalist = data.values.tolist()
    # Convert figure8 to a NumPy array
    data_array = np.array(datalist)
    

    # Subtract the true x,y or z position, take the absolute value, and calculate the average
    average_x = np.abs(np.median(data_array[:, 0])-true_x[i-1])
    average_y = np.abs(np.median(data_array[:, 1])-true_y[i-1])
    average_z = np.abs(np.median(data_array[:, 2])-0.92)
    squared_x = np.square(average_x)
    squared_y = np.square(average_y)
    squared_z = np.square(average_z)
    squared_sum_xy = np.add(squared_x, squared_y)
    average_xy = np.sqrt(squared_sum_xy)
    squared_sum_xyz = np.add(squared_sum_xy, squared_z)
    average_xyz = np.sqrt(squared_sum_xyz)

    # Append the averages to the DataFrame
    result_list.append({'X': true_x[i-1], 'Y': true_y[i-1],'Median_error_x': average_x, 'Median_error_y': average_y, 'Median-error_z': average_z, 'Median_error_xy': average_xy, 'Median_error_xyz': average_xyz})

    print(f"Average of x: {average_x}")
    print(f"Average of y: {average_y}")
    print(f"Average of z: {average_z}")

    i+=1

result_df = pd.DataFrame(result_list)

# Write the DataFrame to a new CSV file
result_df.to_csv('Median4_z.csv', index=False)




