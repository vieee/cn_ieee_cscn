#Global variables to read
import Globals
#Import type and condition checking barriers.
from check import *
#Import the point class
from Point import Point

#I'm not calling range of the sensor by its name because python has a range function
class Sensor:
	#Radius is a static value as the radii of all sensors will be the same
	radius=Globals.sensor_sensing_radius
	def __init__(self,center_coordinates,lifetime):
		#Perform error checking first.
		type_check(coordinates,(Point,),'Sensor coordinates must be an object of type \'Point\'.')
		type_check(lifetime,(int,float),'Lifetime must be a positive integer or float')
		value_check(lifetime>0,'Lifetime must greater than 0')
		self.coordinates=coordinates
		#The lifetime will be different for each sensor.
		self.remaining_lifetime=lifetime

