#Function that adds a struct of a particular type to a struct array.
#It is the users responsibility to ensure that the correct struct type is added.
function return_struct=add_struct(struct_array,struct_data)
	#If the struct array is newly initialized , the fieldnames will be empty.
	#So we use that to check for emptiness first.
	#This is because in GNU Octave , even empty struct arrays come with a size of 1.
	fnames=fieldnames(struct_array);
	#Get the dimensions of the fieldnames matrix.
	fsize=size(fnames);
	#If the number of rows are 0 , the struct array is empty.
	#And we enter the first element.
	if(fsize(1)==0)
		struct_array(1)=struct_data;
	#Otherwise enter the ('length'+1)th element.(Indexing is from 1 , not from 0)
	else
		array_length=size(struct_array)(2);
		struct_array(array_length+1)=struct_data;
	endif
	return_struct=struct_array;
endfunction
#The condition in the if statement can be compressed as:
#	if(size(fieldnames(struct_array))(1)==0)
