#Needs more work!
function arr=get_area_vlines(gc,hsepr)
	height=get_height(gc);
	arr=[];
	x_start=gc.bottom_left.x;
	x_end=gc.top_right.x;
	base_y=gc.bottom_left.y;
	count=0
	for x=x_start:hsepr:x_end
#TODO
#Correct this!!!
		arr[count]=VerticalLineSegment(x,base_y,base_y+height)
		count+=1
	endfor
endfunction
