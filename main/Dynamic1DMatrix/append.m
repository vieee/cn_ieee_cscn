#Append a value into the '1D array'.
function _d1dm=append(d1dm,data)
	#Append.
	d1dm._mx(d1dm._c_i)=data;
	#Modify index.
	d1dm._c_i+=1;
	#Update return statement.
	_d1dm=d1dm;
endfunction
