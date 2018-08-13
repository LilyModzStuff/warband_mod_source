# Dynamic Troop Trees by Dunde, modified by Caba'drin.

from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
# from header_items import *   # Added for Show all Items presentation.
# from module_items import *   # Added for Show all Items presentation.
from header_skills import *

import string

####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

presentations = [

("faction_troop_tree", 0, mesh_load_window,
 [(ti_on_presentation_load,
  [(presentation_set_duration, 999999),
   (set_fixed_point_multiplier, 1000),
   ## WINDYPLAINS+ ## - Added an exit button to the presentation.
	(create_game_button_overlay, "$g_presentation_obj_21", "@Done"),
	(position_set_x, pos1, 885),
	(position_set_y, pos1, 30),
	(overlay_set_position, "$g_presentation_obj_21", pos1),
   ## WINDYPLAINS- ##
   # Title
   (position_set_y, pos1, title_pos_y), (position_set_x, pos1, title_pos_x),  # Title Position
   (position_set_x, pos3, title_size),  (position_set_y, pos3, title_size),   # Title Size
   (create_text_overlay, reg0, "str_faction_troop_tree", tf_center_justify), (overlay_set_color, reg0, title_black),
   (overlay_set_position, reg0, pos1), (overlay_set_size, reg0, pos3),
   (position_set_y, pos1, title_pos_y-1),  (position_set_x, pos1, title_pos_x-1),  # Title Position
   (create_text_overlay, reg0, "str_faction_troop_tree", tf_center_justify), (overlay_set_color, reg0, title_red),
   (overlay_set_position, reg0, pos1), (overlay_set_size, reg0, pos3),      
   # Create Objects
   (create_combo_label_overlay, "$g_presentation_obj_1"), #type
   (position_set_x, pos1, title_pos_x), (position_set_y, pos1, title_pos_y-50), (overlay_set_position, "$g_presentation_obj_1",  pos1),
   # Objects
   (assign, ":hi_faction", "fac_kingdoms_end"),
   (try_begin),
      (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
      (assign, ":lo_faction", "fac_kingdom_1"),
   (else_try),
      (assign, ":lo_faction", "fac_player_supporters_faction"),
   (try_end),
   (try_for_range, ":faction", ":lo_faction", ":hi_faction"),
      (str_store_faction_name, s1, ":faction"),
      (overlay_add_item,  "$g_presentation_obj_1", s1),
   (try_end),
   (store_sub, reg12, ":hi_faction", ":lo_faction"),
   (val_clamp, reg11, 0, reg12),
   (overlay_set_val,  "$g_presentation_obj_1", reg11),
   (store_add, "$faction_display", ":lo_faction", reg11),
   (faction_get_slot, ":culture", "$faction_display", slot_faction_culture),
   (call_script, "script_prsnt_culture_troop_tree", ":culture"), ]),
 (ti_on_presentation_event_state_change, 
  [(store_trigger_param_1, ":object"),
   (store_trigger_param_2, ":value"),
   (set_fixed_point_multiplier, 1000),
   (try_begin), 
     (eq, ":object", "$g_presentation_obj_1"),
     (assign, reg11, ":value"),     
     (start_presentation, "prsnt_faction_troop_tree"),
   (else_try),
     (troop_get_slot, ":limit", "trp_temp_array_c", 100),
     (val_add, ":limit", 1), (assign, ":troop_no", 0),
     (try_for_range, ":slot", 101, ":limit"),
        (le, ":troop_no", 0),
        (troop_slot_eq, "trp_temp_array_c", ":slot", ":object"),
        (troop_get_slot, ":troop_no", "trp_temp_array_b", ":slot"),
     (try_end),      
     (gt, ":troop_no", 0),
     (assign, "$temp", ":troop_no"), 
     (assign, "$g_presentation_next_presentation", "prsnt_faction_troop_tree"),
     (start_presentation, "prsnt_troop_note"),
   (try_end), ]), 
   
   ## Event to process when running the presentation
  (ti_on_presentation_run,
   [(try_begin),
      (this_or_next|key_clicked, key_escape),
      (key_clicked, key_right_mouse_button),
      (presentation_set_duration, 0),
      (assign, "$faction_display", 0),
      (jump_to_menu, "mnu_reports"), # I asume it's called from report menu, you can modify it to any menus or using $next_menu declarated by menu that call this presentation
    (try_end), ]),  
	
	## WINDYPLAINS+ ##
	(ti_on_presentation_event_state_change,
    [
        (store_trigger_param_1, ":object"),
       
		(try_begin),
			##### DONE BUTTON #####
			(eq, "$g_presentation_obj_21", ":object"),
			(presentation_set_duration, 0),
		(try_end),
	]),
	## WINDYPLAINS- ##
	]),
	
	
# rubik CC's Presentation      
  ("troop_note", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        ## init troop items
        (call_script, "script_copy_inventory", "$temp", "trp_temp_array_a"),
        (try_for_range, ":i_slot", 0, 10),
          (troop_get_inventory_slot, ":item", "trp_temp_array_a", ":i_slot"),
          (gt, ":item", -1),
          (troop_add_item,"trp_temp_array_a",":item"),
          (troop_set_inventory_slot, "trp_temp_array_a", ":i_slot", -1),
        (try_end),

        ## back
        (create_game_button_overlay, "$g_presentation_obj_1", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_1", pos1),

        ################
        (store_mul, ":cur_troop", "$temp", 2), #with weapons
        (create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_game_party_window", ":cur_troop"),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg0, pos1),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 350),
        (overlay_set_position, reg0, pos1),

        (str_store_troop_name, s1, "$temp"),
        (store_character_level, ":troop_level", "$temp"),
        (assign, reg1, ":troop_level"),
        (str_store_string, s1, "@Name: {s1}^Level: {reg1}"),
        (call_script, "script_get_troop_max_hp", "$temp"),
        (str_store_string, s1, "@{s1}^HP: {reg0}"),

        (create_text_overlay, reg0, "@{s1}", tf_double_space),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_position, reg0, pos1),

        (str_store_string, s3, "@Attributes:"),
        (store_attribute_level, reg1, "$temp", ca_strength),
        (store_attribute_level, reg2, "$temp", ca_intelligence),
        (str_store_string, s3, "@{s3}^STR: {reg1}^INT: {reg2}^^Skills:"),
        (store_skill_level, reg1, skl_power_strike, "$temp"),
        (store_skill_level, reg2, skl_power_draw, "$temp"),
        (store_skill_level, reg3, skl_power_throw, "$temp"),
        (store_skill_level, reg4, skl_horse_archery, "$temp"),
        (str_store_string, s3, "@{s3}^Power Strike: {reg1}^Power Draw: {reg2}^Power Throw: {reg3}^Horse Archery: {reg4}^^Weapon Proficiencies:"),
        (store_proficiency_level, reg1, "$temp", wpt_one_handed_weapon),
        (store_proficiency_level, reg2, "$temp", wpt_two_handed_weapon),
        (store_proficiency_level, reg3, "$temp", wpt_polearm),
        (str_store_string, s3, "@{s3}^1 Hand Wpns: {reg1}^2 Hand Wpns: {reg2}^Polearms: {reg3}"),
        (create_text_overlay, reg0, "@{s3}", tf_double_space),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 100),
        (overlay_set_position, reg0, pos1),

        (str_store_string, s4, "str_empty_string"),
        (store_attribute_level, reg1, "$temp", ca_agility),
        (store_attribute_level, reg2, "$temp", ca_charisma),
        (str_store_string, s4, "@{s4}^AGI: {reg1}^CHA: {reg2}^^"),
        (store_skill_level, reg1, skl_ironflesh, "$temp"),
        (store_skill_level, reg2, skl_athletics, "$temp"),
        (store_skill_level, reg3, skl_shield, "$temp"),
        (store_skill_level, reg4, skl_riding, "$temp"),
        (str_store_string, s4, "@{s4}^Ironflesh: {reg1}^Athletics: {reg2}^Shield: {reg3}^Riding: {reg4}^^"),
        (store_proficiency_level, reg1, "$temp", wpt_archery),
        (store_proficiency_level, reg2, "$temp", wpt_crossbow),
        (store_proficiency_level, reg3, "$temp", wpt_throwing),
        (str_store_string, s4, "@{s4}^Archery: {reg1}^Crossbows: {reg2}^Throwing: {reg3}"),
        (create_text_overlay, reg0, "@{s4}", tf_double_space),
        (position_set_x, pos1, 710),
        (position_set_y, pos1, 100),
        (overlay_set_position, reg0, pos1),
        ################

        (str_clear, s0),
        (create_text_overlay, "$g_presentation_obj_2", s0, tf_scrollable),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 50),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (position_set_x, pos1, 350),
        (position_set_y, pos1, 560),
        (overlay_set_area_size, "$g_presentation_obj_2", pos1),
        (set_container_overlay, "$g_presentation_obj_2"),

        (assign, ":pos_x", 0),
        (assign, ":pos_y", 1840),
        (assign, ":slot_no", 10),
        (try_for_range, ":unused_height", 0, 24),
          (try_for_range, ":unused_width", 0, 4),
            (create_mesh_overlay, reg1, "mesh_inv_slot"),
            (position_set_x, pos1, 800),
            (position_set_y, pos1, 800),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, ":pos_x"),
            (position_set_y, pos1, ":pos_y"),
            (overlay_set_position, reg1, pos1),
            (create_mesh_overlay, reg1, "mesh_mp_inventory_choose"),
            (position_set_x, pos1, 640),
            (position_set_y, pos1, 640),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, ":pos_x"),
            (position_set_y, pos1, ":pos_y"),
            (overlay_set_position, reg1, pos1),
            (troop_set_slot, "trp_temp_array_a", ":slot_no", reg1),
            (troop_get_inventory_slot, ":item_no", "trp_temp_array_a", ":slot_no"),
            (try_begin),
              (gt, ":item_no", -1),
              (create_mesh_overlay_with_item_id, reg1, ":item_no"),
              (position_set_x, pos1, 800),
              (position_set_y, pos1, 800),
              (overlay_set_size, reg1, pos1),
              (store_add, ":item_x", ":pos_x", 40),
              (store_add, ":item_y", ":pos_y", 40),
              (position_set_x, pos1, ":item_x"),
              (position_set_y, pos1, ":item_y"),
              (overlay_set_position, reg1, pos1),
              (troop_set_slot, "trp_temp_array_b", ":slot_no", reg1),
            (try_end),
            (val_add, ":pos_x", 80),
            (val_add, ":slot_no", 1),
          (try_end),
          (assign, ":pos_x", 0),
          (val_sub, ":pos_y", 80),
        (try_end),

        (set_container_overlay, -1),

        (create_text_overlay, reg1, "@Equipments: ", tf_vertical_align_center),
        (position_set_x, pos1, 60),
        (position_set_y, pos1, 635),
        (overlay_set_position, reg1, pos1),
        ## items

#        ####### mouse fix pos system #######
#        (call_script, "script_mouse_fix_pos_ready"),
#        ####### mouse fix pos system #######
      ]),

#    (ti_on_presentation_run,
#      [
#        ####### mouse fix pos system #######
#        (call_script, "script_mouse_fix_pos_run"),
#        ####### mouse fix pos system #######
#    ]),

    (ti_on_presentation_mouse_enter_leave,
      [
      (store_trigger_param_1, ":object"),
      (store_trigger_param_2, ":enter_leave"),

      (try_begin),
        (eq, ":enter_leave", 0),
        (try_for_range, ":slot_no", 10, 106),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_inventory_slot, ":item_no", "trp_temp_array_a", ":slot_no"),
          (try_begin),
            (gt, ":item_no", -1),
            (troop_get_slot, ":target_obj", "trp_temp_array_b", ":slot_no"),
            (overlay_get_position, pos0, ":target_obj"),
            (show_item_details, ":item_no", pos0, 100),
            (assign, "$g_current_opened_item_details", ":slot_no"),
          (try_end),
        (try_end),
      (else_try),
        (try_for_range, ":slot_no", 10, 106),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (try_begin),
            (eq, "$g_current_opened_item_details", ":slot_no"),
            (close_item_details),
          (try_end),
        (try_end),
      (try_end),
    ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (try_begin),
            (eq, "$g_presentation_next_presentation", "prsnt_faction_troop_tree"),
            (assign, "$g_presentation_next_presentation", -1),
            (try_begin),
              (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
              (store_sub, reg11, "$faction_display", "fac_kingdom_1"),
            (else_try),
              (store_sub, reg11, "$faction_display", "fac_player_supporters_faction"),
            (try_end),
            (start_presentation, "prsnt_faction_troop_tree"),
          (else_try),
            (presentation_set_duration, 0),
          (try_end),
        (try_end),
    ]),
  ]),    
# rubik CC's Presentation  

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