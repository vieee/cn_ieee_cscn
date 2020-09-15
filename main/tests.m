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

p=Point(10,10);

gc=GridCell(Point(0,0),p);

gc

p.x=10100;

gc
