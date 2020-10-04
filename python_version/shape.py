import init, math
import copy
class Curve:
	def __init__(self, X, isHorizontal = True):
		if type(X) is init.Sensor:
			self.isCircle = True
			self.x = X.coordinates[0]
			self.y = X.coordinates[1]
			self.radius = init.Sensor.radius
		else:
			self.isCircle = False
			self.isHorizontal = isHorizontal
			if not self.isHorizontal: #When x is constant, it is a vertical line
				self.x = X
				self.y = None
			else:
				self.y = X #When y is constant, it is a horizontal line
				self.x = None

	def getOtherCoordinate(self, val, isX = True):
		if self.isCircle:
			#Only needed if concerned curve is a circle
			#Basically determining whether you have the x or y coordinate as val to find the other
			#By default, it'll find y
			if isX:
				val_y_2 = self.radius**2 - (val - self.x)**2
				if val_y_2 < 0:
					return None
				val_y = math.sqrt(val_y_2)
				return [val_y + self.y, -val_y + self.y]
			else:
				val_x_2 = self.radius**2 - (val - self.y)**2
				if val_x_2 < 0:
					return None
				val_x = math.sqrt(val_x_2)
				return [val_x + self.x, -val_x + self.x]
		else:
			return None

	def get_points_of_intersection(self, original_curve):
		#This will be called in a method of Shape to find some the points of intersection
		#This will later on be filtered out in that solution
		if type(original_curve) is init.Sensor:
			#Allows us to put Sensor directly into the function
			curve = Curve(original_curve)
		elif type(original_curve) is Curve:
			curve = original_curve
		else:
			return []

		if type(curve) is Curve and not self.isCircle:
			if type(curve) is Curve and curve.isCircle:
				if self.isHorizontal:
					x1_x2 = curve.getOtherCoordinate(self.y, False)
					if x1_x2 == None:
						return []
					elif x1_x2[0] != x1_x2[1]:
						return [(x1_x2[0], self.y), (x1_x2[1], self.y)]
					else:
						return [(x1_x2[0], self.y)]
				else:
					y1_y2 = curve.getOtherCoordinate(self.x)
					if y1_y2 == None:
						return []
					elif y1_y2[0] != y1_y2[1]:
						return [(self.x, y1_y2[0]), (self.x, y1_y2[1])]
					else:
						#In case its tangential
						return [(self.x, y1_y2[0])]
		elif type(curve) is Curve:
			if not curve.isCircle:
				#Basically if circle and line, just do line with circle by recursive call
				return curve.get_points_of_intersection(self)
			else:
				#Between intersecting circles
				X = 0
				Y, Z = None, None
				if self.y != curve.y:
					#We know for sure the the two points are not on a common horizontal line
					A = -2 * (self.x - curve.x)
					B = self.x**2 - curve.x**2 + self.y**2 - curve.y**2
					C = 2 * (self.y - curve.y)

					X = 1 + A**2 / C**2
					Y = -2 * self.x + 2 * A * B / C**2 - 2 * A * self.y / C
					Z = B**2 / C**2 - 2*B*self.y / C + self.x**2 + self.y**2 - self.radius**2
					if X == 0 or Y == None or Z == None or Y**2 - 4 * X * Z < 0:
						return []
					else:
						val = math.sqrt(Y**2 - 4 * X * Z)
						if val == 0:
							x1 = -Y / (2 * X)
							y1 = (A * x1 + B) / C
							return [(x1, y1)]
						else:
							x1 = (-Y + val) / (2 * X)
							y1 = (A * x1 + B) / C
							x2 = (-Y - val) / (2 * X)
							y2 = (A * x2 + B) / C
							return [(x1, y1), (x2, y2)]
				elif self.x != curve.x:
					#We know for sure the the two points are not on a common vertical line
					A = -2 * (self.y - curve.y)
					B = self.x**2 - curve.x**2 + self.y**2 - curve.y**2
					C = 2 * (self.x - curve.x)

					X = 1 + A**2 / C**2
					Y = 2*A*B/C**2 - 2*A*self.x / C - 2 * self.y
					Z = B**2/C**2 - 2*B*self.x / C + self.x**2 + self.y**2 - self.radius**2
					if X == 0 or Y == None or Z == None or Y**2 - 4 * X * Z < 0:
						return []
					else:
						val = math.sqrt(Y**2 - 4 * X * Z)
						if val == 0:
							y1 = -Y / (2 * X)
							x1 = (A * y1 + B) / C
							return [(x1, y1)]
						else:
							y1 = (-Y + val) / (2 * X)
							x1 = (A * y1 + B) / C
							y2 = (-Y - val) / (2 * X)
							x2 = (A * y2 + B) / C
							return [(x1, y1), (x2, y2)]

				return []

class Shape:
	#We always initialize a shape with a gridcell
	interval = 0.1
	def __init__(self, grid):
		if type(grid) is init.GridCell:
			self.Q = grid.getVertices() #I'm referring to Q in the paper to make it easy but vertices works too
			temp = grid.getCurveSet()
			self.curveSet = []
			for i in temp:
				curve = Curve(i[0], isHorizontal = i[1])
				self.curveSet.append(curve)

	def consecutive_points_inside(self, sensor):
		if type(sensor) is init.Sensor:
			answer = []
			temp = []
			first = None
			for i in self.Q:
				if Shape.distance_squared(i, sensor.coordinates) <= init.Sensor.radius**2:
					#Basically distance formula but no need to find square root
					temp.append(i)
				else:
					#We will only obtain a consecutive set everytime
					if len(temp) > 0:
						if first == None:
							first = temp

						if len(answer) < len(temp):
							del answer	#Maintains space and no unnecessary space remains
							answer = temp
						temp = []
			if first[0] == self.Q[0] and len(temp) > 0 and temp[-1] == self.Q[-1]:
				temp += first #The last and first vertices are adjacent and thus if both are inside, then union their sets

			if len(answer) < len(temp):
				del answer
				answer = temp
			return answer
		else:
			print("Error: Not a sensor")
			return None

	def distance_squared(coord1, coord2):
		x2 = (coord1[0] - coord2[0])**2
		y2 = (coord1[1] - coord2[1])**2
		return x2 + y2

	'''
		Important:
			get_vertices_for_area only holds accurate if the angular separation is <= 90 degrees
			Even then, it could be wrong due to the uncertainty of arc actually taken by area
			Will rectify in the next version
			Will work on it to encompass all

		get_vertices_for_area is to fundamentally get all the points needed for shapely's common
		area function.
	'''
	def get_vertices_for_area(self):
		answer = []
		length = len(self.Q)
		for i in range(len(self.curveSet)):
			if self.curveSet[i].isCircle:
				a = self.Q[i]
				b = self.Q[(i + 1) % length]
				if abs(a[0] - b[0]) >= abs(a[1] - b[1]):
					if b[0] > a[0]:
						interval_used = Shape.interval
					else:
						interval_used = -Shape.interval
					for i in Range(a[0], b[0], interval_used):
						y1_y2 = self.curveSet[i].getOtherCoordinate(i)
						if y1_y2 != None:
							if (y1_y2[0] <= a[1] and y1_y2[0] >= b[1]) or (y1_y2[0] >= a[1] and y1_y2[0] <= b[1]):
								answer.append(y1_y2[0])
							elif (y1_y2[1] <= a[1] and y1_y2[1] >= b[1]) or (y1_y2[1] >= a[1] and y1_y2[1] <= b[1]):
								answer.append(y1_y2[1])
				else:
					if b[1] > a[1]:
						interval_used = Shape.interval
					else:
						interval_used = -Shape.interval
					for i in Range(a[1], b[1], interval_used):
						x1_x2 = self.curveSet[i].getOtherCoordinate(i, False)
						if x1_x2 != None:
							if (x1_x2[0] <= a[0] and x1_x2[0] >= b[0]) or (x1_x2[0] >= a[0] and x1_x2[0] <= b[0]):
								answer.append(x1_x2[0])
							elif (x1_x2[1] <= a[0] and x1_x2[1] >= b[0]) or (x1_x2[1] >= a[0] and x1_x2[1] <= b[0]):
								answer.append(x1_x2[1])
			else:
				answer.append(self.Q[i])
		if self.Q[-1] != answer[-1]:
			answer.append(self.Q[-1])
		return answer
'''
rect = init.GridCell(500, 500)
shape = Shape(rect)
print(shape.get_vertices_for_area())
init.Sensor.radius = 50
sensor = init.Sensor((475,475))
sensor2 = init.Sensor((400, 475))
c1 = Curve(sensor)
c2 = Curve(sensor2)
print(c2.get_points_of_intersection(sensor))
print(shape.consecutive_points_inside(sensor))
'''