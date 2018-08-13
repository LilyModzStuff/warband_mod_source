class Presentation:
	def __init__(self, id, flags, mesh, trigger_tuples):
		self.id = id
		self.flags = flags
		self.mesh = mesh
		self.triggers = {}
		for trigger_tuple in trigger_tuples:
			self.add_trigger(trigger_tuple)

	def convert_to_tuple(self):
		triggers = []
		for trigger_type in self.triggers:
			for trigger in self.triggers[trigger_type]:
				triggers.append((trigger_type, trigger))
		
		return (self.id, self.flags, self.mesh, triggers)
	
	def add_trigger(self, trigger_tuple):
		trigger_type = trigger_tuple[0]
		trigger = trigger_tuple[1]
		
		if trigger_type not in self.triggers:
			self.triggers[trigger_type] = []
		self.triggers[trigger_type].append(trigger)