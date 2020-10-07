'''
Utility functions for type and value handling.
Written because:

if condition:
	raise <Something>

constructs too repetitive.
'''

def type_check(variable,variable_types,message=''):
	for variable_type in variable_types:
		if isinstance(variable,variable_type):
			return
	raise TypeError(message)

def value_check(condition,message=''):
	if not condition:
		raise ValueError(message)
