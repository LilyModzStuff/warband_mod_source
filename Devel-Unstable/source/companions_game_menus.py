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
####################################################################################################################################
# LAV MODIFICATIONS START (COMPANIONS OVERSEER MOD)
####################################################################################################################################

    ("lco_presentation",0,"Hidden Text","none",
        [
            (jump_to_menu, "mnu_lco_presentation"), # Self-reference
            (try_begin),
                (eq, "$g_lco_page", 2),
                (start_presentation, "prsnt_equipment_overview"),
            (else_try),
                (start_presentation, "prsnt_companions_overview"),
            (try_end),
        ],
        [("lco_go_back",[],"{!}Return",[])]
    ),

    ("lco_view_character",0,"Hidden Text","none",
        [
            (modify_visitors_at_site,"scn_conversation_scene"),
            (reset_visitors),
            (set_visitor,0,"trp_player"),
            (set_visitor,17,"$g_lco_target"),
            (set_jump_mission,"mt_conversation_encounter"),
            (jump_to_scene,"scn_conversation_scene"),
            (change_screen_map_conversation, "$g_lco_target"),
        ],
        [("lco_go_back",[],"{!}Return",[])]
    ),

    ("lco_auto_return",0,"Hidden Text","none",
        [
            (try_begin),
                (gt, "$g_lco_auto_menu", 0),
                (jump_to_menu, "$g_lco_auto_menu"),
                (assign, "$g_lco_auto_menu", 0),
            (else_try),
                (change_screen_return),
            (try_end),
        ],
        [("lco_go_back",[],"{!}Return",[])]
    ),

####################################################################################################################################
# LAV MODIFICATIONS END (COMPANIONS OVERSEER MOD)
####################################################################################################################################
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

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]
        modmerge_game_menus(orig_game_menus)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)