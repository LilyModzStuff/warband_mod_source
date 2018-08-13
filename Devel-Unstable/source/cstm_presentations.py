import collections

import module_skills

from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from header_items import *
from module_constants import *
import string

from cstm_header_presentations import *

####################################################################################################################
#	Each presentation record contains the following fields:
#	1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#	2) Presentation flags. See header_presentations.py for a list of available flags
#	3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#	4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

ACTIVE_FIGHTING_SKILLS = [skill for skill in module_skills.skills if skill[2] & sf_inactive == 0 and skill[2] & 0xf in (ca_strength, ca_agility)]
#print "\n".join([skill[1] for skill in ACTIVE_FIGHTING_SKILLS])

CSTM_INV_SLOT_SIZE = 80
CSTM_INV_CONT_WIDTH = 3
CSTM_INV_CONT_HEIGHT = 4

CSTM_INV_POS_X = 40
CSTM_INV_POS_Y = 50

CSTM_NAME_POS_X = CSTM_INV_POS_X
CSTM_NAME_POS_Y = 685
CSTM_NAME_LABEL_WIDTH = 125
CSTM_NAME_GAP = 340

CSTM_STORE_SLOT_SIZE = 80
CSTM_STORE_CONT_WIDTH = 3
CSTM_STORE_CONT_HEIGHT = 7

CSTM_STORE_POS_X = CSTM_INV_POS_X + CSTM_INV_SLOT_SIZE * CSTM_INV_CONT_WIDTH + 45
CSTM_STORE_POS_Y = CSTM_INV_POS_Y

CSTM_STATS_POS_X = CSTM_STORE_POS_X + CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_WIDTH + 35
CSTM_STATS_POS_Y = 0

CSTM_STATS_SIZE_X = 960 - CSTM_STATS_POS_X
CSTM_STATS_SIZE_Y = CSTM_STORE_CONT_HEIGHT * CSTM_STORE_SLOT_SIZE + CSTM_STORE_POS_Y - CSTM_STATS_POS_Y - 15

CSTM_STATS_ATTR_TEXT_SIZE = 1000
CSTM_STATS_ATTR_ROW_HEIGHT = 27
CSTM_STATS_ATTR_COL_WIDTH = 185
CSTM_STATS_ATTR_CONT_WIDTH = 2
CSTM_STATS_ATTR_SECTION_HEIGHT = int((((attributes_end - 1) / CSTM_STATS_ATTR_CONT_WIDTH)) + 1) * CSTM_STATS_ATTR_ROW_HEIGHT

CSTM_STATS_PROF_TEXT_SIZE = 950
CSTM_STATS_PROF_ROW_HEIGHT = 27
CSTM_STATS_PROF_COL_WIDTH = 185
CSTM_STATS_PROF_CONT_WIDTH = 2
CSTM_STATS_PROF_SECTION_HEIGHT = int((((proficiencies_end - 1) / CSTM_STATS_PROF_CONT_WIDTH)) + 1) * CSTM_STATS_PROF_ROW_HEIGHT

CSTM_STATS_SKL_TEXT_SIZE = 900
CSTM_STATS_SKL_ROW_HEIGHT = 27
CSTM_STATS_SKL_COL_WIDTH = 185
CSTM_STATS_SKL_CONT_WIDTH = 2
CSTM_STATS_SKL_SECTION_HEIGHT = int((((len(ACTIVE_FIGHTING_SKILLS) - 1) / CSTM_STATS_SKL_CONT_WIDTH)) + 1) * CSTM_STATS_SKL_ROW_HEIGHT

CSTM_STATS_POINTS_TEXT_SIZE = 900
CSTM_STATS_POINTS_ROW_HEIGHT = 25
CSTM_STATS_POINTS_COL_WIDTH = 185
CSTM_STATS_POINTS_SECTION_HEIGHT = 2 * CSTM_STATS_POINTS_ROW_HEIGHT

CSTM_STATS_GAP_Y = 40

CSTM_BUTTONS_POS_X = 800
CSTM_BUTTONS_POS_Y = CSTM_NAME_POS_Y
CSTM_BUTTONS_SIZE_X = 100
CSTM_BUTTONS_SIZE_Y = 30
CSTM_BUTTONS_GAP = 20

CSTM_TREE_TITLE_SIZE = 2000
CSTM_TREE_TITLE_POS_X = 50
CSTM_TREE_TITLE_POS_Y = 650

CSTM_TREE_POS_X = 100
CSTM_TREE_POS_Y = 75
CSTM_TREE_X_RIGHT_PADDING = 150

CSTM_TREE_X_OFFSET = 170
CSTM_TREE_Y_OFFSET = 145

CSTM_PREFIX_LABEL_POS_X = CSTM_TREE_TITLE_POS_X
CSTM_PREFIX_LABEL_WIDTH = 75
CSTM_PREFIX_POS_Y = 590

new_presentations = [

	("cstm_start_name_kingdom", 0, mesh_load_window, [
		(ti_on_presentation_load,
		[
			(set_fixed_point_multiplier, 1000),
			(call_script, "script_gpu_create_text_overlay", "str_name_kingdom_text", 500, 450, 1000, 500, 50, tf_center_justify),
			
			(str_store_troop_name, s0, "trp_player"),
			(str_store_string, s7, "str_default_kingdom_name"),
			(call_script, "script_gpu_create_text_box_overlay", "str_default_kingdom_name", 400, 400),
			(assign, "$g_presentation_obj_name_kingdom_1", reg1),
			
			(str_store_string, s0, "@Continue..."),
			(call_script, "script_gpu_create_game_button_overlay", "str_s0", 500, 300),
			(assign, "$g_presentation_obj_name_kingdom_2", reg1),
			
			(presentation_set_duration, 999999),
		]),
		
		(ti_on_presentation_event_state_change,
		[
			(store_trigger_param_1, ":object"),
			(try_begin),
				(eq, ":object", "$g_presentation_obj_name_kingdom_1"),
				
				(str_store_string, s7, s0),
			(else_try),
				(eq, ":object", "$g_presentation_obj_name_kingdom_2"),
				
				(faction_set_name, "fac_player_supporters_faction", s7),
				(faction_set_color, "fac_player_supporters_faction", 0xFF0000),
				(assign, "$players_kingdom_name_set", 1),
				
				(presentation_set_duration, 0),
				(jump_to_menu, "mnu_cstm_choose_troop_tree"),
			(try_end),
		]),
	]),
	
	("cstm_view_custom_troop_tree", 0, mesh_load_window,
	[
		## INITIALISE VARIABLES
		(ti_on_presentation_load,
		[
			(try_for_range, ":overlay_id", 0, 9999),
				(troop_set_slot, "trp_cstm_overlay_troops", ":overlay_id", -1),
			(try_end),
			(assign, "$cstm_customise_button", -1),
			(assign, "$cstm_finalise_button", -1),
			
			(try_for_range, ":custom_troop", cstm_troops_begin, cstm_troops_end),
				(call_script, "script_cstm_troop_refresh_name", ":custom_troop"),
			(try_end),
			
			## TITLE
			(str_store_faction_name, s0, "fac_player_supporters_faction"),
			(str_store_string, s0, "@{s0} Troop Tree"),
			(call_script, "script_gpu_create_text_overlay", "str_s0", CSTM_TREE_TITLE_POS_X, CSTM_TREE_TITLE_POS_Y, CSTM_TREE_TITLE_SIZE, 900, 50, tf_left_align),
			
			## PREFIX
			(str_store_string, s0, "@Prefix: "),
      (call_script, "script_gpu_create_text_overlay", "str_s0", CSTM_PREFIX_LABEL_POS_X, CSTM_PREFIX_POS_Y, 1000, CSTM_PREFIX_LABEL_WIDTH, 50, tf_left_align),
      
      (str_store_troop_name, s0, cstm_troop_tree_prefix),
      (call_script, "script_gpu_create_text_box_overlay", "str_s0", CSTM_PREFIX_LABEL_POS_X + CSTM_PREFIX_LABEL_WIDTH, CSTM_PREFIX_POS_Y),
      (assign, "$cstm_set_prefix", reg1),
			
			## TREE VIEWER
			(store_sub, ":num_splits", "$cstm_num_tiers", 1),
			(store_div, ":offset_x", 1000 - (CSTM_TREE_POS_X + CSTM_TREE_X_RIGHT_PADDING), ":num_splits"),
			(call_script, "script_cstm_create_troop_tree_images", "$cstm_troops_begin", CSTM_TREE_POS_X, CSTM_TREE_POS_Y, ":offset_x", CSTM_TREE_Y_OFFSET, 0),
			
			## EXIT BUTTON
			(str_store_string, s0, "@Exit"),
			(call_script, "script_gpu_create_game_button_overlay", "str_s0", CSTM_BUTTONS_POS_X + CSTM_BUTTONS_SIZE_X + CSTM_BUTTONS_GAP - 50, CSTM_BUTTONS_POS_Y - 10),
			(assign, "$cstm_customise_troop_exit", reg1),
			#(position_set_x, pos1, CSTM_BUTTONS_SIZE_X),
			#(position_set_y, pos1, CSTM_BUTTONS_SIZE_Y),
			#(overlay_set_size, "$cstm_customise_troop_exit", pos1),
			
			(presentation_set_duration, 999999),
		]),
		
		(ti_on_presentation_event_state_change,
		[
			(store_trigger_param_1, ":object"),
			#(store_trigger_param_2, ":value"),
			
			(try_begin),
				(troop_get_slot, ":troop", "trp_cstm_overlay_troops", ":object"),
				(gt, ":troop", 0),
				
				#(str_store_troop_name, s0, ":troop"),
				#(display_message, "@{s0} pressed"),
				(assign, "$cstm_troop_being_customised", ":troop"),
				
				# Back up name so that it can be restored in the event of resetting changes
				(troop_get_slot, ":dummy", ":troop", cstm_slot_troop_dummy),
				(str_store_troop_name, s0, ":dummy"),
				(troop_set_name, "$cstm_presentation_troop", s0),
				(str_store_troop_name_plural, s0, ":dummy"),
				(troop_set_plural_name, "$cstm_presentation_troop", s0),
				
				(start_presentation, "prsnt_cstm_customise_troop"),
			(else_try),
				## PREFIX CHANGED
				(eq, ":object", "$cstm_set_prefix"),
				
				(troop_set_name, cstm_troop_tree_prefix, s0),
				(start_presentation, "prsnt_cstm_view_custom_troop_tree"),
			(else_try),
				## EXIT BUTTON PRESSED
				(eq, ":object", "$cstm_customise_troop_exit"),
				
				(change_screen_return),
				(presentation_set_duration, 0),
			(try_end),
		]),
	]),
	
	("cstm_customise_troop", 0, mesh_load_window,
	[
		(ti_on_presentation_load,
		[
			## INITIALISE VARIABLES
			(assign, "$cstm_item_details_overlay", -1),
			(assign, "$cstm_customise_troop_save", -1),
			(assign, "$cstm_customise_troop_reset", -1),
			(assign, "$cstm_customise_troop_exit", -1),
			(troop_get_slot, "$cstm_item_type_selected", "$cstm_items_array", cstm_slot_array_item_type),
			(try_for_range, ":overlay_id", 0, 9999),
				(troop_set_slot, "trp_cstm_overlay_items", ":overlay_id", -1),
				(troop_set_slot, "trp_cstm_overlay_is_store_item", ":overlay_id", 0),
				(troop_set_slot, "trp_cstm_overlay_is_attribute_box", ":overlay_id", 0),
				(troop_set_slot, "trp_cstm_overlay_is_proficiency_box", ":overlay_id", 0),
				(troop_set_slot, "trp_cstm_overlay_is_skill_box", ":overlay_id", 0),
				(troop_set_slot, "trp_cstm_overlay_attribute", ":overlay_id", -1),
				(troop_set_slot, "trp_cstm_overlay_proficiency", ":overlay_id", -1),
				(troop_set_slot, "trp_cstm_overlay_skill", ":overlay_id", -1),
			(try_end),
			
			(troop_get_slot, ":dummy", "$cstm_troop_being_customised", cstm_slot_troop_dummy),
			
			(store_character_level, ":troop_level", "$cstm_troop_being_customised"),
			(troop_get_slot, "$cstm_total_funds", "trp_cstm_inventory_values", ":troop_level"),
			
			## TROOP IMAGE
			(call_script, "script_cstm_troop_copy_inventory", "$cstm_presentation_troop", ":dummy"),
			(troop_sort_inventory, "$cstm_presentation_troop"),
			(troop_equip_items, "$cstm_presentation_troop"),
			(call_script, "script_gpu_create_troop_image", "$cstm_presentation_troop", -25, 350, 1250),
			(assign, "$cstm_troop_image", reg1),
			
			## TROOP INVENTORY
			(call_script, "script_gpu_create_scrollable_container", CSTM_INV_POS_X, CSTM_INV_POS_Y, CSTM_INV_SLOT_SIZE * CSTM_INV_CONT_WIDTH, CSTM_INV_SLOT_SIZE * CSTM_INV_CONT_HEIGHT),
			(assign, "$cstm_troop_inventory_container", reg1),
			
			(set_container_overlay, "$cstm_troop_inventory_container"),
			
			(try_for_range, ":item_slot", 0, num_equipment_kinds),
				(troop_get_inventory_slot, ":item", ":dummy", ":item_slot"),
				(troop_get_inventory_slot_modifier, ":imod", ":dummy", ":item_slot"),
				(gt, ":item", 0),
				
				(troop_add_item, ":dummy", ":item", ":imod"),
				(troop_set_inventory_slot, ":dummy", ":item_slot", -1),
			(try_end),
			
			(troop_get_inventory_capacity, ":capacity", ":dummy"),
			(val_sub, ":capacity", num_equipment_kinds),
			(try_for_range, ":item_index", 0, ":capacity"),
				(store_add, ":item_slot", ":item_index", num_equipment_kinds),
				(troop_get_inventory_slot, ":item", ":dummy", ":item_slot"),
				
				#(store_mod, ":x", ":item_index", CSTM_INV_CONT_WIDTH),
				#(store_mul, ":pos_x", ":x", CSTM_INV_SLOT_SIZE),
				
				#(store_sub, ":row", ":item_index", ":x"),
				#(val_div, ":row", CSTM_INV_CONT_WIDTH),
				#(store_div, ":num_rows", ":capacity", CSTM_INV_CONT_WIDTH),
				#(store_sub, ":pos_y", ":num_rows", ":row"),
				#(val_sub, ":pos_y", 1),
				#(val_mul, ":pos_y", CSTM_INV_SLOT_SIZE),
				
				(call_script, "script_cstm_get_grid_position", ":item_index", ":capacity", CSTM_INV_CONT_WIDTH, CSTM_INV_SLOT_SIZE, CSTM_INV_SLOT_SIZE),
				(assign, ":pos_x", reg0),
				(assign, ":pos_y", reg1),
				
				#(try_begin),
				#	(gt, ":item", 0),
				#	(str_store_item_name, s0, ":item"),
				#	(assign, reg0, ":item_index"),
				#	(assign, reg1, ":pos_x"),
				#	(assign, reg2, ":pos_y"),
				#	(display_message, "@Slot {reg0}: {s0}. pos_x: {reg1}, pos_y: {reg2}"),
				#(try_end),
				
				(call_script, "script_gpu_create_mesh_overlay", "mesh_inv_slot", ":pos_x", ":pos_y", CSTM_INV_SLOT_SIZE * 10, CSTM_INV_SLOT_SIZE * 10),
				(gt, ":item", 0),
				
				(troop_set_slot, "trp_cstm_overlay_items", reg1, ":item_slot"),
				
				(store_add, ":item_x", ":pos_x", CSTM_INV_SLOT_SIZE / 2),
				(store_add, ":item_y", ":pos_y", CSTM_INV_SLOT_SIZE / 2),
				(call_script, "script_gpu_create_item_overlay", ":item", ":item_x", ":item_y", CSTM_INV_SLOT_SIZE * 10),
			(try_end),
			
			(set_container_overlay, -1),
			
			(str_store_string, s0, "@Right-click to remove"),
      (call_script, "script_gpu_create_text_overlay", "str_s0", CSTM_INV_POS_X, CSTM_INV_POS_Y - 28, 1000, CSTM_INV_SLOT_SIZE * CSTM_INV_CONT_WIDTH, 20, tf_left_align),
			(assign, "$cstm_remove_from_inventory_message", reg1),
			(overlay_set_display, "$cstm_remove_from_inventory_message", 0),
			
			## STORE ITEM TYPE AND MODIFIER SELECTIONS
			#(str_store_string, s0, "@Select an item type:"),
      #(call_script, "script_gpu_create_text_overlay", "str_s0", CSTM_STORE_POS_X, CSTM_STORE_POS_Y + CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_HEIGHT + 20, 1200, CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_WIDTH, 50, tf_left_align),
			
			(call_script, "script_gpu_create_combo_button_overlay", CSTM_STORE_POS_X + CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_WIDTH + 135, CSTM_STORE_POS_Y + CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_HEIGHT + 20),
			(assign, "$cstm_store_item_type_selector", reg1),
			(position_set_x, pos1, 750),
			(position_set_y, pos1, 750),
			(overlay_set_size, "$cstm_store_item_type_selector", pos1),
			# The items for this combo button are added in the modmerge function
			
			(call_script, "script_gpu_create_combo_button_overlay", CSTM_STORE_POS_X + CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_WIDTH + 345, CSTM_STORE_POS_Y + CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_HEIGHT + 20),
			(assign, "$cstm_store_item_modifier_selector", reg1),
			(position_set_x, pos1, 750),
			(position_set_y, pos1, 750),
			(overlay_set_size, "$cstm_store_item_modifier_selector", pos1),
			
			(assign, ":count", 0),
			(try_for_range, ":imod", imod_plain, imod_large_bag+1),
				## Filter for appropriate IMODs based on item type.
				(store_add, ":modifier_string", modifier_strings_begin, ":imod"),
				#(display_message, ":modifier_string"),
				(call_script, "script_cf_cci_imod_appropriate_for_item", "$cstm_item_type_selected", ":imod"),
				
				#(str_store_string, s0, ":modifier_string"),
				#(str_store_string, s0, "@{s0} ACCEPTED"),
				(overlay_add_item, "$cstm_store_item_modifier_selector", ":modifier_string"),
				
				(try_begin),
					(eq, ":imod", "$cstm_item_modifier_selected"),
					
					(overlay_set_val, "$cstm_store_item_modifier_selector", ":count"),
				(try_end),
				
				(val_add, ":count", 1),
			(try_end),
			
			## STORE ITEMS
      #(call_script, "script_gpu_create_text_overlay", "str_s0", CSTM_STORE_POS_X + (CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_WIDTH) / 2, CSTM_STORE_POS_Y + CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_HEIGHT + 15, 1200, CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_WIDTH, 20, tf_center_justify),
			(call_script, "script_gpu_create_combo_label_overlay", CSTM_STORE_POS_X + (CSTM_STORE_SLOT_SIZE * (CSTM_STORE_CONT_WIDTH + 1)) / 2, CSTM_STORE_POS_Y + CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_HEIGHT + 15),
			(assign, "$cstm_item_page_selector", reg1),
			(position_set_x, pos1, 750),
			(position_set_y, pos1, 1000),
			(overlay_set_size, "$cstm_item_page_selector", pos1),
			
			(troop_get_slot, ":num_items", "$cstm_items_array", cstm_slot_array_num_items),
			(store_add, ":num_pages", ":num_items", CSTM_STORE_CONT_WIDTH * CSTM_STORE_CONT_HEIGHT - 1),
			(val_div, ":num_pages", CSTM_STORE_CONT_WIDTH * CSTM_STORE_CONT_HEIGHT),
			
			(try_for_range, ":page_no", 0, ":num_pages"),
				(store_add, reg0, ":page_no", 1),
				(assign, reg1, ":num_pages"),
				(str_store_string, s0, "@Items page {reg0} / {reg1}"),
				(overlay_add_item, "$cstm_item_page_selector", s0),
			(try_end),
			(overlay_set_val, "$cstm_item_page_selector", "$cstm_item_page_no"),
			
			(call_script, "script_gpu_create_scrollable_container", CSTM_STORE_POS_X, CSTM_STORE_POS_Y, CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_WIDTH, CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_HEIGHT),
			(assign, "$cstm_store_container", reg1),
			
			(set_container_overlay, "$cstm_store_container"),
			
			(try_for_range, ":slot_no", 0, CSTM_STORE_CONT_WIDTH * CSTM_STORE_CONT_HEIGHT),
				(store_mul, ":offset", "$cstm_item_page_no", CSTM_STORE_CONT_WIDTH * CSTM_STORE_CONT_HEIGHT),
				(store_add, ":item_index", ":slot_no", ":offset"),
				(call_script, "script_cstm_get_item_from_array", "$cstm_items_array", ":item_index"),
				(assign, ":item", reg0),
				
				#(store_mod, ":x", ":slot_no", CSTM_STORE_CONT_WIDTH),
				#(store_mul, ":pos_x", ":x", CSTM_STORE_SLOT_SIZE),
				
				#(store_sub, ":row", ":slot_no", ":x"),
				#(val_div, ":row", CSTM_STORE_CONT_WIDTH),
				#(store_div, ":num_rows", ":num_items", CSTM_STORE_CONT_WIDTH),
				#(store_sub, ":pos_y", ":num_rows", ":row"),
				#(val_sub, ":pos_y", 1),
				#(val_mul, ":pos_y", CSTM_STORE_SLOT_SIZE),
				
				(call_script, "script_cstm_get_grid_position", ":slot_no", CSTM_STORE_CONT_WIDTH * CSTM_STORE_CONT_HEIGHT, CSTM_STORE_CONT_WIDTH, CSTM_STORE_SLOT_SIZE, CSTM_STORE_SLOT_SIZE),
				(assign, ":pos_x", reg0),
				(assign, ":pos_y", reg1),
				
				#(try_begin),
				#	(gt, ":item", 0),
				#	(str_store_item_name, s0, ":item"),
				#	(assign, reg0, ":slot_no"),
				#	(assign, reg1, ":pos_x"),
				#	(assign, reg2, ":pos_y"),
				#	(display_message, "@Slot {reg0}: {s0}. pos_x: {reg1}, pos_y: {reg2}"),
				#(try_end),
				
				(call_script, "script_gpu_create_mesh_overlay", "mesh_inv_slot", ":pos_x", ":pos_y", CSTM_STORE_SLOT_SIZE * 10, CSTM_STORE_SLOT_SIZE * 10),
				(troop_set_slot, "trp_cstm_overlay_items", reg1, ":item"),
				(troop_set_slot, "trp_cstm_overlay_is_store_item", reg1, 1),
				
				(gt, ":item", 0),
				
				(store_add, ":item_x", ":pos_x", CSTM_STORE_SLOT_SIZE / 2),
				(store_add, ":item_y", ":pos_y", CSTM_STORE_SLOT_SIZE / 2),
				(call_script, "script_gpu_create_item_overlay", ":item", ":item_x", ":item_y", CSTM_STORE_SLOT_SIZE * 10),
			(try_end),
			
			(set_container_overlay, -1),
			
			## AVAILABLE FUNDS
			(str_store_string, s0, "@Remaining funds:"),
      (call_script, "script_gpu_create_text_overlay", "str_s0", CSTM_STORE_POS_X - 3, CSTM_STORE_POS_Y - 28, 1000, CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_WIDTH, 20, tf_left_align),
			
			(call_script, "script_cstm_troop_get_inventory_value", ":dummy"),
			(store_sub, ":remaining_funds", "$cstm_total_funds", reg0),
			(assign, reg0, ":remaining_funds"),
			(str_store_string, s0, "@{reg0} denars"),
      (call_script, "script_gpu_create_text_overlay", "str_s0", CSTM_STORE_POS_X + CSTM_STORE_SLOT_SIZE * CSTM_STORE_CONT_WIDTH, CSTM_STORE_POS_Y - 28, 1000, 200, 20, tf_right_align),
			(try_begin),
				(ge, ":remaining_funds", 0),
				
				(overlay_set_color, reg1, 0x00bb00),
			(else_try),
				(overlay_set_color, reg1, 0xbb0000),
			(try_end),
			
			## STATS
			(call_script, "script_gpu_create_scrollable_container", CSTM_STATS_POS_X, CSTM_STATS_POS_Y, CSTM_STATS_SIZE_X, CSTM_STATS_SIZE_Y),
			(assign, "$cstm_stats_container", reg1),
			
			(set_container_overlay, "$cstm_stats_container"),
			
			(store_character_level, reg0, "$cstm_troop_being_customised"),
			(str_store_string, s0, "@Level {reg0}"),
      (call_script, "script_gpu_create_text_overlay", "str_s0", 0, CSTM_STATS_GAP_Y * 4 + CSTM_STATS_PROF_SECTION_HEIGHT + CSTM_STATS_SKL_SECTION_HEIGHT + CSTM_STATS_POINTS_SECTION_HEIGHT + CSTM_STATS_ATTR_SECTION_HEIGHT, 1200, CSTM_STATS_ATTR_COL_WIDTH, 50, tf_left_align),
			
			# Attributes
			(try_for_range, ":attribute", attributes_begin, attributes_end),
				(call_script, "script_cstm_get_grid_position", ":attribute", 4, CSTM_STATS_ATTR_CONT_WIDTH, CSTM_STATS_ATTR_COL_WIDTH, CSTM_STATS_ATTR_ROW_HEIGHT),
				(assign, ":pos_x", reg0),
				(store_add, ":pos_y", reg1, CSTM_STATS_GAP_Y * 3 + CSTM_STATS_PROF_SECTION_HEIGHT + CSTM_STATS_SKL_SECTION_HEIGHT + CSTM_STATS_POINTS_SECTION_HEIGHT),
				
				(store_add, ":attribute_string", cstm_attribute_strings_begin, ":attribute"),
				(str_store_string, s0, ":attribute_string"),
				(call_script, "script_gpu_create_text_overlay", "str_s0", ":pos_x", ":pos_y", CSTM_STATS_ATTR_TEXT_SIZE, CSTM_STATS_ATTR_COL_WIDTH, CSTM_STATS_ATTR_ROW_HEIGHT, tf_left_align),
				
				(val_add, ":pos_x", CSTM_STATS_ATTR_COL_WIDTH - 75),
				
				(store_attribute_level, ":curr_val", ":dummy", ":attribute"),
				
				(call_script, "script_cstm_troop_get_attribute_min_from_points", "$cstm_troop_being_customised", ":attribute"),
				(assign, ":min", reg0),
				(call_script, "script_cstm_troop_get_attribute_min_from_tree", "$cstm_troop_being_customised", "$cstm_troop_being_customised", ":attribute"),
				(val_max, ":min", reg0),
				
				(store_attribute_level, ":max", ":dummy", ":attribute"),
				(call_script, "script_cstm_get_attribute_points_available", ":dummy", ":attribute"),
				(val_add, ":max", reg0),
				(val_add, ":max", 1),
				
				(try_begin),
					(lt, ":curr_val", ":min"),
					
					(str_store_string, s0, ":attribute_string"),
					(assign, reg0, ":min"),
					(assign, reg1, ":curr_val"),
					(display_message, "@{s0} minimum was being set to {reg0}, but current value is {reg1}"),
					(assign, ":min", ":curr_val"),
				(try_end),
				
				(try_begin),
					(ge, ":curr_val", ":max"),
					
					(str_store_string, s0, ":attribute_string"),
					(assign, reg0, ":max"),
					(assign, reg1, ":curr_val"),
					(display_message, "@{s0} maximum was being set to {reg0}, but current value is {reg1}"),
					(store_add, ":max", ":curr_val", 1),
				(try_end),
				
				#(assign, reg0, ":min"),
				#(assign, reg1, ":max"),
				#(display_message, "@Setting min {s0} to {reg0} and max {s0} to {reg1}"),
				
				(call_script, "script_gpu_create_number_box_overlay", ":pos_x", ":pos_y", ":min", ":max"),
				(troop_set_slot, "trp_cstm_overlay_is_attribute_box", reg1, 1),
				(troop_set_slot, "trp_cstm_overlay_attribute", reg1, ":attribute"),
				(overlay_set_val, reg1, ":curr_val"),
			(try_end),
			
			# Proficiencies
			(try_for_range, ":proficiency", proficiencies_begin, proficiencies_end),
				(call_script, "script_cstm_get_grid_position", ":proficiency", proficiencies_end, CSTM_STATS_PROF_CONT_WIDTH, CSTM_STATS_PROF_COL_WIDTH, CSTM_STATS_PROF_ROW_HEIGHT),
				(assign, ":pos_x", reg0),
				(store_add, ":pos_y", reg1, CSTM_STATS_GAP_Y * 2 + CSTM_STATS_SKL_SECTION_HEIGHT + CSTM_STATS_POINTS_SECTION_HEIGHT),
				
				(store_add, ":proficiency_string", cstm_proficiency_strings_begin, ":proficiency"),
				(str_store_string, s0, ":proficiency_string"),
				(call_script, "script_gpu_create_text_overlay", "str_s0", ":pos_x", ":pos_y", CSTM_STATS_PROF_TEXT_SIZE, CSTM_STATS_PROF_COL_WIDTH, CSTM_STATS_PROF_ROW_HEIGHT, tf_left_align),
				
				(val_add, ":pos_x", CSTM_STATS_PROF_COL_WIDTH - 75),
				
				(store_proficiency_level, ":curr_val", ":dummy", ":proficiency"),
				
				(call_script, "script_cstm_troop_get_proficiency_min_from_points", "$cstm_troop_being_customised", ":proficiency"),
				(assign, ":min", reg0),
				(call_script, "script_cstm_troop_get_proficiency_min_from_tree", "$cstm_troop_being_customised", "$cstm_troop_being_customised", ":proficiency"),
				(val_max, ":min", reg0),
				
				(store_proficiency_level, ":max", ":dummy", ":proficiency"),
				(troop_get_slot, ":max_points", "trp_cstm_proficiency_requirements", ":max"),
				(call_script, "script_cstm_get_proficiency_points_available", ":dummy", ":proficiency"),
				(val_add, ":max_points", reg0),
				(call_script, "script_cstm_troop_get_highest_proficiency_from_points", ":max_points"),
				(assign, ":max", reg0),
				
				# Apply cap from weapon master
				(store_skill_level, ":weapon_master", skl_weapon_master, ":dummy"),
				(store_mul, ":cap", 40, ":weapon_master"),
				(val_add, ":cap", 60),
				(val_min, ":max", ":cap"),
				(val_add, ":max", 1),
				
				(try_begin),
					(lt, ":curr_val", ":min"),
					
					(str_store_string, s0, ":proficiency_string"),
					(assign, reg0, ":min"),
					(assign, reg1, ":curr_val"),
					(display_message, "@{s0} minimum was being set to {reg0}, but current value is {reg1}"),
					(assign, ":min", ":curr_val"),
				(try_end),
				
				(try_begin),
					(ge, ":curr_val", ":max"),
					
					(str_store_string, s0, ":proficiency_string"),
					(assign, reg0, ":max"),
					(assign, reg1, ":curr_val"),
					(display_message, "@{s0} maximum was being set to {reg0}, but current value is {reg1}"),
					(store_add, ":max", ":curr_val", 1),
				(try_end),
				
				(call_script, "script_gpu_create_number_box_overlay", ":pos_x", ":pos_y", ":min", ":max"),
				(troop_set_slot, "trp_cstm_overlay_is_proficiency_box", reg1, 1),
				(troop_set_slot, "trp_cstm_overlay_proficiency", reg1, ":proficiency"),
				(overlay_set_val, reg1, ":curr_val"),
			(try_end),
			
			# Skills added in modmerge function due to need of python code to differentiate between active and non-active skills
			
			(set_container_overlay, -1),
			
			## TROOP NAME
			(str_store_string, s0, "@Name (singular): "),
      (call_script, "script_gpu_create_text_overlay", "str_s0", CSTM_NAME_POS_X + CSTM_NAME_LABEL_WIDTH, CSTM_NAME_POS_Y, 1000, CSTM_NAME_LABEL_WIDTH, 50, tf_right_align),
      
      (str_store_troop_name, s0, ":dummy"),
      (call_script, "script_gpu_create_text_box_overlay", "str_s0", CSTM_NAME_POS_X + CSTM_NAME_LABEL_WIDTH, CSTM_NAME_POS_Y),
      (assign, "$cstm_set_name", reg1),
      
      (str_store_string, s0, "@Name (plural): "),
      (call_script, "script_gpu_create_text_overlay", "str_s0", CSTM_NAME_POS_X + CSTM_NAME_LABEL_WIDTH + CSTM_NAME_GAP, CSTM_NAME_POS_Y, 1000, CSTM_NAME_LABEL_WIDTH, 50, tf_right_align),
      
      (str_store_troop_name_plural, s0, ":dummy"),
      (call_script, "script_gpu_create_text_box_overlay", "str_s0", CSTM_NAME_POS_X + CSTM_NAME_LABEL_WIDTH + CSTM_NAME_GAP, CSTM_NAME_POS_Y),
      (assign, "$cstm_set_name_plural", reg1),
			
			(assign, ":changes_made", "$cstm_name_changed"),
			(try_begin),
				(call_script, "script_cstm_cf_troop_stats_are_different", "$cstm_troop_being_customised", ":dummy"),
				
				(assign, ":changes_made", 1),
			(else_try),
				(call_script, "script_cstm_cf_troop_equipments_are_different", "$cstm_troop_being_customised", ":dummy"),
				
				(assign, ":changes_made", 1),
			(try_end),
			
			## SAVE BUTTON
			(try_begin),
				(eq, ":changes_made", 1),
				(ge, ":remaining_funds", 0),
				
				(str_store_string, s0, "@Save"),
				(call_script, "script_gpu_create_game_button_overlay", "str_s0", CSTM_BUTTONS_POS_X, CSTM_BUTTONS_POS_Y),
				(assign, "$cstm_customise_troop_save", reg1),
				(position_set_x, pos1, CSTM_BUTTONS_SIZE_X),
				(position_set_y, pos1, CSTM_BUTTONS_SIZE_Y),
				(overlay_set_size, "$cstm_customise_troop_save", pos1),
			(end_try),
			
			## RESET BUTTON
			(try_begin),
				(eq, ":changes_made", 1),
				
				(str_store_string, s0, "@Reset"),
				(call_script, "script_gpu_create_game_button_overlay", "str_s0", CSTM_BUTTONS_POS_X + CSTM_BUTTONS_SIZE_X + CSTM_BUTTONS_GAP, CSTM_BUTTONS_POS_Y),
				(assign, "$cstm_customise_troop_reset", reg1),
				#(display_message, "@Reset button: {reg1}"),
				(position_set_x, pos1, CSTM_BUTTONS_SIZE_X),
				(position_set_y, pos1, CSTM_BUTTONS_SIZE_Y),
				(overlay_set_size, "$cstm_customise_troop_reset", pos1),
			(try_end),
			
			## EXIT BUTTON
			(try_begin),
				(neq, ":changes_made", 1),
				
				(str_store_string, s0, "@Exit"),
				(call_script, "script_gpu_create_game_button_overlay", "str_s0", CSTM_BUTTONS_POS_X + CSTM_BUTTONS_SIZE_X + CSTM_BUTTONS_GAP, CSTM_BUTTONS_POS_Y),
				(assign, "$cstm_customise_troop_exit", reg1),
				(position_set_x, pos1, CSTM_BUTTONS_SIZE_X),
				(position_set_y, pos1, CSTM_BUTTONS_SIZE_Y),
				(overlay_set_size, "$cstm_customise_troop_exit", pos1),
			(try_end),
			
			(presentation_set_duration, 999999),
		]),
		
		(ti_on_presentation_mouse_enter_leave,
		[
			(store_trigger_param_1, ":overlay"),
			(store_trigger_param_2, ":mouse_left"),
			
			(try_begin),
				(troop_slot_ge, "trp_cstm_overlay_items", ":overlay", 1),
				
				(try_begin),
					## MOUSE LEFT ITEM
					(eq, ":mouse_left", 1),
					
					(try_begin),
						(eq, "$cstm_item_details_overlay", ":overlay"),
						
						(close_item_details),
						(assign, "$cstm_item_details_overlay", -1),
						(overlay_set_display, "$cstm_remove_from_inventory_message", 0),
					(try_end),
				(else_try),
					## ITEM MOUSED OVER
					(try_begin),
						(gt, "$cstm_item_details_overlay", 0),
						
						(close_item_details),
					(try_end),
					
					(troop_get_slot, ":dummy", "$cstm_troop_being_customised", cstm_slot_troop_dummy),
					(try_begin),
						(troop_slot_eq, "trp_cstm_overlay_is_store_item", ":overlay", 1),
						
						(troop_get_slot, ":item", "trp_cstm_overlay_items", ":overlay"),
						(assign, ":imod", "$cstm_item_modifier_selected"),
					(else_try),
						(troop_get_slot, ":inventory_slot", "trp_cstm_overlay_items", ":overlay"),
						
						(troop_get_inventory_slot, ":item", ":dummy", ":inventory_slot"),
						(troop_get_inventory_slot_modifier, ":imod", ":dummy", ":inventory_slot"),
					(try_end),
					
					(overlay_get_position, pos1, ":overlay"),
					(call_script, "script_cstm_item_get_price_with_modifier", ":item", ":imod"),
					(show_item_details_with_modifier, ":item", ":imod", pos1, reg1),
					(assign, "$cstm_item_details_overlay", ":overlay"),
					
					(neg|troop_slot_eq, "trp_cstm_overlay_is_store_item", ":overlay", 1),
					
					(overlay_set_display, "$cstm_remove_from_inventory_message", 1),
				(try_end),
			(try_end),
		]),
		
		(ti_on_presentation_mouse_press,
		[
			(store_trigger_param_1, ":overlay"),
			(store_trigger_param_2, ":mouse_button"),
			
			(troop_get_slot, ":dummy", "$cstm_troop_being_customised", cstm_slot_troop_dummy),
			
			(try_begin),
				## STORE ITEM SELECTED
				(eq, ":mouse_button", 0),	# Left-click
				(troop_slot_ge, "trp_cstm_overlay_items", ":overlay", 1),
				(troop_slot_eq, "trp_cstm_overlay_is_store_item", ":overlay", 1),
				
				(try_begin),
					(store_free_inventory_capacity, ":free_capacity", ":dummy"),
					(eq, ":free_capacity", 0),
					
					(display_message, "@{s1} has no room left in inventory", 0xff0000),
				(else_try),
					(troop_get_slot, ":item", "trp_cstm_overlay_items", ":overlay"),
					
					(assign, ":meets_requirement", 1),
					(try_begin),
						(call_script, "script_cf_troop_can_use_item_with_modifier", ":dummy", ":item", "$cstm_item_modifier_selected"),
					(else_try),
						(assign, ":meets_requirement", 0),
					(try_end),
					
					(eq, ":meets_requirement", 0),
					
					(str_store_troop_name, s1, ":dummy"),
					(str_store_item_name, s2, ":item"),
					(try_begin),
						(gt, "$cstm_item_modifier_selected", 0),
						
						(store_add, ":modifier_string", modifier_strings_begin, "$cstm_item_modifier_selected"),
						(str_store_string, s0, ":modifier_string"),
						(str_store_string, s2, "@{s0} {s2}"),
					(try_end),
					(call_script, "script_cstm_store_item_requirement_stat_to_s0", ":item"),
					(display_message, "@{reg1} {s0} is required to equip {s2}, {s1} has {reg0}", 0xff0000),
				(else_try),
					(troop_add_item, ":dummy", ":item", "$cstm_item_modifier_selected"),
					(start_presentation, "prsnt_cstm_customise_troop"),
				(try_end),
			(else_try),
				## INVENTORY ITEM REMOVED
				(eq, ":mouse_button", 1),	# Right-click
				
				(troop_get_slot, ":inventory_slot", "trp_cstm_overlay_items", ":overlay"),
				(gt, ":inventory_slot", 0),
				
				(troop_slot_eq, "trp_cstm_overlay_is_store_item", ":overlay", 0),
				
				(troop_set_inventory_slot, ":dummy", ":inventory_slot", -1),
				(start_presentation, "prsnt_cstm_customise_troop"),
			(try_end),
		]),
		
		(ti_on_presentation_run,
		[
			# Emergency escape option if buttons are bugging out - just hit ESC to close presentation at any time
			(try_begin),
				(key_clicked, key_escape),
				
				(presentation_set_duration, 0),
			(try_end),
		]),
		
		(ti_on_presentation_event_state_change,
		[
			(store_trigger_param_1, ":object"),
			(store_trigger_param_2, ":value"),
			
			#(assign, reg0, ":object"),
			#(display_message, "@Object: {reg0}"),
			
			(troop_get_slot, ":dummy", "$cstm_troop_being_customised", cstm_slot_troop_dummy),
			(try_begin),
				## NAME CHANGED
				(eq, ":object", "$cstm_set_name"),
				
				(troop_set_name, ":dummy", s0),
				(str_store_string, s1, "@{s0}s"),
				(troop_set_plural_name, ":dummy", s1),
				(assign, "$cstm_name_changed", 1),
				(start_presentation, "prsnt_cstm_customise_troop"),
			(else_try),
				## PLURAL NAME CHANGED
				(eq, ":object", "$cstm_set_name_plural"),
				
				(troop_set_plural_name, ":dummy", s0),
				(assign, "$cstm_name_changed", 1),
				(start_presentation, "prsnt_cstm_customise_troop"),
			(else_try),
				## ITEM TYPE BEING SELECTED
				(eq, ":object", "$cstm_store_item_type_selector"),
        
        (store_add, "$cstm_items_array", cstm_items_arrays_begin, ":value"),
				(assign, "$cstm_item_modifier_selected", 0),
				(assign, "$cstm_item_page_no", 0),
				(start_presentation, "prsnt_cstm_customise_troop"),
			(else_try),
				## ITEM MODIFIER BEING SELECTED
				(eq, ":object", "$cstm_store_item_modifier_selector"),
				
				(assign, ":count", 0),
				(assign, ":end_cond", imod_large_bag + 1),
				(try_for_range, ":imod", imod_plain, ":end_cond"),
					## Filter for appropriate IMODs based on item type.
					(call_script, "script_cf_cci_imod_appropriate_for_item", "$cstm_item_type_selected", ":imod"),
					
					(try_begin),
						(eq, ":count", ":value"),
						
						(assign, "$cstm_item_modifier_selected", ":imod"),
						(assign, ":end_cond", 0),
					(try_end),
					
					(val_add, ":count", 1),
				(try_end),
				
				(start_presentation, "prsnt_cstm_customise_troop"),
			(else_try),
				## ITEM PAGE CHANGED
				(eq, ":object", "$cstm_item_page_selector"),
				
				(assign, "$cstm_item_page_no", ":value"),
				(start_presentation, "prsnt_cstm_customise_troop"),
			(else_try),
				## ATTRIBUTE CHANGED
				(troop_slot_eq, "trp_cstm_overlay_is_attribute_box", ":object", 1),
				
				(troop_get_slot, ":attribute", "trp_cstm_overlay_attribute", ":object"),
				(call_script, "script_cstm_dummy_set_attribute", ":dummy", ":attribute", ":value"),
				(start_presentation, "prsnt_cstm_customise_troop"),
			(else_try),
				## PROFICIENCY CHANGED
				(troop_slot_eq, "trp_cstm_overlay_is_proficiency_box", ":object", 1),
				
				(troop_get_slot, ":proficiency", "trp_cstm_overlay_proficiency", ":object"),
				(call_script, "script_cstm_dummy_set_proficiency", ":dummy", ":proficiency", ":value"),
				(start_presentation, "prsnt_cstm_customise_troop"),
			(else_try),
				## SKILL CHANGED
				(troop_slot_eq, "trp_cstm_overlay_is_skill_box", ":object", 1),
				
				(troop_get_slot, ":skill", "trp_cstm_overlay_skill", ":object"),
				(call_script, "script_cstm_dummy_set_skill", ":dummy", ":skill", ":value"),
				(start_presentation, "prsnt_cstm_customise_troop"),
			(else_try),
				## SAVE BUTTON PRESSED
				(eq, ":object", "$cstm_customise_troop_save"),
				
				# If equipment is modified, mark this troop as one that shouldn't have equipment overridden by a base troop changing equipment
				(try_begin),
					(call_script, "script_cstm_cf_troop_equipments_are_different", "$cstm_troop_being_customised", ":dummy"),
					
					(troop_set_slot, "$cstm_troop_being_customised", cstm_slot_troop_equipment_modified, 1),
				(try_end),
				
				# Automatically set class (e.g. infantry, archers, cavalry) based on equipment
				(try_begin),
					(call_script, "script_cstm_cf_troop_has_horse", ":dummy"),
					
					(troop_set_class, "$cstm_troop_being_customised", grc_cavalry),
					(troop_set_class, ":dummy", grc_cavalry),
				(else_try),
					(call_script, "script_cstm_cf_troop_has_bow_or_crossbow", ":dummy"),
					
					(troop_set_class, "$cstm_troop_being_customised", grc_archers),
					(troop_set_class, ":dummy", grc_archers),
				(else_try),
					(troop_set_class, "$cstm_troop_being_customised", grc_infantry),
					(troop_set_class, ":dummy", grc_infantry),
				(try_end),
				
				(troop_sort_inventory, "$cstm_troop_being_customised"),
				(troop_equip_items, "$cstm_troop_being_customised"),				
				
				(call_script, "script_cstm_replace_custom_troop_with_dummy", "$cstm_troop_being_customised"),
				(troop_get_slot, ":dummy", "$cstm_troop_being_customised", cstm_slot_troop_dummy),
				
				(troop_get_upgrade_troop, ":upgrade", "$cstm_troop_being_customised", 0),
				(try_begin),
					(gt, ":upgrade", 0),
					
					(call_script, "script_cstm_troop_tree_copy_inventory_if_unmodified", ":upgrade", ":dummy"),
					(call_script, "script_cstm_troop_tree_copy_stats_if_higher", "$cstm_troop_being_customised", ":dummy"),
					
					(troop_get_upgrade_troop, ":upgrade", "$cstm_troop_being_customised", 1),
					(gt, ":upgrade", 0),
					
					(call_script, "script_cstm_troop_tree_copy_inventory_if_unmodified", ":upgrade", ":dummy"),
					(call_script, "script_cstm_troop_tree_copy_stats_if_higher", "$cstm_troop_being_customised", ":dummy"),
				(try_end),
				
				(call_script, "script_cstm_troop_tree_update_stat_minimums", "$cstm_troop_being_customised"),
				
				# Update name backup
				(str_store_troop_name, s0, ":dummy"),
				(troop_set_name, "$cstm_presentation_troop", s0),
				(str_store_troop_name_plural, s0, ":dummy"),
				(troop_set_plural_name, "$cstm_presentation_troop", s0),
				
				(display_message, "@Changes saved"),
				(assign, "$cstm_name_changed", 0),
				
				(start_presentation, "prsnt_cstm_customise_troop"),
			(else_try),
				## RESET BUTTON PRESSED
				(eq, ":object", "$cstm_customise_troop_reset"),
				
				(display_message, "@Changes discarded"),
				(assign, "$cstm_name_changed", 0),
				(call_script, "script_cstm_copy_custom_troop_to_dummy", "$cstm_troop_being_customised"),
				
				# Restore name
				(str_store_troop_name, s0, "$cstm_presentation_troop"),
				(troop_set_name, ":dummy", s0),
				(str_store_troop_name_plural, s0, "$cstm_presentation_troop"),
				(troop_set_plural_name, ":dummy", s0),
				
				(start_presentation, "prsnt_cstm_customise_troop"),
			(else_try),
				## EXIT BUTTON PRESSED
				(eq, ":object", "$cstm_customise_troop_exit"),
				
				(assign, "$cstm_item_modifier_selected", 0),
				(assign, "$cstm_item_page_no", 0),
				(start_presentation, "prsnt_cstm_view_custom_troop_tree"),
			(else_try),
				## TROOP IMAGE PRESSED
				# If cheat mode is on, clicking the troop image will add that troop to the party (1 added by default, 10 added if holding shift)
				(eq, ":object", "$cstm_troop_image"),
				(eq, "$cheat_mode", 1),
				
				(assign, ":num_troops", 1),
				(try_begin),
					(this_or_next|key_is_down, key_left_shift),
					(key_is_down, key_right_shift),
					
					(assign, ":num_troops", 10),
				(try_end),
				
				(party_add_members, "p_main_party", "$cstm_troop_being_customised", ":num_troops"),
				(str_store_troop_name_by_count, s0, "$cstm_troop_being_customised", reg0),
				(display_message, "@{reg0} {s0} added to party"),
			(try_end),
		]),
	])
	
]

def modmerge(var_set):
	try:
		var_name_1 = "presentations"
		orig_presentations = var_set[var_name_1]
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)
	
	orig_presentations.extend(new_presentations)
	
	presentations = collections.OrderedDict()
	for presentation_tuple in orig_presentations:
		presentations[presentation_tuple[0]] = Presentation(*presentation_tuple)
	
	for item_type, string in cstm_item_type_strings.iteritems():
		presentations["cstm_customise_troop"].triggers[ti_on_presentation_load][0].extend([
			(str_store_string, s0, "@" + string),
			(overlay_add_item, "$cstm_store_item_type_selector", s0),
		])
	presentations["cstm_customise_troop"].triggers[ti_on_presentation_load][0].extend([
		(store_sub, ":array_offset", "$cstm_items_array", cstm_items_arrays_begin),
		(overlay_set_val, "$cstm_store_item_type_selector", ":array_offset"),
	])
	
	presentations["cstm_customise_troop"].triggers[ti_on_presentation_load][0].append((set_container_overlay, "$cstm_stats_container"))
	skill_index = 0
	for skill in ACTIVE_FIGHTING_SKILLS[::-1]:
		skill_ref = "skl_" + skill[0]
		base_attribute = skill[2] & 0xf
		
		presentations["cstm_customise_troop"].triggers[ti_on_presentation_load][0].extend([
			(call_script, "script_cstm_get_grid_position", skill_index, len(ACTIVE_FIGHTING_SKILLS), CSTM_STATS_SKL_CONT_WIDTH, CSTM_STATS_SKL_COL_WIDTH, CSTM_STATS_SKL_ROW_HEIGHT),
			(assign, ":pos_x", reg0),
			(store_add, ":pos_y", reg1, CSTM_STATS_GAP_Y + CSTM_STATS_POINTS_SECTION_HEIGHT),
			
			(call_script, "script_cstm_print_skill_to_s0", skill_ref),
			(call_script, "script_gpu_create_text_overlay", "str_s0", ":pos_x", ":pos_y", CSTM_STATS_SKL_TEXT_SIZE, CSTM_STATS_SKL_COL_WIDTH, CSTM_STATS_SKL_ROW_HEIGHT, tf_left_align),
			
			(val_add, ":pos_x", CSTM_STATS_SKL_COL_WIDTH - 75),
			
			# Get the min and max values with the number of skill points available to spend
			(store_skill_level, ":curr_val", skill_ref, ":dummy"),
			
			(call_script, "script_cstm_troop_get_skill_min_from_points", "$cstm_troop_being_customised", skill_ref),
			(assign, ":min", reg0),
			(call_script, "script_cstm_troop_get_skill_min_from_tree", "$cstm_troop_being_customised", "$cstm_troop_being_customised", skill_ref),
			(val_max, ":min", reg0),
			
			# Get max as min plus the maximum number of points that could be spent
			(call_script, "script_cstm_get_skill_points_available", ":dummy", skill_ref),
			(store_add, ":max", ":curr_val", reg0),
			(val_add, ":max", 1),
			
			# Adjust this if necessary to the max allowed by base attribute
			(store_attribute_level, ":attribute_cap", ":dummy", base_attribute),
			(val_div, ":attribute_cap", 3),
			(val_add, ":attribute_cap", 1),
			(val_min, ":max", ":attribute_cap"),
			
			(try_begin),
				(ge, ":curr_val", ":attribute_cap"),
				
				(store_sub, ":difference", ":attribute_cap", ":curr_val"),
				(val_sub, ":difference", 1),
				(troop_raise_skill, ":dummy", skill_ref, ":difference"),
				(store_skill_level, ":curr_val", skill_ref, ":dummy"),
				(assign, reg0, ":curr_val"),
				(display_message, "@{s0} reduced to {reg0}"),
			(try_end),
			
			(try_begin),
				(lt, ":curr_val", ":min"),
				
				(call_script, "script_cstm_print_skill_to_s0", skill_ref),
				(assign, reg0, ":min"),
				(assign, reg1, ":curr_val"),
				(display_message, "@{s0} minimum was being set to {reg0}, but current value is {reg1}"),
				(assign, ":min", ":curr_val"),
			(try_end),
			
			(try_begin),
				(ge, ":curr_val", ":max"),
				
				(call_script, "script_cstm_print_skill_to_s0", skill_ref),
				(assign, reg0, ":max"),
				(assign, reg1, ":curr_val"),
				(display_message, "@{s0} maximum was being set to {reg0}, but current value is {reg1}"),
				(store_add, ":max", ":curr_val", 1),
			(try_end),
			
			#(assign, reg0, ":min"),
			#(assign, reg1, ":max"),
			#(call_script, "script_cstm_print_skill_to_s0", skill_ref),
			#(display_message, "@{s0} bounds: {reg0} - {reg1}"),
			
			(call_script, "script_gpu_create_number_box_overlay", ":pos_x", ":pos_y", ":min", ":max"),
			(troop_set_slot, "trp_cstm_overlay_is_skill_box", reg1, 1),
			(troop_set_slot, "trp_cstm_overlay_skill", reg1, skill_ref),
			(overlay_set_val, reg1, ":curr_val"),
		])
		skill_index += 1
	
	presentations["cstm_customise_troop"].triggers[ti_on_presentation_load][0].extend([
		(call_script, "script_cstm_get_attribute_points_available", ":dummy"),
		(str_store_string, s0, "@Attribute points: {reg0}"),
		(call_script, "script_gpu_create_text_overlay", "str_s0", 0, CSTM_STATS_POINTS_ROW_HEIGHT, CSTM_STATS_POINTS_TEXT_SIZE, CSTM_STATS_POINTS_COL_WIDTH, CSTM_STATS_POINTS_ROW_HEIGHT, tf_left_align),
		
		(call_script, "script_cstm_get_proficiency_points_available", ":dummy"),
		(str_store_string, s0, "@Proficiency points: {reg0}"),
		(call_script, "script_gpu_create_text_overlay", "str_s0", 0, 0, CSTM_STATS_POINTS_TEXT_SIZE, CSTM_STATS_POINTS_COL_WIDTH, CSTM_STATS_POINTS_ROW_HEIGHT, tf_left_align),
		
		(call_script, "script_cstm_get_skill_points_available", ":dummy"),
		(str_store_string, s0, "@Skill points: {reg0}"),
		(call_script, "script_gpu_create_text_overlay", "str_s0", CSTM_STATS_POINTS_COL_WIDTH, CSTM_STATS_POINTS_ROW_HEIGHT, CSTM_STATS_POINTS_TEXT_SIZE, CSTM_STATS_POINTS_COL_WIDTH, CSTM_STATS_POINTS_ROW_HEIGHT, tf_left_align),
		
		(set_container_overlay, -1),
	])
	
	del orig_presentations[:]
	for presentation_id in presentations:
		orig_presentations.append(presentations[presentation_id].convert_to_tuple())

	#print var_name_1 + " done"