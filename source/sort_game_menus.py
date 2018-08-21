from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *
from header_modmerger import *

from module_constants import *

####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#  
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################

camp_options = [

  ("sort_troops",[],"Sort my troops by level.",
  [
   (call_script, "script_sort_party_by_level", "p_main_party", 1),
   (display_message, "@Your troops have been sorted"),
  ]),

]

garrison_options = [
  ("garrison_exchange_troops",
  [],
  "Exchange troops with the garrison",
  [
    (change_screen_exchange_members,1),
  ]),
  
  ("garrison_add_all_troops",
  [
    (assign, ":party_has_soldiers", 0),
    (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
    (try_for_range, ":stack", 1, ":num_stacks"),
      (party_stack_get_troop_id, ":troop", "p_main_party", ":stack"),
      (neg|troop_is_hero, ":troop"),
      (assign, ":party_has_soldiers", 1),
    (try_end),
    
    (eq, ":party_has_soldiers", 1),
  ],
  "Add all troops to the garrison",
  [
    (call_script, "script_move_troops_unordered", "$g_encountered_party", "p_main_party", 1),
  ]),
  
  ("garrison_add_wounded_troops",
  [
    (assign, ":party_has_wounded_soldiers", 0),
    (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
    (try_for_range, ":stack", 1, ":num_stacks"),
      (party_stack_get_troop_id, ":troop", "p_main_party", ":stack"),
      (neg|troop_is_hero, ":troop"),
      (party_stack_get_num_wounded, ":num_wounded", "p_main_party", ":stack"),
      (gt, ":num_wounded", 0),
      (assign, ":party_has_wounded_soldiers", 1),
    (try_end),
    
    (eq, ":party_has_wounded_soldiers", 1),
  ],
  "Add wounded troops to the garrison",
  [
    (call_script, "script_get_temp_parties"),
    (assign, ":temp_party", reg0),
    (party_clear, ":temp_party"),
  
    (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
    (try_for_range_backwards, ":stack", 1, ":num_stacks"),
      (party_stack_get_troop_id, ":troop", "p_main_party", ":stack"),
      (neg|troop_is_hero, ":troop"),
      (party_stack_get_num_wounded, ":num_wounded", "p_main_party", ":stack"),
      (party_remove_members_wounded_first, "p_main_party", ":troop", ":num_wounded"),
      (assign, ":num_moved", reg0),
      (party_add_members, ":temp_party", ":troop", ":num_moved"),
      (party_wound_members, ":temp_party", ":troop", ":num_moved"),
    (try_end),
    
    (call_script, "script_move_troops_unordered", "$g_encountered_party", ":temp_party", 0),
  ]),
  
  ("garrison_withdraw_all_troops",
  [
    (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
    (party_get_num_companions, ":garrison_size", "$g_encountered_party"),
    
    (gt, ":garrison_size", 0),
    (le, ":garrison_size", ":free_capacity"),
  ],
  "Withdraw all troops from the garrison",
  [
    (call_script, "script_move_troops_unordered", "p_main_party", "$g_encountered_party", 0),
  ]),
  
  ("garrison_withdraw_best_troops",
  [
    (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
    (party_get_num_companions, ":garrison_size", "$g_encountered_party"),
    
    (gt, ":garrison_size", 0),
    (gt, ":garrison_size", ":free_capacity"),
  ],
  "Withdraw the most experienced troops from the garrison",
  [
    (call_script, "script_move_troops_in_order", "p_main_party", "$g_encountered_party", 0),
  ]),
  
  ("garrison_withdraw_non_wounded_troops",
  [
    (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
    
    (assign, ":total_non_wounded", 0),
    (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
    (try_for_range, ":stack", 0, ":num_stacks"),
      (party_stack_get_troop_id, ":troop", "$g_encountered_party", ":stack"),
      (neg|troop_is_hero, ":troop"),
      (party_stack_get_size, ":num_troops", "$g_encountered_party", ":stack"),
      (party_stack_get_num_wounded, ":num_wounded", "$g_encountered_party", ":stack"),
      (store_sub, ":num_non_wounded", ":num_troops", ":num_wounded"),
      (val_add, ":total_non_wounded", ":num_non_wounded"),
    (try_end),
    
    (gt, ":total_non_wounded", 0),
    (le, ":total_non_wounded", ":free_capacity"),
  ],
  "Withdraw all combat ready troops from the garrison",
  [
    (call_script, "script_get_temp_parties"),
    (assign, ":temp_party", reg0),
    (party_clear, ":temp_party"),
    
    #First move all wounded troops into temp_party
    (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
    (try_for_range_backwards, ":stack", 0, ":num_stacks"),
      (party_stack_get_troop_id, ":troop", "$g_encountered_party", ":stack"),
      (neg|troop_is_hero, ":troop"),
      (party_stack_get_num_wounded, ":num_wounded", "$g_encountered_party", ":stack"),
      (party_remove_members_wounded_first, "$g_encountered_party", ":troop", ":num_wounded"),
      (assign, ":num_moved", reg0),
      (party_add_members, ":temp_party", ":troop", ":num_moved"),
      (party_wound_members, ":temp_party", ":troop", ":num_moved"),
    (try_end),
    
    (call_script, "script_move_troops_unordered", "p_main_party", "$g_encountered_party", 0),
    (call_script, "script_move_troops_unordered", "$g_encountered_party", ":temp_party", 0),
  ]),
  
  ("garrison_withdraw_best_non_wounded_troops",
  [
    (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
    
    (assign, ":total_non_wounded", 0),
    (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
    (try_for_range, ":stack", 0, ":num_stacks"),
      (party_stack_get_troop_id, ":troop", "$g_encountered_party", ":stack"),
      (neg|troop_is_hero, ":troop"),
      (party_stack_get_size, ":num_troops", "$g_encountered_party", ":stack"),
      (party_stack_get_num_wounded, ":num_wounded", "$g_encountered_party", ":stack"),
      (store_sub, ":num_non_wounded", ":num_troops", ":num_wounded"),
      (val_add, ":total_non_wounded", ":num_non_wounded"),
    (try_end),
    
    (gt, ":total_non_wounded", 0),
    (gt, ":total_non_wounded", ":free_capacity"),
  ],
  "Withdraw the most experienced combat ready troops from the garrison",
  [
    (call_script, "script_get_temp_parties"),
    (assign, ":temp_party", reg0),
    (party_clear, ":temp_party"),
    
    #First move all wounded troops into temp_party
    (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
    (try_for_range_backwards, ":stack", 0, ":num_stacks"),
      (party_stack_get_troop_id, ":troop", "$g_encountered_party", ":stack"),
      (neg|troop_is_hero, ":troop"),
      (party_stack_get_num_wounded, ":num_wounded", "$g_encountered_party", ":stack"),
      (party_remove_members_wounded_first, "$g_encountered_party", ":troop", ":num_wounded"),
      (assign, ":num_moved", reg0),
      (party_add_members, ":temp_party", ":troop", ":num_moved"),
      (party_wound_members, ":temp_party", ":troop", ":num_moved"),
    (try_end),
    
    (call_script, "script_move_troops_in_order", "p_main_party", "$g_encountered_party", 0),
    (call_script, "script_move_troops_unordered", "$g_encountered_party", ":temp_party", 0),
  ]),

  ("garrison_sort_troops",
  [	  
    (store_party_size_wo_prisoners, ":party_size", "$g_encountered_party"),
    (gt, ":party_size", 0),
  ],
  "Sort the garrison",
  [
    (call_script, "script_sort_party_by_level", "$g_encountered_party", 0),
    (display_message, "@Garrison sorted"),
  ]),
  
  ("garrison_return",
  [],
  "Return",
  [
    (jump_to_menu, "mnu_town"),
  ]),
]

victory_party_exchange_options = [
  ("inspect",
  [],
  "Inspect the prisoners and freed prisoners",
  [
    (change_screen_exchange_with_party, "p_temp_party"),
  ]),
  
  ("recruit_all",
  [
    (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
    (party_get_num_companions, ":num_freed_prisoners", "p_temp_party"),
    (le, ":num_freed_prisoners", ":free_capacity"),
  ],
  "Recruit all the freed prisoners",
  [
    (call_script, "script_move_troops_unordered", "p_main_party", "p_temp_party", 0),
  ]),
  
  ("recruit_best",
  [
    (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
    (party_get_num_companions, ":num_freed_prisoners", "p_temp_party"),
    (gt, ":num_freed_prisoners", ":free_capacity"),
  ],
  "Recruit the most experienced freed prisoners",
  [
    (call_script, "script_move_troops_unordered", "p_main_party", "p_temp_party", 0),
  ]),
  
  ("swap",
  [
    (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
    (party_get_num_companions, ":num_freed_prisoners", "p_temp_party"),
    (gt, ":num_freed_prisoners", ":free_capacity"),
  ],
  "Swap your lesser troops for freed prisoners",
  [
    (call_script, "script_move_troops_unordered", "p_temp_party", "p_main_party", 0),
    (call_script, "script_move_troops_in_order", "p_main_party", "p_temp_party", 0),
  ]),
  
  ("finish",
  [],
  "Finish",
  [
    (change_screen_return),
  ]),
]

def get_menu(menus, id):
  return get_object(menus, id)
  
def get_menu_option(menu, id):
  menu_options = menu[5]
  return get_object(menu_options, id)
  
def replace_menu_option(menu, old_menu_option, new_menu_option):
  replace_element(menu[5], old_menu_option, new_menu_option)
  
def add_menu_options(menu, options, bottom_offset):
  return tuple_insert_after(menu, 5, menu[5][len(menu[5]) - bottom_offset], options)
  
def add_menu_option_before(menu, option, search_option):
  return tuple_insert_before(menu, 5, ref_option, [option])

def add_menu_option_after(menu, option, search_option):
  return tuple_insert_after(menu, 5, ref_option, [option])
  
def replace_menu_operations(menu, old_operations, new_operations):
  operations = menu[4]
  replace_sublist(operations, old_operations, new_operations)
  
def replace_menu_option_consequences(menu, menu_option, old_consequences, new_consequences):
  menu_option_list = list(menu_option)
  consequences = menu_option_list[3]
  replace_sublist(consequences, old_consequences, new_consequences)
  new_menu_option = tuple(menu_option_list)
  replace_menu_option(menu, menu_option, new_menu_option)
  
def replace_menu_option_consequences_entirely(menu, menu_option, new_consequences):
  menu_option_list = list(menu_option)
  menu_option_list[3] = new_consequences
  new_menu_option = tuple(menu_option_list)
  replace_menu_option(menu, menu_option, new_menu_option)

def modmerge(var_set):
  try:
    var_name_1 = "game_menus"
    orig_menus = var_set[var_name_1]
    
    # START do your own stuff to do merging

    camp_menu = get_menu(orig_menus, "camp")
    replace_element(orig_menus, camp_menu, add_menu_options(camp_menu, camp_options, 1))
      
    manage_garrison_menu = ("manage_garrison", mnf_enable_hot_keys|mnf_scale_picture, "Manage this castle's garrison", "none", [], garrison_options)
    orig_menus.append(manage_garrison_menu)
      
    town_menu = get_menu(orig_menus, "town")
    manage_garrison = get_menu_option(town_menu, "castle_station_troops")
    new_manage_garrison_consequences = [
      (jump_to_menu, "mnu_manage_garrison"),
    ]
    replace_menu_option_consequences_entirely(town_menu, manage_garrison, new_manage_garrison_consequences)
      
    victory_party_exchange_menu = ("victory_party_exchange", 0, "You shouldn't be reading this... {s9}", "none", [], victory_party_exchange_options)
    orig_menus.append(victory_party_exchange_menu)
    
    victory_menu = get_menu(orig_menus, "total_victory")
    old_operations = [
      (change_screen_exchange_with_party, "p_temp_party"),
    ]
    new_operations = [
      (jump_to_menu, "mnu_victory_party_exchange"),
    ]
    replace_menu_operations(victory_menu, old_operations, new_operations)

    # END do your own stuff
      
  except KeyError:
      errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
      raise ValueError(errstring)