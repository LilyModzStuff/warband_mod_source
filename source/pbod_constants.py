## Prebattle Orders & Deployment by Caba'drin
## v0.92
## 20 Jan 2012

from module_constants import *

## Prebattle Orders & Deployment Begin
max_battle_size = 1000 #RESET if you've modded the battlesize
skirmish_min_distance = 1500 #Min distance you wish maintained, in cm. Where agent will retreat
skirmish_max_distance = 2500 #Max distance to maintain, in cm. Where agent will stop retreating

#PBOD General
current_version = 920
slot_party_pbod_mod_version = 46  #slot_village_player_can_not_steal_cattle
pbod_last_troop     = "trp_companions_discard" #Last Troop in Troops File  Floris: "trp_troops_end"; native: "trp_relative_of_merchants_end" 
order_frame_presobj = "trp_bandit_leaders_end"  #dummy troop slots used in battle Floris: "trp_tpe_presobj"   Native: "trp_bandit_leaders_end"

#Deployment
slot_troop_prebattle_first_round           = 37  #slot_lady_no_messages 
#slot_troop_prebattle_array                 = 38  #slot_lady_last_suitor 
slot_troop_prebattle_num_upgrade           = 52  #slot_lord_reputation_type  
slot_troop_prebattle_preupgrade_check      = 39  #slot_troop_betrothal_time   
slot_party_prebattle_customized_deployment = 47  #slot_center_accumulated_rents  
slot_party_prebattle_battle_size           = 48  #slot_center_accumulated_tariffs 
slot_party_prebattle_size_in_battle        = 49  #slot_town_wealth  
slot_party_prebattle_in_battle_count       = 50  #slot_town_prosperity
#Split Divisions
slot_party_prebattle_customized_divisions  = 51  #slot_town_player_odds 
slot_party_reinforcement_stage 		       = 107 #for main_party_backup
slot_troop_prebattle_alt_division          = 48  #slot_troop_set_decision_seed
slot_troop_prebattle_alt_division_percent  = 49  #slot_troop_temp_decision_seed 
slot_troop_prebattle_alt_division_amount   = 50  #slot_troop_recruitment_random 
#Troop slots--for soldiers (non-heros, non-lords, non-player) only
#Party slots--for the main party and main party backup only
#Orders
slot_party_prebattle_plan                  = 231 #slot_center_shipyards
slot_party_prebattle_num_orders            = 232 #slot_center_household_gardens 
slot_party_prebattle_order_array_begin     = 250 #slot_town_trade_good_prices_begin 
#Party slots--for the main party only--up to 320 used in this version
#reg()s from 6-50 used in this version (only during order presentation)
#Weather Prof Decrease - temp, used only for 1 mission at a time then can be discarded
slot_troop_proficiency_modified  = 335
slot_troop_orig_wpt_archery      = 336
slot_troop_orig_wpt_crossbow     = 337
slot_troop_orig_wpt_throwing     = 338
slot_troop_pnty_wpt_archery      = 339 ##heroes only
slot_troop_pnty_wpt_crossbow     = 340 ##heroes only
slot_troop_pnty_wpt_throwing     = 341 ##heroes only
#Agent Slots
slot_agent_lance         = 33
slot_agent_horsebow      = 34
slot_agent_spear         = 35
slot_agent_horse         = 36
slot_agent_volley_fire   = 37
slot_agent_spearwall     = 38
slot_agent_player_braced = 39
slot_agent_alt_div_check = 40
#slot_agent_new_division  = 41
#Team Slots (so high to allow for formations)
slot_team_d0_order_weapon     = 300 #plus 8 more for the other divisions
slot_team_d0_order_shield     = 309 #plus 8 more for the other divisions
slot_team_d0_order_skirmish   = 318 #plus 8 more for the other divisions
slot_team_d0_order_volley     = 327 #plus 8 more for the other divisions
slot_team_d0_order_sp_brace   = 336 #plus 8 more for the other divisions

slot_team_d0_formation_to_resume = 350

#PBOD Preference Slots (used for p_main_party; available 72 - 108)
slot_party_pref_prefs_set    = 72
slot_party_pref_div_dehorse  = slot_town_village_product         #76
slot_party_pref_div_no_ammo  = slot_town_rebellion_readiness     #77
slot_party_pref_wu_lance     = slot_town_arena_melee_mission_tpl #78
slot_party_pref_wu_harcher   = slot_town_arena_torny_mission_tpl #79
slot_party_pref_wu_spear     = slot_town_arena_melee_1_num_teams #80
slot_party_pref_dmg_tweaks   = slot_town_arena_melee_1_team_size #81
slot_party_pref_spear_brace  = slot_town_arena_melee_2_num_teams #82
slot_party_pref_formations   = slot_town_arena_melee_2_team_size #83
slot_party_pref_bodyguard    = slot_town_arena_melee_3_num_teams #84
slot_party_pref_bc_continue  = slot_town_arena_melee_3_team_size #85
slot_party_pref_bc_charge_ko = slot_town_arena_melee_cur_tier    #86
slot_party_pref_wp_prof_decrease = 87

#Order Tracking
slot_party_gk_order          = 108
slot_party_gk_order_hold_over_there = slot_party_gk_order #for party #2 at the moment, also used for backup_party

#Order Constants
ranged    = 0
onehand   = 1
twohands  = 2
polearm   = 3
shield    = 4
noshield  = 5
free      = 6 #shield
clear     = -1
begin     = 1
end       = 0

cam_mode_default = 0
cam_mode_follow  = 1
cam_mode_free    = 2
cam_mode_shoot   = 3
cam_position     = 47 #pos47


BP_Spawn = 0




#Values for agent_get_combat_state
cs_free                      = 0
cs_target_in_sight           = 1     # ranged units
cs_guard                     = 2     # no shield
cs_wield                     = 3     # reach out weapon, preparing to strike, melee units
cs_fire                      = 3     # ranged units
cs_swing                     = 4     # cut / thrust, melee units
cs_load                      = 4     # crossbow units
cs_still                     = 7     # melee units, happens, not always (seems to have something to do with the part of body hit), when hit
cs_no_visible_targets        = 7     # ranged units or blocking iwth a shield
cs_target_on_right_hand_side = 8     # horse archers

# For the player or dead units it always returns 0.
# But for living human agents here are some of the values it can return and what each seems to mean:
# 0 = nothing active
# 1 = firing ranged
# 3 = preparing and holding attack (either melee or ranged)
# 4 = swinging with melee
# 7 = recovering from being hit
# 8 = ranged equipped, no target in field of view

#Key definitions moved to globals to allow for in-game remapping
#See script "prebattle_init_default_keys" and the presentation "pbod_redefine_keys"
###################################################################################
# AutoLoot: Modified Constants
# Most of these are slot definitions, make sure they do not clash with your mod's other slot usage
###################################################################################
# This is an item slot
# slot_item_difficulty = 5

# # Autoloot improved by rubik begin
# slot_item_weight                  = 6

slot_item_cant_on_horseback       = 10
# slot_item_type_not_for_sell       = 11
# slot_item_modifier_multiplier     = 12

slot_item_needs_two_hands	= 41
slot_item_length	        = 42
slot_item_speed	            = 43
slot_item_thrust_damage	= 44
slot_item_swing_damage	= 45
slot_item_couchable     = 46
slot_item_pike          = 47

slot_item_head_armor	= slot_item_needs_two_hands
slot_item_body_armor	= slot_item_thrust_damage
slot_item_leg_armor	    = slot_item_swing_damage

slot_item_horse_speed	= slot_item_needs_two_hands
slot_item_horse_armor	= slot_item_thrust_damage
slot_item_horse_charge	= slot_item_swing_damage
# # Autoloot end

#-- Dunde's Key Config BEGIN
#-- Parts to modify as your mod need --------------
from header_triggers import *
keys_list = [ 
              ("$key_camera_forward",key_up),
              ("$key_camera_backward",key_down),
	          ("$key_camera_left", key_left),
	          ("$key_camera_right", key_right),
			  ("$key_camera_zoom_plus",key_numpad_plus),     #Num + to zoom in
              ("$key_camera_zoom_min",key_numpad_minus),     #Num - to zoom out
			  ("$key_camera_next",key_left_mouse_button),    #right key to jump to next bot
              ("$key_camera_prev",key_right_mouse_button),   #left key to jump to prev bot
			  ("$key_camera_toggle",key_end),                #END button to toggle camera mode
	          ("$key_order_7", key_f7),
	          ("$key_order_8", key_f8),
	          ("$key_order_9", key_f9),
			  ("$key_order_10", key_f10),
	          ("$key_special_0", key_b), #Pike Bracing
	          ("$key_special_1", key_m), #Whistle for Horse 	
			  #("$key_special_2", key_g), #Deploy Pavise	#Floris Only
			  ("$key_special_3", key_left_mouse_button), #Shield Bash		  
			]
#--------------------------------------------------
             
all_keys_list   = [ 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x1e, 0x30, 0x2e, 0x20, 0x12, 0x21, 0x22, 0x23, 0x17, 0x24,
                    0x25, 0x26, 0x32, 0x31, 0x18, 0x19, 0x10, 0x13, 0x1f, 0x14, 0x16, 0x2f, 0x11, 0x2d, 0x15, 0x2c, 0x52, 0x4f, 0x50, 0x51, 
                    0x4b, 0x4c, 0x4d, 0x47, 0x48, 0x49, 0x45, 0xb5, 0x37, 0x4a, 0x4e, 0x9c, 0x53, 0xd2, 0xd3, 0xc7, 0xcf, 0xc9, 0xd1, 0xc8, 
                    0xd0, 0xcb, 0xcd, 0x3b, 0x3c, 0x3d, 0x3e, 0x3f, 0x40, 0x41, 0x42, 0x43, 0x44, 0x57, 0x58, 0x39, 0x1c, 0x0f, 0x0e, 0x1a, 
                    0x1b, 0x33, 0x34, 0x35, 0x2b, 0x0d, 0x0c, 0x27, 0x28, 0x29, 0x3a, 0x2a, 0x36, 0x1d, 0x9d, 0x38, 0xb8, 0xe0, 0xe1, 0xe2, 
                    0xe3, 0xe4, 0xe5, 0xe6, 0xe7, 0xee, 0xef, ]

number_of_keys            = len(keys_list)
number_of_all_keys        = len(all_keys_list)
two_columns_limit         = 20

slot_default_keys_begin   = 0
slot_keys_begin           = slot_default_keys_begin + number_of_keys
slot_key_overlay_begin    = slot_keys_begin         + number_of_keys
slot_key_defs_begin       = slot_key_overlay_begin  + number_of_keys + number_of_keys

key_config_data = "trp_temp_array_c" #"trp_key_config"
key_names_begin = "str_key_no1"
key_label_begin = "str_0x02"
#-- Dunde's Key Config END

## Prebattle Orders & Deployment End