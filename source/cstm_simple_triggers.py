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

	# This trigger will activate upon the game being loaded
	(0,
	[
		(try_begin),
			(store_item_kind_count, reg0, "itm_no_item", "trp_cstm_load_check"),
			(eq, reg0, 0),
			
			# Restore custom troop inventories, which are reset upon loading
			(try_for_range, ":troop", "$cstm_troops_begin", "$cstm_troops_end"),
				(call_script, "script_cstm_replace_custom_troop_with_dummy", ":troop"),
			(try_end),
			
			# Re-establish the item arrays used for troop equipment options in case new items have been added
			(call_script, "script_cstm_setup_item_arrays"),
			
			(troop_add_item, "trp_cstm_load_check", "itm_no_item"),
		(try_end),
	]),
	
]

def modmerge(var_set):
	try:
		var_name_1 = "simple_triggers"
		orig_simple_triggers = var_set[var_name_1]
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)
	
	orig_simple_triggers.extend(new_simple_triggers)
	
	simple_triggers = [SimpleTrigger(*st_tuple) for st_tuple in orig_simple_triggers]
	
	del orig_simple_triggers[:]
	orig_simple_triggers.extend([simple_trigger.convert_to_tuple() for simple_trigger in simple_triggers])