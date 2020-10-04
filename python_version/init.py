import math, random
#I'm not calling range of the sensor by its name because python has a range function
class Sensor:
	radius = 0 #Radius is a static value as the radii of all sensors will be the same
	total_lifetime = 0
	def __init__(self, coordinates):
		self.coordinates = coordinates
		self.remaining_lifetime = Sensor.total_lifetime

class GridCell:
	density = 0	#Whether we take it to be consistent for each and every single area, keeping density static is better
	n = 0
	#Can accept coordinates or even width and height)
	def __init__(self, attr1, attr2):
		#If coordinates
		if type(attr1) == type(attr2) and (type(attr1) is list or type(attr1) is tuple):
			self.bottom_left = tuple(attr1)
			self.top_right = tuple(attr2)
			self.width = attr2[0] - attr1[0]
			self.height = attr2[1] - attr1[0]
		elif type(attr1) == type(attr2):
			#If dimensions
			self.width = attr1
			self.height = attr2
			self.bottom_left = (0, 0)
			self.top_right = (self.width, self.height)
		else:
			self.width, self.height = 0, 0
			self.bottom_left, self.top_right = (0, 0), (0, 0)
	
	def getVertices(self):
		return [self.bottom_left, (self.top_right[0], self.bottom_left[1]), self.top_right, (self.bottom_left[0], self.top_right[1])]

	def getCurveSet(self):
		#For the random shape
		#If it is a horizontal vertex, it will be as (value, True), if vertical (value, False)
		return [(self.bottom_left[1], True), (self.top_right[0], False), (self.top_right[1], True), (self.bottom_left[0], False)]

#Range is basically range but it will be for real numbers, its basically just a while loop, but okay
#Just like range, its default value
def Range(start, end, change = 1, less_than_equal_to = True):
	answer = []
	if start == end:
		return [start]
	elif change == 0 or (start < end and change < 0) or (start > end and change > 0):
		print("Error: Infinite loop")
		return [] #This is infinite, might as well do nothing
	else:
		temp = start
		if less_than_equal_to:
			while temp <= end:
				answer.append(temp)
				temp += change
		else:
			while temp < end:
				answer.append(temp)
				temp += change
		return answer

def init():
	width, height = map(int, input("Enter the width and height of the area: ").strip().split())
	rect = GridCell(width, height)
	while GridCell.density <= 0:
		GridCell.density = float(input("Enter the density of sensors in this area: "))

	while Sensor.radius <= 0:
		Sensor.radius = float(input("Enter the range of the sensors: "))

	while Sensor.total_lifetime <= 0:
		Sensor.total_lifetime = float(input("Enter the total lifetime of each sensor: "))
	
	GridCell.n = math.floor(GridCell.density * rect.width * rect.height)

	no_of_temp_squares = math.floor(rect.width * rect.height * 2 / Sensor.radius**2)

	sensors = []

	if GridCell.n < no_of_temp_squares:
		print("Do Jash's method")	#Do Jash's method
	else:
		temp_square_side = Sensor.radius / math.sqrt(2)
		'''
		y = rect.bottom_left[1]
		while y <= rect.top_right[1]:
			x = rect.bottom_left[0]
			while x <= rect.top_right[0]:
				sensor = Sensor((x, y))
				sensors.append(sensor)
				x += temp_square_side
			y += temp_square_side
		'''
		for y in Range(rect.bottom_left[1], rect.top_right[1], temp_square_side):
			for x in Range(rect.bottom_left[0], rect.top_right[0], temp_square_side):
				sensor = Sensor((x, y))
				sensors.append(sensor)
		if GridCell.n > len(sensors):
			current_left = GridCell.n - len(sensors)
			low_x = rect.bottom_left[0] - Sensor.radius
			loy_y = rect.bottom_left[1] - Sensor.radius
			for i in range(current_left):
				#This covers the area in which the sensor can affect the main area
				#Therefore it randomly places the sensor within a rectangle of width + 2r and height + 2r
				sensor = Sensor((low_x + (rect.width + 2 * Sensor.radius) * random.random(), low_y + (rect.height + 2 * Sensor.radius) * random.random()))
				sensors.append(sensor)
	return rect, sensors

#rect, sensors = init()
#Range(0.5, 5.5) to get 0.5, 1.5, ... , 4.5, 5.5
#Range(0.5, 5.5, less_than_equal_to = False) to get 0.5, 1.5, ...., 4.5
#Range(0.5, 5.5, 0.5) to get 0.5, 1.0, ..., 5.5
#Range(0.5, 5.5, 0.5, less_than_equal_to = False) to get 0.5, 1.5, ...., 4.5, 5.0

#rect, sensors = init()
