# Scripts for measuring the UWB accuracy with a 0.5m interval grid on the ground

This folder includes scripts for collecting and processing data for determining the accuracy of the UWB system with a grid.

Kalman_state_iterations.py is for collecting position data on the grid. For each grid position, the Crazyflie position is logged for 10s at 100Hz. After logging for a grid position is done, the message 'move' is displayed. Hereafter there are 13 seconds to move the Crazyflie to the next grid position. No humans should be inside the flight space when the position logging starts again, as this can decrease the UWB accuracy.
In line 16 the number of measurements can be altered if a different number of grid positions is used. Line 123 states the name of the resulting data files.

MEA.py and MAE_z.py calculate the MAE for each grid location and stores this data in a single file. MAE_z.py was used for measurement on a pole (height of 0.92m). The data files from Kalman_state_iterations.py are read in line 17. The MAE results are found in the final report, section 5.1, Tables 1 and 2. 

The resulting CSV files from MEA.py and MAE_z.py are used in Heatmap.py to create a heatmap of the accuracy of the grid. These heatmaps are also found in section 5.1. In mean_error_all.py these same files can also be used to determine the average MAE for an entire run.

Median_error.py calculates the absolute error from the median, similar to MAE.py. 

Stedev.py is for determining the standard deviation of the accuracy measurements at a single location on the grid. The script is currently built such that 46 measurements of 10s at 100Hz are performed. These results are in section 5.2 of the final report.


