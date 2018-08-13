from header_operations import *
from cstm_constants import *

class Script:
	def __init__(self, id, operations):
		self.id = id
		self.operations = operations
	
	def convert_to_tuple(self):
		return (self.id, self.operations)

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