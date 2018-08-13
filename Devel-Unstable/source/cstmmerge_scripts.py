# -*- coding: cp1254 -*-
import collections
import math

from header_common import *
from header_operations import *
from header_items import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from header_presentations import *
from ID_items import *
from ID_animations import *

from cstm_header_scripts import *

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

new_scripts = [
	
	# script_cstm_troop_set_stats_to_default
	("cstm_troop_set_stats_to_default",
	[
		(store_script_param, ":troop", 1),
		
		(call_script, "script_cstm_troop_reset_stats", ":troop"),
	
		(troop_raise_attribute, ":troop", ca_strength, CSTM_STR_START),
		(troop_raise_attribute, ":troop", ca_agility, CSTM_AGI_START),
		(troop_raise_attribute, ":troop", ca_intelligence, CSTM_INT_START),
		(troop_raise_attribute, ":troop", ca_charisma, CSTM_CHA_START),
		
		(troop_get_type, ":gender", ":troop"),
		(try_begin),
			(eq, ":gender", 1),
			
			(troop_raise_attribute, ":troop", ca_agility, 1),
		(else_try),
			(troop_raise_attribute, ":troop", ca_strength, 1),
		(try_end),
		
		(try_for_range, ":proficiency", 0, 7),
			(troop_raise_proficiency_linear, ":troop", ":proficiency", CSTM_WP_LEVELS_START),
		(try_end),
		
		(troop_raise_skill, ":troop", skl_trade, 2),
		(troop_raise_skill, ":troop", skl_inventory_management, 2),
		(troop_raise_skill, ":troop", skl_prisoner_management, 1),
		(troop_raise_skill, ":troop", skl_leadership, 1),
		
		#(str_store_troop_name, s0, ":troop"),
		#(display_log_message, "@Setting {s0} stats to default"),
	]),
	
	# script_cstm_item_type_get_cost_modifier
	("cstm_item_type_get_cost_modifier",
	[
		(store_script_param, ":item_type", 1),
		(store_script_param, ":imod", 2),
		
		(assign, ":cost_modifier", 0),
		
		# Armour modifiers
		(try_begin),
			(is_between, ":item_type", itp_type_head_armor, itp_type_hand_armor + 1),
			
			(try_begin),
				(eq, ":imod", imod_lordly),
				(assign, ":cost_modifier", 1050),
			(else_try),
				(eq, ":imod", imod_reinforced),
				(assign, ":cost_modifier", 550),
			(else_try),
				(eq, ":imod", imod_hardened),
				(assign, ":cost_modifier", 290),
			(else_try),
				(eq, ":imod", imod_thick),
				(assign, ":cost_modifier", 160),
			(else_try),
				(eq, ":imod", imod_sturdy),
				(assign, ":cost_modifier", 70),
			(else_try),
				(eq, ":imod", imod_crude),
				(assign, ":cost_modifier", -17),
			(else_try),
				(eq, ":imod", imod_battered),
				(assign, ":cost_modifier", -25),
			(else_try),
				(eq, ":imod", imod_ragged),
				(assign, ":cost_modifier", -30),
			(else_try),
				(eq, ":imod", imod_rusty),
				(assign, ":cost_modifier", -45),
			(else_try),
				(eq, ":imod", imod_tattered),
				(assign, ":cost_modifier", -50),
			(else_try),
				(eq, ":imod", imod_cracked),
				(assign, ":cost_modifier", -50),
			(try_end),
		(else_try),
			(eq, ":item_type", itp_type_shield),
			
			(try_begin),
				(eq, ":imod", imod_reinforced),
				(assign, ":cost_modifier", 110),
			(else_try),
				(eq, ":imod", imod_thick),
				(assign, ":cost_modifier", 60),
			(else_try),
				(eq, ":imod", imod_battered),
				(assign, ":cost_modifier", -15),
			(else_try),
				(eq, ":imod", imod_cracked),
				(assign, ":cost_modifier", -40),
			(try_end),
		(else_try),
			(this_or_next|is_between, ":item_type", itp_type_one_handed_wpn, itp_type_polearm + 1),
			(is_between, ":item_type", itp_type_bow, itp_type_thrown + 1),
			
			(try_begin),
				(eq, ":imod", imod_masterwork),
				(assign, ":cost_modifier", 1650),
			(else_try),
				(eq, ":imod", imod_tempered),
				(assign, ":cost_modifier", 670),
			(else_try),
				(eq, ":imod", imod_strong),
				(assign, ":cost_modifier", 360),
			(else_try),
				(eq, ":imod", imod_balanced),
				(assign, ":cost_modifier", 250),
			(else_try),
				(eq, ":imod", imod_heavy),
				(assign, ":cost_modifier", 90),
			(else_try),
				(eq, ":imod", imod_chipped),
				(assign, ":cost_modifier", -28),
			(else_try),
				(eq, ":imod", imod_rusty),
				(assign, ":cost_modifier", -45),
			(else_try),
				(eq, ":imod", imod_bent),
				(assign, ":cost_modifier", -35),
			(else_try),
				(eq, ":imod", imod_cracked),
				(assign, ":cost_modifier", -50),
			(try_end),
		(else_try),
			(is_between, ":item_type", itp_type_arrows, itp_type_bolts + 1),
			
			(try_begin),
				(eq, ":imod", imod_large_bag),
				(assign, ":cost_modifier", 90),
			(else_try),
				(eq, ":imod", imod_bent),
				(assign, ":cost_modifier", -35),
			(try_end),
		(else_try),
			(eq, ":item_type", itp_type_horse),
			
			(try_begin),
				(eq, ":imod", imod_champion),
				(assign, ":cost_modifier", 1350),
			(else_try),
				(eq, ":imod", imod_spirited),
				(assign, ":cost_modifier", 550),
			(else_try),
				(eq, ":imod", imod_heavy),
				(assign, ":cost_modifier", 90),
			(else_try),
				(eq, ":imod", imod_stubborn),
				(assign, ":cost_modifier", -10),
			(else_try),
				(eq, ":imod", imod_swaybacked),
				(assign, ":cost_modifier", -40),
			(else_try),
				(eq, ":imod", imod_lame),
				(assign, ":cost_modifier", -60),
			(try_end),
		(try_end),
		
		(assign, reg0, ":cost_modifier"),
	]),
	
	# script_cstm_reset_lord_armies_in_player_faction
	("cstm_reset_lord_armies_in_player_faction",
	[
		(try_for_range, ":lord", lords_begin, lords_end),
			(store_faction_of_troop, ":faction", ":lord"),
			(eq, ":faction", "fac_player_supporters_faction"),
			
			#(str_store_troop_name, s0, ":lord"),
			#(display_message, "@Refilling {s0}'s army"),
			
			(troop_get_slot, ":lord_party", ":lord", slot_troop_leaded_party),
			(gt, ":lord_party", 0),
			
			(party_clear, ":lord_party"),
			(party_add_leader, ":lord_party", ":lord"),
			
			(troop_set_slot, ":lord", slot_troop_wealth, 9000),
			(assign, ":num_tries", 30),

			(try_for_range, ":unused", 0, ":num_tries"),
				(call_script, "script_hire_men_to_kingdom_hero_party", ":lord"),
			(try_end),
			
			(troop_get_slot, ":renown", ":lord", slot_troop_renown),
			(store_div, ":xp_rounds", ":renown", 100),
			(try_for_range, ":unused", 0, ":xp_rounds"),
				(call_script, "script_upgrade_hero_party", ":lord_party", 4000),
			(try_end),
		(try_end),
	]),
	
	# script_cstm_reset_garrisons_in_player_faction
	("cstm_reset_garrisons_in_player_faction",
	[
		(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":faction", ":center_no"),
			(eq, ":faction", "fac_player_supporters_faction"),
			
			(party_clear, ":center_no"),
			
			(assign, ":garrison_strength", 15), 
			(try_begin),
				(party_slot_eq, ":center_no", slot_party_type, spt_town),
				(assign, ":garrison_strength", 40), 
			(try_end),
			(try_for_range, ":unused", 0, ":garrison_strength"),
				(call_script, "script_cf_reinforce_party", ":center_no"),
			(try_end),
			
			(store_div, ":xp_rounds", ":garrison_strength", 5),
			(val_add, ":xp_rounds", 2),

			(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),                

			(try_begin), #hard
				(eq, ":reduce_campaign_ai", 0),
				(assign, ":xp_addition_for_centers", 7500),
			(else_try), #moderate
				(eq, ":reduce_campaign_ai", 1),
				(assign, ":xp_addition_for_centers", 5000),
			(else_try), #easy
				(eq, ":reduce_campaign_ai", 2),
				(assign, ":xp_addition_for_centers", 2500),
			(try_end),

			(try_for_range, ":unused", 0, ":xp_rounds"),          
				(party_upgrade_with_xp, ":center_no", ":xp_addition_for_centers", 0),
			(try_end),
		(try_end),
	]),
	
	## If you want to add any extra items to the equipment options, do so by making the condition true below
	# script_cstm_cf_item_is_eligible_equipment_option
	("cstm_cf_item_is_eligible_equipment_option",
	[
		(store_script_param, ":item", 1),
		
		(assign, ":item_eligible", 0),
		(try_begin),
			(item_has_property, ":item", itp_merchandise),
			(store_item_value, ":value", ":item"),
			(gt, ":value", 0),
			
			(assign, ":item_eligible", 1),
		(else_try),
			(this_or_next|eq, ":item", "itm_strange_armor"),
			(this_or_next|eq, ":item", "itm_strange_boots"),
			(this_or_next|eq, ":item", "itm_strange_helmet"),
			(this_or_next|eq, ":item", "itm_strange_sword"),
			(this_or_next|eq, ":item", "itm_strange_great_sword"),
			(eq, ":item", "itm_strange_short_sword"),
			
			(assign, ":item_eligible", 1),
		(else_try),
			(eq, 0, 1),	## CHANGE THIS
			
			(assign, ":item_eligible", 1),
		(try_end),
		
		(eq, ":item_eligible", 1),
	]),
	
]

def modmerge(var_set):
	try:
		var_name_1 = "scripts"
		orig_scripts = var_set[var_name_1]
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)
	
	orig_scripts.extend(new_scripts)
	
	scripts = collections.OrderedDict()
	for script_tuple in orig_scripts:
		scripts[script_tuple[0]] = Script(*script_tuple)
	
	# Add 150 to party size if player is king (may want to remove this if merging into a mod that already accounts for this)
	scripts["game_get_party_companion_limit"].operations[-1:-1] = [
		(try_begin),
			(eq, "$players_kingdom", "fac_player_supporters_faction"),
			(faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
			
			(val_add, reg0, 150),
		(try_end),
	]
	#print scripts["game_get_party_companion_limit"].operations
	
	# To fully avoid any local variable name clashes, use registers for adding operations to existing scripts (being careful not to use ones that may be overwritten between operations, especially by scripts)
	current_faction = reg0
	original_faction = reg1
	culture = reg2
	curr_center = reg3
	
	# Extend give center to faction script to change the culture if giving to player faction (enabling recruitment of custom troops)
	# If local variable names for script params are changed from Native for any reason, the below should still get them
	center_var = [operation[1] for operation in scripts["give_center_to_faction_aux"].operations if type(operation) == tuple and operation[0] == store_script_param_1][-1]
	faction_var = [operation[1] for operation in scripts["give_center_to_faction_aux"].operations if type(operation) == tuple and operation[0] == store_script_param_2][-1]
	index = scripts["give_center_to_faction_aux"].operations.index([operation for operation in scripts["give_center_to_faction_aux"].operations if type(operation) == tuple and operation[0] == store_script_param_2][-1])
	scripts["give_center_to_faction_aux"].operations[index+1:index+1] = [
		(try_begin),
			(eq, faction_var, "fac_player_supporters_faction"),
			(ge, "$cstm_troops_begin", cstm_troops_begin),
			
			#(str_store_party_name, s0, center_var),
			#(display_message, "@Changing {s0} culture to that of player faction"),
			(call_script, "script_cstm_center_set_culture", center_var, "fac_culture_player"),
		(else_try),
			(store_faction_of_party, current_faction, center_var),
			(eq, current_faction, "fac_player_supporters_faction"),
			
			(party_get_slot, original_faction, center_var, slot_center_original_faction),
			(faction_get_slot, culture, original_faction, slot_faction_culture),
			(call_script, "script_cstm_center_set_culture", center_var, culture),
		(try_end),
	]
	
	# Similarly extend change troop faction script to change the culture of any fiefs taken with the lord to the player faction (enabling recruitment of custom troops)
	# If local variable names for script params are changed from Native for any reason, the below should still get them
	troop_var = [operation[1] for operation in scripts["change_troop_faction"].operations if type(operation) == tuple and operation[0] == store_script_param_1][-1]
	faction_var = [operation[1] for operation in scripts["change_troop_faction"].operations if type(operation) == tuple and operation[0] == store_script_param_2][-1]
	index = scripts["change_troop_faction"].operations.index([operation for operation in scripts["change_troop_faction"].operations if type(operation) == tuple and operation[0] == store_script_param_2][-1])
	scripts["change_troop_faction"].operations[index+1:index+1] = [
		(try_for_range, curr_center, centers_begin, centers_end),
			(party_slot_eq, curr_center, slot_town_lord, troop_var),
			
			(try_begin),
				(eq, faction_var, "fac_player_supporters_faction"),
				
				(call_script, "script_cstm_center_set_culture", curr_center, "fac_culture_player"),
			(else_try),
				(store_faction_of_party, current_faction, curr_center),
				(eq, current_faction, "fac_player_supporters_faction"),
				
				(party_get_slot, original_faction, curr_center, slot_center_original_faction),
				(faction_get_slot, culture, original_faction, slot_faction_culture),
				(call_script, "script_cstm_center_set_culture", curr_center, culture),
			(try_end),
		(try_end),
	]
	
	faction_var = [operation[1] for operation in scripts["cf_reinforce_party"].operations if type(operation) == tuple and operation[0] == store_faction_of_party][-1]
	index = scripts["cf_reinforce_party"].operations.index((eq, faction_var, "fac_player_supporters_faction")) + 1
	if index > 0:
		scripts["cf_reinforce_party"].operations[index:index] = [
			(eq, 0, 1),
		]
	
	party_type_var = [operation[1] for operation in scripts["cf_reinforce_party"].operations if type(operation) == tuple and operation[0] == party_get_slot and operation[3] == slot_party_type][-1]
	index = scripts["cf_reinforce_party"].operations.index((eq, party_type_var, spt_kingdom_hero_party)) + 1
	if index > 0:
		scripts["cf_reinforce_party"].operations[index:index] = [
			(neq, faction_var, "fac_player_supporters_faction"),
		]
	#print "\n".join([str(x) for x in scripts["cf_reinforce_party"].operations])
	
	del orig_scripts[:]
	for script_id in scripts:
		orig_scripts.append(scripts[script_id].convert_to_tuple())