'''
Initialize the global variables.
If the global variables are already initialized , then ignore this file.
'''

#Import global variables to modify.
from Globals import *
#Import type and condition checking barriers.
from check import *
#Import sub-file.
import init_sensors


'''
Set the sensing radius of the sensors.
'''
def set_sensing_radius(r):
	type_check(r,(int,float),'Sensing radius must be a positive integer or a float')
	value_check(r>0,'Sensing radius must be greater than 0')
	global sensor_sensing_radius
	sensor_sensing_radius=r

'''
Set the width of the sensing region.
'''
def set_sensing_region_width(width):
	type_check(width,(int,float),'Region width must be a positive integer or a float')
	value_check(width>0,'Region width must be greater than 0')
	global sensing_region_width
	sensing_region_width=width

'''
Set the height of the sensing region.
'''
def set_sensing_region_height(height):
	type_check(height,(int,float),'Region height must be a positive integer or a float')
	value_check(height>0,'Region height must be greater than 0')
	global sensing_region_height
	sensing_region_height=height

'''
Set the density of the sensors.
'''
def set_sensor_density(density):
	type_check(density,(int,float),'Density must be a positive integer or a float')
	value_check(density>0,'Density must be greater than 0')
	global sensor_density
	sensor_density=density


def set_sensor_coordinates():
	sensors=init_sensors.set_sensor_coordinates(sensing_region_width,sensing_region_height,sensor_density)
	return sensors
