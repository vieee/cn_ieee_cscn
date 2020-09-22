function _d1dm=append(d1dm,data)
	d1dm._mx(d1dm._c_i)=data;
	d1dm._c_i+=1;
	_d1dm=d1dm;
endfunction
