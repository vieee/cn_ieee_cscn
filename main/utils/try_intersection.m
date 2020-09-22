#Try to intersect a sensors sensing radius with an array of vlines.
function [area_of_intersection,vline_indices_to_remove,vlines_to_add]=try_intersection(sensor,shapearea)
	#The initial area of intersection is 0.
	area_of_intersection=0;
	#Struct array of the indices of the lines to remove(lines which come inside the sensing radius)
	#This is a dynamic 1D matrix(dymanic array)
	vline_indices_to_remove=Dynamic1DMatrix();
	#Struct array of the lines to add(lines which remain outside the sensing radius)
	#This is an array ot structs
	vlines_to_add=StructArray();
	#Repeat the following for every line in the shape area.
	num_lines=size(shapearea.vlines)(2);
	for x=1:1:num_lines
		vline=shapearea.vlines(x);
		#The end Y-coordinates of the line segment.
		#Lower bound.
		vline_min=min([vline.y1,vline.y2]);
		#Upper bound.
		vline_max=max([vline.y1,vline.y2]);
		#Y-coordinates of intersection of the sensing circle with a vline
		y_coords=sensor_X_vline(sensor,vline);
		yc_min=min(y_coords);
		yc_max=max(y_coords);
		
		#Case 1:This line comes outside the circle completely.
		#The points of intersection are thus imaginary.
		#If any one point is imaginary , the other must also be imaginary and so we do nothing.
		if(imag(yc_min)!=0)
			continue;
		#Case 2:This line comes inside the circle completely.
		#The points of intersection are real.
		#Both segment endpoints come within the Y-coordinates of intersection.
		#Both Y-coordinates come between the endpoints of the line segment.
		elseif(in_between(yc_min,vline_min,yc_max) && in_between(yc_min,vline_max,yc_max))
			#This line segment must be removed completely.
			#No new vertical line segment will be added.
			#Add the current index in the list of indices to be removed.
			vline_indices_to_remove=append(vline_indices_to_remove,x);
			#The length of this line will be used to calculate the possible area of this circle.
			area_of_intersection+=vls_length(vline);
		#Case 3:Circle cuts the segment at some point.
		#This is tricky.
		else
			#Case 3.1:The circle cuts the line at exactly 2 point.
			if(in_between(vline_min,yc_min,vline_max) && in_between(vline_min,yc_max,vline_max))
				#The length to be considered is the distance between the two points.
				area_of_intersection+=(yc_max-yc_min);
				#Add the current index in the list of indices to be removed.
				vline_indices_to_remove=append(vline_indices_to_remove,x);
				#Two new vlines will have to be added.
				#One from vline_min to yc_min.
				#Another from yc_max to vline_max.
				vlines_to_add=add_struct(vlines_to_add,VerticalLineSegment(vline.x,vline_min,yc_min));
				vlines_to_add=add_struct(vlines_to_add,VerticalLineSegment(vline.x,yc_max,vline_max));
			#Case 3.2:The circle cuts the line at exactly 1 point and the point is yc_min
			elseif(in_between(vline_min,yc_min,vline_max))
				#In this case , vline_max lies within the circle.
				#The length to be considered is the distance between yc_min and vline_max.
				area_of_intersection+=(vline_max-yc_min);
				#Add the current index in the list of indices to be removed.
				vline_indices_to_remove=append(vline_indices_to_remove,x);
				#A vline from vline_min to yc_min is added as it is the residual line outside the circle.
				vlines_to_add=add_struct(vlines_to_add,VerticalLineSegment(vline.x,vline_min,yc_min));
			#Case 3.3:The circle cuts the line at exactly 1 point and the point is yc_max
			elseif(in_between(vline_min,yc_max,vline_max))
				#In this case , vline_min lies within the circle.
				#The length to be considered is the distance between yc_max and vline_min.
				area_of_intersection+=(yc_max-vline_min);
				#Add the current index in the list of indices to be removed.
				vline_indices_to_remove=append(vline_indices_to_remove,x);
				#A vline from yc_max to vline_max is added as it is the residual line outside the circle.
				vlines_to_add=add_struct(vlines_to_add,VerticalLineSegment(vline.x,yc_max,vline_max));
			endif
		endif
	endfor
	area_of_intersection*=shapearea.dx;
endfunction
