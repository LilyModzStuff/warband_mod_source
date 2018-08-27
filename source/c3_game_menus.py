from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *


game_menus = [
	
	#######################################################
	("start_game_0",mnf_disable_all_keys,"Terminal","none",
		[
			(try_begin),
				(eq, "$quit_status", 1),
				(change_screen_quit),
			(else_try),
				(call_script,"script_c3_defaults"),
				(jump_to_menu, "mnu_c3_initialize"),
			(try_end),
		],[]
	),
	
	########################################
	("c3_initialize",0,"Initializing","none", 
		[
		(assign,"$g_talk_troop","trp_player"),
		#assigning attributes, skills, and proficiencies to a reg
		(store_attribute_level, reg1,"$g_talk_troop",ca_strength),
		(store_attribute_level, reg2,"$g_talk_troop",ca_agility),
		(store_attribute_level, reg3,"$g_talk_troop",ca_intelligence),
		(store_attribute_level, reg4,"$g_talk_troop",ca_charisma),
		(store_skill_level,reg6,skl_ironflesh,"$g_talk_troop"),
		(store_skill_level,reg7,skl_power_strike,"$g_talk_troop"),
		(store_skill_level,reg8,skl_power_throw,"$g_talk_troop"),
		(store_skill_level,reg9,skl_power_draw,"$g_talk_troop"),
		(store_skill_level,reg10,skl_weapon_master,"$g_talk_troop"),
		(store_skill_level,reg11,skl_shield,"$g_talk_troop"),
		(store_skill_level,reg12,skl_athletics,"$g_talk_troop"),
		(store_skill_level,reg13,skl_riding,"$g_talk_troop"),
		(store_skill_level,reg14,skl_horse_archery,"$g_talk_troop"),
		(store_skill_level,reg15,skl_looting,"$g_talk_troop"),
		(store_skill_level,reg16,skl_trainer,"$g_talk_troop"),
		(store_skill_level,reg17,skl_tracking,"$g_talk_troop"),
		(store_skill_level,reg18,skl_tactics,"$g_talk_troop"),
		(store_skill_level,reg19,skl_pathfinding,"$g_talk_troop"),
		(store_skill_level,reg20,skl_spotting,"$g_talk_troop"),
		(store_skill_level,reg21,skl_inventory_management,"$g_talk_troop"),
		(store_skill_level,reg22,skl_wound_treatment,"$g_talk_troop"),
		(store_skill_level,reg23,skl_surgery,"$g_talk_troop"),
		(store_skill_level,reg24,skl_first_aid,"$g_talk_troop"),
		(store_skill_level,reg25,skl_engineer,"$g_talk_troop"),
		(store_skill_level,reg26,skl_persuasion,"$g_talk_troop"),
		(store_skill_level,reg27,skl_prisoner_management,"$g_talk_troop"),
		(store_skill_level,reg28,skl_leadership,"$g_talk_troop"),
		(store_skill_level,reg29,skl_trade,"$g_talk_troop"),
		(assign,reg41,60), #proficiency base level that free points can be added up to
		(store_proficiency_level,reg35,"$g_talk_troop",wpt_one_handed_weapon),
		(store_proficiency_level,reg36,"$g_talk_troop",wpt_two_handed_weapon),
		(store_proficiency_level,reg37,"$g_talk_troop",wpt_polearm),
		(store_proficiency_level,reg38,"$g_talk_troop",wpt_archery),
		(store_proficiency_level,reg39,"$g_talk_troop",wpt_crossbow),
		(store_proficiency_level,reg40,"$g_talk_troop",wpt_throwing),
		
		(assign, reg0, 14), # unassigned attribute pts
		(assign, reg5, 14), # unassigned skill pts
		(assign, reg34,10), # unassigned proficiency pts
		
		(start_presentation, "prsnt_custom_character_creation"),
		],[]),
	
	#####################################################
	("c3_finalize",mnf_disable_all_keys,"Finalize","none",
		[
			(set_show_messages, 0),
			
			#gender
			(try_begin),#Man
				(eq,"$character_gender",0),
				(troop_set_type,"trp_player", 0),
				(assign,"$character_gender",tf_male),
			(else_try),#Woman
				(troop_set_type,"trp_player", 1),
				(assign, "$character_gender", tf_female),
			(try_end),
			
			(try_begin),
				(eq,"$c3_status",0), #monarch (kingdom)
				(call_script, "script_change_player_right_to_rule",25),
				(troop_set_slot,"trp_player", slot_troop_renown,500),
				(call_script,"script_change_player_honor",3),
				
				#gold and gear
				(troop_add_gold,"trp_player",25000),
				(troop_add_item,"trp_player","itm_light_lance",0),
				(troop_add_item, "trp_player","itm_saddle_horse",0),
				(troop_add_item, "trp_player","itm_hunting_crossbow",0),
				(troop_add_item, "trp_player","itm_bolts",0),
				(troop_add_item,"trp_player","itm_brigandine_red",0),
				(troop_add_item,"trp_player","itm_khergit_war_helmet",0),
				(troop_add_item,"trp_player","itm_mail_chausses",0),
				(troop_add_item,"trp_player","itm_mail_mittens",0),
				(troop_add_item,"trp_player","itm_tab_shield_round_d",0),
				(troop_add_item,"trp_player","itm_sword_medieval_c",0),
				
				#food
				(troop_add_item,"trp_player","itm_smoked_fish",0),
				(troop_add_item,"trp_player","itm_bread",0),
				(troop_add_item,"trp_player","itm_sausages",0),
				(troop_add_item,"trp_player","itm_dried_meat",0),
				(troop_add_item,"trp_player","itm_apples",0),
				(troop_add_item,"trp_player","itm_grain",0),
				(troop_add_item,"trp_player","itm_cabbages",0),
				
			(else_try),
				(eq,"$c3_status",1), #monarch (principality)
				(call_script, "script_change_player_right_to_rule",10),
				(troop_set_slot,"trp_player", slot_troop_renown,300),
				(call_script,"script_change_player_honor",3),
				
				#gold and gear
				(troop_add_gold,"trp_player",13500),
				(troop_add_item,"trp_player","itm_padded_leather",0),
				(troop_add_item,"trp_player","itm_leather_gloves",0),
				(troop_add_item,"trp_player","itm_footman_helmet",0),
				(troop_add_item,"trp_player","itm_leather_boots",0),
				(troop_add_item,"trp_player","itm_tab_shield_round_c",0),
				(troop_add_item,"trp_player","itm_light_lance",0),
				(troop_add_item, "trp_player","itm_saddle_horse",0),
				(troop_add_item,"trp_player","itm_sword_medieval_b",0),
				(troop_add_item, "trp_player","itm_hunting_crossbow",0),
				(troop_add_item, "trp_player","itm_bolts",0),
				
				#food
				(troop_add_item,"trp_player","itm_smoked_fish",0),
				(troop_add_item,"trp_player","itm_bread",0),
				(troop_add_item,"trp_player","itm_sausages",0),
				(troop_add_item,"trp_player","itm_dried_meat",0),
				
			(else_try),
				(eq,"$c3_status",2), #vassal lord
				(troop_set_slot,"trp_player",slot_troop_renown,160),
				(call_script,"script_change_player_honor", 3),
				
				#gold and gear
				(troop_add_gold,"trp_player",1000),
				(troop_add_item,"trp_player","itm_red_gambeson",0),
				(troop_add_item,"trp_player","itm_skullcap",0),
				(troop_add_item,"trp_player","itm_leather_boots",0),
				(troop_add_item,"trp_player","itm_tab_shield_round_b",0),
				(troop_add_item,"trp_player","itm_light_lance",0),
				(troop_add_item, "trp_player","itm_saddle_horse",0),
				(troop_add_item,"trp_player","itm_sword_medieval_a",0),
				(troop_add_item, "trp_player","itm_hunting_crossbow",0),
				(troop_add_item, "trp_player","itm_bolts",0),
				
				#food
				(troop_add_item,"trp_player","itm_bread",0),
				(troop_add_item,"trp_player","itm_dried_meat",0),
			
			(else_try),
				(eq,"$c3_status",3), #free lord
				(eq,"$character_gender",0), #man
				(troop_set_slot, "trp_player", slot_troop_renown, 100),
				
				#gold and gear
				(troop_add_gold, "trp_player", 500),
				(troop_add_item, "trp_player","itm_leather_cap",0),
				(troop_add_item, "trp_player","itm_ankle_boots",0),
				(troop_add_item, "trp_player","itm_tabard",0),
				(troop_add_item, "trp_player","itm_saddle_horse",0),
				(troop_add_item, "trp_player","itm_sword_medieval_b_small",0),
				(troop_add_item, "trp_player","itm_tab_shield_round_a",0),
				(troop_add_item, "trp_player","itm_hunting_crossbow",0),
				(troop_add_item, "trp_player","itm_bolts",0),
				
				#food
				(troop_add_item,"trp_player","itm_dried_meat",0),
				
			(else_try),
				(eq,"$c3_status",3), #free lord
				(eq,"$character_gender",1), #woman
				(troop_set_slot, "trp_player", slot_troop_renown, 75),
				
				#gold and gear
				(troop_add_gold, "trp_player", 300),
				(troop_add_item, "trp_player","itm_blue_hose",0),
				(troop_add_item, "trp_player","itm_sarranid_dress_a",0),
				(troop_add_item, "trp_player","itm_saddle_horse",0),
				(troop_add_item, "trp_player","itm_dagger",0),
				(troop_add_item, "trp_player","itm_hunting_crossbow",0),
				(troop_add_item, "trp_player","itm_bolts",0),
				
				#food
				(troop_add_item,"trp_player","itm_dried_meat",0),
				
			(else_try),
				(eq,"$c3_status",4), #commoner
				(eq,"$character_gender",0), #man
				(troop_set_slot, "trp_player", slot_troop_renown, 30),
				
				#gold and gear
				(troop_add_gold, "trp_player", 75),
				(troop_add_item, "trp_player","itm_wrapping_boots",0),
				(troop_add_item, "trp_player","itm_coarse_tunic",0),
				(troop_add_item, "trp_player","itm_sumpter_horse",0),
				(troop_add_item, "trp_player","itm_hatchet",0),
				(troop_add_item, "trp_player","itm_hunting_bow",0),
				(troop_add_item, "trp_player","itm_arrows",0),
				
				#food
				(troop_add_item, "trp_player","itm_bread",0),
				
			(else_try),
				(eq,"$c3_status",4), #commoner
				(eq,"$character_gender",1), #woman
				
				#gold and gear
				(troop_add_gold, "trp_player", 50),
				(troop_add_item, "trp_player","itm_woolen_hose",0),
				(troop_add_item, "trp_player","itm_dress",0),
				(troop_add_item, "trp_player","itm_sumpter_horse",0),
				(troop_add_item, "trp_player","itm_cleaver",0),
				(troop_add_item, "trp_player","itm_pitch_fork",0),
				
				#food
				(troop_add_item,"trp_player","itm_bread",0),
				
			(try_end),
			
			# if nobility, assign banner
			(try_begin),
				(this_or_next|eq,"$c3_status", 0),
				(this_or_next|eq,"$c3_status", 1),
				(this_or_next|eq,"$c3_status", 2),
				(eq, "$c3_status", 3),
				(jump_to_menu, "mnu_auto_return"),
		(jump_to_menu, "mnu_choose_banner"),
                        (else_try),
				(jump_to_menu, "mnu_auto_return"),
			(try_end),
			(set_show_messages, 1),
		],[]),
]

c3_redirect = [
	
	(set_show_messages, 0),
	(try_begin),
		(eq,"$c3_status",0),#monarch (kingdom)
			#kingdom setup
			(try_begin),
				(eq, "$c3_start", 5), #swadia
				(call_script,"script_c3_kingdom_monarch_of","fac_kingdom_1"),
			(else_try),
				(eq, "$c3_start", 4), #vaegir
				(call_script,"script_c3_kingdom_monarch_of","fac_kingdom_2"),
			(else_try),
				(eq, "$c3_start", 3), #khergit
				(call_script,"script_c3_kingdom_monarch_of","fac_kingdom_3"),
			(else_try),
				(eq, "$c3_start", 2), #nord
				(call_script,"script_c3_kingdom_monarch_of","fac_kingdom_4"),
			(else_try),
				(eq, "$c3_start", 1), #rhodok
				(call_script,"script_c3_kingdom_monarch_of","fac_kingdom_5"),
			(else_try),
				(eq, "$c3_start", 0), #sarranid
				(call_script,"script_c3_kingdom_monarch_of","fac_kingdom_6"),
			(try_end),
		(set_show_messages, 1),
		(start_presentation,"prsnt_c3_kingdom_finalize"),
	(else_try),
		(eq,"$c3_status",1),#monarch (principality)
			#kingdom setup
			(try_begin),
				(eq, "$c3_start", 5), #swadia
				(call_script,"script_c3_principality_monarch_in","fac_kingdom_1"),
			(else_try),
				(eq, "$c3_start", 4), #vaegir
				(call_script,"script_c3_principality_monarch_in","fac_kingdom_2"),
			(else_try),
				(eq, "$c3_start", 3), #khergit
				(call_script,"script_c3_principality_monarch_in","fac_kingdom_3"),
			(else_try),
				(eq, "$c3_start", 2), #nord
				(call_script,"script_c3_principality_monarch_in","fac_kingdom_4"),
			(else_try),
				(eq, "$c3_start", 1), #rhodok
				(call_script,"script_c3_principality_monarch_in","fac_kingdom_5"),
			(else_try),
				(eq, "$c3_start", 0), #sarranid
				(call_script,"script_c3_principality_monarch_in","fac_kingdom_6"),
			(try_end),
		(set_show_messages, 1),
		(start_presentation,"prsnt_c3_kingdom_finalize"),
		
	(else_try),
		(eq,"$c3_status",2),#vassal
		#kingdom setup
			(try_begin),
				(eq, "$c3_start", 5), #swadia
				(call_script,"script_c3_vassal_in","fac_kingdom_1"),
			(else_try),
				(eq, "$c3_start", 4), #vaegir
				(call_script,"script_c3_vassal_in","fac_kingdom_2"),
			(else_try),
				(eq, "$c3_start", 3), #khergit
				(call_script,"script_c3_vassal_in","fac_kingdom_3"),
			(else_try),
				(eq, "$c3_start", 2), #nord
				(call_script,"script_c3_vassal_in","fac_kingdom_4"),
			(else_try),
				(eq, "$c3_start", 1), #rhodok
				(call_script,"script_c3_vassal_in","fac_kingdom_5"),
			(else_try),
				(eq, "$c3_start", 0), #sarranid
				(call_script,"script_c3_vassal_in","fac_kingdom_6"),
			(try_end),
		(set_show_messages, 1),
		(change_screen_return),
		
	(else_try),
		(this_or_next|eq,"$c3_status",3),
		(eq,"$c3_status",4),
		(try_begin),
			(eq, "$c3_start", 5), #swadia - praven
			(party_relocate_near_party, "p_main_party","p_town_6", 2),
		(else_try),
			(eq, "$c3_start", 4), #vaegir - reyvadin
			(party_relocate_near_party, "p_main_party","p_town_8", 2),
		(else_try),
			(eq, "$c3_start", 3), #khergit - tulga
			(party_relocate_near_party, "p_main_party","p_town_10", 2),
		(else_try),
			(eq, "$c3_start", 2), #nord - sargoth
			(party_relocate_near_party, "p_main_party","p_town_1", 2),
		(else_try),
			(eq, "$c3_start", 1), #rhodok - jelkala
			(party_relocate_near_party, "p_main_party","p_town_5", 2),
		(else_try),
			(eq, "$c3_start", 0), #sarranid - shariz
			(party_relocate_near_party, "p_main_party","p_town_19", 2),
		(try_end),
		(set_show_messages, 1),
		(change_screen_return),
	(try_end),
]

from util_wrappers import *
from util_common import *

def modmerge_game_menus(orig_game_menus, check_duplicates = True):
	
	try:#insert nobility redirect
		find_i = list_find_first_match_i( orig_game_menus, "start_phase_2" )
		codeblock = GameMenuWrapper( orig_game_menus[find_i]).GetOpBlock()
		codeblock.Append(c3_redirect)
	except:
		import sys
		print "Kings Choice Injecton failed:", sys.exc_info()[1]
		raise
		
	if( not check_duplicates ):
		orig_game_menus.extend(game_menus) # Use this only if there are no replacements (i.e. no duplicated item names)
	else:
	# Use the following loop to replace existing entries with same id
		for i in range (0,len(game_menus)): #originally - for i in range (0,len(game_menus)-1):
			find_index = find_object(orig_game_menus, game_menus[i][0]); # find_object is from header_common.py
			if( find_index == -1 ):
				orig_game_menus.append(game_menus[i])
			else:
				orig_game_menus[find_index] = game_menus[i]

def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]
        modmerge_game_menus(orig_game_menus)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
