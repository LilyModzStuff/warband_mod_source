from header_common import *
from header_operations import *
from header_parties import *


array_debug 		= 0
array_signature     = 0xFFFE # Just a magic number.  But should not be changed if desire to be compativle with older save-games
array_version       = 1 # marks the current structure version of array, possibly allowing graceful upgrading of older versions of arrays in existing savegame
array_slot_offset   = 1000 # start of array values.  Shifted up by 1000 to avoid clash with other party slots

slot_array_0        = array_slot_offset  # first element

##generate constants from slot_array_1 to slot_array_99, the lazy fashion
try:
    import sys
    module = sys.modules[__name__]    
    for i in range(1,100):
      setattr(module, "slot_array_%d"%(i), eval("slot_array_%d+1" %(i-1)))
except:
    raise


slot_array_size     = 999 # stores current size of array
slot_array_owner    = 998 #(if 0, array will never be cleaned up, otherwise, this is the party id that owns the array, and when party no longer exists, the array can be cleaned up)
slot_array_signature= 997 # a special slot that will contain a magic value (array_signature) that identifies that this is array
slot_array_version  = 996 # see array_version


# array script definitions
scripts=[

# script_array_create
# Function: Create and return a new array (party)
# Basically, create a dummy party and sets a recognition pattern in certain slots
# Arguments:
# Return: reg0 = id of new array
("array_create",[
    # create fake party
    (set_spawn_radius, 0),
    (spawn_around_party, 1, "pt_none"), # use p_temp_party for position
    (assign, ":array", reg0),
    (party_set_flags, ":array", pf_disabled, 1),
    
    # initialize array data
    
    (party_set_slot, ":array", slot_array_size, 0),
    (party_set_slot, ":array", slot_array_owner, 0),
    (party_set_slot, ":array", slot_array_signature, array_signature),  # magic number to use for array identification            
    (party_set_slot, ":array", slot_array_version, array_version),      # array version  
	(try_begin),
		(eq, array_debug, 1),
		(display_log_message, "@array[{reg0}] created"),
	(try_end),
   ]), # array_create


# script_array_destroy
# Function: Destroys an array.  Does nothing if not an array
# Arguments:array id
# Return:	
("array_destroy",[
    (store_script_param_1, ":array"),
    (try_begin),
        (call_script, "script_cf_array_is_array", ":array"),
		(call_script, "script_array_destroy_sub_arrays", ":array"), #Caba addition for recursive deletion
        (remove_party, ":array"),
		(eq, array_debug, 1),
		(assign, reg0, ":array"),
        (display_log_message, "@array[{reg0}] destroyed"),
    (try_end),
   ]), #


# script_cf_array_is_array
# Function: checks if something is an array
# fails if target is not an array
# Arguments:array id
# Return:
# Fail: if not an array
("cf_array_is_array",[
    (store_script_param_1, ":array"),
    (party_slot_eq, ":array", slot_array_signature, array_signature),
  ]), #

# script_array_get_owner
# Function: Gets the owner for an array, which affects automatic garbage collection
# Arguments:array id
# Return:reg0= owner
("array_get_owner",[
    # note: no type checking for now
    (store_script_param_1, ":array"),
    (party_get_slot, reg0, ":array", slot_array_owner),
   ]), #

# script_array_get_version
# Function: Gets the version for an array, which affects automatic garbage collection
# Arguments:array id
# Return:reg0= version
("array_get_version",[
    # note: no type checking for now
    (store_script_param_1, ":array"),
    (party_get_slot, reg0, ":array", slot_array_version),
  ]), #


# script_array_set_owner
# Function: Sets owner for an array, which affects automatic garbage collection
# Arguments:array id, owner(party) : 0 is a special value indicating that 
#     array should never be cleaned up.  Otherwise, if the owning party is no 
#     longer active, it will be cleaned up during garbage collection.
#     Setting to -1 explicitly will also make it clean up on next garbage collection
# Return:	
("array_set_owner",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":owner"),
    (try_begin),
        (call_script, "script_cf_array_is_array", ":array"),
        (party_set_slot, ":array", slot_array_owner, ":owner"),
    (try_end),
   ]), #


("array_clear",[
    (store_script_param_1, ":array"),
    (party_set_slot, ":array", slot_array_size, 0), # quick clear.  just set size to 0    
   ]), #

# script_array_get_size
# Function: gets array size
# Arguments:array id
# Return: reg0 = array size
("array_get_size",[
    (store_script_param_1, ":array"),
    (party_get_slot, reg0, ":array", slot_array_size),
   ]), #


# script_cf_array_get_element
# Function: can fail version which gets array element at position
# Arguments:array id, index
# Return: reg0 = element at index
# Fail: if index out of range
# Also see: script_array_get_element
("cf_array_get_element",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":index"),
    (party_get_slot, ":size", ":array", slot_array_size),
    (ge, ":index", 0),
    (gt, ":size", ":index"),
    (val_add, ":index", array_slot_offset), # add offset to get actual slot for element
    (party_get_slot, reg0, ":array", ":index"),    
  ]), #

# script_cf_array_set_element
# Function: can fail version which sets array element at position
# Arguments:array id, index, value
# Return:
# Fail: if index out of range
# Also see: script_array_set_element
("cf_array_set_element",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":index"),
    (store_script_param, ":value", 3),
    (party_get_slot, ":size", ":array", slot_array_size),
    (ge, ":index", 0),
    (gt, ":size", ":index"),
    (val_add, ":index", array_slot_offset), # add offset to get actual slot for element
    (party_set_slot, ":array", ":index", ":value"),
  ]), #


# script_array_get_element
# Function: non failing version which gets array element at position, no range checking
# Arguments:array id, index, default_value
# Return: reg0 = element at index if found, default value otherwise
# Also see: script_cf_array_get_element
("array_get_element",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":index"),
    (party_get_slot, ":size", ":array", slot_array_size),
    (try_begin),
        (ge, ":index", 0),
        (gt, ":size", ":index"),
        (val_add, ":index", array_slot_offset), # add offset to get actual slot for element
        (party_get_slot, reg0, ":array", ":index"),    
    (else_try),
        (store_script_param, reg0,3), # return default value        
    (try_end),
  ]), #

# script_array_set_element
# Function: non fail version which sets array element at position, and does nothing if index out of range
# Arguments:array id, index, value
# Return:
# Also see: script_cf_array_set_element
("array_set_element",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":index"),
    (store_script_param, ":value", 3),
    (try_begin),
        (party_get_slot, ":size", ":array", slot_array_size),
        (ge, ":index", 0),
        (gt, ":size", ":index"),
        (val_add, ":index", array_slot_offset), # add offset to get actual slot for element
        (party_set_slot, ":array", ":index", ":value"),
    (try_end),
  ]), #


# array_pushback
# Function: Inserts a value at the end of array
# Arguments:array id, value
# Return:
("array_pushback",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":value"),
    (party_get_slot, ":size", ":array", slot_array_size),    
    (store_add, ":slot_end", ":size", array_slot_offset),
    (party_set_slot, ":array", ":slot_end", ":value"),
    
    # update size  
    (val_add, ":size", 1),  
    (party_set_slot, ":array", slot_array_size, ":size"),
  ]), #

# array_pushfront
# Function: Inserts a value at the front of array #and removes the last value
# Arguments:array id, value
# Return:
("array_pushfront",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":value"),
    (party_get_slot, ":size", ":array", slot_array_size),    
    (val_sub, ":size",1),
	(call_script, "script_array_p_shift_range", ":array", 0, ":size", 1, ":value"), # shift all values right by 1 place, fill empty with value
    # update size  
    (val_add, ":size", 1),  
    (party_set_slot, ":array", slot_array_size, ":size"),
  ]), #


# array_popback
# Function: removes and returns the last element in array if it exists
# Arguments:array id
# Fail: if array is empty
# Return: reg0=value which was at the back of array
("cf_array_popback",[
    (store_script_param_1, ":array"),
    (party_get_slot, ":size", ":array", slot_array_size),    
    (ge, ":size", 0),
    (val_sub, ":size", 1),    
    (store_add, ":slot_back", ":size", array_slot_offset),
    (party_get_slot, reg0, ":array", ":slot_back"),    
    (party_set_slot, ":array", slot_array_size, ":size"),
  ]), #

# array_popfront
# Function: removes and returns the first element in array if it exists
# Arguments:array id
# Fail: if array is empty
# Return:
# Return: reg0=value which was at the front of array
("cf_array_popfront",[
    (store_script_param_1, ":array"),
    (party_get_slot, ":size", ":array", slot_array_size),    
    (ge, ":size", 0),

    (party_get_slot, ":value", ":array", slot_array_0),

    (call_script, "script_array_remove", ":array", 0), # remove element 0
    # update size  
    (val_sub, ":size",1),
    (party_set_slot, ":array", slot_array_size, ":size"),
    (assign, reg0, ":value"),
  ]), #


# script_cf_array_insert
# Function: Inserts a value at position (other values will be shifted backwards)
# Arguments:array id, index, value
# Return:
# Fail: if index out of range
("cf_array_insert",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":index"),
    (store_script_param, ":value", 3),
    (party_get_slot, ":size", ":array", slot_array_size),
    (ge, ":index", 0),
    (ge, ":size", ":index"),
    
    (call_script, "script_array_p_shift_range", ":array",":index", ":size", 1, ":value"),
    
    # update size  
    (val_add, ":size", 1),  
    (party_set_slot, ":array", slot_array_size, ":size"),
  ]), #

# script_cf_array_insert_n
# Function: Inserts n instances of a value at position (other values will be shifted backwards)
# Arguments:array id, index, value, n
# Return:
# Fail: if index out of range
("cf_array_insert_n",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":index"),
    (store_script_param, ":value", 3),
    (store_script_param, ":n", 4),
    (party_get_slot, ":size", ":array", slot_array_size),
    (ge, ":index", 0),
    (ge, ":n", 0),
    (ge, ":size", ":index"),    
    (call_script, "script_array_p_shift_range", ":array", ":index", ":size", ":n", ":value"),    
    # update size  
    (val_add, ":size", ":n"),  
    (party_set_slot, ":array", slot_array_size, ":size"),
  ]), #


# script_cf_array_remove
# Function: Removes a value at position (other values will be shifted forward)
# Arguments:array id, index
# Return:
# Fail: if index out of range
("cf_array_remove",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":index"),
    (party_get_slot, ":size", ":array", slot_array_size),
    (ge, ":index", 0),
    (gt, ":size", ":index"),
    (val_add, ":index", 1),    
    (call_script, "script_array_p_shift_range", ":array", ":index", ":size", -1, 0),
    
    # update size  
    (val_sub, ":size", 1),  
    (party_set_slot, ":array", slot_array_size, ":size"),
  ]), #

# script_cf_array_remove_n
# Function: Removes n values at position (other values will be shifted forward).  If end of array is reached before n elements are removed, it is stop there.
# Arguments:array id, index, n
# Return:
# Fail: if index out of range
("cf_array_remove_n",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":index"),
    (store_script_param, ":n", 3),
    (party_get_slot, ":size", ":array", slot_array_size),
    (ge, ":index", 0),
    (ge, ":n", 0),
    (gt, ":size", ":index"),    
    (val_add, ":index", ":n"),
    (store_sub, ":neg_n", 0, ":n"),
    (call_script, "script_array_p_shift_range",":array", ":index", ":size", ":neg_n", 0),    
    # update size  
    (val_sub, ":size", ":n"),  
    (party_set_slot, ":array", slot_array_size, ":size"),
  ]), #




# non-failing versions of insert and remove, which is similar to the can fail version, just don't do anything if index out of range.

# script_array_insert
# Function: Inserts a value at position (other values will be shifted backwards)
# Arguments:array id, index, value
# Return:
("array_insert",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":index"),
    (store_script_param, ":value", 3),
    (party_get_slot, ":size", ":array", slot_array_size),
    (try_begin),
        (ge, ":index", 0),
        (ge, ":size", ":index"),
        
        (call_script, "script_array_p_shift_range",":array", ":index", ":size", 1, ":value"),
        
        # update size  
        (val_add, ":size", 1),  
        (party_set_slot, ":array", slot_array_size, ":size"),
    (try_end),
  ]), #

# script_array_insert_n
# Function: Inserts n instances of a value at position (other values will be shifted backwards)
# Arguments:array id, index, value, n
# Return:
("array_insert_n",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":index"),
    (store_script_param, ":value", 3),
    (store_script_param, ":n", 4),
    (party_get_slot, ":size", ":array", slot_array_size),
    (try_begin),
        (ge, ":index", 0),
        (ge, ":n", 0),
        (ge, ":size", ":index"),    
        (call_script, "script_array_p_shift_range", ":array",":index", ":size", ":n", ":value"),    
        # update size  
        (val_add, ":size", ":n"),  
        (party_set_slot, ":array", slot_array_size, ":size"),
    (try_end),
  ]), #



# script_array_remove
# Function: Removes a value at position (other values will be shifted forward)
# Arguments:array id, index
# Return:
# Fail: if index out of range
("array_remove",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":index"),
    (party_get_slot, ":size", ":array", slot_array_size),
    (try_begin),
        (ge, ":index", 0),
        (gt, ":size", ":index"),
        (val_add, ":index", 1),    
        (call_script, "script_array_p_shift_range", ":array",":index", ":size", -1, 0),
        
        # update size  
        (val_sub, ":size", 1),  
        (party_set_slot, ":array", slot_array_size, ":size"),
    (try_end),
  ]), #
  
# script_array_remove_n
# Function: Removes n values at position (other values will be shifted forward)
# Arguments:array id, index, n
# Return:
# Fail: if index out of range
("array_remove_n",[
    (store_script_param_1, ":array"),
    (store_script_param_2, ":index"),
    (store_script_param, ":n", 3),
    (party_get_slot, ":size", ":array", slot_array_size),
    (try_begin),
        (ge, ":index", 0),
        (ge, ":n", 0),
        (gt, ":size", ":index"),    
        (val_add, ":index", ":n"),
        (store_sub, ":neg_n", 0, ":n"),
        (call_script, "script_array_p_shift_range",":array", ":index", ":size", ":neg_n", 0),    
        # update size  
        (val_sub, ":size", ":n"),  
        (party_set_slot, ":array", slot_array_size, ":size"),
    (try_end),
  ]), #


##### private scripts #####
# Private function not to be called by non-array scripts

# script_array_destroy_sub_arrays
# Caba'drin addition
# Function: called by array_destroy to recrusively destroy all sub-arrays of the calling array
#    preventing errors, etc, from garbage collection
# Arguments: array id
("array_destroy_sub_arrays", [
    (store_script_param_1, ":master_array"),
       
    (try_for_parties, ":array"),
		(call_script, "script_cf_array_is_array", ":array"),
		(call_script, "script_array_get_owner", ":array"),
		(eq, ":master_array", reg0),
		(call_script, "script_array_destroy", ":array"),
	(try_end),
   ]),

# script_array_p_shift_range
# Function: private function to shift range of values in position (start_idx, end_idx-1) right by n places. (n>0 means shift right, n<0 means shift lef, n=0 means no shift)
#   Note that this shift is done REGARDLESS of actual array size, as long as the indices do not go below 0.  If so, operations regarding those values will be ignored.
#   Spaces created by shifts will be filled with default_value
# Arguments: array id, start_idx, end_idx, shift_offset, default_value
# Fail: never
("array_p_shift_range",[
    (store_script_param, ":array", 1),
    (store_script_param, ":start_index", 2),
    (store_script_param, ":end_index", 3),
    (store_script_param, ":shift_offset", 4),
    (store_script_param, ":default_value", 5),
    
    (val_add, ":end_index",1),
    
    #debug start
	(try_begin),
		(eq, array_debug, 1),
		(assign, reg21, ":array"),
		(assign, reg22, ":start_index"),
		(assign, reg23, ":end_index"),
		(assign, reg24, ":shift_offset"),
		(assign, reg25, ":default_value"),
		(display_debug_message, "@array_p_shift_range array={reg21}, start_index={reg22}, end_index={reg23}, shift_offset={reg24}, default_value={reg25}"),
	(try_end),
    #debug end
    (store_add, ":dst_start_index", ":start_index", ":shift_offset"),
    (store_add, ":dst_end_index", ":end_index", ":shift_offset"),
    
    (try_begin),
        (gt, ":shift_offset", 0), # shifting right
        #(display_log_message, "@shift_offset>0"),
        (try_for_range_backwards, ":i", ":start_index", ":end_index"),
            #(assign, reg31, ":i"),                                  
            #(display_log_message, "@i={reg31}"),
            (store_add, ":slot_i", ":i", array_slot_offset),
            (party_get_slot, ":value", ":array", ":slot_i"), # value = A[i]
            (store_add, ":slot_dst_i", ":slot_i", ":shift_offset"),
            (party_set_slot, ":array", ":slot_dst_i", ":value"), # A[i + offset] = value
            (try_begin), # if position is blank left by shifting, fill in with default value
                (gt, ":dst_start_index", ":i"),
                (party_set_slot, ":array", ":slot_i", ":default_value"), # A[i] = default_value                    
            (try_end),                      
            #(assign, reg32, ":slot_i"),
            #(assign, reg34, ":slot_dst_i"),
            #(display_log_message, "@slot_i={reg32}"),
            #(display_log_message, "@slot_dst_i={reg34}"),
        (try_end),
    (else_try),
        (gt, 0, ":shift_offset"), # shifting left
        #(display_log_message, "@shift_offset<0"),
        (try_for_range, ":i", ":start_index", ":end_index"),
            (try_begin),
                (store_add, ":dst_i", ":i", array_slot_offset),
                (ge, ":dst_i", 0),
                
                (store_add, ":slot_i", ":i", array_slot_offset),
                (party_get_slot, ":value", ":array", ":slot_i"), # value = A[i]
                (store_add, ":slot_dst_i", ":slot_i", ":shift_offset"),
                (party_set_slot, ":array", ":slot_dst_i", ":value"), # A[i - offset] = value
                (try_begin), # if position is blank left by shifting, fill in with default value
                    (ge, ":i", ":dst_end_index"),
                    (party_set_slot, ":array", ":slot_i", ":default_value"), # A[i] = default_value                    
                (try_end),                                                            
            (try_end),        
        (try_end),
    (try_end),
]), #


] # scripts

from util_scripts import *
def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1127 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "scripts"
		orig_scripts = var_set[var_name_1]
		
		add_scripts(orig_scripts, scripts, True)
		
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)
	