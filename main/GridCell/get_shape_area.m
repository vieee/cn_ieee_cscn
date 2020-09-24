#Work is done.
#TODO
#Needs commenting and explanation!!
function shape_area=get_shape_area(gc,hsepr)
	#Get the height of the grid cell
	height=get_height(gc);
	#The initial X-coordinate
	x_start=gc.bottom_left.x;
	#The final X-coordinate
	x_end=gc.top_right.x;
	#The Y-coordinate of the base.
	base_y=gc.bottom_left.y;
	#The ShapeArea struct to define the area of the cell.
	shape_area=ShapeArea(hsepr);
	#Fill up the ShapeArea struct with all the vline structs.
	#But ignore the last one if it hits the opposite boundary.
	for x=x_start:hsepr:x_end
		if(x==x_end)
			break;
		endif
		shape_area=add_vline(shape_area,VerticalLineSegment(x,base_y,base_y+height));
	endfor
endfunction

