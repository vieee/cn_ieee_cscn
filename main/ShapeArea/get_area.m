#Calculate the area of a ShapeArea struct.
function a=get_area(sa)
	vlines=sa.vlines;
	#The number of lines that make up the ShapeArea.
	num_vlines=size(vlines)(2);
	a=0;
	for x=1:1:num_vlines
		a+=vls_length(vlines(x));
	endfor
	#Multiply by the horizontal separation.
	a*=sa.dx;
endfunction;
