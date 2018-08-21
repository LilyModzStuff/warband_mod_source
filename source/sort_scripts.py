from header_common import *
from header_operations import *
from module_constants import *

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################


scripts = [

  ("get_temp_parties",
  [
    (party_template_get_slot, ":num_temp_parties", "pt_none", slot_party_template_temp_parties_made),
    (try_begin),
      (eq, ":num_temp_parties", 0),
      (set_spawn_radius, 0),
      (spawn_around_party, "p_main_party", "pt_none"),
      (assign, ":temp_party", reg0),
      (disable_party, ":temp_party"),
      (party_template_set_slot, "pt_none", slot_party_template_temp_party, ":temp_party"),
      (val_add, ":num_temp_parties"),
      (party_template_set_slot, "pt_none", slot_party_template_temp_parties_made, ":num_temp_parties"),
      
      (set_spawn_radius, 0),
      (spawn_around_party, "p_main_party", "pt_none"),
      (assign, ":temp_party_2", reg0),
      (disable_party, ":temp_party_2"),
      (party_template_set_slot, "pt_none", slot_party_template_temp_party_2, ":temp_party_2"),
      (val_add, ":num_temp_parties"),
      (party_template_set_slot, "pt_none", slot_party_template_temp_parties_made, ":num_temp_parties"),
    (else_try),
      (party_template_get_slot, ":temp_party", "pt_none", slot_party_template_temp_party),
      (party_template_get_slot, ":temp_party_2", "pt_none", slot_party_template_temp_party_2),
    (try_end),
    
    (assign, reg0, ":temp_party"),
    (assign, reg1, ":temp_party_2"),
  ]),

  ("sort_party_by_level",
  [
    (call_script, "script_get_temp_parties"),
    (assign, ":temp_party", reg0),
    (assign, ":temp_party_2", reg1),
    
    (party_clear, ":temp_party"),
    (party_clear, ":temp_party_2"),
  
    (store_script_param_1, ":party"),
    (store_script_param_2, ":skip_leader"),
    (party_get_num_companion_stacks, ":num_stacks", ":party"),
    
    #Remove all troops (excluding party leader if selected) from the party and add them to temporary parties
    (assign, ":start_pos", 0),
    (try_begin),
      (eq, ":skip_leader", 1),
      (assign, ":start_pos", 1),
    (end_try),
    (try_for_range_backwards, ":stack", ":start_pos", ":num_stacks"),
      (party_stack_get_troop_id, ":troop", ":party", ":stack"),
      
      #Move wounded troops to temp parties first
      (party_stack_get_num_wounded, ":num_wounded", ":party", ":stack"),
      (party_remove_members, ":party", ":troop", ":num_wounded"),
      (assign, ":num_moved", reg0),
      (try_begin),
        (troop_get_slot, ":is_skill_companion", ":troop", slot_troop_skill_companion),
        (eq, ":is_skill_companion", 1),
        (party_add_members, ":temp_party_2", ":troop", ":num_moved"),
        (party_wound_members, ":temp_party_2", ":troop", ":num_moved"),
      (else_try),
        (party_add_members, ":temp_party", ":troop", ":num_moved"),
        (party_wound_members, ":temp_party", ":troop", ":num_moved"),
      (try_end),
      
      #Move the remainder
      (party_stack_get_size, ":num_troops", ":party", ":stack"),
      (party_remove_members, ":party", ":troop", ":num_troops"),
      (assign, ":num_moved", reg0),
      (try_begin),
        (troop_get_slot, ":is_skill_companion", ":troop", slot_troop_skill_companion),
        (eq, ":is_skill_companion", 1),
        (party_add_members, ":temp_party_2", ":troop", ":num_moved"),
      (else_try),
        (party_add_members, ":temp_party", ":troop", ":num_moved"),
      (try_end),
    (try_end),
    
    (call_script, "script_move_troops_in_order", ":party", ":temp_party", 0),
    (call_script, "script_move_troops_unordered", ":party", ":temp_party_2", 0),
  ]),
  
  ("move_troops_in_order",
  [
    (store_script_param_1, ":destination_party"),
    (store_script_param_2, ":source_party"),
    (store_script_param, ":skip_leader", 3),
    
    (party_get_num_companion_stacks, ":num_stacks", ":source_party"),
    (assign, ":start_pos", 0),
    (try_begin),
      (eq, ":skip_leader", 1),
      (assign, ":start_pos", 1),
    (try_end),

    #In order from highest level to lowest, remove troops from source party and add them to the destination party
    (try_for_range_backwards, ":unused", ":start_pos", ":num_stacks"),
    
      #Get the highest level of the troops in source party
      (assign, ":max_level", 0),
      (party_get_num_companion_stacks, ":num_stacks", ":source_party"),
      (try_for_range, ":stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":troop", ":source_party", ":stack"),
        (store_character_level, ":level", ":troop"),
        (val_max, ":max_level", ":level"),
      (try_end),
      
      #Remove all troops with the highest level from source party and add them to the destination party
      (try_for_range_backwards, ":stack", 0, ":num_stacks"),
        #Stop if there is no more room in the destination party
        (party_get_free_companions_capacity, ":free_capacity", ":destination_party"),
        (gt, ":free_capacity", 0),
        
        #Get the troop type and check if it is one of the highest level troops
        (party_stack_get_troop_id, ":troop", ":source_party", ":stack"),
        (store_character_level, ":level", ":troop"),
        (eq, ":level", ":max_level"),
        
        #Move the wounded members
        (party_stack_get_num_wounded, ":num_wounded", ":source_party", ":stack"),
        (val_min, ":num_wounded", ":free_capacity"),
        (party_remove_members_wounded_first, ":source_party", ":troop", ":num_wounded"),
        (assign, ":num_moved", reg0),
        (party_add_members, ":destination_party", ":troop", ":num_moved"),
        (party_wound_members, ":destination_party", ":troop", ":num_moved"),
        
        #Move the remainder
        (party_get_free_companions_capacity, ":free_capacity", ":destination_party"),
        (gt, ":free_capacity", 0),
        (party_stack_get_size, ":num_troops", ":source_party", ":stack"),
        (val_min, ":num_troops", ":free_capacity"),
        (party_remove_members, ":source_party", ":troop", ":num_troops"),
        (assign, ":num_moved", reg0),
        (party_add_members, ":destination_party", ":troop", ":num_moved"),
      (try_end),
    (try_end),
  ]),
  
  ("move_troops_unordered",
  [
    (store_script_param_1, ":destination_party"),
    (store_script_param_2, ":source_party"),
    (store_script_param, ":skip_leader", 3),
    
    (party_get_num_companion_stacks, ":num_stacks", ":source_party"),
    (assign, ":start_pos", 0),
    (try_begin),
      (eq, ":skip_leader", 1),
      (assign, ":start_pos", 1),
    (try_end),
    
    #Remove all troops from source party and add them to the destination party
    (try_for_range_backwards, ":stack", ":start_pos", ":num_stacks"),
      #Stop if there is no more room in the destination party
      (party_get_free_companions_capacity, ":free_capacity", ":destination_party"),
      (gt, ":free_capacity", 0),
      
      #Get the troop type
      (party_stack_get_troop_id, ":troop", ":source_party", ":stack"),
      
      #Move the wounded members
      (party_stack_get_num_wounded, ":num_wounded", ":source_party", ":stack"),
      (val_min, ":num_wounded", ":free_capacity"),
      (party_remove_members_wounded_first, ":source_party", ":troop", ":num_wounded"),
      (assign, ":num_moved", reg0),
      (party_add_members, ":destination_party", ":troop", ":num_moved"),
      (party_wound_members, ":destination_party", ":troop", ":num_moved"),
      
      #Move the remainder
      (party_get_free_companions_capacity, ":free_capacity", ":destination_party"),
      (gt, ":free_capacity", 0),
      (party_stack_get_size, ":num_troops", ":source_party", ":stack"),
      (val_min, ":num_troops", ":free_capacity"),
      (party_remove_members, ":source_party", ":troop", ":num_troops"),
      (assign, ":num_moved", reg0),
      (party_add_members, ":destination_party", ":troop", ":num_moved"),
    (try_end),
  ]),
]