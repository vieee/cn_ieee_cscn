#Defines a cell in a grid.
#The cell is defined by the bottom left corner and the upper right corner.
function gc=GridCell(xbl,ybl,xtr,ytr)
	gc.bottom_left=Point(xbl,ybl);
	gc.top_right=Point(xtr,ytr);
endfunction;
