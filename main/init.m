#This simply creates the major area and randomly creates the sensors in separate positions
function [rect, sensors] = init()
	width = input("Please state the length of the area: ");
	height = input("Please state the width of the area: ");
	rect = GridCell(0, 0, width, height);
	sensors = StructArray();
	n = input("Please enter the number of Sensors: ");
	r = input("Please enter the range of each sensor: ");
	min_no = width * height * 2 / (r * r);
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
	Please enter the number of Sensors: 105
	Please enter the range of each sensor: 2
	1.051990 0.812503
	2.232733 0.838081
	3.569205 1.179047
	4.634457 0.031148
	6.907031 0.980785
	7.201801 0.312616
	8.663522 0.659577
	10.532102 0.445877
	1.328954 1.709679
	2.814515 1.949929
	3.749500 1.528161
	5.076053 1.435016
	6.859819 2.189065
	7.741527 1.733464
	9.463590 2.742337
	11.035851 1.862852
	0.882745 2.890305
	2.757878 3.401402
	3.185446 2.974191
	5.260553 3.622270
	6.083459 3.856161
	7.496494 3.213701
	9.459570 3.805857
	10.868361 2.888842
	0.570645 5.464068
	2.415048 4.287285
	3.316654 5.029693
	4.776159 5.255692
	5.958374 4.890017
	7.912183 4.594054
	9.701826 4.544584
	10.526212 4.837751
	1.167661 5.817456
	1.423795 6.576228
	3.697660 6.150429
	4.932777 6.573497
	6.259678 6.076114
	8.078401 6.442286
	9.106823 6.429546
	10.025973 5.792639
	0.948690 7.241602
	2.813658 7.250266
	3.706508 7.243234
	5.294791 8.432670
	5.943250 7.828534
	7.123746 7.962594
	8.836321 7.524631
	10.771792 7.377209
	0.665202 9.113150
	2.025894 8.576837
	4.204986 9.898391
	4.407961 9.139393
	6.168954 9.086868
	7.691481 9.301762
	8.608640 9.032468
	11.312198 9.807295
	0.876939 10.812734
	1.748970 9.963501
	3.637333 10.792804
	4.588192 11.158908
	6.046169 9.914518
	8.302962 10.635466
	8.836104 10.610019
	9.964537 10.633725
	3.827242 2.932102
	4.074155 5.355465
	1.140093 2.630156
	5.352563 7.313009
	7.092287 0.108631
	1.640310 2.065320
	4.434816 2.291439
	5.959969 1.923413
	8.608284 7.211330
	9.152361 0.784429
	1.218781 0.343715
	4.437439 2.952980
	7.111098 4.773313
	5.180669 3.512252
	7.833184 5.350378
	3.934031 0.114440
	3.475947 6.022907
	7.715902 9.949540
	0.965916 6.330635
	3.468006 4.857291
	8.018308 5.619514
	9.156140 8.791636
	8.706186 4.202590
	9.828886 7.429282
	8.419413 4.254447
	0.989420 7.384868
	2.545583 6.551082
	5.883681 0.215524
	7.317459 6.212747
	0.118031 9.323585
	4.940960 9.738363
	0.750028 7.124318
	7.398666 4.782150
	1.956830 0.574421
	2.041786 4.650994
	0.155368 8.413246
	5.141108 9.162052
	1.157215 0.063597
	0.087631 1.129387
	5.173037 7.552799
	1.395935 7.378317
	1.482758 4.608307
	8.587071 9.386702
	9.786027 6.152949
	4.204787 8.363015
	2.100622 5.730589
	7.654379 1.496522
	7.370582 1.977226
	7.871720 4.013683
	2.412919 8.610026
	4.388996 4.694437
	3.149239 8.879906
	8.481993 6.099009
	7.793101 6.364063
	2.046112 3.511239
#}
