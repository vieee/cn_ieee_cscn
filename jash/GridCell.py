#Global variables to read.
from Globals import sensor_density as SENSOR_DENSITY
#Import type and condition checking barriers.
from check import *
#Import the point class
from Point import Point



class GridCell():
	#Whether we take it to be consistent for each and every single area, keeping density static is better
	density=SENSOR_DENSITY
	#Parameter 2:Bottom left point.
	#Parameter 3:Width of gridcell.
	#Parameter 4:Height of gridcell.
	def __init__(self,bottom_left,width,height):
		type_check(bottom_left,(Point,),'Bottom left point must be of type\'Point\'')
		type_check(width,(int,float),'Width must be a positive integer or float')
		type_check(height,(int,float),'Height must be a positive integer or float')
		value_check(width>0,'Width must be greater than 0')
		value_check(height>0,'Height must be greater than 0')
		#Bottom left point.
		self.bottom_left=bottom_left.copy()
		#Width
		self.width=width
		#Height
		self.height=height
	
	#Return the set of vertices corresponding to this grid cell.
	#Equivalent to initializing Q in the column generation approach.
	def get_vertex_set(self):
		#Bottom left
		bl=self.bottom_left.copy()
		#Bottom right
		br=Point(self.bottom_left._x+width,self.bottom_left._y)
		#Top left
		tl=Point(self.bottom_left._x,self.bottom_left._y+height)
		#Top right
		tr=Point(self.bottom_left._x+width,self.bottom_left._y+height)
		#Return the set.
		return set((bl,br,tl,tr))


#Left as it is.


	#Get the vertices of the grid cell.
	def getVertices(self):
		return [self.bottom_left, (self.top_right[0], self.bottom_left[1]), self.top_right, (self.bottom_left[0], self.top_right[1])]

	def getCurveSet(self):
		#For the random shape
		#If it is a horizontal vertex, it will be as (value, True), if vertical (value, False)
		return [(self.bottom_left[1], True), (self.top_right[0], False), (self.top_right[1], True), (self.bottom_left[0], False)]






#TODO
#Write tests and comment.
