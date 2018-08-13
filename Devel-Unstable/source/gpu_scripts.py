# Generic Presentation Utilities (1.0) by Windyplains
# Released --/--/--

from header_common import *
from header_operations import *
from header_mission_templates import *
from header_items import *
from header_presentations import * 
from module_constants import *


####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

scripts = [	 
###########################################################################################################################
#####                                          Presentation Utilities 1.0                                             #####
###########################################################################################################################
# script_gpu_create_checkbox     - pos_x, pos_y, label, storage_slot, value_slot
# script_gpu_create_mesh         - mesh_id, pos_x, pos_y, size_x, size_y
# script_gpu_create_portrait     - troop_id, pos_x, pos_y, size, storage_id
# script_gpu_create_button       - title, pos_x, pos_y, storage_id
# script_gpu_create_text_label   - title, pos_x, pos_y, storage_id, design
# script_gpu_resize_object       - storage_id, percent size
# script_gpu_draw_line           - x length, y length, pos_x, pos_y, color
# script_gpu_container_heading   - pos_x, pos_y, size_x, size_y, storage_id
# script_gpu_create_slider - min, max, pos_x, pos_y, storage_id, value_id
		
# script_gpu_create_mesh
# Creates a mesh image based on mesh ID, (x,y) position, (x,y) size.
# Input: mesh_id, pos_x, pos_y, size_x, size_y
# Output: none
("gpu_create_mesh",
		[
			(store_script_param, ":mesh", 1),
			(store_script_param, ":pos_x", 2),
			(store_script_param, ":pos_y", 3),
			(store_script_param, ":size_x", 4),
			(store_script_param, ":size_y", 5),
			
			(set_fixed_point_multiplier, 1000),
			
			(create_mesh_overlay, reg1, ":mesh"),
			
			(position_set_x, pos1, ":pos_x"),
			(position_set_y, pos1, ":pos_y"),
			(overlay_set_position, reg1, pos1),

			(position_set_x, pos2, ":size_x"),
			(position_set_y, pos2, ":size_y"),
			(overlay_set_size, reg1, pos2),
		]
	),

# script_gpu_create_slider
# Creates a slider based on mesh ID, (x,y) position, (x,y) size.
# Input: min, max, pos_x, pos_y, storage_id, value_id
# Output: none
("gpu_create_slider",
		[
			(store_script_param, ":minimum", 1),
			(store_script_param, ":maximum", 2),
			(store_script_param, ":pos_x", 3),
			(store_script_param, ":pos_y", 4),
			(store_script_param, ":storage", 5),
			(store_script_param, ":value_id", 6),
			
			(set_fixed_point_multiplier, 1000),
			
			(store_add, ":text_pos_y", ":pos_y", 0), (position_set_y, pos1, ":text_pos_y"),
			(store_add, ":text_pos_x", ":pos_x", 125), (position_set_x, pos1, ":text_pos_x"),
			(create_slider_overlay, reg1, ":minimum", ":maximum"),
			(troop_set_slot, "$gpu_storage", ":storage", reg1),
			(overlay_set_position, reg1, pos1),
			(troop_get_slot, ":value", "$gpu_data", ":value_id"),
			(overlay_set_val, reg1, ":value"),
		]
	),

# script_gpu_create_button
# Creates a button based on title, (x,y) position, and storage slot ID.
# Input: title, pos_x, pos_y, storage_id
# Output: none
("gpu_create_button",
		[
			(store_script_param, ":title", 1),
			(store_script_param, ":pos_x", 2),
			(store_script_param, ":pos_y", 3),
			(store_script_param, ":storage", 4),
			
			(set_fixed_point_multiplier, 1000),
			
			(create_button_overlay, reg1, ":title"),
			(position_set_x, pos1, ":pos_x"),
			(position_set_y, pos1, ":pos_y"),
			(overlay_set_position, reg1, pos1),
			(troop_set_slot, "$gpu_storage", ":storage", reg1),
		]
	),
	
# script_gpu_create_game_button
# Creates a button based on title, (x,y) position, and storage slot ID.
# Input: title, pos_x, pos_y, storage_id
# Output: none
("gpu_create_game_button",
		[
			(store_script_param, ":title", 1),
			(store_script_param, ":pos_x", 2),
			(store_script_param, ":pos_y", 3),
			(store_script_param, ":storage", 4),
			
			(set_fixed_point_multiplier, 1000),
			
			(create_game_button_overlay, reg1, ":title"),
			(position_set_x, pos1, ":pos_x"),
			(position_set_y, pos1, ":pos_y"),
			(overlay_set_position, reg1, pos1),
			(troop_set_slot, "$gpu_storage", ":storage", reg1),
		]
	),
	
# script_gpu_create_text_label
# Creates a button based on title, (x,y) position, and storage slot ID.
# Input: title, pos_x, pos_y, storage_id, design
# Output: none
("gpu_create_text_label",
		[
			(store_script_param, ":title", 1),
			(store_script_param, ":pos_x", 2),
			(store_script_param, ":pos_y", 3),
			(store_script_param, ":storage", 4),
			(store_script_param, ":design", 5),
			
			(try_begin),
				(eq, ":design", gpu_center_with_outline),
				(create_text_overlay, reg1, ":title", tf_center_justify|tf_with_outline|tf_vertical_align_center),
			(else_try),
				(eq, ":design", gpu_center),
				(create_text_overlay, reg1, ":title", tf_center_justify|tf_vertical_align_center),
			(else_try),
				(eq, ":design", gpu_left_with_outline),
				(create_text_overlay, reg1, ":title", tf_left_align|tf_with_outline|tf_vertical_align_center),
			(else_try),
				(eq, ":design", gpu_left),
				(create_text_overlay, reg1, ":title", tf_left_align|tf_vertical_align_center),
			(else_try),
				(eq, ":design", gpu_right_with_outline),
				(create_text_overlay, reg1, ":title", tf_right_align|tf_with_outline|tf_vertical_align_center),
			(else_try),
				(eq, ":design", gpu_right),
				(create_text_overlay, reg1, ":title", tf_right_align|tf_vertical_align_center),
			(try_end), 
			
			(position_set_x, pos1, ":pos_x"),
			(position_set_y, pos1, ":pos_y"),
			(overlay_set_position, reg1, pos1),
			(troop_set_slot, "$gpu_storage", ":storage", reg1),
			(try_begin),
				(ge, wp_gpu_debug, 1),
				(assign, reg31, reg1),
				(assign, reg32, ":storage"),
				(str_store_string, s31, ":title"),
				(display_message, "@DEBUG (GPU): Label '{s31}' stored in slot {reg32}, value {reg31}."),
			(try_end),
		]
	),
	
# script_gpu_create_checkbox
# Creates a checkbox based on (x,y) position, text label, slot obj_id is stored in, and slot current value is stored in.
# Input: pos_x, pos_y, label, storage_slot, value_slot
# Output: none
("gpu_create_checkbox",
		[
			(store_script_param, ":pos_x", 1),
			(store_script_param, ":pos_y", 2),
			(store_script_param, ":label", 3),
			(store_script_param, ":storage", 4),
			(store_script_param, ":val_slot", 5),
			
			# text
			(store_add, ":text_pos_x", ":pos_x", 20), (position_set_x, pos1, ":text_pos_x"),
			(store_add, ":text_pos_y", ":pos_y", 10),  (position_set_y, pos1, ":text_pos_y"),
			(create_text_overlay, reg1, ":label", tf_left_align|tf_vertical_align_center),
			(overlay_set_position, reg1, pos1),
			# checkbox
			(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
			(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
			(create_check_box_overlay, reg1, "mesh_checkbox_off", "mesh_checkbox_on"),
			(overlay_set_position, reg1, pos1),
			(troop_set_slot, "$gpu_storage", ":storage", reg1),
			(troop_get_slot, ":setting", "$gpu_data", ":val_slot"),
			(overlay_set_val, reg1, ":setting"),
		]
	),
	
# script_gpu_create_checkbox_white 
# Creates a checkbox based on (x,y) position, text label, slot obj_id is stored in, and slot current value is stored in.  This was done for dark backgrounds.
# Input: pos_x, pos_y, label, storage_slot, value_slot
# Output: none
("gpu_create_checkbox_white",
		[
			(store_script_param, ":pos_x", 1),
			(store_script_param, ":pos_y", 2),
			(store_script_param, ":label", 3),
			(store_script_param, ":storage", 4),
			(store_script_param, ":val_slot", 5),
			
			# text
			(store_add, ":text_pos_x", ":pos_x", 20), (position_set_x, pos1, ":text_pos_x"),
			(store_add, ":text_pos_y", ":pos_y", 10),  (position_set_y, pos1, ":text_pos_y"),
			(create_text_overlay, reg1, ":label", tf_left_align|tf_vertical_align_center|tf_with_outline),
			(overlay_set_position, reg1, pos1),
			(overlay_set_color, reg1, gpu_white),
			# checkbox
			(store_add, ":checkbox_pos_x", ":pos_x", 0), (position_set_x, pos1, ":checkbox_pos_x"),
			(store_add, ":checkbox_pos_y", ":pos_y", 5), (position_set_y, pos1, ":checkbox_pos_y"),
			(create_check_box_overlay, reg1, "mesh_checkbox_off", "mesh_checkbox_on"),
			(overlay_set_position, reg1, pos1),
			(troop_set_slot, "$gpu_storage", ":storage", reg1),
			(troop_get_slot, ":setting", "$gpu_data", ":val_slot"),
			(overlay_set_val, reg1, ":setting"),
		]
	),
	
# script_gpu_resize_object
# Creates a mesh image based on troop ID, (x,y) position, size.
# Input: storage_id, pos_x, pos_y
# Output: none
("gpu_resize_object",
		[
			(store_script_param, ":object_slot", 1),
			(store_script_param, ":size", 2),
			
			(val_mul, ":size", 10),
			(troop_get_slot, ":obj", "$gpu_storage", ":object_slot"),
			(position_set_x, pos3, ":size"),
			(position_set_y, pos3, ":size"),
			(overlay_set_size, ":obj", pos3),
			
		]
	),
	
# script_gpu_change_color
# Changes the color of an object based on a storage_id & new color.
# Input: storage_id, pos_x, pos_y
# Output: none
("gpu_change_color",
		[
			(store_script_param, ":object_slot", 1),
			(store_script_param, ":color", 2),
			
			(troop_get_slot, ":obj", "$gpu_storage", ":object_slot"),
			(overlay_set_color, ":obj", ":color"),
			
		]
	),
	
# script_gpu_create_portrait
# Creates a mesh image based on troop ID, (x,y) position, size.
# Input: troop_id, pos_x, pos_y, size, storage_id
# Output: none
("gpu_create_portrait",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":pos_x", 2),
			(store_script_param, ":pos_y", 3),
			(store_script_param, ":size", 4),
			(store_script_param, ":storage", 5),
			
			(set_fixed_point_multiplier, 1000),
			(create_mesh_overlay_with_tableau_material, reg1, -1, "tableau_troop_note_mesh", ":troop_no"),
			(position_set_x, pos2, ":pos_x"),
			(position_set_y, pos2, ":pos_y"),
			(overlay_set_position, reg1, pos2),
			(position_set_x, pos3, ":size"),
			(position_set_y, pos3, ":size"),
			(overlay_set_size, reg1, pos3),
			(troop_set_slot, "$gpu_storage", ":storage", reg1),
		]
	),
	
# script_gpu_draw_line
# Modified from Custom Commander by Rubik.
# Inputs: horizontal size, vertical size, ( pos x, pos y), color code
	("gpu_draw_line",
	  [
		(store_script_param, ":size_x", 1),
		(store_script_param, ":size_y", 2),
		(store_script_param, ":pos_x", 3),
		(store_script_param, ":pos_y", 4),
		(store_script_param, ":color", 5),
		
		(create_mesh_overlay, reg1, "mesh_white_plane"),
		(val_mul, ":size_x", 50),
		(val_mul, ":size_y", 50),
		(position_set_x, pos1, ":size_x"),
		(position_set_y, pos1, ":size_y"),
		(overlay_set_size, reg1, pos1),
		(position_set_x, pos1, ":pos_x"),
		(position_set_y, pos1, ":pos_y"),
		(overlay_set_position, reg1, pos1),
		(overlay_set_color, reg1, ":color"),
		(troop_set_slot, "$gpu_storage", 0, reg1),
	]),
	
# script_gpu_container_heading
# Creates a container overlay based on troop ID, (x,y) position, size.
# Input: pos_x, pos_y, size_x, size_y, storage_id
# Output: none
("gpu_container_heading",
		[
			(store_script_param, ":pos_x", 1),
			(store_script_param, ":pos_y", 2),
			(store_script_param, ":size_x", 3),
			(store_script_param, ":size_y", 4),
			(store_script_param, ":storage", 5),
			
			(str_clear, s0),
			(create_text_overlay, reg1, s0, tf_scrollable_style_2),
			(position_set_x, pos1, ":pos_x"),
			(position_set_y, pos1, ":pos_y"),
			(overlay_set_position, reg1, pos1),
			(position_set_x, pos1, ":size_x"),
			(position_set_y, pos1, ":size_y"), 
			(overlay_set_area_size, reg1, pos1),
			(set_container_overlay, reg1),
			(troop_set_slot, "$gpu_storage", ":storage", reg1),
		]
	),
	
# script_gpu_create_checkbox     - pos_x, pos_y, label, storage_slot, value_slot
# script_gpu_create_mesh         - mesh_id, pos_x, pos_y, size_x, size_y
# script_gpu_create_portrait     - troop_id, pos_x, pos_y, size, storage_id
# script_gpu_create_button       - title, pos_x, pos_y, storage_id
# script_gpu_create_text_label   - title, pos_x, pos_y, storage_id, design
# script_gpu_resize_object       - storage_id, percent size
# script_gpu_draw_line           - x length, y length, pos_x, pos_y, color
# script_gpu_container_heading   - pos_x, pos_y, size_x, size_y, storage_id
# script_gpu_create_slider       - min, max, pos_x, pos_y, storage_id, value_id	
# script_gpu_change_color        - storage_id, color_id
("gpu_prsnt_panel_color_chooser",
		[
			(store_script_param, ":pos_x", 1),
			(store_script_param, ":pos_y", 2),
			
			(set_fixed_point_multiplier, 1000),
			
			(try_begin),
				(eq, "$gpu_ccp_mode", gpu_ccp_display),
				# Create borders
				(store_add, ":pos_x_right", ":pos_x", 220),
				
				# (assign, ":spacing_slider_to_text", 25),
				# (assign, ":spacing_text_to_slider", 43),
				(assign, ":spacing_slider_to_slider", 25),
				(store_add, ":x_labels", ":pos_x", 10),
				(store_sub, ":y_line_1", ":pos_y", 10), # Sample Text
				(store_sub, ":y_line_2", ":y_line_1", ":spacing_slider_to_slider"), # Menu
				(store_sub, ":y_line_3", ":y_line_2", ":spacing_slider_to_slider"), # Option 1 - text
				(store_sub, ":y_line_4", ":y_line_3", ":spacing_slider_to_slider"), # Option 1 - slider
				(store_sub, ":y_line_4_slider", ":y_line_4", 12),
				(store_sub, ":y_line_5", ":y_line_4", ":spacing_slider_to_slider"), # Option 2 - text
				(store_sub, ":y_line_5_slider", ":y_line_5", 12),
				(store_sub, ":y_line_6", ":y_line_5", ":spacing_slider_to_slider"), # Option 2 - slider
				(store_sub, ":y_line_6_slider", ":y_line_6", 12),
				(store_sub, ":y_line_7", ":y_line_6", ":spacing_slider_to_slider"), # Option 3 - text
				(store_sub, ":y_line_7_slider", ":y_line_7", 12),
				(store_sub, ":y_line_8", ":y_line_7", ":spacing_slider_to_slider"), # Option 3 - slider
				(store_sub, ":y_line_9", ":y_line_8", ":spacing_slider_to_slider"), # Output information
				(store_sub, ":y_line_9_slider", ":y_line_9", 12),
				(store_sub, ":y_line_10", ":y_line_9", ":spacing_slider_to_slider"), # Output information
				(store_sub, ":y_line_10_slider", ":y_line_10", 12),
				(store_sub, ":y_line_11", ":y_line_10", ":spacing_slider_to_slider"), # Output information
				(store_sub, ":y_line_12", ":y_line_11", ":spacing_slider_to_slider"), # Output information
				(store_sub, ":y_line_12_slider", ":y_line_12", 12),
				(store_sub, ":y_line_13", ":y_line_12", ":spacing_slider_to_slider"), # Output information
				(store_sub, ":y_line_13_slider", ":y_line_13", 12),
				
				(store_sub, ":y_buttons", ":y_line_13", 52),
				(store_sub, ":y_bottom", ":y_buttons", 10),
				(store_add, ":x_values", ":pos_x", 205), # 260
				# (store_add, ":x_output", ":pos_x", 135),
				(store_add, ":x_sliders", ":pos_x", 55),
				(store_sub, ":x_length", ":pos_x_right", ":pos_x"),
				(store_sub, ":y_length", ":pos_y", ":y_bottom"),
				(store_add, ":y_lengthR", ":y_length", 2),
				(call_script, "script_gpu_draw_line", ":x_length", ":y_length", ":pos_x", ":y_bottom", gpu_gray), # background
				(call_script, "script_gpu_draw_line", ":x_length", 2, ":pos_x", ":pos_y", gpu_black), # - Top
				(call_script, "script_gpu_draw_line", ":x_length", 2, ":pos_x", ":y_bottom", gpu_black), # - Bottom
				(call_script, "script_gpu_draw_line", 2, ":y_length", ":pos_x", ":y_bottom", gpu_black), # | Left
				(call_script, "script_gpu_draw_line", 2, ":y_lengthR", ":pos_x_right", ":y_bottom", gpu_black), # | Right
					
				# Line - 1 - Currently selected object
				(assign, reg0, "$gpu_object"),
				(call_script, "script_gpu_create_text_label", "str_kmt_reg0", ":x_values", ":y_line_1", gpu_obj_selected_object_text, gpu_right),
				(call_script, "script_gpu_resize_object", gpu_obj_selected_object_text, 50),
				(call_script, "script_gpu_create_text_label", "str_kmt_title_object_selected", ":x_labels", ":y_line_1", gpu_obj_selected_object_label, gpu_left),
				(call_script, "script_gpu_resize_object", gpu_obj_selected_object_label, 50),
				
				# Line - 2 - Current x,y position
				(mouse_get_position, pos1),
				(position_get_x, reg1, pos1),
				(position_get_y, reg2, pos1),
				(call_script, "script_gpu_create_text_label", "str_kmt_reg1_reg2_pos", ":x_values", ":y_line_2", gpu_obj_current_position, gpu_right),
				(call_script, "script_gpu_resize_object", gpu_obj_current_position, 50),
				(call_script, "script_gpu_create_text_label", "str_kmt_title_current_position", ":x_labels", ":y_line_2", gpu_obj_current_pos_label, gpu_left),
				(call_script, "script_gpu_resize_object", gpu_obj_current_pos_label, 50),
				
				# Line - 3 - RGB Text & Output Value
				(call_script, "script_gpu_create_text_label", "str_kmt_title_RGB", ":x_labels", ":y_line_3", gpu_obj_rgb_label, gpu_left),
				(call_script, "script_gpu_resize_object", gpu_obj_rgb_label, 50),
				(call_script, "script_gpu_create_text_label", "str_kmt_reg0", ":x_values", ":y_line_3", gpu_obj_output_text, gpu_right),
				(call_script, "script_gpu_merge_color"),
				(call_script, "script_gpu_resize_object", gpu_obj_output_text, 50),
				
				# Line - 4 - Red color slider
				(call_script, "script_gpu_create_slider", 0, 255, ":x_sliders", ":y_line_4_slider", gpu_obj_red_color_slider, gpu_val_foreground_red), # Red slider
				(call_script, "script_gpu_resize_object", gpu_obj_red_color_slider, 50),
				(troop_get_slot, reg0, "$gpu_storage", gpu_val_foreground_red),
				(call_script, "script_gpu_create_text_label", "str_kmt_reg0", ":x_values", ":y_line_4", gpu_obj_red_color_text, gpu_right),
				(call_script, "script_gpu_resize_object", gpu_obj_red_color_text, 50),
				(call_script, "script_gpu_create_text_label", "str_kmt_title_red", ":x_labels", ":y_line_4", gpu_obj_red_color_label, gpu_left),
				(call_script, "script_gpu_resize_object", gpu_obj_red_color_label, 50),
				
				# Line - 5 - Green color slider
				(call_script, "script_gpu_create_slider", 0, 255, ":x_sliders", ":y_line_5_slider", gpu_obj_green_color_slider, gpu_val_foreground_green), # Green slider
				(call_script, "script_gpu_resize_object", gpu_obj_green_color_slider, 50),
				(troop_get_slot, reg0, "$gpu_storage", gpu_val_foreground_green),
				(call_script, "script_gpu_create_text_label", "str_kmt_reg0", ":x_values", ":y_line_5", gpu_obj_green_color_text, gpu_right),
				(call_script, "script_gpu_resize_object", gpu_obj_green_color_text, 50),
				(call_script, "script_gpu_create_text_label", "str_kmt_title_green", ":x_labels", ":y_line_5", gpu_obj_green_color_label, gpu_left),
				(call_script, "script_gpu_resize_object", gpu_obj_green_color_label, 50),
				
				# Line - 6 - Blue color slider
				(call_script, "script_gpu_create_slider", 0, 255, ":x_sliders", ":y_line_6_slider", gpu_obj_blue_color_slider, gpu_val_foreground_blue), # Blue slider
				(call_script, "script_gpu_resize_object", gpu_obj_blue_color_slider, 50),
				(troop_get_slot, reg0, "$gpu_storage", gpu_val_foreground_blue),
				(call_script, "script_gpu_create_text_label", "str_kmt_reg0", ":x_values", ":y_line_6", gpu_obj_blue_color_text, gpu_right),
				(call_script, "script_gpu_resize_object", gpu_obj_blue_color_text, 50),
				(call_script, "script_gpu_create_text_label", "str_kmt_title_blue", ":x_labels", ":y_line_6", gpu_obj_blue_color_label, gpu_left),
				(call_script, "script_gpu_resize_object", gpu_obj_blue_color_label, 50),
				
				# Line - 7 - Transparency slider
				(call_script, "script_gpu_create_slider", 0, 255, ":x_sliders", ":y_line_7_slider", gpu_obj_transparency_slider, gpu_val_transparency), # Y slider
				(call_script, "script_gpu_resize_object", gpu_obj_transparency_slider, 50),
				(troop_get_slot, reg0, "$gpu_storage", gpu_val_transparency),
				(call_script, "script_gpu_create_text_label", "str_kmt_reg0", ":x_values", ":y_line_7", gpu_obj_transparency_text, gpu_right),
				(call_script, "script_gpu_resize_object", gpu_obj_transparency_text, 50),
				(call_script, "script_gpu_create_text_label", "str_kmt_title_alpha", ":x_labels", ":y_line_7", gpu_obj_transparency_label, gpu_left),
				(call_script, "script_gpu_resize_object", gpu_obj_transparency_label, 50),
				
				# Line - 8 - Movement label
				(call_script, "script_gpu_create_text_label", "str_kmt_title_movement", ":x_labels", ":y_line_8", gpu_obj_movement_label, gpu_left),
				(call_script, "script_gpu_resize_object", gpu_obj_movement_label, 50),
				
				# Line - 9 - X movement slider
				(call_script, "script_gpu_create_slider", 0, 1000, ":x_sliders", ":y_line_9_slider", gpu_obj_move_x_slider, gpu_val_movable_x), # X slider
				(call_script, "script_gpu_resize_object", gpu_obj_move_x_slider, 50),
				(troop_get_slot, reg0, "$gpu_storage", gpu_val_movable_x),
				(call_script, "script_gpu_create_text_label", "str_kmt_reg0", ":x_values", ":y_line_9", gpu_obj_move_x_text, gpu_right),
				(call_script, "script_gpu_resize_object", gpu_obj_move_x_text, 50),
				(call_script, "script_gpu_create_text_label", "str_kmt_title_x_pos", ":x_labels", ":y_line_9", gpu_obj_move_x_label, gpu_left),
				(call_script, "script_gpu_resize_object", gpu_obj_move_x_label, 50),
				
				# Line - 10 - Y movement slider
				(call_script, "script_gpu_create_slider", 0, 800, ":x_sliders", ":y_line_10_slider", gpu_obj_move_y_slider, gpu_val_movable_y), # Y slider
				(call_script, "script_gpu_resize_object", gpu_obj_move_y_slider, 50),
				(troop_get_slot, reg0, "$gpu_storage", gpu_val_movable_y),
				(call_script, "script_gpu_create_text_label", "str_kmt_reg0", ":x_values", ":y_line_10", gpu_obj_move_y_text, gpu_right),
				(call_script, "script_gpu_resize_object", gpu_obj_move_y_text, 50),
				(call_script, "script_gpu_create_text_label", "str_kmt_title_y_pos", ":x_labels", ":y_line_10", gpu_obj_move_y_label, gpu_left),
				(call_script, "script_gpu_resize_object", gpu_obj_move_y_label, 50),
				
				# Line - 11 - Resizing label
				(call_script, "script_gpu_create_text_label", "str_kmt_title_resizing", ":x_labels", ":y_line_11", gpu_obj_resizing_label, gpu_left),
				(call_script, "script_gpu_resize_object", gpu_obj_resizing_label, 50),
				
				# Line - 12 - X resize slider
				(call_script, "script_gpu_create_slider", 0, 300, ":x_sliders", ":y_line_12_slider", gpu_obj_resize_x_slider, gpu_val_resize_x), # X slider
				(call_script, "script_gpu_resize_object", gpu_obj_resize_x_slider, 50),
				(troop_get_slot, reg0, "$gpu_storage", gpu_val_movable_x),
				(call_script, "script_gpu_create_text_label", "str_kmt_reg0", ":x_values", ":y_line_12", gpu_obj_resize_x_text, gpu_right),
				(call_script, "script_gpu_resize_object", gpu_obj_resize_x_text, 50),
				(call_script, "script_gpu_create_text_label", "str_kmt_title_x_size", ":x_labels", ":y_line_12", gpu_obj_resize_x_label, gpu_left),
				(call_script, "script_gpu_resize_object", gpu_obj_resize_x_label, 50),
				
				# Line - 13 - Y resize slider
				(call_script, "script_gpu_create_slider", 0, 300, ":x_sliders", ":y_line_13_slider", gpu_obj_resize_y_slider, gpu_val_resize_y), # Y slider
				(call_script, "script_gpu_resize_object", gpu_obj_resize_y_slider, 50),
				(troop_get_slot, reg0, "$gpu_storage", gpu_val_movable_y),
				(call_script, "script_gpu_create_text_label", "str_kmt_reg0", ":x_values", ":y_line_13", gpu_obj_resize_y_text, gpu_right),
				(call_script, "script_gpu_resize_object", gpu_obj_resize_y_text, 50),
				(call_script, "script_gpu_create_text_label", "str_kmt_title_y_size", ":x_labels", ":y_line_13", gpu_obj_resize_y_label, gpu_left),
				(call_script, "script_gpu_resize_object", gpu_obj_resize_y_label, 50),
				
				# Line - 14 - Undo Button
				(call_script, "script_gpu_create_button", "str_kmt_undo", ":x_labels", ":y_buttons", gpu_obj_undo_button),
				
				# Line - 15 - Hide Button
				(store_add, ":pos_x_hide", ":pos_x", 152),
				(call_script, "script_gpu_create_button", "str_kmt_hide", ":pos_x_hide", ":y_buttons", gpu_obj_hide_button), # 238, 140
			(else_try),
				(call_script, "script_gpu_create_button", "str_kmt_show", ":pos_x_hide", ":y_buttons", gpu_obj_show_button), # 238, 140
				(position_set_x, pos1, 50),
				(position_set_y, pos1, 50),
				(overlay_set_position, reg1, pos1),
			(try_end),
		]
	),

("gpu_events_panel_color_chooser",
		[
			(store_script_param, ":object", 1),
			(store_script_param, ":value", 2),
			(assign, ":request_restart", 0),
			(troop_set_slot, "$gpu_storage", 0, "$gpu_object"),
			
			(try_begin), ### SLIDER 4 - Font Color ###
				(troop_slot_eq, "$gpu_storage", gpu_obj_red_color_slider, ":object"),
				(troop_set_slot, "$gpu_storage", gpu_val_foreground_red, ":value"),
				(call_script, "script_gpu_merge_color"),
				(call_script, "script_gpu_change_color", 0, reg0),
				(assign, reg1, ":value"),
				(troop_get_slot, ":obj_text", "$gpu_storage", gpu_obj_red_color_text),
				(overlay_set_text, ":obj_text", "@{reg1}"),
			
			(else_try), ### SLIDER 5 - Font Color ###
				(troop_slot_eq, "$gpu_storage", gpu_obj_green_color_slider, ":object"),
				(troop_set_slot, "$gpu_storage", gpu_val_foreground_green, ":value"),
				(call_script, "script_gpu_merge_color"),
				(call_script, "script_gpu_change_color", 0, reg0), # gpu_obj_sample_text_foreground
				(assign, reg1, ":value"),
				(troop_get_slot, ":obj_text", "$gpu_storage", gpu_obj_green_color_text),
				(overlay_set_text, ":obj_text", "@{reg1}"),
			
			(else_try), ### SLIDER 6 - Font Color ###
				(troop_slot_eq, "$gpu_storage", gpu_obj_blue_color_slider, ":object"),
				(troop_set_slot, "$gpu_storage", gpu_val_foreground_blue, ":value"),
				(call_script, "script_gpu_merge_color"),
				(call_script, "script_gpu_change_color", 0, reg0), # gpu_obj_sample_text_foreground
				(assign, reg1, ":value"),
				(troop_get_slot, ":obj_text", "$gpu_storage", gpu_obj_blue_color_text),
				(overlay_set_text, ":obj_text", "@{reg1}"),
			
			(else_try), ### SLIDER 7 - Transparency ###
				(troop_slot_eq, "$gpu_storage", gpu_obj_transparency_slider, ":object"),
				(troop_set_slot, "$gpu_storage", gpu_val_transparency, ":value"),
				(troop_get_slot, ":obj_target", "$gpu_storage", 0), # gpu_obj_sample_text_background
				(overlay_set_alpha, ":obj_target", ":value"),
				(assign, reg1, ":value"),
				(troop_get_slot, ":obj_text", "$gpu_storage", gpu_obj_transparency_text),
				(overlay_set_text, ":obj_text", "@{reg1}"),
			
			(else_try), ### SLIDER 9 - Moving X Axis ###
				(troop_slot_eq, "$gpu_storage", gpu_obj_move_x_slider, ":object"),
				(troop_set_slot, "$gpu_storage", gpu_val_movable_x, ":value"),
				(position_set_x, pos1, ":value"),
				(troop_get_slot, ":pos_y", "$gpu_storage", gpu_val_movable_y),
				(position_set_y, pos1, ":pos_y"),
				(overlay_set_position, "$gpu_object", pos1),
				(assign, reg1, ":value"),
				(troop_get_slot, ":obj_text", "$gpu_storage", gpu_obj_move_x_text),
				(overlay_set_text, ":obj_text", "@{reg1}"),
			
			(else_try), ### SLIDER 10 - Moving Y Axis ###
				(troop_slot_eq, "$gpu_storage", gpu_obj_move_y_slider, ":object"),
				(troop_set_slot, "$gpu_storage", gpu_val_movable_y, ":value"),
				(position_set_y, pos1, ":value"),
				(troop_get_slot, ":pos_x", "$gpu_storage", gpu_val_movable_x),
				(position_set_x, pos1, ":pos_x"),
				(overlay_set_position, "$gpu_object", pos1),
				(assign, reg1, ":value"),
				(troop_get_slot, ":obj_text", "$gpu_storage", gpu_obj_move_y_text),
				(overlay_set_text, ":obj_text", "@{reg1}"),
				
			(else_try), ### SLIDER 12 - Resizing X Axis ###
				(troop_slot_eq, "$gpu_storage", gpu_obj_resize_x_slider, ":object"),
				(troop_set_slot, "$gpu_storage", gpu_val_movable_x, ":value"),
				(store_mul, ":pos_x", ":value", 10),
				(position_set_x, pos1, ":pos_x"),
				(troop_get_slot, ":pos_y", "$gpu_storage", gpu_val_resize_y),
				(val_mul, ":pos_y", 10),
				(position_set_y, pos1, ":pos_y"),
				(overlay_set_size, "$gpu_object", pos1),
				(assign, reg1, ":value"),
				(troop_get_slot, ":obj_text", "$gpu_storage", gpu_obj_resize_x_text),
				(overlay_set_text, ":obj_text", "@{reg1}"),
			
			(else_try), ### SLIDER 13 - Resizing Y Axis ###
				(troop_slot_eq, "$gpu_storage", gpu_obj_resize_y_slider, ":object"),
				(troop_set_slot, "$gpu_storage", gpu_val_movable_y, ":value"),
				(store_mul, ":pos_y", ":value", 10),
				(position_set_y, pos1, ":pos_y"),
				(troop_get_slot, ":pos_x", "$gpu_storage", gpu_val_resize_x),
				(val_mul, ":pos_x", 10),
				(position_set_x, pos1, ":pos_x"),
				(overlay_set_size, "$gpu_object", pos1),
				(assign, reg1, ":value"),
				(troop_get_slot, ":obj_text", "$gpu_storage", gpu_obj_resize_y_text),
				(overlay_set_text, ":obj_text", "@{reg1}"),
			
			(else_try), ### Hide Button ###
				(troop_slot_eq, "$gpu_storage", gpu_obj_hide_button, ":object"),
				(assign, "$gpu_ccp_mode", gpu_ccp_hide),
				(assign, ":request_restart", 1),
			
			(else_try), ### Show Button ###
				(troop_slot_eq, "$gpu_storage", gpu_obj_show_button, ":object"),
				(assign, "$gpu_ccp_mode", gpu_ccp_display),
				(assign, ":request_restart", 1),
			
			(else_try), ### Undo Button ###
				(troop_slot_eq, "$gpu_storage", gpu_obj_undo_button, ":object"),
				(assign, ":request_restart", 1),
			
			(try_end),
			
			
			(assign, reg0, ":request_restart"),
		]
	),
	
# script_gpu_mouseclick_panel_color_chooser
# Creates a mesh image based on mesh ID, (x,y) position, (x,y) size.
# Input: mesh_id, pos_x, pos_y, size_x, size_y
# Output: none
("gpu_mouseclick_panel_color_chooser",
		[
			(store_script_param, ":object", 1),
			(store_script_param, ":value", 2),
			
			(try_begin),
				(neq, "$gpu_ccp_mode", gpu_ccp_hide),
				(mouse_get_position, pos1),
				(position_get_x, reg1, pos1),
				(position_get_y, reg2, pos1),
				(troop_get_slot, ":obj_target", "$gpu_storage", gpu_obj_current_position),
				(overlay_set_text, ":obj_target", "@( {reg1}, {reg2} )"),
				(eq, ":value", 1), # Right button click
				(assign, "$gpu_object", ":object"),
				(troop_set_slot, "$gpu_storage", 0, ":object"),
				(troop_get_slot, ":obj_target", "$gpu_storage", gpu_obj_selected_object_text),
				(assign, reg1, "$gpu_object"),
				(overlay_set_text, ":obj_target", "@{reg1}"),
				(troop_set_slot, "$gpu_storage", gpu_val_resize_x, 100),
				(troop_set_slot, "$gpu_storage", gpu_val_resize_y, 100),
				(overlay_get_position, pos2, ":object"),
				(position_get_x, reg1, pos2),
				(position_get_y, reg2, pos2),
				(troop_set_slot, "$gpu_storage", gpu_val_movable_x, reg1),
				(troop_set_slot, "$gpu_storage", gpu_val_movable_y, reg2),
				(troop_get_slot, ":obj_x", "$gpu_storage", gpu_obj_move_x_slider),
				(troop_get_slot, ":obj_x_text", "$gpu_storage", gpu_obj_move_x_text),
				(overlay_set_val, ":obj_x", reg1),
				(overlay_set_text, ":obj_x_text", "@{reg1}"),
				
				(troop_get_slot, ":obj_y", "$gpu_storage", gpu_obj_move_y_slider),
				(troop_get_slot, ":obj_y_text", "$gpu_storage", gpu_obj_move_y_text),
				(overlay_set_val, ":obj_y", reg2),
				(overlay_set_text, ":obj_y_text", "@{reg2}"),
				
			(try_end),
		]
	),
	
("gpu_merge_color",
		[
			(troop_get_slot, ":red", "$gpu_storage", gpu_val_foreground_red),
			(troop_get_slot, ":green", "$gpu_storage", gpu_val_foreground_green),
			(troop_get_slot, ":blue", "$gpu_storage", gpu_val_foreground_blue),
						
			(store_div, ":red_1", ":red", 16),
			(store_mod, ":red_2", ":red", 16),
			
			(store_div, ":green_1", ":green", 16),
			(store_mod, ":green_2", ":green", 16),
			
			(store_div, ":blue_1", ":blue", 16),
			(store_mod, ":blue_2", ":blue", 16),
			
			(assign, ":color", 0),
			(val_add, ":color", ":blue_2"), # Adds in first character -----X
			(store_mul, ":char_2", ":blue_1", 16), # 16 = 16^1
			(val_add, ":color", ":char_2"), # Adds in second character ----X-
			(store_mul, ":char_3", ":green_2", 256), # 256 = 16^2
			(val_add, ":color", ":char_3"), # Adds in third character ---X--
			(store_mul, ":char_4", ":green_1", 4096), # 4096 = 16^3
			(val_add, ":color", ":char_4"), # Adds in third character --X---
			(store_mul, ":char_5", ":red_2", 65536), # 65536 = 16^4
			(val_add, ":color", ":char_5"), # Adds in third character -X----
			(store_mul, ":char_6", ":red_1", 1048576), # 1048576 = 16^5
			(val_add, ":color", ":char_6"), # Adds in third character -X----
			
			(assign, reg0, ":color"),

			(troop_get_slot, ":obj_output", "$gpu_storage", gpu_obj_output_text),
			(overlay_set_text, ":obj_output", "@{reg0}"),

		]
	),
	
]


from util_wrappers import *
from util_scripts import *

                
def modmerge_scripts(orig_scripts):
	# process script directives first
	# process_script_directives(orig_scripts, scripts_directives)
	# add remaining scripts
	add_scripts(orig_scripts, scripts, True)
	
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "scripts"
        orig_scripts = var_set[var_name_1]
    
        
		# START do your own stuff to do merging
		
        modmerge_scripts(orig_scripts)

		# END do your own stuff
        
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)