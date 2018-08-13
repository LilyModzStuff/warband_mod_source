# Tournament Play Enhancements (1.1) by Windyplains
# Released 9/2/2011

from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *
from module_items import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
## TOURNAMENT PLAY ENHANCEMENTS (1.1) begin - Windyplains (items not created by me)
["red_tpe_tunic",              "Tournament Tunic", [("arena_tunicR_new",0)], itp_type_body_armor|itp_covers_legs,0,1720,weight(10)|abundance(55)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0),imodbits_plate,[],[fac_kingdom_1]],
["blue_tpe_tunic",             "Tournament Tunic", [("arena_tunicB_new",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(10)|abundance(55)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
["green_tpe_tunic",            "Tournament Tunic", [("arena_tunicG_new",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(10)|abundance(55)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
["gold_tpe_tunic",             "Tournament Tunic", [("arena_tunicY_new",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(10)|abundance(55)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
["red_tpe_armor",              "Tournament Armor", [("arena_armorR_new",0)], itp_type_body_armor|itp_covers_legs,0,1720,weight(22)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0),imodbits_plate,[],[fac_kingdom_1]],
["blue_tpe_armor",             "Tournament Armor", [("arena_armorB_new",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(22)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
["green_tpe_armor",            "Tournament Armor", [("arena_armorG_new",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(22)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
["gold_tpe_armor",             "Tournament Armor", [("arena_armorY_new",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(22)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
["tpe_enhanced_shield_red",    "Tournament Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(600)|body_armor(15)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["tpe_enhanced_shield_blue",   "Tournament Shield", [("arena_shield_blue",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(600)|body_armor(15)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["tpe_enhanced_shield_green",  "Tournament Shield", [("arena_shield_green",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(600)|body_armor(15)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["tpe_enhanced_shield_yellow", "Tournament Shield", [("arena_shield_yellow",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(600)|body_armor(15)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["tpe_normal_boots",           "Tournament Greaves", [("spl_greaves",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 34 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["tpe_enhanced_boots",         "Tournament Greaves", [("lthr_greaves",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 34 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
["tpe_normal_spear",           "Tournament Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(95) | weapon_length(120)|swing_damage(10 , blunt) | thrust_damage(15 ,  blunt),imodbits_polearm ],
["tpe_enhanced_spear",         "Tournament Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(70) | weapon_length(150)|swing_damage(15 , blunt) | thrust_damage(23 ,  blunt),imodbits_polearm ],
["tpe_normal_bow",             "Tournament Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(24, blunt),imodbits_bow ],
["tpe_enhanced_bow",           "Tournament Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(95) | shoot_speed(40) | thrust_damage(36, blunt),imodbits_bow ],
["tpe_normal_crossbow",        "Tournament Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(50)| shoot_speed(68) | thrust_damage(30,blunt)|max_ammo(1),imodbits_crossbow],
["tpe_enhanced_crossbow",      "Tournament Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(60)| shoot_speed(68) | thrust_damage(45,blunt)|max_ammo(1),imodbits_crossbow],
["tpe_normal_javelin",         "Tournament Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(100) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown],
["tpe_normal_javelin_melee",   "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(16,  blunt)|weapon_length(75),imodbits_polearm ],
["tpe_enhanced_javelin",       "Tournament Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(100) | shoot_speed(28) | thrust_damage(40, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown],
["tpe_enhanced_javelin_melee", "Tournament Javelin Melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(22,  blunt)|weapon_length(75),imodbits_polearm ],
["tpe_normal_sword",           "Tournament Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(100)|weapon_length(90)|swing_damage(18,blunt)|thrust_damage(16,blunt),imodbits_none],
["tpe_enhanced_sword",         "Tournament Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 243 , weight(1.5)|spd_rtng(105) | weapon_length(90)|swing_damage(27 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],
["tpe_normal_greatsword",      "Tournament Greatsword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword, 21, weight(6.25)|spd_rtng(90)|weapon_length(120)|swing_damage(27,blunt)|thrust_damage(22,blunt),imodbits_none],
["tpe_enhanced_greatsword",    "Tournament Greatsword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 670 , weight(2.75)|spd_rtng(90) | weapon_length(120)|swing_damage(40 , blunt) | thrust_damage(27 ,  blunt),imodbits_sword_high ],
["tpe_normal_lance",           "Tournament Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_greatlance, 18, weight(4.25) |spd_rtng(58)|weapon_length(240)|swing_damage(10,blunt)|thrust_damage(15,blunt),imodbits_none],
["tpe_enhanced_lance",         "Tournament Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_greatlance, 90 , weight(4.25)|spd_rtng(70) | weapon_length(240)|swing_damage(15 , blunt) | thrust_damage(23 ,  blunt),imodbits_none ],
## TOURNAMENT PLAY ENHANCEMENTS end
]

from util_common import *

def modmerge_items(orig_items):
    # add remaining meshes
    from util_common import add_objects
    num_appended, num_replaced, num_ignored = add_objects(orig_items, items)
    #print num_appended, num_replaced, num_ignored
	
	
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "items"
        orig_items = var_set[var_name_1]
        modmerge_items(orig_items)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)