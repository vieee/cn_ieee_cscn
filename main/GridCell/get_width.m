#Returns the width of the grid cell.
function w=get_width(gc)
	w=abs(gc.bottom_left.x-gc.top_right.x);
endfunction
