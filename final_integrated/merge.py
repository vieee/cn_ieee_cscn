from Sensor import Sensor
from CoverSet import CoverSet
from random import randint

def merge_coversets(coverset_lists):
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



