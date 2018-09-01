import collections

class Menu:
	def __init__(self, id, flags = 0, text = "", mesh_name = "none", operations = [], option_tuples = []):
		self.id = id
		self.flags = flags
		self.text = text
		self.mesh_name = mesh_name
		self.operations = operations
		self.options = collections.OrderedDict()
		
		for option_tuple in option_tuples:
			option_id = option_tuple[0]
			if option_id in self.options.keys():
				index = 1
				new_option_id = option_id + "_" + str(index)
				while new_option_id in self.options:
					index += 1
					new_option_id = option_id + "_" + str(index)
				
				option_id = new_option_id
			
			self.options[option_id] = MenuOption(*option_tuple[0:5])
	
	def __eq__(self, other):
		return (isinstance(other, self.__class__) and self.id == other.id)
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def convert_to_tuple(self):
		option_tuples = []
		for option_id in self.options:
			option_tuples.append(self.options[option_id].convert_to_tuple())
		
		return (self.id, self.flags, self.text, self.mesh_name, self.operations, option_tuples)
	
	def add_option(self, option_tuple):
		id = option_tuple[0]
		if id in self.options.keys():
			index = 1
			new_id = id + "_" + str(index)
			while new_id in self.options.keys():
				index += 1
				new_id = id + "_" + str(index)
			
			id = new_id
		
		self.options[id] = MenuOption(*option_tuple)
	
	def add_options(self, option_tuples):
		for option_tuple in option_tuples:
			self.add_option(option_tuple)
	
	def insert_option_after(self, option_tuple, ref_id):
		old_options = self.options
		self.options = collections.OrderedDict()
		
		for option_id in old_options.keys():
			self.options[option_id] = old_options[option_id]
			if option_id == ref_id:
				self.add_option(option_tuple)
	
	def insert_option_before(self, option_tuple, ref_id):
		old_options = self.options
		self.options = collections.OrderedDict()
		
		for option_id in old_options.keys():
			if option_id == ref_id:
				self.add_option(option_tuple)
			self.options[option_id] = old_options[option_id]

class MenuOption:
	def __init__(self, id, conditions = [], text = "", consequences = [], doortext = ""):
		self.id = id
		self.conditions = conditions
		self.text = text
		self.consequences = consequences
		self.doortext = doortext
	
	def convert_to_tuple(self):
		return (self.id, self.conditions, self.text, self.consequences, self.doortext)