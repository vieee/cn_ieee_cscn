'''
Utility functions for type and value handling.
Written because sometimes I find the:

if condition:
	raise <Something>

constructs too repetitive.
'''

#If the type of 'variable' matches any one type in 'variable_types' , do nothing.
#Otherwise , raise a TypeError with the error message as 'message'.
def type_check(variable,variable_types,message=''):
	for variable_type in variable_types:
		if isinstance(variable,variable_type):
			return
	raise TypeError(message)

#If the condition 'condition' is true , then do nothing.
#Else , raise a ValueError with the error message as 'message'.
def value_check(condition,message=''):
	if not condition:
		raise ValueError(message)
