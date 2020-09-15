#Function to find the index of a struct in a struct array.
function idx=locate_struct(struct_array,struct_data)
	#Get the length of the array(number of columns)
	array_length=size(struct_array)(2);
	#For every struct in the array , do
	for x=1:1:array_length
		#If the structs match , return the index.
		if(isequal(struct_array(x),struct_data))
			idx=x;
			return;
		endif
	endfor
	#Return -1 if nothing was found.
	idx=-1;
endfunction
