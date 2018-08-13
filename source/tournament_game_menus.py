# Tournament Play Enhancements (1.2) by Windyplains
# Released 9/22/2011

# WHAT THIS FILE DOES:
# Replaces "town_tournament" menu.
# Replaces "town_tournament_won" menu.

# INSTALLATION INSTRUCTIONS:
# 1) In module_game_menus.py you need to do the following:
#    a) Rename "town_tournament_won" to "orig_town_tournament_won".
#    b) Rename "town_tournament" to "orig_town_tournament".
#
# Note: The new name isn't as important as simply changing the old names so that these menus below replace them on compile.  Yes, I am aware Modmerger should do this itself,
# but that feature doesn't appear to function properly.  It simply doesn't add the menus if they are duplicate instead of replacing the old ones.

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
## REPLACEMENT MENU - menu_town_tournament_won
(
    "town_tournament_won",mnf_disable_all_keys,
    "You have won the tournament of {s3}! You are filled with pride as the crowd cheers your name.\
 In addition to honour, fame and glory, you earn a prize of {reg9} denars. {s8}",
    "none",
    [
        ## TOURNAMENT PLAY ENHANCEMENTS (1.0) begin - Windyplains
		# Determine scaled renown
		(call_script, "script_tpe_determine_scaled_renown"),
		(assign, ":sr_renown", reg0),

		# Determines relation gain based on repeated wins in the same town.
		(str_store_party_name, s3, "$current_town"),
		(party_get_slot, ":total_wins", "$current_town", slot_center_tournament_wins),
		(val_add, ":total_wins", 1),
		(party_set_slot, "$current_town", slot_center_tournament_wins, ":total_wins"),
		
		(try_begin),
			(eq, "$g_wp_tpe_renown_scaling", 1),
			(call_script, "script_change_troop_renown", "trp_player", ":sr_renown"),
			(call_script, "script_change_player_relation_with_center", "$current_town", ":total_wins"),
			
			# Raises relation with Lords that are (present) AND (friendly).  Enemies lose relation.
			(call_script, "script_tpe_rep_gain_lords"),
			
			# Raises relation with Ladies that are (present).  More so if in courtship.
			(call_script, "script_tpe_rep_gain_ladies"),
		(else_try),
			# Everything in this grouping leaves the settings as they would be in the Native game.
			(call_script, "script_change_troop_renown", "trp_player", 20),
			(call_script, "script_change_player_relation_with_center", "$current_town", 1),
		(try_end),
		#(str_store_party_name, s3, "$current_town"),                                      # original script removed by Renown Scaling.
		#(call_script, "script_change_troop_renown", "trp_player", 20),                    # original script removed by Renown Scaling.
        #(call_script, "script_change_player_relation_with_center", "$current_town", 1),   # original script removed by Renown Scaling.
		## TOURNAMENT PLAY ENHANCEMENTS end
		
        (assign, reg9, 500), # Was 200
        (add_xp_to_troop, 700, "trp_player"), # Was 250
        (troop_add_gold, "trp_player", reg9),
        (str_clear, s8),
        (store_add, ":total_win", "$g_tournament_bet_placed", "$g_tournament_bet_win_amount"),
        (try_begin),
          (gt, "$g_tournament_bet_win_amount", 0),
          (assign, reg8, ":total_win"),
          (str_store_string, s8, "@Moreover, you earn {reg8} denars from the clever bets you placed on yourself..."),
        (try_end),
		(try_begin),
			(this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
				(neg|troop_slot_ge, "trp_player", slot_troop_renown, 70),
			(neg|troop_slot_ge, "trp_player", slot_troop_renown, 145),

			(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, sfai_feast),
			(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),
			(str_store_string, s8, "str_s8_you_are_also_invited_to_attend_the_ongoing_feast_in_the_castle"),
		(try_end),
        (troop_add_gold, "trp_player", ":total_win"),
        (assign, ":player_odds_sub", 0),
        (store_div, ":player_odds_sub", "$g_tournament_bet_win_amount", 5),
        (party_get_slot, ":player_odds", "$current_town", slot_town_player_odds),
        (val_sub, ":player_odds", ":player_odds_sub"),
        (val_max, ":player_odds", 250),
        (party_set_slot, "$current_town", slot_town_player_odds, ":player_odds"),
        (call_script, "script_play_victorious_sound"),
        
        (unlock_achievement, ACHIEVEMENT_MEDIEVAL_TIMES),
		# TPE 1.2 + Added ability to auto-activate TPE.
		(try_begin),
			(eq, wp_tpe_player_can_disable, 0),
			(assign, "$g_wp_tpe_active", 1),
		(try_end),
		# TPE 1.2 -
        ],
    [
      ("continue", [], "Continue...",
       [(jump_to_menu, "mnu_town"),
        ]),
    ]
  ),
  
 ## REPLACEMENT MENU - menu_town_tournament
 (
    "town_tournament",mnf_disable_all_keys,
    "{s1}You are at tier {reg0} of the tournament, with {reg1} participants remaining. In the next round, there will be {reg2} teams with {reg3} {reg4?fighters:fighter} each.",
    "none",
    [
        (party_set_slot, "$current_town", slot_town_has_tournament, 0), #No way to return back if this menu is left
        (call_script, "script_sort_tournament_participant_troops"),#Moving trp_player to the top of the list
        (call_script, "script_get_num_tournament_participants"),
        (assign, ":num_participants", reg0),
        (try_begin),
          (neg|troop_slot_eq, "trp_tournament_participants", 0, 0),#Player is defeated

          (assign, ":player_odds_add", 0),
          (store_div, ":player_odds_add", "$g_tournament_bet_placed", 5),
          (party_get_slot, ":player_odds", "$current_town", slot_town_player_odds),
          (val_add, ":player_odds", ":player_odds_add"),
          (val_min, ":player_odds", 4000),
          (party_set_slot, "$current_town", slot_town_player_odds, ":player_odds"),

          (jump_to_menu, "mnu_town_tournament_lost"),
        (else_try),
          (eq, ":num_participants", 1),#Tournament won
          (jump_to_menu, "mnu_town_tournament_won"),
        (else_try),
          (try_begin),
            (le, "$g_tournament_next_num_teams", 0),
            (call_script, "script_get_random_tournament_team_amount_and_size"),
            (assign, "$g_tournament_next_num_teams", reg0),
            (assign, "$g_tournament_next_team_size", reg1),
          (try_end),
          (assign, reg2, "$g_tournament_next_num_teams"),
          (assign, reg3, "$g_tournament_next_team_size"),
          (store_sub, reg4, reg3, 1),
          (str_clear, s1),
          (try_begin),
            (eq, "$g_tournament_player_team_won", 1),
            (str_store_string, s1, "@Victory is yours! You have won this melee, but now you must prepare yourself for the next round. "),
          (else_try),
            (eq, "$g_tournament_player_team_won", 0),
            (str_store_string, s1, "@You have been bested in this melee, but the master of ceremonies declares a recognition of your skill and bravery, allowing you to take part in the next round. "),
          (try_end),
          (assign, reg1, ":num_participants"),
          (store_add, reg0, "$g_tournament_cur_tier", 1),
        (try_end),
        ],
    [
      ("tournament_view_participants", [], "View participants.",
       [(jump_to_menu, "mnu_tournament_participants"),
        ]),
		
	  ## TOURNAMENT PLAY ENHANCEMENTS (1.0) begin - Windyplains
	  ("tournament_options_panel", [(eq, "$g_wp_tpe_active", 1),], "Change tournament options.",
       [
	    (change_screen_return),
		(assign, "$g_wp_tpe_troop", "trp_player"),
	    (start_presentation, "prsnt_tournament_options_panel"),
        ]),

      ("tournament_bet", [(neq, "$g_tournament_cur_tier", "$g_tournament_last_bet_tier"),(troop_slot_eq, "trp_player", slot_troop_tournament_bet_option, 0)], "Place a bet on yourself.",
       [(jump_to_menu, "mnu_tournament_bet"),
        ]), # WP_TPE changes this to disappear if the persistent bet option is set.
		
      ("tournament_join_next_fight", [], "Fight in the next round.",
       [
		   # continued TPE enhancements.  This inputs your persistent bet.
			(try_begin),
				(eq, "$g_wp_tpe_active", 1),
				(troop_get_slot, ":bet_amount", "trp_player", slot_troop_tournament_bet_amount),
				(store_troop_gold,":current_gold","trp_player"),
				(try_begin),
					(ge, ":current_gold", ":bet_amount"),
					(call_script, "script_tournament_place_bet", ":bet_amount"),
					(store_troop_gold,":current_gold","trp_player"),
					(assign, reg1, ":current_gold"),
					(assign, reg0, ":bet_amount"),
					(display_message, "@You place a bet of {reg0} denars before starting the round.  You have {reg1} denars remaining."),
				(else_try),
					(assign, reg0, ":bet_amount"),
					(display_message, "@You were unable to cover a bet of {reg0} denars."),
				(try_end),
			(try_end),
      ## TOURNAMENT PLAY ENHANCEMENTS end
	  
		   (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
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
           (troop_set_slot, "trp_tournament_participants", 0, -1),#Removing trp_player from the list
           (troop_set_slot, "trp_temp_array_a", 0, "trp_player"),
           (try_for_range, ":slot_no", 1, "$g_tournament_num_participants_for_fight"),
             (call_script, "script_get_random_tournament_participant"),
             (troop_set_slot, "trp_temp_array_a", ":slot_no", reg0),
           (try_end),
           (call_script, "script_shuffle_troop_slots", "trp_temp_array_a", 0, "$g_tournament_num_participants_for_fight"),
           
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
           
           (set_jump_mission, "mt_arena_melee_fight"),
           
		    ## TOURNAMENT PLAY ENHANCEMENTS (1.0) begin - Windyplains - Tournament Teams
			(assign, ":player_tally", 0),
			(call_script, "script_copy_inventory", "trp_temp_troop", "trp_temp_array_a"),
		    (try_for_range, ":team", 0, "$g_tournament_next_num_teams"),
				(try_for_range, ":teammate", 0, "$g_tournament_next_team_size"),
					(store_mul, ":slot_no", ":team", 8),
					(val_add, ":slot_no", ":teammate"),
					(troop_get_slot, ":troop_no", "trp_temp_array_a", ":player_tally"),
					(troop_set_slot, "trp_temp_troop", ":slot_no", ":troop_no"),
					(troop_set_slot, "trp_temp_array_b", ":slot_no", ":team"),
					(troop_set_slot, "trp_temp_array_c", ":slot_no", ":slot_no"),
					(set_visitor, ":slot_no", ":troop_no"),
					(call_script, "script_tpe_set_items_for_tournament", ":troop_no", ":team", ":slot_no"),
					(val_add, ":player_tally", 1),
				(try_end),
			(try_end),
			(call_script, "script_copy_inventory", "trp_temp_array_a", "trp_temp_troop"),

		   (assign, "$g_tournament_next_num_teams", 0),
           (assign, "$g_tournament_next_team_size", 0),
           
		   ## TPE 1.2 + Added native town tournament styles back.
		   (try_begin),
				(eq, "$g_wp_tpe_active", 0),
			   (try_begin),
				 (eq, ":town_original_faction", "fac_kingdom_1"),
				 #Swadia
				 (store_mod, ":mod", ":town_index_within_faction", 4),
				 (try_begin),
				   (eq, ":mod", 0),
				   (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 0, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
				 (else_try),
				   (eq, ":mod", 1),
				   (call_script, "script_set_items_for_tournament", 100, 100, 0, 0, 0, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
				 (else_try),
				   (eq, ":mod", 2),
				   (call_script, "script_set_items_for_tournament", 100, 0, 100, 0, 0, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
				 (else_try),
				   (eq, ":mod", 3),
				   (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 40, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
				 (try_end),
			   (else_try),
				 (eq, ":town_original_faction", "fac_kingdom_2"),
				 #Vaegirs
				 (store_mod, ":mod", ":town_index_within_faction", 4),
				 (try_begin),
				   (eq, ":mod", 0),
				   (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 0, 0, 0, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
				 (else_try),
				   (eq, ":mod", 1),
				   (call_script, "script_set_items_for_tournament", 100, 50, 0, 0, 0, 20, 30, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
				 (else_try),
				   (eq, ":mod", 2),
				   (call_script, "script_set_items_for_tournament", 100, 0, 50, 0, 0, 20, 30, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
				 (else_try),
				   (eq, ":mod", 3),
				   (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 30, 0, 60, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
				 (try_end),
			   (else_try),
				 (eq, ":town_original_faction", "fac_kingdom_3"),
				 #Khergit
				 (store_mod, ":mod", ":town_index_within_faction", 2),
				 (try_begin),
				   (eq, ":mod", 0),
				   (call_script, "script_set_items_for_tournament", 100, 0, 0, 0, 0, 40, 60, 0, "itm_arena_tunic_red", "itm_steppe_helmet_red"),
				 (else_try),
				   (eq, ":mod", 1),
				   (call_script, "script_set_items_for_tournament", 100, 50, 25, 0, 0, 30, 50, 0, "itm_arena_tunic_red", "itm_steppe_helmet_red"),
				 (try_end),
			   (else_try),
				 (eq, ":town_original_faction", "fac_kingdom_4"),
				 #Nords
				 (store_mod, ":mod", ":town_index_within_faction", 3),
				 (try_begin),
				   (eq, ":mod", 0),
				   (call_script, "script_set_items_for_tournament", 0, 0, 50, 80, 0, 0, 0, 0, "itm_arena_armor_red", -1),
				 (else_try),
				   (eq, ":mod", 1),
				   (call_script, "script_set_items_for_tournament", 0, 0, 50, 80, 50, 0, 0, 0, "itm_arena_armor_red", -1),
				 (else_try),
				   (eq, ":mod", 2),
				   (call_script, "script_set_items_for_tournament", 40, 0, 0, 100, 0, 0, 0, 0, "itm_arena_armor_red", -1),
				 (try_end),
			   (else_try),
				 #Rhodoks
				 (eq, ":town_original_faction", "fac_kingdom_5"),
				 (call_script, "script_set_items_for_tournament", 25, 100, 60, 0, 30, 0, 30, 50, "itm_arena_tunic_red", "itm_tourney_helm_red"), # TPE Change itm_arena_helmet_red
			   (else_try),
				 #Sarranids
				 (store_mod, ":mod", ":town_index_within_faction", 2),
				 (try_begin),
				   (eq, ":mod", 0),
				   (call_script, "script_set_items_for_tournament", 100, 40, 60, 0, 30, 30, 0, 0, "itm_arena_tunic_red", "itm_arena_turban_red"),
				 (else_try),
				   (call_script, "script_set_items_for_tournament", 50, 0, 60, 0, 30, 30, 0, 0, "itm_arena_tunic_red", "itm_arena_turban_red"),
				 (try_end),
			   (try_end),
		   (try_end),
		   ## TPE 1.2 -
		   
           (jump_to_scene, ":arena_scene"),
           (change_screen_mission),
        ]),
      ("leave_tournament",[],"Withdraw from the tournament.",
       [
           (jump_to_menu, "mnu_tournament_withdraw_verify"),
        ]),

###########################################################################################################################
#####                                                TPE 1.1 Additions                                                #####
###########################################################################################################################

	 ("debug_leave_tournament",[(eq, wp_tpe_debug, 1),],"DEBUG: Exit the tournament.",
       [
           (party_set_slot, "$current_town", slot_town_has_tournament, 1), # To allow re-entry for testing.
		   (jump_to_menu, "mnu_town"),
        ]),
		
###########################################################################################################################
#####                                                TPE 1.2 Additions                                                #####
###########################################################################################################################

	  ("tpe_enable",[(eq, "$g_wp_tpe_active", 0), (eq, wp_tpe_player_can_disable, 1),],"Enable tournament enhancements.",
       [(assign, "$g_wp_tpe_active", 1),]),
		
	  ("tpe_disable",[(eq, "$g_wp_tpe_active", 1), (eq, wp_tpe_player_can_disable, 1),],"Disable tournament enhancements.",
       [(assign, "$g_wp_tpe_active", 0),]),
		
    ]
  ),
 ]
	
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

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]
        modmerge_game_menus(orig_game_menus)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
