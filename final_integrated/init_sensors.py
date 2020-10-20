#Import random.
import random
#Import the sensor.
from Sensor import Sensor

'''
Set the coordinates of the sensors.
'''
def set_sensor_coordinates(sensor_coords,region_width,region_height,sensor_density):

	#sensor_coords = []
	sensor_side = (1/(sensor_density))**(1/2) 
	#Round it to an integer.
	int_side=int(sensor_side)


	print(region_width,int_side,region_width//int_side)

	for i in range(int(region_width//int_side)):
		for j in range(int(region_height//int_side)):

			# we do the following to reduce the probability of sensors to be at the corners of the cell
			if(random.random()>0.2):
				temp=[random.randint(1,int_side-1) for _ in range(2)]
			else:
				temp=[random.randint(0,int_side) for _ in range(2)]

			#Sensor X-coordinate.
			x=int((temp[0]+(sensor_side*i))%region_width)
			#Sensor Y-coordinate.
			y=int((temp[1]+(sensor_side*j))%region_height)
			#Set sensor lifetime as 100 now(must be randomized later)
			l=100
			#The new sensor.
			sensor=Sensor(x,y,l)
#			sensor_coords.append(Sensor('S'+str(i)+str(j),[],sensor))
			sensor_coords.append(sensor)
	return sensor_coords

