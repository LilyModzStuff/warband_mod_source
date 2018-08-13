# Formations for Warband by Motomataru
# rel. 06/08/11
# EDIT FOR ORDER DISPLAY 11/19/10 by Caba'drin
# EDIT TO USE SLOTS 02/23/11 by Caba'drin


from header_common import *
from header_operations import *
from header_mission_templates import *
from module_constants import *

# Formations triggers v3 by motomataru, Warband port
# Global variables	*_formation_type holds type of formation: see "Formation modes" in module_constants
#					*_formation_move_order hold the current move order for the formation
#					*_space hold the multiplier of extra space ordered into formation by the player

formations_triggers = [
	(ti_before_mission_start, 0, 0, [], [
		(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(party_set_slot, 2, slot_party_gk_order_hold_over_there, 0),
		#(assign, "$native_display", 0),
		(assign, "$rethink_on_formation", 0),
		(assign, "$autorotate_at_player", formation_autorotate_at_player),
		
		(try_for_range, ":team", 0, 4),
			(try_for_range, ":division", 0, 9),
				(store_add, ":slot", slot_team_d0_type, ":division"),
				(team_set_slot, ":team", ":slot", sdt_unknown),
				(store_add, ":slot", slot_team_d0_speed_limit, ":division"),
				(team_set_slot, ":team", ":slot", 10),
				(store_add, ":slot", slot_team_d0_target_team, ":division"),
				(team_set_slot, ":team", ":slot", -1),
				(store_add, ":slot", slot_team_d0_fclock, ":division"),
				(team_set_slot, ":team", ":slot", 1),
			(try_end),
		(try_end),
		#ensure item slots are loaded whatever save game this is...
		#(neq, "$new_session", 1),
		# # Autoloot improved by rubik begin
		#(call_script, "script_init_item_score"),
		#(call_script, "script_setup_noswing_item_slots"),
		# # Autoloot improved by rubik end
		#(assign, "$new_session", 1),
	]),

# Start troops in formation
	(0, formation_delay_for_spawn, ti_once, [], [
		(get_player_agent_no, "$fplayer_agent_no"),
		(agent_get_team, "$fplayer_team_no", "$fplayer_agent_no"),
		(call_script, "script_store_battlegroup_data"),
		
		#get team faction
		(store_sub, ":num_kingdoms", kingdoms_end, kingdoms_begin),
		(store_mul, ":end", 4, ":num_kingdoms"),
		(try_for_range, ":slot", 0, ":end"),
			(team_set_slot, scratch_team, ":slot", 0),
		(try_end),		
		(try_for_agents, ":cur_agent"),
			(agent_is_human, ":cur_agent"),
			(agent_get_team, ":cur_team", ":cur_agent"),
			(agent_get_troop_id, ":cur_troop", ":cur_agent"),
			(store_troop_faction, ":cur_faction", ":cur_troop"),
			(is_between, ":cur_faction", kingdoms_begin, kingdoms_end),
			(store_mul, ":slot", ":cur_team", ":num_kingdoms"),
			(val_sub, ":cur_faction", kingdoms_begin),
			(val_add, ":slot", ":cur_faction"),
			(team_get_slot, ":count", scratch_team, ":slot"),
			(val_add, ":count", 1),
			(team_set_slot, scratch_team, ":slot", ":count"),
		(try_end),
		
		(try_for_range, ":team", 0, 4),
			(team_slot_ge, ":team", slot_team_size, 1),
			(team_get_leader, ":fleader", ":team"),
			(try_begin),
				(ge, ":fleader", 0),
				(agent_get_troop_id, ":fleader_troop", ":fleader"),
				(store_troop_faction, ":team_faction", ":fleader_troop"),
			(else_try),
				(assign, ":team_faction", 0),
				(assign, ":modal_count", 0),
				(store_mul, ":begin", ":team", ":num_kingdoms"),
				(store_add, ":end", ":begin", ":num_kingdoms"),
				(try_for_range, ":slot", ":begin", ":end"),
					(team_get_slot, ":count", scratch_team, ":slot"),
					(gt, ":count", ":modal_count"),
					(assign, ":modal_count", ":count"),
					(store_sub, ":team_faction", ":begin", ":slot"),
					(val_add, ":team_faction", kingdoms_begin),
				(try_end),
			(try_end),		
			(team_set_slot, ":team", slot_team_faction, ":team_faction"),
		(try_end),
		
	    #CABA - EDIT FROM HERE ON ONCE EVERYTHING IS COMPLETE. WOULD NEED TO DO MORE DIVISIONS HERE...OR REMOVE DEFAULT FORMATIONS
		## NOTE - new moto formations has forming ranks code here
	]),

	(.1, 0, 0, [
		(neq, "$when_f1_first_detected", 0),
		(store_mission_timer_c_msec, reg0),
		(val_sub, reg0, "$when_f1_first_detected"),
		(ge, reg0, 250),	#check around .3 seconds later (Native trigger delay does not work right)
		(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_1),	#next trigger set MOVE menu?
	 ], [
		(assign, "$when_f1_first_detected", 0),
		
		(try_begin),
			(game_key_is_down, gk_order_1),	#BUT player is holding down key?
			(party_set_slot, 2, slot_party_gk_order_hold_over_there, 2), #holdit/hold_over_there
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, 2, slot_party_gk_order_hold_over_there, 1), #as holdit
			(call_script, "script_player_order_formations", mordr_hold),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
			(party_set_slot, 2, slot_party_gk_order_hold_over_there, 0), #as holdit
		(try_end),
	]),
	
#implement HOLD OVER THERE when player lets go of key/etc
	(.5, 0, 0, [(neg|main_hero_fallen)], [
		(set_fixed_point_multiplier, 100),
		(store_mission_timer_c_msec, "$last_player_trigger"),
		
		(try_begin),	#set up revertible types for type check
			(try_for_range, ":team", 0, 4),
				(try_for_range, ":division", 0, 9),
					(store_add, ":slot", slot_team_d0_type, ":division"),
					(this_or_next|team_slot_eq, ":team", ":slot", sdt_skirmisher),
					(team_slot_eq, ":team", ":slot", sdt_harcher),
					(team_set_slot, ":team", ":slot", sdt_unknown),
				(try_end),
			(try_end),
		(try_end),

		(call_script, "script_store_battlegroup_data"),
		(call_script, "script_team_get_position_of_enemies", Enemy_Team_Pos, "$fplayer_team_no", grc_everyone),
		(assign, ":num_enemies", reg0),
		
		(try_begin),
			(eq, ":num_enemies", 0),	#no more enemies?
			(try_for_range, ":division", 0, 9),
				(call_script, "script_formation_end", "$fplayer_team_no", ":division"),
			(try_end),
		(try_end),
		
		(gt, ":num_enemies", 0),
		(call_script, "script_division_reset_places"),
			
		#implement HOLD OVER THERE when player lets go of key
		(try_begin),
			(party_slot_eq, 2, slot_party_gk_order_hold_over_there, 2),
			(neg|game_key_is_down, gk_order_1),
			
			(assign, ":num_bgroups", 0),
			(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
				(store_add, ":slot", slot_team_d0_target_team, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", -1),
				(store_add, ":slot", slot_team_d0_size, ":division"),
				(team_slot_ge, "$fplayer_team_no", ":slot", 1),
				(store_add, ":slot", slot_team_d0_fclock, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", 1),
				(team_get_order_position, pos1, "$fplayer_team_no", ":division"),
				(val_add, ":num_bgroups", 1),
			(try_end),	
			
			(gt, ":num_bgroups", 0),
			(copy_position, Target_Pos, pos1),	#kludge around team_get_order_position rotation problems
			
			#player designating target battlegroup?
			(assign, ":distance_to_enemy", Far_Away),
			(try_for_range, ":team", 0, 4),
				(teams_are_enemies, ":team", "$fplayer_team_no"),
				(team_slot_ge, ":team", slot_team_size, 1),
				(try_for_range, ":division", 0, 9),
					(store_add, ":slot", slot_team_d0_size, ":division"),
					(team_slot_ge, ":team", ":slot", 1),
					(call_script, "script_battlegroup_get_position", Temp_Pos, ":team", ":division"),
					(get_distance_between_positions, reg0, Target_Pos, Temp_Pos),
					(gt, ":distance_to_enemy", reg0),
					(assign, ":distance_to_enemy", reg0),
					(assign, ":closest_enemy_team", ":team"),
					(assign, ":closest_enemy_division", ":division"),
				(try_end),
			(try_end),
			
			(call_script, "script_battlegroup_get_action_radius", ":closest_enemy_team", ":closest_enemy_division"),
			(assign, ":radius_enemy_battlegroup", reg0),
			
			(try_begin),
				(le, ":distance_to_enemy", ":radius_enemy_battlegroup"),	#target position within radius of an enemy battlegroup?
				(call_script, "script_battlegroup_get_position", Target_Pos, ":closest_enemy_team", ":closest_enemy_division"),
				(gt, ":num_bgroups", 1),
				(store_add, ":slot", slot_team_d0_type, ":closest_enemy_division"),
				(team_get_slot, reg0, ":closest_enemy_team", ":slot"),
				(call_script, "script_str_store_division_type_name", s1, reg0),
				(display_message, "@...and attack enemy {s1} division!"),
			(try_end),
			
			(call_script, "script_point_y_toward_position", Target_Pos, Enemy_Team_Pos),
			
			#place player divisions
			(agent_get_position, pos49, "$fplayer_agent_no"),
			(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
				(store_add, ":slot", slot_team_d0_size, ":division"),
				(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
				(gt, ":troop_count", 0),
				
				(try_begin),
					(le, ":distance_to_enemy", ":radius_enemy_battlegroup"),	#target position within radius of an enemy battlegroup?
					(store_add, ":slot", slot_team_d0_target_team, ":division"),
					(team_set_slot, "$fplayer_team_no", ":slot", ":closest_enemy_team"),
					(store_add, ":slot", slot_team_d0_target_division, ":division"),
					(team_set_slot, "$fplayer_team_no", ":slot", ":closest_enemy_division"),
				(try_end),
				
				(store_add, ":slot", slot_team_d0_formation, ":division"),
				(team_get_slot, ":fformation", "$fplayer_team_no", ":slot"),
				
				(try_begin),
					(gt, ":num_bgroups", 1),
					(agent_set_position, "$fplayer_agent_no", Target_Pos),	#fake out script_battlegroup_place_around_leader
					(call_script, "script_player_attempt_formation", ":division", ":fformation", 1),
				(else_try),
					(try_begin),
						(le, ":distance_to_enemy", ":radius_enemy_battlegroup"),	#target position within radius of an enemy battlegroup?
						(call_script, "script_battlegroup_get_attack_destination", Target_Pos, "$fplayer_team_no", ":division", ":closest_enemy_team", ":closest_enemy_division"),
						(store_add, ":slot", slot_team_d0_type, ":closest_enemy_division"),
						(team_get_slot, reg0, ":closest_enemy_team", ":slot"),
						(call_script, "script_str_store_division_type_name", s1, reg0),
						(display_message, "@...and attack enemy {s1} division!"),
					(try_end),
			
					(neq, ":fformation", formation_none),
					(call_script, "script_set_formation_destination", "$fplayer_team_no", ":division", Target_Pos),
					(store_add, ":slot", slot_team_d0_formation_space, ":division"),
					(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
					(try_begin),
						(store_add, ":slot", slot_team_d0_type, ":division"),
						(team_get_slot, ":sd_type", "$fplayer_team_no", ":slot"),
						(neq, ":sd_type", sdt_cavalry),
						(neq, ":sd_type", sdt_harcher),
						(call_script, "script_get_centering_amount", ":fformation", ":troop_count", ":div_spacing"),
						(try_begin),
							(eq, ":sd_type", sdt_archer),
							(val_mul, reg0, -1),
							(assign, ":script", "script_form_archers"),
						(else_try),
							(assign, ":script", "script_form_infantry"),
						(try_end),
						(position_move_x, Target_Pos, reg0),
					(else_try),
						(assign, ":script", "script_form_cavalry"),
					(try_end),
					(copy_position, pos1, Target_Pos),
					(call_script, ":script", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":fformation"),		
				(try_end),
				(store_add, ":slot", slot_team_d0_move_order, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", mordr_hold),		
			(try_end), #division loop
			(agent_set_position, "$fplayer_agent_no", pos49),
			(party_set_slot, 2, slot_party_gk_order_hold_over_there, 0),
		(try_end),	#HOLD OVER THERE

		#periodic functions
		(try_begin),	#rethink after reform
			(gt, "$rethink_on_formation", 0),
			(try_for_agents, ":agent"),
				(agent_force_rethink, ":agent"),
			(try_end),
			(assign, "$rethink_on_formation", 0),
		(try_end),
		
		(assign, "$autorotate_at_player", 0),
		(try_for_range, ":division", 0, 9),
			(store_add, ":slot", slot_team_d0_size, ":division"),
			(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
			(gt, ":troop_count", 0),
			
			(store_add, ":slot", slot_team_d0_target_team, ":division"),
			(team_get_slot, ":target_team", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_target_division, ":division"),
			(team_get_slot, ":target_division", "$fplayer_team_no", ":slot"),
			(try_begin),
				(ge, ":target_team", 0),	#enemy battlegroup targeted?
				(store_add, ":slot", slot_team_d0_size, ":target_division"),
				(team_get_slot, reg0, ":target_team", ":slot"),
				
				(le, reg0, 0),	#target destroyed?
				(store_add, ":slot", slot_team_d0_target_team, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", -1),
			
				(store_add, ":slot", slot_team_d0_type, ":target_division"),
				(team_get_slot, reg0, ":target_team", ":slot"),
				(call_script, "script_str_store_division_type_name", s1, reg0),
				
				#(store_add, reg0, ":division", 1),
				(str_store_class_name, s2, ":division"),
				(display_message, "@{s2}: returning after destroying enemy {s1} division."),
				(store_add, ":slot", slot_team_d0_move_order, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", mordr_follow),
			(try_end),
				
			(store_add, ":slot", slot_team_d0_fclock, ":division"),
			(team_get_slot, ":fclock", "$fplayer_team_no", ":slot"),
			(store_mod, ":time_slice", ":fclock", Reform_Trigger_Modulus),
			(val_add, ":fclock", 1),
			(team_set_slot, "$fplayer_team_no", ":slot", ":fclock"),

			(try_begin),
				(store_add, ":slot", slot_team_d0_move_order, ":division"),
				(team_slot_eq, "$fplayer_team_no", ":slot", mordr_follow),
				(try_begin),
					(eq, formation_place_around_leader, 1),
					(call_script, "script_battlegroup_place_around_leader", "$fplayer_team_no", ":division"),
				(else_try),
					(call_script, "script_battlegroup_place_at_leader", "$fplayer_team_no", ":division"),
				(try_end),
				(team_set_slot, "$fplayer_team_no", ":slot", mordr_follow),	#override script_battlegroup_place_around_leader

			#periodically reform
			(else_try),
				(eq, ":time_slice", 0),
				(team_get_movement_order, reg0, "$fplayer_team_no", ":division"),
				(neq, reg0, mordr_stand_ground),
				(store_add, ":slot", slot_team_d0_formation, ":division"),
				(team_get_slot, ":fformation", "$fplayer_team_no", ":slot"),
				(try_begin),
					(neq, ":fformation", formation_none),
					(store_add, ":slot", slot_team_d0_formation_space, ":division"),
					(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
					(store_add, ":slot", slot_team_d0_type, ":division"),
					(team_get_slot, ":sd_type", "$fplayer_team_no", ":slot"),
					
					(try_begin),
						(ge, ":target_team", 0),	#enemy battlegroup targeted?
						(try_begin),
							(this_or_next|eq, ":sd_type", sdt_archer),
							(this_or_next|eq, ":sd_type", sdt_harcher),
							(eq, ":sd_type", sdt_skirmisher),
							(store_add, ":slot", slot_team_d0_in_melee, ":division"),
							(team_slot_eq, "$fplayer_team_no", ":slot", 1),	#ranged are firing?
							(call_script, "script_formation_current_position", pos1, "$fplayer_team_no", ":division"),	#stop advancing
						(else_try),
							(call_script, "script_battlegroup_get_attack_destination", pos1, "$fplayer_team_no", ":division", ":target_team", ":target_division"),
						(try_end),
						
					(else_try),
						(call_script, "script_get_formation_destination", pos1, "$fplayer_team_no", ":division"),
						(try_begin),
							(neq, ":sd_type", sdt_cavalry),
							(neq, ":sd_type", sdt_harcher),
							(position_move_y, pos1, -2000),
						(try_end),
						(call_script, "script_point_y_toward_position", pos1, Enemy_Team_Pos),
						(try_begin),
							(neq, ":sd_type", sdt_cavalry),
							(neq, ":sd_type", sdt_harcher),
							(position_move_y, pos1, 2000),
						(try_end),
					(try_end),
					
					(call_script, "script_set_formation_destination", "$fplayer_team_no", ":division", pos1),
					
					(try_begin),	
						(neq, ":sd_type", sdt_cavalry),
						(neq, ":sd_type", sdt_harcher),					
						(call_script, "script_get_centering_amount", ":fformation", ":troop_count", ":div_spacing"),
						(try_begin),
							(eq, ":sd_type", sdt_archer),
							(val_mul, reg0, -1),
						(try_end),
						(position_move_x, pos1, reg0),	
					(try_end),
					
					(try_begin),
						(eq, ":sd_type", sdt_archer),
						(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":fformation"),		
					(else_try),
						(this_or_next|eq, ":sd_type", sdt_cavalry),
						(eq, ":sd_type", sdt_harcher),
						(try_begin),
							(ge, ":target_team", 0),	#enemy battlegroup targeted?
							(call_script, "script_formation_current_position", pos29, "$fplayer_team_no", ":division"),
							(call_script, "script_battlegroup_get_position", Enemy_Team_Pos, ":target_team", ":target_division"),
							(get_distance_between_positions, ":distance_to_enemy", pos29, Enemy_Team_Pos),
							
							(call_script, "script_battlegroup_get_action_radius", "$fplayer_team_no", ":division"),
							(assign, ":combined_radius", reg0),
							(call_script, "script_battlegroup_get_action_radius", ":target_team", ":target_division"),
							(val_add, ":combined_radius", reg0),
							
							(le, ":distance_to_enemy", ":combined_radius"),
							(call_script, "script_formation_end", "$fplayer_team_no", ":division"),
							#(store_add, reg0, ":division", 1),
							(str_store_class_name, s1, ":division"),
							(display_message, "@{s1}: cavalry formation disassembled."),
							(set_show_messages, 0),
							(team_give_order, "$fplayer_team_no", ":division", mordr_charge),
							(set_show_messages, 1),
						(else_try),
							(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
						(try_end),
					(else_try),				
						(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":fformation"),	
					(try_end),
	
					(val_add, "$rethink_on_formation", 1),
					
				(else_try),	#divisions not in formation
					(ge, ":target_team", 0),	#enemy battlegroup targeted?
					(store_add, ":slot", slot_team_d0_target_division, ":division"),
					(team_get_slot, ":target_division", "$fplayer_team_no", ":slot"),
					(try_begin),
						(this_or_next|eq, ":sd_type", sdt_archer),
						(this_or_next|eq, ":sd_type", sdt_harcher),
						(eq, ":sd_type", sdt_skirmisher),
						(store_add, ":slot", slot_team_d0_in_melee, ":division"),
						(team_slot_eq, "$fplayer_team_no", ":slot", 1),	#ranged are firing?
						(call_script, "script_battlegroup_get_position", pos1, "$fplayer_team_no", ":division"),	#stop advancing
					(else_try),
						(call_script, "script_battlegroup_get_attack_destination", pos1, "$fplayer_team_no", ":division", ":target_team", ":target_division"),
					(try_end),
					(call_script, "script_set_formation_destination", "$fplayer_team_no", ":division", pos1),
					(team_get_movement_order, ":existing_order", "$fplayer_team_no", ":division"),
					(try_begin),
						(ge, ":target_team", 0),	#enemy battlegroup targeted?
						(call_script, "script_battlegroup_get_position", pos29, "$fplayer_team_no", ":division"),
						(call_script, "script_battlegroup_get_position", Enemy_Team_Pos, ":target_team", ":target_division"),
						(get_distance_between_positions, ":distance_to_enemy", pos29, Enemy_Team_Pos),
						
						(call_script, "script_battlegroup_get_action_radius", "$fplayer_team_no", ":division"),
						(assign, ":combined_radius", reg0),
						(call_script, "script_battlegroup_get_action_radius", ":target_team", ":target_division"),
						(val_add, ":combined_radius", reg0),
						
						(le, ":distance_to_enemy", ":combined_radius"),
						(try_begin),
							(neq, ":existing_order", mordr_charge),
							(set_show_messages, 0),
							(team_give_order, "$fplayer_team_no", ":division", mordr_charge),
							(set_show_messages, 1),
						(try_end),
					(else_try),
						(neq, ":existing_order", mordr_hold),
						(set_show_messages, 0),
						(team_give_order, "$fplayer_team_no", ":division", mordr_hold),
						(set_show_messages, 1),
					(try_end),
				(try_end),
			(try_end),	#Periodic Reform
		(try_end),	#Division Loop
				
		(assign, "$autorotate_at_player", formation_autorotate_at_player),
	]),

	(ti_on_agent_spawn, 0, 0, [], [(store_trigger_param_1, ":agent"),(call_script, "script_agent_fix_division", ":agent")]),
]
#end formations triggers

def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1127 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "mission_templates"
		orig_mission_templates = var_set[var_name_1]

		# START do your own stuff to do merging

		modmerge_formations_mission_templates(orig_mission_templates)

		# END do your own stuff
            
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)


def modmerge_formations_mission_templates(orig_mission_templates):
	# brute force add formation triggers to all mission templates with mtf_battle_mode
	#for i in range (0,len(orig_mission_templates)):
	#	if( orig_mission_templates[i][1] & mtf_battle_mode ):
	#		orig_mission_templates[i][5].extend(formations_triggers)
	find_i = find_object( orig_mission_templates, "lead_charge" )
	orig_mission_templates[find_i][5].extend(formations_triggers)
	find_i = find_object( orig_mission_templates, "quick_battle_battle" )
	orig_mission_templates[find_i][5].extend(formations_triggers)