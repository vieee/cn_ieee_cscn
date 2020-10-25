'''
MAIN ENTRY POINT OF THE PROGRAM IS HERE.
'''

import Globals

import init_sensors

import create_grids

import find_coversets

import merge

if __name__=='__main__':

	#All global variables have been set.

	#Set all sensors here.
	init_sensors.set_sensor_coordinates()

	#Set the value of K.
	K=int(input('Enter K:'))

	grid_cells=create_grids.create_grids(K)

	coversets_of_cells=find_coversets.find_coversets(grid_cells)

	final_result=merge.merge_coversets(coversets_of_cells)

	max_time=0
	for k,cs in enumerate(final_result):
		print(f'Time of coverset {k}',cs.lifetime)
		max_time+=cs.lifetime
	print('Maximum lifetime of the network',max_time)


