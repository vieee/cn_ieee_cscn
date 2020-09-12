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

p1=Point(0,0);
p2=Point(10,10);

gc=GridCell(p1,p2);

hs=2;

a=get_area_vlines(gc,hs)
