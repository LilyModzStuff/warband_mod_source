## Prebattle Orders & Deployment by Caba'drin
## v0.92
## 20 Jan 2012

from header_common import *
from header_items import *
from header_operations import *
from header_mission_templates import *
from module_constants import *

## Prebattle Orders & Deployment Begin
init_player_global_variables = ( #in pbod_common_triggers and custom_camera_triggers
  0, 0, ti_once, [(get_player_agent_no, "$fplayer_agent_no"),(ge, "$fplayer_agent_no", 0)], [
  #(ti_after_mission_start, 0, 0, [], [ 
	#(get_player_agent_no, "$fplayer_agent_no"),
	(agent_get_team, "$fplayer_team_no", "$fplayer_agent_no"),		
	(agent_get_horse, ":horse", "$fplayer_agent_no"),
	(agent_set_slot, "$fplayer_agent_no", slot_agent_horse, ":horse"),
  ])
  
init_scene_boundaries = ( #in field_ai_triggers
   ti_after_mission_start, 0, 0, [
    (set_fixed_point_multiplier, 1),
	(get_scene_boundaries, pos2, pos3),
	(position_get_x, "$g_bound_right", pos2),
	(position_get_y, "$g_bound_top", pos2),
	(position_get_x, "$g_bound_left", pos3),
	(position_get_y, "$g_bound_bottom", pos3),
   ], [])
  
shield_bash = ( #in pbod_common_triggers
   0, 0, 1, 
   [
	(game_key_is_down, gk_defend),
	(key_clicked, "$key_special_3"),
	(neg|main_hero_fallen),
	(ge, "$fplayer_agent_no", 0),
	(call_script, "script_cf_shield_bash"),
   ],[]) 

common_pbod_triggers = [
  init_player_global_variables,
  
  #Fix for setting divisions, duplicated in formations code, so disabled in mst_lead_charge
  (ti_on_agent_spawn, 0, 0, [(neq, "$g_next_menu", "mnu_simple_encounter"),(neq, "$g_next_menu", "mnu_join_battle")], [(store_trigger_param_1, ":agent"),(call_script, "script_prebattle_agent_fix_division", ":agent")]),
  (0.5, 0, 0, [(neq, "$g_next_menu", "mnu_simple_encounter"), #not mst_lead_charge (or the various village raid templates...will be better with WSE)
			   (neq, "$g_next_menu", "mnu_join_battle"),
			   (store_mission_timer_a, reg0),(gt, reg0, 4)], 
   [
    (try_for_agents, ":agent"),
		(agent_is_alive, ":agent"),
		(agent_slot_ge, ":agent", slot_agent_new_division, 0),
	    (agent_get_division, ":division", ":agent"),
		(neg|agent_slot_eq, ":agent", slot_agent_new_division, ":division"),
		(agent_get_slot, ":division", ":agent", slot_agent_new_division),
		(agent_set_division, ":agent", ":division"),
	(try_end),   
   ]), 
   
  shield_bash, 
 ] 

real_deployment_triggers = [
 (0, 0.8, ti_once, [(mission_cam_set_screen_color, 0xFF000000),],
   [
	(mission_cam_animate_to_screen_color, 0x00000000, 1000),
   ]),
 ]

split_troop_division_triggers = [
 (0, 0.5, ti_once, [(party_slot_eq, "p_main_party", slot_party_prebattle_customized_divisions, 1)], [  #was ti_after_mission_start, 0, 0 ...better to distance from spawning
	(call_script, "script_prebattle_split_troop_divisions"),
	(party_set_slot, "p_main_party_backup", slot_party_reinforcement_stage, 0),
   ]),
 (1, 0, 0, [(party_slot_eq, "p_main_party", slot_party_prebattle_customized_divisions, 1)], [
    (try_begin),
		(this_or_next|eq, "$fplayer_team_no", 0),
		(eq, "$fplayer_team_no", 2),
		(assign, ":reinforcement_stage", "$defender_reinforcement_stage"),
	(else_try),
		(assign, ":reinforcement_stage", "$attacker_reinforcement_stage"),
	(try_end),
	(neg|party_slot_eq, "p_main_party_backup", slot_party_reinforcement_stage, ":reinforcement_stage"),
	
	(call_script, "script_prebattle_split_troop_divisions"),
	
	(party_set_slot, "p_main_party_backup", slot_party_reinforcement_stage, ":reinforcement_stage"),
   ]),
 ]
		
prebattle_deployment_triggers  = [
 (ti_before_mission_start, 0, 0, [(party_slot_eq, "p_main_party", slot_party_prebattle_customized_deployment, 1)], [
	#Find the number of soldiers in each troop-stack that are ready to upgrade by upgrading the party and finding
	#the changes in troops after the upgrade, then storing the number upgraded in a troop slot.
	(call_script, "script_party_copy", "p_temp_party", "p_main_party"),
	(party_upgrade_with_xp, "p_main_party", 1, 1),

	(party_get_num_companion_stacks, ":previous_num_of_stacks", "p_temp_party"),
	(try_for_range, ":i", 0, ":previous_num_of_stacks"), 
		(party_stack_get_troop_id, ":troop_id", "p_temp_party", ":i"),
		(neg|troop_is_hero, ":troop_id"),
        (troop_set_slot, ":troop_id", slot_troop_prebattle_preupgrade_check, 0),
		(troop_set_slot, ":troop_id",  slot_troop_prebattle_num_upgrade, 0),
	(try_end),
	
	(try_for_range, ":i", 0, ":previous_num_of_stacks"), 
		(party_stack_get_troop_id, ":troop_id", "p_temp_party", ":i"),
		(neg|troop_is_hero, ":troop_id"),
		(troop_slot_eq, ":troop_id", slot_troop_prebattle_preupgrade_check, 0),
		
		(try_for_range, ":down_upgrade_array", slot_party_prebattle_customized_deployment, slot_party_prebattle_customized_deployment + 7),
		    (party_set_slot, "p_main_party_backup", ":down_upgrade_array", 0), #Create an Array of 6 variables to hold current troop's down/upgrade path
		(try_end),
		(assign, ":troop", ":troop_id"),
		(assign, ":end", 7),
     	(try_for_range, ":unused", 0, ":end"),		
			(assign, ":stacks", ":previous_num_of_stacks"),
		    (try_for_range, ":n", 0, ":stacks"), #Find another troop that upgrades to the current troop in the party
			    (party_stack_get_troop_id, ":troop_to_upgrade", "p_temp_party", ":n"),
		        (neg|troop_is_hero, ":troop_to_upgrade"),
				(neq, ":troop_to_upgrade", ":troop"),
			    (troop_get_upgrade_troop, ":upgrade_troop", ":troop_to_upgrade", 0),
			    (eq, ":upgrade_troop", ":troop"),
			    (assign, ":stacks", 0),
		    (try_end),
		    (try_begin),
		        (neq, ":upgrade_troop", ":troop"), #nothing in the party upgrades to this troop
				(assign, ":end", 0), #Break 'Find Downgrades' Loop
				(troop_slot_eq, ":troop", slot_troop_prebattle_preupgrade_check, 0),
				(party_count_members_of_type, ":pre_upgrade", "p_temp_party", ":troop"),
		        (party_count_members_of_type, ":post_upgrade", "p_main_party", ":troop"),
			    (store_sub, ":difference", ":pre_upgrade", ":post_upgrade"),
                (val_max, ":difference", 0), #don't let it be negative
			    (troop_set_slot, ":troop", slot_troop_prebattle_num_upgrade, ":difference"),
				(troop_set_slot, ":troop", slot_troop_prebattle_preupgrade_check, 1),
		    (else_try),
		    #something upgrades to this troop in the party; record that upgrade_troop, then loop again to check if anything upgrades to THAT troop
			    (assign, ":array_begin", slot_party_prebattle_customized_deployment),
				(try_for_range_backwards, ":downgrade_array", ":array_begin", slot_party_prebattle_customized_deployment + 7),
				    (party_slot_eq, "p_main_party_backup", ":downgrade_array", 0),
					(party_set_slot, "p_main_party_backup", ":downgrade_array", ":troop_to_upgrade"),
					(assign, ":array_begin", slot_party_prebattle_customized_deployment + 7),
				(try_end),
				(assign, ":troop", ":troop_to_upgrade"),
			(try_end), #Does anything upgrade to this troop? If-Then-Else
		(try_end), #Downgrade Do...Loop
		
		(troop_slot_eq, ":troop_id", slot_troop_prebattle_preupgrade_check, 0), 
		#If this troop was finished above (nothing upgrades to it, so it isn't mid/end of a continuous tree) no need to continue
		
		(assign, ":troop", ":troop_id"),
		(assign, ":end", 7),
     	(try_for_range, ":unused", 0, ":end"),	
			(troop_get_upgrade_troop, ":upgrade_troop", ":troop", 0),
			(party_count_members_of_type, ":num_upgrade", "p_main_party", ":upgrade_troop"),
			(try_begin),
			    (gt, ":num_upgrade", 0),
			    (assign, ":array_end", slot_party_prebattle_customized_deployment + 7),
			    (try_for_range, ":upgrade_array", slot_party_prebattle_customized_deployment, ":array_end"),
				    (party_slot_eq, "p_main_party_backup", ":upgrade_array", 0),
				    (party_set_slot, "p_main_party_backup", ":upgrade_array", ":upgrade_troop"),
			        (assign, ":array_end", slot_party_prebattle_customized_deployment),
	            (try_end),
			    (assign, ":troop", ":upgrade_troop"),
			(else_try),
			    (assign, ":end", 0),
			(try_end),
		(try_end), #Upgrade Do...Loop

		#Use Upgrade and 'Downgrade' paths to calculate upgrade numbers for a continuous troop tree.
		(assign, ":end", slot_party_prebattle_customized_deployment + 7),
		(try_for_range, ":down_upgrade_array", slot_party_prebattle_customized_deployment, ":end"), 
		    (party_get_slot, ":troop", "p_main_party_backup", ":down_upgrade_array"),
			(gt, ":troop", 0),
			(troop_slot_eq, ":troop", slot_troop_prebattle_preupgrade_check, 1), #Find "Beginning" of Upgrade Path	
			
			(assign, ":begin_upgrade_tree", ":down_upgrade_array"),
			(assign, ":previous_num_upgraded", 0),
			(try_for_range_backwards, ":upgrade_array", slot_party_prebattle_customized_deployment, ":begin_upgrade_tree"),
			    (party_get_slot, ":top_troop", "p_main_party_backup", ":upgrade_array"),
				(gt, ":top_troop", 0),
				(party_count_members_of_type, ":pre_upgrade", "p_temp_party", ":top_troop"),
		        (party_count_members_of_type, ":post_upgrade", "p_main_party", ":top_troop"),
			    (store_sub, ":difference", ":post_upgrade", ":pre_upgrade"),
				(val_add, ":difference", ":previous_num_upgraded"),
                (val_max, ":difference", 0), #don't let it be negative
				(assign, ":previous_num_upgraded", ":difference"),
				
				(store_sub, ":prior_troop_slot", ":upgrade_array", 1),
				(try_begin),
			        (ge, ":prior_troop_slot", slot_party_prebattle_customized_deployment),
					(party_get_slot, ":prior_troop", "p_main_party_backup", ":prior_troop_slot"),
				(else_try),
				    (eq, ":prior_troop_slot", slot_party_prebattle_customized_deployment - 1),
					(assign, ":prior_troop", ":troop_id"),
                (try_end),
				(gt, ":prior_troop", 0),
				(troop_slot_eq, ":prior_troop", slot_troop_prebattle_preupgrade_check, 0),
			    (troop_set_slot, ":prior_troop", slot_troop_prebattle_num_upgrade, ":difference"),
				(troop_set_slot, ":top_troop", slot_troop_prebattle_preupgrade_check, 1),
			(try_end), #Upgrade Backwards Loop
			
			(troop_set_slot, ":troop_id", slot_troop_prebattle_preupgrade_check, 1),
			
			(assign, ":previous_num_upgraded", 0),
			(try_for_range, ":downgrade_array", ":begin_upgrade_tree", ":end"),
				(party_get_slot, ":bottom_troop", "p_main_party_backup", ":downgrade_array"),
				(gt, ":bottom_troop", 0),
				
				(try_begin),
				    (troop_slot_eq, ":bottom_troop", slot_troop_prebattle_preupgrade_check, 1),
					(troop_get_slot, ":previous_num_upgraded", ":bottom_troop", slot_troop_prebattle_num_upgrade),
				(else_try),
				    (troop_slot_eq, ":bottom_troop", slot_troop_prebattle_preupgrade_check, 0),				
					(party_count_members_of_type, ":pre_upgrade", "p_temp_party", ":bottom_troop"),
		            (party_count_members_of_type, ":post_upgrade", "p_main_party", ":bottom_troop"),
			        (store_sub, ":difference", ":post_upgrade", ":pre_upgrade"),
				    (val_add, ":difference", ":previous_num_upgraded"),
                    (val_max, ":difference", 0), #don't let it be negative
        			(assign, ":previous_num_upgraded", ":difference"),
			        (troop_set_slot, ":bottom_troop", slot_troop_prebattle_num_upgrade, ":difference"),
				    (troop_set_slot, ":bottom_troop", slot_troop_prebattle_preupgrade_check, 1),
                (try_end),
			(try_end), #Downgrade Loop
			(assign, ":end", slot_party_prebattle_customized_deployment), #Break Loop
		(try_end), #Locate "Beginning"/End of Upgrade Path 'Loop'
	(try_end), #Party Stack Loop
				
    (call_script, "script_party_copy", "p_main_party", "p_temp_party"), #Return party to pre-upgrade state
	
	(troop_set_slot, "trp_player", slot_troop_prebattle_first_round, 1),
	
    #REMOVE 'EXTRA' SOLDIERS FROM THE PARTY, TO ENSURE CORRECT SPAWN
	(party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
	(val_add, ":num_of_stacks", 1),
	(try_for_range_backwards, ":i", 0, ":num_of_stacks"),
		(party_stack_get_troop_id, ":troop_id", "p_main_party", ":i"),
		#(neq, ":troop_id", "trp_player"),
		(troop_get_slot, ":num_of_agents", ":troop_id", slot_troop_prebattle_first_round),
		(party_stack_get_size, ":stack_size", "p_main_party", ":i"),
		(store_sub, ":difference", ":stack_size", ":num_of_agents"),
		(gt, ":difference", 0),
	    (party_remove_members_wounded_first, "p_main_party", ":troop_id", ":difference"),
	(try_end),
    ]),
	
 (ti_after_mission_start, 0, 0, [(party_slot_eq, "p_main_party", slot_party_prebattle_customized_deployment, 1)], [
    #Add people back to the party 
	(party_get_num_companion_stacks, ":target_num_of_stacks", "p_temp_party"),
	(try_for_range, ":i", 0, ":target_num_of_stacks"),
		(party_stack_get_troop_id, ":target_stack_troop", "p_temp_party", ":i"),
		(neq, ":target_stack_troop", "trp_player"),
		(party_stack_get_size, ":target_stack_size", "p_temp_party", ":i"),
		
		(party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
		(assign, ":cur_stack_size", 0),
		(assign, ":cur_num_wounded", 0),
		(try_for_range, ":n", 0, ":num_of_stacks"),
			(party_stack_get_troop_id, ":stack_troop", "p_main_party", ":n"),
			(eq, ":stack_troop", ":target_stack_troop"),
			(party_stack_get_size, ":cur_stack_size", "p_main_party", ":n"),
			(party_stack_get_num_wounded, ":cur_num_wounded", "p_main_party", ":n"),
			(assign, ":num_of_stacks", 0),
		(try_end),
		
        (store_sub, ":difference", ":target_stack_size", ":cur_stack_size"),

		(try_begin),
		    (gt, ":difference", 0),
            (party_add_members, "p_main_party", ":target_stack_troop", ":difference"),
            (party_stack_get_num_wounded, ":target_num_wounded", "p_temp_party", ":i"),
		    (val_sub, ":target_num_wounded", ":cur_num_wounded"),
		    (gt, ":target_num_wounded", 0),
            (party_wound_members, "p_main_party", ":stack_troop", ":target_num_wounded"),
		(try_end),
		
		#Re-apply XP so troops that were ready to upgrade are still ready to upgrade
		(neg|troop_is_hero, ":target_stack_troop"),
		(troop_get_slot, ":num_to_upgrade", ":target_stack_troop", slot_troop_prebattle_num_upgrade),
		(gt, ":num_to_upgrade", 0),
		(call_script, "script_game_get_upgrade_xp", ":target_stack_troop"),
		(store_mul, ":xp_to_add", ":num_to_upgrade", reg0),
		(party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
		(try_for_range, ":n", 0, ":num_of_stacks"),
			(party_stack_get_troop_id, ":stack_troop", "p_main_party", ":n"),
			(eq, ":stack_troop", ":target_stack_troop"),
            (party_add_xp_to_stack, "p_main_party", ":n", ":xp_to_add"),
			(assign, ":num_of_stacks", 0),
		(try_end),
	(try_end), #Backup party stack loop
	(party_set_slot, "p_main_party", slot_party_prebattle_customized_deployment, 0),
    ]),
 ] + split_troop_division_triggers

prebattle_orders_triggers = [
 (0, 0.6, ti_once, [(party_slot_ge, "p_main_party", slot_party_prebattle_num_orders, 1)], [ #was ti_once, adjusted to conditions failure to work around engine problems
		(party_get_slot, ":num_of_orders", "p_main_party", slot_party_prebattle_num_orders),
		(party_set_slot, "p_main_party", slot_party_prebattle_num_orders, 0), #fix test
		(set_show_messages, 0),	 
		(assign, ":delay_count", 0),
		(assign, ":start_position", 0), #real deployment/positioning
		(try_for_range, ":i", 0, ":num_of_orders"),    
		    (store_add, ":ith_order_slot", ":i", slot_party_prebattle_order_array_begin),
            (party_get_slot, ":order_index", "p_main_party", ":ith_order_slot"),
			(ge, ":order_index", 10), 
			
			#Take 3 digit order index and get component parts: group, type, order
			(store_div, ":ith_order_group", ":order_index", 100),
			(store_mul, ":ith_order_type", ":ith_order_group", 100),
			(val_sub, ":order_index", ":ith_order_type"),
			(store_div, ":ith_order_type", ":order_index", 10),
			(store_mul, ":ith_order", ":ith_order_type", 10),
			(store_sub, ":ith_order", ":order_index", ":ith_order"),

			#Turn type and order into Native order
			(assign, ":delay_order", 0),
			(try_begin),
			    (eq, ":ith_order_type", 1), #Start Position: hold, follow, charge; mordr_ 0-2; 3=11 stand ground
				(eq, ":ith_order", 3), 
				(assign, ":ith_order", 11), #Stand Ground
			(else_try),
			    (eq, ":ith_order_type", 2), #Other movement orders: mordr_ 3-8, 
				(is_between, ":ith_order", 5, 9), #5 - 8; Forward/Back 10 Paces, Stand Closer/Spread Out
				(assign, ":delay_order", 1), #To fix bugs with these orders, and to accomodate formations
				(val_add, ":delay_count", 1), #they are delayed 1-2 seconds
			(else_try), 
			    (eq, ":ith_order_type", 3), #Native Weapon Use orders: mordr_ 9,10,12,13
				(try_begin),
				    (eq, ":ith_order", 0),
					(assign, ":ith_order", 10), #Use Any Weapon
				(else_try),
				    (eq, ":ith_order", 2),
					(assign, ":ith_order", 12), #Hold Fire
				(else_try),
				    (eq, ":ith_order", 3),
					(assign, ":ith_order", 13), #Fire at Will
				(try_end),
			(else_try),
			    (eq, ":ith_order_type", 4), #Formations
				(set_show_messages, 0),
				(assign, "$battle_phase", BP_Spawn), #real deployment/positioning
				(call_script, "script_player_attempt_formation", ":ith_order_group", ":ith_order", 0),
				(assign, ":start_position", 1), #real deployment/positioning
			(else_try),
				(is_between, ":ith_order_type", 5, 7), #5 or 6; Caba Weapon and Shield orders
				(val_add, ":delay_count", 1), #To fix bugs with these orders, they are delayed 1-2 seconds
			(else_try),
			    (eq, ":ith_order_type", 7), #Caba Skirmish
				(eq, ":ith_order", 1), #Begin Skirmish, any other value would be an error			
				(team_set_order_listener, "$fplayer_team_no", ":ith_order_group"),
				(call_script, "script_order_skirmish_begin_end", begin, "$fplayer_team_no"),
				(team_set_order_listener, "$fplayer_team_no", -1),
			(try_end),
            (try_begin),
			    (is_between, ":ith_order_type", 1, 4),
				(neq, ":delay_order", 1),
				(team_give_order, "$fplayer_team_no", ":ith_order_group", ":ith_order"),
			(try_end),			
		(try_end), #End Order Slot Loop	
        (team_set_order_listener, "$fplayer_team_no", grc_everyone), #Reset	
        (set_show_messages, 1),
		(display_message, "@Everyone, you know what to do. To your positions!", 0xFFDDDD66),
		(try_begin),
		    (eq, ":num_of_orders", 1),
			(party_get_slot, ":first_order", "p_main_party_backup", slot_party_prebattle_order_array_begin),
			(party_set_slot, "p_main_party", slot_party_prebattle_order_array_begin, ":first_order"),
			(party_set_slot, "p_main_party_backup", slot_party_prebattle_order_array_begin, 0),
		(try_end),	
        # (try_begin),
            # (eq, ":delay_count", 0),
            # (party_set_slot, "p_main_party", slot_party_prebattle_num_orders, 0),
		# (try_end),
		(try_begin),
			(eq, ":delay_count", 0), #deal with formations if no +/-10 paces orders are given
			(eq, ":start_position", 1),
			(call_script, "script_prebattle_agents_set_start_positions", "$fplayer_team_no"),
		(try_end),		
		(assign, "$battle_phase", BP_Setup), #real deployment/positioning
	]),
	
 (0, 1, ti_once, [(party_slot_ge, "p_main_party_backup", slot_party_prebattle_num_orders, 1)], [ #was ti_once, adjusted to conditions failure to work around engine problems
		#To fix bugs with Move Forward/Back 10 Paces and Caba Weapon orders
		#these orders are applied separately, after other orders
		(set_show_messages, 0),	 
		
		(party_get_slot, ":num_of_orders", "p_main_party_backup", slot_party_prebattle_num_orders), #change to _backup, fix test
		(party_set_slot, "p_main_party_backup", slot_party_prebattle_num_orders, 0), #change to _backup, fix test
		(try_for_range, ":i", 0, ":num_of_orders"),    
		    (store_add, ":ith_order_slot", ":i", slot_party_prebattle_order_array_begin),
            (party_get_slot, ":order_index", "p_main_party", ":ith_order_slot"),
			(ge, ":order_index", 10), 

			#Take 3 digit order index and get component parts: group, type, order
			(store_div, ":ith_order_group", ":order_index", 100),
			(store_mul, ":ith_order_type", ":ith_order_group", 100),
			(val_sub, ":order_index", ":ith_order_type"),
			(store_div, ":ith_order_type", ":order_index", 10),
			(this_or_next|is_between, ":ith_order_type", 5, 7), # 5 or 6; Caba Weapon and Shield orders
			(eq, ":ith_order_type", 2), #Movement Orders
			(store_mul, ":ith_order", ":ith_order_type", 10),
			(store_sub, ":ith_order", ":order_index", ":ith_order"),
			
			(try_begin), 
                (eq, ":ith_order_type", 2),	 #set slots for execution below		
                (is_between, ":ith_order", 5, 9), #5 - 8; Forward/Back 10 Paces, Stand Closer/Spread Out	
			    # (store_add, ":slot", slot_team_d0_formation, ":ith_order_group"),
				# (team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
				(store_add, ":ith_repeat_slot", ":ith_order_slot", 70), #30 for partial version
			    (party_get_slot, ":num_repeats", "p_main_party", ":ith_repeat_slot"),
			    (val_max, ":num_repeats", 1),
			    #(try_for_range, ":unused", 0, ":num_repeats"),
				(try_begin),
					# (set_show_messages, 0),	
					# (team_give_order, "$fplayer_team_no", ":ith_order_group", ":ith_order"),
				    # (team_set_order_listener, "$fplayer_team_no", ":ith_order_group"),
				    # (call_script, "script_player_order_formations", ":ith_order"),
				    # (team_set_order_listener, "$fplayer_team_no", -1), #Reset					
					(is_between, ":ith_order", 5, 7), #+/-10 paces
					# (store_add, ":slot", slot_team_d0_move_order, ":ith_order_group"),
					# (team_get_slot, ":prev_order", "$fplayer_team_no", ":slot"),	
					# (team_set_slot, "$fplayer_team_no", ":slot", ":ith_order"),	
											
					# (try_begin),
						# (store_add, ":slot", slot_team_d0_formation, ":ith_order_group"),
						# (neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
						(call_script, "script_formation_current_position", pos63, "$fplayer_team_no", ":ith_order_group"),
					# (else_try),
						# (agent_get_position, pos63, "$fplayer_agent_no"),
						# (call_script, "script_get_formation_destination", pos0, "$fplayer_team_no", ":ith_order_group"),
						# (position_copy_rotation, pos63, pos0),
					# (try_end),
					(call_script, "script_set_formation_destination", "$fplayer_team_no", ":ith_order_group", pos63),
					(try_begin),
						(eq, ":ith_order", mordr_advance),
						(assign, ":ith_order", 1),
					(else_try),
						(assign, ":ith_order", -1),
					(try_end),
					(val_mul, ":ith_order", ":num_repeats"),
					(call_script, "script_formation_move_position", "$fplayer_team_no", ":ith_order_group", pos63, ":ith_order"),
				(else_try), #Closer/spread out
					(store_add, ":slot", slot_team_d0_formation_space, ":ith_order_group"),
					(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
					(try_begin),
						(eq, ":ith_order", mordr_stand_closer),
						(val_mul, ":num_repeats", -1),
					(try_end),
					(val_add, ":div_spacing", ":num_repeats"),
					(val_clamp, ":div_spacing", -3, 2), #Native formations go down to four ranks, and at most 2 spread out
					(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
			    (try_end),
			(else_try),
			    (is_between, ":ith_order_type", 5, 7), #5 or 6; Caba Weapon and Shield orders
				(team_set_order_listener, "$fplayer_team_no", ":ith_order_group"),
				(call_script, "script_order_weapon_type_switch", ":ith_order", "$fplayer_team_no"),
				(team_set_order_listener, "$fplayer_team_no", -1), #Reset
			(try_end),	
		(try_end),		
        (team_set_order_listener, "$fplayer_team_no", grc_everyone), #Reset			
        		
		#place player divisions -- use the formation system to set agents' scripted_destination (hopefully this works)
		(set_fixed_point_multiplier, 100),
		(call_script, "script_team_get_position_of_enemies", Enemy_Team_Pos, "$fplayer_team_no", grc_everyone),
		(try_for_range, ":division", 0, 9),
			(store_add, ":slot", slot_team_d0_size, ":division"),
			(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
			(gt, ":troop_count", 0),
			#(store_add, ":slot", slot_team_d0_formation, ":division"),
			#(team_get_slot, ":fformation", "$fplayer_team_no", ":slot"),
			#(eq, ":fformation", formation_none),
			(team_get_order_position, Target_Pos, "$fplayer_team_no", ":division"),
			(position_get_x, reg0, Target_Pos),
			(convert_from_fixed_point, reg0),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(this_or_next|neq, reg0, 20), #some reason the initial order position is always (20, 20); if this isn't the position there should be a +/-10 order
			(neq, ":div_spacing", 0), #theres a stand closer/spread out order
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":fformation", "$fplayer_team_no", ":slot"),
			(try_begin),
			    (eq, ":fformation", formation_none),
				(eq, reg0, 20), #correct order position from (20,20) for spacing-only fixes
				(call_script, "script_formation_current_position", Target_Pos, "$fplayer_team_no", ":division"),
			(try_end),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(team_get_slot, ":sd_type", "$fplayer_team_no", ":slot"),
			(call_script, "script_point_y_toward_position", Target_Pos, Enemy_Team_Pos),
			(call_script, "script_set_formation_destination", "$fplayer_team_no", ":division", Target_Pos),
			(try_begin),
				(eq, ":fformation", formation_none),
				(val_add, ":div_spacing", formation_start_spread_out),
				(lt, ":div_spacing", 0), #ordered stand_closer at least once
				(assign, ":fformation", formation_ranks),
				(assign, ":sd_type", sdt_archer), #so uses archer stagger
				# (val_add, ":div_spacing", 1),
			# (else_try),
				# (val_max, ":div_spacing", 1), #at least 1 (for horses on top of one another, etc)
			(try_end),
			(call_script, "script_get_centering_amount", ":fformation", ":troop_count", ":div_spacing"),
			(try_begin), #to force a line
                (this_or_next|eq, ":fformation", formation_none),
				(eq, ":sd_type", sdt_archer),
				(val_mul, reg0, -1), #centering amount
				(assign, ":script", "script_form_archers"),
			(else_try), #taking care of pre-battled ordered wedge formations
				(eq, ":fformation", formation_wedge),
				(assign, ":script", "script_form_cavalry"),
			(else_try), # told to stand_closer at least once
				(assign, ":script", "script_form_infantry"),
			(try_end),
			(position_move_x, Target_Pos, reg0),
			(copy_position, pos1, Target_Pos),
			(assign, "$battle_phase", BP_Spawn), #real deployment/positioning
			(call_script, ":script", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":fformation"),		
			
			#for post-positioning business, so the spread out/stand closer orders apply in the re-arranging
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(neq, ":div_spacing", 0),
			(assign, ":start", 0),
			(assign, ":end", 0),
			(try_begin),
				(lt, ":div_spacing", 0),
				(assign, ":start", ":div_spacing"),
			(else_try),
				(assign, ":end", ":div_spacing"),
			(try_end),
			(try_for_range, ":unused", ":start", ":end"),
				(lt, ":div_spacing", 0),
				(team_give_order, "$fplayer_team_no", ":division", mordr_stand_closer),
			(else_try),
				(team_give_order, "$fplayer_team_no", ":division", mordr_spread_out),
			(try_end),		
		(try_end), #division loop
		(call_script, "script_prebattle_agents_set_start_positions", "$fplayer_team_no"), #set position based on scripted destination
		(assign, "$battle_phase", BP_Setup), #real deployment/positioning
		
		(set_show_messages, 1),
	]),
 ] + real_deployment_triggers

caba_order_triggers = [
	(ti_before_mission_start, 0, 0, [], [
		(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(party_set_slot, "p_main_party_backup", slot_party_gk_order, 0),
		(party_set_slot, 2, slot_party_gk_order_hold_over_there, 0),
		
		(try_for_range, ":team", 0, 4),
			(try_for_range, ":i", slot_team_d0_order_weapon, slot_team_d0_order_shield + 9),
				(team_set_slot, ":team", ":i", clear),
			(try_end),
		(try_end),	
	]),
#-----------------------------------------------------------------
#Descripcion: Detecta la clase seleccionada o orden de formacion		
    (0, 0, 0, [
        (this_or_next|game_key_clicked, gk_group0_hear),
        (this_or_next|game_key_clicked, gk_group1_hear),
        (this_or_next|game_key_clicked, gk_group2_hear),
        (this_or_next|game_key_clicked, gk_group3_hear),
        (this_or_next|game_key_clicked, gk_group4_hear),
        (this_or_next|game_key_clicked, gk_group5_hear),
        (this_or_next|game_key_clicked, gk_group6_hear),
        (this_or_next|game_key_clicked, gk_group7_hear),
        (this_or_next|game_key_clicked, gk_group8_hear),
        (this_or_next|game_key_clicked, gk_everyone_hear),
		(this_or_next|game_key_clicked, gk_reverse_order_group), 
		(game_key_clicked, gk_everyone_around_hear),
		(neg|main_hero_fallen)
	], 
	
   [
   
   (get_player_agent_no,":player"),
   (agent_is_alive, ":player"),
   
   (neq, "$character_gender",tf_female),
   (try_begin),
      (game_key_clicked, gk_group0_hear),
      (agent_play_sound, ":player", "snd_orden_infanteria"),
   (else_try),
      (game_key_clicked, gk_group1_hear),
       (agent_play_sound, ":player", "snd_orden_arqueros"),
   (else_try),
      (game_key_clicked, gk_group2_hear),
       (agent_play_sound, ":player", "snd_orden_caballeria"),
   (else_try),
      (game_key_clicked, gk_group3_hear),
       (agent_play_sound, ":player", "snd_orden_todos"),	  
   (else_try),
      (game_key_clicked, gk_group4_hear),
       (agent_play_sound, ":player", "snd_orden_todos"),	  
   (else_try),
      (game_key_clicked, gk_group5_hear),
       (agent_play_sound, ":player", "snd_orden_todos"),	  
   (else_try),
      (game_key_clicked, gk_group6_hear),
       (agent_play_sound, ":player", "snd_orden_todos"),	  
   (else_try),
      (game_key_clicked, gk_group7_hear),
       (agent_play_sound, ":player", "snd_orden_todos"),	  
   (else_try),
      (game_key_clicked, gk_group8_hear),
       (agent_play_sound, ":player", "snd_orden_todos"),	  
   (else_try),
      (game_key_clicked, gk_everyone_hear),
       (agent_play_sound, ":player", "snd_orden_todos"),
   (else_try),
      (game_key_clicked, gk_reverse_order_group),
       (agent_play_sound, ":player", "snd_orden_todos"),
   (else_try),
      (game_key_clicked, gk_everyone_around_hear),
       (agent_play_sound, ":player", "snd_orden_todos"),
#   (else_try),
#      (key_clicked, key_f8),
#      (try_begin),
#         (eq, "$tecla_f8", 1),
#         (agent_play_sound, ":player", "snd_orden_seguidme"),
#      (else_try),
#         (agent_play_sound, ":player", "snd_orden_posicion"),
      (try_end),
   (try_end),
    ],
 #fin hispania 1200 ordenes/voces
#-----------------------------------------------------------------	
	 [
		(party_set_slot, "p_main_party", slot_party_gk_order, 0),
        (start_presentation, "prsnt_caba_order_display"),
    ]),
	
	#(ti_escape_pressed, 0, 0, [],          [(party_set_slot, "p_main_party", slot_party_gk_order, 0),(is_presentation_active, "prsnt_caba_order_display"),(presentation_set_duration, 0)]),
	(0, 0, 0, [(this_or_next|key_clicked, "$key_order_9"),(key_clicked, key_escape)], [(party_set_slot, "p_main_party", slot_party_gk_order, 0),(is_presentation_active, "prsnt_caba_order_display"),(presentation_set_duration, 0)]),
		
	(0, 0, 0, [(game_key_clicked, gk_order_1),(neg|main_hero_fallen)], [
		(store_mission_timer_c_msec, "$when_f1_first_detected"), #CABA?
		(try_begin),
			(neg|party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_1),
			(neg|party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_2),
			(neg|party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_3),
			(party_set_slot, "p_main_party", slot_party_gk_order, gk_order_1),
			(party_set_slot, 2, slot_party_gk_order_hold_over_there, 0), #also "holdit"
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_1),	#HOLD		
			(party_set_slot, 2, slot_party_gk_order_hold_over_there, 1), #as "holdit"
			#(call_script, "script_player_order_formations", mordr_hold),
			#(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_2),	#ADVANCE
			(call_script, "script_player_order_formations", mordr_advance),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_3),	#HOLD FIRE
			(call_script, "script_order_volley_begin_end", end, "$fplayer_team_no"),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(try_end),
	]),
	
	(0, 0, 0, [(game_key_clicked, gk_order_2),(neg|main_hero_fallen)], [
		(try_begin),
			(neg|party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_1),
			(neg|party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_2),
			(neg|party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_3),
			(party_set_slot, "p_main_party", slot_party_gk_order, gk_order_2),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_1),	#FOLLOW
			(call_script, "script_player_order_formations", mordr_follow),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_2),	#FALL BACK
			(call_script, "script_player_order_formations", mordr_fall_back),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_3),	#FIRE AT WILL
			(call_script, "script_order_volley_begin_end", end, "$fplayer_team_no"),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(try_end),
	]),
	
	(0, 0, 0, [(game_key_clicked, gk_order_3),(neg|main_hero_fallen)], [
		(try_begin),
			(neg|party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_1),
			(neg|party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_2),
			(neg|party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_3),
			(party_set_slot, "p_main_party", slot_party_gk_order, gk_order_3),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_1),	#CHARGE
			(call_script, "script_player_order_formations", mordr_charge),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_2),	#SPREAD OUT
			(call_script, "script_player_order_formations", mordr_spread_out),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_3),	#BLUNT WEAPONS
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(try_end),
	]),
	
	(0, 0, 0, [(game_key_clicked, gk_order_4),(neg|main_hero_fallen)], [
		(try_begin),
			(party_slot_eq, "p_main_party", slot_party_gk_order, 0),
			(this_or_next|eq, "$g_next_menu", "mnu_simple_encounter"), #mst_lead_charge
			(eq, "$g_next_menu", "mnu_join_battle"),
			(party_set_slot, "p_main_party", slot_party_gk_order, gk_order_4),
            (start_presentation, "prsnt_caba_order_display"),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_1),	#STAND GROUND
			(call_script, "script_player_order_formations", mordr_stand_ground),			
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_2),	#STAND CLOSER
			(call_script, "script_player_order_formations", mordr_stand_closer),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_3),	#ANY WEAPON
			(call_script, "script_order_set_display_text", clear),
			(call_script, "script_order_set_team_slot", clear, "$fplayer_team_no"),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_4),	#FORMATION - RANKS	
			(call_script, "script_division_reset_places"), ## CABA - check this new script
			(agent_get_position, pos49, "$fplayer_agent_no"),
			(try_for_range, ":division", 0, 9),
			    (class_is_listening_order, "$fplayer_team_no", ":division"),
				(store_add, ":slot", slot_team_d0_target_team, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", -1),
				(store_add, ":slot", slot_team_d0_size, ":division"),
				(team_slot_ge, "$fplayer_team_no", ":slot", 1),
				(store_add, ":slot", slot_team_d0_fclock, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", 1),
				
				#Fake out at position
				(call_script, "script_battlegroup_get_position", Temp_Pos, "$fplayer_team_no", ":division"),
				(agent_set_position, "$fplayer_agent_no", Temp_Pos),
				(call_script, "script_player_attempt_formation", ":division", formation_ranks, 1),				
			(try_end),
			(agent_set_position, "$fplayer_agent_no", pos49),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, "$key_order_7"),	#End Special Order
			(call_script, "script_order_end_active_order", "$fplayer_team_no"),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),  
		(try_end),
	]),
	
	(0, 0, 0, [(game_key_clicked, gk_order_5),(neg|main_hero_fallen)], [
		(try_begin),
			(party_slot_eq, "p_main_party", slot_party_gk_order, 0),
			(party_set_slot, "p_main_party", slot_party_gk_order, gk_order_5),
            (start_presentation, "prsnt_caba_order_display"),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_1),	#RETREAT
			(call_script, "script_player_order_formations", mordr_retreat),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_2),	#MOUNT
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
		    (party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_4), #FORMATION - SHIELDWALL
			(call_script, "script_division_reset_places"),
			(agent_get_position, pos49, "$fplayer_agent_no"),
			(try_for_range, ":division", 0, 9),
			    (class_is_listening_order, "$fplayer_team_no", ":division"),
				(store_add, ":slot", slot_team_d0_target_team, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", -1),
				(store_add, ":slot", slot_team_d0_size, ":division"),
				(team_slot_ge, "$fplayer_team_no", ":slot", 1),
				(store_add, ":slot", slot_team_d0_fclock, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", 1),
				
				#Fake out at position
				(call_script, "script_battlegroup_get_position", Temp_Pos, "$fplayer_team_no", ":division"),
				(agent_set_position, "$fplayer_agent_no", Temp_Pos),
				(call_script, "script_player_attempt_formation", ":division", formation_shield, 1),				
			(try_end),
			(agent_set_position, "$fplayer_agent_no", pos49),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_5),	#One-Hander
			(call_script, "script_order_set_display_text", onehand),
			(call_script, "script_order_weapon_type_switch", onehand, "$fplayer_team_no"),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),		
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_6),	#Shield
			(call_script, "script_order_set_display_text", shield),
			(call_script, "script_order_weapon_type_switch", shield, "$fplayer_team_no"),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, "$key_order_7"),	#Begin Skirmish
			(call_script, "script_order_set_display_text", begin + 8),
			(call_script, "script_order_skirmish_begin_end", begin, "$fplayer_team_no"),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),    
		(try_end),
	]),
	
	(0, 0, 0, [(game_key_clicked, gk_order_6),(neg|main_hero_fallen)], [
	    (try_begin),
			(party_slot_eq, "p_main_party", slot_party_gk_order, 0),
			(party_set_slot, "p_main_party", slot_party_gk_order, gk_order_6),
            (start_presentation, "prsnt_caba_order_display"),
		(else_try),
		    (party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_2),	#DISMOUNT
		    (call_script, "script_player_order_formations", mordr_dismount),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_4), #FORMATION - WEDGE
			(call_script, "script_division_reset_places"),
			(agent_get_position, pos49, "$fplayer_agent_no"),
			(try_for_range, ":division", 0, 9),
			    (class_is_listening_order, "$fplayer_team_no", ":division"),
				(store_add, ":slot", slot_team_d0_target_team, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", -1),
				(store_add, ":slot", slot_team_d0_size, ":division"),
				(team_slot_ge, "$fplayer_team_no", ":slot", 1),
				(store_add, ":slot", slot_team_d0_fclock, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", 1),
				
				#Fake out at position
				(call_script, "script_battlegroup_get_position", Temp_Pos, "$fplayer_team_no", ":division"),
				(agent_set_position, "$fplayer_agent_no", Temp_Pos),
				(call_script, "script_player_attempt_formation", ":division", formation_wedge, 1),				
			(try_end),
			(agent_set_position, "$fplayer_agent_no", pos49),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_5),	#Two-Handers
			(call_script, "script_order_set_display_text", twohands),
			(call_script, "script_order_weapon_type_switch", twohands, "$fplayer_team_no"),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_6),	#No Shield
			(call_script, "script_order_set_display_text", noshield),
			(call_script, "script_order_weapon_type_switch", noshield, "$fplayer_team_no"),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, "$key_order_7"),	#Volley
			(call_script, "script_order_set_display_text", begin + 10),
			(call_script, "script_order_volley_begin_end", begin, "$fplayer_team_no"),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),    
		(try_end),
	]),

    (0, 0, 0, [(key_clicked, "$key_order_7"),(neg|main_hero_fallen)], [ #f7
	    (try_begin),
		    (party_slot_eq, "p_main_party", slot_party_gk_order, 0), 
		    (party_set_slot, "p_main_party", slot_party_gk_order, "$key_order_7"),
            (start_presentation, "prsnt_caba_order_display"),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_4), #FORMATION - SQUARE
			(call_script, "script_division_reset_places"),
			(agent_get_position, pos49, "$fplayer_agent_no"),
			(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
				(store_add, ":slot", slot_team_d0_target_team, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", -1),
				(store_add, ":slot", slot_team_d0_size, ":division"),
				(team_slot_ge, "$fplayer_team_no", ":slot", 1),
				(store_add, ":slot", slot_team_d0_fclock, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", 1),
				
				#Fake out at position
				(call_script, "script_battlegroup_get_position", Temp_Pos, "$fplayer_team_no", ":division"),
				(agent_set_position, "$fplayer_agent_no", Temp_Pos),
				(call_script, "script_player_attempt_formation", ":division", formation_square, 1),				
			(try_end),
			(agent_set_position, "$fplayer_agent_no", pos49),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_5),	#Polearms
			(call_script, "script_order_set_display_text", polearm),
			(call_script, "script_order_weapon_type_switch", polearm, "$fplayer_team_no"),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_6),	#Free Shield
			(call_script, "script_order_set_display_text", free),
			(call_script, "script_order_set_team_slot", free, "$fplayer_team_no"),
			#(call_script, "script_order_weapon_type_switch", free, "$fplayer_team_no"),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, "$key_order_7"),	#Brace Spear
			(call_script, "script_order_set_display_text", begin + 12),
			(call_script, "script_order_sp_brace_begin_end", begin, "$fplayer_team_no"),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),  
		(try_end),
	]),
		
    (0, 0, 0, [(key_clicked, "$key_order_8"),(neg|main_hero_fallen)], [ #F8
	    (try_begin),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_4), #FORMATION - CANCEL
			(call_script, "script_player_order_formations", mordr_charge),
			(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_5),
			(call_script, "script_order_set_display_text", ranged),
		    (call_script, "script_order_weapon_type_switch", ranged, "$fplayer_team_no"),
		    (party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(try_end),
	]),
 ]
 
field_ai_triggers = [
  init_scene_boundaries,
#  (ti_on_agent_spawn, 0, 0, [], [(store_trigger_param_1, ":agent"),(call_script, "script_weapon_use_classify_agent", ":agent")]), # On spawn, mark lancers, spears, horse archers using a slot. Force lancers to equip lances, horse archers to equip bows 
#  (2, 0, 0, [(this_or_next|party_slot_eq, "p_main_party", slot_party_pref_wu_lance, 1),(this_or_next|party_slot_eq, "p_main_party", slot_party_pref_wu_harcher, 1),(party_slot_eq, "p_main_party", slot_party_pref_wu_spear, 1),(store_mission_timer_a, reg0),(gt, reg0, 4)],
   # Check to make sure there are no lance users on foot, if so force them to
   # switch to their sword. This should also affect troops that were NEVER mounted,
   # but are still equipped with lances, such as Taiga Bandits.
   # Check horse archers ammo, and if none left, switch to sword.
   # For mounted lancers and foot spears, affect their Decision on weapon use,
   # based on if closest 3 enemies are within 5 meters and if currently attacking/defending.
#   [  	   
#	(try_for_agents, ":agent"), # Run through all active NPCs on the battle field.
     # Hasn't been defeated.
#        (agent_is_alive, ":agent"),
#		(agent_is_non_player, ":agent"),
#		(assign, ":caba_weapon_order", clear), # For Caba'drin Orders
#		(assign, ":shield_order", clear), # For Caba'drin Orders
#		(assign, ":weapon_order", 0),
#		(assign, ":fire_order", 0),
#		(try_begin),
#		    (agent_get_team, ":team", ":agent"),
#			(eq, ":team", "$fplayer_team_no"),
#			(agent_get_division, ":class", ":agent"),
#			(team_get_weapon_usage_order, ":weapon_order", ":team", ":class"),
#			(team_get_hold_fire_order, ":fire_order", ":team", ":class"),

#			(store_add, ":slot", slot_team_d0_order_weapon, ":class"),
#			(team_get_slot, ":caba_weapon_order", ":team", ":slot"),
#			(store_add, ":slot", slot_team_d0_order_shield, ":class"),
#			(team_get_slot, ":shield_order", ":team", ":slot"),
#		(try_end),
#		(neq, ":weapon_order", wordr_use_blunt_weapons), #Not ordered to use blunts
#		(eq, ":caba_weapon_order", clear), # For Caba'drin orders; no active weapon order
#        (try_begin),
#			(party_slot_eq, "p_main_party", slot_party_pref_wu_lance, 1),
#            (agent_get_slot, ":lance", ":agent", slot_agent_lance),
#            (gt, ":lance", 0),  # Lancer?
     # Get wielded item.
#            (agent_get_wielded_item, ":wielded", ":agent", 0),
      # They riding a horse?
#            (agent_get_horse, ":horse", ":agent"),
#            (try_begin),
#                (le, ":horse", 0), # Isn't riding a horse.
#                (agent_set_slot, ":agent", slot_agent_lance, 0), # No longer a lancer
#                (eq, ":wielded", ":lance"), # Still using lance?
#				(try_begin),
#				    (eq, ":shield_order", 1),
#					(assign, ":inc_two_handers", 0),
#				(else_try),
#				    (assign, ":inc_two_handers", 1),
#				(try_end),
#                (call_script, "script_weapon_use_backup_weapon", ":agent", ":inc_two_handers"), # Then equip a close weapon
#            (else_try),
     # Still mounted
#                (agent_get_position, pos1, ":agent"),    
#                (call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team", pos1),
#                (assign, ":avg_dist", reg0), # Find distance of nearest 3 enemies
				#SHOULD CLOSEST MATTER???
#                (try_begin),
#                    (lt, ":avg_dist", 500), # Are the enemies within 5 meters?
#                    (agent_get_combat_state, ":combat", ":agent"),
#                    (gt, ":combat", 3), # Agent currently in combat? ...avoids switching before contact
#                    (eq, ":wielded", ":lance"), # Still using lance?
#					(try_begin),
#				        (eq, ":shield_order", 1),
#					    (assign, ":inc_two_handers", 0),
#				    (else_try),
#				        (assign, ":inc_two_handers", 1),
#				    (try_end),
#                    (call_script, "script_weapon_use_backup_weapon", ":agent", ":inc_two_handers"), # Then equip a close weapon
#                (else_try),
#                    (neq, ":wielded", ":lance"), # Enemies farther than 5 meters and/or not fighting, and not using lance?
#                    (agent_set_wielded_item, ":agent", ":lance"), # Then equip it!
#                (try_end),
#            (try_end),
#        (else_try),
#			(party_slot_eq, "p_main_party", slot_party_pref_wu_harcher, 1),
#		    (agent_get_slot, ":bow", ":agent", slot_agent_horsebow),
#            (gt, ":bow", 0),  # Horse archer?
#			(neq, ":fire_order", aordr_hold_your_fire), #Not ordered to hold fire
     # Get wielded item.
#            (agent_get_wielded_item, ":wielded", ":agent", 0),
      # They have ammo left?
#            (agent_get_ammo, ":ammo", ":agent"),
#            (try_begin),
#			    (le, ":ammo", 0), # No ammo left
#				(agent_set_slot, ":agent", slot_agent_horsebow, 0), # No longer a horse archer
#                (eq, ":wielded", ":bow"), # Still using bow?
#				(try_begin),
#				    (eq, ":shield_order", 1),
#					(assign, ":inc_two_handers", 0),
#				(else_try),
#				    (assign, ":inc_two_handers", 1),
#				(try_end),
#                (call_script, "script_weapon_use_backup_weapon", ":agent", ":inc_two_handers"), # Then equip a close weapon
#			(else_try),
#			    (gt, ":ammo", 0),
#				(agent_get_horse, ":horse", ":agent"),
#				(le, ":horse", 0), #No Horse, no command, let AI choose (I think)
#			(else_try),
#                (gt, ":ammo", 0),
#				(neq, ":wielded", ":bow"), # Still have ammo, still mounted and not using bow?
#                (agent_set_wielded_item, ":agent", ":bow"), # Then equip it!
#			(try_end),
#		(else_try),
#		    (party_slot_eq, "p_main_party", slot_party_pref_wu_spear, 1),
#		    (agent_get_slot, ":spear", ":agent", slot_agent_spear),   
#            (gt, ":spear", 0), # Spear-Unit?   

#			(store_add, ":slot", slot_team_d0_formation, ":class"),
#			(team_slot_eq, ":team", ":slot", formation_none),			
#			(neq, ":shield_order", 1),
			
#            (agent_get_position, pos1, ":agent"), # Find distance of nearest 3 enemies
#            (call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team", pos1),
#            (assign, ":avg_dist", reg0),
#            (assign, ":closest_dist", reg1),
#			(agent_get_wielded_item, ":wielded", ":agent", 0), # Get wielded
#            (try_begin), #Weapon Use
#                (this_or_next|lt, ":closest_dist", 300), # Closest enemy within 3 meters?
#                (lt, ":avg_dist", 700), # Are the 3 enemies within an average of 7 meters?
#                (agent_get_combat_state, ":combat", ":agent"),
#                (gt, ":combat", 3), # Agent currently in combat? ...avoids switching before contact
#                (eq, ":wielded", ":spear"), # Still using spear?
#                (call_script, "script_weapon_use_backup_weapon", ":agent", 1), # Then equip a close weapon
#            (else_try),
#                (neq, ":wielded", ":spear"), # Enemies farther than 7 meters and/or not fighting, and not using spear?
#                (agent_set_wielded_item, ":agent", ":spear"), # Then equip it!                
#            (try_end),
#        (try_end),
#    (try_end),
#    ]),
	
  (ti_on_agent_hit, 0, 0, [(party_slot_eq, "p_main_party", slot_party_pref_dmg_tweaks, 1)],
    # Horse Trample buff  
    # Pike vs Horse buff
   [
    (store_trigger_param_1, ":agent"),
	(store_trigger_param_2, ":attacker"),
	(store_trigger_param_3, ":damage"),
	(assign, ":weapon", reg0),
	
	(assign, ":orig_damage", ":damage"),
	
	(try_begin),
	    (agent_is_human, ":agent"), 
		#(agent_is_non_player, ":agent"), #Maybe remove?
	    (try_begin), #Horse Trample Buff
		    (neg|agent_is_human, ":attacker"),
            (eq, ":weapon", -1),
            (agent_get_item_id, ":horse", ":attacker"),
			(ge, ":horse", 0),
			(gt, ":orig_damage", 5),
			(item_get_slot, ":horse_charge", ":horse", slot_item_horse_charge), #Approximation for weight
            (try_begin),      
                (lt, ":horse_charge", 18),
				(val_div, ":horse_charge", 3),
                (val_max, ":damage", ":horse_charge"),
            (else_try),
                (is_between, ":horse_charge", 18, 25),
				(val_div, ":horse_charge", 2),
                (val_max, ":damage", ":horse_charge"),      
            (else_try),
                (val_max, ":damage", ":horse_charge"),
            (try_end),
			(try_begin),
				(agent_get_speed, pos0, ":attacker"),
				(position_get_y, ":forward_speed", pos0),
				(position_get_x, ":lateral_speed", pos0), #Double check
				(val_max, ":forward_speed", ":lateral_speed"), #Double check
				(convert_from_fixed_point, ":forward_speed"),
				(gt, ":forward_speed", 6),
				(val_mul, ":damage", 2),
			(try_end),
        (try_end),
	(else_try), #Pike Buff
	    (neg|agent_is_human, ":agent"),
		(gt, ":weapon", 0),
		(item_slot_ge, ":weapon", slot_item_length, 150),
		(agent_get_horse, ":horse", ":attacker"),
		(eq, ":horse", -1),
					
		(try_begin),
		    (agent_get_action_dir, ":direction", ":attacker"), #invalid = -1, down = 0, right = 1, left = 2, up = 3
		    (eq, ":direction", 0), #thrust	
			(val_mul, ":damage", 2),
    		(val_max, ":damage", 50), #was 120
		(else_try),
			(val_mul, ":damage", 3),
			(val_div, ":damage", 2),
		    (val_max, ":damage", 30), #was 60
		(try_end),
		(val_max, ":damage", ":orig_damage"),

		(agent_get_speed, pos0, ":agent"),
		(position_get_y, ":forward_speed", pos0),
		(position_get_x, ":lateral_speed", pos0), #Double check
		(val_max, ":forward_speed", ":lateral_speed"), #Double check
		(convert_from_fixed_point, ":forward_speed"),
		(val_sub, ":forward_speed", 3),
		(val_clamp, ":forward_speed", -2, 4),
		(store_mul, ":speed_mod", ":forward_speed", 10), #Between -20 and +40
		(val_add, ":damage", ":speed_mod"),		

		(agent_get_item_id, ":horse", ":agent"), #New Armor damage reduction
		(item_get_slot, ":armor", ":horse", slot_item_horse_armor),
		(val_div, ":armor", 4), #Range of 2-14
		(val_sub, ":damage", ":armor"),
		
		#Horses randomly rear if they take damage
		(store_random_in_range, ":random_no", 0, 100),
		(try_begin),
		    (store_div, ":chance_mod", ":orig_damage", 5),
			(val_sub, ":random_no", ":chance_mod"),
			(val_sub, ":random_no", ":forward_speed"),
			(try_begin),
			    (gt, ":orig_damage", 5),
				(eq, ":direction", 0),
				(val_sub, ":random_no", 10),
			(try_end),
			(lt, ":random_no", 10),
			(agent_set_animation, ":agent", "anim_horse_rear"),
		(try_end),	
	(try_end), #Human v Horse
	
	(gt, ":damage", ":orig_damage"),
	(val_sub, ":damage", ":orig_damage"),
    (store_agent_hit_points, ":hitpoints" , ":agent", 1),
    (val_sub, ":hitpoints", ":damage"),
	(agent_set_hit_points, ":agent", ":hitpoints", 1),	
	
	(assign, reg2, -1),
	(agent_get_horse,":playerhorse","$fplayer_agent_no"),
	(try_begin),
		(try_begin),
	        (eq, ":agent", ":playerhorse"),
			(assign, reg2, 0),
		(else_try),
		    (eq, ":agent", "$fplayer_agent_no"),
			(assign, reg2, 1),
		(try_end),
		(neq, reg2, -1),
	    (assign, reg1, ":damage"),		
	    (display_message, "@{reg2?You:Your mount} received {reg1} extra damage!",0xff4040),
    (else_try),
	    (try_begin),
		    (eq, ":attacker", ":playerhorse"),
			(assign, reg2, 0),
		(else_try),
		    (eq, ":attacker", "$fplayer_agent_no"),
			(assign, reg2, 1),
		(try_end),
		(neq, reg2, -1),
		(assign, reg1, ":damage"),	
		(display_message, "@{reg2?You strike:Your horse charges} for {reg1} bonus damage!"),
    (try_end),
   ]),	
  
  (ti_on_agent_dismount, 0, 0, [(party_get_slot, reg3, "p_main_party", slot_party_pref_div_dehorse),(is_between, reg3, 0, 9)], #De-Horse Trigger #Valid division 0-8
   [
	(store_trigger_param_2, ":horse"),
	(neg|agent_is_alive, ":horse"),
	
	(store_trigger_param_1, ":rider"), 
	(agent_is_alive, ":rider"),
    (agent_is_non_player, ":rider"),
	
	(agent_get_team, ":team", ":rider"),
	
	(try_begin),
	    (eq, ":team", "$fplayer_team_no"),
		(agent_set_division, ":rider", reg3),
		(agent_set_slot, ":rider", slot_agent_new_division, reg3),
	(else_try),
	    (agent_set_division, ":rider", grc_infantry),
		(agent_set_slot, ":rider", slot_agent_new_division, grc_infantry),
	(try_end),
   ]),

  (ti_on_item_unwielded, 0, 0, [(party_get_slot, reg3, "p_main_party", slot_party_pref_div_no_ammo),(is_between, reg3, 0, 9)], #Out of Ammo Trigger #Valid division 0-8
   [
    (store_trigger_param_2, ":weapon"),
	(ge, ":weapon", 0),
	(item_get_type, ":type", ":weapon"),
	(this_or_next|eq, ":type", itp_type_bow),
	(eq, ":type", itp_type_crossbow),
	
	(store_trigger_param_1, ":agent"),
    (agent_is_alive, ":agent"),
    (agent_is_non_player, ":agent"),
	
	(agent_get_ammo, ":ammo", ":agent", 0),
	(le, ":ammo", 0),	
	(agent_get_horse, ":horse", ":agent"),
	(eq, ":horse", -1),
	
	(agent_get_team, ":team", ":agent"),
	(assign, ":continue", 1),
	(try_begin),
		(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town), #Sieges
		(party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),		
		(this_or_next|eq, ":team", "$defender_team"),
		(eq, ":team", "$defender_team_2"),
		(assign, ":continue", 0), #To not reassign units that will get their ammo refilled.
	(try_end),
	(eq, ":continue", 1),	
	
	(try_begin),
	    (eq, ":team", "$fplayer_team_no"),
		(agent_set_division, ":agent", reg3),
		(agent_set_slot, ":agent", slot_agent_new_division, reg3),
	(else_try),
	    (agent_set_division, ":agent", grc_infantry),
		(agent_set_slot, ":agent", slot_agent_new_division, grc_infantry),
	(try_end),  
   ]),
   
  (2, 0, ti_once, [(store_mission_timer_a, reg0),(gt, reg0, 2)], [ #Force Cav to Stay Mounted
    (set_show_messages, 0),   
    (try_for_range, ":team", 0, 4),
	    #(neq, ":team", "$fplayer_team_no"),		
		(try_for_range, ":division", 0, 9),
		    (store_add, ":slot", slot_team_d0_type, ":division"),
			(this_or_next|team_slot_eq, ":team", ":slot", sdt_cavalry),
			(team_slot_eq, ":team", ":slot", sdt_harcher),
			(team_give_order, ":team", ":division", mordr_mount),
		(try_end),		
	(try_end),
	(set_show_messages, 1),
   ]),
  
  (1, 0, 0, [(party_slot_eq, "p_main_party", slot_party_pref_spear_brace, 1),(store_mission_timer_a, reg0),(gt, reg0, 2)], [ ###GENERAL AI TRIGGER for SPECIAL ORDERS 
		(set_fixed_point_multiplier, 100),
		(try_for_range, ":division", 0, 9), #Player auto-remove brace
			(store_add, ":slot", slot_team_d0_order_sp_brace, ":division"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", 0), #brace active
			(call_script, "script_formation_current_position", pos2, "$fplayer_team_no", ":division"),
			(call_script, "script_get_nearest_enemy_battlegroup_current_position", pos1, "$fplayer_team_no", pos2),
			(this_or_next|lt, reg0, 325), #distance
			(position_is_behind_position,pos1,pos2),
			(team_set_order_listener, "$fplayer_team_no", ":division"),
			(call_script, "script_order_sp_brace_begin_end", end, "$fplayer_team_no"),
			(team_set_order_listener, "$fplayer_team_no", -1),
		(try_end),
	    (try_for_range, ":team", 0, 4), #For AI
			(neq, ":team", "$fplayer_team_no"),
			(team_slot_ge, ":team", slot_team_size, 1),
			(assign, ":mordr", -1),
			(team_get_slot, ":faction", ":team", slot_team_faction),
			(this_or_next|eq, ":faction", "fac_deserters"),
			(is_between, ":faction", kingdoms_begin, kingdoms_end),
			(try_begin), #Spear Bracing Decision-making
				(this_or_next|eq, ":faction", "fac_player_supporters_faction"), #Player's lords can brace
				(eq, ":faction", "fac_kingdom_5"), #Rhodoks	
				(try_begin),
					(team_slot_eq, ":team", slot_team_d0_order_sp_brace, 0), #Spearbrace order not active
					(store_add, ":slot", slot_team_d0_size, grc_infantry), 
					(team_slot_ge, ":team", slot_team_d0_size, 10),
					(store_add, ":slot", slot_team_d0_weapon_length, grc_infantry),
					(team_slot_ge, ":team", ":slot", 80), #have long weapons/polearms (until bumped to a separate division)
					(store_add, ":slot", slot_team_d0_formation, grc_infantry),
					(team_get_movement_order, ":mordr", ":team", grc_infantry),
					(this_or_next|neg|team_slot_eq, ":team", ":slot", formation_none),
					(neq, ":mordr", mordr_charge), #Not Charging	
					(assign, ":num_cav", 0),
					(try_for_range, ":enemy_team", 0, 4),
						(teams_are_enemies, ":enemy_team", ":team"),
						(team_slot_ge, ":enemy_team", slot_team_size, 1),
						(team_get_slot, reg0, ":enemy_team", slot_team_num_cavalry), 
						(val_add, ":num_cav", reg0),
					(try_end),		
					(ge, ":num_cav", 5), #sufficent enemy cav to care
					(assign, ":distance", 99999),
					(call_script, "script_formation_current_position", pos2, ":team", grc_infantry),
					(call_script, "script_team_get_position_of_enemies", pos1, ":team", grc_cavalry),
					(get_distance_between_positions, ":distance", pos1, pos2),
					(is_between, ":distance", 1500, 5000), #cav distance
					(call_script, "script_get_nearest_enemy_battlegroup_current_position", pos1, ":team", pos2),
					(gt, reg0, 600), #nearest distance
					(neg|position_is_behind_position,pos1,pos2),
					(team_set_order_listener, ":team", grc_infantry),
					(call_script, "script_order_sp_brace_begin_end", begin, ":team"),
					(team_set_order_listener, ":team", -1),
				(else_try), #Should only capture an eligible team that is now charging, so bracing should turn off
					(neg|team_slot_eq, ":team", slot_team_d0_order_sp_brace, 0), #Order Active
					(assign, ":end", 0),
					(try_begin),
						(assign, ":num_cav", 0),
						(try_for_range, ":enemy_team", 0, 4),
							(teams_are_enemies, ":enemy_team", ":team"),
							(team_slot_ge, ":enemy_team", slot_team_size, 1),
							(team_get_slot, reg0, ":enemy_team", slot_team_num_cavalry), 
							(val_add, ":num_cav", reg0),
						(try_end),		
						(team_get_movement_order, ":mordr", ":team", grc_infantry),
						(this_or_next|eq, ":mordr", mordr_charge),
						(lt, ":num_cav", 5),
						(assign, ":end", 1),
					(else_try),
						(store_add, ":slot", slot_team_d0_size, grc_infantry), 
						(neg|team_slot_ge, ":team", slot_team_d0_size, 10),
						(assign, ":end", 1),
					(else_try),
						(store_add, ":slot", slot_team_d0_weapon_length, grc_infantry),
						(neg|team_slot_ge, ":team", ":slot", 80), #have long weapons/polearms (until bumped to a separate division)
						(assign, ":end", 1),
					(else_try),
						(assign, ":distance", 0),
						(call_script, "script_formation_current_position", pos2, ":team", grc_infantry),
						(call_script, "script_team_get_position_of_enemies", pos1, ":team", grc_cavalry),
						(get_distance_between_positions, ":distance", pos1, pos2),
						(gt, ":distance", 6500),
						(assign, ":end", 1),
					(else_try), #after contact, end brace
						(call_script, "script_get_nearest_enemy_battlegroup_current_position", pos1, ":team", pos2),
						(this_or_next|lt, reg0, 350), #distance
						(position_is_behind_position,pos1,pos2),
						(assign, ":end", 1),
					(try_end),
					(eq, ":end", 1),
					(team_set_order_listener, ":team", grc_infantry),
					(call_script, "script_order_sp_brace_begin_end", end, ":team"),
					(team_set_order_listener, ":team", -1),
				(try_end),
			(try_end), #End Spear Bracing
			(try_begin), #Volley/Skirmish Decision Making
				(neq, ":faction", "fac_kingdom_1"), #Swadia
				(neq, ":faction", "fac_kingdom_5"), #Rhodoks...Exclude Cross-bow users
				(try_begin),
					(store_add, ":slot", slot_team_d0_order_skirmish, grc_archers),
					(neg|team_slot_eq, ":team", ":slot", 1), #not skirmishing
					(team_get_slot, ":num_archers", ":team", slot_team_num_archers),
					(team_get_slot, ":size", ":team", slot_team_size),
					(store_mul, reg0, ":num_archers", 100),
					(val_div, reg0, ":size"),
					(is_between, reg0, 25, 76), #25-75% archers
					(assign, ":num_enemies", 0),
					(try_for_range, ":enemy_team", 0, 4),
						(teams_are_enemies, ":enemy_team", ":team"),
						(team_get_slot, reg0, ":enemy_team", slot_team_size), 
						(val_add, ":num_enemies", reg0),
					(try_end),		
					(lt, ":num_archers", ":num_enemies"),
					(team_set_order_listener, ":team", grc_archers),
					(call_script, "script_order_skirmish_begin_end", begin, ":team"),
					(team_set_order_listener, ":team", -1),
				(else_try),
					(store_add, ":slot", slot_team_d0_order_skirmish, grc_archers),
					(team_slot_eq, ":team", ":slot", 1), #skirmishing
					(team_get_slot, ":num_archers", ":team", slot_team_num_archers),
					(assign, ":num_enemies", 0),
					(try_for_range, ":enemy_team", 0, 4),
						(teams_are_enemies, ":enemy_team", ":team"),
						(team_get_slot, reg0, ":enemy_team", slot_team_size), 
						(val_add, ":num_enemies", reg0),
					(try_end),	
					(gt, ":num_archers", ":num_enemies"),
					(team_set_order_listener, ":team", grc_archers),
					(call_script, "script_order_skirmish_begin_end", end, ":team"),
					(team_set_order_listener, ":team", -1),
				(try_end),
			(else_try),
				(this_or_next|eq, ":faction", "fac_kingdom_1"), #Swadia
				(eq, ":faction", "fac_kingdom_5"), #Rhodoks... Cross-bow users
				(assign, ":distance", 99999),
				(try_begin),
					(store_add, ":slot", slot_team_d0_order_volley, grc_archers),
					(neg|team_slot_ge, ":team", ":slot", 1), #Not Volleying
					(team_get_slot, reg1, ":team", slot_team_num_archers),
					(team_get_slot, ":size", ":team", slot_team_size),
					(val_mul, reg1, 100),
					(val_div, reg1, ":size"),
					(gt, reg1, 25), #>25% archers
					(team_get_movement_order, ":mordr", ":team", grc_archers),
					(neq, ":mordr", mordr_charge),	
					(call_script, "script_battlegroup_get_position", pos2, ":team", grc_archers),
					(call_script, "script_get_nearest_enemy_battlegroup_location", Temp_Pos, ":team", pos2),					
					(is_between, reg0, 1000, 7000),
					(team_set_order_listener, ":team", grc_archers),
					(call_script, "script_order_volley_begin_end", begin, ":team"),
					(team_set_order_listener, ":team", -1),
				(else_try),
					(store_add, ":slot", slot_team_d0_order_volley, grc_archers),
					(team_slot_ge, ":team", ":slot", 1),
					(assign, ":end", 0),
					(try_begin),
						(team_get_movement_order, ":mordr", ":team", grc_archers),
						(eq, ":mordr", mordr_charge),	
						(assign, ":end", 1),
					(else_try),
						(call_script, "script_battlegroup_get_position", pos2, ":team", grc_archers),
					    (call_script, "script_get_nearest_enemy_battlegroup_location", Temp_Pos, ":team", pos2),
						(neg|is_between, reg0, 1000, 8000),
						(assign, ":end", 1),
					(try_end),					
					(eq, ":end", 1),
					(team_set_order_listener, ":team", grc_archers),
					(call_script, "script_order_volley_begin_end", end, ":team"),
					(team_set_order_listener, ":team", -1),
				(try_end),
			(try_end), #End Skirmish/Volley
		(try_end), #Team Loop
    ]),
      
  (0.5, 0, 0, [(call_script, "script_cf_order_active_check", slot_team_d0_order_skirmish)], [(call_script, "script_order_skirmish_skirmish")]), 
 
  (1, 0, 0, [(call_script, "script_cf_order_active_check", slot_team_d0_order_volley)], [
		(try_begin), #Disable Volley @ end of battle 
			(neq, "$g_battle_result", 0),
			(try_for_range, ":team", 0, 4),
				(try_for_range, ":slot", slot_team_d0_order_volley, slot_team_d0_order_volley + 9),
					(team_set_slot, ":team", ":slot", 0),
				(try_end),
			(try_end),
		(try_end),
		
		(try_for_range, ":team", 0, 4),
			(try_for_range, ":division", 0, 9),
			    (store_add, ":slot", slot_team_d0_order_volley, ":division"),
				(team_slot_ge, ":team", ":slot", 1),
				(team_get_slot, ":volley_counter", ":team", ":slot"),
				(val_add, ":volley_counter", 1),
				(team_set_slot, ":team", ":slot", ":volley_counter"),
			(try_end),
		(try_end),
		
		(try_for_agents, ":agent"),
		    (agent_is_alive, ":agent"),
			(agent_is_non_player, ":agent"),
			(agent_slot_ge, ":agent", slot_agent_volley_fire, 1),
			(agent_get_ammo, ":ammo", ":agent", 1),
			(gt, ":ammo", 0),
			
			(agent_get_team, ":team", ":agent"),
			(agent_get_division, ":division", ":agent"),
			(store_add, ":slot", slot_team_d0_order_volley, ":division"),
			(team_get_slot, ":volley_counter", ":team", ":slot"),
			
			(agent_get_slot, ":volley_wpn_type", ":agent", slot_agent_volley_fire),
			(try_begin),
				(eq, ":volley_wpn_type", itp_type_bow),
				(assign, ":delay", 2),
			(else_try),
				(eq, ":volley_wpn_type", itp_type_crossbow),
				(assign, ":delay", 5),
			(try_end),
			(agent_get_combat_state, ":cs", ":agent"),
			#(assign, reg0, ":cs"),
			#(display_message, "str_reg0"),
			#(lt, ":cs", 4),
			#(neq, ":cs", 2),
			(this_or_next|eq, ":cs", 1),
			(eq, ":cs", 3),
						
			(store_mod, reg0, ":volley_counter", ":delay"),		
			(try_begin),
				(eq, reg0, 0),
				(agent_set_attack_action, ":agent", 0, 0), #Fire
			(else_try),
				(agent_set_attack_action, ":agent", 0, 1), #Ready and Aim
			(try_end),
		(try_end),
     ]),
 
  (0, 0, 3, [(key_clicked, "$key_special_1")], [   #call_horse_trigger
      (agent_get_slot, ":horse", "$fplayer_agent_no", slot_agent_horse),
      (gt, ":horse", 0),
      (agent_is_active, ":horse"), 
	  (agent_get_horse, reg0, "$fplayer_agent_no"),
	  (eq, reg0, -1), ##be sure player isn't currently mounted
      #(agent_play_sound, "$fplayer_agent_no", "snd_whistle"), #Floris
	  (agent_play_sound, "$fplayer_agent_no", "snd_silbido"),  #Native
      (display_message,"@You whistle for your horse."),
      (agent_is_alive,":horse"),
      (agent_get_position, pos1, "$fplayer_agent_no"),
      (agent_set_scripted_destination, ":horse", pos1, 0),
     ]),
   
  ##Spearwall Kit - Edited from The Mercenary by Caba'drin  
  (0.1, 0, 0, [(call_script, "script_cf_order_active_check", slot_team_d0_order_sp_brace)], [ #spearwall_trigger_1
		(try_for_agents,":agent"),
           (agent_is_alive,":agent"),
           (agent_is_human,":agent"),
		   (agent_slot_eq, ":agent", slot_agent_is_running_away, 0),
		   (agent_slot_ge, ":agent", slot_agent_spear, 1),
		   (agent_get_wielded_item, ":weapon", ":agent", 0),
           (agent_slot_eq, ":agent", slot_agent_spear, ":weapon"),
		   (agent_get_team,":team1",":agent"),
           (agent_get_division,":class",":agent"),
		   (team_get_movement_order,":order",":team1",":class"),
		   (assign,":continue",0),
           (try_begin),
		      (neq, ":agent", "$fplayer_agent_no"),
		      (store_add, ":slot", slot_team_d0_order_sp_brace, ":class"),
			  (team_slot_eq, ":team1", ":slot", 1),
			  (this_or_next|eq,":order",mordr_hold),
              (eq,":order",mordr_stand_ground),
			  (assign, ":continue", 1),
		   (else_try),
              (eq, ":agent", "$fplayer_agent_no"), 
              (agent_slot_eq, "$fplayer_agent_no", slot_agent_player_braced, 1),
              (assign, ":continue", 1),
		   (try_end),
		   (eq, ":continue", 1),
		   (agent_get_speed, pos0, ":agent"), #New
		   (position_get_y, ":speed", pos0),
		   (position_get_x, ":speed_x", pos0),
		   (val_max, ":speed", ":speed_x"),
		   #(assign, reg0, ":speed"),
		   #(display_message, "@Speed: {reg0}"),
		   (eq, ":speed", 0),
		   (try_begin),
				(agent_get_animation, ":anim", ":agent"),				
				#Try block for proper animation--high, low, standing; w or w/o shield (hopefully?)
				(try_begin),
				    (item_slot_eq, ":weapon", slot_item_pike, 1),
					(assign, ":anim_bracing", "anim_spearwall_bracing_low"),
				(else_try),
				    (assign, ":anim_bracing", "anim_spearwall_bracing"),
				(try_end),
				(neq, ":anim", ":anim_bracing"),
				(agent_set_animation, ":agent", ":anim_bracing"),
				(agent_get_position, pos1, ":agent"), ##lessens some spinning
				(agent_set_scripted_destination, ":agent", pos1), ##lessens some spinning
				(agent_get_look_position, pos1, ":agent"),
				(position_get_x, ":x", pos1),
				(position_get_y, ":y", pos1),
				(agent_set_slot, ":agent", slot_agent_target_x_pos, ":x"),
				(agent_set_slot, ":agent", slot_agent_target_y_pos, ":y"),
				(agent_set_slot, ":agent", slot_agent_spearwall, 0), #Begin count with animation resetting
		   (try_end),
		   #(eq, ":continue", 1),
		   (agent_get_slot,":speartimer",":agent",slot_agent_spearwall),
           (try_begin),
                (lt,":speartimer",20),
                (val_add,":speartimer",1),
                (agent_set_slot,":agent",slot_agent_spearwall,":speartimer"),
           (try_end),
		   (agent_set_is_alarmed, ":agent", 0), ##lessens some spinning
		   (agent_get_slot, ":x", ":agent", slot_agent_target_x_pos),
		   (agent_get_slot, ":y", ":agent", slot_agent_target_y_pos),
		   (init_position, pos2),
		   (position_set_x, pos2, ":x"),
		   (position_set_y, pos2, ":y"),
		   (agent_set_look_target_position, ":agent", pos2),
           (ge,":speartimer",20),
		   (item_get_slot, ":spear_dist", ":weapon", slot_item_length), #CABA
           (assign, ":dist_to_beat", ":spear_dist"),
           (assign,":victim",-1),
		   (assign, ":vic_rider", -1),
           (agent_get_position,pos1,":agent"),
           (try_for_agents,":possible_victim"),
              (agent_is_alive,":possible_victim"),
              (neg|agent_is_human,":possible_victim"),
              (agent_get_rider,":rider",":possible_victim"),
              (ge,":rider",0),
              (agent_get_team,":team2",":rider"),
              (teams_are_enemies,":team1",":team2"),
              (agent_get_position,pos2,":possible_victim"),
              (get_distance_between_positions,":dist",pos1,pos2),
              (lt,":dist",":dist_to_beat"), #CABA
              (neg|position_is_behind_position,pos2,pos1),
			  (get_angle_between_positions, ":angle", pos1, pos2), #CABA
			  (val_abs, ":angle"), #CABA
			  (convert_from_fixed_point, ":angle"), #CABA
              (is_between, ":angle", 165, 181),  #30 degrees... have to be facing one another
			  #(position_transform_position_to_local, pos2, pos1, pos2),
			  #(position_get_x, ":x", pos2),
			  #(position_get_y, ":y", pos2),
			  #(val_abs, ":x"),
			  #(store_atan2, ":angle", ":x", ":y"), #first value is y, second is x - so say header_operations. not so
			  #(convert_from_fixed_point, ":angle"), #CABA
			  # (assign, reg0, ":angle"),
		      # (display_message, "str_reg0"),			  
			  #(is_between, ":angle", 0, 21), #40 degree field...perhaps more appropriate for that distance			  			  
			  (agent_get_speed, pos0, ":possible_victim"), #CABA
              (position_get_y, ":speed", pos0), #CABA
			  (position_get_x, ":speed_x", pos0), #CABA - just be be sure
			  (val_max, ":speed", ":speed_x"), #CABA - just to be sure
              (ge, ":speed", 300), #CABA at least half speed; full speed horse 800-1100, was 400
              (assign, ":dist_to_beat", ":dist"), #CABA ...now it will progressively find the closest target
              (assign,":victim",":possible_victim"), #CABA
			  (assign,":vic_rider", ":rider"),
           (try_end),
           (gt,":victim",-1),
		   (display_message, "@Brace should hit"),
           (agent_set_animation, ":agent", "anim_spearwall_bracing_recoil"),
		   (agent_set_slot, ":agent", slot_agent_spearwall, 0),
           (agent_play_sound,":victim","snd_metal_hit_high_armor_high_damage"),
           (store_agent_hit_points,":hp",":victim",0), #This stores as a %
           (store_agent_hit_points,":oldhp",":victim",1), #This stores as absoulte # - Pre-Damage
           (val_div,":speed",6), # Orig 2; Remember to change this if the timing on speed checks changes
           (val_sub,":speed",10), #CABA - w/speed div by 8-10, a speed over 900 will be an instant-kill. Might want to change divisor to 10?
           (try_begin), #Pike Bonus Damage
		      (item_slot_eq, ":weapon", slot_item_pike, 1),
			  (val_add, ":speed", 5),
			  (gt, ":spear_dist", 200),
			  (val_add, ":speed", 5),
		   (try_end),
		   # (assign, reg0, ":speed"),
		   # (display_message, "str_reg0"),
		   (val_sub,":hp",":speed"),
           (val_max,":hp", 0),
           (agent_set_hit_points, ":victim", ":hp", 0), #NEW HP% = Previous HP% - (Speed/8)
           (agent_deliver_damage_to_agent,":victim",":victim"), ##CHANGE TO THE AGENT DEALING DAMAGE? Probably not to avoid double pike-buff
           (store_agent_hit_points,":hp",":victim",1), #Post-Damage HP 
		   (try_begin), ## REAR or RIDER DAMAGE
		       (gt, ":hp", 0), #IF THE HORSE IS STILL ALIVE, base 50% chance of rearing
			   (store_random_in_range, ":random_no", 0, 100),
			   (try_begin), #Pike bonus block
				  (item_slot_eq, ":weapon", slot_item_pike, 1),
				  (val_sub, ":random_no", 10), #"Pike" with 60% chance
				  (gt, ":spear_dist", 200),
				  (val_sub, ":random_no", 10), #Longest Pikes with 70% chance
			   (try_end),
			   (lt, ":random_no", 50),
			   (agent_set_animation, ":victim", "anim_horse_rear"),
		   (else_try), #Horse Killed, so damage rider on fall
		       (le, ":hp", 0),
		       # #(agent_set_no_dynamics, ":victim", 1), #0 = turn dynamics off, 1 = turn dynamics on (required for cut-scenes)    ????
			   # (agent_get_position, pos2, ":victim"),
			   # (position_move_y, pos2, -100), #back 1m
			   # (agent_set_position, ":victim", pos2), #above here, trying to prevent horse forward momentum too much...nothing works
			   (store_random_in_range, ":random_no", 40, 75), #Rider should loose 1/4 - 3/5 of HP
			   (store_agent_hit_points, ":rider_hp", ":vic_rider", 0),
			   (val_min, ":random_no", ":rider_hp"),
			   (agent_set_hit_points, ":vic_rider", ":random_no", 0),
		   (try_end),
		   (try_begin),
              (agent_get_horse,":playerhorse","$fplayer_agent_no"),
              (eq,":victim",":playerhorse"),         
              (val_sub,":oldhp",":hp"),
              (assign,reg1,":oldhp"),
              (display_message,"@Your horse received {reg1} damage from a braced spear!",0xff4040),
           (else_try),
              (eq, ":agent", "$fplayer_agent_no"),
              (val_sub,":oldhp",":hp"),
              (assign,reg1,":oldhp"),
              (str_store_item_name, s1, ":weapon"),
              (display_message,"@Braced {s1} dealt {reg1} damage!"),
              (agent_set_slot, "$fplayer_agent_no", slot_agent_player_braced, 0),
           (try_end),
        (try_end),
    ]),

  (0, 0, 2, [(key_clicked, "$key_special_0"),(agent_is_alive,"$fplayer_agent_no"),(neg|agent_slot_eq, "$fplayer_agent_no", slot_agent_player_braced, 1)], #spearwall_trigger_2
       [
      	(agent_get_horse, reg0, "$fplayer_agent_no"),
		(eq, reg0, -1), ##be sure player isn't currently mounted
        (agent_get_wielded_item, ":weapon", "$fplayer_agent_no", 0), #CABA
        (assign, ":valid_weapon", 0), #CABA
        (try_begin), #CABA-whole block
            (agent_slot_ge, "$fplayer_agent_no", slot_agent_spear, 1),
            (agent_slot_eq, "$fplayer_agent_no", slot_agent_spear, ":weapon"),
            (assign, ":valid_weapon", 1),
        (else_try),
            (ge, ":weapon", 0),
            (item_get_type, ":wpn_type", ":weapon"),
            (eq, ":wpn_type", itp_type_polearm),
            (agent_set_slot, "$fplayer_agent_no", slot_agent_spear, ":weapon"),
            (assign, ":valid_weapon", 1),
        (try_end),
        (eq, ":valid_weapon", 1),       
		(str_store_item_name, s1, ":weapon"), #CABA
        (display_message,"@Bracing {s1} for charge.",0x6495ed),
        #(agent_set_animation, "$fplayer_agent_no", "anim_spearwall_hold"),
        (agent_set_slot, "$fplayer_agent_no", slot_agent_player_braced, 1), #CABA
    ]),
       
  (0, 0, 0, [(this_or_next|game_key_clicked, gk_attack),(this_or_next|game_key_clicked, gk_defend), #spearwall_trigger_3
        (this_or_next|game_key_clicked, gk_move_forward),(this_or_next|game_key_clicked, gk_move_backward),
        (this_or_next|game_key_clicked, gk_move_left),(this_or_next|game_key_clicked, gk_move_right),
        (this_or_next|game_key_clicked, gk_equip_primary_weapon),(this_or_next|game_key_clicked, gk_equip_secondary_weapon),
        (this_or_next|game_key_clicked, gk_action),(game_key_clicked, gk_sheath_weapon),
		(agent_is_alive,"$fplayer_agent_no"),(neg|agent_slot_eq, "$fplayer_agent_no", slot_agent_player_braced, 0),
        ],
       [
#        (display_message,"@Releasing from brace.",0x6495ed),
        #(agent_set_animation, "$fplayer_agent_no", "anim_release_thrust_staff"),
#		(agent_set_animation, "$fplayer_agent_no", "anim_spearwall_bracing_recoil"),
        (agent_set_slot, "$fplayer_agent_no", slot_agent_player_braced, 0), #CABA
    ]), 
  ##Spearwall Kit - Edited from The Mercenary by Caba'drin
 ] 

bodyguard_triggers = [
 (ti_after_mission_start, 0, 0, [(party_slot_eq, "p_main_party", slot_party_pref_bodyguard, 1),(neq, "$g_mt_mode", tcm_disguised)], #condition for not sneaking in; to exclude prison-breaks, etc change to (eq, "$g_mt_mode", tcm_default")
   [
    #Get number of bodyguards
    (store_skill_level, ":leadership", "skl_leadership", "trp_player"),
    (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
    (val_div, ":leadership", 3),
    (val_div, ":renown", 400),
    (store_add, ":max_guards", ":renown", ":leadership"),
    (val_min, ":max_guards", 4),
   
    (ge, ":max_guards", 1),
	
	#Prepare Scene/Mission Template
	(assign, ":entry_point", 0),
	(assign, ":mission_tpl", 0),
	(try_begin),		
		(party_slot_eq, "$current_town", slot_party_type, spt_village),
		(assign, ":entry_point", 11), #Village Elder's Entry
		(assign, ":mission_tpl", "mt_village_center"),
	(else_try),
		(this_or_next|eq, "$talk_context", tc_prison_break),
		(this_or_next|eq, "$talk_context", tc_escape),
		(eq, "$talk_context", tc_town_talk),
		(assign, ":entry_point", 24), #Prison Guard's Entry
		(try_begin),
			(party_slot_eq, "$current_town", slot_party_type, spt_castle),
			(assign, ":mission_tpl", "mt_castle_visit"),
		(else_try),
			(assign, ":mission_tpl", "mt_town_center"),
		(try_end),
	(else_try),
		(eq, "$talk_context", tc_tavern_talk),
		(assign, ":entry_point", 17), #First NPC Tavern Entry
	(try_end),
	(try_begin),
		(neq, "$talk_context", tc_tavern_talk),
		(agent_slot_ge, "$fplayer_agent_no", slot_agent_horse, 1), #If the player spawns with a horse, the bodyguard will too.
		(mission_tpl_entry_set_override_flags, ":mission_tpl", ":entry_point", 0),
	(try_end),	
	(store_current_scene, ":cur_scene"),
	(modify_visitors_at_site, ":cur_scene"),  
   
    #Find and Spawn Bodyguards
    (assign, ":bodyguard_count", 0),   
    (party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
    (try_for_range, ":i", 0, ":num_of_stacks"),
        (party_stack_get_troop_id, ":troop_id", "p_main_party", ":i"),
        (neq, ":troop_id", "trp_player"),
        (troop_is_hero, ":troop_id"),
        (neg|troop_is_wounded, ":troop_id"),
        (val_add, ":bodyguard_count", 1),
				
		(try_begin), #For prison-breaks
		    (this_or_next|eq, "$talk_context", tc_escape),
            (eq, "$talk_context", tc_prison_break),	  
            (troop_set_slot, ":troop_id", slot_troop_will_join_prison_break, 1),
		(try_end),

        (add_visitors_to_current_scene, ":entry_point", ":troop_id", 1),

        (eq, ":bodyguard_count", ":max_guards"),
        (assign, ":num_of_stacks", 0), #Break Loop       
    (try_end), #Stack Loop
    (gt, ":bodyguard_count", 0), #If bodyguards spawned...
    (set_show_messages, 0),   
    (team_give_order, "$fplayer_team_no", 8, mordr_follow), #Division 8 to avoid potential conflicts
	(team_set_order_listener, "$fplayer_team_no", 8),
    (set_show_messages, 1),   
   ]),   

 (ti_on_agent_spawn, 0, 0, [(party_slot_eq, "p_main_party", slot_party_pref_bodyguard, 1)], 
   [
	(store_trigger_param_1, ":agent"),
	(agent_get_troop_id, ":troop", ":agent"),
	(neq, ":troop", "trp_player"),
	(troop_is_hero, ":troop"),
	(main_party_has_troop, ":troop"),
	
	(get_player_agent_no, ":player"),
	(ge, ":player", 0),
	(agent_get_team, ":player_team", ":player"),
	
	(agent_get_position,pos1,":player"),		
	
	(agent_set_team, ":agent", ":player_team"),
	(agent_set_division, ":agent", 8),
	(agent_add_relation_with_agent, ":agent", ":player", 1),
	(agent_set_is_alarmed, ":agent", 1),
	(store_random_in_range, ":shift", 1, 3),
	(val_mul, ":shift", 100),
	(position_move_y, pos1, ":shift"),
	(store_random_in_range, ":shift", 1, 3),
	(store_random_in_range, ":shift_2", 0, 2),
	(val_mul, ":shift_2", -1),
	(try_begin),
		(neq, ":shift_2", 0),
		(val_mul, ":shift", ":shift_2"),
	(try_end),
	(position_move_x, pos1, ":shift"),
	(agent_set_position, ":agent", pos1),
   ]),
  
 (ti_on_agent_killed_or_wounded, 0, 0, [(party_slot_eq, "p_main_party", slot_party_pref_bodyguard, 1)],
    [
     (store_trigger_param_1, ":dead_agent"),
        
     (agent_get_troop_id, ":troop", ":dead_agent"),
	 (neq, ":troop", "trp_player"),
	 (troop_is_hero, ":troop"),
	 (main_party_has_troop, ":troop"),
	 (neg|troop_is_wounded, ":troop"),
	 (party_wound_members, "p_main_party", ":troop", 1),
	]),
 ]
  
custom_camera_triggers = [  
 init_player_global_variables,
 # CUSTOM CAMERA - dunde (Rubik, MartinF) + DEATH CAMERA - MadVader  + Combination and reworking by Caba
 (0, 0, ti_once, [(get_player_agent_no, "$cam_current_agent"), (gt, "$cam_current_agent", -1)], #camera_init
    [ (assign,"$cam_mode", cam_mode_default),(assign, "$cam_free", -1), #cam_free was 0; -1 not free; 0 custom/movement free; 1 all agent cycle free		   
	  #(assign, "$g_camera_z", 300),(assign, "$g_camera_y", -1000),(assign, "$g_camera_x", 0),	  
	  #(assign, "$deathcam_on", 0),(assign, "$shoot_mode",0), 			
	  (assign, "$pin_player_fallen", 0),
      # mouse center coordinates (non-windowed)
      (assign, "$camera_mouse_center_x", 500),
      (assign, "$camera_mouse_center_y", 375),
      # last recorded mouse coordinates
      (assign, "$camera_mouse_x", "$camera_mouse_center_x"),
      (assign, "$camera_mouse_y", "$camera_mouse_center_y"),
      # counts how many cycles the mouse stays in the same position, to determine new center in windowed mode
      (assign, "$camera_mouse_counter", 0),
	  (neg|is_between, "$camera_mouse_deadzone", 1, 11),(assign, "$camera_mouse_deadzone", 3), #CABA Changed from a constant, former comment: set this to a positive number (MV: 2 or 3 works well for me, but needs testing on other people's PCs)
	]),
	
 ## MadVader deathcam begin
 (0, 0, 0, [(eq, "$cam_mode", cam_mode_free), #deathcam_move
      (this_or_next|key_clicked, "$key_camera_forward"),
      (this_or_next|key_is_down, "$key_camera_forward"),
      (this_or_next|key_clicked, "$key_camera_backward"),
      (this_or_next|key_is_down, "$key_camera_backward"),
      (this_or_next|key_clicked, "$key_camera_left"),
      (this_or_next|key_is_down, "$key_camera_left"),
      (this_or_next|key_clicked, "$key_camera_right"),
      (key_is_down, "$key_camera_right"),],
    [
      (mission_cam_get_position, cam_position),
      (assign, ":move_x", 0),
      (assign, ":move_y", 0),
      (try_begin), #forward
        (this_or_next|key_clicked, "$key_camera_forward"),
        (key_is_down, "$key_camera_forward"),
        (assign, ":move_y", 10),
      (try_end),
      (try_begin), #backward
        (this_or_next|key_clicked, "$key_camera_backward"),
        (key_is_down, "$key_camera_backward"),
        (assign, ":move_y", -10),
      (try_end),
      (try_begin), #left
        (this_or_next|key_clicked, "$key_camera_left"),
        (key_is_down, "$key_camera_left"),
        (assign, ":move_x", -10),
      (try_end),
      (try_begin), #right
        (this_or_next|key_clicked, "$key_camera_right"),
        (key_is_down, "$key_camera_right"),
        (assign, ":move_x", 10),
      (try_end),
      (position_move_x, cam_position, ":move_x"),
      (position_move_y, cam_position, ":move_y"),
	  (try_begin),
		(position_get_distance_to_ground_level, ":to_ground", cam_position),
		(lt, ":to_ground", 0),
		(position_set_z_to_ground_level, cam_position),
		(position_move_z, cam_position, 50),
	  (try_end),
	  (mission_cam_set_position, cam_position),   
    ]),

 (0, 0, 0, [(eq, "$cam_mode", cam_mode_free),  #deathcam_rotate
      (neg|is_presentation_active, "prsnt_battle"),
      (mouse_get_position, pos1),
      (set_fixed_point_multiplier, 1000),
      (position_get_x, reg1, pos1),
      (position_get_y, reg2, pos1),
      (this_or_next|neq, reg1, "$camera_mouse_center_x"),
      (neq, reg2, "$camera_mouse_center_y"),],
    [
      # fix for windowed mode: recenter the mouse
      (assign, ":continue", 1),
      (try_begin),
        (eq, reg1, "$camera_mouse_x"),
        (eq, reg2, "$camera_mouse_y"),
        (val_add, "$camera_mouse_counter", 1),
        (try_begin), #hackery: if the mouse hasn't moved for X cycles, recenter it
          (gt, "$camera_mouse_counter", 50),
          (assign, "$camera_mouse_center_x", reg1),
          (assign, "$camera_mouse_center_y", reg2),
          (assign, "$camera_mouse_counter", 0),
        (try_end),
        (assign, ":continue", 0),
      (try_end),
      (eq, ":continue", 1), #continue only if mouse has moved
      (assign, "$camera_mouse_counter", 0), # reset recentering hackery
     
      # update recorded mouse position
      (assign, "$camera_mouse_x", reg1),
      (assign, "$camera_mouse_y", reg2),
     
      (mission_cam_get_position, cam_position),
      (store_sub, ":shift", "$camera_mouse_center_x", reg1), #horizontal shift for pass 0
      (store_sub, ":shift_vertical", reg2, "$camera_mouse_center_y"), #for pass 1
     
      (try_for_range, ":pass", 0, 2), #pass 0: check mouse x movement (left/right), pass 1: check mouse y movement (up/down)
        (try_begin),
          (eq, ":pass", 1),
          (assign, ":shift", ":shift_vertical"), #get ready for the second pass
        (try_end),
		(store_mul, ":neg_deadzone", "$camera_mouse_deadzone", -1), #Caba - this and next line altered to make variable
        (this_or_next|lt, ":shift", ":neg_deadzone"), #skip pass if not needed (mouse deadzone)
        (gt, ":shift", "$camera_mouse_deadzone"),
       
        (assign, ":sign", 1),
        (try_begin),
          (lt, ":shift", 0),
          (assign, ":sign", -1),
        (try_end),
        # square root calc
        (val_abs, ":shift"),
        (val_sub, ":shift", "$camera_mouse_deadzone"), # ":shift" is now 1 or greater
        (convert_to_fixed_point, ":shift"),
        (store_sqrt, ":shift", ":shift"),
        (convert_from_fixed_point, ":shift"),
        (val_clamp, ":shift", 1, 6), #limit rotation speed
        (val_mul, ":shift", ":sign"),
        (try_begin),
          (eq, ":pass", 0), # rotate around z (left/right)
          (store_mul, ":minusrotx", "$g_camera_rotx", -1),
          (position_rotate_x, cam_position, ":minusrotx"), #needed so camera yaw won't change
          (position_rotate_z, cam_position, ":shift"),
          (position_rotate_x, cam_position, "$g_camera_rotx"), #needed so camera yaw won't change
        (try_end),
        (try_begin),
          (eq, ":pass", 1), # rotate around x (up/down)
          (position_rotate_x, cam_position, ":shift"),
          (val_add, "$g_camera_rotx", ":shift"),
        (try_end),
      (try_end), #try_for_range ":pass"
      (mission_cam_set_position, cam_position),
    ]),
 ## MadVader deathcam end
 
 (0, 0, 0, [(eq, "$cam_mode", cam_mode_follow)], #camera_follow
   [
     (set_fixed_point_multiplier, 100),
     (agent_get_look_position, cam_position, "$cam_current_agent"),
     (position_get_rotation_around_x, ":angle", cam_position),
     (store_sub, ":reverse", 0, ":angle"),
     (position_rotate_x, cam_position, ":reverse"),
	 (try_begin),
	    (eq, "$cam_free", -1),
		(val_clamp, "$g_camera_x", -1000, 1000),
	    (val_clamp, "$g_camera_y", -1000, 1000),
		(val_min, "$g_camera_z", 1000),
	 (try_end),
     (position_move_y, cam_position, "$g_camera_y"),
     (position_move_z, cam_position, "$g_camera_z"),
	 (position_move_x, cam_position, "$g_camera_x"),
     (agent_get_horse, ":horse_agent", "$cam_current_agent"),
     (try_begin),
        (ge, ":horse_agent", 0),
        (position_move_z, cam_position, 80),       
     (try_end),
     (store_mul, ":reverse", -1, "$g_camera_y"),
     (store_atan2, ":drop", "$g_camera_z", ":reverse"),
     (convert_from_fixed_point, ":drop"),
     (val_sub, ":angle", ":drop"),
     (position_rotate_x, cam_position, ":angle"),
	 (try_begin),
		(position_get_distance_to_ground_level, ":to_ground", cam_position),
		(lt, ":to_ground", 0),
		(position_set_z_to_ground_level, cam_position),
		(position_move_z, cam_position, 50),
	 (try_end),
	 (try_begin), ##CABA - Deployment
		(eq, "$battle_phase", BP_Spawn),  ##CABA - Deployment
		(mission_cam_set_position, cam_position), ##CABA - Deployment
	 (else_try), ##CABA - Deployment
		(mission_cam_animate_to_position, cam_position, 100, 0),
	 (try_end), ##CABA - Deployment	 
  
    (try_begin), 
		(neg|main_hero_fallen),
		(this_or_next|game_key_clicked, gk_view_char),
		(game_key_clicked, gk_cam_toggle),
		(mission_cam_set_mode, 0),
		(assign, "$cam_mode", cam_mode_default),
	(try_end),
  ]),
  
 (0, 0, 0, [(key_clicked, "$key_camera_toggle"),(lt, "$cam_mode", cam_mode_shoot)], #camera_toggle
   # toggling only when came mode =0 or 1 (2=disable) ; shoot_mode=1 temporary diable toggling
   [(try_begin),
     (eq, "$cam_mode", cam_mode_default),
	 (assign, "$g_camera_z", 300),
	 (assign, "$g_camera_y", -1000),
	 (assign, "$g_camera_x", 0),
	 (assign, "$cam_mode", cam_mode_follow),
    (else_try),
     (eq, "$cam_mode", cam_mode_follow),
	 (try_begin),
	    (eq, "$cam_free", -1),
		(try_begin),
		    (neg|main_hero_fallen),
			(get_player_agent_no, "$cam_current_agent"),                 
		(try_end),
		(assign, "$cam_mode", cam_mode_default),
	 (else_try),
		(try_begin),
			(main_hero_fallen),
			(mission_cam_get_position, cam_position),
			(position_get_rotation_around_x, "$g_camera_rotx", cam_position),
		(else_try),
			(assign, "$g_camera_rotx", 0),
		(try_end),		
		(assign, "$cam_mode", cam_mode_free),
     (try_end),
    (else_try),
     (eq, "$cam_mode", cam_mode_free),
	 (try_begin),
	    (ge, "$cam_free", 0),
		(assign, "$g_camera_z", 300),
	    (assign, "$g_camera_y", -1000),
	    (assign, "$g_camera_x", 0),
		(assign, "$cam_mode", cam_mode_follow),
	 (else_try),
	    (assign, "$cam_mode", cam_mode_default),
	 (try_end),
    (try_end),
	(start_presentation, "prsnt_caba_camera_mode_display"),
    (try_begin),
      (eq, "$cam_mode", cam_mode_default),
      (mission_cam_set_mode, 0),
    (else_try),
      (mission_cam_set_mode, 1),
    (try_end),
  ]),

 (0, 0, 0, [(eq, "$cam_mode", cam_mode_follow), #camera_follow_move
      (this_or_next|key_is_down, "$key_camera_forward"),
      (this_or_next|key_is_down, "$key_camera_backward"),
      (this_or_next|key_is_down, "$key_camera_left"),
      (this_or_next|key_is_down, "$key_camera_right"),
      (this_or_next|key_is_down, "$key_camera_zoom_plus"), 
	  (this_or_next|key_is_down, "$key_camera_zoom_min"),
	  (this_or_next|key_clicked, "$key_camera_next"),
	  (this_or_next|key_clicked, "$key_camera_prev"),
	  (game_key_is_down, gk_attack),],
    [ 
	  (try_begin), #initialize shoot
		(game_key_is_down, gk_attack),
		(neg|main_hero_fallen),
		(eq, "$fplayer_agent_no","$cam_current_agent"),(agent_is_alive, "$fplayer_agent_no"),(agent_get_wielded_item,":weapon","$cam_current_agent",0),(ge, ":weapon", 0),(item_get_type, ":type", ":weapon"), (this_or_next|eq,":type",itp_type_bow),(this_or_next|eq,":type",itp_type_crossbow),(eq,":type",itp_type_thrown),
		(assign, "$cam_mode", cam_mode_shoot),
		(mission_cam_set_mode, 0),
	  (try_end),
	  (try_begin), #cycle agents
		(ge, "$cam_free", 1),
		(try_begin),
			(key_clicked, "$key_camera_next"),
			(call_script, "script_cust_cam_cycle_forwards"),
		(else_try),
			(key_clicked, "$key_camera_prev"),
			(call_script, "script_cust_cam_cycle_backwards"),
		(try_end),		
	  (try_end),
      (try_begin), #forward
        (key_is_down, "$key_camera_forward"),
        (val_add, "$g_camera_y",1),(neg|game_key_is_down, gk_zoom),(val_add, "$g_camera_y",9),
      (try_end),
      (try_begin), #backward
        (key_is_down, "$key_camera_backward"),
        (val_sub, "$g_camera_y",1),(neg|game_key_is_down, gk_zoom),(val_sub, "$g_camera_y",9),
      (try_end),
      (try_begin), #left
        (key_is_down, "$key_camera_left"),
        (val_sub, "$g_camera_x",1),(neg|game_key_is_down, gk_zoom),(val_sub, "$g_camera_x",9),
      (try_end),
      (try_begin), #right
        (key_is_down, "$key_camera_right"),
        (val_add, "$g_camera_x",1),(neg|game_key_is_down, gk_zoom),(val_add, "$g_camera_x",9),
      (try_end),
	  (try_begin), #up
        (key_is_down, "$key_camera_zoom_plus"),
        (val_add, "$g_camera_z",1),(neg|game_key_is_down, gk_zoom),(val_add, "$g_camera_z",9),
      (try_end),
      (try_begin), #down
        (key_is_down, "$key_camera_zoom_min"),
        (val_sub, "$g_camera_z",1),(neg|game_key_is_down, gk_zoom),(val_sub, "$g_camera_z",9),(val_max,"$g_camera_z", 50),
      (try_end),
    ]),
	
 (0, 0, 0,[(eq, "$cam_mode", cam_mode_shoot),(neg|game_key_is_down, gk_attack)], [(assign,"$cam_mode", cam_mode_follow),(mission_cam_set_mode, 1)]) , #camera_return_normal      
  
 ]
## Prebattle Orders & Deployment End

bc_tab_press_addon = [
		#PBOD - Battle Continuation
		(else_try),
		  (party_slot_eq, "p_main_party", slot_party_pref_bc_continue, 1), #PBOD Battle Continuation On
		  (this_or_next|main_hero_fallen),   #CABA EDIT/FIX FOR DEATH CAM
		  (eq, "$pin_player_fallen", 1),
		  (str_store_string, s5, "str_retreat"),
		  (call_script, "script_simulate_retreat", 5, 20, 0),
		  (call_script, "script_count_mission_casualties_from_agents"),
		  (set_mission_result, -1),
		  (finish_mission,0),
		#PBOD - Battle Continuation END
]

batt_continue_addon = [
	(try_begin),
	  (party_slot_eq, "p_main_party", slot_party_pref_bc_continue, 1), #PBOD Battle Continuation Active
	  (assign, ":num_allies", 0),		
	  (try_for_agents, ":agent"),
		 (agent_is_ally, ":agent"),
		 (agent_is_alive, ":agent"),
		 (val_add, ":num_allies", 1),
	  (try_end),
	  (gt, ":num_allies", 0),
	  (try_begin),
		  (neq, "$cam_free", 1),
		  (display_message, "@You have been knocked out by the enemy. Watch your men continue the fight without you or press Tab to retreat."),
		  (call_script, "script_cust_cam_init_death_cam", cam_mode_free),
		  (party_slot_eq, "p_main_party", slot_party_pref_bc_charge_ko, 1), #PBOD "Charge on KO" Active
		  (set_show_messages, 0),
		  (team_give_order, "$fplayer_team_no", grc_everyone, mordr_charge),
		  (team_set_order_listener, "$fplayer_team_no", grc_everyone),
		  (call_script, "script_player_order_formations", mordr_charge),
		  (set_show_messages, 1),
	  (try_end),
	(else_try),
]
	
from util_wrappers import *
from util_common import *

def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1143 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "mission_templates"
		orig_mission_templates = var_set[var_name_1]

		# START do your own stuff to do merging

		modmerge_mission_templates(orig_mission_templates)

		# END do your own stuff
            
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)


def modmerge_mission_templates(orig_mission_templates):
	from module_mission_templates import common_battle_tab_press, common_battle_check_victory_condition, common_battle_order_panel, common_siege_check_defeat_condition
	
	for i in range(len(orig_mission_templates)):
		mt_name = orig_mission_templates[i][0]
		##Extending trigger lists with triggers appropriate to the templates
		if( mt_name=="lead_charge" or mt_name=="village_raid" or mt_name=="village_attack_bandits"):
			orig_mission_templates[i][5].extend(common_pbod_triggers+prebattle_orders_triggers+prebattle_deployment_triggers+caba_order_triggers+field_ai_triggers+custom_camera_triggers)
		elif ("besiege" in mt_name or "castle_attack" in mt_name or mt_name=="entrenched_encounter" or mt_name=="ship_battle"):
			orig_mission_templates[i][5].extend(common_pbod_triggers+prebattle_orders_triggers+prebattle_deployment_triggers+caba_order_triggers+custom_camera_triggers)
		elif( mt_name=="town_default" or mt_name=="town_center" or mt_name=="village_center" or mt_name=="bandits_at_night" or mt_name=="castle_visit" or mt_name=="visit_entrenchment"):
			orig_mission_templates[i][5].extend(common_pbod_triggers+bodyguard_triggers+caba_order_triggers+custom_camera_triggers)
		elif( not "tutorial" in mt_name and not "multiplayer" in mt_name ):
		    #( mt_name=="alley_fight" or orig_mission_templates[i][1] & mtf_arena_fight):
			orig_mission_templates[i][5].extend(common_pbod_triggers+custom_camera_triggers)
		
		##Battle Continuation:
		trigger_i = MissionTemplateWrapper(orig_mission_templates[i]).FindTrigger_i(1,4,ti_once,[(main_hero_fallen)])
		if ( trigger_i != None ):
			trigger = orig_mission_templates[i][5][trigger_i]
			codeblock = TriggerWrapper(trigger).GetConsequenceBlock()
			pos = codeblock.FindLineMatching((assign, "$pin_player_fallen", 1))
			if (codeblock.GetLineContent(pos+1) != (try_begin) ): #hasn't yet been edited (error check for common triggers, used in sieges)
				codeblock.InsertAfter(pos, batt_continue_addon)
				codeblock.Append([(try_end)])
				if (trigger == common_siege_check_defeat_condition):
					pos = codeblock.FindLineMatching((party_slot_eq, "p_main_party", slot_party_pref_bc_charge_ko, 1))
					codeblock.RemoveAt(pos, 6) #remove "Charge on KO" lines for main siege missions
			#Change re-arm interval from ti_once to 0 (using work around to edit immutable tuple)
			orig_mission_templates[i][5][trigger_i] = list(orig_mission_templates[i][5][trigger_i])
			orig_mission_templates[i][5][trigger_i][2] = 0
			orig_mission_templates[i][5][trigger_i] = tuple(orig_mission_templates[i][5][trigger_i])
	
	##Battle Continuation, continued; editing common triggers
	try:
		codeblock = TriggerWrapper(common_battle_tab_press).GetConsequenceBlock()
		pos = codeblock.FindLineMatching((call_script, "script_cf_check_enemies_nearby"))
		codeblock.InsertBefore(pos-1, bc_tab_press_addon) #pos-1 to jump above the else try
		
		codeblock = TriggerWrapper(common_battle_check_victory_condition).GetConditionBlock()
		pos = codeblock.FindLineMatching((neg|main_hero_fallen, 0))
		codeblock.InsertBefore(pos,[(this_or_next|party_slot_eq, "p_main_party", slot_party_pref_bc_continue, 1)])
		
		codeblock = TriggerWrapper(common_battle_order_panel).GetConsequenceBlock()
		pos = codeblock.FindLineMatching((game_key_clicked, gk_view_orders))
		codeblock.InsertAfter(pos,[(neg|main_hero_fallen)])
		
	except:
		import sys
		print "Injecton 1 failed:", sys.exc_info()[1]
		raise