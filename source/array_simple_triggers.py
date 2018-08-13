from array_scripts import *

simple_triggers=[
  # array Garbage Collection.  Will delete all arrays marked for deletion (-ve value for owner), or if their owner (party) is no longer active
    (1, [
		(try_begin),
			(eq, array_debug, 1),
			(display_log_message, "@array GC"),
		(try_end),
    
        (try_for_parties, ":array"),
            (call_script, "script_cf_array_is_array", ":array"),
            (call_script, "script_array_get_owner", ":array"),
            (assign, ":owner", reg0),
            (try_begin),
                (this_or_next|eq, ":owner", 0), # no GC
                (this_or_next|party_slot_eq, ":owner", slot_array_signature, array_signature), #caba addition for sub-arrays (this is all "script_cf_array_is_array" is) 
				(party_is_active, ":owner"),
				(try_begin),
					(eq, array_debug, 1),
					(display_log_message, "@array GC: owner active, an array or is 0"),
				(try_end),
            (else_try),
                (assign, reg21, ":array"),  
				(try_begin),
					(eq, array_debug, 1),				
					(display_log_message, "@array GC: removing {reg21}"),
				(try_end),
                # do garbage collection
                (call_script, "script_array_destroy", ":array"),
            (try_end),            
        (try_end),        
    ]),
] # simple_triggers



from util_common import *
def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1127 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "simple_triggers"
		orig_simple_triggers = var_set[var_name_1]
		
		add_objects(orig_simple_triggers, simple_triggers, False)
		
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)