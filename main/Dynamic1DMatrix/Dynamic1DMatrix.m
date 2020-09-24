#This data structure is designed to act as a dynamic array.
#Currently this array supports only the append operation.
#Further work is required.
#The dynamic array is actually a structure with an index of the size of the array and the array itself.
#The 'array' is actually a 1xn matrix.
function d1dm=Dynamic1DMatrix()
	d1dm=struct();
	#The current index to insert at.
	d1dm._c_i=1;
	#The actual matrix
	d1dm._mx=[];
endfunction
