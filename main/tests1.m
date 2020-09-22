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
#Add the path for the struct array functions.
addpath("./ShapeArea");

gc=GridCell(0,0,5,5);
vl=get_shape_area(gc,1);
a=get_area(vl);
a

hs=0.0009;
vl=ShapeArea(hs);
for x=0:hs:5
	if(x==5)
		break;
	endif
	vl=add_vline(vl,VerticalLineSegment(0,0,x));
endfor

a=get_area(vl);
a

#For a length of 5 units , optimum horizontal seperation is 0.0009

