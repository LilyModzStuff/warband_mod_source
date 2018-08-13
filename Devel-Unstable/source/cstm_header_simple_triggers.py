class SimpleTrigger:
	def __init__(self, check_interval, operations = []):
		self.check_interval = check_interval
		self.operations = operations
	
	def __str__(self):
		script_string = "(" + str(self.check_interval) + ",\n[\n"
		for operation in self.operations:
			script_string += "\t" + str(operation) + ",\n"
		script_string += "])"
		return script_string
	
	def convert_to_tuple(self):
		return (self.check_interval, self.operations)