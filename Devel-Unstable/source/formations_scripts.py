# Formations for Warband by Motomataru
# rel. 05/02/11
#EDITED FOR MANY DIVISIONS BY CABA'DRIN 02/23/11

from header_common import *
from header_operations import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from ID_animations import *
from module_constants import *

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

scripts = [
# #Formations Scripts	  
  # script_division_reset_places by motomataru
  # Input: none
  # Output: none
  # Resets globals for placing divisions around player for script_battlegroup_place_around_leader
  ("division_reset_places", [
	(assign, "$next_cavalry_place", formation_minimum_spacing_horse_width),	#first spot RIGHT of the player
	(assign, "$next_archer_place", 1000),	#first spot 10m FRONT of the player
	(assign, "$next_infantry_place", -1 * formation_minimum_spacing_horse_width),	#first spot LEFT of the player
  ]),
   
  # script_battlegroup_place_around_leader by motomataru
  # Input: team, division
  # Output: pos61 division position
  ("battlegroup_place_around_leader", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(team_get_leader, ":fleader", ":fteam"),
	(try_begin),
		(gt, ":fleader", -1),	#any team members left?
		
		(agent_get_position, pos1, ":fleader"),
		(try_begin),
			(eq, "$autorotate_at_player", 1),
			(call_script, "script_team_get_position_of_enemies", Enemy_Team_Pos, ":fteam", grc_everyone),
			(neq, reg0, 0),	#more than 0 enemies still alive?
			(call_script, "script_point_y_toward_position", pos1, Enemy_Team_Pos),
		(try_end),

		(store_add, ":slot", slot_team_d0_type, ":fdivision"),
		(team_get_slot, ":sd_type", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_size, ":fdivision"),
		(team_get_slot, ":num_troops", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
		(team_get_slot, ":fformation", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
		(team_get_slot, ":formation_extra_spacing", ":fteam", ":slot"),
		(try_begin),
			(this_or_next|eq, ":sd_type", sdt_cavalry),
			(eq, ":sd_type", sdt_harcher),
			(position_move_x, pos1, "$next_cavalry_place", 0),
			(try_begin),	#handle Native's way of doing things
				(eq, ":fformation", formation_none),
				(try_begin),
					(ge, ":formation_extra_spacing", 0),
					(store_mul, ":troop_space", ":formation_extra_spacing", 133),
					(val_add, ":troop_space", 150),
				(else_try),	#handle Native multi-ranks
					(assign, ":troop_space", 200),
					(val_mul, ":formation_extra_spacing", -1),
					(val_add, ":formation_extra_spacing", 1),
					(val_div, ":num_troops", ":formation_extra_spacing"),
				(try_end),
				(store_mul, ":formation_width", ":num_troops", ":troop_space"),
				(store_div, reg0, ":formation_width", 2),
				(position_move_x, pos1, reg0, 0),	#cavalry set up RIGHT of leader
				(copy_position, pos61, pos1),
			(else_try),
				(store_mul, ":troop_space", ":formation_extra_spacing", 50),
				(val_add, ":troop_space", formation_minimum_spacing_horse_width),
				(convert_to_fixed_point, ":num_troops"),
				(store_sqrt, ":formation_width", ":num_troops"),
				(val_mul, ":formation_width", ":troop_space"),
				(convert_from_fixed_point, ":formation_width"),
				(val_sub, ":formation_width", ":troop_space"),
				(store_div, reg0, ":formation_width", 2),
				(position_move_x, pos1, reg0, 0),	#cavalry set up RIGHT of leader
				(copy_position, pos61, pos1),
				(call_script, "script_form_cavalry", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing"),
			(try_end),
			(val_add, "$next_cavalry_place", ":formation_width"),
			(val_add, "$next_cavalry_place", formation_minimum_spacing_horse_width),

		(else_try),
			(eq, ":sd_type", sdt_archer),
			(position_move_y, pos1, "$next_archer_place"),	#archers set up FRONT of leader
			(copy_position, pos61, pos1),
			(try_begin),
				(neq, ":fformation", formation_none),
				(call_script, "script_get_centering_amount", formation_default, ":num_troops", ":formation_extra_spacing"),
				(val_mul, reg0, -1),
				(position_move_x, pos1, reg0, 0),
				(call_script, "script_form_archers", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing", ":fformation"),
			(try_end),
			(val_add, "$next_archer_place", 500),	#next archers 5m FRONT of these
			
		(else_try),
			(eq, ":sd_type", sdt_skirmisher),
			(position_move_y, pos1, "$next_archer_place"),	#skirmishers set up FRONT of leader
			(copy_position, pos61, pos1),
			(try_begin),
				(neq, ":fformation", formation_none),
				(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
				(position_move_x, pos1, reg0, 0),
				(call_script, "script_form_infantry", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing", ":fformation"),
			(try_end),
			(val_add, "$next_archer_place", 500),	#next archers 5m FRONT of these
			
		(else_try),
			(position_move_x, pos1, "$next_infantry_place", 0),
			(copy_position, pos61, pos1),
			(try_begin),	#handle Native's way of doing things
				(eq, ":fformation", formation_none),
				(try_begin),
					(ge, ":formation_extra_spacing", 0),
					(store_mul, ":troop_space", ":formation_extra_spacing", 75),	#Native minimum spacing not consistent but less than this
					(val_add, ":troop_space", 100),
				(else_try),	#handle Native multi-ranks
					(assign, ":troop_space", 150),
					(val_mul, ":formation_extra_spacing", -1),
					(val_add, ":formation_extra_spacing", 1),
					(val_div, ":num_troops", ":formation_extra_spacing"),
				(try_end),
				(store_mul, ":formation_width", ":num_troops", ":troop_space"),
				(store_div, reg0, ":formation_width", 2),
				(val_mul, reg0, -1),	#infantry set up LEFT of leader
				(position_move_x, pos61, reg0, 0),
			(else_try),
				(call_script, "script_form_infantry", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing", ":fformation"),
				(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
				(store_mul, ":formation_width", 2, reg0),
				(store_mul, ":troop_space", ":formation_extra_spacing", 50),
				(val_add, ":troop_space", formation_minimum_spacing),
				(val_add, ":formation_width", ":troop_space"),
				(val_mul, reg0, -1),	#infantry set up LEFT of leader
				(position_move_x, pos61, reg0, 0),
			(try_end),
			(val_sub, "$next_infantry_place", ":formation_width"),	#next infantry 1m LEFT of these
			(val_sub, "$next_infantry_place", 100),
		(try_end),
		
		(store_add, ":slot", slot_team_d0_move_order, ":fdivision"),
		(team_set_slot, ":fteam", ":slot", mordr_hold),
		(set_show_messages, 0),
		(team_get_movement_order, reg0, ":fteam", ":fdivision"),
		(try_begin),
			(neq, reg0, mordr_hold),
			(team_give_order, ":fteam", ":fdivision", mordr_hold),
		(try_end),
		(call_script, "script_set_formation_destination", ":fteam", ":fdivision", pos61),
		(set_show_messages, 1),
	(try_end),
  ]),
  
  # script_battlegroup_place_at_leader by Caba'drin
  # Input: team, division
  # Output: pos61 division position
  ("battlegroup_place_at_leader", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(team_get_leader, ":fleader", ":fteam"),
	(try_begin),
		(gt, ":fleader", -1),	#any team members left?
		
		(agent_get_position, pos1, ":fleader"),		
		(try_begin),
			(eq, "$autorotate_at_player", 1),
			(call_script, "script_team_get_position_of_enemies", pos60, ":fteam", grc_everyone),
			(neq, reg0, 0),	#more than 0 enemies still alive?
			(call_script, "script_point_y_toward_position", pos1, pos60),
		(try_end),

		(store_add, ":slot", slot_team_d0_type, ":fdivision"),
		(team_get_slot, ":sd_type", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_size, ":fdivision"),
		(team_get_slot, ":num_troops", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
		(team_get_slot, ":fformation", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
		(team_get_slot, ":formation_extra_spacing", ":fteam", ":slot"),

		(copy_position, pos61, pos1),
		(neq, ":fformation", formation_none),	
		(try_begin),
			(this_or_next|eq, ":sd_type", sdt_cavalry),
			(eq, ":sd_type", sdt_harcher),
			(call_script, "script_form_cavalry", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing"),

		(else_try),
			(eq, ":sd_type", sdt_archer),
			(call_script, "script_get_centering_amount", formation_default, ":num_troops", ":formation_extra_spacing"),
			(val_mul, reg0, -1),
			(position_move_x, pos1, reg0, 0),
			(call_script, "script_form_archers", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing", ":fformation"),
		
		(else_try),
			(eq, ":sd_type", sdt_skirmisher),
			(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
			(position_move_x, pos1, reg0, 0),
			(call_script, "script_form_infantry", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing", ":fformation"),
			
		(else_try),
			(call_script, "script_form_infantry", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing", ":fformation"),
		(try_end),
		
		(store_add, ":slot", slot_team_d0_move_order, ":fdivision"),
		(team_set_slot, ":fteam", ":slot", mordr_hold),
		(set_show_messages, 0),
		(team_get_movement_order, reg0, ":fteam", ":fdivision"),
		(try_begin),
			(neq, reg0, mordr_hold),
			(team_give_order, ":fteam", ":fdivision", mordr_hold),
		(try_end),
		(call_script, "script_set_formation_destination", ":fteam", ":fdivision", pos61),
		(set_show_messages, 1),
	(try_end),
  ]),
  
  # script_form_cavalry by motomataru
  # Input: (pos1), team, division, agent number of team leader, spacing
  # Output: none
  # Form in wedge, (now not) excluding horse archers
  # Creates formation starting at pos1
  ("form_cavalry", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fleader", 3),
	(store_script_param, ":formation_extra_spacing", 4),
	(store_mul, ":extra_space", ":formation_extra_spacing", 50),
	(store_add, ":x_distance", formation_minimum_spacing_horse_width, ":extra_space"),
	(store_add, ":y_distance", formation_minimum_spacing_horse_length, ":extra_space"),
	(store_add, ":slot", slot_team_d0_first_member, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", -1),
	(assign, ":max_level", 0),
	(try_for_agents, ":agent"),
		(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
		(agent_get_troop_id, ":troop_id", ":agent"),
		(store_character_level, ":troop_level", ":troop_id"),
		(gt, ":troop_level", ":max_level"),
		(assign, ":max_level", ":troop_level"),
	(end_try),
	(assign, ":column", 1),
	(assign, ":rank_dimension", 1),
	(store_mul, ":neg_y_distance", ":y_distance", -1),
	(store_mul, ":neg_x_distance", ":x_distance", -1),
	(store_div, ":wedge_adj", ":x_distance", 2),
	(store_div, ":neg_wedge_adj", ":neg_x_distance", 2),
	(val_add, ":max_level", 1),
	(assign, ":form_left", 1),
	(try_for_range_backwards, ":rank_level", 0, ":max_level"),	#put troops with highest exp in front
		(try_for_agents, ":agent"),
			(agent_get_troop_id, ":troop_id", ":agent"),
			(store_character_level, ":troop_level", ":troop_id"),
			(eq, ":troop_level", ":rank_level"),				
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
			(agent_set_scripted_destination, ":agent", pos1, 1),
			(try_begin),	#First Agent
				(store_add, ":slot", slot_team_d0_first_member, ":fdivision"),
				(neg|team_slot_ge, ":fteam", ":slot", 0),
				(team_set_slot, ":fteam", ":slot", ":agent"),
			(try_end),
			(try_begin),
				(eq, ":form_left", 1),
				(position_move_x, pos1, ":neg_x_distance", 0),
			(else_try),
				(position_move_x, pos1, ":x_distance", 0),
			(try_end),
			(val_add, ":column", 1),
			(gt, ":column", ":rank_dimension"),
			(position_move_y, pos1, ":neg_y_distance", 0),
			(try_begin),
				(neq, ":form_left", 1),
				(assign, ":form_left", 1),
				(position_move_x, pos1, ":neg_wedge_adj", 0),
			(else_try),
				(assign, ":form_left", 0),
				(position_move_x, pos1, ":wedge_adj", 0),
			(try_end),			
			(assign, ":column", 1),
			(val_add, ":rank_dimension", 1),
		(end_try),
	(end_try),
  ]),
	   
  # script_form_archers by motomataru
  # Input: (pos1), team, division, agent number of team leader, spacing, formation
  # Output: none
  # Form in line, staggered if formation = formation_ranks
  # Creates formation starting at pos1
  ("form_archers", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fleader", 3),
	(store_script_param, ":formation_extra_spacing", 4),
	(store_script_param, ":archers_formation", 5),
	(store_mul, ":extra_space", ":formation_extra_spacing", 50),
	(store_add, ":distance", formation_minimum_spacing, ":extra_space"),		#minimum distance between troops
	(store_add, ":slot", slot_team_d0_first_member, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", -1),
	(assign, ":total_move_y", 0),	#staggering variable	
	(try_for_agents, ":agent"),
		(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
		(agent_set_scripted_destination, ":agent", pos1, 1),
		(try_begin),	#First Agent
			(store_add, ":slot", slot_team_d0_first_member, ":fdivision"),
			(neg|team_slot_ge, ":fteam", ":slot", 0),
			(team_set_slot, ":fteam", ":slot", ":agent"),
		(try_end),
		(position_move_x, pos1, ":distance", 0),
		(try_begin),
			(eq, ":archers_formation", formation_ranks),
			(val_add, ":total_move_y", 75),
			(try_begin),
				(le, ":total_move_y", 150),
				(position_move_y, pos1, 75, 0),
			(else_try),
				(position_move_y, pos1, -150, 0),
				(assign, ":total_move_y", 0),
			(try_end),
		(try_end),
	(try_end),
  ]),
	   
  # script_form_infantry by motomataru
  # Input: (pos1), team, division, agent number of team leader, spacing, formation
  # Output: none
  # If input "formation" is formation_default, will select a formation based on faction
  # Creates formation starting at pos1
  ("form_infantry", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fleader", 3),
	(store_script_param, ":formation_extra_spacing", 4),
	(store_script_param, ":infantry_formation", 5),
	(store_mul, ":extra_space", ":formation_extra_spacing", 50),
	(store_add, ":distance", formation_minimum_spacing, ":extra_space"),		#minimum distance between troops	
	(store_mul, ":neg_distance", ":distance", -1),
	(store_add, ":slot", slot_team_d0_first_member, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", -1),
	(store_add, ":slot", slot_team_d0_size, ":fdivision"),
	(team_get_slot, ":num_troops", ":fteam", ":slot"),
	(try_begin),
		(eq, ":infantry_formation", formation_default),
		(call_script, "script_get_default_formation", ":fteam"),
		(assign, ":infantry_formation", reg0),
	(try_end),
	(team_get_weapon_usage_order, ":weapon_order", ":fteam", ":fdivision"),
	(team_get_hold_fire_order, ":fire_order", ":fteam", ":fdivision"),
	(assign, ":form_left", 1),
	(assign, ":column", 1),
	(assign, ":rank", 1),

	(try_begin),
		(eq, ":infantry_formation", formation_square),
		(convert_to_fixed_point, ":num_troops"),
		(store_sqrt, ":square_dimension", ":num_troops"),
		(convert_from_fixed_point, ":square_dimension"),
		(val_add, ":square_dimension", 1),

		(try_for_agents, ":agent"),
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
			(try_begin), ##CABA - Deployment
				(eq, "$battle_phase", BP_Spawn),  ##CABA - Deployment
				(agent_set_scripted_destination, ":agent", pos1), ##CABA - Deployment
			(else_try), ##CABA - Deployment
				(call_script, "script_formation_process_agent_move", ":fteam", ":fdivision", ":agent", ":rank"),
			(try_end), ##CABA - Deployment
			(try_begin),
				(eq, formation_reequip, 1),
				(eq, ":weapon_order", wordr_use_any_weapon),
				(try_begin),
					(this_or_next|eq, ":rank", 1),
					(this_or_next|ge, ":rank", ":square_dimension"),
					(this_or_next|eq, ":column", 1),
					(ge, ":column", ":square_dimension"),
					(call_script, "script_equip_best_melee_weapon", ":agent", 0, 0, ":fire_order"),
					(agent_set_slot, ":agent", slot_agent_inside_formation, 0),
				(else_try),
					(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1, ":fire_order"),
					(agent_set_slot, ":agent", slot_agent_inside_formation, 1),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":form_left", 1),
				(position_move_x, pos1, ":neg_distance", 0),
			(else_try),
				(position_move_x, pos1, ":distance", 0),
			(try_end),
			(val_add, ":column", 1),
			(gt, ":column", ":square_dimension"),
			(position_move_y, pos1, ":neg_distance", 0),
			(try_begin),
				(neq, ":form_left", 1),
				(assign, ":form_left", 1),
				(position_move_x, pos1, ":neg_distance", 0),
			(else_try),
				(assign, ":form_left", 0),
				(position_move_x, pos1, ":distance", 0),
			(try_end),			
			(assign, ":column", 1),		
			(val_add, ":rank", 1),
		(end_try),
		
	(else_try),
		(eq, ":infantry_formation", formation_wedge),
		(assign, ":max_level", 0),
		(try_for_agents, ":agent"),
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
			(agent_get_troop_id, ":troop_id", ":agent"),
			(store_character_level, ":troop_level", ":troop_id"),
			(gt, ":troop_level", ":max_level"),
			(assign, ":max_level", ":troop_level"),
		(end_try),

		(assign, ":rank_dimension", 1),
		(store_div, ":wedge_adj", ":distance", 2),
		(store_div, ":neg_wedge_adj", ":neg_distance", 2),
		(val_add, ":max_level", 1),
		(try_for_range_backwards, ":rank_level", 0, ":max_level"),	#put troops with highest exp in front
			(try_for_agents, ":agent"),
				(agent_get_troop_id, ":troop_id", ":agent"),
				(store_character_level, ":troop_level", ":troop_id"),
				(eq, ":troop_level", ":rank_level"),				
				(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
				(try_begin), ##CABA - Deployment
					(eq, "$battle_phase", BP_Spawn),  ##CABA - Deployment
					(agent_set_scripted_destination, ":agent", pos1), ##CABA - Deployment
				(else_try), ##CABA - Deployment
					(call_script, "script_formation_process_agent_move", ":fteam", ":fdivision", ":agent", ":rank_dimension"),
				(try_end), ##CABA - Deployment
				(try_begin),
					(eq, formation_reequip, 1),
					(eq, ":weapon_order", wordr_use_any_weapon),
					(try_begin),
						(this_or_next|eq, ":column", 1),
						(ge, ":column", ":rank_dimension"),
						(call_script, "script_equip_best_melee_weapon", ":agent", 0, 0, ":fire_order"),
						(agent_set_slot, ":agent", slot_agent_inside_formation, 0),
					(else_try),
						(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1, ":fire_order"),
						(agent_set_slot, ":agent", slot_agent_inside_formation, 1),
					(try_end),
				(try_end),
				(try_begin),
					(eq, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(position_move_x, pos1, ":distance", 0),
				(try_end),
				(val_add, ":column", 1),
				(gt, ":column", ":rank_dimension"),
				(position_move_y, pos1, ":neg_distance", 0),
				(try_begin),
					(neq, ":form_left", 1),
					(assign, ":form_left", 1),
					(position_move_x, pos1, ":neg_wedge_adj", 0),
				(else_try),
					(assign, ":form_left", 0),
					(position_move_x, pos1, ":wedge_adj", 0),
				(try_end),			
				(assign, ":column", 1),
				(val_add, ":rank_dimension", 1),
			(end_try),
		(end_try),
		
	(else_try),
		(eq, ":infantry_formation", formation_ranks),
		(store_div, ":rank_dimension", ":num_troops", 3),		#basic three ranks
		(val_add, ":rank_dimension", 1),		
		(assign, ":max_level", 0),
		(try_for_agents, ":agent"),
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
			(agent_get_troop_id, ":troop_id", ":agent"),
			(store_character_level, ":troop_level", ":troop_id"),
			(gt, ":troop_level", ":max_level"),
			(assign, ":max_level", ":troop_level"),
		(end_try),


		(val_add, ":max_level", 1),
		(try_for_range_backwards, ":rank_level", 0, ":max_level"),	#put troops with highest exp in front
			(try_for_agents, ":agent"),
				(agent_get_troop_id, ":troop_id", ":agent"),
				(store_character_level, ":troop_level", ":troop_id"),
				(eq, ":troop_level", ":rank_level"),				
				(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
				(try_begin), ##CABA - Deployment
					(eq, "$battle_phase", BP_Spawn),  ##CABA - Deployment
					(agent_set_scripted_destination, ":agent", pos1), ##CABA - Deployment
				(else_try), ##CABA - Deployment
					(call_script, "script_formation_process_agent_move", ":fteam", ":fdivision", ":agent", ":rank"),
				(try_end), ##CABA - Deployment
				(try_begin),
					(eq, formation_reequip, 1),
					(eq, ":weapon_order", wordr_use_any_weapon),
					(try_begin),
						(eq, ":rank", 1),
						(call_script, "script_equip_best_melee_weapon", ":agent", 0, 0, ":fire_order"),
						(agent_set_slot, ":agent", slot_agent_inside_formation, 0),
					(else_try),
						(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1, ":fire_order"),
						(agent_set_slot, ":agent", slot_agent_inside_formation, 1),
					(try_end),
				(try_end),
				(try_begin),
					(eq, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(position_move_x, pos1, ":distance", 0),
				(try_end),
				(val_add, ":column", 1),

				(gt, ":column", ":rank_dimension"),	#next rank?
				(position_move_y, pos1, ":neg_distance", 0),
				(try_begin),
					(neq, ":form_left", 1),
					(assign, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(assign, ":form_left", 0),
					(position_move_x, pos1, ":distance", 0),
				(try_end),			
				(assign, ":column", 1),
				(val_add, ":rank", 1),
			(end_try),
		(end_try),
		
	(else_try),
		(eq, ":infantry_formation", formation_shield),
		(store_div, ":rank_dimension", ":num_troops", 3),		#basic three ranks
		(val_add, ":rank_dimension", 1),
		(assign, ":first_second_rank_agent", -1),
		(assign, ":min_len_non_shielded", -1),
		(try_for_range, ":weap_group", 0, 4),
			(store_mul, ":min_len", ":weap_group", Third_Max_Weapon_Length),
			(store_add, ":max_len", ":min_len", Third_Max_Weapon_Length),
			(try_begin),
				(gt, ":min_len_non_shielded", -1),	#looped through agents at least once since rank 2
				(assign, ":min_len_non_shielded", ":min_len"),
			(try_end),
			(try_for_agents, ":agent"),
				(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
				(agent_get_wielded_item, ":agent_weapon", ":agent", 0),
				(try_begin),
					(gt, ":agent_weapon", itm_no_item),
					(item_get_slot, ":weapon_length", ":agent_weapon", slot_item_length),
				(else_try),
					(assign, ":weapon_length", 0),
				(try_end),
				(try_begin),
					(gt, ":rank", 1),
					(try_begin),
						(eq, ":first_second_rank_agent", ":agent"),	#looped through agents at least once since rank 2
						(assign, ":min_len_non_shielded", ":min_len"),
					(else_try),
						(eq, ":first_second_rank_agent", -1),
						(assign, ":first_second_rank_agent", ":agent"),
					(try_end),
					(eq, formation_reequip, 1),
					(eq, ":weapon_order", wordr_use_any_weapon),
					(ge, ":weapon_length", ":min_len"),	#avoid reequipping agents that are already in formation
					(eq, ":min_len_non_shielded", -1),	#haven't looped through agents at least once since rank 2
					(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1, ":fire_order"),	#longest weapon, including two-handed
					(agent_set_slot, ":agent", slot_agent_inside_formation, 1),
					(agent_get_wielded_item, ":agent_weapon", ":agent", 0),
					(try_begin),
						(gt, ":agent_weapon", itm_no_item),
						(item_get_slot, ":weapon_length", ":agent_weapon", slot_item_length),
					(else_try),
						(assign, ":weapon_length", 0),
					(try_end),
				(try_end),
				
				(assign, ":form_up", 0),
				(agent_get_wielded_item, ":agent_shield", ":agent", 1),
				(try_begin),
					(gt, ":agent_shield", itm_no_item),
					(item_get_type, reg0, ":agent_shield"),
					(eq, reg0, itp_type_shield),
					(try_begin),
						(is_between, ":weapon_length", ":min_len", ":max_len"),
						(assign, ":form_up", 1),
					(try_end),
				(else_try),
					(this_or_next|gt, ":rank", 1),
					(gt, ":weap_group", 2),
					(is_between, ":weapon_length", ":min_len_non_shielded", ":max_len"),
					(assign, ":form_up", 1),
				(try_end),

				(eq, ":form_up", 1),
				(try_begin), ##CABA - Deployment
					(eq, "$battle_phase", BP_Spawn),  ##CABA - Deployment
					(agent_set_scripted_destination, ":agent", pos1), ##CABA - Deployment
				(else_try), ##CABA - Deployment
					(call_script, "script_formation_process_agent_move", ":fteam", ":fdivision", ":agent", ":rank"),
				(try_end), ##CABA - Deployment
				(try_begin),
					(eq, formation_reequip, 1),
					(eq, ":weapon_order", wordr_use_any_weapon),
					(eq, ":rank", 1),
					(call_script, "script_equip_best_melee_weapon", ":agent", 1, 0, ":fire_order"),	#best weapon, force shield
					(agent_set_slot, ":agent", slot_agent_inside_formation, 0),
				(try_end),
				(try_begin),
					(eq, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(position_move_x, pos1, ":distance", 0),
				(try_end),
				(val_add, ":column", 1),
				
				(gt, ":column", ":rank_dimension"),	#next rank?
				(position_move_y, pos1, ":neg_distance", 0),
				(try_begin),
					(neq, ":form_left", 1),
					(assign, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(assign, ":form_left", 0),
					(position_move_x, pos1, ":distance", 0),
				(try_end),			
				(assign, ":column", 1),
				(val_add, ":rank", 1),
			(try_end),
		(try_end),
	(try_end),

	#calculate percent in place from counts from section above (see script_formation_process_agent_move)
	(store_add, ":slot", slot_team_d0_size, ":fdivision"),
	(team_get_slot, ":num_troops", ":fteam", ":slot"),
	(store_add, ":slot", slot_team_d0_percent_in_place, ":fdivision"),
	(team_get_slot, reg0, ":fteam", ":slot"),
	(val_mul, reg0, 100),
	(val_div, reg0, ":num_troops"),
	(team_set_slot, ":fteam", ":slot", reg0),
  ]),
	   
  # script_get_default_formation by motomataru
  # Input: team id
  # Output: reg0 default formation
  ("get_default_formation", [
	(store_script_param, ":fteam", 1),
	(team_get_slot, ":ffaction", ":fteam", slot_team_faction),
	(try_begin),
	    (this_or_next|eq, ":ffaction", fac_player_supporters_faction),
		(eq, ":ffaction", fac_player_faction),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(assign, ":ffaction", "$players_kingdom"),
	(try_end),

	#assign default formation
	(try_begin),
		(eq, ":ffaction", fac_kingdom_1),	#Swadians
		(assign, reg0, formation_shield),
	(else_try),
		(eq, ":ffaction", fac_kingdom_2),	#Vaegirs
		(assign, reg0, formation_ranks),
	(else_try),
		(eq, ":ffaction", fac_kingdom_3),	#Khergit
		(assign, reg0, formation_none),	#Khergit have underdeveloped infantry
	(else_try),
		(eq, ":ffaction", fac_kingdom_4),	#Nords
		(assign, reg0, formation_shield),
	(else_try),
		(eq, ":ffaction", fac_kingdom_5),	#Rhodoks
		(assign, reg0, formation_shield),
	(else_try),
		(eq, ":ffaction", fac_kingdom_6),	#Sarranid
		(assign, reg0, formation_ranks),
	(else_try),
	    (this_or_next|eq, ":ffaction", fac_player_supporters_faction),
		(eq, ":ffaction", fac_player_faction),	#independent player
		(assign, reg0, formation_ranks),
	(else_try),
		(assign, reg0, formation_none),	#riffraff don't use formations
	(try_end),
  ]),

  # script_formation_process_agent_move by motomataru
  # Input: (pos1), team, division, agent, which rank of formation agent is in
  # Output: (pos1) may change to reference first agent's anticipated position
  # This function sets scripted destination and performs other tasks related to making the formation look nice on the move (and more)
  ("formation_process_agent_move", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":agent", 3),
	(store_script_param, ":rank", 4),
	
	(agent_set_scripted_destination, ":agent", pos1, 1),
	
	(agent_get_position, Current_Pos, ":agent"),
	(get_distance_between_positions, ":distance_to_go", Current_Pos, pos1),

	(store_add, ":slot", slot_team_d0_speed_limit, ":fdivision"),
	(team_get_slot, ":speed_limit", ":fteam", ":slot"),
	
	(agent_get_speed, Speed_Pos, ":agent"),
	(position_transform_position_to_parent, Temp_Pos, Current_Pos, Speed_Pos),
	(call_script, "script_point_y_toward_position", Current_Pos, Temp_Pos),	#get direction of travel
	(store_mul, ":expected_travel", reg0, formation_reform_interval),
	(store_div, ":speed", ":expected_travel", Km_Per_Hour_To_Cm),

	#First Agent
	(try_begin),
		(store_add, ":slot", slot_team_d0_first_member, ":fdivision"),
		(neg|team_slot_ge, ":fteam", ":slot", 0),
		(team_set_slot, ":fteam", ":slot", ":agent"),
		
		(try_begin),	#reset speed when first member stopped
			(le, ":speed", 5),	#minimum observed speed
			(store_add, ":slot", slot_team_d0_speed_limit, ":fdivision"),
			(team_set_slot, ":fteam", ":slot", Top_Speed),
			(agent_set_speed_limit, ":agent", Top_Speed),
			
		(else_try),	#first member in motion
			(val_mul, ":speed", 2),	#after terrain & encumbrance, agents tend to move about half their speed limit
			(try_begin),	#speed up if everyone caught up
				(store_add, ":slot", slot_team_d0_percent_in_place, ":fdivision"),
				(team_slot_ge, ":fteam", ":slot", 100),
				(try_begin),
					(ge, ":speed", ":speed_limit"),
					(val_add, ":speed_limit", 1),
				(try_end),
			(else_try),	#else slow down
				(val_min, ":speed_limit", ":speed"),
				(val_sub, ":speed_limit", 1),
				(val_max, ":speed_limit", 5),	#minimum observed speed
			(try_end),
			
			#build formation from first agent
			(store_add, ":slot", slot_team_d0_prev_first_member, ":fdivision"),
			(team_slot_eq, ":fteam", ":slot", ":agent"),	#looking at same first member as last call?
			
			(store_mul, ":expected_travel", ":speed_limit", Km_Per_Hour_To_Cm),
			(lt, ":expected_travel", ":distance_to_go"),	#more than one call from destination?

			(store_add, ":slot", slot_team_d0_speed_limit, ":fdivision"),
			(team_set_slot, ":fteam", ":slot", ":speed_limit"),
			(agent_set_speed_limit, ":agent", ":speed_limit"),
			
			(copy_position, Temp_Pos, Current_Pos),
			(call_script, "script_point_y_toward_position", Temp_Pos, pos1),
			(position_move_y, Temp_Pos, ":expected_travel", 0),	#anticipate where first member will be next
			(position_copy_rotation, Temp_Pos, pos1),	#conserve destination facing of formation
			(copy_position, pos1, Temp_Pos),	#reference the rest of the formation to first member's anticipated position
		(try_end),

		(store_add, ":slot", slot_team_d0_percent_in_place, ":fdivision"),
		(team_set_slot, ":fteam", ":slot", 1),	#reinit: always count first member as having arrived
		(store_add, ":slot", slot_team_d0_prev_first_member, ":fdivision"),
		(team_set_slot, ":fteam", ":slot", ":agent"),

	#Not First Agent
	(else_try),
		(try_begin),
			(le, ":speed", 0),
			(assign, ":speed_limit", Top_Speed),
		(else_try),
			(neg|position_is_behind_position, pos1, Current_Pos),
			(store_div, ":speed_limit", ":distance_to_go", Km_Per_Hour_To_Cm),
			(val_max, ":speed_limit", 1),
		(else_try),
			(store_add, ":slot", slot_team_d0_in_melee, ":fdivision"),
			(team_slot_eq, ":fteam", ":slot", 0),
			(assign, ":speed_limit", 1),
		(else_try),
			(assign, ":speed_limit", Top_Speed),
		(try_end),
		(agent_set_speed_limit, ":agent", ":speed_limit"),
		(try_begin),
			(this_or_next|le, ":speed", 0),	#reached previous destination or blocked OR
			(this_or_next|lt, ":speed_limit", Top_Speed),	#destination within reach OR
			(position_is_behind_position, pos1, Current_Pos),	#agent ahead of formation
			(store_add, ":slot", slot_team_d0_percent_in_place, ":fdivision"),
			(team_get_slot, reg0, ":fteam", ":slot"),
			(val_add, reg0, 1),
			(team_set_slot, ":fteam", ":slot", reg0),
		(try_end),
	(try_end),

	#Housekeeping
	(try_begin),
		(eq, ":rank", 1),
		(agent_set_slot, ":agent", slot_agent_in_first_rank, 1),
	(else_try),
		(agent_set_slot, ":agent", slot_agent_in_first_rank, 0),
	(try_end),
  ]),

  # script_equip_best_melee_weapon by motomataru
  # Input: agent id, flag to force shield, flag to force for length ALONE, current fire order
  # Output: none
  # Caba - edit to comply with weapon/shield-type orders
  ("equip_best_melee_weapon", [
	(store_script_param, ":agent", 1),
	(store_script_param, ":force_shield", 2),
	(store_script_param, ":force_length", 3),
	(store_script_param, ":fire_order", 4),

	(try_begin), #CABA additions
		(agent_get_division, ":division", ":agent"),
		(agent_get_team, ":team", ":agent"),
		(store_add, ":slot", slot_team_d0_order_weapon, ":division"),
		(team_slot_eq, ":team", ":slot", clear),
		
		(try_begin),
			(store_add, ":slot", slot_team_d0_order_shield, ":division"),
			(team_slot_eq, ":team", ":slot", shield),
			(assign, ":force_shield", 1),
		(try_end), #CABA additions end
	
		#priority items
		(assign, ":shield", itm_no_item),
		(assign, ":weapon", itm_no_item),
		(try_for_range, ":item_slot", ek_item_0, ek_head),
			(agent_get_item_slot, ":item", ":agent", ":item_slot"),
			(gt, ":item", itm_no_item),
			(item_get_type, ":weapon_type", ":item"),
			(try_begin),
				(eq, ":weapon_type", itp_type_shield),
				(assign, ":shield", ":item"),
			(else_try),
				(eq, ":weapon_type", itp_type_thrown),
				(eq, ":fire_order", aordr_fire_at_will),
				# (agent_get_ammo, ":ammo", ":agent", 0),	#assume infantry would have no other kind of ranged weapon
				# (gt, ":ammo", 0),
				(assign, ":weapon", ":item"),	#use thrown weapons first
			(try_end),
		(try_end),

		#select weapon
		(try_begin),
			(eq, ":weapon", itm_no_item),
			(assign, ":cur_score", 0),
			(try_for_range, ":item_slot", ek_item_0, ek_head),
				(agent_get_item_slot, ":item", ":agent", ":item_slot"),
				(gt, ":item", itm_no_item),
				(item_get_type, ":weapon_type", ":item"),
				(neq, ":weapon_type", itp_type_shield),

				(item_get_slot, reg0, ":item", slot_item_needs_two_hands),
				(this_or_next|eq, reg0, 0),
				(this_or_next|eq, ":force_shield", 0),
				(eq, ":shield", itm_no_item),
				
				(try_begin),
					(neq, ":force_length", 0),
					(item_get_slot, ":item_length", ":item", slot_item_length),
					(try_begin),
						(lt, ":cur_score", ":item_length"),
						(assign, ":cur_score", ":item_length"),
						(assign, ":weapon", ":item"),
					(try_end),
				(else_try),
					(assign, ":imod", imodbit_plain),
					(agent_get_troop_id, ":troop_id", ":agent"),
					(try_begin),    #only heroes have item modifications
						(troop_is_hero, ":troop_id"),
						(try_for_range, ":troop_item_slot",  ek_item_0, ek_head),    # heroes have only 4 possible weapons (equipped)
							(troop_get_inventory_slot, reg0, ":troop_id", ":troop_item_slot"),  #Find Item Slot with same item ID as Equipped Weapon
							(eq, reg0, ":item"),
							(troop_get_inventory_slot_modifier, ":imod", ":troop_id", ":troop_item_slot"),
						(try_end),
					(try_end), 

					(call_script, "script_get_item_score_with_imod", ":item", ":imod"),
					(lt, ":cur_score", reg0),
					(assign, ":cur_score", reg0),
					(assign, ":weapon", ":item"),
				(try_end),
			(try_end),
		(try_end),

		#equip selected items if needed
		(agent_get_wielded_item, reg0, ":agent", 0),
		(try_begin),
			(neq, reg0, ":weapon"),
			(try_begin),
				(gt, ":shield", itm_no_item),
				(agent_get_wielded_item, reg0, ":agent", 1),
				(neq, reg0, ":shield"),	#reequipping secondary will UNequip (from experience)
				(agent_set_wielded_item, ":agent", ":shield"),
			(try_end),
			(gt, ":weapon", itm_no_item),
			(agent_set_wielded_item, ":agent", ":weapon"),
		(try_end),
	(try_end),
  ]),

  # script_formation_current_position by motomataru
  # Input: destination position (not pos0), team, division
  # Output: in destination position
  # As opposed to script_battlegroup_get_position, this obtains target rotation
  ("formation_current_position", [
	(store_script_param, ":fposition", 1),
	(store_script_param, ":fteam", 2),
	(store_script_param, ":fdivision", 3),
	(call_script, "script_battlegroup_get_position", ":fposition", ":fteam", ":fdivision"),
	(call_script, "script_get_formation_destination", pos0, ":fteam", ":fdivision"),
	(position_copy_rotation, ":fposition", pos0),
	(call_script, "script_battlegroup_get_depth", ":fteam", ":fdivision"),
	(val_div, reg0, 2),	#position from script_battlegroup_get_position is in middle of bg
	(position_move_y, ":fposition", reg0, 0),
  ]),

  # script_get_centering_amount by motomataru
  # Input: formation type, number of troops, extra spacing
  #        Use formation type formation_default to use script for archer line
  # Output: reg0 number of centimeters to adjust x-position to center formation
  ("get_centering_amount", [
	(store_script_param, ":troop_formation", 1),
	(store_script_param, ":num_troops", 2),
	(store_script_param, ":extra_spacing", 3),
	(store_mul, ":troop_space", ":extra_spacing", 50),
	(val_add, ":troop_space", formation_minimum_spacing),
	(assign, reg0, 0),
	(try_begin),
		(eq, ":troop_formation", formation_square),
		(convert_to_fixed_point, ":num_troops"),
		(store_sqrt, reg0, ":num_troops"),
		(val_mul, reg0, ":troop_space"),
		(convert_from_fixed_point, reg0),
		(val_sub, reg0, ":troop_space"),
	(else_try),
		(this_or_next|eq, ":troop_formation", formation_ranks),
		(eq, ":troop_formation", formation_shield),
		(store_div, reg0, ":num_troops", 3),
		(try_begin),
			(store_mod, reg1, ":num_troops", 3),
			(eq, reg1, 0),
			(val_sub, reg0, 1),
		(try_end),
		(val_mul, reg0, ":troop_space"),
	(else_try),
		(this_or_next|eq, ":troop_formation", formation_none), #CABA - also a line
		(eq, ":troop_formation", formation_default),	#assume these are archers in a line
		(store_mul, reg0, ":num_troops", ":troop_space"),
	(try_end),
	(val_div, reg0, 2),
  ]),

  # script_formation_end
  # Input: team, division
  # Output: none
  ("formation_end", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(try_begin),
		(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
		(neg|team_slot_eq, ":fteam", ":slot", formation_none),
		(team_set_slot, ":fteam", ":slot", formation_none),
		(team_get_leader, ":leader", ":fteam"),
		
		(try_for_agents, ":agent"),
			(agent_is_alive, ":agent"),
			(agent_is_human, ":agent"),
			(agent_get_team, ":team", ":agent"),
			(eq, ":team", ":fteam"),
			(neq, ":leader", ":agent"),
			(agent_get_division, ":bgdivision", ":agent"),
			(eq, ":bgdivision", ":fdivision"),
			(agent_clear_scripted_mode, ":agent"),
			(agent_set_speed_limit, ":agent", 100),
			(agent_set_slot, ":agent", slot_agent_in_first_rank, 0),
			(agent_set_slot, ":agent", slot_agent_inside_formation, 0),
		(try_end),
		
		(try_begin),
			(eq, ":fteam", "$fplayer_team_no"),
			(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			
			#adjust for differences between the two systems of spreading out
			(set_show_messages, 0),
			(try_begin),
				(gt, ":div_spacing", 3),
				(assign, ":div_spacing", 2),	#Native maximum spread out
			(else_try),
				(gt, ":div_spacing", 0),
				(team_give_order, "$fplayer_team_no", ":fdivision", mordr_stand_closer),
				(try_begin),
					(gt, ":div_spacing", 1),
					(assign, ":div_spacing", 1),
				(else_try),
					(assign, ":div_spacing", 0),
				(try_end),
			(try_end),
			(set_show_messages, 1),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
		(try_end),
	(try_end),
  ]),

  # script_formation_move_position by motomataru
  # Input: team, division, formation current position, (1 to advance or -1 to withdraw or 0 to redirect)
  # Output: pos1 (offset for centering)
  ("formation_move_position", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fcurrentpos", 3),
	(store_script_param, ":direction", 4),
	(copy_position, pos1, ":fcurrentpos"),
	(call_script, "script_team_get_position_of_enemies", Enemy_Team_Pos, ":fteam", grc_everyone),
	(try_begin),
		(neq, reg0, 0),	#more than 0 enemies still alive?
		(copy_position, pos1, ":fcurrentpos"),	#restore current formation "position"
		(call_script, "script_point_y_toward_position", pos1, Enemy_Team_Pos),	#record angle from center to enemy
		(assign, ":distance_to_enemy", reg0),
		(call_script, "script_get_formation_destination", pos61, ":fteam", ":fdivision"),
		(get_distance_between_positions, ":move_amount", pos1, pos61),	#distance already moving from previous orders
		(val_add, ":move_amount", 1000),
		(try_begin),
			(gt, ":direction", 0),	#moving forward?
			(gt, ":move_amount", ":distance_to_enemy"),
			(assign, ":move_amount", ":distance_to_enemy"),
		(try_end),
		(val_mul, ":move_amount", ":direction"),
		(position_move_y, pos1, ":move_amount", 0),
		(try_begin),
			(lt, ":distance_to_enemy", 1000),	#less than a move away?
			(position_copy_rotation, pos1, pos61),	#avoid rotating formation
		(try_end),
		(call_script, "script_set_formation_destination", ":fteam", ":fdivision", pos1),
		(store_add, ":slot", slot_team_d0_size, ":fdivision"),
		(team_get_slot, ":num_troops", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
		(team_get_slot, ":formation_extra_spacing", ":fteam", ":slot"),
		(try_begin),
			(store_add, ":slot", slot_team_d0_type, ":fdivision"),
			(neg|team_slot_eq, ":fteam", ":slot", sdt_archer),
			(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
			(team_get_slot, ":fformation", ":fteam", ":slot"),
			(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
		(else_try),
			(call_script, "script_get_centering_amount", formation_default, ":num_troops", ":formation_extra_spacing"),
			(val_mul, reg0, -1),
		(try_end),
		(position_move_x, pos1, reg0, 0),
	(try_end),
  ]),

  # script_set_formation_destination by motomataru
  # Input: team, troop class, position
  # Kluge around buggy *_order_position functions for teams 0-3
  ("set_formation_destination", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fposition", 3),
	
	(position_get_x, ":x", ":fposition"),
	(position_get_y, ":y", ":fposition"),
	(position_get_rotation_around_z, ":zrot", ":fposition"),
	
	(store_add, ":slot", slot_team_d0_destination_x, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", ":x"),	
	(store_add, ":slot", slot_team_d0_destination_y, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", ":y"),	
	(store_add, ":slot", slot_team_d0_destination_zrot, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", ":zrot"),
	
	(team_set_order_position, ":fteam", ":fdivision", ":fposition"),
  ]),	

  # script_get_formation_destination by motomataru
  # Input: position, team, troop class
  # Output: input position (pos0 used)
  # Kluge around buggy *_order_position functions for teams 0-3
  ("get_formation_destination", [
	(store_script_param, ":fposition", 1),
	(store_script_param, ":fteam", 2),
	(store_script_param, ":fdivision", 3),
	(init_position, ":fposition"),
	(try_begin),
	    #(is_between, ":fteam", 0, 4), #Caba - this will always pass
		(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
		(neg|team_slot_eq, ":fteam", ":slot", formation_none), #caba adjust rather than team check
		(store_add, ":slot", slot_team_d0_destination_x, ":fdivision"),
		(team_get_slot, ":x", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_destination_y, ":fdivision"),
		(team_get_slot, ":y", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_destination_zrot, ":fdivision"),
		(team_get_slot, ":zrot", ":fteam", ":slot"),
		
		(position_set_x, ":fposition", ":x"),
		(position_set_y, ":fposition", ":y"),
		(position_rotate_z, ":fposition", ":zrot"),
	(else_try), 
		(store_add, ":slot", slot_team_d0_first_member, ":fdivision"),
		(team_get_slot, reg0, ":fteam", ":slot"),
		(try_begin),	  # "launder" team_get_order_position shutting down position_move_x
			(gt, reg0, -1),
			(team_get_order_position, ":fposition", ":fteam", ":fdivision"),
			(agent_get_position, pos0, reg0),
			(agent_set_position, reg0, ":fposition"),
			(agent_get_position, ":fposition", reg0),
			(agent_set_position, reg0, pos0),
		(try_end),
	(try_end),
	(position_set_z_to_ground_level, ":fposition"),
  ]),	

  # script_cf_battlegroup_valid_formation by Caba'drin
  # Input: team, division, formation
  # Output: reg0: troop count/1 if too few troops/0 if wrong type
  ("cf_battlegroup_valid_formation", [
    (store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fformation", 3),
	
	(assign, ":valid_type", 0),
	(store_add, ":slot", slot_team_d0_type, ":fdivision"),
	(team_get_slot, ":sd_type", ":fteam", ":slot"),
	(try_begin), #Eventually make this more complex with the sub-divisions
		(this_or_next|eq, ":sd_type", sdt_cavalry),
		(eq, ":sd_type", sdt_harcher),
		(assign, ":size_minimum", formation_min_cavalry_troops),
		(try_begin),
			(eq, ":fformation", formation_wedge),
			(assign, ":valid_type", 1),
		(try_end),
	(else_try),
		(eq, ":sd_type", sdt_archer),
		(assign, ":size_minimum", formation_min_foot_troops),
		(try_begin),
			(this_or_next|eq, ":fformation", formation_ranks),
			(eq, ":fformation", formation_default),
			(assign, ":valid_type", 1),
		(try_end),
	(else_try),
		(store_add, ":slot", slot_team_d0_order_sp_brace, ":fdivision"),
		(team_slot_eq, ":fteam", ":slot", 0), ##CABA - not braced
		(assign, ":size_minimum", formation_min_foot_troops),
		(neq, ":fformation", formation_none),
		(assign, ":valid_type", 1), #all types valid
	(try_end),
	
	(try_begin),
	    (eq, ":valid_type", 0),
		(assign, ":num_troops", 0),
	(else_try),
		(store_add, ":slot", slot_team_d0_size, ":fdivision"),
	    (team_get_slot, ":num_troops", ":fteam", ":slot"),
	    (lt, ":num_troops", ":size_minimum"),
		(assign, ":num_troops", 1),
	(try_end),
	
	(assign, reg0, ":num_troops"),
	(gt, ":num_troops", 1)
  ]),

  # script_cf_valid_formation_member by motomataru #CABA - Modified for Classify_agent phase out
  # Input: team, division, agent number of team leader, test agent
  # Output: failure indicates agent is not member of formation
  ("cf_valid_formation_member", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fleader", 3),
	(store_script_param, ":agent", 4),
	(neq, ":fleader", ":agent"),
	(agent_get_division, ":bgdivision", ":agent"),
	(try_begin), #Maintain any changed divisions
		(agent_slot_ge, ":agent", slot_agent_new_division, 0),
		(neg|agent_slot_eq, ":agent", slot_agent_new_division, ":bgdivision"),
		(agent_get_slot, ":bgdivision", ":agent", slot_agent_new_division),
		(agent_set_division, ":agent", ":bgdivision"),
	(try_end),
	(eq, ":bgdivision", ":fdivision"),
	(agent_get_team, ":team", ":agent"),
	(eq, ":team", ":fteam"),
	(agent_is_alive, ":agent"),
	(agent_is_human, ":agent"),
	(agent_slot_eq, ":agent", slot_agent_is_running_away, 0),
  ]),

# #Player team formations functions
  # script_player_attempt_formation
  # Inputs:	arg1: division
  #			arg2: formation identifier (formation_*)
  # Output: none
  ("player_attempt_formation", [
	(store_script_param, ":fdivision", 1),
	(store_script_param, ":fformation", 2),
	(store_script_param, ":at_pos", 3),
	(set_fixed_point_multiplier, 100),
	(try_begin),
		(eq, ":fformation", formation_ranks),
		(str_store_string, s1, "@ranks"),
	(else_try),
		(eq, ":fformation", formation_shield),
		(str_store_string, s1, "@shield wall"),
	(else_try),
		(eq, ":fformation", formation_wedge),
		(str_store_string, s1, "@wedge"),
	(else_try),
		(eq, ":fformation", formation_square),
		(str_store_string, s1, "@square"),
	(else_try),
		(str_store_string, s1, "@up"),
	(try_end),
	(str_store_class_name, s2, ":fdivision"),

	(try_begin),
		(call_script, "script_cf_battlegroup_valid_formation", "$fplayer_team_no", ":fdivision", ":fformation"),
		(try_begin),	#new formation?
			(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", ":fformation"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":fformation"),
			(display_message, "@{!}{s2} forming {s1}."),
			(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			
			#bring unformed divisions into sync with formations' minimum
			(set_show_messages, 0),
			(assign, reg0, ":div_spacing"),
			(try_for_range, reg1, reg0, formation_start_spread_out),	#spread out for ease of forming up	
				(team_give_order, "$fplayer_team_no", ":fdivision", mordr_spread_out),
				(val_add, ":div_spacing", 1),
			(try_end),
			(set_show_messages, 1),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
		(try_end),
		
	(else_try),
		(assign, ":return_val", reg0),
		(call_script, "script_formation_end", "$fplayer_team_no", ":fdivision"),
		(neq, ":fformation", formation_none),
		(try_begin),
			(gt, ":return_val", 0),
			(display_message, "@Not enough troops in {s2} to form {s1}, but holding."),
		(else_try),
			(store_add, ":slot", slot_team_d0_type, ":fdivision"),
			(team_get_slot, reg0, "$fplayer_team_no", ":slot"),
			(call_script, "script_str_store_division_type_name", s3, reg0),
			(display_message, "@{!}{s2} is an {s3} division and cannot form {s1}, so is holding."),
		(try_end),
	(try_end),
	(try_begin),
		(this_or_next|eq, ":at_pos", 0),
		(eq, formation_place_around_leader, 1),
		(call_script, "script_battlegroup_place_around_leader", "$fplayer_team_no", ":fdivision"),
	(else_try),
		(call_script, "script_battlegroup_place_at_leader", "$fplayer_team_no", ":fdivision"),
	(try_end),
  ]),

  # script_str_store_division_type_name by motomataru
  # Input:	destination, division type (sdt_*)
  # Output: none
  ("str_store_division_type_name", [
	(store_script_param, ":str_reg", 1),
	(store_script_param, ":division_type", 2),
	(try_begin),
		(eq, ":division_type", sdt_infantry),
		(str_store_string, ":str_reg", "@infantry"),
	(else_try),
		(eq, ":division_type", sdt_archer),
		(str_store_string, ":str_reg", "@archer"),
	(else_try),
		(eq, ":division_type", sdt_cavalry),
		(str_store_string, ":str_reg", "@cavalry"),
	(else_try),
		(eq, ":division_type", sdt_polearm),
		(str_store_string, ":str_reg", "@polearm"),
	(else_try),
		(eq, ":division_type", sdt_skirmisher),
		(str_store_string, ":str_reg", "@skirmisher"),
	(else_try),
		(eq, ":division_type", sdt_harcher),
		(str_store_string, ":str_reg", "@mounted archer"),
	(else_try),
		(eq, ":division_type", sdt_support),
		(str_store_string, ":str_reg", "@support"),
	(else_try),
		(eq, ":division_type", sdt_bodyguard),
		(str_store_string, ":str_reg", "@bodyguard"),
	(else_try),
		(str_store_string, ":str_reg", "@undetermined type of"),
	(try_end),
  ]),
  
  # script_player_order_formations by motomataru
  # Inputs:	arg1: order to formation (mordr_*)
  # Output: none
  ("player_order_formations", [
	(store_script_param, ":forder", 1),
	(set_fixed_point_multiplier, 100),
	
	(try_begin), #On hold, any formations reform in new location		
		(eq, ":forder", mordr_hold),
		(call_script, "script_division_reset_places"),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_target_team, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", -1),
			(store_add, ":slot", slot_team_d0_size, ":division"),	#apply to all divisions (not just formations)
			(team_slot_ge, "$fplayer_team_no", ":slot", 1),
			(store_add, ":slot", slot_team_d0_fclock, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", 1),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(call_script, "script_player_attempt_formation", ":division", ":formation", 1),
		(try_end),
		
	(else_try),	#Follow is hold	repeated frequently
		(eq, ":forder", mordr_follow),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_target_team, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", -1),
			(store_add, ":slot", slot_team_d0_size, ":division"),	#apply to all divisions (not just formations)
			(team_slot_ge, "$fplayer_team_no", ":slot", 1),
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),	#update formations
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(call_script, "script_player_attempt_formation", ":division", ":formation", 1),

			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),
		(try_end),
		
	(else_try),	#charge or retreat ends formation
		(this_or_next|eq, ":forder", mordr_charge),
		(eq, ":forder", mordr_retreat),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_target_team, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", -1),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			(call_script, "script_formation_end", "$fplayer_team_no", ":division"),
			
			(store_add, ":slot", slot_team_d0_type, ":division"),
			#(store_add, reg0, ":division", 1),
			(str_store_class_name, s1, ":division"),
			(try_begin),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_infantry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_polearm),
				(display_message, "@{s1}: infantry formation disassembled."),
			(else_try),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(display_message, "@{s1}: archer formation disassembled."),
			(else_try),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_skirmisher),
				(display_message, "@{s1}: skirmisher formation disassembled."),
			(else_try),
				(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(display_message, "@{s1}: cavalry formation disassembled."),
			(else_try),
				(display_message, "@{s1}: formation disassembled."),			
			(try_end),
		(try_end),
		
	(else_try),	#dismount ends formation
		(eq, ":forder", mordr_dismount),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			(try_begin),
				(store_add, ":slot", slot_team_d0_type, ":division"),
				(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_formation_end", "$fplayer_team_no", ":division"),
				(display_message, "@Cavalry formation disassembled."),
				
			(else_try),	#address bug that cavalry in scripted mode won't dismount
				(try_for_agents, ":agent"),
					(agent_is_alive, ":agent"),
					(agent_is_human, ":agent"),
					(agent_get_team, ":team", ":agent"),
					(eq, ":team", "$fplayer_team_no"),
					(neq, "$fplayer_agent_no", ":agent"),
					(agent_get_division, ":bgdivision", ":agent"),
					(eq, ":bgdivision", ":division"),
					(agent_clear_scripted_mode, ":agent"),
					(agent_set_speed_limit, ":agent", 100),
				(try_end),
			(try_end),
        (try_end),
			
	(else_try), 
		(eq, ":forder", mordr_advance),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_target_team, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", -1),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_get_slot, ":prev_order", "$fplayer_team_no", ":slot"),	
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),	
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(neq, ":formation", formation_none),
			
			(store_add, ":slot", slot_team_d0_fclock, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", 1),
			
			(call_script, "script_formation_current_position", pos63, "$fplayer_team_no", ":division"),
			(try_begin),
				(neq, ":prev_order", mordr_advance),
				(call_script, "script_set_formation_destination", "$fplayer_team_no", ":division", pos63),
			(try_end),
			(call_script, "script_formation_move_position", "$fplayer_team_no", ":division", pos63, 1),

			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(else_try),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
			(else_try),
				(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(try_end),
        (try_end),			

	(else_try),
		(eq, ":forder", mordr_fall_back),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_target_team, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", -1),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_get_slot, ":prev_order", "$fplayer_team_no", ":slot"),	
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),	
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(neq, ":formation", formation_none),
			
			(store_add, ":slot", slot_team_d0_fclock, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", 1),
			
			(call_script, "script_formation_current_position", pos63, "$fplayer_team_no", ":division"),
			(try_begin),
				(neq, ":prev_order", mordr_fall_back),
				(call_script, "script_set_formation_destination", "$fplayer_team_no", ":division", pos63),
			(try_end),
			(call_script, "script_formation_move_position", "$fplayer_team_no", ":division", pos63, -1),			

			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(else_try),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
			(else_try),
				(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(try_end),
        (try_end),		

	(else_try),
		(eq, ":forder", mordr_stand_closer),		
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(gt, ":div_spacing", -3),	#Native formations go down to four ranks
			(val_sub, ":div_spacing", 1),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(neq, ":formation", formation_none),
			
			(store_add, ":slot", slot_team_d0_fclock, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", 1),
			
			(try_begin),	#bring unformed divisions into sync with formations' minimum
				(lt, ":div_spacing", 0),
				(set_show_messages, 0),
				(assign, reg0, ":div_spacing"),
				(try_for_range, reg1, reg0, 0),
					(team_give_order, "$fplayer_team_no", ":division", mordr_spread_out),
					(val_add, ":div_spacing", 1),
				(try_end),
				(set_show_messages, 1),
				(store_add, ":slot", slot_team_d0_formation_space, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
				
			(else_try),
				(call_script, "script_get_formation_destination", pos1, "$fplayer_team_no", ":division"),
				(store_add, ":slot", slot_team_d0_type, ":division"),
				(try_begin),
					(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
					(store_add, ":slot", slot_team_d0_size, ":division"),
					(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
					(call_script, "script_get_centering_amount", formation_default, ":troop_count", ":div_spacing"),
					(val_mul, reg0, -1),
					(position_move_x, pos1, reg0),				
					(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
				(else_try),
					(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
					(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
					(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
				(else_try),
					(store_add, ":slot", slot_team_d0_size, ":division"),
					(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
					(call_script, "script_get_centering_amount", ":formation", ":troop_count", ":div_spacing"),
					(position_move_x, pos1, reg0),
					(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
				(try_end),
			(try_end),
		(try_end),

	(else_try),
		(eq, ":forder", mordr_spread_out),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(try_begin),
				(this_or_next|neq, ":formation", formation_none),
				(lt, ":div_spacing", 2),	#Native maxes at 2
				(val_add, ":div_spacing", 1),
			(try_end),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
			
			(neq, ":formation", formation_none),
			
			(store_add, ":slot", slot_team_d0_fclock, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", 1),

			#bring unformed divisions into sync with formations' minimum
			(set_show_messages, 0),
			(assign, reg0, ":div_spacing"),
			(try_for_range, reg1, reg0, 1),
				(team_give_order, "$fplayer_team_no", ":division", mordr_spread_out),
				(val_add, ":div_spacing", 1),
			(try_end),
			(set_show_messages, 1),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),

			(call_script, "script_get_formation_destination", pos1, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
			    (store_add, ":slot", slot_team_d0_size, ":division"),
	            (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
			    (call_script, "script_get_centering_amount", formation_default, ":troop_count", ":div_spacing"),
			    (val_mul, reg0, -1),
			    (position_move_x, pos1, reg0),				
				(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(else_try),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
			(else_try),
				(store_add, ":slot", slot_team_d0_size, ":division"), 
	            (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
				(call_script, "script_get_centering_amount", ":formation", ":troop_count", ":div_spacing"),
			    (position_move_x, pos1, reg0),
				(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"), 
			(try_end),
		(try_end),

	(else_try),
		(eq, ":forder", mordr_stand_ground),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_target_team, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", -1),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),	
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(neq, ":formation", formation_none),
			
			(store_add, ":slot", slot_team_d0_fclock, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", 1),
			
			(call_script, "script_formation_current_position", pos63, "$fplayer_team_no", ":division"),
			(copy_position, pos1, pos63),		
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
			    (store_add, ":slot", slot_team_d0_size, ":division"),
	            (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
			    (call_script, "script_get_centering_amount", formation_default, ":troop_count", ":div_spacing"),
			    (val_mul, reg0, -1),
			    (position_move_x, pos1, reg0),				
				(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(else_try),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
			(else_try),
				(store_add, ":slot", slot_team_d0_size, ":division"),
	            (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),	
				(call_script, "script_get_centering_amount", ":formation", ":troop_count", ":div_spacing"),
			    (position_move_x, pos1, reg0),
				(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(try_end),
			(call_script, "script_set_formation_destination", "$fplayer_team_no", ":division", pos63),
		(try_end),			
	(try_end)
  ]),

  
# #Utilities used by formations
  # script_point_y_toward_position by motomataru
  # Input: from position, to position
  # Output: reg0 fixed point distance
  ("point_y_toward_position", [
	(store_script_param, ":from_position", 1),
	(store_script_param, ":to_position", 2),
	(position_get_x, ":dist_x_to_cosine", ":to_position"),
	(position_get_x, ":from_coord", ":from_position"),
	(val_sub, ":dist_x_to_cosine", ":from_coord"),
	(store_mul, ":sum_square", ":dist_x_to_cosine", ":dist_x_to_cosine"),
	(position_get_y, ":dist_y_to_sine", ":to_position"),
	(position_get_y, ":from_coord", ":from_position"),
	(val_sub, ":dist_y_to_sine", ":from_coord"),
	(store_mul, reg0, ":dist_y_to_sine", ":dist_y_to_sine"),
	(val_add, ":sum_square", reg0),
	(convert_from_fixed_point, ":sum_square"),
	(store_sqrt, ":distance_between", ":sum_square"),
	(try_begin),
		(gt, ":distance_between", 0),
		(convert_to_fixed_point, ":dist_x_to_cosine"),
		(val_div, ":dist_x_to_cosine", ":distance_between"),
		(convert_to_fixed_point, ":dist_y_to_sine"),
		(val_div, ":dist_y_to_sine", ":distance_between"),
		(try_begin),
			(lt, ":dist_x_to_cosine", 0),
			(assign, ":bound_a", 90),
			(assign, ":bound_b", 270),
			(assign, ":theta", 180),
		(else_try),
			(assign, ":bound_a", 90),
			(assign, ":bound_b", -90),
			(assign, ":theta", 0),
		(try_end),
		(assign, ":sine_theta", 0),	#avoid error on compile
		(convert_to_fixed_point, ":theta"),
		(convert_to_fixed_point, ":bound_a"),
		(convert_to_fixed_point, ":bound_b"),
		(try_for_range, reg0, 0, 6),	#precision 90/2exp6 (around 2 degrees)
			(store_sin, ":sine_theta", ":theta"),
			(try_begin),
				(gt, ":sine_theta", ":dist_y_to_sine"),
				(assign, ":bound_a", ":theta"),
			(else_try),
				(lt, ":sine_theta", ":dist_y_to_sine"),
				(assign, ":bound_b", ":theta"),
			(try_end),
			(store_add, ":angle_sum", ":bound_b", ":bound_a"),
			(store_div, ":theta", ":angle_sum", 2),
		(try_end),
		(convert_from_fixed_point, ":theta"),
		(position_get_rotation_around_z, reg0, ":from_position"),
		(val_sub, ":theta", reg0),
		(val_sub, ":theta", 90),	#point y-axis at destination
		(position_rotate_z, ":from_position", ":theta"),
	(try_end),
	
	(assign, reg0, ":distance_between"),
  ]),

  #script_agent_fix_division by Caba'drin
  #Input: agent_id
  #Output: nothing (agent divisions changed, slot set) 
  #To fix AI troop divisions from the engine applying player's party divisions on all agents
  #This is called after agent_reassign_team, so can safely assume correct team is set
  ("agent_fix_division",
   [
    (store_script_param_1, ":agent"),	
	(agent_set_slot, ":agent", slot_agent_new_division, -1),	
	(get_player_agent_no, ":player"),	#after_mission_start triggers are called after spawn, so globals can't be used yet
	
	(try_begin),
	    (ge, ":player", 0),
		(neq, ":agent", ":player"),
		(agent_is_human, ":agent"),
		(agent_get_team, ":player_team", ":player"),
		(agent_get_team, ":team", ":agent"),
		(this_or_next|main_hero_fallen),
		(neq, ":team", ":player_team"),
		(agent_get_troop_id, ":troop", ":agent"),
		(try_begin),
			(troop_is_guarantee_horse, ":troop"),
			(assign, ":target_division", grc_cavalry),
		(else_try),
			(troop_is_guarantee_ranged, ":troop"),
			(assign, ":target_division", grc_archers),
		(else_try),
			(assign, ":target_division", grc_infantry),		
		(try_end),
		(agent_get_division, ":division", ":agent"),
		(neq, ":division", ":target_division"),
		(agent_set_division, ":agent", ":target_division"),
		(agent_set_slot, ":agent", slot_agent_new_division, ":target_division"),
	(try_end),
   ]),
  

  
  # script_store_battlegroup_type by Caba'drin   ##NEEDS EDIT per PMs with moto
  # Input: team, division
  # Output: reg0 and slot_team_dx_type with sdt_* value
  # Automatically called from store_battlegroup_data
  ("store_battlegroup_type", [
    (store_script_param_1, ":fteam"),
	(store_script_param_2, ":fdivision"),
	
	#hard-code the traditional three
	(try_begin),
		(eq, ":fdivision", grc_infantry),
		(assign, ":div_type", sdt_infantry),
	(else_try),
		(eq, ":fdivision", grc_archers),
		(assign, ":div_type", sdt_archer),
	(else_try),
		(eq, ":fdivision", grc_cavalry),
		(assign, ":div_type", sdt_cavalry),
		
	#attempt to type the rest
	(else_try),
		(assign, ":count_infantry", 0),
		(assign, ":count_archer", 0),
		(assign, ":count_cavalry", 0),
		(assign, ":count_harcher", 0),
		(assign, ":count_polearms", 0),
		(assign, ":count_skirmish", 0),
		(assign, ":count_support", 0),
		(assign, ":count_bodyguard", 0),	

		(try_for_agents, ":cur_agent"),
			(agent_is_alive, ":cur_agent"),      
			(agent_is_human, ":cur_agent"), 
			(agent_slot_eq, ":cur_agent", slot_agent_is_running_away, 0),
			(agent_get_team, ":bgteam", ":cur_agent"),
			(eq, ":bgteam", ":fteam"),
			#(call_script, "script_classify_agent", ":cur_agent"),
			#(assign, ":bgdivision", reg0),
			(team_get_leader, ":leader", ":fteam"),
			(neq, ":leader", ":cur_agent"),
			(agent_get_division, ":bgdivision", ":cur_agent"),
			(eq, ":bgdivision", ":fdivision"),
			(agent_get_troop_id, ":cur_troop", ":cur_agent"),
			(agent_get_ammo, ":cur_ammo", ":cur_agent", 0),
			(agent_get_wielded_item, reg0, ":cur_agent", 0),
			
			(try_begin),
				(lt, reg0, 0),
				(assign, ":cur_weapon_type", 0),
			(else_try),
				(item_get_type, ":cur_weapon_type", reg0), 
			(try_end),
			
			(try_begin),
				(neg|troop_is_hero, ":cur_troop"),
				(try_begin), #Cavalry	
					(agent_get_horse, reg0, ":cur_agent"),
					(ge, reg0, 0),
					(try_begin),				
						(gt, ":cur_ammo", 0),
						(val_add, ":count_harcher", 1),
					(else_try),
						(val_add, ":count_cavalry", 1),
					(try_end),
				(else_try), #Archers
					(gt, ":cur_ammo", 0),
					(try_begin),
						(eq, ":cur_weapon_type", itp_type_thrown),
						(val_add, ":count_skirmish", 1),
					(else_try),
						(val_add, ":count_archer", 1),
					(try_end),
				(else_try), #Infantry
					(try_begin),
						(eq, ":cur_weapon_type", itp_type_polearm),
						(val_add, ":count_polearms", 1),
					(else_try),
						(val_add, ":count_infantry", 1),
					(try_end),			    
				(try_end),
			(else_try), #Heroes
				(assign, ":support_skills", 0), #OPEN TO SUGGESTIONS HERE    ?skl_trade, skl_spotting, skl_pathfinding, skl_tracking?
				(store_skill_level, reg0, skl_engineer, ":cur_troop"),
				(val_add, ":support_skills", reg0),
				(store_skill_level, reg0, skl_first_aid, ":cur_troop"),
				(val_add, ":support_skills", reg0),
				(store_skill_level, reg0, skl_surgery, ":cur_troop"),
				(val_add, ":support_skills", reg0),
				(store_skill_level, reg0, skl_wound_treatment, ":cur_troop"),
				(val_add, ":support_skills", reg0),
				(try_begin),
					(gt, ":support_skills", 5),
					(val_add, ":count_support", 1),
				(else_try),
					(val_add, ":count_bodyguard", 1),
				(try_end),		
			(try_end), #Regular v Hero		
		(try_end), #Agent Loop	
			
		#Do Comparisons With Counts, set ":div_type"
		(assign, ":slot", slot_team_d0_type),
		(team_set_slot, scratch_team, ":slot", ":count_infantry"),
		(val_add, ":slot", 1),
		(team_set_slot, scratch_team, ":slot", ":count_archer"),
		(val_add, ":slot", 1),
		(team_set_slot, scratch_team, ":slot", ":count_cavalry"),
		(val_add, ":slot", 1),
		(team_set_slot, scratch_team, ":slot", ":count_polearms"),
		(val_add, ":slot", 1),
		(team_set_slot, scratch_team, ":slot", ":count_skirmish"),
		(val_add, ":slot", 1),
		(team_set_slot, scratch_team, ":slot", ":count_harcher"),
		(val_add, ":slot", 1),
		(team_set_slot, scratch_team, ":slot", ":count_support"),
		(val_add, ":slot", 1),
		(team_set_slot, scratch_team, ":slot", ":count_bodyguard"),

		(assign, ":count_to_beat", 0),
		(assign, ":count_total", 0),
		(try_for_range, ":type", sdt_infantry, sdt_infantry + 8), #only 8 sdt_types at the moment
			(store_add, ":slot", slot_team_d0_type, ":type"),
			(team_get_slot, ":count", scratch_team, ":slot"),
			(val_add, ":count_total", ":count"),
			(lt, ":count_to_beat", ":count"),
			(assign, ":count_to_beat", ":count"),
			(assign, ":div_type", ":type"),
		(try_end),
		
		(val_mul, ":count_to_beat", 2),
		(try_begin),
			(lt, ":count_to_beat", ":count_total"), #Less than half of this division
			(assign, ":count_to_beat", 0),
			(assign, ":div_type", -1),
			(try_for_range, ":type", sdt_infantry, sdt_infantry + 3), #check main types for a majority
				(store_add, ":slot", slot_team_d0_type, ":type"),
				(team_get_slot, ":count", scratch_team, ":slot"),
				(val_add, ":slot", 3),	#subtype is three more than main type
				(team_get_slot, reg0, scratch_team, ":slot"),
				(val_add, ":count", reg0),
				(lt, ":count_to_beat", ":count"),
				(assign, ":count_to_beat", ":count"),
				(assign, ":div_type", ":type"),
			(try_end),
		
			(val_mul, ":count_to_beat", 2),
			(lt, ":count_to_beat", ":count_total"), #Less than half of this division
			(assign, ":div_type", sdt_unknown), #Or 0
		(try_end),
	(try_end),	#divisions 3-8
	
	(store_add, ":slot", slot_team_d0_type, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", ":div_type"),
	(assign, reg0, ":div_type"),  
  ]),

  # script_store_battlegroup_data by motomataru #EDITED TO SLOTS FOR MANY DIVISIONS BY CABA'DRIN
  # Input: none
  # Output: sets positions and globals to track data on ALL groups in a battle
  # Globals used: pos1, reg0, reg1, #CABA - NO LONGER USED: positions 24-45
  ("store_battlegroup_data", [
	(assign, ":team0_leader", 0),
	(assign, ":team0_x_leader", 0),
	(assign, ":team0_y_leader", 0),
	(assign, ":team0_level_leader", 0),
	(assign, ":team1_leader", 0),
	(assign, ":team1_x_leader", 0),
	(assign, ":team1_y_leader", 0),
	(assign, ":team1_level_leader", 0),
	(assign, ":team2_leader", 0),
	(assign, ":team2_x_leader", 0),
	(assign, ":team2_y_leader", 0),
	(assign, ":team2_level_leader", 0),
	(assign, ":team3_leader", 0),
	(assign, ":team3_x_leader", 0),
	(assign, ":team3_y_leader", 0),
	(assign, ":team3_level_leader", 0),
	
	#Team Slots reset every mission, like agent slots, but just to be sure for when it gets called during the mission
	(try_for_range, ":team", 0, 4),
		(try_for_range, ":slot", reset_team_stats_begin, reset_team_stats_end), #Those within the "RESET GROUP" in formations_constants
			(team_set_slot, ":team", ":slot", 0),
		(try_end),	
        (try_for_range, ":division", 0, 9), #CABA trial to have an agent to get for non-formation divisions
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_slot_eq, ":team", ":slot", formation_none),
			(store_add, ":slot", slot_team_d0_first_member, ":division"),
			(team_set_slot, ":team", ":slot", -1),
		(try_end),
	(try_end),

	(try_for_agents, ":cur_agent"),
		(agent_is_alive, ":cur_agent"),      
		(agent_is_human, ":cur_agent"), 
		(agent_get_division, ":bgdivision", ":cur_agent"),
		(try_begin), #Maintain any changed divisions
			(agent_slot_ge, ":cur_agent", slot_agent_new_division, 0),
			(neg|agent_slot_eq, ":cur_agent", slot_agent_new_division, ":bgdivision"),
			(agent_get_slot, ":bgdivision", ":cur_agent", slot_agent_new_division),
			(agent_set_division, ":cur_agent", ":bgdivision"),
		(try_end),
		(agent_slot_eq, ":cur_agent", slot_agent_is_running_away, 0),
		(agent_get_team, ":bgteam", ":cur_agent"),
		#(call_script, "script_classify_agent", ":cur_agent"),
		#(assign, ":bgdivision", reg0),
		#(agent_get_division, ":bgdivision", ":cur_agent"),
		(try_begin),
			(team_get_leader, ":leader", ":bgteam"),
		    (eq, ":leader", ":cur_agent"),
			(assign, ":bgdivision", -1),
		(try_end),
		(agent_get_troop_id, ":cur_troop", ":cur_agent"),
		(store_character_level, ":cur_level", ":cur_troop"),
		(agent_get_ammo, ":cur_ammo", ":cur_agent", 0),
		(assign, ":cur_weapon_type", 0),
		(assign, ":cur_weapon_length", 0),
		(assign, ":cur_swung_weapon_length", 0),
		(agent_get_wielded_item, ":cur_weapon", ":cur_agent", 0),
		(try_begin),
			(is_between, ":cur_weapon", weapons_begin, weapons_end),
			(item_get_slot, ":cur_weapon_length", ":cur_weapon", slot_item_length),

			(item_get_slot, reg0, ":cur_weapon", slot_item_thrust_damage),
			(item_slot_ge, ":cur_weapon", slot_item_swing_damage, reg0),
			(assign, ":cur_swung_weapon_length", ":cur_weapon_length"),
		(try_end),
		(agent_get_position, pos1, ":cur_agent"),
		(position_get_x, ":x_value", pos1),
		(position_get_y, ":y_value", pos1),
		(try_begin),
		    (eq, ":bgdivision", -1), #Leaders
			(try_begin),
				(eq, ":bgteam", 0),
				(assign, ":team0_leader", 1),
				(assign, ":team0_x_leader", ":x_value"),
				(assign, ":team0_y_leader", ":y_value"),
				(assign, ":team0_level_leader", ":cur_level"),
			(else_try),
				(eq, ":bgteam", 1),
				(assign, ":team1_leader", 1),
				(assign, ":team1_x_leader", ":x_value"),
				(assign, ":team1_y_leader", ":y_value"),
				(assign, ":team1_level_leader", ":cur_level"),
			(else_try),
				(eq, ":bgteam", 2),
				(assign, ":team2_leader", 1),
				(assign, ":team2_x_leader", ":x_value"),
				(assign, ":team2_y_leader", ":y_value"),
				(assign, ":team2_level_leader", ":cur_level"),
			(else_try),
				(eq, ":bgteam", 3),
				(assign, ":team3_leader", 1),
				(assign, ":team3_x_leader", ":x_value"),
				(assign, ":team3_y_leader", ":y_value"),
				(assign, ":team3_level_leader", ":cur_level"),
			(try_end),
		(else_try),
			# (agent_get_ammo, reg0, ":cur_agent", 1),	#Division in Melee
			(try_begin),
				# (le, reg0, 0),	#not wielding ranged weapon?
				(store_add, ":slot", slot_team_d0_in_melee, ":bgdivision"),
				(team_slot_eq, ":bgteam", ":slot", 0),
				(agent_get_attack_action, reg0, ":cur_agent"),
				(gt, reg0, 0),
				(team_set_slot, ":bgteam", ":slot", 1),
			(try_end),
			
			(store_add, ":slot", slot_team_d0_size, ":bgdivision"), #Division Count
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", 1),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(try_begin), #CABA - set first_member for unformed divisions to have an agent to get - testing - seems to do what i needed
				(store_add, ":slot", slot_team_d0_formation, ":bgdivision"),
				(team_slot_eq, ":bgteam", ":slot", formation_none),
				(store_add, ":slot", slot_team_d0_first_member, ":bgdivision"),
				(neg|team_slot_ge, ":bgteam", ":slot", 0),
				(team_set_slot, ":bgteam", ":slot", ":cur_agent"),
			(try_end),
			
			(try_begin),
				(gt, ":cur_ammo", 0),
				(store_add, ":slot", slot_team_d0_percent_ranged, ":bgdivision"), #Division Percentage are Archers
				(team_get_slot, ":value", ":bgteam", ":slot"),
				(val_add, ":value", 1),
				(team_set_slot, ":bgteam", ":slot", ":value"),
			(else_try),
				(store_add, ":slot", slot_team_d0_low_ammo, ":bgdivision"), #Division Running out of Ammo Flag
				(team_set_slot, ":bgteam", ":slot", 1),
			(try_end),
			
			(try_begin),
				(eq, ":cur_weapon_type", itp_type_thrown),
				(store_add, ":slot", slot_team_d0_percent_throwers, ":bgdivision"), #Division Percentage are Throwers
				(team_get_slot, ":value", ":bgteam", ":slot"),
				(val_add, ":value", 1),
				(team_set_slot, ":bgteam", ":slot", ":value"),
			(try_end),
			
			(store_add, ":slot", slot_team_d0_level, ":bgdivision"), #Division Level
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":cur_level"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_weapon_length, ":bgdivision"), #Division Weapon Length
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":cur_weapon_length"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_swung_weapon_length, ":bgdivision"), #Division Swung Weapon Length
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":cur_swung_weapon_length"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(try_begin),	#Division First Rank Weapon Length
				(agent_slot_ge, ":cur_agent", slot_agent_in_first_rank, 1),
				(store_add, ":slot", slot_team_d0_front_weapon_length, ":bgdivision"),
				(team_get_slot, ":value", ":bgteam", ":slot"),
				(val_add, ":value", ":cur_weapon_length"),
				(team_set_slot, ":bgteam", ":slot", ":value"),
				(store_add, ":slot", slot_team_d0_front_agents, ":bgdivision"),
				(team_get_slot, ":value", ":bgteam", ":slot"),
				(val_add, ":value", 1),
				(team_set_slot, ":bgteam", ":slot", ":value"),
			(try_end),
			
			(store_add, ":slot", slot_team_d0_avg_x, ":bgdivision"), #Position X
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":x_value"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_avg_y, ":bgdivision"), #Position Y
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":y_value"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
		(try_end), #Leader vs Regular
		
		(agent_get_class, ":troop_class", ":cur_agent"),
		(try_begin),
			(eq, ":troop_class", grc_archers),
			(team_get_slot, ":value", ":bgteam", slot_team_num_archers),
			(val_add, ":value", 1),
			(team_set_slot, ":bgteam", slot_team_num_archers, ":value"),
			
		(else_try),
			(eq, ":troop_class", grc_cavalry),
			(team_get_slot, ":value", ":bgteam", slot_team_num_cavalry),
			(val_add, ":value", 1),
			(team_set_slot, ":bgteam", slot_team_num_cavalry, ":value"),
			
		(else_try),
			(eq, ":troop_class", grc_infantry),
			(team_get_slot, ":value", ":bgteam", slot_team_num_infantry),
			(val_add, ":value", 1),
			(team_set_slot, ":bgteam", slot_team_num_infantry, ":value"),
			
			#agent is the nearest infantry to enemy starting point?
			(try_for_range, ":enemy_team_no", 0, 4),
				(teams_are_enemies, ":enemy_team_no", ":bgteam"),
				(team_get_slot, reg0, ":enemy_team_no", slot_team_starting_x),
				(position_set_x, pos0, reg0),
				(team_get_slot, reg0, ":enemy_team_no", slot_team_starting_y),
				(position_set_y, pos0, reg0),
				(position_set_z_to_ground_level, pos0),
				(get_distance_between_positions, ":new_distance", pos0, pos1),
				
				(team_get_slot, ":old_distance", ":enemy_team_no", slot_team_dist_enemy_inf_to_start),
				(try_begin),
					(this_or_next|eq, ":old_distance", 0),
					(lt, ":new_distance", ":old_distance"),
					(team_set_slot, ":enemy_team_no", slot_team_dist_enemy_inf_to_start, ":new_distance"),
				(try_end),
			(try_end),
		(try_end),
		
		#find nearest enemy agent
		(agent_set_slot, ":cur_agent", slot_agent_nearest_enemy_agent, -1),
		(try_for_agents, ":enemy_agent"),
			(agent_is_alive, ":enemy_agent"),
			(agent_is_human, ":enemy_agent"),
			(agent_get_team, ":enemy_team_no", ":enemy_agent"),
			(teams_are_enemies, ":enemy_team_no", ":bgteam"),
			(agent_slot_eq, ":enemy_agent", slot_agent_is_running_away, 0),
			(agent_get_position, pos0, ":enemy_agent"),
			(get_distance_between_positions, ":new_distance", pos0, pos1),
			
			(try_begin),
				(agent_get_slot, ":closest_enemy", ":cur_agent", slot_agent_nearest_enemy_agent),
				(eq, ":closest_enemy", -1),
				(agent_set_slot, ":cur_agent", slot_agent_nearest_enemy_agent, ":enemy_agent"),
				
			(else_try),
				(agent_get_position, pos2, ":closest_enemy"),
				(get_distance_between_positions, ":old_distance", pos2, pos1),
				(lt, ":new_distance", ":old_distance"),
				(agent_set_slot, ":cur_agent", slot_agent_nearest_enemy_agent, ":enemy_agent"),
			(try_end),
		(try_end),
		
		#update division information
		(try_begin),
		    (ge, ":bgdivision", 0),	#not leaders
			(agent_get_slot, ":closest_enemy", ":cur_agent", slot_agent_nearest_enemy_agent),
			(neq, ":closest_enemy", -1),
			(agent_get_position, pos0, ":closest_enemy"),
			(get_distance_between_positions, ":new_distance", pos0, pos1),
			
			(try_begin),
				(lt, ":new_distance", 350),
				(agent_get_division, reg0, ":closest_enemy"),
				(store_add, ":slot", slot_team_d0_enemy_supporting_melee, reg0),
				(agent_get_team, reg0, ":closest_enemy"),
				(team_get_slot, ":value", reg0, ":slot"),
				(val_add, ":value", 1),
				(team_set_slot, reg0, ":slot", ":value"),
			(try_end),
			
			(store_add, ":slot", slot_team_d0_closest_enemy_dist, ":bgdivision"),
			(team_get_slot, ":old_distance", ":bgteam", ":slot"),
			(try_begin),
				(this_or_next|eq, ":old_distance", 0),
				(lt, ":new_distance", ":old_distance"),
				(team_set_slot, ":bgteam", ":slot", ":new_distance"),
				(store_add, ":slot", slot_team_d0_closest_enemy, ":bgdivision"),
				(team_set_slot, ":bgteam", ":slot", ":closest_enemy"),
			(try_end),
			
			(assign, ":doit", 0),
			(agent_get_class, ":enemy_troop_class", ":closest_enemy"),
			(store_add, ":slot", slot_team_d0_type, ":bgdivision"),
			(team_get_slot, ":value", ":bgteam", ":slot"),
			
			#AI infantry division tracks non-infantry to preferably chase
			(try_begin),
				(this_or_next|eq, ":value", sdt_polearm),
				(eq, ":value", sdt_infantry),
				(neq, ":enemy_troop_class", grc_cavalry),
				(assign, ":doit", 1),
				
			#AI archer division tracks infantry to avoid
			(else_try),
				(this_or_next|eq, ":value", sdt_archer),
				(eq, ":value", sdt_skirmisher),
				(eq, ":enemy_troop_class", grc_infantry),
				(assign, ":doit", 1),
			(try_end),
			
			(eq, ":doit", 1),
			(store_add, ":slot", slot_team_d0_closest_enemy_special_dist, ":bgdivision"),
			(team_get_slot, ":old_distance", ":bgteam", ":slot"),
			(try_begin),
				(this_or_next|eq, ":old_distance", 0),
				(lt, ":new_distance", ":old_distance"),
				(team_set_slot, ":bgteam", ":slot", ":new_distance"),
				(store_add, ":slot", slot_team_d0_closest_enemy_special, ":bgdivision"),
				(team_set_slot, ":bgteam", ":slot", ":closest_enemy"),
			(try_end),
		(try_end),
	(try_end), #Agent Loop
	
	#calculate team sizes, sum positions; within calculate battle group averages
	(try_for_range, ":team", 0, 4),
	    (assign, ":team_size", 0),
		(assign, ":team_level", 0),
		(assign, ":team_x", 0),
		(assign, ":team_y", 0),
		
	    (try_for_range, ":division", 0, 9),
		    #sum for team averages
		    (store_add, ":slot", slot_team_d0_size, ":division"),
		    (team_get_slot, ":division_size", ":team", ":slot"),
			(gt, ":division_size", 0),
			(val_add, ":team_size", ":division_size"),
			
			(store_add, ":slot", slot_team_d0_level, ":division"),
		    (team_get_slot, ":division_level", ":team", ":slot"),
			(val_add, ":team_level", ":division_level"),
			
			(store_add, ":slot", slot_team_d0_avg_x, ":division"),
		    (team_get_slot, ":division_x", ":team", ":slot"),
			(val_add, ":team_x", ":division_x"),
			
			(store_add, ":slot", slot_team_d0_avg_y, ":division"),
		    (team_get_slot, ":division_y", ":team", ":slot"),
			(val_add, ":team_y", ":division_y"),
			
            #calculate battle group averages
			(store_add, ":slot", slot_team_d0_level, ":division"),
			(val_div, ":division_level", ":division_size"),			
			(team_set_slot, ":team", ":slot", ":division_level"),
			
			(store_add, ":slot", slot_team_d0_percent_ranged, ":division"),
			(team_get_slot, ":value", ":team", ":slot"),
			(val_mul, ":value", 100),
			(val_div, ":value", ":division_size"), 
			(team_set_slot, ":team", ":slot", ":value"),	

			(store_add, ":slot", slot_team_d0_percent_throwers, ":division"),
			(team_get_slot, ":value", ":team", ":slot"),
			(val_mul, ":value", 100),
			(val_div, ":value", ":division_size"), 
			(team_set_slot, ":team", ":slot", ":value"),	
		
			(store_add, ":slot", slot_team_d0_weapon_length, ":division"),
		    (team_get_slot, ":value", ":team", ":slot"),
			(val_div, ":value", ":division_size"),
			(team_set_slot, ":team", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_swung_weapon_length, ":division"),
		    (team_get_slot, ":value", ":team", ":slot"),
			(val_div, ":value", ":division_size"),
			(team_set_slot, ":team", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_front_agents, ":division"),
			(team_get_slot, reg0, ":team", ":slot"),
			(try_begin),
				(gt, reg0, 0),
				(store_add, ":slot", slot_team_d0_front_weapon_length, ":division"),
				(team_get_slot, ":value", ":team", ":slot"),
				(val_div, ":value", reg0),
				(team_set_slot, ":team", ":slot", ":value"),
			(try_end),
			
			(store_add, ":slot", slot_team_d0_avg_x, ":division"),
			(val_div, ":division_x", ":division_size"),
		    (team_set_slot, ":team", ":slot", ":division_x"),
			
			(store_add, ":slot", slot_team_d0_avg_y, ":division"),
			(val_div, ":division_y", ":division_size"),
		    (team_set_slot, ":team", ":slot", ":division_y"),
			
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(team_get_slot, reg0, ":team", ":slot"),
			(try_begin),
				(neg|is_between, reg0, 0, 8),	#TODO reset on reinforcements
                (call_script, "script_store_battlegroup_type", ":team", ":division"),
			(try_end),
		(try_end), #Division Loop
		
		#Team Leader Additions
		(try_begin),
		    (eq, ":team", 0),
			(val_add, ":team_size", ":team0_leader"),
			(val_add, ":team_level", ":team0_level_leader"),
			(val_add, ":team_x", ":team0_x_leader"),
			(val_add, ":team_y", ":team0_y_leader"),
		(else_try),
		    (eq, ":team", 1),
			(val_add, ":team_size", ":team1_leader"),
			(val_add, ":team_level", ":team1_level_leader"),
			(val_add, ":team_x", ":team1_x_leader"),
			(val_add, ":team_y", ":team1_y_leader"),
		(else_try),
			(eq, ":team", 2),
			(val_add, ":team_size", ":team2_leader"),
			(val_add, ":team_level", ":team2_level_leader"),
			(val_add, ":team_x", ":team2_x_leader"),
			(val_add, ":team_y", ":team2_y_leader"),
		(else_try),
			(eq, ":team", 3),
			(val_add, ":team_size", ":team3_leader"),
			(val_add, ":team_level", ":team3_level_leader"),
			(val_add, ":team_x", ":team3_x_leader"),
			(val_add, ":team_y", ":team3_y_leader"),		
		(try_end),
		
		#calculate team averages 
		(gt, ":team_size", 0),
		(team_set_slot, ":team", slot_team_size, ":team_size"),
		(val_div, ":team_level", ":team_size"),
		(team_set_slot, ":team", slot_team_level, ":team_level"),	
			
		(val_div, ":team_x", ":team_size"),
		(team_set_slot, ":team", slot_team_avg_x, ":team_x"),
		(val_div, ":team_y", ":team_size"),
		(team_set_slot, ":team", slot_team_avg_y, ":team_y"),
	(try_end), #Team Loop
	]),

  # script_battlegroup_get_position by motomataru #CABA - EDITED TO USE SLOTS, NOT STORED POS NUMBERS
  # Input: destination position, team, division
  # Output:	battle group position
  #			average team position if "troop class" input NOT set to 0-8
  # NB: Assumes that battle groups beyond 2 are PLAYER team
  ("battlegroup_get_position", [
	(store_script_param, ":bgposition", 1),
	(store_script_param, ":bgteam", 2),
	(store_script_param, ":bgdivision", 3),
	
	(assign, ":x", 0),
	(assign, ":y", 0),
	(init_position, ":bgposition"),
	(try_begin),
		(neg|is_between, ":bgdivision", 0, 9),
		(team_slot_ge, ":bgteam", slot_team_size, 1),
		(team_get_slot, ":x", ":bgteam", slot_team_avg_x),
		(team_get_slot, ":y", ":bgteam", slot_team_avg_y),
	(else_try),
		(is_between, ":bgdivision", 0, 9),
		(store_add, ":slot", slot_team_d0_size, ":bgdivision"),
		(team_slot_ge, ":bgteam", ":slot", 1),
		
		(store_add, ":slot", slot_team_d0_avg_x, ":bgdivision"),
		(team_get_slot, ":x", ":bgteam", ":slot"),
		
		(store_add, ":slot", slot_team_d0_avg_y, ":bgdivision"),
		(team_get_slot, ":y", ":bgteam", ":slot"),
	(try_end),
	(position_set_x, ":bgposition", ":x"),
	(position_set_y, ":bgposition", ":y"),
	(position_set_z_to_ground_level, ":bgposition"),
  ]),	
 
  # script_battlegroup_get_attack_destination by motomataru
  # Input: destination position, team, division, target team, target division
  # Output:	melee position against target battlegroup
  ("battlegroup_get_attack_destination", [
	(store_script_param, ":bgposition", 1),
	(store_script_param, ":bgteam", 2),
	(store_script_param, ":bgdivision", 3),
	(store_script_param, ":enemy_team", 4),
	(store_script_param, ":enemy_division", 5),
	
	(store_add, ":slot", slot_team_d0_formation, ":bgdivision"),
	(team_get_slot, ":bgformation", ":bgteam", ":slot"),
	(try_begin),
		(eq, ":bgformation", formation_none),
		(call_script, "script_battlegroup_get_position", ":bgposition", ":bgteam", ":bgdivision"),
	(else_try),
		(call_script, "script_formation_current_position", ":bgposition", ":bgteam", ":bgdivision"),
	(try_end),
	
	(store_add, ":slot", slot_team_d0_formation, ":enemy_division"),
	(team_get_slot, ":enemy_formation", ":enemy_team", ":slot"),
	(try_begin),
		(eq, ":enemy_formation", formation_none),
		(call_script, "script_battlegroup_get_position", Enemy_Team_Pos, ":enemy_team", ":enemy_division"),
	(else_try),
		(call_script, "script_formation_current_position", Enemy_Team_Pos, ":enemy_team", ":enemy_division"),
	(try_end),
	
	(get_distance_between_positions, ":distance_to_move", ":bgposition", Enemy_Team_Pos),
	
	(call_script, "script_battlegroup_get_action_radius", ":bgteam", ":bgdivision"),
	(assign, ":bgradius", reg0),
	(call_script, "script_battlegroup_get_action_radius", ":enemy_team", ":enemy_division"),
	(store_add, ":combined_radius", ":bgradius", reg0),

	(try_begin),
		(neq, ":bgformation", formation_none),	#in formation AND
		(le, ":distance_to_move", ":combined_radius"),	#close to enemy
		(store_mul, reg0, -350, formation_reform_interval),	#back up one move (to avoid wild swings / reversals on overruns)
		(position_move_y, ":bgposition", reg0),
		(get_distance_between_positions, ":distance_to_move", ":bgposition", Enemy_Team_Pos),
	(try_end),

	(try_begin),
		(eq, ":bgformation", formation_none),
		(call_script, "script_battlegroup_get_depth", ":bgteam", ":bgdivision"),
		(val_div, reg0, 2),	#position from script_battlegroup_get_position is in middle of bg
		(val_sub, ":distance_to_move", reg0),
	(try_end),
		
	(store_add, ":slot", slot_team_d0_front_weapon_length, ":bgdivision"),
	(team_get_slot, ":striking_distance", ":bgteam", ":slot"),
	# (val_mul, ":striking_distance", 150),	#experiential tweak
	# (val_div, ":striking_distance", 100),
	
	(try_begin),
		(neq, ":bgformation", formation_none),
		(store_add, ":slot", slot_team_d0_formation_space, ":bgdivision"),
		(team_get_slot, reg0, ":bgteam", ":slot"),
		(val_mul, reg0, 50),
		(val_add, reg0, formation_minimum_spacing),
		(val_sub, ":bgradius", reg0),	#used to punch wedges through enemy
		(val_max, ":bgradius", 0),
	(try_end),

	(try_begin),
		(this_or_next|eq, ":enemy_formation", formation_none),
		(eq, ":enemy_formation", formation_default),
		(call_script, "script_battlegroup_get_depth", ":enemy_team", ":enemy_division"),
		(val_div, reg0, 2),	#position from script_battlegroup_get_position is in middle of bg
		(try_begin),
			(eq, ":bgformation", formation_wedge),
			(val_add, ":distance_to_move", ":bgradius"),	#drive wedge through target formation!
		(else_try),
			(val_sub, ":distance_to_move", reg0),
			(val_sub, ":distance_to_move", ":striking_distance"),
		(try_end),
		
	(else_try),	#enemy in formation
		(store_add, ":slot", slot_team_d0_first_member, ":enemy_division"),
		(team_get_slot, reg0, ":enemy_team", ":slot"),
		(try_begin),
			(eq, reg0, -1),
			(assign, reg1, ":enemy_team"),
			(assign, reg2, ":enemy_division"),
			(assign, reg3, ":enemy_formation"),
			#(display_message, "@script_battlegroup_get_attack_destination: bad first agent team {reg1} division {reg2} formation {reg3}"),
			(assign, ":enemy_formation_speed", 0),
		(else_try),
				(agent_get_speed, Speed_Pos, reg0),
				(init_position, Temp_Pos),
				(get_distance_between_positions, ":enemy_formation_speed", Speed_Pos, Temp_Pos),
				(val_mul, ":enemy_formation_speed", formation_reform_interval),	#calculate distance to next call
		(try_end),
		(position_is_behind_position, ":bgposition", Enemy_Team_Pos),	#attacking from rear?
		(val_add, ":distance_to_move", ":enemy_formation_speed"),	#catch up to anticipated position
		(call_script, "script_battlegroup_get_depth", ":enemy_team", ":enemy_division"),
		(try_begin),
			(eq, ":bgformation", formation_wedge),
			(val_div, reg0, 2),
			(val_sub, ":distance_to_move", reg0),	#drive wedge through target formation!
			(val_add, ":distance_to_move", ":bgradius"),
		(else_try),
			(val_sub, ":distance_to_move", reg0),
			(val_sub, ":distance_to_move", ":striking_distance"),
		(try_end),
		
	(else_try),	#attacking enemy formation from front
		(try_begin),
			(store_add, ":slot", slot_team_d0_in_melee, ":bgdivision"),
			(team_slot_eq, ":bgteam", ":slot", 0),
			(val_sub, ":distance_to_move", ":enemy_formation_speed"),	#avoid overrunning enemy
		(try_end),
		
		(eq, ":bgformation", formation_wedge),
		(call_script, "script_battlegroup_get_depth", ":enemy_team", ":enemy_division"),
		(val_div, reg0, 2),
		(val_add, ":distance_to_move", reg0),	#drive wedge through target formation!
		(val_add, ":distance_to_move", ":bgradius"),
		
	(else_try),	#ranks attacking enemy formation from front
		(val_sub, ":distance_to_move", ":striking_distance"),
	(try_end),

	(call_script, "script_point_y_toward_position", ":bgposition", Enemy_Team_Pos),
	(position_move_y, ":bgposition", ":distance_to_move"),
  ]),	
 
  # script_battlegroup_get_depth by motomataru
  # Input: team, division
  # Output:	reg0 depth of battlegroup in cm
  ("battlegroup_get_depth", [
	(store_script_param, ":bgteam", 1),
	(store_script_param, ":bgdivision", 2),

	(assign, ":depth", 0),
	(store_add, ":slot", slot_team_d0_formation_space, ":bgdivision"),
	(team_get_slot, ":spacing", ":bgteam", ":slot"),
	(store_add, ":slot", slot_team_d0_formation, ":bgdivision"),
	(team_get_slot, ":bgformation", ":bgteam", ":slot"),
	
	(try_begin),
		(eq, ":bgformation", formation_none),
		(try_begin),
			(lt, ":spacing", 0),	#Native multi-ranks?
			(store_mul, ":depth", ":spacing", -1),
			(val_mul, ":depth", 100),
		(try_end),
		
	(else_try),	#three-rank formations
		(this_or_next|eq, ":bgformation", formation_ranks),
		(eq, ":bgformation", formation_shield),
		(store_mul, ":depth", ":spacing", 50),
		(val_add, ":depth", formation_minimum_spacing),
		(val_mul, ":depth", 2),
		
	(else_try),
		(this_or_next|eq, ":bgformation", formation_wedge),
		(eq, ":bgformation", formation_square),
		(store_add, ":slot", slot_team_d0_size, ":bgdivision"),
		(team_get_slot, ":size_enemy_battlegroup", ":bgteam", ":slot"),
		(call_script, "script_get_centering_amount", formation_square, ":size_enemy_battlegroup", ":spacing"),
		(store_mul, ":depth", reg0, 2),
		(try_begin),
			(eq, ":bgformation", formation_wedge),
			(val_mul, ":depth", 1414),
			(val_div, ":depth", 1000),
		(try_end),
	(try_end),

	(assign, reg0, ":depth"),
  ]),	
 
  # script_battlegroup_get_action_radius by motomataru
  # Input: team, division
  # Output:	reg0 radius of battlegroup's "zone of control" (now length of battlegroup in cm)
  ("battlegroup_get_action_radius", [
	(store_script_param, ":bgteam", 1),
	(store_script_param, ":bgdivision", 2),

	(store_add, ":slot", slot_team_d0_size, ":bgdivision"),
	(team_get_slot, ":size_battlegroup", ":bgteam", ":slot"),
	(store_add, ":slot", slot_team_d0_formation, ":bgdivision"),
	(team_get_slot, ":formation", ":bgteam", ":slot"),
	(store_add, ":slot", slot_team_d0_formation_space, ":bgdivision"),
	(team_get_slot, ":spacing", ":bgteam", ":slot"),
	
	# (try_begin),
		# (lt, ":spacing", 0),
		# (assign, reg0, ":bgteam"),
		# (assign, reg1, ":bgdivision"),
		# (assign, reg2, ":formation"),
		# (display_message, "@battlegroup_get_action_radius: negative radius for team {reg0} division {reg1} formation {reg2}"),
	# (try_end),
	
	(try_begin),
		(eq, ":formation", formation_none),
		(try_begin),
			(ge, ":spacing", 0),
			(store_mul, ":troop_space", ":spacing", 75),	#Native minimum spacing not consistent but around this
			(val_add, ":troop_space", 100),
		(else_try),	#handle Native multi-ranks
			(assign, ":troop_space", 150),
			(val_mul, ":spacing", -1),
			(val_add, ":spacing", 1),
			(val_div, ":size_battlegroup", ":spacing"),
		(try_end),
		(store_mul, ":formation_width", ":size_battlegroup", ":troop_space"),
		(store_div, reg0, ":formation_width", 2),
	(else_try),
		(eq, ":formation", formation_wedge),
		(call_script, "script_get_centering_amount", formation_square, ":size_battlegroup", ":spacing"),
		(val_mul, reg0, 4),
		(val_div, reg0, 3),
	(else_try),
		(call_script, "script_get_centering_amount", ":formation", ":size_battlegroup", ":spacing"),
	(try_end),
	
	(val_mul, reg0, 2),
  ]),	
 
  # script_team_get_position_of_enemies by motomataru
  # Input: destination position, team, troop class/division
  # Output: destination position: average position if reg0 > 0
  #			reg0: number of enemies
  # Run script_store_battlegroup_data before calling!
  ("team_get_position_of_enemies", [
	(store_script_param, ":enemy_position", 1),
	(store_script_param, ":team_no", 2),
	(store_script_param, ":troop_type", 3),
	(assign, ":pos_x", 0),
	(assign, ":pos_y", 0),
	(assign, ":total_size", 0),	
	(try_begin),
		(neq, ":troop_type", grc_everyone),
		(assign, ":closest_distance", Far_Away),
		(call_script, "script_battlegroup_get_position", Temp_Pos, ":team_no", grc_everyone),
	(try_end),
	
	(try_for_range, ":other_team", 0, 4),
		(teams_are_enemies, ":other_team", ":team_no"),
		(try_begin),
			(eq, ":troop_type", grc_everyone),
			(team_get_slot, ":team_size", ":other_team", slot_team_size),
			(try_begin),
				(gt, ":team_size", 0),
				(call_script, "script_battlegroup_get_position", ":enemy_position", ":other_team", grc_everyone),
				(position_get_x, reg0, ":enemy_position"),
				(val_mul, reg0, ":team_size"),
				(val_add, ":pos_x", reg0),
				(position_get_y, reg0, ":enemy_position"),
				(val_mul, reg0, ":team_size"),
				(val_add, ":pos_y", reg0),
			(try_end),
		(else_try),	#for multiple divisions, should find the CLOSEST of a given type
			(assign, ":team_size", 0),			
			(try_for_range, ":enemy_battle_group", 0, 9),
				(store_add, ":slot", slot_team_d0_size, ":enemy_battle_group"),
	            (team_get_slot, ":troop_count", ":other_team", ":slot"),
				(gt, ":troop_count", 0),
				(store_add, ":slot", slot_team_d0_type, ":enemy_battle_group"),
				(team_get_slot, ":bg_type", ":other_team", ":slot"),
				(store_sub, ":bg_root_type", ":bg_type", 3), #subtype is three more than main type
				(this_or_next|eq, ":bg_type", ":troop_type"),
				(eq, ":bg_root_type", ":troop_type"),
				(val_add, ":team_size", ":troop_count"),
				(call_script, "script_battlegroup_get_position", ":enemy_position", ":other_team", ":enemy_battle_group"),
				(get_distance_between_positions, reg0, Temp_Pos, ":enemy_position"),
				(lt, reg0, ":closest_distance"),
				(assign, ":closest_distance", reg0),
				(position_get_x, ":pos_x", ":enemy_position"),
				(position_get_y, ":pos_y", ":enemy_position"),
			(try_end),
		(try_end),
		(val_add, ":total_size", ":team_size"),
	(try_end),
	
	(try_begin),
		(eq, ":total_size", 0),
		(init_position, ":enemy_position"),
	(else_try),
	    (eq, ":troop_type", grc_everyone),
		(val_div, ":pos_x", ":total_size"),
		(position_set_x, ":enemy_position", ":pos_x"),
		(val_div, ":pos_y", ":total_size"),
		(position_set_y, ":enemy_position", ":pos_y"),
		(position_set_z_to_ground_level, ":enemy_position"),
	(else_try),
		(position_set_x, ":enemy_position", ":pos_x"),
		(position_set_y, ":enemy_position", ":pos_y"),
		(position_set_z_to_ground_level, ":enemy_position"),
	(try_end),

	(assign, reg0, ":total_size"),
  ]),

# # Autoloot improved by rubik begin
  #("init_item_score", set_item_score()),

  ("get_item_score_with_imod", [
    (store_script_param, ":item", 1),
    (store_script_param, ":imod", 2),

    (item_get_type, ":type", ":item"),
    (try_begin),
      (eq, ":type", itp_type_book),
      (item_get_slot, ":i_score", ":item", slot_item_intelligence_requirement),
    (else_try),
      (eq, ":type", itp_type_horse),
      (item_get_slot, ":horse_speed", ":item", slot_item_horse_speed),
      (item_get_slot, ":horse_armor", ":item", slot_item_horse_armor),
      (item_get_slot, ":horse_charge", ":item", slot_item_horse_charge),

      (try_begin),
        (eq, ":imod", imod_swaybacked),
        (val_add, ":horse_speed", -2),
      (else_try),
        (eq, ":imod", imod_lame),
        (val_add, ":horse_speed", -5),
      (else_try),
        (eq, ":imod", imod_heavy),
        (val_add, ":horse_armor", 3),
        (val_add, ":horse_charge", 4),
      (else_try),
        (eq, ":imod", imod_spirited),
        (val_add, ":horse_speed", 1),
        (val_add, ":horse_armor", 1),
        (val_add, ":horse_charge", 1),
      (else_try),
        (eq, ":imod", imod_champion),
        (val_add, ":horse_speed", 2),
        (val_add, ":horse_armor", 2),
        (val_add, ":horse_charge", 2),
      (try_end),

      (store_mul, ":i_score", ":horse_speed", ":horse_armor"),
      (val_mul, ":i_score", ":horse_charge"),
    (else_try),
      (eq, ":type", itp_type_shield),
      (item_get_slot, ":shield_size", ":item", slot_item_length),
      (item_get_slot, ":shield_armor", ":item", slot_item_body_armor),
      (item_get_slot, ":shield_speed", ":item", slot_item_speed),

      (try_begin),
        (eq, ":imod", imod_cracked),
        (val_add, ":shield_armor", -4),
      (else_try),
        (eq, ":imod", imod_battered),
        (val_add, ":shield_armor", -2),
      (else_try),
        (eq, ":imod", imod_thick),
        (val_add, ":shield_armor", 2),
      (else_try),
        (eq, ":imod", imod_reinforced),
        (val_add, ":shield_armor", 4),
      (try_end),

      (val_add, ":shield_armor", 5),
      (store_mul, ":i_score", ":shield_armor", ":shield_size"),
      (val_mul, ":i_score", ":shield_speed"),
    (else_try),
      (this_or_next|eq, ":type", itp_type_head_armor),
      (this_or_next|eq, ":type", itp_type_body_armor),
      (this_or_next|eq, ":type", itp_type_foot_armor),
      (eq, ":type", itp_type_hand_armor),
      (item_get_slot, ":head_armor", ":item", slot_item_head_armor),
      (item_get_slot, ":body_armor", ":item", slot_item_body_armor),
      (item_get_slot, ":leg_armor", ":item", slot_item_leg_armor),
      (store_add, ":i_score", ":head_armor", ":body_armor"),
      (val_add, ":i_score", ":leg_armor"),

      (assign, ":imod_effect_mul", 0),
      (try_begin),
        (gt, ":head_armor", 0),
        (val_add, ":imod_effect_mul", 1),
      (try_end),
      (try_begin),
        (gt, ":body_armor", 0),
        (val_add, ":imod_effect_mul", 1),
      (try_end),
      (try_begin),
        (gt, ":leg_armor", 0),
        (val_add, ":imod_effect_mul", 1),
      (try_end),

      (try_begin),
        (eq, ":imod", imod_plain),
        (assign, ":imod_effect", 0),
      (else_try),
        (eq, ":imod", imod_cracked),
        (assign, ":imod_effect", -4),
      (else_try),
        (eq, ":imod", imod_rusty),
        (assign, ":imod_effect", -3),
      (else_try),
        (eq, ":imod", imod_battered),
        (assign, ":imod_effect", -2),
      (else_try),
        (eq, ":imod", imod_crude),
        (assign, ":imod_effect", -1),
      (else_try),
        (eq, ":imod", imod_tattered),
        (assign, ":imod_effect", -3),
      (else_try),
        (eq, ":imod", imod_ragged),
        (assign, ":imod_effect", -2),
      (else_try),
        (eq, ":imod", imod_sturdy),
        (assign, ":imod_effect", 1),
      (else_try),
        (eq, ":imod", imod_thick),
        (assign, ":imod_effect", 2),
      (else_try),
        (eq, ":imod", imod_hardened),
        (assign, ":imod_effect", 3),
      (else_try),
        (eq, ":imod", imod_reinforced),
        (assign, ":imod_effect", 4),
      (else_try),
        (eq, ":imod", imod_lordly),
        (assign, ":imod_effect", 6),
      (try_end),

      (val_mul, ":imod_effect", ":imod_effect_mul"),
      (val_add, ":i_score", ":imod_effect"),
    (else_try),
      (this_or_next|eq, ":type", itp_type_one_handed_wpn),
      (this_or_next|eq, ":type", itp_type_two_handed_wpn),
      (this_or_next|eq, ":type", itp_type_bow),
      (this_or_next|eq, ":type", itp_type_crossbow),
      (eq, ":type", itp_type_polearm),
      (item_get_slot, ":item_speed", ":item", slot_item_speed),
      (item_get_slot, ":item_length", ":item", slot_item_length),
      (item_get_slot, ":swing_damage", ":item", slot_item_swing_damage),
      (item_get_slot, ":thrust_damage", ":item", slot_item_thrust_damage),
      (val_mod, ":swing_damage", 256),
      (val_mod, ":thrust_damage", 256),
      (assign, ":item_damage", ":swing_damage"),
      (val_max, ":item_damage", ":thrust_damage"),

      (try_begin),
        (eq, ":imod", imod_cracked),
        (val_add, ":item_damage", -5),
      (else_try),
        (eq, ":imod", imod_rusty),
        (val_add, ":item_damage", -3),
      (else_try),
        (eq, ":imod", imod_bent),
        (val_add, ":item_damage", -3),
        (val_add, ":item_speed", -3),
      (else_try),
        (eq, ":imod", imod_chipped),
        (val_add, ":item_damage", -1),
      (else_try),
        (eq, ":imod", imod_balanced),
        (val_add, ":item_damage", 3),
        (val_add, ":item_speed", 3),
      (else_try),
        (eq, ":imod", imod_tempered),
        (val_add, ":item_damage", 4),
      (else_try),
        (eq, ":imod", imod_masterwork),
        (val_add, ":item_damage", 5),
        (val_add, ":item_speed", 1),
      (else_try),
        (eq, ":imod", imod_heavy),
        (val_add, ":item_damage", 2),
        (val_add, ":item_speed", -2),
      (else_try),
        (eq, ":imod", imod_strong),
        (val_add, ":item_damage", 3),
        (val_add, ":item_speed", -3),
      (try_end),

      (try_begin),
        (this_or_next|eq, ":type", itp_type_bow),
        (eq, ":type", itp_type_crossbow),
        (store_mul, ":i_score", ":item_damage", ":item_speed"),
      (else_try),
        (this_or_next|eq, ":type", itp_type_one_handed_wpn),
        (this_or_next|eq, ":type", itp_type_two_handed_wpn),
        (eq, ":type", itp_type_polearm),
        (store_mul, ":i_score", ":item_damage", ":item_speed"),
        (val_mul, ":i_score", ":item_length"),
      (try_end),
    (else_try),
      (this_or_next|eq, ":type", itp_type_arrows),
      (this_or_next|eq, ":type", itp_type_bolts),
      (eq, ":type", itp_type_thrown),
      (item_get_slot, ":thrust_damage", ":item", slot_item_thrust_damage),
      (val_mod, ":thrust_damage", 256),
      (assign, ":i_score", ":thrust_damage"),
      (val_add, ":i_score", 3), # +3 to make sure damage > 0

      (try_begin),
        (eq, ":imod", imod_plain),
        (val_mul, ":i_score", 2),
      (else_try),
        (eq, ":imod", imod_large_bag),
        (val_mul, ":i_score", 2),
        (val_add, ":i_score", 1),
      (else_try),
        (eq, ":imod", imod_bent),
        (val_sub, ":i_score", 3),
        (val_mul, ":i_score", 2),
      (else_try),
        (eq, ":imod", imod_heavy),
        (val_add, ":i_score", 2),
        (val_mul, ":i_score", 2),
      (else_try),
        (eq, ":imod", imod_balanced),
        (val_add, ":i_score", 3),
        (val_mul, ":i_score", 2),
      (try_end),
    (try_end),

    (assign, reg0, ":i_score"),
  ]),
# # Autoloot improved by rubik end


# # M&B Standard AI with changes for formations #CABA - OK; Need expansion when new AI divisions to work with
  # script_formation_battle_tactic_init_aux
  # Input: team_no, battle_tactic
  # Output: none
  ("formation_battle_tactic_init_aux",
    [
      (store_script_param, ":team_no", 1),
      (store_script_param, ":battle_tactic", 2),
      (team_get_leader, ":ai_leader", ":team_no"),
      (try_begin),
        (eq, ":battle_tactic", btactic_hold),
        (agent_get_position, pos1, ":ai_leader"),
        (call_script, "script_find_high_ground_around_pos1", ":team_no", 30),
        (copy_position, pos1, pos52),
        (call_script, "script_find_high_ground_around_pos1", ":team_no", 30), # call again just in case we are not at peak point.
        (copy_position, pos1, pos52),
        (call_script, "script_find_high_ground_around_pos1", ":team_no", 30), # call again just in case we are not at peak point.
        (team_give_order, ":team_no", grc_everyone, mordr_hold),
        (team_set_order_position, ":team_no", grc_everyone, pos52),
        (team_give_order, ":team_no", grc_archers, mordr_advance),
        (team_give_order, ":team_no", grc_archers, mordr_advance),
      (else_try),
        (eq, ":battle_tactic", btactic_follow_leader),
        (team_get_leader, ":ai_leader", ":team_no"),
        (ge, ":ai_leader", 0),
        (agent_set_speed_limit, ":ai_leader", 8),
        (agent_get_position, pos60, ":ai_leader"),
        (team_give_order, ":team_no", grc_everyone, mordr_hold),
        (team_set_order_position, ":team_no", grc_everyone, pos60),
      (try_end),
# formations additions
	  (call_script, "script_division_reset_places"),
	  (call_script, "script_get_default_formation", ":team_no"),
	  (assign, ":fformation", reg0),
	  
	  (try_begin),
		(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_infantry, ":fformation"),
		(store_add, ":slot", slot_team_d0_formation, grc_infantry),
		(team_set_slot, ":team_no", ":slot", ":fformation"),
		(store_add, ":slot", slot_team_d0_formation_space, grc_infantry),
		(team_set_slot, ":team_no", ":slot", 0),
	  (else_try),
		(call_script, "script_formation_end", ":team_no", grc_infantry),
	  (try_end),
	  (call_script, "script_battlegroup_place_around_leader", ":team_no", grc_infantry),
	  
	  (try_begin),
		(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_archers, formation_default),
		(store_add, ":slot", slot_team_d0_formation, grc_archers),
		(team_set_slot, ":team_no", ":slot", formation_default),
		(store_add, ":slot", slot_team_d0_formation_space, grc_archers),
		(team_set_slot, ":team_no", ":slot", 2),
	  (else_try),
		(call_script, "script_formation_end", ":team_no", grc_archers),
	  (try_end),
	  (call_script, "script_battlegroup_place_around_leader", ":team_no", grc_archers),
	  
	  (try_begin),
		(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_cavalry, formation_wedge),
		(store_add, ":slot", slot_team_d0_formation, grc_cavalry),
		(team_set_slot, ":team_no", ":slot", formation_wedge),
		(store_add, ":slot", slot_team_d0_formation_space, grc_cavalry),
		(team_set_slot, ":team_no", ":slot", 0),
	  (else_try),
		(call_script, "script_formation_end", ":team_no", grc_cavalry),
	  (try_end),
	  (call_script, "script_battlegroup_place_around_leader", ":team_no", grc_cavalry),
	  
	  (team_give_order, ":team_no", grc_archers, mordr_spread_out),
	  (team_give_order, ":team_no", grc_archers, mordr_spread_out),
# end formations additions
  ]),
  
  # script_formation_battle_tactic_apply_aux #CABA - OK; Need expansion when new AI divisions to work with
  # Input: team_no, battle_tactic
  # Output: battle_tactic
  ("formation_battle_tactic_apply_aux",
    [
      (store_script_param, ":team_no", 1),
      (store_script_param, ":battle_tactic", 2),
      (store_mission_timer_a, ":mission_time"),
      (try_begin),
        (eq, ":battle_tactic", btactic_hold),
        (copy_position, pos1, pos52),
        (call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team_no", 1),
        (assign, ":avg_dist", reg0),
        (assign, ":min_dist", reg1),
        (try_begin),
          (this_or_next|lt, ":min_dist", 1000),
          (lt, ":avg_dist", 4000),
          (assign, ":battle_tactic", 0),
		  (call_script, "script_formation_end", ":team_no", grc_infantry),	#formations
		  (call_script, "script_formation_end", ":team_no", grc_archers),	#formations
		  (call_script, "script_formation_end", ":team_no", grc_cavalry),	#formations
          (team_give_order, ":team_no", grc_everyone, mordr_charge),
        (try_end),
      (else_try),
        (eq, ":battle_tactic", btactic_follow_leader),
        (team_get_leader, ":ai_leader", ":team_no"),
        (try_begin),
          (agent_is_alive, ":ai_leader"),
          (agent_set_speed_limit, ":ai_leader", 9),
          (call_script, "script_team_get_average_position_of_enemies", ":team_no"),
          (copy_position, pos60, pos0),
          (ge, ":ai_leader", 0),
          (agent_get_position, pos61, ":ai_leader"),
          (position_transform_position_to_local, pos62, pos61, pos60), #pos62 = vector to enemy w.r.t leader
          (position_normalize_origin, ":distance_to_enemy", pos62),
          (convert_from_fixed_point, ":distance_to_enemy"),
          (assign, reg17, ":distance_to_enemy"),
          (position_get_x, ":dir_x", pos62),
          (position_get_y, ":dir_y", pos62),
          (val_mul, ":dir_x", 23),
          (val_mul, ":dir_y", 23), #move 23 meters
          (position_set_x, pos62, ":dir_x"),
          (position_set_y, pos62, ":dir_y"),
        
          (position_transform_position_to_parent, pos63, pos61, pos62), #pos63 is 23m away from leader in the direction of the enemy.
          (position_set_z_to_ground_level, pos63),
        
          (team_give_order, ":team_no", grc_everyone, mordr_hold),
          (team_set_order_position, ":team_no", grc_everyone, pos63),
#formations code
		  (call_script, "script_point_y_toward_position", pos63, pos60),
		  (agent_get_position, pos49, ":ai_leader"),
		  (agent_set_position, ":ai_leader", pos63),	#fake out script_battlegroup_place_around_leader
		  (call_script, "script_division_reset_places"),
		  (call_script, "script_get_default_formation", ":team_no"),
		  (assign, ":fformation", reg0),
		  
		  (try_begin),
			(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_infantry, ":fformation"),
			(store_add, ":slot", slot_team_d0_formation, grc_infantry),
			(team_set_slot, ":team_no", ":slot", ":fformation"),
			(store_add, ":slot", slot_team_d0_formation_space, grc_infantry),
			(team_set_slot, ":team_no", ":slot", 0),
		  (else_try),
			(call_script, "script_formation_end", ":team_no", grc_infantry),
		  (try_end),
		  (call_script, "script_battlegroup_place_around_leader", ":team_no", grc_infantry),
		  
		  (try_begin),
			(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_archers, formation_default),
			(store_add, ":slot", slot_team_d0_formation, grc_archers),
			(team_set_slot, ":team_no", ":slot", formation_default),
			(store_add, ":slot", slot_team_d0_formation_space, grc_archers),
			(team_set_slot, ":team_no", ":slot", 2),
		  (else_try),
			(call_script, "script_formation_end", ":team_no", grc_archers),
		  (try_end),
		  (call_script, "script_battlegroup_place_around_leader", ":team_no", grc_archers),
		  
		  (try_begin),
			(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_cavalry, formation_wedge),
			(store_add, ":slot", slot_team_d0_formation, grc_cavalry),
			(team_set_slot, ":team_no", ":slot", formation_wedge),
			(store_add, ":slot", slot_team_d0_formation_space, grc_cavalry),
			(team_set_slot, ":team_no", ":slot", 0),
		  (else_try),
			(call_script, "script_formation_end", ":team_no", grc_cavalry),
		  (try_end),
		  (call_script, "script_battlegroup_place_around_leader", ":team_no", grc_cavalry),
	  
		  (agent_set_position, ":ai_leader", pos49),
#end formations code
          (agent_get_position, pos1, ":ai_leader"),
          (try_begin),
            (lt, ":distance_to_enemy", 50),
            (ge, ":mission_time", 30),
            (assign, ":battle_tactic", 0),
			(call_script, "script_formation_end", ":team_no", grc_infantry),	#formations
			(call_script, "script_formation_end", ":team_no", grc_archers),	#formations
			(call_script, "script_formation_end", ":team_no", grc_cavalry),	#formations
            (team_give_order, ":team_no", grc_everyone, mordr_charge),
            (agent_set_speed_limit, ":ai_leader", 60),
          (try_end),
        (else_try),
          (assign, ":battle_tactic", 0),
		  (call_script, "script_formation_end", ":team_no", grc_infantry),	#formations
		  (call_script, "script_formation_end", ":team_no", grc_archers),	#formations
		  (call_script, "script_formation_end", ":team_no", grc_cavalry),	#formations
          (team_give_order, ":team_no", grc_everyone, mordr_charge),
        (try_end),
      (try_end),
      
      (try_begin), # charge everyone after a while
        (neq, ":battle_tactic", 0),
        (ge, ":mission_time", 300),
        (assign, ":battle_tactic", 0),
		(call_script, "script_formation_end", ":team_no", grc_infantry),	#formations
		(call_script, "script_formation_end", ":team_no", grc_archers),	#formations
		(call_script, "script_formation_end", ":team_no", grc_cavalry),	#formations
        (team_give_order, ":team_no", grc_everyone, mordr_charge),
        (team_get_leader, ":ai_leader", ":team_no"),
        (agent_set_speed_limit, ":ai_leader", 60),
      (try_end),
      (assign, reg0, ":battle_tactic"),
  ]),
  
  # Replacement script for battle_tactic_init_aux to switch between using
  # M&B Standard AI with changes for formations and original based on
  # NOTE: original script "battle_tactic_init_aux" should be renamed to "orig_battle_tactic_init_aux"
  # constant formation_native_ai_use_formation ( 0: original, 1: use formation )
  # script_battle_tactic_init_aux
  # Input: team_no, battle_tactic
  # Output: none
  ("battle_tactic_init_aux",
    [
      (store_script_param, ":team_no", 1),
      (store_script_param, ":battle_tactic", 2),
	  (try_begin),
		#(eq, formation_native_ai_use_formation, 1),
		(party_slot_ge, "p_main_party", slot_party_pref_formations, 1),
		(assign, ":continue", 0),
		(get_player_agent_no, ":player_agent"),
        (agent_get_team, ":player_team", ":player_agent"), #before globals are set
        (try_begin),
          (teams_are_enemies, ":team_no", ":player_team"),
          (party_slot_eq, "$g_enemy_party", slot_party_type, spt_kingdom_hero_party),
          (assign, ":continue", 1),
        (else_try),
          (neg|teams_are_enemies, ":team_no", ":player_team"),
          (gt, "$g_ally_party", 0),
          (party_slot_eq, "$g_ally_party", slot_party_type, spt_kingdom_hero_party),
          (assign, ":continue", 1),
        (try_end),
        (this_or_next|eq, ":continue", 1),
		(eq, AI_for_kingdoms_only, 0), #to prevent riffraff from using formations		
		(call_script, "script_formation_battle_tactic_init_aux", ":team_no", ":battle_tactic"),
	  (else_try),
		(call_script, "script_orig_battle_tactic_init_aux", ":team_no", ":battle_tactic"),
	  (try_end),
    ]),

  # Replacement script for battle_tactic_init_aux to switch between using
  # M&B Standard AI with changes for formations and original based on
  # NOTE: original script "battle_tactic_apply_aux" should be renamed to "orig_battle_tactic_apply_aux"
  # constant formation_native_ai_use_formation ( 0: original, 1: use formation )
  # script_battle_tactic_apply_aux
  # Input: team_no, battle_tactic
  # Output: battle_tactic
  ("battle_tactic_apply_aux",
    [
      (store_script_param, ":team_no", 1),
      (store_script_param, ":battle_tactic", 2),
	  (try_begin),
		#(eq, formation_native_ai_use_formation, 1),
		(party_slot_ge, "p_main_party", slot_party_pref_formations, 1),
		(call_script, "script_formation_battle_tactic_apply_aux", ":team_no", ":battle_tactic"),
	  (else_try),
		(call_script, "script_orig_battle_tactic_apply_aux", ":team_no", ":battle_tactic"),
	  (try_end),
  ]),

] # scripts

from module_items import *

def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1127 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "scripts"
		orig_scripts = var_set[var_name_1]
		
		modmerge_formations_scripts(orig_scripts)
		
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)

from util_wrappers import *
from util_scripts import *

scripts_directives = [
	#rename scripts to "insert" switch scripts (see end of scripts[])
	[SD_RENAME, "battle_tactic_init_aux" , "orig_battle_tactic_init_aux"],
	[SD_RENAME, "battle_tactic_apply_aux" , "orig_battle_tactic_apply_aux"],
	#insert formations before last call in team_give_order_from_order_panel
	[SD_OP_BLOCK_INSERT, "team_give_order_from_order_panel", D_SEARCH_FROM_BOTTOM | D_SEARCH_LINENUMBER | D_INSERT_BEFORE, 0, 0, [
		(call_script, "script_player_order_formations", ":order"),	#for formations
	]],
] # scripts_rename

def modmerge_formations_scripts(orig_scripts):
	# process script directives first
	process_script_directives(orig_scripts, scripts_directives)
	# add remaining scripts
	add_scripts(orig_scripts, scripts, True)