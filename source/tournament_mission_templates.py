# Tournament Play Enhancements (1.5) by Windyplains

# WHAT THIS FILE DOES:
# Replaces the "arena_melee_fight" tournament template and designates new triggers for different tournament types.

from header_common import *
from header_operations import *
from module_constants import *
from header_mission_templates import *
from module_mission_templates import *
# from pbod_mission_templates import *

##################
# BEGIN TRIGGERS #
##################
tpe_standard_triggers = [
###################
# NATIVE TRIGGERS # This is all stuff copied from the original arena_melee_fight that were relevant to tournaments.
###################
	# TRIGGER 0
	(ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest"),
										   (assign, "$g_arena_training_num_agents_spawned", 0)]),
										   
	# TRIGGER 1
	(ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),
	
	# TRIGGER 2
	(ti_tab_pressed, 0, 0, [(neg|main_hero_fallen),],
	   [(try_begin),
		  (eq, "$g_mt_mode", abm_visit),
		  (set_trigger_result, 1),
		(else_try),
		  (question_box,"str_give_up_fight"),
		(try_end),
		]),
	
	# TRIGGER 3
	(ti_question_answered, 0, 0, [(neg|main_hero_fallen),],
	   [(store_trigger_param_1,":answer"),
		(eq,":answer",0),
		(try_begin),
		  (eq, "$g_mt_mode", abm_tournament),
		  (call_script, "script_tpe_end_tournament_fight", 0),
		# (else_try),
		  # (eq, "$g_mt_mode", abm_village_fist_fighting),
		  # (call_script, "script_end_village_fist_fight", 0),
		(else_try),
		  (eq, "$g_mt_mode", abm_training),
		  (get_player_agent_no, ":player_agent"),
		  (agent_get_kill_count, "$g_arena_training_kills", ":player_agent", 1),#use this for conversation
		(try_end),
		(finish_mission,0),
		]),
	  
	# TRIGGER 4
	(0, 0, ti_once, [],
	   [
		 (eq, "$g_mt_mode", abm_tournament),
		 (play_sound, "snd_arena_ambiance", sf_looping),
		 (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
		 ]),


################
# TPE TRIGGERS #
################
	
	# TRIGGER 5: Dynamic Weapon AI
	(1, 0, 0, 
		[(eq, "$g_mt_mode", abm_tournament),],
		[
		  # Run through all active NPCs on the tournament battle field.
		  (try_for_agents, ":agent_self"),
			# Isn't a player.
			(agent_is_non_player, ":agent_self"),
			# Isn't a horse.
			(agent_is_human, ":agent_self"),
			# Hasn't been defeated.
			(agent_is_alive, ":agent_self"),
			# exclude tournament masters
			(agent_get_troop_id, ":troop_self", ":agent_self"),
			(neg|is_between, ":troop_self", "trp_town_1_arena_master", "trp_town_1_armorer"),
			# They riding a horse?
			(agent_get_horse, ":horse", ":agent_self"), # 0 - No, 1 - Yes
			
			# Determine closest enemy.
			(assign, ":shortest_distance", 10000),
			(str_store_string, s1, "@No one"),
			(str_store_troop_name, s2, ":troop_self"),
			(agent_get_position, pos1, ":agent_self"),
			(assign, ":distance", 10000),
			(try_for_agents, ":agent_enemy"),
				(agent_get_troop_id, ":troop_enemy", ":agent_enemy"),
				# Not looking at self.
				(neq, ":agent_enemy", ":agent_self"),
				# exclude tournament masters
				(neg|is_between, ":troop_enemy", "trp_town_1_arena_master", "trp_town_1_armorer"),
				# Not an ally
				(agent_get_team, ":team_self", ":agent_self"),
				(agent_get_team, ":team_enemy", ":agent_enemy"),
				(neq, ":team_self", ":team_enemy"),
				# Isn't a horse.
				(agent_is_human, ":agent_enemy"),
				# Hasn't been defeated.
				(agent_is_alive, ":agent_enemy"),
				
				(agent_get_position, pos2, ":agent_enemy"),
				(get_distance_between_positions,":distance",pos1,pos2),
				(try_begin),
					(lt, ":distance", ":shortest_distance"),
					(assign, ":shortest_distance", ":distance"),
					(str_store_troop_name, s1, ":troop_enemy"),
					(assign, reg0, ":shortest_distance"),
					(agent_get_horse, ":enemy_mounted", ":agent_enemy"),
				(try_end),
			(try_end),
			
			# If you enable this save yourself a headache and up the trigger timing.
			(try_begin), (ge, DEBUG_TPE_ai_behavior, 3), (display_message, "@DEBUG (Weapon AI): {s2}'s closest enemy is {s1} at a distance of {reg0}."), (try_end),
			
			# TPE+ 1.4 - New custom tournament design items.
			(store_sub, ":city_settings", "$current_town", towns_begin),
			(val_mul, ":city_settings", 10),
			# Normal weapons
			(store_add, ":slot_lance",    ":city_settings", tdp_val_setting_lance),
			(store_add, ":slot_archery",  ":city_settings", tdp_val_setting_archery),
			(store_add, ":slot_onehand",  ":city_settings", tdp_val_setting_onehand),
			(store_add, ":slot_twohand",  ":city_settings", tdp_val_setting_twohand),
			(store_add, ":slot_crossbow", ":city_settings", tdp_val_setting_crossbow),
			(store_add, ":slot_throwing", ":city_settings", tdp_val_setting_throwing),
			(store_add, ":slot_polearm",  ":city_settings", tdp_val_setting_polearm),
			# (store_add, ":slot_horse",    ":city_settings", tdp_val_setting_horse),
			# (store_add, ":slot_outfit",   ":city_settings", tdp_val_setting_outfit),
			(troop_get_slot, ":item_normal_lance",    tpe_appearance, ":slot_lance"),
			(troop_get_slot, ":item_normal_archery",  tpe_appearance, ":slot_archery"),
			(troop_get_slot, ":item_normal_onehand",  tpe_appearance, ":slot_onehand"),
			(troop_get_slot, ":item_normal_twohand",  tpe_appearance, ":slot_twohand"),
			(troop_get_slot, ":item_normal_crossbow", tpe_appearance, ":slot_crossbow"),
			(troop_get_slot, ":item_normal_throwing", tpe_appearance, ":slot_throwing"),
			(troop_get_slot, ":item_normal_polearm",  tpe_appearance, ":slot_polearm"),
			# (troop_get_slot, ":item_normal_horse",    tpe_appearance, ":slot_horse"),
			# (troop_get_slot, ":item_normal_outfit",   tpe_appearance, ":slot_outfit"),
			# Enhanced weapons
			(store_add, ":slot_enh_lance", ":slot_lance", 100),
			(store_add, ":slot_enh_archery", ":slot_archery", 100),
			(store_add, ":slot_enh_onehand", ":slot_onehand", 100),
			(store_add, ":slot_enh_twohand", ":slot_twohand", 100),
			(store_add, ":slot_enh_crossbow", ":slot_crossbow", 100),
			(store_add, ":slot_enh_throwing", ":slot_throwing", 100),
			(store_add, ":slot_enh_polearm", ":slot_polearm", 100),
			# (store_add, ":slot_enh_horse", ":slot_horse", 100),
			# (store_add, ":slot_enh_outfit", ":slot_outfit", 100),
			(troop_get_slot, ":item_enh_lance",    tpe_appearance, ":slot_enh_lance"),
			(troop_get_slot, ":item_enh_archery",  tpe_appearance, ":slot_enh_archery"),
			(troop_get_slot, ":item_enh_onehand",  tpe_appearance, ":slot_enh_onehand"),
			(troop_get_slot, ":item_enh_twohand",  tpe_appearance, ":slot_enh_twohand"),
			(troop_get_slot, ":item_enh_crossbow", tpe_appearance, ":slot_enh_crossbow"),
			(troop_get_slot, ":item_enh_throwing", tpe_appearance, ":slot_enh_throwing"),
			(troop_get_slot, ":item_enh_polearm",  tpe_appearance, ":slot_enh_polearm"),
			# (troop_get_slot, ":item_enh_horse",    tpe_appearance, ":slot_enh_horse"),
			# (troop_get_slot, ":item_enh_outfit",   tpe_appearance, ":slot_enh_outfit"),
			
			(assign, ":weapon_choice", 0),
			(try_begin),
				(ge, ":horse", 0),
				(this_or_next|agent_has_item_equipped, ":agent_self", ":item_normal_lance"),
				(agent_has_item_equipped, ":agent_self", ":item_enh_lance"),
				(assign, ":weapon_choice", 2), # Bypasses melee/ranged options.
			(else_try),
				(le, ":enemy_mounted", 0),
				(le, ":shortest_distance", wp_tpe_enemy_approaching_foot),
				(assign, ":weapon_choice", 1),
			(else_try),
				(ge, ":enemy_mounted", 1),
				(le, ":shortest_distance", wp_tpe_enemy_approaching_mounted),
				(assign, ":weapon_choice", 1),
			(try_end),
			
			(try_begin),
				(eq, ":weapon_choice", 1),
				(agent_set_wielded_item, ":agent_self", ":item_normal_polearm"),
				(agent_set_wielded_item, ":agent_self", ":item_enh_polearm"),
				(agent_set_wielded_item, ":agent_self", ":item_normal_onehand"),
				(agent_set_wielded_item, ":agent_self", ":item_enh_onehand"),
				(agent_set_wielded_item, ":agent_self", ":item_normal_twohand"),
				(agent_set_wielded_item, ":agent_self", ":item_enh_twohand"),
				(try_begin),
					# AI behavior change to make unmounted spear wielders use their spear two-handed.
					(lt, ":horse", 0),
					# Determine if the agent is using a spear.
					(this_or_next|agent_has_item_equipped, ":agent_self", ":item_normal_polearm"),
					(agent_has_item_equipped, ":agent_self", ":item_enh_polearm"),
					# Unwield shield
					(this_or_next|agent_has_item_equipped,":agent_self",wp_tpe_normal_shield),
					(agent_has_item_equipped,":agent_self",wp_tpe_enhanced_shield),
					(agent_unequip_item, ":agent_self", wp_tpe_normal_shield),
					(agent_unequip_item, ":agent_self", wp_tpe_enhanced_shield),
					(ge, DEBUG_TPE_ai_behavior, 1),
					(display_message, "@DEBUG (TPE): {s2} is wielding a spear on foot and discards shield."),
				(try_end),
			(else_try),
				(eq, ":weapon_choice", 0),
				(agent_set_wielded_item, ":agent_self", ":item_normal_archery"),
				(agent_set_wielded_item, ":agent_self", ":item_enh_archery"),
				(agent_set_wielded_item, ":agent_self", ":item_normal_crossbow"),
				(agent_set_wielded_item, ":agent_self", ":item_enh_crossbow"),
				(agent_set_wielded_item, ":agent_self", ":item_normal_throwing"),
				(agent_set_wielded_item, ":agent_self", ":item_enh_throwing"),
			(else_try),
				(eq, ":weapon_choice", 2),
				(agent_set_wielded_item, ":agent_self", ":item_normal_lance"),
				(agent_set_wielded_item, ":agent_self", ":item_enh_lance"),
			(try_end),
		  (try_end),
	   ]),

	# TRIGGER 6: Runs through all active agents on the battlefield and forces them to wear shoes.
	(0, 0, ti_once, 
		[(eq, "$g_mt_mode", abm_tournament),
		(eq, wp_tpe_mod_opt_actual_gear, 0),],
		[
			# Run through all active NPCs on the tournament battle field.
			(try_for_agents, ":agent_self"),
				(agent_equip_item, ":agent_self", wp_tpe_normal_boots),
				(agent_equip_item, ":agent_self", wp_tpe_enhanced_boots),
			(try_end),
		]),
	
	# TRIGGER 7: This trigger sets up the mission end conditions.
	(1, 4, ti_once, 
		[(eq, "$g_mt_mode", abm_tournament),
		(num_active_teams_le, 1),
		],
		[
			# Determine highest scoring team.
			(assign, ":best_team", 0),
			(troop_get_slot, ":highest_score", "trp_tpe_presobj", tpe_icd_team_0_points),
			(try_begin),
				(troop_slot_ge, "trp_tpe_presobj", tpe_icd_team_1_points, ":highest_score"),
				(troop_get_slot, ":highest_score", "trp_tpe_presobj", tpe_icd_team_1_points),
				(assign, ":best_team", 1),
			(try_end),
			(try_begin),
				(troop_slot_ge, "trp_tpe_presobj", tpe_icd_team_2_points, ":highest_score"),
				(troop_get_slot, ":highest_score", "trp_tpe_presobj", tpe_icd_team_2_points),
				(assign, ":best_team", 2),
			(try_end),
			(try_begin),
				(troop_slot_ge, "trp_tpe_presobj", tpe_icd_team_3_points, ":highest_score"),
				(troop_get_slot, ":highest_score", "trp_tpe_presobj", tpe_icd_team_3_points),
				(assign, ":best_team", 3),
			(try_end),
			
			(try_for_agents, ":agent_no"),
				(agent_is_human, ":agent_no"), # Remove horses.
				(agent_get_team, ":agent_team", ":agent_no"),
				(agent_get_troop_id, ":troop_id", ":agent_no"),
				(try_begin),
					(eq, ":agent_team", ":best_team"),
					(call_script, "script_tpe_award_point_to_troop", ":troop_id", 1, tpe_point_best_scoring_team, wp_green), # Members of highest scoring team get 1 point.
				(try_end),
				(agent_is_alive, ":agent_no"),
				(neg|is_between, ":troop_id", arena_masters_begin, arena_masters_end),#omit tournament master
				
				(try_begin), # AWARD: Cautious Approach (survive a round without scoring a point)
					(troop_slot_eq, ":troop_id", slot_troop_tournament_round_points, 0),
					(ge, "$g_tournament_num_participants_for_fight", tpe_careful_min_participants),
					(troop_set_slot, tpe_award_data, tpe_cautious_approach, ":troop_id"),
					(str_store_troop_name, s1, ":troop_id"),
					(troop_slot_eq, TPE_OPTIONS, tpe_val_opt_awards, 1), # Player option to enable/disable award displays.
					(display_message, "@AWARD GRANTED: {s1} has earned the CAUTIOUS APPROACH award!"),
				(try_end),
				
				### Determine if match merits survivor points ###
				(try_begin),
					(ge, "$g_tournament_num_participants_for_fight", tpe_survival_min_participants),
					(call_script, "script_tpe_award_point_to_troop", ":troop_id", 2, tpe_point_won_the_round, wp_green), # All surviving members gain 2 points.
				(try_end),
			(try_end),
			(get_player_agent_no, ":agent_player"),
			(agent_get_team, ":player_team", ":agent_player"),

			# Come up with some progress for the people who didn't get to be in this match.
			(call_script, "script_tpe_score_non_participants"),
			
			# Tally up difficulty payouts
			(troop_get_slot, ":bid_bonus", TPE_OPTIONS, tpe_val_bet_bid),
			(val_mul, ":bid_bonus", 2),
			(call_script, "script_tpe_get_difficulty_value"),
			#(troop_get_slot, ":difficulty", TPE_OPTIONS, tpe_val_diff_setting),
			(troop_get_slot, ":cumulative_diff", "trp_tpe_presobj", tpe_val_cumulative_diff),
			(val_add, ":cumulative_diff", reg1),
			(val_add, ":cumulative_diff", ":bid_bonus"),
			(troop_set_slot, "trp_tpe_presobj", tpe_val_cumulative_diff, ":cumulative_diff"),
			
			(try_begin),
				(store_remaining_team_no, ":winning_team"),
				(eq, ":winning_team", ":player_team"),
				
				# Calculate wager payout.
				(try_begin),
					(troop_get_slot, ":bid", TPE_OPTIONS, tpe_val_bet_bid),
					(troop_get_slot, ":wager", TPE_OPTIONS, tpe_val_bet_wager),
					# Prevent payment if you didn't bid or wager anything.
					(ge, ":bid", 1),
					(ge, ":wager", 1),
					(troop_slot_ge, "trp_player", slot_troop_tournament_round_points, ":bid"),
					# You won, so you get your roundly bet payout.
					(call_script, "script_tpe_calculate_wager_for_bid"),
					(display_message, "@You have earned {reg4} denars for your clever bet this round.", wp_green),
					
					(set_show_messages, 0),
					(troop_add_gold, "trp_player", reg4),
					(set_show_messages, 1),
				(try_end),
				
				# End the match.
				(call_script, "script_play_victorious_sound"),
				(call_script, "script_tpe_end_tournament_fight", 1),
				
				(finish_mission),
			(else_try),
				(call_script, "script_tpe_end_tournament_fight", 0),
				(finish_mission),
			(try_end),
		]),

	# # TRIGGER 8: AI Remount Behavior
	# (10, 0, 0, 
		# [(eq, "$g_mt_mode", abm_tournament),
		# (troop_get_slot, ":difficulty", TPE_OPTIONS, tpe_val_diff_setting),
		# (ge, ":difficulty", 9), # Medium Difficulty
		# (ge, wp_tpe_released_version, 200),
		# ],
		# [
			# (set_show_messages, 0),
			# (try_for_range, ":team_no"),
				# (team_give_order, ":team_no", grc_everyone, mordr_mount),
			# (try_end),
			# (set_show_messages, 1),
			
			# # (try_for_agents, ":agent_no"),
				# # (agent_is_alive, ":agent_no"),
				# # (agent_is_human, ":agent_no"),
				# # (agent_get_horse, ":has_horse", ":agent_no"),
				# # (le, ":has_horse", 0),
				# # (agent_get_team, ":team_no", ":agent_no"),
				# # (agent_get_division , ":division_no", ":agent_no"),
				# # (team_give_order, ":team_no", ":division_no", mordr_mount),
				# # (try_begin),
					# # (ge, DEBUG_TPE_general, 1),
					# # (agent_get_troop_id, ":troop_no", ":agent_no"),
					# # (str_store_troop_name, s1, ":troop_no"),
					# # (assign, reg1, ":team_no"),
					# # (assign, reg2, ":division_no"),
					# # (display_message, "@DEBUG (TPE): {s1} of team {reg1} division {reg2} is ordered to find a mount."),
				# # (try_end),
			# # (try_end),
		# ]),
	
	# # TRIGGER 9: AI Focus Fire Behavior
	# (1, 0, 0, 
		# [(eq, "$g_mt_mode", abm_tournament),
		# (troop_get_slot, ":difficulty", TPE_OPTIONS, tpe_val_diff_setting),
		# (ge, ":difficulty", 17), # Hard Difficulty
		# (ge, wp_tpe_released_version, 200),
		# ],
		# [
			# (try_for_agents, ":agent_no"),
				# (agent_is_alive, ":agent_no"),
				# (agent_is_human, ":agent_no"),
				# (agent_get_team, ":team_no", ":agent_no"),
				# (team_get_leader, ":agent_leader", ":team_no"),
				# (neq, ":agent_no", ":agent_leader"),
				# #(agent_set_look_target_agent, <agent_id>, <agent_id>),
				
				# (agent_get_division , ":division_no", ":agent_no"),
				# (team_give_order, ":team_no", ":division_no", mordr_mount),
				# (try_begin),
					# (ge, DEBUG_TPE_general, 1),
					# (agent_get_troop_id, ":troop_no", ":agent_no"),
					# (str_store_troop_name, s1, ":troop_no"),
					# (assign, reg1, ":team_no"),
					# (assign, reg2, ":division_no"),
					# (display_message, "@DEBUG (TPE): {s1} of team {reg1} division {reg2} is ordered to find a mount."),
				# (try_end),
			# (try_end),
		# ]),

	# TRIGGER 10: Counts time spent in the current match.
	(1, 0, 0, 
		[(eq, "$g_mt_mode", abm_tournament),
		#(ge, wp_tpe_released_version, 200),
		],
		[
			# Count time in the tournament match.
			(val_add, "$g_wp_tpe_timer", 1),
			
			# Updates the match timer display if activated.
			(eq, "$g_wp_tpe_icd_activated", 1),
			(ge, "$g_wp_tpe_timer", 2),
			(store_div, ":minutes", "$g_wp_tpe_timer", 60),
			(store_mod, ":seconds", "$g_wp_tpe_timer", 60),
			(troop_get_slot, ":obj_timer", "trp_tpe_presobj", tpe_obj_match_timer),
			(assign, reg31, ":minutes"),
			(str_clear, s31),
			(try_begin),
				(lt, ":seconds", 10),
				(str_store_string, s31, "@0"),
			(try_end),
			(assign, reg32, ":seconds"),
			(str_store_string, s32, "@{s31}{reg32}"),
			(try_begin),
				(troop_slot_eq, "trp_tpe_presobj", tpe_trigger_enable_icd, 0),
				(is_presentation_active, "prsnt_tpe_team_display"),
				(overlay_set_text, ":obj_timer", "@Match Time - {reg31}:{s32}"),
			(else_try),
				# Attempts to reboot the ICD if it was disabled.
				(neg|is_presentation_active, "prsnt_tpe_team_display"),
				(eq, "$g_wp_tpe_option_icd_active", 1),
				(try_begin),
					(troop_slot_eq, "trp_tpe_presobj", tpe_trigger_enable_icd, 1),
					(troop_set_slot, "trp_tpe_presobj", tpe_trigger_enable_icd, 0),
				(try_end),
				(start_presentation, "prsnt_tpe_team_display"),
			(try_end),
			
			# Updates the stalemate timer display if activated.
			(troop_slot_eq, "trp_tpe_presobj", tpe_icd_stalemate_active, 1),
			(troop_get_slot, ":time_of_death", "trp_tpe_presobj", tpe_time_of_death),
			(store_sub, ":time_since_death", "$g_wp_tpe_timer", ":time_of_death"),
			(store_sub, ":seconds", wp_tpe_stalemate_timer_limit, ":time_since_death"),
			(troop_get_slot, ":obj_timer", "trp_tpe_presobj", tpe_icd_stalemate_timer),
			(str_clear, s31),
			(try_begin),
				(lt, ":seconds", 10),
				(str_store_string, s31, "@0"),
			(try_end),
			(assign, reg32, ":seconds"),
			(str_store_string, s32, "@{s31}{reg32}"),
			(try_begin),
				(troop_slot_eq, "trp_tpe_presobj", tpe_trigger_enable_icd, 0),
				(is_presentation_active, "prsnt_tpe_team_display"),
				(overlay_set_text, ":obj_timer", "@Stalemate Timer - 0:{s32}"),
			(try_end),
		]),
		
	# TRIGGER 11: Catches the death of a contestant and awards points to victor team/agent, updates displays of points & members.
	(ti_on_agent_killed_or_wounded, 0, 0, 
		[(eq, "$g_mt_mode", abm_tournament),],
		[
			(store_trigger_param_1, ":agent_victim"),
			(store_trigger_param_2, ":agent_killer"),
			
			# Reset the stalemate forced ending timer if active.
			(try_begin),
				(troop_slot_ge, "trp_tpe_presobj", tpe_time_of_death, 0),
				(troop_set_slot, "trp_tpe_presobj", tpe_time_of_death, "$g_wp_tpe_timer"),
				(troop_set_slot, "trp_tpe_presobj", tpe_icd_stalemate_active, 0),
				(try_begin),
					(eq, "$g_wp_tpe_icd_activated", 1),
					(troop_slot_eq, "trp_tpe_presobj", tpe_trigger_enable_icd, 0),
					(is_presentation_active, "prsnt_tpe_team_display"),
					(troop_get_slot, ":obj_timer", "trp_tpe_presobj", tpe_icd_stalemate_timer),
					(str_clear, s31),
					(overlay_set_text, ":obj_timer", "@{s31}"),
				(try_end),
				(ge, DEBUG_TPE_general, 1),
				(assign, reg1, "$g_wp_tpe_timer"),
				(display_message, "@DEBUG (TPE): Stalemate timer reset.  Attack registered at time {reg1} seconds."),
			(try_end),
			
			# Is this a valid kill worth gaining points?
			(agent_is_human, ":agent_victim"),
			(agent_get_team, ":team_victim", ":agent_victim"),
			(agent_get_team, ":team_killer", ":agent_killer"),
			(neq, ":team_killer", ":team_victim"),  # Prevent points gained from friendly kills.
			
			# Award points to killing agent & team.
			(agent_get_troop_id, ":troop_killer", ":agent_killer"),
			(call_script, "script_tpe_award_point_to_troop", ":troop_killer", 1, tpe_point_eliminated_opponent, wp_green),
			(call_script, "script_tpe_update_kill_count", ":troop_killer", 1),
			
			(ge, wp_tpe_released_version, 136),
			
			# Announce awarding of points.
			(try_begin),
				(troop_slot_eq, TPE_OPTIONS, tpe_val_opt_teampoints, 1),
				(get_player_agent_no, ":agent_player"),
				(agent_get_team, ":team_player", ":agent_player"),
				(try_begin),
					(eq, ":team_killer", 0),
					(str_store_string, s1, "@red"),
				(else_try),
					(eq, ":team_killer", 1),
					(str_store_string, s1, "@blue"),
				(else_try),
					(eq, ":team_killer", 2),
					(str_store_string, s1, "@green"),
				(else_try),
					(eq, ":team_killer", 3),
					(str_store_string, s1, "@yellow"),
				(try_end),
				
				(try_begin),
					(eq, ":team_killer", ":team_player"),
					(display_message, "@The Tournament Master announces, 'Point awarded to {s1} team for disabling an opponent.'", wp_green),
				(else_try),
					(display_message, "@The Tournament Master announces, 'Point awarded to {s1} team for disabling an opponent.'", wp_red),
				(try_end),
			(try_end),
			
			# Update in combat display (ICD).
			(try_begin),
				(eq, "$g_wp_tpe_option_icd_active", 1),
				(troop_slot_eq, "trp_tpe_presobj", tpe_trigger_enable_icd, 0),
				(is_presentation_active, "prsnt_tpe_team_display"),
				(call_script, "script_tpe_update_team_points", ":team_killer"),
				(try_begin),
					(eq, ":team_victim", 0),
					(val_sub, "$g_wp_tpe_team_0_members", 1),
					(store_mul, ":lifebar_length", "$g_wp_tpe_team_0_members", tpe_lifebar_pip_size),
					(val_max, ":lifebar_length", 1),
					# Create outer bar
					(troop_get_slot, ":obj_lifebar_outer", "trp_tpe_presobj", tpe_obj_team_0_outerbar),
					(store_add, ":lifebar_outer", ":lifebar_length", 4),
					(store_mul, ":size_y", tpe_lifebar_outer_width, 50),
					(store_mul, ":size_x", ":lifebar_outer", 50),
					(position_set_y, pos1, ":size_y"),
					(position_set_x, pos1, ":size_x"),
					(overlay_set_size, ":obj_lifebar_outer", pos1),
					# Create inner bar
					(troop_get_slot, ":obj_lifebar", "trp_tpe_presobj", tpe_obj_team_0_lifebar),
					(store_mul, ":size_y", tpe_lifebar_pip_width, 50),
					(store_mul, ":size_x", ":lifebar_length", 50),
					(position_set_y, pos1, ":size_y"),
					(position_set_x, pos1, ":size_x"),
					(overlay_set_size, ":obj_lifebar", pos1),
					
				(else_try),
					(eq, ":team_victim", 1),
					(val_sub, "$g_wp_tpe_team_1_members", 1),
					(store_mul, ":lifebar_length", "$g_wp_tpe_team_1_members", tpe_lifebar_pip_size),
					(val_max, ":lifebar_length", 1),
					# Create outer bar
					(troop_get_slot, ":obj_lifebar_outer", "trp_tpe_presobj", tpe_obj_team_1_outerbar),
					(store_add, ":lifebar_outer", ":lifebar_length", 4),
					(store_mul, ":size_y", tpe_lifebar_outer_width, 50),
					(store_mul, ":size_x", ":lifebar_outer", 50),
					(position_set_y, pos1, ":size_y"),
					(position_set_x, pos1, ":size_x"),
					(overlay_set_size, ":obj_lifebar_outer", pos1),
					# Create inner bar
					(troop_get_slot, ":obj_lifebar", "trp_tpe_presobj", tpe_obj_team_1_lifebar),
					(store_mul, ":size_y", tpe_lifebar_pip_width, 50),
					(store_mul, ":size_x", ":lifebar_length", 50),
					(position_set_y, pos1, ":size_y"),
					(position_set_x, pos1, ":size_x"),
					(overlay_set_size, ":obj_lifebar", pos1),
					
				(else_try),
					(eq, ":team_victim", 2),
					(val_sub, "$g_wp_tpe_team_2_members", 1),
					(store_mul, ":lifebar_length", "$g_wp_tpe_team_2_members", tpe_lifebar_pip_size),
					(val_max, ":lifebar_length", 1),
					# Create outer bar
					(troop_get_slot, ":obj_lifebar_outer", "trp_tpe_presobj", tpe_obj_team_2_outerbar),
					(store_add, ":lifebar_outer", ":lifebar_length", 4),
					(store_mul, ":size_y", tpe_lifebar_outer_width, 50),
					(store_mul, ":size_x", ":lifebar_outer", 50),
					(position_set_y, pos1, ":size_y"),
					(position_set_x, pos1, ":size_x"),
					(overlay_set_size, ":obj_lifebar_outer", pos1),
					# Create inner bar
					(troop_get_slot, ":obj_lifebar", "trp_tpe_presobj", tpe_obj_team_2_lifebar),
					(store_mul, ":size_y", tpe_lifebar_pip_width, 50),
					(store_mul, ":size_x", ":lifebar_length", 50),
					(position_set_y, pos1, ":size_y"),
					(position_set_x, pos1, ":size_x"),
					(overlay_set_size, ":obj_lifebar", pos1),
					
				(else_try),
					(eq, ":team_victim", 3),
					(val_sub, "$g_wp_tpe_team_3_members", 1),
					(store_mul, ":lifebar_length", "$g_wp_tpe_team_3_members", tpe_lifebar_pip_size),
					(val_max, ":lifebar_length", 1),
					# Create outer bar
					(troop_get_slot, ":obj_lifebar_outer", "trp_tpe_presobj", tpe_obj_team_3_outerbar),
					(store_add, ":lifebar_outer", ":lifebar_length", 4),
					(store_mul, ":size_y", tpe_lifebar_outer_width, 50),
					(store_mul, ":size_x", ":lifebar_outer", 50),
					(position_set_y, pos1, ":size_y"),
					(position_set_x, pos1, ":size_x"),
					(overlay_set_size, ":obj_lifebar_outer", pos1),
					# Create inner bar
					(troop_get_slot, ":obj_lifebar", "trp_tpe_presobj", tpe_obj_team_3_lifebar),
					(store_mul, ":size_y", tpe_lifebar_pip_width, 50),
					(store_mul, ":size_x", ":lifebar_length", 50),
					(position_set_y, pos1, ":size_y"),
					(position_set_x, pos1, ":size_x"),
					(overlay_set_size, ":obj_lifebar", pos1),
					
				(try_end),

				(call_script, "script_tpe_icd_ranking"),
			(else_try),
				# Attempts to reboot the ICD if it was disabled.
				(eq, "$g_wp_tpe_option_icd_active", 1),
				(troop_slot_eq, "trp_tpe_presobj", tpe_trigger_enable_icd, 1),
				(troop_set_slot, "trp_tpe_presobj", tpe_trigger_enable_icd, 0),
				(start_presentation, "prsnt_tpe_team_display"),
			(try_end),
		]),

	# TRIGGER 12: Allows you to see the damage dealt by your teammates.
	(ti_on_agent_hit, 0, 0, [
		(eq, "$g_mt_mode", abm_tournament),
		(eq, "$g_wp_tpe_option_team_damage", 1),
		], 
		[
			# Trigger Param 1: damage inflicted agent_id
			# Trigger Param 2: damage dealer agent_id
			# Trigger Param 3: inflicted damage
			(store_trigger_param_1, ":agent_victim"),
			(store_trigger_param_2, ":agent_attacker"),
			(store_trigger_param_3, ":damage"),
			
			# Figure out player's team.
			(get_player_agent_no, ":agent_player"),
			(agent_get_team, ":team_player", ":agent_player"),
			(neq, ":agent_player", ":agent_attacker"), # Remove player mirroring messages.
			
			# Determine if attacker was from same team as player.
			(agent_get_team, ":team_attacker", ":agent_attacker"),
			(eq, ":team_attacker", ":team_player"),
			
			# Qualify the victim.
			(agent_is_human, ":agent_victim"), # I don't care about horse damage.
			
			# Display information.
			(agent_get_troop_id, ":troop_attacker", ":agent_attacker"),
			(agent_get_troop_id, ":troop_victim", ":agent_victim"),
			(str_store_troop_name, s1, ":troop_attacker"),
			(str_store_troop_name, s2, ":troop_victim"),
			(assign, reg1, ":damage"),
			(display_message, "@Your ally, {s1}, delivers {reg1} damage to {s2}.", wp_green),
		]),
		
	# TRIGGER 13: Initialization trigger that happens EACH ROUND.
	(ti_after_mission_start, 0, ti_once, 
		[(eq, "$g_mt_mode", abm_tournament),
		(assign, "$g_wp_tpe_icd_activated", 0),],
		[
			(assign, "$g_wp_tpe_icd_activated", 0),
			
			# Assign an initial following team for the death camera.
			# (try_begin),
				# (eq, MOD_PBOD_INSTALLED, 1), # (dependency) PBOD - Custom camera
				# (get_player_agent_no, ":agent_player"),
				# (agent_get_team, ":team_player", ":agent_player"),
				# (assign, "$fplayer_team_no", ":team_player"),
				# (assign, "$fplayer_agent_no", ":agent_player"),
			# (try_end),
			
			# Reset team point tallies.
			(troop_set_slot, "trp_tpe_presobj", tpe_icd_team_0_points, 0),
			(troop_set_slot, "trp_tpe_presobj", tpe_icd_team_1_points, 0),
			(troop_set_slot, "trp_tpe_presobj", tpe_icd_team_2_points, 0),
			(troop_set_slot, "trp_tpe_presobj", tpe_icd_team_3_points, 0),
			
			# Reset points for all participants.
			(try_for_range, ":slot_no", 0, wp_tpe_max_tournament_participants),
				(troop_get_slot, ":troop_no", tpe_tournament_roster, ":slot_no"),
				(troop_set_slot, ":troop_no", slot_troop_tournament_round_points, 0),
				(troop_set_slot, ":troop_no", slot_troop_tournament_participating, 0),
			(try_end),
			(troop_set_slot, "trp_player", slot_troop_tournament_round_points, 0), # For some reason player isn't getting caught above.
			
			# Reset award data for the round.
			(call_script, "script_tpe_initialize_award_data_per_round"),
			(troop_set_slot, tpe_award_data, tpe_kill_count, 0),
			(troop_set_slot, tpe_award_data, tpe_award_display_passes, 0),
			
			# Set everyone who actually made it into the round as participating.
			(try_for_agents, ":agent_no"),
				(agent_get_troop_id, ":troop_no", ":agent_no"),
				(troop_set_slot, ":troop_no", slot_troop_tournament_participating, 1),
			(try_end),
			
			# Reset the stalemate timer to 0.
			(troop_set_slot, "trp_tpe_presobj", tpe_time_of_death, 0),
			
			# Create in-combat display.
			(try_begin),
				(eq, "$g_wp_tpe_option_icd_active", 1),
				(start_presentation, "prsnt_tpe_team_display"),
			(try_end),
		]),

	# TRIGGER 14: Initialization trigger that happens ONCE PER TOURNAMENT.
	(ti_before_mission_start, 0, ti_once, 
		[(eq, "$g_mt_mode", abm_tournament),
		(eq, "$g_tournament_cur_tier", 1),],
		[
			# Reset points for all participants.
			(try_for_range, ":slot_no", 0, wp_tpe_max_tournament_participants),
				(troop_get_slot, ":troop_no", "trp_tournament_participants", ":slot_no"),
				(troop_set_slot, ":troop_no", slot_troop_tournament_round_points, 0),
				(troop_set_slot, ":troop_no", slot_troop_tournament_total_points, 0),
			(try_end),
		]),
		   	   
	# TRIGGER 15: Trash Talking
	(ti_on_agent_hit, 0, 0, 
		[(eq, "$g_mt_mode", abm_tournament),
		(ge, wp_tpe_released_version, 200),], 
		[
			# Trigger Param 1: damage inflicted agent_id
			# Trigger Param 2: damage dealer agent_id
			(store_trigger_param_1, ":agent_victim"),
			(store_trigger_param_2, ":agent_attacker"),
			(agent_get_team, ":team_victim", ":agent_victim"),
			(agent_get_team, ":team_attacker", ":agent_attacker"),
			
			(str_clear, s3),
			(assign, ":quality_check", 0),
			(try_begin),
				(neg|agent_is_human, ":agent_victim"),
				(assign, ":agent_talker", ":agent_attacker"),
				(assign, ":agent_listener", -1),
				(str_store_string, s2, "@taunts"),
				(str_store_string, s3, "@You shall be walking home after I finish with that nag of yours!"),
				(str_clear, s4),
				(assign, ":quality_check", 1),
			(else_try),
				(eq, ":team_victim", ":team_attacker"),
				(assign, ":agent_talker", ":agent_victim"),
				(assign, ":agent_listener", ":agent_attacker"),
				(str_store_string, s2, "@bellows"),
				(str_store_string, s3, "@Just who's side are you on?"),
				(str_store_string, s4, "@ at "),
				(assign, ":quality_check", 1),
			(try_end),
			
			
			(ge, ":quality_check", 1),
			
			# Display information.
			(agent_get_troop_id, ":troop_talker", ":agent_talker"),
			(str_store_troop_name, s1, ":troop_talker"),
			(try_begin),
				(str_clear, s5),
				(ge, ":agent_listener", 0),
				(agent_get_troop_id, ":troop_listener", ":agent_listener"),
				(str_store_troop_name, s5, ":troop_listener"),
			(try_end),
			(display_message, "@{s1} {s2}, '{s3}'{s4}{s5}."),
		]),
		
	# TRIGGER 16: This trigger sets up the mission end conditions for village brawls.
	(1, 4, ti_once, 
		[
			(eq, "$g_mt_mode", abm_village_fist_fighting),
			(num_active_teams_le, 1),
			(ge, wp_tpe_released_version, 200),
		],
	    [
			(try_begin),
				(neg|main_hero_fallen),
				# You WIN
			(else_try),
				# You LOSE
			(try_end),
			
			(finish_mission),
		]),
	
	# TRIGGER 17: Equip "native gear" scaled troops in appropriate colors.
	(ti_after_mission_start, 0, ti_once, 
		[(eq, "$g_mt_mode", abm_tournament),
		(eq, wp_tpe_mod_opt_actual_gear, 1),],
		[
			(try_for_agents, ":agent_no"),
				(agent_is_human, ":agent_no"),
				(agent_get_troop_id, ":troop_no", ":agent_no"),
				(is_between, ":troop_no", tpe_scaled_troops_begin, tpe_scaled_troops_end), # Is it a scaled troop.
				(agent_get_team, ":agent_team", ":agent_no"),
				(store_add, ":armor_body", wp_tpe_enhanced_armor, ":agent_team"),
				(store_add, ":armor_helm", wp_tpe_enhanced_helmet, ":agent_team"),
				(agent_equip_item, ":agent_no", ":armor_body"),
				(agent_equip_item, ":agent_no", ":armor_helm"),
				(agent_equip_item, ":agent_no", wp_tpe_enhanced_boots),
			(try_end),
		]),
		
	# TRIGGER 18: Player dies, round continues.  Warning of this feature to the player.
	(0, 0, ti_once, [(main_hero_fallen),],
	   [(display_message, "@You have fallen during this round, but will be able to continue onto the next round when only one team remains."),
	    (troop_set_slot, "trp_tpe_presobj", tpe_time_of_death, "$g_wp_tpe_timer"),
	    # (try_begin),
			# (eq, MOD_PBOD_INSTALLED, 1), # (dependency) PBOD - Custom camera
			# (display_message, "@You may move your camera around using the arrow keys."),
			# # Sets up camera for free movement.
			# (call_script, "script_cust_cam_init_death_cam", cam_mode_free),
		# (try_end),
		]),
	
	# TRIGGER 19: Player dies triggering a countdown timer to prevent infinite matches due to AI stupidity or game glitch.
	(1, 0, 0, [(main_hero_fallen),],
	    [
			(troop_get_slot, ":time_of_death", "trp_tpe_presobj", tpe_time_of_death),
			(store_sub, ":time_since_death", "$g_wp_tpe_timer", ":time_of_death"),
			(store_sub, ":countdown_limit", wp_tpe_stalemate_timer_limit, 10),
			(ge, ":time_since_death", ":countdown_limit"),
			(store_sub, reg1, wp_tpe_stalemate_timer_limit, ":time_since_death"),
			(troop_set_slot, "trp_tpe_presobj", tpe_icd_stalemate_active, 1),
			#(display_message, "@Stalemate defected.  Match will be closed in {reg1} seconds."),
			(ge, ":time_since_death", wp_tpe_stalemate_timer_limit),
			(call_script, "script_tpe_end_tournament_fight", 0),
			(finish_mission),
		]),
	
	# TRIGGER 20: This trigger tries to capture an attempt to change screens to prevent log spam on the ICD presentation.
	(0, 0, 0, 
		[
			(eq, "$g_wp_tpe_option_icd_active", 1),
			# (this_or_next|key_clicked, key_l),
			# (this_or_next|key_clicked, key_q),
			# (this_or_next|key_clicked, key_c),
			# (key_clicked, key_escape),
			(this_or_next|game_key_clicked, gk_game_log_window),
			(this_or_next|game_key_clicked, gk_quests_window),
			(this_or_next|game_key_clicked, gk_character_window),
			(this_or_next|game_key_clicked, gk_leave),
			(game_key_clicked, key_escape),
			(neg|key_clicked, key_s), # Beats me why 's' is triggering this at all.
		],
	    [
			#(display_message, "@DEBUG: A GAMEKEY WAS CLICKED THAT CAUSED ICD TO DISABLE!!!!"),
			(troop_set_slot, "trp_tpe_presobj", tpe_trigger_enable_icd, 1),
		]),
		
	# TRIGGER 21: Attempts to fix the riderless horse immunity bug.
	(20, 0, 0, 
		[
			(eq, "$g_mt_mode", abm_tournament),
		], 
		[
			(try_for_agents, ":agent_no"),
				
				# Qualify the victim.
				(neg|agent_is_human, ":agent_no"),                    # I only want horses.
				(agent_get_rider, ":agent_rider", ":agent_no"),
				(agent_is_alive, ":agent_no"),                        # No point in beating a dead horse :)
				(eq, ":agent_rider", -1),                             # Returned if there is no rider for the horse.
				(agent_get_item_id, ":item_horse", ":agent_no"),
				(remove_agent, ":agent_no"),
				(ge, DEBUG_TPE_general, 2),                           # Diagnostic information if debug turned on.
				(str_store_item_name, s32, ":item_horse"),
				(assign, reg31, ":agent_no"),
				(display_message, "@DEBUG (TPE): Horse '{s32}' #{reg31} is riderless and will be removed."),
			(try_end),
		]),
		
	# TRIGGER 22: ICD Reboot & HP Update : (dependency) Custom Commander
	(0, 0, 0, 
		[(eq, "$g_mt_mode", abm_tournament),], 
		[
			(try_begin),
				(is_presentation_active, "prsnt_tpe_team_display"),
				(eq, "$g_wp_tpe_option_icd_active", 1),
				(troop_slot_eq, "trp_tpe_presobj", tpe_trigger_enable_icd, 0),
				(eq, MOD_CUSTOM_COMMANDER_INSTALLED, 1), # Dependency (Custom Commander)
				# (troop_slot_eq, TPE_OPTIONS, tpe_val_show_health, 1), # Default display option.
				# (call_script, "script_update_agent_hp_bar"),
			(try_end),
		]),
		
	# TRIGGER 23: Reduces damage dealt to "champion" scaled heroes and Lords to subtly improve their performance.
	(ti_on_agent_hit, 0, 0, 
		[(eq, "$g_mt_mode", abm_tournament),], 
		[
			# Trigger Param 1: damage inflicted agent_id
			# Trigger Param 2: damage dealer agent_id
			# Trigger Param 3: inflicted damage
			(store_trigger_param_1, ":agent_victim"),
			#(store_trigger_param_2, ":agent_attacker"),
			(store_trigger_param_3, ":initial_damage"),
			
			# Qualify the victim.
			(agent_is_human, ":agent_victim"), # I don't care about horse damage.
			(agent_get_troop_id, ":troop_victim", ":agent_victim"),
			(this_or_next|is_between, ":troop_victim", tpe_scaled_champions_begin, tpe_scaled_champions_end),
			(is_between, ":troop_victim", active_npcs_begin, active_npcs_end),
			
			# Determine damage absorption.
			(troop_get_slot, ":difficulty", TPE_OPTIONS, tpe_val_diff_setting),
			(store_sub, ":limiter", 24, ":difficulty"),
			(store_sub, ":percent_absorbed", wp_tpe_champion_damage_absorb_factor, ":limiter"),
			(store_sub, ":percent_taken", 100, ":percent_absorbed"),
			(store_mul, ":reduced_damage", ":initial_damage", ":percent_taken"),
			(val_div, ":reduced_damage", 100),
			
			# Display information.
			(try_begin),
				(ge, DEBUG_TPE_ai_behavior, 1),
				(str_store_troop_name, s2, ":troop_victim"),
				(assign, reg1, ":initial_damage"),
				(assign, reg2, ":reduced_damage"),
				(display_message, "@DEBUG (TPE AI): {s2} receives {reg2} damage reduced from {reg1}.", wp_green),
			(try_end),
			
			# Return new damage result.
			(set_trigger_result, ":reduced_damage"),
		]),
		
	# TRIGGER 24: Shield Bash (dependency) PBOD
	# shield_bash,
	
################
# END TRIGGERS #
################
]
	
	
tpe_tournament_triggers = [
(
    "tpe_tournament_standard",mtf_arena_fight,-1,
    "You enter a melee fight in the arena.",
    [
	  (0,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[]),
	  (1,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[]),
	  (2,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[]),
	  (3,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[]),
	  (4,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[]),
	  (5,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[]),
	  (6,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[]),
	  (7,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[]),

	  (8,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[]),
	  (9,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[]),
	  (10,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[]),
	  (11,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[]),
	  (12,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[]),
	  (13,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[]),
	  (14,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[]),
	  (15,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[]),

	  (16,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[]),
	  (17,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[]),
	  (18,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[]),
	  (19,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[]),
	  (20,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[]),
	  (21,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[]),
	  (22,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[]),
	  (23,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[]),

	  (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[]),
	  (25,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[]),
	  (26,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[]),
	  (27,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[]),
	  (28,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[]),
	  (29,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[]),
	  (30,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[]),
	  (31,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[]),
#32
      # (32, mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_practice_sword_heavy]),
      # (33,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_practice_staff]),
      # (34,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword, itm_practice_shield]),
      # (35,mtef_visitor_source|mtef_team_4,af_override_all,aif_start_alarmed,1,[itm_practice_staff]),
      # (36, mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows, itm_practice_dagger]),
      # (37,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_practice_sword, itm_practice_shield]),
      # (38,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword_heavy]),
      # (39,mtef_visitor_source|mtef_team_4,af_override_all,aif_start_alarmed,1,[itm_practice_staff]),
# #40-49 not used yet
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_horse,itm_arena_tunic_yellow, itm_tourney_helm_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword_heavy,itm_arena_tunic_yellow, itm_tourney_helm_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword_heavy,itm_practice_horse,itm_arena_tunic_yellow, itm_tourney_helm_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_lance,itm_practice_shield,itm_practice_horse,itm_arena_tunic_yellow, itm_tourney_helm_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_dagger, itm_arena_tunic_yellow, itm_tourney_helm_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword,itm_practice_shield,itm_arena_tunic_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword_heavy,itm_practice_horse,itm_arena_tunic_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_lance,itm_practice_shield,itm_practice_horse,itm_arena_tunic_yellow, itm_tourney_helm_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_horse,itm_arena_tunic_yellow, itm_tourney_helm_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_horse,itm_arena_tunic_yellow, itm_tourney_helm_yellow]),

      # (50, mtef_scene_source,af_override_horse|af_override_weapons|af_override_head,0,1,[]),
      # (51, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[]),
      # (52, mtef_scene_source,af_override_horse,0,1,[]),
# #not used yet:
      (53, mtef_scene_source,af_override_horse,0,1,[]),(54, mtef_scene_source,af_override_horse,0,1,[]),(55, mtef_scene_source,af_override_horse,0,1,[]),
# #used for torunament master scene

      # (56, mtef_visitor_source|mtef_team_0, af_override_all, aif_start_alarmed, 1, [itm_practice_sword, itm_practice_shield, itm_ar_rho_t3_aketon_a, itm_he_swa_t3_helmet_a]),
      # (57, mtef_visitor_source|mtef_team_0, af_override_all, aif_start_alarmed, 1, [itm_practice_sword, itm_practice_shield, itm_ar_rho_t3_aketon_a, itm_he_swa_t3_helmet_a]),
	],
    tpe_standard_triggers # + custom_camera_triggers # (dependency) PBOD
  ),
  
(
    "tpe_tournament_native_gear",mtf_arena_fight,-1,
    "You enter a melee fight in the arena.",
    [
	  (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
	  (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
	  (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
	  (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
	  (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
	  (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
	  (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
	  (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

	  (8,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
	  (9,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
	  (10,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
	  (11,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
	  (12,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
	  (13,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
	  (14,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
	  (15,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

	  (16,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
	  (17,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
	  (18,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
	  (19,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
	  (20,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
	  (21,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
	  (22,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
	  (23,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),

	  (24,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
	  (25,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
	  (26,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
	  (27,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
	  (28,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
	  (29,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
	  (30,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
	  (31,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
#32
      # (32, mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_practice_sword_heavy]),
      # (33,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_practice_staff]),
      # (34,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword, itm_practice_shield]),
      # (35,mtef_visitor_source|mtef_team_4,af_override_all,aif_start_alarmed,1,[itm_practice_staff]),
      # (36, mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows, itm_practice_dagger]),
      # (37,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_practice_sword, itm_practice_shield]),
      # (38,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword_heavy]),
      # (39,mtef_visitor_source|mtef_team_4,af_override_all,aif_start_alarmed,1,[itm_practice_staff]),
# #40-49 not used yet
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_horse,itm_arena_tunic_yellow, itm_tourney_helm_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword_heavy,itm_arena_tunic_yellow, itm_tourney_helm_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword_heavy,itm_practice_horse,itm_arena_tunic_yellow, itm_tourney_helm_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_lance,itm_practice_shield,itm_practice_horse,itm_arena_tunic_yellow, itm_tourney_helm_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_dagger, itm_arena_tunic_yellow, itm_tourney_helm_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword,itm_practice_shield,itm_arena_tunic_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword_heavy,itm_practice_horse,itm_arena_tunic_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_lance,itm_practice_shield,itm_practice_horse,itm_arena_tunic_yellow, itm_tourney_helm_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_horse,itm_arena_tunic_yellow, itm_tourney_helm_yellow]),
      # (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_horse,itm_arena_tunic_yellow, itm_tourney_helm_yellow]),

      # (50, mtef_scene_source,af_override_horse|af_override_weapons|af_override_head,0,1,[]),
      # (51, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[]),
      # (52, mtef_scene_source,af_override_horse,0,1,[]),
# #not used yet:
      (53, mtef_scene_source,af_override_horse,0,1,[]),(54, mtef_scene_source,af_override_horse,0,1,[]),(55, mtef_scene_source,af_override_horse,0,1,[]),
#used for torunament master scene

      # (56, mtef_visitor_source|mtef_team_0, af_override_all, aif_start_alarmed, 1, [itm_practice_sword, itm_practice_shield, itm_ar_rho_t3_aketon_a, itm_he_swa_t3_helmet_a]),
      # (57, mtef_visitor_source|mtef_team_0, af_override_all, aif_start_alarmed, 1, [itm_practice_sword, itm_practice_shield, itm_ar_rho_t3_aketon_a, itm_he_swa_t3_helmet_a]),
	],
    tpe_standard_triggers # + custom_camera_triggers # (dependency) PBOD
  ),

]
		
# def modmerge_mission_templates(orig_mission_templates):
	# find_i = find_object( orig_mission_templates, "arena_melee_fight" )
	# orig_mission_templates[find_i][5].extend(AI_triggers)

def modmerge_mission_templates(orig_mission_templates, check_duplicates = False):
    if( not check_duplicates ):
        orig_mission_templates.extend(tpe_tournament_triggers) # Use this only if there are no replacements (i.e. no duplicated item names)
    else:
    # Use the following loop to replace existing entries with same id
        for i in range (0,len(tpe_tournament_triggers)-1):
          find_index = find_object(orig_mission_templates, tpe_tournament_triggers[i][0]); # find_object is from header_common.py
          if( find_index == -1 ):
            orig_mission_templates.append(tpe_tournament_triggers[i])
          else:
            orig_mission_templates[find_index] = tpe_tournament_triggers[i]
			
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "mission_templates"
        orig_mission_templates = var_set[var_name_1]
        modmerge_mission_templates(orig_mission_templates)

    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)