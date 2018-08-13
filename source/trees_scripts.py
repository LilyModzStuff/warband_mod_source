# Dynamic Troop Trees by Dunde, modified by Caba'drin.

from header_common import *
from header_operations import *
from module_constants import *
from header_mission_templates import *
from header_items import *
from header_presentations import *
from header_skills import *

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

scripts = [	 
# ("prsnt_culture_troop_tree",
 # [(store_script_param_1, ":culture"),
  # (store_sub, ":num", ":culture", fac_culture_1), (val_mod, ":num", 6),
  # (store_add, ":slot",  ":num","mesh_pic_arms_swadian"),
  # (create_mesh_overlay, reg0, ":slot"),
  # (store_add, ":slot", ":num", "mesh_pic_swad"),
  # (create_mesh_overlay, reg1, ":slot"),
  # (position_set_x, pos1, 180),(position_set_y, pos1, 560),
  # (position_set_x, pos2, 500),(position_set_y, pos2, 25),      
  # (position_set_x, pos3, 500),(position_set_y, pos3, 500),
  # (overlay_set_position, reg0, pos1), (overlay_set_size, reg0, pos3),      
  # (overlay_set_position, reg1, pos2), (overlay_set_size, reg1, pos3),       
  # (try_for_range, ":slot", 0, 61),
     # (troop_set_slot, "trp_temp_array_a", ":slot", 0),
     # (troop_set_slot, "trp_temp_array_b", ":slot", 0),
     # (troop_set_slot, "trp_temp_array_c", ":slot", 0),
     # (store_add, ":num", 100),
     # (troop_set_slot, "trp_temp_array_b", ":num", -1),
     # (troop_set_slot, "trp_temp_array_c", ":num", -1),
  # (try_end),
  # (faction_get_slot, ":troop_no", ":culture", slot_faction_tier_1_troop),
  # # lowest troop tiers initialization BEGIN 
  # (troop_set_slot, "trp_temp_array_a", 0, 1),           # Number of Lowest Tier Troop
  # (troop_set_slot, "trp_temp_array_a", 1, 1),           # 1 for 1st troop
  # (troop_set_slot, "trp_temp_array_b", 1, ":troop_no"), # 1st troop id
  # # lowest troop tiers initialization END 
  # (assign, ":max_tier", 0), (assign, ":no_tier", 0),
  # (try_for_range, ":tier", 1, 10),                      # Asuming that you wont make troop tree more than 10 tiers
     # (eq, ":no_tier", 0),
     # (assign, ":no_tier", 1),
     # (store_sub, ":prev_tier", ":tier", 1),
     # (store_mul, ":slot_for_prev_num", ":prev_tier", 10),
     # (store_mul, ":slot_for_num", ":tier", 10),
     # (assign, ":num", 0),
     # (troop_get_slot, ":prev_num", "trp_temp_array_a", ":slot_for_prev_num"),
     # (gt, ":prev_num", 0),
     # (val_add, ":prev_num", 1),
     # (try_for_range, ":tree_no",  1,  ":prev_num"),     
        # (store_add, ":prev_slot", ":tree_no", ":slot_for_prev_num"),
        # (troop_get_slot, ":troop_no", "trp_temp_array_b", ":prev_slot"),
        # (gt, ":troop_no", 0),
        # (troop_get_upgrade_troop, ":next_troop", ":troop_no", 0),
        # (gt, ":next_troop", 0),
        # (assign, ":no_tier", 0), 
        # (val_add, ":num", 1),
        # (troop_set_slot, "trp_temp_array_a", ":slot_for_num", ":num"),
        # (store_add, ":slot", ":slot_for_num", ":num"),
        # (troop_set_slot, "trp_temp_array_a", ":slot", ":tree_no"),
        # (troop_set_slot, "trp_temp_array_b", ":slot", ":next_troop"),
        # (troop_get_upgrade_troop, ":next_troop", ":troop_no", 1),
        # (gt, ":next_troop", 0),
        # (val_add, ":num", 1),
        # (troop_set_slot, "trp_temp_array_a", ":slot_for_num", ":num"),
        # (store_add, ":slot", ":slot_for_num", ":num"),
        # (troop_set_slot, "trp_temp_array_a", ":slot", ":tree_no"),
        # (troop_set_slot, "trp_temp_array_b", ":slot", ":next_troop"),
     # (try_end),
     # (eq, ":no_tier", 0),
     # (val_add, ":max_tier", 1),
  # (try_end),
  # (store_mul, ":max_num_tier", ":max_tier", 10), (val_add, ":max_tier", 1),
  # (troop_get_slot, ":num", "trp_temp_array_a", ":max_num_tier"),
  # (val_add, ":num", 1),
  # (try_for_range, ":tree_no", 1, ":num"),
     # (store_add, ":slot", ":max_num_tier", ":tree_no"),
     # (store_mul, ":subs", ":tree_no", troop_tree_space_y),
     # (store_sub, ":pos", working_pos_y + 35, ":subs"),
     # (troop_set_slot, "trp_temp_array_c", ":slot", ":pos"),
  # (try_end),
  # (try_for_range_backwards, ":tier", 1, ":max_tier"),
     # (store_mul, ":slot_for_num", ":tier", 10),
     # (store_sub, ":prev_tier", ":tier", 1),
     # (store_mul, ":slot_for_prev_num", ":prev_tier", 10),
     # (troop_get_slot, ":prev_num", "trp_temp_array_a", ":slot_for_prev_num"),
     # (gt, ":prev_num", 0),
     # (val_add, ":prev_num", 1),
     # (try_for_range, ":tree_no", 1, ":prev_num"),
        # (store_add, ":prev_slot", ":tree_no", ":slot_for_prev_num"),
        # (assign, ":prev_pos", 0), (assign, ":num", 0),
        # (try_for_range, ":subs", 1, 10),
           # (store_add, ":slot", ":subs", ":slot_for_num"),
           # (troop_slot_eq, "trp_temp_array_a", ":slot", ":tree_no"),
           # (troop_get_slot, ":pos", "trp_temp_array_c", ":slot"),           
           # (val_add, ":prev_pos", ":pos"),
           # (val_add, ":num", 1),
        # (try_end),
        # (gt, ":num", 0),
        # (val_div, ":prev_pos", ":num"),
        # (troop_set_slot, "trp_temp_array_c", ":prev_slot", ":prev_pos"),
     # (try_end),
     # (assign, ":pos", 999),
     # (try_for_range, ":tree_no", 1, ":prev_num"), 
        # (store_add, ":prev_slot", ":tree_no", ":slot_for_prev_num"),
        # (troop_get_slot, ":prev_pos", "trp_temp_array_c", ":prev_slot"),           
        # (gt, ":prev_pos", 0),
        # (lt, ":prev_pos", ":pos"),
        # (assign, ":pos", ":prev_pos"),
     # (try_end),        
     # (try_for_range, ":tree_no", 1, ":prev_num"), 
        # (store_add, ":prev_slot", ":tree_no", ":slot_for_prev_num"),
        # (troop_get_slot, ":prev_pos", "trp_temp_array_c", ":prev_slot"),           
        # (eq, ":prev_pos", 0),
        # (store_sub, ":prev_pos", ":pos", troop_tree_space_y),
        # (assign, ":pos", ":prev_pos"),
        # (troop_set_slot, "trp_temp_array_c", ":prev_slot", ":prev_pos"),     
     # (try_end),
  # (try_end),
  # (val_add, ":max_num_tier", 11), (troop_set_slot, "trp_temp_array_c", 100, 0), (assign, ":num",100),
  # (try_for_range, ":slot", 0,  ":max_num_tier"),
     # (troop_get_slot, ":troop_no", "trp_temp_array_b", ":slot"),
     # (gt, ":troop_no", 0),
     # (store_div, ":posx", ":slot", 10),
     # (val_mul, ":posx", troop_tree_space_x),
     # (val_add, ":posx", troop_tree_left),
     # (troop_get_slot, ":posy", "trp_temp_array_c", ":slot"),
     # (val_add, ":num", 1),
     # (call_script, "script_prsnt_upgrade_tree_troop_and_name", ":troop_no", ":posx", ":posy"),
     # (troop_set_slot, "trp_temp_array_c", ":num", reg1),
     # (troop_set_slot, "trp_temp_array_b", ":num", ":troop_no"),
     # (store_mod, ":cur_slot",  ":slot", 10),
     # (gt, ":cur_slot", 0),
     # (store_sub, ":cur_slot1", ":slot", ":cur_slot"),
     # (val_add,   ":cur_slot1", 10),     
     # (store_add, ":cur_slot2", ":cur_slot1", 10),
     # (try_for_range, ":slot2", ":cur_slot1", ":cur_slot2"), 
        # (troop_slot_ge, "trp_temp_array_b", ":slot2", 1), 
        # (troop_slot_eq, "trp_temp_array_a", ":slot2", ":cur_slot"),
        # (store_add, ":posx2", ":posx", troop_tree_space_x),
        # (store_add, ":posx1", ":posx", troop_tree_space_x/2),
        # (troop_get_slot, ":posy2", "trp_temp_array_c", ":slot2"),
        # (store_add, ":posy1", ":posy", troop_tree_space_y/2),
        # (val_add, ":posy2", troop_tree_space_y/2),
        # (call_script, "script_prsnt_lines_to", ":posx", ":posy1", ":posx2", ":posy2", title_black),
        # (val_sub, ":posy2", 3),
        # (call_script, "script_prsnt_upgrade_tree_troop_cost", ":troop_no", ":posx1", ":posy2"),
     # (try_end),     
  # (try_end),
  # (troop_set_slot, "trp_temp_array_c", 100, ":num"),  ]),
  
("prsnt_culture_troop_tree",
 [(store_script_param_1, ":culture"),
  (store_sub, ":num", ":culture", fac_culture_1), (val_mod, ":num", 6),
  (store_add, ":slot",  ":num","mesh_pic_arms_swadian"),
  (create_mesh_overlay, reg0, ":slot"),
  (store_add, ":slot", ":num", "mesh_pic_swad"),
  (create_mesh_overlay, reg1, ":slot"),
  (position_set_x, pos1, 180),(position_set_y, pos1, 560),
  (position_set_x, pos2, 500),(position_set_y, pos2, 25),      
  (position_set_x, pos3, 500),(position_set_y, pos3, 500),
  (overlay_set_position, reg0, pos1), (overlay_set_size, reg0, pos3),      
  (overlay_set_position, reg1, pos2), (overlay_set_size, reg1, pos3),       
  (try_for_range, ":slot", 0, 61),
     (troop_set_slot, "trp_temp_array_a", ":slot", 0),
     (troop_set_slot, "trp_temp_array_b", ":slot", 0),
     (troop_set_slot, "trp_temp_array_c", ":slot", 0),
     (store_add, ":num", ":slot", 100), #Caba - was missing ":slot"
     (troop_set_slot, "trp_temp_array_b", ":num", -1),
     (troop_set_slot, "trp_temp_array_c", ":num", -1),
  (try_end),
  #try-else block here to get 'troop-no' (or above) for non-kingdom trees
  (faction_get_slot, ":troop_no", ":culture", slot_faction_tier_1_troop),
  # lowest troop tiers initialization BEGIN 
  (troop_set_slot, "trp_temp_array_a", 0, 1),           # Number of Lowest Tier Troop
  (troop_set_slot, "trp_temp_array_a", 1, 1),           # 1 for 1st troop
  (troop_set_slot, "trp_temp_array_b", 1, ":troop_no"), # 1st troop id
  # lowest troop tiers initialization END 
  (assign, ":max_tier", 0), (assign, ":no_tier", 0),
  ## Calculates number of tiers--":max_tiers" and number of branches (more or less)
  (try_for_range, ":tier", 1, 10),                      # Asuming that you wont make troop tree more than 10 tiers
     (eq, ":no_tier", 0),
     (assign, ":no_tier", 1),
     (store_sub, ":prev_tier", ":tier", 1),
     (store_mul, ":slot_for_prev_num", ":prev_tier", 10),
     (store_mul, ":slot_for_num", ":tier", 10),
     (assign, ":num", 0),
     (troop_get_slot, ":prev_num", "trp_temp_array_a", ":slot_for_prev_num"),
     (gt, ":prev_num", 0),
     (val_add, ":prev_num", 1),
     (try_for_range, ":tree_no",  1,  ":prev_num"),     
        (store_add, ":prev_slot", ":tree_no", ":slot_for_prev_num"),
        (troop_get_slot, ":troop_no", "trp_temp_array_b", ":prev_slot"),
        (gt, ":troop_no", 0),
        #Caba - check for duplication
        (assign, ":end", ":tree_no"),
        (try_for_range, ":i", 1, ":end"), #check troops of this prev_tier previously looped over, be sure this troop hasn't been checked
            (store_add, ":other_prev_slot", ":i", ":slot_for_prev_num"),
            (neq, ":prev_slot", ":other_prev_slot"), #just to be sure
            (troop_slot_eq, "trp_temp_array_b", ":other_prev_slot", ":troop_no"),
            (assign, ":end", 0), #break loop, found in checked list
        (try_end),
        (neq, ":end", 0),
        #Caba - end
        (troop_get_upgrade_troop, ":next_troop", ":troop_no", 0),
        (gt, ":next_troop", 0),
        (assign, ":no_tier", 0), 
        (val_add, ":num", 1),
        (troop_set_slot, "trp_temp_array_a", ":slot_for_num", ":num"),
        (store_add, ":slot", ":slot_for_num", ":num"),
        (troop_set_slot, "trp_temp_array_a", ":slot", ":tree_no"),
        (troop_set_slot, "trp_temp_array_b", ":slot", ":next_troop"),
        (troop_get_upgrade_troop, ":next_troop", ":troop_no", 1),
        (gt, ":next_troop", 0),
        (val_add, ":num", 1),
        (troop_set_slot, "trp_temp_array_a", ":slot_for_num", ":num"),
        (store_add, ":slot", ":slot_for_num", ":num"),
        (troop_set_slot, "trp_temp_array_a", ":slot", ":tree_no"),
        (troop_set_slot, "trp_temp_array_b", ":slot", ":next_troop"),
     (try_end),
     (eq, ":no_tier", 0),
     (val_add, ":max_tier", 1),
  (try_end),
  (store_mul, ":max_num_tier", ":max_tier", 10), (val_add, ":max_tier", 1),
  (troop_get_slot, ":num", "trp_temp_array_a", ":max_num_tier"),
  (val_add, ":num", 1),
  #Calculate Y Position of last tier's branches? ???
  (try_for_range, ":tree_no", 1, ":num"),
     (store_add, ":slot", ":max_num_tier", ":tree_no"),
     (store_mul, ":subs", ":tree_no", troop_tree_space_y),
     (store_sub, ":pos", working_pos_y + 35, ":subs"),
     (troop_set_slot, "trp_temp_array_c", ":slot", ":pos"),
  (try_end),
  #Calculate Troop Y positions
  (try_for_range_backwards, ":tier", 1, ":max_tier"),
     (store_mul, ":slot_for_num", ":tier", 10),
     (store_sub, ":prev_tier", ":tier", 1),
     (store_mul, ":slot_for_prev_num", ":prev_tier", 10),
     (troop_get_slot, ":prev_num", "trp_temp_array_a", ":slot_for_prev_num"),
     (gt, ":prev_num", 0),
     (val_add, ":prev_num", 1),
     (try_for_range, ":tree_no", 1, ":prev_num"),
        (store_add, ":prev_slot", ":tree_no", ":slot_for_prev_num"),
        (assign, ":prev_pos", 0), (assign, ":num", 0),
        (try_for_range, ":subs", 1, 10),
           (store_add, ":slot", ":subs", ":slot_for_num"),
           (troop_slot_eq, "trp_temp_array_a", ":slot", ":tree_no"),
           #Caba - check for duplication - loop over past troops rather than using a troop slot (change?)
           (troop_get_slot, ":troop_no", "trp_temp_array_b", ":slot"),
           (assign, ":end", ":slot"),
           (try_for_range, ":i", 0, ":end"), #check troops of this prev_tier previously looped over, be sure this troop hasn't been checked
                (neq, ":i", ":slot"), #just to be sure
                (troop_slot_eq, "trp_temp_array_b", ":i", ":troop_no"),
                (assign, ":end", 0), #break loop, found in checked list
           (try_end),
           (neq, ":end", 0),
           #Caba - end
           (troop_get_slot, ":pos", "trp_temp_array_c", ":slot"),           
           (val_add, ":prev_pos", ":pos"),
           (val_add, ":num", 1),
        (try_end),
        (gt, ":num", 0),
        (val_div, ":prev_pos", ":num"),
        (troop_set_slot, "trp_temp_array_c", ":prev_slot", ":prev_pos"),
     (try_end),
     (assign, ":pos", 999),
     (try_for_range, ":tree_no", 1, ":prev_num"), 
        (store_add, ":prev_slot", ":tree_no", ":slot_for_prev_num"),
        (troop_get_slot, ":prev_pos", "trp_temp_array_c", ":prev_slot"),           
        (gt, ":prev_pos", 0),
        (lt, ":prev_pos", ":pos"),
        (assign, ":pos", ":prev_pos"),
     (try_end),        
     (try_for_range, ":tree_no", 1, ":prev_num"), 
        (store_add, ":prev_slot", ":tree_no", ":slot_for_prev_num"),
        (troop_get_slot, ":prev_pos", "trp_temp_array_c", ":prev_slot"),           
        (eq, ":prev_pos", 0),
        (store_sub, ":prev_pos", ":pos", troop_tree_space_y),
        (assign, ":pos", ":prev_pos"),
        (troop_set_slot, "trp_temp_array_c", ":prev_slot", ":prev_pos"),     
     (try_end),
  (try_end),
  (val_add, ":max_num_tier", 11), (troop_set_slot, "trp_temp_array_c", 100, 0), (assign, ":num",100),
  #Draw Troops, Titles - Calcuate X and position of Connecting Lines
  (try_for_range, ":slot", 0,  ":max_num_tier"),
     (troop_get_slot, ":troop_no", "trp_temp_array_b", ":slot"),
     (gt, ":troop_no", 0),
     #Caba - check for duplication - loop over past troops rather than using a troop slot (change?)
     (assign, ":end", ":slot"),
     (try_for_range, ":i", 0, ":end"), #check troops of this prev_tier previously looped over, be sure this troop hasn't been checked
        (neq, ":i", ":slot"), #just to be sure
        (troop_slot_eq, "trp_temp_array_b", ":i", ":troop_no"),
        (assign, ":end", 0), #break loop, found in checked list
     (try_end),
     (neq, ":end", 0),
     #Caba - end
     (store_div, ":posx", ":slot", 10),
     (val_mul, ":posx", troop_tree_space_x),
     (val_add, ":posx", troop_tree_left),
     (troop_get_slot, ":posy", "trp_temp_array_c", ":slot"),
     (val_add, ":num", 1),
     (call_script, "script_prsnt_upgrade_tree_troop_and_name", ":troop_no", ":posx", ":posy"),
     (troop_set_slot, "trp_temp_array_c", ":num", reg1),
     (troop_set_slot, "trp_temp_array_b", ":num", ":troop_no"),
     (store_mod, ":cur_slot",  ":slot", 10),
     (gt, ":cur_slot", 0),
     ## Draw lines to next troops, if found
     (store_sub, ":cur_slot1", ":slot", ":cur_slot"),
     (val_add,   ":cur_slot1", 10),     
     (store_add, ":cur_slot2", ":cur_slot1", 10),
     (try_for_range, ":slot2", ":cur_slot1", ":cur_slot2"), 
        (troop_slot_ge, "trp_temp_array_b", ":slot2", 1), 
        (troop_slot_eq, "trp_temp_array_a", ":slot2", ":cur_slot"),
        #Caba - check for duplication - loop over past troops rather than using a troop slot (change?)
        (troop_get_slot, ":troop_no", "trp_temp_array_b", ":slot2"),
        (assign, ":end", ":slot2"),
        (try_for_range, ":i", ":cur_slot1", ":end"), #check troops of this prev_tier previously looped over, be sure this troop hasn't been checked
            (neq, ":i", ":cur_slot1"), #just to be sure            
            (troop_slot_eq,  "trp_temp_array_b", ":i", ":troop_no"),
            (assign, ":posy_to_use", ":i"),
            (assign, ":end", 0), #break loop, found in checked list
        (try_end),
        (try_begin),
            (neq, ":end", 0),
            (assign, ":posy_to_use", ":slot2"),
        (try_end),
        #Caba - end
        (store_add, ":posx2", ":posx", troop_tree_space_x),
        (store_add, ":posx1", ":posx", troop_tree_space_x/2),
        (troop_get_slot, ":posy2", "trp_temp_array_c", ":posy_to_use"), #caba ":slot2"),
        (store_add, ":posy1", ":posy", troop_tree_space_y/2),
        (val_add, ":posy2", troop_tree_space_y/2),
        #Caba
        (try_begin),
            (neq, ":end", 0),
        #Caba - end
            (call_script, "script_prsnt_lines_to", ":posx", ":posy1", ":posx2", ":posy2", title_black),
            (val_sub, ":posy2", 3),
            (call_script, "script_prsnt_upgrade_tree_troop_cost", ":troop_no", ":posx1", ":posy2"),
        #Caba  
        (else_try),
            (val_sub, ":posy2", 20),
            (store_sub, ":posx3", ":posx2", 20),
            (call_script, "script_prsnt_lines_to", ":posx", ":posy1", ":posx3", ":posy2", title_black),
            (call_script, "script_prsnt_lines_to", ":posx3", ":posy2", ":posx2", ":posy2", title_black),
        (try_end),
        #Caba - end
     (try_end),     
  (try_end),
  (troop_set_slot, "trp_temp_array_c", 100, ":num"),  ]),
  
("prsnt_lines_to", # Drawing lines from (x1,y1) to (x2,y2), the line will be horizontal til half way, vertical and then horizontal again
 [(store_script_param, ":pos_x1", 1),
  (store_script_param, ":pos_y1", 2),
  (store_script_param, ":pos_x2", 3),
  (store_script_param, ":pos_y2", 4),
  (store_script_param, ":color", 5),
  (try_begin),
     (eq, ":pos_x1", ":pos_x2"),
     (store_sub, ":size", ":pos_y1", ":pos_y2"),
     (val_abs, ":size"),
     (val_min, ":pos_y1", ":pos_y2"),
     (call_script, "script_prsnt_lines", 4, ":size", ":pos_x1", ":pos_y1", ":color"),
  (else_try),
     (eq, ":pos_y1", ":pos_y2"),
     (store_sub, ":size", ":pos_x1", ":pos_x2"),
     (val_abs, ":size"),
     (val_min, ":pos_x1", ":pos_x2"),
     (call_script, "script_prsnt_lines", ":size", 5, ":pos_x1", ":pos_y1", ":color"),
  (else_try),
     (store_add, ":pos_x", ":pos_x1", ":pos_x2"), (val_div, ":pos_x", 2), (val_sub, ":pos_x", 6),
     (call_script, "script_prsnt_lines_to", ":pos_x1", ":pos_y1", ":pos_x",  ":pos_y1", ":color"),
     (call_script, "script_prsnt_lines_to", ":pos_x",  ":pos_y1", ":pos_x",  ":pos_y2", ":color"),
     (call_script, "script_prsnt_lines_to", ":pos_x",  ":pos_y2", ":pos_x2", ":pos_y2", ":color"),
  (try_end), ]),
  
# rubik's CC scripts BEGIN  
("prsnt_upgrade_tree_troop_and_name",
 [(store_script_param, ":troop_no", 1),
  (store_script_param, ":pos_x", 2),
  (store_script_param, ":pos_y", 3),
  (str_store_troop_name, s1, ":troop_no"),
  (create_text_overlay, reg1, "@{s1}", tf_center_justify|tf_vertical_align_center),
  (position_set_x, pos1, smaller_size),
  (position_set_y, pos1, smaller_size),
  (overlay_set_size, reg1, pos1),
  (position_set_x, pos1, ":pos_x"),
  (position_set_y, pos1, ":pos_y"),
  (overlay_set_position, reg1, pos1),
  (val_sub, ":pos_x", 52), # adjusted from 65
  #(val_add, ":pos_y", 5), # adjusted from 10
  (store_mul, ":cur_troop", ":troop_no", 2), #with weapons
  (create_image_button_overlay_with_tableau_material, reg1, -1, "tableau_game_party_window", ":cur_troop"),
  (position_set_x, pos1, troop_tree_size_x),
  (position_set_y, pos1, troop_tree_size_y),
  (overlay_set_size, reg1, pos1),
  (position_set_x, pos1, ":pos_x"),
  (position_set_y, pos1, ":pos_y"),
  (overlay_set_position, reg1, pos1), ]),
  
("prsnt_upgrade_tree_troop_cost",
 [(store_script_param, ":troop_no", 1),
  (store_script_param, ":pos_x", 2),
  (store_script_param, ":pos_y", 3),
  (call_script, "script_game_get_upgrade_cost", ":troop_no"),
  (create_text_overlay, reg1, "@{reg0}", tf_left_align|tf_vertical_align_center),
  (position_set_x, pos1, ":pos_x"),
  (position_set_y, pos1, ":pos_y"),
  (overlay_set_position, reg1, pos1),
  (position_set_x, pos1, smaller_size),
  (position_set_y, pos1, smaller_size),
  (overlay_set_size, reg1, pos1), ]),
  
("prsnt_lines",
 [(store_script_param, ":size_x", 1),
  (store_script_param, ":size_y", 2),
  (store_script_param, ":pos_x", 3),
  (store_script_param, ":pos_y", 4),
  (store_script_param, ":color", 5),
  (create_mesh_overlay, reg1, "mesh_white_plane"),
  (val_mul, ":size_x", 50),
  (val_mul, ":size_y", 50),
  (position_set_x, pos0, ":size_x"),
  (position_set_y, pos0, ":size_y"),
  (overlay_set_size, reg1, pos0),
  (position_set_x, pos0, ":pos_x"),
  (position_set_y, pos0, ":pos_y"),
  (overlay_set_position, reg1, pos0),
  (overlay_set_color, reg1, ":color"), ]),

("get_troop_max_hp",
 [(store_script_param_1, ":troop"),
  (store_skill_level, ":skill", skl_ironflesh, ":troop"),
  (store_attribute_level, ":attrib", ":troop", ca_strength),
  (val_mul, ":skill", 2),
  (val_add, ":skill", ":attrib"),
  (val_add, ":skill", 35),
  (assign, reg0, ":skill"), ]),

("copy_inventory", 
 [(store_script_param_1, ":source"),
  (store_script_param_2, ":target"),
  (troop_clear_inventory, ":target"),
  (troop_get_inventory_capacity, ":inv_cap", ":source"),
  (try_for_range, ":i_slot", 0, ":inv_cap"),
    (troop_get_inventory_slot, ":item", ":source", ":i_slot"),
    (troop_set_inventory_slot, ":target", ":i_slot", ":item"),
    (troop_get_inventory_slot_modifier, ":imod", ":source", ":i_slot"),
    (troop_set_inventory_slot_modifier, ":target", ":i_slot", ":imod"),
    (troop_inventory_slot_get_item_amount, ":amount", ":source", ":i_slot"),
    (gt, ":amount", 0),
    (troop_inventory_slot_set_item_amount, ":target", ":i_slot", ":amount"),
  (try_end), ]),
# rubik's CC scripts END    

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