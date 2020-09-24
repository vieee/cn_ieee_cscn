#Find the points of intersection of the sensing circle of a sensor and a vertical line.
#Only the Y-coordinates of the points of intersection are returned.
function xns=sensor_X_vline(sensor,vline)
	R=sensor.range;
	x1=sensor.location.x;
	y1=sensor.location.y;
	#Sensing circle equation is:
	#		(x-x1)^2 + (y-y1)^2 = R^2

	x0=vline.x;
	#Vertical line segment equation is:
	#		x = x0

	#Putting one inside another , we get
	#		(x0-x1)^2 + (y-y1)^2 = R^2
	#

	#Let (x0-x1)=A
	#
	#		A^2 + y^2 - 2(y1)(y) + y1^2 = R^2
	#
	#		(1)y^2 + (-2*y1)y + (y1^2+A^2-R^2) = 0

	#The above is the equation we have to solve for y.

	t1=1;
	t2=-2*y1;
	t3=y1^2+(x0-x1)^2-R^2;

	#Solve the polynomial with the above coefficients.
	xns=roots([t1,t2,t3]);

endfunction
