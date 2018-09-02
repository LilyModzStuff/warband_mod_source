# Tournament Play Enhancements (1.5) by Windyplains

# WHAT THIS FILE DOES:
# Creates alternate "town_tournament" menu.
# Creates alternate "town_tournament_won" menu.

# INSTALLATION INSTRUCTIONS:


from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *

####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#  
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################

game_menus = [
 (
    "tpe_town_tournament",mnf_disable_all_keys,
    "Tournament of {s25}^^^STATUS:^You are on the {s23} round of the tournament.{s21}^^SETTINGS:^{reg21} teams with {reg22} {reg23?fighters:fighter} each.{s20}^^CURRENT WAGER:^{s26}",
    "none",
    [
		(set_background_mesh, "mesh_tournament_menu"),
		###### TOURNAMENT INITIALIZE #####
		(str_clear, s20),
		(str_clear, s21),
		(str_store_party_name, s25, "$current_town"),
		# (store_current_hours, ":cur_hours"),
		# (call_script, "script_game_get_date_text", 1, ":cur_hours"),
		# (str_store_date, s24, s1),
	
		(try_begin),
			(eq, "$g_tournament_cur_tier", 0),
			# QUEST INSERT #1: qst_floris_active_tournament
		    (call_script, "script_quest_floris_active_tournament_hook_1"),
			(call_script, "script_tpe_copy_array", tpe_tournament_roster, "trp_tournament_participants", wp_tpe_max_tournament_participants),
			(troop_set_slot, "trp_tpe_presobj", tpe_val_cumulative_diff, 0),
			(call_script, "script_tpe_setup_loot_table"), # Initialize loot table.
			# Changes +
			(troop_get_slot, ":value", TPE_OPTIONS, tpe_val_diff_setting),
			(call_script, "script_tpe_difficulty_slider_effects", ":value"),
			# Changes -
		(else_try),
			# figure out player's ranking
			#(store_add, reg21, wp_tpe_max_tournament_participants, 1),
			(assign, reg21, 1),
			(troop_get_slot, ":player_points", "trp_player", slot_troop_tournament_total_points),
			(try_for_range, ":rank", 0, wp_tpe_max_tournament_participants),
				(troop_get_slot, ":troop_no", tpe_tournament_roster, ":rank"),
				(troop_slot_ge, ":troop_no", slot_troop_tournament_total_points, ":player_points"),
				(neg|troop_slot_eq, ":troop_no", slot_troop_tournament_total_points, ":player_points"),
				(val_add, reg21, 1),
			(try_end),
			(lt, reg21, wp_tpe_max_tournament_participants),
			(assign, reg22, wp_tpe_max_tournament_participants),
			(str_store_string, s21, "@^You are currently rank {reg21} of {reg22} participants."),
			(try_begin),
				(le, reg21, 3),
				(store_add, ":string_no", "str_tpe_rank_1", reg21),
				(val_sub, ":string_no", 1),
				(str_store_string, s27, ":string_no"),
			(else_try),
				(is_between, reg21, 4, 11),
				(str_store_string, s27, "str_tpe_rank_4"),
			(else_try),
				(str_store_string, s27, "str_tpe_rank_5"),
			(try_end),
			(str_store_string, s29, "@^'{s27}'"),
			(str_store_string, s21, "@{s21}{s29}"),
		(try_end),
		
		# (call_script, "script_tpe_sort_troops_and_points_without_player", slot_troop_tournament_total_points),
		
		###### PRESET INFORMATION #####
		(party_set_slot, "$current_town", slot_town_has_tournament, 0), #No way to return back if this menu is left
		(troop_set_slot, TPE_OPTIONS, tpe_val_window_mode, 0), # Should setup a default redirection towards round ranking if tpe_jump_to_rankings called.
        (try_begin),
			### END OF TOURNAMENT CONDITIONS ###
			(ge, "$g_tournament_cur_tier", wp_tpe_max_tournament_tiers),
			(troop_set_slot, TPE_OPTIONS, tpe_val_window_mode, 2), # Final presentation of top 3 ranked players.
			(jump_to_menu, "mnu_tpe_jump_to_rankings"),
		(else_try),
          (try_begin),
            (le, "$g_tournament_next_num_teams", 0),
            (call_script, "script_get_random_tournament_team_amount_and_size"),
            (assign, "$g_tournament_next_num_teams", reg0),
            (assign, "$g_tournament_next_team_size", reg1),
          (try_end),
          (assign, reg21, "$g_tournament_next_num_teams"),
          (assign, reg22, "$g_tournament_next_team_size"),
          (store_sub, reg23, reg22, 1),
          #(store_add, reg0, "$g_tournament_cur_tier", 1),
        (try_end),
		##### PRESET INFORMATION #####
		
		# Round Information
		(store_add, ":round_string", "str_tpe_round_1", "$g_tournament_cur_tier"),
		(str_store_string, s23, ":round_string"),
		
		###### DETERMINE PLAYER'S TEAM ######
		(try_begin),
			# Figure out what team the player will be on.
			(troop_get_slot, ":player_team", "trp_player", slot_troop_tournament_team_request),
			(try_begin),
				(eq, ":player_team", 4), # Random option
				(store_random_in_range, ":player_team", 0, "$g_tournament_next_num_teams"),
			(try_end),
			(store_sub, ":max_teams", "$g_tournament_next_num_teams", 1),
			(val_min, ":player_team", ":max_teams"), # To prevent player from picking a team not available.
			(troop_set_slot, TPE_OPTIONS, tpe_random_team_request, ":player_team"),
		(try_end),
		
		# (try_begin),
			# (troop_get_slot, ":difficulty", TPE_OPTIONS, tpe_val_diff_setting),
			# (store_div, ":odds", ":difficulty", 6),
			# (store_sub, ":min_limit", "$g_tournament_next_num_teams", 1),
			# (val_add, ":odds", ":min_limit"),
			# (val_min, ":odds", wp_tpe_maximum_odds),
			# (assign, reg21, ":odds"),
			# (troop_set_slot, "trp_tpe_presobj", tpe_val_bet_odds_num, ":odds"),
			# (troop_set_slot, "trp_tpe_presobj", tpe_val_bet_odds_den, 1),
			# (str_store_string, s20, "@Odds are {reg21} : 1 against you."),
		# (try_end),
		
		# Update difficulty score.
		(call_script, "script_tpe_get_difficulty_value"),
		(str_store_string, s20, "@^{reg1}% Difficulty"),	
		
		# Update betting information.
		(troop_get_slot, ":bid", TPE_OPTIONS, tpe_val_bet_bid),
		(troop_get_slot, ":wager", TPE_OPTIONS, tpe_val_bet_wager),
		(str_clear, s36),
		(try_begin),
			(ge, ":bid", 1),
			(ge, ":wager", 1),
			(assign, reg31, ":bid"),
			(try_begin),
				(ge, ":bid", 2),
				(str_store_string, s28, "@points"),
			(else_try),
				(str_store_string, s28, "@point"),
			(try_end),
			(assign, reg32, ":wager"),
			(try_begin),
				(ge, ":wager", 2),
				(str_store_string, s27, "@denars"),
			(else_try),
				(str_store_string, s27, "@denar"),
			(try_end),
			(str_store_string, s26, "@{reg32} {s27} that you will earn {reg31} {s28} this round."),
		(else_try),
			(str_store_string, s26, "@You have not placed a bet for this round."),
		(try_end),
    ],
    [
      ("tpe_credits", [], "Instructions & Credits",	
		[
			(change_screen_return),
			(troop_set_slot, tci_objects, tci_val_information_mode, 0),
			(start_presentation, "prsnt_tpe_credits"),
		]),
		
	  ("tournament_options_panel", [(eq, "$g_wp_tpe_active", 1),], "Change tournament options",
       [
	    (change_screen_return),
		(assign, "$g_wp_tpe_troop", "trp_player"),
		(troop_set_slot, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
	    (start_presentation, "prsnt_tournament_options_panel"),
        ]),
	  
	  ("tournament_design_panel", [(eq, "$g_wp_tpe_active", 1),], "Edit tournament design",
       [
	    (change_screen_return),
		(assign, "$tournament_town", "$current_town"),
		(start_presentation, "prsnt_tpe_design_settings"),
        ]),

      ("tournament_bet", [(neq, "$g_wp_tpe_active", 1),], "Place a bet on yourself",
       [(jump_to_menu, "mnu_tournament_bet"),
        ]), # TPE+ 1.3 - Betting menu removed if TPE is active.
		
      ("tournament_join_next_fight", [], "Fight in the next round",
       [
		    (call_script, "script_tpe_set_bet"), # TPE+ 1.3 Change
			
			###### CONTINUE NEXT FIGHT - BEGIN #####
			(str_clear, s35), # Point Tracking
			
			(try_begin),
				(party_slot_eq, "$current_town", slot_town_arena_option, 1),
				# Player wants the native scene used.
				(party_get_slot, ":arena_scene", "$current_town", slot_town_arena_alternate),
			(else_try),
				# Default: Adorno's Overhaul Scene
				(party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
			(try_end),
			(modify_visitors_at_site, ":arena_scene"),
			(reset_visitors),
			#Assuming that there are enough participants for the teams
			(assign, "$g_player_tournament_placement", "$g_tournament_cur_tier"),
			(try_begin),
				(gt, "$g_player_tournament_placement", 4),
				(assign, "$g_player_eligible_feast_center_no", "$current_town"),
			(try_end),
			(val_add, "$g_tournament_cur_tier", 1),
			
			
			(store_mul, "$g_tournament_num_participants_for_fight", "$g_tournament_next_num_teams", "$g_tournament_next_team_size"),
			#(troop_set_slot, "trp_tournament_participants", 0, -1),#Removing trp_player from the list
			(troop_set_slot, "trp_temp_array_a", 0, "trp_player"),
			(call_script, "script_tpe_sort_troops_and_points_without_player", slot_troop_tournament_total_points),
			(try_for_range, ":slot", 0, wp_tpe_max_tournament_participants),
				(troop_get_slot, ":troop_info", tpe_ranking_array, ":slot"),
				(str_store_troop_name, s1, ":troop_info"),
				(assign, reg1, ":slot"),
				(ge, DEBUG_TPE_general, 2),
				(display_message, "@DEBUG (TPE): tpe_ranking_array, slot #{reg1} = {s1}"),
			(try_end),
		
			# Clean out points from the last round.
			(try_for_range, ":slot_no", 1, wp_tpe_max_tournament_participants),
				(troop_get_slot, ":troop_no", tpe_tournament_roster, ":slot_no"),
				(troop_set_slot, ":troop_no", slot_troop_tournament_round_points, 0),
				(troop_set_slot, ":troop_no", slot_troop_tournament_participating, 0),
			(try_end),
			
			# Figure out who is going to be in this round.
			(try_for_range, ":slot_no", 1, "$g_tournament_num_participants_for_fight"),
				(try_begin),
					(eq, "$g_tournament_cur_tier", 0),
					#(lt, wp_tpe_released_version, 200),
					#(call_script, "script_get_random_tournament_participant"),
					#(troop_set_slot, "trp_temp_array_a", ":slot_no", reg0),
					(troop_get_slot, ":troop_no", tpe_tournament_roster, ":slot_no"),
					(troop_set_slot, "trp_temp_array_a", ":slot_no", ":troop_no"),
					
					(ge, DEBUG_TPE_general, 2),
					(str_store_troop_name, s1, ":troop_no"),
					(assign, reg1, ":slot_no"),
					(display_message, "@DEBUG (TPE): {s1} placed in slot #{reg1} for tournament.  TPE 1.3"),
				(else_try),
					(troop_get_slot, ":troop_info", tpe_ranking_array, ":slot_no"),
					(troop_set_slot, "trp_temp_array_a", ":slot_no", ":troop_info"),
					(eq, DEBUG_TPE_general, 2),
					(str_store_troop_name, s1, ":troop_info"),
					(assign, reg1, ":slot_no"),
					(display_message, "@DEBUG (TPE): {s1} placed in slot #{reg1} for tournament.  TPE 2.0"),
				(try_end),
			(try_end),
			#(troop_set_slot, "trp_tournament_participants", 0, "trp_player"),
			
			###### FILTER CHECK FOR MULTIPLE PLAYER BUG ######
			(assign, ":player_found", 0),
			(try_for_range, ":slot_no", 0, wp_tpe_max_tournament_participants),
				(troop_get_slot, ":troop_no", "trp_temp_array_a", ":slot_no"),
				(try_begin),
					# Troop is the player.
					(eq, ":troop_no", "trp_player"),
					(eq, ":player_found", 0),
					# Troop is the first valid player.
					(assign, ":player_found", 1),
				(else_try),
					# Troop slot filled by lord, companion or scaled troop.
					(this_or_next|is_between, ":troop_no", active_npcs_begin, active_npcs_end),
					(is_between, ":troop_no", tpe_scaled_troops_begin, tpe_scaled_troops_end),
				(else_try),
					# No valid troop found.
					(call_script, "script_tpe_pick_random_participant"),
					(troop_set_slot, "trp_temp_array_a", ":slot_no", reg0),
					(ge, DEBUG_TPE_general, 1),
					(str_store_troop_name, s1, reg0),
					(assign, reg0, ":slot_no"),
					(display_message, "@DEBUG (TPE): Discovered invalid troop.  Replaced with {s1} in slot {reg0}."),
				(try_end),
			(try_end),
			
			(assign, "$g_mt_mode", abm_tournament),

			(party_get_slot, ":town_original_faction", "$current_town", slot_center_original_faction),
			(assign, ":town_index_within_faction", 0),
			(assign, ":end_cond", towns_end),
			(try_for_range, ":cur_town", towns_begin, ":end_cond"),
				(try_begin),
					(eq, ":cur_town", "$current_town"),
					(assign, ":end_cond", 0), #break
				(else_try),
					(party_slot_eq, ":cur_town", slot_center_original_faction, ":town_original_faction"),
					(val_add, ":town_index_within_faction", 1),
				(try_end),
			(try_end),
		   
			(try_begin),
				(eq, "$g_wp_tpe_active", 1),
				(eq, wp_tpe_mod_opt_actual_gear, 0),
				(assign, ":mission_template", "mt_tpe_tournament_standard"),
			(else_try),
				(eq, "$g_wp_tpe_active", 1),
				(eq, wp_tpe_mod_opt_actual_gear, 1),
				(assign, ":mission_template", "mt_tpe_tournament_native_gear"),
			(else_try),
				(assign, ":mission_template", "mt_arena_melee_fight"),
			(try_end),
			
			(set_jump_mission, ":mission_template"), # TPE+ 1.3 - To divorce TPE tournament from native template entirely.
			
			(troop_get_slot, ":player_team", TPE_OPTIONS, tpe_random_team_request),
			# (store_sub, ":max_teams", "$g_tournament_next_num_teams", 1),
			# (val_min, ":player_team", ":max_teams"), # To prevent player from picking a team not available.
			
			(assign, ":player_joined", 1), # Persistent team
			(assign, ":player_tally", 0),
			(call_script, "script_tpe_copy_array", "trp_temp_troop", "trp_temp_array_a", wp_tpe_max_tournament_participants),
			(try_for_range, ":team", 0, "$g_tournament_next_num_teams"),
				(try_for_range, ":teammate", 0, "$g_tournament_next_team_size"),
					(store_mul, ":slot_no", ":team", 8),
					(val_add, ":slot_no", ":teammate"),
					(try_begin),
						(eq, ":player_team", ":team"),
						(eq, ":player_joined", 1),
						(assign, ":player_joined", 0),
						(assign, ":new_troop", "trp_player"),
					(else_try),
						(store_add, ":temp_slot", ":player_tally", ":player_joined"),
						(troop_get_slot, ":new_troop", "trp_temp_array_a", ":temp_slot"),
						# (call_script, "script_tpe_pick_random_participant"),
						# (assign, ":new_troop", reg0),
					(try_end),
					(try_begin),
						(eq, DEBUG_TPE_general, 2),
						(assign, reg1, ":team"),
						(assign, reg2, ":slot_no"),
						(str_store_troop_name, s1, ":new_troop"),
						(display_message, "@DEBUG (TPE): Entry #{reg2} / Team #{reg1} = {s1}"),
					(try_end),
					(troop_set_slot, "trp_temp_troop", ":slot_no", ":new_troop"),  # Stores actual troop information.
					(troop_set_slot, "trp_temp_array_b", ":slot_no", ":team"),    # Stores which team troop is on.
					(troop_set_slot, "trp_temp_array_c", ":slot_no", ":slot_no"), # Stores which entry spot troop gets.
					(set_visitor, ":slot_no", ":new_troop"),
					(call_script, "script_tpe_set_items_for_tournament", ":new_troop", ":team", ":slot_no"),
					(val_add, ":player_tally", 1),
					# Check to see if native gear option is being used instead.
					(eq, wp_tpe_mod_opt_actual_gear, 1),
					(mission_tpl_entry_clear_override_items, "mt_tpe_tournament_native_gear", ":slot_no"),
				(try_end),
			(try_end),
			(call_script, "script_tpe_copy_array", "trp_temp_array_a", "trp_temp_troop", wp_tpe_max_tournament_participants),
			
			(assign, "$g_wp_tpe_team_size", "$g_tournament_next_team_size"),
			(assign, "$g_wp_tpe_timer", 0),
			   
			(jump_to_scene, ":arena_scene"),
			(change_screen_mission),
			###### CONTINUE NEXT FIGHT - END ######
        ]),
      ("leave_tournament",[],"Withdraw from the tournament.",
       [
           (jump_to_menu, "mnu_tpe_tournament_withdraw_verify"),
        ]),

###########################################################################################################################
#####                                                TPE 1.1 Additions                                                #####
###########################################################################################################################

	  ("debug_leave_tournament",[(ge, DEBUG_TPE_general, 1),],"DEBUG: Exit the tournament.",
       [
           (party_set_slot, "$current_town", slot_town_has_tournament, 1), # To allow re-entry for testing.
		   (jump_to_menu, "mnu_town"),
        ]),

    ]), # End of town_tournament
###########################################################################################################################
#####                                           END OF TPE_TOWN_TOURNAMENT                                            #####
###########################################################################################################################
	
	("tpe_jump_to_rankings", mnf_scale_picture|mnf_disable_all_keys,
		"I shouldn't see this.  This should automatically be covered by the ranking display.",
		"none",
		[
			(try_begin),
				(troop_slot_eq, TPE_OPTIONS, tpe_val_window_mode, 0),
				(change_screen_return),
				(start_presentation, "prsnt_tpe_ranking_display"),
			(else_try),
				(troop_slot_eq, TPE_OPTIONS, tpe_val_window_mode, 1),
				(change_screen_return),
				(assign, "$g_wp_tpe_troop", "trp_player"),
				(troop_set_slot, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
				(start_presentation, "prsnt_tournament_options_panel"),
			(else_try),
				(troop_slot_eq, TPE_OPTIONS, tpe_val_window_mode, 2), # Tournament Ending
				(change_screen_return),
				(start_presentation, "prsnt_tpe_final_display"),
			(try_end),
		],
		[
			("continue",[], "View Rankings...",	[]),
		]),
		
	("tpe_tournament_withdraw_verify",0,
		"Are you sure you want to withdraw from the tournament?",
		"none",
		[],
		[
			("tournament_withdraw_yes", [], "Yes. This is a pointless affectation.",
				[(jump_to_menu, "mnu_tpe_town_tournament_won_by_another"),]),
			  
			("tournament_withdraw_no", [], "No, not as long as there is a chance of victory!",
				[(jump_to_menu, "mnu_tpe_town_tournament"),]),
		]),
  
    ("tpe_town_tournament_won_by_another",mnf_disable_all_keys,
		"As the only {reg3?fighter:man} to remain undefeated this day, {s1} wins the lists and the glory of this tournament.",
		"none",
		[
			(call_script, "script_tpe_sort_troops_and_points_without_player", slot_troop_tournament_total_points),
			(assign, ":winner_found", 0),
			(try_for_range, ":rank", 1, 5),
				(eq, ":winner_found", 0),
				(troop_get_slot, ":troop_winner", tpe_ranking_array, ":rank"),
				(neq, ":troop_winner", "trp_player"),
				(assign, ":winner_found", 1),
			(try_end),
			(call_script, "script_change_troop_renown", ":troop_winner", 20),
			(troop_get_type, reg3, ":troop_winner"),
			(str_store_troop_name, s1, ":troop_winner"),
		],
		[
			("continue", [], "Continue...",
				[(jump_to_menu, "mnu_town"),]),
		]),
		
	# TPE+ 1.4
	# Adds in configuration menu to access tournament settings outside of tournaments.
	("tpe_tournament_config",mnf_disable_all_keys,
		"This is the Tournament Play Enhancement configuration menu.  Here you can alter tournament settings to function as you wish.",
		"none",
		[
			(this_or_next|eq, MOD_FLORIS_INSTALLED, 0),
			(this_or_next|ge, DEBUG_TPE_general, 1),
			(this_or_next|ge, DEBUG_TPE_ai_behavior, 1),
			(ge, DEBUG_TPE_DESIGN, 1),
		],
		[
			("tpe_enable_tourny", [(eq, "$g_wp_tpe_active", 0),], "Enable Tournament Enhancements",	
				[
					(assign, "$g_wp_tpe_active", 1),
					(jump_to_menu, "mnu_tpe_tournament_config"),
				]),
			
			("tpe_disable_tourny", [(eq, "$g_wp_tpe_active", 1),], "Disable Tournament Enhancements",	
				[
					(assign, "$g_wp_tpe_active", 0),
					(assign, "$tpe_quests_active", 0),
					(jump_to_menu, "mnu_tpe_tournament_config"),
				]),
			
			("tpe_enable_quests", 
				[
					(eq, "$tpe_quests_active", 0),
					(eq, "$g_wp_tpe_active", 1),
				], "Enable Automatic Tournament Quests",	
				[
					(assign, "$tpe_quests_active", 1),
					(jump_to_menu, "mnu_tpe_tournament_config"),
				]),
			
			("tpe_disable_quests", [(eq, "$tpe_quests_active", 1),], "Disable Automatic Tournament Quests",	
				[
					(assign, "$tpe_quests_active", 0),
					# Disable quest if anything is active.
					(try_begin),
						(this_or_next|check_quest_active, "qst_floris_active_tournament"),
						(neg|quest_slot_eq, "qst_floris_active_tournament", slot_quest_current_state, 0),
						(complete_quest, "qst_floris_active_tournament"),
						(display_message, "@Quest ended due to tournament system quests being disabled."),
						(quest_set_slot, "qst_floris_active_tournament", slot_quest_current_state, 0),
					(try_end),
					# Back to tournament system settings menu.
					(jump_to_menu, "mnu_tpe_tournament_config"),
				]),
			
			("tpe_quest_setting_low", 
				[
					(eq, "$tpe_quests_active", 1),
					(eq, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_LOW),
				], "Set Quest Reactions to Medium (Current: Low)",	
				[
					(assign, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_MEDIUM),
					(jump_to_menu, "mnu_tpe_tournament_config"),
				]),
			
			("tpe_quest_setting_med", 
				[
					(eq, "$tpe_quests_active", 1),
					(eq, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_MEDIUM),
				], "Set Quest Reactions to High (Current: Medium)",	
				[
					(assign, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_HIGH),
					(jump_to_menu, "mnu_tpe_tournament_config"),
				]),
			
			("tpe_quest_setting_high", 
				[
					(eq, "$tpe_quests_active", 1),
					(eq, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_HIGH),
				], "Set Quest Reactions to Low (Current: High)",	
				[
					(assign, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_LOW),
					(jump_to_menu, "mnu_tpe_tournament_config"),
				]),
			
			("tpe_jump_to_options", [(eq, "$g_wp_tpe_active", 1),], "Display Tournament Player Options",	
				[
					(change_screen_return),
					(assign, "$g_wp_tpe_troop", "trp_player"),
					(troop_set_slot, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
					(start_presentation, "prsnt_tournament_options_panel"),
				]),
				
			("tpe_jump_to_design", [(eq, "$g_wp_tpe_active", 1),], "Display Tournament Design Options",	
				[
					(change_screen_return),
					(assign, "$tournament_town", "p_town_1"), # Just picking a default.
					(start_presentation, "prsnt_tpe_design_settings"),
				]),
				
			("tpe_credits", [], "Credits & Information",	
				[
					(change_screen_return),
					(troop_set_slot, tci_objects, tci_val_information_mode, 0),
					(start_presentation, "prsnt_tpe_credits"),
				]),
				
			# ("tpe_loot_table", [], "Sort TPE Loot Table",	
				# [
					# (try_for_range, ":item_slot", 201, 242),
						# (troop_get_slot, ":item_no", tpe_xp_table, ":item_slot"),
						# (store_sub, reg31, ":item_slot", 200),
						# (str_store_item_name, s31, ":item_no"),
						# (store_item_value, reg32, ":item_no"),
						# (display_message, "@Item #{reg31} - '{s31}' is worth {reg32} denars."),
						# (eq, ":item_slot", 24),
						# (display_message, "@END OF NON-SCALING LOOT"),
					# (try_end),
				# ]),
				
			("continue", [], "Continue...",	[(jump_to_menu, "mnu_camp"),]),
		]),
 ]

tpe_join = [
	(else_try),
	(eq, "$g_wp_tpe_active", 1),
	(call_script, "script_tpe_fill_tournament_participants_troop", "$current_town", 1),
	(assign, "$g_tournament_cur_tier", 0),
	(assign, "$g_tournament_player_team_won", -1),
	(assign, "$g_tournament_bet_placed", 0),
	(assign, "$g_tournament_bet_win_amount", 0),
	(assign, "$g_tournament_last_bet_tier", -1),
	(assign, "$g_tournament_next_num_teams", 0),
	(assign, "$g_tournament_next_team_size", 0),
	(jump_to_menu, "mnu_tpe_town_tournament"),
	(try_end),
]

from util_common import *
from util_wrappers import *

def modmerge_game_menus(orig_game_menus, check_duplicates = False):
    if( not check_duplicates ):
        orig_game_menus.extend(game_menus) # Use this only if there are no replacements (i.e. no duplicated item names)
    else:
    # Use the following loop to replace existing entries with same id
        for i in range (0,len(game_menus)-1):
          find_index = find_object(orig_game_menus, game_menus[i][0]); # find_object is from header_common.py
          if( find_index == -1 ):
            orig_game_menus.append(game_menus[i])
          else:
            orig_game_menus[find_index] = game_menus[i]
	
	# splice this into camp menu to call the tournament options menu
    find_index = find_object(orig_game_menus, "camp")
    orig_game_menus[find_index][5].insert(9,
            ("camp_mod_opition",[],"Tournament System Settings", [(jump_to_menu, "mnu_tpe_tournament_config")]),
          )
		  
# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]
        modmerge_game_menus(orig_game_menus)
        find_i = list_find_first_match_i( orig_game_menus, "town" )
        menuoption = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOption("join_tournament")
        codeblock = menuoption.GetConsequenceBlock()
        codeblock.InsertBefore(0, [(try_begin), (eq, "$g_wp_tpe_active", 0),])
        codeblock.Append(tpe_join)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)