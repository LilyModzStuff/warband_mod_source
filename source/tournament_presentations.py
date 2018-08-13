# Tournament Play Enhancements (1.2) by Windyplains
# Released 9/22/2011

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
#####                                           TPE 1.2 New Option Display                                            #####
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
		(assign, ":pos_y_options", 700), # 635
		#(assign, ":pos_y_enhancements", 400),
		
		# OBJ #1 - DESCRIPTION text box
		(create_text_overlay, reg1, "@TOURNAMENT SETTINGS",  tf_center_justify|tf_with_outline),
		(overlay_set_color, reg1, wp_white),
		(position_set_x, pos1, 745),
        (position_set_y, pos1, 665),
        (overlay_set_position, reg1, pos1),
		(position_set_x, pos1, 1400),
        (position_set_y, pos1, 1400),
		(overlay_set_size, reg1, pos1),	
		
		# OBJ #24 - DESCRIPTION text box
		(create_text_overlay, "$g_presentation_obj_24"),
		(position_set_x, pos1, 80),
        (position_set_y, pos1, 310),
		(overlay_set_position, "$g_presentation_obj_24", pos1),
		(overlay_set_text, "$g_presentation_obj_24", "@You have nothing."),
		
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

		# OBJ #26 - RANDOMIZE button
        (create_game_button_overlay, "$g_presentation_obj_26", "@Randomize"),
        (position_set_x, pos1, 660),
        (position_set_y, pos1, 50),
        (overlay_set_position, "$g_presentation_obj_26", pos1),
		
		# CHARACTER MENU BEGIN
		# OBJ 21 - Text
		(position_set_x, pos1, 290),
        (position_set_y, pos1, 345),
		
		(create_combo_label_overlay, "$g_presentation_obj_18"),
        (overlay_set_position, "$g_presentation_obj_18", pos1),
		(party_get_num_companion_stacks, ":num_stacks","p_main_party"),
		(assign, ":hero_slot", 0),
        (try_for_range, ":stack_num", 0, ":num_stacks"),
          (party_stack_get_troop_id,":stack_troop","p_main_party",":stack_num"),
          (troop_is_hero, ":stack_troop"),
		  (str_clear, s1),
		  (str_store_troop_name, s1, ":stack_troop"),
		  (troop_set_slot, "trp_temp_troop", ":hero_slot", ":stack_troop"),
		  (val_add, ":hero_slot", 1),
		  (overlay_add_item, "$g_presentation_obj_18", "@{s1}"),
		  (try_begin),
			(eq, ":stack_troop", "$g_wp_tpe_troop"),
			(overlay_set_val, "$g_presentation_obj_18", ":stack_num"),
		  (try_end),
        (try_end),
		# CHARACTER MENU END
			
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
		(position_set_y, pos1, 540), 
		(overlay_set_area_size, reg1, pos1),
		(set_container_overlay, reg1),
		############### OPTIONS CONTAINER BEGIN ###############
			(assign, ":pos_x", ":pos_x_options"),  # Sets the second column of options.
			(assign, ":pos_y", ":pos_y_options"),
			
			## OBJ 17r1 - Text
			(create_text_overlay, "$g_presentation_obj_17", "@Global Options", tf_vertical_align_center|tf_with_outline),
			(overlay_set_color, "$g_presentation_obj_17", wp_white),
			(position_set_x, pos1, ":pos_x_titles"),
			(position_set_y, pos1, ":pos_y"),
			(overlay_set_position, "$g_presentation_obj_17", pos1),
			
			## OBJ #36 - Option: Renown Scaling - checkbox
			(val_add, ":pos_y", ":title_frame_y_margin"),
			# text
			(store_add, ":text_pos_x", ":pos_x", ":checkbox_text_x_margin"), (position_set_x, pos1, ":text_pos_x"),
			(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
			(create_text_overlay, "$g_presentation_obj_36", "@Renown Scaling", tf_left_align|tf_vertical_align_center),
			(overlay_set_position, "$g_presentation_obj_36", pos1),
			# checkbox
			(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
			(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
			(create_check_box_overlay, "$g_presentation_obj_36", "mesh_checkbox_off", "mesh_checkbox_on"),
			(overlay_set_position, "$g_presentation_obj_36", pos1),
			
			# OBJ 19 - PERSISTENT BETTING dropdown Menu
			(val_sub, ":pos_y", 40), 
			(store_add, ":text_pos_y", ":pos_y", 0), (position_set_y, pos1, ":text_pos_y"),
			(store_add, ":text_pos_x", ":pos_x", 125), (position_set_x, pos1, ":text_pos_x"),
			(create_combo_button_overlay, "$g_presentation_obj_19"),
			(overlay_set_position, "$g_presentation_obj_19", pos1),
			(overlay_add_item, "$g_presentation_obj_19", "@Bet Nothing"), # Bet values are defined in tournament_constants.py
			(assign, reg5, wp_tpe_bet_tier_1),
			(overlay_add_item, "$g_presentation_obj_19", "@Bet {reg5} per round"),
			(assign, reg5, wp_tpe_bet_tier_2),
			(overlay_add_item, "$g_presentation_obj_19", "@Bet {reg5} per round"),
			(assign, reg5, wp_tpe_bet_tier_3),
			(overlay_add_item, "$g_presentation_obj_19", "@Bet {reg5} per round"),
			(assign, reg5, wp_tpe_bet_tier_4),
			(overlay_add_item, "$g_presentation_obj_19", "@Bet {reg5} per round"),
			(assign, reg5, wp_tpe_bet_tier_5),
			(overlay_add_item, "$g_presentation_obj_19", "@Bet {reg5} per round"),
			(troop_get_slot, ":bet_option", "trp_player", slot_troop_tournament_bet_option),
			(overlay_set_val, "$g_presentation_obj_19", ":bet_option"),
		
			## OBJ 17r2 - Text
			(val_add, ":pos_y", ":checkbox_frame_y_margin"),
			(val_add, ":pos_y", ":checkbox_frame_y_margin"),
			#(assign, ":pos_x", ":pos_x_options"),
			(create_text_overlay, "$g_presentation_obj_17", "@Individual Options", tf_vertical_align_center|tf_with_outline),
			(overlay_set_color, "$g_presentation_obj_17", wp_white),
			(position_set_x, pos1, ":pos_x_titles"),
			(store_add, ":text_pos_y", ":pos_y", ":checkbox_text_y_margin"),  (position_set_y, pos1, ":text_pos_y"),
			(overlay_set_position, "$g_presentation_obj_17", pos1),

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
			(create_text_overlay, "$g_presentation_obj_9", "@Javelin & Shield", tf_left_align|tf_vertical_align_center),
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
			(str_store_string, s1, "@Help Display"),
			(str_store_string, s2, "@To find out more information about a \
									^specific feature simply hover the mouse \
									^cursor over that option.^^^"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_2"), # The DONE button.
			(str_store_string, s1, "@The 'Done' Button"),
			(str_store_string, s2, "@This will end the current presentation and \
									^return to the tournament menu.^^^^"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_26"), # The RANDOMIZE button.
			(str_store_string, s1, "@The 'Randomize' Button"),
			(str_store_string, s2, "@This will automatically select three\
									^randomly chosen options for your character\
									^that will stay the same each round.  If\
									^you want to always have random choices\
									^use the 'Always Random' option."),
		(else_try),
			(eq, ":object", "$g_presentation_obj_18"), # The Character Button.
			(str_store_string, s1, "@The 'Character' Button"),
			(str_store_string, s2, "@Using the arrows you can cycle through\
									^your character and each companion you\
									^currently have in your party.^^^"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_19"), # The Persistent Bet menu.
			(str_store_string, s1, "@The 'Persistent Bet' Menu"),
			(str_store_string, s2, "@By setting this menu you will automatically\
									^place the appropriate bet amount every\
									^round of a tournament if you have enough\
									^money to do so.\
									^Note: This works for the player only.^"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_36"), # The Renown Scaling checkbox.
			(str_store_string, s1, "@The 'Renown Scaling' Checkbox"),
			(str_store_string, s2, "@With this enabled you will gain an amount\
									^of renown on a tournament win proportional\
									^to your level and renown.  The higher your\
									^level or renown is the less you will receive.\
									^Note: This works for the player only.^"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_37"), # The Always Randomize checkbox.
			(str_store_string, s1, "@The 'Always Randomize' Checkbox"),
			(str_store_string, s2, "@With this enabled you will always have\
									^random options chosen each round.  This\
									^allows you to have an experience closer\
									^to native gameplay.\
									^Note: This works for the player only.^"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_38"), # The Never Spawn checkbox.
			(str_store_string, s1, "@The 'Never Spawn' Checkbox"),
			(str_store_string, s2, "@With this enabled the selected character\
									^will never be chosen to join tournaments\
									^to keep out companions that are not meant\
									^to be fighters.\
									^Note: This works for companions only.^"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_11"), # The HORSE checkbox.
			(str_store_string, s1, "@The 'Horse' Checkbox"),
			# str_store_string,s2, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  - Used for length checking.
			(str_store_string, s2, "@You will always enter play mounted.  By\
									^enabling this you open up the option to\
									^select the enhanced horse which is a\
									^warhose.^^"),
		(try_end),
		(overlay_set_text, "$g_presentation_obj_3", "@{s1}"),
		(overlay_set_text, "$g_presentation_obj_16", "@{s2}"),
      ]),
	
    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
		
		(try_begin),
			(eq, ":object", "$g_presentation_obj_2"), # The DONE button.
			(presentation_set_duration, 0),
		(else_try),
			(eq, ":object", "$g_presentation_obj_26"), # The RANDOMIZE button.
			(call_script, "script_tpe_equip_troop", "$g_wp_tpe_troop"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_4"), # Lance checkbox
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_lance, ":value", ":object"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_5"), # Bow & Arrow checkbox
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_bow, ":value", ":object"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_6"), # 1H Weapon & Shield checkbox
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_onehand, ":value", ":object"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_7"), # 2H Weapon checkbox
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_twohand, ":value", ":object"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_8"), # Crossbow checkbox
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_crossbow, ":value", ":object"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_9"), # Throwing checkbox
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_throwing, ":value", ":object"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_10"), # Polearm checkbox
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_polearm, ":value", ":object"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_11"), # Horse checkbox
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_horse, ":value", ":object"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_12"), # Enhanced Horse checkbox
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_enhanced_horse, ":value", ":object"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_13"), # Enhanced Armor checkbox
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_enhanced_armor, ":value", ":object"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_14"), # Enhanced Weapons checkbox
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_enhanced_weapons, ":value", ":object"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_15"), # Enhanced Shield checkbox
			(call_script, "script_tpe_set_option", "$g_wp_tpe_troop", slot_troop_tournament_enhanced_shield, ":value", ":object"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_18"), # Character menu
			(troop_get_slot, "$g_wp_tpe_troop", "trp_temp_troop", ":value"),
			(str_store_troop_name, s5, "$g_wp_tpe_troop"),
			#(display_message, "@Character menu set to {s5}."),
		(else_try),
			(eq, ":object", "$g_presentation_obj_19"), # Persistent Bet menu
			(troop_set_slot, "trp_player", slot_troop_tournament_bet_option, ":value"),
			# Betting values are defined in tournament_constants.py
			(try_begin),
				(eq, ":value", 0),
				(troop_set_slot, "$g_wp_tpe_troop", slot_troop_tournament_bet_amount, 0),
			(else_try),
				(eq, ":value", 1),
				(troop_set_slot, "$g_wp_tpe_troop", slot_troop_tournament_bet_amount, wp_tpe_bet_tier_1),
			(else_try),
				(eq, ":value", 2),
				(troop_set_slot, "$g_wp_tpe_troop", slot_troop_tournament_bet_amount, wp_tpe_bet_tier_2),
			(else_try),
				(eq, ":value", 3),
				(troop_set_slot, "$g_wp_tpe_troop", slot_troop_tournament_bet_amount, wp_tpe_bet_tier_3),
			(else_try),
				(eq, ":value", 4),
				(troop_set_slot, "$g_wp_tpe_troop", slot_troop_tournament_bet_amount, wp_tpe_bet_tier_4),
			(else_try),
				(eq, ":value", 5),
				(troop_set_slot, "$g_wp_tpe_troop", slot_troop_tournament_bet_amount, wp_tpe_bet_tier_5),
			(try_end),
			(troop_get_slot, ":bet_amount", "trp_player", slot_troop_tournament_bet_amount),
			(assign, reg0, ":bet_amount"),
			#(display_message, "@Your bet per round has been set to {reg0}."),
		(else_try),
			(eq, ":object", "$g_presentation_obj_36"), # Renown Scaling checkbox
			(assign, "$g_wp_tpe_renown_scaling", ":value"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_37"), # Always Randomize checkbox
			(try_begin),
				(eq, ":value", 1),
				(call_script, "script_tpe_clear_selections", "$g_wp_tpe_troop"),
				(troop_set_slot, "$g_wp_tpe_troop", slot_troop_tournament_always_randomize, 0),
			(else_try),
				(troop_set_slot, "$g_wp_tpe_troop", slot_troop_tournament_always_randomize, 1),
			(try_end),
		(else_try),
			(eq, ":object", "$g_presentation_obj_38"), # Never Spawn checkbox
			(try_begin),
				(neq, "$g_wp_tpe_troop", "trp_player"),
				(troop_set_slot, "$g_wp_tpe_troop", slot_troop_tournament_never_spawn, ":value"),
			(else_try),
				(display_message, "@You really don't want that turned ON for your main character."),
				(overlay_set_val, "$g_presentation_obj_38", 0),
			(try_end),
		(try_end),
		(start_presentation, "prsnt_tournament_options_panel"),
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