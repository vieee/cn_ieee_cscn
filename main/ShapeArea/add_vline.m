#Adds a structure of type VerticalLineSegment struct to a ShapeArea struct.
function _sa=add_vline(sa,vline)
	sa.vlines=add_struct(sa.vlines,vline);
	_sa=sa;
endfunction;