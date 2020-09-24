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

z=StructArray();

z=add_struct(z,Point(0,0));
z=add_struct(z,Point(0,1));
z=add_struct(z,Point(0,2));
z=add_struct(z,Point(0,3));
z=add_struct(z,Point(0,4));

for x=1:1:size(z)(2)
	z(x)
endfor

#Delete a struct at index 3
z(3)=[];

printf("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n");

for x=1:1:size(z)(2)
	z(x)
endfor

