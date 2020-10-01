addpath("./cn_ieee_cscn/main/GridCell");
addpath("./cn_ieee_cscn/main/StructArray");
# This simply creates the major area and randomly creates the sensors in separate positions
function [rect, sensors] = init()
	width = input("Please state the length of the area: ");
	height = input("Please state the width of the area: ");
	rect = GridCell(0, 0, width, height);
	sensors = StructArray();
	n = input("Please enter the number of Sensors: ");
	r = input("Please enter the range of each sensor: ");
	for i = 1 : 1 : n
		sensor = Sensor(width * rand(1), height * rand(1), r);
		sensors = add_struct(sensors, sensor);
		# disp(sensors(i + 1));
	endfor
endfunction

#{
This is how we implement it
[rect, sensors] = init();
for i = 1 : 1 : length(sensors)
	disp(sensors(i));
endfor
#}
