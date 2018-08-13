# Dynamic Troop Trees by Dunde, modified by Caba'drin.

from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

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
## REPLACEMENT MENU - menu_town_tournament_won
# (
    # "new_town_tournament_won",mnf_disable_all_keys,
    # "You have won the tournament of {s3}! You are filled with pride as the crowd cheers your name.\
 # In addition to honour, fame and glory, you earn a prize of {reg9} denars. {s8}",
    # "none",
    # [
		
    # ],
    # [
      # ("continue", [], "Continue...",
       # [(jump_to_menu, "mnu_town"),
        # ]),
    # ]
  # ),
 
 ]

	
def modmerge_game_menus(orig_game_menus, check_duplicates = False):
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
	# splice this into report menu to call the mod options presentation
    find_index = find_object(orig_game_menus, "reports")
    orig_game_menus[find_index][5].insert(0,
            ("troop_tree_viewer",[],"View Troop Trees", [(start_presentation, "prsnt_faction_troop_tree")]),
          )

		  
		  
# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]
        modmerge_game_menus(orig_game_menus)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)