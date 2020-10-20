'''
Chirags Method:
Code for finding out the area:
'''
import math


#Algorithm to find the number of cells/points a Sensor with centre x,y can cover in the grid_cell
def ret_points(centre, grid_cell, R):
	x,y = centre
	points = []
	temp = 1
	
	max_index = len(grid_cell) - 1
	
	deg = 180
	for i in range(y,y-R-1,-1*temp): 
		if i<0 or i>max_index:
			continue

		x_min = round(x + R * math.cos(deg*math.pi/180))
		for j in range(x,x_min,-1*temp): 
			if j<0 or j>max_index:
				continue

			if grid_cell[j][i] == 1:
				points.append([j,i])
			else:
				break
		deg-=90.0/R

	deg = 0
	for i in range(y,y-R-1,-1*temp):
		if i<0 or i>max_index:
			continue

		x_min = round(x + R * math.cos(deg*math.pi/180))
		for j in range(x,x_min,1*temp):
			if j<0 or j>max_index:
				continue

			if grid_cell[j][i] == 1:
				points.append([j,i])
			else:
				break
		deg+=90.0/R
	

	deg = 180
	for i in range(y,y+R+1,1*temp):
		if i<0 or i>max_index:
			continue

		x_min = round(x + R * math.cos(deg*math.pi/180))
		for j in range(x,x_min,-1*temp):
			if j<0 or j>max_index:
				continue

			if grid_cell[j][i] == 1:
				points.append([j,i])
			else:
				break
		deg+=90.0/R

	deg = 360
	for i in range(y,y+R+1,1*temp):
		if i<0 or i>max_index:
			continue

		x_min = round(x + R * math.cos(deg*math.pi/180))
		for j in range(x,x_min,1*temp):
			if j<0 or j>max_index:
				continue

			if grid_cell[j][i] == 1:
				points.append([j,i])
			else:
				break
		deg-=90.0/R
	return points   

