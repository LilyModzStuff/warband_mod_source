from header_items import *
from header_troops import *
from ID_troops import *

from cstmmerge_constants import *
from cstm_troop_trees import *
from cstm_proficiency_requirements import cstm_proficiency_requirements

##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
##############################################################

assert (len(CUSTOM_TROOP_TREES) > 0), "There must be at least one troop tree defined in the CUSTOM_TROOP_TREES variable in cstmmerge_constants"
assert (len(CSTM_SKINS) > 1), "There must be at least two skins defined in the CSTM_SKINS variable in cstmmerge_constants"
	
cstm_troops_begin = "trp_cstm_custom_troop_%s_%d_0_0" % (CUSTOM_TROOP_TREES[0].id, CSTM_SKINS[0].id)
cstm_troops_end = "trp_cstm_custom_troops_end"

cstm_troop_tree_prefix = "trp_cstm_custom_troops_end"	# Gotta use some troop's name to store the prefix string (e.g. "Calradian"), any not having their name displayed for anything will do

next_free_troop_slot = NEW_TROOP_SLOTS_BEGIN
def next_troop_slots(num_slots):
	global next_free_troop_slot
	next_free_troop_slot += num_slots
	return next_free_troop_slot - num_slots

def next_troop_slot():
	return next_troop_slots(1)

## ITEM ARRAY SLOTS - FOR ARRAYS OF ITEMS AVAILABLE AS EQUIPMENT OPTIONS
cstm_slot_array_num_items = 0																			# Number of items in a particular array, e.g. Horses
cstm_slot_array_item_type = 1																			# The type of items stored in the array
cstm_slot_array_items_begin = 2																		# First slot that items begin being stored in

## PARTY SLOTS
cstm_slot_center_initial_lord = NEW_PARTY_SLOTS_BEGIN							# The lord initially given a fief; these lords will be added to the player's faction when using the start as king option

## TROOP SLOTS
cstm_slot_troop_dummy = next_troop_slot()													# The dummy troop used to store unsaved customisations (but also equipment more permanently as the non-hero troops will get theirs reset in each load)
cstm_slot_troop_custom_troop = next_troop_slot()									# The actual custom troop a dummy is for
cstm_slot_troop_base_troop = next_troop_slot()										# The troop that upgrades into this one
cstm_slot_troop_equipment_modified = next_troop_slot()						# Indicator of whether the equipment has been modified for a troop (equipment added to base troops will be added if not)

# The below are all used to calculate troop total inventory values in script_cstm_troop_get_inventory_value
cstm_slot_troop_armour_values_begin = next_troop_slots(4)					# The total sum value of all armours of a particular type in the troop's inventory
cstm_slot_troop_armour_counts_begin = next_troop_slots(4)					# The number of armours of a particular type in the troop's inventory
cstm_slot_troop_weapon_values = next_troop_slot()									# The total sum value of weapons in the troop's inventory (melee weapons and shields, but will also include ranged for troops without ranged weapons guaranteed)
cstm_slot_troop_weapon_count = next_troop_slot()									# The number of weapons in the troop's inventory (melee weapons and shields, but will also include ranged for troops without ranged weapons guaranteed)
cstm_slot_troop_ranged_values = next_troop_slot()									# The total sum value of ranged weapons in the troop's inventory (only used if troop has ranged weapons guaranteed)
cstm_slot_troop_ranged_count = next_troop_slot()									# The number of ranged weapons in the troop's inventory (only used if troop has ranged weapons guaranteed)
cstm_slot_troop_shield_values = next_troop_slot()									# The total sum value of shields in the troop's inventory
cstm_slot_troop_shield_count = next_troop_slot()									# The number of shields in the troop's inventory
cstm_slot_troop_horse_values = next_troop_slot()									# The total sum value of horses in the troop's inventory
cstm_slot_troop_horse_count = next_troop_slot()										# The number of horses in the troop's inventory

modifier_strings_begin = "str_cstm_imod_string_plain"

## STAT STRINGS
cstm_attribute_strings_begin = "str_cstm_ca_strength"
cstm_skill_strings_begin = "str_cstm_skill_trade"
cstm_proficiency_strings_begin = "str_cstm_wpt_one_handed_weapon"

## ITEM ARRAY IDS
def cstm_items_array_id(item_type):
	id = ""
	try:
		id = "cstm_items_" + cstm_item_type_strings[item_type].lower().replace(" ", "_")
	except:
		raise ValueError("Couldn't find an item array ID for item type " + str(item_type))
	return id

cstm_items_arrays_begin = "trp_" + cstm_items_array_id(itp_type_horse)
cstm_items_arrays_end = "trp_cstm_overlay_troops"