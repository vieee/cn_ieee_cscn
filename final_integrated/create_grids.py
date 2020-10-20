'''
Classify sensors into each gridcell for further analysis.
'''
from Sensor import Sensor

import Globals

#Jash
def create_grids(K):

	#Aliasing globals
	height=Globals.sensing_region_height
	width=Globals.sensing_region_width
	R=Globals.sensor_sensing_radius

	cell_x=cell_y=2*K*R
	#The storage structure for the sensors.
	grid_sensors=[[[] for j in range(height//cell_y)] for i in range(width//cell_x)]
	for i in range(width//cell_x):
		for j in range(height//cell_y):
			start_x = i * cell_x
			start_y = j * cell_y
			end_x = start_x + cell_x
			end_y = start_y + cell_y
			poi = []
#TODO
#Optimize this.
			for sensor in Globals.sensors:
				x,y=sensor.center()
				if start_x<=x<=end_x and start_y<=y<=end_y:
					poi.append(sensor)
			grid_sensors[i][j]=poi
	return grid_sensors


