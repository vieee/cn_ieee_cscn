#Global variables to read
from Globals import sensor_sensing_radius as SENSOR_SENSING_RADIUS
#Import type and condition checking barriers.
from check import *

class Sensor:
	#Radius is a static value as the radii of all sensors will be the same
	radius=SENSOR_SENSING_RADIUS
	#The id which will be assigned to a new sensor object.
	sid=0
	def __init__(self,x,y,lifetime):
		#Perform error checking first.
		type_check(x,(int,float),'X-coordinate must be an integer or float')
		type_check(y,(int,float),'Y-coordinate must be an integer or float')
		type_check(lifetime,(int,float),'Sensor lifetime must be a positive integer or float')
		value_check(lifetime>0,'Lifetime must greater than 0')

		#Set the center coordinates.
		self._x=x
		self._y=y

		#The lifetime will be different for each sensor.
		self.max_lifetime=lifetime

		#The id
		self.id=Sensor.sid
		Sensor.sid+=1

	#Can this sensor sense a point 'point'?
	def can_sense(self,x,y):
		type_check(x,(int,float),'X-coordinate must be an integer or float')
		type_check(y,(int,float),'Y-coordinate must be an integer or float')
		return (self._x-x)**2+(self._y-y)**2<=Sensor.radius**2

	#Object representation in human readable form.
	def dump_vars(self):
		#print(f'Sensor:[Center:(self._x,self._y),Radius:{Sensor.radius},Remaining Time:{self.max_lifetime}]')
		print('Sensor:[Center:(self._x,self._y),Radius:', Sensor.radius, ', Remaining Time:', self.max_lifetime, ']')

	def __repr__(self):
		#return f'({self.id})'
		return '(%s)'%(self.id)

	#Return the center as a tuple of the form (x,y)
	def center(self):
		return (self._x,self._y)

	#Return the maximum lifetime of the sensor.
	def lifetime(self):
		return self.max_lifetime

