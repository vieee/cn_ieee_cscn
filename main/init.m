#This simply creates the major area and randomly creates the sensors in separate positions
function [rect, sensors] = init()
	width = input("Please state the length of the area: ");
	height = input("Please state the width of the area: ");
	rect = GridCell(0, 0, width, height);
	sensors = StructArray();
	n = input("Please enter the number of Sensors: ");
	r = input("Please enter the range of each sensor: ");
	min_no = width * height * 2 / r;
	#	We check if is perfectly divisible or not
	if(min_no != floor(min_no))
		#	Since it is not perfectly divisible, we can assume some residual area to be present
		#	This residual area will consist of minor rectangles.
		val1 = 0;
		val2 = 0;
		#If the width cant sufficiently divide the squares, then you get an extra column of squares
		if((width * 1.414 / r) - floor(width * 1.414 / r) > 0.001 * r)
			val1 = ceil(1.414 * height / r);
		endif

		#If the height cannot sufficiently divide the squares, then you get an extra row of squares
		if((height * 1.414 / r) - floor(height * 1.414 / r) > 0.001 * r)
			val2 = ceil(1.414 * width / r);
		endif

		#There could be an error of one extra sensor, which is acceptable
		min_no = floor(min_no) + val1 + val2;
	endif

	if(n < min_no)
		for i = 1 : 1 : n
			sensor = Sensor(width * rand(1), height * rand(1), r);
			sensors = add_struct(sensors, sensor);
		endfor
	else
		interval = r / 1.414;
		#{
			Basically divide the entire area into squares of side R / sqrt(2) ie. R / 1.414
			Randomly place a sensor in each of those. That way, you can always guarantee there
			is atleast one coverset covering the entire area.

			We find the min no. of those squares and place sensor in each of those.
			In case we can add anymore sensors, we just randomly place them now.
		#}
		for i = 0 : interval : height
			for j = 0 : interval : width
				sensor = Sensor(j + rand(1) * interval, i + rand(1) * interval, r);
				sensors = add_struct(sensors, sensor);
			endfor
		endfor
		for i = 1 : 1 : n - min_no
			sensor = Sensor(width * rand(1), height * rand(1), r);
			sensors = add_struct(sensors, sensor);
		endfor
	endif
endfunction

#{
[rect, sensors] = init();
for i = 1 : 1 : length(sensors)
	printf("%f %f\n", sensors(i).location.x, sensors(i).location.y);
endfor
#}

#This is how we implement it
#[rect, sensors] = init();
#for i = 1 : 1 : length(sensors)
#	disp(sensors(i));
#endfor

#{
	This is for the one with printf inside
	
	Please state the length of the area: 10
	Please state the width of the area: 10
	Please enter the number of Sensors: 100
	Please enter the range of each sensor: 2
	0.487526 0.782340
	2.286264 1.245565
	3.720290 0.227262
	4.655021 1.339346
	5.857859 0.522815
	8.211111 1.244111
	8.799286 0.070632
	11.098213 0.021965
	1.149255 1.520924
	2.379926 2.738386
	3.929685 2.414347
	5.336380 2.301182
	5.854652 2.644718
	7.694689 2.696295
	8.618093 2.124886
	11.094680 2.760133
	0.596738 3.893679
	2.195599 3.426093
	4.196826 3.151857
	4.360392 3.129508
	6.510548 3.311326
	7.573876 4.034976
	8.506048 2.962528
	10.764479 3.689606
	0.838099 5.384201
	2.343015 5.396114
	2.871605 4.832161
	5.045894 5.383712
	6.505988 5.515690
	8.091111 4.596417
	9.504781 5.485195
	10.525570 5.277428
	1.305815 6.996327
	2.741329 6.588256
	3.377892 5.924282
	4.843042 6.426611
	6.358076 6.211246
	8.348239 6.890434
	8.890722 5.920166
	11.183066 6.242560
	1.009591 7.715203
	1.922085 7.363253
	3.610915 7.638772
	5.195563 7.754635
	6.657291 7.516904
	7.500711 8.242373
	8.623038 7.328367
	10.254152 7.282592
	1.024959 9.693125
	2.522649 9.278714
	3.879714 9.344734
	5.158582 9.530820
	6.987807 9.759316
	7.548625 8.924261
	8.898465 8.601783
	10.060842 9.519102
	0.712780 11.311276
	2.527834 10.357936
	3.073301 11.025501
	4.957417 10.234167
	6.363876 10.186892
	7.228615 10.879180
	9.449477 10.112478
	9.957395 10.503561
#}
