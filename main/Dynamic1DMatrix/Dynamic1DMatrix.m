function d1dm=Dynamic1DMatrix()
	d1dm=struct();
	#The current index to insert at.
	d1dm._c_i=1;
	#The actual matrix
	d1dm._mx=[];
endfunction
