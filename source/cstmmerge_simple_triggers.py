from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *
from module_constants import *

from cstm_header_simple_triggers import *

####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#	Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################

new_simple_triggers = [

	# Add any new triggers here

]

def operation_matches(operation, arg_tuple):
	matches = False
	if type(operation) == tuple and len(operation) == len(arg_tuple):
		matches = True
		for i in xrange(len(arg_tuple)):
			if arg_tuple[i] != '?' and arg_tuple[i] != operation[i]:
				matches = False
				break
	
	return matches

def modmerge(var_set):
	try:
		var_name_1 = "simple_triggers"
		orig_simple_triggers = var_set[var_name_1]
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)
	
	orig_simple_triggers.extend(new_simple_triggers)
	
	simple_triggers = [SimpleTrigger(*st_tuple) for st_tuple in orig_simple_triggers]
	
	try:
		# Make Diplomacy recruiters go to player faction villages
		dplmc_recruiter_trigger = [trigger for trigger in simple_triggers if len([operation for operation in trigger.operations if operation_matches(operation, (party_slot_eq, '?', slot_party_type, dplmc_spt_recruiter))]) > 0][0]
		get_faction_operations = [(i, operation) for i, operation in enumerate(dplmc_recruiter_trigger.operations) if type(operation) == tuple and operation[0] == party_get_slot and operation[3] == slot_center_original_faction]
		for operation_tuple in get_faction_operations[::-1]:
			index = operation_tuple[0]
			operation = operation_tuple[1]
			
			faction_var = operation[1]
			village_var = operation[2]
			
			dplmc_recruiter_trigger.operations[index+1:index+1] = [
				(try_begin),
					(store_faction_of_party, reg0, village_var),
					(eq, reg0, "fac_player_supporters_faction"),
					
					(assign, faction_var, "fac_player_supporters_faction"),
				(try_end),
			]
	except NameError:
		print "Diplomacy Recruiter party type not found, disregarding changes to recruiter trigger"
	
	del orig_simple_triggers[:]
	orig_simple_triggers.extend([simple_trigger.convert_to_tuple() for simple_trigger in simple_triggers])