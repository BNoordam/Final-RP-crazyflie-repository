import numpy as np
import pandas as pd

# number of measurements
i=1
iter=46

# grid reference points
true_x=np.array([0.5,1,1.5,2,2.5]+[0,0.5,1,1.5,2,2.5]*6+[0.5,1,1.5,2,2.5])
true_y=np.array([0]*5+[0.5]*6+[1]*6+[1.5]*6+[2]*6+[2.5]*6+[3]*6+[3.5]*5)

# Create an empty DataFrame to store the averages
result_list = []

while i<=iter:
    # Call for the file names for each value of i
    file_name = f"logged_data_kalman_{i}.csv"
    # Read CSV
    data = pd.read_csv(file_name, header=0, delimiter=',', skiprows=0, usecols=[2, 3, 4])
    datalist = data.values.tolist()
    # Convert to a NumPy array
    data_array = np.array(datalist)
    

    # Subtract the true x,y or z position, take the absolute value, and calculate the average
    average_x = np.mean(np.abs(data_array[:, 0]-true_x[i-1]))
    average_y = np.mean(np.abs(data_array[:, 1]-true_y[i-1]))
    average_z = np.mean(np.abs(data_array[:, 2]))
    squared_x = np.square(average_x)
    squared_y = np.square(average_y)
    squared_sum_xy = np.add(squared_x, squared_y)
    average_xy = np.sqrt(squared_sum_xy)
    x = true_x.reshape(-1, 1)
    y = true_y.reshape(-1, 1)

    # Append the averages to the DataFrame
    result_list.append({'True_x': true_x[i-1], 'True_y': true_y[i-1],'Average_x': average_x, 'Average_y': average_y, 'Average_z': average_z, 'Average_xy': average_xy})

    print(f"Average of x: {average_x}")
    print(f"Average of y: {average_y}")
    print(f"Average of z: {average_z}")

    i+=1

result_df = pd.DataFrame(result_list)

# Write the DataFrame to a new CSV file
result_df.to_csv('MAE.csv', index=False)


