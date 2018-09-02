# Tournament Play Enhancements (1.5) by Windyplains

from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
from header_items import *   # Added for Show all Items presentation.
from module_items import *   # Added for Show all Items presentation.
import string

####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

presentations = [
###########################################################################################################################
#####                                                 OPTION DISPLAY                                                  #####
###########################################################################################################################
("tournament_options_panel", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
		
		(create_mesh_overlay, reg1, "mesh_face_gen_window"),
        (position_set_x, pos1, 0),
        (position_set_y, pos1, 0),
        (overlay_set_position, reg1, pos1),
		
		# GPU kit definitions.
		(assign, "$gpu_storage", "trp_tpe_presobj"),
		(assign, "$gpu_data",    "trp_tpe_presobj"),
		
        # Margin Declarations
		#(assign, ":checkbox_text_x_margin", 525), # was 20
		(assign, ":pos_x_options", 0), # was 610
		(assign, ":pos_x_proficiencies", -290),
		(assign, ":pos_y_proficiencies", -10),
		(store_sub, ":pos_x_titles", ":pos_x_options", 5),
		(assign, ":checkbox_text_x_margin", 20),
		(assign, ":checkbox_text_y_margin", 10),
		(assign, ":checkbox_frame_y_margin", -28),
		(assign, ":title_frame_y_margin", -38),
		(try_begin),
			(eq, wp_tpe_mod_opt_actual_gear, 1),
			(assign, ":pos_y_options", 500),
		(else_try),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
			(assign, ":pos_y_options", 1000),
		(else_try),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_display_settings),
			(assign, ":pos_y_options", 500),
		(try_end),
		#(assign, ":pos_y_enhancements", 400),
		
		# CHARACTER MENU BEGIN
		# OBJ 21 - Text
		(position_set_x, pos1, 290),
        (position_set_y, pos1, 345),
		
		(troop_get_slot, ":selected_profile", TPE_OPTIONS, tpe_val_menu_troop_pick),
		(create_combo_label_overlay, reg1),
        (overlay_set_position, reg1, pos1),
		(troop_set_slot, "trp_tpe_presobj", tpe_obj_menu_troop_pick, reg1),
		(party_get_num_companion_stacks, ":num_stacks","p_main_party"),
		(assign, ":hero_slot", 0),
        (try_for_range, ":stack_num", 0, ":num_stacks"),
			(store_add, ":slot_pick", tpe_val_menu_troop_1, ":hero_slot"),
			(party_stack_get_troop_id,":troop_no","p_main_party",":stack_num"),
			(troop_is_hero, ":troop_no"),
			(str_clear, s1),
			(str_store_troop_name, s1, ":troop_no"),
			(troop_set_slot, "trp_tpe_presobj", ":slot_pick", ":troop_no"),
			(try_begin),
				(ge, DEBUG_TPE_general, 2),
				(assign, reg31, ":slot_pick"),
				(display_message, "@DEBUG (TPE): Added '{s1}' to character chooser menu.  Slot #{reg31}"),
			(try_end),
			(val_add, ":hero_slot", 1),
			(overlay_add_item, reg1, "@{s1}"),
        (try_end),
		(overlay_set_val, reg1, ":selected_profile"),
		# CHARACTER MENU END
			
		# OBJ #1 - DESCRIPTION text box
		(create_text_overlay, reg1, "@TOURNAMENT SETTINGS",  tf_center_justify|tf_with_outline),
		(overlay_set_color, reg1, wp_white),
		(position_set_x, pos1, 745),
        (position_set_y, pos1, 665),
        (overlay_set_position, reg1, pos1),
		(position_set_x, pos1, 1400),
        (position_set_y, pos1, 1400),
		(overlay_set_size, reg1, pos1),	
		
		(call_script, "script_gpu_create_text_label", "str_tpe_label_difficulty_score", 745, 650, tpe_text_difficulty_score, gpu_center),
		(call_script, "script_tpe_get_difficulty_value"),
		
		(try_begin),
			(eq, wp_tpe_mod_opt_actual_gear, 0),
			# OBJ #24 - DESCRIPTION text box
			(create_text_overlay, "$g_presentation_obj_24"),
			(position_set_x, pos1, 80),
			(position_set_y, pos1, 310),
			(overlay_set_position, "$g_presentation_obj_24", pos1),
			(overlay_set_text, "$g_presentation_obj_24", "@You have nothing."),
		(try_end),
		
		# OBJ 25 - Weapon Logic text.
		(create_text_overlay, "$g_presentation_obj_25"),
		(position_set_x, pos1, 80),
        (position_set_y, pos1, 285),
		(overlay_set_position, "$g_presentation_obj_25", pos1),
		(overlay_set_text, "$g_presentation_obj_25", "@Your weapon selection is adequate."),
		(call_script, "script_tpe_weapon_logic", "$g_wp_tpe_troop"),
		
        # OBJ #2 - DONE button
        (create_game_button_overlay, "$g_presentation_obj_2", "@Done"),
        (position_set_x, pos1, 820),
        (position_set_y, pos1, 50),
        (overlay_set_position, "$g_presentation_obj_2", pos1),

		# OBJ #26 - DISPLAY SETTINGS button
		(try_begin),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
			(str_store_string, s1, "@Display Settings"),
		(else_try),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_display_settings),
			(str_store_string, s1, "@Combat Settings"),
		(else_try),
			(str_store_string, s1, "@ERROR!"),
		(try_end),
		(create_game_button_overlay, "$g_presentation_obj_26", "@{s1}"),
		(position_set_x, pos1, 660),
		(position_set_y, pos1, 50),
		(overlay_set_position, "$g_presentation_obj_26", pos1),
		
        # OBJ 22 - Character Portrait
		(create_mesh_overlay_with_tableau_material, "$g_presentation_obj_22", -1, "tableau_troop_note_mesh", "$g_wp_tpe_troop"),
        (position_set_x, pos2, 165), # 75 seemed to left adjust to the frame.
        (position_set_y, pos2, 390),
        (overlay_set_position, "$g_presentation_obj_22", pos2),
        (position_set_x, pos2, 800), #1150
        (position_set_y, pos2, 800), #1150
        (overlay_set_size, "$g_presentation_obj_22", pos2),
		
		#####################
		## OPTIONS SECTION ##
		#####################
		
		(str_clear, s0),
		(create_text_overlay, reg1, s0, tf_scrollable_style_2),
		(position_set_x, pos1, 580),
		(position_set_y, pos1, 105),
		(overlay_set_position, reg1, pos1),
		(position_set_x, pos1, 340),
		(position_set_y, pos1, 530), 
		(overlay_set_area_size, reg1, pos1),
		(set_container_overlay, reg1),
		############### OPTIONS CONTAINER BEGIN ###############
			(assign, ":pos_x", ":pos_x_options"),  # Sets the second column of options.
			(assign, ":pos_y", ":pos_y_options"),
			
			(str_clear, s1),
			(create_text_overlay, "$g_presentation_obj_17", s1, tf_vertical_align_center|tf_with_outline),
			(position_set_x, pos1, ":pos_x_titles"),
			(position_set_y, pos1, ":pos_y"),
			(overlay_set_position, "$g_presentation_obj_17", pos1),
				
			(try_begin),
				####### DISPLAY / GLOBAL SETTINGS #######
				(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_display_settings),
			
				## OBJ 17r1 - Text
				(val_add, ":pos_y", ":title_frame_y_margin"),
				(create_text_overlay, "$g_presentation_obj_17", "@Global Options", tf_vertical_align_center|tf_with_outline),
				(overlay_set_color, "$g_presentation_obj_17", wp_white),
				(position_set_x, pos1, ":pos_x_titles"),
				(position_set_y, pos1, ":pos_y"),
				(overlay_set_position, "$g_presentation_obj_17", pos1),
				
				(try_begin),
					(eq, wp_tpe_mod_opt_renown_scale_enabled, 1),
					## OBJ #36 - Option: Renown Scaling - checkbox
					(val_add, ":pos_y", ":title_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, reg1, "@Renown Scaling", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, reg1, pos1),
					(troop_set_slot, "trp_tpe_presobj", tpe_label_renown_scale, reg1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, reg1, "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, reg1, pos1),
					(troop_set_slot, "trp_tpe_presobj", tpe_checkbox_renown_scale, reg1),
					(overlay_set_val, reg1, "$g_wp_tpe_renown_scaling"),
				(try_end),
				
				# OBJ (211) - Option: Level Scaling - checkbox
				(val_add, ":pos_y", ":title_frame_y_margin"),
				# text
				(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
				(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
				(create_text_overlay, reg1, "@Enable level scaling", tf_left_align|tf_vertical_align_center),
				(overlay_set_position, reg1, pos1),
				# checkbox
				(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
				(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
				(create_check_box_overlay, reg1, "mesh_checkbox_off", "mesh_checkbox_on"),
				(overlay_set_position, reg1, pos1),
				(troop_set_slot, "trp_tpe_presobj", tpe_checkbox_level_scale, reg1),
				(troop_get_slot, ":setting", TPE_OPTIONS, tpe_val_level_scale),
				(overlay_set_val, reg1, ":setting"),
				
				## OBJ 17r1 - Text
				(val_add, ":pos_y", ":title_frame_y_margin"),
				(val_add, ":pos_y", ":title_frame_y_margin"),
				(create_text_overlay, "$g_presentation_obj_17", "@Display Options", tf_vertical_align_center|tf_with_outline),
				(overlay_set_color, "$g_presentation_obj_17", wp_white),
				(position_set_x, pos1, ":pos_x_titles"),
				(position_set_y, pos1, ":pos_y"),
				(overlay_set_position, "$g_presentation_obj_17", pos1),
				
				# OBJ (215) - Option: In Combat Display - checkbox
				(val_add, ":pos_y", ":title_frame_y_margin"),
				# text
				(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
				(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
				(create_text_overlay, reg1, "@Show combat display", tf_left_align|tf_vertical_align_center),
				(overlay_set_position, reg1, pos1),
				# checkbox
				(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
				(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
				(create_check_box_overlay, reg1, "mesh_checkbox_off", "mesh_checkbox_on"),
				(overlay_set_position, reg1, pos1),
				(troop_set_slot, "trp_tpe_presobj", tpe_checkbox_opt_icd, reg1),
				(overlay_set_val, reg1, "$g_wp_tpe_option_icd_active"),
				
				# OBJ (244) - Option: Display Health Bars - checkbox
				(try_begin),
					(eq, MOD_CUSTOM_COMMANDER_INSTALLED, 1), # This option is dependant upon Custom Commander scripts.
					(val_add, ":pos_y", ":title_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, reg1, "@Show health bars", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, reg1, pos1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, reg1, "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, reg1, pos1),
					(troop_set_slot, "trp_tpe_presobj", tpe_checkbox_show_health, reg1),
					(troop_get_slot, reg2, TPE_OPTIONS, tpe_val_show_health),
					(overlay_set_val, reg1, reg2),
				(try_end),
				
				# OBJ (215) - Option: Show team points - checkbox
				(val_add, ":pos_y", ":title_frame_y_margin"),
				# text
				(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
				(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
				(create_text_overlay, reg1, "@Show team points awarded", tf_left_align|tf_vertical_align_center),
				(overlay_set_position, reg1, pos1),
				# checkbox
				(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
				(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
				(create_check_box_overlay, reg1, "mesh_checkbox_off", "mesh_checkbox_on"),
				(overlay_set_position, reg1, pos1),
				(troop_set_slot, "trp_tpe_presobj", tpe_checkbox_opt_teampoints, reg1),
				(troop_get_slot, reg2, TPE_OPTIONS, tpe_val_opt_teampoints),
				(overlay_set_val, reg1, reg2),
				
				# OBJ (216) - Option: Show teammate's damage - checkbox
				(val_add, ":pos_y", ":title_frame_y_margin"),
				# text
				(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
				(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
				(create_text_overlay, reg1, "@Show teammate's damage", tf_left_align|tf_vertical_align_center),
				(overlay_set_position, reg1, pos1),
				# checkbox
				(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
				(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
				(create_check_box_overlay, reg1, "mesh_checkbox_off", "mesh_checkbox_on"),
				(overlay_set_position, reg1, pos1),
				(troop_set_slot, "trp_tpe_presobj", tpe_checkbox_opt_damage, reg1),
				(overlay_set_val, reg1, "$g_wp_tpe_option_team_damage"),
			
				# OBJ (226) - Option: Display awards during game - checkbox
				(val_add, ":pos_y", ":title_frame_y_margin"),
				# text
				(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
				(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
				(create_text_overlay, reg1, "@Show when awards are granted", tf_left_align|tf_vertical_align_center),
				(overlay_set_position, reg1, pos1),
				# checkbox
				(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
				(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
				(create_check_box_overlay, reg1, "mesh_checkbox_off", "mesh_checkbox_on"),
				(overlay_set_position, reg1, pos1),
				(troop_set_slot, "trp_tpe_presobj", tpe_checkbox_opt_awards, reg1),
				(troop_get_slot, reg2, TPE_OPTIONS, tpe_val_opt_awards),
				(overlay_set_val, reg1, reg2),
				
				# OBJ (232) - Option: Display points during game - checkbox
				(val_add, ":pos_y", ":title_frame_y_margin"),
				# text
				(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
				(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
				(create_text_overlay, reg1, "@Show when points are awarded", tf_left_align|tf_vertical_align_center),
				(overlay_set_position, reg1, pos1),
				# checkbox
				(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
				(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
				(create_check_box_overlay, reg1, "mesh_checkbox_off", "mesh_checkbox_on"),
				(overlay_set_position, reg1, pos1),
				(troop_set_slot, "trp_tpe_presobj", tpe_checkbox_opt_points, reg1),
				(troop_get_slot, reg2, TPE_OPTIONS, tpe_val_opt_points),
				(overlay_set_val, reg1, reg2),
			
			(else_try),
				####### COMBAT SETTINGS #######
				(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
				
				# OBJ (218) - Persistent Team slider
				(val_sub, ":pos_y", 75), 
				(store_add, ":text_pos_y", ":pos_y", 0), (position_set_y, pos1, ":text_pos_y"),
				(store_add, ":text_pos_x", ":pos_x", 155), (position_set_x, pos1, ":text_pos_x"),
				(create_slider_overlay, reg1, 0, 4),
				(troop_set_slot, "trp_tpe_presobj", tpe_slider_team_choice, reg1),
				(overlay_set_position, reg1, pos1),
				(troop_get_slot, ":team_option", "trp_player", slot_troop_tournament_team_request),
				(overlay_set_val, reg1, ":team_option"),
				
				(store_add, ":text_pos_y", ":pos_y", 30), (position_set_y, pos1, ":text_pos_y"),
				(store_add, ":text_pos_x", ":pos_x", 15), (position_set_x, pos1, ":text_pos_x"),
				(create_text_overlay, reg1, "@Team:", tf_left_align|tf_with_outline),
				(overlay_set_color, reg1, 0xDDDDDD),
				(overlay_set_position, reg1, pos1),
				
				# OBJ (219) - Persistent Team value text
				(store_add, ":text_pos_y", ":pos_y", 30), (position_set_y, pos1, ":text_pos_y"),
				(store_add, ":text_pos_x", ":pos_x", 300), (position_set_x, pos1, ":text_pos_x"),
				(troop_get_slot, reg2, "trp_player", slot_troop_tournament_team_request),
				(call_script, "script_tpe_color_team_name", reg2),
				(assign, ":color", reg1),
				(create_text_overlay, reg1, "@{s1}", tf_right_align|tf_with_outline),
				(overlay_set_color, reg1, ":color"),
				(overlay_set_position, reg1, pos1),
				(troop_set_slot, "trp_tpe_presobj", tpe_text_team_choice, reg1),
				
				# OBJ (217) - Persistent Bet slider
				(val_sub, ":pos_y", 75), 
				(store_add, ":text_pos_y", ":pos_y", 0), (position_set_y, pos1, ":text_pos_y"),
				(store_add, ":text_pos_x", ":pos_x", 155), (position_set_x, pos1, ":text_pos_x"),
				(create_slider_overlay, reg1, wp_tpe_bet_minimum, wp_tpe_bet_maximum),
				(troop_set_slot, "trp_tpe_presobj", tpe_slider_bet_value, reg1),
				(overlay_set_position, reg1, pos1),
				(troop_get_slot, ":bet_option", TPE_OPTIONS, tpe_val_bet_wager),
				(overlay_set_val, reg1, ":bet_option"),
				
				# OBJ (nil) - Persistent Bid label
				(store_add, ":text_pos_y", ":pos_y", 30), (position_set_y, pos1, ":text_pos_y"),
				(store_add, ":text_pos_x", ":pos_x", 15), (position_set_x, pos1, ":text_pos_x"),
				(create_text_overlay, reg1, "@Wager:", tf_left_align|tf_with_outline),
				(overlay_set_color, reg1, 0xDDDDDD),
				(overlay_set_position, reg1, pos1),
				
				# OBJ (218) - Persistent Bid value text
				(store_add, ":text_pos_y", ":pos_y", 30), (position_set_y, pos1, ":text_pos_y"),
				(store_add, ":text_pos_x", ":pos_x", 300), (position_set_x, pos1, ":text_pos_x"),
				(create_text_overlay, reg1, "@ ", tf_right_align|tf_with_outline),
				(troop_set_slot, "trp_tpe_presobj", tpe_text_bet_value, reg1),
				(overlay_set_color, reg1, 0xDDDDDD),
				(overlay_set_position, reg1, pos1),
				(troop_get_slot, reg21, TPE_OPTIONS, tpe_val_bet_wager),
				(overlay_set_text, reg1, "@{reg21} denars"),
				
				# OBJ (217) - Bid slider
				(val_sub, ":pos_y", 75), 
				(store_add, ":text_pos_y", ":pos_y", 0), (position_set_y, pos1, ":text_pos_y"),
				(store_add, ":text_pos_x", ":pos_x", 155), (position_set_x, pos1, ":text_pos_x"),
				(create_slider_overlay, reg1, 2, 10),
				(troop_set_slot, "trp_tpe_presobj", tpe_slider_bid_value, reg1),
				(overlay_set_position, reg1, pos1),
				(troop_get_slot, ":bet_option", TPE_OPTIONS, tpe_val_bet_bid),
				(overlay_set_val, reg1, ":bet_option"),
				
				# OBJ (nil) - Bid label
				(store_add, ":text_pos_y", ":pos_y", 30), (position_set_y, pos1, ":text_pos_y"),
				(store_add, ":text_pos_x", ":pos_x", 15), (position_set_x, pos1, ":text_pos_x"),
				(create_text_overlay, reg1, "@Bid:", tf_left_align|tf_with_outline),
				(overlay_set_color, reg1, 0xDDDDDD),
				(overlay_set_position, reg1, pos1),
				
				# OBJ (212) - Bid Setting Label
				(store_add, ":text_pos_y", ":pos_y", 30), (position_set_y, pos1, ":text_pos_y"),
				(store_add, ":text_pos_x", ":pos_x", 300), (position_set_x, pos1, ":text_pos_x"),
				(create_text_overlay, reg1, "@ ", tf_right_align|tf_with_outline),
				(troop_set_slot, "trp_tpe_presobj", tpe_text_bid_amount, reg1),
				(overlay_set_color, reg1, 0xDDDDDD),
				(overlay_set_position, reg1, pos1),
				
				# OBJ (212) - Bid Payout Label
				(val_sub, ":pos_y", 35), 
				(store_add, ":text_pos_y", ":pos_y", 0), (position_set_y, pos1, ":text_pos_y"),
				(store_add, ":text_pos_x", ":pos_x", 155), (position_set_x, pos1, ":text_pos_x"),
				(create_text_overlay, reg1, "@ ", tf_center_justify),
				(troop_set_slot, "trp_tpe_presobj", tpe_text_bet_payout, reg1),
				#(overlay_set_color, reg1, 0xDDDDDD),
				(overlay_set_position, reg1, pos1),
				(call_script, "script_tpe_calculate_wager_for_bid"),
				
				# OBJ (221) - Difficulty Setting slider
				(troop_get_slot, ":diff_setting", TPE_OPTIONS, tpe_val_diff_setting),
				(try_begin),
					(eq, ":diff_setting", 0),
					(troop_set_slot, "trp_tpe_presobj", tpe_random_diff_enabled, 1),
				(try_end),
				(val_sub, ":pos_y", 75), 
				(store_add, ":text_pos_y", ":pos_y", 0), (position_set_y, pos1, ":text_pos_y"),
				(store_add, ":text_pos_x", ":pos_x", 155), (position_set_x, pos1, ":text_pos_x"),
				(create_slider_overlay, reg1, 0, 24),
				(troop_set_slot, "trp_tpe_presobj", tpe_slider_difficulty, reg1),
				(overlay_set_position, reg1, pos1),
				(try_begin),
					(neg|troop_slot_eq, "trp_tpe_presobj", tpe_random_diff_enabled, 1),
					(overlay_set_val, reg1, ":diff_setting"),
				(else_try),
					(overlay_set_val, reg1, 0),
				(try_end),
				
				# OBJ (nil) - Difficulty label
				(store_add, ":text_pos_y", ":pos_y", 30), (position_set_y, pos1, ":text_pos_y"),
				(store_add, ":text_pos_x", ":pos_x", 15), (position_set_x, pos1, ":text_pos_x"),
				(create_text_overlay, reg1, "@Difficulty:", tf_left_align|tf_with_outline),
				(overlay_set_color, reg1, 0xDDDDDD),
				(overlay_set_position, reg1, pos1),
				
				# OBJ (223) - Difficulty Setting text
				(store_add, ":text_pos_y", ":pos_y", 30), (position_set_y, pos1, ":text_pos_y"),
				(store_add, ":text_pos_x", ":pos_x", 300), (position_set_x, pos1, ":text_pos_x"),
				(troop_get_slot, reg2, TPE_OPTIONS, tpe_val_diff_setting),
				(assign, ":diff_setting", reg2),
				(call_script, "script_tpe_difficulty_slider_effects", ":diff_setting"),
				(create_text_overlay, reg1, "@{s1}", tf_right_align|tf_with_outline),
				(overlay_set_color, reg1, reg5),
				(overlay_set_position, reg1, pos1),
				(troop_set_slot, "trp_tpe_presobj", tpe_text_diff_setting, reg1),
				
				# OBJ (213) - Team Numbers text (based on difficulty setting)
				(val_add, ":pos_y", ":checkbox_frame_y_margin"),
				(store_add, ":text_pos_y", ":pos_y", 0), (position_set_y, pos1, ":text_pos_y"),
				(store_add, ":text_pos_x", ":pos_x", 0), (position_set_x, pos1, ":text_pos_x"),
				(try_begin),
					(eq, ":diff_setting", 0),
					(str_store_string, s1, "@Random team number and size"),
				(else_try),
					(assign, reg2, "$g_tournament_next_num_teams"),
					(assign, reg3, "$g_tournament_next_team_size"),
					(str_store_string, s1, "@Match: {reg2} teams of {reg3} members"),
				(try_end),
				(create_text_overlay, reg1, "@{s1}", tf_left_align|tf_vertical_align_center),
				(troop_set_slot, "trp_tpe_presobj", tpe_text_team_number, reg1),
				#(overlay_set_color, reg1, 0xDDDDDD),
				(overlay_set_position, reg1, pos1),
				
				## OBJ 17r2 - Text
				(val_add, ":pos_y", ":checkbox_frame_y_margin"),
				(val_add, ":pos_y", ":checkbox_frame_y_margin"),
				#(assign, ":pos_x", ":pos_x_options"),
				(create_text_overlay, "$g_presentation_obj_17", "@Individual Options", tf_vertical_align_center|tf_with_outline),
				(overlay_set_color, "$g_presentation_obj_17", wp_white),
				(position_set_x, pos1, ":pos_x_titles"),
				(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
				(overlay_set_position, "$g_presentation_obj_17", pos1),

				(try_begin),
					(eq, wp_tpe_mod_opt_actual_gear, 0),
					## OBJ #37 - Always Randomize - checkbox
					(val_add, ":pos_y", ":checkbox_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, "$g_presentation_obj_37", "@Always randomize equipment", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, "$g_presentation_obj_37", pos1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, "$g_presentation_obj_37", "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, "$g_presentation_obj_37", pos1),
				(try_end),
				
				## OBJ #38 - Never Spawn - checkbox
				(val_add, ":pos_y", ":checkbox_frame_y_margin"),
				# text
				(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
				(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
				(create_text_overlay, "$g_presentation_obj_38", "@Never spawn this character", tf_left_align|tf_vertical_align_center),
				(overlay_set_position, "$g_presentation_obj_38", pos1),
				# checkbox
				(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
				(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
				(create_check_box_overlay, "$g_presentation_obj_38", "mesh_checkbox_off", "mesh_checkbox_on"),
				(overlay_set_position, "$g_presentation_obj_38", pos1),
				
				(try_begin),
					(eq, wp_tpe_mod_opt_actual_gear, 0),
					## OBJ - WEAPON TYPES
					(val_add, ":pos_y", ":checkbox_frame_y_margin"),
					(val_add, ":pos_y", ":checkbox_frame_y_margin"),
					(create_text_overlay, reg1, "@Weapon Choices             Skill", tf_vertical_align_center|tf_with_outline),
					(overlay_set_color, reg1, wp_white),
					(position_set_x, pos1, ":pos_x_titles"),
					(position_set_y, pos1, ":pos_y"),
					(overlay_set_position, reg1, pos1),
					
					## OBJ #4 - Lance - checkbox
					(val_add, ":pos_y", ":title_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, "$g_presentation_obj_4", "@Lance & Shield", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, "$g_presentation_obj_4", pos1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, "$g_presentation_obj_4", "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, "$g_presentation_obj_4", pos1),
					# Lance weapon proficiencies
					(store_proficiency_level, reg2, "$g_wp_tpe_troop", wpt_polearm),
					(store_sub, ":pos_x_wpt", ":pos_x", ":pos_x_proficiencies"), (position_set_x, pos1, ":pos_x_wpt"),
					(store_sub, ":pos_y_wpt", ":pos_y", ":pos_y_proficiencies"), (position_set_y, pos1, ":pos_y_wpt"),
					(create_text_overlay, reg1, "@{reg2}", tf_center_justify|tf_vertical_align_center),
					(overlay_set_position, reg1, pos1),
					
					## OBJ #5 - Bow & Arrows - checkbox
					(val_add, ":pos_y", ":checkbox_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, "$g_presentation_obj_5", "@Bow & Arrow", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, "$g_presentation_obj_5", pos1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, "$g_presentation_obj_5", "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, "$g_presentation_obj_5", pos1),
					# Bow weapon proficiencies
					(store_proficiency_level, reg2, "$g_wp_tpe_troop", wpt_archery),
					(store_sub, ":pos_x_wpt", ":pos_x", ":pos_x_proficiencies"), (position_set_x, pos1, ":pos_x_wpt"),
					(store_sub, ":pos_y_wpt", ":pos_y", ":pos_y_proficiencies"), (position_set_y, pos1, ":pos_y_wpt"),
					(create_text_overlay, reg1, "@{reg2}", tf_center_justify|tf_vertical_align_center),
					(overlay_set_position, reg1, pos1),
					
					## OBJ #6 - 1H & Shield - checkbox
					(val_add, ":pos_y", ":checkbox_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, "$g_presentation_obj_6", "@One Handed & Shield", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, "$g_presentation_obj_6", pos1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, "$g_presentation_obj_6", "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, "$g_presentation_obj_6", pos1),
					# One handed weapons weapon proficiencies
					(store_proficiency_level, reg2, "$g_wp_tpe_troop", wpt_one_handed_weapon),
					(store_sub, ":pos_x_wpt", ":pos_x", ":pos_x_proficiencies"), (position_set_x, pos1, ":pos_x_wpt"),
					(store_sub, ":pos_y_wpt", ":pos_y", ":pos_y_proficiencies"), (position_set_y, pos1, ":pos_y_wpt"),
					(create_text_overlay, reg1, "@{reg2}", tf_center_justify|tf_vertical_align_center),
					(overlay_set_position, reg1, pos1),
					
					## OBJ #7 - 2H Weapon - checkbox
					(val_add, ":pos_y", ":checkbox_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, "$g_presentation_obj_7", "@Two Handed Weapon", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, "$g_presentation_obj_7", pos1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, "$g_presentation_obj_7", "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, "$g_presentation_obj_7", pos1),
					# two handed weapons weapon proficiencies
					(store_proficiency_level, reg2, "$g_wp_tpe_troop", wpt_two_handed_weapon),
					(store_sub, ":pos_x_wpt", ":pos_x", ":pos_x_proficiencies"), (position_set_x, pos1, ":pos_x_wpt"),
					(store_sub, ":pos_y_wpt", ":pos_y", ":pos_y_proficiencies"), (position_set_y, pos1, ":pos_y_wpt"),
					(create_text_overlay, reg1, "@{reg2}", tf_center_justify|tf_vertical_align_center),
					(overlay_set_position, reg1, pos1),
					
					## OBJ #8 - Crossbow & Bolts - checkbox
					(val_add, ":pos_y", ":checkbox_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, "$g_presentation_obj_8", "@Crossbow & Bolts", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, "$g_presentation_obj_8", pos1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, "$g_presentation_obj_8", "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, "$g_presentation_obj_8", pos1),
					# crossbow weapon proficiencies
					(store_proficiency_level, reg2, "$g_wp_tpe_troop", wpt_crossbow),
					(store_sub, ":pos_x_wpt", ":pos_x", ":pos_x_proficiencies"), (position_set_x, pos1, ":pos_x_wpt"),
					(store_sub, ":pos_y_wpt", ":pos_y", ":pos_y_proficiencies"), (position_set_y, pos1, ":pos_y_wpt"),
					(create_text_overlay, reg1, "@{reg2}", tf_center_justify|tf_vertical_align_center),
					(overlay_set_position, reg1, pos1),
					
					## OBJ #9 - Throwing & Shield - checkbox
					(val_add, ":pos_y", ":checkbox_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, "$g_presentation_obj_9", "@Thrown Weapon & Shield", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, "$g_presentation_obj_9", pos1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, "$g_presentation_obj_9", "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, "$g_presentation_obj_9", pos1),
					# javelin weapon proficiencies
					(store_proficiency_level, reg2, "$g_wp_tpe_troop", wpt_throwing),
					(store_sub, ":pos_x_wpt", ":pos_x", ":pos_x_proficiencies"), (position_set_x, pos1, ":pos_x_wpt"),
					(store_sub, ":pos_y_wpt", ":pos_y", ":pos_y_proficiencies"), (position_set_y, pos1, ":pos_y_wpt"),
					(create_text_overlay, reg1, "@{reg2}", tf_center_justify|tf_vertical_align_center),
					(overlay_set_position, reg1, pos1),
					
					## OBJ #10 - Polearm - checkbox
					(val_add, ":pos_y", ":checkbox_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, "$g_presentation_obj_10", "@Polearm (spear)", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, "$g_presentation_obj_10", pos1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, "$g_presentation_obj_10", "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, "$g_presentation_obj_10", pos1),
					# polearm weapon proficiencies
					(store_proficiency_level, reg2, "$g_wp_tpe_troop", wpt_polearm),
					(store_sub, ":pos_x_wpt", ":pos_x", ":pos_x_proficiencies"), (position_set_x, pos1, ":pos_x_wpt"),
					(store_sub, ":pos_y_wpt", ":pos_y", ":pos_y_proficiencies"), (position_set_y, pos1, ":pos_y_wpt"),
					(create_text_overlay, reg1, "@{reg2}", tf_center_justify|tf_vertical_align_center),
					(overlay_set_position, reg1, pos1),
					
					#### ENHANCEMENTS
					#OBJ - WEAPON TYPES
					(val_add, ":pos_y", ":checkbox_frame_y_margin"),
					(create_text_overlay, reg1, "@Enhancements", tf_vertical_align_center|tf_with_outline),
					(overlay_set_color, reg1, wp_white),
					(position_set_x, pos1, ":pos_x_titles"),
					(position_set_y, pos1, ":pos_y"),
					(overlay_set_position, reg1, pos1),
					
					## OBJ #11 - Horse - checkbox
					(val_add, ":pos_y", ":title_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, "$g_presentation_obj_11", "@Horse", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, "$g_presentation_obj_11", pos1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, "$g_presentation_obj_11", "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, "$g_presentation_obj_11", pos1),
					
					## OBJ #12 - Enhanced Horse - checkbox
					(val_add, ":pos_y", ":checkbox_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, "$g_presentation_obj_12", "@Enhanced Horse", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, "$g_presentation_obj_12", pos1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, "$g_presentation_obj_12", "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, "$g_presentation_obj_12", pos1),
					
					## OBJ #13 - Enhanced Armor - checkbox
					(val_add, ":pos_y", ":checkbox_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, "$g_presentation_obj_13", "@Enhanced Armor", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, "$g_presentation_obj_13", pos1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, "$g_presentation_obj_13", "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, "$g_presentation_obj_13", pos1),
					
					## OBJ #14 - Enhanced Weapons - checkbox
					(val_add, ":pos_y", ":checkbox_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, "$g_presentation_obj_14", "@Enhanced Weapons", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, "$g_presentation_obj_14", pos1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, "$g_presentation_obj_14", "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, "$g_presentation_obj_14", pos1),
					
					## OBJ #15 - Enhanced Shield - checkbox
					(val_add, ":pos_y", ":checkbox_frame_y_margin"),
					# text
					(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
					(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
					(create_text_overlay, "$g_presentation_obj_15", "@Enhanced Shield", tf_left_align|tf_vertical_align_center),
					(overlay_set_position, "$g_presentation_obj_15", pos1),
					# checkbox
					(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
					(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
					(create_check_box_overlay, "$g_presentation_obj_15", "mesh_checkbox_off", "mesh_checkbox_on"),
					(overlay_set_position, "$g_presentation_obj_15", pos1),
				(try_end),
			(try_end), # End of display type.
		############### OPTIONS CONTAINER END ###############	
		(set_container_overlay, -1),
		
		#####################
		## INFOBOX SECTION ##
		#####################
		
		# OBJ - Title
		(position_set_x, pos1, 65),
		(position_set_y, pos1, 175),
		(str_store_string, s1, "@Basic Options"),
		(create_text_overlay, "$g_presentation_obj_3", "@{s1}", tf_left_align|tf_with_outline),
		(overlay_set_color, "$g_presentation_obj_3", wp_white),
		(overlay_set_position, "$g_presentation_obj_3", pos1),
			
		# OBJ - Text
		(str_store_string, s2, "@You may choose three from the following\
								^weapon or enhancement options that will\
								^determine your starting equipment.  \
								^Additional options to the right allow you \
								^to set persistent options for each round."),
		(create_text_overlay, "$g_presentation_obj_16", "@{s2}"),
		(position_set_x, pos1, 70),
		(position_set_y, pos1, 55),
		(overlay_set_position, "$g_presentation_obj_16", pos1),
		
		# Set the initial checkbox positions
		(call_script, "script_tpe_update_presentation"),
      ]),
	
	(ti_on_presentation_mouse_enter_leave,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
		
		(try_begin),
			# Mouse left object and shouldn't be in another object so clear out the infobox.
			(eq, ":value", 1),
			(str_clear, s1),
			(str_clear, s2),
			
		(else_try), ###### HELP - DONE BUTTON ######
			(eq, ":object", "$g_presentation_obj_2"),
			(str_store_string, s1, "@The 'Done' Button"),
			(str_store_string, s2, "@This will end the current presentation and \
									^return to the tournament menu.^^^^"),
									
		(else_try), ###### HELP - SETTINGS BUTTON ######
			(eq, ":object", "$g_presentation_obj_26"),
			(str_store_string, s1, "@The 'Settings' Button"),
			(str_store_string, s2, "@This will toggle between the option displays\
									^for visual and text effects or combat\
									^preferences.^^^"),
									
		(else_try), ###### HELP - CHARACTER SELECTOR ######
			#(eq, ":object", "$g_presentation_obj_18"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_obj_menu_troop_pick, ":object"),
			(str_store_string, s1, "@The 'Character' Chooser"),
			(str_store_string, s2, "@Using the arrows you can cycle through\
									^your character and each companion you\
									^currently have in your party.^^^"),
									
		(else_try), ###### HELP - PERSISTENT BET ######
			(this_or_next|troop_slot_eq, "trp_tpe_presobj", tpe_slider_bet_value, ":object"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_text_bet_value, ":object"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
			(str_store_string, s1, "@The 'Persistent Bet' Slider"),
			(str_store_string, s2, "@By setting this slider you will automatically\
									^place the appropriate bet amount every\
									^round of a tournament if you have enough\
									^money to do so.\
									^Note: This works for the player only.^"),
									
		(else_try), ###### HELP - TEAM SLIDER ######
			(this_or_next|troop_slot_eq, "trp_tpe_presobj", tpe_slider_team_choice, ":object"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_text_team_choice, ":object"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
			(str_store_string, s1, "@The 'Persistent Team' Slider"),
			(str_store_string, s2, "@By setting this slider you will automatically\
									^be placed on the requested team if there\
									^is enough teams to support it.  Team order\
									^is red, blue, green then yellow.\
									^Note: This works for the player only.^"),
									
		(else_try), ###### HELP - DIFFICULTY SLIDER ######
			(this_or_next|troop_slot_eq, "trp_tpe_presobj", tpe_slider_difficulty, ":object"),
			(this_or_next|troop_slot_eq, "trp_tpe_presobj", tpe_text_team_number, ":object"), 
			(troop_slot_eq, "trp_tpe_presobj", tpe_text_diff_setting, ":object"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
			(call_script, "script_tpe_difficulty_display_info"),

		(else_try), ###### HELP - RENOWN SCALING ###### 
			(this_or_next|troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_renown_scale, ":object"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_label_renown_scale, ":object"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_display_settings),
			(str_store_string, s1, "@The 'Renown Scaling' Checkbox"),
			(str_store_string, s2, "@With this enabled you will gain an amount\
									^of renown on a tournament win proportional\
									^to your level and renown.  The higher your\
									^level or renown is the less you will receive.\
									^Note: This works for the player only.^"),
									
		(else_try), ###### HELP - DISPLAY HEALTH BARS ###### 
			(troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_show_health, ":object"),
			(eq, MOD_CUSTOM_COMMANDER_INSTALLED, 1), # This option is dependant upon Custom Commander scripts.
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_display_settings),
			(str_store_string, s1, "@The 'Display Health Bars' Checkbox"),
			(str_store_string, s2, "@With this enabled you see health bars shown\
									^above each participant's head based upon your\
									^settings selected in the main mod settings.^^^"),
									
		(else_try), ###### HELP - ALWAYS RANDOMIZE OPTION ######
			(eq, ":object", "$g_presentation_obj_37"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
			(str_store_string, s1, "@The 'Always Randomize' Checkbox"),
			(str_store_string, s2, "@With this enabled you will always have\
									^random options chosen each round.  This\
									^allows you to have an experience closer\
									^to native gameplay.\
									^Note: This works for the player only.^"),
									
		(else_try), ###### HELP - NEVER SPAWN OPTION ######
			(eq, ":object", "$g_presentation_obj_38"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
			(str_store_string, s1, "@The 'Never Spawn' Checkbox"),
			(str_store_string, s2, "@With this enabled the selected character\
									^will never be chosen to join tournaments\
									^to keep out companions that are not meant\
									^to be fighters.\
									^Note: This works for companions only.^"),
									
		(else_try), ###### HELP - HORSE OPTION ######
			(eq, ":object", "$g_presentation_obj_11"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
			(str_store_string, s1, "@The 'Horse' Checkbox"),
			(str_store_string, s2, "@You will always enter play mounted.  By\
									^enabling this you open up the option to\
									^select the enhanced horse which is a\
									^warhose.^^"),
									
		(else_try), ###### HELP - SHOW COMBAT DISPLAY OPTION ######
			(troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_opt_icd, ":object"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_display_settings),
			(str_store_string, s1, "@The 'Show Combat Display' Checkbox"),
			(str_store_string, s2, "@Enable this to see a realtime display of\
									^each team's remaining members, points\
									^acquired and the top three ranking members\
									^of the round.\
									^Note: This is currently disabled.^"),
									
		(else_try), ###### HELP - SHOW TEAMMATE DAMAGE OPTION ######
			(troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_opt_damage, ":object"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_display_settings),
			(str_store_string, s1, "@The 'Show Teammate Damage' Checkbox"),
			(str_store_string, s2, "@Enable this to see the damage dealt by\
									^your teammates displayed in the message\
									^window during combat.^^^"),
									
		(else_try), ###### HELP - SHOW COMBAT AWARDS OPTION ######
			(troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_opt_awards, ":object"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_display_settings),
			(str_store_string, s1, "@The 'Display Awards in Combat' Checkbox"),
			(str_store_string, s2, "@Enable this to see when competitors earn\
									^awards during combat.^^^^"),
									
		(else_try), ###### HELP - SHOW POINT AWARDS OPTION ######
			(troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_opt_points, ":object"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_display_settings),
			(str_store_string, s1, "@The 'Display Points in Combat' Checkbox"),
			(str_store_string, s2, "@Enable this to see when competitors earn\
									^points during combat.^^^^"),
									
		(else_try), ###### HELP - SHOW TEAM POINTS OPTION ######
			(troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_opt_teampoints, ":object"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_display_settings),
			(str_store_string, s1, "@The 'Display Team Point Awards' Checkbox"),
			(str_store_string, s2, "@Enable this to see when each team earns\
									^points during combat.^^^^"),
									
		(else_try), ###### HELP - LEVEL SCALING OPTION ######
			(troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_level_scale, ":object"),
			(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_display_settings),
			(str_store_string, s1, "@The 'Enable Level Scaling' Checkbox"),
			(str_store_string, s2, "@Enable this to cause generic opponents\
									^in the arena to scale with you to\
									^maintain an evened out difficulty effect.\
									^throughout your character's level.^^"),
		(try_end),
		(overlay_set_text, "$g_presentation_obj_3", "@{s1}"),
		(overlay_set_text, "$g_presentation_obj_16", "@{s2}"),
      ]),
	
    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
		
		(try_begin), ####### DONE BUTTON #######
			(eq, ":object", "$g_presentation_obj_2"),
			(troop_set_slot, TPE_OPTIONS, tpe_val_window_mode, 0),
			(presentation_set_duration, 0),
			
		(else_try), ####### DISPLAY SETTINGS BUTTON #######
			(eq, ":object", "$g_presentation_obj_26"),
			(try_begin),
				(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
				(troop_set_slot, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_display_settings),
			(else_try),
				(troop_slot_eq, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_display_settings),
				(troop_set_slot, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
			(try_end),
			(start_presentation, "prsnt_tournament_options_panel"),
			
		(else_try), ####### LANCE #######
			(eq, ":object", "$g_presentation_obj_4"),
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_lance, ":value", ":object"),
			
		(else_try), ####### BOW #######
			(eq, ":object", "$g_presentation_obj_5"),
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_bow, ":value", ":object"),
			
		(else_try), ####### ONE HANDED WEAPON #######
			(eq, ":object", "$g_presentation_obj_6"),
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_onehand, ":value", ":object"),
			
		(else_try), ####### TWO HANDED WEAPON #######
			(eq, ":object", "$g_presentation_obj_7"),
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_twohand, ":value", ":object"),
			
		(else_try), ####### CROSSBOW #######
			(eq, ":object", "$g_presentation_obj_8"),
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_crossbow, ":value", ":object"),
			
		(else_try), ####### THROWING WEAPONS #######
			(eq, ":object", "$g_presentation_obj_9"),
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_throwing, ":value", ":object"),
			
		(else_try), ####### POLEARMS #######
			(eq, ":object", "$g_presentation_obj_10"),
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_polearm, ":value", ":object"),
			
		(else_try), ####### HORSE #######
			(eq, ":object", "$g_presentation_obj_11"),
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_horse, ":value", ":object"),
			
		(else_try), ####### ENHANCED HORSE #######
			(eq, ":object", "$g_presentation_obj_12"),
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_enhanced_horse, ":value", ":object"),
			
		(else_try), ####### ENHANCED ARMOR #######
			(eq, ":object", "$g_presentation_obj_13"),
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_enhanced_armor, ":value", ":object"),
			
		(else_try), ####### ENHANCED WEAPONS #######
			(eq, ":object", "$g_presentation_obj_14"),
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_enhanced_weapons, ":value", ":object"),
			
		(else_try), ####### ENHANCED SHIELD #######
			(eq, ":object", "$g_presentation_obj_15"),
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_enhanced_shield, ":value", ":object"),
			
		(else_try), ####### CHARACTER SELECTOR #######
			(troop_slot_eq, "trp_tpe_presobj", tpe_obj_menu_troop_pick, ":object"),
			(troop_set_slot, TPE_OPTIONS, tpe_val_menu_troop_pick, ":value"),
			(store_add, ":troop_pick", tpe_val_menu_troop_1, ":value"),
			(troop_get_slot, "$g_wp_tpe_troop", "trp_tpe_presobj", ":troop_pick"),
			(start_presentation, "prsnt_tournament_options_panel"),
			
		(else_try), ####### PERSISTENT BET SLIDER #######
			(troop_slot_eq, "trp_tpe_presobj", tpe_slider_bet_value, ":object"),
			(troop_get_slot, ":obj_text", "trp_tpe_presobj", tpe_text_bet_value),
			(overlay_set_val, ":object", ":value"),
			(troop_set_slot, TPE_OPTIONS, tpe_val_bet_wager, ":value"),
			(assign, reg2, ":value"),
			(overlay_set_text, ":obj_text", "@{reg2} denars"),
			(call_script, "script_tpe_calculate_wager_for_bid"),
			
		(else_try), ####### POINT BID SLIDER #######
			(troop_slot_eq, "trp_tpe_presobj", tpe_slider_bid_value, ":object"),
			(troop_get_slot, ":slider_text", "trp_tpe_presobj", tpe_text_bid_amount),
			(troop_set_slot, TPE_OPTIONS, tpe_val_bet_bid, ":value"),
			(call_script, "script_tpe_calculate_wager_for_bid"),
			
		(else_try), ####### TEAM CHOICE SLIDER #######
			(troop_slot_eq, "trp_tpe_presobj", tpe_slider_team_choice, ":object"),
			(troop_get_slot, ":slider_text", "trp_tpe_presobj", tpe_text_team_choice),
			(call_script, "script_tpe_color_team_name", ":value"),
			(overlay_set_text, ":slider_text", "@{s1}"), # Change related text.
			(overlay_set_color, ":slider_text", reg1), # Change related text color
			(overlay_set_val, ":object", ":value"),  # Fix slider position.
			(troop_set_slot, "trp_player", slot_troop_tournament_team_request, ":value"),
			# Update difficulty score.
			(call_script, "script_tpe_get_difficulty_value"),
			
		(else_try), ####### RENOWN SCALING CHECKBOX #######
			(troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_renown_scale, ":object"),
			(assign, "$g_wp_tpe_renown_scaling", ":value"),
			
		(else_try), ####### ALWAYS RANDOMIZE CHECKBOX #######
			(eq, ":object", "$g_presentation_obj_37"),
			(try_begin),
				(eq, ":value", 1),
				(call_script, "script_tpe_clear_selections", "$g_wp_tpe_troop"),
				(troop_set_slot, "$g_wp_tpe_troop", slot_troop_tournament_always_randomize, 0),
				(call_script, "script_tpe_update_presentation"),
			(else_try),
				(troop_set_slot, "$g_wp_tpe_troop", slot_troop_tournament_always_randomize, 1),
			(try_end),
			# Update difficulty score.
			(call_script, "script_tpe_get_difficulty_value"),
			
		(else_try), ####### NEVER SPAWN CHECKBOX #######
			(eq, ":object", "$g_presentation_obj_38"),
			(try_begin),
				(neq, "$g_wp_tpe_troop", "trp_player"),
				(troop_set_slot, "$g_wp_tpe_troop", slot_troop_tournament_never_spawn, ":value"),
			(else_try),
				(display_message, "@You really don't want that turned ON for your main character."),
				(overlay_set_val, "$g_presentation_obj_38", 0),
			(try_end),
			
		(else_try), ####### DIFFICULTY SLIDER #######
			(troop_slot_eq, "trp_tpe_presobj", tpe_slider_difficulty, ":object"),
			(troop_set_slot, TPE_OPTIONS, tpe_val_diff_setting, ":value"), # Store the new difficulty setting.
			(overlay_set_val, ":object", ":value"),  # Fix slider position.
			(try_begin),
				(ge, ":value", 1),
				(troop_set_slot, "trp_tpe_presobj", tpe_random_diff_enabled, 0),
			(else_try),
				(troop_set_slot, "trp_tpe_presobj", tpe_random_diff_enabled, 1),
			(try_end),
		
			# Figure out what the new difficulty setting changes
			(call_script, "script_tpe_difficulty_slider_effects", ":value"),     # Reconfigure the teams & payout.
			(troop_get_slot, ":slider_text", "trp_tpe_presobj", tpe_text_diff_setting),
			(overlay_set_text, ":slider_text", "@{s1}"), # Change related text.
			(overlay_set_color, ":slider_text", reg5),
			
			# Update the current team information for this configuration.
			(troop_get_slot, ":team_text", "trp_tpe_presobj", tpe_text_team_number),
			(try_begin),
				(this_or_next|eq, ":value", 0),
				(troop_slot_eq, "trp_tpe_presobj", tpe_random_diff_enabled, 1),
				(str_store_string, s1, "@Random team number and size"),
			(else_try),
				(assign, reg2, "$g_tournament_next_num_teams"),
				(assign, reg3, "$g_tournament_next_team_size"),
				(str_store_string, s1, "@Match: {reg2} teams of {reg3} members"),
			(try_end),
			(overlay_set_text, ":team_text", "@{s1}"), # Change related text.
			
			# Update the bid payout
			(call_script, "script_tpe_calculate_wager_for_bid"),
			
			# Update the Infobox Display
			(call_script, "script_tpe_difficulty_display_info"),
			(overlay_set_text, "$g_presentation_obj_3", "@{s1}"),
			(overlay_set_text, "$g_presentation_obj_16", "@{s2}"),
			
			# Update difficulty score.
			(call_script, "script_tpe_get_difficulty_value"),
			
		(else_try), ####### SHOW TEAMMATE DAMAGE CHECKBOX #######
			(troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_opt_damage, ":object"),
			(assign, "$g_wp_tpe_option_team_damage", ":value"),
			(troop_get_slot, ":slider_text", "trp_tpe_presobj", tpe_checkbox_opt_damage),
			(overlay_set_val, ":object", "$g_wp_tpe_option_team_damage"),
			
		(else_try), ####### SHOW COMBAT DISPLAY CHECKBOX #######
			(troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_opt_icd, ":object"),
			(assign, "$g_wp_tpe_option_icd_active", ":value"),
			(troop_get_slot, ":slider_text", "trp_tpe_presobj", tpe_checkbox_opt_icd),
			(overlay_set_val, ":object", "$g_wp_tpe_option_icd_active"),
			
		(else_try), ####### LEVEL SCALING CHECKBOX #######
			(troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_level_scale, ":object"),
			(troop_set_slot, TPE_OPTIONS, tpe_val_level_scale, ":value"),
			# Update difficulty score.
			(call_script, "script_tpe_get_difficulty_value"),
			
		(else_try), ####### DISPLAY AWARDS CHECKBOX #######
			(troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_opt_awards, ":object"),
			(troop_set_slot, TPE_OPTIONS, tpe_val_opt_awards, ":value"),
		
		(else_try), ####### DISPLAY POINTS AWARDED CHECKBOX #######
			(troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_opt_points, ":object"),
			(troop_set_slot, TPE_OPTIONS, tpe_val_opt_points, ":value"),
		
		(else_try), ####### DISPLAY HEALTH BARS CHECKBOX #######
			(troop_slot_eq, "trp_tpe_presobj", tpe_checkbox_show_health, ":object"),
			(troop_set_slot, TPE_OPTIONS, tpe_val_show_health, ":value"),
		
		(try_end),
      ]),
    ]),
	
##################################################
####             RANKING DISPLAY              ####
##################################################
# Tournament menus are redirected here between rounds to display current ranking and options to continue to
# the next round.
  ("tpe_ranking_display", 0, mesh_load_window, [
    (ti_on_presentation_load,
    [
		(set_fixed_point_multiplier, 1000),
		(create_mesh_overlay, reg1, "mesh_face_gen_window"),
        (position_set_x, pos1, 0),
        (position_set_y, pos1, 0),
        (overlay_set_position, reg1, pos1),
		
		# GPU kit definitions.
		(assign, "$gpu_storage", "trp_tpe_presobj"),
		(assign, "$gpu_data",    "trp_tpe_presobj"),
		
		# OBJ #1 - EXIT TOURNAMENT button
		(try_begin),
			(eq, DEBUG_TPE_general, 1),
			(create_game_button_overlay, "$g_presentation_obj_1", "@DEBUG Mode Exit"),
        (else_try),
			(create_game_button_overlay, "$g_presentation_obj_1", "@Exit Tournament"),
		(try_end),
        (position_set_x, pos1, 140), # 430 aligned it to the right side.
        (position_set_y, pos1, 60),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
		
		# OBJ #2 - CONTINUE button
		(try_begin),
			(lt, "$g_tournament_cur_tier", wp_tpe_max_tournament_tiers),
			(str_store_string, s22, "@Continue"),
		(else_try),
			(str_store_string, s22, "@Finish"),
		(try_end),
        (create_game_button_overlay, "$g_presentation_obj_2", "@{s22}"),
        (position_set_x, pos1, 140),
        (position_set_y, pos1, 110),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
		
		# OBJ #4 - TOURNAMENT OPTIONS button
        (create_game_button_overlay, "$g_presentation_obj_4", "@Tournament Options"),
        (position_set_x, pos1, 280),
        (position_set_y, pos1, 290),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
		
		# OBJ #3 - RANKING DISPLAY button
		(call_script, "script_tpe_copy_array", tpe_ranking_array, tpe_tournament_roster, wp_tpe_max_tournament_participants),
		
		(try_begin),
			(eq, "$g_wp_tpe_rank_pres_mode", wp_tpe_tournament_ranking),
			(str_store_string, s11, "@Round Standings"),
			(call_script, "script_tpe_sort_troops_and_points", slot_troop_tournament_total_points),
			(assign, ":points_slot", slot_troop_tournament_total_points),
			(str_store_string, s12, "@Tournament Rankings"),
		(else_try),
			(eq, "$g_wp_tpe_rank_pres_mode", wp_tpe_round_ranking),
			(str_store_string, s11, "@Tournament Standings"),
			(call_script, "script_tpe_sort_troops_and_points", slot_troop_tournament_round_points),
			(assign, ":points_slot", slot_troop_tournament_round_points),
			(assign, reg3, "$g_tournament_cur_tier"),
			(str_store_string, s12, "@Round {reg3} Rankings"),
		(try_end),
		(create_game_button_overlay, "$g_presentation_obj_3", "@{s11}"),
		(position_set_x, pos1, 140),
        (position_set_y, pos1, 160),
		(overlay_set_position, "$g_presentation_obj_3", pos1),
		
		# Presentation title overlay, centered at the top of right pane
		
        (create_text_overlay, reg1, "@{s12}", tf_center_justify|tf_with_outline),
        (overlay_set_color, reg1, 0xDDDDDD),
		(position_set_x, pos1, 740),
        (position_set_y, pos1, 665),
        (overlay_set_position, reg1, pos1),
		(position_set_x, pos1, 1200),
        (position_set_y, pos1, 1200),
		(overlay_set_size, reg1, pos1),	
		
		
		### DIFFICULTY SLIDER - BEGIN ###
		(assign, ":pos_x", 235),
		(assign, ":pos_y", 210),
		# OBJ (221) - Difficulty Setting slider
		(troop_get_slot, ":diff_setting", TPE_OPTIONS, tpe_val_diff_setting),
		(try_begin),
			(eq, ":diff_setting", 0),
			(troop_set_slot, "trp_tpe_presobj", tpe_random_diff_enabled, 1),
		(try_end),
		(val_sub, ":pos_y", 75), 
		(store_add, ":text_pos_y", ":pos_y", 0), (position_set_y, pos1, ":text_pos_y"),
		(store_add, ":text_pos_x", ":pos_x", 125), (position_set_x, pos1, ":text_pos_x"),
		(create_slider_overlay, reg1, 0, 24),
		(troop_set_slot, "trp_tpe_presobj", tpe_slider_difficulty, reg1),
		(overlay_set_position, reg1, pos1),
		(try_begin),
			(neg|troop_slot_eq, "trp_tpe_presobj", tpe_random_diff_enabled, 1),
			(overlay_set_val, reg1, ":diff_setting"),
		(else_try),
			(overlay_set_val, reg1, 0),
		(try_end),
		
		# OBJ (nil) - Difficulty label
		(store_add, ":text_pos_y", ":pos_y", 35), (position_set_y, pos1, ":text_pos_y"),
		(store_add, ":text_pos_x", ":pos_x", -15), (position_set_x, pos1, ":text_pos_x"),
		(create_text_overlay, reg1, "@Difficulty:", tf_left_align|tf_with_outline),
		(overlay_set_color, reg1, 0xDDDDDD),
		(overlay_set_position, reg1, pos1),
		
		# OBJ (223) - Difficulty Setting text
		(store_add, ":text_pos_y", ":pos_y", 35), (position_set_y, pos1, ":text_pos_y"),
		(store_add, ":text_pos_x", ":pos_x", 235), (position_set_x, pos1, ":text_pos_x"),
		(troop_get_slot, reg2, TPE_OPTIONS, tpe_val_diff_setting),
		(assign, ":diff_setting", reg2),
		(call_script, "script_tpe_difficulty_slider_effects", ":diff_setting"),
		(create_text_overlay, reg1, "@{s1}", tf_right_align|tf_with_outline),
		(overlay_set_color, reg1, reg5),
		(overlay_set_position, reg1, pos1),
		(troop_set_slot, "trp_tpe_presobj", tpe_text_diff_setting, reg1),
		
		# OBJ (213) - Team Numbers text (based on difficulty setting)
		(val_add, ":pos_y", -23),
		(store_add, ":text_pos_y", ":pos_y", 0), (position_set_y, pos1, ":text_pos_y"),
		(store_add, ":text_pos_x", ":pos_x", -5), (position_set_x, pos1, ":text_pos_x"),
		(try_begin),
			(eq, ":diff_setting", 0),
			(str_store_string, s1, "@Random team number and size"),
		(else_try),
			(assign, reg2, "$g_tournament_next_num_teams"),
			(assign, reg3, "$g_tournament_next_team_size"),
			(str_store_string, s1, "@{reg2} teams of {reg3} members"),
		(try_end),
		(create_text_overlay, reg1, "@{s1}", tf_left_align|tf_vertical_align_center),
		(troop_set_slot, "trp_tpe_presobj", tpe_text_team_number, reg1),
		#(overlay_set_color, reg1, 0xDDDDDD),
		(overlay_set_position, reg1, pos1),
		### DIFFICULTY SLIDER - END ###
		
		(val_sub, ":pos_y", 80), 
		
		# OBJ (nil) - Persistent Bet label
		(store_add, ":text_pos_y", ":pos_y", 30), (position_set_y, pos1, ":text_pos_y"),
		(store_add, ":text_pos_x", ":pos_x", -15), (position_set_x, pos1, ":text_pos_x"),
		(create_text_overlay, reg1, "@Bid:", tf_left_align|tf_with_outline),
		(overlay_set_color, reg1, 0xDDDDDD),
		(overlay_set_position, reg1, pos1),
		
		# OBJ (218) - Persistent Bet value text
		(store_add, ":text_pos_y", ":pos_y", 30), (position_set_y, pos1, ":text_pos_y"),
		(store_add, ":text_pos_x", ":pos_x", 235), (position_set_x, pos1, ":text_pos_x"), # 250
		(create_text_overlay, reg1, "str_tpe_label_long_bid", tf_right_align|tf_with_outline),
		(troop_set_slot, "trp_tpe_presobj", tpe_text_bet_value, reg1),
		(store_troop_gold, ":current_cash", "trp_player"),
		(try_begin),
			(ge, ":current_cash", reg3),
			(overlay_set_color, reg1, 0xDDDDDD),
		(else_try),
			(overlay_set_color, reg1, gpu_red),
		(try_end),
		(overlay_set_position, reg1, pos1),
		(call_script, "script_tpe_calculate_wager_for_bid"),
		
		# OBJ (244) - Current cash value text
		# (store_add, ":text_pos_y", ":pos_y", 30), (position_set_y, pos1, ":text_pos_y"),
		# (store_add, ":text_pos_x", ":pos_x", 250), (position_set_x, pos1, ":text_pos_x"),
		# (assign, reg2, ":current_cash"),
		# (create_text_overlay, reg1, "@{reg2}", tf_right_align|tf_with_outline),
		# (troop_set_slot, "trp_tpe_presobj", tpe_text_cash_value, reg1),
		# (overlay_set_color, reg1, 0xDDDDDD),
		# (overlay_set_position, reg1, pos1),
		
		# OBJ (nil) - Current Cash
		(call_script, "script_gpu_create_mesh", "mesh_tpe_golden_coins", 458, 65, 250, 250),
		
			
		# OBJ # 8 - Page display for ranking information.
		(try_begin),
			(eq, "$g_wp_tpe_rank_pres_mode", wp_tpe_tournament_ranking),
			# (this_or_next|eq, "$g_wp_tpe_rank_pres_mode", wp_tpe_tournament_ranking),
			# (ge, "$g_wp_tpe_total_agents", 11),
			(create_combo_label_overlay, "$g_presentation_obj_8"),
			(position_set_x, pos1, 740),
			(position_set_y, pos1, 55),
			(overlay_set_position, "$g_presentation_obj_8", pos1),
			(overlay_add_item, "$g_presentation_obj_8", "@Page 1 (1-10)"),
			(overlay_add_item, "$g_presentation_obj_8", "@Page 2 (11-20)"),
			(overlay_set_val, "$g_presentation_obj_8", "$g_presentation_obj_9"),
		(try_end),
		(try_begin),
			(eq, "$g_wp_tpe_rank_pres_mode", wp_tpe_tournament_ranking),
			# (this_or_next|eq, "$g_wp_tpe_rank_pres_mode", wp_tpe_tournament_ranking),
			# (ge, "$g_wp_tpe_total_agents", 21),
			(overlay_add_item, "$g_presentation_obj_8", "@Page 3 (21-30)"),
			(overlay_set_val, "$g_presentation_obj_8", "$g_presentation_obj_9"),
		(try_end),
		(try_begin),
			(eq, "$g_wp_tpe_rank_pres_mode", wp_tpe_tournament_ranking),
			# (this_or_next|eq, "$g_wp_tpe_rank_pres_mode", wp_tpe_tournament_ranking),
			# (ge, "$g_wp_tpe_total_agents", 21),
			(overlay_add_item, "$g_presentation_obj_8", "@Page 4 (31-40)"),
			(overlay_set_val, "$g_presentation_obj_8", "$g_presentation_obj_9"),
		(try_end),
		(assign, ":low_rank", 0),
		(assign, ":high_rank", 10),
		(assign, ":rank_adjust", 0),
		(try_begin),
			(eq, "$g_presentation_obj_9", 1), # Page 2 (10-19)
			(assign, ":low_rank", 10),
			(assign, ":high_rank", 20),
			(assign, ":rank_adjust", 10),
		(else_try),
			(eq, "$g_presentation_obj_9", 2), # Page 3 (20-29)
			(assign, ":low_rank", 20),
			(assign, ":high_rank", 30),
			(assign, ":rank_adjust", 20),
		(else_try),
			(eq, "$g_presentation_obj_9", 3), # Page 4 (30-39)
			(assign, ":low_rank", 30),
			(assign, ":high_rank", 32),
			(assign, ":rank_adjust", 30),
		(try_end),
		
		(assign, ":player_found", 0),
		(try_for_range, ":slot_no", 0, wp_tpe_max_tournament_participants),
			(troop_get_slot, ":troop_no", tpe_ranking_array, ":slot_no"),
			(eq, ":troop_no", "trp_player"),
			(eq, ":player_found", 0),
			(val_add, ":player_found", 1),
			(assign, ":player_slot", ":slot_no"),
		(try_end),
		(try_for_range, ":ranking", ":low_rank", ":high_rank"),
			(store_add, ":rank_display", ":ranking", 1),
			(val_sub, ":rank_display", ":rank_adjust"),
			(store_add, ":rank_state", 30, ":rank_display"),
			(troop_set_slot, "trp_tpe_presobj", ":rank_state", 0),  # So that a box is force drawn.
			
			(store_mul, ":pos_y_adjust", 55, ":ranking"),
			(store_sub, ":pos_y", 600, ":pos_y_adjust"),
			(store_mul, ":slot_base", 10, ":ranking"),
			(val_add, ":slot_base", 100),
			(store_add, ":slot_pos_x", ":slot_base", 6),
			(store_add, ":slot_pos_y", ":slot_base", 7),
			(store_add, ":slot_type", ":slot_base", 8),
			
			(troop_get_slot, ":troop_no", tpe_ranking_array, ":ranking"),
			(troop_get_slot, ":points", ":troop_no", ":points_slot"),
			(troop_set_slot, "trp_tpe_presobj", ":slot_pos_x", 525),
			(troop_set_slot, "trp_tpe_presobj", ":slot_pos_y", ":pos_y"),
			(troop_set_slot, "trp_tpe_presobj", ":slot_type", wp_tpe_icd_round_rank),
			(try_begin),
				(this_or_next|ge, "$g_tournament_num_participants_for_fight", ":rank_display"),
				(eq, "$g_wp_tpe_rank_pres_mode", wp_tpe_tournament_ranking),
				(this_or_next|neq, ":troop_no", "trp_player"),
				(eq, ":ranking", ":player_slot"),
				(call_script, "script_tpe_create_ranking_box", ":troop_no", ":points", ":rank_display", 0), # 685 should line up with the top line of the shields.
			(try_end),
		(try_end),	
		
				
		(try_begin),
		###############################################
		# AWARDS DISPLAY +
		###############################################
			(eq, DEBUG_TPE_general, 0),
			
			# Increase the # of award display passes.
			(troop_get_slot, ":passes", tpe_award_data, tpe_award_display_passes),
			(val_add, ":passes", 1),
			(troop_set_slot, tpe_award_data, tpe_award_display_passes, ":passes"),
			
			(create_text_overlay, reg1, "@TOURNAMENT AWARDS", tf_center_justify|tf_with_outline),
			(overlay_set_color, reg1, 0xDDDDDD),
			(position_set_x, pos1, 280),
			(position_set_y, pos1, 630),
			(overlay_set_position, reg1, pos1),
			(position_set_x, pos1, 1200),
			(position_set_y, pos1, 1200),
			(overlay_set_size, reg1, pos1),
			
			(call_script, "script_gpu_create_text_label", "str_tpe_label_difficulty_score", 280, 615, tpe_text_difficulty_score, gpu_center),
			(call_script, "script_tpe_get_difficulty_value"),
		
			(str_clear, s0),
			(create_text_overlay, reg1, s0, tf_scrollable_style_2),
			(position_set_x, pos1, 40), # was 40
			(position_set_y, pos1, 335), # 285
			(overlay_set_position, reg1, pos1),
			(position_set_x, pos1, 460), # 420
			(position_set_y, pos1, 270), # 350
			(overlay_set_area_size, reg1, pos1),
			(set_container_overlay, reg1),
				(try_begin),
					# Check to see if these have been awarded & displayed already.  Prevent multiple gains by toggling presentations.
					(troop_slot_eq, tpe_award_data, tpe_award_display_passes, 1),
					(str_clear, s25),
					(assign, ":renown_gain", 0),
					(try_begin),
						(troop_slot_ge, tpe_award_data, tpe_first_blood, 0),
						(troop_get_slot, ":troop_no", tpe_award_data, tpe_first_blood),
						(str_store_troop_name, s2, ":troop_no"),
						(call_script, "script_tpe_award_scaled_xp", ":troop_no", tpe_award_swiftest_cut_xp),
						(assign, reg21, tpe_award_swiftest_cut_renown),
						(str_store_string, s25, "@{s25}^Swiftest Cut^Awarded to {s2}^+{reg1} experience^+{reg21} renown^"),
						(try_begin),
							(eq, ":troop_no", "trp_player"),
							(val_add, ":renown_gain", tpe_award_swiftest_cut_renown),
						(else_try),
							(call_script, "script_change_troop_renown", ":troop_no", tpe_award_swiftest_cut_renown),
						(try_end),
						(call_script, "script_tpe_increase_award_count", ":troop_no", 1),
					(try_end),
					(try_begin),
						(troop_slot_ge, tpe_award_data, tpe_most_kills, 0),
						(troop_get_slot, ":troop_no", tpe_award_data, tpe_most_kills),
						(troop_get_slot, ":kills", tpe_award_data, tpe_data_most_kills),
						(assign, reg2, ":kills"),
						(str_store_troop_name, s2, ":troop_no"),
						(call_script, "script_tpe_award_scaled_xp", ":troop_no", tpe_award_most_kills_xp),
						(assign, reg21, tpe_award_most_kills_renown),
						(str_store_string,s25, "@{s25}^Fiercest Competitor: {reg2}^Awarded to {s2}^+{reg1} experience^+{reg21} renown^"),
						(try_begin),
							(eq, ":troop_no", "trp_player"),
							(val_add, ":renown_gain", tpe_award_most_kills_renown),
						(else_try),
							(call_script, "script_change_troop_renown", ":troop_no", tpe_award_most_kills_renown),
						(try_end),
						(call_script, "script_tpe_increase_award_count", ":troop_no", 1),
					(try_end),
					(try_begin),
						(troop_slot_ge, tpe_award_data, tpe_berserker_1, 0),
						(troop_get_slot, ":troop_no", tpe_award_data, tpe_berserker_1),
						(str_store_troop_name, s2, ":troop_no"),
						(call_script, "script_tpe_award_scaled_xp", ":troop_no", tpe_award_dominant_presence_xp),
						(assign, reg21, tpe_award_dominant_presence_renown),
						(str_store_string, s25, "@{s25}^Dominant Presence^Awarded to {s2}^+{reg1} experience^+{reg21} renown^"),
						(try_begin),
							(eq, ":troop_no", "trp_player"),
							(val_add, ":renown_gain", tpe_award_dominant_presence_renown),
						(else_try),
							(call_script, "script_change_troop_renown", ":troop_no", tpe_award_dominant_presence_renown),
						(try_end),
						(call_script, "script_tpe_increase_award_count", ":troop_no", 1),
					(try_end),
					(try_begin),
						(troop_slot_ge, tpe_award_data, tpe_berserker_2, 0),
						(troop_get_slot, ":troop_no", tpe_award_data, tpe_berserker_2),
						(str_store_troop_name, s2, ":troop_no"),
						(call_script, "script_tpe_award_scaled_xp", ":troop_no", tpe_award_dominant_presence_xp),
						(assign, reg21, tpe_award_dominant_presence_renown),
						(str_store_string, s25, "@{s25}^Dominant Presence^Awarded to {s2}^+{reg1} experience^+{reg21} renown^"),
						(try_begin),
							(eq, ":troop_no", "trp_player"),
							(val_add, ":renown_gain", tpe_award_dominant_presence_renown),
						(else_try),
							(call_script, "script_change_troop_renown", ":troop_no", tpe_award_dominant_presence_renown),
						(try_end),
						(call_script, "script_tpe_increase_award_count", ":troop_no", 1),
					(try_end),
					(try_begin),
						(troop_slot_ge, tpe_award_data, tpe_berserker_3, 0),
						(troop_get_slot, ":troop_no", tpe_award_data, tpe_berserker_3),
						(str_store_troop_name, s2, ":troop_no"),
						(call_script, "script_tpe_award_scaled_xp", ":troop_no", tpe_award_dominant_presence_xp),
						(assign, reg21, tpe_award_dominant_presence_renown),
						(str_store_string, s25, "@{s25}^Dominant Presence^Awarded to {s2}^+{reg1} experience^+{reg21} renown^"),
						(try_begin),
							(eq, ":troop_no", "trp_player"),
							(val_add, ":renown_gain", tpe_award_dominant_presence_renown),
						(else_try),
							(call_script, "script_change_troop_renown", ":troop_no", tpe_award_dominant_presence_renown),
						(try_end),
					(try_end),
					(try_begin),
						(troop_slot_ge, tpe_award_data, tpe_legendary_warrior_1, 0),
						(troop_get_slot, ":troop_no", tpe_award_data, tpe_legendary_warrior_1),
						(str_store_troop_name, s2, ":troop_no"),
						(call_script, "script_tpe_award_scaled_xp", ":troop_no", tpe_award_legendary_presence_xp),
						(assign, reg21, tpe_award_legendary_presence_renown),
						(str_store_string, s25, "@{s25}^Legendary Presence^Awarded to {s2}^+{reg1} experience^+{reg21} renown^"),
						(try_begin),
							(eq, ":troop_no", "trp_player"),
							(val_add, ":renown_gain", tpe_award_legendary_presence_renown),
						(else_try),
							(call_script, "script_change_troop_renown", ":troop_no", tpe_award_legendary_presence_renown),
						(try_end),
						(call_script, "script_tpe_increase_award_count", ":troop_no", 1),
					(try_end),
					(try_begin),
						(troop_slot_ge, tpe_award_data, tpe_legendary_warrior_2, 0),
						(troop_get_slot, ":troop_no", tpe_award_data, tpe_legendary_warrior_2),
						(str_store_troop_name, s2, ":troop_no"),
						(call_script, "script_tpe_award_scaled_xp", ":troop_no", tpe_award_legendary_presence_xp),
						(assign, reg21, tpe_award_legendary_presence_renown),
						(str_store_string, s25, "@{s25}^Legendary Presence^Awarded to {s2}^+{reg1} experience^+{reg21} renown^"),
						(try_begin),
							(eq, ":troop_no", "trp_player"),
							(val_add, ":renown_gain", tpe_award_legendary_presence_renown),
						(else_try),
							(call_script, "script_change_troop_renown", ":troop_no", tpe_award_legendary_presence_renown),
						(try_end),
						(call_script, "script_tpe_increase_award_count", ":troop_no", 1),
					(try_end),
					(try_begin),
						(troop_slot_ge, tpe_award_data, tpe_mythical_warrior, 0),
						(troop_get_slot, ":troop_no", tpe_award_data, tpe_mythical_warrior),
						(str_store_troop_name, s2, ":troop_no"),
						(call_script, "script_tpe_award_scaled_xp", ":troop_no", tpe_award_mythical_presence_xp),
						(assign, reg21, tpe_award_mythical_presence_renown),
						(str_store_string, s25, "@{s25}^Mythical Presence^Awarded to {s2}^+{reg1} experience^+{reg21} renown^"),
						(try_begin),
							(eq, ":troop_no", "trp_player"),
							(val_add, ":renown_gain", tpe_award_mythical_presence_renown),
						(else_try),
							(call_script, "script_change_troop_renown", ":troop_no", tpe_award_mythical_presence_renown),
						(try_end),
						(call_script, "script_tpe_increase_award_count", ":troop_no", 1),
					(try_end),
					(try_begin),
						(troop_slot_ge, tpe_award_data, tpe_cautious_approach, 0),
						(troop_get_slot, ":troop_no", tpe_award_data, tpe_cautious_approach),
						(str_store_troop_name, s2, ":troop_no"),
						(assign, reg21, tpe_award_cautious_approach_renown),
						(str_store_string, s25, "@{s25}^Cautious Approach^Awarded to {s2}^{reg21} renown^"),
						(try_begin),
							(eq, ":troop_no", "trp_player"),
							(val_add, ":renown_gain", tpe_award_cautious_approach_renown),
						(else_try),
							(call_script, "script_change_troop_renown", ":troop_no", tpe_award_cautious_approach_renown),
						(try_end),
						(call_script, "script_tpe_increase_award_count", ":troop_no", 1),
					(try_end),
					
					# Final renown awarding to combine them all.  Don't move this.
					(try_begin),
						(neq, ":renown_gain", 0),
						(call_script, "script_change_troop_renown", "trp_player", ":renown_gain"),
					(try_end),
				(try_end),
			
				# Creates the actual list.
				(create_text_overlay, reg1, "@{s25}", tf_center_justify),
				(position_set_x, pos1, 240),
				(position_set_y, pos1, 590),
				(overlay_set_position, reg1, pos1),
			(set_container_overlay, -1),
			
		(else_try),
		###############################################
		# DIAGNOSTIC CODE +
		###############################################
		
			(ge, DEBUG_TPE_general, 1),
			(set_show_messages, 0),
			
			(assign, ":pos_x_1", 55),                  # create slot # display
			(assign, ":pos_x_t1", 95),
			(store_add, ":pos_x_2", ":pos_x_1", 30),   # create TROOP NAME
			(store_add, ":pos_x_t2", ":pos_x_2", 40),
			(store_add, ":pos_x_3", ":pos_x_2", 130),  # create ROUND POINTS
			(store_add, ":pos_x_t3", ":pos_x_3", 40),
			(store_add, ":pos_x_6", ":pos_x_3", 90),   # create TOTAL POINTS
			(store_add, ":pos_x_t6", ":pos_x_6", 40),
			(assign, ":pos_y_titles", 660),
			(assign, ":pos_y_titles2", 645),
			(assign, ":pos_y_data", 620),
			(assign, ":pos_y_step", 20),
			(assign, ":text_size", 500),
			
			# Generate Titles
			# Slot #
			(create_text_overlay, reg1, "@Slot", tf_left_align),
			(position_set_x, pos1, ":pos_x_t1"),
			(position_set_y, pos1, ":pos_y_titles"),
			(overlay_set_position, reg1, pos1),
			(position_set_x, pos1, ":text_size"),
			(position_set_y, pos1, ":text_size"),
			(overlay_set_size, reg1, pos1),
			(create_text_overlay, reg1, "@#", tf_left_align),
			(position_set_x, pos1, ":pos_x_t1"),
			(position_set_y, pos1, ":pos_y_titles2"),
			(overlay_set_position, reg1, pos1),
			(position_set_x, pos1, ":text_size"),
			(position_set_y, pos1, ":text_size"),
			(overlay_set_size, reg1, pos1),
			##### TROOP ID #####
			(position_set_x, pos1, ":text_size"),
			(position_set_y, pos1, ":text_size"),
			(overlay_set_size, reg1, pos1),
			(create_text_overlay, reg1, "@TROOP", tf_left_align),
			(position_set_x, pos1, ":pos_x_t2"),
			(position_set_y, pos1, ":pos_y_titles2"),
			(overlay_set_position, reg1, pos1),
			(position_set_x, pos1, ":text_size"),
			(position_set_y, pos1, ":text_size"),
			(overlay_set_size, reg1, pos1),
			##### ROUND POINTS #####
			(position_set_x, pos1, ":text_size"),
			(position_set_y, pos1, ":text_size"),
			(overlay_set_size, reg1, pos1),
			(create_text_overlay, reg1, "@ROUND POINTS", tf_left_align),
			(position_set_x, pos1, ":pos_x_t3"),
			(position_set_y, pos1, ":pos_y_titles2"),
			(overlay_set_position, reg1, pos1),
			(position_set_x, pos1, ":text_size"),
			(position_set_y, pos1, ":text_size"),
			(overlay_set_size, reg1, pos1),
			##### TOTAL POINTS #####
			(position_set_x, pos1, ":text_size"),
			(position_set_y, pos1, ":text_size"),
			(overlay_set_size, reg1, pos1),
			(create_text_overlay, reg1, "@TOTAL POINTS", tf_left_align),
			(position_set_x, pos1, ":pos_x_t6"),
			(position_set_y, pos1, ":pos_y_titles2"),
			(overlay_set_position, reg1, pos1),
			(position_set_x, pos1, ":text_size"),
			(position_set_y, pos1, ":text_size"),
			(overlay_set_size, reg1, pos1),

			(str_clear, s0),
			(create_text_overlay, reg1, s0, tf_scrollable_style_2),
			(position_set_x, pos1, 40),
			(position_set_y, pos1, 285),
			(overlay_set_position, reg1, pos1),
			(position_set_x, pos1, 420),
			(position_set_y, pos1, 350), 
			(overlay_set_area_size, reg1, pos1),
			(set_container_overlay, reg1),
				(troop_set_slot, "trp_tpe_presobj", tpe_debug_container, reg1),
				
				(assign, ":pos_y", ":pos_y_data"),
				
				(try_for_range, ":slot_no", 0, wp_tpe_max_tournament_participants),
					# create slot # display
					(assign, reg2, ":slot_no"),
					(create_text_overlay, reg1, "@{reg2}", tf_left_align),
					(position_set_x, pos1, ":pos_x_1"),
					(position_set_y, pos1, ":pos_y"),
					(overlay_set_position, reg1, pos1),
					(position_set_x, pos1, ":text_size"),
					(position_set_y, pos1, ":text_size"),
					(overlay_set_size, reg1, pos1),
					
					##### TROOP NAME #####
					(troop_get_slot, ":troop_no", tpe_ranking_array, ":slot_no"),
					(str_store_troop_name, s1, ":troop_no"),
					(create_text_overlay, reg1, "@{s1}", tf_left_align),
					(position_set_x, pos1, ":pos_x_2"),
					(position_set_y, pos1, ":pos_y"),
					(overlay_set_position, reg1, pos1),
					(position_set_x, pos1, ":text_size"),
					(position_set_y, pos1, ":text_size"),
					(overlay_set_size, reg1, pos1),
					
					##### ROUND POINTS #####
					(troop_get_slot, reg2, ":troop_no", slot_troop_tournament_round_points),
					(create_text_overlay, reg1, "@{reg2}", tf_left_align),
					(position_set_x, pos1, ":pos_x_3"),
					(position_set_y, pos1, ":pos_y"),
					(overlay_set_position, reg1, pos1),
					(position_set_x, pos1, ":text_size"),
					(position_set_y, pos1, ":text_size"),
					(overlay_set_size, reg1, pos1),
					
					##### TOTAL POINTS #####
					(troop_get_slot, reg2, ":troop_no", slot_troop_tournament_total_points),
					(create_text_overlay, reg1, "@{reg2}", tf_left_align),
					(position_set_x, pos1, ":pos_x_6"),
					(position_set_y, pos1, ":pos_y"),
					(overlay_set_position, reg1, pos1),
					(position_set_x, pos1, ":text_size"),
					(position_set_y, pos1, ":text_size"),
					(overlay_set_size, reg1, pos1),
					
					(val_sub, ":pos_y", ":pos_y_step"),
				(try_end),
			(set_container_overlay, -1),
			(set_show_messages, 1),
		(try_end),
		###############################################
		# DIAGNOSTIC CODE -
		###############################################
		
		(presentation_set_duration, 999999),
    ]),
    (ti_on_presentation_event_state_change,
    [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
		
		(try_begin),
			(lt, DEBUG_TPE_general, 1),
			(eq, ":object", "$g_presentation_obj_1"), # The EXIT button.
			(presentation_set_duration, 0),
			(jump_to_menu, "mnu_tpe_tournament_withdraw_verify"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_1"), # The DEBUG MODE EXIT.
			(ge, DEBUG_TPE_general, 1),
			(presentation_set_duration, 0),
			(party_set_slot, "$current_town", slot_town_has_tournament, 1), # To allow re-entry for testing.
			(jump_to_menu, "mnu_town"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_4"), # The TOURNAMENT OPTIONS button.
			(presentation_set_duration, 0),
			(troop_set_slot, TPE_OPTIONS, tpe_val_window_mode, 1),
			(jump_to_menu, "mnu_tpe_jump_to_rankings"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_2"), # The CONTINUE button.
			(presentation_set_duration, 0),
			(try_begin),
				(lt, "$g_tournament_cur_tier", wp_tpe_max_tournament_tiers),
				(jump_to_menu, "mnu_tpe_town_tournament"),
			(else_try),
				(troop_set_slot, TPE_OPTIONS, tpe_val_window_mode, 2),
				(jump_to_menu, "mnu_tpe_jump_to_rankings"),
				# (try_begin),
					# (eq, "$g_wp_tpe_active", 1),
					# (jump_to_menu, "mnu_new_town_tournament_won"), # New TPE menu.
				# (else_try),
					# (jump_to_menu, "mnu_town_tournament_won"), # Native menu.
				# (try_end),
			(try_end),
		(else_try),
			(eq, ":object", "$g_presentation_obj_3"), # The RANKING DISPLAY button.
			(try_begin),
				(eq, "$g_wp_tpe_rank_pres_mode", wp_tpe_round_ranking),
				(assign, "$g_wp_tpe_rank_pres_mode", wp_tpe_tournament_ranking),
			(else_try),
				(eq, "$g_wp_tpe_rank_pres_mode", wp_tpe_tournament_ranking),
				(assign, "$g_wp_tpe_rank_pres_mode", wp_tpe_round_ranking),
			(try_end),
			(assign, "$g_presentation_obj_9", 0), # Bugfix to prevent being too many pages into one type of view and switching to another.
			(start_presentation, "prsnt_tpe_ranking_display"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_8"),
			(assign, "$g_presentation_obj_9", ":value"),
			(start_presentation, "prsnt_tpe_ranking_display"),
		
		(else_try), ####### DIFFICULTY SLIDER #######
			(troop_slot_eq, "trp_tpe_presobj", tpe_slider_difficulty, ":object"),
			(troop_set_slot, TPE_OPTIONS, tpe_val_diff_setting, ":value"), # Store the new difficulty setting.
			(overlay_set_val, ":object", ":value"),  # Fix slider position.
			(try_begin),
				(ge, ":value", 1),
				(troop_set_slot, "trp_tpe_presobj", tpe_random_diff_enabled, 0),
			(else_try),
				(troop_set_slot, "trp_tpe_presobj", tpe_random_diff_enabled, 1),
			(try_end),
			
			# Figure out what the new difficulty setting changes
			(call_script, "script_tpe_difficulty_slider_effects", ":value"),     # Reconfigure the teams & payout.
			(troop_get_slot, ":slider_text", "trp_tpe_presobj", tpe_text_diff_setting),
			(overlay_set_text, ":slider_text", "@{s1}"), # Change related text.
			(overlay_set_color, ":slider_text", reg5),
			
			# Update the current team information for this configuration.
			(troop_get_slot, ":team_text", "trp_tpe_presobj", tpe_text_team_number),
			(try_begin),
				(this_or_next|eq, ":value", 0),
				(troop_slot_eq, "trp_tpe_presobj", tpe_random_diff_enabled, 1),
				(str_store_string, s1, "@Random teams and sizes"),
			(else_try),
				(assign, reg2, "$g_tournament_next_num_teams"),
				(assign, reg3, "$g_tournament_next_team_size"),
				(str_store_string, s1, "@{reg2} teams of {reg3} members"),
			(try_end),
			(overlay_set_text, ":team_text", "@{s1}"), # Change related text.
			
			# Update difficulty score.
			(call_script, "script_tpe_get_difficulty_value"),
			
		(try_end),
		
	]),
  ]),

###############################################################
####              TOURNAMENT WINNNER DISPLAY               ####
###############################################################
# Tournament menus are redirected here between rounds to display current ranking and options to continue to
# the next round.
  ("tpe_final_display", 0, mesh_load_window, [
    (ti_on_presentation_load,
    [
		(set_fixed_point_multiplier, 1000),
		# (create_mesh_overlay, reg1, "mesh_face_gen_window"),
        # (position_set_x, pos1, 0),
        # (position_set_y, pos1, 0),
        # (overlay_set_position, reg1, pos1),
		
		
		################################ BEGIN PRESENTATION CODE ################################
		# OBJ #1 - EXIT TOURNAMENT button
		(create_game_button_overlay, "$g_presentation_obj_1", "@Exit Tournament"),
        (position_set_x, pos1, 895), # 430 aligned it to the right side.
        (position_set_y, pos1, 30),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
		
		################################ TOURNAMENT RANKINGS ################################
		
		# Set some initial values to prevent player showing up as a default.
		(assign, ":troop_first", -1),
		(assign, ":troop_second", -1),
		(assign, ":troop_third", -1),
		(assign, ":points_first", -1),
		(assign, ":points_second", -1),
		(assign, ":points_third", -1),
		
		# First place pass
		(try_for_range, ":rank", 0, wp_tpe_max_tournament_participants),
			(troop_get_slot, ":troop_no", tpe_ranking_array, ":rank"),
			(troop_get_slot, ":troop_points", ":troop_no", slot_troop_tournament_total_points),
			(lt, ":points_first", ":troop_points"),
			(assign, ":troop_first", ":troop_no"),
			(assign, ":points_first", ":troop_points"),
		(try_end),
		# Second place pass
		(try_for_range, ":rank", 0, wp_tpe_max_tournament_participants),
			(troop_get_slot, ":troop_no", tpe_ranking_array, ":rank"),
			(troop_get_slot, ":troop_points", ":troop_no", slot_troop_tournament_total_points),
			(neq, ":troop_no", ":troop_first"),
			(lt, ":points_second", ":troop_points"),
			(assign, ":troop_second", ":troop_no"),
			(assign, ":points_second", ":troop_points"),
		(try_end),
		# Third place pass
		(try_for_range, ":rank", 0, wp_tpe_max_tournament_participants),
			(troop_get_slot, ":troop_no", tpe_ranking_array, ":rank"),
			(troop_get_slot, ":troop_points", ":troop_no", slot_troop_tournament_total_points),
			(neq, ":troop_no", ":troop_first"),
			(neq, ":troop_no", ":troop_second"),
			(lt, ":points_third", ":troop_points"),
			(assign, ":troop_third", ":troop_no"),
			(assign, ":points_third", ":troop_points"),
		(try_end),
		# Error trap display
		(try_begin),
			(this_or_next|eq, ":troop_first", -1),
			(this_or_next|eq, ":troop_second", -1),
			(eq, ":troop_third", -1),
			(assign, reg31, ":troop_first"),
			(assign, reg31, ":troop_second"),
			(assign, reg31, ":troop_third"),
			(display_message, "@ERROR (TPE): An invalid winner found.  1st = {reg31}, 2nd = {reg32}, 3rd = {reg33}."),
		(try_end),
		
		################################ PRESET CODE THAT NEEDED TO COME FIRST ################################
		# Determines relation gain issued depending on a player victory.
		(try_begin),
			(eq, ":troop_first", "trp_player"),
			(str_store_party_name, s3, "$current_town"),
			(party_get_slot, ":total_wins", "$current_town", slot_center_tournament_wins),
			(val_add, ":total_wins", 1),
			(party_set_slot, "$current_town", slot_center_tournament_wins, ":total_wins"),
		(try_end),
		
		# Assigning this will...
		# ...prevent or enable the ability to deciate a tournament win to a lady per their conditional block in module_dialogs.  Must be > 3 to dedicate.
		# ...prevent or enable the ability to join a feast if renown is low.  Must have "$g_player_eligible_feast_center_no" & "$current_town" equal to join.
		(try_begin),
			(this_or_next|eq, ":troop_first", "trp_player"),
			(this_or_next|eq, ":troop_second", "trp_player"),
			(eq, ":troop_third", "trp_player"),
			(assign, "$g_player_tournament_placement", 5),
			(assign, "$g_player_eligible_feast_center_no", "$current_town"),
		(else_try),
			(assign, "$g_player_tournament_placement", 1),
			(assign, "$g_player_eligible_feast_center_no", -1),
		(try_end),
		
		################################ CREATE THE PRESENTATION ################################
		(create_text_overlay, reg1, "@TOURNAMENT WINNERS", tf_center_justify|tf_with_outline),
		(overlay_set_color, reg1, wp_blue),
		(position_set_x, pos1, 500),
		(position_set_y, pos1, 635),
		(overlay_set_position, reg1, pos1),
		(position_set_x, pos1, 1500),
		(position_set_y, pos1, 1500),
		(overlay_set_size, reg1, pos1),
		
		(assign, ":potrait_size", 400),
		(assign, ":numeral_size", 2500),
		(assign, ":pos_x_titles", 115),
		(assign, ":pos_x_port", 215),
		(assign, ":pos_x_name_add", 50),
		(assign, ":pos_x_gains", 375),
		(assign, ":pos_x_prizes", 625),
		(assign, ":pos_y_first", 450),
		(assign, ":pos_y_second", 280),
		(assign, ":pos_y_third", 110),
		(assign, ":pos_y_port_name_sub", 25),
		(assign, ":pos_y_title_name_add", 40),
		
		(call_script, "script_tpe_draw_line", 900, 3, 50, 419, wp_black), # - Between 1st & 2nd
		(call_script, "script_tpe_draw_line", 900, 3, 50, 250, wp_black), # - Between 2nd & 3rd

		
		################################ FIRST PLACE ################################
		(create_text_overlay, reg1, "@1st", tf_center_justify|tf_with_outline),
		(overlay_set_color, reg1, 0xDDDDDD),
		(position_set_x, pos1, ":pos_x_titles"),
		(store_add, ":pos_y_name", ":pos_y_first", ":pos_y_title_name_add"),
		(position_set_y, pos1, ":pos_y_name"),
		(overlay_set_position, reg1, pos1),
		(position_set_x, pos1, ":numeral_size"),
		(position_set_y, pos1, ":numeral_size"),
		(overlay_set_size, reg1, pos1),
		
		# OBJ (nil) - Character Portrait
		(call_script, "script_tpe_get_faction_image", ":troop_first"), # returns reg1 as a troop_id
		(create_mesh_overlay_with_tableau_material, reg1, -1, "tableau_troop_note_mesh", reg1),
        (position_set_x, pos2, ":pos_x_port"), # 75 seemed to left adjust to the frame.
        (position_set_y, pos2, ":pos_y_first"),
        (overlay_set_position, reg1, pos2),
        (position_set_x, pos2, ":potrait_size"), #800
        (position_set_y, pos2, ":potrait_size"), #800
        (overlay_set_size, reg1, pos2),
		
		# OBJ (nil) - Character name
		(str_store_troop_name, s1, ":troop_first"),
		(create_text_overlay, reg1, "@{s1}", tf_center_justify),
		(store_add, ":pos_x_name", ":pos_x_port", ":pos_x_name_add"),
		(store_sub, ":pos_y_name", ":pos_y_first", ":pos_y_port_name_sub"),
		(position_set_x, pos1, ":pos_x_name"),
		(position_set_y, pos1, ":pos_y_name"),
		(overlay_set_position, reg1, pos1),
		
		# OBJ (nil) - Rewards label
		(create_text_overlay, reg1, "@Tournament Awards", tf_left_align|tf_with_outline),
		(store_add, ":pos_y_name", ":pos_y_first", 80),
		(store_sub, ":pos_x_name", ":pos_x_gains", 5),
		(position_set_x, pos1, ":pos_x_name"),
		(position_set_y, pos1, ":pos_y_name"),
		(overlay_set_position, reg1, pos1),
		(overlay_set_color, reg1, 0xDDDDDD),
		
		(call_script, "script_tpe_calc_final_rewards", ":troop_first", 1),
		# OBJ (nil) - Cash Gain
		(create_text_overlay, reg1, "@{reg5} denars", tf_left_align),
		(store_add, ":pos_y_name", ":pos_y_first", 54),
		(position_set_x, pos1, ":pos_x_gains"),
		(position_set_y, pos1, ":pos_y_name"),
		(overlay_set_position, reg1, pos1),
		
		# OBJ (nil) - Experience Gain
		(create_text_overlay, reg1, "@{reg6} experience", tf_left_align),
		(store_add, ":pos_y_name", ":pos_y_first", 32),
		(position_set_x, pos1, ":pos_x_gains"),
		(position_set_y, pos1, ":pos_y_name"),
		(overlay_set_position, reg1, pos1),
		
		# OBJ (nil) - Renown Gain
		(create_text_overlay, reg1, "@{reg7} renown", tf_left_align),
		(store_add, ":pos_y_name", ":pos_y_first", 10),
		(position_set_x, pos1, ":pos_x_gains"),
		(position_set_y, pos1, ":pos_y_name"),
		(overlay_set_position, reg1, pos1),
		
		(try_begin),
			(eq, ":troop_first", "trp_player"),
			(unlock_achievement, ACHIEVEMENT_MEDIEVAL_TIMES),
		(try_end),
		
		(try_begin),
			(eq, wp_tpe_mod_opt_award_items_on_win, 1),
			# OBJ (nil) - Prizes label
			(create_text_overlay, reg1, "@Tournament Prizes", tf_left_align|tf_with_outline),
			(store_add, ":pos_y_name", ":pos_y_first", 80),
			(store_sub, ":pos_x_name", ":pos_x_prizes", 5),
			(position_set_x, pos1, ":pos_x_name"),
			(position_set_y, pos1, ":pos_y_name"),
			(overlay_set_position, reg1, pos1),
			(overlay_set_color, reg1, 0xDDDDDD),
			
			(call_script, "script_tpe_award_loot", 100),
			(assign, ":prize", reg1),
			(try_begin),
				(this_or_next|eq, ":troop_first", "trp_player"),
				(is_between, ":troop_first", companions_begin, companions_end),
				(troop_add_item, ":troop_first", ":prize"),
			(try_end),
			(str_store_item_name, s1, ":prize"),
			# OBJ (nil) - Cash Gain
			(create_text_overlay, reg1, "@{s1}", tf_left_align),
			(store_add, ":pos_y_name", ":pos_y_first", 54),
			(position_set_x, pos1, ":pos_x_prizes"),
			(position_set_y, pos1, ":pos_y_name"),
			(overlay_set_position, reg1, pos1),
		(try_end),
		
		################################ SECOND PLACE ################################
		(try_begin),
			(neq, ":troop_second", -1),
			(create_text_overlay, reg1, "@2nd", tf_center_justify|tf_with_outline),
			(overlay_set_color, reg1, 0xDDDDDD),
			(position_set_x, pos1, ":pos_x_titles"),
			(store_add, ":pos_y_name", ":pos_y_second", ":pos_y_title_name_add"),
			(position_set_y, pos1, ":pos_y_name"),
			(overlay_set_position, reg1, pos1),
			(position_set_x, pos1, ":numeral_size"),
			(position_set_y, pos1, ":numeral_size"),
			(overlay_set_size, reg1, pos1),
			
			# OBJ (nil) - Character Portrait
			(call_script, "script_tpe_get_faction_image", ":troop_second"), # returns reg1 as a troop_id
			(create_mesh_overlay_with_tableau_material, reg1, -1, "tableau_troop_note_mesh", reg1),
			(position_set_x, pos2, ":pos_x_port"), # 75 seemed to left adjust to the frame.
			(position_set_y, pos2, ":pos_y_second"),
			(overlay_set_position, reg1, pos2),
			(position_set_x, pos2, ":potrait_size"), #800
			(position_set_y, pos2, ":potrait_size"), #800
			(overlay_set_size, reg1, pos2),
			
			# OBJ (nil) - Character name
			(str_store_troop_name, s1, ":troop_second"),
			(create_text_overlay, reg1, "@{s1}", tf_center_justify),
			(store_add, ":pos_x_name", ":pos_x_port", ":pos_x_name_add"),
			(store_sub, ":pos_y_name", ":pos_y_second", ":pos_y_port_name_sub"),
			(position_set_x, pos1, ":pos_x_name"),
			(position_set_y, pos1, ":pos_y_name"),
			(overlay_set_position, reg1, pos1),
			
			# OBJ (nil) - Rewards label
			(create_text_overlay, reg1, "@Tournament Awards", tf_left_align|tf_with_outline),
			(store_sub, ":pos_x_name", ":pos_x_gains", 5),
			(store_add, ":pos_y_name", ":pos_y_second", 80),
			(position_set_x, pos1, ":pos_x_name"),
			(position_set_y, pos1, ":pos_y_name"),
			(overlay_set_position, reg1, pos1),
			(overlay_set_color, reg1, 0xDDDDDD),
			
			(call_script, "script_tpe_calc_final_rewards", ":troop_second", 2),
			# OBJ (nil) - Cash Gain
			(create_text_overlay, reg1, "@{reg5} denars", tf_left_align),
			(store_add, ":pos_y_name", ":pos_y_second", 54),
			(position_set_x, pos1, ":pos_x_gains"),
			(position_set_y, pos1, ":pos_y_name"),
			(overlay_set_position, reg1, pos1),
			
			# OBJ (nil) - Experience Gain
			(create_text_overlay, reg1, "@{reg6} experience", tf_left_align),
			(store_add, ":pos_y_name", ":pos_y_second", 32),
			(position_set_x, pos1, ":pos_x_gains"),
			(position_set_y, pos1, ":pos_y_name"),
			(overlay_set_position, reg1, pos1),
			
			# OBJ (nil) - Renown Gain
			(create_text_overlay, reg1, "@{reg7} renown", tf_left_align),
			(store_add, ":pos_y_name", ":pos_y_second", 10),
			(position_set_x, pos1, ":pos_x_gains"),
			(position_set_y, pos1, ":pos_y_name"),
			(overlay_set_position, reg1, pos1),
			
			(try_begin),
				(eq, wp_tpe_mod_opt_award_items_on_win, 1),
				# OBJ (nil) - Prizes label
				(create_text_overlay, reg1, "@Tournament Prizes", tf_left_align|tf_with_outline),
				(store_add, ":pos_y_name", ":pos_y_second", 80),
				(store_sub, ":pos_x_name", ":pos_x_prizes", 5),
				(position_set_x, pos1, ":pos_x_name"),
				(position_set_y, pos1, ":pos_y_name"),
				(overlay_set_position, reg1, pos1),
				(overlay_set_color, reg1, 0xDDDDDD),
				
				(call_script, "script_tpe_award_loot", 70),
				(assign, ":prize", reg1),
				(try_begin),
					(this_or_next|eq, ":troop_second", "trp_player"),
					(is_between, ":troop_second", companions_begin, companions_end),
					(troop_add_item, ":troop_second", ":prize"),
				(try_end),
				(str_store_item_name, s1, ":prize"),
				# OBJ (nil) - Cash Gain
				(create_text_overlay, reg1, "@{s1}", tf_left_align),
				(store_add, ":pos_y_name", ":pos_y_second", 54),
				(position_set_x, pos1, ":pos_x_prizes"),
				(position_set_y, pos1, ":pos_y_name"),
				(overlay_set_position, reg1, pos1),
			(try_end),
		(try_end),
		
		################################ THIRD PLACE ################################
		(try_begin),
			(neq, ":points_third", -1),
			(create_text_overlay, reg1, "@3rd", tf_center_justify|tf_with_outline),
			(overlay_set_color, reg1, 0xDDDDDD),
			(position_set_x, pos1, ":pos_x_titles"),
			(store_add, ":pos_y_name", ":pos_y_third", ":pos_y_title_name_add"),
			(position_set_y, pos1, ":pos_y_name"),
			(overlay_set_position, reg1, pos1),
			(position_set_x, pos1, ":numeral_size"),
			(position_set_y, pos1, ":numeral_size"),
			(overlay_set_size, reg1, pos1),
			
			# OBJ (nil) - Character Portrait
			(call_script, "script_tpe_get_faction_image", ":troop_third"), # returns reg1 as a troop_id
			(create_mesh_overlay_with_tableau_material, reg1, -1, "tableau_troop_note_mesh", reg1),
			(position_set_x, pos2, ":pos_x_port"), # 75 seemed to left adjust to the frame.
			(position_set_y, pos2, ":pos_y_third"),
			(overlay_set_position, reg1, pos2),
			(position_set_x, pos2, ":potrait_size"), #800
			(position_set_y, pos2, ":potrait_size"), #800
			(overlay_set_size, reg1, pos2),
			
			# OBJ (nil) - Character name
			(str_store_troop_name, s1, ":troop_third"),
			(create_text_overlay, reg1, "@{s1}", tf_center_justify),
			(store_add, ":pos_x_name", ":pos_x_port", ":pos_x_name_add"),
			(store_sub, ":pos_y_name", ":pos_y_third", ":pos_y_port_name_sub"),
			(position_set_x, pos1, ":pos_x_name"),
			(position_set_y, pos1, ":pos_y_name"),
			(overlay_set_position, reg1, pos1),
			
			# OBJ (nil) - Rewards label
			(create_text_overlay, reg1, "@Tournament Awards", tf_left_align|tf_with_outline),
			(store_sub, ":pos_x_name", ":pos_x_gains", 5),
			(store_add, ":pos_y_name", ":pos_y_third", 80),
			(position_set_x, pos1, ":pos_x_name"),
			(position_set_y, pos1, ":pos_y_name"),
			(overlay_set_position, reg1, pos1),
			(overlay_set_color, reg1, 0xDDDDDD),
			
			(call_script, "script_tpe_calc_final_rewards", ":troop_third", 3),
			# OBJ (nil) - Cash Gain
			(create_text_overlay, reg1, "@{reg5} denars", tf_left_align),
			(store_add, ":pos_y_name", ":pos_y_third", 54),
			(position_set_x, pos1, ":pos_x_gains"),
			(position_set_y, pos1, ":pos_y_name"),
			(overlay_set_position, reg1, pos1),
			
			# OBJ (nil) - Experience Gain
			(create_text_overlay, reg1, "@{reg6} experience", tf_left_align),
			(store_add, ":pos_y_name", ":pos_y_third", 32),
			(position_set_x, pos1, ":pos_x_gains"),
			(position_set_y, pos1, ":pos_y_name"),
			(overlay_set_position, reg1, pos1),
			
			# OBJ (nil) - Renown Gain
			(create_text_overlay, reg1, "@{reg7} renown", tf_left_align),
			(store_add, ":pos_y_name", ":pos_y_third", 10),
			(position_set_x, pos1, ":pos_x_gains"),
			(position_set_y, pos1, ":pos_y_name"),
			(overlay_set_position, reg1, pos1),
			
			(try_begin),
				(eq, wp_tpe_mod_opt_award_items_on_win, 1),
				# OBJ (nil) - Prizes label
				(create_text_overlay, reg1, "@Tournament Prizes", tf_left_align|tf_with_outline),
				(store_add, ":pos_y_name", ":pos_y_third", 80),
				(store_sub, ":pos_x_name", ":pos_x_prizes", 5),
				(position_set_x, pos1, ":pos_x_name"),
				(position_set_y, pos1, ":pos_y_name"),
				(overlay_set_position, reg1, pos1),
				(overlay_set_color, reg1, 0xDDDDDD),
				
				(call_script, "script_tpe_award_loot", 40),
				(assign, ":prize", reg1),
				(try_begin),
					(this_or_next|eq, ":troop_third", "trp_player"),
					(is_between, ":troop_third", companions_begin, companions_end),
					(troop_add_item, ":troop_third", ":prize"),
				(try_end),
				(str_store_item_name, s1, ":prize"),
				# OBJ (nil) - Cash Gain
				(create_text_overlay, reg1, "@{s1}", tf_left_align),
				(store_add, ":pos_y_name", ":pos_y_third", 54),
				(position_set_x, pos1, ":pos_x_prizes"),
				(position_set_y, pos1, ":pos_y_name"),
				(overlay_set_position, reg1, pos1),
			(try_end),
		(try_end),
		
		################################ AWARD NOBILITY REACTIONS ################################
		(try_begin),
			(eq, wp_tpe_mod_opt_nobilty_reactions, 1),
			# Raises relation with Lords that are (present) AND (friendly).  Enemies lose relation.
			(call_script, "script_tpe_rep_gain_lords"),
			
			# Raises relation with Ladies that are (present).  More so if in courtship.
			(call_script, "script_tpe_rep_gain_ladies"),
		(try_end),
		(str_clear, s8),
		
		###############
		
		(presentation_set_duration, 999999),
    ]),
    (ti_on_presentation_event_state_change,
    [
        (store_trigger_param_1, ":object"),
        #(store_trigger_param_2, ":value"),
		
		(try_begin),
			(eq, ":object", "$g_presentation_obj_1"), # The EXIT button.
			(presentation_set_duration, 0),
			(jump_to_menu, "mnu_town"),
		(try_end),
		
	]),
  ]),
  
###########################################################################################################################
#####                                                IN-COMBAT DISPLAY                                                #####
###########################################################################################################################

# Creates an in-combat display showing each team's color, remaining troops and accumulated points.
  ("tpe_team_display",prsntf_read_only,0,[
      (ti_on_presentation_load,
       [
        (set_fixed_point_multiplier, 1000),
        
		(assign, "$gpu_storage", "trp_tpe_presobj"),
		(assign, "$gpu_data",    "trp_tpe_presobj"),
		
		(try_begin),
			# Assign margin settings
			(assign,    ":pos_x_col_1", 15),                  # Left edge of team labels
			(store_add, ":pos_x_col_2", ":pos_x_col_1", 185), # Right edge of points
			(store_add, ":pos_x_col_3", ":pos_x_col_2",   0), # Left edge of health bars
			
			(assign,    ":row_space", 30),
			(assign,    ":pos_y_row_1", 720),                             # First team
			(store_sub, ":pos_y_row_2", ":pos_y_row_1", ":row_space"), # Second team
			(store_sub, ":pos_y_row_3", ":pos_y_row_2", ":row_space"), # Third team
			(store_sub, ":pos_y_row_4", ":pos_y_row_3", ":row_space"), # Fourth team
			(store_sub, ":pos_y_row_5", ":pos_y_row_4", ":row_space"), # Space holder
			(store_sub, ":pos_y_row_6", ":pos_y_row_5", ":row_space"), # Timer
			(store_sub, ":pos_y_row_7", ":pos_y_row_6", 35), # Stalemate Timer
			
			# Determine how many people are on each team
			(assign, "$g_wp_tpe_team_0_members", 0),
			(assign, "$g_wp_tpe_team_1_members", 0),
			(assign, "$g_wp_tpe_team_2_members", 0),
			(assign, "$g_wp_tpe_team_3_members", 0),
			(try_for_agents, ":agent_no"),
				# Is the agent alive?
				(agent_is_alive, ":agent_no"),
				# What team is he on?
				(agent_get_team  , ":team_no", ":agent_no"),
				(try_begin),
					(eq, ":team_no", 0),
					(val_add, "$g_wp_tpe_team_0_members", 1),
				(else_try),
					(eq, ":team_no", 1),
					(val_add, "$g_wp_tpe_team_1_members", 1),
				(else_try),
					(eq, ":team_no", 2),
					(val_add, "$g_wp_tpe_team_2_members", 1),
				(else_try),
					(eq, ":team_no", 3),
					(val_add, "$g_wp_tpe_team_3_members", 1),
				(try_end),
			(try_end),
		
			##### RED TEAM #####
			# Team label
			(call_script, "script_gpu_create_text_label", "str_tpe_red_team", ":pos_x_col_1", ":pos_y_row_1", tpe_obj_team_0_label, gpu_left_with_outline),
			(overlay_set_color, reg1, wp_red),
			# Current points display
			(troop_get_slot, reg5, "trp_tpe_presobj", tpe_icd_team_0_points),
			(call_script, "script_gpu_create_text_label", "str_tpe_reg5", ":pos_x_col_2", ":pos_y_row_1", tpe_obj_team_0_points, gpu_right_with_outline),
			(overlay_set_color, reg1, wp_white),
			# Team health bar
			(store_mul, ":lifebar_length", "$g_wp_tpe_team_0_members", tpe_lifebar_pip_size),
			(store_add, ":lifebar_outer", ":lifebar_length", 4),
			(call_script, "script_gpu_draw_line", ":lifebar_outer", tpe_lifebar_outer_width, ":pos_x_col_3", ":pos_y_row_1", wp_black),
			(troop_set_slot, "trp_tpe_presobj", tpe_obj_team_0_outerbar, reg1),
			(store_add, ":x_inner_bar", ":pos_x_col_3", 2),
			(store_add, ":y_inner_bar", ":pos_y_row_1", 2),
			(call_script, "script_gpu_draw_line", ":lifebar_length", tpe_lifebar_pip_width, ":x_inner_bar", ":y_inner_bar", wp_red),
			(troop_set_slot, "trp_tpe_presobj", tpe_obj_team_0_lifebar, reg1),
			
			##### BLUE TEAM #####
			# Team label
			(call_script, "script_gpu_create_text_label", "str_tpe_blue_team", ":pos_x_col_1", ":pos_y_row_2", tpe_obj_team_1_label, gpu_left_with_outline),
			(overlay_set_color, reg1, wp_blue),
			# Current points display
			(troop_get_slot, reg5, "trp_tpe_presobj", tpe_icd_team_1_points),
			(call_script, "script_gpu_create_text_label", "str_tpe_reg5", ":pos_x_col_2", ":pos_y_row_2", tpe_obj_team_1_points, gpu_right_with_outline),
			(overlay_set_color, reg1, wp_white),
			# Team health bar
			(store_mul, ":lifebar_length", "$g_wp_tpe_team_1_members", tpe_lifebar_pip_size),
			(store_add, ":lifebar_outer", ":lifebar_length", 4),
			(call_script, "script_gpu_draw_line", ":lifebar_outer", tpe_lifebar_outer_width, ":pos_x_col_3", ":pos_y_row_2", wp_black),
			(troop_set_slot, "trp_tpe_presobj", tpe_obj_team_1_outerbar, reg1),
			(store_add, ":x_inner_bar", ":pos_x_col_3", 2),
			(store_add, ":y_inner_bar", ":pos_y_row_2", 2),
			(call_script, "script_gpu_draw_line", ":lifebar_length", tpe_lifebar_pip_width, ":x_inner_bar", ":y_inner_bar", wp_blue),
			(troop_set_slot, "trp_tpe_presobj", tpe_obj_team_1_lifebar, reg1),
			
			(try_begin),
				(ge, "$g_tournament_next_num_teams", 3),
				##### GREEN TEAM #####
				# Team label
				(call_script, "script_gpu_create_text_label", "str_tpe_green_team", ":pos_x_col_1", ":pos_y_row_3", tpe_obj_team_2_label, gpu_left_with_outline),
				(overlay_set_color, reg1, wp_green),
				# Current points display
				(troop_get_slot, reg5, "trp_tpe_presobj", tpe_icd_team_2_points),
				(call_script, "script_gpu_create_text_label", "str_tpe_reg5", ":pos_x_col_2", ":pos_y_row_3", tpe_obj_team_2_points, gpu_right_with_outline),
				(overlay_set_color, reg1, wp_white),
				# Team health bar
				(store_mul, ":lifebar_length", "$g_wp_tpe_team_2_members", tpe_lifebar_pip_size),
				(store_add, ":lifebar_outer", ":lifebar_length", 4),
				(call_script, "script_gpu_draw_line", ":lifebar_outer", tpe_lifebar_outer_width, ":pos_x_col_3", ":pos_y_row_3", wp_black),
				(troop_set_slot, "trp_tpe_presobj", tpe_obj_team_2_outerbar, reg1),
				(store_add, ":x_inner_bar", ":pos_x_col_3", 2),
				(store_add, ":y_inner_bar", ":pos_y_row_3", 2),
				(call_script, "script_gpu_draw_line", ":lifebar_length", tpe_lifebar_pip_width, ":x_inner_bar", ":y_inner_bar", wp_green),
				(troop_set_slot, "trp_tpe_presobj", tpe_obj_team_2_lifebar, reg1),
			(try_end),
			
			(try_begin),
				(ge, "$g_tournament_next_num_teams", 4),
				##### YELLOW TEAM #####
				# Team label
				(call_script, "script_gpu_create_text_label", "str_tpe_yellow_team", ":pos_x_col_1", ":pos_y_row_4", tpe_obj_team_3_label, gpu_left_with_outline),
				(overlay_set_color, reg1, wp_yellow),
				# Current points display
				(troop_get_slot, reg5, "trp_tpe_presobj", tpe_icd_team_3_points),
				(call_script, "script_gpu_create_text_label", "str_tpe_reg5", ":pos_x_col_2", ":pos_y_row_4", tpe_obj_team_3_points, gpu_right_with_outline),
				(overlay_set_color, reg1, wp_white),
				# Team health bar
				(store_mul, ":lifebar_length", "$g_wp_tpe_team_3_members", tpe_lifebar_pip_size),
				(store_add, ":lifebar_outer", ":lifebar_length", 4),
				(call_script, "script_gpu_draw_line", ":lifebar_outer", tpe_lifebar_outer_width, ":pos_x_col_3", ":pos_y_row_4", wp_black),
				(troop_set_slot, "trp_tpe_presobj", tpe_obj_team_3_outerbar, reg1),
				(store_add, ":x_inner_bar", ":pos_x_col_3", 2),
				(store_add, ":y_inner_bar", ":pos_y_row_4", 2),
				(call_script, "script_gpu_draw_line", ":lifebar_length", tpe_lifebar_pip_width, ":x_inner_bar", ":y_inner_bar", wp_yellow),
				(troop_set_slot, "trp_tpe_presobj", tpe_obj_team_3_lifebar, reg1),
			(try_end),
			
			# Match Timer
			(call_script, "script_gpu_create_text_label", "str_tpe_game_timer", ":pos_x_col_1", ":pos_y_row_6", tpe_obj_match_timer, gpu_left_with_outline),
			(overlay_set_color, reg1, wp_white),
			
			# Stalemate Timer
			(str_clear, s21),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_col_1", ":pos_y_row_7", tpe_icd_stalemate_timer, gpu_left_with_outline),
			(overlay_set_color, reg1, wp_white),
			
			##### DEVELOPE ICD RANKING DISPLAY #####
			# Setup margin definitions
			(assign,    ":pos_x_icd_col_1", 595),                     # Column for point tally.
			(store_add, ":pos_x_icd_col_2", ":pos_x_icd_col_1",  30), # Column for troop names.
			(store_add, ":pos_x_icd_col_3", ":pos_x_icd_col_2", 220), # Column for agent team.
			
			(assign, ":adjust", 11),
			(store_sub, ":pos_y_row_1a", ":pos_y_row_1", 0),
			(store_sub, ":pos_y_row_2a", ":pos_y_row_2", ":adjust"),
			(store_sub, ":pos_y_row_3a", ":pos_y_row_3", ":adjust"),
			(store_sub, ":pos_y_row_4a", ":pos_y_row_4", ":adjust"),
			(store_sub, ":pos_y_row_5a", ":pos_y_row_5", ":adjust"),
			(store_sub, ":pos_y_row_6a", ":pos_y_row_6", ":adjust"),
			
			# (call_script, "script_gpu_draw_line", 950, 1, 25, 714, wp_black), # Guide line
			# (call_script, "script_gpu_draw_line", 950, 1, 25, 684, wp_black), # Guide line
			# (call_script, "script_gpu_draw_line", 950, 1, 25, 654, wp_black), # Guide line
			
			# Point labels
			(str_clear, s21),
			(call_script, "script_gpu_create_text_label", "str_tpe_icd_label_points", ":pos_x_icd_col_1", ":pos_y_row_1a", tpe_icd_label_points,  gpu_center_with_outline), # Label
			(overlay_set_color, reg1, wp_white),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_1", ":pos_y_row_2a", tpe_icd_rank_1_points, gpu_center_with_outline),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_1", ":pos_y_row_3a", tpe_icd_rank_2_points, gpu_center_with_outline),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_1", ":pos_y_row_4a", tpe_icd_rank_3_points, gpu_center_with_outline),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_1", ":pos_y_row_5a", tpe_icd_rank_4_points, gpu_center_with_outline),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_1", ":pos_y_row_6a", tpe_icd_rank_5_points, gpu_center_with_outline),
			
			# Troop name labels
			(call_script, "script_gpu_create_text_label", "str_tpe_icd_label_troop", ":pos_x_icd_col_2", ":pos_y_row_1a", tpe_icd_label_troop,  gpu_left_with_outline), # Label
			(overlay_set_color, reg1, wp_white),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_2", ":pos_y_row_2a", tpe_icd_rank_1_troop, gpu_left_with_outline),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_2", ":pos_y_row_3a", tpe_icd_rank_2_troop, gpu_left_with_outline),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_2", ":pos_y_row_4a", tpe_icd_rank_3_troop, gpu_left_with_outline),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_2", ":pos_y_row_5a", tpe_icd_rank_4_troop, gpu_left_with_outline),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_2", ":pos_y_row_6a", tpe_icd_rank_5_troop, gpu_left_with_outline),
			
			# Team labels
			(call_script, "script_gpu_create_text_label", "str_tpe_icd_label_team", ":pos_x_icd_col_3", ":pos_y_row_1a", tpe_icd_label_team,  gpu_left_with_outline), # Label
			(overlay_set_color, reg1, wp_white),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_3", ":pos_y_row_2a", tpe_icd_rank_1_team, gpu_left_with_outline),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_3", ":pos_y_row_3a", tpe_icd_rank_2_team, gpu_left_with_outline),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_3", ":pos_y_row_4a", tpe_icd_rank_3_team, gpu_left_with_outline),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_3", ":pos_y_row_5a", tpe_icd_rank_4_team, gpu_left_with_outline),
			(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":pos_x_icd_col_3", ":pos_y_row_6a", tpe_icd_rank_5_team, gpu_left_with_outline),
			
			#hp bar
			(try_begin),
				(eq, MOD_CUSTOM_COMMANDER_INSTALLED, 1), # Dependency (Custom Commander)
				# (troop_slot_eq, TPE_OPTIONS, tpe_val_show_health, 1), # Default display option.
				# (try_for_agents, ":agent_no"),
					# (agent_set_slot, ":agent_no", slot_agent_hp_bar_overlay_id, 0),
					# (agent_set_slot, ":agent_no", slot_agent_hp_bar_bg_overlay_id, 0),
				# (try_end),
				# (call_script, "script_update_agent_hp_bar"),
			(try_end),
			
			(assign, "$g_wp_tpe_icd_activated", 1),
		(try_end),
		
		(presentation_set_duration, 999999),
       ]),
       
     ]),
	 
###############################################################
####               TOURNAMENT DESIGN PANEL                 ####
###############################################################
# This preference panel will set what kinds of equipment the player wishes allowed in each city's specific tournaments.
  ("tpe_design_settings", 0, mesh_load_window, [
    (ti_on_presentation_load,
    [
		(set_fixed_point_multiplier, 1000),
		(assign, "$gpu_storage", "trp_tpe_presobj"),
		(assign, "$gpu_data",    "trp_tpe_settings"),
		(call_script, "script_tdp_define_weapons"),  # Initialization script for tpe_weapons array.
		
		#### INITIALIZE ARENA SCENES ####
		# This was done to prevent Floris 2.52 from breaking save games.
		(try_for_range, ":town_no", towns_begin, towns_end),
			(store_sub, ":offset", ":town_no", towns_begin),
			(store_add, ":cur_object_no", "scn_town_1_arena_alternate", ":offset"),
			(party_set_slot,":town_no", slot_town_arena_alternate, ":cur_object_no"),
		(try_end),
		#### END INITIALIZATION OF SCENES ####
		
		# Background Mesh
		(create_mesh_overlay, reg1, "mesh_tournament_design_panel"),
        (position_set_x, pos1, 0),
        (position_set_y, pos1, 0),
        (overlay_set_position, reg1, pos1),
		
		# Button Definitions
		(call_script, "script_gpu_create_game_button", "str_tdp_label_done", 895, 15, tdp_obj_button_done),
		(call_script, "script_gpu_create_game_button", "str_tdp_label_enable_all", 730, 15, tdp_obj_button_enable_all),
		(call_script, "script_gpu_create_game_button", "str_tdp_label_native_settings", 565, 15, tdp_obj_button_native_settings),
		
		
		# Margins
		(assign, ":x_col_label_titles",     30), # Left aligned.
		(assign, ":x_col_slider_chance",   240), # Centered.
		(assign, ":x_col_value_chance",    465), # Right aligned.
		(assign, ":x_col_menu_appearance", 620), # Centered.
		(assign, ":x_col_button_disable",  735), # Centered.
		# (assign, ":x_col_button_centers",  900), # Centered.
		(assign, ":y_row_headers",         600),
		(assign, ":y_row_onehand",         560), # 1
		(assign, ":y_row_twohand",         520), # 2
		(assign, ":y_row_polearm",         480), # 3
		# dividing line @ 450
		(assign, ":y_row_lance",           420), # 4
		(assign, ":y_row_archery",         380), # 5
		(assign, ":y_row_crossbow",        340), # 6
		(assign, ":y_row_throwing",        300), # 7
		# dividing line @ 270
		(assign, ":y_row_mount",           240), # 8
		# dividing line @ 210
		(assign, ":y_row_outfit",          180), # 9 
		(assign, ":button_offset",          13),
		(store_sub, ":y_row_lance_buttons", ":y_row_lance", ":button_offset"),
		(store_sub, ":y_row_archery_buttons", ":y_row_archery", ":button_offset"),
		(store_sub, ":y_row_onehand_buttons", ":y_row_onehand", ":button_offset"),
		(store_sub, ":y_row_twohand_buttons", ":y_row_twohand", ":button_offset"),
		(store_sub, ":y_row_crossbow_buttons", ":y_row_crossbow", ":button_offset"),
		(store_sub, ":y_row_throwing_buttons", ":y_row_throwing", ":button_offset"),
		(store_sub, ":y_row_polearm_buttons", ":y_row_polearm", ":button_offset"),
		(store_sub, ":y_row_mount_buttons", ":y_row_mount", ":button_offset"),
		(store_sub, ":y_row_outfit_buttons", ":y_row_outfit", ":button_offset"),
		
		# Create header display
		(str_store_party_name, s21, "$tournament_town"),
		(str_store_string, s21, "@City of {s21}"),
		(call_script, "script_gpu_create_text_label", "str_tpe_s21", 25, 680, 0, gpu_left_with_outline),
		(overlay_set_color, reg1, gpu_white),
		(call_script, "script_gpu_resize_object", 0, 150),
		# (party_get_slot, ":troop_lord", "$tournament_town", slot_town_lord),
		# (store_troop_faction, ":faction_no", ":troop_lord"),
		(call_script, "script_tpe_store_town_faction_to_reg0", "$tournament_town"),
		(str_store_faction_name, s21, reg0),
		(call_script, "script_gpu_create_text_label", "str_tpe_s21", ":x_col_label_titles", 650, 0, gpu_left),
		# Dividing Lines
		(call_script, "script_gpu_draw_line", 770, 2, 15, 630, gpu_gray), # horizontal line underneath city & faction names.
		(call_script, "script_gpu_draw_line", 2, 650, 785, 75, gpu_gray), # vertical line separating selectable cities from current city settings.
		(call_script, "script_gpu_draw_line", 770, 1, 15, 450, gpu_gray), # horizontal line between group 1 & 2.
		(call_script, "script_gpu_draw_line", 770, 1, 15, 270, gpu_gray), # horizontal line between group 2 & 3.
		(call_script, "script_gpu_draw_line", 770, 1, 15, 210, gpu_gray), # horizontal line between group 3 & 4.
		# Minor Text Headings
		(call_script, "script_gpu_create_text_label", "str_tdp_label_center_list", 855, 680, 0, gpu_center_with_outline),
		(overlay_set_color, reg1, gpu_white),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_chance_header", 325, ":y_row_headers", 0, gpu_center),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_appearance", 585,":y_row_headers", 0, gpu_center),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_player_setting", 730, ":y_row_headers", 0, gpu_center),
		
		
		# Labels - Column 1
		(call_script, "script_gpu_create_text_label", "str_tdp_label_lance",    ":x_col_label_titles", ":y_row_lance",    tdp_obj_label_lance,    gpu_left),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_archery",  ":x_col_label_titles", ":y_row_archery",  tdp_obj_label_archery,  gpu_left),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_onehand",  ":x_col_label_titles", ":y_row_onehand",  tdp_obj_label_onehand,  gpu_left),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_twohand",  ":x_col_label_titles", ":y_row_twohand",  tdp_obj_label_twohand,  gpu_left),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_crossbow", ":x_col_label_titles", ":y_row_crossbow", tdp_obj_label_crossbow, gpu_left),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_throwing", ":x_col_label_titles", ":y_row_throwing", tdp_obj_label_throwing, gpu_left),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_polearm",  ":x_col_label_titles", ":y_row_polearm",  tdp_obj_label_polearm,  gpu_left),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_horse",    ":x_col_label_titles", ":y_row_mount",    tdp_obj_label_horse,    gpu_left),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_outfit",   ":x_col_label_titles", ":y_row_outfit",   tdp_obj_label_outfit,   gpu_left),
		(assign, ":obj_size", 70),
		(call_script, "script_gpu_resize_object", tdp_obj_label_lance,    ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_archery,  ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_onehand,  ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_twohand,  ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_crossbow, ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_throwing, ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_polearm,  ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_horse,    ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_outfit,   ":obj_size"),
		
		# Chance of Loading Sliders - Column 2
		(call_script, "script_tdp_create_slider", ":x_col_slider_chance", ":y_row_lance_buttons",    tdp_obj_slider_lance,    tdp_val_setting_lance),
		(call_script, "script_tdp_create_slider", ":x_col_slider_chance", ":y_row_archery_buttons",  tdp_obj_slider_archery,  tdp_val_setting_archery),
		(call_script, "script_tdp_create_slider", ":x_col_slider_chance", ":y_row_onehand_buttons",  tdp_obj_slider_onehand,  tdp_val_setting_onehand),
		(call_script, "script_tdp_create_slider", ":x_col_slider_chance", ":y_row_twohand_buttons",  tdp_obj_slider_twohand,  tdp_val_setting_twohand),
		(call_script, "script_tdp_create_slider", ":x_col_slider_chance", ":y_row_crossbow_buttons", tdp_obj_slider_crossbow, tdp_val_setting_crossbow),
		(call_script, "script_tdp_create_slider", ":x_col_slider_chance", ":y_row_throwing_buttons", tdp_obj_slider_throwing, tdp_val_setting_throwing),
		(call_script, "script_tdp_create_slider", ":x_col_slider_chance", ":y_row_polearm_buttons",  tdp_obj_slider_polearm,  tdp_val_setting_polearm),
		(call_script, "script_tdp_create_slider", ":x_col_slider_chance", ":y_row_mount_buttons",    tdp_obj_slider_horse,    tdp_val_setting_horse),
		#(call_script, "script_tdp_create_slider", ":x_col_slider_chance", ":y_row_outfit_buttons",   tdp_obj_slider_outfit,   tdp_val_setting_outfit),
		(assign, ":obj_size", 70),
		(call_script, "script_gpu_resize_object", tdp_obj_slider_lance,    ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_slider_archery,  ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_slider_onehand,  ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_slider_twohand,  ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_slider_crossbow, ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_slider_throwing, ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_slider_polearm,  ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_slider_horse,    ":obj_size"),
		#(call_script, "script_gpu_resize_object", tdp_obj_slider_outfit,   ":obj_size"),
		
		### Scene Choice ###
		(position_set_x, pos1, 360),
        (position_set_y, pos1, ":y_row_outfit_buttons"),
        (create_combo_button_overlay, reg1),
		(troop_set_slot, tdp_objects, tdp_obj_menu_scene, reg1),
        (overlay_set_position, reg1, pos1),
		(overlay_add_item, reg1, "@Native Arena"),
		(try_begin),
			(eq, MOD_ARENA_OVERHAUL_INSTALLED, 1),
			(overlay_add_item, reg1, "@Adorno's Overhaul Arena"),
		(try_end),
		(party_get_slot, ":option_setting", "$tournament_town", slot_town_arena_option),
		(overlay_set_val, reg1, ":option_setting"),
		(call_script, "script_gpu_resize_object", tdp_obj_menu_scene, 70),
		
		# Load Setting Value - Column 3
		(store_sub, ":city_offset", "$tournament_town", towns_begin),
		(store_mul, ":city_settings", ":city_offset", 10),
		# Lances
		(store_add, ":slot_offset", ":city_settings", tdp_val_setting_lance),
		(troop_get_slot, reg21, tpe_settings, ":slot_offset"),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_value_chance", ":y_row_lance",    tdp_obj_label_chance_of_lance,    gpu_right),
		# Archery
		(store_add, ":slot_offset", ":city_settings", tdp_val_setting_archery),
		(troop_get_slot, reg21, tpe_settings, ":slot_offset"),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_value_chance", ":y_row_archery",  tdp_obj_label_chance_of_archery,  gpu_right),
		# One Hand
		(store_add, ":slot_offset", ":city_settings", tdp_val_setting_onehand),
		(troop_get_slot, reg21, tpe_settings, ":slot_offset"),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_value_chance", ":y_row_onehand",  tdp_obj_label_chance_of_onehand,  gpu_right),
		# Two Hand
		(store_add, ":slot_offset", ":city_settings", tdp_val_setting_twohand),
		(troop_get_slot, reg21, tpe_settings, ":slot_offset"),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_value_chance", ":y_row_twohand",  tdp_obj_label_chance_of_twohand,  gpu_right),
		# Crossbow
		(store_add, ":slot_offset", ":city_settings", tdp_val_setting_crossbow),
		(troop_get_slot, reg21, tpe_settings, ":slot_offset"),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_value_chance", ":y_row_crossbow", tdp_obj_label_chance_of_crossbow, gpu_right),
		# Throwing
		(store_add, ":slot_offset", ":city_settings", tdp_val_setting_throwing),
		(troop_get_slot, reg21, tpe_settings, ":slot_offset"),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_value_chance", ":y_row_throwing", tdp_obj_label_chance_of_throwing, gpu_right),
		# Polearm
		(store_add, ":slot_offset", ":city_settings", tdp_val_setting_polearm),
		(troop_get_slot, reg21, tpe_settings, ":slot_offset"),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_value_chance", ":y_row_polearm",  tdp_obj_label_chance_of_polearm,  gpu_right),
		# Horse
		(store_add, ":slot_offset", ":city_settings", tdp_val_setting_horse),
		(troop_get_slot, reg21, tpe_settings, ":slot_offset"),
		(assign, ":value", reg21),
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_value_chance", ":y_row_mount",    tdp_obj_label_chance_of_horse,    gpu_right),
		(try_begin),
			# Anti-Exploit - Establish minimum mount chance of 50% if player has them selected.
			(troop_slot_eq, "trp_player", slot_troop_tournament_horse, 1),
			(is_between, ":value", 1, 50), # Allow player to set horse chance to 0.
			(troop_set_slot, tpe_settings, ":slot_offset", 50),
			(assign, reg21, 50),
			(str_store_string, s21, "@{reg21}%"),
			(troop_get_slot, ":obj_label", tdp_objects, tdp_obj_label_chance_of_horse),
			(overlay_set_text, ":obj_label", s21),
			#(overlay_set_color, ":obj_label", gpu_red),
			(troop_get_slot, ":obj_slider", tdp_objects, tdp_obj_slider_horse),
			(overlay_set_val, ":obj_slider", reg21),
		(try_end),
		(assign, ":obj_size", 70),
		(call_script, "script_gpu_resize_object", tdp_obj_label_chance_of_lance,    ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_chance_of_archery,  ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_chance_of_onehand,  ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_chance_of_twohand,  ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_chance_of_crossbow, ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_chance_of_throwing, ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_chance_of_polearm,  ":obj_size"),
		(call_script, "script_gpu_resize_object", tdp_obj_label_chance_of_horse,    ":obj_size"),
		
		# Appearance Menu Option - Column 4
		
		# Lances
        (position_set_x, pos1, ":x_col_menu_appearance"),
        (position_set_y, pos1, ":y_row_lance_buttons"),
        (create_combo_button_overlay, reg1),
		(troop_set_slot, tdp_objects, tdp_obj_menu_type_of_lance, reg1),
        (overlay_set_position, reg1, pos1),
        (try_for_range, ":slot_no", tpe_weapons_lance, tpe_weapons_archery),
			(troop_get_slot, ":item_no", tpe_weapons, ":slot_no"),
			(ge, ":item_no", 1), # Filter check for invalid items.
			(str_store_item_name, s1, ":item_no"),
			(overlay_add_item, reg1, "@{s1}"),
			(ge, DEBUG_TPE_DESIGN, 2),
			(display_message, "@DEBUG (TPE Design): Item '{s1}' added."),
		(try_end), # (overlay_add_item, reg1, "@Tournament Lance"),
		(store_add, ":appearance_slot", ":city_settings", tdp_val_setting_lance),
		(troop_get_slot, ":option_setting", tpe_menu_options, ":appearance_slot"),
        (overlay_set_val, reg1, ":option_setting"),
		(call_script, "script_gpu_resize_object", tdp_obj_menu_type_of_lance, 70),
		
		# Archery
        (position_set_x, pos1, ":x_col_menu_appearance"),
        (position_set_y, pos1, ":y_row_archery_buttons"),
        (create_combo_button_overlay, reg1),
		(troop_set_slot, tdp_objects, tdp_obj_menu_type_of_archery, reg1),
        (overlay_set_position, reg1, pos1),
        (try_for_range, ":slot_no", tpe_weapons_archery, tpe_weapons_onehand),
			(troop_get_slot, ":item_no", tpe_weapons, ":slot_no"),
			(ge, ":item_no", 1), # Filter check for invalid items.
			(str_store_item_name, s1, ":item_no"),
			(overlay_add_item, reg1, "@{s1}"),
			(ge, DEBUG_TPE_DESIGN, 2),
			(display_message, "@DEBUG (TPE Design): Item '{s1}' added."),
		(try_end), # (overlay_add_item, reg1, "@Tournament Bow"),
		(store_add, ":appearance_slot", ":city_settings", tdp_val_setting_archery),
		(troop_get_slot, ":option_setting", tpe_menu_options, ":appearance_slot"),
        (overlay_set_val, reg1, ":option_setting"),
		(call_script, "script_gpu_resize_object", tdp_obj_menu_type_of_archery, 70),
		
		# One Hand
        (position_set_x, pos1, ":x_col_menu_appearance"),
        (position_set_y, pos1, ":y_row_onehand_buttons"),
        (create_combo_button_overlay, reg1),
		(troop_set_slot, tdp_objects, tdp_obj_menu_type_of_onehand, reg1),
        (overlay_set_position, reg1, pos1),
		(try_for_range, ":slot_no", tpe_weapons_onehand, tpe_weapons_twohand),
			(troop_get_slot, ":item_no", tpe_weapons, ":slot_no"),
			(ge, ":item_no", 1), # Filter check for invalid items.
			(str_store_item_name, s1, ":item_no"),
			(overlay_add_item, reg1, "@{s1}"),
			(ge, DEBUG_TPE_DESIGN, 2),
			(display_message, "@DEBUG (TPE Design): Item '{s1}' added."),
		(try_end),
        # (overlay_add_item, reg1, "@Tournament Sword"),
		(store_add, ":appearance_slot", ":city_settings", tdp_val_setting_onehand),
		(troop_get_slot, ":option_setting", tpe_menu_options, ":appearance_slot"),
        (overlay_set_val, reg1, ":option_setting"),
		(call_script, "script_gpu_resize_object", tdp_obj_menu_type_of_onehand, 70),
		
		# Two Hand
        (position_set_x, pos1, ":x_col_menu_appearance"),
        (position_set_y, pos1, ":y_row_twohand_buttons"),
        (create_combo_button_overlay, reg1),
		(troop_set_slot, tdp_objects, tdp_obj_menu_type_of_twohand, reg1),
        (overlay_set_position, reg1, pos1),
        (try_for_range, ":slot_no", tpe_weapons_twohand, tpe_weapons_crossbow),
			(troop_get_slot, ":item_no", tpe_weapons, ":slot_no"),
			(ge, ":item_no", 1), # Filter check for invalid items.
			(str_store_item_name, s1, ":item_no"),
			(overlay_add_item, reg1, "@{s1}"),
			(ge, DEBUG_TPE_DESIGN, 2),
			(display_message, "@DEBUG (TPE Design): Item '{s1}' added."),
		(try_end), # (overlay_add_item, reg1, "@Tournament Greatsword"),
		(store_add, ":appearance_slot", ":city_settings", tdp_val_setting_twohand),
		(troop_get_slot, ":option_setting", tpe_menu_options, ":appearance_slot"),
        (overlay_set_val, reg1, ":option_setting"),
		(call_script, "script_gpu_resize_object", tdp_obj_menu_type_of_twohand, 70),
		
		# Crossbow
        (position_set_x, pos1, ":x_col_menu_appearance"),
        (position_set_y, pos1, ":y_row_crossbow_buttons"),
        (create_combo_button_overlay, reg1),
		(troop_set_slot, tdp_objects, tdp_obj_menu_type_of_crossbow, reg1),
        (overlay_set_position, reg1, pos1),
        (try_for_range, ":slot_no", tpe_weapons_crossbow, tpe_weapons_throwing),
			(troop_get_slot, ":item_no", tpe_weapons, ":slot_no"),
			(ge, ":item_no", 1), # Filter check for invalid items.
			(str_store_item_name, s1, ":item_no"),
			(overlay_add_item, reg1, "@{s1}"),
			(ge, DEBUG_TPE_DESIGN, 2),
			(display_message, "@DEBUG (TPE Design): Item '{s1}' added."),
		(try_end), # (overlay_add_item, reg1, "@Tournament Crossbow"),
		(store_add, ":appearance_slot", ":city_settings", tdp_val_setting_crossbow),
		(troop_get_slot, ":option_setting", tpe_menu_options, ":appearance_slot"),
        (overlay_set_val, reg1, ":option_setting"),
		(call_script, "script_gpu_resize_object", tdp_obj_menu_type_of_crossbow, 70),
		
		# Throwing
        (position_set_x, pos1, ":x_col_menu_appearance"),
        (position_set_y, pos1, ":y_row_throwing_buttons"),
        (create_combo_button_overlay, reg1),
		(troop_set_slot, tdp_objects, tdp_obj_menu_type_of_throwing, reg1),
        (overlay_set_position, reg1, pos1),
        (try_for_range, ":slot_no", tpe_weapons_throwing, tpe_weapons_polearm),
			(troop_get_slot, ":item_no", tpe_weapons, ":slot_no"),
			(ge, ":item_no", 1), # Filter check for invalid items.
			(str_store_item_name, s1, ":item_no"),
			(overlay_add_item, reg1, "@{s1}"),
			(ge, DEBUG_TPE_DESIGN, 2),
			(display_message, "@DEBUG (TPE Design): Item '{s1}' added."),
		(try_end), # (overlay_add_item, reg1, "@Tournament Javelins"),
		(store_add, ":appearance_slot", ":city_settings", tdp_val_setting_throwing),
		(troop_get_slot, ":option_setting", tpe_menu_options, ":appearance_slot"),
        (overlay_set_val, reg1, ":option_setting"),
		(call_script, "script_gpu_resize_object", tdp_obj_menu_type_of_throwing, 70),
		
		# Polearm
        (position_set_x, pos1, ":x_col_menu_appearance"),
        (position_set_y, pos1, ":y_row_polearm_buttons"),
        (create_combo_button_overlay, reg1),
		(troop_set_slot, tdp_objects, tdp_obj_menu_type_of_polearm, reg1),
        (overlay_set_position, reg1, pos1),
        (try_for_range, ":slot_no", tpe_weapons_polearm, tpe_weapons_mount),
			(troop_get_slot, ":item_no", tpe_weapons, ":slot_no"),
			(ge, ":item_no", 1), # Filter check for invalid items.
			(str_store_item_name, s1, ":item_no"),
			(overlay_add_item, reg1, "@{s1}"),
			(ge, DEBUG_TPE_DESIGN, 2),
			(display_message, "@DEBUG (TPE Design): Item '{s1}' added."),
		(try_end), # (overlay_add_item, reg1, "@Tournament Spear"),
		(store_add, ":appearance_slot", ":city_settings", tdp_val_setting_polearm),
		(troop_get_slot, ":option_setting", tpe_menu_options, ":appearance_slot"),
        (overlay_set_val, reg1, ":option_setting"),
		(call_script, "script_gpu_resize_object", tdp_obj_menu_type_of_polearm, 70),
		
		# Mount
        (position_set_x, pos1, ":x_col_menu_appearance"),
        (position_set_y, pos1, ":y_row_mount_buttons"),
        (create_combo_button_overlay, reg1),
		(troop_set_slot, tdp_objects, tdp_obj_menu_type_of_horse, reg1),
        (overlay_set_position, reg1, pos1),
        (try_for_range, ":slot_no", tpe_weapons_mount, tpe_weapons_outfit),
			(troop_get_slot, ":item_no", tpe_weapons, ":slot_no"),
			(ge, ":item_no", 1), # Filter check for invalid items.
			(str_store_item_name, s1, ":item_no"),
			(overlay_add_item, reg1, "@{s1}"),
			(ge, DEBUG_TPE_DESIGN, 2),
			(display_message, "@DEBUG (TPE Design): Item '{s1}' added."),
		(try_end), # (overlay_add_item, reg1, "@Tournament Mount"),
		(store_add, ":appearance_slot", ":city_settings", tdp_val_setting_horse),
		(troop_get_slot, ":option_setting", tpe_menu_options, ":appearance_slot"),
        (overlay_set_val, reg1, ":option_setting"),
		(call_script, "script_gpu_resize_object", tdp_obj_menu_type_of_horse, 70),
		
		# Outfit
        (position_set_x, pos1, ":x_col_menu_appearance"),
        (position_set_y, pos1, ":y_row_outfit_buttons"),
        (create_combo_button_overlay, reg1),
		(troop_set_slot, tdp_objects, tdp_obj_menu_type_of_outfit, reg1),
        (overlay_set_position, reg1, pos1),
        (try_for_range, ":slot_no", tpe_weapons_outfit, tpe_weapons_end_of_normal_items),
			(troop_get_slot, ":item_no", tpe_weapons, ":slot_no"),
			(ge, ":item_no", 1), # Filter check for invalid items.
			(str_store_item_name, s1, ":item_no"),
			(overlay_add_item, reg1, "@{s1}"),
			(ge, DEBUG_TPE_DESIGN, 2),
			(display_message, "@DEBUG (TPE Design): Item '{s1}' added."),
		(try_end), # (overlay_add_item, reg1, "@Standard Outfit"),
		(store_add, ":appearance_slot", ":city_settings", tdp_val_setting_outfit),
		(troop_get_slot, ":option_setting", tpe_menu_options, ":appearance_slot"),
        (overlay_set_val, reg1, ":option_setting"),
		(call_script, "script_gpu_resize_object", tdp_obj_menu_type_of_outfit, 70),
		
		# Real Chance % - Column 5
		# (store_sub, ":city_offset", "$tournament_town", towns_begin),
		# (store_mul, ":city_settings", ":city_offset", 10),
		(assign, reg21, 0),
		# Lances
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_button_disable", ":y_row_lance",    tdp_obj_label_real_chance_of_lance, gpu_center),
		(call_script, "script_gpu_resize_object", tdp_obj_label_real_chance_of_lance, 70),
		# Archery
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_button_disable", ":y_row_archery",    tdp_obj_label_real_chance_of_archery, gpu_center),
		(call_script, "script_gpu_resize_object", tdp_obj_label_real_chance_of_archery, 70),
		# One Hand
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_button_disable", ":y_row_onehand",    tdp_obj_label_real_chance_of_onehand, gpu_center),
		(call_script, "script_gpu_resize_object", tdp_obj_label_real_chance_of_onehand, 70),
		# Two Hand
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_button_disable", ":y_row_twohand",    tdp_obj_label_real_chance_of_twohand, gpu_center),
		(call_script, "script_gpu_resize_object", tdp_obj_label_real_chance_of_twohand, 70),
		# Crossbow
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_button_disable", ":y_row_crossbow",    tdp_obj_label_real_chance_of_crossbow, gpu_center),
		(call_script, "script_gpu_resize_object", tdp_obj_label_real_chance_of_crossbow, 70),
		# Throwing
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_button_disable", ":y_row_throwing",    tdp_obj_label_real_chance_of_throwing, gpu_center),
		(call_script, "script_gpu_resize_object", tdp_obj_label_real_chance_of_throwing, 70),
		# Polearm
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_button_disable", ":y_row_polearm",    tdp_obj_label_real_chance_of_polearm, gpu_center),
		(call_script, "script_gpu_resize_object", tdp_obj_label_real_chance_of_polearm, 70),
		# Mounts
		(call_script, "script_gpu_create_text_label", "str_tdp_label_reg21_percent", ":x_col_button_disable", ":y_row_mount",    tdp_obj_label_real_chance_of_mount, gpu_center),
		(call_script, "script_gpu_resize_object", tdp_obj_label_real_chance_of_mount, 70),
		
		(call_script, "script_tpe_determine_real_chance"),
		
		# Disable / Enable Buttons - Column 5
		# (call_script, "script_gpu_create_button", "str_tdp_label_disable", 700, ":y_row_mount_buttons",    tdp_obj_button_disable_horse),
		# (assign, ":obj_size", 70),
		# (call_script, "script_gpu_resize_object", tdp_obj_button_disable_horse,    ":obj_size"),
		
		# Selectable City Buttons - Column 6
		(store_sub, ":total_towns", towns_end, towns_begin),
		(val_add, ":total_towns", 1),
		(store_mul, ":scroll_length", ":total_towns", 35),
		(store_add, ":towns_end", ":total_towns", 200),
		(troop_set_slot, tdp_objects, tdp_obj_centers_begin, 200),
		(troop_set_slot, tdp_objects, tdp_obj_centers_end,   ":towns_end"),
		# script_gpu_container_heading   - pos_x, pos_y, size_x, size_y, storage_id
		(call_script, "script_gpu_container_heading", 750, 75, 200, 585, tdp_obj_container_center_buttons),
		
			(try_for_range, ":center_no", towns_begin, towns_end),
				(store_sub, ":center_offset", ":center_no", towns_begin),
				(store_add, ":center_slot", 200, ":center_offset"),
				(str_store_party_name, s21, ":center_no"),
				(call_script, "script_gpu_create_button", "str_tpe_s21", 50, ":scroll_length", 0),
				(troop_set_slot, tdp_objects, ":center_slot", reg1),
				(val_sub, ":scroll_length", 35),
			(try_end),
			
		(set_container_overlay, -1),
		
		(try_begin),
			(ge, DEBUG_TPE_DESIGN, 1),
			(call_script, "script_gpu_create_game_button", "str_tdp_label_test_scripts", 400, 15, tdp_obj_button_test_scripts),
		(try_end),
		(call_script, "script_gpu_create_checkbox_white", 35, 20, "str_tdp_label_affect_all_cities", tdp_obj_checkbox_affect_all_cities, tdp_val_checkbox_affect_all_cities),
		
		(presentation_set_duration, 999999),
    ]),
	
    (ti_on_presentation_event_state_change,
    [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
		# (assign, reg21, ":object"),
		# (display_message, "@The object interacted with is #{reg21}."),
		
		# (store_sub, ":city_offset", "$tournament_town", towns_begin),
		# (store_mul, ":city_settings", ":city_offset", 10),
		
		(try_begin),
			##### ACCEPT BUTTON #####
			(troop_slot_eq, tdp_objects, tdp_obj_button_done, ":object"),
			(presentation_set_duration, 0),
		
		(else_try),
			##### ENABLE ALL BUTTON #####
			(troop_slot_eq, tdp_objects, tdp_obj_button_enable_all, ":object"),
			(try_begin),
				(troop_slot_eq, tdp_objects, tdp_val_checkbox_affect_all_cities, 1),
				(try_for_range, ":center_no", towns_begin, towns_end),
					(call_script, "script_tpe_initialize_default_design_settings", ":center_no"),
				(try_end),
			(else_try),
				(call_script, "script_tpe_initialize_default_design_settings", "$tournament_town"),
			(try_end),
			(start_presentation, "prsnt_tpe_design_settings"),
			
		(else_try),
			##### NATIVE SETTINGS BUTTON #####
			(troop_slot_eq, tdp_objects, tdp_obj_button_native_settings, ":object"),
			(try_begin),
				(troop_slot_eq, tdp_objects, tdp_val_checkbox_affect_all_cities, 1),
				(try_for_range, ":center_no", towns_begin, towns_end),
					(call_script, "script_tpe_initialize_native_design_settings", ":center_no"),
				(try_end),
			(else_try),
				(call_script, "script_tpe_initialize_native_design_settings", "$tournament_town"),
			(try_end),
			(start_presentation, "prsnt_tpe_design_settings"),

		# (else_try),
			# ##### TEST SCRIPTS BUTTON #####
			# (troop_slot_eq, tdp_objects, tdp_obj_button_test_scripts, ":object"),
			# (store_sub, ":center_selected", "$tournament_town", towns_begin),
			# (store_mul, ":slots_begin", ":center_selected", 10),
			# (store_add, ":slots_end", ":slots_begin", 10),
			# (try_for_range, ":slot", ":slots_begin", ":slots_end"),
				# (troop_get_slot, ":item_no", tpe_appearance, ":slot"),
				# (ge, ":item_no", 1),
				# (assign, reg21, ":slot"),
				# (assign, reg22, ":item_no"),
				# (str_store_item_name, s21, ":item_no"),
				# (display_message, "@Found: Item #{reg22} - '{s21}' in slot #{reg21}."),
			# (try_end),
			
		(else_try),
			##### APPLY TO ALL CENTERS CHECKBOX #####
			(troop_slot_eq, tdp_objects, tdp_obj_checkbox_affect_all_cities, ":object"),
			(troop_set_slot, tdp_objects, tdp_val_checkbox_affect_all_cities, ":value"),
			
		(else_try),
			##### LANCE SLIDER #####
			(troop_slot_eq, tdp_objects, tdp_obj_slider_lance, ":object"),
			(call_script, "script_tdp_update_slider", ":object", tdp_val_setting_lance, ":value"),
			
		(else_try),
			##### ARCHERY SLIDER #####
			(troop_slot_eq, tdp_objects, tdp_obj_slider_archery, ":object"),
			(call_script, "script_tdp_update_slider", ":object", tdp_val_setting_archery, ":value"),
			
		(else_try),
			##### ONE HAND SLIDER #####
			(troop_slot_eq, tdp_objects, tdp_obj_slider_onehand, ":object"),
			(call_script, "script_tdp_update_slider", ":object", tdp_val_setting_onehand, ":value"),
			
		(else_try),
			##### TWO HAND SLIDER #####
			(troop_slot_eq, tdp_objects, tdp_obj_slider_twohand, ":object"),
			(call_script, "script_tdp_update_slider", ":object", tdp_val_setting_twohand, ":value"),
			
		(else_try),
			##### CROSSBOWS SLIDER #####
			(troop_slot_eq, tdp_objects, tdp_obj_slider_crossbow, ":object"),
			(call_script, "script_tdp_update_slider", ":object", tdp_val_setting_crossbow, ":value"),
			
		(else_try),
			##### THROWING SLIDER #####
			(troop_slot_eq, tdp_objects, tdp_obj_slider_throwing, ":object"),
			(call_script, "script_tdp_update_slider", ":object", tdp_val_setting_throwing, ":value"),
			
		(else_try),
			##### POLEARM SLIDER #####
			(troop_slot_eq, tdp_objects, tdp_obj_slider_polearm, ":object"),
			(call_script, "script_tdp_update_slider", ":object", tdp_val_setting_polearm, ":value"),
			
		(else_try),
			##### MOUNT SLIDER #####
			(troop_slot_eq, tdp_objects, tdp_obj_slider_horse, ":object"),
			(call_script, "script_tdp_update_slider", ":object", tdp_val_setting_horse, ":value"),
			
		(else_try),
			##### SCENE MENU #####
			(troop_slot_eq, tdp_objects, tdp_obj_menu_scene, ":object"),
			(party_set_slot, "$tournament_town", slot_town_arena_option, ":value"),
			(ge, DEBUG_TPE_DESIGN, 1),
			(assign, reg1, ":value"),
			(display_message, "@DEBUG (TPE Design): Scene set to option {reg1}."),
			
		(else_try),
			##### LANCE MENU #####
			(troop_slot_eq, tdp_objects, tdp_obj_menu_type_of_lance, ":object"),
			(call_script, "script_tdp_update_menu_selection", tdp_val_setting_lance, tpe_weapons_lance, ":value"),
			
		(else_try),
			##### ARCHERY MENU #####
			(troop_slot_eq, tdp_objects, tdp_obj_menu_type_of_archery, ":object"),
			(call_script, "script_tdp_update_menu_selection", tdp_val_setting_archery, tpe_weapons_archery, ":value"),
			
		(else_try),
			##### ONE HAND MENU #####
			(troop_slot_eq, tdp_objects, tdp_obj_menu_type_of_onehand, ":object"),
			(call_script, "script_tdp_update_menu_selection", tdp_val_setting_onehand, tpe_weapons_onehand, ":value"),
			
		(else_try),
			##### TWO HAND MENU #####
			(troop_slot_eq, tdp_objects, tdp_obj_menu_type_of_twohand, ":object"),
			(call_script, "script_tdp_update_menu_selection", tdp_val_setting_twohand, tpe_weapons_twohand, ":value"),
			
		(else_try),
			##### CROSSBOW MENU #####
			(troop_slot_eq, tdp_objects, tdp_obj_menu_type_of_crossbow, ":object"),
			(call_script, "script_tdp_update_menu_selection", tdp_val_setting_crossbow, tpe_weapons_crossbow, ":value"),
			
		(else_try),
			##### THROWING MENU #####
			(troop_slot_eq, tdp_objects, tdp_obj_menu_type_of_throwing, ":object"),
			(call_script, "script_tdp_update_menu_selection", tdp_val_setting_throwing, tpe_weapons_throwing, ":value"),
			
		(else_try),
			##### POLEARM MENU #####
			(troop_slot_eq, tdp_objects, tdp_obj_menu_type_of_polearm, ":object"),
			(call_script, "script_tdp_update_menu_selection", tdp_val_setting_polearm, tpe_weapons_polearm, ":value"),
			
		(else_try),
			##### MOUNT MENU #####
			(troop_slot_eq, tdp_objects, tdp_obj_menu_type_of_horse, ":object"),
			(call_script, "script_tdp_update_menu_selection", tdp_val_setting_horse, tpe_weapons_mount, ":value"),
			
		(else_try),
			##### OUTFIT MENU #####
			(troop_slot_eq, tdp_objects, tdp_obj_menu_type_of_outfit, ":object"),
			(call_script, "script_tdp_update_menu_selection", tdp_val_setting_outfit, tpe_weapons_outfit, ":value"),
			
		(else_try),
			##### CHANGE CENTER BUTTON #####
			(troop_get_slot, ":towns_begin", tdp_objects, tdp_obj_centers_begin),
			(troop_get_slot, ":towns_end",   tdp_objects, tdp_obj_centers_end),
			(assign, ":pass", 0),
			(try_for_range, ":center_button_check", ":towns_begin", ":towns_end"),
				(eq, ":pass", 0), # Makes sure only the first qualifying match is used.
				(troop_slot_eq, tdp_objects, ":center_button_check", ":object"),
				(assign, ":pass", ":center_button_check"),
			(try_end),
			(is_between, ":pass", ":towns_begin", ":towns_end"),
			(store_sub, ":center_selected", ":pass", ":towns_begin"),
			(store_add, ":center_no", towns_begin, ":center_selected"),
			(assign, "$tournament_town", ":center_no"),
			(start_presentation, "prsnt_tpe_design_settings"),
			
		(try_end),
		
	]),
  ]),
  
##############################################################################
####               TOURNAMENT CREDITS & INFORMATION PANEL                 ####
##############################################################################
# This preference panel will set what kinds of equipment the player wishes allowed in each city's specific tournaments.
  ("tpe_credits", 0, mesh_load_window, [
    (ti_on_presentation_load,
    [
		(set_fixed_point_multiplier, 1000),
		(assign, "$gpu_storage", tci_objects),
		(assign, "$gpu_data",    tci_objects),
		
		# Background Mesh
		(create_mesh_overlay, reg1, "mesh_tournament_design_panel"),
        (position_set_x, pos1, 0),
        (position_set_y, pos1, 0),
        (overlay_set_position, reg1, pos1),
		
		# Margins
		(assign, ":x_col_label_titles",     20), # Left aligned.
		(assign, ":y_line_step",            25), # Spacing between lines of text.
		(store_sub, ":x_col_bold_titles", ":x_col_label_titles", 5), # Left aligned.
		#(store_sub, ":x_col_num_titles",  ":x_col_label_titles", 5), # Right aligned.
		
		# Button Definitions
		(call_script, "script_gpu_create_game_button", "str_tci_exit",        895, 15, tci_obj_button_exit),
		(try_begin),
			(neg|troop_slot_eq, tci_objects, tci_val_information_mode, 0), # Not the Main Topics Mode
			(call_script, "script_gpu_create_game_button", "str_tci_main_topics", 730, 15, tci_obj_button_main_topics),
		(try_end),
		
		# Create header display
		(call_script, "script_gpu_create_text_label", "str_tci_main_title", 15, 680, 0, gpu_left_with_outline),
		(overlay_set_color, reg1, gpu_white),
		(call_script, "script_gpu_resize_object", 0, 150),
		(call_script, "script_gpu_create_text_label", "str_tci_sub_title", ":x_col_label_titles", 650, 0, gpu_left),
		# Dividing Lines
		(call_script, "script_gpu_draw_line", 970, 2, 15, 630, gpu_gray), # horizontal line sub title.
		
		### INFORMATION TOPICS ###
		(call_script, "script_gpu_container_heading", 0, 75, 960, 525, tci_obj_container_info),
			
			# Determine what kind of information to display here.
			(try_begin),
				(troop_slot_eq, tci_objects, tci_val_information_mode, 0), # Main Topics
				(assign, ":string_begin", "str_tpe_info_0a"),
				(assign, ":string_end",   "str_tpe_info_1a"),
			(else_try),
				(troop_slot_eq, tci_objects, tci_val_information_mode, 1), # Gameplay
				(assign, ":string_begin", "str_tpe_info_1a"),
				(assign, ":string_end",   "str_tpe_info_2a"),
			(else_try),
				(troop_slot_eq, tci_objects, tci_val_information_mode, 2), # Scoring
				(assign, ":string_begin", "str_tpe_info_2a"),
				(assign, ":string_end",   "str_tpe_info_3a"),
			(else_try),
				(troop_slot_eq, tci_objects, tci_val_information_mode, 3), # Betting
				(assign, ":string_begin", "str_tpe_info_3a"),
				(assign, ":string_end",   "str_tpe_info_4a"),
			(else_try),
				(troop_slot_eq, tci_objects, tci_val_information_mode, 4), # Options Panel
				(assign, ":string_begin", "str_tpe_info_4a"),
				(assign, ":string_end",   "str_tpe_info_5a"),
			(else_try),
				(troop_slot_eq, tci_objects, tci_val_information_mode, 5), # Design Panel
				(assign, ":string_begin", "str_tpe_info_5a"),
				(assign, ":string_end",   "str_tpe_info_6a"),
			(else_try),
				(troop_slot_eq, tci_objects, tci_val_information_mode, 6), # Rewards
				(assign, ":string_begin", "str_tpe_info_6a"),
				(assign, ":string_end",   "str_tpe_info_7a"),
			(else_try),
				(troop_slot_eq, tci_objects, tci_val_information_mode, 7), # Achievements
				(assign, ":string_begin", "str_tpe_info_7a"),
				(assign, ":string_end",   "str_tpe_info_8a"),
			(else_try),
				(troop_slot_eq, tci_objects, tci_val_information_mode, 8), # Credits
				(assign, ":string_begin", "str_tpe_info_8a"),
				(assign, ":string_end",   "str_tpe_info_9a"),
			(try_end),
			(assign, ":topic_count", 0),
			(store_sub, ":y_start", ":string_end", ":string_begin"),
			(val_mul, ":y_start", ":y_line_step"),
			(val_add, ":y_start", ":y_line_step"),
			(assign, ":pos_y", ":y_start"),
			
			(call_script, "script_gpu_create_text_label", "str_tpe_info_1b",  ":x_col_bold_titles",  ":pos_y", 0, gpu_left),
			
			(troop_get_slot, ":title_string", tci_objects, tci_val_information_mode),
			(val_add, ":title_string", "str_tpe_info_0"),
			(call_script, "script_gpu_create_text_label", ":title_string",  ":x_col_bold_titles",  ":pos_y", 0, gpu_left_with_outline),
			(overlay_set_color, reg1, gpu_white),
			(val_sub, ":pos_y", ":y_line_step"),
			
			(try_for_range, ":topic_no", ":string_begin", ":string_end"),
				(store_add, ":obj_slot", tci_obj_topics_begin, ":topic_count"),
				(val_add, ":topic_count", 1),
				(try_begin),
					(troop_slot_eq, tci_objects, tci_val_information_mode, 0), # Main Topics
					(assign, reg5, ":topic_count"),
					#(call_script, "script_gpu_create_text_label",  "str_tpe_reg5", ":x_col_num_titles",   ":pos_y", 0, gpu_right),
					(store_sub, ":pos_y_button", ":pos_y", 13),
					(store_add, ":pos_x_button", ":x_col_label_titles", 0),
					(call_script, "script_gpu_create_button", ":topic_no", ":pos_x_button", ":pos_y_button", ":obj_slot"),
					(position_set_x, pos1, 1250),
					(position_set_y, pos1, 1000),
					(overlay_set_size, reg1, pos1),
					# (assign, reg21, ":topic_count"),
					# (val_add, reg21, 1),
					# (val_div, reg21, 2),
					# (assign, reg22, ":obj_slot"),
					# (display_message, "@Topic #{reg21}, Object {reg1} stored in slot {reg22}."),
				(else_try),
					(call_script, "script_gpu_create_text_label",  ":topic_no", ":x_col_label_titles", ":pos_y", 0, gpu_left),
					#(call_script, "script_gpu_resize_object", 0, 70),
				(try_end),
				(val_sub, ":pos_y", ":y_line_step"),
			(try_end),
			#(val_div, ":topic_count", 2),
			(store_add, ":obj_slot", tci_obj_topics_begin, ":topic_count"),
			(troop_set_slot, tci_objects, tci_obj_topics_end, ":obj_slot"),
		(set_container_overlay, -1),
		
		(presentation_set_duration, 999999),
    ]),
	
    (ti_on_presentation_event_state_change,
    [
        (store_trigger_param_1, ":object"),
        #(store_trigger_param_2, ":value"),
		# (assign, reg21, ":object"),
		# (display_message, "@The object interacted with is #{reg21}."),
		
		(try_begin),
			##### DONE BUTTON #####
			(troop_slot_eq, tci_objects, tci_obj_button_exit, ":object"),
			(presentation_set_duration, 0),
			
		(else_try),
			##### BACK BUTTON #####
			(troop_slot_eq, tci_objects, tci_obj_button_main_topics, ":object"),
			(neg|troop_slot_eq, tci_objects, tci_val_information_mode, 0), # Not the Main Topics Mode
			(troop_set_slot, tci_objects, tci_val_information_mode, 0),
			(start_presentation, "prsnt_tpe_credits"),
			
		(else_try),
			##### ANY INFO TOPIC BUTTON #####
			(troop_slot_eq, tci_objects, tci_val_information_mode, 0), # Main Topics
			# (troop_get_slot, ":topics_begin", tci_objects, tci_obj_topics_begin),
			# (troop_get_slot, ":topics_end",   tci_objects, tci_obj_topics_end),
			# (assign, reg21, ":topics_begin"),
			# (assign, reg22, ":topics_end"),
			#(display_message, "@DEBUG: Topic strings go from {reg21} to {reg22}."),
			(assign, ":pass", 0),
			(try_for_range, ":slot_no", tci_obj_topics_begin, tci_obj_topics_end),
				# (assign, reg21, ":slot_no"),
				# (troop_get_slot, reg22, tci_objects, ":slot_no"),
				# (display_message, "@Slot {reg21} holds object #{reg22}."),
				(troop_slot_eq, tci_objects, ":slot_no", ":object"),
				(assign, ":pass", ":slot_no"),
			(try_end),
			(ge, ":pass", 1),
			#(is_between, ":object", ":topics_begin", ":topics_end"),
			(store_sub, ":topic_no", ":pass", tci_obj_topics_begin),
			(val_add, ":topic_no", 1),
			(troop_set_slot, tci_objects, tci_val_information_mode, ":topic_no"),
			(start_presentation, "prsnt_tpe_credits"),
			
		(try_end),
		
	]),
  ]),
 ]
	
def modmerge_presentations(orig_presentations, check_duplicates = False):
    if( not check_duplicates ):
        orig_presentations.extend(presentations) # Use this only if there are no replacements (i.e. no duplicated item names)
    else:
    # Use the following loop to replace existing entries with same id
        for i in range (0,len(presentations)-1):
          find_index = find_object(orig_presentations, presentations[i][0]); # find_object is from header_common.py
          if( find_index == -1 ):
            orig_presentations.append(presentations[i])
          else:
            orig_presentations[find_index] = presentations[i]

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "presentations"
        orig_presentations = var_set[var_name_1]
        modmerge_presentations(orig_presentations)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)