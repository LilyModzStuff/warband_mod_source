from header_operations import *
from cstm_constants import *

class Script:
	def __init__(self, id, operations):
		self.id = id
		self.operations = operations
	
	def convert_to_tuple(self):
		return (self.id, self.operations)
	
	def script_param(self, param_no):
		store_script_param_operations = [store_script_param]
		if param_no == 1:
			store_script_param_operations.append(store_script_param_1)
		elif param_no == 2:
			store_script_param_operations.append(store_script_param_2)
		
		script_params = [operation[1] for operation in self.operations if type(operation) == tuple and operation[0] in store_script_param_operations and (operation[0] != store_script_param or operation[2] == param_no)]
		
		if len(script_params) == 0:
			raise ValueError("Tried to get script parameter %d of script %s, but no store_script_param operation could be found" % (param_no, self.id))
		
		return script_params[0]
	
	def store_script_param_index(self, param_no):
		store_script_param_operations = [store_script_param]
		if param_no == 1:
			store_script_param_operations.append(store_script_param_1)
		elif param_no == 2:
			store_script_param_operations.append(store_script_param_2)
		
		store_script_param_tuples = [operation for operation in self.operations if type(operation) == tuple and operation[0] in store_script_param_operations and (operation[0] != store_script_param or operation[2] == param_no)]
		
		if len(store_script_param_tuples) == 0:
			raise ValueError("Tried to get script parameter %d of script %s, but no store_script_param operation could be found" % (param_no, self.id))
		
		return self.operations.index(store_script_param_tuples[0])

def custom_tree_start_slot_operations(custom_troop_tree, skin):
		operations = []
		
		for tier in xrange(custom_troop_tree.num_tiers):
			for branch in xrange(min(tier + 1, custom_troop_tree.num_branches)):
				custom_troop_id = "trp_" + custom_troop_tree.get_custom_troop_id(skin, branch, tier)
				dummy_id = "trp_" + custom_troop_tree.get_custom_troop_dummy_id(skin, branch, tier)
				
				attribute_points = custom_troop_tree.levels_per_upgrade
				if tier == 0:
					attribute_points = custom_troop_tree.levels_start
				
				operations.extend([
					(troop_set_slot, custom_troop_id, cstm_slot_troop_dummy, dummy_id),
					(troop_set_slot, dummy_id, cstm_slot_troop_custom_troop, custom_troop_id),
					
					#(call_script, "script_cstm_troop_reset_stats", custom_troop_id),
					(call_script, "script_cstm_troop_set_stats_to_default", custom_troop_id),
					(call_script, "script_cstm_copy_custom_troop_to_dummy", custom_troop_id),
				])
		
		return operations