# Formations for Warband by Motomataru
# rel. 05/02/11

#Formation modes
formation_none      = 0
formation_default   = 1
formation_ranks     = 2
formation_shield    = 3
formation_wedge     = 4
formation_square    = 5

#Formation tweaks
formation_minimum_spacing	= 67
formation_minimum_spacing_horse_length	= 300
formation_minimum_spacing_horse_width	= 200
formation_start_spread_out	= 2
formation_min_foot_troops	= 12
formation_min_cavalry_troops	= 5
formation_autorotate_at_player	= 1
formation_native_ai_use_formation = 1
formation_delay_for_spawn	= .4
formation_reequip	= 1	#TO DO: One-time-on-form option when formation slots integrated
formation_reform_interval	= 2 #seconds
formation_place_around_leader = 0


#Other constants (not tweaks)
Third_Max_Weapon_Length = 250 / 3
Km_Per_Hour_To_Cm = formation_reform_interval * 100000 / 3600
Reform_Trigger_Modulus = formation_reform_interval * 2	#trigger is half-second
Top_Speed	= 13
Far_Away	= 1000000

###################################################################################
# AutoLoot: Modified Constants
# Most of these are slot definitions, make sure they do not clash with your mod's other slot usage
###################################################################################
# This is an item slot
# slot_item_difficulty = 5

# # Autoloot improved by rubik begin
# slot_item_weight                  = 6

# slot_item_cant_on_horseback       = 10
# slot_item_type_not_for_sell       = 11
# slot_item_modifier_multiplier     = 12

# slot_item_needs_two_hands   = 41
# slot_item_length            = 42
# slot_item_speed             = 43
# slot_item_thrust_damage     = 44
# slot_item_swing_damage      = 45
#slot_item_weapon_noswing     = 46
#slot_item_weapon_swing       = 47

# slot_item_head_armor        = slot_item_needs_two_hands
# slot_item_body_armor        = slot_item_thrust_damage
# slot_item_leg_armor         = slot_item_swing_damage

# slot_item_horse_speed       = slot_item_needs_two_hands
# slot_item_horse_armor       = slot_item_thrust_damage
# slot_item_horse_charge      = slot_item_swing_damage
# # Autoloot end

#positions used through formations and AI triggers
Current_Pos     = 12	#pos12
Speed_Pos       = 14	#pos14
Target_Pos      = 16	#pos16
Enemy_Team_Pos  = 24	#pos24
Temp_Pos        = 28	#pos28


#Team Slots
slot_team_faction                       = 1
slot_team_starting_x                    = 2
slot_team_starting_y                    = 3
slot_team_reinforcement_stage           = 4

#Reset with every call of Store_Battlegroup_Data
slot_team_size                          = 5
slot_team_adj_size                      = 6 #cavalry double counted for AI considerations
slot_team_num_infantry                  = 7	#class counts
slot_team_num_archers                   = 8
slot_team_num_cavalry                   = 9
slot_team_level                         = 10
slot_team_dist_enemy_inf_to_start       = 11
slot_team_avg_x                         = 12
slot_team_avg_y                         = 13
#Team Slots end

#Battlegroup slots (1 for each of 9 divisions)
slot_team_d0_size                       = 14
slot_team_d0_percent_ranged             = 23
slot_team_d0_percent_throwers           = 32
slot_team_d0_low_ammo                   = 41
slot_team_d0_level                      = 50
slot_team_d0_armor                      = 59
slot_team_d0_weapon_length              = 68
slot_team_d0_swung_weapon_length        = 77
slot_team_d0_front_weapon_length        = 86
slot_team_d0_front_agents               = 95	#for calculating slot_team_d0_front_weapon_length
slot_team_d0_in_melee                   = 104
slot_team_d0_enemy_supporting_melee     = 113
slot_team_d0_closest_enemy              = 122
slot_team_d0_closest_enemy_dist         = 131	#for calculating slot_team_d0_closest_enemy
slot_team_d0_closest_enemy_special      = 140	#tracks non-cavalry for AI infantry division, infantry for AI archer division
slot_team_d0_closest_enemy_special_dist = 149	#for calculating slot_team_d0_closest_enemy_special
slot_team_d0_avg_x                      = 158
slot_team_d0_avg_y                      = 167
#End Reset Group

slot_team_d0_type                       = 176
slot_team_d0_formation                  = 185
slot_team_d0_formation_space            = 194
slot_team_d0_move_order                 = 203	#now used only for player divisions
slot_team_d0_fclock                     = 212	#now used only for player divisions
slot_team_d0_first_member               = 221
slot_team_d0_prev_first_member          = 230
slot_team_d0_speed_limit                = 239
slot_team_d0_percent_in_place           = 248
slot_team_d0_destination_x              = 257
slot_team_d0_destination_y              = 266
slot_team_d0_destination_zrot           = 275
slot_team_d0_target_team                = 284	#targeted battlegroup (team ID)
slot_team_d0_target_division            = 293	#targeted battlegroup (division ID)
#Battlegroup slots end

reset_team_stats_begin = slot_team_size  
reset_team_stats_end   = slot_team_d0_avg_y + 8 + 1

scratch_team = 7

#Slot Division Type definitions
sdt_infantry   = 0
sdt_archer     = 1
sdt_cavalry    = 2
sdt_polearm    = 3
sdt_skirmisher = 4
sdt_harcher    = 5
sdt_support    = 6
sdt_bodyguard  = 7
sdt_unknown    = -1

#Other slots
#the following applied only to infantry in formation
slot_agent_in_first_rank       = 26
slot_agent_inside_formation    = 27
slot_agent_nearest_enemy_agent = 28
slot_agent_new_division        = 29

#from module_constants import slot_town_rebellion_readiness, slot_town_arena_melee_mission_tpl
#slot_party_cabadrin_order_d0 = slot_town_arena_melee_mission_tpl #78
#slot_party_gk_order          = slot_town_rebellion_readiness #77


