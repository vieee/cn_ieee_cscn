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
			s=Sensor(Point(x,y),randint(10,20))
			#Add the sensor.
			cs.addSensor(s)
		#Add the coverset.
		ls.append(cs)
	return ls

coverset_lists.append(generate_coversets(2,4))
coverset_lists.append(generate_coversets(3,3))
coverset_lists.append(generate_coversets(4,2))

def print_coverset_list(c):
	print('.......')
	for x in c:
		#print(f'\t{x}')
		print('\t%s'%(x))
	print('.......')

print('Coverset lists:\n')
for c in coverset_lists:
	print_coverset_list(c)
print('->>>>>>>>\n')
	

def tryMerge(coverset_lists):
	#Store the results.
	resultant_coversets=[]

	while True:

		#Calculate minimum.

		#Get all lifetimes of the first coversets.
		#An IndexError means that the coversets of a particular gridcell have been exhausted.
		#In that case, break out and return the result.
		try:
			lifetimes_of_first_coversets=[coverset_list[0].lifetime for coverset_list in coverset_lists]
		except IndexError:
			break
		#The minimum time.
		min_time=min(lifetimes_of_first_coversets)

		#The union of the coversets.

		#A new coverset will contain all the first coversets.
		Xi=CoverSet()
		for coverset_list in coverset_lists:
			#Take union of all coversets.
			Xi.addSensorsFromCoverSet(coverset_list[0])
			#Reduce the first coversets by the appropriate time.
			success=coverset_list[0].reduceLifetime(min_time)
			#Remove if we consume the coverset completely.
			if not success:
				coverset_list.pop(0)
			#If not, some part of the coverset is still left over. So do nothing.
			#Set the time of the Xith coverset.
		Xi.lifetime=min_time
		#Add to results.
		resultant_coversets.append(Xi)
	#Return results.
	return resultant_coversets


res=tryMerge(coverset_lists)

print('Resultant Coverset List:\n')
print_coverset_list(res)
print('->>>>>>>>\n')

