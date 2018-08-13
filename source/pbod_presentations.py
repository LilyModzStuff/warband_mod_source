## Prebattle Orders & Deployment by Caba'drin
## v0.92
## 20 Jan 2012

from header_common import *
from header_presentations import *
from header_operations import *
from header_triggers import *
from ID_meshes import *
from module_constants import *


## Prebattle Orders & Deployment Begin   
presentations = [
 ("prebattle_custom_deployment", 0, mesh_load_window, [
    (ti_on_presentation_load,
     [(set_fixed_point_multiplier, 1000),
	  (assign, "$g_presentation_credits_obj_1", 0),
	  
	    (party_get_slot, ":battle_size", "p_main_party", slot_party_prebattle_battle_size),	
		(set_show_messages, 0),
	  	(call_script, "script_calculate_battle_advantage"),
		(assign, ":battle_advantage", reg0),
		(set_show_messages, 1),
		(call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
		(assign, ":friend_count", reg0),	  
		(call_script, "script_party_count_members_with_full_health", "p_main_party"),
		(assign, ":num_our_regulars_remaining", reg0),		
		
		(store_mul, ":players_share", ":num_our_regulars_remaining", 100),
		(val_div, ":players_share", ":friend_count"), #This likely needs more work...it doesn't appear to be a flat %
		
		#Results below this point are x100 for 2 decimal point accuracy
		(store_sub, ":battle_size_scaled", ":battle_size", 30), #Scale battle_size to the engine used 30-150 = 0-1 scale
		(val_mul, ":battle_size_scaled", 100),
		(val_div, ":battle_size_scaled", 120),
		
		(assign, ":spawn_point_count", 12),
		(try_begin),
		    (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
		    (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
			(val_mul, ":battle_advantage", 2),
            (val_div, ":battle_advantage", 3), #scale down the advantage a bit for sieges.
			(val_add, ":spawn_point_count", 6), #For all sieges
			(eq, "$g_next_menu", "mnu_siege_started_defender"), #Siege Defense?
			(party_slot_eq, "$g_encountered_party", slot_center_siege_with_belfry, 1),
		    #(display_message, "@Siege Defense - Belfry"), #Debug
			(val_add, ":spawn_point_count", 2), #For tower defense only
		(try_end),
		(val_mul, ":spawn_point_count", 100),
		
		(store_mul, ":num_ally_in_battle", ":battle_size_scaled", 4),
		(val_add, ":num_ally_in_battle", 125),
		
		(val_add, ":battle_advantage", 15),
		(val_mul, ":battle_advantage", 100),
		(val_div, ":battle_advantage", 15),
		(val_clamp, ":battle_advantage", 20, 250),
		
		(val_mul, ":num_ally_in_battle", ":battle_advantage"),
		(val_mul, ":num_ally_in_battle", ":spawn_point_count"),
		(val_div, ":num_ally_in_battle", 1000000), #For 3 values that were multiplied by 100
		(val_add, ":num_ally_in_battle", 1), #To account for rounding
		
		(store_mul, ":num_player_troops_in_battle", ":num_ally_in_battle", ":players_share"),
		(val_div, ":num_player_troops_in_battle", 100),
		
		# (store_mul, ":batt_adv_multiplier", ":battle_size", 26),
		# (val_add, ":batt_adv_multiplier", 220),
		# (val_mul, ":batt_adv_multiplier", ":battle_advantage"),
		
		# (store_mul, ":batt_adv_multiplier", ":battle_size", 26),
		# (val_add, ":batt_adv_multiplier", 220),
		# (val_mul, ":batt_adv_multiplier", ":battle_advantage"),
		# (store_mul, ":size_offset", ":battle_size", 396),
		# (val_add, ":size_offset", 3300),
		# (store_add, ":num_ally_in_battle", ":batt_adv_multiplier", ":size_offset"),
		# (val_div, ":num_ally_in_battle", 1000),
		# (store_mul, ":num_player_troops_in_battle", ":num_ally_in_battle", ":players_share"),
		# (val_div, ":num_player_troops_in_battle", 100),
		
		# (store_mul, ":minimum_in_battle", ":battle_size", 8),
		# (val_div, ":minimum_in_battle", 100),
		# (val_add, ":minimum_in_battle", 1),
		# (store_sub, ":maximum_in_battle", ":battle_size", ":minimum_in_battle"),
		# (val_add, ":maximum_in_battle", 1),
		# (val_clamp, ":num_player_troops_in_battle", ":minimum_in_battle", ":maximum_in_battle"),
		
		(val_min, ":num_player_troops_in_battle", ":num_our_regulars_remaining"), #Make sure it doesn't say the player can spawn more than they have
		(party_set_slot, "p_main_party", slot_party_prebattle_size_in_battle, ":num_player_troops_in_battle"),

      (create_text_overlay, reg0, "@Plan Deployment", tf_center_justify|tf_single_line|tf_with_outline),
      (overlay_set_color, reg0, 0xFFFFFFFF),
      (position_set_x, pos1, 1500),
      (position_set_y, pos1, 1500),
      (overlay_set_size, reg0, pos1),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 680),
      (overlay_set_position, reg0, pos1),

	  (party_get_slot, ":round_size", "p_main_party", slot_party_prebattle_size_in_battle),
	  (assign, reg1, ":round_size"),
	  (create_text_overlay, reg0, "@You will have {reg1} troops available at the battle's start", tf_center_justify|tf_single_line),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 650),
      (overlay_set_position, reg0, pos1),
	  
      (create_text_overlay, reg0, "@Troop",  tf_center_justify),
      (position_set_x, pos1, 105),
      (position_set_y, pos1, 600),
      (overlay_set_position, reg0, pos1),

      (create_text_overlay, reg0, "@# at start  / # in party", tf_center_justify),
      (position_set_x, pos1, 385),
      (position_set_y, pos1, 600),
      (overlay_set_position, reg0, pos1),
   
      (str_clear, s0),
      (create_text_overlay, "$g_presentation_obj_bugdet_report_container", s0, tf_scrollable_style_2),
      (position_set_x, pos1, 50),
      (position_set_y, pos1, 100),
      (overlay_set_position, "$g_presentation_obj_bugdet_report_container", pos1),
      (position_set_x, pos1, 385),#was 360
      (position_set_y, pos1, 500), 
      (overlay_set_area_size, "$g_presentation_obj_bugdet_report_container", pos1),
      (set_container_overlay, "$g_presentation_obj_bugdet_report_container"),
   
   	  (assign, ":in_count", 0),
      (assign, ":cur_y_adder", 40),  
	  (party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
	  (store_mul, ":cur_y", ":num_of_stacks", ":cur_y_adder"),
	  
		(try_for_range, ":i", 0, ":num_of_stacks"),
			(party_stack_get_troop_id, ":troop_id", "p_main_party", ":i"),
			(neq, ":troop_id", "trp_player"),
			(party_stack_get_size, ":stack_size", "p_main_party", ":i"),
			(party_stack_get_num_wounded, ":stack_wounded", "p_main_party", ":i"),
			(val_sub, ":stack_size", ":stack_wounded"),
			(troop_get_slot, ":num_of_agents", ":troop_id", slot_troop_prebattle_first_round),
			(val_min, ":num_of_agents", ":stack_size"),
			(troop_set_slot, ":troop_id", slot_troop_prebattle_first_round, ":num_of_agents"),
			
            (val_add, ":in_count", ":num_of_agents"),
			
			(str_store_troop_name, s1, ":troop_id"),
			(create_text_overlay, reg0, s1),
			(position_set_x, pos1, 800),
			(position_set_y, pos1, 800),
			(overlay_set_size, reg0, pos1),
			(position_set_x, pos1, 25),
			(position_set_y, pos1, ":cur_y"),
			(overlay_set_position, reg0, pos1),
			
			(assign, reg0, ":stack_size"),
			(str_store_string, s1, "@/ {reg0}"),
			(create_text_overlay, reg0, s1),
			(position_set_x, pos1, 325),
			(position_set_y, pos1, ":cur_y"),
			(overlay_set_position, reg0, pos1),
						
			(val_add, ":stack_size", 1), #for upper limit of number box
			
			(create_number_box_overlay, reg0, 0, ":stack_size"),
			(overlay_set_val, reg0, ":num_of_agents"),
			(position_set_x, pos1, 250),
			(position_set_y, pos1, ":cur_y"),
			(overlay_set_position, reg0, pos1),
				
			(troop_set_slot, "trp_temp_array_a", ":troop_id", reg0),

			(val_sub, ":cur_y", ":cur_y_adder"),
		(try_end), #End Stack/Troop Loop

	    (set_container_overlay, -1),

		(party_set_slot, "p_main_party", slot_party_prebattle_in_battle_count, ":in_count"),
		(assign, reg0, ":in_count"),
		(create_text_overlay, reg60, "@{reg0}", tf_with_outline),
		(try_begin), 		
		    (gt, ":in_count", ":round_size"),
			(overlay_set_color, reg60, 0xFF1100),
		(else_try),
		    (overlay_set_color, reg60, 0xFFFFFF),
		(try_end),
		(position_set_x, pos1, 290),
		(position_set_y, pos1, 50),
		(overlay_set_position, reg60, pos1),
		
		(assign, reg0, ":round_size"),
		(create_text_overlay, reg0, "@of {reg0} troops", 0),
		(position_set_x, pos1, 330),
		(position_set_y, pos1, 50),
		(overlay_set_position, reg0, pos1),
		
		(create_mesh_overlay, reg0, "mesh_pic_charge"),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, reg0, pos1),
        (position_set_x, pos1, 225), 
        (position_set_y, pos1, 50),
        (overlay_set_position, reg0, pos1),
		
	  (create_game_button_overlay, "$g_presentation_obj_custom_battle_designer_19", "@Ready Troops", 0),
      (position_set_x, pos1, 880),
      (position_set_y, pos1, 15),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_19", pos1),

      (create_game_button_overlay, "$g_presentation_obj_custom_battle_designer_20", "@Reassess", 0),
      (position_set_x, pos1, 722),
      (position_set_y, pos1, 15),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_20", pos1),
	  
	  (create_game_button_overlay, "$g_presentation_obj_custom_battle_designer_18", "@Scrap All", 0),
      (position_set_x, pos1, 565),
      (position_set_y, pos1, 15),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_18", pos1),

		#Preview button?
	
	  (presentation_set_duration, 999999),
      ]),
	(ti_on_presentation_run,
      [	
	    (try_begin),
			(key_clicked, key_escape),
			(presentation_set_duration, 0),
        (try_end),
	    (party_get_slot, ":battle_size", "p_main_party", slot_party_prebattle_battle_size),	
	    (this_or_next|lt, ":battle_size", 30),
		(gt, ":battle_size", max_battle_size),
		(assign, "$g_presentation_credits_obj_1", 1),
		(start_presentation, "prsnt_prebattle_record_battle_size"),
      ]),
    (ti_on_presentation_event_state_change,
     [
       (store_trigger_param_1, ":object"),
       (store_trigger_param_2, ":value"),
	   
	   	(try_begin), #Buttons
			(eq, ":object", "$g_presentation_obj_custom_battle_designer_20"),
			(jump_to_menu, "$g_next_menu"),
			(presentation_set_duration, 0),
		(else_try),
		    (eq, ":object", "$g_presentation_obj_custom_battle_designer_18"),
			(party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
		    (try_for_range, ":i", 0, ":num_of_stacks"),
			    (party_stack_get_troop_id, ":troop_id", "p_main_party", ":i"),
			    (neq, ":troop_id", "trp_player"),
			    (troop_get_slot, ":overlay_id", "trp_temp_array_a", ":troop_id"),
			    (troop_set_slot, ":troop_id", slot_troop_prebattle_first_round, 0),
			    (overlay_set_val, ":overlay_id", 0),
		    (try_end),
			(party_set_slot, "p_main_party", slot_party_prebattle_in_battle_count, 0),
			(overlay_set_text, reg60, "@0"),
			(overlay_set_color, reg60, 0xFFFFFF),
		(else_try),
		    (eq, ":object", "$g_presentation_obj_custom_battle_designer_19"),
			(party_get_slot, ":cur_count", "p_main_party", slot_party_prebattle_in_battle_count),
		    (party_get_slot, ":round_size", "p_main_party", slot_party_prebattle_size_in_battle),
			(try_begin),
			    (gt, ":cur_count", ":round_size"),
		        (create_text_overlay, reg0, "@Too many troops^Check number available", tf_center_justify|tf_with_outline),
				(overlay_set_color, reg0, 0xFF1100),
		        (position_set_x, pos1, 600),
		        (position_set_y, pos1, 500),
		        (overlay_set_position, reg0, pos1),
			    (position_set_x, pos1, 0),
		        (position_set_y, pos1, 0),
				(overlay_animate_to_size, reg0, 3000, pos1),
			(else_try),
			    (party_set_slot, "p_main_party", slot_party_prebattle_customized_deployment, 1),
			    (jump_to_menu, "$g_next_menu"),
			    (presentation_set_duration, 0),
			(try_end),
		(else_try), #Number Boxes

		 (party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
		 (try_for_range, ":i", 0, ":num_of_stacks"),
			(party_stack_get_troop_id, ":troop_id", "p_main_party", ":i"),
			(neq, ":troop_id", "trp_player"),
			(troop_slot_eq, "trp_temp_array_a", ":troop_id", ":object"),
			(troop_get_slot, ":num_agents", ":troop_id", slot_troop_prebattle_first_round),
			(assign, ":num_of_stacks", 0), #loop breaker
		 (try_end),
		 
		 (party_get_slot, ":cur_count", "p_main_party", slot_party_prebattle_in_battle_count),
		 (party_get_slot, ":round_size", "p_main_party", slot_party_prebattle_size_in_battle),
		 (store_sub, ":dif", ":value", ":num_agents"),
		 (store_add, ":new_total", ":cur_count", ":dif"),
		 
		 (try_begin),
			(gt, ":new_total", ":round_size"),
			(ge, ":new_total", ":cur_count"),
			(try_begin),
			    (ge, ":cur_count", ":round_size"), #if it was too big to begin with, reset value
				(assign, ":modified_value", ":num_agents"), #revert to pre-change number
				(assign, ":new_total", ":cur_count"), #revert to pre-change number
			(else_try),
			    (store_sub, ":dif2", ":new_total", ":round_size"),
				(val_sub, ":dif", ":dif2"),
				(val_max, ":dif", 0),
				(store_add, ":modified_value", ":value", ":dif"),
				(store_add, ":new_total", ":cur_count", ":dif"),
			(try_end),
			(overlay_set_val, ":object", ":modified_value"),
			(troop_set_slot, ":troop_id", slot_troop_prebattle_first_round, ":modified_value"),
		 (else_try),
		    (troop_set_slot, ":troop_id", slot_troop_prebattle_first_round, ":value"),
		 (try_end),
		 
		 (assign, reg0, ":new_total"),
		 (overlay_set_text, reg60, "@{reg0}"),
		 (try_begin),
			(gt, ":new_total", ":round_size"),
			(overlay_set_color, reg60, 0xFF1100),
		 (else_try),
			(overlay_set_color, reg60, 0xFFFFFF),
		 (try_end),
		 (party_set_slot, "p_main_party", slot_party_prebattle_in_battle_count, ":new_total"),
	   (try_end),	 
		 
       ]),
    ]),
	
 ("prebattle_orders",0, mesh_note_window_bottom,[
     (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        (assign, "$g_formation_group0_selected", 0),
        (assign, "$g_formation_group1_selected", 0),
        (assign, "$g_formation_group2_selected", 0),
        (assign, "$g_formation_group3_selected", 0),
        (assign, "$g_formation_group4_selected", 0),
        (assign, "$g_formation_group5_selected", 0),
        (assign, "$g_formation_group6_selected", 0),
        (assign, "$g_formation_group7_selected", 0),
        (assign, "$g_formation_group8_selected", 0),
        (assign, "$g_presentation_obj_battle_but0", -1),
        (assign, "$g_presentation_obj_battle_but1", -1),
        (assign, "$g_presentation_obj_battle_but2", -1),
        (assign, "$g_presentation_obj_battle_but3", -1),
        (assign, "$g_presentation_obj_battle_but4", -1),
        (assign, "$g_presentation_obj_battle_but5", -1),
        (assign, "$g_presentation_obj_battle_but6", -1),
        (assign, "$g_presentation_obj_battle_but7", -1),
        (assign, "$g_presentation_obj_battle_but8", -1),
        (str_clear, s7),   
	
	    (position_set_y, pos1, 700),
        		
		(create_text_overlay, "$g_presentation_credits_obj_2", "@Initial", tf_center_justify|tf_single_line|tf_with_outline),
        (overlay_set_color, "$g_presentation_credits_obj_2", 0xFFAAAAAA),
        (position_set_x, pos1, 225),
        (overlay_set_position, "$g_presentation_credits_obj_2", pos1),
        (create_text_overlay, "$g_presentation_credits_obj_3", "@Movement 1", tf_center_justify|tf_single_line|tf_with_outline),
        (overlay_set_color, "$g_presentation_credits_obj_3", 0xFFAAAAAA),
        (position_set_x, pos1, 357), #415; 400
        (overlay_set_position, "$g_presentation_credits_obj_3", pos1),
        (create_text_overlay, "$g_presentation_credits_obj_4", "@Movement 2", tf_center_justify|tf_single_line|tf_with_outline),
        (overlay_set_color, "$g_presentation_credits_obj_4", 0xFFAAAAAA),
        (position_set_x, pos1, 487), #590 ; 575
        (overlay_set_position, "$g_presentation_credits_obj_4", pos1),
		(create_text_overlay, "$g_presentation_credits_obj_5", "@Formation", tf_center_justify|tf_single_line|tf_with_outline),
        (overlay_set_color, "$g_presentation_credits_obj_5", 0xFFAAAAAA),
        (position_set_x, pos1, 610),
        (overlay_set_position, "$g_presentation_credits_obj_5", pos1),
		
		(create_text_overlay, "$g_presentation_credits_obj_6", "@Attack", tf_center_justify|tf_single_line|tf_with_outline),
        (overlay_set_color, "$g_presentation_credits_obj_6", 0xFFAAAAAA),
        (position_set_x, pos1, 225),
        (overlay_set_position, "$g_presentation_credits_obj_6", pos1),
		(overlay_set_display, "$g_presentation_credits_obj_6", 0),
		(create_text_overlay, "$g_presentation_credits_obj_7", "@Weapon Type", tf_center_justify|tf_single_line|tf_with_outline),
        (overlay_set_color, "$g_presentation_credits_obj_7", 0xFFAAAAAA),
        (position_set_x, pos1, 360), #390
        (overlay_set_position, "$g_presentation_credits_obj_7", pos1),
		(overlay_set_display, "$g_presentation_credits_obj_7", 0),
		(create_text_overlay, "$g_presentation_credits_obj_8", "@Shield", tf_center_justify|tf_single_line|tf_with_outline),
        (overlay_set_color, "$g_presentation_credits_obj_8", 0xFFAAAAAA),
        (position_set_x, pos1, 485), #490
        (overlay_set_position, "$g_presentation_credits_obj_8", pos1),
		(overlay_set_display, "$g_presentation_credits_obj_8", 0),
		(create_text_overlay, "$g_presentation_credits_obj_9", "@Skirmish", tf_center_justify|tf_single_line|tf_with_outline),
        (overlay_set_color, "$g_presentation_credits_obj_9", 0xFFAAAAAA),
        (position_set_x, pos1, 600), #590
        (overlay_set_position, "$g_presentation_credits_obj_9", pos1),
		(overlay_set_display, "$g_presentation_credits_obj_9", 0),

        (assign, "$group0_has_troops", 0),
        (assign, "$group1_has_troops", 0),
        (assign, "$group2_has_troops", 0),
        (assign, "$group3_has_troops", 0),
        (assign, "$group4_has_troops", 0),
        (assign, "$group5_has_troops", 0),
        (assign, "$group6_has_troops", 0),
        (assign, "$group7_has_troops", 0),
        (assign, "$group8_has_troops", 0),
        (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
        (assign, "$num_classes", 0),
		(try_for_range, ":troop_iterator", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":cur_troop_id", "p_main_party", ":troop_iterator"),
          (troop_get_class, ":troop_class", ":cur_troop_id"),
          (neq, "trp_player", ":cur_troop_id"),
          (try_begin),
			(eq, ":troop_class", 0),
            (try_begin),
              (neq, "$group0_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group0_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 1),
            (try_begin),
              (neq, "$group1_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group1_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 2),
            (try_begin),
              (neq, "$group2_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group2_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 3),
            (try_begin),
              (neq, "$group3_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group3_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 4),
            (try_begin),
              (neq, "$group4_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group4_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 5),
            (try_begin),
              (neq, "$group5_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group5_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 6),
            (try_begin),
              (neq, "$group6_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group6_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 7),
            (try_begin),
              (neq, "$group7_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group7_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 8),
            (try_begin),
              (neq, "$group8_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group8_has_troops", 1),
          (try_end),
        (try_end),
		#Split Divisions
		(try_for_range, ":troop_iterator", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":cur_troop_id", "p_main_party", ":troop_iterator"),
          (troop_get_class, ":troop_class", ":cur_troop_id"),
          (neq, "trp_player", ":cur_troop_id"),
		  (neg|troop_is_hero, ":cur_troop_id"),
		  (troop_slot_ge,  ":cur_troop_id", slot_troop_prebattle_alt_division_percent, 1), #Has a split active
		  (troop_get_slot, ":alt_division", ":cur_troop_id", slot_troop_prebattle_alt_division),
		  (is_between, ":alt_division", 0, 9), #Valid division
		  (neq, ":troop_class", ":alt_division"), #So there is an actual change to make
		  (assign, ":troop_class", ":alt_division"),
          (try_begin),
			(eq, ":troop_class", 0),
            (try_begin),
              (neq, "$group0_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group0_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 1),
            (try_begin),
              (neq, "$group1_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group1_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 2),
            (try_begin),
              (neq, "$group2_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group2_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 3),
            (try_begin),
              (neq, "$group3_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group3_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 4),
            (try_begin),
              (neq, "$group4_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group4_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 5),
            (try_begin),
              (neq, "$group5_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group5_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 6),
            (try_begin),
              (neq, "$group6_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group6_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 7),
            (try_begin),
              (neq, "$group7_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group7_has_troops", 1),
          (else_try),
            (eq, ":troop_class", 8),
            (try_begin),
              (neq, "$group8_has_troops", 1),
              (val_add, "$num_classes", 1),
            (try_end),
            (assign, "$group8_has_troops", 1),
          (try_end),
        (try_end),
		#Split Divisions End

        (assign, ":stat_position_x", 0),
        (assign, ":stat_position_y", 653),
        (assign, ":stat_position_check_x", 20),
        (assign, ":stat_position_check_y", 662),
        (assign, ":stat_position_name_x", 50),
        (assign, ":stat_position_name_y", 660),
		(assign, ":stat_position_order_y", 660),
        (try_begin),
          (eq, "$group0_has_troops", 1),
          (create_image_button_overlay, "$g_presentation_obj_battle_but0", "mesh_white_plane", "mesh_white_plane"),
          (val_add, ":stat_position_x", 15),
		  (position_set_x, pos1, ":stat_position_x"),
          (position_set_y, pos1, ":stat_position_y"),
          (overlay_set_position, "$g_presentation_obj_battle_but0", pos1),
		  (val_add, ":stat_position_x", -15),
          (val_add, ":stat_position_y", -40),

          (position_set_x, pos1, 32650),
          (position_set_y, pos1, 2000),
          (overlay_set_size, "$g_presentation_obj_battle_but0", pos1),
          (overlay_set_alpha, "$g_presentation_obj_battle_but0", 0),
          (overlay_set_color, "$g_presentation_obj_battle_but0", 0xFFFF00),

          (create_check_box_overlay, "$g_presentation_obj_battle_check0", "mesh_checkbox_off", "mesh_checkbox_on"),
          (position_set_x, pos2, ":stat_position_check_x"),
          (position_set_y, pos2, ":stat_position_check_y"),
          (overlay_set_position, "$g_presentation_obj_battle_check0", pos2),
          (val_add, ":stat_position_check_y", -40),

          (str_store_class_name, s7, 0),
		  (create_text_overlay, "$g_presentation_obj_battle_name0", s7, 0),
          (position_set_x, pos3, ":stat_position_name_x"),
          (position_set_y, pos3, ":stat_position_name_y"),
          (overlay_set_position, "$g_presentation_obj_battle_name0", pos3),
        
          (val_add, ":stat_position_name_y", -40),

          (create_text_overlay, "$g_presentation_but0_movement", "str_space", tf_center_justify), #Initial
          (create_text_overlay, "$g_presentation_but0_riding", "str_space", tf_center_justify), #Position 1
          (create_text_overlay, "$g_presentation_but0_weapon_usage", "str_space", tf_center_justify), #Position 2
		  (create_text_overlay, reg(6), "str_space", tf_center_justify), #Formations
		  
		  (create_text_overlay, reg(15), "str_space", tf_center_justify), #Native Weapon
		  (create_text_overlay, reg(24), "str_space", tf_center_justify), #Caba'drin Weapon
		  (create_text_overlay, reg(33), "str_space", tf_center_justify), #Caba'drin Shield	 
          (create_text_overlay, reg(42), "str_space", tf_center_justify), #Caba'drin Skirmish			  
		  
		  (position_set_x, pos1, 950),
		  (position_set_y, pos1, 950),
		  (overlay_set_size, "$g_presentation_but0_movement", pos1),
		  (overlay_set_size, "$g_presentation_but0_riding", pos1),
		  (overlay_set_size, "$g_presentation_but0_weapon_usage", pos1),
		  (overlay_set_size, reg(6), pos1),
		  (overlay_set_size, reg(15), pos1),
		  (overlay_set_size, reg(24), pos1),
		  (overlay_set_size, reg(33), pos1),
		  (overlay_set_size, reg(42), pos1),
		  
		  (overlay_set_display, reg(15), 0),
		  (overlay_set_display, reg(24), 0),
		  (overlay_set_display, reg(33), 0),
          (overlay_set_display, reg(42), 0),		  

		  (position_set_y, pos1, ":stat_position_order_y"),
          (position_set_x, pos1, 225), 
          (overlay_set_position, "$g_presentation_but0_movement", pos1),
          (position_set_x, pos1, 355), #350 ; 380 ; 400
          (overlay_set_position, "$g_presentation_but0_riding", pos1),
          (position_set_x, pos1, 485), #475 ; 500; 570
          (overlay_set_position, "$g_presentation_but0_weapon_usage", pos1),
		  (position_set_x, pos1, 605), #
          (overlay_set_position, reg(6), pos1),
		  
		  (position_set_x, pos1, 225),
          (overlay_set_position, reg(15), pos1),
		  (position_set_x, pos1, 355), #350
          (overlay_set_position, reg(24), pos1),
          (position_set_x, pos1, 485), #475
          (overlay_set_position, reg(33), pos1),
		  (position_set_x, pos1, 605), #600  
		  (overlay_set_position, reg(42), pos1),
          (val_add, ":stat_position_order_y", -40),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_1", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_1", pos1),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_11", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_11", pos1),
        (try_end),
        (try_begin),
          (eq, "$group1_has_troops", 1),
          (create_image_button_overlay, "$g_presentation_obj_battle_but1", "mesh_white_plane", "mesh_white_plane"),
		  (val_add, ":stat_position_x", 15),
          (position_set_x, pos1, ":stat_position_x"),
          (position_set_y, pos1, ":stat_position_y"),
          (overlay_set_position, "$g_presentation_obj_battle_but1", pos1),
          (val_add, ":stat_position_y", -40),
		  (val_add, ":stat_position_x", -15),

          (position_set_x, pos1, 32650),
          (position_set_y, pos1, 2000),
          (overlay_set_size, "$g_presentation_obj_battle_but1", pos1),
          (overlay_set_alpha, "$g_presentation_obj_battle_but1", 0),
          (overlay_set_color, "$g_presentation_obj_battle_but1", 0xFFFF00),

          (create_check_box_overlay, "$g_presentation_obj_battle_check1", "mesh_checkbox_off", "mesh_checkbox_on"),
          (position_set_x, pos2, ":stat_position_check_x"),
          (position_set_y, pos2, ":stat_position_check_y"),
          (overlay_set_position, "$g_presentation_obj_battle_check1", pos2),
          (val_add, ":stat_position_check_y", -40),        

		  (str_store_class_name, s7, 1),
          (create_text_overlay, "$g_presentation_obj_battle_name1", s7, 0),
          (position_set_x, pos3, ":stat_position_name_x"),
          (position_set_y, pos3, ":stat_position_name_y"),
          (overlay_set_position, "$g_presentation_obj_battle_name1", pos3),
          (val_add, ":stat_position_name_y", -40),

          (create_text_overlay, "$g_presentation_but1_movement", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but1_riding", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but1_weapon_usage", "str_space", tf_center_justify),
		  (create_text_overlay, reg(7), "str_space", tf_center_justify), #Formations
		  
		  (create_text_overlay, reg(16), "str_space", tf_center_justify), #Native Weapon
		  (create_text_overlay, reg(25), "str_space", tf_center_justify), #Caba'drin Weapon
		  (create_text_overlay, reg(34), "str_space", tf_center_justify), #Caba'drin Shield	 
          (create_text_overlay, reg(43), "str_space", tf_center_justify), #Caba'drin Skirmish	
		  
		  (position_set_x, pos1, 950),
		  (position_set_y, pos1, 950),
		  (overlay_set_size, "$g_presentation_but1_movement", pos1),
		  (overlay_set_size, "$g_presentation_but1_riding", pos1),
		  (overlay_set_size, "$g_presentation_but1_weapon_usage", pos1),
		  (overlay_set_size, reg(7), pos1),
		  (overlay_set_size, reg(16), pos1),
		  (overlay_set_size, reg(25), pos1),
		  (overlay_set_size, reg(34), pos1),
		  (overlay_set_size, reg(43), pos1),
		  
		  (overlay_set_display, reg(16), 0),
		  (overlay_set_display, reg(25), 0),
		  (overlay_set_display, reg(34), 0),
          (overlay_set_display, reg(43), 0),

		  (position_set_y, pos1, ":stat_position_order_y"),
          (position_set_x, pos1, 225),
          (overlay_set_position, "$g_presentation_but1_movement", pos1),
          (position_set_x, pos1, 355), #350 ; 380 ; 400
          (overlay_set_position, "$g_presentation_but1_riding", pos1),
          (position_set_x, pos1, 485), #475 ; 500 ; 570
          (overlay_set_position, "$g_presentation_but1_weapon_usage", pos1),
		  (position_set_x, pos1, 605),
          (overlay_set_position, reg(7), pos1),
		  
		  (position_set_x, pos1, 225),
          (overlay_set_position, reg(16), pos1),
		  (position_set_x, pos1, 355), #350
          (overlay_set_position, reg(25), pos1),
          (position_set_x, pos1, 485), #475
          (overlay_set_position, reg(34), pos1),
		  (position_set_x, pos1, 605), #600  
		  (overlay_set_position, reg(43), pos1),
          (val_add, ":stat_position_order_y", -40),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_2", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_2", pos1),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_12", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_12", pos1),
        (try_end),
        (try_begin),
          (eq, "$group2_has_troops", 1),
          (create_image_button_overlay, "$g_presentation_obj_battle_but2", "mesh_white_plane", "mesh_white_plane"),
		  (val_add, ":stat_position_x", 15),
          (position_set_x, pos1, ":stat_position_x"),
          (position_set_y, pos1, ":stat_position_y"),
          (overlay_set_position, "$g_presentation_obj_battle_but2", pos1),
          (val_add, ":stat_position_y", -40),
		  (val_add, ":stat_position_x", -15),

          (position_set_x, pos1, 32650),
          (position_set_y, pos1, 2000),
          (overlay_set_size, "$g_presentation_obj_battle_but2", pos1),
          (overlay_set_alpha, "$g_presentation_obj_battle_but2", 0),
          (overlay_set_color, "$g_presentation_obj_battle_but2", 0xFFFF00),

          (create_check_box_overlay, "$g_presentation_obj_battle_check2", "mesh_checkbox_off", "mesh_checkbox_on"),          
          (position_set_x, pos2, ":stat_position_check_x"),
          (position_set_y, pos2, ":stat_position_check_y"),
          (overlay_set_position, "$g_presentation_obj_battle_check2", pos2),
          (val_add, ":stat_position_check_y", -40),        

		  (str_store_class_name, s7, 2),
          (create_text_overlay, "$g_presentation_obj_battle_name2", s7, 0),
          (position_set_x, pos3, ":stat_position_name_x"),
          (position_set_y, pos3, ":stat_position_name_y"),
          (overlay_set_position, "$g_presentation_obj_battle_name2", pos3),
          (val_add, ":stat_position_name_y", -40),

          (create_text_overlay, "$g_presentation_but2_movement", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but2_riding", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but2_weapon_usage", "str_space", tf_center_justify),
		  (create_text_overlay, reg(8), "str_space", tf_center_justify), #Formations
		  
		  (create_text_overlay, reg(17), "str_space", tf_center_justify), #Native Weapon
		  (create_text_overlay, reg(26), "str_space", tf_center_justify), #Caba'drin Weapon
		  (create_text_overlay, reg(35), "str_space", tf_center_justify), #Caba'drin Shield	 
          (create_text_overlay, reg(44), "str_space", tf_center_justify), #Caba'drin Skirmish	
		  
		  (position_set_x, pos1, 950),
		  (position_set_y, pos1, 950),
		  (overlay_set_size, "$g_presentation_but2_movement", pos1),
		  (overlay_set_size, "$g_presentation_but2_riding", pos1),
		  (overlay_set_size, "$g_presentation_but2_weapon_usage", pos1),
		  (overlay_set_size, reg(8), pos1),
		  (overlay_set_size, reg(17), pos1),
		  (overlay_set_size, reg(26), pos1),
		  (overlay_set_size, reg(35), pos1),
		  (overlay_set_size, reg(44), pos1),
		  
		  (overlay_set_display, reg(17), 0),
		  (overlay_set_display, reg(26), 0),
		  (overlay_set_display, reg(35), 0),
          (overlay_set_display, reg(44), 0),
		  
		  (position_set_y, pos1, ":stat_position_order_y"),
          (position_set_x, pos1, 225),
          (overlay_set_position, "$g_presentation_but2_movement", pos1),
          (position_set_x, pos1, 355), #350 ; 380
          (overlay_set_position, "$g_presentation_but2_riding", pos1),
          (position_set_x, pos1, 485), #475 ; 500
          (overlay_set_position, "$g_presentation_but2_weapon_usage", pos1),
		  (position_set_x, pos1, 605),
          (overlay_set_position, reg(8), pos1),
		  
		  (position_set_x, pos1, 225),
          (overlay_set_position, reg(17), pos1),
		  (position_set_x, pos1, 355), #350
          (overlay_set_position, reg(26), pos1),
          (position_set_x, pos1, 485), #475
          (overlay_set_position, reg(35), pos1),
		  (position_set_x, pos1, 605), #600 
		  (overlay_set_position, reg(44), pos1),
          (val_add, ":stat_position_order_y", -40),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_3", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_3", pos1),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_13", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_13", pos1),
        (try_end),
        (try_begin),
          (eq, "$group3_has_troops", 1),
          (create_image_button_overlay, "$g_presentation_obj_battle_but3", "mesh_white_plane", "mesh_white_plane"),
		  (val_add, ":stat_position_x", 15),
          (position_set_x, pos1, ":stat_position_x"),
          (position_set_y, pos1, ":stat_position_y"),
          (overlay_set_position, "$g_presentation_obj_battle_but3", pos1),
          (val_add, ":stat_position_y", -40),
		  (val_add, ":stat_position_x", -15),

          (position_set_x, pos1, 32650),
          (position_set_y, pos1, 2000),
          (overlay_set_size, "$g_presentation_obj_battle_but3", pos1),
          (overlay_set_alpha, "$g_presentation_obj_battle_but3", 0),
          (overlay_set_color, "$g_presentation_obj_battle_but3", 0xFFFF00),

          (create_check_box_overlay, "$g_presentation_obj_battle_check3", "mesh_checkbox_off", "mesh_checkbox_on"),          
          (position_set_x, pos2, ":stat_position_check_x"),
          (position_set_y, pos2, ":stat_position_check_y"),
          (overlay_set_position, "$g_presentation_obj_battle_check3", pos2),
          (val_add, ":stat_position_check_y", -40),        

		  (str_store_class_name, s7, 3),
          (create_text_overlay, "$g_presentation_obj_battle_name3", s7, 0),
          (position_set_x, pos3, ":stat_position_name_x"),
          (position_set_y, pos3, ":stat_position_name_y"),
          (overlay_set_position, "$g_presentation_obj_battle_name3", pos3),
          (val_add, ":stat_position_name_y", -40),

          (create_text_overlay, "$g_presentation_but3_movement", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but3_riding", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but3_weapon_usage", "str_space", tf_center_justify),
		  (create_text_overlay, reg(9), "str_space", tf_center_justify), #Formations
		  
          (create_text_overlay, reg(18), "str_space", tf_center_justify), #Native Weapon
		  (create_text_overlay, reg(27), "str_space", tf_center_justify), #Caba'drin Weapon
		  (create_text_overlay, reg(36), "str_space", tf_center_justify), #Caba'drin Shield	 
          (create_text_overlay, reg(45), "str_space", tf_center_justify), #Caba'drin Skirmish			  

          (position_set_x, pos1, 950),
		  (position_set_y, pos1, 950),
		  (overlay_set_size, "$g_presentation_but3_movement", pos1),
		  (overlay_set_size, "$g_presentation_but3_riding", pos1),
		  (overlay_set_size, "$g_presentation_but3_weapon_usage", pos1),
		  (overlay_set_size, reg(9), pos1),
		  (overlay_set_size, reg(18), pos1),
          (overlay_set_size, reg(27), pos1),
		  (overlay_set_size, reg(36), pos1),
		  (overlay_set_size, reg(45), pos1),
		  
		  (overlay_set_display, reg(18), 0),
		  (overlay_set_display, reg(27), 0),
		  (overlay_set_display, reg(36), 0),
          (overlay_set_display, reg(45), 0),		  
		  
		  (position_set_y, pos1, ":stat_position_order_y"),
          (position_set_x, pos1, 225),
          (overlay_set_position, "$g_presentation_but3_movement", pos1),
          (position_set_x, pos1, 355), #350 ; 380
          (overlay_set_position, "$g_presentation_but3_riding", pos1),
          (position_set_x, pos1, 485), #475 ; 500
          (overlay_set_position, "$g_presentation_but3_weapon_usage", pos1),
		  (position_set_x, pos1, 605),
          (overlay_set_position, reg(9), pos1),
		  
		  (position_set_x, pos1, 225),
          (overlay_set_position, reg(18), pos1),
		  (position_set_x, pos1, 355), #350
          (overlay_set_position, reg(27), pos1),
          (position_set_x, pos1, 485), #475
          (overlay_set_position, reg(36), pos1),
		  (position_set_x, pos1, 605), #600 
		  (overlay_set_position, reg(45), pos1),
          (val_add, ":stat_position_order_y", -40),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_4", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_4", pos1),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_14", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_14", pos1),
        (try_end),
        (try_begin),
          (eq, "$group4_has_troops", 1),
          (create_image_button_overlay, "$g_presentation_obj_battle_but4", "mesh_white_plane", "mesh_white_plane"),
		  (val_add, ":stat_position_x", 15),
          (position_set_x, pos1, ":stat_position_x"),
          (position_set_y, pos1, ":stat_position_y"),
          (overlay_set_position, "$g_presentation_obj_battle_but4", pos1),
          (val_add, ":stat_position_y", -40),
		  (val_add, ":stat_position_x", -15),

          (position_set_x, pos1, 32650),
          (position_set_y, pos1, 2000),
          (overlay_set_size, "$g_presentation_obj_battle_but4", pos1),
          (overlay_set_alpha, "$g_presentation_obj_battle_but4", 0),
          (overlay_set_color, "$g_presentation_obj_battle_but4", 0xFFFF00),

          (create_check_box_overlay, "$g_presentation_obj_battle_check4", "mesh_checkbox_off", "mesh_checkbox_on"),          
          (position_set_x, pos2, ":stat_position_check_x"),
          (position_set_y, pos2, ":stat_position_check_y"),
          (overlay_set_position, "$g_presentation_obj_battle_check4", pos2),
          (val_add, ":stat_position_check_y", -40),        

		  (str_store_class_name, s7, 4), 
          (create_text_overlay, "$g_presentation_obj_battle_name4", s7, 0),
          (position_set_x, pos3, ":stat_position_name_x"),
          (position_set_y, pos3, ":stat_position_name_y"),
          (overlay_set_position, "$g_presentation_obj_battle_name4", pos3),
          (val_add, ":stat_position_name_y", -40),
        
          (create_text_overlay, "$g_presentation_but4_movement", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but4_riding", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but4_weapon_usage", "str_space", tf_center_justify),
		  (create_text_overlay, reg(10), "str_space", tf_center_justify), #Formations
		  
		  (create_text_overlay, reg(19), "str_space", tf_center_justify), #Native Weapon
		  (create_text_overlay, reg(28), "str_space", tf_center_justify), #Caba'drin Weapon
		  (create_text_overlay, reg(37), "str_space", tf_center_justify), #Caba'drin Shield	 
          (create_text_overlay, reg(46), "str_space", tf_center_justify), #Caba'drin Skirmish	
		  
		  (position_set_x, pos1, 950),
		  (position_set_y, pos1, 950),
		  (overlay_set_size, "$g_presentation_but4_movement", pos1),
		  (overlay_set_size, "$g_presentation_but4_riding", pos1),
		  (overlay_set_size, "$g_presentation_but4_weapon_usage", pos1),
		  (overlay_set_size, reg(10), pos1),
		  (overlay_set_size, reg(19), pos1),
		  (overlay_set_size, reg(28), pos1),
		  (overlay_set_size, reg(37), pos1),
		  (overlay_set_size, reg(46), pos1),
		  
		  (overlay_set_display, reg(19), 0),
		  (overlay_set_display, reg(28), 0),
		  (overlay_set_display, reg(37), 0),
          (overlay_set_display, reg(46), 0),
		  
		  (position_set_y, pos1, ":stat_position_order_y"),
          (position_set_x, pos1, 225),
          (overlay_set_position, "$g_presentation_but4_movement", pos1),
          (position_set_x, pos1, 355), #350 ; 380
          (overlay_set_position, "$g_presentation_but4_riding", pos1),
          (position_set_x, pos1, 485), #475 ; 500
          (overlay_set_position, "$g_presentation_but4_weapon_usage", pos1),
		  (position_set_x, pos1, 605),
          (overlay_set_position, reg(10), pos1),
		  
		  (position_set_x, pos1, 225),
          (overlay_set_position, reg(19), pos1),
		  (position_set_x, pos1, 355), #350
          (overlay_set_position, reg(28), pos1),
          (position_set_x, pos1, 485), #475
          (overlay_set_position, reg(37), pos1),
		  (position_set_x, pos1, 605), #600 
		  (overlay_set_position, reg(46), pos1),
          (val_add, ":stat_position_order_y", -40),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_5", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_5", pos1),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_15", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_15", pos1),
        (try_end),
        (try_begin),
          (eq, "$group5_has_troops", 1),
          (create_image_button_overlay, "$g_presentation_obj_battle_but5", "mesh_white_plane", "mesh_white_plane"),
		  (val_add, ":stat_position_x", 15),
          (position_set_x, pos1, ":stat_position_x"),
          (position_set_y, pos1, ":stat_position_y"),
          (overlay_set_position, "$g_presentation_obj_battle_but5", pos1),
          (val_add, ":stat_position_y", -40),
		  (val_add, ":stat_position_x", -15),

          (position_set_x, pos1, 32650),
          (position_set_y, pos1, 2000),
          (overlay_set_size, "$g_presentation_obj_battle_but5", pos1),
          (overlay_set_alpha, "$g_presentation_obj_battle_but5", 0),
          (overlay_set_color, "$g_presentation_obj_battle_but5", 0xFFFF00),

          (create_check_box_overlay, "$g_presentation_obj_battle_check5", "mesh_checkbox_off", "mesh_checkbox_on"),          
          (position_set_x, pos2, ":stat_position_check_x"),
          (position_set_y, pos2, ":stat_position_check_y"),
          (overlay_set_position, "$g_presentation_obj_battle_check5", pos2),
          (val_add, ":stat_position_check_y", -40),        

		  (str_store_class_name, s7, 5),
          (create_text_overlay, "$g_presentation_obj_battle_name5", s7, 0),
          (position_set_x, pos3, ":stat_position_name_x"),
          (position_set_y, pos3, ":stat_position_name_y"),
          (overlay_set_position, "$g_presentation_obj_battle_name5", pos3),
          (val_add, ":stat_position_name_y", -40),

          (create_text_overlay, "$g_presentation_but5_movement", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but5_riding", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but5_weapon_usage", "str_space", tf_center_justify),
		  (create_text_overlay, reg(11), "str_space", tf_center_justify), #Formations
		  
		  (create_text_overlay, reg(20), "str_space", tf_center_justify), #Native Weapon
		  (create_text_overlay, reg(29), "str_space", tf_center_justify), #Caba'drin Weapon
		  (create_text_overlay, reg(38), "str_space", tf_center_justify), #Caba'drin Shield	 
          (create_text_overlay, reg(47), "str_space", tf_center_justify), #Caba'drin Skirmish	
		  
		  (position_set_x, pos1, 950),
		  (position_set_y, pos1, 950),
		  (overlay_set_size, "$g_presentation_but5_movement", pos1),
		  (overlay_set_size, "$g_presentation_but5_riding", pos1),
		  (overlay_set_size, "$g_presentation_but5_weapon_usage", pos1),
          (overlay_set_size, reg(11), pos1),		 
		  (overlay_set_size, reg(20), pos1),
		  (overlay_set_size, reg(29), pos1),
		  (overlay_set_size, reg(38), pos1),
		  (overlay_set_size, reg(47), pos1),
		  
		  (overlay_set_display, reg(20), 0),
		  (overlay_set_display, reg(29), 0),
		  (overlay_set_display, reg(38), 0),
          (overlay_set_display, reg(47), 0),
		  
		  (position_set_y, pos1, ":stat_position_order_y"),
          (position_set_x, pos1, 225),
          (overlay_set_position, "$g_presentation_but5_movement", pos1),
          (position_set_x, pos1, 355), #350 ; 380
          (overlay_set_position, "$g_presentation_but5_riding", pos1),
          (position_set_x, pos1, 485), #475 ; 500
          (overlay_set_position, "$g_presentation_but5_weapon_usage", pos1),
		  (position_set_x, pos1, 605),
          (overlay_set_position, reg(11), pos1),
		  
		  (position_set_x, pos1, 225),
          (overlay_set_position, reg(20), pos1),
		  (position_set_x, pos1, 355), #350
          (overlay_set_position, reg(29), pos1),
          (position_set_x, pos1, 485), #475
          (overlay_set_position, reg(38), pos1),
		  (position_set_x, pos1, 605), #600 
		  (overlay_set_position, reg(47), pos1),
          (val_add, ":stat_position_order_y", -40),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_6", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_6", pos1),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_16", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_16", pos1),
        (try_end),
        (try_begin),
          (eq, "$group6_has_troops", 1),
          (create_image_button_overlay, "$g_presentation_obj_battle_but6", "mesh_white_plane", "mesh_white_plane"),
		  (val_add, ":stat_position_x", 15),
          (position_set_x, pos1, ":stat_position_x"),
          (position_set_y, pos1, ":stat_position_y"),
          (overlay_set_position, "$g_presentation_obj_battle_but6", pos1),
          (val_add, ":stat_position_y", -40),
		  (val_add, ":stat_position_x", -15),

          (position_set_x, pos1, 32650),
          (position_set_y, pos1, 2000),
          (overlay_set_size, "$g_presentation_obj_battle_but6", pos1),
          (overlay_set_alpha, "$g_presentation_obj_battle_but6", 0),
          (overlay_set_color, "$g_presentation_obj_battle_but6", 0xFFFF00),

          (create_check_box_overlay, "$g_presentation_obj_battle_check6", "mesh_checkbox_off", "mesh_checkbox_on"),          
          (position_set_x, pos2, ":stat_position_check_x"),
          (position_set_y, pos2, ":stat_position_check_y"),
          (overlay_set_position, "$g_presentation_obj_battle_check6", pos2),
          (val_add, ":stat_position_check_y", -40),        

		  (str_store_class_name, s7, 6), 
          (create_text_overlay, "$g_presentation_obj_battle_name6", s7, 0),
          (position_set_x, pos3, ":stat_position_name_x"),
          (position_set_y, pos3, ":stat_position_name_y"),
          (overlay_set_position, "$g_presentation_obj_battle_name6", pos3),
          (val_add, ":stat_position_name_y", -40),

          (create_text_overlay, "$g_presentation_but6_movement", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but6_riding", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but6_weapon_usage", "str_space", tf_center_justify),
		  (create_text_overlay, reg(12), "str_space", tf_center_justify), #Formations
		  
		  (create_text_overlay, reg(21), "str_space", tf_center_justify), #Native Weapon
		  (create_text_overlay, reg(30), "str_space", tf_center_justify), #Caba'drin Weapon
		  (create_text_overlay, reg(39), "str_space", tf_center_justify), #Caba'drin Shield	 
          (create_text_overlay, reg(48), "str_space", tf_center_justify), #Caba'drin Skirmish	

		  (position_set_x, pos1, 950),
		  (position_set_y, pos1, 950),
		  (overlay_set_size, "$g_presentation_but6_movement", pos1),
		  (overlay_set_size, "$g_presentation_but6_riding", pos1),
		  (overlay_set_size, "$g_presentation_but6_weapon_usage", pos1),
		  (overlay_set_size, reg(12), pos1),
		  (overlay_set_size, reg(21), pos1),
		  (overlay_set_size, reg(30), pos1),
		  (overlay_set_size, reg(39), pos1),
		  (overlay_set_size, reg(48), pos1),
		  
		  (overlay_set_display, reg(21), 0),
		  (overlay_set_display, reg(30), 0),
		  (overlay_set_display, reg(39), 0),
          (overlay_set_display, reg(48), 0),
		  
		  (position_set_y, pos1, ":stat_position_order_y"),
          (position_set_x, pos1, 225),
          (overlay_set_position, "$g_presentation_but6_movement", pos1),
          (position_set_x, pos1, 355), #350 ; 380
          (overlay_set_position, "$g_presentation_but6_riding", pos1),
          (position_set_x, pos1, 485), #475 ; 500
          (overlay_set_position, "$g_presentation_but6_weapon_usage", pos1),
		  (position_set_x, pos1, 605),
          (overlay_set_position, reg(12), pos1),
		  
		  (position_set_x, pos1, 225),
          (overlay_set_position, reg(21), pos1),
		  (position_set_x, pos1, 355), #350
          (overlay_set_position, reg(30), pos1),
          (position_set_x, pos1, 485), #475
          (overlay_set_position, reg(39), pos1),
		  (position_set_x, pos1, 605), #600 
		  (overlay_set_position, reg(48), pos1),
          (val_add, ":stat_position_order_y", -40),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_7", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_7", pos1),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_17", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_17", pos1),
        (try_end),
        (try_begin),
          (eq, "$group7_has_troops", 1),
          (create_image_button_overlay, "$g_presentation_obj_battle_but7", "mesh_white_plane", "mesh_white_plane"),
		  (val_add, ":stat_position_x", 15),
          (position_set_x, pos1, ":stat_position_x"),
          (position_set_y, pos1, ":stat_position_y"),
          (overlay_set_position, "$g_presentation_obj_battle_but7", pos1),
          (val_add, ":stat_position_y", -40),
		  (val_add, ":stat_position_x", -15),

          (position_set_x, pos1, 32650),
          (position_set_y, pos1, 2000),
          (overlay_set_size, "$g_presentation_obj_battle_but7", pos1),
          (overlay_set_alpha, "$g_presentation_obj_battle_but7", 0),
          (overlay_set_color, "$g_presentation_obj_battle_but7", 0xFFFF00),

          (create_check_box_overlay, "$g_presentation_obj_battle_check7", "mesh_checkbox_off", "mesh_checkbox_on"),          
          (position_set_x, pos2, ":stat_position_check_x"),
          (position_set_y, pos2, ":stat_position_check_y"),
          (overlay_set_position, "$g_presentation_obj_battle_check7", pos2),
          (val_add, ":stat_position_check_y", -40),        

		  (str_store_class_name, s7, 7),
          (create_text_overlay, "$g_presentation_obj_battle_name7", s7, 0),
          (position_set_x, pos3, ":stat_position_name_x"),
          (position_set_y, pos3, ":stat_position_name_y"),
          (overlay_set_position, "$g_presentation_obj_battle_name7", pos3),
          (val_add, ":stat_position_name_y", -40),

          (create_text_overlay, "$g_presentation_but7_movement", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but7_riding", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but7_weapon_usage", "str_space", tf_center_justify),
		  (create_text_overlay, reg(13), "str_space", tf_center_justify), #Formations
		  
		  (create_text_overlay, reg(22), "str_space", tf_center_justify), #Native Weapon
		  (create_text_overlay, reg(31), "str_space", tf_center_justify), #Caba'drin Weapon
		  (create_text_overlay, reg(40), "str_space", tf_center_justify), #Caba'drin Shield	 
          (create_text_overlay, reg(49), "str_space", tf_center_justify), #Caba'drin Skirmish	
		  
		  (position_set_x, pos1, 950),
		  (position_set_y, pos1, 950),
		  (overlay_set_size, "$g_presentation_but7_movement", pos1),
		  (overlay_set_size, "$g_presentation_but7_riding", pos1),
		  (overlay_set_size, "$g_presentation_but7_weapon_usage", pos1),
		  (overlay_set_size, reg(13), pos1),
		  (overlay_set_size, reg(22), pos1),
          (overlay_set_size, reg(31), pos1),
		  (overlay_set_size, reg(40), pos1),
		  (overlay_set_size, reg(49), pos1),
		  
		  (overlay_set_display, reg(22), 0),
		  (overlay_set_display, reg(31), 0),
		  (overlay_set_display, reg(40), 0),
          (overlay_set_display, reg(49), 0),		  
		  
		  (position_set_y, pos1, ":stat_position_order_y"),
          (position_set_x, pos1, 225),
          (overlay_set_position, "$g_presentation_but7_movement", pos1),
          (position_set_x, pos1, 355), #350 ; 380
          (overlay_set_position, "$g_presentation_but7_riding", pos1),
          (position_set_x, pos1, 485), #475 ; 500
          (overlay_set_position, "$g_presentation_but7_weapon_usage", pos1),
		  (position_set_x, pos1, 605), #475 ; 500
          (overlay_set_position, reg(13), pos1),
		  
		  (position_set_x, pos1, 225),
          (overlay_set_position, reg(22), pos1),
		  (position_set_x, pos1, 355), #350
          (overlay_set_position, reg(31), pos1),
          (position_set_x, pos1, 485), #475
          (overlay_set_position, reg(40), pos1),
		  (position_set_x, pos1, 605), #600 
		  (overlay_set_position, reg(49), pos1),
          (val_add, ":stat_position_order_y", -40),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_8", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_8", pos1),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_18", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_18", pos1),
        (try_end),
        (try_begin),
          (eq, "$group8_has_troops", 1),
          (create_image_button_overlay, "$g_presentation_obj_battle_but8", "mesh_white_plane", "mesh_white_plane"),
		  (val_add, ":stat_position_x", 15),
          (position_set_x, pos1, ":stat_position_x"),
          (position_set_y, pos1, ":stat_position_y"),
          (overlay_set_position, "$g_presentation_obj_battle_but8", pos1),
          (val_add, ":stat_position_y", -40),
		  (val_add, ":stat_position_x", -15),

          (position_set_x, pos1, 32650),
          (position_set_y, pos1, 2000),
          (overlay_set_size, "$g_presentation_obj_battle_but8", pos1),
          (overlay_set_alpha, "$g_presentation_obj_battle_but8", 0),
          (overlay_set_color, "$g_presentation_obj_battle_but8", 0xFFFF00),

          (create_check_box_overlay, "$g_presentation_obj_battle_check8", "mesh_checkbox_off", "mesh_checkbox_on"),          
          (position_set_x, pos2, ":stat_position_check_x"),
          (position_set_y, pos2, ":stat_position_check_y"),
          (overlay_set_position, "$g_presentation_obj_battle_check8", pos2),
          (val_add, ":stat_position_check_y", -40),        

		  (str_store_class_name, s7, 8),
          (create_text_overlay, "$g_presentation_obj_battle_name8", s7, 0),
          (position_set_x, pos3, ":stat_position_name_x"),
          (position_set_y, pos3, ":stat_position_name_y"),
          (overlay_set_position, "$g_presentation_obj_battle_name8", pos3),
          (val_add, ":stat_position_name_y", -40),

          (create_text_overlay, "$g_presentation_but8_movement", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but8_riding", "str_space", tf_center_justify),
          (create_text_overlay, "$g_presentation_but8_weapon_usage", "str_space", tf_center_justify),
		  (create_text_overlay, reg(14), "str_space", tf_center_justify), #Formations
		  
		  (create_text_overlay, reg(23), "str_space", tf_center_justify), #Native Weapon
		  (create_text_overlay, reg(32), "str_space", tf_center_justify), #Caba'drin Weapon
		  (create_text_overlay, reg(41), "str_space", tf_center_justify), #Caba'drin Shield	 
          (create_text_overlay, reg(50), "str_space", tf_center_justify), #Caba'drin Skirmish	
		  
		  (position_set_x, pos1, 950),
		  (position_set_y, pos1, 950),
		  (overlay_set_size, "$g_presentation_but8_movement", pos1),
		  (overlay_set_size, "$g_presentation_but8_riding", pos1),
		  (overlay_set_size, "$g_presentation_but8_weapon_usage", pos1),
		  (overlay_set_size, reg(14), pos1),
		  (overlay_set_size, reg(23), pos1),
          (overlay_set_size, reg(32), pos1),
		  (overlay_set_size, reg(41), pos1),
		  (overlay_set_size, reg(50), pos1),
		  
		  (overlay_set_display, reg(23), 0),
		  (overlay_set_display, reg(32), 0),
		  (overlay_set_display, reg(41), 0),
          (overlay_set_display, reg(50), 0),		  
		  
		  (position_set_y, pos1, ":stat_position_order_y"),
          (position_set_x, pos1, 225),
          (overlay_set_position, "$g_presentation_but8_movement", pos1),
          (position_set_x, pos1, 355), #350 ; 380
          (overlay_set_position, "$g_presentation_but8_riding", pos1),
          (position_set_x, pos1, 485), #475 ; 500
          (overlay_set_position, "$g_presentation_but8_weapon_usage", pos1),
		  (position_set_x, pos1, 605),
          (overlay_set_position, reg(14), pos1),
		  
		  (position_set_x, pos1, 225),
          (overlay_set_position, reg(23), pos1),
		  (position_set_x, pos1, 355), #350
          (overlay_set_position, reg(32), pos1),
          (position_set_x, pos1, 485), #475
          (overlay_set_position, reg(41), pos1),
		  (position_set_x, pos1, 605), #600 
		  (overlay_set_position, reg(50), pos1),
          (val_add, ":stat_position_order_y", -40),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_9", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_9", pos1),
		  
		  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_19", "str_space"),
		  #(overlay_set_color, "$g_presentation_credits_obj_1", 0xAAAAAA),
		  (position_set_x, pos1, 600),
          (position_set_y, pos1, 600),
          (overlay_set_size, "$g_presentation_obj_custom_battle_designer_19", pos1),
        (try_end),
		
		(assign, ":y_position_for_order_buttons", 640),
        (assign, ":addition_y_position", "$num_classes"),
        (val_mul, ":addition_y_position", -40),
        (val_add, ":y_position_for_order_buttons", ":addition_y_position"),
		(val_sub, ":y_position_for_order_buttons", 50),

        (create_listbox_overlay, "$g_presentation_obj_battle_10", "str_space", 0), #Positioning
        (create_listbox_overlay, "$g_presentation_obj_battle_11", "str_space", 0), #Movement
        (create_listbox_overlay, "$g_presentation_obj_battle_12", "str_space", 0), #Duplicate movement
		(create_listbox_overlay, "$g_presentation_obj_battle_17", "str_space", 0), #Formations
        (create_listbox_overlay, "$g_presentation_obj_battle_13", "str_space", 0), #Native Weapon
		(create_listbox_overlay, "$g_presentation_obj_battle_14", "str_space", 0), #Caba'drin Weapon Type
		(create_listbox_overlay, "$g_presentation_obj_battle_15", "str_space", 0), #Caba'drin Shield
		(create_listbox_overlay, "$g_presentation_obj_battle_16", "str_space", 0), #Caba'drin Skirmish
        
        (overlay_add_item, "$g_presentation_obj_battle_10", "@Stand Ground"),
        (overlay_add_item, "$g_presentation_obj_battle_10", "@Charge"),
        (overlay_add_item, "$g_presentation_obj_battle_10", "@Follow Me"),
        (overlay_add_item, "$g_presentation_obj_battle_10", "@Hold Position"),
		(overlay_add_item, "$g_presentation_obj_battle_10", "@None"),
       
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 600),
        (overlay_set_size, "$g_presentation_obj_battle_10", pos1),

        (position_set_x, pos1, 170),
        (position_set_y, pos1, ":y_position_for_order_buttons"),
        (overlay_set_position, "$g_presentation_obj_battle_10", pos1),
		(overlay_set_color, "$g_presentation_obj_battle_10", 0xFF0000),
        (overlay_set_alpha, "$g_presentation_obj_battle_10", 0x60),
        (overlay_set_val, "$g_presentation_obj_battle_10", 4),
		

        (overlay_add_item, "$g_presentation_obj_battle_11", "@Dismount"),
        (overlay_add_item, "$g_presentation_obj_battle_11", "@Mount"),
		(overlay_add_item, "$g_presentation_obj_battle_11", "@Spread Out"),
        (overlay_add_item, "$g_presentation_obj_battle_11", "@Stand Closer"),
        (overlay_add_item, "$g_presentation_obj_battle_11", "@Back 10"),
        (overlay_add_item, "$g_presentation_obj_battle_11", "@Forward 10"),
		(overlay_add_item, "$g_presentation_obj_battle_11", "@None"),
        
        (position_set_x, pos1, 500), #500
        (position_set_y, pos1, 600),
        (overlay_set_size, "$g_presentation_obj_battle_11", pos1),

        (position_set_x, pos1, 305), #290 ; 320 ; 340
		(val_add, ":y_position_for_order_buttons", -35),
        (position_set_y, pos1, ":y_position_for_order_buttons"),
        (overlay_set_position, "$g_presentation_obj_battle_11", pos1),
        (overlay_set_color, "$g_presentation_obj_battle_11", 0xFF6600),
        (overlay_set_alpha, "$g_presentation_obj_battle_11", 0x60),
        (overlay_set_val, "$g_presentation_obj_battle_11", 6),

		(val_add, ":y_position_for_order_buttons", -50),		
		(create_number_box_overlay, reg(51), 1, 5), #Repeat 1
		(create_number_box_overlay, reg(52), 1, 5), #Repeat 1
		(overlay_set_val, reg(51), 1),
		(overlay_set_val, reg(52), 1),
		(position_set_x, pos1, 320), #315 ; 355
        (position_set_y, pos1, ":y_position_for_order_buttons"),
		(overlay_set_position, reg(51), pos1),		
		(position_set_x, pos1, 452), #437 ; 520
		(overlay_set_position, reg(52), pos1),
		(assign, reg53, 0), #Repeat 1 holder
		(assign, reg54, 0), #Repeat 2 holder
		
		(create_text_overlay, reg0, "@Repeat x"),
		(position_set_x, pos1, 900),
		(position_set_y, pos1, 900),
		(overlay_set_size, reg0, pos1),
		(position_set_x, pos1, 295), #285 ; 325
		(val_add, ":y_position_for_order_buttons", 25),
		(position_set_y, pos1, ":y_position_for_order_buttons"),
		(overlay_set_position, reg0, pos1),
		(create_text_overlay, reg0, "@Repeat x"),
		(position_set_x, pos1, 900),
		(position_set_y, pos1, 900),
		(overlay_set_size, reg0, pos1),
		(position_set_x, pos1, 422), #407 ; 497
		(position_set_y, pos1, ":y_position_for_order_buttons"),
		(overlay_set_position, reg0, pos1),
		(val_add, ":y_position_for_order_buttons", 25),

        (overlay_add_item, "$g_presentation_obj_battle_12", "@Dismount"),
        (overlay_add_item, "$g_presentation_obj_battle_12", "@Mount"),
		(overlay_add_item, "$g_presentation_obj_battle_12", "@Spread Out"),
        (overlay_add_item, "$g_presentation_obj_battle_12", "@Stand Closer"),
        (overlay_add_item, "$g_presentation_obj_battle_12", "@Back 10"),
        (overlay_add_item, "$g_presentation_obj_battle_12", "@Forward 10"),
		(overlay_add_item, "$g_presentation_obj_battle_12", "@None"),
		
        (position_set_x, pos1, 500), #500
        (position_set_y, pos1, 600),
        (overlay_set_size, "$g_presentation_obj_battle_12", pos1),

        (position_set_x, pos1, 430), #410 ; 450 ; 510
        (position_set_y, pos1, ":y_position_for_order_buttons"),
        (overlay_set_position, "$g_presentation_obj_battle_12", pos1),
        (overlay_set_color, "$g_presentation_obj_battle_12", 0xFF6600),
        (overlay_set_alpha, "$g_presentation_obj_battle_12", 0x60),
        (overlay_set_val, "$g_presentation_obj_battle_12", 6),
		(val_add, ":y_position_for_order_buttons", 35), 
		
		
		(overlay_add_item, "$g_presentation_obj_battle_17", "@Square"),
        (overlay_add_item, "$g_presentation_obj_battle_17", "@Wedge"),
        (overlay_add_item, "$g_presentation_obj_battle_17", "@Shieldwall"),
        (overlay_add_item, "$g_presentation_obj_battle_17", "@Ranks"),
		(overlay_add_item, "$g_presentation_obj_battle_17", "@None"),
		
        (position_set_x, pos1, 500), #500
        (position_set_y, pos1, 600),
        (overlay_set_size, "$g_presentation_obj_battle_17", pos1),

        (position_set_x, pos1, 555), #410 ; 450
        (position_set_y, pos1, ":y_position_for_order_buttons"),
        (overlay_set_position, "$g_presentation_obj_battle_17", pos1),
        (overlay_set_color, "$g_presentation_obj_battle_17", 0xFF6600),
        (overlay_set_alpha, "$g_presentation_obj_battle_17", 0x60),
        (overlay_set_val, "$g_presentation_obj_battle_17", 4),
		#(val_add, ":y_position_for_order_buttons", 35), 
		

        (overlay_add_item, "$g_presentation_obj_battle_13", "@Fire At Will"),
        (overlay_add_item, "$g_presentation_obj_battle_13", "@Hold Your Fire"),
        (overlay_add_item, "$g_presentation_obj_battle_13", "@Use Blunt Weapons"),
        (overlay_add_item, "$g_presentation_obj_battle_13", "@Use Any Weapon"),
		(overlay_add_item, "$g_presentation_obj_battle_13", "@None"),
        
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 600),
        (overlay_set_size, "$g_presentation_obj_battle_13", pos1),
        (position_set_x, pos1, 175), #530 ; 170
        (position_set_y, pos1, ":y_position_for_order_buttons"),
        (overlay_set_position, "$g_presentation_obj_battle_13", pos1),
        (overlay_set_alpha, "$g_presentation_obj_battle_13", 0x60),
        (overlay_set_val, "$g_presentation_obj_battle_13", 4),
		(overlay_set_display, "$g_presentation_obj_battle_13", 0),		
		
		(overlay_add_item, "$g_presentation_obj_battle_14", "@Ranged"),
        (overlay_add_item, "$g_presentation_obj_battle_14", "@Polearms"),
        (overlay_add_item, "$g_presentation_obj_battle_14", "@Two Handed"),
        (overlay_add_item, "$g_presentation_obj_battle_14", "@One Handed"),
		(overlay_add_item, "$g_presentation_obj_battle_14", "@None"),
        
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 600),
        (overlay_set_size, "$g_presentation_obj_battle_14", pos1),
        (position_set_x, pos1, 305), #290
        (position_set_y, pos1, ":y_position_for_order_buttons"),
        (overlay_set_position, "$g_presentation_obj_battle_14", pos1),
        (overlay_set_alpha, "$g_presentation_obj_battle_14", 0x60),
        (overlay_set_val, "$g_presentation_obj_battle_14", 4),
		(overlay_set_display, "$g_presentation_obj_battle_14", 0),
		
        (overlay_add_item, "$g_presentation_obj_battle_15", "@No Shields"),
        (overlay_add_item, "$g_presentation_obj_battle_15", "@Use Shields"),
		(overlay_add_item, "$g_presentation_obj_battle_15", "@None"),
        
		(val_add, ":y_position_for_order_buttons", 35),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 600),
        (overlay_set_size, "$g_presentation_obj_battle_15", pos1),
        (position_set_x, pos1, 430), #410
        (position_set_y, pos1, ":y_position_for_order_buttons"),
        (overlay_set_position, "$g_presentation_obj_battle_15", pos1),
        (overlay_set_alpha, "$g_presentation_obj_battle_15", 0x60),
        (overlay_set_val, "$g_presentation_obj_battle_15", 2),
		(overlay_set_display, "$g_presentation_obj_battle_15", 0),
		
		#(overlay_add_item, "$g_presentation_obj_battle_16", "@Melee"),
        (overlay_add_item, "$g_presentation_obj_battle_16", "@Avoid Melee"),
		(overlay_add_item, "$g_presentation_obj_battle_16", "@None"),
        
		(val_add, ":y_position_for_order_buttons", 18),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 600),
        (overlay_set_size, "$g_presentation_obj_battle_16", pos1),
        (position_set_x, pos1, 555), #495 ; 530
        (position_set_y, pos1, ":y_position_for_order_buttons"),
        (overlay_set_position, "$g_presentation_obj_battle_16", pos1),
        (overlay_set_alpha, "$g_presentation_obj_battle_16", 0x60),
        (overlay_set_val, "$g_presentation_obj_battle_16", 1),
		(overlay_set_display, "$g_presentation_obj_battle_16", 0),
		
		(val_sub, ":y_position_for_order_buttons", 53),
		
		(val_sub, ":y_position_for_order_buttons", 50),
		(create_button_overlay, "$g_presentation_obj_battle_24", "@Turn to weapon orders..."),
		(position_set_x, pos1, 900),
		(position_set_y, pos1, 900),
		(overlay_set_size, "$g_presentation_obj_battle_24", pos1),
		(position_set_x, pos1, 450), #500
        #(position_set_y, pos1, ":y_position_for_order_buttons"),
		(position_set_y, pos1, 150),
		(overlay_set_position,  "$g_presentation_obj_battle_24", pos1),	
		
		
		(create_game_button_overlay, "$g_presentation_obj_battle_25", "@Reassess"), 
        (position_set_x, pos1, 420),
        (position_set_y, pos1, 8),
        (overlay_set_position, "$g_presentation_obj_battle_25", pos1),
		
		(create_game_button_overlay, "$g_presentation_obj_battle_26", "@Scrap All"), 
        (position_set_x, pos1, 580),
        (position_set_y, pos1, 8),
        (overlay_set_position, "$g_presentation_obj_battle_26", pos1),
		
		(create_game_button_overlay, "$g_presentation_obj_battle_27", "@Prepare Orders"),
        (position_set_x, pos1, 740),
        (position_set_y, pos1, 8),
        (overlay_set_position, "$g_presentation_obj_battle_27", pos1),
		
		(create_game_button_overlay, "$g_presentation_obj_battle_28", "@Dispatch Orders"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 8),
        (overlay_set_position, "$g_presentation_obj_battle_28", pos1),
				
		(call_script, "script_prebattle_order_get_stored"),
						
		(presentation_set_duration, 999999),
        ]),
		
     (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
		
		(try_begin), #Buttons
			(eq, ":object", "$g_presentation_obj_battle_25"),
			(jump_to_menu, "$g_next_menu"),
			(presentation_set_duration, 0),
		(else_try),
		    (eq, ":object", "$g_presentation_obj_battle_26"),
			(party_set_slot, "p_main_party", slot_party_prebattle_plan, 0),
			(call_script, "script_prebattle_order_clear_all"),
		(else_try),
		    (eq, ":object", "$g_presentation_obj_battle_27"),
			(call_script, "script_prebattle_order_preview_orders"),
		(else_try),
		    (eq, ":object", "$g_presentation_obj_battle_28"),
			(party_set_slot, "p_main_party", slot_party_prebattle_plan, 1),
			(call_script, "script_prebattle_order_store_orders"),
			(jump_to_menu, "$g_next_menu"),
			(presentation_set_duration, 0),
		(else_try),
		    (eq, ":object", "$g_presentation_obj_battle_24"),
			(overlay_get_position, pos1, "$g_presentation_obj_battle_24"),
			(position_get_x, ":x", pos1),
			(try_begin),
			    (eq, ":x", 450),
				#clear movement order overlays
				(overlay_set_display, "$g_presentation_obj_battle_10", 0), #Order Selection Boxes
				(overlay_set_display, "$g_presentation_obj_battle_11", 0),
				(overlay_set_display, "$g_presentation_obj_battle_12", 0),
				(overlay_set_display, "$g_presentation_obj_battle_17", 0),
				(overlay_set_display,                         reg(51), 0), #Repeat Boxes
				(overlay_set_display,                         reg(52), 0),
				(overlay_set_display, "$g_presentation_credits_obj_2", 0), #Headings
				(overlay_set_display, "$g_presentation_credits_obj_3", 0),
				(overlay_set_display, "$g_presentation_credits_obj_4", 0),
				(overlay_set_display, "$g_presentation_credits_obj_5", 0),
				(store_add, ":overlay", reg(51), 2),
				(overlay_set_display,                      ":overlay", 0),
				(val_add, ":overlay", 1),
				(overlay_set_display,                      ":overlay", 0),
				#(overlay_set_display, "$g_presentation_credits_obj_5", 0),
				#display weapon order overlays
				(overlay_set_display, "$g_presentation_obj_battle_13", 1), #Order Selection Boxes
				(overlay_set_display, "$g_presentation_obj_battle_14", 1),
				(overlay_set_display, "$g_presentation_obj_battle_15", 1),
				(overlay_set_display, "$g_presentation_obj_battle_16", 1),
				(overlay_set_display, "$g_presentation_credits_obj_6", 1), #Headings
				(overlay_set_display, "$g_presentation_credits_obj_7", 1), 
				(overlay_set_display, "$g_presentation_credits_obj_8", 1),
				(overlay_set_display, "$g_presentation_credits_obj_9", 1),
				(try_begin), #Toggle by Division order display
				    (eq, "$group0_has_troops", 1),
                    (overlay_set_display, "$g_presentation_but0_movement", 0), #Initial
                    (overlay_set_display, "$g_presentation_but0_riding", 0), #Position 1
                    (overlay_set_display, "$g_presentation_but0_weapon_usage", 0), #Position 2
					(overlay_set_display, reg(6), 0),  #Formation
		            (overlay_set_display, reg(15), 1), #Native Weapon
					(overlay_set_display, reg(24), 1), #Caba'drin Weapon
					(overlay_set_display, reg(33), 1), #Caba'drin Shield
					(overlay_set_display, reg(42), 1), #Caba'drin Skirmish
				(try_end),
				(try_begin),
				    (eq, "$group1_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but1_movement", 0), #Initial
                    (overlay_set_display, "$g_presentation_but1_riding", 0), #Position 1
                    (overlay_set_display, "$g_presentation_but1_weapon_usage", 0), #Position 2
					(overlay_set_display, reg(7), 0),  #Formation
		            (overlay_set_display, reg(16), 1), #Native Weapon
					(overlay_set_display, reg(25), 1), #Caba'drin Weapon
					(overlay_set_display, reg(34), 1), #Caba'drin Shield
					(overlay_set_display, reg(43), 1), #Caba'drin Skirmish
				(try_end),
				(try_begin),
				    (eq, "$group2_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but2_movement", 0), #Initial
                    (overlay_set_display, "$g_presentation_but2_riding", 0), #Position 1
                    (overlay_set_display, "$g_presentation_but2_weapon_usage", 0), #Position 2
					(overlay_set_display, reg(8), 0),  #Formation
		            (overlay_set_display, reg(17), 1), #Native Weapon
					(overlay_set_display, reg(26), 1), #Caba'drin Weapon
					(overlay_set_display, reg(35), 1), #Caba'drin Shield
					(overlay_set_display, reg(44), 1), #Caba'drin Skirmish
				(try_end),
				(try_begin),
				    (eq, "$group3_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but3_movement", 0), #Initial
                    (overlay_set_display, "$g_presentation_but3_riding", 0), #Position 1
                    (overlay_set_display, "$g_presentation_but3_weapon_usage", 0), #Position 2
					(overlay_set_display, reg(9), 0),  #Formation
		            (overlay_set_display, reg(18), 1), #Native Weapon
					(overlay_set_display, reg(27), 1), #Caba'drin Weapon
					(overlay_set_display, reg(36), 1), #Caba'drin Shield
					(overlay_set_display, reg(45), 1), #Caba'drin Skirmish
				(try_end),
				(try_begin),
				    (eq, "$group4_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but4_movement", 0), #Initial
                    (overlay_set_display, "$g_presentation_but4_riding", 0), #Position 1
                    (overlay_set_display, "$g_presentation_but4_weapon_usage", 0), #Position 2
					(overlay_set_display, reg(10), 0),  #Formation
		            (overlay_set_display, reg(19), 1), #Native Weapon
					(overlay_set_display, reg(28), 1), #Caba'drin Weapon
					(overlay_set_display, reg(37), 1), #Caba'drin Shield
					(overlay_set_display, reg(46), 1), #Caba'drin Skirmish
				(try_end),
				(try_begin),
				    (eq, "$group5_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but5_movement", 0), #Initial
                    (overlay_set_display, "$g_presentation_but5_riding", 0), #Position 1
                    (overlay_set_display, "$g_presentation_but5_weapon_usage", 0), #Position 2
					(overlay_set_display, reg(11), 0),  #Formation
		            (overlay_set_display, reg(20), 1), #Native Weapon
					(overlay_set_display, reg(29), 1), #Caba'drin Weapon
					(overlay_set_display, reg(38), 1), #Caba'drin Shield
					(overlay_set_display, reg(47), 1), #Caba'drin Skirmish
				(try_end),
				(try_begin),
				    (eq, "$group6_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but6_movement", 0), #Initial
                    (overlay_set_display, "$g_presentation_but6_riding", 0), #Position 1
                    (overlay_set_display, "$g_presentation_but6_weapon_usage", 0), #Position 2
					(overlay_set_display, reg(12), 0),  #Formation
		            (overlay_set_display, reg(21), 1), #Native Weapon
					(overlay_set_display, reg(30), 1), #Caba'drin Weapon
					(overlay_set_display, reg(39), 1), #Caba'drin Shield
					(overlay_set_display, reg(48), 1), #Caba'drin Skirmish
				(try_end),
				(try_begin),
				    (eq, "$group7_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but7_movement", 0), #Initial
                    (overlay_set_display, "$g_presentation_but7_riding", 0), #Position 1
                    (overlay_set_display, "$g_presentation_but7_weapon_usage", 0), #Position 2
					(overlay_set_display, reg(13), 0),  #Formation
		            (overlay_set_display, reg(22), 1), #Native Weapon
					(overlay_set_display, reg(31), 1), #Caba'drin Weapon
					(overlay_set_display, reg(40), 1), #Caba'drin Shield
					(overlay_set_display, reg(49), 1), #Caba'drin Skirmish
				(try_end),
				(try_begin),
				    (eq, "$group8_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but8_movement", 0), #Initial
                    (overlay_set_display, "$g_presentation_but8_riding", 0), #Position 1
                    (overlay_set_display, "$g_presentation_but8_weapon_usage", 0), #Position 2
					(overlay_set_display, reg(14), 0),  #Formation
		            (overlay_set_display, reg(23), 1), #Native Weapon
					(overlay_set_display, reg(32), 1), #Caba'drin Weapon
					(overlay_set_display, reg(41), 1), #Caba'drin Shield
					(overlay_set_display, reg(50), 1), #Caba'drin Skirmish
				(try_end),
				(position_set_x, pos1, 150),
				(overlay_set_text, "$g_presentation_obj_battle_24", "@...Turn to positioning orders"),
				(overlay_set_position, "$g_presentation_obj_battle_24", pos1),
			(else_try),
			    (eq, ":x", 150),
				#clear weapon order overlays
				(overlay_set_display, "$g_presentation_obj_battle_13", 0), #Order Selection Boxes
				(overlay_set_display, "$g_presentation_obj_battle_14", 0),
				(overlay_set_display, "$g_presentation_obj_battle_15", 0),
				(overlay_set_display, "$g_presentation_obj_battle_16", 0),
				(overlay_set_display, "$g_presentation_credits_obj_6", 0), #Headings
				(overlay_set_display, "$g_presentation_credits_obj_7", 0), 
				(overlay_set_display, "$g_presentation_credits_obj_8", 0),
				(overlay_set_display, "$g_presentation_credits_obj_9", 0),
				#display movement order overlays
				(overlay_set_display, "$g_presentation_obj_battle_10", 1), #Order Selection Boxes
				(overlay_set_display, "$g_presentation_obj_battle_11", 1),
				(overlay_set_display, "$g_presentation_obj_battle_12", 1),
				(overlay_set_display, "$g_presentation_obj_battle_17", 1),
				(overlay_set_display,                         reg(51), 1), #Repeat Boxes
				(overlay_set_display,                         reg(52), 1),
				(overlay_set_display, "$g_presentation_credits_obj_2", 1), #Headings
				(overlay_set_display, "$g_presentation_credits_obj_3", 1),
				(overlay_set_display, "$g_presentation_credits_obj_4", 1),
				(overlay_set_display, "$g_presentation_credits_obj_5", 1),
				(store_add, ":overlay", reg(51), 2),
				(overlay_set_display,                      ":overlay", 1),
				(val_add, ":overlay", 1),
				(overlay_set_display,                      ":overlay", 1),
				#(overlay_set_display, "$g_presentation_credits_obj_5", 1),
				(try_begin), #Toggle by Division order display
				    (eq, "$group0_has_troops", 1),
                    (overlay_set_display, "$g_presentation_but0_movement", 1), #Initial
                    (overlay_set_display, "$g_presentation_but0_riding", 1), #Position 1
                    (overlay_set_display, "$g_presentation_but0_weapon_usage", 1), #Position 2
					(overlay_set_display, reg(6), 1),  #Formation
		            (overlay_set_display, reg(15), 0), #Native Weapon
					(overlay_set_display, reg(24), 0), #Caba'drin Weapon
					(overlay_set_display, reg(33), 0), #Caba'drin Shield
					(overlay_set_display, reg(42), 0), #Caba'drin Skirmish
				(try_end),
				(try_begin),
					(eq, "$group1_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but1_movement", 1), #Initial
                    (overlay_set_display, "$g_presentation_but1_riding", 1), #Position 1
                    (overlay_set_display, "$g_presentation_but1_weapon_usage", 1), #Position 2
					(overlay_set_display, reg(7), 1),  #Formation
		            (overlay_set_display, reg(16), 0), #Native Weapon
					(overlay_set_display, reg(25), 0), #Caba'drin Weapon
					(overlay_set_display, reg(34), 0), #Caba'drin Shield
					(overlay_set_display, reg(43), 0), #Caba'drin Skirmish
				(try_end),
				(try_begin),
					(eq, "$group2_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but2_movement", 1), #Initial
                    (overlay_set_display, "$g_presentation_but2_riding", 1), #Position 1
                    (overlay_set_display, "$g_presentation_but2_weapon_usage", 1), #Position 2
					(overlay_set_display, reg(8), 1),  #Formation
		            (overlay_set_display, reg(17), 0), #Native Weapon
					(overlay_set_display, reg(26), 0), #Caba'drin Weapon
					(overlay_set_display, reg(35), 0), #Caba'drin Shield
					(overlay_set_display, reg(44), 0), #Caba'drin Skirmish
				(try_end),
				(try_begin),
				    (eq, "$group3_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but3_movement", 1), #Initial
                    (overlay_set_display, "$g_presentation_but3_riding", 1), #Position 1
                    (overlay_set_display, "$g_presentation_but3_weapon_usage", 1), #Position 2
					(overlay_set_display, reg(9), 1),  #Formation
		            (overlay_set_display, reg(18), 0), #Native Weapon
					(overlay_set_display, reg(27), 0), #Caba'drin Weapon
					(overlay_set_display, reg(36), 0), #Caba'drin Shield
					(overlay_set_display, reg(45), 0), #Caba'drin Skirmish
				(try_end),
				(try_begin),
				    (eq, "$group4_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but4_movement", 1), #Initial
                    (overlay_set_display, "$g_presentation_but4_riding", 1), #Position 1
                    (overlay_set_display, "$g_presentation_but4_weapon_usage", 1), #Position 2
					(overlay_set_display, reg(10), 1),  #Formation
		            (overlay_set_display, reg(19), 0), #Native Weapon
					(overlay_set_display, reg(28), 0), #Caba'drin Weapon
					(overlay_set_display, reg(37), 0), #Caba'drin Shield
					(overlay_set_display, reg(46), 0), #Caba'drin Skirmish
				(try_end),
				(try_begin),
				    (eq, "$group5_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but5_movement", 1), #Initial
                    (overlay_set_display, "$g_presentation_but5_riding", 1), #Position 1
                    (overlay_set_display, "$g_presentation_but5_weapon_usage", 1), #Position 2
					(overlay_set_display, reg(11), 1),  #Formation
		            (overlay_set_display, reg(20), 0), #Native Weapon
					(overlay_set_display, reg(29), 0), #Caba'drin Weapon
					(overlay_set_display, reg(38), 0), #Caba'drin Shield
					(overlay_set_display, reg(47), 0), #Caba'drin Skirmish
				(try_end),
				(try_begin),
				    (eq, "$group6_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but6_movement", 1), #Initial
                    (overlay_set_display, "$g_presentation_but6_riding", 1), #Position 1
                    (overlay_set_display, "$g_presentation_but6_weapon_usage", 1), #Position 2
					(overlay_set_display, reg(12), 1),  #Formation
		            (overlay_set_display, reg(21), 0), #Native Weapon
					(overlay_set_display, reg(30), 0), #Caba'drin Weapon
					(overlay_set_display, reg(39), 0), #Caba'drin Shield
					(overlay_set_display, reg(48), 0), #Caba'drin Skirmish
				(try_end),
				(try_begin),
				    (eq, "$group7_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but7_movement", 1), #Initial
                    (overlay_set_display, "$g_presentation_but7_riding", 1), #Position 1
                    (overlay_set_display, "$g_presentation_but7_weapon_usage", 1), #Position 2
					(overlay_set_display, reg(13), 1),  #Formation
		            (overlay_set_display, reg(22), 0), #Native Weapon
					(overlay_set_display, reg(31), 0), #Caba'drin Weapon
					(overlay_set_display, reg(40), 0), #Caba'drin Shield
					(overlay_set_display, reg(49), 0), #Caba'drin Skirmish
				(try_end),
				(try_begin),
				    (eq, "$group8_has_troops", 1),
				    (overlay_set_display, "$g_presentation_but8_movement", 1), #Initial
                    (overlay_set_display, "$g_presentation_but8_riding", 1), #Position 1
                    (overlay_set_display, "$g_presentation_but8_weapon_usage", 1), #Position 2
					(overlay_set_display, reg(14), 1),  #Formation
		            (overlay_set_display, reg(23), 0), #Native Weapon
					(overlay_set_display, reg(32), 0), #Caba'drin Weapon
					(overlay_set_display, reg(41), 0), #Caba'drin Shield
					(overlay_set_display, reg(50), 0), #Caba'drin Skirmish
				(try_end),
				(position_set_x, pos1, 450),
				(overlay_set_text, "$g_presentation_obj_battle_24", "@Turn to weapon orders..."),
				(overlay_set_position, "$g_presentation_obj_battle_24", pos1),
			(try_end),			
	    (else_try), #Division Selection, Order Selection
          (eq, "$group0_has_troops", 1),
          (eq, ":object", "$g_presentation_obj_battle_check0"),
          (assign, "$g_formation_group0_selected", ":value"),
          (try_begin),
            (eq, ":value", 1),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but0", 250, 0x44),
          (else_try),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but0", 250, 0),
          (try_end),
        (else_try),
          (eq, "$group1_has_troops", 1),
          (eq, ":object", "$g_presentation_obj_battle_check1"),
          (assign, "$g_formation_group1_selected", ":value"),
          (try_begin),
            (eq, ":value", 1),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but1", 250, 0x44),
          (else_try),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but1", 250, 0),
          (try_end),
        (else_try),
          (eq, "$group2_has_troops", 1),
          (eq, ":object", "$g_presentation_obj_battle_check2"),
          (assign, "$g_formation_group2_selected", ":value"),
          (try_begin),
            (eq, ":value", 1),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but2", 250, 0x44),
          (else_try),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but2", 250, 0),
          (try_end),
        (else_try),
          (eq, "$group3_has_troops", 1),
          (eq, ":object", "$g_presentation_obj_battle_check3"),
          (assign, "$g_formation_group3_selected", ":value"),
          (try_begin),
            (eq, ":value", 1),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but3", 250, 0x44),
          (else_try),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but3", 250, 0),
          (try_end),
        (else_try),
          (eq, "$group4_has_troops", 1),
          (eq, ":object", "$g_presentation_obj_battle_check4"),
          (assign, "$g_formation_group4_selected", ":value"),
          (try_begin),
            (eq, ":value", 1),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but4", 250, 0x44),
          (else_try),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but4", 250, 0),
          (try_end),
        (else_try),
          (eq, "$group5_has_troops", 1),
          (eq, ":object", "$g_presentation_obj_battle_check5"),
          (assign, "$g_formation_group5_selected", ":value"),
          (try_begin),
            (eq, ":value", 1),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but5", 250, 0x44),
          (else_try),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but5", 250, 0),
          (try_end),
        (else_try),
          (eq, "$group6_has_troops", 1),
          (eq, ":object", "$g_presentation_obj_battle_check6"),
          (assign, "$g_formation_group6_selected", ":value"),
          (try_begin),
            (eq, ":value", 1),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but6", 250, 0x44),
          (else_try),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but6", 250, 0),
          (try_end),
        (else_try),
          (eq, "$group7_has_troops", 1),
          (eq, ":object", "$g_presentation_obj_battle_check7"),
          (assign, "$g_formation_group7_selected", ":value"),
          (try_begin),
            (eq, ":value", 1),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but7", 250, 0x44),
          (else_try),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but7", 250, 0),
          (try_end),
        (else_try),
          (eq, "$group8_has_troops", 1),
          (eq, ":object", "$g_presentation_obj_battle_check8"),
          (assign, "$g_formation_group8_selected", ":value"),
          (try_begin),
            (eq, ":value", 1),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but8", 250, 0x44),
          (else_try),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but8", 250, 0),
          (try_end),        
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but0"),
        
          (assign, "$g_formation_group0_selected", 1),
          (overlay_animate_to_alpha, "$g_presentation_obj_battle_but0", 250, 0x44),
          (overlay_set_val, "$g_presentation_obj_battle_check0", 1),

          (try_begin),
            (eq, "$group1_has_troops", 1),
            (assign, "$g_formation_group1_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check1", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but1", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group2_has_troops", 1),
            (assign, "$g_formation_group2_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check2", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but2", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group3_has_troops", 1),
            (assign, "$g_formation_group3_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check3", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but3", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group4_has_troops", 1),
            (assign, "$g_formation_group4_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check4", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but4", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group5_has_troops", 1),
            (assign, "$g_formation_group5_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check5", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but5", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group6_has_troops", 1),
            (assign, "$g_formation_group6_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check6", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but6", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group7_has_troops", 1),
            (assign, "$g_formation_group7_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check7", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but7", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group8_has_troops", 1),
            (assign, "$g_formation_group8_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check8", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but8", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but1"),

          (assign, "$g_formation_group1_selected", 1),
          (overlay_animate_to_alpha, "$g_presentation_obj_battle_but1", 250, 0x44),
          (overlay_set_val, "$g_presentation_obj_battle_check1", 1),

          (try_begin),
            (eq, "$group0_has_troops", 1),
            (assign, "$g_formation_group0_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check0", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but0", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group2_has_troops", 1),
            (assign, "$g_formation_group2_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check2", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but2", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group3_has_troops", 1),
            (assign, "$g_formation_group3_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check3", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but3", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group4_has_troops", 1),
            (assign, "$g_formation_group4_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check4", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but4", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group5_has_troops", 1),
            (assign, "$g_formation_group5_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check5", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but5", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group6_has_troops", 1),
            (assign, "$g_formation_group6_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check6", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but6", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group7_has_troops", 1),
            (assign, "$g_formation_group7_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check7", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but7", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group8_has_troops", 1),
            (assign, "$g_formation_group8_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check8", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but8", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but2"),

          (assign, "$g_formation_group2_selected", 1),
          (overlay_animate_to_alpha, "$g_presentation_obj_battle_but2", 250, 0x44),
          (overlay_set_val, "$g_presentation_obj_battle_check2", 1),

          (try_begin),
            (eq, "$group0_has_troops", 1),
            (assign, "$g_formation_group0_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check0", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but0", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group1_has_troops", 1),
            (assign, "$g_formation_group1_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check1", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but1", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group3_has_troops", 1),
            (assign, "$g_formation_group3_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check3", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but3", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group4_has_troops", 1),
            (assign, "$g_formation_group4_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check4", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but4", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group5_has_troops", 1),
            (assign, "$g_formation_group5_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check5", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but5", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group6_has_troops", 1),
            (assign, "$g_formation_group6_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check6", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but6", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group7_has_troops", 1),
            (assign, "$g_formation_group7_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check7", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but7", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group8_has_troops", 1),
            (assign, "$g_formation_group8_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check8", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but8", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but3"),

          (assign, "$g_formation_group3_selected", 1),
          (overlay_animate_to_alpha, "$g_presentation_obj_battle_but3", 250, 0x44),
          (overlay_set_val, "$g_presentation_obj_battle_check3", 1),

          (try_begin),
            (eq, "$group0_has_troops", 1),
            (assign, "$g_formation_group0_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check0", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but0", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group1_has_troops", 1),
            (assign, "$g_formation_group1_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check1", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but1", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group2_has_troops", 1),
            (assign, "$g_formation_group2_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check2", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but2", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group4_has_troops", 1),
            (assign, "$g_formation_group4_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check4", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but4", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group5_has_troops", 1),
            (assign, "$g_formation_group5_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check5", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but5", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group6_has_troops", 1),
            (assign, "$g_formation_group6_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check6", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but6", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group7_has_troops", 1),
            (assign, "$g_formation_group7_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check7", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but7", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group8_has_troops", 1),
            (assign, "$g_formation_group8_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check8", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but8", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but4"),

          (assign, "$g_formation_group4_selected", 1),
          (overlay_animate_to_alpha, "$g_presentation_obj_battle_but4", 250, 0x44),
          (overlay_set_val, "$g_presentation_obj_battle_check4", 1),

          (try_begin),
            (eq, "$group0_has_troops", 1),
            (assign, "$g_formation_group0_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check0", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but0", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group1_has_troops", 1),
            (assign, "$g_formation_group1_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check1", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but1", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group2_has_troops", 1),
            (assign, "$g_formation_group2_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check2", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but2", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group3_has_troops", 1),
            (assign, "$g_formation_group3_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check3", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but3", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group5_has_troops", 1),
            (assign, "$g_formation_group5_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check5", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but5", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group6_has_troops", 1),
            (assign, "$g_formation_group6_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check6", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but6", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group7_has_troops", 1),
            (assign, "$g_formation_group7_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check7", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but7", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group8_has_troops", 1),
            (assign, "$g_formation_group8_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check8", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but8", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but5"),

          (assign, "$g_formation_group5_selected", 1),
          (overlay_animate_to_alpha, "$g_presentation_obj_battle_but5", 250, 0x44),
          (overlay_set_val, "$g_presentation_obj_battle_check5", 1),

          (try_begin),
            (eq, "$group0_has_troops", 1),
            (assign, "$g_formation_group0_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check0", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but0", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group1_has_troops", 1),
            (assign, "$g_formation_group1_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check1", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but1", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group2_has_troops", 1),
            (assign, "$g_formation_group2_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check2", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but2", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group3_has_troops", 1),
            (assign, "$g_formation_group3_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check3", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but3", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group4_has_troops", 1),
            (assign, "$g_formation_group4_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check4", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but4", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group6_has_troops", 1),
            (assign, "$g_formation_group6_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check6", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but6", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group7_has_troops", 1),
            (assign, "$g_formation_group7_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check7", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but7", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group8_has_troops", 1),
            (assign, "$g_formation_group8_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check8", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but8", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but6"),

          (assign, "$g_formation_group6_selected", 1),
          (overlay_animate_to_alpha, "$g_presentation_obj_battle_but6", 250, 0x44),
          (overlay_set_val, "$g_presentation_obj_battle_check6", 1),

          (try_begin),
            (eq, "$group0_has_troops", 1),
            (assign, "$g_formation_group0_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check0", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but0", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group1_has_troops", 1),
            (assign, "$g_formation_group1_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check1", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but1", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group2_has_troops", 1),
            (assign, "$g_formation_group2_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check2", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but2", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group3_has_troops", 1),
            (assign, "$g_formation_group3_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check3", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but3", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group4_has_troops", 1),
            (assign, "$g_formation_group4_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check4", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but4", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group5_has_troops", 1),
            (assign, "$g_formation_group5_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check5", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but5", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group7_has_troops", 1),
            (assign, "$g_formation_group7_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check7", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but7", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group8_has_troops", 1),
            (assign, "$g_formation_group8_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check8", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but8", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but7"),

          (assign, "$g_formation_group7_selected", 1),
          (overlay_animate_to_alpha, "$g_presentation_obj_battle_but7", 250, 0x44),
          (overlay_set_val, "$g_presentation_obj_battle_check7", 1),

          (try_begin),
            (eq, "$group0_has_troops", 1),
            (assign, "$g_formation_group0_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check0", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but0", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group1_has_troops", 1),
            (assign, "$g_formation_group1_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check1", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but1", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group2_has_troops", 1),
            (assign, "$g_formation_group2_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check2", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but2", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group3_has_troops", 1),
            (assign, "$g_formation_group3_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check3", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but3", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group4_has_troops", 1),
            (assign, "$g_formation_group4_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check4", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but4", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group5_has_troops", 1),
            (assign, "$g_formation_group5_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check5", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but5", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group6_has_troops", 1),
            (assign, "$g_formation_group6_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check6", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but6", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group8_has_troops", 1),
            (assign, "$g_formation_group8_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check8", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but8", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but8"),

          (assign, "$g_formation_group8_selected", 1),
          (overlay_animate_to_alpha, "$g_presentation_obj_battle_but8", 250, 0x44),
          (overlay_set_val, "$g_presentation_obj_battle_check8", 1),

          (try_begin),
            (eq, "$group0_has_troops", 1),
            (assign, "$g_formation_group0_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check0", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but0", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group1_has_troops", 1),
            (assign, "$g_formation_group1_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check1", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but1", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group2_has_troops", 1),
            (assign, "$g_formation_group2_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check2", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but2", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group3_has_troops", 1),
            (assign, "$g_formation_group3_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check3", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but3", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group4_has_troops", 1),
            (assign, "$g_formation_group4_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check4", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but4", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group5_has_troops", 1),
            (assign, "$g_formation_group5_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check5", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but5", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group6_has_troops", 1),
            (assign, "$g_formation_group6_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check6", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but6", 250, 0),
          (try_end),
          (try_begin),
            (eq, "$group7_has_troops", 1),
            (assign, "$g_formation_group7_selected", 0),
            (overlay_set_val, "$g_presentation_obj_battle_check7", 0),
            (overlay_animate_to_alpha, "$g_presentation_obj_battle_but7", 250, 0),
          (try_end),
        (else_try), #Order Selection
          (eq, ":object", "$g_presentation_obj_battle_10"),
		  (try_begin),
            (eq, ":value", 4),
			#(str_store_string, s1, "@-"),
			(call_script, "script_prebattle_order_update_text_slot", 0, -1, 0),
          (else_try),
            (eq, ":value", 3),
			#(str_store_string, s1, "@Hold"),
			(call_script, "script_prebattle_order_update_text_slot", 0, 0, 0),
          (else_try),
            (eq, ":value", 2),
			#(str_store_string, s1, "@Follow Me"),
			(call_script, "script_prebattle_order_update_text_slot", 0, 1, 0),
          (else_try),
            (eq, ":value", 1),
			#(str_store_string, s1, "@Charge"),
			(call_script, "script_prebattle_order_update_text_slot", 0, 2, 0),
		  (else_try),
            (eq, ":value", 0),
			#(str_store_string, s1, "@Stand Ground"),
			(call_script, "script_prebattle_order_update_text_slot", 0, 3, 0),
          (try_end),
        (else_try),
          (this_or_next|eq, ":object", "$g_presentation_obj_battle_11"),
		  (eq, ":object", "$g_presentation_obj_battle_12"),
		  (try_begin),
		        (eq, ":object", "$g_presentation_obj_battle_11"),
				(assign, ":column", 1),
				(assign, ":repeat", reg53),
		  (else_try),
				(eq, ":object", "$g_presentation_obj_battle_12"),
				(assign, ":column", 2),
				(assign, ":repeat", reg54),
		  (try_end),
		  (try_begin),
            (eq, ":value", 6),
			#(str_store_string, s1, "@-"),
			(call_script, "script_prebattle_order_update_text_slot", ":column", -1, 0),
          (else_try),
            (eq, ":value", 1),
			#(str_store_string, s1, "@Mount"),
			(call_script, "script_prebattle_order_update_text_slot", ":column", 3, 0),
          (else_try),
            (eq, ":value", 0),
			#(str_store_string, s1, "@Dismount"),
			(call_script, "script_prebattle_order_update_text_slot", ":column", 4, 0),
          (else_try),
            (eq, ":value", 5),
			#(str_store_string, s1, "@Forward 10"),
			(call_script, "script_prebattle_order_update_text_slot", ":column", 5, ":repeat"),
			(call_script, "script_prebattle_order_update_text_slot", 0, 0, 0), #Also, hold
          (else_try),
            (eq, ":value", 4),
			#(str_store_string, s1, "@Back 10"),
			(call_script, "script_prebattle_order_update_text_slot", ":column", 6, ":repeat"),
			(call_script, "script_prebattle_order_update_text_slot", 0, 0, 0), #Also, hold
          (else_try),
            (eq, ":value", 3),
			#(str_store_string, s1, "@Stand Closer"),
			(call_script, "script_prebattle_order_update_text_slot", ":column", 7, ":repeat"),
          (else_try),
            (eq, ":value", 2),
		    #(str_store_string, s1, "@Spread Out"),
			(call_script, "script_prebattle_order_update_text_slot", ":column", 8, ":repeat"),
		  (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_17"),
		  (try_begin),
            (eq, ":value", 4),
			#(str_store_string, s1, "@-"),
			(call_script, "script_prebattle_order_update_text_slot", 3, -1, 0),
          (else_try),        
		    (eq, ":value", 3),
			#(str_store_string, s1, "@Ranks"),
			(call_script, "script_prebattle_order_update_text_slot", 3, formation_ranks, 0),
			(call_script, "script_prebattle_order_update_text_slot", 0, 0, 0), #Also, hold
          (else_try),
            (eq, ":value", 2),
			#(str_store_string, s1, "@Shieldwall"),
			(call_script, "script_prebattle_order_update_text_slot", 3, formation_shield, 0),
			(call_script, "script_prebattle_order_update_text_slot", 0, 0, 0), #Also, hold
		 (else_try), 
		    (eq, ":value", 1),
			#(str_store_string, s1, "@Wedge"),
			(call_script, "script_prebattle_order_update_text_slot", 3, formation_wedge, 0),
			(call_script, "script_prebattle_order_update_text_slot", 0, 0, 0), #Also, hold
          (else_try),
            (eq, ":value", 0),
			#(str_store_string, s1, "@Square"),
			(call_script, "script_prebattle_order_update_text_slot", 3, formation_square, 0),
			(call_script, "script_prebattle_order_update_text_slot", 0, 0, 0), #Also, hold
          (try_end),		  
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_13"),
		  (try_begin),
            (eq, ":value", 4),
			#(str_store_string, s1, "@-"),
			(call_script, "script_prebattle_order_update_text_slot", 4, -1, 0),
          (else_try),
		    (eq, ":value", 1),
			#(str_store_string, s1, "@Hold Fire"),
			(call_script, "script_prebattle_order_update_text_slot", 4, 2, 0),
          (else_try),
            (eq, ":value", 0),
			#(str_store_string, s1, "@Fire at Will"),
			(call_script, "script_prebattle_order_update_text_slot", 4, 3, 0),
          (else_try),         
		    (eq, ":value", 3),
			#(str_store_string, s1, "@Any Weapon"),
			(call_script, "script_prebattle_order_update_text_slot", 4, 0, 0),
          (else_try),
            (eq, ":value", 2),
			#(str_store_string, s1, "@Blunt Weapons"),
			(call_script, "script_prebattle_order_update_text_slot", 4, 9, 0),
          (try_end),
		(else_try), 
          (eq, ":object", "$g_presentation_obj_battle_14"),
		  (try_begin),
            (eq, ":value", 4),
			#(str_store_string, s1, "@-"),
			(call_script, "script_prebattle_order_update_text_slot", 5, -1, 0),
          (else_try),
            (eq, ":value", 3),
			#(str_store_string, s1, "@One Handed),
			(call_script, "script_prebattle_order_update_text_slot", 5, 1, 0),
          (else_try),
            (eq, ":value", 2),
			#(str_store_string, s1, "@Two Handed"),
			(call_script, "script_prebattle_order_update_text_slot", 5, 2, 0),
          (else_try),
            (eq, ":value", 1),
			#(str_store_string, s1, "@Polearms"),
			(call_script, "script_prebattle_order_update_text_slot", 5, 3, 0),
		  (else_try),
            (eq, ":value", 0),
			#(str_store_string, s1, "@Ranged"),
			(call_script, "script_prebattle_order_update_text_slot", 5, 0, 0),
          (try_end),
		(else_try), 
          (eq, ":object", "$g_presentation_obj_battle_15"),
		  (try_begin),
            (eq, ":value", 2),
			#(str_store_string, s1, "@-"),
			(call_script, "script_prebattle_order_update_text_slot", 6, -1, 0),
          (else_try),
            (eq, ":value", 1),
			#(str_store_string, s1, "@Use Shields"),
			(call_script, "script_prebattle_order_update_text_slot", 6, 4, 0),
          (else_try),
            (eq, ":value", 0),
			#(str_store_string, s1, "@No Shields"),
			(call_script, "script_prebattle_order_update_text_slot", 6, 5, 0),
          (try_end),
		(else_try), 
          (eq, ":object", "$g_presentation_obj_battle_16"),
		  (try_begin),
            (eq, ":value", 1),
			#(str_store_string, s1, "@-"),
			(call_script, "script_prebattle_order_update_text_slot", 7, -1, 0),
          (else_try),
            (eq, ":value", 0),
			#(str_store_string, s1, "@Avoid Melee"),
			(call_script, "script_prebattle_order_update_text_slot", 7, 1, 0),
          (try_end),
		(else_try), #Repeat Number Boxes
		  (eq, ":object", reg51),
		  	# (overlay_get_position, pos1, "$g_presentation_obj_battle_24"),
		    # (position_get_x, ":x", pos1),
		    # (eq, ":x", 450), #Only when position orders displayed
		    (assign, reg53, ":value"),
		(else_try),
		  (eq, ":object", reg52),
		    (assign, reg54, ":value"),
	  (try_end),
		 
    ]),
		
	(ti_on_presentation_mouse_enter_leave,
       [(store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":enter_leave"),
        (try_begin),
          (eq, ":object", "$g_presentation_obj_battle_but0"),
          (try_begin),
            (eq, ":enter_leave", 0),
            (overlay_animate_to_color, "$g_presentation_but0_movement", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but0_riding", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but0_weapon_usage", 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(6), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(15), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(24), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(33), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(42), 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name0", 250, 0xFFFFFF),
          (else_try),
            (overlay_animate_to_color, "$g_presentation_but0_movement", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but0_riding", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but0_weapon_usage", 250, 0),
			(overlay_animate_to_color, reg(6), 250, 0),
			(overlay_animate_to_color, reg(15), 250, 0),
			(overlay_animate_to_color, reg(24), 250, 0),
			(overlay_animate_to_color, reg(33), 250, 0),
			(overlay_animate_to_color, reg(42), 250, 0),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name0", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but1"),
          (try_begin),
            (eq, ":enter_leave", 0),
            (overlay_animate_to_color, "$g_presentation_but1_movement", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but1_riding", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but1_weapon_usage", 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(7), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(16), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(25), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(34), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(43), 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name1", 250, 0xFFFFFF),
          (else_try),
            (overlay_animate_to_color, "$g_presentation_but1_movement", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but1_riding", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but1_weapon_usage", 250, 0),
			(overlay_animate_to_color, reg(7), 250, 0),
			(overlay_animate_to_color, reg(16), 250, 0),
			(overlay_animate_to_color, reg(25), 250, 0),
			(overlay_animate_to_color, reg(34), 250, 0),
			(overlay_animate_to_color, reg(43), 250, 0),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name1", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but2"),
          (try_begin),
            (eq, ":enter_leave", 0),
            (overlay_animate_to_color, "$g_presentation_but2_movement", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but2_riding", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but2_weapon_usage", 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(8), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(17), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(26), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(35), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(44), 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name2", 250, 0xFFFFFF),
          (else_try),
            (overlay_animate_to_color, "$g_presentation_but2_movement", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but2_riding", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but2_weapon_usage", 250, 0),
			(overlay_animate_to_color, reg(8), 250, 0),
			(overlay_animate_to_color, reg(17), 250, 0),
			(overlay_animate_to_color, reg(26), 250, 0),
			(overlay_animate_to_color, reg(35), 250, 0),
			(overlay_animate_to_color, reg(44), 250, 0),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name2", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but3"),
          (try_begin),
            (eq, ":enter_leave", 0),
            (overlay_animate_to_color, "$g_presentation_but3_movement", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but3_riding", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but3_weapon_usage", 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(9), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(18), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(27), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(36), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(45), 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name3", 250, 0xFFFFFF),
          (else_try),
            (overlay_animate_to_color, "$g_presentation_but3_movement", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but3_riding", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but3_weapon_usage", 250, 0),
			(overlay_animate_to_color, reg(9), 250, 0),
			(overlay_animate_to_color, reg(18), 250, 0),
			(overlay_animate_to_color, reg(27), 250, 0),
			(overlay_animate_to_color, reg(36), 250, 0),
			(overlay_animate_to_color, reg(45), 250, 0),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name3", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but4"),
          (try_begin),
            (eq, ":enter_leave", 0),
            (overlay_animate_to_color, "$g_presentation_but4_movement", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but4_riding", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but4_weapon_usage", 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(10), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(19), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(28), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(37), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(46), 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name4", 250, 0xFFFFFF),
          (else_try),
            (overlay_animate_to_color, "$g_presentation_but4_movement", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but4_riding", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but4_weapon_usage", 250, 0),
			(overlay_animate_to_color, reg(10), 250, 0),
			(overlay_animate_to_color, reg(19), 250, 0),
			(overlay_animate_to_color, reg(28), 250, 0),
			(overlay_animate_to_color, reg(37), 250, 0),
			(overlay_animate_to_color, reg(46), 250, 0),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name4", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but5"),
          (try_begin),
            (eq, ":enter_leave", 0),
            (overlay_animate_to_color, "$g_presentation_but5_movement", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but5_riding", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but5_weapon_usage", 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(11), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(20), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(29), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(38), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(47), 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name5", 250, 0xFFFFFF),
          (else_try),
            (overlay_animate_to_color, "$g_presentation_but5_movement", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but5_riding", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but5_weapon_usage", 250, 0),
			(overlay_animate_to_color, reg(11), 250, 0),
			(overlay_animate_to_color, reg(20), 250, 0),
			(overlay_animate_to_color, reg(29), 250, 0),
			(overlay_animate_to_color, reg(38), 250, 0),
			(overlay_animate_to_color, reg(47), 250, 0),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name5", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but6"),
          (try_begin),
            (eq, ":enter_leave", 0),
            (overlay_animate_to_color, "$g_presentation_but6_movement", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but6_riding", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but6_weapon_usage", 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(12), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(21), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(30), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(39), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(48), 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name6", 250, 0xFFFFFF),
          (else_try),
            (overlay_animate_to_color, "$g_presentation_but6_movement", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but6_riding", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but6_weapon_usage", 250, 0),
			(overlay_animate_to_color, reg(12), 250, 0),
			(overlay_animate_to_color, reg(21), 250, 0),
			(overlay_animate_to_color, reg(30), 250, 0),
			(overlay_animate_to_color, reg(39), 250, 0),
			(overlay_animate_to_color, reg(48), 250, 0),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name6", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but7"),
          (try_begin),
            (eq, ":enter_leave", 0),
            (overlay_animate_to_color, "$g_presentation_but7_movement", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but7_riding", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but7_weapon_usage", 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(13), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(22), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(31), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(40), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(49), 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name7", 250, 0xFFFFFF),
          (else_try),
            (overlay_animate_to_color, "$g_presentation_but7_movement", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but7_riding", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but7_weapon_usage", 250, 0),
			(overlay_animate_to_color, reg(13), 250, 0),
			(overlay_animate_to_color, reg(22), 250, 0),
			(overlay_animate_to_color, reg(31), 250, 0),
			(overlay_animate_to_color, reg(40), 250, 0),
			(overlay_animate_to_color, reg(49), 250, 0),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name7", 250, 0),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_but8"),
          (try_begin),
            (eq, ":enter_leave", 0),
            (overlay_animate_to_color, "$g_presentation_but8_movement", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but8_riding", 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_but8_weapon_usage", 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(14), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(23), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(32), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(41), 250, 0xFFFFFF),
			(overlay_animate_to_color, reg(50), 250, 0xFFFFFF),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name8", 250, 0xFFFFFF),
          (else_try),
            (overlay_animate_to_color, "$g_presentation_but8_movement", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but8_riding", 250, 0),
            (overlay_animate_to_color, "$g_presentation_but8_weapon_usage", 250, 0),
			(overlay_animate_to_color, reg(14), 250, 0),
			(overlay_animate_to_color, reg(23), 250, 0),
			(overlay_animate_to_color, reg(32), 250, 0),
			(overlay_animate_to_color, reg(41), 250, 0),
			(overlay_animate_to_color, reg(50), 250, 0),
            (overlay_animate_to_color, "$g_presentation_obj_battle_name8", 250, 0),
          (try_end),
        (try_end),
        ]),
		
      (ti_on_presentation_run,
        [
        (try_begin),
	      (key_clicked, key_escape),
		  (party_set_slot, "p_main_party", slot_party_prebattle_plan, 0),
		  (jump_to_menu, "$g_next_menu"),
		  (presentation_set_duration, 0),
		(try_end),
        ]),
      ]),

 ("prebattle_record_battle_size",0,mesh_load_window,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        (str_store_string, s1, "@Record Battle Size as set in Options"),
        (create_text_overlay, reg1, s1, tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_position, reg1, pos1),
        (overlay_set_text, reg1, s1),
		(create_number_box_overlay, "$g_presentation_obj_name_kingdom_1", 30, max_battle_size + 1),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 400),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),
		(party_get_slot, ":battle_size", "p_main_party", slot_party_prebattle_battle_size),
        (overlay_set_val, "$g_presentation_obj_name_kingdom_1", ":battle_size"),

        
        (create_button_overlay, "$g_presentation_obj_name_kingdom_2", "@Continue...", tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_2", pos1),
        (presentation_set_duration, 999999),
        ]),
      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
	    (store_trigger_param_2, ":value"),
        (try_begin),
          (eq, ":object", "$g_presentation_obj_name_kingdom_1"),
		  (party_set_slot, "p_main_party", slot_party_prebattle_battle_size, ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_name_kingdom_2"),
		  (party_get_slot, ":battle_size", "p_main_party", slot_party_prebattle_battle_size),
		  (val_clamp, ":battle_size", 30, max_battle_size + 1),
		  (party_set_slot, "p_main_party", slot_party_prebattle_battle_size, ":battle_size"),
          (try_begin),
		    (eq, "$g_presentation_credits_obj_1", 1),
			(start_presentation, "prsnt_prebattle_custom_deployment"),
		  (else_try),
		    (presentation_set_duration, 0),
		  (try_end),
        (try_end),
        ]),
    ]),
   
 ("pbod_preferences", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
		
		(try_begin),
			(party_slot_eq, "p_main_party", slot_party_pref_prefs_set, 0),
			(call_script, "script_prebattle_set_default_prefs"),
			(party_set_slot, "p_main_party", slot_party_pref_prefs_set, 1),
		(try_end),
		
		(str_clear, s0),
        (create_text_overlay, reg0, s0, tf_scrollable),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 50),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 550),
        (position_set_y, pos1, 630),
        (overlay_set_area_size, reg0, pos1),
        (set_container_overlay, reg0),
		
		(assign, ":num_options", 15),
		(val_add, ":num_options", 2), #For extra space for headings
		(assign, ":cur_y_shift", 50),
		(store_div, ":line_y_shift", ":cur_y_shift", 2),
		(store_mul, ":headings_y", ":cur_y_shift", ":num_options"),
		(store_sub, ":inputs_y", ":headings_y", 5),
		

        ## Headings
		(position_set_x, pos1, 50),
        
        (create_text_overlay, reg0, "@Record Battle Size as set in Options:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		
		(store_sub, ":line_1_y", ":headings_y", ":line_y_shift"), #LINE 1 Here
		(val_sub, ":headings_y", ":cur_y_shift"),
		(val_sub, ":headings_y", 30),		
        
        (create_text_overlay, reg0, "@The 'Weapon Use Fixes' change NPC decision-^making with the following weapon types.^^Un-tick the boxes if you dislike the behavior.", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),
		(val_sub, ":headings_y", 20),

        (create_text_overlay, reg0, "@Use NPC Lancer Fix:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),
		(assign, "$g_presentation_obj_banner_selection_2", reg0), #For Mouse-Overs

        (create_text_overlay, reg0, "@Use NPC Horse Archer Fix:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),

        (create_text_overlay, reg0, "@Use NPC Spear/Polearm Fix:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),
		
		(store_add, ":line_2_y", ":headings_y", ":line_y_shift"), #LINE 2 Here
		
		(create_text_overlay, reg0, "@Use Pike/Horse Damage Tweaks:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),
		
		(create_text_overlay, reg0, "@Reassign De-horsed Cavalry to:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),
		
		(create_text_overlay, reg0, "@Reassign No-Ammo Archers to:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),
		
		(create_text_overlay, reg0, "@Enable Battle Continuation:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),
		
		(create_text_overlay, reg0, "@Batt. Cont., Charge after KO:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),
		
		(create_text_overlay, reg0, "@Formations Battle AI:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),
		
		(create_text_overlay, reg0, "@Enable AI to use Special Orders:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),
		
		(create_text_overlay, reg0, "@Enable Bodyguards in Towns/Villages:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),
		
		(create_text_overlay, reg0, "@Enable ranged penalty from weather:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),
		
		(store_add, ":line_3_y", ":headings_y", ":line_y_shift"), #LINE 3 HERE

        (create_text_overlay, reg0, "@Disable Companions' complaints:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),

        (create_text_overlay, reg0, "@Enable the cheat menu:", tf_vertical_align_center),
        (position_set_y, pos1, ":headings_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":headings_y", ":cur_y_shift"),

        ## Lines
		
		(create_mesh_overlay, reg0, "mesh_white_plane"),
        (position_set_x, pos1, 23500),
        (position_set_y, pos1, 100),
        (overlay_set_size, reg0, pos1),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, ":line_1_y"),
        (overlay_set_position, reg0, pos1),
        (overlay_set_color, reg0, 0),
		
		(create_mesh_overlay, reg0, "mesh_white_plane"),
        (position_set_x, pos1, 23500),
        (position_set_y, pos1, 100),
        (overlay_set_size, reg0, pos1),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, ":line_2_y"),
        (overlay_set_position, reg0, pos1),
        (overlay_set_color, reg0, 0), #0x000000
		
		(create_mesh_overlay, reg0, "mesh_white_plane"),
        (position_set_x, pos1, 23500),
        (position_set_y, pos1, 100),
        (overlay_set_size, reg0, pos1),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, ":line_3_y"),
        (overlay_set_position, reg0, pos1),
        (overlay_set_color, reg0, 0), #0x000000
        
        ## Inputs
        (position_set_x, pos1, 450),

		(val_sub, ":inputs_y", 9),	
        (create_number_box_overlay, "$g_presentation_obj_name_kingdom_1", 30, max_battle_size + 1),
        (position_set_y, pos1, ":inputs_y"),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),
        (party_get_slot, ":battle_size", "p_main_party", slot_party_prebattle_battle_size),
        (overlay_set_val, "$g_presentation_obj_name_kingdom_1", ":battle_size"),
		(val_sub, ":inputs_y", ":cur_y_shift"),
		(val_sub, ":inputs_y", ":cur_y_shift"),
		(val_sub, ":inputs_y", 41),

        (create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"), #Lancer
        (position_set_y, pos1, ":inputs_y"),
        (overlay_set_position, reg0, pos1),
		(val_sub, ":inputs_y", ":cur_y_shift"),

        (create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"), #Horse Archer
        (position_set_y, pos1, ":inputs_y"),
        (overlay_set_position, reg0, pos1),  
        (val_sub, ":inputs_y", ":cur_y_shift"),		

        (create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"), #Spear/Polearm
        (position_set_y, pos1, ":inputs_y"),
        (overlay_set_position, reg0, pos1),  
		(val_sub, ":inputs_y", ":cur_y_shift"),
        
		(create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"), #Damage
        (position_set_y, pos1, ":inputs_y"),
        (overlay_set_position, reg0, pos1),	
        (val_sub, ":inputs_y", ":cur_y_shift"),		
		
		(create_combo_button_overlay, reg0), #De-Horsed Division Set
		(position_set_x, pos1, 485),
		(val_sub, ":inputs_y", 8),
		(position_set_y, pos1, ":inputs_y"),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 700),
		(position_set_y, pos1, 800),
		(overlay_set_size, reg0, pos1),
		(try_for_range, ":i", 0, 9),
		    (str_store_class_name, s1, ":i"),
			(overlay_add_item, reg0, s1),
		(try_end),
		(overlay_add_item, reg0, "@{!}- Disabled -"),
		(position_set_x, pos1, 450),
		(val_add, ":inputs_y", 8),
		(val_sub, ":inputs_y", ":cur_y_shift"),
		
		(create_combo_button_overlay, reg0), #Out of Ammo Archer Division Set
		(position_set_x, pos1, 485),
		(val_sub, ":inputs_y", 8),
		(position_set_y, pos1, ":inputs_y"),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 700),
		(position_set_y, pos1, 800),
		(overlay_set_size, reg0, pos1),
		(try_for_range, ":i", 0, 9),
		    (str_store_class_name, s1, ":i"),
			(overlay_add_item, reg0, s1),
		(try_end),
		(overlay_add_item, reg0, "@{!}- Disabled -"),
		(position_set_x, pos1, 450),
		(val_add, ":inputs_y", 8),
		(val_sub, ":inputs_y", ":cur_y_shift"),
		
		(create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"), #Battle Continuation
        (position_set_y, pos1, ":inputs_y"),
        (overlay_set_position, reg0, pos1),	
        (val_sub, ":inputs_y", ":cur_y_shift"),	
		
		# (create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"), #Post-KD Charge
        # (position_set_y, pos1, ":inputs_y"),
        # (overlay_set_position, reg0, pos1),	
        # (val_sub, ":inputs_y", ":cur_y_shift"),

		(create_combo_button_overlay, reg0), #Post-KD Charge
		(position_set_x, pos1, 485),
		(val_sub, ":inputs_y", 8),
		(position_set_y, pos1, ":inputs_y"),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 700),
		(position_set_y, pos1, 800),
		(overlay_set_size, reg0, pos1),
		(overlay_add_item, reg0, "@{!}- Disabled -"),
		(overlay_add_item, reg0, "@Charge All"),
		(overlay_add_item, reg0, "@Formations AI"),
		(position_set_x, pos1, 450),
		(val_add, ":inputs_y", 8),
		(val_sub, ":inputs_y", ":cur_y_shift"),		
		
		# (create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"), #AI Formations
        # (position_set_y, pos1, ":inputs_y"),
        # (overlay_set_position, reg0, pos1),	
        # (val_sub, ":inputs_y", ":cur_y_shift"),	
		
		(create_combo_button_overlay, reg0), #AI Formations
		(position_set_x, pos1, 485),
		(val_sub, ":inputs_y", 8),
		(position_set_y, pos1, ":inputs_y"),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 700),
		(position_set_y, pos1, 800),
		(overlay_set_size, reg0, pos1),
		(overlay_add_item, reg0, "@{!}- Disabled -"),
		(overlay_add_item, reg0, "@Formations AI"),
		(overlay_add_item, reg0, "@Native AI, w/Formations"),
		(position_set_x, pos1, 450),
		(val_add, ":inputs_y", 8),
		(val_sub, ":inputs_y", ":cur_y_shift"),	
		
		(create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"), #AI Spear Brace/Special Orders
        (position_set_y, pos1, ":inputs_y"),
        (overlay_set_position, reg0, pos1),	
        (val_sub, ":inputs_y", ":cur_y_shift"),	
		
		(create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"), #Bodyguards
        (position_set_y, pos1, ":inputs_y"),
        (overlay_set_position, reg0, pos1),	
        (val_sub, ":inputs_y", ":cur_y_shift"),	
		
		(create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"), #Weather Proficiency Penalty
        (position_set_y, pos1, ":inputs_y"),
        (overlay_set_position, reg0, pos1),	
        (val_sub, ":inputs_y", ":cur_y_shift"),	
		
		(create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"),
        (position_set_y, pos1, ":inputs_y"),
        (overlay_set_position, reg0, pos1),
        (overlay_set_val, reg0, "$disable_npc_complaints"),
		(val_sub, ":inputs_y", ":cur_y_shift"),

        (create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"),
        (position_set_y, pos1, ":inputs_y"),
        (overlay_set_position, reg0, pos1),
        (overlay_set_val, reg0, "$cheat_mode"),   
        (val_sub, ":inputs_y", ":cur_y_shift"),		
        
        (set_container_overlay, -1),
		
	    #Set Values of Caba'drin Order Preferences
		(party_get_slot, ":pref_lancer", "p_main_party", slot_party_pref_wu_lance),
        (party_get_slot, ":pref_harcher", "p_main_party", slot_party_pref_wu_harcher),
        (party_get_slot, ":pref_spear", "p_main_party", slot_party_pref_wu_spear),
		(party_get_slot, ":pref_damage", "p_main_party", slot_party_pref_dmg_tweaks),
		
		(party_get_slot, ":pref_bodyguard", "p_main_party", slot_party_pref_bodyguard),
        (party_get_slot, ":pref_battcont", "p_main_party", slot_party_pref_bc_continue),
        (party_get_slot, ":pref_KOcharge", "p_main_party", slot_party_pref_bc_charge_ko),
		(party_get_slot, ":pref_dehorsed", "p_main_party", slot_party_pref_div_dehorse),
		(party_get_slot, ":pref_outofammo", "p_main_party", slot_party_pref_div_no_ammo),
		(party_get_slot, ":pref_formAI", "p_main_party", slot_party_pref_formations),
		(party_get_slot, ":pref_spbrace", "p_main_party", slot_party_pref_spear_brace),
		(party_get_slot, ":pref_wpnprofd", "p_main_party", slot_party_pref_wp_prof_decrease),
		
		(store_add, ":overlay", "$g_presentation_obj_name_kingdom_1", 1),
		(overlay_set_val, ":overlay", ":pref_lancer"), 
		(val_add, ":overlay", 1),
		(overlay_set_val, ":overlay", ":pref_harcher"), 
		(val_add, ":overlay", 1),
		(overlay_set_val, ":overlay", ":pref_spear"), 
		(val_add, ":overlay", 1),
		(overlay_set_val, ":overlay", ":pref_damage"), 
		(val_add, ":overlay", 1),
		(overlay_set_val, ":overlay", ":pref_dehorsed"),
		(val_add, ":overlay", 1),
		(overlay_set_val, ":overlay", ":pref_outofammo"),
		(val_add, ":overlay", 1),
		(overlay_set_val, ":overlay", ":pref_battcont"),
		(val_add, ":overlay", 1),
		(overlay_set_val, ":overlay", ":pref_KOcharge"),
		(val_add, ":overlay", 1),
		(overlay_set_val, ":overlay", ":pref_formAI"),
		(val_add, ":overlay", 1),
		(overlay_set_val, ":overlay", ":pref_spbrace"),
		(val_add, ":overlay", 1),
		(overlay_set_val, ":overlay", ":pref_bodyguard"),
		(val_add, ":overlay", 1),
		(overlay_set_val, ":overlay", ":pref_wpnprofd"),

		## Mouse-over Tips	
		(create_text_overlay, reg0, "@PBOD Mod^Options", tf_center_justify|tf_with_outline),
		(overlay_set_color, reg0, 0xFFFFFFFF),
		(position_set_x, pos1, 800),
        (position_set_y, pos1, 600),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 2000),
        (position_set_y, pos1, 2000),
        (overlay_set_size, reg0, pos1),
		
        (str_store_string, s0, "@Mouse-over options for further information."),
        (create_text_overlay, "$g_presentation_obj_banner_selection_1", s0, tf_double_space|tf_scrollable),
        (position_set_x, pos1, 650),
        (position_set_y, pos1, 400),
        (overlay_set_position, "$g_presentation_obj_banner_selection_1", pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_banner_selection_1", pos1),
        (position_set_x, pos1, 300),
        (position_set_y, pos1, 150),
        (overlay_set_area_size, "$g_presentation_obj_banner_selection_1", pos1),
		
		
        ## Button
		(position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (create_game_button_overlay, "$g_presentation_obj_name_kingdom_2", "@Done", tf_center_justify),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_2", pos1),  

		(position_set_x, pos1, 740),
		(create_game_button_overlay, reg0, "@Restore Defaults", tf_center_justify),
        (overlay_set_position, reg0, pos1),	

		(position_set_x, pos1, 900),
        (position_set_y, pos1, 75),
		(create_game_button_overlay, reg0, "@Key Settings", tf_center_justify),
		(overlay_set_position, reg0, pos1),
      ]),

	  (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

		(try_begin),
          (eq, ":object", "$g_presentation_obj_name_kingdom_1"),
		  (party_set_slot, "p_main_party", slot_party_prebattle_battle_size, ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_name_kingdom_2"),
		  
		  (party_get_slot, ":battle_size", "p_main_party", slot_party_prebattle_battle_size),
		  (val_clamp, ":battle_size", 30, max_battle_size + 1),
		  (party_set_slot, "p_main_party", slot_party_prebattle_battle_size, ":battle_size"),
		  
          (presentation_set_duration, 0),	  
		(else_try),
		  (store_add, ":overlay", "$g_presentation_obj_name_kingdom_2", 1),
		  (eq, ":object", ":overlay"),
		  (call_script, "script_prebattle_set_default_prefs"),
		  (start_presentation, "prsnt_pbod_preferences"),
		(else_try),
		  (val_add, ":overlay", 1),
		  (eq, ":object", ":overlay"),
		  (start_presentation, "prsnt_pbod_redefine_keys"),
		(else_try),
		  (store_add, ":overlay", "$g_presentation_obj_name_kingdom_1", 1),
		  (eq, ":object", ":overlay"), #Lancer		  
		  (party_set_slot, "p_main_party", slot_party_pref_wu_lance, ":value"),	       
		(else_try),
		  (val_add, ":overlay", 1),
		  (eq, ":object", ":overlay"), #Horse Archer
		  (party_set_slot, "p_main_party", slot_party_pref_wu_harcher, ":value"),	
		(else_try),
		  (val_add, ":overlay", 1),
		  (eq, ":object", ":overlay"), #Spear
		  (party_set_slot, "p_main_party", slot_party_pref_wu_spear, ":value"),	
		(else_try),
		  (val_add, ":overlay", 1),
		  (eq, ":object", ":overlay"), #Damage
		  (party_set_slot, "p_main_party", slot_party_pref_dmg_tweaks, ":value"),	
		(else_try),
		  (val_add, ":overlay", 1),
		  (eq, ":object", ":overlay"),  #De-horsed
		  (party_set_slot, "p_main_party", slot_party_pref_div_dehorse, ":value"),	
		(else_try),
		  (val_add, ":overlay", 1),
		  (eq, ":object", ":overlay"), #Out of Ammo
		  (party_set_slot, "p_main_party", slot_party_pref_div_no_ammo, ":value"),	
		(else_try),
		  (val_add, ":overlay", 1),
		  (eq, ":object", ":overlay"), #Battle Continuation
		  (party_set_slot, "p_main_party", slot_party_pref_bc_continue, ":value"),
		(else_try),
		  (val_add, ":overlay", 1),
		  (eq, ":object", ":overlay"), #KO Charge
		  (party_set_slot, "p_main_party", slot_party_pref_bc_charge_ko, ":value"),
		(else_try),
		  (val_add, ":overlay", 1),
		  (eq, ":object", ":overlay"), #AI Formations
		  (party_set_slot, "p_main_party", slot_party_pref_formations, ":value"),
        (else_try),
		  (val_add, ":overlay", 1),
		  (eq, ":object", ":overlay"), #AI Spear Brace/Special Orders
		  (party_set_slot, "p_main_party", slot_party_pref_spear_brace, ":value"),		  
		(else_try),
		  (val_add, ":overlay", 1),
		  (eq, ":object", ":overlay"), #Bodyguard
		  (party_set_slot, "p_main_party", slot_party_pref_bodyguard, ":value"),
		(else_try),
		  (val_add, ":overlay", 1),
		  (eq, ":object", ":overlay"), #Weather Proficiency Penalty
		  (party_set_slot, "p_main_party", slot_party_pref_wp_prof_decrease, ":value"),			  
		(else_try),
		  (val_add, ":overlay", 1),
		  (eq, ":object", ":overlay"), #NPC Complaints
		  (assign, "$disable_npc_complaints", ":value"),
		(else_try),
		  (val_add, ":overlay", 1),
		  (eq, ":object", ":overlay"), #Cheat Mode
		  (assign, "$cheat_mode", ":value"),
        (try_end),
      ]),
	  
	  (ti_on_presentation_mouse_enter_leave, #Mouse-Over Pref-Tips
	  [
	    (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":enter_leave"), #0 if mouse enters, 1 if mouse leaves
		(try_begin),
			(eq, ":enter_leave", 1),
			#Clear String...or do nothing?
		(else_try),
			(eq, ":enter_leave", 0),
			(store_add, ":overlay", "$g_presentation_obj_name_kingdom_1", 1), #Input
			(assign, ":overlay_2", "$g_presentation_obj_banner_selection_2"), #Heading
			(try_begin),
			  (lt, ":object", ":overlay_2"),
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@Mouse-over options for further information."),
			(else_try),
			  (this_or_next|eq, ":object", ":overlay_2"),
			  (eq, ":object", ":overlay"), #Lancer		  
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@Weapon Use Fix for Lancers will force mounted bots with lances to use them unless they are surrounded by enemies."),       
			(else_try),
			  (val_add, ":overlay", 1),
			  (val_add, ":overlay_2", 1),
			  (this_or_next|eq, ":object", ":overlay_2"),
			  (eq, ":object", ":overlay"), #Horse Archer
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@Weapon Use Fix for Horse Archers will force mounted bots with bows to use them until they run out of ammo."),       
			(else_try),
			  (val_add, ":overlay", 1),
			  (val_add, ":overlay_2", 1),
			  (this_or_next|eq, ":object", ":overlay_2"),
			  (eq, ":object", ":overlay"), #Spear
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@Weapon Use Fix for Spear/Polearms will force infantry bots with polearms to use them unless they are surrounded by enemies."),       
			(else_try),
			  (val_add, ":overlay", 1),
			  (val_add, ":overlay_2", 1),
			  (this_or_next|eq, ":object", ":overlay_2"),
			  (eq, ":object", ":overlay"), #Damage
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@Damage tweaks will give a flat boost to damage from spears to horses, and charge damage from horses to infantry, in an attempt to compensate for poor AI use of polearms and charges."),        
			(else_try),
			  (val_add, ":overlay", 1),
			  (val_add, ":overlay_2", 1),
			  (this_or_next|eq, ":object", ":overlay_2"),
			  (eq, ":object", ":overlay"),  #De-horsed
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@Mounted bots, once their horse dies, can be re-assinged to a division of your choosing. If active, AI bots will be reassigned to infantry."),       	
			(else_try),
			  (val_add, ":overlay", 1),
			  (val_add, ":overlay_2", 1),
			  (this_or_next|eq, ":object", ":overlay_2"),
			  (eq, ":object", ":overlay"), #Out of Ammo
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@Foot archer bots, once out of ammo, can be re-assinged to a division of your choosing. If active, AI bots will be reassigned to infantry."),	
			(else_try),
			  (val_add, ":overlay", 1),
			  (val_add, ":overlay_2", 1),
			  (this_or_next|eq, ":object", ":overlay_2"),
			  (eq, ":object", ":overlay"), #Battle Continuation
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@Battle Continuation allows your troops to continue fighting after you are knocked out."),
			(else_try),
			  (val_add, ":overlay", 1),
			  (val_add, ":overlay_2", 1),
			  (this_or_next|eq, ":object", ":overlay_2"),
			  (eq, ":object", ":overlay"), #KO Charge
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@If Battle Continuation is active, you can select what your troops will do after you get knocked out: Disabled has them continue their previous orders; Charge all will give everyone a charge order; Formations AI (if active for the AI) will allow the new AI to take over for you."),
			(else_try),
			  (val_add, ":overlay", 1),
			  (val_add, ":overlay_2", 1),
			  (this_or_next|eq, ":object", ":overlay_2"),
			  (eq, ":object", ":overlay"), #AI Formations
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@Select your prefered Battle AI: Disabled is Native AI; Formations AI both allows the AI to use formations and changes their battle decision-making; Native AI w/Formations is Native AI but carries out the Native AI with basic formations."),
			(else_try),
			  (val_add, ":overlay", 1),
			  (val_add, ":overlay_2", 1),
			  (this_or_next|eq, ":object", ":overlay_2"),
			  (eq, ":object", ":overlay"), #AI Spear Brace/Special Orders
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@Enabling AI Special Orders allows the AI teams to use volley fire (crossbows), skirmish mode (bow-users), and spear-bracing (polearm infantry)."),
			(else_try),
			  (val_add, ":overlay", 1),
			  (val_add, ":overlay_2", 1),
			  (this_or_next|eq, ":object", ":overlay_2"),
			  (eq, ":object", ":overlay"), #Bodyguard
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@Bodyguards allows your companions to serve as your character's bodyguards in town and village scenes. The number of bodyguards depends on your character's leadership and renown."),
			(else_try),
			  (val_add, ":overlay", 1),
			  (val_add, ":overlay_2", 1),
			  (this_or_next|eq, ":object", ":overlay_2"),
			  (eq, ":object", ":overlay"), #Weather Proficiency Penalty
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@The Weather Proficiency Penalties lowers the ranged weapons proficiencies of all troops while in battle in heavy fog, rain/snow, or at night to reflect the poor conditions for archery."),			  
			(else_try),
			  (val_add, ":overlay", 1),
			  (val_add, ":overlay_2", 1),
			  (this_or_next|eq, ":object", ":overlay_2"),
			  (eq, ":object", ":overlay"), #NPC Complaints
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@Disabling NPC Complaints will mute your companion's complaints about eachother or your decisions. It will not remove the consequences of their opinions, however."),
			(else_try),
			  (val_add, ":overlay", 1),
			  (val_add, ":overlay_2", 1),
			  (this_or_next|eq, ":object", ":overlay_2"),
			  (eq, ":object", ":overlay"), #Cheat Mode
			  (overlay_set_text, "$g_presentation_obj_banner_selection_1", "@The cheat/debug mode activates debug messages as well as the 'cheatmenu' in your Camp Menu and additional options under Reports."),
			(try_end),
		(try_end),	  
	  ]),
    ]),

 # Key configuration by Dunde
 ("pbod_redefine_keys", 0, mesh_load_window, 
  [(ti_on_presentation_load, 
    [(presentation_set_duration, 999999),
     (set_fixed_point_multiplier, 1000),
     (assign, "$g_presentation_obj_custom_battle_designer_1", 0),                    
     (call_script, "script_init_key_config"), #CABA-Initialize Slots to use TEMP troop
	 (init_position, pos1),
     # Tittle
     (position_set_y, pos1, 650),  (position_set_x, pos1, 500),  # Tittle Position
     (position_set_x, pos2, 2000), (position_set_y, pos2, 2000), # Tittle Size
     (create_text_overlay, reg0, "@Keys Configuration", tf_center_justify),
     (overlay_set_position, reg0, pos1), (overlay_set_size, reg0, pos2),
     (position_set_y, pos1, 25), (position_set_x, pos1, 50),   # Notes' Position
     (position_set_x, pos2, 750), (position_set_y, pos2, 750), # Note's Size
     (create_text_overlay, "$g_presentation_obj_custom_battle_designer_2", "@Press Esc to^^Disable a key", tf_left_align),
     (overlay_set_position, "$g_presentation_obj_custom_battle_designer_2", pos1), 
	 (overlay_set_size, "$g_presentation_obj_custom_battle_designer_2", pos2),
     (overlay_set_color, "$g_presentation_obj_custom_battle_designer_2", 0x600000),  # Note's Color  
     (overlay_set_alpha, "$g_presentation_obj_custom_battle_designer_2", 0x00),      # Note's invisible  
     (position_set_y, pos1, 600),                             # First KeyConfig's Label Position
     (try_begin),
        (le, number_of_keys, two_columns_limit),                 # KeyConfig's Labels Size
        (position_set_x, pos2, 1000), (position_set_y, pos2, 1000), 
        (position_set_x, pos1, 50),
     (else_try),
        (position_set_x, pos2, 750), (position_set_y, pos2, 750),   
         (position_set_x, pos1, 25),
     (try_end),     
     (position_set_x, pos3, 120),  (position_set_y, pos3, 30),   # KeyConfig's Buttons Size     
     (try_for_range, ":no", 0, number_of_keys),
        (store_add, ":off_string", ":no", key_names_begin),             # Offset for Label String
        (store_add, ":off_overlay2", ":no", slot_key_overlay_begin),    # Offset for Buttons Overlay
        (store_add, ":off_overlay1", ":off_overlay2", number_of_keys),  # Offset for Labels Overlay
        (create_text_overlay, reg1, ":off_string", tf_left_align),              # Creating,
        (troop_set_slot, key_config_data, ":off_overlay1", reg1),               # Saving,
        (overlay_set_position, reg1, pos1), (overlay_set_size, reg1, pos2),     # Positioning, and Resizing KeyConfig Labels
        (try_begin),
           (le, number_of_keys, two_columns_limit),
           (position_move_x, pos1, 35),                                         # Move Right to give spave between labels and buttons
        (else_try),
           (position_move_x, pos1, 24), 
        (try_end),   
        (create_game_button_overlay, reg2, "str_no_string", tf_center_justify), # Creating,
        (troop_set_slot, key_config_data, ":off_overlay2", reg2),               # Saving,
        (overlay_set_position, reg2, pos1), (overlay_set_size, reg2, pos3),     # Positioning, and Resizing KeyConfig Buttons
        (try_begin),
           (le, number_of_keys, two_columns_limit),
           (position_move_x, pos1, -35),                                        # Move Left
        (else_try),
           (position_move_x, pos1, -24), 
        (try_end),   
        (position_move_y, pos1, -4),              # Move left, and move down for next keyconfig's label and button
        (try_begin),          
            (le, number_of_keys, two_columns_limit), 
            (try_begin),
               (eq, number_of_keys/2, ":no"),                                   # Half of keyconfigs positions are moved up and right
               (assign, ":move_y", number_of_keys/2+1), (val_mul, ":move_y", 4),
               (position_move_y, pos1, ":move_y"),
               (position_move_x, pos1, 50),
            (try_end),
        (else_try),          
            (try_begin),
               (eq, number_of_keys/3, ":no"),          # 2nd 1/3 part of keyconfigs positions are moved up and right
               (assign, ":move_y", number_of_keys/3+1), (val_mul, ":move_y", 4),
               (position_move_y, pos1, ":move_y"),
               (position_move_x, pos1, 33),
            (try_end),
            (try_begin),
               (eq, 2*number_of_keys/3, ":no"),        # 3nd 2/3 part of keyconfigs positions are moved up and right
               (assign, ":move_y", number_of_keys/3+1), (val_mul, ":move_y", 4),
               (position_move_y, pos1, ":move_y"),
               (position_move_x, pos1, 33),
            (try_end),
        (try_end),  
     (try_end),
	 (call_script, "script_set_config_slot_key_config"),                        # Get Current KeyConfig
     (call_script, "script_update_key_config_buttons"),                         # Writting the  Captions
     #Mouse Dead-Zone addition
	 (create_text_overlay, reg1, "@DeathCam Mouse Sensitivity", tf_left_align),              # Creating,
	 #keep in 1st column
	 (try_begin),
        (le, number_of_keys, two_columns_limit),                
        (position_set_x, pos1, 50),
     (else_try),
        (position_set_x, pos1, 25),
     (try_end), 
     (position_move_y, pos1, -8), 	
     #end force 1st column---need to manually edit...or remove and leave in last column	 
     (overlay_set_position, reg1, pos1), (overlay_set_size, reg1, pos2),     # Positioning, and Resizing KeyConfig Labels
	 (try_begin),
	   (le, number_of_keys, two_columns_limit),
	   (position_move_x, pos1, 38),                                         # Move Right to give spave between labels and buttons
	 (else_try),
	   (position_move_x, pos1, 27), 
	 (try_end),  
	 (create_slider_overlay, reg2, 1, 10),
	 (overlay_set_position, reg2, pos1), 
	 (position_set_x, pos3, 700),
	 (position_set_y, pos3, 700),
	 (overlay_set_size, reg2, pos3),     # Positioning, and Resizing KeyConfig Buttons
	 (try_begin),
		(neg|is_between, "$camera_mouse_deadzone", 1, 11),
		(assign, "$camera_mouse_deadzone", 3), #default
	 (try_end),
	 (store_sub, ":inverse_deadzone", 11, "$camera_mouse_deadzone"), #so higher values is more sensitive
	 (overlay_set_val, reg2, ":inverse_deadzone"),
	 #Mouse Dead-Zone addition end
	 # Other Buttons
     (position_set_y, pos1, 25), (position_set_x, pos1, 900),                   
     (create_game_button_overlay, "$g_presentation_obj_custom_battle_designer_3", "@OK", tf_center_justify),          # OK Button
     (overlay_set_position, "$g_presentation_obj_custom_battle_designer_3", pos1),
     (position_move_x, pos1, -16),
     (create_game_button_overlay, "$g_presentation_obj_custom_battle_designer_4", "@Reset", tf_center_justify),       # RESET Button
     (overlay_set_position, "$g_presentation_obj_custom_battle_designer_4", pos1),                       
     (position_move_x, pos1, -16),
     (create_game_button_overlay, "$g_presentation_obj_custom_battle_designer_5", "@Default", tf_center_justify),     # DEFAULT Button
     (overlay_set_position, "$g_presentation_obj_custom_battle_designer_5", pos1),
	 (create_game_button_overlay, "$g_presentation_obj_custom_battle_designer_6", "@Mod Options"),
     (position_set_x, pos1, 900),
     (position_set_y, pos1, 75),
     (overlay_set_position, "$g_presentation_obj_custom_battle_designer_6", pos1),
	]),
	
   (ti_on_presentation_event_state_change, 
    [(store_trigger_param_1, ":object"),
     (assign, ":found", 0),
     (store_add, ":upper_limit", slot_key_overlay_begin, number_of_keys),    #  Checking
     (try_for_range, ":slot", slot_key_overlay_begin, ":upper_limit"),       # for all KeyConfigs Button Overlay
        (troop_slot_eq, key_config_data, ":slot", ":object"),                # Found the Right Button Overlay?
        (assign, "$g_presentation_obj_custom_battle_designer_1", 1),                              # Flag the event
        (assign, "$g_presentation_credits_obj_1", ":object"),                                      # Get The Overlay 
        (overlay_set_text, "$g_presentation_credits_obj_1", "@Press a key", tf_center_justify),    # Change it's caption & color
        (overlay_set_color, "$g_presentation_credits_obj_1", 0x0000FF),
        (overlay_set_hilight_color, "$g_presentation_credits_obj_1", 0x0000FF),
        (store_sub, "$g_presentation_credits_obj_2", ":slot",  number_of_keys),
        (assign, ":found", ":slot"), (assign, ":upper_limit", ":slot"),      # Break the Loops
     (try_end),     
     (try_begin),
        (gt, ":found", 0),                                                  # Skip, the Object is a keyconfig button 
     #Mouse Dead-Zone addition
	 (else_try),
	   (store_sub, ":overlay", "$g_presentation_obj_custom_battle_designer_3", 1),
	   (eq, ":object", ":overlay"),
	   (store_trigger_param_2, ":value"),
	   (store_sub, "$camera_mouse_deadzone", 11, ":value"),
	   (overlay_set_val, ":overlay", ":value"), #looks cleaner
	 #Mouse Dead-Zone addition end
	 (else_try),    
       (eq, ":object", "$g_presentation_obj_custom_battle_designer_3"),     # OK pressed?
       (call_script, "script_set_global_var_key_config"),                   # Write the Config to Global Variable
       (call_script, "script_update_key_config_buttons"), # it's not neccessary, just incase
       (presentation_set_duration, 0),    # Quit from KeyConfig Presentation
     (else_try),    
       (eq, ":object", "$g_presentation_obj_custom_battle_designer_4"),     # RESET pressed? 
       (call_script, "script_set_config_slot_key_config"),                  # Reload Current Config
       (call_script, "script_update_key_config_buttons"),                   # Update Captions
     (else_try),
       (eq, ":object", "$g_presentation_obj_custom_battle_designer_5"),     # DEFAULT pressed?
       (call_script, "script_reset_to_default_keys"),                       # Reload Default Config
       (call_script, "script_update_key_config_buttons"),                   # Update Captions 
     (else_try),
       (eq, ":object", "$g_presentation_obj_custom_battle_designer_6"),     # RETURN TO PREFERENCES
	   (call_script, "script_set_global_var_key_config"),                   # Write the Config to Global Variable
	   (start_presentation, "prsnt_pbod_preferences"),                      # Go To Preferences
	   #(start_presentation, "prsnt_mod_option"),
     (try_end),
     (try_begin),
        (eq, "$g_presentation_obj_custom_battle_designer_1", 1),                    # if a Button's waiting to set 
        (overlay_set_alpha, "$g_presentation_obj_custom_battle_designer_2", 0xFF),  # then make The Note visible
     (try_end), ]),

  (ti_on_presentation_run, 
   [(eq, "$g_presentation_obj_custom_battle_designer_1", 1),                                     # if a Button's waiting to set 
    (assign, "$g_presentation_obj_custom_battle_designer_1", 0),                                 #
    (assign, ":found", 0),
    (store_add, ":upper_limit", slot_key_defs_begin, number_of_all_keys),   # Checking
    (try_for_range, ":no", slot_key_defs_begin,  ":upper_limit"),           # for all keys
       (troop_get_slot, ":key", key_config_data, ":no"),                    # reload the key from slot
       (key_clicked, ":key"),                                               # if that key's clicked?
       (troop_set_slot, key_config_data, "$g_presentation_credits_obj_2", ":key"),                # Yes, then save the new config for the button
       (assign, ":found", ":key"),                                          # Flag we found it
       (assign, ":upper_limit", ":no"),                                     # Break the Loops
    (try_end),
    (try_begin),
       (gt, ":found", 0),                                                   # We Found the key
    (else_try),   
       (key_clicked, key_escape),                                           # ESC clicked?
       (troop_set_slot, key_config_data, "$g_presentation_credits_obj_2", 0xff),      # Disable the button
    (else_try),
       (assign, "$g_presentation_obj_custom_battle_designer_1", 1),          # else? do nothing. The Button's still waiting
    (try_end),
    (try_begin),
       (eq, "$g_presentation_obj_custom_battle_designer_1", 0),                     # if there's new keyconfig for the button
       (try_for_range, ":no", slot_keys_begin, slot_keys_begin + number_of_keys),   # Check if there is another button use the same key
           (neq, ":no",  "$g_presentation_credits_obj_2"),
           (troop_slot_eq, key_config_data, ":no", ":found"),                       # if there is, then disable the button
           (troop_set_slot, key_config_data, ":no", 0xff),
       (try_end),                          
       (overlay_set_hilight_color, "$g_presentation_credits_obj_1", 0x00ff00),      # Set the button color back to normal
       (overlay_set_alpha, "$g_presentation_obj_custom_battle_designer_2", 0x00),   # The Note must be dissapear again
       (call_script, "script_update_key_config_buttons"),                           # Update Captions
    (try_end), 
    ]),  
   ]),      
	
 ("caba_order_display", prsntf_read_only,0,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
		(try_for_range, ":i", 0, 9),
			(troop_set_slot, order_frame_presobj, ":i", -1),
		(try_end),
		
		(call_script, "script_init_key_config"),
		# #WSE Operations - game_key_get_key
		# (game_key_get_key, reg0, gk_order_4),
		# (call_script, "script_str_store_key_name", s10, reg0), #F4
		# (game_key_get_key, reg0, gk_order_5),
		# (call_script, "script_str_store_key_name", s11, reg0), #F5
		# (game_key_get_key, reg0, gk_order_6),
		# (call_script, "script_str_store_key_name", s12, reg0), #F6
		(str_store_string, s10, "str_0x3e"), #F4
		(str_store_string, s11, "str_0x3f"), #F5
		(str_store_string, s12, "str_0x40"), #F6...no way other than WSE to get the string for what is assigned to a game key
		(call_script, "script_str_store_key_name", s13, "$key_order_7"), #F7
		(call_script, "script_str_store_key_name", s14, "$key_order_8"), #F8
		(call_script, "script_str_store_key_name", s15, "$key_order_9"), #F9
		
		(assign, ":y_position", 560),
		(try_begin), #Figure out which orders to display, set strings
			(party_slot_eq, "p_main_party", slot_party_gk_order, 0),
			(try_begin),
				(this_or_next|eq, "$g_next_menu", "mnu_simple_encounter"), #mst_lead_charge
			    (eq, "$g_next_menu", "mnu_join_battle"),
				(str_store_string, s1, "@{s10} - Formation type orders"),
				(str_store_string, s2, "@{s11} - Weapon orders"),
				(str_store_string, s3, "@{s12} - Shield orders"),
				(str_store_string, s4, "@{s13} - Attack orders"),
			
				(assign, ":num_orders", 4),
			(else_try),
				(str_store_string, s1, "@{s11} - Weapon orders"),
				(str_store_string, s2, "@{s12} - Shield orders"),
				(str_store_string, s3, "@{s13} - Attack orders"),
			
				(assign, ":num_orders", 3),
			(try_end),
			(assign, ":y_position", 473), #470
		(else_try),
		    (party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_4),
			(str_store_string, s1, "@{s10} - Ranks"),
			(str_store_string, s2, "@{s11} - Shieldwall"),
            (str_store_string, s3, "@{s12} - Wedge"),
			(str_store_string, s4, "@{s13} - Square"),
			(str_store_string, s5, "@{s14} - No Formation"),
			(str_store_string, s6, "@{s15} - Escape Menu"),
			
            (assign, ":num_orders", 6),
		(else_try),	
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_5),
			(str_store_string, s1, "@{s11} - One Handers"),
			(str_store_string, s2, "@{s12} - Two Handers"),
            (str_store_string, s3, "@{s13} - Polearms"),
			(str_store_string, s4, "@{s14} - Ranged"),
			(str_store_string, s5, "@{s15} - Escape Menu"),

            (assign, ":num_orders", 5),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_6),
			(str_store_string, s1, "@{s11} - Use Shields"),
			(str_store_string, s2, "@{s12} - No Shields"),
			(str_store_string, s3, "@{s13} - Free"),
			(str_store_string, s4, "@{s15} - Escape Menu"),
			
            (assign, ":num_orders", 4),
		(else_try),
			(party_slot_eq, "p_main_party", slot_party_gk_order, "$key_order_7"),
			(str_store_string, s1, "@{s10} - End Order"),
			(str_store_string, s2, "@{s11} - Skirmish"),
			(str_store_string, s3, "@{s12} - Volley Fire"),
			(str_store_string, s4, "@{s13} - Brace Polearms"),
			(str_store_string, s5, "@{s15} - Escape Menu"),
			
            (assign, ":num_orders", 5),
		(try_end),
		(party_get_slot, ":starting_order", "p_main_party", slot_party_gk_order),
		(party_set_slot, "p_main_party_backup", slot_party_gk_order, ":starting_order"),

		(try_for_range, ":i", 0, ":num_orders"),
		    (store_add, ":string", ":i", 1),
			(str_store_string_reg, s0, ":string"),

		    (create_text_overlay, ":overlay", s0),
			(overlay_set_color, ":overlay", 0xFFFFFF),
			(position_set_x, pos1, 1000),
			(position_set_y, pos1, 1000),
			(overlay_set_size, ":overlay", pos1),
			(position_set_x, pos1, 0),
			(position_set_y, pos1, ":y_position"),
			(overlay_set_position, ":overlay", pos1),
			
			(troop_set_slot, order_frame_presobj, ":i", ":overlay"),
			
			(val_sub, ":y_position", 30),
		(try_end),
		(store_mul, ":add_back", 30, ":num_orders"),
		(val_add, ":y_position", ":add_back"),
		(val_sub, ":y_position", 3),
		(try_for_range, ":i", 0, ":num_orders"),
		    (create_mesh_overlay, ":overlay", "mesh_order_frame"),
			(position_set_x, pos1, 700),#712
			(position_set_y, pos1, 700),#780
			(overlay_set_size, ":overlay", pos1),
			
			(position_set_x, pos1, 0),
			(position_set_y, pos1, ":y_position"),
			(overlay_set_position, ":overlay", pos1),
			
			(val_sub, ":y_position", 30),
		(try_end),
		
		(try_begin),
			(neg|party_slot_eq, "p_main_party", slot_party_gk_order, 0),
			(create_mesh_overlay, ":overlay", "mesh_white_plane"),
			(overlay_set_color, ":overlay", 0),
			(overlay_set_alpha, ":overlay", 0x10),
			(position_set_x, pos1, 14000),
			(position_set_y, pos1, 4500),
			(overlay_set_size, ":overlay", pos1),
			
			(position_set_x, pos1, 0),
			(position_set_y, pos1, 498),
			(overlay_set_position, ":overlay", pos1),
		(try_end),    

		(presentation_set_duration, 999999),
	   ]),
	(ti_on_presentation_run,
       [(store_trigger_param_1, ":cur_time"),
        (gt, ":cur_time", 100), #0.1 Second after Pres. Start
        (try_begin),
		  (this_or_next|key_clicked, "$key_order_9"), #current exit key
		  (this_or_next|game_key_clicked, gk_order_1),
          (this_or_next|game_key_clicked, gk_order_2),
          (this_or_next|game_key_clicked, gk_order_3), #Order Keys not used by Expanded Orders
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
		  (this_or_next|game_key_clicked, gk_everyone_around_hear),
          (game_key_clicked, gk_reverse_order_group),
		  (presentation_set_duration, 0),
        (else_try),
			(assign, ":key", -1),
		    (try_begin),
				(game_key_clicked, gk_order_4),
			    (assign, ":key", 4),
			(else_try),
 			    (game_key_clicked, gk_order_5),
			    (assign, ":key", 5),
		    (else_try),
      			(game_key_clicked, gk_order_6),
		    	(assign, ":key", 6),
			(else_try),
			    (key_clicked, "$key_order_7"),
				(assign, ":key", 7),
		    (else_try),
			    (key_clicked, "$key_order_8"),
				(assign, ":key", 8),
			(try_end),
			(neq, ":key", -1),
			(try_begin),
			    (party_slot_eq, "p_main_party_backup", slot_party_gk_order, 0),
		        (presentation_set_duration, 0),
			(else_try),
			    (try_begin),
					(party_slot_eq, "p_main_party_backup", slot_party_gk_order, gk_order_4),
					(assign, ":min_key", 4),
					(assign, ":max_key", 8),
				(else_try),
					(party_slot_eq, "p_main_party_backup", slot_party_gk_order, gk_order_5),
					(assign, ":min_key", 5),
					(assign, ":max_key", 8),
				(else_try),
				    (party_slot_eq, "p_main_party_backup", slot_party_gk_order, gk_order_6),
					(assign, ":min_key", 5),
					(assign, ":max_key", 7),
				(else_try),
				    (party_slot_eq, "p_main_party_backup", slot_party_gk_order, "$key_order_7"),
					(assign, ":min_key", 4),
					(assign, ":max_key", 7),
				(try_end),
				(store_sub, ":num_orders", ":max_key", ":min_key"),
				(val_add, ":num_orders", 1),
				(store_sub, ":key_pressed", ":key", ":min_key"),
				(is_between, ":key_pressed", 0, ":num_orders"),
				(val_add, ":num_orders", 1), #For the cancel box
				(try_for_range, ":i", 0, ":num_orders"),
    				(troop_get_slot, ":overlay", order_frame_presobj, ":i"),
					(neq, ":i", ":key_pressed"),
					(overlay_animate_to_alpha, ":overlay", 400, 0x00),
					(val_add, ":overlay", ":num_orders"),
					(overlay_animate_to_alpha, ":overlay", 400, 0x00),
				(else_try),				
					(overlay_animate_to_alpha, ":overlay", 1100, 0x00),
					(val_add, ":overlay", ":num_orders"),
					(overlay_animate_to_alpha, ":overlay", 1100, 0x00),
				(try_end),			
				(presentation_set_duration, 200), #100
			(try_end),
        (try_end),
        ]),
	]),		

 ("caba_camera_mode_display", prsntf_read_only, 0, [
    (ti_on_presentation_load,
      [
        (set_fixed_point_multiplier, 1000),
		(presentation_set_duration, 200),
		
		(try_begin),
		    (main_hero_fallen),
			(str_store_string, s0, "@DeathCam"),
		(else_try),
		    (str_store_string, s0, "@Camera"),
		(try_end),
		(try_begin),
		    (eq, "$cam_mode", cam_mode_default),
			(str_store_string, s1, "@Default"),
		(else_try),
			(eq, "$cam_mode", cam_mode_follow),
			(str_store_string, s1, "@Follow"),
		(else_try),
			(eq, "$cam_mode", cam_mode_free),
			(str_store_string, s1, "@Free"),
		(try_end),
		
		(str_store_string, s0, "@{!}{s0} Mode: {s1}"),
		
		(create_text_overlay, "$g_presentation_obj_name_kingdom_1", s0),
		(overlay_set_color, "$g_presentation_obj_name_kingdom_1", 0xFFFFFF),
		(position_set_x, pos1, 1000),
		(position_set_y, pos1, 1000),
		(overlay_set_size, "$g_presentation_obj_name_kingdom_1", pos1),
		(position_set_x, pos1, 750),
		(position_set_y, pos1, 625),
		(overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),
		
		(create_mesh_overlay, "$g_presentation_obj_name_kingdom_2", "mesh_order_frame"), #order_frame" mp_ui_command_panel
		(position_set_x, pos1, 570),
		(position_set_y, pos1, 725),
		(overlay_set_size, "$g_presentation_obj_name_kingdom_2", pos1),		
		(position_set_x, pos1, 745),
		(position_set_y, pos1, 622),
		(overlay_set_position, "$g_presentation_obj_name_kingdom_2", pos1),
	   ]),
	(ti_on_presentation_run,
      [ 
        #(set_fixed_point_multiplier, 1000),	  
	    (store_trigger_param_1, ":time"),
		(ge, ":time", 1000),		
		(overlay_animate_to_alpha, "$g_presentation_obj_name_kingdom_1", 400, 0x00),
		(overlay_animate_to_alpha, "$g_presentation_obj_name_kingdom_2", 400, 0x00),
       ]),
    ]),
	
 ("prebattle_custom_divisions", 0, mesh_load_window, [ #diff mesh?
    (ti_on_presentation_load,
     [(set_fixed_point_multiplier, 1000),
	 
	  (try_for_range, ":i", soldiers_begin, soldiers_end),
	    (troop_set_slot, "trp_temp_array_a", ":i", -1), #Overlays
		(troop_set_slot, "trp_temp_array_b", ":i", -1), #Split- Percent
		(troop_set_slot, "trp_temp_array_c", ":i", -1), #Split- Division
	  (try_end),
	
	  #Headers
	  (create_text_overlay, reg0, "@Troop Assignments", tf_center_justify|tf_single_line|tf_with_outline),
      (overlay_set_color, reg0, 0xFFFFFFFF),
      (position_set_x, pos1, 1500),
      (position_set_y, pos1, 1500),
      (overlay_set_size, reg0, pos1),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 680),
      (overlay_set_position, reg0, pos1),

	  (create_text_overlay, reg0, "@Split Troops into Secondary Divisions", tf_center_justify|tf_single_line),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 650),
      (overlay_set_position, reg0, pos1),
	  
      (create_text_overlay, reg0, "@Troops by^ Primary Division",  tf_center_justify),
      (position_set_x, pos1, 170),
      (position_set_y, pos1, 600),
      (overlay_set_position, reg0, pos1),

	  (position_set_x, pos2, 800),
      (position_set_y, pos2, 800),
	  
      (create_text_overlay, reg0, "@# in^Main Division", tf_center_justify),
      (position_set_x, pos1, 352),
      #(position_set_y, pos1, 600),
      (overlay_set_position, reg0, pos1),
	  (overlay_set_size, reg0, pos2),
	  
	  (create_text_overlay, reg0, "@Show/^Hide", tf_center_justify),
      (position_set_x, pos1, 425),
      #(position_set_y, pos1, 600),
      (overlay_set_position, reg0, pos1),
	  (overlay_set_size, reg0, pos2),
	  
	  (create_text_overlay, reg0, "@# in^Secondary Division", tf_center_justify),
      (position_set_x, pos1, 630),
      #(position_set_y, pos1, 600),
      (overlay_set_position, reg0, pos1),
	  (overlay_set_size, reg0, pos2),
	  
	  (create_text_overlay, reg0, "@Secondary^Division", tf_center_justify),
      (position_set_x, pos1, 755), #added 55 to all
      #(position_set_y, pos1, 600),
      (overlay_set_position, reg0, pos1),
	  (overlay_set_size, reg0, pos2),

	  #Container
      (str_clear, s0),
      (create_text_overlay, "$g_presentation_obj_bugdet_report_container", s0, tf_scrollable_style_2),
      (position_set_x, pos1, 105),
      (position_set_y, pos1, 80),
      (overlay_set_position, "$g_presentation_obj_bugdet_report_container", pos1),
      (position_set_x, pos1, 750),
      (position_set_y, pos1, 500),
      (overlay_set_area_size, "$g_presentation_obj_bugdet_report_container", pos1),
      (set_container_overlay, "$g_presentation_obj_bugdet_report_container"),
   
	  #Count Classes to Set Proper Size
	  (party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
	  (assign, ":num_of_classes", 0),
	  (try_for_range, ":class", 0, 9),
		(assign, ":end", ":num_of_stacks"),
		(try_for_range, ":i", 0, ":end"),
			(party_stack_get_troop_id, ":troop_id", "p_main_party", ":i"),
			(neq, ":troop_id", "trp_player"),
			(neg|troop_is_hero, ":troop_id"),
			(troop_get_class, ":trp_class", ":troop_id"),
			(eq, ":trp_class", ":class"),

			(val_add, ":num_of_classes", 1),
			(assign, ":end", 0), #Break
		(try_end),
	  (try_end),
	  
	  #Calculate Container Size
      (assign, ":cur_y_adder", 20),
	  (store_mul, ":cur_y", ":num_of_stacks", ":cur_y_adder"),
	  (store_mul, ":class_y_addition", ":num_of_classes", 3), #For spaces, headings, lines
	  (val_mul, ":class_y_addition", ":cur_y_adder"),
	  (val_add, ":cur_y", ":class_y_addition"),
	  
	  #Troop List and Setting Controls
	  (try_for_range, ":class", 0, 9),
	    (assign, ":class_has_troops", 0),
		(assign, ":every_other", 0),
		(assign, ":title_y", ":cur_y"),

		(try_for_range, ":i", 0, ":num_of_stacks"),
			(party_stack_get_troop_id, ":troop_id", "p_main_party", ":i"),
			(neq, ":troop_id", "trp_player"),
			(neg|troop_is_hero, ":troop_id"),
			(troop_get_class, ":trp_class", ":troop_id"),
			(eq, ":trp_class", ":class"),
			
			(party_stack_get_size, ":stack_size", "p_main_party", ":i"),
			(party_stack_get_num_wounded, ":stack_wounded", "p_main_party", ":i"),
			(val_sub, ":stack_size", ":stack_wounded"),
			(gt, ":stack_size", 0),
			(assign, ":class_has_troops", 1),
			
			(val_sub, ":cur_y", ":cur_y_adder"),
			
			(try_begin), #Shade every other row
				(eq, ":every_other", 1),
				(create_mesh_overlay, reg0, "mesh_white_plane"),
				(position_set_x, pos1, 36200),
				(position_set_y, pos1, 1000),
				(overlay_set_size, reg0, pos1),
				(position_set_x, pos1, 15),
				(position_set_y, pos1, ":cur_y"),
				(overlay_set_position, reg0, pos1),
				(overlay_set_color, reg0, 0xFFFFFF),
				(overlay_set_alpha, reg0, 0x50),
				(assign, ":every_other", 0),
			(else_try),
				(assign, ":every_other", 1),
			(try_end),
			
			(str_store_troop_name, s1, ":troop_id"),
			(create_text_overlay, reg0, s1),
			(position_set_x, pos2, 900),
			(position_set_y, pos2, 900),
			(overlay_set_size, reg0, pos2),
			(position_set_x, pos1, 15),
			(position_set_y, pos1, ":cur_y"),
			(overlay_set_position, reg0, pos1),
			
			(assign, reg0, ":stack_size"),
			(str_store_string, s1, "str_reg0"), #Number in Primary Division
			(create_text_overlay, reg0, s1),
			(position_set_x, pos1, 240),
			(position_set_y, pos1, ":cur_y"),
			(overlay_set_position, reg0, pos1),
			(overlay_set_size, reg0, pos2),
			
			#Tick box to activate alternate division
			(create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"), 
			(position_set_x, pos1, 315),
			(position_set_y, pos1, ":cur_y"),
			(overlay_set_position, reg0, pos1),						
							
			(create_slider_overlay, reg0, 0, 51), #Percentage
			(position_set_x, pos1, 465),
			(position_set_y, pos1, ":cur_y"),
			(overlay_set_position, reg0, pos1),	
            (position_set_x, pos1, 500),
			(position_set_y, pos1, 500),
			(overlay_set_size, reg0, pos1),				
			(troop_set_slot, "trp_temp_array_a", ":troop_id", reg0), #store overlay ID for tracking changes
				
			(create_text_overlay, reg0, "@{!}% to split"), #Percent Value
			(position_set_x, pos1, 700),
			(position_set_y, pos1, 700),
			(overlay_set_size, reg0, pos1),
			(position_set_x, pos1, 465),
			(position_set_y, pos1, ":cur_y"),
			(overlay_set_position, reg0, pos1),
						
			(str_clear, s0),
			(create_text_overlay, reg0, s0), #Number in alt division
			(overlay_set_size, reg0, pos2),
			(position_set_x, pos1, 520),
			(position_set_y, pos1, ":cur_y"),
			(overlay_set_position, reg0, pos1),
			
			(create_combo_button_overlay, reg0), #Which alt division
			(try_for_range, ":button_class", 0, 9),
				(str_store_class_name, s0, ":button_class"),
				(overlay_add_item, reg0, s0),			
			(try_end),
			(overlay_add_item, reg0, "@{!}- Disabled -"),
			(position_set_x, pos1, 700),
			(position_set_y, pos1, ":cur_y"),
			(overlay_set_position, reg0, pos1),	
			(position_set_x, pos1, 600),
			(position_set_y, pos1, 600),
			(overlay_set_size, reg0, pos1),	
			(overlay_set_val, reg0, 9),
			

			#Check for saved values, set things appropriately
			(troop_get_slot, ":alt_percent", ":troop_id", slot_troop_prebattle_alt_division_percent),
			(troop_get_slot, ":alt_division", ":troop_id", slot_troop_prebattle_alt_division),
			(assign, ":display", 0),
			(try_begin),
				(this_or_next|gt, ":alt_percent", 0),
				(is_between, ":alt_division", 1, 9), #skip 0 if it is an empty slot
				(assign, ":display", 1),
			(try_end),
			(troop_get_slot, ":slider", "trp_temp_array_a", ":troop_id"),
			(store_add, ":end", ":slider", 4),
			(try_for_range, ":overlay", ":slider", ":end"),
			    (overlay_set_display, ":overlay", ":display"),	
			(try_end),
			(eq, ":display", 1),
			(store_sub, ":overlay", ":slider", 1),
			(overlay_set_val, ":overlay", 1), #Tick box ticked
			
			(try_begin),
				(is_between, ":alt_division", 0, 9), #skip 0 if it is an empty slot
				(val_add, ":overlay", 4),
				(overlay_set_val, ":overlay", ":alt_division"),
			(try_end),
			
			#Calculate/display saved split
			(gt, ":alt_percent", 0),
			(overlay_set_val, ":slider", ":alt_percent"),
			(store_add, ":overlay", ":slider", 1),
			(assign, reg0, ":alt_percent"),
			(overlay_set_text, ":overlay", "str_reg0_percent"),
			(store_mul, ":alt_num", ":alt_percent", ":stack_size"),
			(val_div, ":alt_num", 100),
			(val_sub, ":stack_size", ":alt_num"),
			(val_sub, ":overlay", 3),
			(assign, reg0, ":stack_size"),
			(overlay_set_text, ":overlay", "str_reg0"),
			(val_add, ":overlay", 4),
			(assign, reg0, ":alt_num"),
			(overlay_set_text, ":overlay", "str_reg0"),
		(try_end), #End Stack/Troop Loop
		(eq, ":class_has_troops", 1),
		
		(str_store_class_name, s1, ":class"),
		(create_text_overlay, reg0, s1, tf_with_outline), 
		(position_set_x, pos1, 1000),
		(position_set_y, pos1, 1000),
		(overlay_set_size, reg0, pos1),
		(position_set_x, pos1, 25),
		(position_set_y, pos1, ":title_y"),
		(overlay_set_position, reg0, pos1),
		
		(val_sub, ":cur_y", ":cur_y_adder"),
		
		#Draw Line
		(create_mesh_overlay, reg0, "mesh_white_plane"),
        (position_set_x, pos1, 37000),
        (position_set_y, pos1, 150),
        (overlay_set_size, reg0, pos1),
        (position_set_x, pos1, 5),
        (position_set_y, pos1, ":cur_y"),
        (overlay_set_position, reg0, pos1),
        (overlay_set_color, reg0, 0),
		
		(val_sub, ":cur_y", ":cur_y_adder"),
		(val_sub, ":cur_y", ":cur_y_adder"),
	 (try_end), #End Class Loop

	 (set_container_overlay, -1),
	 
	 	#Tick box to activate/disable splitting divisions
		(create_check_box_overlay, "$g_presentation_obj_custom_battle_designer_20", "mesh_checkbox_off", "mesh_checkbox_on"), 
		(position_set_x, pos1, 830),
		(position_set_y, pos1, 680),
		(overlay_set_position, "$g_presentation_obj_custom_battle_designer_20", pos1),	
		(party_get_slot, ":value", "p_main_party", slot_party_prebattle_customized_divisions),
		(overlay_set_val, "$g_presentation_obj_custom_battle_designer_20", ":value"),
		(str_store_string, s0, "@Disabled"),
		(str_store_string, s1, "@Split Active"),
		(str_store_string_reg, s2, ":value"),
		
	 	(create_text_overlay, reg0, s2),
		(position_set_x, pos1, 850),
		(position_set_y, pos1, 675),
		(overlay_set_position, reg0, pos1),
			
		#Bottom Buttons
	  	(create_game_button_overlay, "$g_presentation_obj_battle_25", "@Clear All"), 
        (position_set_x, pos1, 420),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_battle_25", pos1),
		
		(create_game_button_overlay, "$g_presentation_obj_battle_26", "@Discard Changes"), 
        (position_set_x, pos1, 580),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_battle_26", pos1),
		
		(create_game_button_overlay, "$g_presentation_obj_battle_27", "@Save"),
        (position_set_x, pos1, 740),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_battle_27", pos1),
		
		(create_game_button_overlay, "$g_presentation_obj_battle_28", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_battle_28", pos1),	 
	 
	 (presentation_set_duration, 999999),
     ]),
	(ti_on_presentation_run,
      [	
	    (try_begin),
			(key_clicked, key_escape),
			(presentation_set_duration, 0),
			(party_set_slot, "p_main_party", slot_party_prebattle_customized_divisions, 0),
        (try_end),
      ]),
    (ti_on_presentation_event_state_change,
     [
       (store_trigger_param_1, ":object"),
       (store_trigger_param_2, ":value"),
	   
	    (try_begin), #Done
			(eq, ":object", "$g_presentation_obj_battle_28"),
			(presentation_set_duration, 0),
		(else_try), #Save
			(eq, ":object", "$g_presentation_obj_battle_27"),
			#Loop to Set Troop Slots from Temp Arrays
			(party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
			(try_for_range, ":i", 0, ":num_of_stacks"),
				(party_stack_get_troop_id, ":troop_id", "p_main_party", ":i"),
				(troop_get_slot, ":percent", "trp_temp_array_b", ":troop_id"),
				(try_begin),
					(gt, ":percent", -1),
					(troop_set_slot, ":troop_id", slot_troop_prebattle_alt_division_percent, ":percent"),
				(try_end),
				(troop_get_slot, ":division", "trp_temp_array_c", ":troop_id"),	
				(try_begin),
					(gt, ":division", -1),
					(troop_set_slot, ":troop_id", slot_troop_prebattle_alt_division, ":division"),
				(try_end),				
			(try_end),			
			(party_set_slot, "p_main_party", slot_party_prebattle_customized_divisions, 1),
			(overlay_set_val, "$g_presentation_obj_custom_battle_designer_20", 1),
			(store_add, ":overlay", "$g_presentation_obj_custom_battle_designer_20", 1),
			(overlay_set_text, ":overlay", "@Split Active"),		
		(else_try), #Discard (reload saved)
		    (eq, ":object", "$g_presentation_obj_battle_26"),
			(start_presentation, "prsnt_prebattle_custom_divisions"), 
	    (else_try), #Clear All(&Disable)
		    (eq, ":object", "$g_presentation_obj_battle_25"),
		    (try_for_range, ":troop_id", soldiers_begin, soldiers_end), 
				(troop_set_slot, ":troop_id", slot_troop_prebattle_alt_division, -1),
				(troop_set_slot, ":troop_id", slot_troop_prebattle_alt_division_percent, -1),
		    (try_end),
		    (party_set_slot, "p_main_party", slot_party_prebattle_customized_divisions, 0),
			(start_presentation, "prsnt_prebattle_custom_divisions"), 	
        (else_try),	#Active/Disable Tick Box
			(eq, ":object", "$g_presentation_obj_custom_battle_designer_20"),
			(str_store_string, s1, "@Split Active"),
			(str_store_string, s0, "@Disabled"),
			(str_store_string_reg, s2, ":value"),
			(store_add, ":overlay", ":object", 1),
			(overlay_set_text, ":overlay", s2),	 
			(party_set_slot, "p_main_party", slot_party_prebattle_customized_divisions, ":value"),
		(else_try), #Troop-specific settings
		    (party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
			(try_for_range, ":i", 0, ":num_of_stacks"),
				(party_stack_get_troop_id, ":troop_id", "p_main_party", ":i"),
				(troop_get_slot, ":overlay", "trp_temp_array_a", ":troop_id"), 
				(eq, ":object", ":overlay"), #Slider
				(is_between, ":value", 0, 51),
				(troop_set_slot, "trp_temp_array_b", ":troop_id", ":value"), #temp storage until 'save' is clicked
				
				(overlay_set_val, ":object", ":value"), #looks cleaner
				(store_add, ":other_overlay", ":overlay", 1),
				(assign, reg0, ":value"),
				(overlay_set_text, ":other_overlay", "str_reg0_percent"),	
				
				(party_stack_get_size, ":stack_size", "p_main_party", ":i"),
				(party_stack_get_num_wounded, ":stack_wounded", "p_main_party", ":i"),
				(val_sub, ":stack_size", ":stack_wounded"),
				
				#Calculate/display new split
				(store_mul, ":alt_num", ":value", ":stack_size"),
				(val_div, ":alt_num", 100),
				(val_sub, ":stack_size", ":alt_num"),
				(val_sub, ":other_overlay", 3),
				(assign, reg0, ":stack_size"),
				(overlay_set_text, ":other_overlay", "str_reg0"),
				(val_add, ":other_overlay", 4),
				(assign, reg0, ":alt_num"),
				(overlay_set_text, ":other_overlay", "str_reg0"),				
			(else_try),
			    (val_sub, ":overlay", 1),
				(eq, ":object", ":overlay"), #Check Box
				(store_add, ":begin", ":overlay", 1),
				(store_add, ":end", ":overlay", 5),
				(try_for_range, ":other_overlay", ":begin", ":end"),
					(overlay_set_display, ":other_overlay", ":value"),
				(try_end),
			(else_try),
				(val_add, ":overlay", 4), #Division combo box
				(eq, ":object", ":overlay"),				
				(troop_set_slot, "trp_temp_array_c", ":troop_id", ":value"), #temp storage until 'save' is clicked
			(try_end),	#Troop Loop
        (try_end),			
	 ]),
    ]),			
]
## Prebattle Orders & Deployment End

battle_flag_addon = [
		##PBOD Begin
		(create_mesh_overlay, reg0, "mesh_flag4"),
		(overlay_set_alpha, reg0, 0),
		(create_mesh_overlay, reg0, "mesh_flag5"),
		(overlay_set_alpha, reg0, 0),
		(create_mesh_overlay, reg0, "mesh_flag6"),
		(overlay_set_alpha, reg0, 0),
		(create_mesh_overlay, reg0, "mesh_flag7"),
		(overlay_set_alpha, reg0, 0),
		(create_mesh_overlay, reg0, "mesh_flag8"),
		(overlay_set_alpha, reg0, 0),
		(create_mesh_overlay, reg0, "mesh_flag9"),
		(overlay_set_alpha, reg0, 0),
        ##PBOD End
 ]

battle_has_troops_replace = [
		(assign, "$num_classes", 0),
		(try_for_agents, ":agent"),
		  (agent_set_slot, ":agent", slot_agent_map_overlay_id, 0),
		  (agent_is_alive, ":agent"),
		  (agent_is_human, ":agent"),
		  (agent_is_non_player, ":agent"),
		  (agent_get_party_id, ":party", ":agent"),
		  (eq, ":party", "p_main_party"),
		  (agent_get_division, ":troop_class", ":agent"),
] 
 
from util_common import *
from util_wrappers import *
from util_presentations import *

def modmerge_presentations(orig_presentations):
	add_objects(orig_presentations, presentations, True)	#add_presentations doesn't work
	
    # inject code into battle presentation
	try:
		find_i = list_find_first_match_i( orig_presentations, "battle" )
		battlep = PresentationWrapper(orig_presentations[find_i])
		codeblock = battlep.FindTrigger(ti_on_presentation_load).GetOpBlock()
		pos = codeblock.FindLineMatching( (overlay_set_alpha, "$g_battle_map_cavalry_order_flag", 0) )
		codeblock.InsertAfter(pos, battle_flag_addon)			
	except:
		import sys
		print "Injecton 1 failed:", sys.exc_info()[1]
		raise
	try:
		find_i = list_find_first_match_i( orig_presentations, "battle" )
		battlep = PresentationWrapper(orig_presentations[find_i])
		codeblock = battlep.FindTrigger(ti_on_presentation_load).GetOpBlock()
		pos = codeblock.FindLineMatching( (try_for_agents, ":agent_no") )
		codeblock.RemoveAt(pos, 5) #removes try_for_agents loop and get_player_agent_no/troop_id
		pos = codeblock.FindLineMatching( (party_get_num_companion_stacks, ":num_stacks", "p_main_party") ) #removes try_for_range start of has_troop counting loop
		codeblock.RemoveAt(pos, 6)
		pos = codeblock.FindLineMatching( (assign, "$group8_has_troops", 0) )
		codeblock.InsertAfter(pos, battle_has_troops_replace)
	except:
		import sys
		print "Injecton 2 failed:", sys.exc_info()[1]
		raise

		# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "presentations"
        orig_presentations = var_set[var_name_1]
        modmerge_presentations(orig_presentations)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)