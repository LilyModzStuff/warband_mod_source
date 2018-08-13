## Prebattle Orders & Deployment by Caba'drin
## v0.92
## 20 Jan 2012
from header_game_menus import *
from module_constants import *

camp_addon = [
	  ## PreBattle Orders & Deployment Begin
 	  ("action_prebattle_mod_preferences",[],
		"PBOD Mod Preferences.",
       [(start_presentation, "prsnt_pbod_preferences")]
      ), 	  
	  ("action_prebattle_custom_divisions",[],
		"Manage Split Troop Assignments.",
       [(start_presentation, "prsnt_prebattle_custom_divisions")]
      ), 
      ## PreBattle Orders & Deployment End
]

menu_opblock_addon = [
		## PreBattle Orders & Deployment Begin
		(try_begin),
		    (party_slot_eq, "p_main_party", slot_party_prebattle_customized_deployment, 1),
			(str_store_string, s4, "@{s4}^^The troops you selected are ready to join you in battle."),
		(else_try),			
			(str_store_string, s4, "@{s4}^^Your captains will deal with troop assignments."),
		(try_end),
		(try_begin),
            (party_slot_eq, "p_main_party", slot_party_prebattle_plan, 1),
			(str_store_string, s4, "@{s4}^^Your orders have been sent to your captains."),
		(else_try),
			(str_store_string, s4, "@{s4}^^There is no tactical plan in place."),
		(try_end),
		## PreBattle Orders & Deployment End
]

deployment_mno_condition = [
		(party_get_skill_level, ":tactics", "p_main_party", skl_tactics),
		(ge, ":tactics", 2),
		
		(call_script, "script_party_count_fit_for_battle", "p_collective_friends"),
		(assign, ":friend_count", reg0),
		(call_script, "script_party_count_fit_for_battle", "p_collective_enemy"),
		(assign, ":enemy_count", reg0),
		(store_add, ":total_combatants", ":friend_count", ":enemy_count"),
		(party_get_slot, ":battle_size", "p_main_party", slot_party_prebattle_battle_size),
		(gt, ":total_combatants", ":battle_size"),
]

orders_mno_condition = [	  
		(party_get_skill_level, ":tactics", "p_main_party", skl_tactics),
		(ge, ":tactics", 2),
]

alt_attack_mno_condition = [	  
		(party_get_skill_level, ":tactics", "p_main_party", skl_tactics),
		(ge, ":tactics", 1),
		(party_slot_eq, "p_main_party", slot_party_prebattle_plan, 0),
]
	  
clear_orders = [
        (try_begin),
		    (party_slot_eq, "p_main_party", slot_party_prebattle_customized_deployment, 1),
		    (party_set_slot, "p_main_party", slot_party_prebattle_customized_deployment, 0),
		(try_end),
	    (try_begin),
		    (party_slot_eq, "p_main_party", slot_party_prebattle_plan, 1),
			(party_set_slot, "p_main_party", slot_party_prebattle_plan, 0),
		    (party_set_slot, "p_main_party", slot_party_prebattle_num_orders, 0),
		(try_end),
]

do_hold = [     
        (party_set_slot, "p_main_party", slot_party_prebattle_num_orders, 1),
	    (party_get_slot, ":first_order", "p_main_party", slot_party_prebattle_order_array_begin),
		(try_begin),
		    (gt, ":first_order", 0),
			(party_set_slot, "p_main_party_backup", slot_party_prebattle_order_array_begin, ":first_order"),
        (try_end),
		(party_set_slot, "p_main_party", slot_party_prebattle_order_array_begin, 910),		     
]

do_follow = [      
        (party_set_slot, "p_main_party", slot_party_prebattle_num_orders, 1),
		(party_get_slot, ":first_order", "p_main_party", slot_party_prebattle_order_array_begin),
		(try_begin),
		    (gt, ":first_order", 0),
			(party_set_slot, "p_main_party_backup", slot_party_prebattle_order_array_begin, ":first_order"),
        (try_end),
        (party_set_slot, "p_main_party", slot_party_prebattle_order_array_begin, 911),		
]

do_orders = [
        (party_set_slot, "p_main_party", slot_party_prebattle_plan, 0),
]

noplan = [(party_slot_eq, "p_main_party", slot_party_prebattle_plan, 0),]

game_menus = [] #for any menus that need to be added to the end

from util_wrappers import *
from util_common import *

def add_pbod_to(objlist, menu_id):
	try:
		find_i = list_find_first_match_i( objlist, menu_id )
		menu = GameMenuWrapper(objlist[find_i])
		menuoptions = menu.GetMenuOptions()
		menuID = menu.GetId() 
		if ("siege" in menuID and not "castle" in menuID):
			attack_i = list_find_first_containing_i(menuoptions, "join")
		else:
			attack_i = list_find_first_containing_i(menuoptions, "attack")
		for i in range(len(menuoptions)):
			menuID = GameMenuOptionWrapper(menuoptions[i]).GetId()
			if not ( #i == attack_i or #not the main attack option, or other options to skip:
			   "siege_request_meeting" == menuID or "wait_24_hours" == menuID or "talk_to_siege_commander" == menuID ##for sieges
			   or "change_commander" in menuID or "dplmc_negotiate_with_besieger" == menuID or "access_crew" == menuID ##for mods that include custom commander, diplomacy, or Floris sea battles
			   ): 
				GameMenuOptionWrapper(menuoptions[i]).GetConditionBlock().Append(noplan)
		menuID = menu.GetId() 
		attack = GameMenuOptionWrapper(menuoptions[attack_i])
		can_attack = attack.GetConditionBlock().Unwrap()
		do_attack  = attack.GetConsequenceBlock().Unwrap()
		if not ("siege" in menuID):
			#create follow option
			newoption = ("follow", can_attack+alt_attack_mno_condition, "Lead your troops.", do_follow+do_attack)
			menuoptions.insert(attack_i, newoption)
			#create hold option
			newoption = ("hold", can_attack+alt_attack_mno_condition, "Take the field.", do_hold+do_attack)
			menuoptions.insert(attack_i, newoption)
		#create clear plan option
		newoption = ("clear_orders", [(this_or_next|party_slot_eq, "p_main_party", slot_party_prebattle_customized_deployment, 1),
		  (party_slot_eq, "p_main_party", slot_party_prebattle_plan, 1),], "Re-assess the situation.", clear_orders+[(jump_to_menu, "mnu_"+menuID),])
		menuoptions.insert(attack_i, newoption)
		#if not ("siege" in menuID):		
		#create use pb-orders option
		newoption = ("do_orders", [(party_slot_eq, "p_main_party", slot_party_prebattle_plan, 1),], "Enough planning. To battle!", do_orders+do_attack)
		menuoptions.insert(attack_i, newoption)
		#create make pb-orders option
		newoption = ("orders", can_attack+orders_mno_condition, "Plan your battle with the enemy.", [(assign, "$g_next_menu", "mnu_"+menuID),(start_presentation, "prsnt_prebattle_orders"),])
		menuoptions.insert(attack_i, newoption)
		#create deployment option
		newoption = ("deployment", can_attack+deployment_mno_condition, "Choose who will join you in battle.", [(assign, "$g_next_menu", "mnu_"+menuID),(start_presentation, "prsnt_prebattle_custom_deployment"),])
		menuoptions.insert(attack_i, newoption)	
		#add clear variables to native attack option
		attack.GetConsequenceBlock().InsertBefore(0,[
		   (try_begin),
			(party_slot_eq, "p_main_party", slot_party_prebattle_plan, 1),
			(party_set_slot, "p_main_party", slot_party_prebattle_plan, 0),
		   (try_end),
		 ])
		if ("castle_siege" == menuID):
			menu.GetOpBlock.Append([(try_begin),can_attack+menu_opblock_addon,(else_try),(str_clear, s4),(try_end),])
		else:
			menu.GetOpBlock().Append(menu_opblock_addon)
		menu.GetOpBlock().InsertBefore(0, [(str_clear, s4)])
		#Change Text in immutable tuple by swapping to list and then back
		objlist[find_i] = list(objlist[find_i])
		objlist[find_i][2] += " {s4}" #tag string s4 to end of menu text, set in menu_opblock_addon
		objlist[find_i] = tuple(objlist[find_i])
		
	
	except:
		import sys
		print "Add PBOD failed:", menu, sys.exc_info()[1]
		raise

def modmerge_game_menus(orig_game_menus, check_duplicates = False):
	try:
		find_i = list_find_first_match_i( orig_game_menus, "camp_mod_preferences" )
		menuoptions = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
		find_i = list_find_first_match_i(menuoptions, "camp_action")		
		OpBlockWrapper(menuoptions).InsertAfter(find_i, camp_addon)		

		add_pbod_to( orig_game_menus, "simple_encounter" )
		add_pbod_to( orig_game_menus, "join_battle" )
		add_pbod_to( orig_game_menus, "castle_besiege" )
		add_pbod_to( orig_game_menus, "besiegers_camp_with_allies" )
		add_pbod_to( orig_game_menus, "siege_started_defender" )
	except:
		import sys
		print "Injecton 1 failed:", sys.exc_info()[1]
		raise


	
	if( not check_duplicates ):
		orig_game_menus.extend(game_menus) # Use this only if there are no replacements (i.e. no duplicated item names)
	else:
    # Use the following loop to replace existing entries with same id
		for i in range (0,len(game_menus)-1):
			find_index = find_object(orig_game_menus, game_menus[i][0]); # find_object is from header_common.py
			if( find_index == -1 ):
				orig_game_menus.append(game_menus[i])
			else:
				orig_game_menus[find_index] = game_menus[i]

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]
        modmerge_game_menus(orig_game_menus)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)