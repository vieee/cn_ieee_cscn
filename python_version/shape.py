import init, math
import copy
class Curve:
	interval = 0.1
	#direction = 0 is anti-clockwise, direction = 1 is clockwise
	def getQuadrant(self, current_pos, direction = None):
		xx = current_pos[0] - self.x
		yy = current_pos[1] - self.y
		if xx != 0:
			xx /= abs(xx)

		if yy != 0:
			yy /= abs(yy)

		quad_vals = {
			(0, 1, 0): 2,
			(0, 1, 1): 1,
			(0, -1, 0): 4,
			(0, -1, 1): 3,
			(1, 0, 0): 1,
			(1, 0, 1): 4,
			(-1, 0, 0): 3,
			(-1, 0, 1): 2,
			(1, 1): 1,
			(-1, 1): 2,
			(-1, -1): 3,
			(1, -1): 4
		}
		
		if xx == 0 or yy == 0:
			return quad_vals[(xx, yy, direction)]
		else:
			return quad_vals[(xx, yy)]

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

	def getQuadrantRange(self, current_pos, direction, div_by_x = True, final_pos = None): #We're doing this wrt x
		quadrant = self.getQuadrant(current_pos, direction)
		if div_by_x:
			upper_bounds = {
				(0, 1): (self.x, -Curve.interval),
				(0, 2): (self.x - self.radius, -Curve.interval),
				(0, 3): (self.x, Curve.interval),
				(0, 4): (self.x + self.radius, Curve.interval),
				(1, 1): (self.x + self.radius, Curve.interval),
				(1, 2): (self.x, Curve.interval),
				(1, 3): (self.x - self.radius, -Curve.interval),
				(1, 4): (self.x, -Curve.interval)
			}
			if final_pos == None:
				return init.Range(current_pos[0], upper_bounds[(direction, quadrant)][0], upper_bounds[(direction, quadrant)][1])
			else:
				return init.Range(current_pos[0], final_pos[0], upper_bounds[(direction, quadrant)][1])
		else:
			upper_bounds = {
				(0, 1): (self.y + self.radius, Curve.interval),
				(0, 2): (self.y, -Curve.interval),
				(0, 3): (self.y - self.radius, -Curve.interval),
				(0, 4): (self.y, Curve.interval),
				(1, 1): (self.y, -Curve.interval),
				(1, 2): (self.y + self.radius, Curve.interval),
				(1, 3): (self.y, Curve.interval),
				(1, 4): (self.y - self.radius, -Curve.interval)
			}
			if final_pos == None:
				return init.Range(current_pos[1], upper_bounds[(direction, quadrant)][0], upper_bounds[(direction, quadrant)][1])
			else:
				return init.Range(current_pos[1], final_pos[1], upper_bounds[(direction, quadrant)][1])

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
			if first != None and first[0] == self.Q[0] and len(temp) > 0 and temp[-1] == self.Q[-1]:
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

	def getDirection(self, index):
		length = len(self.Q)
		start, finish = self.Q[index], self.Q[(index + 1) % length]
		if self.curveSet[index - 1].isCircle or self.curveSet[(index + 1) % length].isCircle:
			quadrant = -1
			currCurve = None
			if self.curveSet[index - 1].isCircle:
				currCurve = index - 1
				currStart = start
			elif self.curveSet[(index + 1) % length].isCircle:
				currCurve = (index + 1) % length
				currStart = finish

			if currStart[0] != self.curveSet[currCurve].x and currStart[1] != self.curveSet[currCurve].y:
				quadrant = self.curveSet[currCurve].getQuadrant(currStart)
			y1_y2 = self.curveSet[currCurve].getOtherCoordinate(currStart[0] - Shape.interval)
			temp = (self.curveSet[currCurve].x, self.curveSet[currCurve].y)
			directions = None
			goLess = None
			if Shape.distance_squared(temp, (currStart[0] - Shape.interval, y1_y2[0])) <= self.curveSet[currCurve].radius**2 or Shape.distance_squared(temp, (currStart[0] - Shape.interval, y1_y2[1])) <= self.curveSet[currCurve].radius**2:
				directions = {
					1: 1, 2: 1, 3: 0, 4: 0
				}
				if Shape.distance_squared(temp, (currStart[0] - Shape.interval, y1_y2[0])) <= self.curveSet[currCurve].radius**2:
					goLess = [True, 0]
				else:
					goLess = [True, 1]
			else:
				directions = {
					1: 0, 2: 0, 3: 1, 4: 1
				}
				goLess = [False, -1]

			if quadrant != -1:
				return directions[quadrant]
			else:
				if goLess[0]:
					quadrant = self.curveSet[currCurve].getQuadrant((currStart[0] - Shape.interval, y1_y2[goLess[1]]))
				else:
					y3_y4 = self.curveSet[currCurve].getOtherCoordinate(currStart[0] + Shape.interval)
					val = -1
					if Shape.distance_squared(temp, (currStart[0] + Shape.interval, y3_y4[0])) <= self.curveSet[currCurve].radius**2:
						val = 0
					else:
						val = 1
					quadrant = self.curveSet[currCurve].getQuadrant((currStart[0] + Shape.interval, y3_y4[val]))

				xx = currStart[0] - self.x
				yy = currStart[1] - self.y
				if xx != 0:
					xx /= abs(xx)

				if yy != 0:
					yy /= abs(yy)

				directions = {
					(1, 0, 4): 0, (1, 0, 1): 1,
					(0, 1, 1): 0, (0, 1, 2): 1,
					(-1, 0, 2): 0, (-1, 0, 3): 1,
					(0, -1, 3): 0, (0, -1, 4): 1
				}
				return directions[(xx, yy, quadrant)]
		else:
			#Assumption: Vertices are in proper order and thus it each of the cases, we go clockwise only
			return 1
	
	def get_area_of_intersection(self, sensor):
		#Basically the matrix form of (x2 - x1) and (y2 - y1)
		temp = self.areaVertices - np.array(sensor.coordinates)
		temp *= temp
		#A matrix with columns (x2 - x1)^2 and (y2 - y1)^2
		temp = np.sum(temp, axis = 1)
		#This accomplishes (x2 - x1)^2 + (y2 - y1)^2
		temp -= sensor.radius**2
		#This is distance^2 - radius^2, basically if an element is <= 0, it is within the sensor's range
		return temp

	def check_best_sensor(self, sensors):
		area = None
		points = None
		index = None
		for i in range(len(sensors)):
			#Run through each sensor
			temp_points = self.consecutive_points_inside(sensors[i])
			'''
				consecutive_points_inside() basically finds the maximum number of consecutive
				vertices inside the sensor's range
			'''
			if points == None or len(temp_points) > len(points):
				index = i
				points = temp_points
				#Basically if a sensor covers a higher no. of consecutive points, it is the best sensor
				area = self.get_area_of_intersection(sensors[i])
			elif len(points) == len(temp_points):
				#No. of vertices of set Q inside the sensors are the same.
				temp_area = self.get_area_of_intersection(sensors[i])
				#If the number of vertices covered by new sensor are more than the ones of the new one
				#Then the new sensor is the best sensor
				'''
					np.where() is a function which returns an array of indices of a matrix
					that fulfill a condition.

					Therefore the number of vertices inside the range of the sensor will be compared
					and based on that, the best sensor is selected.

					--------------Refer to area_of_intersection-------------------

					Now, we know that if an element in the matrix has <= 0, then the vertex from which
					we derived it from is inside the circle.

					We find the index of all such vertices using np.where()
					np.where() returns (matrix needed, datatype)
					Therefore for the matrix, take np.where()[0]

					Now you have an array of all the indices which are in the intersection area.
					
					After finding the best sensor, simply remove all of the vertices that were in the intersection area.
					This reduces the matrix size in the next iteration
					
					The moment the size of this matrix is 0, we get a coverset
				'''
				if len(np.where(temp_area <= 0)[0].tolist()) > len(np.where(area <= 0)[0].tolist()):
					index = i
					points = temp_points
					area = temp_area
		area = np.where(area <= 0)[0].tolist()
		self.areaVertices = self.areaVertices.tolist()
		#print(len(self.areaVertices))
		c1 = len(self.areaVertices)
		'''
			We get the best sensors's area and remove the vertices which were in its intersection
		'''
		for i in range(len(area) - 1, -1, -1):
			self.areaVertices.pop(i)
		c2 = len(self.areaVertices)
		print("No. of points intersected:", c1 - c2)
		#print(len(self.areaVertices))
		self.areaVertices = np.array(self.areaVertices)
		'''
			We now have the remaining set of vertices representing the irregular shape
		'''
		return index, points
'''
To execute the function to get best sensor
rect, sensors = init.init()
print(len(sensors))
Xs = []
Ys = []
for i in sensors:
	Xs.append(i.coordinates[0])
	Ys.append(i.coordinates[1])
Xs = np.array(Xs)
Ys = np.array(Ys)
plt.scatter(Xs, Ys, s = 0.7)
plt.show()

shapex = Shape(rect)
index, points = shapex.check_best_sensor(sensors)
print(index, points)
'''

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
'''
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

		Important:
			get_vertices_for_area only holds accurate if the angular separation is <= 90 degrees
			Even then, it could be wrong due to the uncertainty of arc actually taken by area
			Will rectify in the next version
			Will work on it to encompass all

		get_vertices_for_area is to fundamentally get all the points needed for shapely's common
		area function.
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
