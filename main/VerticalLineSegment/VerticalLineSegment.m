#The VerticalLineSegment struct defines a vertical line.
#x is the X-coordinate which is common for both end points.
#y1 and y2 are the Y-coordinates of both end points.
#The endpoints of the line segment are (x,y1) and (x,y2).
function vline=VerticalLineSegment(x,y1,y2)
	vline.x=x;
	vline.y1=y1;
	vline.y2=y2;
endfunction
