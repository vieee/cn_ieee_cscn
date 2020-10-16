#Global variables to read
from Globals import sensor_sensing_radius as SENSOR_SENSING_RADIUS
#Import type and condition checking barriers.
from check import *
#Import the point class
from Point import Point

#I'm not calling range of the sensor by its name because python has a range function
class Sensor:
	#Radius is a static value as the radii of all sensors will be the same
	radius=SENSOR_SENSING_RADIUS
	#The id which will be assigned to a new sensor object.
	sid=0
	def __init__(self,center_coordinates,lifetime):
		#Perform error checking first.
		type_check(center_coordinates,(Point,),'Sensor coordinates must be an object of type \'Point\'.')
		type_check(lifetime,(int,float),'Lifetime must be a positive integer or float')
		value_check(lifetime>0,'Lifetime must greater than 0')
		self.center=center_coordinates.copy()
		#The lifetime will be different for each sensor.
		self.remaining_lifetime=lifetime
		#The id
		self.id=Sensor.sid
		Sensor.sid+=1

	#Can this sensor sense a point 'point'?
	def can_sense(self,point):
		return self.center.distance_squared(point)<=Sensor.radius**2

	#Object representation in human readable form.
	def __repr__(self):
#		return f'Sensor:[Center:[{self.center}],Radius:{Sensor.radius},Remaining Time:{self.remaining_lifetime}]'
		return f'{self.id}'


p=Point(1,2)
s=Sensor(p,10)
print(s)
