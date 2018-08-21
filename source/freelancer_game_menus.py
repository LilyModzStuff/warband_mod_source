# Freelancer (1.3) by Taragoth
# Released 11 July 2011
# Edits by Caba'drin 14 Dec 2011
# Mod-Merger'd by Windyplains, Monnikje and Caba'drin

from header_game_menus import *
from module_constants import *
from header_items import *

####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#  
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################

game_menus = [
#+freelancer start
#menu_world_map_soldier
    ("world_map_soldier",0,
    "What do you need to do soldier?",
    "none",
    [
	 (set_background_mesh, "mesh_pic_soldier_world_map"),
	 (troop_get_slot, "$enlisted_party", "$enlisted_lord", slot_troop_leaded_party), #CABA - to refresh it? maybe not necessessary
	],
	[
		("join_commander_battle",[
			(party_get_battle_opponent, ":commander_opponent", "$enlisted_party"),
			(gt, ":commander_opponent", 0),
		],"Follow the commander into battle.",[
		    (party_set_slot, "p_freelancer_party_backup", slot_party_last_in_combat, 1), #needed to catch post-battle and detach any attached parties
			
			(try_begin),
				(neg|troop_is_guarantee_horse, "$player_cur_troop"), 
				(troop_get_inventory_slot, ":horse", "trp_player", ek_horse),
				(gt, ":horse", 0),
				(troop_get_inventory_slot_modifier, ":horse_imod", "trp_player", ek_horse),
				(set_show_messages, 0),
				(troop_add_item, "trp_player", ":horse", ":horse_imod"),
				(troop_set_inventory_slot, "trp_player", ek_horse, -1),
				(set_show_messages, 1),
			(try_end),
			(start_encounter, "$enlisted_party"),
			(change_screen_map),
		]),
		
        ("enter_town",[(party_is_in_any_town,"$enlisted_party"),] ,"Enter stationed town.",
        [(party_get_cur_town, ":town_no", "$enlisted_party"),(start_encounter, ":town_no"),(change_screen_map),]),
	 
		("commander",[(party_get_battle_opponent, ":commander_opponent", "$enlisted_party"),(lt, ":commander_opponent", 0),],
		   "Request audience with your commander.",
        [(jump_to_menu, "mnu_commander_aud"),]),
		
		("revolt",[],"Revolt against the commander!",
        [(jump_to_menu, "mnu_ask_revolt"),]),
		
		("desert",[],"Desert the army.(keep equipment but lose relations)",
        [(jump_to_menu, "mnu_ask_desert"),]),
		
		("report",[],"Commander's Report",
		[(start_presentation, "prsnt_taragoth_lords_report"),]),
		
		("return_to_duty",[
			(party_get_battle_opponent, ":commander_opponent", "$enlisted_party"),
			(this_or_next|lt, ":commander_opponent", 0),
			(troop_is_wounded, "trp_player"),
		],"Return to duty.",
        [(change_screen_map),
		(assign, "$g_infinite_camping", 1),
        (rest_for_hours_interactive, 24 * 365, 5, 1),
		]),
    ]),
  
#menu_aud_with_commander 
  (
    "commander_aud",0,
    "Your request for a meeting is relayed to your commander's camp, and finally {s6} appears from his tent to speak with you.",
    "none",
    [(set_background_mesh, "mesh_pic_soldier_world_map"),(str_store_troop_name, s6, "$enlisted_lord")],
    [
      ("continue",[],
       "Continue...",
       [
		(try_begin),
			(neg|party_is_in_any_town, "$enlisted_party"),
			(start_encounter, "$enlisted_party"),
			(change_screen_map),
		(else_try),
			#Fake that it is a party encounter when enlisted party in a town (lines taken from script_game_event_party_encounter)
			(assign, "$g_encountered_party", "$enlisted_party"),
			(store_faction_of_party, "$g_encountered_party_faction","$g_encountered_party"),
			(store_relation, "$g_encountered_party_relation", "$g_encountered_party_faction", "fac_player_faction"),
			(party_get_slot, "$g_encountered_party_type", "$g_encountered_party", slot_party_type),
			(party_get_template_id,"$g_encountered_party_template","$g_encountered_party"),
			(assign, "$talk_context", tc_party_encounter),
			(call_script, "script_setup_party_meeting", "$g_encountered_party"),
		(try_end),
        ]),
		("reject_talk_lord",[],"No, nevermind.",
        [(change_screen_map),]),
    ]
  ),
 
    #menu_ask_revolt
    ("ask_revolt",0,
    "Are you sure you want to revolt?",
    "none",
    [(set_background_mesh, "mesh_pic_soldier_rebel"),(str_store_troop_name, s6, "$enlisted_lord")],[
		("confirm_revolt",[],"Yes, {s6} will be the death of us all, it is time to act!",
        [(jump_to_menu, "mnu_revolt"),]),
		
		("reject_revolt",[],"No, I am loyal to {s6}.",
        [(change_screen_return),]),
    ]),
	 
    #menu_revolt
    ("revolt",0,
    "Do you want to release the prisoners to help your men?",
    "none",
    [
        (set_background_mesh, "mesh_pic_soldier_rebel"),
		(assign, "$cant_leave_encounter", 1),

        #revert parties to former settings
		(call_script, "script_freelancer_detach_party"),
		(call_script, "script_event_player_deserts"),
		#adds other troops to join player revolt
        (call_script, "script_get_desert_troops"),
		
        #decreases player relation to his commander and faction
        (call_script, "script_change_player_relation_with_troop", "$enlisted_lord", -10),
		
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (try_begin),
            (party_get_battle_opponent, ":commander_enemy", "$enlisted_party"),
            (gt, ":commander_enemy", 0),
            (store_faction_of_party, ":other_faction", ":commander_enemy"),
            (store_relation, ":relation", ":other_faction", ":commander_faction"),
            (store_sub, ":mod_relation", 100, ":relation"),
            (val_add, ":mod_relation", 5),
            (call_script, "script_change_player_relation_with_faction_ex", ":commander_faction", ":mod_relation"),
        (try_end),
    ],
    [
        ("revolt_prisoners",[],"Yes, I will take the risk for a greater advantage.",
        [
            (party_clear, "p_temp_party_2"),
            #loop adding commander's prisoners to player party as troops
            (party_get_num_prisoner_stacks, ":num_stacks", "$enlisted_party"),
            (try_for_range, ":cur_stack", 0, ":num_stacks"),
                (party_prisoner_stack_get_troop_id , ":prisoner_troop", "$enlisted_party", ":cur_stack"),
                (ge, ":prisoner_troop", 1),
                (party_prisoner_stack_get_size, ":stack_size", "$enlisted_party", ":cur_stack"),
                (party_remove_prisoners, "$enlisted_party", ":prisoner_troop", ":stack_size"),
                (party_add_members, "p_temp_party_2", ":prisoner_troop", ":stack_size"),
            (try_end),
			(party_attach_to_party, "p_temp_party_2", "p_main_party"),
            (start_encounter, "$enlisted_party"),
            (change_screen_map),
        ]),

        ("revolt_no_prisoners",[],"No, I don't trust prisoners.",
        [
			(start_encounter, "$enlisted_party"),
            (change_screen_map),
        ]),
		
    ]),
	
 
    #menu_ask_desert
    ("ask_desert",0,
    "Do you want to desert?",
    "none",
    [(set_background_mesh, "mesh_pic_soldier_desert"),],[
        ("confirm_desert",[],"Yes, this is pointless.",
        [(jump_to_menu, "mnu_desert"),]),

        ("reject_desert",[],"No, I am loyal to my commander.",
        [(change_screen_return),]),
    ]),
  
    #menu_desert
    ("desert",0,
    "While in the army you've made some good friends. Some could possibly follow you.",
    "none",
    [
        (set_background_mesh, "mesh_pic_soldier_desert"),
		
		(call_script, "script_freelancer_detach_party"),
		(call_script, "script_event_player_deserts"),
	],
    [
        ("desert_party",[],"Try to convince them to follow you.",[
            #1 in 4 chance of being caught with others
            (store_random_in_range, ":chance_caught", 0, 4),
            (try_begin),
                (eq, ":chance_caught", 0),
				(assign, "$g_encountered_party", "$enlisted_party"),
		        (jump_to_menu, "mnu_captivity_start_wilderness"),
            (else_try),
                (call_script, "script_get_desert_troops"),
				(call_script, "script_party_restore"),	
                (call_script, "script_set_parties_around_player_ignore_player", 2, 4),
            (try_end),
            (change_screen_map),(display_message, "@You have deserted, and are now wanted!"), ]),

        ("desert_alone",[],"No, I have a better chance alone.",[
            #1 in 10 chance of being caught alone
            (store_random_in_range, ":chance_caught", 0, 10),
            (try_begin),
                (eq, ":chance_caught", 0),
                (assign, "$g_encountered_party", "$enlisted_party"),
		        (jump_to_menu, "mnu_captivity_start_wilderness"),
            (else_try),
			    (call_script, "script_party_restore"),
                (call_script, "script_set_parties_around_player_ignore_player", 2, 4),
            (try_end),
            (change_screen_map),
			(display_message, "@You have deserted, and are now wanted!"), ]),
    ]
			
		),
  
    #menu_upgrade_path
   ("upgrade_path",0,
    "In recognition of your excellent service, you have been promoted.",
    "none",[
		(set_background_mesh, "mesh_pic_soldier_world_map"),
		(call_script, "script_freelancer_unequip_troop", "$player_cur_troop"),
		],
    [
        ("upgrade_path_1",[
            (troop_get_upgrade_troop, ":path_1_troop", "$player_cur_troop", 0),
            (ge, ":path_1_troop", 0),
            (str_store_troop_name, s66, ":path_1_troop"),],
        "{s66}",[
            (troop_get_upgrade_troop, "$player_cur_troop", "$player_cur_troop", 0),
			(store_troop_faction, ":commander_faction", "$enlisted_lord"),
			(faction_set_slot, ":commander_faction", slot_faction_freelancer_troop, "$player_cur_troop"),
			(call_script, "script_freelancer_equip_troop", "$player_cur_troop"),
			(str_store_troop_name, s5, "$player_cur_troop"),
		    (str_store_string, s5, "@Current rank: {s5}"),
            (add_quest_note_from_sreg, "qst_freelancer_enlisted", 3, s5, 1),
            (change_screen_map),]),

        ("upgrade_path_2",[
            (troop_get_upgrade_troop, ":path_2_troop", "$player_cur_troop", 1),
            (ge, ":path_2_troop", 1),
            (str_store_troop_name, s67, ":path_2_troop"),],
        "{s67}",[
            (troop_get_upgrade_troop, "$player_cur_troop", "$player_cur_troop", 1),
			(store_troop_faction, ":commander_faction", "$enlisted_lord"),
			(faction_set_slot, ":commander_faction", slot_faction_freelancer_troop, "$player_cur_troop"),
			(call_script, "script_freelancer_equip_troop", "$player_cur_troop"),
			(str_store_troop_name, s5, "$player_cur_troop"),
		    (str_store_string, s5, "@Current rank: {s5}"),
            (add_quest_note_from_sreg, "qst_freelancer_enlisted", 3, s5, 1),
            (change_screen_map),]),
    ]),
#+freelancer end
 ]
 

pre_join_freelancer = [
          (eq, "$freelancer_state", 1),
		  (try_begin),
			(party_get_attached_to, ":attached", "$enlisted_party"),
			(this_or_next|eq, "$enlisted_party", "$g_encountered_party_2"),
			(eq, ":attached", "$g_encountered_party_2"),
			(select_enemy, 0),
			(assign,"$g_enemy_party","$g_encountered_party"),
            (assign,"$g_ally_party","$g_encountered_party_2"),
		  (else_try),
		    (select_enemy, 1),
			(assign,"$g_enemy_party","$g_encountered_party_2"),
			(assign,"$g_ally_party","$g_encountered_party"),
		  (try_end),
          (jump_to_menu,"mnu_join_battle"),
]	

join_siege_outside_freelancer = [
          (eq, "$freelancer_state", 1),
		  (try_begin),
			(store_troop_faction, ":commanders_faction", "$enlisted_lord"),
			(store_relation, ":relation", ":commanders_faction", "$g_encountered_party_faction"),
			(this_or_next|eq, ":commanders_faction", "$g_encountered_party_faction"), #encountered party is always the castle/town sieged
			(ge, ":relation", 0),
			(jump_to_menu, "mnu_siege_started_defender"),
		  (else_try),
			(jump_to_menu, "mnu_besiegers_camp_with_allies"),
		  (try_end),

]

join_battle_collect_others = [
	(try_begin),
		(eq, "$freelancer_state", 1),
		(call_script, "script_let_nearby_parties_join_current_battle", 0, 0),
		(str_store_party_name, 1,"$g_enemy_party"), #to prevent bug'd text from the above script (which also uses s1)
	(try_end),
]		  

join_wounded_freelancer = [
	("join_wounded",[
	  (eq, "$freelancer_state", 1),
	  (troop_is_wounded, "trp_player"),
	  ],
	  "You are too wounded to fight.",[(leave_encounter),(change_screen_map)]),
]


from util_wrappers import *
from util_common import *


def modmerge_game_menus(orig_game_menus, check_duplicates = False):
	try: #battle joining
		find_i = list_find_first_match_i( orig_game_menus, "pre_join" )
		codeblock = GameMenuWrapper(orig_game_menus[find_i]).GetOpBlock()
		codeblock.Append(pre_join_freelancer)	
		find_i = list_find_first_match_i( orig_game_menus, "join_battle" )
		codeblock = GameMenuWrapper(orig_game_menus[find_i]).GetOpBlock()
		pos = codeblock.FindLineMatching( (call_script, "script_encounter_init_variables") )
		codeblock.InsertBefore(pos, join_battle_collect_others)	
		find_i = list_find_first_match_i( orig_game_menus, "join_siege_outside" )
		codeblock = GameMenuWrapper(orig_game_menus[find_i]).GetOpBlock()
		codeblock.Append(join_siege_outside_freelancer)			
	except:
		import sys
		print "Injecton 1 failed:", sys.exc_info()[1]
		raise
		
	try: #victory processing
		find_i = list_find_first_match_i( orig_game_menus, "total_victory" )
		codeblock = GameMenuWrapper(orig_game_menus[find_i]).GetOpBlock()
		pos = codeblock.FindLineMatching( (assign, "$talk_context", tc_ally_thanks) )
		codeblock.InsertBefore(pos, not_in_party ) #prevents player in party from being thanked by allies	
		pos = codeblock.FindLineMatching( (assign, ":break", 0), 1 )  #skip first (right at top) find to go to second instance
		codeblock.InsertBefore(pos, not_in_party ) #prevents player in party from talking to enemy leaders
		pos = codeblock.FindLineMatching( (assign, ":break", 0) , 2 ) #next break
		codeblock.InsertBefore(pos, not_in_party ) #prevents player in party from talking to freed heroes after battle
		pos = codeblock.FindLineMatching( (gt, ":total_capture_size", 0) ) 
		codeblock.InsertBefore(pos, not_in_party )  #makes it so player can not have prisoners while in commanders party
		pos = codeblock.FindLineMatching( (change_screen_return) )
		pos += 1 #one more line to skip over the(else_try)
		codeblock.InsertAfter(pos, not_enlisted )  #prevents player's actions from having political consequences when in party	
	except:
		import sys
		print "Injecton 2 failed:", sys.exc_info()[1]
		raise
	
	try: #extra menu options
		find_i = list_find_first_match_i( orig_game_menus, "join_battle" )
		codeblock = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
		codeblock.extend(join_wounded_freelancer) 
	##FLORIS ONLY BEGIN
		codeblock = GameMenuWrapper(orig_game_menus[find_i]).GetOpBlock()
		pos = codeblock.FindLineMatching( (str_store_troop_name,s7,"$g_player_troop") )
		codeblock.InsertBefore(pos, [(str_clear, s4),]+not_in_party )	
		find_i = list_find_first_match_i( orig_game_menus, "besiegers_camp_with_allies" )
		codeblock = GameMenuWrapper(orig_game_menus[find_i]).GetOpBlock()
		pos = codeblock.FindLineMatching( (str_store_troop_name,s7,"$g_player_troop") )
		codeblock.InsertBefore(pos, [(str_clear, s4),]+not_in_party )	
		find_i = list_find_first_match_i( orig_game_menus, "siege_started_defender" )
		codeblock = GameMenuWrapper(orig_game_menus[find_i]).GetOpBlock()
		pos = codeblock.FindLineMatching( (str_store_troop_name,s5,"$g_player_troop") )
		codeblock.InsertBefore(pos, [(str_clear, s4),]+not_in_party )		
	##FLORIS ONLY END
		find_i = list_find_first_match_i( orig_game_menus, "siege_started_defender" )
		codeblock = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
		codeblock.extend(join_wounded_freelancer)	
		find_i = list_find_first_match_i( orig_game_menus, "besiegers_camp_with_allies" )
		codeblock = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
		codeblock.extend(join_wounded_freelancer)	
	except:
		import sys
		print "Injecton 3 failed:", sys.exc_info()[1]
		raise

	try: #disabling menu options
		find_i = list_find_first_match_i( orig_game_menus, "join_battle" )
		menulist = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
		for i in range(len(menulist)):
			menuID = GameMenuOptionWrapper(menulist[i]).GetId()
			if not ("join_attack" == menuID or "join_wounded" == menuID):
				codeblock = GameMenuOptionWrapper(menulist[i]).GetConditionBlock()
				codeblock.InsertBefore(0, not_in_party)
		find_i = list_find_first_match_i( orig_game_menus, "besiegers_camp_with_allies" )
		menulist = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
		for i in range(len(menulist)):
			menuID = GameMenuOptionWrapper(menulist[i]).GetId()
			if not ( "talk_to_siege_commander" == menuID or "join_siege_with_allies" == menuID or "join_wounded" == menuID):
				codeblock = GameMenuOptionWrapper(menulist[i]).GetConditionBlock()
				codeblock.InsertBefore(0, not_in_party)		
		find_i = list_find_first_match_i( orig_game_menus, "siege_started_defender" )
		menulist = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
		for i in range(len(menulist)):
			menuID = GameMenuOptionWrapper(menulist[i]).GetId()
			if not ("siege_defender_join_battle" == menuID or "join_wounded" == menuID):
				codeblock = GameMenuOptionWrapper(menulist[i]).GetConditionBlock()
				codeblock.InsertBefore(0, not_in_party)	
	except:
		import sys
		print "Injecton 4 failed:", sys.exc_info()[1]
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