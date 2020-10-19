'''
MAIN ENTRY POINT OF THE PROGRAM IS HERE.
'''

from Globals import *
#Remove this if globals are set directly.
from init import *


if __name__=='__main__':

	#Remove this if globals are set directly.
	'''
	set_sensing_radius(float(input('Enter sensing radius:')))
	set_sensing_region_width(float(input('Enter sensing region width:')))
	set_sensing_region_height(float(input('Enter sensing region height:')))
	set_sensor_density(float(input('Enter sensor density:')))
#	'''
	#End of block to be removed.

	#Set all sensors here.
	#Jashs/Tanishs algo.
	set_sensor_coordinates()

	#Set the value of K.
	K=int(input('Enter K:'))

	print('here',sensor_coordinates)



