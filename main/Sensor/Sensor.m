#This struct defines a sensor and its sensing range.
#The sensor is located at (x,y) and has a sensing radius R.
function sensor=Sensor(x,y,R)
	sensor.location=Point(x,y);
	sensor.range=R;
endfunction
