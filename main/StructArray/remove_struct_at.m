#Given a structure array 'sa' , remove the structure at index 'at'.
#All subsequent elements are shifted by 1.
function _sa=remove_struct_at(sa,at)
	#Remove it.
	sa(at)=[];
	_sa=sa;
endfunction;

