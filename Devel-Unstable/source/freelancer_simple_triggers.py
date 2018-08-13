# Freelancer (1.3) by Taragoth
# Released 11 July 2011
# Edits by Caba'drin 14 Dec 2011
# Mod-Merger'd by Windyplains, Monnikje and Caba'drin

from header_common import *
from header_operations import *
from header_items import *
from module_constants import *

####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#  Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################



simple_triggers = [
#+freelancer start
  #  WEEKLY PAY AND CHECKS FOR UPGRADE

    (24 * 7, [
        (eq, "$freelancer_state", 1),
		(troop_get_slot, ":service_xp_start", "trp_player", slot_troop_freelancer_start_xp),
        (troop_get_xp, ":player_xp_cur", "trp_player"),
        (store_sub, ":service_xp_cur", ":player_xp_cur", ":service_xp_start"),

        #ranks for pay levels and to upgrade player equipment based on upgrade troop level times 1000
        # (try_begin),
           # (troop_get_upgrade_troop, ":upgrade_troop", "$player_cur_troop", 0),
           # (gt, ":upgrade_troop", 1), #make sure troop is valid and not player troop
           # (store_character_level, ":level", ":upgrade_troop"),
           # (store_pow, ":required_xp", ":level", 2), #square the level and
           # (val_mul, ":required_xp", 100),           #multiply by 100 to get xp
           # (ge, ":service_xp_cur", ":level"),
           # (jump_to_menu, "mnu_upgrade_path"),
        # (try_end),
		(try_begin),
           (troop_get_upgrade_troop, ":upgrade_troop", "$player_cur_troop", 0),
           (gt, ":upgrade_troop", 1), #make sure troop is valid and not player troop
           
		   (call_script, "script_game_get_upgrade_xp", "$player_cur_troop"),
		   (assign, ":required_xp", reg0),		   
		   ##THIS  BLOCK IS ALMOST DEFINITELY BE BETTER than the above two lines which could be commented out in exchange for them.
		   # (store_character_level, ":cur_level", "$player_cur_troop"),
           # (val_sub, ":cur_level", 1),
           # (get_level_boundary, ":cur_level", ":cur_level"),
		   # (store_character_level, ":required_xp", ":upgrade_troop"),
		   # (val_sub, ":required_xp", 1),
		   # (get_level_boundary, ":required_xp", ":required_xp"),
		   # (val_sub, ":required_xp", ":cur_level"),		   
		   ##
		   		   
           (ge, ":service_xp_cur", ":required_xp"),
		   (try_begin),
		   		(call_script, "script_cf_freelancer_player_can_upgrade", ":upgrade_troop"),
				(troop_set_slot, "trp_player", slot_troop_freelancer_start_xp, ":player_xp_cur"),
				(jump_to_menu, "mnu_upgrade_path"),
		   (else_try),
				(assign, ":reason", reg0), #from cf_freelancer_player_can_upgrade
				(try_begin),
					(eq, ":reason", 0), #not enough strength, for melee weapons
					(display_message, "@You are not strong enough to lift a weapon fit for your promotion!"),
				(else_try),
					(eq, ":reason", 1), #not enough strength, for armor
					(display_message, "@You are not strong enough to hold all that weight required with promotion!."),
				(else_try),
					(eq, ":reason", 2), #not enough power draw/throw/strength for bow/crossbow/throwing
					(display_message, "@Your arms are to weak to advance in the artillary at this moment."),
				(else_try),
					(eq, ":reason", 3), #not enough riding skill for horse
					(display_message, "@You require more horse riding skills to fit your next poisition!"),
				(try_end),				
		   (try_end),			
        (try_end),
		
		
		
        (store_character_level, ":level", "$player_cur_troop"),
        #pays player 10 times the troop level
        (store_mul, ":weekly_pay", 10, ":level"),
        (troop_add_gold, "trp_player", ":weekly_pay"),
        (add_xp_to_troop, 70, "trp_player"),
        (play_sound, "snd_money_received", 0),
    ]),

#  HOURLY CHECKS

    (1,[
        (eq, "$freelancer_state", 1),
        #so that sight and camera follows near commander's party
        (set_camera_follow_party, "$enlisted_party"),
        (party_relocate_near_party, "p_main_party", "$enlisted_party", 1), 

        (assign, ":num_food", 0),
        (troop_get_inventory_capacity, ":max_inv_slot", "trp_player"),
        (try_for_range, ":cur_inv_slot", ek_item_0, ":max_inv_slot"),
           (troop_get_inventory_slot, ":cur_item", "trp_player", ":cur_inv_slot"),
           (ge, ":cur_item", 0),
           (is_between, ":cur_item", food_begin, food_end),
           (val_add, ":num_food", 1),
        (try_end),
        (try_begin),
           (lt, ":num_food", 2),
           (troop_add_item, "trp_player", "itm_bread"),
        (try_end),
    ]),
	
  #+freelancer end  
]


# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "simple_triggers"
        orig_simple_triggers = var_set[var_name_1]
        orig_simple_triggers.extend(simple_triggers)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
		
	for i in range (0,len(orig_simple_triggers)):
		if (SimpleTriggerWrapper(i).GetInterval() == 32): #the only one in Native is for offering vassalage
			codeblock = SimpleTriggerWrapper(i).GetOpBlock()
			codeblock.InsertBefore(0, (eq, "$freelancer_state", 0)) # Freelancer - Added to prevent vassalage while enlisted and becoming stuck in a lord's army.  - Windy
