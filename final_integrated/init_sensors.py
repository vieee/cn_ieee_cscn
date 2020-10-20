'''
Set the coordinates of the sensors.
'''

#Import random.
import random
#Import the sensor.
from Sensor import Sensor
#Import all global variables.
import Globals

def set_sensor_coordinates():

	#Aliasing the global variables
	region_height=Globals.sensing_region_height
	region_width=Globals.sensing_region_width
	sensor_density=Globals.sensor_density

	Globals.sensors=[]

	sensor_side = (1/(sensor_density))**(1/2) 
	#Round it to an integer.
	int_side=int(sensor_side)

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
			l=random.randint(80,100)
			#The new sensor.
			sensor=Sensor(x,y,l)

			Globals.sensors.append(sensor)

