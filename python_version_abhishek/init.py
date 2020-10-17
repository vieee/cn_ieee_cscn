'''
Initialize the global variables.
If the global variables are already initialized , then ignore this file.
'''

#Import global variables to modify.
from Globals import *
#Import type and condition checking barriers.
from check import *


'''
Set the sensing radius of the sensors.
'''
def set_sensing_radius(r):
	type_check(r,(int,float),'Sensing radius must be a positive integer or a float')
	value_check(r>0,'Sensing radius must be greater than 0')
	global sensor_sensing_radius
	sensor_sensing_radius=r

'''
Set the maximum lifetime of each sensor.
'''
#TODO
#Remove this.
def set_sensor_max_lifetime(l):
	type_check(l,(int,float),'Lifetime must be a positive integer or a float')
	value_check(l>0,'Lifetime must be greater than 0')
	global sensor_maximum_lifetime
	sensor_maximum_lifetime=l

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

'''
Set the coordinates of the sensors.
'''
def set_sensor_coordinates():
	print('init.set_sensor_coordinates():Use methods defined by Tanish or/and Jash.')
	pass

#Tests
#RUN 'Python3 init.py' to execute these.
if __name__=='__main__':
	#	
	#Start defining the global variables one by one.
	#
	set_sensing_radius(int(input('Enter sensing radius:')))
	set_sensor_max_lifetime(int(input('Enter sensor max lifetime:')))
	set_sensing_region_width(int(input('Enter sensing region width:')))
	set_sensing_region_height(int(input('Enter sensing region height:')))
	set_sensor_density(float(input('Enter sensor density:')))
	set_sensor_coordinates()
	print('Sensor Radius:',sensor_sensing_radius)
	print('Sensor Maximum Lifetime:',sensor_maximum_lifetime)
	print('Sensing Region Width:',sensing_region_width)
	print('Sensing Region Height:',sensing_region_height)
	print('Sensor Density:',sensor_density)
	print('Sensor Coordinates:',sensor_coordinates)

