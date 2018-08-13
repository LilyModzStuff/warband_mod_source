# Formations AI for Warband by Motomataru
# rel. 01/03/11

# This function attaches AI_triggers only to missions "lead_charge" and "quick_battle_battle"
# For other missions, add to end of triggers list like so: " ] + AI_triggers "


from header_common import *
from header_operations import *
from header_mission_templates import *
from module_constants import *

#AI triggers v3 for WB by motomataru
AI_triggers = [  
	(ti_before_mission_start, 0, 0, [(party_slot_eq, "p_main_party", slot_party_pref_formations, 1)], [
		# (assign, "$cur_casualties", 0), #just use BP_Fight if prev_casualties no longer matters
		# (assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
		(assign, "$battle_phase", BP_Setup),
		# (assign, "$clock_reset", 0),
		(init_position, Team0_Cavalry_Destination),
		(init_position, Team1_Cavalry_Destination),
		(init_position, Team2_Cavalry_Destination),
		(init_position, Team3_Cavalry_Destination),
	]),

	(0, AI_Delay_For_Spawn, ti_once, [(party_slot_eq, "p_main_party", slot_party_pref_formations, 1)], [
		(try_for_agents, ":cur_agent"),
			(agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 0),
		(try_end),
		(set_fixed_point_multiplier, 100),
		# (call_script, "script_store_battlegroup_data"),	done in formations trigger
		(try_for_range, ":team", 0, 4),
			(call_script, "script_battlegroup_get_position", pos0, ":team", grc_everyone),
			(position_get_x, reg0, pos0),
			(team_set_slot, ":team", slot_team_starting_x, reg0),
			(position_get_y, reg0, pos0),
			(team_set_slot, ":team", slot_team_starting_y, reg0),
			
			#prevent confusion over AI not using formations for archers
			(neq, ":team", "$fplayer_team_no"),
			(store_add, ":slot", slot_team_d0_formation, grc_archers),
			(team_set_slot, ":team", ":slot", formation_none),
		(try_end),
		(call_script, "script_field_tactics", 1)
	]),

	(0.1, 0, 0, [(party_slot_eq, "p_main_party", slot_party_pref_formations, 1)], [	
		(store_mission_timer_c_msec, reg0),
		(val_sub, reg0, "$last_player_trigger"),
		(ge, reg0, 250),	#delay to offset from formations trigger (trigger delay does not work right)
		(val_add, "$last_player_trigger", 500),
		
		(set_fixed_point_multiplier, 100),
		(call_script, "script_store_battlegroup_data"),
		(try_begin),	
			(lt, "$battle_phase", BP_Fight),
			(call_script, "script_cf_count_casualties"),
			(assign, "$battle_phase", BP_Fight),
			(call_script, "script_field_tactics", 1), #to reset ranged on fighting start
			(assign, "$ranged_clock", 0), 
		(else_try),
			(eq, "$battle_phase", BP_Setup), #army moves to initial position during setup (don't reassess archer position)	
			(call_script, "script_field_tactics", 0),
		(else_try),
			(call_script, "script_field_tactics", 1),
			(ge, "$battle_phase", BP_Fight),
			(store_mul, reg1, 5, Reform_Trigger_Modulus),
			(store_mod, reg0, "$ranged_clock", reg1),		
			(eq, reg0, 0),
			(try_begin),
				(neg|team_slot_eq, 0, slot_team_reinforcement_stage, "$defender_reinforcement_stage"),
				(team_set_slot, 0, slot_team_reinforcement_stage, "$defender_reinforcement_stage"),	
				(try_for_range, ":division", 0, 9),
					(store_add, ":slot", slot_team_d0_type, ":division"),
					(team_set_slot, 0, ":slot", sdt_unknown),
					(team_set_slot, 2, ":slot", sdt_unknown),
				(try_end),
			(try_end),
			(try_begin),
				(neg|team_slot_eq, 1, slot_team_reinforcement_stage, "$attacker_reinforcement_stage"),
				(team_set_slot, 1, slot_team_reinforcement_stage, "$attacker_reinforcement_stage"),	
				(try_for_range, ":division", 0, 9),
					(store_add, ":slot", slot_team_d0_type, ":division"),
					(team_set_slot, 1, ":slot", sdt_unknown),
					(team_set_slot, 3, ":slot", sdt_unknown),
				(try_end),
			(try_end),
		(try_end),

		(try_begin),
			(eq, "$battle_phase", BP_Setup),
			(assign, ":not_in_setup_position", 0),
			(try_for_range, ":bgteam", 0, 4),
				(neq, ":bgteam", "$fplayer_team_no"),
				(team_slot_ge, ":bgteam", slot_team_size, 1),
				(call_script, "script_battlegroup_get_position", pos1, ":bgteam", grc_archers),
				(team_get_order_position, pos0, ":bgteam", grc_archers),
				(get_distance_between_positions, reg0, pos0, pos1),
				(gt, reg0, 500),
				(assign, ":not_in_setup_position", 1),
			(try_end),
			(eq, ":not_in_setup_position", 0),	#all AI reached setup position?
			(assign, "$battle_phase", BP_Jockey),
		(try_end),
		
		(val_add, "$ranged_clock", 1),
	]),

	(0, 0, ti_once, [ ##caba-encorporate in another trigger?? standard death-cam ones?
		(main_hero_fallen),	#if AI to take over for mods with post-player battle action
		(party_slot_eq, "p_main_party", slot_party_pref_formations, 1),
		(party_slot_eq, "p_main_party", slot_party_pref_bc_charge_ko, 2),
	], [
		(try_for_agents, ":agent"),	#reassign agents to the divisions AI uses
			(agent_is_alive, ":agent"),
			(call_script, "script_agent_fix_division", ":agent"),
		(try_end),

		(set_show_messages, 0),	#undo special player commands for divisions AI uses
		(team_set_order_listener, "$fplayer_team_no", grc_everyone),
		(call_script, "script_order_set_team_slot", clear, "$fplayer_team_no"),
		(team_give_order, "$fplayer_team_no", grc_everyone, mordr_use_any_weapon),
		(team_give_order, "$fplayer_team_no", grc_everyone, mordr_fire_at_will),
		(set_show_messages, 1),
	]),
]

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

		modmerge_formAI_mission_templates(orig_mission_templates)

		# END do your own stuff
            
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)

from util_wrappers import *		
def modmerge_formAI_mission_templates(orig_mission_templates):
	find_i = find_object( orig_mission_templates, "lead_charge" )
	orig_mission_templates[find_i][5].extend(AI_triggers)
	trigger = MissionTemplateWrapper(orig_mission_templates[find_i]).FindTrigger(0, 0, ti_once, [(store_mission_timer_a,":mission_time"),(ge,":mission_time",2)],
        [(call_script, "script_select_battle_tactic"),(call_script, "script_battle_tactic_init")])
	codeblock = trigger.GetConditionBlock()
	codeblock.InsertBefore(0, [(neg|party_slot_eq, "p_main_party", slot_party_pref_formations, 1)]) ## PBOD - Formations AI NOT active
	trigger = MissionTemplateWrapper(orig_mission_templates[find_i]).FindTrigger(5, 0, 0, [(store_mission_timer_a,":mission_time"),(ge,":mission_time",3),(call_script, "script_battle_tactic_apply")], []) 
	codeblock = trigger.GetConditionBlock()
	codeblock.InsertBefore(0, [(neg|party_slot_eq, "p_main_party", slot_party_pref_formations, 1)]) ## PBOD - Formations AI NOT active
	
	find_i = find_object( orig_mission_templates, "quick_battle_battle" )
	orig_mission_templates[find_i][5].extend(AI_triggers)

	

