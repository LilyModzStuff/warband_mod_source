# Companions Overview by Lav
# Modmerger compilation by Windyplains

strings = [
####################################################################################################################################
# LAV MODIFICATIONS START (COMPANIONS OVERSEER MOD)
####################################################################################################################################

  # Version string
  ("lco_version", "Companions Overseer v. 1.20"),

  # Interface element strings
  ("lco_i_return",           "Return"),
  ("lco_i_attributes",       "View Attributes"),
  ("lco_i_equipment",        "View Equipment"),
  ("lco_i_ae_with",          "Auto-Equip Companions With:"),
  ("lco_i_ae_with_horses",   "Horses"),
  ("lco_i_ae_with_armors",   "Armors"),
  ("lco_i_ae_with_shields",  "Shields"),
  ("lco_i_ae_companion",     "Equip Companion"),
  ("lco_i_ae_everyone",      "Equip Everyone"),
  ("lco_i_title_companions", "Companions"),
  ("lco_i_list_companions",  "List Companions"),
  ("lco_i_list_lords",       "List Kingdom Lords"),
  ("lco_i_list_regulars",    "List Regular Troops"),
  ("lco_i_hero_panel_title", "Accessible Companions"),
  ("lco_i_weapons",          "Weapons:"),
  ("lco_i_armor",            "Armor:"),
  ("lco_i_horse",            "Horse:"),
  ("lco_i_books",            "Books"),
  ("lco_i_inventory",        "Inventory:"),
  ("lco_i_discard",          "Discard/Loot:"),
  ("lco_i_retrieve",         "Retrieve All Items"),
  ("lco_i_denars",           "{reg60} denar(s)"), # No longer used as of V1.20
  ("lco_i_character",        "Character Screen"),
  ("lco_i_ie_icon",          "I/E"),

  # Slot name strings
  ("lco_slot_name_0", "(weapon slot)"),
  ("lco_slot_name_1", "(weapon slot)"),
  ("lco_slot_name_2", "(weapon slot)"),
  ("lco_slot_name_3", "(weapon slot)"),
  ("lco_slot_name_4", "(helm slot)"),
  ("lco_slot_name_5", "(armor slot)"),
  ("lco_slot_name_6", "(boots slot)"),
  ("lco_slot_name_7", "(gauntlets slot)"),
  ("lco_slot_name_8", "(horse slot)"),
  ("lco_slot_name_9", "(book slot)"),
  ("lco_slot_name_A", "(book slot)"),
  ("lco_slot_frozen", "(frozen)"),

  # Messages and error strings
  ("lco_error_drop_first", "Please deposit currently dragged item somewhere first."),
  ("lco_message_hero_ae", "{s41} has equipped {reg60?her:him}self from your inventory."),
  ("lco_message_all_heroes_ae", "Your companions have equipped themselves from your inventory."),
  ("lco_message_hero_no_need", "{s40} has no need for {s41}."),
  ("lco_error_inv_full", "Cannot give item to player, inventory is full."),
  ("lco_message_hero_replaced", "{s40} replaced {reg4?her:his} {s41} with {s39}."),
  ("lco_message_hero_equipped", "{s40} equipped {s41}."),
  ("lco_message_nobody_needs", "Nobody wants to take {s41}."),
  ("lco_drop_error_type", "You cannot drop this item here!"),
  ("lco_drop_error_reqs", "Item prerequisites are not met to equip it!"),
  ("lco_drop_error_control", "You cannot control this troop's equipment."),
  ("lco_impossible_error", "SCRIPT ERROR #001: NO SWAP ITEM FOUND."),

  # Functional strings
  ("lco_drop_here", "Drop items here to discard them.^Currently {reg0} item(s) discarded."),
  ("lco_s40", "{s40}"),
  ("lco_reg40", "{reg40}"),
  ("lco_reg40_41", "{reg40}/{reg41}"),
  ("lco_s42_s41", "{s42} {s41}"),
  ("lco_s41_reg60_reg61", "{s41} ({reg60}/{reg61})"),
  ("lco_s41_reg60", "{s41} ({reg60})"),

  # Modifier name strings
  ("item_imod_name_0", "Plain"),
  ("item_imod_name_1", "Cracked"),
  ("item_imod_name_2", "Rusty"),
  ("item_imod_name_3", "Bent"),
  ("item_imod_name_4", "Chipped"),
  ("item_imod_name_5", "Battered"),
  ("item_imod_name_6", "Poor"),
  ("item_imod_name_7", "Crude"),
  ("item_imod_name_8", "Old"),
  ("item_imod_name_9", "Cheap"),
  ("item_imod_name_10", "Fine"),
  ("item_imod_name_11", "Well Made"),
  ("item_imod_name_12", "Sharp"),
  ("item_imod_name_13", "Balanced"),
  ("item_imod_name_14", "Tempered"),
  ("item_imod_name_15", "Deadly"),
  ("item_imod_name_16", "Exquisite"),
  ("item_imod_name_17", "Masterwork"),
  ("item_imod_name_18", "Heavy"),
  ("item_imod_name_19", "Strong"),
  ("item_imod_name_20", "Powerful"),
  ("item_imod_name_21", "Tattered"),
  ("item_imod_name_22", "Ragged"),
  ("item_imod_name_23", "Rough"),
  ("item_imod_name_24", "Sturdy"),
  ("item_imod_name_25", "Thick"),
  ("item_imod_name_26", "Hardened"),
  ("item_imod_name_27", "Reinforced"),
  ("item_imod_name_28", "Superb"),
  ("item_imod_name_29", "Lordly"),
  ("item_imod_name_30", "Lame"),
  ("item_imod_name_31", "Swaybacked"),
  ("item_imod_name_32", "Stubborn"),
  ("item_imod_name_33", "Timid"),
  ("item_imod_name_34", "Meek"),
  ("item_imod_name_35", "Spirited"),
  ("item_imod_name_36", "Champion"),
  ("item_imod_name_37", "Fresh"),
  ("item_imod_name_38", "Day-old"),
  ("item_imod_name_39", "Two Days-old"),
  ("item_imod_name_40", "Smelling"),
  ("item_imod_name_41", "Rotten"),
  ("item_imod_name_42", "Large Bag of"),

  # Attribute/skill/proficiency name strings
  ("lco_c_level", "Level"),
  ("lco_c_xp", "XP"),
  ("lco_c_xp2next_level", "XP to Next Lvl"),
  ("lco_c_hp", "HP/Max HP"),
  ("lco_c_morale", "Morale"),
  ("lco_c_str", "Strength"),
  ("lco_c_agi", "Agility"),
  ("lco_c_int", "Intelligence"),
  ("lco_c_cha", "Charisma"),
  ("lco_c_ironflesh", "Ironflesh"),
  ("lco_c_pstrike", "Power Strike"),
  ("lco_c_pthrow", "Power Throw"),
  ("lco_c_pdraw", "Power Draw"),
  ("lco_c_wmaster", "Weapon Master"),
  ("lco_c_shield", "Shield"),
  ("lco_c_athletics", "Athletics"),
  ("lco_c_riding", "Riding"),
  ("lco_c_harchery", "Horse Archery"),
  ("lco_c_looting", "Looting"),
  ("lco_c_trainer", "Trainer"),
  ("lco_c_tracking", "Tracking"),
  ("lco_c_tactics", "Tactics"),
  ("lco_c_pathfinding", "Pathfinding"),
  ("lco_c_spotting", "Spotting"),
  ("lco_c_invmanage", "Inventory Mngmt"),
  ("lco_c_woundtreat", "Wound Trtmnt"),
  ("lco_c_surgery", "Surgery"),
  ("lco_c_firstaid", "First Aid"),
  ("lco_c_engineer", "Engineer"),
  ("lco_c_persuasion", "Persuasion"),
  ("lco_c_pmanage", "Prisoner Mngmt"),
  ("lco_c_leadership", "Leadership"),
  ("lco_c_trade", "Trade"),
  ("lco_c_1hw", "1H Weapons"),
  ("lco_c_2hw", "2H Weapons"),
  ("lco_c_polearms", "Polearms"),
  ("lco_c_bows", "Archery"),
  ("lco_c_xbows", "Crossbows"),
  ("lco_c_throwing", "Throwing"),

####################################################################################################################################
# LAV MODIFICATIONS END (COMPANIONS OVERSEER MOD)
####################################################################################################################################
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