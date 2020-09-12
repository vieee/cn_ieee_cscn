#Defines a cell in a grid.
#The cell is defined by the bottom left corner and the upper right corner.
function gc=GridCell(bottom_left,top_right)
	gc.bottom_left=bottom_left;
	gc.top_right=top_right;
endfunction;
