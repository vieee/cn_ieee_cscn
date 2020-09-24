#Creates a structure that defines the approximate area of a random shape.
function sa=ShapeArea(hsepr)
	sa=struct();
	sa.dx=hsepr;
	sa.vlines=StructArray();
endfunction
