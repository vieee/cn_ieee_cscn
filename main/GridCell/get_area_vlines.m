#Work is done.
#TODO
#Needs commenting and explanation!!
function vlines=get_area_vlines(gc,hsepr)
	#Get the height of the grid cell
	height=get_height(gc);
	#The initial X-coordinate
	x_start=gc.bottom_left.x;
	#The final X-coordinate
	x_end=gc.top_right.x;
	#The Y-coordinate of the base.
	base_y=gc.bottom_left.y;
	#The struct array to hold all vertical lines that make up the grid.
	vlines=struct();
	#Fill up the struct array with all the vline structs.
	for x=x_start:hsepr:x_end
		vlines=add_struct(vlines,VerticalLineSegment(x,base_y,base_y+height));
	endfor
	#Take the last one also in case it wasn't included.
	if(x<x_end)
		vlines=add_struct(vlines,VerticalLineSegment(x_end,base_y,base_y+height));
	endif
endfunction
