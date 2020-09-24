#Defines a cell in a grid.
#The cell is defined by the bottom left corner and the upper right corner.
function gc=GridCell(xbl,ybl,xtr,ytr)
	#The bottom left point.
	gc.bottom_left=Point(xbl,ybl);
	#The top right point.
	gc.top_right=Point(xtr,ytr);
endfunction;
