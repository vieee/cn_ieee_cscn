from Point import Point
from Sensor import Sensor
from CoverSet import CoverSet
from random import randint
from pprint import pprint

#List of lists of coversets.
coverset_lists=[]
#This demo is only concerned with time and so set arbitary coordinates.
x,y=0,0

def generate_coversets(num_cover_sets,num_sensors_in_each):
	ls=[]
	#Generate each coverset.
	for i in range(num_cover_sets):
		cs=CoverSet()
		#Generate sensors for each coverset.
		for j in range(num_sensors_in_each):
			s=Sensor(Point(x,y),randint(1,10))
			#Add the sensor.
			cs.addSensor(s)
		#Add the coverset.
		ls.append(cs)
	return ls

coverset_lists.append(generate_coversets(2,5))
coverset_lists.append(generate_coversets(3,5))
coverset_lists.append(generate_coversets(4,5))

#pprint(coverset_lists)

def tryMerge(coverset_lists):
	#Store the results.
	resultant_coversets=[]

	while True:
		#Calculate minimum.
		min_time=float('inf')
		for coverset_list in coverset_lists:
			#Exit when a particular gridcell has all its cover sets exhausted.
			try:
				min_time=min(min_time,coverset_list[0].lifetime)
			except IndexError:
				return resultant_coversets
		#A new coverset will contain all the first coversets.
		xi=CoverSet()
		for coverset_list in coverset_lists:
			xi.addSensorsFromCoverSet(coverset_list[0])

		#Reduce the first coversets
		for coverset_list in coverset_lists:
			success=coverset_list[0].reduceLifetime(min_time)
			#Remove if we consume the coverset completely.
			if not success:
				coverset_list.pop(0)
			#If not, some part of the coverset is still left over. So do nothing.
			#Set the time of the Xith coverset.
		xi.lifetime=min_time
		#Add to results.
		resultant_coversets.append(xi)
	#Return results.
	return resultant_coversets


res=tryMerge(coverset_lists)

pprint(res)


