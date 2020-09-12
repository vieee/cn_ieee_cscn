#Returns the length of a vertical line segment.
#It is just the absolute difference between the two Y coordinates.
function l=vls_length(vline)
	l=abs(vline.y1-vline.y2);
endfunction
