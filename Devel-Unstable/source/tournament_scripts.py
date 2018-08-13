# Tournament Play Enhancements (1.2) by Windyplains
# Released 9/22/2011

from header_common import *
from header_operations import *
from module_constants import *
from header_mission_templates import *
from header_items import *
from header_presentations import *  # (COMPANIONS OVERSEER MOD)
from companions_constants import *  # (COMPANIONS OVERSEER MOD)

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

scripts = [
## TOURNAMENT PLAY ENHANCEMENTS (1.0) begin - Windyplains
# script_TPE_UPDATE_PRESENTATION
  ("tpe_update_presentation",
    [
		# Set the initial checkbox positions
		# OBJ 4 initialize
		(troop_get_slot, ":status", "$g_wp_tpe_troop", slot_troop_tournament_lance),
		(overlay_set_val, "$g_presentation_obj_4", ":status"),
		# OBJ 5 initialize
		(troop_get_slot, ":status", "$g_wp_tpe_troop", slot_troop_tournament_bow),
		(overlay_set_val, "$g_presentation_obj_5", ":status"),
		# OBJ 6 initialize
		(troop_get_slot, ":status", "$g_wp_tpe_troop", slot_troop_tournament_onehand),
		(overlay_set_val, "$g_presentation_obj_6", ":status"),
		# OBJ 7 initialize
		(troop_get_slot, ":status", "$g_wp_tpe_troop", slot_troop_tournament_twohand),
		(overlay_set_val, "$g_presentation_obj_7", ":status"),
		# OBJ 8 initialize
		(troop_get_slot, ":status", "$g_wp_tpe_troop", slot_troop_tournament_crossbow),
		(overlay_set_val, "$g_presentation_obj_8", ":status"),
		# OBJ 9 initialize
		(troop_get_slot, ":status", "$g_wp_tpe_troop", slot_troop_tournament_throwing),
		(overlay_set_val, "$g_presentation_obj_9", ":status"),
		# OBJ 10 initialize
		(troop_get_slot, ":status", "$g_wp_tpe_troop", slot_troop_tournament_polearm),
		(overlay_set_val, "$g_presentation_obj_10", ":status"),
		# OBJ 11 initialize
		(troop_get_slot, ":status", "$g_wp_tpe_troop", slot_troop_tournament_horse),
		(overlay_set_val, "$g_presentation_obj_11", ":status"),
		# OBJ 12 initialize
		(troop_get_slot, ":status", "$g_wp_tpe_troop", slot_troop_tournament_enhanced_horse),
		(overlay_set_val, "$g_presentation_obj_12", ":status"),
		(try_begin),
			(troop_slot_eq, "$g_wp_tpe_troop", slot_troop_tournament_horse, 0),  # Checks if the enhanced horse option should be displayed or not.
			(overlay_set_display, "$g_presentation_obj_12", 0),
		(else_try),
			(overlay_set_display, "$g_presentation_obj_12", 1),
		(try_end),
		# OBJ 13 initialize
		(troop_get_slot, ":status", "$g_wp_tpe_troop", slot_troop_tournament_enhanced_armor),
		(overlay_set_val, "$g_presentation_obj_13", ":status"),
		# OBJ 14 initialize
		(troop_get_slot, ":status", "$g_wp_tpe_troop", slot_troop_tournament_enhanced_weapons),
		(overlay_set_val, "$g_presentation_obj_14", ":status"),
		# OBJ 15 initialize
		(troop_get_slot, ":status", "$g_wp_tpe_troop", slot_troop_tournament_enhanced_shield),
		(overlay_set_val, "$g_presentation_obj_15", ":status"),
		(try_begin),                                                            # Checks if the enhanced shield option should be displayed or not.
			(troop_slot_eq, "$g_wp_tpe_troop", slot_troop_tournament_onehand, 0),    # Is the player using the 1H + Shield option?
			(troop_slot_eq, "$g_wp_tpe_troop", slot_troop_tournament_throwing, 0),   # Is the player using the Javelin + Shield option?
			(troop_slot_eq, "$g_wp_tpe_troop", slot_troop_tournament_lance, 0),      # Is the player using the Lance + Shield option?
			(overlay_set_display, "$g_presentation_obj_15", 0),
		(else_try),
			(overlay_set_display, "$g_presentation_obj_15", 1),
		(try_end),
		
		##### PORTRAIT CODE begin
        # OBJ 22 - Character Portrait
		(create_mesh_overlay_with_tableau_material, "$g_presentation_obj_22", -1, "tableau_troop_note_mesh", "$g_wp_tpe_troop"),
        (position_set_x, pos2, 165),
        (position_set_y, pos2, 390),
        (overlay_set_position, "$g_presentation_obj_22", pos2),
        (position_set_x, pos2, 800), #1150
        (position_set_y, pos2, 800), #1150
        (overlay_set_size, "$g_presentation_obj_22", pos2),
		##### PORTRAIT CODE end
		
		# OBJ 24 initialize
		(troop_get_slot, ":status", "$g_wp_tpe_troop", slot_troop_tournament_selections),
		(store_sub, reg0, 3, ":status"),
		(overlay_set_text, "$g_presentation_obj_24", "@You have {reg0} option(s) remaining."),
		# OBJ 36 initialize
		(overlay_set_val, "$g_presentation_obj_36", "$g_wp_tpe_renown_scaling"),
		# OBJ 37 initialize
		(try_begin),
			(troop_slot_eq, "$g_wp_tpe_troop", slot_troop_tournament_always_randomize, 0),
			(overlay_set_val, "$g_presentation_obj_37", 1),
		(else_try),
			(overlay_set_val, "$g_presentation_obj_37", 0),
		(try_end),
		# OBJ 38 initialize
		(troop_get_slot, ":status", "$g_wp_tpe_troop", slot_troop_tournament_never_spawn),
		(overlay_set_val, "$g_presentation_obj_38", ":status"),
		
	]
  ),
  
# script_TPE_EQUIP_AGENT
# Input: arg1 = troop
  ("tpe_equip_troop",
    [	
		(store_script_param, ":troop", 1),
		
	    # Clear any previous choices
		(call_script, "script_tpe_clear_selections", ":troop"),
		
		# Pick a melee weapon
		(store_random_in_range, ":coin_flip", 1, 4),
		(try_begin),
			(eq, ":coin_flip", 1),
			(troop_set_slot, ":troop", slot_troop_tournament_polearm, 1),
		(else_try),
			(eq, ":coin_flip", 2),
			(troop_set_slot, ":troop", slot_troop_tournament_twohand, 1),
		(else_try),
			(troop_set_slot, ":troop", slot_troop_tournament_onehand, 1),
		(try_end),
		
		# Auxiliary weapon or primary enhancement choice
		(store_random_in_range, ":coin_flip", 1, 11),
		(try_begin),
			(is_between, ":coin_flip", 1, 3),
			(troop_set_slot, ":troop", slot_troop_tournament_lance, 1),
		(else_try),
			(is_between, ":coin_flip", 3, 5),
			(troop_set_slot, ":troop", slot_troop_tournament_bow, 1),
		(else_try),
			(is_between, ":coin_flip", 5, 7),
			(troop_set_slot, ":troop", slot_troop_tournament_crossbow, 1),
		(else_try),
			(is_between, ":coin_flip", 7, 9),
			(troop_set_slot, ":troop", slot_troop_tournament_throwing, 1),
		(else_try),
			(troop_set_slot, ":troop", slot_troop_tournament_horse, 1),
		(try_end),
		
		# Last choice for additional enhancement
		(store_random_in_range, ":coin_flip", 1, 10),
		(try_begin),
			(is_between, ":coin_flip", 1, 4),
			(try_begin),
				(troop_get_slot, ":horse_check", ":troop", slot_troop_tournament_horse),
				(eq, ":horse_check", 0),
				(troop_set_slot, ":troop", slot_troop_tournament_horse, 1),
				(assign, ":last_choice", slot_troop_tournament_horse),
			(else_try),
				(troop_set_slot, ":troop", slot_troop_tournament_enhanced_horse, 1),
				(assign, ":last_choice", slot_troop_tournament_enhanced_horse),
			(try_end),
		(else_try),
			(is_between, ":coin_flip", 4, 6),
			(troop_set_slot, ":troop", slot_troop_tournament_enhanced_weapons, 1),
			(assign, ":last_choice", slot_troop_tournament_enhanced_weapons),
		(else_try),
			(eq, ":coin_flip", 6),
			(this_or_next|troop_slot_eq, ":troop", slot_troop_tournament_throwing, 1),
			(this_or_next|troop_slot_eq, ":troop", slot_troop_tournament_lance, 1),
			(troop_slot_eq, ":troop", slot_troop_tournament_onehand, 1),
			(troop_set_slot, ":troop", slot_troop_tournament_enhanced_shield, 1),
			(assign, ":last_choice", slot_troop_tournament_enhanced_shield),
		(else_try),
			(troop_set_slot, ":troop", slot_troop_tournament_enhanced_armor, 1),
			(assign, ":last_choice", slot_troop_tournament_enhanced_armor),
		(try_end),
		
		(try_begin), # Checks to see if a person has a lance without a horse.
			(troop_slot_eq, ":troop", slot_troop_tournament_lance, 1),
			(troop_slot_eq, ":troop", slot_troop_tournament_horse, 0),
			(troop_set_slot, ":troop", slot_troop_tournament_horse, 1),
			(troop_set_slot, ":troop", ":last_choice", 0),
		(try_end),
		
		(troop_set_slot, ":troop", slot_troop_tournament_selections, 3),
	]
  ),
  
 
# script_TPE_WEAPON_LOGIC
# Input: arg1 = troop
  ("tpe_weapon_logic",
    [	
		(store_script_param, ":troop", 1),
		
		(assign, ":tally_weapons", 0),
		(assign, ":tally_weapon_slots", 0),
		(assign, ":melee_weapon_check", 0),
		
		(try_for_range, ":weapon_choice", slot_troop_tournament_begin, slot_troop_tournament_horse), # horse is first enhancement after weapons
			(troop_get_slot, ":status", ":troop", ":weapon_choice"),
			(eq, ":status", 1),
			(val_add, ":tally_weapons", 1),
			(try_begin),
				(this_or_next|eq, ":weapon_choice", slot_troop_tournament_onehand),
				(this_or_next|eq, ":weapon_choice", slot_troop_tournament_twohand),
				(eq, ":weapon_choice", slot_troop_tournament_polearm),
				(assign, ":melee_weapon_check", 1),
			(try_end),
			(try_begin),
				(eq, ":weapon_choice", slot_troop_tournament_lance),
				(val_add, ":tally_weapon_slots", 1),
			(else_try),
				(eq, ":weapon_choice", slot_troop_tournament_bow),
				(val_add, ":tally_weapon_slots", 2),
			(else_try),
				(eq, ":weapon_choice", slot_troop_tournament_onehand),
				(val_add, ":tally_weapon_slots", 1),
			(else_try),
				(eq, ":weapon_choice", slot_troop_tournament_twohand),
				(val_add, ":tally_weapon_slots", 1),
			(else_try),
				(eq, ":weapon_choice", slot_troop_tournament_throwing),
				(val_add, ":tally_weapon_slots", 1),
			(else_try),
				(eq, ":weapon_choice", slot_troop_tournament_crossbow),
				(val_add, ":tally_weapon_slots", 2),
			(else_try),
				(eq, ":weapon_choice", slot_troop_tournament_polearm),
				(val_add, ":tally_weapon_slots", 1),
			(try_end),
		(try_end),
		
		# Make sure we only count 1 shield.
		(assign, ":tally_shields", 0),
		(assign, ":add_shield", 0),
		(troop_get_slot, ":add_shield", ":troop", slot_troop_tournament_lance),
		(val_add, ":tally_shields",  ":add_shield"),
		(troop_get_slot, ":add_shield", ":troop", slot_troop_tournament_onehand),
		(val_add, ":tally_shields",  ":add_shield"),
		(troop_get_slot, ":add_shield", ":troop", slot_troop_tournament_throwing),
		(val_add, ":tally_shields",  ":add_shield"),
		(val_min, ":tally_shields", 1),
		(val_add, ":tally_weapon_slots", ":tally_shields"),
			
		(try_begin), # Check to see if you have any weapons selected.
			(eq, ":tally_weapons", 0),
			(overlay_set_text, "$g_presentation_obj_25", "@You have no weapons selected."),
		(else_try), # Check to see if you've exceeded four weapon slots.
			(gt, ":tally_weapon_slots", 4),
			(overlay_set_text, "$g_presentation_obj_25", "@You currently have selected more than four weapon spots."),
		(else_try), # Check to see if you have any melee weapons.
			(neq, ":melee_weapon_check", 1),
			(overlay_set_text, "$g_presentation_obj_25", "@You currently have no melee weapon selected."),
		(else_try),
			(overlay_set_text, "$g_presentation_obj_25", "@Your weapon selection is adequate."),
		(try_end),
		
		(try_begin),
			(eq, wp_tpe_debug, 1),
			(assign, reg0, ":tally_weapons"),
			(assign, reg1, ":tally_weapon_slots"),
			(assign, reg2, ":melee_weapon_check"),
			(assign, reg3, ":tally_shields"),
			(display_message, "@DEBUG (TPE Weapon Logic): You have {reg1} weapon slots ({reg3} shield) used to support {reg0} weapons.  Melee weapon check: {reg2}"),
		(try_end),
	]
  ),

# script_TPE_SET_OPTION
# Input: arg1 = troop, arg2 = slot, arg3 = value, arg4 = object
  ("tpe_set_option",
    [
		(store_script_param, ":troop", 1),
		(store_script_param, ":option_slot", 2),
		(store_script_param, ":new_value", 3),
		(store_script_param, ":obj_option", 4),
		
		(troop_get_slot, ":old_value", ":troop", ":option_slot"),
		(assign, ":allow_remove", 0),
		(assign, ":allow_add", 0),
		(troop_get_slot, ":total_options", ":troop", slot_troop_tournament_selections),
		
		(try_begin),                                 # Too many options to add another.
			(eq, ":new_value", 1),
			(this_or_next|ge, ":total_options", 3),
			(lt, ":total_options", 0),
			(display_message, "@You already have three options selected."),
			(overlay_set_val, ":obj_option", ":old_value"),    # Prevents check being changed if invalid.  Display purpose only.
		(else_try),                                  # Allow option to be unchecked.
			(eq, ":new_value", 0),
			(eq, ":total_options", 3),
			(assign, ":allow_remove", 1),
			(val_sub, ":total_options", 1),
			(troop_set_slot, ":troop", slot_troop_tournament_selections, ":total_options"),
			(troop_set_slot, ":troop", ":option_slot", ":new_value"),
		(else_try),                                  # Allow option to be unchecked or checked.
			(lt, ":total_options", 3),
			(assign, ":allow_add", 1),
			(try_begin),
				(eq, ":new_value", 1),
				(val_add, ":total_options", 1),
			(else_try),
				(eq, ":new_value", 0),
				(val_sub, ":total_options", 1),
			(try_end),
			(troop_set_slot, ":troop", ":option_slot", ":new_value"),
			(troop_set_slot, ":troop", slot_troop_tournament_selections, ":total_options"),
		(try_end),
		
		(try_begin),
			(this_or_next|eq, ":allow_remove", 1),
			(eq, ":allow_add", 1),
			
			## CONDITIONAL CHECKBOXES begin
			(assign, ":remove_option", 0),   # This will toggle to 1 if a conditional checkbox option is removed due to a requirement being unselected.
			(assign, ":add_option", 0),      # This will toggle to 1 if a conditional checkbox option is added due to a requirement being selected.
		
			# Enhanced Horse
			(try_begin),
				(eq, ":option_slot", slot_troop_tournament_horse),
				(assign, ":conditional_obj", "$g_presentation_obj_12"), # Enhanced Horse - OBJ #12
				(assign, ":conditional_slot", slot_troop_tournament_enhanced_horse),
				(try_begin),
					(eq, ":new_value", 0),
					(assign, ":remove_option", 1),
				(else_try),
					(assign, ":add_option", 1),
				(try_end),
			(try_end),
			
			# Enhanced Shield
			(try_begin),
				(this_or_next|eq, ":option_slot", slot_troop_tournament_onehand),
				(this_or_next|eq, ":option_slot", slot_troop_tournament_throwing),
				(eq, ":option_slot", slot_troop_tournament_lance),
				(assign, ":conditional_obj", "$g_presentation_obj_15"), # Enhanced Shield - OBJ #15
				(assign, ":conditional_slot", slot_troop_tournament_enhanced_shield),
				(try_begin),
					(eq, ":new_value", 1),
					(assign, ":add_option", 1),
				(else_try),
					(troop_slot_eq, ":troop", slot_troop_tournament_onehand, 0),
					(troop_slot_eq, ":troop", slot_troop_tournament_throwing, 0),
					(troop_slot_eq, ":troop", slot_troop_tournament_lance, 0),
					(assign, ":remove_option", 1),
				(try_end),
			(try_end),
			
			# Add or remove option as needed.
			(try_begin),
				(eq, ":remove_option", 1), # Remove options that have lost their requirements
				(troop_get_slot, ":status", ":troop", ":conditional_slot"),
				(try_begin),
					(eq, ":status", 1),                                  # Is the conditional item even selected?
					(troop_set_slot, ":troop", ":conditional_slot", 0),  # Change the conditional option to unselected.
					(val_sub, ":total_options", 1),                      # Make sure you get that option back as well.
					(troop_set_slot, ":troop", slot_troop_tournament_selections, ":total_options"),
					(overlay_set_val, ":conditional_obj", ":status"),    # Update the display for the conditional option.
				(try_end),
				(overlay_set_display, ":conditional_obj", 0),            # Disables the lost option.
				(assign, ":remove_option", 0),
			(else_try),
				(eq, ":add_option", 1), # Adds options that have met their requirements
				(troop_get_slot, ":status", ":troop", ":conditional_slot"),  # Make sure it isn't already available & selected.
				(overlay_set_val, ":conditional_obj", ":status"),            # Set it to whatever it was stored as.
				(overlay_set_display, ":conditional_obj", 1),                # Displays the option.
				(assign, ":add_option", 0),
			(try_end),
			## CONDITIONAL CHECKBOXES end
		(try_end),
		
		# Set to randomize or remove based on options taken.
		(try_begin),
			(troop_slot_ge, ":troop", slot_troop_tournament_selections, 1),
			(troop_set_slot, ":troop", slot_troop_tournament_always_randomize, 1),
		(else_try),
			(troop_set_slot, ":troop", slot_troop_tournament_always_randomize, 0),
		(try_end),
		
		# Update display of options remaining.
		(call_script, "script_tpe_update_presentation"),
    ]
  ),

# script_tpe_clear_selections (blanks out troop template choices)
# Input: arg1 = troop
# Output: none
  ("tpe_clear_selections",
    [
		(store_script_param, ":troop_id", 1),
		(try_for_range, ":selection", slot_troop_tournament_begin, slot_troop_tournament_end), # Clear out any previously selected options.
			(troop_set_slot, ":troop_id", ":selection", 0),
		(try_end),
		(troop_set_slot, ":troop_id", slot_troop_tournament_selections, 0),
	]),
	
# script_tpe_set_items_for_tournament
# Input: 
# Output: none (sets mt_arena_melee_fight items)
  ("tpe_set_items_for_tournament",
    [
		(store_script_param, ":troop_id", 1),
		(store_script_param, ":troop_team", 2),
		(store_script_param, ":troop_entry", 3),
		(mission_tpl_entry_clear_override_items, "mt_arena_melee_fight", ":troop_entry"),
			
		(try_begin),
			(eq, wp_tpe_debug, 1),
			(str_store_troop_name, s1, ":troop_id"),
			(assign, reg0, ":troop_team"),
			(assign, reg1, ":troop_entry"),
			(display_message, "@DEBUG (TPE): {s1} is on team {reg0} and should load at entry {reg1}."),
		(try_end),
			
		# Do they have any gear arranged for them?
		(try_begin),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_always_randomize, 0),   # checks for preset equipment settings.
			(call_script, "script_tpe_equip_troop", ":troop_id"),                      # gears up the troop.
		(try_end),
			
		(str_clear, s1),
			
		# Do they get a horse?
           (try_begin),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_enhanced_horse, 1),
			(assign, ":team_horse", wp_tpe_enhanced_horse),
			#(val_add, ":team_horse", ":troop_team"), TESTING - Commented since I don't have different colored warhorses yet.
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", ":team_horse"),
			(str_store_string, s1, "@{s1} enhanced horse (+2),"), # debugging
		(else_try),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_horse, 1),
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_normal_horse),
			(str_store_string, s1, "@{s1} horse (+1),"), # debugging
		(try_end),
			
		# Do they have enhanced armor?
		(try_begin),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_enhanced_armor, 1),
			(assign, ":team_armor", wp_tpe_enhanced_armor),
			(val_add, ":team_armor", ":troop_team"),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", ":team_armor"),
			(str_store_string, s1, "@{s1} enhanced armor (+1),"), # debugging
			(assign, ":team_helmet", wp_tpe_enhanced_helmet),
			(val_add, ":team_helmet", ":troop_team"),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", ":team_helmet"),
			(str_store_string, s1, "@{s1} enhanced helmet,"), # debugging
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_enhanced_boots),
			(str_store_string, s1, "@{s1} enhanced boots,"), # debugging
		(else_try),
			(assign, ":team_armor", wp_tpe_normal_armor),
			(val_add, ":team_armor", ":troop_team"),
			(str_store_string, s1, "@{s1} armor,"), # debugging
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", ":team_armor"),
			# (assign, ":team_helmet", wp_tpe_normal_helmet),  # Section commented out to prevent normal armor having a helm.
			# (val_add, ":team_helmet", ":troop_team"),
			# (str_store_string, s1, "@{s1} helmet,"), # debugging
			# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", ":team_helmet"),
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_normal_boots),
			(str_store_string, s1, "@{s1} boots,"), # debugging
		(try_end),
			
		# Do they have an enhanced shield?
		(try_begin),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_enhanced_shield, 1),
			(assign, ":team_armor", wp_tpe_enhanced_shield),
			(val_add, ":team_armor", ":troop_team"),
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", ":team_armor"),
			(str_store_string, s1, "@{s1} enhanced shield (+1),"), # debugging
		(else_try),
			(this_or_next|troop_slot_eq, ":troop_id", slot_troop_tournament_lance, 1),
			(this_or_next|troop_slot_eq, ":troop_id", slot_troop_tournament_onehand, 1),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_throwing, 1),
			(assign, ":team_armor", wp_tpe_normal_shield),
			(val_add, ":team_armor", ":troop_team"),
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", ":team_armor"),
			(str_store_string, s1, "@{s1} shield,"), # debugging
		(try_end),
			
		# Lances
		(try_begin),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_lance, 1),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_enhanced_weapons, 1),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_enhanced_lance),
			(str_store_string, s1, "@{s1} enhanced lance (+2),"), # debugging
		(else_try),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_lance, 1),
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_normal_lance),
			(str_store_string, s1, "@{s1} lance (+1),"), # debugging
		(try_end),
			
		# Bows
		(try_begin),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_bow, 1),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_enhanced_weapons, 1),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_enhanced_bow),
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", "itm_practice_arrows"),
			(str_store_string, s1, "@{s1} enhanced bow (+2),"), # debugging
		(else_try),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_bow, 1),
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_normal_bow),
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", "itm_practice_arrows"),
			(str_store_string, s1, "@{s1} bow (+1),"), # debugging
		(try_end),
			
		# Single handed weapons
		(try_begin),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_onehand, 1),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_enhanced_weapons, 1),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_enhanced_sword),
			(str_store_string, s1, "@{s1} enhanced sword (+2),"), # debugging
		(else_try),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_onehand, 1),
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_normal_sword),
			(str_store_string, s1, "@{s1} sword (+1),"), # debugging
		(try_end),
			
		# Two handed weapons
		(try_begin),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_twohand, 1),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_enhanced_weapons, 1),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_enhanced_greatsword),
			(str_store_string, s1, "@{s1} enhanced greatsword (+2),"), # debugging
		(else_try),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_twohand, 1),
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_normal_greatsword),
			(str_store_string, s1, "@{s1} greatsword (+1),"), # debugging
		(try_end),
			
		# Crossbows
		(try_begin),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_crossbow, 1),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_enhanced_weapons, 1),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_enhanced_crossbow),
			(str_store_string, s1, "@{s1} enhanced crossbow (+2),"), # debugging
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", "itm_practice_bolts"),
		(else_try),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_crossbow, 1),
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_normal_crossbow),
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", "itm_practice_bolts"),
			(str_store_string, s1, "@{s1} crossbow (+1),"), # debugging
		(try_end),
			
		# Thown Weapons
		(try_begin),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_throwing, 1),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_enhanced_weapons, 1),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_enhanced_javelin),
			(str_store_string, s1, "@{s1} enhanced javelins (+2),"), # debugging
		(else_try),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_throwing, 1),
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_normal_javelin),
			(str_store_string, s1, "@{s1} javelins (+1),"), # debugging
		(try_end),
			
		# Polearms
		(try_begin),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_polearm, 1),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_enhanced_weapons, 1),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_enhanced_polearm),
			(str_store_string, s1, "@{s1} enhanced polearm (+2),"), # debugging
		(else_try),
			(troop_slot_eq, ":troop_id", slot_troop_tournament_polearm, 1),
			(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":troop_entry", wp_tpe_normal_polearm),
			(str_store_string, s1, "@{s1} polearm (+1),"), # debugging
		(try_end),
			
		(try_begin),
			(eq, wp_tpe_debug, 1),
			(str_store_troop_name, s2, ":troop_id"),
			(display_message, "@DEBUG (TPE): {s2} receives {s1}."),
		(try_end),
	]),
## TOURNAMENT PLAY ENHANCEMENTS end

# Not part of TPE, but copied from Custom Commander since it is used.
	("copy_inventory",
	  [
		(store_script_param_1, ":source"),
		(store_script_param_2, ":target"),
		
		(troop_clear_inventory, ":target"),
		(troop_get_inventory_capacity, ":inv_cap", ":source"),
		(try_for_range, ":i_slot", 0, ":inv_cap"),
		  (troop_get_inventory_slot, ":item", ":source", ":i_slot"),
		  (troop_set_inventory_slot, ":target", ":i_slot", ":item"),
		  (troop_get_inventory_slot_modifier, ":imod", ":source", ":i_slot"),
		  (troop_set_inventory_slot_modifier, ":target", ":i_slot", ":imod"),
		  (troop_inventory_slot_get_item_amount, ":amount", ":source", ":i_slot"),
		  (gt, ":amount", 0),
		  (troop_inventory_slot_set_item_amount, ":target", ":i_slot", ":amount"),
		(try_end),
	]),
	

# script_tpe_determine_scaled_renown
# This section implements the "Renown Scaling" feature.
# Inputs: None
# Output: reg0 (new renown)
  ("tpe_determine_scaled_renown",
    [
		# Determine renown gained by player level.
		(store_character_level, ":player_level", "trp_player"),
		(store_div, ":sr_level_factor", 40, ":player_level"),  # Balanced for a max level of 40.  Beyond this you get minimum gain.
		(val_mul, ":sr_level_factor", 5),
		(store_div, ":sr_factor_limit", wp_tpe_max_renown, 2), # Since two factors are used.  Total is split by 2.
		(val_min, ":sr_level_factor", ":sr_factor_limit"),     # Prevents an extremely low level gaining more renown than intended.
		(val_max, ":sr_level_factor", 5),                      # Sets a minimum renown gain of 5 no matter how high your level is.
		
		# Determine renown gained by player renown.
		(troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
		(store_div, ":sr_renown_factor", 1500, ":player_renown"),  # Balanced for a max renown of 1500.  Beyond this you get minimum gain.
		(val_mul, ":sr_renown_factor", 5),
		(store_div, ":sr_factor_limit", wp_tpe_max_renown, 2),  # Since two factors are used.  Total is split by 2.
		(val_min, ":sr_renown_factor", ":sr_factor_limit"),     # Prevents an extremely low level gaining more renown than intended.
		(val_max, ":sr_renown_factor", 5),                      # Sets a minimum renown gain of 5 no matter how high your level is.
		
		(store_add, reg0, ":sr_level_factor", ":sr_renown_factor"), # combines both factors.
	]),
	
# script_tpe_rep_gain_ladies
# This section implements the "Lady Reactions" feature.
# Inputs: None
# Output: None
  ("tpe_rep_gain_ladies",
    [
		# Raises relation with Ladies that are (present).  More so if in courtship.
		(try_for_range, ":troop_npc", kingdom_ladies_begin, kingdom_ladies_end),
			(troop_slot_eq, ":troop_npc", slot_troop_cur_center, "$current_town"), # For the Ladies.
			(assign, ":lady_rep", 1),
			(try_begin),
				(troop_slot_ge, ":troop_npc", slot_troop_courtship_state, 2),
				(val_add, ":lady_rep", 2),
			(try_end),
			(call_script, "script_change_player_relation_with_troop", ":troop_npc", ":lady_rep"),
		(try_end),
	]),
	
# script_tpe_rep_gain_lords
# This section implements the "Lord Reactions" feature.
# Inputs: None
# Output: None
  ("tpe_rep_gain_lords",
    [
		# Raises relation with Lords that are (present) AND (friendly).  Enemies gain nothing.
		(party_collect_attachments_to_party, "$current_town", "p_temp_party"),
		(party_get_num_companion_stacks,":party_stacks","p_temp_party"),
		(try_for_range, ":stack_no", 0, ":party_stacks"),
			(party_stack_get_troop_id,":troop_in_party","p_temp_party",":stack_no"),
			(troop_is_hero, ":troop_in_party"),
			(neg|is_between, ":troop_in_party", companions_begin, companions_end), # Removed companions from this benefit.
			(call_script, "script_troop_get_player_relation", ":troop_in_party"),
			(assign, ":relation", reg0),
			(assign, ":relation_gain", 0),
			(try_begin),
				(ge, ":relation", 10),
				(val_add, ":relation_gain", 1),
			(else_try),
				(le, ":relation", -5),
				(val_sub, ":relation_gain", -1),
			(else_try),
				(try_begin),
					(eq, wp_tpe_debug, 1),
					(str_store_troop_name, s1, ":troop_in_party"),
					(str_store_party_name, s2, "$current_town"),
					(display_message, "@DEBUG (TPE): {s1} was found in {s2}, but relation was too neutral to matter."),
				(try_end),
			(try_end),
			(call_script, "script_change_player_relation_with_troop", ":troop_in_party", ":relation_gain"),
		(try_end),
	]),
	
###########################################################################################################################
#####                                                TPE 1.2 Additions                                                #####
###########################################################################################################################
  # script_set_items_for_tournament
  # Input: arg1 = horse_chance, arg2 = lance_chance (with horse only), arg3 = sword_chance, arg4 = axe_chance, arg5 = bow_chance (without horse only), arg6 = javelin_chance (with horse only), arg7 = mounted_bow_chance (with horse only), arg8 = crossbow_sword_chance, arg9 = armor_item_begin, arg10 = helm_item_begin
  # Output: none (sets mt_arena_melee_fight items)
  ("set_items_for_tournament",
    [
      (store_script_param, ":horse_chance", 1),
      (store_script_param, ":lance_chance", 2),
      (store_script_param, ":sword_chance", 3),
      (store_script_param, ":axe_chance", 4),
      (store_script_param, ":bow_chance", 5),
      (store_script_param, ":javelin_chance", 6),
      (store_script_param, ":mounted_bow_chance", 7),
      (store_script_param, ":crossbow_sword_chance", 8),
      (store_script_param, ":armor_item_begin", 9),
      (store_script_param, ":helm_item_begin", 10),
      (store_add, ":total_chance", ":sword_chance", ":axe_chance"),
      (val_add, ":total_chance", ":crossbow_sword_chance"),
      (try_for_range, ":i_ep", 0, 32),
        (mission_tpl_entry_clear_override_items, "mt_arena_melee_fight", ":i_ep"),
        (assign, ":has_horse", 0),
        (store_div, ":cur_team", ":i_ep", 8),
        (try_begin),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", ":horse_chance"),
          (assign, ":has_horse", 1),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_horse"),
        (try_end),
        (try_begin),
          (eq, ":has_horse", 1),
          (store_add, ":cur_total_chance", ":total_chance", ":lance_chance"),
          (val_add, ":cur_total_chance", ":javelin_chance"),
          (val_add, ":cur_total_chance", ":mounted_bow_chance"),
        (else_try),
          (store_add, ":cur_total_chance", ":total_chance", ":bow_chance"),
        (try_end),
        (store_random_in_range, ":random_no", 0, ":cur_total_chance"),
        (store_add, ":cur_shield_item", "itm_arena_shield_red", ":cur_team"),
        (try_begin),
          (val_sub, ":random_no", ":sword_chance"),
          (lt, ":random_no", 0),
          (try_begin),
            (store_random_in_range, ":sub_random_no", 0, 100),
            (lt, ":sub_random_no", 50),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", wp_tpe_normal_sword),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
#            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_shield"),
          (else_try),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", wp_tpe_normal_greatsword),
          (try_end),
        (else_try),
          (val_sub, ":random_no", ":axe_chance"),
          (lt, ":random_no", 0),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_axe"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
#         (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_shield"),
        (else_try),
          (val_sub, ":random_no", ":crossbow_sword_chance"),
          (lt, ":random_no", 0),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", wp_tpe_normal_sword),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", wp_tpe_normal_crossbow),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_bolts"),
        (else_try),
          (eq, ":has_horse", 0),
          (val_sub, ":random_no", ":bow_chance"),
          (lt, ":random_no", 0),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", wp_tpe_normal_bow),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_arrows"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", wp_tpe_normal_sword),
        (else_try),
          (eq, ":has_horse", 1),
          (val_sub, ":random_no", ":lance_chance"),
          (lt, ":random_no", 0),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", wp_tpe_normal_lance),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
		  (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", wp_tpe_normal_sword),
#          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_shield"),
        (else_try),
          (eq, ":has_horse", 1),
          (val_sub, ":random_no", ":javelin_chance"),
          (lt, ":random_no", 0),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", wp_tpe_normal_javelin),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
		  (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", wp_tpe_normal_sword),
#          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_shield"),
        (else_try),
          (eq, ":has_horse", 1),
          (val_sub, ":random_no", ":mounted_bow_chance"),
          (lt, ":random_no", 0),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", wp_tpe_normal_bow),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_arrows"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", wp_tpe_normal_sword),
        (try_end),
        (try_begin),
          (ge, ":armor_item_begin", 0),
          (store_add, ":cur_armor_item", ":armor_item_begin", ":cur_team"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_armor_item"),
        (try_end),
        (try_begin),
          (ge, ":helm_item_begin", 0),
          (store_add, ":cur_helm_item", ":helm_item_begin", ":cur_team"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_helm_item"),
        (try_end),
      (try_end),
     ]),
]

from util_wrappers import *
from util_scripts import *

scripts_directives = [
	#rename scripts to "insert" switch scripts (see end of scripts[])
	[SD_RENAME, "set_items_for_tournament" , "orig_set_items_for_tournament"], 
	[SD_OP_BLOCK_INSERT, "fill_tournament_participants_troop", D_SEARCH_FROM_BOTTOM | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER, (neq, ":cur_troop", "trp_kidnapped_girl"), 0, 
		[(neg|troop_slot_eq, ":cur_troop", slot_troop_tournament_never_spawn, 1),], 1],
] # scripts_rename
                
def modmerge_scripts(orig_scripts):
	# process script directives first
	process_script_directives(orig_scripts, scripts_directives)
	# add remaining scripts
	add_scripts(orig_scripts, scripts, True)
	
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "scripts"
        orig_scripts = var_set[var_name_1]
    
        
		# START do your own stuff to do merging
		
        modmerge_scripts(orig_scripts)

		# END do your own stuff
        
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)