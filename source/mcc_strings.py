# Character Creation Presentation (1.0.2)
# Created by Windyplains.  Inspired by Dunde's character creation presentation in Custom Commander.

strings = [
	# Object Titles
	("mcc_label_done", "Done"),
	("mcc_label_back", "Back"),
	("mcc_label_default", "Default"),
	("mcc_label_random", "Randomize"),
	("mcc_label_menus", "Character Background"),
	("mcc_label_story", "Your Story"),
	("mcc_label_gender", "Your gender:"),
	("mcc_label_father", "Your father was:"),
	("mcc_label_earlylife", "You spent your early life as:"),
	("mcc_label_later", "Later you became:"),
	("mcc_label_reason", "The reason for an adventure:"),
	("mcc_label_gameplay_options", "Game Options"),
	# ("mcc_label_fog_of_war", "Fog of War"),
	# ("mcc_label_mtt", "Troop Tree"),
	# ("mcc_label_gather_npcs", "Gather Companions"),
	("mcc_label_region", "Starting Region"),
	("mcc_empty", "{s31}"),
	("mcc_str", "STR"),
	("mcc_agi", "AGI"),
	("mcc_int", "INT"),
	("mcc_cha", "CHA"),
	("mcc_zero", "0"),
	("mcc_skl_ironflesh", "Ironflesh"),
	("mcc_skl_powerstrike", "Power Strike"),
	("mcc_skl_powerthrow", "Power Throw"),
	("mcc_skl_powerdraw", "Power Draw"),
	("mcc_skl_weaponmaster", "Weapon Master"),
	("mcc_skl_shield", "Shield"),
	("mcc_skl_athletics", "Athletics"),
	("mcc_skl_riding", "Riding"),
	("mcc_skl_horsearchery", "Horse Archery"),
	("mcc_skl_looting", "Looting"),
	# ("mcc_skl_foraging", "Foraging"),
	("mcc_skl_trainer", "Trainer"),
	("mcc_skl_tracking", "Tracking"),
	("mcc_skl_tactics", "Tactics"),
	("mcc_skl_pathfinding", "Path-finding"),
	("mcc_skl_spotting", "Spotting"),
	("mcc_skl_inventorymanagement", "Inventory Mgmt."),
	("mcc_skl_woundtreatment", "Wound Treatment"),
	("mcc_skl_surgery", "Surgery"),
	("mcc_skl_firstaid", "First Aid"),
	("mcc_skl_engineer", "Engineer"),
	("mcc_skl_persuasion", "Persuasion"),
	("mcc_skl_prisonermanagement", "Prisoner Mgmt."),
	("mcc_skl_leadership", "Leadership"),
	("mcc_skl_trade", "Trade"),
]

from util_common import *

def modmerge_strings(orig_strings):
    # add remaining strings
    from util_common import add_objects
    num_appended, num_replaced, num_ignored = add_objects(orig_strings, strings)
    #print num_appended, num_replaced, num_ignored
	
	
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "strings"
        orig_strings = var_set[var_name_1]
        modmerge_strings(orig_strings)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)