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
	#Jashs/Tanishs algo.
	init_sensors.set_sensor_coordinates()

	#Set the value of K.
	K=int(input('Enter K:'))

	
	grid_cells=create_grids.create_grids(K)

	coversets_of_cells=find_coversets.find_coversets(grid_cells)

	'''
	print(len(coversets_of_cells))
	print('................')
	print(coversets_of_cells[0][-1],coversets_of_cells[0][0])
	print('................')
	print(coversets_of_cells[1][-1],coversets_of_cells[1][0])
	print('................')
	print(coversets_of_cells[2][-1],coversets_of_cells[2][0])
	print('................')
	print(coversets_of_cells[3][-1],coversets_of_cells[3][0])
	print('................')
#	'''

	final_result=merge.merge_coversets(coversets_of_cells)

	print(final_result)


