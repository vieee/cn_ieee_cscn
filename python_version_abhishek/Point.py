#Import type and condition checking barriers.
from check import *

'''
Defines a point in a plane.
'''
class Point():
	#x:X-coordinate
	#y:Y-coordinate
	def __init__(self,x,y):
		type_check(x,(int,float),'X-coordinate must be an integer or a float')
		type_check(y,(int,float),'Y-coordinate must be an integer or a float')
		self._x=x
		self._y=y
	
	#Return the coordinates as a tuple.
	#Used by shapely maybe??
	def coordinates(self):
		return (self._x,self._y)
	
	#Display the object details in human readable form.
	def __repr__(self):
		return f'Point:(x={self._x},y={self._y})'

	#Deep copy a point and return it.
	#Use this , or use the 'deepcopy' function from the 'copy' module.
	def copy(self):
		return Point(self._x,self._y)

	#Return the square of the distance of a point from the object.
	def distance_squared(self,point):
		type_check(point,(Point,),'Argument must be a point')
		return (self._x-point._x)**2+(self._y-point._y)**2

	#Definition of equality between two points.
	#P1==P2 is defined as:
	def __eq__(self,point):
		type_check(point,(Point,),'Argument must be a point')
		return (self._x==point._x and self._y==point._y)




#Tests.
#Run as 'Python3 Point.py'
if __name__=='__main__':
#	x,y=map(int,input('Enter X and Y coordinates: ').split(' '))
#	p=Point(x,y)
	p=Point(1,1.901)
	print(p)

	print(p.coordinates())

	p1=Point(10,10)
	p2=Point(20,20)
	print(p1.distance_squared(p2))

	p1=Point(1,2)
	p2=Point(1,2)
	print(p1 is p2)
	print(p1==p2)
