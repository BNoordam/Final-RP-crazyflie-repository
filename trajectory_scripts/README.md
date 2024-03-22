# Trajectory following scripts  (LInk with report)

The script Spiral_trajectory_log_cam.py lets a Crazyflie fly a predetermined trajectory generated in uav_trajectories, logs the Kalman position estimates, and saves an image stream sent by the AI deck over WIFI, by calling the opencv-viewer.py script.
The trajectory to fly can be changed by uploading a different 8th-order polynomial generated in uav_trajectories instead of "yaw20_cf1.csv" in line 66. The trajectory following code was based on: https://github.com/bitcraze/crazyflie-lib-python/blob/master/examples/autonomy/autonomous_sequence_high_level.py
The name of the csv file where the position data is saved can be changed in line 199. 
Before it is possible to stream and save images the instructions in https://github.com/BNoordam/aideck-gap8-examples should be followed for implementing the bitcraze wifi video streaming example on the AI deck, and the instructions in https://github.com/BNoordam/WIFI_dongle for installing the WIFI dongle.

The script swarm_2cf.py is for flying trajectories simultaneously with multiple Crazyflies. Currently, the script is for two Crazyflies, but by adding more URIs (Crazyflie radio addresses) (line 203) and trajectories to follow (line 100) in the code, this number can be increased. Each Crazyflie in the swarm should have a unique radio address, which can be altered in the cfclient.

plot_traject.py plots 3d trajectories from the logged position data in Spiral_trajectory_log_cam.py or the timed waypoints generated in uav_trajectories. These timed waypoints are used as a reference for the trajectory following accuracy. XYZ_plot_Mellinger_Max.py plots and compares multiple position logs' mean, minimum and maximum values to the reference timed waypoints for x, y, z, and yaw. XYZ_plot_Mellinger_STD.py does the same for the mean and standard deviation. These results and plots are found in section 5.3 of the final report

MAE_traject_Fit.py determines the MAE for x, y, z, and yaw by comparing the position log to the timed waypoints. It is important to keep in mind that the timed waypoints trajectory is the same as the used trajectory of the position log in these scripts.

## Flowchart of the data/activity flow of the scripts in this folder

![flowchartGit drawio](https://github.com/BNoordam/Final-RP-crazyflie-repository/assets/146953161/331b81de-9727-419d-a538-6e3af9275bbb)

## Flowchart explanation
All of the .py files in the flowchart are found in this directory. The logged position data, yaw{i} files, and the timed_waypoints_yaw{i} files can all be found in the Google drive in data/crazyflie trajectories.
