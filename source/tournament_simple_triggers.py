# Tournament Play Enhancements (1.5) by Windyplains

from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *
##diplomacy start+
# from header_terrain_types import *
# from module_factions import dplmc_factions_end
##diplomacy end+
from module_quests import *
from module_constants import *

####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#  Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################



simple_triggers = [
	
# QUEST: floris_active_tournament
# Determine if tournaments are active in a town.
#  - Deliver quest if tournament active and quest is not.  
#  - End quest if tournament is not active and quest is.
(12,
	[
		(map_free),
		(eq, "$tpe_quests_active", 1),
		(assign, ":closest_town_no", -1),
		(assign, ":closest_town_dist", -1),
		(try_for_range, ":center_no", towns_begin, towns_end),
			(party_get_slot, ":has_tournament", ":center_no", slot_town_has_tournament), # 0 = no, 1 = last day, 2+ = ongoing.
			(try_begin),
				##### ACQUIRE QUEST: Determine appropriate city #####
				# Make sure there is enough time to travel there.
				(ge, ":has_tournament", 3),
				# Check if the town is hostile to the player.
				(call_script, "script_tpe_store_town_faction_to_reg0", ":center_no"),
				(store_relation, ":relation", reg0, "fac_player_supporters_faction"),
				(ge, ":relation", 0),
				(party_get_slot, ":troop_host", ":center_no", slot_town_lord),
				(ge, ":troop_host", 0), # Make sure someone actually controls the town.
				(neq, ":troop_host", "trp_player"), # Make sure the player isn't inviting himself.
				# See if this town is closer than the current candidate.
				(store_distance_to_party_from_party, ":distance", "p_main_party", ":center_no"),
				(this_or_next|lt, ":distance", ":closest_town_dist"),
				(eq, ":closest_town_dist", -1),
				(assign, ":closest_town_dist", ":distance"),
				(assign, ":closest_town_no", ":center_no"),
				(ge, DEBUG_TPE_QUESTS, 1),
				(assign, reg31, ":has_tournament"),
				(str_store_party_name, s31, ":center_no"),
				(display_message, "@DEBUG (Quest Pack 1): {s31} has a tournament with {reg31} days left."),
			(else_try),
				##### FAIL QUEST: EXPIRED #####
				(le, ":has_tournament", 0),
				# Condition: Ensure quest IS active.
				(check_quest_active, "qst_floris_active_tournament"),
				(neg|quest_slot_eq, "qst_floris_active_tournament", slot_quest_current_state, qp1_tournament_participated_in_tournament),
				(neg|quest_slot_eq, "qst_floris_active_tournament", slot_quest_current_state, qp1_tournament_refused_invitation),
				(quest_slot_eq, "qst_floris_active_tournament", slot_quest_target_center, ":center_no"),
				# Set quest to failed due to timeout.
				(fail_quest, "qst_floris_active_tournament"),
				(complete_quest, "qst_floris_active_tournament"),
				(quest_set_slot, "qst_floris_active_tournament", slot_quest_current_state, qp1_tournament_refused_invitation),
				(try_begin),
					(quest_slot_eq, "qst_floris_active_tournament", slot_quest_current_state, qp1_tournament_message_received), # If you weren't invited then no one should care if you don't attend.
					(ge, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_MEDIUM),
					(call_script, "script_change_troop_renown", "trp_player", -2),
					(ge, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_HIGH),
					(quest_get_slot, ":town_lord", "qst_floris_active_tournament", slot_quest_giver_troop),
					(str_store_troop_name, s21, ":town_lord"),
					(display_message, "@{s21} is insulted by your refusal of his invitation.", gpu_red),
					(call_script, "script_troop_change_relation_with_troop", "trp_player", ":town_lord", -2),
				(try_end),
				# Let the player know he failed the quest if he's close enough to hear of it end.
				#(call_script, "script_cf_qus_party_close_to_center", "p_main_party", ":center_no"),
				(str_store_party_name, s31, ":center_no"),
				(display_message, "@The tournament in {s31} has ended."),
			(else_try),
				##### FAIL QUEST: HELD IN HOSTILE CITY ####
				(check_quest_active, "qst_floris_active_tournament"),
				(quest_slot_eq, "qst_floris_active_tournament", slot_quest_target_center, ":center_no"),
				(call_script, "script_tpe_store_town_faction_to_reg0", ":center_no"),
				(store_relation, ":relation", reg0, "fac_player_supporters_faction"),
				(lt, ":relation", 0),
				# Set quest to failed due to inability to attend.
				(fail_quest, "qst_floris_active_tournament"),
				(complete_quest, "qst_floris_active_tournament"),
				(str_store_party_name, s31, ":center_no"),
				(display_message, "@Quest ended due to {s31} becoming hostile."),
				(quest_set_slot, "qst_floris_active_tournament", slot_quest_current_state, 0),
			(try_end),
		(try_end),
		
		# Now assign a tournament to go to if there is a valid option and the quest isn't already active.
		(is_between, ":closest_town_no", towns_begin, towns_end),
		(neg|check_quest_active, "qst_floris_active_tournament"),
		(quest_slot_eq, "qst_floris_active_tournament", slot_quest_dont_give_again_remaining_days, 0),
		#(call_script, "script_cf_qus_party_close_to_center", "p_main_party", ":center_no"),
				
		# Initialize some quest information.
		(party_get_slot, ":days_left", ":closest_town_no", slot_town_has_tournament),
		(quest_set_slot, "qst_floris_active_tournament", slot_quest_target_center, ":closest_town_no"),
		(quest_set_slot, "qst_floris_active_tournament", slot_quest_expiration_days, ":days_left"),
		(quest_set_slot, "qst_floris_active_tournament", slot_quest_dont_give_again_period, 10),
		(quest_set_slot, "qst_floris_active_tournament", slot_quest_dont_give_again_remaining_days, 10),
		(quest_set_slot, "qst_floris_active_tournament", slot_quest_xp_reward, 100),
		(party_get_slot, ":town_lord", ":closest_town_no", slot_town_lord),
		(troop_is_hero, ":town_lord"),
		(quest_set_slot, "qst_floris_active_tournament", slot_quest_giver_troop, ":town_lord"),
		
		(str_clear, s8),
		(str_clear, s9),
		(str_clear, s12),
		(str_clear, s13),
		
		# Set quest to active.
		(quest_get_slot, ":town_lord", "qst_floris_active_tournament", slot_quest_giver_troop),
		(quest_get_slot, ":closest_town_no", "qst_floris_active_tournament", slot_quest_target_center),
		(str_store_troop_name_link, s9, ":town_lord"),
		(str_store_party_name_link, s13, ":closest_town_no"),
		(str_store_troop_name, s8, ":town_lord"),
		(str_store_party_name, s12, ":closest_town_no"),
		(try_begin), # Checks if your renown warrants an invitation based on distance away.
			(store_distance_to_party_from_party, ":distance", "p_main_party", ":closest_town_no"),
			(val_mul, ":distance", 2),
			(troop_slot_ge, "trp_player", slot_troop_renown, 50),
			(troop_slot_ge, "trp_player", slot_troop_renown, ":distance"),
			(dialog_box, "str_qp1_tournaments_invited_by_s8_to_s12", "@A Messenger Arrives"),
			(str_store_string, s2, "str_qp1_quest_desc_tournament_invited_by_s9_to_s13"),
			(quest_set_slot, "qst_floris_active_tournament", slot_quest_current_state, qp1_tournament_message_received),
		(else_try),
			(dialog_box, "str_qp1_tournaments_held_by_s8_in_s12", "@Rumor of the Road"),
			(str_store_string, s2, "str_qp1_quest_desc_tournament_held_by_s9_to_s13"),
			(quest_set_slot, "qst_floris_active_tournament", slot_quest_current_state, 0), # Should mean no one cares if you come or not.
		(try_end),
		(setup_quest_text, "qst_floris_active_tournament"),
		(call_script, "script_start_quest", "qst_floris_active_tournament", ":town_lord"),
	]),

# QUEST: floris_active_tournament
# Determine if tournaments are active in a town.
#  - Deliver quest if tournament active and quest is not.  
#  - End quest if tournament is not active and quest is.
(12,
	[
		(map_free),
		(this_or_next|ge, DEBUG_TPE_general, 1),
		(ge, DEBUG_TPE_QUESTS, 1),
		(eq, "$g_wp_tpe_active", 1),
		(str_clear, s21),
		(display_message, "@List of Active Tournaments"),
		(try_for_range, ":center_no", towns_begin, towns_end),
			(party_get_slot, ":has_tournament", ":center_no", slot_town_has_tournament), # 0 = no, 1 = last day, 2+ = ongoing.
			(ge, ":has_tournament", 1),
			(assign, reg31, ":has_tournament"),
			(str_store_party_name, s31, ":center_no"),
			(display_message, "@{s31} has a tournament with {reg31} days left."),
		(try_end),
	]),

]


# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "simple_triggers"
        orig_simple_triggers = var_set[var_name_1]
        orig_simple_triggers.extend(simple_triggers)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)