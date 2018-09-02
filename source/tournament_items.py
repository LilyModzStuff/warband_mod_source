# Tournament Play Enhancements (1.5) by Windyplains

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

tournament_items = [
# Native Versions of Items
# TPE+ 1.1 items
["red_tpe_tunic",              "Tournament Tunic", [("arena_tunic_red",0)], itp_type_body_armor|itp_covers_legs,0,1720,weight(10)|abundance(55)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0),imodbits_plate,[],[fac_kingdom_1]],
["blue_tpe_tunic",             "Tournament Tunic", [("arena_tunic_blue",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(10)|abundance(55)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
["green_tpe_tunic",            "Tournament Tunic", [("arena_tunic_green",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(10)|abundance(55)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
["gold_tpe_tunic",             "Tournament Tunic", [("arena_tunic_yellow",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(10)|abundance(55)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
["red_tpe_armor",              "Tournament Armor", [("arena_armor_red",0)], itp_type_body_armor|itp_covers_legs,0,1720,weight(22)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0),imodbits_plate,[],[fac_kingdom_1]],
["blue_tpe_armor",             "Tournament Armor", [("arena_armor_blue",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(22)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
["green_tpe_armor",            "Tournament Armor", [("arena_armor_green",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(22)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
["gold_tpe_armor",             "Tournament Armor", [("arena_armor_yellow",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(22)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
# ["red_tpe_tunic",              "Tournament Tunic", [("arena_tunicR_new",0)], itp_type_body_armor|itp_covers_legs,0,1720,weight(10)|abundance(55)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0),imodbits_plate,[],[fac_kingdom_1]],
# ["blue_tpe_tunic",             "Tournament Tunic", [("arena_tunicB_new",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(10)|abundance(55)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
# ["green_tpe_tunic",            "Tournament Tunic", [("arena_tunicG_new",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(10)|abundance(55)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
# ["gold_tpe_tunic",             "Tournament Tunic", [("arena_tunicY_new",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(10)|abundance(55)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
# ["red_tpe_armor",              "Tournament Armor", [("arena_armorR_new",0)], itp_type_body_armor|itp_covers_legs,0,1720,weight(22)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0),imodbits_plate,[],[fac_kingdom_1]],
# ["blue_tpe_armor",             "Tournament Armor", [("arena_armorB_new",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(22)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
# ["green_tpe_armor",            "Tournament Armor", [("arena_armorG_new",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(22)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
# ["gold_tpe_armor",             "Tournament Armor", [("arena_armorY_new",0)], itp_type_body_armor|itp_covers_legs,0,1544,weight(22)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
["tpe_enhanced_shield_red",    "Tournament Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(600)|body_armor(15)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["tpe_enhanced_shield_blue",   "Tournament Shield", [("arena_shield_blue",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(600)|body_armor(15)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["tpe_enhanced_shield_green",  "Tournament Shield", [("arena_shield_green",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(600)|body_armor(15)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["tpe_enhanced_shield_yellow", "Tournament Shield", [("arena_shield_yellow",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(600)|body_armor(15)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["tpe_normal_boots",           "Tournament Greaves", [("spl_greaves",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 34 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["tpe_enhanced_boots",         "Tournament Greaves", [("lthr_greaves",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 34 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
["tpe_normal_spear",           "Tournament Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear|itcf_overswing_polearm, 0 , weight(4.5)|difficulty(0)|spd_rtng(85) | weapon_length(120)|swing_damage(12 , blunt) | thrust_damage(18 ,  blunt),imodbits_polearm ],
["tpe_enhanced_spear",         "Tournament Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear|itcf_overswing_polearm, 0 , weight(4.5)|difficulty(0)|spd_rtng(85) | weapon_length(140)|swing_damage(18 , blunt) | thrust_damage(27 ,  blunt),imodbits_polearm ],
["tpe_normal_bow",             "Tournament Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(24, blunt),imodbits_bow ],
["tpe_enhanced_bow",           "Tournament Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(95) | shoot_speed(40) | thrust_damage(36, blunt),imodbits_bow ],
["tpe_normal_crossbow",        "Tournament Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(50)| shoot_speed(68) | thrust_damage(30,blunt)|max_ammo(1),imodbits_crossbow],
["tpe_enhanced_crossbow",      "Tournament Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(60)| shoot_speed(68) | thrust_damage(45,blunt)|max_ammo(1),imodbits_crossbow],
["tpe_normal_javelin",         "Tournament Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(100) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown],
["tpe_normal_javelin_melee",   "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(90) |swing_damage(12, blunt)| thrust_damage(16,  blunt)|weapon_length(75),imodbits_polearm ],
["tpe_enhanced_javelin",       "Tournament Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(100) | shoot_speed(28) | thrust_damage(40, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown],
["tpe_enhanced_javelin_melee", "Tournament Javelin Melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(95) |swing_damage(12, blunt)| thrust_damage(22,  blunt)|weapon_length(90),imodbits_polearm ],
["tpe_normal_sword",           "Tournament Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(95)|weapon_length(90)|swing_damage(18,blunt)|thrust_damage(16,blunt),imodbits_none],
["tpe_enhanced_sword",         "Tournament Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 243 , weight(1.5)|spd_rtng(105) | weapon_length(100)|swing_damage(27 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],
["tpe_normal_greatsword",      "Tournament Greatsword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword, 21, weight(6.25)|spd_rtng(80)|weapon_length(110)|swing_damage(27,blunt)|thrust_damage(22,blunt),imodbits_none],
["tpe_enhanced_greatsword",    "Tournament Greatsword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 670 , weight(2.75)|spd_rtng(90) | weapon_length(120)|swing_damage(40 , blunt) | thrust_damage(27 ,  blunt),imodbits_sword_high ],
["tpe_normal_lance",           "Tournament Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_greatlance, 18, weight(4.25) |spd_rtng(70)|weapon_length(200)|swing_damage(10,blunt)|thrust_damage(15,blunt),imodbits_none],
["tpe_enhanced_lance",         "Tournament Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_greatlance, 90 , weight(4.25)|spd_rtng(75) | weapon_length(240)|swing_damage(15 , blunt) | thrust_damage(23 ,  blunt),imodbits_none ],
["tpe_normal_horse_red",       "Tournament Horse", [("ho_vae_long_royalred",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(100)|body_armor(15)|difficulty(0)|horse_speed(45)|horse_maneuver(41)|horse_charge(10)|horse_scale(110),imodbits_horse_basic],
["tpe_normal_horse_blue",      "Tournament Horse", [("ho_nor_war_bluebarded",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(100)|body_armor(15)|difficulty(0)|horse_speed(45)|horse_maneuver(41)|horse_charge(10)|horse_scale(110),imodbits_horse_basic],
["tpe_normal_horse_green",     "Tournament Horse", [("ho_rho_war_deergreen",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(100)|body_armor(15)|difficulty(0)|horse_speed(45)|horse_maneuver(41)|horse_charge(10)|horse_scale(110),imodbits_horse_basic],
["tpe_normal_horse_yellow",    "Tournament Horse", [("ho_sar_war_yellowroyal",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(100)|body_armor(15)|difficulty(0)|horse_speed(45)|horse_maneuver(41)|horse_charge(10)|horse_scale(110),imodbits_horse_basic],
["tpe_enhanced_horse_red",     "Tournament Warhorse", [("ho_vae_long_royalred",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(165)|body_armor(40)|difficulty(0)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
["tpe_enhanced_horse_blue",    "Tournament Warhorse", [("ho_nor_war_bluebarded",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(165)|body_armor(40)|difficulty(0)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
["tpe_enhanced_horse_green",   "Tournament Warhorse", [("ho_rho_war_deergreen",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(165)|body_armor(40)|difficulty(0)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
["tpe_enhanced_horse_yellow",  "Tournament Warhorse", [("ho_sar_war_yellowroyal",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(165)|body_armor(40)|difficulty(0)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
# ["tpe_normal_horse_red",       "Tournament Horse", [("ho_vae_long_royalred",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(100)|body_armor(15)|difficulty(0)|horse_speed(45)|horse_maneuver(41)|horse_charge(10)|horse_scale(110),imodbits_horse_basic],
# ["tpe_normal_horse_blue",      "Tournament Horse", [("ho_nor_war_bluebarded",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(100)|body_armor(15)|difficulty(0)|horse_speed(45)|horse_maneuver(41)|horse_charge(10)|horse_scale(110),imodbits_horse_basic],
# ["tpe_normal_horse_green",     "Tournament Horse", [("ho_rho_war_deergreen",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(100)|body_armor(15)|difficulty(0)|horse_speed(45)|horse_maneuver(41)|horse_charge(10)|horse_scale(110),imodbits_horse_basic],
# ["tpe_normal_horse_yellow",    "Tournament Horse", [("ho_sar_war_yellowroyal",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(100)|body_armor(15)|difficulty(0)|horse_speed(45)|horse_maneuver(41)|horse_charge(10)|horse_scale(110),imodbits_horse_basic],
# ["tpe_enhanced_horse_red",     "Tournament Warhorse", [("ho_vae_long_royalred",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(165)|body_armor(40)|difficulty(0)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
# ["tpe_enhanced_horse_blue",    "Tournament Warhorse", [("ho_nor_war_bluebarded",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(165)|body_armor(40)|difficulty(0)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
# ["tpe_enhanced_horse_green",   "Tournament Warhorse", [("ho_rho_war_deergreen",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(165)|body_armor(40)|difficulty(0)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
# ["tpe_enhanced_horse_yellow",  "Tournament Warhorse", [("ho_sar_war_yellowroyal",0)], itp_type_horse, 0, 1224,abundance(50)|hit_points(165)|body_armor(40)|difficulty(0)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
# TPE+ 1.4 items
["tpe_normal_axe",             "Tournament Axe", [("we_sar_axe_onehanded",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(90) | weapon_length(70) | swing_damage(20, blunt) | thrust_damage(0, pierce), imodbits_axe],
["tpe_enhanced_axe",           "Tournament Axe", [("we_sar_axe_onehanded",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(95) | weapon_length(75) | swing_damage(28, blunt) | thrust_damage(0, pierce), imodbits_axe],
["tpe_normal_quarterstaff",    "Tournament Staff", [("we_sar_spear_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(110) | weapon_length(118)|swing_damage(22, blunt) | thrust_damage(18,blunt),imodbits_none],
["tpe_enhanced_quarterstaff",  "Tournament Staff", [("we_sar_spear_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(115) | weapon_length(118)|swing_damage(31, blunt) | thrust_damage(25,blunt),imodbits_none],
["tpe_normal_greataxe",        "Tournament Greataxe", [("tutorial_battle_axe",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(85) | weapon_length(108)|swing_damage(27 , blunt) | thrust_damage(0 ,  blunt),imodbits_axe ],
["tpe_enhanced_greataxe",      "Tournament Greataxe", [("tutorial_battle_axe",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(90) | weapon_length(108)|swing_damage(38 , blunt) | thrust_damage(0 ,  blunt),imodbits_axe ],
["tpe_normal_scimitar",        "Tournament Scimitar", [("we_sar_sword_scimitar",0),("we_sar_scabbard_scimitar", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,411,weight(1.5)|abundance(60)|difficulty(8)|spd_rtng(100)|weapon_length(97)|swing_damage(16, blunt)|thrust_damage(0, blunt),imodbits_sword_high],
["tpe_enhanced_scimitar",      "Tournament Scimitar", [("we_sar_sword_scimitar",0),("we_sar_scabbard_scimitar", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,411,weight(1.5)|abundance(60)|difficulty(8)|spd_rtng(108)|weapon_length(97)|swing_damage(22, blunt)|thrust_damage(0, blunt),imodbits_sword_high],
["tpe_normal_throwing_axe",    "Tournament Throwing Axes", [("we_nor_axe_throw_light",0)], itp_type_thrown|itp_primary|itp_next_item_as_melee,itcf_throw_axe,100,weight(5)|abundance(100)|difficulty(0)|spd_rtng(85)|shoot_speed(18)|thrust_damage(30, blunt)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy],
	["tpe_normal_throwing_axe_melee", "Tournament Throwing Axe", [("we_nor_axe_throw_light",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield,itc_scimitar,100,weight(1)|abundance(100)|difficulty(0)|spd_rtng(90)|weapon_length(53)|swing_damage(27, blunt),imodbits_thrown_minus_heavy],
["tpe_enhanced_throwing_axe",  "Tournament Throwing Axes", [("we_nor_axe_throw_light",0)], itp_type_thrown|itp_primary|itp_next_item_as_melee,itcf_throw_axe,100,weight(5)|abundance(100)|difficulty(0)|spd_rtng(85)|shoot_speed(18)|thrust_damage(42, blunt)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy],
	["tpe_enhanced_throwing_axe_melee", "Tournament Throwing Axe", [("we_nor_axe_throw_light",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield,itc_scimitar,100,weight(1)|abundance(100)|difficulty(0)|spd_rtng(95)|weapon_length(63)|swing_damage(38, blunt),imodbits_thrown_minus_heavy],
["tpe_normal_throwing_daggers",   "Tournament Daggers", [("practice_dagger",0)], itp_type_thrown |itp_primary|itp_next_item_as_melee ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(100) | shoot_speed(25) | thrust_damage(16 , blunt)|max_ammo(25)|weapon_length(0),imodbits_missile],
	["tpe_normal_throwing_daggers_melee","Practice Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(14, blunt)|thrust_damage(14, blunt),imodbits_none],
["tpe_enhanced_throwing_daggers", "Tournament Daggers", [("practice_dagger",0)], itp_type_thrown |itp_primary|itp_next_item_as_melee ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(110) | shoot_speed(25) | thrust_damage(22 , blunt)|max_ammo(25)|weapon_length(0),imodbits_missile],
	["tpe_enhanced_throwing_daggers_melee","Practice Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(115)|weapon_length(47)|swing_damage(20, blunt)|thrust_damage(20, blunt),imodbits_none],
## TOURNAMENT PLAY ENHANCEMENTS end
]
		
from util_common import *
from util_wrappers import *

def modmerge_items(orig_items):
    pos = list_find_first_match_i(orig_items, "items_end")
    OpBlockWrapper(orig_items).InsertBefore(pos, tournament_items)	
	
def modmerge(var_set):
    try:
        var_name_1 = "items"
        orig_items = var_set[var_name_1]
        modmerge_items(orig_items)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)