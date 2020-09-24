#Returns the height of the grid cell.
function h=get_height(gc)
	h=abs(gc.bottom_left.y-gc.top_right.y);
endfunction
