# Freelancer (1.3) by Taragoth
# Released 11 July 2011
# Edits by Caba'drin 14 Dec 2011
# Mod-Merger'd by Windyplains, Monnikje and Caba'drin

from header_common import *
from header_operations import *
from header_triggers import *

from module_constants import *

####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################


triggers = [
#+freelancer start

#  CHECKS IF "$enlisted_party" IS DEFEATED
    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
        (gt, "$enlisted_party", 0),
        (neg|party_is_active, "$enlisted_party"),
		(check_quest_active, "qst_freelancer_enlisted"),
    ],
    [
		(call_script, "script_freelancer_event_player_captured"),		
		(assign, "$g_encountered_party", "$g_enemy_party"),
		(jump_to_menu, "mnu_captivity_start_wilderness"),
    ]),

 #  CHECKS IF "$enlisted_party" HAS JOINED BATTLE
    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
		(check_quest_active, "qst_freelancer_enlisted"),
		
		#collected nearby enemies->detach (post-battle)
		(try_begin), 
			(party_slot_ge, "p_freelancer_party_backup", slot_party_last_in_combat, 1),
			(map_free),
			(party_set_slot, "p_freelancer_party_backup", slot_party_last_in_combat, 0),
			(party_get_num_attached_parties, ":num_attached", "p_main_party"),
			(try_for_range_backwards, ":i", 0, ":num_attached"),
				(party_get_attached_party_with_rank, ":party", "p_main_party", ":i"),
				(party_detach, ":party"),
			(try_end),
		(try_end),
		
		#Is currently in battle
        (party_get_battle_opponent, ":commander_enemy", "$enlisted_party"),
        (gt, ":commander_enemy", 0),
		
		#checks that the player's health is high enough to join battle
        (store_troop_health, ":player_health", "trp_player"),
        (ge, ":player_health", 50),
    ],
    [
        (jump_to_menu, "mnu_world_map_soldier"),
    ]),

#  CHECKS IF PLAYER WON THE REVOLT
    (1.0, 0, 0, [
        (check_quest_active, "qst_freelancer_revolt"),
    ],
    [	
		(quest_get_slot, ":revolt_joiners", "qst_freelancer_revolt", slot_quest_target_party),
		(try_begin),
			(quest_slot_eq, "qst_freelancer_revolt", slot_quest_current_state, 0),
			(try_begin),
				(neg|party_is_active, "$enlisted_party"), #victory
				(try_begin),
					(gt, ":revolt_joiners", 0),
					(party_is_active, ":revolt_joiners"),
					(party_detach, ":revolt_joiners"),
					(quest_set_slot, "qst_freelancer_revolt", slot_quest_current_state, 1),
				(else_try),
					(call_script, "script_finish_quest", "qst_freelancer_revolt", 100),
				(try_end),
			(else_try),  #Defeat, enlisted party still active
				(try_begin),
					(gt, ":revolt_joiners", 0),
					(party_is_active, ":revolt_joiners"),
					(party_detach, ":revolt_joiners"),
					(remove_party, ":revolt_joiners"),
				(try_end),
				(call_script, "script_fail_quest", "qst_freelancer_revolt"),
				(call_script, "script_end_quest", "qst_freelancer_revolt"),
			(try_end),
			(assign, "$enlisted_party", 0),
		(try_end),
		
		(quest_slot_ge, "qst_freelancer_revolt", slot_quest_current_state, 1),

		(try_begin),
		    (quest_slot_eq, "qst_freelancer_revolt", slot_quest_current_state, 1),

			(store_skill_level, ":cur_leadership", "skl_leadership", "trp_player"),
			(store_skill_level, ":cur_persuasion", "skl_persuasion", "trp_player"),
			(store_add, ":chance", ":cur_persuasion", ":cur_leadership"),
			(val_add, ":chance", 10),
			(store_random_in_range, ":prisoner_state", 0, ":chance"),

			(try_begin),
				(is_between, ":prisoner_state", 0, 5),
				(call_script, "script_party_calculate_strength", "p_main_party", 0),
				(assign, ":main_strength", reg0),
				(call_script, "script_party_calculate_strength", ":revolt_joiners", 0),
				(assign, ":temp_strength", reg0),
				(ge, ":temp_strength", ":main_strength"),

				(party_get_num_prisoner_stacks, ":num_stacks", ":revolt_joiners"),
				(try_for_range, ":cur_stack", 0, ":num_stacks"),
					(party_prisoner_stack_get_troop_id, ":cur_troops", ":revolt_joiners", ":cur_stack"),
					(party_prisoner_stack_get_size, ":cur_size", ":revolt_joiners", ":cur_stack"),
					(party_remove_prisoners, ":revolt_joiners", ":cur_troops", ":cur_size"),
				(try_end),

				(quest_set_slot, "qst_freelancer_revolt", slot_quest_current_state, 2),
				
				(dialog_box, "@The released prisoners were not be trusted and they are preparing to attack you!", "@Warning!"),
				(start_encounter, ":revolt_joiners"),
				(change_screen_map),
			(else_try),
				(is_between, ":prisoner_state", 5, 10),
				(dialog_box, "@The released prisoners scattered as soon as the battle finished. You will not be seeing them again.", "@Notice!"),
				(remove_party, ":revolt_joiners"),
				(call_script, "script_finish_quest", "qst_freelancer_revolt", 100),
				(quest_set_slot, "qst_freelancer_revolt", slot_quest_current_state, 0),
			(else_try),
				(dialog_box, "@The released prisoners have remained loyal and will join your party", "@Notice!"),
				(call_script, "script_party_add_party", "p_main_party", ":revolt_joiners"),
				(remove_party, ":revolt_joiners"),
				(call_script, "script_finish_quest", "qst_freelancer_revolt", 100),
				(quest_set_slot, "qst_freelancer_revolt", slot_quest_current_state, 0),
			(try_end),
		(else_try), #After fight with released prisoners
			(quest_slot_eq, "qst_freelancer_revolt", slot_quest_current_state, 2),
			(try_begin),
				(neg|party_is_active, ":revolt_joiners"),
				(neq, "$g_player_is_captive", 1),
				(call_script, "script_finish_quest", "qst_freelancer_revolt", 100),
			(else_try),
				(call_script, "script_fail_quest", "qst_freelancer_revolt"),
				(call_script, "script_end_quest", "qst_freelancer_revolt"),
			(try_end),
			(quest_set_slot, "qst_freelancer_revolt", slot_quest_current_state, 0),
		(try_end),
    ]),

# IF LEFT MOUSE CLICK GO TO SOLDIER'S MENU
    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
        (key_clicked, key_left_mouse_button),

        (set_fixed_point_multiplier, 1000),
        (mouse_get_position, pos0),
        (position_get_y, ":y", pos0),
        (gt, ":y", 50), #allows the camp, reports, quests, etc. buttons to be clicked
    ],
    [
        (jump_to_menu, "mnu_world_map_soldier"),
        (rest_for_hours_interactive, 9999, 4, 0),
    ]),

(24.0, 0, 0, [
        (eq, "$freelancer_state", 2),
    ],
    [
		(try_for_range, ":cur_quest", freelancer_quests_begin, freelancer_quests_end),
			(check_quest_active, ":cur_quest"),
			(quest_get_slot, ":days_left", ":cur_quest", slot_quest_expiration_days),
			(ge, ":days_left", 1),
			(val_sub, ":days_left", 1), #to give extra warning...before this whole trigger is merged over to simple triggers or into the quest pack
			(try_begin),
				(eq, ":days_left", 5),
				(str_store_troop_name, s13, "$enlisted_lord"),
				(dialog_box, "@You have 5 days remaining in your leave from the party of {s13} before you will be declared a deserter.", "@Notice!"),
			(else_try),
				(is_between, ":days_left", 2, 5),
				(assign, reg0, ":days_left"),
				(display_message, "@You have {reg0} days left until you are declared as a deserter!"),
			(else_try),
				(eq, ":days_left", 1),
				(str_store_troop_name, s13, "$enlisted_lord"),
				(dialog_box, "@You must check in with your commander {s13} immediately or you will be declared a deserter!", "@Warning!"),
			(try_end),
		(try_end),
    ]),


#+freelancer end
]


# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "triggers"
        orig_triggers = var_set[var_name_1]
        orig_triggers.extend(triggers)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)