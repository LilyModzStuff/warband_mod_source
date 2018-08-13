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
    ],
    [
        (assign, "$freelancer_state", 0),
        (call_script, "script_freelancer_detach_party"),
		
		#to prevent companions from being lost forever
		(call_script, "script_party_restore"), 
		(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
        (try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
			(party_stack_get_troop_id, ":return_troop", "p_main_party", ":cur_stack"),
			(neg|troop_is_hero, ":return_troop"),
			(party_stack_get_size, ":stack_size", "p_main_party", ":cur_stack"),
			(party_remove_members, "p_main_party", ":return_troop", ":stack_size"),
		(try_end),

        #removes faction relation given at enlist
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
            (neq, ":commander_faction", ":cur_faction"),
			(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
            (call_script, "script_set_player_relation_with_faction", ":cur_faction", 0),
        (try_end),

		(assign, "$g_encountered_party", "$g_enemy_party"),
		(jump_to_menu, "mnu_captivity_start_wilderness"),
    ]),

 #  CHECKS IF "$enlisted_party" HAS JOINED BATTLE

    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
		
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
        (eq, "$freelancer_state", 0),
        (gt, "$enlisted_party", 0),
        (neg|party_is_active, "$enlisted_party"),

		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":commander_faction"),
        (lt, ":relation", 0),

        (party_get_attached_party_with_rank, ":attached_party", "p_main_party", 0),
        (eq, "p_temp_party_2", ":attached_party"),
    ],
    [
        (assign, "$enlisted_party", -1),
        (party_detach, "p_temp_party_2"),
        (store_skill_level, ":cur_leadership", "skl_leadership", "trp_player"),
        (store_skill_level, ":cur_persuasion", "skl_persuasion", "trp_player"),
        (store_add, ":chance", ":cur_persuasion", ":cur_leadership"),
        (val_add, ":chance", 10),
        (store_random_in_range, ":prisoner_state", 0, ":chance"),

        (try_begin),
            (is_between, ":prisoner_state", 0, 5),
            (call_script, "script_party_calculate_strength", "p_main_party", 0),
            (assign, ":main_strength", reg0),
            (call_script, "script_party_calculate_strength", "p_temp_party_2", 0),
            (assign, ":temp_strength", reg0),
            (ge, ":temp_strength", ":main_strength"),

            (party_get_num_prisoner_stacks, ":num_stacks", "p_temp_party_2"),
            (try_for_range, ":cur_stack", 0, ":num_stacks"),
                (party_prisoner_stack_get_troop_id, ":cur_troops", "p_temp_party_2", ":cur_stack"),
                (party_prisoner_stack_get_size, ":cur_size", "p_temp_party_2", ":cur_stack"),
                (party_remove_prisoners, "p_temp_party_2", ":cur_troops", ":cur_size"),
            (try_end),

            (tutorial_box, "@The released prisoners were not be trusted and they are preparing to attack you!", "@Warning!"),
            (start_encounter, "p_temp_party_2"),
            (change_screen_map),
        (else_try),
            (is_between, ":prisoner_state", 5, 10),
            (tutorial_box, "@The released prisoners scattered as soon as the battle finished. You will not be seeing them again.", "@Notice!"),
            (party_clear, "p_temp_party_2"),
        (else_try),
            (tutorial_box, "@The released prisoners have remained loyal and will join your party", "@Notice!"),
            (party_get_num_companion_stacks, ":num_stacks", "p_temp_party_2"),
            (try_for_range, ":cur_stack", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":cur_troops", "p_temp_party_2", ":cur_stack"),
                (party_stack_get_size, ":cur_size", "p_temp_party_2", ":cur_stack"),
                (party_add_members, "p_main_party", ":cur_troops", ":cur_size"),
            (try_end),
            (party_clear, "p_temp_party_2"),
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
		(troop_get_slot, ":days_left", "trp_player", slot_troop_days_on_mission),
		(try_begin),
		  (gt, ":days_left", 5),
		  (val_sub, ":days_left", 1),
		  (troop_set_slot, "trp_player", slot_troop_days_on_mission, ":days_left"),
		(else_try),		  
		  (is_between, ":days_left", 1, 5),
		  (assign, reg0, ":days_left"),
		  (display_message, "@You have {reg0} days left till you are declared as a deserter!"),
		  (val_sub, ":days_left", 1),
		  (troop_set_slot, "trp_player", slot_troop_days_on_mission, ":days_left"),
		(else_try), #declare deserter
		  (eq, ":days_left", 0),
		  (call_script, "script_event_player_deserts"),
          (display_message, "@You have now been declared as a deserter!"),
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