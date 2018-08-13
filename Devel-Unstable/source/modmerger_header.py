# modmerger framework
# by sphere

modmerger_version = 201

# Note: the following is from Warband 1.127 module system.

from modmerger_options import *


# list of current module components
# not in use atm
mod_components = [
    "animations",
    "constants",
    "dialogs",
    "factions",
    "game_menus",
    "info",
    "info_pages",
    "items",
    "map_icons",
    "meshes",
    "mission_templates",
    "music",
    "particle_systems",
    "parties",
    "party_templates",
    "postfx",
    "presentations",
    "quests",
    "scenes",
    "scene_props",
    "scripts",
    "simple_triggers",
    "skills",
    "skins",
    "sounds",
    "strings",
    "tableau_materials",
    "triggers",
    "troops",
    "variables",
]

# these are components that do not need to be branded
mod_components0=[
    "info",
]

# These are the components requiring full import of symbols.  Currently only "constants"
mod_components1=[
   "constants",
]

# these are components which passes in variable with same name as the component name itself
mod_components2=[
    "animations",
    "dialogs",
    "game_menus",
    "info_pages",
    "items",
    "map_icons",
    "meshes",
    "particle_systems",
    "parties",
    "party_templates",
    "presentations",
    "quests",
    "scenes",
    "scene_props",
    "scripts",
    "simple_triggers",
    "skills",
    "skins",
    "sounds",
    "strings",
    "triggers",
    "troops",
]

# This is a list of components with a list of the important global variables defined in it)
mod_components3={
    #"info": ["export_dir"], # export_dir
    "variables" : ["reserved_variables"] , # reserved_variables
    "music": ["tracks"], # tracks
    "tableau_materials" : ["tableaus"] , # tableaus
    "postfx" : ["postfx_params"], # postfx_params
    "factions" :["factions","default_kingdom_relations"],
    "mission_templates": [
        "mission_templates",
        "multiplayer_server_check_belfry_movement", 
        "multiplayer_server_spawn_bots", 
        "multiplayer_server_manage_bots", 
        "multiplayer_server_check_polls", 
        "multiplayer_server_check_end_map", 
        "multiplayer_once_at_the_first_frame",
        "multiplayer_battle_window_opened",
        "common_battle_mission_start",
        "common_battle_tab_press",
        "common_battle_init_banner",
        "common_arena_fight_tab_press",
        "common_custom_battle_tab_press",
        "custom_battle_check_victory_condition",
        "custom_battle_check_defeat_condition",
        "common_battle_victory_display",
        "common_siege_question_answered",
        "common_custom_battle_question_answered",
        "common_custom_siege_init",
        "common_siege_init",
        "common_music_situation_update",
        "common_siege_ai_trigger_init",
        "common_siege_ai_trigger_init_2",
        "common_siege_ai_trigger_init_after_2_secs",
        "common_siege_defender_reinforcement_check",
        "common_siege_defender_reinforcement_archer_reposition",
        "common_siege_attacker_reinforcement_check",
        "common_siege_attacker_do_not_stall",
        "common_battle_check_friendly_kills",
        "common_battle_check_victory_condition",
        "common_battle_victory_display",
        "common_siege_refill_ammo",
        "common_siege_check_defeat_condition",
        "common_battle_order_panel",
        "common_battle_order_panel_tick",
        "common_battle_inventory",
        "common_inventory_not_available",
        "common_siege_init_ai_and_belfry",
        "common_siege_move_belfry",
        "common_siege_rotate_belfry",
        "common_siege_assign_men_to_belfry",
        "tournament_triggers",
     ],
}


# fix for mb vanilla
if module_sys_info["version"] <= 1011:
    mod_components.remove("info_pages")
    mod_components.remove("postfx")

    mod_components3["mission_templates"] = [   #1011 version
      "mission_templates",
      "common_battle_mission_start",
      "common_battle_tab_press",
      "common_arena_fight_tab_press",
      "common_custom_battle_tab_press",
      "common_battle_victory_display",
      "common_siege_question_answered",
      "common_custom_battle_question_answered",
      "common_custom_siege_init",
      "common_siege_init",
      "common_music_situation_update",
      "common_siege_ai_trigger_init",
      "common_siege_ai_trigger_init_2",
      "common_siege_ai_trigger_init_after_2_secs",
      "common_siege_defender_reinforcement_check",
      "common_siege_defender_reinforcement_archer_reposition",
      "common_siege_attacker_reinforcement_check",
      "common_siege_attacker_do_not_stall",
      "common_battle_check_friendly_kills",
      "common_battle_check_victory_condition",
      "common_battle_victory_display",
      "common_siege_refill_ammo",
      "common_siege_check_defeat_condition",
      "common_battle_order_panel",
      "common_battle_order_panel_tick",
      "common_battle_inventory",
      "common_inventory_not_available",
      "common_siege_init_ai_and_belfry",
      "common_siege_move_belfry",
      "common_siege_rotate_belfry",
      "common_siege_assign_men_to_belfry",
   ]
 


# gets the type of component on whether it is found in mod_components1 or mod_components2.  Those not found in either are returned as 0
def get_component_type(component_name):
    comp_type = 0
    
    try:
        mod_components1.index(component_name)
        comp_type  |= 1
    except ValueError:
        pass
    try:
        mod_components2.index(component_name)
        comp_type  |= 2
    except ValueError:
        pass

    try:
        mod_components3[component_name]
        comp_type  |= 4
    except KeyError:
        pass

    return comp_type