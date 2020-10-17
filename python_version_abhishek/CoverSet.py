#Import type and condition checking barriers.
from check import *
#Import the point class
from Sensor import Sensor

#
#Defines a cover set.
#
class CoverSet():
	#
	#Consrtuctor initializes values.
	#
	def __init__(self):
		self.sensor_set=set()
		self.lifetime=float('inf')

	#
	#Reduce the lifetime of the coverset to the new lifetime.
	#Returns True if the lifetime is non-zero after reducing, False otherwise.
	#If the return value is false, then the final reduction in lifetime did not occur.
	#
	def reduceLifetime(self,lifetime):
		type_check(lifetime,(int,float),'Lifetime must be a +ve integer/float')
		value_check(lifetime>0,'Lifetime must be +ve ')
		if self.lifetime>lifetime:
			self.lifetime-=lifetime
			return True
		return False
	
	#
	#Add a sensor to the coverset.
	#
	def addSensor(self,sensor):
		type_check(sensor,(Sensor,),'sensor must be a Sensor')
		l1=len(self.sensor_set)
		self.sensor_set.add(sensor)
		l2=len(self.sensor_set)
		#We were able to add
		if l1==l2-1:
			self.lifetime=min(self.lifetime,sensor.remaining_lifetime)
			return True
		#Return False on failure to add sensor.
		return False

	#
	#Add all sensors from coverset c to the current coverset.
	#
	def addSensorsFromCoverSet(self,cover_set):
		type_check(cover_set,(CoverSet,),'cover_set must be a CoverSet')
		#Repeat for every sensor in cover_set.
		for sensor in cover_set.sensor_set:
			self.sensor_set.add(sensor)
		self.lifetime=min(self.lifetime,cover_set.lifetime)

	#
	#Human readable representation.
	#
	def __repr__(self):
		print('{(Lifetime:',self.lifetime,')')
		for sensor in self.sensor_set:
			print(sensor,end=' ')
		print('}')
		return ''



