from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *
from util_wrappers import *
from util_common import *
from module_constants import *

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
		
		("start_phase_2",mnf_disable_all_keys, #start_phase_2_5
			"{!}{s16}",
			"none",
			[
				(str_store_party_name, s1, "$g_starting_town"),
				(str_store_string, s16, "$g_journey_string"),
			],
				[
					("continue",[], "Continue...",
						[
							(jump_to_menu, "mnu_start_phase_3"),
						]),
				]
		),
		
 ]
 
update_menu_start_game_0_block = [

      ("cc_pres_test",[],"Continue...", [(call_script, "script_mcc_default_settings"), (start_presentation, "prsnt_mcc_character_creation")]),
          
]



# Adding new game menu function
def add_game_menus(orig_game_menus, game_menus, check_duplicates = True):
    addmode = ADDMODE_REPLACE_EXIST
    if  not check_duplicates:
        addmode = ADDMODE_APPEND
    return add_objects(orig_game_menus, game_menus, addmode)

# Menu option replacing function
def modmerge_game_menus(orig_game_menus, check_duplicates = False):
    try: #full replace mno_sail_from_port in mnu_town
        menu_new_game = list_find_first_match_i(orig_game_menus, "start_game_0") # get "Town" menu
        menu_new_game_options_list = GameMenuWrapper(orig_game_menus[menu_new_game]).GetMenuOptions() # get option list
        for option_i in range(len(menu_new_game_options_list)): # checking all menu options
            option_id = GameMenuOptionWrapper(menu_new_game_options_list[option_i]).GetId() # take the name of current menu_option
            if (option_id == "continue"): # if is target option
                menu_new_game_options_list[option_i] = update_menu_start_game_0_block[0] # full replace it by new code
				
	

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
	


	
    # splice this into camp menu to call the mod options presentation
    # find_index = find_object(orig_game_menus, "start_game_0")
    # orig_game_menus[find_index][5].insert(0,
            # ("cc_pres_test",[],"Creation Screen", [(call_script, "script_mcc_default_settings"), (start_presentation, "prsnt_mcc_character_creation")]),
          # ),
		  
	
    # find_index = find_object(orig_game_menus, "start_phase_2")
    # orig_game_menus[find_index][5].insert(0,
            # ("continue",[], "Click this one!",
		   # [
			# (party_set_flags, "$current_town", pf_no_label, 0),
			# (jump_to_menu, "mnu_start_phase_3"),
		   # ]),
		   
		  # ),



          
# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]
	add_game_menus(orig_game_menus, game_menus, True)
        modmerge_game_menus(orig_game_menus)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
 

