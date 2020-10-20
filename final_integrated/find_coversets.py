'''
Functions to find the coversets of a grid cell according to column generation approach.
Chirags Code
'''
#Numpy for calculations.
import numpy as np
#Global variables.
import Globals
#Sensor class.
from Sensor import Sensor
#Coverset class.
from CoverSet import CoverSet
#Function for calculating area.
import find_area

# This is the factor by which the Gridcell needs to be expanded or divided.
# This will be used to expand all the parameters later on for example the Sensing Radius
MULT_FACTOR=2
COVER_PERC=0.07

def find_coversets(grid_sensors):
	#Scaling the radius.
	scaled_radius=Globals.sensor_sensing_radius*MULT_FACTOR

	#List containing all sets of coversets.
	#More friendly with my merge function.
	coverset_sets=[]

	#Dictionary of coversets.
#	coverset_dict={}
	#Number of cells in any direction.
	le=len(grid_sensors)
	#Dimension of a single grid cell.(assume square)
	dimen_of_gridcell=Globals.sensing_region_width//le
	#Maximum area.
	max_val=0
	#Sensor with maximum area.
	max_sensor=None
	#Cells covered by the maximum sensor.
	max_sensor_cells=None
	#Begin:
	for i in range(le):

		for j in range(le):

			print('Generating coversets for cell',i,j,'.......')

			grid_cell=np.ones((dimen_of_gridcell*MULT_FACTOR,dimen_of_gridcell*MULT_FACTOR)) # 200 x 200
			all_cover_sets_for_one_cell = []
			cover_set=CoverSet()

			while len(grid_sensors[i][j])>0:
				max_val = 0

				for sensor in grid_sensors[i][j]: 

					x,y=sensor.center()
					x = (x-i*dimen_of_gridcell)*MULT_FACTOR
					y = (y-j*dimen_of_gridcell)*MULT_FACTOR
					x = x if x<len(grid_cell) else len(grid_cell)-1
					y = y if y<len(grid_cell) else len(grid_cell)-1

					cells = find_area.ret_points((x,y),grid_cell,scaled_radius)

					if len(cells) > max_val:
						max_val = len(cells)
						max_sensor = sensor
						#Store cells covered by the largest sensor to zero them out later on.
						max_sensor_cells=cells

				#Zero them out here.
				for x,y in max_sensor_cells:
					grid_cell[x][y] = 0

				if max_val <= 0 or np.count_nonzero(grid_cell == 1) < int(COVER_PERC*(len(grid_cell)**2)):
					if np.count_nonzero(grid_cell == 1) < int(COVER_PERC*(len(grid_cell)**2)):
						print('Added....')
						all_cover_sets_for_one_cell.append(cover_set)

					cover_sets=CoverSet()
					grid_cell = np.ones((dimen_of_gridcell*MULT_FACTOR,dimen_of_gridcell*MULT_FACTOR))

					continue

				cover_set.addSensor(max_sensor)

				grid_sensors[i][j].remove(max_sensor)
#			coverset_dict[(i,j)] = all_cover_sets_for_one_cell
			coverset_sets.append(all_cover_sets_for_one_cell)

	return coverset_sets



