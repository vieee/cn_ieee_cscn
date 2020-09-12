#Check if a sensor of sensing range R can sense a point P.
#Returns 1 if true and 0 otherwise.
function status=can_sense(sensor,P)
	status=(separationSquared(P,sensor.location)<=sensor.range^2);
endfunction
