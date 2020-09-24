#Add the path for all the utility functions.
addpath("./utils");
#Add the path for the vertical line segment struct.
addpath("./VerticalLineSegment");
#Add the path for the sensor struct.
addpath("./Sensor");
#Add the path for the point struct.
addpath("./Point");
#Add the path for the grid cell struct.
addpath("./GridCell");
#Add the path for the struct array functions.
addpath("./StructArray");
#Add the path for the shape area functions.
addpath("./ShapeArea");
#Add the path for the duynamic array functions.
addpath("./Dynamic1DMatrix")

#Testing the intersection of vlines and circles.
gc=GridCell(0,0,10,10);

#Test 1:Sensor at corner
sensor=Sensor(0,0,5);
gc_shape_area=get_shape_area(gc,0.005);
[a,b,c]=try_intersection(sensor,gc_shape_area);
a

#Test 2:Sensor at center
sensor=Sensor(5,5,5);
gc_shape_area=get_shape_area(gc,0.005);
[a,b,c]=try_intersection(sensor,gc_shape_area);
a

#Test 3:Sensor on vertical side
sensor=Sensor(5,0,5);
gc_shape_area=get_shape_area(gc,0.005);
[a,b,c]=try_intersection(sensor,gc_shape_area);
a

#Test 4:Sensor on horizontal side
sensor=Sensor(0,5,5);
gc_shape_area=get_shape_area(gc,0.001);
[a,b,c]=try_intersection(sensor,gc_shape_area);
a

#Test 5:Random Location
sensor=Sensor(1,0,5);
gc_shape_area=get_shape_area(gc,0.001);
[a,b,c]=try_intersection(sensor,gc_shape_area);
a


#
#The second parameter passed into get_shape_area() determines the accuracy of the algorithm.
#A smaller value increases the accuracy but also increases the time period of execution.
#
#As a rule of thumb , keep the value between [0.01 to 0.001].
#
#The time and accuracy also depends upon the shape and the location of the sensor.(Look at cases 3 and 4)
#
