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

sensor=Sensor(1,0,5);

gc_shape_area=get_shape_area(gc,0.001);

[a,to_remove,to_add]=try_intersection(sensor,gc_shape_area);

a
