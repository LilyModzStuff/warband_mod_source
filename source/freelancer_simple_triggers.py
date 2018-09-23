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
		(store_current_hours, reg0),
		(val_add, reg0, 24 * 7),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_next_payday, reg0),
		
		(try_begin),
			(troop_get_upgrade_troop, ":upgrade_troop", "$player_cur_troop", 0),
			(gt, ":upgrade_troop", 1), #make sure troop is valid and not player troop
			(quest_slot_ge, "qst_freelancer_enlisted", slot_quest_freelancer_upgrade_xp, 1),	
			(quest_get_slot, ":service_xp_start", "qst_freelancer_enlisted", slot_quest_freelancer_start_xp),
			(troop_get_xp, ":player_xp_cur", "trp_player"),
			(store_sub, ":service_xp_cur", ":player_xp_cur", ":service_xp_start"),		   
			(neg|quest_slot_ge, "qst_freelancer_enlisted", slot_quest_freelancer_upgrade_xp, ":service_xp_cur"),
			(jump_to_menu, "mnu_upgrade_path"),		
        (try_end),
		
        (store_character_level, ":level", "$player_cur_troop"),
        #pays player 10 times the troop level
        (store_mul, ":weekly_pay", 10, ":level"),
        (troop_add_gold, "trp_player", ":weekly_pay"),
        (add_xp_to_troop, 70, "trp_player"),
        (play_sound, "snd_money_received", 0),
		
        (assign, ":num_food", 0),
        (troop_get_inventory_capacity, ":max_inv_slot", "trp_player"),
        (try_for_range, ":cur_inv_slot", ek_item_0, ":max_inv_slot"),
           (troop_get_inventory_slot, ":cur_item", "trp_player", ":cur_inv_slot"),
           (ge, ":cur_item", 0),
           (is_between, ":cur_item", food_begin, food_end),
           (troop_inventory_slot_get_item_amount, reg0, "trp_player", ":cur_inv_slot"),
		   (val_add, ":num_food", reg0),
        (try_end),
        (try_begin),
           (lt, ":num_food", 10),
           (troop_add_item, "trp_player", "itm_bread"),
        (try_end),
    ]),

#  HOURLY CHECKS

    (1,[
        (eq, "$freelancer_state", 1),
        #so that sight and camera follows near commander's party
        (set_camera_follow_party, "$enlisted_party"),
        (party_relocate_near_party, "p_main_party", "$enlisted_party", 1), 
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
