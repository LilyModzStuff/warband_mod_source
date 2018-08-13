from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *
#SB : optional menu toggles
from header_triggers import key_left_shift, key_right_shift
from module_constants import *

from compiler import *
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

game_menus = [
  ("start_game_0",menu_text_color(0xFF000000)|mnf_disable_all_keys,
  ##diplomacy begin
    "Welcome, adventurer, to Diplomacy for Mount & Blade: Warband. Before beginning the game you must create your character. Remember that in the traditional medieval society depicted in the game, war and politics are usually dominated by male members of the nobility. That does not however mean that you should not choose to play a female character, or one who is not of noble birth. Male nobles may have a somewhat easier start, but women and commoners can attain all of the same goals -- and in fact may have a much more interesting if more challenging early game.",
  ##diplomacy end
  "none",
    [],
    [
     ("continue",[],"Continue...",
       [
       #SB : randomized quick start
        (try_begin),
          (this_or_next|key_is_down, key_left_shift),
          (key_is_down, key_right_shift),
          (assign, "$g_disable_condescending_comments", 0),
          (store_random_in_range, "$character_gender", tf_male, tf_female + 1),
          (troop_set_type, "trp_player", "$character_gender"),
          (store_random_in_range, "$background_type", cb_noble, cb_priest + 1),
          (store_random_in_range, "$background_answer_2", cb2_page, dplmc_cb2_acolyte + 1),
          (store_random_in_range, "$background_answer_3", dplmc_cb3_bravo, cb3_student + 1),
          (store_random_in_range, "$background_answer_4", cb4_revenge, cb4_greed + 1),
          (str_store_string, s13, "@Perhaps you have forgotten the face of your father."),
          (jump_to_menu, "mnu_choose_skill"),
        (else_try),
          (jump_to_menu, "mnu_start_game_1"),
        (try_end),
        ]
       ),
      ("go_back",[],"Go back",
       [
         (change_screen_quit),
       ]),
    ]
  ),

  ("start_phase_2",mnf_disable_all_keys,
    "You hear about Calradia, a land torn between rival kingdoms battling each other for supremacy,\
 a haven for knights and mercenaries, cutthroats and adventurers, all willing to risk their lives in pursuit of fortune, power, or glory...\
 In this land which holds great dangers and even greater opportunities, you believe you may leave your past behind and start a new life.\
 You feel that finally, you hold the key of your destiny in your hands, free to choose as you will,\
 and that whatever course you take, great adventures will await you. Drawn by the stories you hear about Calradia and its kingdoms, you...",
    "none",
    [
      #SB : auto-sort through inventory, get rid of duplicate armor (and add them as gold)
      #weapons can have duplicates but are mostly a none issue, player might want to reroll anyway
      # (set_show_messages, 0),
      (assign, ":bonus_gold", 0),
      (troop_get_inventory_capacity, ":capacity", "trp_player"),
      (assign, ":helmet_score", -1),
      (assign, ":shield_score", -1),
      (assign, ":chest_score", -1),
      (assign, ":boots_score", -1),
      (assign, ":glove_score", -1),
      # (assign, ":weapon_score", -1),
      (try_for_range, ":i_slot", 0, ":capacity"),
        (troop_get_inventory_slot, ":item_no", "trp_player", ":i_slot"),
        (ge, ":item_no", 0),
        (item_get_type, ":itp", ":item_no"),
        # (this_or_next|is_between, ":itp", itp_type_one_handed_wpn, itp_type_goods),
        (this_or_next|eq, ":itp", itp_type_shield),
        (is_between, ":itp", itp_type_head_armor, itp_type_pistol), #skip horses, food, etc
        (troop_get_inventory_slot_modifier, ":imod_no", "trp_player", ":i_slot"),
        (call_script, "script_dplmc_troop_can_use_item", "trp_player", ":item_no", ":imod_no"),
        (eq, reg0, 1), #only parse those we can use
        (call_script, "script_dplmc_get_item_score_with_imod", ":item_no", ":imod_no"),
        (assign, ":score", reg0),
        (try_begin),
          (eq, ":itp", itp_type_head_armor),
          # (try_begin),
            # (lt, ":score", ":helmet_score"),
            # (troop_set_inventory_slot, "trp_player", ":i_slot", -1),
            # (call_script, "script_dplmc_get_item_value_with_imod", ":item_no", ":imod_no"),
            # (val_add, ":bonus_gold", reg0),
          # (else_try),
          (gt, ":score", ":helmet_score"),
          (assign, ":helmet_score", ":score"),
        (else_try),
          (eq, ":itp", itp_type_body_armor),
          (gt, ":score", ":chest_score"),
          (assign, ":chest_score", ":score"),
        (else_try),
          (eq, ":itp", itp_type_foot_armor),
          (gt, ":score", ":boots_score"),
          (assign, ":boots_score", ":score"),
        (else_try),
          (eq, ":itp", itp_type_hand_armor),
          (gt, ":score", ":glove_score"),
          (assign, ":glove_score", ":score"),
        (else_try),
          (eq, ":itp", itp_type_shield),
          (gt, ":score", ":shield_score"),
          (assign, ":shield_score", ":score"),
        (try_end),
      (try_end),
      
      (try_for_range, ":i_slot", 0, ":capacity"),
        (troop_get_inventory_slot, ":item_no", "trp_player", ":i_slot"),
        (ge, ":item_no", 0),
        (item_get_type, ":itp", ":item_no"),
        (is_between, ":itp", itp_type_head_armor, itp_type_pistol), #skip horses, food, etc
        (troop_get_inventory_slot_modifier, ":imod_no", "trp_player", ":i_slot"),
        # (call_script, "script_dplmc_troop_can_use_item", "trp_player", ":item_no", ":imod_no"),
        # (eq, reg0, 1), #only parse those we can use
        (call_script, "script_dplmc_get_item_score_with_imod", ":item_no", ":imod_no"),
        (assign, ":score", reg0),
        (try_begin),
          (eq, ":itp", itp_type_head_armor),
          (lt, ":score", ":helmet_score"),
          (assign, ":score", -1),
        (else_try),
          (eq, ":itp", itp_type_body_armor),
          (lt, ":score", ":chest_score"),
          (assign, ":score", -1),
        (else_try),
          (eq, ":itp", itp_type_foot_armor),
          (lt, ":score", ":boots_score"),
          (assign, ":score", -1),
        (else_try),
          (eq, ":itp", itp_type_hand_armor),
          (lt, ":score", ":glove_score"),
          (assign, ":score", -1),
        (else_try),
          (eq, ":itp", itp_type_shield),
          (lt, ":score", ":shield_score"),
          (assign, ":score", -1),
        (try_end),
        (eq, ":score", -1), #found a worse item
        (troop_set_inventory_slot, "trp_player", ":i_slot", -1),
        (call_script, "script_dplmc_get_item_value_with_imod", ":item_no", ":imod_no"),
        (val_add, ":bonus_gold", reg0),
      (try_end),
      (val_div, ":bonus_gold", 2),
      (troop_add_gold, "trp_player", ":bonus_gold"),
      # (set_show_messages, 1),
    ],
    [##diplomacy start+ Replace "join" with "Join" in the following
      ("town_1",[(eq, "$current_startup_quest_phase", 0),],"Join a caravan to Praven, in the Kingdom of Swadia.",
       [
         (assign, "$current_town", "p_town_6"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_praven"),
		 (jump_to_menu, "mnu_start_phase_2_5"),
#         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
#         (change_screen_return),
       ]),

      ("town_2",[(eq, "$current_startup_quest_phase", 0),],"Join a caravan to Reyvadin, in the Kingdom of the Vaegirs.",
       [
         (assign, "$current_town", "p_town_8"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_reyvadin"),
		 (jump_to_menu, "mnu_start_phase_2_5"),
#         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
#         (change_screen_return),
       ]),

      ("town_3",[(eq, "$current_startup_quest_phase", 0),],"Join a caravan to Tulga, in the Khergit Khanate.",
       [
         (assign, "$current_town", "p_town_10"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_tulga"),
		 (jump_to_menu, "mnu_start_phase_2_5"),
#         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
#         (change_screen_return),
       ]),

      ("town_4",[(eq, "$current_startup_quest_phase", 0),],"Take a ship to Sargoth, in the Kingdom of the Nords.",
       [
         (assign, "$current_town", "p_town_1"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_sargoth"),
		 (jump_to_menu, "mnu_start_phase_2_5"),
#         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
#         (change_screen_return),
       ]),

      ("town_5",[(eq, "$current_startup_quest_phase", 0),],"Take a ship to Jelkala, in the Kingdom of the Rhodoks.",
       [
         (assign, "$current_town", "p_town_5"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_jelkala"),
		 (jump_to_menu, "mnu_start_phase_2_5"),
#         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
#         (change_screen_return),
       ]),

      ("town_6",[(eq, "$current_startup_quest_phase", 0),],"Join a caravan to Shariz, in the Sarranid Sultanate.",
       [
         (assign, "$current_town", "p_town_19"),
         (assign, "$g_starting_town", "$current_town"),
         (assign, "$g_journey_string", "str_journey_to_shariz"),
		 (jump_to_menu, "mnu_start_phase_2_5"),
#         (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
#         (change_screen_return),
       ]),
##diplomacy end+ (replaced "join" with "Join")

      ("tutorial_cheat",[(eq,1,0)],"{!}CHEAT!",
       [
         (change_screen_return),
         (assign, "$cheat_mode", 1),
         (set_show_messages, 0),
		 (add_xp_to_troop, 15000, "trp_player"),
         (troop_raise_skill, "trp_player", skl_leadership, 7),
         (troop_raise_skill, "trp_player", skl_prisoner_management, 5),
         (troop_raise_skill, "trp_player", skl_inventory_management, 10),
         (party_add_members, "p_main_party", "trp_swadian_knight", 10),
         (party_add_members, "p_main_party", "trp_vaegir_knight", 10),
         (party_add_members, "p_main_party", "trp_vaegir_archer", 10),
         (party_add_members, "p_main_party", "trp_swadian_sharpshooter", 10),
         (troop_add_item, "trp_player","itm_scale_armor",0),
         (troop_add_item, "trp_player","itm_full_helm",0),

         (troop_add_item, "trp_player","itm_hafted_blade_b",0),
         (troop_add_item, "trp_player","itm_hafted_blade_a",0),
         (troop_add_item, "trp_player","itm_morningstar",0),
         (troop_add_item, "trp_player","itm_tutorial_spear",0),
         (troop_add_item, "trp_player","itm_tutorial_staff",0),
         (troop_add_item, "trp_player","itm_tutorial_staff_no_attack",0),
         (troop_add_item, "trp_player","itm_arena_lance",0),
         (troop_add_item, "trp_player","itm_practice_staff",0),
         (troop_add_item, "trp_player","itm_practice_lance",0),
         (troop_add_item, "trp_player","itm_practice_javelin",0),
         (troop_add_item, "trp_player","itm_scythe",0),
         (troop_add_item, "trp_player","itm_pitch_fork",0),
         (troop_add_item, "trp_player","itm_military_fork",0),
         (troop_add_item, "trp_player","itm_battle_fork",0),
         (troop_add_item, "trp_player","itm_boar_spear",0),
         (troop_add_item, "trp_player","itm_jousting_lance",0),
         (troop_add_item, "trp_player","itm_double_sided_lance",0),
         (troop_add_item, "trp_player","itm_glaive",0),
         (troop_add_item, "trp_player","itm_poleaxe",0),
         (troop_add_item, "trp_player","itm_polehammer",0),
         (troop_add_item, "trp_player","itm_staff",0),
         (troop_add_item, "trp_player","itm_quarter_staff",0),
         (troop_add_item, "trp_player","itm_iron_staff",0),
         (troop_add_item, "trp_player","itm_shortened_spear",0),
         (troop_add_item, "trp_player","itm_spear",0),
         (troop_add_item, "trp_player","itm_war_spear",0),
         (troop_add_item, "trp_player","itm_military_scythe",0),
         (troop_add_item, "trp_player","itm_light_lance",0),
         (troop_add_item, "trp_player","itm_lance",0),
         (troop_add_item, "trp_player","itm_heavy_lance",0),
         (troop_add_item, "trp_player","itm_great_lance",0),
         (troop_add_item, "trp_player","itm_pike",0),
         (troop_add_item, "trp_player","itm_ashwood_pike",0),
         (troop_add_item, "trp_player","itm_awlpike",0),
         (troop_add_item, "trp_player","itm_throwing_spears",0),
         (troop_add_item, "trp_player","itm_javelin",0),
         (troop_add_item, "trp_player","itm_jarid",0),

         (troop_add_item, "trp_player","itm_long_axe_b",0),

         (set_show_messages, 1),

         (try_for_range, ":cur_place", scenes_begin, scenes_end),
           (scene_set_slot, ":cur_place", slot_scene_visited, 1),
         (try_end),

         (call_script, "script_get_player_party_morale_values"),
         (party_set_morale, "p_main_party", reg0),
       ]
	   ),
    ]
  ),




  (
    "start_game_3",mnf_disable_all_keys,
    "Choose your scenario:",
    "none",
    [
      (assign, "$g_custom_battle_scenario", 0),
      (assign, "$g_custom_battle_scenario", "$g_custom_battle_scenario"),
##      #Default banners
##      (troop_set_slot, "trp_banner_background_color_array", 126, 0xFF212221),
##      (troop_set_slot, "trp_banner_background_color_array", 127, 0xFF212221),
##      (troop_set_slot, "trp_banner_background_color_array", 128, 0xFF2E3B10),
##      (troop_set_slot, "trp_banner_background_color_array", 129, 0xFF425D7B),
##      (troop_set_slot, "trp_banner_background_color_array", 130, 0xFF394608),
      ],
    [
##      ("custom_battle_scenario_1",[], "Skirmish 1",
##       [
##           (assign, "$g_custom_battle_scenario", 0),
##           (jump_to_menu, "mnu_custom_battle_2"),
##
##        ]
##       ),
####      ("custom_battle_scenario_2",[],"Siege Attack 1",
####       [
####           (assign, "$g_custom_battle_scenario", 1),
####           (jump_to_menu, "mnu_custom_battle_2"),
####
####        ]
####       ),
##      ("custom_battle_scenario_3",[],"Skirmish 2",
##       [
##           (assign, "$g_custom_battle_scenario", 1),
##           (jump_to_menu, "mnu_custom_battle_2"),
##
##        ]
##       ),
##       ("custom_battle_scenario_4",[],"Siege Defense",
##       [
##           (assign, "$g_custom_battle_scenario", 2),
##           (jump_to_menu, "mnu_custom_battle_2"),
##        ]
##       ),
##       ("custom_battle_scenario_5",[],"Skirmish 3",
##       [
##           (assign, "$g_custom_battle_scenario", 3),
##           (jump_to_menu, "mnu_custom_battle_2"),
##        ]
##       ),
##      ("custom_battle_scenario_6",[],"Siege Attack",
##       [
##           (assign, "$g_custom_battle_scenario", 4),
##           (jump_to_menu, "mnu_custom_battle_2"),
##
##        ]
##       ),
      ("go_back",[],"Go back",
       [(change_screen_quit),
        ]
		),
    ]
  ),

##  ("start_game_3",mnf_disable_all_keys,
##    "Choose your scenario:",
##    "none",
##    [
##      (assign, "$g_custom_battle_scenario", 0),
##      (assign, "$g_custom_battle_scenario", "$g_custom_battle_scenario"),
####      #Default banners
####      (troop_set_slot, "trp_banner_background_color_array", 126, 0xFF212221),
####      (troop_set_slot, "trp_banner_background_color_array", 127, 0xFF212221),
####      (troop_set_slot, "trp_banner_background_color_array", 128, 0xFF2E3B10),
####      (troop_set_slot, "trp_banner_background_color_array", 129, 0xFF425D7B),
####      (troop_set_slot, "trp_banner_background_color_array", 130, 0xFF394608),
##      ],
##    [
####      ("custom_battle_scenario_1",[], "Skirmish 1",
####       [
####           (assign, "$g_custom_battle_scenario", 0),
####           (jump_to_menu, "mnu_custom_battle_2"),
####
####        ]
####       ),
######      ("custom_battle_scenario_2",[],"Siege Attack 1",
######       [
######           (assign, "$g_custom_battle_scenario", 1),
######           (jump_to_menu, "mnu_custom_battle_2"),
######
######        ]
######       ),
####      ("custom_battle_scenario_3",[],"Skirmish 2",
####       [
####           (assign, "$g_custom_battle_scenario", 1),
####           (jump_to_menu, "mnu_custom_battle_2"),
####
####        ]
####       ),
####       ("custom_battle_scenario_4",[],"Siege Defense",
####       [
####           (assign, "$g_custom_battle_scenario", 2),
####           (jump_to_menu, "mnu_custom_battle_2"),
####        ]
####       ),
####       ("custom_battle_scenario_5",[],"Skirmish 3",
####       [
####           (assign, "$g_custom_battle_scenario", 3),
####           (jump_to_menu, "mnu_custom_battle_2"),
####        ]
####       ),
####      ("custom_battle_scenario_6",[],"Siege Attack",
####       [
####           (assign, "$g_custom_battle_scenario", 4),
####           (jump_to_menu, "mnu_custom_battle_2"),
####
####        ]
####       ),
##      ("go_back",[],"Go back",
##       [(change_screen_quit),
##        ]
##       ),
##    ]
##  ),

  (
    "tutorial",mnf_disable_all_keys,
    "You approach a field where the locals are training with weapons. You can practice here to improve your combat skills.",
    "none",
    [
      (try_begin),
        (eq, "$g_tutorial_entered", 1),
        (change_screen_quit),
      (else_try),
        (set_passage_menu, "mnu_tutorial"),
##        (try_begin),
##          (eq, "$tutorial_1_finished", 1),
##          (str_store_string, s1, "str_finished"),
##        (else_try),
##          (str_store_string, s1, "str_empty_string"),
##        (try_end),
##        (try_begin),
##          (eq, "$tutorial_2_finished", 1),
##          (str_store_string, s2, "str_finished"),
##        (else_try),
##          (str_store_string, s2, "str_empty_string"),
##        (try_end),
##        (try_begin),
##          (eq, "$tutorial_3_finished", 1),
##          (str_store_string, s3, "str_finished"),
##        (else_try),
##          (str_store_string, s3, "str_empty_string"),
##        (try_end),
##        (try_begin),
##          (eq, "$tutorial_4_finished", 1),
##          (str_store_string, s4, "str_finished"),
##        (else_try),
##          (str_store_string, s4, "str_empty_string"),
##        (try_end),
##        (try_begin),
##          (eq, "$tutorial_5_finished", 1),
##          (str_store_string, s5, "str_finished"),
##        (else_try),
##          (str_store_string, s5, "str_empty_string"),
##        (try_end),
        (assign, "$g_tutorial_entered", 1),
      (try_end),
    ],
    [
##      ("tutorial_1",
##      [(eq,1,0),],
##      "Tutorial #1: Basic movement and weapon selection. {s1}",
##      [
##        #(modify_visitors_at_site,"scn_tutorial_1"),(reset_visitors,0),
####           (set_jump_mission,"mt_tutorial_1"),
####           (jump_to_scene,"scn_tutorial_1"),(change_screen_mission)]),
##      ]),
##
##      ("tutorial_2",[(eq,1,0),],"Tutorial #2: Fighting with a shield. {s2}",[
####           (modify_visitors_at_site,"scn_tutorial_2"),(reset_visitors,0),
####           (set_visitor,1,"trp_tutorial_maceman"),
####           (set_visitor,2,"trp_tutorial_archer"),
####           (set_jump_mission,"mt_tutorial_2"),
####           (jump_to_scene,"scn_tutorial_2"),(change_screen_mission)]),
##           (modify_visitors_at_site,"scn_tutorial_training_ground"),
##           (reset_visitors, 0),
##           (set_player_troop, "trp_player"),
##           (set_visitor,0,"trp_player"),
##           (set_jump_mission,"mt_ai_training"),
##           (jump_to_scene,"scn_tutorial_training_ground"),
##           (change_screen_mission)]),
##
##      ("tutorial_3",[(eq,1,0),],"Tutorial #3: Fighting without a shield. {s3}",[
##           (modify_visitors_at_site,"scn_tutorial_3"),(reset_visitors,0),
##           (set_visitor,1,"trp_tutorial_maceman"),
##           (set_visitor,2,"trp_tutorial_swordsman"),
##           (set_jump_mission,"mt_tutorial_3"),
##           (jump_to_scene,"scn_tutorial_3"),(change_screen_mission)]),
##      ("tutorial_3b",[(eq,0,1)],"Tutorial 3 b",[(try_begin),
##                                                  (ge, "$tutorial_3_state", 12),
##                                                  (modify_visitors_at_site,"scn_tutorial_3"),(reset_visitors,0),
##                                                  (set_visitor,1,"trp_tutorial_maceman"),
##                                                  (set_visitor,2,"trp_tutorial_swordsman"),
##                                                  (set_jump_mission,"mt_tutorial_3_2"),
##                                                  (jump_to_scene,"scn_tutorial_3"),
##                                                  (change_screen_mission),
##                                                (else_try),
##                                                  (display_message,"str_door_locked",message_locked),
##                                                (try_end)], "Next level"),
##      ("tutorial_4",[(eq,1,0),],"Tutorial #4: Riding a horse. {s4}",[
##           (modify_visitors_at_site,"scn_tutorial_training_ground"),
##           (reset_visitors, 0),
##           (set_player_troop, "trp_player"),
##           (assign, "$g_player_troop", "trp_player"),
##           (troop_raise_attribute, "$g_player_troop", ca_strength, 12),
##           (troop_raise_attribute, "$g_player_troop", ca_agility, 9),
##           (troop_raise_attribute, "$g_player_troop", ca_charisma, 5),
##           (troop_raise_skill, "$g_player_troop", skl_shield, 3),
##           (troop_raise_skill, "$g_player_troop", skl_athletics, 2),
##           (troop_raise_skill, "$g_player_troop", skl_riding, 3),
##           (troop_raise_skill, "$g_player_troop", skl_power_strike, 1),
##           (troop_raise_skill, "$g_player_troop", skl_power_draw, 5),
##           (troop_raise_skill, "$g_player_troop", skl_weapon_master, 4),
##           (troop_raise_skill, "$g_player_troop", skl_ironflesh, 1),
##           (troop_raise_skill, "$g_player_troop", skl_horse_archery, 6),
##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_one_handed_weapon, 70),
##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_two_handed_weapon, 70),
##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_polearm, 70),
##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_crossbow, 70),
##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_throwing, 70),
##
##        (troop_clear_inventory, "$g_player_troop"),
##        (troop_add_item, "$g_player_troop","itm_leather_jerkin",0),
##        (troop_add_item, "$g_player_troop","itm_leather_boots",0),
##        (troop_add_item, "$g_player_troop","itm_practice_sword",0),
##        (troop_add_item, "$g_player_troop","itm_quarter_staff",0),
##        (troop_equip_items, "$g_player_troop"),
##        (set_visitor,0,"trp_player"),
##        (set_visitor,32,"trp_tutorial_fighter_1"),
##        (set_visitor,33,"trp_tutorial_fighter_2"),
##        (set_visitor,34,"trp_tutorial_fighter_3"),
##        (set_visitor,35,"trp_tutorial_fighter_4"),
##        (set_visitor,40,"trp_tutorial_master_archer"),
##        (set_visitor,41,"trp_tutorial_archer_1"),
##        (set_visitor,42,"trp_tutorial_archer_1"),
##        (set_visitor,60,"trp_tutorial_master_horseman"),
##        (set_visitor,61,"trp_tutorial_rider_1"),
##        (set_visitor,62,"trp_tutorial_rider_1"),
##        (set_visitor,63,"trp_tutorial_rider_2"),
##        (set_visitor,64,"trp_tutorial_rider_2"),
##        (set_jump_mission,"mt_tutorial_training_ground"),
##        (jump_to_scene,"scn_tutorial_training_ground"),
##        (change_screen_mission),
##      ]),
##
##      ("tutorial_5",
##      [
##        (eq,1,0),
##      ],
##      "Tutorial #5: Commanding a band of soldiers. {s5}",
##      [
##        (modify_visitors_at_site,"scn_tutorial_5"),(reset_visitors,0),
##        (set_visitor,0,"trp_player"),
##        (set_visitor,1,"trp_vaegir_infantry"),
##        (set_visitor,2,"trp_vaegir_infantry"),
##        (set_visitor,3,"trp_vaegir_infantry"),
##        (set_visitor,4,"trp_vaegir_infantry"),
##        (set_jump_mission,"mt_tutorial_5"),
##        (jump_to_scene,"scn_tutorial_5"),
##        (change_screen_mission),
##      ]),
##
##      ("tutorial_edit_custom_battle_scenes",
##      [(eq,1,0),],
##      "(NO TRANSLATE) tutorial_edit_custom_battle_scenes",
##      [
##        (jump_to_menu,"mnu_custom_battle_scene"),
##      ]),

      ("continue",[],"Continue...",
      [
        (modify_visitors_at_site,"scn_tutorial_training_ground"),
        (reset_visitors, 0),
        (set_player_troop, "trp_player"),
        (assign, "$g_player_troop", "trp_player"),
        (troop_raise_attribute, "$g_player_troop", ca_strength, 12),
        (troop_raise_attribute, "$g_player_troop", ca_agility, 9),
        (troop_raise_attribute, "$g_player_troop", ca_charisma, 5),
        (troop_raise_skill, "$g_player_troop", skl_shield, 3),
        (troop_raise_skill, "$g_player_troop", skl_athletics, 2),
        (troop_raise_skill, "$g_player_troop", skl_riding, 3),
        (troop_raise_skill, "$g_player_troop", skl_power_strike, 1),
        (troop_raise_skill, "$g_player_troop", skl_power_draw, 5),
        (troop_raise_skill, "$g_player_troop", skl_weapon_master, 4),
        (troop_raise_skill, "$g_player_troop", skl_ironflesh, 1),
        (troop_raise_skill, "$g_player_troop", skl_horse_archery, 6),
        (troop_raise_proficiency_linear, "$g_player_troop", wpt_one_handed_weapon, 70),
        (troop_raise_proficiency_linear, "$g_player_troop", wpt_two_handed_weapon, 70),
        (troop_raise_proficiency_linear, "$g_player_troop", wpt_polearm, 70),
        (troop_raise_proficiency_linear, "$g_player_troop", wpt_crossbow, 70),
        (troop_raise_proficiency_linear, "$g_player_troop", wpt_throwing, 70),

        (troop_clear_inventory, "$g_player_troop"),
        (troop_add_item, "$g_player_troop","itm_leather_jerkin",0),
        (troop_add_item, "$g_player_troop","itm_leather_boots",0),
        (troop_add_item, "$g_player_troop","itm_practice_sword",0),
        (troop_add_item, "$g_player_troop","itm_quarter_staff",0),
        (troop_equip_items, "$g_player_troop"),
        (set_visitor,0,"trp_player"),
        (set_visitor,32,"trp_tutorial_fighter_1"),
        (set_visitor,33,"trp_tutorial_fighter_2"),
        (set_visitor,34,"trp_tutorial_fighter_3"),
        (set_visitor,35,"trp_tutorial_fighter_4"),
        (set_visitor,40,"trp_tutorial_master_archer"),
        (set_visitor,41,"trp_tutorial_archer_1"),
        (set_visitor,42,"trp_tutorial_archer_1"),
        (set_visitor,60,"trp_tutorial_master_horseman"),
        (set_visitor,61,"trp_tutorial_rider_1"),
        (set_visitor,62,"trp_tutorial_rider_1"),
        (set_visitor,63,"trp_tutorial_rider_2"),
        (set_visitor,64,"trp_tutorial_rider_2"),
        (set_jump_mission,"mt_tutorial_training_ground"),
        (jump_to_scene,"scn_tutorial_training_ground"),
        (change_screen_mission),
        ]),

      ("go_back_dot",
      [],
      "Go back.",
       [
         (change_screen_quit),
       ]),
    ]
  ),

  ("reports",mnf_enable_hot_keys,
   "Character Renown: {reg5}^Honor Rating: {reg6}^Party Morale: {reg8}^Party Size Limit: {reg7}^",
   "none",
   [(call_script, "script_game_get_party_companion_limit"),
    (assign, ":party_size_limit", reg0),
    (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
    (assign, reg5, ":renown"),
    (assign, reg6, "$player_honor"),
    (assign, reg7, ":party_size_limit"),
    #(call_script, "script_get_player_party_morale_values"),
    #(party_set_morale, "p_main_party", reg0),
    (party_get_morale, reg8, "p_main_party"),

    ##diplomacy begin
    (str_clear, s1),
    (try_begin),
	    (gt, "$g_next_pay_time", 0),
      (str_store_date, s1, "$g_next_pay_time"),
      (str_store_string, s1, "@ Next pay day: {s1}"),
    (try_end),

    (try_begin),
      (is_between, "$g_player_affiliated_troop", lords_begin, kingdom_ladies_end),
      (str_store_troop_name, s5, "$g_player_affiliated_troop"),
      (str_store_string, s1, "@{s1}^^Affiliated to {s5}"),
    (try_end),
    ##diplomacy end
   ],
    [
      ("cheat_faction_orders",[(ge,"$cheat_mode",1)],"{!}Cheat: Faction orders.",
       [(jump_to_menu, "mnu_faction_orders"),
        ]
       ),
	  ("action_view_world_map",[],"View the world map.",
       [
           (start_presentation, "prsnt_world_map"),
        ]
       ),
	  
      ("view_character_report",[],"View character report.",
       [(jump_to_menu, "mnu_character_report"),
        ]
       ),
      ("view_party_size_report",[],"View party size report.",
       [(jump_to_menu, "mnu_party_size_report"),
        ]
       ),

      ("view_npc_mission_report",[],"View companion mission report.",
       [(jump_to_menu, "mnu_companion_report"),
        #SB : we modified this, reset the global to the player so it shows up first
        (assign, "$g_player_troop", "trp_player"),
        #could also jump to presentation directly
        ]
       ),

      ("view_weekly_budget_report",[],"View weekly budget report.",
       [
         (assign, "$g_apply_budget_report_to_gold", 0),
         (start_presentation, "prsnt_budget_report"),
        ]
       ),

      ("view_morale_report",[],"View party morale report.",
       [(jump_to_menu, "mnu_morale_report"),
        ]
       ),

#NPC companion changes begin
##diplomacy start
      ("lord_relations",[],"View list of known lords by relation.",
       [
         #(jump_to_menu, "mnu_lord_relations"),
         (assign, "$g_jrider_pres_called_from_menu", 1),
         (assign, "$g_character_presentation_type", 1),
         (start_presentation, "prsnt_jrider_character_relation_report"),
        ]
       ),
##diplomacy end

	##diplomacy start+ see dplmc_affiliated_family_report
     ("view_affiliated_family_report",[
		#(this_or_next|troop_slot_ge, "trp_player", slot_troop_spouse, 1),
        (this_or_next|ge,"$cheat_mode",1),
		(is_between, "$g_player_affiliated_troop", kingdoms_begin, kingdoms_end),
		], "View affiliated family member / spouse report.",
       [
           (jump_to_menu, "mnu_dplmc_affiliated_family_report"),
        ]
       ),
	##diplomacy end+

      ("courtship_relations",[],"View courtship relations.",
       [
		(jump_to_menu, "mnu_courtship_relations"),
        ]
       ),

      ("status_check",[(eq,"$cheat_mode",1)],"{!}NPC status check.",
       [
        (try_for_range, ":npc", companions_begin, companions_end),
            (main_party_has_troop, ":npc"),
            (str_store_troop_name, 4, ":npc"),
            (troop_get_slot, reg3, ":npc", slot_troop_morality_state),
            (troop_get_slot, reg4, ":npc", slot_troop_2ary_morality_state),
            (troop_get_slot, reg5, ":npc", slot_troop_personalityclash_state),
            (troop_get_slot, reg6, ":npc", slot_troop_personalityclash2_state),
            (troop_get_slot, reg7, ":npc", slot_troop_personalitymatch_state),
            (display_message, "@{!}{s4}: M{reg3}, 2M{reg4}, PC{reg5}, 2PC{reg6}, PM{reg7}"),
        (try_end),
        ]
       ),

#NPC companion changes end

	   ##diplomacy begin
     ("view_faction_relations_report",[],"View faction relations report.",
       [
           # Jrider + REPORTS PRESENTATIONS 1.2, comment to hook faction report presentation
           ##(jump_to_menu, "mnu_faction_relations_report"),
           (start_presentation, "prsnt_jrider_faction_relations_report"),
           # Jrider -
        ]
       ),
       
     ("dplmc_show_economic_report",[],"View prosperity report.",
       [
           (jump_to_menu, "mnu_dplmc_economic_report"),
        ]
       ),
       ##diplomacy end

      ("resume_travelling",[],"Resume travelling.",
       [(change_screen_return),
        ]
       ),
      ]
  ),

  (
    "custom_battle_scene",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "(NO_TRANS)",

    "none",
    [],
    [

      ("quick_battle_scene_1",[],"{!}quick_battle_scene_1",
       [
           (set_jump_mission,"mt_ai_training"),
           (jump_to_scene,"scn_quick_battle_scene_1"),(change_screen_mission)
		]
       ),
      ("quick_battle_scene_2",[],"{!}quick_battle_scene_2",
       [
           (set_jump_mission,"mt_ai_training"),
           (jump_to_scene,"scn_quick_battle_scene_2"),(change_screen_mission)
		]
       ),
      ("quick_battle_scene_3",[],"{!}quick_battle_scene_3",
       [
           (set_jump_mission,"mt_ai_training"),
           (jump_to_scene,"scn_quick_battle_scene_3"),(change_screen_mission)
		]
       ),
      ("quick_battle_scene_4",[],"{!}quick_battle_scene_4",
       [
           (set_jump_mission,"mt_ai_training"),
           (jump_to_scene,"scn_quick_battle_scene_4"),(change_screen_mission)
		]
       ),
      ("quick_battle_scene_5",[],"{!}quick_battle_scene_5",
       [
           (set_jump_mission,"mt_ai_training"),
           (jump_to_scene,"scn_quick_battle_scene_5"),(change_screen_mission)
		]
       ),

      ("go_back",[],"{!}Go back",
       [(change_screen_quit),
        ]
       ),
      ]
  ),

  #depreciated
##  (
##    "custom_battle_2",mnf_disable_all_keys,
##    "{s16}",
##    "none",
##    [
##     (assign, "$g_battle_result", 0),
##     (set_show_messages, 0),
##
##     (troop_clear_inventory, "trp_player"),
##     (troop_raise_attribute, "trp_player", ca_strength, -1000),
##     (troop_raise_attribute, "trp_player", ca_agility, -1000),
##     (troop_raise_attribute, "trp_player", ca_charisma, -1000),
##     (troop_raise_attribute, "trp_player", ca_intelligence, -1000),
##     (troop_raise_skill, "trp_player", skl_shield, -1000),
##     (troop_raise_skill, "trp_player", skl_athletics, -1000),
##     (troop_raise_skill, "trp_player", skl_riding, -1000),
##     (troop_raise_skill, "trp_player", skl_power_strike, -1000),
##     (troop_raise_skill, "trp_player", skl_power_throw, -1000),
##     (troop_raise_skill, "trp_player", skl_weapon_master, -1000),
##     (troop_raise_skill, "trp_player", skl_horse_archery, -1000),
##     (troop_raise_skill, "trp_player", skl_ironflesh, -1000),
##     (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, -10000),
##     (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, -10000),
##     (troop_raise_proficiency_linear, "trp_player", wpt_polearm, -10000),
##     (troop_raise_proficiency_linear, "trp_player", wpt_archery, -10000),
##     (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, -10000),
##     (troop_raise_proficiency_linear, "trp_player", wpt_throwing, -10000),
##
##     (reset_visitors),
####   Scene 1 Start "Shalow Lake War"
##     (try_begin),
##       (eq, "$g_custom_battle_scenario", 0),
##       (assign, "$g_player_troop", "trp_knight_1_15"),
##       (set_player_troop, "$g_player_troop"),
##
##       (assign, "$g_custom_battle_scene", "scn_quick_battle_1"),
##       (modify_visitors_at_site, "$g_custom_battle_scene"),
##       (set_visitor, 0, "$g_player_troop"),
##
###       (troop_add_item, "trp_player","itm_bascinet",0),
###       (troop_add_item, "trp_player","itm_mail_with_surcoat",0),
###       (troop_add_item, "trp_player","itm_bastard_sword_a",0),
###       (troop_add_item, "trp_player","itm_war_bow",0),
###       (troop_add_item, "trp_player","itm_khergit_arrows",0),
###       (troop_add_item, "trp_player","itm_kite_shield",0),
###       (troop_add_item, "trp_player","itm_hunter",0),
###       (troop_add_item, "trp_player","itm_mail_chausses",0),
###       (troop_equip_items, "trp_player"),
##
##       (set_visitors, 1, "trp_farmer", 13),
##       (set_visitors, 2, "trp_swadian_sergeant", 5),
##       (set_visitors, 3, "trp_swadian_sharpshooter", 4),
##       (set_visitors, 4, "trp_swadian_man_at_arms", 8),
##       (set_visitors, 5, "trp_swadian_knight", 3),
##       (set_visitors, 6, "trp_peasant_woman", 7),
##
####     Enemy
##       (set_visitors, 16, "trp_vaegir_infantry", 6),
##       (set_visitors, 17, "trp_vaegir_archer", 6),
##       (set_visitors, 18, "trp_vaegir_horseman", 4),
##       (set_visitors, 19, "trp_vaegir_knight", 10),
##       (set_visitors, 20, "trp_vaegir_guard", 6),
##       (str_store_string, s16, "str_custom_battle_1"),
##
####   SCENE 3 Start "Mountain Bandit Hunt"
##     (else_try),
##       (eq, "$g_custom_battle_scenario", 1),
##       (assign, "$g_player_troop", "trp_knight_2_5"),
##       (set_player_troop, "$g_player_troop"),
##
##       (assign, "$g_custom_battle_scene", "scn_quick_battle_3"),
##       (modify_visitors_at_site, "$g_custom_battle_scene"),
##       (set_visitor, 0, "$g_player_troop"),
##
##       (set_visitors, 1, "trp_vaegir_archer", 4),
##       (set_visitors, 2, "trp_vaegir_archer", 5),
##       (set_visitors, 3, "trp_vaegir_veteran", 4),
##       (set_visitors, 4, "trp_vaegir_horseman", 4),
##       (set_visitors, 5, "trp_vaegir_footman", 2),
##       (set_visitors, 6, "trp_vaegir_knight", 4),
#### ENEMY
##
##       (set_visitors, 16, "trp_mountain_bandit", 4),
##       (set_visitors, 17, "trp_bandit", 8),
##       (set_visitors, 18, "trp_mountain_bandit", 8),
##       (set_visitors, 19, "trp_mountain_bandit", 6),
##       (set_visitors, 20, "trp_sea_raider", 5),
##       (set_visitors, 21, "trp_mountain_bandit", 4),
##       (set_visitors, 22, "trp_brigand", 6),
##       (set_visitors, 23, "trp_sea_raider", 8),
##       (set_visitors, 25, "trp_brigand", 10),
##       (str_store_string, s16, "str_custom_battle_2"),
##
####   SCENE 4 Start "Grand Stand"
##     (else_try),
##       (eq, "$g_custom_battle_scenario", 2),
##       (assign, "$g_player_troop", "trp_kingdom_5_lady_1"),
##       (set_player_troop, "$g_player_troop"),
##
##       (troop_raise_attribute, "$g_player_troop", ca_strength, 12),
##       (troop_raise_attribute, "$g_player_troop", ca_agility, 9),
##       (troop_raise_attribute, "$g_player_troop", ca_charisma, 5),
##       (troop_raise_attribute, "$g_player_troop", ca_intelligence, 5),
##       (troop_raise_skill, "$g_player_troop", skl_shield, 3),
##       (troop_raise_skill, "$g_player_troop", skl_athletics, 2),
##       (troop_raise_skill, "$g_player_troop", skl_riding, 3),
##       (troop_raise_skill, "$g_player_troop", skl_power_strike, 4),
##       (troop_raise_skill, "$g_player_troop", skl_power_draw, 5),
##       (troop_raise_skill, "$g_player_troop", skl_weapon_master, 4),
##       (troop_raise_skill, "$g_player_troop", skl_ironflesh, 6),
##       (troop_raise_proficiency_linear, "$g_player_troop", wpt_one_handed_weapon, 100),
##       (troop_raise_proficiency_linear, "$g_player_troop", wpt_two_handed_weapon, 30),
##       (troop_raise_proficiency_linear, "$g_player_troop", wpt_polearm, 20),
##       (troop_raise_proficiency_linear, "$g_player_troop", wpt_crossbow, 110),
##       (troop_raise_proficiency_linear, "$g_player_troop", wpt_throwing, 10),
##
##       (assign, "$g_custom_battle_scene", "scn_quick_battle_4"),
##       (modify_visitors_at_site, "$g_custom_battle_scene"),
##       (set_visitor, 0, "$g_player_troop"),
##
##       (troop_clear_inventory, "$g_player_troop"),
##       (troop_add_item, "$g_player_troop","itm_helmet_with_neckguard",0),
##       (troop_add_item, "$g_player_troop","itm_plate_armor",0),
##       (troop_add_item, "$g_player_troop","itm_iron_greaves",0),
##       (troop_add_item, "$g_player_troop","itm_mail_chausses",0),
##       (troop_add_item, "$g_player_troop","itm_tab_shield_small_round_c",0),
##       (troop_add_item, "$g_player_troop","itm_heavy_crossbow",0),
##       (troop_add_item, "$g_player_troop","itm_bolts",0),
##       (troop_add_item, "$g_player_troop","itm_sword_medieval_b_small",0),
##       (troop_equip_items, "$g_player_troop"),
#### US
##       (set_visitors, 1, "trp_vaegir_infantry", 4),
##       (set_visitors, 2, "trp_vaegir_archer", 3),
##       (set_visitors, 3, "trp_vaegir_infantry", 4),
##       (set_visitors, 4, "trp_vaegir_archer", 3),
##       (set_visitors, 5, "trp_vaegir_infantry", 3),
##       (set_visitors, 6, "trp_vaegir_footman", 5),
##       (set_visitors, 7, "trp_vaegir_footman", 4),
##       (set_visitors, 8, "trp_vaegir_archer", 3),
##
#### ENEMY
##       (set_visitors, 16, "trp_swadian_footman", 8),
##       (set_visitors, 17, "trp_swadian_crossbowman", 9),
##       (set_visitors, 18, "trp_swadian_sergeant", 7),
##       (set_visitors, 19, "trp_swadian_sharpshooter", 8),
##       (set_visitors, 20, "trp_swadian_militia", 13),
##       (str_store_string, s16, "str_custom_battle_3"),
##
####   Scene 5 START
##     (else_try),
##       (eq, "$g_custom_battle_scenario", 3),
##       (assign, "$g_player_troop", "trp_knight_1_10"),
##       (set_player_troop, "$g_player_troop"),
##
##       (assign, "$g_custom_battle_scene", "scn_quick_battle_5"),
##       (modify_visitors_at_site, "$g_custom_battle_scene"),
##       (set_visitor, 0, "$g_player_troop"),
##
#### US
##       (set_visitors, 1, "trp_swadian_knight", 3),
##       (set_visitors, 2, "trp_swadian_sergeant", 4),
##       (set_visitors, 3, "trp_swadian_sharpshooter", 8),
##       (set_visitors, 4, "trp_swadian_man_at_arms", 8),
##       (set_visitors, 5, "trp_swadian_knight", 2),
##
####     enemy
##       (set_visitors, 16, "trp_vaegir_infantry", 8),
##       (set_visitors, 17, "trp_vaegir_archer", 10),
##       (set_visitors, 18, "trp_vaegir_horseman", 4),
##       (set_visitors, 19, "trp_vaegir_knight", 10),
##       (set_visitors, 20, "trp_vaegir_guard", 7),
##       (str_store_string, s16, "str_custom_battle_4"),
##
##     (else_try),
##       (eq, "$g_custom_battle_scenario", 4),
##
####       (assign, "$g_custom_battle_scene", "scn_quick_battle_6"),
##       (assign, "$g_custom_battle_scene", "scn_quick_battle_7"),
##
###   Player Wear
##       (assign, "$g_player_troop", "trp_knight_4_9"),
##       (set_player_troop, "$g_player_troop"),
##
##       (modify_visitors_at_site, "$g_custom_battle_scene"),
##       (set_visitor, 0, "$g_player_troop"),
##
##       (set_visitors, 1, "trp_nord_archer", 4),
##       (set_visitors, 2, "trp_nord_archer", 4),
##       (set_visitors, 3, "trp_nord_champion", 4),
##       (set_visitors, 4, "trp_nord_veteran", 5),
##       (set_visitors, 5, "trp_nord_warrior", 5),
##       (set_visitors, 6, "trp_nord_trained_footman", 8),
##
#### ENEMY
##       (set_visitors, 11, "trp_vaegir_knight", 2),
##       (set_visitors, 12, "trp_vaegir_guard", 6),
##       (set_visitors, 13, "trp_vaegir_infantry", 8),
##       (set_visitors, 14, "trp_vaegir_veteran", 10),
##       (set_visitors, 16, "trp_vaegir_skirmisher", 5),
##       (set_visitors, 17, "trp_vaegir_archer", 4),
##       (set_visitors, 18, "trp_vaegir_marksman", 2),
##       (set_visitors, 19, "trp_vaegir_skirmisher", 4),
##       (set_visitors, 20, "trp_vaegir_skirmisher", 3),
##       (set_visitors, 21, "trp_vaegir_skirmisher", 3),
##       (set_visitors, 22, "trp_vaegir_skirmisher", 3),
##       (set_visitors, 23, "trp_vaegir_archer", 2),
##       (str_store_string, s16, "str_custom_battle_5"),
##     (try_end),
##     (set_show_messages, 1),
##     ],
##
##    [
##      ("custom_battle_go",[],"Start.",
##       [(try_begin),
##          (eq, "$g_custom_battle_scenario", 2),
####          (set_jump_mission,"mt_custom_battle_siege"),
##        (else_try),
##          (eq, "$g_custom_battle_scenario", 4),
####          (set_jump_mission,"mt_custom_battle_5"),
##        (else_try),
####          (set_jump_mission,"mt_custom_battle"),
##        (try_end),
##        (jump_to_menu, "mnu_custom_battle_end"),
##        (jump_to_scene,"$g_custom_battle_scene"),
##        (change_screen_mission),
##        ]
##       ),
##      ("leave_custom_battle_2",[],"Cancel.",
##       [(jump_to_menu, "mnu_start_game_3"),
##        ]
##       ),
##    ]
##  ),


  (
    "custom_battle_end",mnf_disable_all_keys,
    "The battle is over. {s1} Your side killed {reg5} enemies and lost {reg6} troops over the battle. You personally slew {reg7} men in the fighting.",
    "none",
    [(music_set_situation, 0),
     (assign, reg5, "$g_custom_battle_team2_death_count"),
     (assign, reg6, "$g_custom_battle_team1_death_count"),
     (get_player_agent_kill_count, ":kill_count"),
     (get_player_agent_kill_count, ":wound_count", 1),
     (store_add, reg7, ":kill_count", ":wound_count"),
     (try_begin),
       (eq, "$g_battle_result", 1),
       (str_store_string, s1, "str_battle_won"),
     (else_try),
       (str_store_string, s1, "str_battle_lost"),
     (try_end),

     (try_begin),
       (ge, "$g_custom_battle_team2_death_count", 100),
       (unlock_achievement, ACHIEVEMENT_LOOK_AT_THE_BONES),
     (try_end),
     ],
    [
      ("continue",[],"Continue...",
       [(change_screen_quit),
        ]
       ),
    ]
  ),

  ("start_game_1",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Select your character's gender.",
    "none",
##diplomacy start+ Reset prejudice preferences
    [
        (assign, "$g_disable_condescending_comments", 0),
    ],
##diplomacy end+
    [
      ("start_male",[],"Male",
       [
         (troop_set_type,"trp_player", 0),
         (assign,"$character_gender", tf_male),
         (jump_to_menu,"mnu_start_character_1"),
        ]
       ),
      ("start_female",[],"Female",
       [
         (troop_set_type, "trp_player", 1),
         (assign, "$character_gender", tf_female),
##diplomacy start+
#Jump to the prejudice-level menu instead
#         (jump_to_menu, "mnu_start_character_1"),
         (jump_to_menu, "mnu_dplmc_start_select_prejudice"),
##diplomacy end+
       ]
       ),
	  ("go_back",[],"Go back",
       [
	     (jump_to_menu,"mnu_start_game_0"),
       ]),
    ]
  ),

  (
    "start_character_1",mnf_disable_all_keys,
    "You were born years ago, in a land far away. Your father was...",
    "none",
    [
    (str_clear,s10),
    (str_clear,s11),
    (str_clear,s12),
    (str_clear,s13),
    (str_clear,s14),
    (str_clear,s15),
    (assign, reg11, "$character_gender"), #SB : every string now uses reg11 for daughter/son boy/girl etc
    ],
    [
    ("start_noble",[],"An impoverished noble.",[
        (assign,"$background_type",cb_noble),
        (str_store_string,s10,"str_story_parent_noble"),
        (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_merchant",[],"A travelling merchant.",[
        (assign,"$background_type",cb_merchant),
        (str_store_string,s10,"str_story_parent_merchant"),
        (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_guard",[],"A veteran warrior.",[
        (assign,"$background_type",cb_guard),
        (str_store_string,s10,"str_story_parent_guard"),
        (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_forester",[],"A hunter.",[
        (assign,"$background_type",cb_forester),
        (str_store_string,s10,"str_story_parent_forester"),
        (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_nomad",[],"A steppe nomad.",[
        (assign,"$background_type",cb_nomad),
        (str_store_string,s10,"str_story_parent_nomad"),
        (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_thief",[],"A thief.",[
        (assign,"$background_type",cb_thief),
        (str_store_string,s10,"str_story_parent_thief"),
        (jump_to_menu,"mnu_start_character_2"),
    ]),
    #SB: could say "Your father was... The Church" instead of "A Priest/s"
    ("start_priest",[],"A fleeting memory.",[
        (assign,"$background_type",cb_priest),
        (str_store_string,s10,"str_story_parent_priest"),
        (jump_to_menu,"mnu_start_character_2"),
    ]),
    ("go_back",[],"Go back",
     [(jump_to_menu,"mnu_start_game_1"),
    ]),
    ]
  ),
  (
    "start_character_2",0,
    "{s10}^^ You started to learn about the world almost as soon as you could walk and talk. You spent your early life as...",
    "none",
    [],
    [
      ("page",[
          ],"A page at a nobleman's court.",[
            (assign,"$background_answer_2", cb2_page),
            (str_store_string,s11,"str_story_childhood_page"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
      ("apprentice",[
          ],"A craftsman's apprentice.",[
            (assign,"$background_answer_2", cb2_apprentice),
            (str_store_string,s11,"str_story_childhood_apprentice"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
      ("stockboy",[
          ],"A shop assistant.",[
            (assign,"$background_answer_2",cb2_merchants_helper),
            (str_store_string,s11,"str_story_childhood_stockboy"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
      ("urchin",[
          ],"A street urchin.",[
            (assign,"$background_answer_2",cb2_urchin),
            (str_store_string,s11,"str_story_childhood_urchin"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
      ("nomad",[
          ],"A steppe child.",[
            (assign,"$background_answer_2",cb2_steppe_child),
            (str_store_string,s11,"str_story_childhood_nomad"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),

        #SB : standardize strings as prompted
     ("mummer",[],"A mummer.",[
            (assign,"$background_answer_2",dplmc_cb2_mummer),
            (str_store_string,s11,"str_story_childhood_mummer"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
     ("courtier",[],"A courtier.",[
            (assign,"$background_answer_2",dplmc_cb2_courtier),
            (str_store_string,s11,"str_story_childhood_courtier"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
        #SB : conditional of parents being noble
     ("noble",[ #"Noble in Training" is vaguely similar to role of courtier/page, 
        #we pretend this means you were not fostered but rather educated in-situ
        (eq, "$background_type", cb_noble),
        ],"An unexpected heir.",[
            (assign,"$background_answer_2",dplmc_cb2_noble),
            (str_store_string,s11,"str_story_childhood_noble"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
     ("acolyte",[],"A cleric acolyte.",[
            (assign,"$background_answer_2",dplmc_cb2_acolyte),
            (str_store_string,s11,"str_story_childhood_acolyte"),
            (jump_to_menu,"mnu_start_character_3"),
        ]),
      ("go_back",[],"Go back.",
     [(jump_to_menu,"mnu_start_character_1"),
    ]),
    ]
  ),
  (
    "start_character_3",mnf_disable_all_keys,
    "As a {reg11?girl:boy} growing out of childhood, {s11}^^ Then, as a young adult, life changed as it always does. You became...",
    "none",
    [],
    [
    #SB : maybe restrict these two by gender like squire?
     ("bravo",[],"A travelling bravo.",[
       (assign,"$background_answer_3",dplmc_cb3_bravo),
     (str_store_string,s12,"str_story_job_bravo"),
	(jump_to_menu,"mnu_start_character_4"),
       ]),
     ("merc",[],"A sellsword in foreign lands.",[
       (assign,"$background_answer_3",dplmc_cb3_merc),
     (str_store_string,s12,"str_story_job_merc"),
	(jump_to_menu,"mnu_start_character_4"),
       ]),

      ("squire",[(eq,"$character_gender",tf_male)],"A squire.",[
        (assign,"$background_answer_3",cb3_squire),
      (str_store_string,s12,"str_story_job_squire"),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("lady",[(eq,"$character_gender",tf_female)],"A lady-in-waiting.",[
        (assign,"$background_answer_3",cb3_lady_in_waiting),
      (str_store_string,s12,"str_story_job_lady"),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("troubadour",[],"A troubadour.",[
        (assign,"$background_answer_3",cb3_troubadour),
      (str_store_string,s12,"str_story_job_troubadour"),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("student",[],"A university student.",[
        (assign,"$background_answer_3",cb3_student),
      (str_store_string,s12,"str_story_job_student"),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("peddler",[],"A goods peddler.",[
        (assign,"$background_answer_3",cb3_peddler),
      (str_store_string,s12,"str_story_job_peddler"),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("craftsman",[],"A smith.",[
        (assign,"$background_answer_3", cb3_craftsman),
      (str_store_string,s12,"str_story_job_craftsman"),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("poacher",[],"A game poacher.",[
        (assign,"$background_answer_3", cb3_poacher),
      (str_store_string,s12,"str_story_job_poacher"),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
     ("preacher",[],"An itinerant preacher.",[
       (assign,"$background_answer_3", dplmc_cb3_preacher),
     (str_store_string,s12,"str_story_job_preacher"),
	(jump_to_menu,"mnu_start_character_4"),
       ]),
      ("go_back",[],"Go back.",
       [(jump_to_menu,"mnu_start_character_2"),
        ]
       ),
    ]
  ),

  (
    "start_character_4",mnf_disable_all_keys,
    "Though the distinction felt sudden to you, somewhere along the way you had become a {reg11?woman:man}, and the whole world seemed to change around you.\
 {s12}^^But soon everything changed and you decided to strike out on your own as an adventurer. What made you take this decision was...",
    #Finally, what made you decide to strike out on your own as an adventurer?",
    "none",
    [],
    [
      ("revenge",[],"Personal revenge.",[
        (assign,"$background_answer_4", cb4_revenge),
        (str_store_string,s13,"str_story_reason_revenge"),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("death",[],"The loss of a loved one.",[
        (assign,"$background_answer_4",cb4_loss),
        (str_store_string,s13,"str_story_reason_death"),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("wanderlust",[],"Wanderlust.",[
        (assign,"$background_answer_4",cb4_wanderlust),
        (str_store_string,s13,"str_story_reason_wanderlust"),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
        #SB : condition of at least one priestly background
     ("fervor",[
        (this_or_next|eq, "$background_type", cb_priest),
        (eq, "$background_answer_2", dplmc_cb2_acolyte),
     ],"Religious fervor.",[
        (assign,"$background_answer_4",dplmc_cb4_fervor),
        (str_store_string,s13,"str_story_reason_fervor"),
        (jump_to_menu,"mnu_choose_skill"),
       ]),
      ("disown",[],"Being forced out of your home.",[
        (assign,"$background_answer_4",cb4_disown),
        (str_store_string,s13,"str_story_reason_disown"),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
     ("greed",[],"Lust for money and power.",[
        (assign,"$background_answer_4",cb4_greed),
        (str_store_string,s13,"str_story_reason_greed"),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("go_back",[],"Go back.",
       [(jump_to_menu,"mnu_start_character_3"),
        ]
       ),
    ]
  ),


  (
    "choose_skill",mnf_disable_all_keys,
    "Only you know exactly what caused you to give up your old life and become an adventurer. {s13}",
    "none",
    [(assign,"$current_string_reg",10),
	 (assign, ":difficulty", 0),

	 (try_begin),
		(eq, "$character_gender", tf_female),
		(str_store_string, s14, "str_woman"),
		(val_add, ":difficulty", 1),
	 (else_try),
		(str_store_string, s14, "str_man"),
	 (try_end),

	 (try_begin),
        (eq,"$background_type",cb_noble),
		(str_store_string, s15, "str_noble"),
		(val_sub, ":difficulty", 1),
	 (else_try),
		(str_store_string, s15, "str_common"),
	 (try_end),

	 (try_begin),
		(eq, ":difficulty", -1),
		(str_store_string, s16, "str_may_find_that_you_are_able_to_take_your_place_among_calradias_great_lords_relatively_quickly"),
	 (else_try),
		(eq, ":difficulty", 0),
		(str_store_string, s16, "str_may_face_some_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
	 (else_try),
		(eq, ":difficulty", 1),
		(str_store_string, s16, "str_may_face_great_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
	 (try_end),
	],
    [
##      ("start_swordsman",[],"Swordsmanship.",[
##        (assign, "$starting_skill", 1),
##        (str_store_string, s14, "@You are particularly talented at swordsmanship."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),
##      ("start_archer",[],"Archery.",[
##        (assign, "$starting_skill", 2),
##        (str_store_string, s14, "@You are particularly talented at archery."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),
##      ("start_medicine",[],"Medicine.",[
##        (assign, "$starting_skill", 3),
##        (str_store_string, s14, "@You are particularly talented at medicine."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),
      ("begin_adventuring",[],"Become an adventurer and ride to your destiny.",[
           (set_show_messages, 0),
           (try_begin),
             (eq, "$character_gender", tf_male),
             (troop_raise_attribute, "trp_player",ca_strength,1),
             (troop_raise_attribute, "trp_player",ca_charisma,1),
           (else_try),
             (troop_raise_attribute, "trp_player",ca_agility,1),
             (troop_raise_attribute, "trp_player",ca_intelligence,1),
           (try_end),

           (troop_raise_attribute, "trp_player",ca_strength,1),
           (troop_raise_attribute, "trp_player",ca_agility,1),
           (troop_raise_attribute, "trp_player",ca_charisma,1),

           (troop_raise_skill, "trp_player","skl_leadership",1),
           (troop_raise_skill, "trp_player","skl_riding",1),
##           (try_begin),
##             (eq, "$starting_skill", 1),
##             (troop_raise_attribute, "trp_player",ca_agility,1),
##             (troop_raise_attribute, "trp_player",ca_strength,1),
##             (troop_raise_skill, "trp_player",skl_power_strike,2),
##             (troop_raise_proficiency, "trp_player",0,30),
##             (troop_raise_proficiency, "trp_player",1,20),
##           (else_try),
##             (eq, "$starting_skill", 2),
##             (troop_raise_attribute, "trp_player",ca_strength,2),
##             (troop_raise_skill, "trp_player",skl_power_draw,2),
##             (troop_raise_proficiency, "trp_player",3,50),
##           (else_try),
##             (troop_raise_attribute, "trp_player",ca_intelligence,1),
##             (troop_raise_attribute, "trp_player",ca_charisma,1),
##             (troop_raise_skill, "trp_player",skl_first_aid,1),
##             (troop_raise_skill, "trp_player",skl_wound_treatment,1),
##             (troop_add_item, "trp_player","itm_winged_mace",0),
##             (troop_raise_proficiency, "trp_player",0,15),
##             (troop_raise_proficiency, "trp_player",1,15),
##             (troop_raise_proficiency, "trp_player",2,15),
##           (try_end),


      (try_begin),
        (eq,"$background_type",cb_noble),
        (eq,"$character_gender",tf_male),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,2),
        (troop_raise_skill, "trp_player",skl_weapon_master,1),
        (troop_raise_skill, "trp_player",skl_power_strike,1),
        (troop_raise_skill, "trp_player",skl_riding,1),
        (troop_raise_skill, "trp_player",skl_tactics,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_polearm,10),

        (troop_add_item, "trp_player","itm_tab_shield_round_a",imod_battered),
        (troop_set_slot, "trp_player", slot_troop_renown, 100),
        (call_script, "script_change_player_honor", 3),


##        (troop_add_item, "trp_player","itm_red_gambeson",imod_plain),
##        (troop_add_item, "trp_player","itm_sword",imod_plain),
##        (troop_add_item, "trp_player","itm_dagger",imod_balanced),
##        (troop_add_item, "trp_player","itm_woolen_hose",0),
##        (troop_add_item, "trp_player","itm_dried_meat",0),
##        (troop_add_item, "trp_player","itm_saddle_horse",imod_plain),
        (troop_add_gold, "trp_player", 100),
      (else_try),
        (eq,"$background_type",cb_noble),
        (eq,"$character_gender",tf_female),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
        (troop_raise_skill, "trp_player",skl_riding,2),
        (troop_raise_skill, "trp_player",skl_first_aid,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),

        (troop_set_slot, "trp_player", slot_troop_renown, 50),
        (troop_add_item, "trp_player","itm_tab_shield_round_a",imod_battered),

##        (troop_add_item, "trp_player","itm_dress",imod_sturdy),
##        (troop_add_item, "trp_player","itm_dagger",imod_watered_steel),
##        (troop_add_item, "trp_player","itm_woolen_hose",0),
##        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
##        (troop_add_item, "trp_player","itm_bolts",0),
##        (troop_add_item, "trp_player","itm_smoked_fish",0),
##        (troop_add_item, "trp_player","itm_courser",imod_spirited),
        (troop_add_gold, "trp_player", 100),
      (else_try),
        (eq,"$background_type",cb_merchant),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_riding,1),
        (troop_raise_skill, "trp_player",skl_leadership,1),
        (troop_raise_skill, "trp_player",skl_trade,2),
        (troop_raise_skill, "trp_player",skl_inventory_management,1),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),

##        (troop_add_item, "trp_player","itm_leather_jacket",0),
##        (troop_add_item, "trp_player","itm_leather_boots",0),
##        (troop_add_item, "trp_player","itm_fur_hat",0),
##        (troop_add_item, "trp_player","itm_dagger",0),
##        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
##        (troop_add_item, "trp_player","itm_bolts",0),
##        (troop_add_item, "trp_player","itm_smoked_fish",0),
##        (troop_add_item, "trp_player","itm_saddle_horse",0),
##        (troop_add_item, "trp_player","itm_sumpter_horse",0),
##        (troop_add_item, "trp_player","itm_salt",0),
##        (troop_add_item, "trp_player","itm_salt",0),
##        (troop_add_item, "trp_player","itm_salt",0),
##        (troop_add_item, "trp_player","itm_pottery",0),
##        (troop_add_item, "trp_player","itm_pottery",0),

        (troop_add_gold, "trp_player", 250),
        (troop_set_slot, "trp_player", slot_troop_renown, 20),
      (else_try),
        (eq,"$background_type",cb_guard),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player","skl_ironflesh",1),
        (troop_raise_skill, "trp_player","skl_power_strike",1),
        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_leadership",1),
        (troop_raise_skill, "trp_player","skl_trainer",1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,15),
        (troop_raise_proficiency, "trp_player",wpt_polearm,20),
        (troop_raise_proficiency, "trp_player",wpt_throwing,10),
        (troop_add_item, "trp_player","itm_tab_shield_kite_b",imod_battered),

##        (troop_add_item, "trp_player","itm_leather_jerkin",imod_ragged),
##        (troop_add_item, "trp_player","itm_skullcap",imod_rusty),
##        (troop_add_item, "trp_player","itm_spear",0),
##        (troop_add_item, "trp_player","itm_arming_sword",imod_chipped),
##        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
##        (troop_add_item, "trp_player","itm_hunter_boots",0),
##        (troop_add_item, "trp_player","itm_leather_gloves",imod_ragged),
##        (troop_add_item, "trp_player","itm_bolts",0),
##        (troop_add_item, "trp_player","itm_smoked_fish",0),
##        (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
        (troop_add_gold, "trp_player", 50),
        (troop_set_slot, "trp_player", slot_troop_renown, 10),
      (else_try),
        (eq,"$background_type",cb_forester),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,2),
        (troop_raise_skill, "trp_player","skl_power_draw",1),
        (troop_raise_skill, "trp_player","skl_tracking",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
        (troop_raise_skill, "trp_player","skl_spotting",1),
        (troop_raise_skill, "trp_player","skl_athletics",1),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_archery,30),
##        (troop_add_item, "trp_player","itm_short_bow",imod_bent),
##        (troop_add_item, "trp_player","itm_arrows",0),
##        (troop_add_item, "trp_player","itm_axe",imod_chipped),
##        (troop_add_item, "trp_player","itm_rawhide_coat",0),
##        (troop_add_item, "trp_player","itm_hide_boots",0),
##        (troop_add_item, "trp_player","itm_dried_meat",0),
##        (troop_add_item, "trp_player","itm_sumpter_horse",imod_heavy),
##        (troop_add_item, "trp_player","itm_furs",0),
        (troop_add_gold, "trp_player", 30),
      (else_try),
        (eq,"$background_type",cb_nomad),
        (eq,"$character_gender",tf_male),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_power_draw",1),
        (troop_raise_skill, "trp_player","skl_horse_archery",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
        (troop_raise_skill, "trp_player","skl_riding",2),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_archery,30),
        (troop_raise_proficiency, "trp_player",wpt_throwing,10),
        (troop_add_item, "trp_player","itm_tab_shield_small_round_a",imod_battered),
##        (troop_add_item, "trp_player","itm_javelin",imod_bent),
##        (troop_add_item, "trp_player","itm_sword_khergit_1",imod_rusty),
##        (troop_add_item, "trp_player","itm_nomad_armor",0),
##        (troop_add_item, "trp_player","itm_hide_boots",0),
##        (troop_add_item, "trp_player","itm_horse_meat",0),
##        (troop_add_item, "trp_player","itm_steppe_horse",0),
        (troop_add_gold, "trp_player", 15),
        (troop_set_slot, "trp_player", slot_troop_renown, 10),
      (else_try),
        (eq,"$background_type",cb_nomad),
        (eq,"$character_gender",tf_female),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_wound_treatment",1),
        (troop_raise_skill, "trp_player","skl_first_aid",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
        (troop_raise_skill, "trp_player","skl_riding",2),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,5),
        (troop_raise_proficiency, "trp_player",wpt_archery,20),
        (troop_raise_proficiency, "trp_player",wpt_throwing,5),
        (troop_add_item, "trp_player","itm_tab_shield_small_round_a",imod_battered),
##        (troop_add_item, "trp_player","itm_javelin",imod_bent),
##        (troop_add_item, "trp_player","itm_sickle",imod_plain),
##        (troop_add_item, "trp_player","itm_nomad_armor",0),
##        (troop_add_item, "trp_player","itm_hide_boots",0),
##        (troop_add_item, "trp_player","itm_steppe_horse",0),
##        (troop_add_item, "trp_player","itm_grain",0),
        (troop_add_gold, "trp_player", 20),
      (else_try),
        (eq,"$background_type",cb_thief),
        (troop_raise_attribute, "trp_player",ca_agility,3),
        (troop_raise_skill, "trp_player","skl_athletics",2),
        (troop_raise_skill, "trp_player","skl_power_throw",1),
        (troop_raise_skill, "trp_player","skl_inventory_management",1),
        (troop_raise_skill, "trp_player","skl_looting",1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_throwing,20),
        (troop_add_item, "trp_player","itm_throwing_knives",0),
##        (troop_add_item, "trp_player","itm_stones",0),
##        (troop_add_item, "trp_player","itm_cudgel",imod_plain),
##        (troop_add_item, "trp_player","itm_dagger",imod_rusty),
##        (troop_add_item, "trp_player","itm_shirt",imod_tattered),
##        (troop_add_item, "trp_player","itm_black_hood",imod_tattered),
##        (troop_add_item, "trp_player","itm_wrapping_boots",imod_ragged),
        (troop_add_gold, "trp_player", 25),
     (else_try), #SB : re-enable priests
       (eq,"$background_type",cb_priest),
       (troop_raise_attribute, "trp_player",ca_strength,1),
       (troop_raise_attribute, "trp_player",ca_intelligence,2),
       (troop_raise_attribute, "trp_player",ca_charisma,1),
       (troop_raise_skill, "trp_player","skl_wound_treatment",1),
       (troop_raise_skill, "trp_player","skl_leadership",1),
       (troop_raise_skill, "trp_player","skl_prisoner_management",1),
       (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
       (troop_add_item, "trp_player","itm_robe",0),
       # (troop_add_item, "trp_player","itm_wrapping_boots",0), #SB : remove most of these, cb3 adds equipment
       # (troop_add_item, "trp_player","itm_club",0),
       (troop_add_item, "trp_player","itm_grain",imod_large_bag),
       # (troop_add_item, "trp_player","itm_sumpter_horse",0), #SB: I guess it's a donkey or something
       (troop_add_gold, "trp_player", 10),
       (troop_set_slot, "trp_player", slot_troop_renown, 10),
      (try_end),

    (try_begin),
        (eq,"$background_answer_2",cb2_page),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_skill, "trp_player","skl_power_strike",1),
        (troop_raise_skill, "trp_player","skl_persuasion",1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
        (troop_raise_proficiency, "trp_player",wpt_polearm,5),
    (else_try),
        (eq,"$background_answer_2",cb2_apprentice),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_skill, "trp_player","skl_engineer",1),
        (troop_raise_skill, "trp_player","skl_trade",1),
    (else_try),
        (eq,"$background_answer_2",cb2_urchin),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_spotting",1),
        (troop_raise_skill, "trp_player","skl_looting",1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
        (troop_raise_proficiency, "trp_player",wpt_throwing,5),
    (else_try),
        (eq,"$background_answer_2",cb2_steppe_child),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_skill, "trp_player","skl_horse_archery",1),
        (troop_raise_skill, "trp_player","skl_power_throw",1),
        (troop_raise_proficiency, "trp_player",wpt_archery,15),
        (call_script,"script_change_troop_renown", "trp_player", 5),
    (else_try),
        (eq,"$background_answer_2",cb2_merchants_helper),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player","skl_inventory_management",1),
        (troop_raise_skill, "trp_player","skl_trade",1),
	(else_try),
       (eq,"$background_answer_2",dplmc_cb2_mummer),
       (troop_raise_attribute, "trp_player",ca_intelligence,1),
       (troop_raise_attribute, "trp_player",ca_charisma,1),
       # (troop_raise_skill, "trp_player",skl_leadership,1), #SB : +2 attr, +2 skill
       (troop_raise_skill, "trp_player",skl_athletics,1),
       (troop_raise_skill, "trp_player",skl_riding,1),
       (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,5),
       (troop_raise_proficiency, "trp_player",wpt_polearm,5),
       (call_script,"script_change_troop_renown", "trp_player", 15),
	(else_try),
       (eq,"$background_answer_2",dplmc_cb2_courtier),
       (troop_raise_attribute, "trp_player",ca_charisma,2), #SB : lower to +2
       (troop_raise_attribute, "trp_player",ca_agility,1),
       (troop_raise_skill, "trp_player","skl_weapon_master",1),
       (troop_raise_skill, "trp_player","skl_persuasion",1), #add this I guess from page
       (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
       # (troop_raise_proficiency, "trp_player",wpt_polearm,10), #this is way too much wpt for a courtier
       (troop_raise_proficiency, "trp_player",wpt_crossbow, 5),
       (call_script,"script_change_troop_renown", "trp_player", 20),
	(else_try),
       (eq,"$background_answer_2",dplmc_cb2_noble),
       (troop_raise_attribute, "trp_player",ca_intelligence,1),
       (troop_raise_attribute, "trp_player",ca_charisma,2),
       (troop_raise_skill, "trp_player","skl_leadership",1),
       (troop_raise_skill, "trp_player","skl_tactics",1),
       (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
       (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
       (call_script,"script_change_troop_renown", "trp_player", 15),
       #SB : add background renown/honor/rtr
       (val_add, "$player_right_to_rule", 1),
	(else_try),
       (eq,"$background_answer_2",dplmc_cb2_acolyte),
       (troop_raise_attribute, "trp_player",ca_agility,1),
       (troop_raise_attribute, "trp_player",ca_intelligence,1),
       (troop_raise_attribute, "trp_player",ca_charisma,1),
       (troop_raise_skill, "trp_player",skl_leadership,1),
       (troop_raise_skill, "trp_player",skl_surgery,1),
       (troop_raise_skill, "trp_player",skl_first_aid,1),
       (troop_raise_proficiency, "trp_player",wpt_polearm,10),
       (call_script,"script_change_troop_renown", "trp_player", 5),
	(try_end),

	(try_begin), #SB :re-enable 3x cb3 options, adding 1x body armor and weapon + food
       (eq,"$background_answer_3",dplmc_cb3_bravo),
       (troop_raise_attribute, "trp_player",ca_strength,1),
       (troop_raise_skill, "trp_player","skl_power_strike",1),
       (troop_raise_skill, "trp_player","skl_shield",1),
       (troop_add_gold, "trp_player", 10),
       # (try_begin),
       # (this_or_next|player_has_item,"itm_sword"),
       # (troop_has_item_equipped,"trp_player","itm_sword"),
       # (troop_remove_item, "trp_player","itm_sword"),
       # (try_end),
       # (try_begin),
       # (this_or_next|player_has_item,"itm_arming_sword"),
       # (troop_has_item_equipped,"trp_player","itm_arming_sword"),
       # (troop_remove_item, "trp_player","itm_arming_sword"),
       # (try_end),
       # (troop_add_item, "trp_player","itm_short_sword",0),
       # (troop_add_item, "trp_player","itm_wooden_shield",imod_battered),
       (store_random_in_range, ":shield_item", "itm_norman_shield_1", "itm_tab_shield_round_a"),
       (troop_add_item, "trp_player",":shield_item",imod_heavy),
       (store_random_in_range, ":armor_item", "itm_gambeson", "itm_tribal_warrior_outfit"),
       (store_random_in_range, ":armor_imod", imod_tattered, imod_reinforced),
       (troop_add_item, "trp_player",":armor_item",":armor_imod"),
       (troop_add_item, "trp_player", "itm_ankle_boots", 0),
       #store a random sword
       (store_random_in_range, ":weapon_item", "itm_long_voulge", "itm_mace_1"),
       (try_begin), #2+4 offset for scimitar + sarranid swords
         (lt, ":weapon_item", "itm_sword_medieval_a"),
         (val_sub, ":weapon_item", "itm_long_voulge"),
         (val_add, ":weapon_item", "itm_scimitar"),
       (try_end),
       (troop_add_item, "trp_player",":weapon_item"),
       (store_random_in_range, ":food_item", "itm_dried_meat", "itm_grain"),
       (troop_add_item, "trp_player",":food_item"),
       (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
       (troop_raise_proficiency, "trp_player",wpt_crossbow,10),
   (else_try),
       (eq,"$background_answer_3",dplmc_cb3_merc),
       (troop_raise_attribute, "trp_player",ca_agility,1),
       (troop_raise_skill, "trp_player",skl_weapon_master,1),
       (troop_raise_skill, "trp_player",skl_shield,1),
       # (try_begin),
       # (this_or_next|player_has_item,"itm_hide_boots"),
       # (troop_has_item_equipped,"trp_player","itm_hide_boots"),
       # (troop_remove_item, "trp_player","itm_hide_boots"),
       # (try_end),
       #store crap gear here, this depends on Native's item ordering
       (store_random_in_range, ":helmet_item", "itm_byzantion_helmet_a", "itm_tunic_with_green_cape"),
       (store_random_in_range, ":weapon_item", "itm_sword_medieval_a", "itm_club_with_spike_head"),
       (store_random_in_range, ":armor_item", "itm_leather_jerkin", "itm_lamellar_vest"),
       (store_random_in_range, ":boots_item", "itm_hunter_boots", "itm_splinted_greaves"),
       (store_random_in_range, ":helmet_imod", imod_tattered, imod_reinforced),
       (store_random_in_range, ":weapon_imod", imod_crude, imod_deadly),
       (store_random_in_range, ":armor_imod", imod_tattered, imod_reinforced),
       
       #SB : pick 1 set for each faction
       (store_random_in_range, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
       (try_begin),
         (eq, ":faction_no", "fac_kingdom_1"),
         (store_random_in_range, ":helmet_item", "itm_norman_helmet", "itm_kettle_hat"),
         (store_random_in_range, ":weapon_item", "itm_awlpike", "itm_bec_de_corbin_a"),
       (else_try),
         (eq, ":faction_no", "fac_kingdom_2"),
         (store_random_in_range, ":helmet_item", "itm_vaegir_fur_cap", "itm_vaegir_lamellar_helmet"),
       (else_try),
         (eq, ":faction_no", "fac_kingdom_3"), #original items
         (assign, ":helmet_item", "itm_khergit_guard_helmet"),
         (store_random_in_range, ":weapon_item", "itm_sword_khergit_1", "itm_sword_khergit_4"),
         (assign, ":boots_item","itm_mail_chausses"),
         (assign, ":helmet_imod", imod_crude),
       (else_try),
         (eq, ":faction_no", "fac_kingdom_4"), #pick axes, some are fairly expensive
         (store_random_in_range, ":weapon_item","itm_one_handed_war_axe_a", "itm_bardiche"),
         (assign, ":helmet_item", 0),
       (else_try),
         (eq, ":faction_no", "fac_kingdom_5"), #pick from the blunt range
         (store_random_in_range, ":weapon_item","itm_military_hammer", "itm_sickle"),
       (else_try),
         (eq, ":faction_no", "fac_kingdom_6"), #a fairly complete set of gear
         (troop_add_item, "trp_player","itm_sarranid_warrior_cap",imod_hardened),
         (store_random_in_range, ":boots_item", "itm_sarranid_boots_a", "itm_sarranid_boots_d"),
         (store_random_in_range, ":helmet_item", "itm_sarranid_felt_hat", "itm_sarranid_horseman_helmet"),
         # (assign, ":weapon_item","itm_sarranid_two_handed_mace_1"),
       (try_end),
       (try_begin),
         (gt, ":helmet_item", 0),
         (troop_add_item, "trp_player", ":helmet_item", ":helmet_imod"),
       (try_end),
       (try_begin),
         (gt, ":weapon_item", 0),
         (try_begin),
           (call_script, "script_dplmc_troop_can_use_item", "trp_player", ":weapon_item", ":weapon_imod"),
           (eq, reg0, 1),
           (troop_add_item, "trp_player", ":weapon_item", ":weapon_imod"),
         (else_try), #use a low-requirement common spear, or highest wpt_proficiency I guess
           (store_random_in_range, ":weapon_item", "itm_shortened_spear", "itm_light_lance"),
           (troop_add_item, "trp_player", ":weapon_item", ":weapon_imod"),
         (try_end),
       (try_end),
       (try_begin),
         (gt, ":armor_item", 0),
         (try_begin),
           (call_script, "script_dplmc_troop_can_use_item", "trp_player", ":armor_item", ":armor_imod"),
           (eq, reg0, 1),
           (troop_add_item, "trp_player", ":armor_item", ":armor_imod"),
         (else_try), #use a low-requirement gambeson
           (store_random_in_range, ":armor_item", "itm_blue_gambeson", "itm_nomad_vest"),
           (troop_add_item, "trp_player", ":armor_item", ":armor_imod"),
         (try_end),
       (try_end),
       (try_begin),
         (gt, ":boots_item", 0),
         (troop_add_item, "trp_player", ":boots_item", 0),
       (try_end),
       
       (store_random_in_range, ":food_item", "itm_cattle_meat", "itm_siege_supply"),
       (troop_add_item, "trp_player",":food_item"),
       # (troop_add_gold, "trp_player", 20),
       # (troop_raise_proficiency, "trp_player",wpt_polearm,20),
       (try_for_range, ":unused", 0, 4),
         (store_random_in_range, ":wpt", wpt_one_handed_weapon, wpt_firearm),
         (troop_raise_proficiency, "trp_player",":wpt",5), #"taught you how to wield any weapon you desired"
       (try_end),
   (else_try),
        (eq,"$background_answer_3",cb3_poacher),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_skill, "trp_player","skl_power_draw",1),
        (troop_raise_skill, "trp_player","skl_tracking",1),
        (troop_raise_skill, "trp_player","skl_spotting",1),
        (troop_raise_skill, "trp_player","skl_athletics",1),
        (troop_add_gold, "trp_player", 10),
        (troop_raise_proficiency, "trp_player",wpt_polearm,10),
        (troop_raise_proficiency, "trp_player",wpt_archery,35),

        (troop_add_item, "trp_player","itm_axe",imod_chipped),
        (troop_add_item, "trp_player","itm_rawhide_coat",0),
        (troop_add_item, "trp_player","itm_hide_boots",0),
        (troop_add_item, "trp_player","itm_hunting_bow",0),
        (troop_add_item, "trp_player","itm_barbed_arrows",0),
        (troop_add_item, "trp_player","itm_sumpter_horse",imod_heavy),
        (troop_add_item, "trp_player","itm_dried_meat",0),
        (troop_add_item, "trp_player","itm_dried_meat",0),
        (troop_add_item, "trp_player","itm_furs",0),
        (troop_add_item, "trp_player","itm_furs",0),
    (else_try),
        (eq,"$background_answer_3",cb3_craftsman),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),

        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_engineer",1),
        (troop_raise_skill, "trp_player","skl_tactics",1),
        (troop_raise_skill, "trp_player","skl_trade",1),

        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
        (troop_add_gold, "trp_player", 100),


        (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
        (troop_add_item, "trp_player","itm_coarse_tunic",0),

        (troop_add_item, "trp_player","itm_sword_medieval_b", imod_balanced),
        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
        (troop_add_item, "trp_player","itm_bolts",0),

        (troop_add_item, "trp_player","itm_tools",0),
        (troop_add_item, "trp_player","itm_saddle_horse",0),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
    (else_try),
        (eq,"$background_answer_3",cb3_peddler),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_riding",1),
        (troop_raise_skill, "trp_player","skl_trade",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
        (troop_raise_skill, "trp_player","skl_inventory_management",1),

        (troop_add_item, "trp_player","itm_leather_gloves",imod_plain),
        (troop_add_gold, "trp_player", 90),
        (troop_raise_proficiency, "trp_player",wpt_polearm,15),

        (troop_add_item, "trp_player","itm_leather_jacket",0),
        (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
        (troop_add_item, "trp_player","itm_fur_hat",0),
        (troop_add_item, "trp_player","itm_staff",0),
        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
        (troop_add_item, "trp_player","itm_bolts",0),
        (troop_add_item, "trp_player","itm_saddle_horse",0),
        (troop_add_item, "trp_player","itm_sumpter_horse",0),

        (troop_add_item, "trp_player","itm_linen",0),
        (troop_add_item, "trp_player","itm_pottery",0),
        (troop_add_item, "trp_player","itm_wool",0),
        (troop_add_item, "trp_player","itm_wool",0),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
   (else_try),
       (eq,"$background_answer_3",dplmc_cb3_preacher),
       (troop_raise_attribute, "trp_player",ca_strength,1),
       (troop_raise_attribute, "trp_player",ca_charisma,1),
       (troop_raise_skill, "trp_player","skl_shield",1),
       (troop_raise_skill, "trp_player","skl_wound_treatment",1),
       (troop_raise_skill, "trp_player","skl_first_aid",1),
       (troop_raise_skill, "trp_player","skl_surgery",1),
       (troop_add_item, "trp_player","itm_leather_gloves",imod_ragged),
       (troop_add_item, "trp_player","itm_quarter_staff",imod_heavy),
       #remove monk stuff, add pilgrim stuff
       (troop_remove_item, "trp_player", "itm_robe"),
       # (troop_remove_item, "trp_player", "itm_black_hood"),
       (troop_add_item, "trp_player", "itm_pilgrim_disguise"),
       (troop_add_item, "trp_player", "itm_pilgrim_hood"),
       (troop_add_item, "trp_player", "itm_wrapping_boots"),
       (troop_add_item, "trp_player", "itm_cheese"), #add 1x food
       (troop_add_gold, "trp_player", 10),
       (troop_raise_proficiency, "trp_player",wpt_polearm,20),
    (else_try),
        (eq,"$background_answer_3",cb3_troubadour),
        (troop_raise_attribute, "trp_player",ca_charisma,2),

        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_persuasion",1),
        (troop_raise_skill, "trp_player","skl_leadership",1),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),

        (troop_add_gold, "trp_player", 80),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,25),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,10),

        (troop_add_item, "trp_player","itm_tabard",imod_sturdy),
        (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
        (troop_add_item, "trp_player","itm_sword_medieval_a", imod_rusty),
        (troop_add_item, "trp_player","itm_hunting_crossbow", 0),
        (troop_add_item, "trp_player","itm_bolts", 0),
        (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
    (else_try),
        (eq,"$background_answer_3",cb3_squire),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_skill, "trp_player","skl_riding",1),
        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_power_strike",1),
        (troop_raise_skill, "trp_player","skl_leadership",1),

        (troop_add_gold, "trp_player", 20),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,30),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,30),
        (troop_raise_proficiency, "trp_player",wpt_polearm,30),
        (troop_raise_proficiency, "trp_player",wpt_archery,10),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,10),
        (troop_raise_proficiency, "trp_player",wpt_throwing,10),

        (troop_add_item, "trp_player","itm_leather_jerkin",imod_ragged),
        (troop_add_item, "trp_player","itm_leather_boots",imod_tattered),

        (troop_add_item, "trp_player","itm_sword_medieval_a", imod_rusty),
        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
        (troop_add_item, "trp_player","itm_bolts",0),
        (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
    (else_try),
        (eq,"$background_answer_3",cb3_lady_in_waiting),
        (eq,"$character_gender",tf_female),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,1),

        (troop_raise_skill, "trp_player","skl_persuasion",2),
        (troop_raise_skill, "trp_player","skl_riding",1),
        (troop_raise_skill, "trp_player","skl_wound_treatment",1),

        (troop_add_item, "trp_player","itm_dagger", 0),
        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
        (troop_add_item, "trp_player","itm_bolts",0),
        (troop_add_item, "trp_player","itm_courser", imod_spirited),
        (troop_add_item, "trp_player","itm_woolen_hood",imod_sturdy),
        (troop_add_item, "trp_player","itm_woolen_dress",imod_sturdy),
        (troop_add_gold, "trp_player", 100),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,15),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
    (else_try),
        (eq,"$background_answer_3",cb3_student),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),

        (troop_raise_skill, "trp_player","skl_weapon_master",1),
        (troop_raise_skill, "trp_player","skl_surgery",1),
        (troop_raise_skill, "trp_player","skl_wound_treatment",1),
        (troop_raise_skill, "trp_player","skl_persuasion",1),

        (troop_add_gold, "trp_player", 80),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_crossbow,20),

        (troop_add_item, "trp_player","itm_linen_tunic",imod_sturdy),
        (troop_add_item, "trp_player","itm_woolen_hose",0),
        (troop_add_item, "trp_player","itm_sword_medieval_a", imod_rusty),
        (troop_add_item, "trp_player","itm_hunting_crossbow", 0),
        (troop_add_item, "trp_player","itm_bolts", 0),
        (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
        (troop_add_item, "trp_player","itm_smoked_fish",0),
        (store_random_in_range, ":book_no", books_begin, books_end),
        (troop_add_item, "trp_player",":book_no",0),
    (try_end),

      (try_begin),
        (eq,"$background_answer_4",cb4_revenge),
        (troop_raise_attribute, "trp_player",ca_strength,2),
        (troop_raise_skill, "trp_player","skl_power_strike",1),
      (else_try),
        (eq,"$background_answer_4",cb4_loss),
        (troop_raise_attribute, "trp_player",ca_charisma,2),
        (troop_raise_skill, "trp_player","skl_ironflesh",1),
      (else_try),
        (eq,"$background_answer_4",cb4_wanderlust),
        (troop_raise_attribute, "trp_player",ca_agility,2),
        (troop_raise_skill, "trp_player","skl_pathfinding",1),
      (else_try),
        (eq,"$background_answer_4",dplmc_cb4_fervor),
        (troop_raise_attribute, "trp_player",ca_charisma,1),
        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
        (troop_raise_proficiency, "trp_player",wpt_throwing,10), #wait what
      (else_try),
        (eq,"$background_answer_4",cb4_disown),
        (troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_weapon_master",1),
      (else_try),
        (eq,"$background_answer_4",cb4_greed),
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_skill, "trp_player","skl_looting",1),
      (try_end),

      #SB : pre-allocate disguises
      (try_begin),
        (assign, ":disguise", disguise_pilgrim), #always available
        #farmer, acquired from not picking inappropriate noble/priestly options
        (try_begin),
          (neq, "$background_type", cb_noble),
          (neq, "$background_type", cb_priest),
          (neq, "$background_answer_2", cb2_page),
          (neq, "$background_answer_2", dplmc_cb2_courtier),
          (neq, "$background_answer_2", dplmc_cb2_noble),
          (neq, "$background_answer_2", dplmc_cb2_acolyte),
          (is_between, "$background_answer_3", cb3_poacher, dplmc_cb3_preacher),
          (val_add, ":disguise", disguise_farmer),
        (try_end),
        (try_begin),
          (this_or_next|eq, "$background_type", cb_forester),
          (this_or_next|eq, "$background_answer_2", cb2_steppe_child),
          (eq, "$background_answer_3", cb3_poacher),
          (val_add, ":disguise", disguise_hunter),
        (try_end),
        (try_begin),
          (this_or_next|eq, "$background_type", cb_merchant),
          (this_or_next|eq, "$background_answer_2", cb2_merchants_helper),
          (eq, "$background_answer_3", cb3_peddler),
          (val_add, ":disguise", disguise_merchant),
        (try_end),
        (try_begin),
          (this_or_next|eq, "$background_type", cb_guard),
          (this_or_next|eq, "$background_answer_3", dplmc_cb3_bravo),
          (this_or_next|eq, "$background_answer_3", dplmc_cb3_merc),
          (eq, "$background_answer_3", cb3_squire),
          (val_add, ":disguise", disguise_guard),
        (try_end),
        (try_begin),
          (this_or_next|eq, "$background_answer_2", dplmc_cb2_mummer),
          (eq, "$background_answer_3", cb3_troubadour),
          (val_add, ":disguise", disguise_bard),
        (try_end),
      (try_end),
      (troop_set_slot, "trp_player", slot_troop_player_disguise_sets, ":disguise"),

           (try_begin),
             (eq, "$background_type", cb_noble),
             (jump_to_menu, "mnu_auto_return"),
#normal_banner_begin
#             (start_presentation, "prsnt_banner_selection"),
#custom_banner_begin
#             (start_presentation, "prsnt_custom_banner"),
              (assign, "$g_edit_banner_troop", "trp_player"),
              (jump_to_menu, "mnu_choose_banner"),
           (else_try),
             (change_screen_return, 0),
           (try_end),
           (set_show_messages, 1),
        ]),
      ("go_back_dot",[],"Go back.",[
        (jump_to_menu,"mnu_start_character_4"),
        ]),
    ]
  ),

  (
    "past_life_explanation",mnf_disable_all_keys,
    "{s3}",
    "none",
    [
     (try_begin),
       (gt,"$current_string_reg",14),
       (assign,"$current_string_reg",10),
     (try_end),
     (str_store_string_reg,s3,"$current_string_reg"),
     (try_begin),
       (ge,"$current_string_reg",14),
       (str_store_string,s5,"@Back to the beginning..."),
     (else_try),
       (str_store_string,s5,"@View next segment..."),
     (try_end),
     ],
    [
      ("view_next",[],"{s5}",[
        (val_add,"$current_string_reg",1),
        (jump_to_menu, "mnu_past_life_explanation"),
        ]),
      ("continue",[],"Continue...",
       [
        ]),
      ("go_back_dot",[],"Go back.",[
        (jump_to_menu, "mnu_choose_skill"),
        ]),
    ]
  ),

  (
    "auto_return",0,
    "{!}This menu automatically returns to caller.",
    "none",
    [(change_screen_return, 0)],
    [
    ]
  ),
  ("morale_report",0,
   "{s1}",
   "none",
   [
     (call_script, "script_get_player_party_morale_values"),

     (assign, ":target_morale", reg0),
     (assign, reg1, "$g_player_party_morale_modifier_party_size"),
     (try_begin),
       (gt, reg1, 0),
       (str_store_string, s2, "@{!} -"),
     (else_try),
       (str_store_string, s2, "str_space"),
     (try_end),

     (assign, reg2, "$g_player_party_morale_modifier_leadership"),
     (try_begin),
       (gt, reg2, 0),
       (str_store_string, s3, "@{!} +"),
     (else_try),
       (str_store_string, s3, "str_space"),
     (try_end),

     (try_begin),
       (gt, "$g_player_party_morale_modifier_no_food", 0),
       (assign, reg7, "$g_player_party_morale_modifier_no_food"),
       (str_store_string, s5, "@^No food:  -{reg7}"),
     (else_try),
       (str_store_string, s5, "str_space"),
     (try_end),
     (assign, reg3, "$g_player_party_morale_modifier_food"),
     (try_begin),
       (gt, reg3, 0),
       (str_store_string, s4, "@{!} +"),
     (else_try),
       (str_store_string, s4, "str_space"),
     (try_end),

     (try_begin),
       (gt, "$g_player_party_morale_modifier_debt", 0),
       (assign, reg6, "$g_player_party_morale_modifier_debt"),
       (str_store_string, s6, "@^Wage debt:  -{reg6}"),
     (else_try),
       (str_store_string, s6, "str_space"),
     (try_end),

     (party_get_morale, reg5, "p_main_party"),
     (store_sub, reg4, reg5, ":target_morale"),
     (try_begin),
       (gt, reg4, 0),
       (str_store_string, s7, "@{!} +"),
     (else_try),
       (str_store_string, s7, "str_space"),
     (try_end),

     (assign, reg6, 50),

     (str_store_string, s1, "str_current_party_morale_is_reg5_current_party_morale_modifiers_are__base_morale__50_party_size_s2reg1_leadership_s3reg2_food_variety_s4reg3s5s6_recent_events_s7reg4_total__reg5___"),

     (try_for_range, ":kingdom_no", npc_kingdoms_begin, npc_kingdoms_end),
       (faction_get_slot, ":faction_morale", ":kingdom_no",  slot_faction_morale_of_player_troops),
       (val_div, ":faction_morale", 100),
       (neq, ":faction_morale", 0),
       (assign, reg6, ":faction_morale"),
       (str_store_faction_name, s9, ":kingdom_no"),
       (str_store_string, s1, "str_s1extra_morale_for_s9_troops__reg6_"),
     (try_end),
    ],
    [
      ("continue",[],"Continue...",
      [
        (jump_to_menu, "mnu_reports"),
      ]),
    ]
  ),


  ("courtship_relations",0,
   "{s1}",
   "none",
   [(str_store_string, s1, "str_courtships_in_progress_"),
    (try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
		(troop_slot_eq, ":lady", slot_troop_met, 2),
		(call_script, "script_troop_get_relation_with_troop", "trp_player", ":lady"),
		(gt, reg0, 0),
		(assign, reg3, reg0),

		(str_store_troop_name, s2, ":lady"),

		(store_current_hours, ":hours_since_last_visit"),
		(troop_get_slot, ":last_visit_hour", ":lady", slot_troop_last_talk_time),
		(val_sub, ":hours_since_last_visit", ":last_visit_hour"),
		(store_div, ":days_since_last_visit", ":hours_since_last_visit", 24),
		(assign, reg4, ":days_since_last_visit"),

		(str_store_string, s1, "str_s1_s2_relation_reg3_last_visit_reg4_days_ago"),
	(try_end),

	(str_store_string, s1, "str_s1__poems_known"),
	(try_begin),
		 (gt, "$allegoric_poem_recitations", 0),
		 (str_store_string, s1, "str_s1_storming_the_castle_of_love_allegoric"),
	(try_end),
	(try_begin),
		 (gt, "$tragic_poem_recitations", 0),
		 (str_store_string, s1, "str_s1_kais_and_layali_tragic"),
	(try_end),
	(try_begin),
		 (gt, "$comic_poem_recitations", 0),
		 (str_store_string, s1, "str_s1_a_conversation_in_the_garden_comic"),
	(try_end),
	(try_begin),
		 (gt, "$heroic_poem_recitations", 0),
		 (str_store_string, s1, "str_s1_helgered_and_kara_epic"),
	(try_end),
	(try_begin),
		 (gt, "$mystic_poem_recitations", 0),
		 (str_store_string, s1, "str_s1_a_hearts_desire_mystic"),
	(try_end),

    ],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),


  ("lord_relations",0,
   "{s1}",
   "none",
   [
    ##diplomacy start+
	 #Avoid unnecessary iterations, since below we only use slto_kingdom_hero troops.
    (assign, ":met_lord_count", 0),
    #Add support for promoted kingdom ladies.
    #(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
    (try_for_range, ":active_npc", heroes_begin, heroes_end),
      (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
      (troop_slot_ge, ":active_npc", slot_troop_met, 1),
      (val_add, ":met_lord_count", 1),
    ##diplomacy end+
		(troop_set_slot, ":active_npc", slot_troop_temp_slot, 0),
	(try_end),

	(str_clear, s1),
    ##diplomacy start+
    #Add support for promoted kingdom ladies.
    #(try_for_range, ":unused", active_npcs_begin, active_npcs_end),#<- changed
    #We counted the number of heroes, so we can cut down on the number of
    #iterations (since expanding this from active_npcs to heroes means that
    #a lot of them will not be lords).
    (try_for_range, ":unused", 0, ":met_lord_count"),#<- added
		(assign, ":score_to_beat", -100),
		(assign, ":best_relation_remaining_npc", -1),
		#Add support for promoted kingdom ladies
		#(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),#<-changed
		(try_for_range, ":active_npc", heroes_begin, heroes_end),#<-added
	##diplomacy end+
			(troop_slot_eq, ":active_npc", slot_troop_temp_slot, 0),
			(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
			(troop_slot_ge, ":active_npc", slot_troop_met, 1),

			(call_script, "script_troop_get_player_relation", ":active_npc"),
			(assign, ":relation_with_player", reg0),
			(ge, ":relation_with_player", ":score_to_beat"),

			(assign, ":score_to_beat", ":relation_with_player"),
			(assign, ":best_relation_remaining_npc", ":active_npc"),
		(try_end),
		(gt, ":best_relation_remaining_npc", -1),

		(str_store_troop_name_link, s4, ":best_relation_remaining_npc"),
		(assign, reg4, ":score_to_beat"),
		(str_store_string, s1, "@{!}{s1}^{s4}: {reg4}"),
		(troop_set_slot, ":best_relation_remaining_npc", slot_troop_temp_slot, 1),
	(try_end),


    ],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),



  ("companion_report",0,
   "{s7}{s2}",
   "none",
   [
   (str_clear, s1),
   (str_clear, s2),
   (str_store_string, s7, "str_no_companions_in_service"),

   (try_begin),
	(troop_get_slot, ":spouse_or_betrothed", "trp_player", slot_troop_spouse),
	(try_begin),
		##diplomacy start+ Test gender with script
		#(troop_get_type, ":is_female", "trp_player"),#<- replaced
		(call_script, "script_cf_dplmc_troop_is_female", "trp_player"),
		#(eq, ":is_female", 1),#<- replaced
		##diplomacy end+
		(str_store_string, s8, "str_husband"),
	(else_try),
		(str_store_string, s8, "str_wife"),
	(try_end),

	(try_begin),
		(le, ":spouse_or_betrothed", 0),
		(troop_get_slot, ":spouse_or_betrothed", "trp_player", slot_troop_betrothed),
		(str_store_string, s8, "str_betrothed"),
	(try_end),
	(gt, ":spouse_or_betrothed", 0),

	(str_store_troop_name, s4, ":spouse_or_betrothed"),
	(troop_get_slot, ":cur_center", ":spouse_or_betrothed", slot_troop_cur_center),
	(try_begin),
		(is_between, ":cur_center", centers_begin, centers_end),
		(str_store_party_name, s5, ":cur_center"),
	(else_try),
		(troop_slot_eq, ":spouse_or_betrothed", slot_troop_occupation, slto_kingdom_hero),
		(str_store_string, s5, "str_leading_party"),
	(else_try),
		(str_store_string, s5, "str_whereabouts_unknown"),
    (try_end),
	(str_store_string, s3, "str_s4_s8_s5"),
	# (str_store_string, s2, s1),
	(str_store_string, s2, "str_s2_s3"),

   (try_end),


   (try_begin),
    (ge, "$cheat_mode", 1),
	(ge, "$npc_to_rejoin_party", 0),
    (str_store_troop_name, s5, "$npc_to_rejoin_party"),
    (str_store_string, s1, s2),
	(str_store_string, s2, "@{!}DEBUG -- {s1}^NPC in rejoin queue: {s5}^"),
   (try_end),


   (try_for_range, ":companion", companions_begin, companions_end),
		# (str_clear, s2),
		(str_clear, s3),

		(try_begin),
			# (troop_get_slot, ":days_left", ":companion", slot_troop_days_on_mission),

			(troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),
            #SB : replace the call
            (call_script, "script_companion_get_mission_string", ":companion"),


			# (str_store_troop_name, s4, ":companion"),

			# (try_begin),
				# (troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_kingsupport),
				# (str_store_string, s8, "str_gathering_support"),
				# (try_begin),
					# (eq, ":days_left", 1),
					# (str_store_string, s5, "str_expected_back_imminently"),
				# (else_try),
					# (assign, reg3, ":days_left"),
					# (str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
				# (try_end),
			# (else_try),
				# (troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_gather_intel),
				# (troop_get_slot, ":town_with_contacts", ":companion", slot_troop_town_with_contacts),
				# (str_store_party_name, s11, ":town_with_contacts"),

				# (str_store_string, s8, "str_gathering_intelligence"),
				# (try_begin),
					# (eq, ":days_left", 1),
					# (str_store_string, s5, "str_expected_back_imminently"),
				# (else_try),
					# (assign, reg3, ":days_left"),
					# (str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
				# (try_end),
			# (else_try),	#This covers most diplomatic missions

				# (troop_slot_ge, ":companion", slot_troop_current_mission, npc_mission_peace_request),
				# ##diplomacy begin
				# (neg|troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_rejoin_when_possible), #SB : replace hard constant 8
        		# ##diplomacy end

				# (troop_get_slot, ":faction", ":companion", slot_troop_mission_object),
				# (str_store_faction_name, s9, ":faction"),
				# (str_store_string, s8, "str_diplomatic_embassy_to_s9"),
				# (try_begin),
					# (eq, ":days_left", 1),
					# (str_store_string, s5, "str_expected_back_imminently"),
				# (else_try),
					# (assign, reg3, ":days_left"),
					# (str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
				# (try_end),
			# (else_try),
				# (eq, ":companion", "$g_player_minister"),
				# (str_store_string, s8, "str_serving_as_minister"),
				# (try_begin),
					# (is_between, "$g_player_court", centers_begin, centers_end),
					# (str_store_party_name, s9, "$g_player_court"),
					# (str_store_string, s5, "str_in_your_court_at_s9"),
				# (else_try),
					# (str_store_string, s5, "str_whereabouts_unknown"),
				# (try_end),
			# (else_try),
				# (main_party_has_troop, ":companion"),
				# (str_store_string, s8, "str_under_arms"),
				# (str_store_string, s5, "str_in_your_party"),
			# (else_try),
				# (troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_rejoin_when_possible),
				# (str_store_string, s8, "str_attempting_to_rejoin_party"),
				# (str_store_string, s5, "str_whereabouts_unknown"),
			# (else_try),	#Companions who are in a center
				# (troop_slot_ge, ":companion", slot_troop_cur_center, 1),

				# (str_store_string, s8, "str_separated_from_party"),
				# (str_store_string, s5, "str_whereabouts_unknown"),
			# (else_try), #Excludes companions who have occupation = retirement
				# (try_begin),
					# (check_quest_active, "qst_lend_companion"),
					# (quest_slot_eq, "qst_lend_companion", slot_quest_target_troop, ":companion"),
					# (str_store_string, s8, "@On loan,"), 
				# (else_try),
					# (check_quest_active, "qst_lend_surgeon"),
					# (quest_slot_eq, "qst_lend_surgeon", slot_quest_target_troop, ":companion"),
					# (str_store_string, s8, "@On loan,"), 
				# (else_try),
					# (troop_set_slot, ":companion", slot_troop_current_mission, npc_mission_rejoin_when_possible),
					# (str_store_string, s8, "str_attempting_to_rejoin_party"),                  
				# (try_end),
				# (str_store_string, s5, "str_whereabouts_unknown"),

				(try_begin),
					(ge, "$cheat_mode", 1),
					(troop_get_slot, reg2, ":companion", slot_troop_current_mission),
					(troop_get_slot, reg3, ":companion", slot_troop_days_on_mission),
					(troop_get_slot, reg4, ":companion", slot_troop_prisoner_of_party),
					(troop_get_slot, reg4, ":companion", slot_troop_playerparty_history),

					(display_message, "@{!}DEBUG: {s4} current mission: {reg2}, days on mission: {reg3}, prisoner: {reg4}, pphistory: {reg5}"),
				(try_end),
			# (try_end),

			# (str_store_string, s3, "str_s4_s8_s5"),

			# (str_store_string, s2, s1),
            (str_store_string_reg, s3, s0),
			(str_store_string, s2, "str_s2_s3"),

			(str_clear, s7), #"no companions in service"
		# (else_try),
			# (neg|troop_slot_eq, ":companion", slot_troop_occupation, slto_kingdom_hero),
			# (troop_slot_ge, ":companion", slot_troop_prisoner_of_party, centers_begin),

			# (str_store_troop_name, s4, ":companion"),
			# (str_store_string, s8, "str_missing_after_battle"),
			# (str_store_string, s5, "str_whereabouts_unknown"),

			# (str_store_string, s3, "str_s4_s8_s5"),
			# (str_store_string, s2, s1),
			# (str_store_string, s1, "str_s2_s3"),
			# (str_clear, s7), #"no companions in service"

		(try_end),

   (try_end),


    ],
    [
    
    #SB : start commander presentation
      ("start",[],"Companion Overview...",
       [
        # (assign, "$g_player_troop", "trp_player"),
        #clear troop's temp slots for presentation
        (try_for_range, ":stack_troop", active_npcs_including_player_begin, companions_end),
          (troop_set_slot, ":stack_troop", dplmc_slot_troop_temp_slot, 0),
        (try_end),
        (troop_set_slot, "trp_player", dplmc_slot_troop_temp_slot, 0),
        #assign first companion to be selected
        # (party_get_num_companion_stacks, ":end", "p_main_party"),
        # (try_for_range, ":stack_no", 1, ":end"),
          # (party_stack_get_troop_id, ":troop_no", "p_main_party", ":stack_no"),
          # (is_between, ":troop_no", companions_begin, companions_end),
          # (assign, "$g_player_troop", ":troop_no"),
          # (assign, ":end", -1),
        # (try_end),
        # (set_player_troop, "$g_player_troop"),
        
        #To do : add $supported_pretender and/or spouse in two placeholder troops before active_npcs
        (start_presentation, "prsnt_companion_overview"),
        ]
       ),
      
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        #SB : fix globals
        (assign, "$g_player_troop", "trp_player"),
        (set_player_troop, "$g_player_troop"),
        ]
       ),
    ]
  ),





  ("faction_orders",0,
   "{!}{s9}",
   "none",
   [
    (str_clear, s9),
    (store_current_hours, ":cur_hours"),
    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
        (neq, ":faction_no", "fac_player_supporters_faction"),

        (faction_get_slot, ":old_faction_ai_state", ":faction_no", slot_faction_ai_state),

	    (try_begin),
			(faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
			(gt, ":faction_marshal", -1),
			(assign, ":faction_ai_decider", ":faction_marshal"),
	    (else_try),
			(faction_get_slot, ":faction_ai_decider", ":faction_no", slot_faction_leader),
	    (try_end),


        #(*1) these two lines moved to here from (*2)
        (call_script, "script_npc_decision_checklist_faction_ai_alt", ":faction_ai_decider"),
	    (assign, ":new_strategy", reg0),
	    (str_store_string, s26, s14),

        #(3*) these three lines moved to here from (*4)
        (faction_get_slot, ":faction_ai_state", ":faction_no", slot_faction_ai_state),
        (faction_get_slot, ":faction_ai_object", ":faction_no", slot_faction_ai_object),
        (faction_get_slot, ":faction_marshall", ":faction_no", slot_faction_marshall),

        (faction_get_slot, ":faction_ai_offensive_max_followers", ":faction_no", slot_faction_ai_offensive_max_followers),
        (str_store_faction_name, s10, ":faction_no"),

	   (try_begin),
			(faction_get_slot, ":faction_issue", ":faction_no", slot_faction_political_issue),

			(try_begin),
				(eq, ":faction_issue", 1),
				(str_store_string, s11, "@Appoint next marshal"),
			(else_try),
				(is_between, ":faction_issue", centers_begin, centers_end),
				(str_store_party_name, s12, ":faction_issue"),
				(str_store_string, s11, "@Award {s12} as fief"),
			(else_try),
				(eq, ":faction_issue", 0),
				(str_store_string, s11, "str_dplmc_none"),
			(else_try),
				(assign, reg3, ":faction_issue"),
				(str_store_string, s11, "@{!}Error ({reg3})"),
			(try_end),

			(store_current_hours, reg4),
			(faction_get_slot, ":faction_issue_put_on_agenda", ":faction_no", slot_faction_political_issue_time),
			(val_sub, reg4, ":faction_issue_put_on_agenda"),

	        (str_store_string, s10, "@{!}{s10}^Faction political issue: {s11}"),
			(try_begin),
				(faction_slot_ge, ":faction_no", slot_faction_political_issue, 1),
				(str_store_string, s10, "@{!}{s10} (on agenda {reg4} hours)"),
			(try_end),
	   (try_end),


       (assign, reg2, ":faction_ai_offensive_max_followers"),
       (try_begin),
         (eq, ":faction_ai_state", sfai_default),
         (str_store_string, s11, "@{!}Defending"),
       (else_try),
         (eq, ":faction_ai_state", sfai_gathering_army),
         (str_store_string, s11, "@{!}Gathering army"),
       (else_try),
         (eq, ":faction_ai_state", sfai_attacking_center),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "@{!}Besieging {s11}"),
       (else_try),
         (eq, ":faction_ai_state", sfai_raiding_village),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "@{!}Raiding {s11}"),
       (else_try),
         (eq, ":faction_ai_state", sfai_attacking_enemy_army),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "str_attacking_enemy_army_near_s11"),
       (else_try),
         (eq, ":faction_ai_state", sfai_feast),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "str_holding_feast_at_s11"),
	   (else_try),
         (eq, ":faction_ai_state", sfai_attacking_enemies_around_center),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "@{!}Attacking enemies around {s11}"),
       (else_try),
	     (assign, reg4, ":faction_ai_state"),
		 (str_store_string, s11, "str_sfai_reg4"),
	   (try_end),

       (try_begin),
         (lt, ":faction_marshall", 0),
         (str_store_string, s12, "@No one"),
       (else_try),
         (str_store_troop_name, s12, ":faction_marshall"),
		 (troop_get_slot, reg21, ":faction_marshall", slot_troop_controversy),
		 (str_store_string, s12, "@{!}{s12} (controversy: {reg21})"),
       (try_end),

	   (try_for_parties, ":screen_party"),
			(party_slot_eq, ":screen_party", slot_party_ai_state, spai_screening_army),
			(store_faction_of_party, ":screen_party_faction", ":screen_party"),
			(eq, ":screen_party_faction", ":faction_no"),

			(str_store_party_name, s38, ":screen_party"),
			(str_store_string, s12, "@{!}{s12}^Screening party: {s38}"),
	   (try_end),

       #(*2) these two lines moved to up (look *1)
	   #(call_script, "script_npc_decision_checklist_faction_ai", ":faction_no"),
	   #(assign, ":new_strategy", reg0),

       #(try_begin),
       #  (this_or_next|eq, ":new_strategy", sfai_default),
       #  (eq, ":new_strategy", sfai_feast),
	   #
	   #  (store_current_hours, ":hours"),
	   #  (faction_set_slot, ":faction_no", slot_faction_ai_last_rest_time, ":hours"),
	   #(try_end),
      (try_begin),
         #new condition to rest, (a faction's new strategy should be feast or default) and (":hours_at_current_state" > 20)
         (this_or_next|eq, ":new_strategy", sfai_default),
         (eq, ":new_strategy", sfai_feast),

         (store_current_hours, ":hours_at_current_state"),
         (faction_get_slot, ":current_state_started", ":faction_no", slot_faction_ai_current_state_started),
         (val_sub, ":hours_at_current_state", ":current_state_started"),
         (ge, ":hours_at_current_state", 18),

         (store_current_hours, ":hours"),
         (faction_set_slot, ":faction_no", slot_faction_ai_last_rest_time, ":hours"),
       (try_end),

        #Change of strategy
        (try_begin),
          (neq, ":new_strategy", ":old_faction_ai_state"),

          (store_current_hours, ":hours"),
          (faction_set_slot, ":faction_no", slot_faction_ai_current_state_started, ":hours"),
        (try_end),

	   (call_script, "script_evaluate_realm_stability", ":faction_no"),
	   (assign, ":disgruntled_lords", reg0),
	   (assign, ":restless_lords", reg1),

	   (faction_get_slot, ":last_feast_ended", ":faction_no", slot_faction_last_feast_start_time),
	   (store_sub, ":hours_since_last_feast", ":cur_hours", ":last_feast_ended"),
	   (val_sub, ":hours_since_last_feast", 72),

	   (faction_get_slot, ":current_state_started", ":faction_no", slot_faction_ai_current_state_started),
	   (store_sub, ":hours_at_current_state", ":cur_hours", ":current_state_started"),

       (faction_get_slot, ":faction_ai_last_offensive_time", ":faction_no", slot_faction_last_offensive_concluded),
       (store_sub, ":hours_since_last_offensive", ":cur_hours", ":faction_ai_last_offensive_time"),

       (faction_get_slot, ":faction_ai_last_rest", ":faction_no", slot_faction_ai_last_rest_time),
       (store_sub, ":hours_since_last_rest", ":cur_hours", ":faction_ai_last_rest"),

       (faction_get_slot, ":faction_ai_last_decisive_event", ":faction_no", slot_faction_ai_last_decisive_event),
       (store_sub, ":hours_since_last_decisive_event", ":cur_hours", ":faction_ai_last_decisive_event"),

	   (assign, reg3, ":hours_at_current_state"),
	   (assign, reg4, ":hours_since_last_offensive"),
	   (assign, reg5, ":hours_since_last_feast"),

	   (assign, reg7, ":disgruntled_lords"),
	   (assign, reg8, ":restless_lords"),
	   (assign, reg9, ":hours_since_last_rest"),
	   (assign, reg10, ":hours_since_last_decisive_event"),
	   (str_store_string, s14, s26),

       (str_store_string, s9, "str_s9s10_current_state_s11_hours_at_current_state_reg3_current_strategic_thinking_s14_marshall_s12_since_the_last_offensive_ended_reg4_hours_since_the_decisive_event_reg10_hours_since_the_last_rest_reg9_hours_since_the_last_feast_ended_reg5_hours_percent_disgruntled_lords_reg7_percent_restless_lords_reg8__"),
     (try_end),

     (try_begin),
       (neg|is_between, "$g_cheat_selected_faction", kingdoms_begin, kingdoms_end),
       (call_script, "script_get_next_active_kingdom", kingdoms_end),
       (assign, "$g_cheat_selected_faction", reg0),
     (try_end),
     (str_store_faction_name, s10, "$g_cheat_selected_faction"),
     (str_store_string, s9, "@Selected faction is: {s10}^^{s9}"),
    ],
    [
      ("faction_orders_next_faction", [],"{!}Select next faction.",
       [
         (call_script, "script_get_next_active_kingdom", "$g_cheat_selected_faction"),
         (assign, "$g_cheat_selected_faction", reg0),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
       
       #SB : debug slots
      ("faction_orders_slots", [],"{!}Debug slots.",
       [
         (assign, "$g_presentation_input", rename_kingdom),
         (assign, "$g_presentation_state", 0),
         (start_presentation, "prsnt_modify_slots"),
        ]
       ),

      ("faction_orders_political_collapse", [],"{!}CHEAT - Cause all lords in faction to fall out with their liege.",
       [
	   (try_for_range, ":lord", active_npcs_begin, active_npcs_end),
			(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
			(store_faction_of_troop, ":troop_faction", ":lord"),
			(eq, ":troop_faction", "$g_cheat_selected_faction"),
			(faction_get_slot, ":faction_liege", ":troop_faction", slot_faction_leader),
			(call_script, "script_troop_change_relation_with_troop", ":lord", ":faction_liege", -200),
	   (try_end),

	   ]
       ),

      ("faction_orders_defend", [],"{!}Force defend.",
       [
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_state, sfai_default),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_object, -1),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_feast", [],"{!}Force feast.",
       [

		 (assign, ":location_high_score", 0),
		 (try_for_range, ":location", walled_centers_begin, walled_centers_end),
			(neg|party_slot_ge, ":location", slot_center_is_besieged_by, 1),
			(store_faction_of_party, ":location_faction", ":location"),
			(eq, ":location_faction", "$g_cheat_selected_faction"),
			(party_get_slot, ":location_lord", ":location", slot_town_lord),
			(troop_get_slot, ":location_score", ":location_lord", slot_troop_renown),
			(store_random_in_range, ":random", 0, 1000), #will probably be king or senior lord
			(val_add, ":location_score", ":random"),
			(gt, ":location_score", ":location_high_score"),
			(assign, ":location_high_score", ":location_score"),
			(assign, ":location_feast", ":location"),
		 (try_end),

		 (try_begin),
			(gt, ":location_feast", centers_begin),
			(faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_state, sfai_feast),
			(faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_object, ":location_feast"),
			(try_begin),
			  (eq, "$g_player_eligible_feast_center_no", ":location_feast"),
			  (assign, "$g_player_eligible_feast_center_no", -1),
			(try_end),

			(store_current_hours, ":hours"),
			(faction_set_slot, "$g_cheat_selected_faction", slot_faction_last_feast_start_time, ":hours"),
		 (try_end),

	     (jump_to_menu, "mnu_faction_orders"),
        ]
       ),


      ("faction_orders_gather", [],"{!}Force gather army.",
       [
         (store_current_hours, ":cur_hours"),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_state, sfai_gathering_army),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_last_offensive_concluded, ":cur_hours"),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_offensive_max_followers, 1),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_object, -1),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_increase_time", [],"{!}Increase last offensive time by 24 hours.",
       [
         (faction_get_slot, ":faction_ai_last_offensive_time", "$g_cheat_selected_faction", slot_faction_last_offensive_concluded),
         (val_sub, ":faction_ai_last_offensive_time", 24),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_last_offensive_concluded, ":faction_ai_last_offensive_time"),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_rethink", [],"{!}Force rethink.",
       [
         (call_script, "script_init_ai_calculation"),
         (call_script, "script_decide_faction_ai", "$g_cheat_selected_faction"),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_rethink_all", [],"{!}Force rethink for all factions.",
       [
         (call_script, "script_recalculate_ais"),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),

	   # ("enable_alt_ai",[(eq, "$g_use_alternative_ai", 2),],"{!}CHEAT! - enable alternative ai",
       # [
	   # (assign, "$g_use_alternative_ai", 1),
	   # (jump_to_menu, "mnu_faction_orders"),
       # ]
       # ),

	   # ("disable_alt_ai",[(eq, "$g_use_alternative_ai", 2)],"{!}CHEAT! - disable alternative ai",
       # [
	   # (assign, "$g_use_alternative_ai", 0),
	   # (jump_to_menu, "mnu_faction_orders"),
       # ]
       # ),

       #SB : see if this works
     ("faction_orders_pretend", [],"{!}Restore pretender.",
       [
         # (call_script, "script_recalculate_ais"),
         (store_sub, "$supported_pretender", "$g_cheat_selected_faction", npc_kingdoms_begin),
         (val_add, "$supported_pretender", pretenders_begin),
         (assign, "$g_talk_troop", "$supported_pretender"),
         (party_add_members, "p_main_party", "$supported_pretender", 1),
         # (troop_get_slot, "$supported_pretender_old_faction", "$supported_pretender", slot_troop_original_faction),
         (assign, "$supported_pretender_old_faction", "$g_cheat_selected_faction"),
         (troop_set_faction, "$g_talk_troop", "fac_player_supporters_faction"),
         (faction_set_slot, "fac_player_supporters_faction", slot_faction_leader, "$supported_pretender"),
         (assign, "$g_talk_troop_faction", "fac_player_supporters_faction"),

         (quest_set_slot, "qst_rebel_against_kingdom", slot_quest_giver_troop, "$supported_pretender"),
         (quest_set_slot, "qst_rebel_against_kingdom", slot_quest_target_faction, "$supported_pretender_old_faction"),

         (str_store_faction_name_link, s14, "$supported_pretender_old_faction"),
         (str_store_troop_name_link, s13, "$supported_pretender"),
         (setup_quest_text,"qst_rebel_against_kingdom"),
         (str_store_string, s2, "@You promised to help {s13} claim the throne of {s14}."),
         (call_script, "script_start_quest", "qst_rebel_against_kingdom", "$supported_pretender"),
         
         #merge lords
         (try_begin),
           (eq, "$players_kingdom", "fac_player_supporters_faction"),
           (call_script, "script_deactivate_player_faction"),
           (try_for_range, ":npc", active_npcs_begin, active_npcs_end),
              (store_faction_of_troop, ":npc_faction", ":npc"),
              (eq, ":npc_faction", "fac_player_supporters_faction"),
              (troop_slot_eq, ":npc", slot_troop_occupation, slto_kingdom_hero),
              (call_script, "script_change_troop_faction", ":npc", "$g_talk_troop_faction"),
           (try_end),
         (try_end),
                 
         (try_begin),
           (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
           (neq, "$players_kingdom", "fac_player_supporters_faction"),
           (neq, "$players_kingdom", "$g_talk_troop_faction"), #ie, don't leave faction if the player is already part of the same kingdom

           (faction_get_slot, ":old_leader", "$players_kingdom", slot_faction_leader),
           (call_script, "script_add_log_entry", logent_renounced_allegiance,   "trp_player",  -1, ":old_leader", "$players_kingdom"),
           (call_script, "script_activate_player_faction", "$g_talk_troop"),
         (try_end),
         
         (call_script, "script_player_join_faction", "$g_talk_troop_faction"),
         
         (call_script, "script_add_notification_menu", "mnu_notification_faction_defeated", "$g_cheat_selected_faction", 0),
         (change_screen_return),
        ]
       ),
      ("faction_orders_init_econ", [],"{!}Initialize economic stats.",
       [
         (call_script, "script_initialize_economic_information"),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),



      ("go_back_dot",[],"{!}Go back.",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),


  ("character_report",0,
   "{s9}",
   "none",
   [(try_begin),
      (gt, "$g_player_reading_book", 0),
      (player_has_item, "$g_player_reading_book"),
      (str_store_item_name, s8, "$g_player_reading_book"),
      (str_store_string, s9, "@You are currently reading {s8}."),
    (else_try),
      (assign, "$g_player_reading_book", 0),
      (str_store_string, s9, "@You are not reading any books."),
    (try_end),
    (assign, ":num_friends", 0),
    (assign, ":num_enemies", 0),
    (str_store_string, s6, "str_dplmc_none"),
    (str_store_string, s8, "str_dplmc_none"),
    (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
	  (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
		(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive_pretender),
	  (call_script, "script_troop_get_player_relation", ":troop_no"),
      (assign, ":player_relation", reg0),
      #(troop_get_slot, ":player_relation", ":troop_no", slot_troop_player_relation),
      (try_begin),
        (gt, ":player_relation", 20),
        (try_begin),
          (eq, ":num_friends", 0),
          (str_store_troop_name, s8, ":troop_no"),
        (else_try),
          (eq, ":num_friends", 1),
          (str_store_troop_name, s7, ":troop_no"),
          (str_store_string, s8, "@{s7} and {s8}"),
        (else_try),
          (str_store_troop_name, s7, ":troop_no"),
          (str_store_string, s8, "@{!}{s7}, {s8}"),
        (try_end),
        (val_add, ":num_friends", 1),
      (else_try),
        (lt, ":player_relation", -20),
        (try_begin),
          (eq, ":num_enemies", 0),
          (str_store_troop_name, s6, ":troop_no"),
        (else_try),
          (eq, ":num_enemies", 1),
          (str_store_troop_name, s5, ":troop_no"),
          (str_store_string, s6, "@{s5} and {s6}"),
        (else_try),
          (str_store_troop_name, s5, ":troop_no"),
          (str_store_string, s6, "@{!}{s5}, {s6}"),
        (try_end),
        (val_add, ":num_enemies", 1),
      (try_end),
    (try_end),

	#lord recruitment changes begin
	(str_clear, s12),
	(try_begin),
		(gt, "$player_right_to_rule", 0),
		(assign, reg12, "$player_right_to_rule"),
		(str_store_string, s12, "str__right_to_rule_reg12"),
	(try_end),

	(str_clear, s15),
	(try_begin),
		(this_or_next|gt, "$claim_arguments_made", 0),
		(this_or_next|gt, "$ruler_arguments_made", 0),
		(this_or_next|gt, "$victory_arguments_made", 0),
		(this_or_next|gt, "$lords_arguments_made", 0),
		(eq, 1, 0),

		(assign, reg3, "$claim_arguments_made"),
		(assign, reg4, "$ruler_arguments_made"),
		(assign, reg5, "$victory_arguments_made"),
		(assign, reg6, "$lords_arguments_made"),
		(assign, reg7, "$benefit_arguments_made"),

		(str_store_string, s15, "str_political_arguments_made_legality_reg3_rights_of_lords_reg4_unificationpeace_reg5_rights_of_commons_reg6_fief_pledges_reg7"),
	(try_end),

	#lord recruitment changes begin

    (assign, reg3, "$player_honor"),
    (troop_get_slot, reg2, "trp_player", slot_troop_renown),

    (str_store_string, s9, "str_renown_reg2_honour_rating_reg3s12_friends_s8_enemies_s6_s9"),

    (call_script, "script_get_number_of_hero_centers", "trp_player"),
    (assign, ":no_centers", reg0),
    (try_begin),
      (gt, ":no_centers", 0),
      (try_for_range, ":i_center", 0, ":no_centers"),
        (call_script, "script_troop_get_leaded_center_with_index", "trp_player", ":i_center"),
        (assign, ":cur_center", reg0),
        (try_begin),
          (eq, ":i_center", 0),
          (str_store_party_name, s8, ":cur_center"),
        (else_try),
          (eq, ":i_center", 1),
          (str_store_party_name, s7, ":cur_center"),
          (str_store_string, s8, "@{s7} and {s8}"),
        (else_try),
          (str_store_party_name, s7, ":cur_center"),
          (str_store_string, s8, "@{!}{s7}, {s8}"),
        (try_end),
      (try_end),
      (str_store_string, s9, "@Your estates are: {s8}.^{s9}"),
    (try_end),
    (try_begin),
      (gt, "$players_kingdom", 0),

      (str_store_faction_name, s8, "$players_kingdom"),
      (try_begin),
	  ##diplomacy start+ Handle player is co-ruler of NPC faction
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(str_store_string, s9, "str_you_are_king_queen_of_s8_s9"),
	  (else_try),
	  ##diplomacy end+
        (this_or_next|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
        (neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
        #(str_store_string, s9, "@You are a lord of {s8}.^{s9}"),
        (str_store_string, s9, "str_you_are_a_lord_lady_of_s8_s9"),
      (else_try),
        (str_store_string, s9, "str_you_are_king_queen_of_s8_s9"),
      (try_end),

    (try_end),
    ],
    [

	#lord recruitment changes begin

	("continue",[(eq,"$cheat_mode",1)],"{!}CHEAT! - increase Right to Rule",
       [
	   (val_add, "$player_right_to_rule", 10),
	   (jump_to_menu, "mnu_character_report"),
       ]
       ),


	("continue",[(eq,"$cheat_mode",1),
		(str_store_troop_name, s14, "$g_talk_troop"),
	],"{!}CHEAT! - increase your relation with {s14}",
       [
	   (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 10),
	   (jump_to_menu, "mnu_character_report"),
       ]
       ),
       
	("cheat_slots",[(eq,"$cheat_mode",1),
        (str_store_troop_name, s14, "$g_talk_troop"),
	],"{!}CHEAT! - Access {s14} troop slots",
       [
	   # (assign, "$g_talk_troop", "trp_player"),
	   (jump_to_menu, "mnu_display_troop_slots"),
       ]
       ),



	("continue",[(eq,"$cheat_mode",1)],"{!}CHEAT! - increase honor",
       [
	   (val_add, "$player_honor", 10),
	   (jump_to_menu, "mnu_character_report"),
       ]
       ),

	("continue",[(eq,"$cheat_mode",1)],"{!}CHEAT! - increase renown",
       [
	   (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
	   (val_add, ":renown", 50),
	   (troop_set_slot, "trp_player", slot_troop_renown, ":renown"),

	   (jump_to_menu, "mnu_character_report"),
       ]
       ),

	("continue",[(eq,"$cheat_mode",1)],"{!}CHEAT! - increase persuasion",
       [
	   (troop_raise_skill, "trp_player", "skl_persuasion", 1),

	   (jump_to_menu, "mnu_character_report"),
       ]
       ),

	("continue",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),

	#lord recruitment changes end

	   ]
  ),

  ("party_size_report",0,
   "{s1}",
   "none",
   [(call_script, "script_game_get_party_companion_limit"),
    (assign, ":party_size_limit", reg0),

    (store_skill_level, ":leadership", "skl_leadership", "trp_player"),
    (val_mul, ":leadership", 5),
    (store_attribute_level, ":charisma", "trp_player", ca_charisma),

    (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
    (val_div, ":renown", 25),
    (try_begin),
      (gt, ":leadership", 0),
      (str_store_string, s2, "@{!} +"),
    (else_try),
      (str_store_string, s2, "str_space"),
    (try_end),
    (try_begin),
      (gt, ":charisma", 0),
      (str_store_string, s3, "@{!} +"),
    (else_try),
      (str_store_string, s3, "str_space"),
    (try_end),
    (try_begin),
      (gt, ":renown", 0),
      (str_store_string, s4, "@{!} +"),
    (else_try),
      (str_store_string, s4, "str_space"),
    (try_end),

    
    #SB : other modifiers from party_get_ideal_size, listed in order of precedence
    (try_for_range, ":sreg", s6, s10),
      (str_clear, ":sreg"),
    (try_end),

    (try_begin),
      (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
      # (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
      # the above script doesn't exactly work for pretender
      (try_begin),
        # (ge, reg0, DPLMC_FACTION_STANDING_LEADER), #exclude spouse
        (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
        (store_mul, ":king_bonus", 5, "$player_right_to_rule"), #20 is "legit" ruler
        (val_clamp, ":king_bonus", dplmc_marshal_party_bonus, dplmc_monarch_party_bonus + 1),
        (assign, reg6, ":king_bonus"),
        (str_store_string, s8, "@Monarch: +{reg6}^"),
      (else_try),
        (assign, ":king_bonus", 0),
      (try_end),
    
      (try_begin),
        (faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
        (assign, ":marshal_bonus", dplmc_marshal_party_bonus),
        (assign, reg6, ":marshal_bonus"),
        (str_store_string, s7, "@Marshal: +{reg6}^"),
      (else_try),
        (assign, ":marshal_bonus", 0),
      (try_end),
      #percentage calculation follows
      (assign, ":faction_id", "$players_kingdom"),
      (assign, ":percent", 100),
      #Limit effects of policies for nascent kingdoms.
      (assign, ":policy_min", -3),
      (assign, ":policy_max", 4),#one greater than the maximum
      (try_begin),
          (this_or_next|eq, ":faction_id", "fac_player_supporters_faction"),
          (faction_slot_eq, ":faction_id", slot_faction_leader, "trp_player"),
          (faction_get_slot, ":policy_max", ":faction_id", slot_faction_num_towns),
          (faction_get_slot, reg0, ":faction_id", slot_faction_num_castles),
          (val_add, ":policy_max", reg0),
          (val_clamp, ":policy_max", 0, 4),#0, 1, 2, 3
          (store_mul, ":policy_min", ":policy_max", -1),
          (val_add, ":policy_max", 1),#one greater than the maximum
      (try_end),
      (try_begin), #we detecting rulership using king_bonus to determine which percent to apply
        (gt, ":king_bonus", 0),
        (try_begin),
          (faction_get_slot, ":centralization", ":faction_id", dplmc_slot_faction_centralization),
          (val_clamp, ":centralization", ":policy_min", ":policy_max"),
          (val_mul, ":centralization", 10),
          (val_add, ":percent", ":centralization"),
        (try_end),
      (else_try), #player is a regular vassal
        (try_begin),
          (faction_get_slot, ":centralization", ":faction_id", dplmc_slot_faction_centralization),
          (val_clamp, ":centralization", ":policy_min", ":policy_max"),
          (val_mul, ":centralization", -3),
          (val_add, ":percent", ":centralization"),
        (try_end),
        (try_begin),
          (faction_get_slot, ":aristocracy", ":faction_id", dplmc_slot_faction_aristocracy),
          (val_clamp, ":aristocracy", ":policy_min", ":policy_max"),
          (val_mul, ":aristocracy", 3),
          (val_add, ":percent", ":aristocracy"),
        (try_end),
        (try_begin),
          (faction_get_slot, ":quality", ":faction_id", dplmc_slot_faction_quality),
          (val_clamp, ":quality", ":policy_min", ":policy_max"),
          (val_mul, ":quality", -4),
          (val_add, ":percent", ":quality"),
        (try_end),
        ##diplomacy end
      (try_end),
      (try_begin),
        (faction_get_slot, ":serfdom", ":faction_id", dplmc_slot_faction_serfdom),
        (val_clamp, ":serfdom", ":policy_min", ":policy_max"),
        (val_mul, ":serfdom", 2), #SB : no multiplier as per description
        (val_add, ":percent", ":serfdom"),
      (try_end),
      #if no change from default, do not display
      (try_begin), 
        (eq, ":percent", 100),
        (assign, ":percent", 0),
      (else_try), #last new string
        (assign, reg6, ":percent"),
        (str_store_string, s9, "@Policy: {reg6}%^"),
      (try_end),
    (else_try), #not affiliated, do not show position-based bonus
      (assign, ":king_bonus", 0),
      (assign, ":marshal_bonus", 0),
      (assign, ":percent", 0),
    (try_end),
    ## CC
    (assign, ":center_bonus", 0),
    (try_for_range, ":cur_center", castles_begin, castles_end),
      (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
      (val_add, ":center_bonus", dplmc_castle_party_bonus),
    (try_end),
    (try_begin),
      (gt, ":center_bonus", 0),
      (assign, reg6, ":center_bonus"),
      (str_store_string, s6, "@Castellan: +{reg6}^"),
    (try_end),
    ## CC
    
    # (assign, reg9, ":percent"),
    # (assign, reg8, ":king_bonus"),
    # (assign, reg7, ":marshal_bonus"),
    # (assign, reg6, ":center_bonus"),
    (assign, reg5, ":party_size_limit"),
    (assign, reg1, ":leadership"),
    (assign, reg2, ":charisma"),
    (assign, reg3, ":renown"),
    #SB : might as well show player party size
    (party_get_num_companions, reg10, "p_main_party"),
    (str_store_string, s1, "@Current party size is {reg10}/{reg5}.^\
Current party size modifiers are:^^\
Base size:  +30^\
Leadership: {s2}{reg1}^\
Charisma: {s3}{reg2}^\
Renown: {s4}{reg3}^^\
{s8}{s7}{s6}{s9}\
TOTAL:  {reg5}"),
    ],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),

  ("faction_relations_report",0,
   "{s1}",
   "none",
   [(str_clear, s2),
    (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
      (neq, ":cur_kingdom", "fac_player_supporters_faction"),
      (store_relation, ":cur_relation", "fac_player_supporters_faction", ":cur_kingdom"),
      (try_begin),
        (ge, ":cur_relation", 90),
        (str_store_string, s3, "@Loyal"),
      (else_try),
        (ge, ":cur_relation", 80),
        (str_store_string, s3, "@Devoted"),
      (else_try),
        (ge, ":cur_relation", 70),
        (str_store_string, s3, "@Fond"),
      (else_try),
        (ge, ":cur_relation", 60),
        (str_store_string, s3, "@Gracious"),
      (else_try),
        (ge, ":cur_relation", 50),
        (str_store_string, s3, "@Friendly"),
      (else_try),
        (ge, ":cur_relation", 40),
        (str_store_string, s3, "@Supportive"),
      (else_try),
        (ge, ":cur_relation", 30),
        (str_store_string, s3, "@Favorable"),
      (else_try),
        (ge, ":cur_relation", 20),
        (str_store_string, s3, "@Cooperative"),
      (else_try),
        (ge, ":cur_relation", 10),
        (str_store_string, s3, "@Accepting"),
      (else_try),
        (ge, ":cur_relation", 0),
        (str_store_string, s3, "@Indifferent"),
      (else_try),
        (ge, ":cur_relation", -10),
        (str_store_string, s3, "@Suspicious"),
      (else_try),
        (ge, ":cur_relation", -20),
        (str_store_string, s3, "@Grumbling"),
      (else_try),
        (ge, ":cur_relation", -30),
        (str_store_string, s3, "@Hostile"),
      (else_try),
        (ge, ":cur_relation", -40),
        (str_store_string, s3, "@Resentful"),
      (else_try),
        (ge, ":cur_relation", -50),
        (str_store_string, s3, "@Angry"),
      (else_try),
        (ge, ":cur_relation", -60),
        (str_store_string, s3, "@Hateful"),
      (else_try),
        (ge, ":cur_relation", -70),
        (str_store_string, s3, "@Revengeful"),
      (else_try),
        (str_store_string, s3, "@Vengeful"),
      (try_end),
      (str_store_faction_name, s4, ":cur_kingdom"),
      (assign, reg1, ":cur_relation"),
      (str_store_string, s2, "@{!}{s2}^{s4}: {reg1} ({s3})"),
    (try_end),
    (str_store_string, s1, "@Your relation with the factions are:^{s2}"),



    ],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),


  ("camp",mnf_scale_picture|mnf_enable_hot_keys,
   "You set up camp. What do you want to do?",
   "none",
   [
     (assign, "$g_player_icon_state", pis_normal),
     (set_background_mesh, "mesh_pic_camp"),
    ],
    [
      ("camp_action_1",[],"Walk around the campsite.", #dckplmc
       [(set_jump_mission,"mt_camp"),
        (call_script, "script_setup_camp_scene"),
        (change_screen_mission),
        ]
       ),
       
       ("formation_mod_option",[],"Formations mod options.", [(start_presentation, "prsnt_formation_mod_option")]),
       
      ("content_options",[],"Content Options.",[(jump_to_menu, "mnu_content_options")]),
       
      ("camp_fuck_1",[(eq,1,0)],"Fuck Test",
       [(jump_to_menu, "mnu_fuck"),
        ]
       ),
       

       
       ##diplomacy begin
###################################################################################
# Autoloot: Allow item management from camp
###################################################################################
##nested diplomacy start+
#Made some changes to autoloot conditions
	("dplmc_camp_manage_inventory",
		[
	  #OLD:
	  #(eq, "$g_autoloot", 1),
      #(store_skill_level, ":inv_skill", "skl_inventory_management", "trp_player"),
      #(gt, "$g_player_chamberlain", 0),
      #(ge, ":inv_skill", 3),
	  #NEW:
	  #1. Must have companions
	  #2. Either a hero in the party must have inventory management 3 or higher, or the player must have inventory management of 2 or higher, or the player or a hero in the party must have a looting skill of 2 or higher
	  (call_script, "script_cf_dplmc_player_party_meets_autoloot_conditions"),
	    ],
	  #"Manage your party's inventory.",
	  "Manage auto-loot settings.",
		[
			(try_begin),
				#dplmc+ Add check if autoloot has not been initialized yet
				(call_script, "script_dplmc_initialize_autoloot", 0),#argument "0" means this does nothing if deemed unnecessary
			(try_end),
			(troop_clear_inventory, "trp_temp_troop"),
			##diplomacy start+
			(assign, "$pool_troop", "trp_temp_troop"),
			(assign, "$dplmc_return_menu", "mnu_camp"),
			##diplomacy end+
			(assign, "$inventory_menu_offset", 0),
            #SB : variable resets
			(assign, "$lord_selected", "trp_player"),
            (str_clear, dplmc_loot_string),
			(jump_to_menu, "mnu_dplmc_manage_loot_pool")
		]
	),

#Alternate display: make it clear why autoloot isn't appearing
	("dplmc_camp_manage_inventory_disabled",
		[
	  #Print this when the player has companions but doesn't meet
	  #the minimum skill levels.
		(try_begin),
			(call_script, "script_cf_dplmc_player_party_meets_autoloot_conditions"),
		(try_end),
		(eq, reg0, 0),
		(disable_menu_option),
	    ],
	  "Auto-loot requires Inventory Management or Looting at rank 2.",
		[
		]
	),
##nested diplomacy end+ Finished changes to autoloot conditions
###################################################################################
# End Autoloot
###################################################################################
    ("dplmc_camp_preferences",
        [
        ],
        "Diplomacy preferences.",
        [
            (jump_to_menu, "mnu_dplmc_preferences"),
            ## SB : global initialization for redefine_keys
            (assign, "$g_presentation_next_presentation", -1),
        ]
    ),

##diplomacy end
      ("camp_action",[],"Take an action.",
       [(jump_to_menu, "mnu_camp_action"),
        ]
       ),
      ("camp_wait_here",[],"Wait here for some time.",
       [
           (assign,"$g_camp_mode", 1),
           (assign, "$g_infinite_camping", 0),
           (assign, "$g_player_icon_state", pis_camping),

           (try_begin),
             (party_is_active, "p_main_party"),
             (party_get_current_terrain, ":cur_terrain", "p_main_party"),
             (try_begin),
               (eq, ":cur_terrain", rt_desert),
               (unlock_achievement, ACHIEVEMENT_SARRANIDIAN_NIGHTS),
             (try_end),
           (try_end),

           (rest_for_hours_interactive, 24 * 365, 5, 1), #rest while attackable

           (change_screen_return),
        ]
       ),
      ("camp_cheat",
       [(ge, "$cheat_mode", 1)
        ], "CHEAT MENU!",
       [(jump_to_menu, "mnu_camp_cheat"),
        ],
       ),
      ("resume_travelling",[],"Resume travelling.",
       [
           (change_screen_return),
        ]
       ),
      ]
  ),
  ("camp_cheat",0,
   "Select a cheat:",
   "none",
   [
     ],
    [
      ("camp_cheat_find_item",[], "Find an item...",
       [(jump_to_menu, "mnu_cheat_find_item"),]
       ),

      ("camp_cheat_weather",[], "Change weather..",
       [(jump_to_menu, "mnu_cheat_change_weather"),]
       ),

      ("camp_cheat_0",[],"{!}Increase player RTR.",
       [
          (try_begin),
            (this_or_next|key_is_down, key_left_shift),
            (key_is_down, key_right_shift),
            (call_script, "script_change_player_right_to_rule", 25),
          (else_try),
            (call_script, "script_change_player_right_to_rule", 3),
          (try_end),
        ]
       ),

      ("camp_cheat_1",[],"{!}Increase player renown.",
       [
          (try_begin),
            (this_or_next|key_is_down, key_left_shift),
            (key_is_down, key_right_shift),
            (call_script, "script_change_troop_renown", "trp_player", 500),
          (else_try),
            (call_script, "script_change_troop_renown", "trp_player", 100),
          (try_end),
        ]
       ),

      ("camp_cheat_2",[],"{!}Increase player honor.",
       [
          (try_begin),
            (this_or_next|key_is_down, key_left_shift),
            (key_is_down, key_right_shift),
            (call_script, "script_change_player_honor", 50),
          (else_try),
            (call_script, "script_change_player_honor", 5),
          (try_end),
        ]
       ),

      ("camp_cheat_3",[],"{!}Update political notes.",
       [
         (try_for_range, ":hero", active_npcs_begin, active_npcs_end),
           (troop_slot_eq, ":hero", slot_troop_occupation, slto_kingdom_hero),
           (call_script, "script_update_troop_political_notes", ":hero"),
         (try_end),

         (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
           (call_script, "script_update_faction_political_notes", ":kingdom"),
         (try_end),
        ]
       ),

      ("camp_cheat_4",[],"{!}Update troop notes.",
       [
         (try_for_range, ":hero", active_npcs_begin, active_npcs_end),
           (troop_slot_eq, ":hero", slot_troop_occupation, slto_kingdom_hero),
           (call_script, "script_update_troop_notes", ":hero"),
         (try_end),

         (try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
           (call_script, "script_update_troop_notes", ":lady"),
           (call_script, "script_update_troop_political_notes", ":lady"),
           (call_script, "script_update_troop_location_notes", ":lady", 0),
         (try_end),
        ]
       ),

       #SB : update tavern npcs
      ("camp_cheat_5",[],"{!}Scramble taverngoers.",
       [
        (try_for_range, ":slots", slot_center_ransom_broker, slot_center_tavern_minstrel + 1),
          (neq, ":slots", slot_center_traveler_info_faction),
          #initialize
          (try_for_range, ":towns", towns_begin, towns_end),
            (party_set_slot, ":towns", ":slots", -1),
          (try_end),

          (try_begin), #parse
            (eq, ":slots", slot_center_ransom_broker),
            (assign, ":start", ransom_brokers_begin),
            (assign, ":end", ransom_brokers_end),
          (else_try),
            (eq, ":slots", slot_center_tavern_traveler),
            (assign, ":start", tavern_travelers_begin),
            (assign, ":end", tavern_travelers_end),
          (else_try),
            (eq, ":slots", slot_center_tavern_minstrel),
            (assign, ":start", tavern_minstrels_begin),
            (assign, ":end", tavern_minstrels_end),
          (else_try),
            (eq, ":slots", slot_center_tavern_bookseller),
            (assign, ":start", tavern_booksellers_begin),
            (assign, ":end", tavern_booksellers_end),
          (try_end),

          #populate
          (assign, ":num_towns", 0),
          (str_store_string, s51, "@nowhere in particular"),
          (try_for_range, ":troop_no", ":start", ":end"),
            (troop_set_slot, ":troop_no", slot_troop_cur_center, -1),
            (store_random_in_range, ":town_no", towns_begin, towns_end),
            
            (try_begin), #ensure no overlaps
              (party_slot_ge, ":town_no", ":slots", ":start"),
              # (assign, ":limit", towns_end),
              # (try_for_range, ":center_no", towns_begin, ":limit"),
                # (assign, ":town_used", 0),
                # (try_for_range, ":other_troop", ":start", ":troop_no"),
                  # (troop_slot_eq, ":other_troop", slot_troop_cur_center, ":center_no"),
                  # (assign, ":town_used", 1),
                # (try_end),
                # (eq, ":town_used", 0), #no other troop uses this slot
                # (party_set_slot, ":center_no", ":slots", ":troop_no"),
                # (assign, ":limit", 1),
              # (try_end),
            (else_try),
              (val_add, ":num_towns", 1),
              (str_store_party_name_link, s50, ":town_no"),
              (party_set_slot, ":town_no", ":slots", ":troop_no"),
              (troop_set_slot, ":troop_no", slot_troop_cur_center, ":town_no"),
              (try_begin),
                (eq, ":num_towns", 1),
                (str_store_string, s51, s50),
              (else_try),
                (str_store_string, s51, "str_s50_comma_s51"),
              (try_end),
            (try_end),
          (try_end),
          (str_store_troop_name_plural, s10, ":start"), #default titles "book_merchant" "ransom_broker" etc
          (str_store_string_reg, s11, s51),
          (display_message, "@You can find {s10}s at {s11}."),
        (try_end),
        (call_script, "script_update_mercenary_units_of_towns"), #might as well
        ]
       ),

      ("camp_cheat_6",[],"{!}Infinite camp",
       [
         (assign,"$g_camp_mode", 1),
         (assign, "$g_infinite_camping", 1),
         (assign, "$g_player_icon_state", pis_camping),
         (rest_for_hours_interactive, 10 * 24 * 365, 20), #10 year rest while not attackable with 20x speed
         (change_screen_return),
        ]
       ),

	   ##nested diplomacy start+
	  ("camp_cheat_7",[(troop_slot_ge, "trp_player", slot_troop_spouse, 1),],"{!}Divorce player spouse",
       [
	 	 (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
        #set this before the loop below, to avoid potential wierdness in the family relation check
		 (troop_set_slot, ":spouse", slot_troop_spouse, -1),
	     (troop_set_slot, "trp_player", slot_troop_spouse, -1),

		#apply relation loss with the spouse
		 (call_script, "script_change_player_relation_with_troop", ":spouse", -40),
	    #change relations with family - inverse of gain from marriage
		(try_for_range, ":family_member", heroes_begin, heroes_end),
		    (neq, ":family_member", ":spouse"),
			(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":spouse", ":family_member"),
			(gt, reg0, 0),
			(val_mul, reg0, -2),
			(val_div, reg0, 3),
			(val_min, reg0, -1),
			(call_script, "script_change_player_relation_with_troop", ":family_member", reg0),
		(try_end),
        ]
       ),
	   ##nested diplomacy end+

      ("cheat_faction_orders",[(ge,"$cheat_mode",1)],
	  "{!}Cheat: Set Debug messages to All.",
       [(assign,"$cheat_mode",1),
         (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),
      ("cheat_faction_orders",[
	  (ge, "$cheat_mode", 1),
	  (neq,"$cheat_mode",3)],"{!}Cheat: Set Debug messages to Econ Only.",
       [(assign,"$cheat_mode",3),
         (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),
      ("cheat_faction_orders",[
	  (ge, "$cheat_mode", 1),
	  (neq,"$cheat_mode",4)],"{!}Cheat: Set Debug messages to Political Only.",
       [(assign,"$cheat_mode",4),
         (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),
      ("camp_cheat_heal",[],"Heal party.",
       [
         (heal_party, "p_main_party"),
        ]
       ),
      ("camp_cheat_xp",[],"Add xp to party.",
       [
         (set_show_messages, 0),
         (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
         (try_for_range, ":stack", 0, ":num_stacks"), #include player if too lazy to ctrl+x
            (party_stack_get_troop_id, ":id", "p_main_party", ":stack"),
            (try_begin),
                # (troop_is_hero, ":id"),
                # (store_character_level, ":level", ":id"),
                # (get_level_boundary, ":xp", ":level"),
                # (troop_get_xp, ":cur_exp", ":id"),
                # (val_sub, ":xp", ":cur_exp"),
                # (add_xp_to_troop, ":xp", ":id"),
            # (else_try),
                (party_stack_get_size, ":size", "p_main_party", ":stack"),
                (call_script, "script_game_get_upgrade_xp", ":id"),
                (store_mul, ":xp", reg0, ":size"),
                (try_begin),
                  (troop_is_hero, ":id"),
                  # (troop_get_xp, ":cur_exp", ":id"),
                  # (val_sub, ":xp", ":cur_exp"),
                  (store_character_level, ":level", ":id"),
                  ##this is so stupid but it works (probably), but add_xp_to_troop caps out at 29999
                  (assign, ":end", 100),
                  (try_begin), #assign block of exp
                    (le, ":level", 10),
                    (assign, ":xp", 100),
                  (else_try),
                    (le, ":level", 25),
                    (assign, ":xp", 1000),
                  (else_try), #most people stop before level 30
                    (le, ":level", 35),
                    (assign, ":xp", 10000),
                  (else_try),
                    (le, ":level", 50),
                    (assign, ":xp", 30000),
                  (else_try),
                    (le, ":level", 60),
                    (assign, ":xp", 1000000),
                  (else_try), #good luck, level caps at 63
                    (assign, ":xp", 10000000),
                  (try_end),
                  # (val_mul, ":xp", ":level"),
                  (try_for_range, ":unused", 0, ":end"),
                    (party_add_xp_to_stack, "p_main_party", ":stack", ":xp"),
                    (add_xp_to_troop, 1, ":id"), #this actually upgrades the level
                    # (add_xp_as_reward, ":xp"),
                    (store_character_level, ":cur_level", ":id"),
                    (lt, ":level", ":cur_level"), #done
                    (assign, ":end", 0),
                  (try_end),
                (else_try),
                  (party_add_xp_to_stack, "p_main_party", ":stack", ":xp"),
                (try_end),
            (try_end),
         (try_end),
         (set_show_messages, 1),
         # (party_upgrade_with_xp, "p_main_party", 1, 0), #random upgrade - disabled
         # (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),
      ("camp_cheat_prisoner",[
          (party_get_num_prisoner_stacks, ":stack", "p_main_party"),
          (gt, ":stack", 0),
          (try_for_range, ":i_stack", 0, ":stack"),
            (party_prisoner_stack_get_troop_id, ":troop", "p_main_party", ":i_stack"),
            (neg|troop_is_hero, ":troop"),
            (assign, ":stack", 0),
          (try_end),
          (eq, ":stack", 0), #found one non-hero entity
      ],"Recruit all prisoners.",
       [ # (call_script, "script_party_add_party_prisoners"),
         # (call_script, "script_party_remove_all_prisoners"),
         (party_get_num_prisoner_stacks, ":num_stacks", "p_main_party"),
         (try_for_range_backwards, ":stack", 0, ":num_stacks"),
            (party_prisoner_stack_get_troop_id, ":troop", "p_main_party", ":stack"),
            (neg|troop_is_hero, ":troop"),
            (gt, ":troop", 0),
            (party_prisoner_stack_get_size, ":amount", "p_main_party", ":stack"),
            (party_remove_prisoners, "p_main_party", ":troop", ":amount"),
            (party_add_members, "p_main_party", ":troop", ":amount"),
         (try_end),
         # (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),
       #do not add more cheat options, no more room in one menu

      ("back_to_camp_menu",[],"{!}Back to camp menu.",
       [
         (jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("cheat_find_item",0,
   "{!}Current item range: {reg5} to {reg6}",
   "none",
   [
     (assign, reg5, "$cheat_find_item_range_begin"),
     (store_add, reg6, "$cheat_find_item_range_begin", max_inventory_items),
     (val_min, reg6, "itm_items_end"),
     (val_sub, reg6, 1),
     ],
    [
    
    #SB : easier debug
      ("cheat_find_item_prev_range",[], "{!}Move to previous range.",
       [
        (val_sub, "$cheat_find_item_range_begin", max_inventory_items),
        (try_begin),
          (lt, "$cheat_find_item_range_begin", 0),
          (assign, "$cheat_find_item_range_begin", itm_items_end-max_inventory_items),
        (try_end),
        (jump_to_menu, "mnu_cheat_find_item"),
       ]
       ),
       
      ("cheat_find_item_next_range",[], "{!}Move to next item range.",
       [
        (val_add, "$cheat_find_item_range_begin", max_inventory_items),
        (try_begin),
          (ge, "$cheat_find_item_range_begin", "itm_items_end"),
          (assign, "$cheat_find_item_range_begin", 0),
        (try_end),
        (jump_to_menu, "mnu_cheat_find_item"),
       ]
       ),

       ("cheat_find_item_choose_this",[], "{!}Choose from this range.",
       [
        (troop_clear_inventory, "trp_find_item_cheat"),
        (store_add, ":max_item", "$cheat_find_item_range_begin", max_inventory_items),
        (val_min, ":max_item", "itm_items_end"),
        (store_sub, ":num_items_to_add", ":max_item", "$cheat_find_item_range_begin"),
        (try_begin), #SB : even more super-cheats
          (this_or_next|key_is_down, key_left_shift),
          (key_is_down, key_right_shift),
          (try_for_range, ":i_slot", 0, ":num_items_to_add"),
            (store_add, ":item_id", "$cheat_find_item_range_begin", ":i_slot"),
            (item_get_type, ":i_type", ":item_id"),
            (try_begin),
              (eq, ":i_type", itp_type_horse),
              (troop_add_item, "trp_find_item_cheat", ":item_id", imod_champion),
            (else_try),
              (this_or_next|eq, ":i_type", itp_type_shield),
              (is_between, ":i_type", itp_type_head_armor, itp_type_pistol),
              (troop_add_item, "trp_find_item_cheat", ":item_id", imod_lordly),
            (else_try),
              (this_or_next|is_between, ":i_type", itp_type_one_handed_wpn, itp_type_goods),
              (is_between, ":i_type", itp_type_pistol, itp_type_animal),
              (troop_add_item, "trp_find_item_cheat", ":item_id", imod_masterwork),
            (else_try),
              (troop_add_item, "trp_find_item_cheat", ":item_id", imod_plain),
            (try_end),
          (try_end),
          (change_screen_loot, "trp_find_item_cheat"),
        (else_try), #Native behaviour
          (try_for_range, ":i_slot", 0, ":num_items_to_add"),
            (store_add, ":item_id", "$cheat_find_item_range_begin", ":i_slot"),
            (troop_add_items, "trp_find_item_cheat", ":item_id", 1),
          (try_end),
          (change_screen_trade, "trp_find_item_cheat"),
        (try_end),
       ]
       ),
       
      ("camp_action_4",[],"{!}Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

   ("cheat_change_weather",0,
   "{!}Current cloud amount: {reg5}^Current Fog Strength: {reg6}",
   "none",
   [
     (get_global_cloud_amount, reg5),
     (get_global_haze_amount, reg6),
     ],
    [
      ("cheat_increase_cloud",[], "{!}Increase Cloud Amount.",
       [
	    (get_global_cloud_amount, ":cur_cloud_amount"),
		(val_add, ":cur_cloud_amount", 5),
		(val_min, ":cur_cloud_amount", 100),
	    (set_global_cloud_amount, ":cur_cloud_amount"),
	   ]
       ),
      ("cheat_decrease_cloud",[], "{!}Decrease Cloud Amount.",
       [
	    (get_global_cloud_amount, ":cur_cloud_amount"),
		(val_sub, ":cur_cloud_amount", 5),
		(val_max, ":cur_cloud_amount", 0),
	    (set_global_cloud_amount, ":cur_cloud_amount"),
	   ]
       ),
      ("cheat_increase_fog",[], "{!}Increase Fog Amount.",
       [
	    (get_global_haze_amount, ":cur_fog_amount"),
		(val_add, ":cur_fog_amount", 5),
		(val_min, ":cur_fog_amount", 100),
	    (set_global_haze_amount, ":cur_fog_amount"),
	   ]
       ),
      ("cheat_decrease_fog",[], "{!}Decrease Fog Amount.",
       [
	    (get_global_haze_amount, ":cur_fog_amount"),
		(val_sub, ":cur_fog_amount", 5),
		(val_max, ":cur_fog_amount", 0),
	    (set_global_haze_amount, ":cur_fog_amount"),
	   ]
       ),

      ("camp_action_4",[],"{!}Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_action",0,
   "Choose an action:",
   "none",
   [
     ],
    [


      ("camp_recruit_prisoners",
       [(troops_can_join, 1),
        (store_current_hours, ":cur_time"),
        (val_sub, ":cur_time", 24),
        (gt, ":cur_time", "$g_prisoner_recruit_last_time"),
        (try_begin),
          (gt, "$g_prisoner_recruit_last_time", 0),
          (assign, "$g_prisoner_recruit_troop_id", 0),
          (assign, "$g_prisoner_recruit_size", 0),
          (assign, "$g_prisoner_recruit_last_time", 0),
        (try_end),
        ], "Recruit some of your prisoners to your party.",
       [(jump_to_menu, "mnu_camp_recruit_prisoners"),
        ],
       ),

      ("action_read_book",[],"Select a book to read.",
       [(jump_to_menu, "mnu_camp_action_read_book"),
        ]
       ),
       
      ("action_food",[],"Change your party's food consumption habits.",
       [(start_presentation, "prsnt_food_options"),
        ]
       ),
       
      #SB : rename changes
      ("camp_change_name",[],"Change the name of your party.",
       [(assign, "$g_presentation_state", rename_party),
       (assign, "$g_encountered_party", "p_main_party"),
       (start_presentation, "prsnt_name_kingdom"),
       ]
       ),
       # #SB : recolor from CC, call this from other presentation
      # ("action_modify_factions_color",[],"Change the color of factions.",
       # [
          # (assign, "$g_presentation_state", recolor_kingdom),
          # (try_begin),
            # (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
            # (store_sub, "$temp", "$players_kingdom", npc_kingdoms_begin),
            # (store_sub, "$temp", 8, "$temp"), #3 to 8 are npc kingdoms
          # (else_try),
            # (assign, "$temp", 9), #player faction
          # (try_end),
          # (start_presentation, "prsnt_change_color"),
        # ]
       # ),
      ("action_rename_kingdom",
       [
         #SB : use bits
         (store_and, ":name_set", "$players_kingdom_name_set", rename_kingdom),
         (eq, ":name_set", rename_kingdom),
         (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
         (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
         ],"Rename your kingdom.",
       [
         #SB : explicitly state kingdom
         (assign, "$g_presentation_state", rename_kingdom),
         (start_presentation, "prsnt_name_kingdom"),
        ]
       ),
      # ("action_recolor_troops",
       # [
         # ],"Recolor your troop groups.",
       # [(assign, "$g_presentation_state", recolor_groups),
        # (jump_to_menu, "mnu_recolor_groups"),
        # ]
       # ),

      # ("action_rename_troops",
       # [
         # (gt, "$g_player_constable", 0),
         # (call_script, "script_cf_has_custom_troops"),
         # ],"Rename your custom troops.",
       # [
        # (jump_to_menu, "mnu_custom_troops"),
        # ]
       # ),
      ##diplomacy begin+
      ##Custom player kingdom vassal titles, credit Caba'drin start
       ("action_change_vassal_title",
        [
        #SB : allow action if co-ruler of $players_kingdom
          (assign, ":is_coruler", -1),
          (try_begin),
           (store_and, ":name_set", "$players_kingdom_name_set", rename_kingdom),
           (eq, ":name_set", rename_kingdom),
            (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
            (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
            (assign, ":is_coruler", 1),
          (else_try),
            (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
            (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
            (ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
            (assign, ":is_coruler", 1),
          (try_end),
          (eq, ":is_coruler", 1),
        ],"Change your vassals' title of nobility.",
        [(start_presentation, "prsnt_dplmc_set_vassal_title"),
        ]
       ),
       ("action_change_policies",
        [
            (gt, "$cheat_mode", 0),
            #SB : name set bits
            (store_and, ":name_set", "$players_kingdom_name_set", rename_kingdom),
            (eq, ":name_set", rename_kingdom),
            (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
            (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
        ],"{!}Cheat: Change kingdom policies",
        [(start_presentation, "prsnt_dplmc_policy_management"),

        ]
       ),
      ##Custom player kingdom vassal titles, credit Caba'drin end
      ##diplomacy end+
      ("action_modify_banner",[(eq, "$cheat_mode", 1)],"{!}Cheat: Modify your banner.",
       [
           #(start_presentation, "prsnt_banner_selection"),
           #(start_presentation, "prsnt_custom_banner"),
           (assign, "$g_edit_banner_troop", "trp_player"),
           (jump_to_menu, "mnu_choose_banner"),
        ]
       ),
      ("action_retire",[],"Retire from adventuring.",
       [(jump_to_menu, "mnu_retirement_verify"),
        ]
       ),
      ("camp_action_4",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_recruit_prisoners",0,
   "You offer your prisoners freedom if they agree to join you as soldiers. {s18}",
   "none",
   [(assign, ":num_regular_prisoner_slots", 0),
    (party_get_num_prisoner_stacks, ":num_stacks", "p_main_party"),
    (try_for_range, ":cur_stack", 0, ":num_stacks"),
      (party_prisoner_stack_get_troop_id, ":cur_troop_id", "p_main_party", ":cur_stack"),
      # (neg|troop_is_hero, ":cur_troop_id"),
      #SB : use script check
      (call_script, "script_game_check_prisoner_can_be_sold", ":cur_troop_id"),
      (eq, reg0, 1),
      (val_add, ":num_regular_prisoner_slots", 1),
    (try_end),
    (try_begin),
      (eq, ":num_regular_prisoner_slots", 0),
      (jump_to_menu, "mnu_camp_no_prisoners"),
    (else_try),
      (eq, "$g_prisoner_recruit_troop_id", 0),
      (store_current_hours, "$g_prisoner_recruit_last_time"),
      (store_random_in_range, ":rand", 0, 100),
      (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
      (store_sub, ":reject_chance", 15, ":persuasion_level"),
      (val_mul, ":reject_chance", 4),
      (try_begin),
        (lt, ":rand", ":reject_chance"),
        (assign, "$g_prisoner_recruit_troop_id", -7),
      (else_try),
        # (assign, ":num_regular_prisoner_slots", 0),
        # (party_get_num_prisoner_stacks, ":num_stacks", "p_main_party"),
        # (try_for_range, ":cur_stack", 0, ":num_stacks"),
          # (party_prisoner_stack_get_troop_id, ":cur_troop_id", "p_main_party", ":cur_stack"),
          # (neg|troop_is_hero, ":cur_troop_id"),
          # (val_add, ":num_regular_prisoner_slots", 1),
        # (try_end),
        (store_random_in_range, ":random_prisoner_slot", 0, ":num_regular_prisoner_slots"),
        (try_for_range, ":cur_stack", 0, ":num_stacks"),
          (party_prisoner_stack_get_troop_id, ":cur_troop_id", "p_main_party", ":cur_stack"),
          (call_script, "script_game_check_prisoner_can_be_sold", ":cur_troop_id"),
          (eq, reg0, 1), #SB : use script call to prevent quest troops from being recruited
          (val_sub, ":random_prisoner_slot", 1),
          (lt, ":random_prisoner_slot", 0),
          (assign, ":num_stacks", 0),
          (assign, "$g_prisoner_recruit_troop_id", ":cur_troop_id"),
          (party_prisoner_stack_get_size, "$g_prisoner_recruit_size", "p_main_party", ":cur_stack"),
        (try_end),
      (try_end),

      (try_begin),
        (gt, "$g_prisoner_recruit_troop_id", 0),
        (party_get_free_companions_capacity, ":capacity", "p_main_party"),
        (val_min, "$g_prisoner_recruit_size", ":capacity"),
        (assign, reg1, "$g_prisoner_recruit_size"),
        (gt, "$g_prisoner_recruit_size", 0),
        (try_begin),
          (gt, "$g_prisoner_recruit_size", 1),
          (assign, reg2, 1),
        (else_try),
          (assign, reg2, 0),
        (try_end),
        (str_store_troop_name_by_count, s1, "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
        (str_store_string, s18, "@{reg1} {s1} {reg2?accept:accepts} the offer."),
      (else_try),
        (str_store_string, s18, "@No one accepts the offer."),
      (try_end),
    (try_end),
    ],
    [
      ("camp_recruit_prisoners_accept",[(gt, "$g_prisoner_recruit_troop_id", 0)],"Take them.",
       [(remove_troops_from_prisoners, "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
        (party_add_members, "p_main_party", "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
        #SB : change base morale reduction by difficulty
        (game_get_reduce_campaign_ai, ":reduce"), #0 to 2
        (val_sub, ":reduce", 4), #-4 to -2
        (store_mul, ":morale_change", ":reduce", "$g_prisoner_recruit_size"),
        (store_troop_faction, ":troop_faction", "$g_prisoner_recruit_troop_id"),
        (store_character_level, ":troop_level", "$g_prisoner_recruit_troop_id"),

        (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
          (faction_set_slot, ":faction", slot_faction_temp_slot, 0),
        (try_end),
        (try_begin), #give extra penalty to faction morale if we recruit high-level enemy troops
          (this_or_next|eq, ":troop_faction", "fac_outlaws"),
          (eq, ":troop_faction", "fac_deserters"),
          (call_script, "script_objectionable_action", tmt_aristocratic, "str_hire_deserters"),
        (else_try),
          (is_between, ":troop_faction", npc_kingdoms_begin, npc_kingdoms_end),
          # (store_character_level, ":relation", "$g_prisoner_recruit_troop_id"),
          (try_begin), #check culture
            (eq, "$players_kingdom", "fac_player_supporters_faction"),
            (is_between, "$g_player_culture", npc_kingdoms_begin, npc_kingdoms_end),
            (eq, "$g_player_culture", ":troop_faction"),
            (assign, ":troop_faction", "$players_kingdom"),
          (try_end),
          (try_begin), #no penalty for same faction
            (eq, ":troop_faction", "$players_kingdom"),
            # (val_sub, ":relation", ":morale_change"), #bonus
            (assign, ":morale_change", 0),
            (assign, "$g_prisoner_recruit_troop_id", 0),
            (assign, "$g_prisoner_recruit_size", 0),
          (else_try), #one point per offended party
            (party_get_num_companion_stacks, ":cap", "p_main_party"),
            (try_for_range, ":stack", 1, ":cap"),
              (party_stack_get_troop_id, ":troop", "p_main_party", ":stack"),
              # (neg|troop_is_hero, ":troop"),
              # (neq, ":troop", "$g_prisoner_recruit_troop_id"), #not just recruited
              (store_faction_of_troop, ":stack_faction", ":troop"),
              # (neq, ":stack_faction", ":troop_faction"),
              (store_relation, ":faction_relation", ":troop_faction", ":stack_faction"),
              (lt, ":faction_relation", 0),
              (faction_get_slot, ":amount", ":stack_faction", slot_faction_temp_slot),
              (party_stack_get_size, ":reduce", "p_main_party", ":stack"),
              (val_sub, ":amount", ":reduce"),
              (faction_set_slot, ":stack_faction", slot_faction_temp_slot, ":amount"),
            (try_end),
          (try_end),
        (try_end),
        (call_script, "script_change_player_party_morale", ":morale_change"),
        (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
          (faction_get_slot, ":relation", ":faction", slot_faction_temp_slot),
          (neq, ":relation", 0),
          (val_sub, ":relation", ":troop_level"),
          (call_script, "script_change_faction_troop_morale", ":faction", ":relation", 1),
        (try_end),
        (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("camp_recruit_prisoners_reject",[(gt, "$g_prisoner_recruit_troop_id", 0)],"Reject them.",
       [(jump_to_menu, "mnu_camp"),
        (assign, "$g_prisoner_recruit_troop_id", 0),
        (assign, "$g_prisoner_recruit_size", 0),
        ]
       ),
      ("continue",[(le, "$g_prisoner_recruit_troop_id", 0)],"Go back.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_no_prisoners",0,
   "You have no prisoners to recruit from.",
   "none",
   [],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_action_read_book",0,
   "Choose a book to read:",
   "none",
   [],
    [
      ("action_read_book_1",[(player_has_item, "itm_book_tactics"),
                             (item_slot_eq, "itm_book_tactics", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_tactics"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_tactics"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_2",[(player_has_item, "itm_book_persuasion"),
                             (item_slot_eq, "itm_book_persuasion", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_persuasion"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_persuasion"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_3",[(player_has_item, "itm_book_leadership"),
                             (item_slot_eq, "itm_book_leadership", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_leadership"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_leadership"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_4",[(player_has_item, "itm_book_intelligence"),
                             (item_slot_eq, "itm_book_intelligence", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_intelligence"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_intelligence"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_5",[(player_has_item, "itm_book_trade"),
                             (item_slot_eq, "itm_book_trade", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_trade"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_trade"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_6",[(player_has_item, "itm_book_weapon_mastery"),
                             (item_slot_eq, "itm_book_weapon_mastery", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_weapon_mastery"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_weapon_mastery"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_7",[(player_has_item, "itm_book_engineering"),
                             (item_slot_eq, "itm_book_engineering", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_engineering"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_engineering"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("camp_action_4",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_action_read_book_start",0,
   "{s1}",
   "none",
   [(assign, ":new_book", "$temp"),
    (str_store_item_name, s2, ":new_book"),
    (try_begin),
      (store_attribute_level, ":int", "trp_player", ca_intelligence),
      (item_get_slot, ":int_req", ":new_book", slot_item_intelligence_requirement),
      (le, ":int_req", ":int"),
      (str_store_string, s1, "@You start reading {s2}. After a few pages,\
 you feel you could learn a lot from this book. You decide to keep it close by and read whenever you have the time."),
      (assign, "$g_player_reading_book", ":new_book"),
    (else_try),
      (str_store_string, s1, "@You flip through the pages of {s2}, but you find the text confusing and difficult to follow.\
 Try as you might, it soon gives you a headache, and you're forced to give up the attempt."),
    (try_end),],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),


  ("retirement_verify",0,
   "You are at day {reg0}. Your current luck is {reg1}. Are you sure you want to retire?",
   "none",
   [
     (store_current_day, reg0),
     (assign, reg1, "$g_player_luck"),
     ],
    [
      ("retire_yes",[],"Yes.",
       [
         (start_presentation, "prsnt_retirement"),
        ]
       ),
      ("retire_no",[],"No.",
       [
         (jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("end_game",0,
   "The decision is made, and you resolve to give up your adventurer's\
 life and settle down. You sell off your weapons and armour, gather up\
 all your money, and ride off into the sunset....",
   "none",
   [],
    [
      ("end_game_bye",[],"Farewell.",
       [
         (change_screen_quit),
        ]
       ),
      ]
  ),

  ("cattle_herd",mnf_scale_picture,
   "You encounter a herd of cattle.",
   "none",
   [(play_sound, "snd_cow_moo"),
    (set_background_mesh, "mesh_pic_cattle"),
   ],
    [
      ("cattle_drive_away",[],"Drive the cattle onward.",
       [
        (party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 1),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_driven_by_party),
        (party_set_ai_object,"$g_encountered_party", "p_main_party"),
        (party_set_extra_text, "$g_encountered_party", "str_ai_bhvr_driven_by_party"),
        (change_screen_return),
        ]
       ),
       
       #SB : cattle tweaks
      ("cattle_drag_with",[
       # (call_script, "script_party_count_members_with_full_health", "p_main_party"),
       # (assign, ":size", reg0),
       # (party_stack_get_size, ":num_cattle", "$g_encountered_party", 0),
       # (gt, ":size", ":num_cattle"),
      ],"Drag the cattle with you.",
       [
        (party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 1),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_escort_party),
        (party_set_ai_object,"$g_encountered_party", "p_main_party"),
        (party_set_extra_text, "$g_encountered_party", "str_ai_bhvr_escort_party"),
        (change_screen_return),
        ]
       ),

      ("cattle_stop",[],"Bring the herd to a stop.",
       [
        (party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 0),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_hold),
        (party_set_extra_text, "$g_encountered_party", "@Grazing"),
        (change_screen_return),
        ]
       ),
      ("cattle_kill",[(assign, ":continue", 1),
                      (try_begin),
                        (check_quest_active, "qst_move_cattle_herd"),
                        (quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, "$g_encountered_party"),
                        (assign, ":continue", 0),
                      (try_end),
                      (eq, ":continue", 1)],"Slaughter some of the animals.",
       [(jump_to_menu, "mnu_cattle_herd_kill"),
        ]
       ),
      ("leave",[],"Leave.",
       [(change_screen_return),
        ]
       ),
      ]
  ),

  ("cattle_herd_kill",0,
   "How many animals do you want to slaughter?",
   "none",
   [(party_get_num_companions, reg5, "$g_encountered_party")],
    [
      ("cattle_kill_1",[(ge, reg5, 1),],"One.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 1),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_2",[(ge, reg5, 2),],"Two.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 2),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_3",[(ge, reg5, 3),],"Three.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 3),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_4",[(ge, reg5, 4),],"Four.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 4),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_5",[(ge, reg5, 5),],"Five.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 5),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_cattle_herd"),
        ]
       ),
      ]
  ),

  ("cattle_herd_kill_end",0,
   "{!}You shouldn't be reading this.",
   "none",
   [(change_screen_return)],
    [
      ]
  ),


  ("arena_duel_fight",0,
   "You and your opponent prepare to duel.",
   "none",
   [
      (troop_get_slot, ":leader_troop_faction", "$g_duel_troop", slot_troop_original_faction),
      (try_begin),
        (eq, ":leader_troop_faction", fac_kingdom_1),
        (set_background_mesh, "mesh_pic_swad"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_2),
        (set_background_mesh, "mesh_pic_vaegir"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_3),
        (set_background_mesh, "mesh_pic_khergit"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_4),
        (set_background_mesh, "mesh_pic_nord"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_5),
        (set_background_mesh, "mesh_pic_rhodock"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_6),
        (set_background_mesh, "mesh_pic_sarranid_encounter"),
      (try_end),
   ],
   [
     ("continue",[],"Continue...",
      [
        (assign, "$g_leave_encounter", 0),
        (assign, ":closest_town", "$g_encountered_party"),

        #restructure this to take into account $g_start_arena_fight_at_nearest_town
        (try_begin), #check if the parameter is necessary
          (neg|is_between, ":closest_town", walled_centers_begin, walled_centers_end),
          (is_between, "$g_start_arena_fight_at_nearest_town", walled_centers_begin, walled_centers_end),
          (assign, ":closest_town", "$g_start_arena_fight_at_nearest_town"),
          (assign, "$g_start_arena_fight_at_nearest_town", 0),
        (try_end),

        (try_begin),
          (is_between, ":closest_town", towns_begin, towns_end),
          (party_get_slot, ":duel_scene", ":closest_town", slot_town_arena),
        (else_try), #SB : duels at castle arena
          (is_between, ":closest_town", castles_begin, castles_end),
          (party_get_slot, ":duel_scene", ":closest_town", slot_castle_exterior),
        (else_try),
          (party_get_current_terrain, ":terrain", "p_main_party"),
          (eq, ":terrain", rt_snow),
          (assign, ":duel_scene", "scn_training_ground_ranged_melee_3"),
        (else_try),
          (this_or_next|eq, ":terrain", rt_desert),
          (eq, ":terrain", rt_steppe), #this is the actual steppe scene
          (assign, ":duel_scene", "scn_training_ground_ranged_melee_4"),
        (else_try),
          (assign, ":duel_scene", "scn_training_ground_ranged_melee_1"),
        (try_end),
        (modify_visitors_at_site, ":duel_scene"),
        (reset_visitors),
        # (set_visitor, 0, "trp_player"),
        # (set_visitor, 1, "$g_duel_troop"),
        (troop_set_slot, "trp_tournament_participants", 0, "trp_player"),
        (troop_set_slot, "trp_tournament_participants", 1, "$g_duel_troop"),
        (set_jump_mission, "mt_duel_with_lord"),
        #SB : check relative standing, 0 = (higher renown)
        (try_begin),
          (troop_is_hero, "$g_duel_troop"),
          (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
          (troop_slot_ge, "$g_duel_troop", slot_troop_renown, ":player_renown"),
          #swap positions
          (troop_set_slot, "trp_tournament_participants", 1, "trp_player"),
          (troop_set_slot, "trp_tournament_participants", 0, "$g_duel_troop"),
        (try_end),
        #SB : set up additional equipment, do not always use sword_medieval_a
        (troop_get_slot, ":faction", "$g_duel_troop", slot_troop_original_faction),
        (try_begin),
          (this_or_next|eq, ":faction", "fac_kingdom_1"),
          (eq, ":faction", "fac_kingdom_5"),
          (store_random_in_range, ":weapon", "itm_sword_medieval_a", "itm_sword_viking_1"),
        (else_try),
          (eq, ":faction", "fac_kingdom_3"),
          (assign, ":weapon", "itm_sword_khergit_1"),
        (else_try),
          (this_or_next|eq, ":faction", "fac_kingdom_2"),
          (eq, ":faction", "fac_kingdom_4"),
          (store_random_in_range, ":weapon", "itm_sword_viking_1", "itm_sword_viking_3_small"),
        # (else_try),
          # (eq, ":faction", "fac_kingdom_5"), #no requirement
          # (assign, ":weapon", "itm_military_cleaver_b"),
        (else_try),
          (eq, ":faction", "fac_kingdom_6"),
          (assign, ":weapon", "itm_scimitar"),
        (else_try),
          (assign, ":weapon", "itm_arena_sword"),
        (try_end),
        
        (try_for_range, ":cur_entry_point", 0, 2),
          (troop_get_slot, ":cur_troop", "trp_tournament_participants", ":cur_entry_point"),
          (try_begin), #within the courtyard, 23/24 is guard entry
            (is_between, ":closest_town", castles_begin, castles_end),
            (val_add, ":cur_entry_point", 2), #to use the new mission template entries 3 & 4
          (try_end),

          (mission_tpl_entry_clear_override_items, "mt_duel_with_lord", ":cur_entry_point"),
          #weapon, make sure they have no difficulty requirement
          (mission_tpl_entry_add_override_item, "mt_duel_with_lord", ":cur_entry_point", ":weapon"),
          # (item_get_type, ":type", ":weapon"),
          # (try_begin),
            # (is_between, ":type", itp_type_pistol, itp_type_bullets),
            # (mission_tpl_entry_add_override_item, "mt_duel_with_lord", ":cur_entry_point", "itm_cartridges2"),
            # (mission_tpl_entry_add_override_item, "mt_duel_with_lord", ":cur_entry_point", "itm_dagger"),#backup
          # (else_try),
            # (eq, ":type", itp_type_crossbow),
            # (mission_tpl_entry_add_override_item, "mt_duel_with_lord", ":cur_entry_point", "itm_practice_bolts_9_amount"),
            # (mission_tpl_entry_add_override_item, "mt_duel_with_lord", ":cur_entry_point", "itm_estoc"),#backup
          # (else_try),
            # (eq, ":type", itp_type_bow),
            # (mission_tpl_entry_add_override_item, "mt_duel_with_lord", ":cur_entry_point", "itm_practice_arrows_10_amount"),
            # (mission_tpl_entry_add_override_item, "mt_duel_with_lord", ":cur_entry_point", ":backup"),#backup
          # (try_end),

          #armor, they're statistically almost the same
          # (troop_get_slot, ":renown", ":cur_troop", slot_troop_renown),
          # (val_min, ":renown", 2000),
          # (store_div, ":armor", ":renown", 500),#0 to 3
          # (val_add, ":armor", "itm_heraldic_mail_with_surcoat"),
          # (mission_tpl_entry_add_override_item, "mt_duel_with_lord", ":cur_entry_point", ":armor"),

          (set_visitor, ":cur_entry_point", ":cur_troop"),
        (try_end),

        (jump_to_scene, ":duel_scene"),
        (jump_to_menu, "mnu_arena_duel_conclusion"),
        (change_screen_mission),
      ]),
    ]
  ),


  ("arena_duel_conclusion",0,
   "{!}{s11}",
   "none",
   [

    (try_begin),
		(eq, "$g_leave_encounter", 1),
		(change_screen_return),
	(try_end),

    (str_store_troop_name, s10, "$g_duel_troop"),
    #SB : change to loop
    (store_add, ":end", lady_quests_end, 2),
    (try_for_range, ":quest", "qst_duel_for_lady", ":end"),
      (try_begin),
        (eq, ":quest", lady_quests_end),
        (assign, ":quest", "qst_denounce_lord"),
      (try_end),
      (quest_slot_eq, ":quest", slot_quest_target_troop, "$g_duel_troop"),
      (try_begin),
        (check_quest_succeeded, ":quest"),
        (str_store_string, s11, "str_s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel"),
        #(set_background_mesh, "mesh_pic_victory"),
      (else_try),
        (check_quest_failed, ":quest"),
        (str_store_string, s11, "str_you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel"),
        #(set_background_mesh, "mesh_pic_defeat"),
      (try_end),
    (try_end),
   ],
   [
     ("continue",[],"Continue...",
      [
        (assign, "$talk_context", tc_after_duel),
        (try_begin), #SB : use the appropriate script calls
          (is_between, "$g_encountered_party", centers_begin, centers_end),
          (call_script, "script_start_court_conversation", "$g_duel_troop", "$g_encountered_party"), #SB : script call
        (else_try),
          (call_script, "script_setup_troop_meeting", "$g_duel_troop", -1), #SB : script call
        (try_end),
        ]),
      ]
  ),


  (
    "simple_encounter",mnf_enable_hot_keys|mnf_scale_picture,
    "{s2} You have {reg10} troops fit for battle against their {reg11}.",
    "none",
    [
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", -1),
        (call_script, "script_encounter_calculate_fit"),
        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (assign, "$g_encounter_is_in_village", 0),
          (assign, "$g_encounter_type", 0),
          (try_begin),
            (party_slot_eq, "$g_enemy_party", slot_party_ai_state, spai_raiding_around_center),
            (party_get_slot, ":village_no", "$g_enemy_party", slot_party_ai_object),

            (store_distance_to_party_from_party, ":dist", ":village_no", "$g_enemy_party"),

            (try_begin),
              (lt, ":dist", raid_distance),
              (assign, "$g_encounter_is_in_village", ":village_no"),
              (assign, "$g_encounter_type", enctype_fighting_against_village_raid),
            (try_end),
          (try_end),
          (try_begin),
            (gt, "$g_player_raiding_village", 0),
            (assign, "$g_encounter_is_in_village", "$g_player_raiding_village"),
            (assign, "$g_encounter_type", enctype_catched_during_village_raid),
            (party_quick_attach_to_current_battle, "$g_encounter_is_in_village", 1), #attach as enemy
            (str_store_string, s1, "@Villagers"),
            (display_message, "str_s1_joined_battle_enemy", message_negative), #SB : colorize
          (else_try),
            (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
            (party_quick_attach_to_current_battle, "$g_encounter_is_in_village", 0), #attach as friend
            (str_store_string, s1, "@Villagers"),
            (display_message, "str_s1_joined_battle_friend", message_positive), #SB : colorize
            # Let village party join battle at your side
          (try_end),

          (call_script, "script_let_nearby_parties_join_current_battle", 0, 0),
          (call_script, "script_encounter_init_variables"),
          (assign, "$encountered_party_hostile", 0),
          (assign, "$encountered_party_friendly", 0),
          (try_begin),
            (gt, "$g_encountered_party_relation", 0),
            (try_begin), #SB : apply provocation override
              (check_quest_active, "qst_cause_provocation"),
              (neg|check_quest_concluded, "qst_cause_provocation"),
              (quest_slot_eq, "qst_cause_provocation", slot_quest_target_faction, "$g_encountered_party_faction"),
              (party_slot_eq, "$g_encountered_party", slot_party_type, spt_kingdom_caravan),
              (assign, "$encountered_party_friendly", 0),
            (else_try),
              (assign, "$encountered_party_friendly", 1),
            (try_end),
          (try_end),
          
          (try_begin),
            (lt, "$g_encountered_party_relation", 0),
            (assign, "$encountered_party_hostile", 1),
            (try_begin),
              (encountered_party_is_attacker),
              (assign, "$cant_leave_encounter", 1),
            (try_end),
          (try_end),
          (assign, "$talk_context", tc_party_encounter),
          (call_script, "script_setup_party_meeting", "$g_encountered_party"),
        (else_try), #second or more turn
#          (try_begin),
#            (call_script, "script_encounter_calculate_morale_change"),
#          (try_end),
          (try_begin),
            # We can leave battle only after some troops have been killed.
            (eq, "$cant_leave_encounter", 1),
            (call_script, "script_party_count_members_with_full_health", "p_main_party_backup"),
            (assign, ":org_total_party_counts", reg0),
            (call_script, "script_party_count_members_with_full_health", "p_encountered_party_backup"),
            (val_add, ":org_total_party_counts", reg0),

            (call_script, "script_party_count_members_with_full_health", "p_main_party"),
            (assign, ":cur_total_party_counts", reg0),
            (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
            (val_add, ":cur_total_party_counts", reg0),

            (store_sub, ":leave_encounter_limit", ":org_total_party_counts", 10),
            (lt, ":cur_total_party_counts", ":leave_encounter_limit"),
            (assign, "$cant_leave_encounter", 0),
          (try_end),
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (try_end),

        #setup s2
        (try_begin),
          (party_is_active, "$g_encountered_party"),
          (str_store_party_name, s1,"$g_encountered_party"),
          (try_begin),
            (eq, "$g_encounter_type", 0),
            (str_store_string, s2,"@You have encountered {s1}."),
          (else_try),
            (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
            (str_store_party_name, s3, "$g_encounter_is_in_village"),
            (str_store_string, s2,"@You have engaged {s1} while they were raiding {s3}."),
          (else_try),
            (eq, "$g_encounter_type", enctype_catched_during_village_raid),
            (str_store_party_name, s3, "$g_encounter_is_in_village"),
            (str_store_string, s2,"@You were caught by {s1} while your forces were raiding {s3}."),
          (try_end),
        (try_end),
        (try_begin),
          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
          (assign, ":num_enemy_regulars_remaining", reg0),
          (assign, ":enemy_finished", 0),
          (try_begin),
            (eq, "$g_battle_result", 1), #battle won

            (this_or_next|le, ":num_enemy_regulars_remaining", 0), #battle won
            (le, ":num_enemy_regulars_remaining",  "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

            (assign, ":enemy_finished",1),
          (else_try),
            (eq, "$g_engaged_enemy", 1),

            (this_or_next|le, ":num_enemy_regulars_remaining", 0),
            (le, "$g_enemy_fit_for_battle", "$num_routed_enemies"),  #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

            (ge, "$g_friend_fit_for_battle",1),
            (assign, ":enemy_finished",1),
          (try_end),

          (this_or_next|eq, ":enemy_finished",1),
          # (this_or_next|eq, ":num_enemy_regulars_remaining",0),
          (eq,"$g_enemy_surrenders",1),
          (assign, "$g_next_menu", -1),
          (jump_to_menu, "mnu_total_victory"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),
          (assign, ":num_our_regulars_remaining", reg0),
          (assign, ":friends_finished",0),
          (try_begin),
            (eq, "$g_battle_result", -1),

            #(eq, ":num_our_regulars_remaining", 0), #battle lost
            (le, ":num_our_regulars_remaining",  "$num_routed_us"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

            (assign,  ":friends_finished", 1),
          (else_try),
            (eq, "$g_engaged_enemy", 1),
            (ge, "$g_enemy_fit_for_battle",1),
            (le, "$g_friend_fit_for_battle",0),
            (assign, ":friends_finished",1),
          (try_end),

          (this_or_next|eq, ":friends_finished",1),
          (eq,"$g_player_surrenders",1),
          (assign, "$g_next_menu", "mnu_captivity_start_wilderness"),
          (jump_to_menu, "mnu_total_defeat"),
        (try_end),


        (try_begin),
          (eq, "$g_encountered_party_template", "pt_looters"),
          (set_background_mesh, "mesh_pic_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_mountain_bandits"),
          (set_background_mesh, "mesh_pic_mountain_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_steppe_bandits"),
          (set_background_mesh, "mesh_pic_steppe_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_taiga_bandits"),
          (set_background_mesh, "mesh_pic_steppe_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_sea_raiders"),
          (set_background_mesh, "mesh_pic_sea_raiders"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_forest_bandits"),
          (set_background_mesh, "mesh_pic_forest_bandits"),
        (else_try),
          (this_or_next|eq, "$g_encountered_party_template", "pt_deserters"),
          (eq, "$g_encountered_party_template", "pt_routed_warriors"),
          (set_background_mesh, "mesh_pic_deserters"),
        #SB : dplmc party templates
        (else_try),
          (eq, "$g_encountered_party_template", "pt_center_reinforcements"),
          (set_background_mesh, "mesh_pic_recruits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_kingdom_hero_party"),
		  (party_stack_get_troop_id, ":leader_troop", "$g_encountered_party", 0),
		  (ge, ":leader_troop", 1),
		  (troop_get_slot, ":leader_troop_faction", ":leader_troop", slot_troop_original_faction),
		  (try_begin),
			(eq, ":leader_troop_faction", fac_kingdom_1),
            (set_background_mesh, "mesh_pic_swad"),
		  (else_try),
			(eq, ":leader_troop_faction", fac_kingdom_2),
            (set_background_mesh, "mesh_pic_vaegir"),
		  (else_try),
			(eq, ":leader_troop_faction", fac_kingdom_3),
            (set_background_mesh, "mesh_pic_khergit"),
		  (else_try),
			(eq, ":leader_troop_faction", fac_kingdom_4),
            (set_background_mesh, "mesh_pic_nord"),
		  (else_try),
			(eq, ":leader_troop_faction", fac_kingdom_5),
            (set_background_mesh, "mesh_pic_rhodock"),
		  (else_try),
			(eq, ":leader_troop_faction", fac_kingdom_6),
            (set_background_mesh, "mesh_pic_sarranid_encounter"),
		  (try_end),
        (try_end),
    ],
    [
      ("encounter_attack",
      [
        (eq, "$encountered_party_friendly", 0),
        (neg|troop_is_wounded, "trp_player"),
      ],
      "Charge the enemy.",
      [
        (assign, "$g_battle_result", 0),
        (assign, "$g_engaged_enemy", 1),
        
        (assign, "$player_deploy_troops", 1),

        (party_get_template_id, ":encountered_party_template", "$g_encountered_party"),
        (try_begin),
		  (eq, ":encountered_party_template", "pt_village_farmers"),
		  (unlock_achievement, ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED),
		(try_end),

        (call_script, "script_calculate_renown_value"),
		##diplomacy start+
		(try_begin),
			#Call this to properly set cached values for strength
			(eq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
			(assign, ":terrain_code", dplmc_terrain_code_none),#defined in header_terrain_types.py
			(try_begin),
				(this_or_next|eq, "$g_encounter_type", enctype_fighting_against_village_raid),
					(eq, "$g_encounter_type", enctype_catched_during_village_raid),
				(assign, ":terrain_code", dplmc_terrain_code_village),#defined in header_terrain_types.py
			(else_try),
				(encountered_party_is_attacker),
				(call_script, "script_dplmc_get_terrain_code_for_battle", "$g_encountered_party", "p_main_party"),
				(assign, ":terrain_code", reg0),
			(else_try),
				(call_script, "script_dplmc_get_terrain_code_for_battle", "p_main_party", "$g_encountered_party"),
				(assign, ":terrain_code", reg0),
			(try_end),
			(neq, ":terrain_code", dplmc_terrain_code_none),
			(call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_main_party", ":terrain_code", 0, 1),
			(call_script, "script_dplmc_party_calculate_strength_in_terrain", "$g_encountered_party", ":terrain_code", 0, 1),
		(try_end),
		##diplomacy end+
        (call_script, "script_calculate_battle_advantage"),
        (set_battle_advantage, reg0),
        (set_party_battle_mode),

        (try_begin),
          (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
          (assign, "$g_village_raid_evil", 0),
          (set_jump_mission,"mt_village_raid"),
          (party_get_slot, ":scene_to_use", "$g_encounter_is_in_village", slot_castle_exterior),
          (jump_to_scene, ":scene_to_use"),
        (else_try),
          (eq, "$g_encounter_type", enctype_catched_during_village_raid),
          (assign, "$g_village_raid_evil", 1), #SB : probably true
          (set_jump_mission,"mt_village_raid"),
          (party_get_slot, ":scene_to_use", "$g_encounter_is_in_village", slot_castle_exterior),
          (jump_to_scene, ":scene_to_use"),
        (else_try),
          (set_jump_mission,"mt_lead_charge"),
          (call_script, "script_setup_random_scene"),
        (try_end),
        (assign, "$g_next_menu", "mnu_simple_encounter"),
        (jump_to_menu, "mnu_battle_debrief"),
        (change_screen_mission),
      ]),

      ("encounter_order_attack",
      [
        (eq, "$encountered_party_friendly", 0),
        (call_script, "script_party_count_members_with_full_health", "p_main_party"),(ge, reg0, 4),
      ],
      "Order your troops to attack without you.",
      [
        (jump_to_menu, "mnu_order_attack_begin"),
        #(simulate_battle,3),
      ]),

      ("encounter_leave",[
          (eq,"$cant_leave_encounter", 0),
          ],"Leave.",[

###NPC companion changes begin
              (try_begin),
                  (eq, "$encountered_party_friendly", 0),
                  (encountered_party_is_attacker),
                  (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
              (try_end),
###NPC companion changes end
#Troop commentary changes begin
              (try_begin),
                  (eq, "$encountered_party_friendly", 0),
#                  (encountered_party_is_attacker),
                  (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
                  (try_for_range, ":stack_no", 0, ":num_stacks"),
                    (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
                    (is_between, ":stack_troop", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
                    (store_troop_faction, ":victorious_faction", ":stack_troop"),
#					(store_relation, ":relation_with_stack_troop", ":victorious_faction", "fac_player_faction"),
#					(lt, ":relation_with_stack_troop", 0),
                    (call_script, "script_add_log_entry", logent_player_retreated_from_lord, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
                  (try_end),
              (try_end),
#Troop commentary changes end
          	(leave_encounter),(change_screen_return)]),
      ("encounter_retreat",[
         (eq,"$cant_leave_encounter", 1),
         (call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
         (assign, ":max_skill", reg0),
         (val_add, ":max_skill", 4),

         (call_script, "script_party_count_members_with_full_health", "p_collective_enemy", 0),
         (assign, ":enemy_party_strength", reg0),
         (val_div, ":enemy_party_strength", 2),

         (val_div, ":enemy_party_strength", ":max_skill"),
         (val_max, ":enemy_party_strength", 1),

         (call_script, "script_party_count_fit_regulars", "p_main_party"),
         (assign, ":player_count", reg0),
         (ge, ":player_count", ":enemy_party_strength"),
         ],"Pull back, leaving some soldiers behind to cover your retreat.",[(jump_to_menu, "mnu_encounter_retreat_confirm"),]),

      ("encounter_surrender",[
         (eq,"$cant_leave_encounter", 1),
          ],"Surrender.",[(assign,"$g_player_surrenders",1)]),
    ]
  ),
  (
    "encounter_retreat_confirm",0,
    "As the party member with the highest tactics skill,\
 ({reg2}), {reg3?you devise:{s3} devises} a plan that will allow you and your men to escape with your lives,\
 but you'll have to leave {reg4} soldiers behind to stop the enemy from giving chase.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),
     (val_add, ":max_skill", 4),

     (call_script, "script_party_count_members_with_full_health", "p_collective_enemy", 0),
     (assign, ":enemy_party_strength", reg0),
     (val_div, ":enemy_party_strength", 2),

     (store_div, reg4, ":enemy_party_strength", ":max_skill"),
     (val_max, reg4, 1),

     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
     
    #SB : add tableau
    (set_fixed_point_multiplier, 100),
    (position_set_x, pos0, 70),
    (position_set_y, pos0, 5),
    (position_set_z, pos0, 75),
    (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", ":max_skill_owner", pos0),
     ],
    [
      ("leave_behind",[],"Go on. The sacrifice of these men will save the rest.",[
          (assign, ":num_casualties", reg4),
          (try_for_range, ":unused", 0, ":num_casualties"),
            (call_script, "script_cf_party_remove_random_regular_troop", "p_main_party"),
            (assign, ":lost_troop", reg0),
            (store_random_in_range, ":random_no", 0, 100),
            (ge, ":random_no", 30),
            (party_add_prisoners, "$g_encountered_party", ":lost_troop", 1),
           (try_end),
           (call_script, "script_change_player_party_morale", -20),
           (call_script, "script_change_troop_renown", "trp_player", -7), #SB : renown change
           (try_begin), #SB: max skill owner uses tactics
             # (eq, reg3, 0),
             (call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
             (is_between, reg1, companions_begin, companions_end),
             (call_script, "script_change_troop_renown", reg1, dplmc_companion_battle_renown), #SB : renown change, less reward
           (try_end),
           (jump_to_menu, "mnu_encounter_retreat"),
          ]),
      ("dont_leave_behind",[],"No. We leave no one behind.",[(jump_to_menu, "mnu_simple_encounter"),]),
    ]
  ),
  (
    "encounter_retreat",0,
    "You tell {reg4} of your troops to hold the enemy while you retreat with the rest of your party.",
    "none",
    [
     ],
    [
      ("continue",[],"Continue...",
	  [
###Troop commentary changes begin
          (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
          (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
          (try_for_range, ":stack_no", 0, ":num_stacks"),
              (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
              (is_between, ":stack_troop", active_npcs_begin, active_npcs_end),
              (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
              (store_troop_faction, ":victorious_faction", ":stack_troop"),
              (call_script, "script_add_log_entry", logent_player_retreated_from_lord_cowardly, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
          (try_end),
###Troop commentary changes end
        (party_ignore_player, "$g_encountered_party", 1),
        (leave_encounter),
		(change_screen_return),
          ##diplomacy begin
          #(assign, "$g_move_fast", 1),
          ##diplomacy end
          ]),
    ]
  ),
  (
    "order_attack_begin",0,
    "Your troops prepare to attack the enemy.",
    "none",
    [],
    [
      ("order_attack_begin",[],"Order the attack to begin.",
      [
        (party_get_template_id, ":encountered_party_template", "$g_encountered_party"),
        (try_begin),
		  (eq, ":encountered_party_template", "pt_village_farmers"),
		  (unlock_achievement, ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED),
		(try_end),

        (assign, "$g_engaged_enemy", 1),
        (jump_to_menu,"mnu_order_attack_2"),
      ]),
      ("call_back",[],"Call them back.",[(jump_to_menu,"mnu_simple_encounter")]),
    ]
  ),
  (
    "order_attack_2",mnf_disable_all_keys,
    "{s4}^^Your casualties: {s8}^^Enemy casualties: {s9}",
    "none",
    [
      (set_background_mesh, "mesh_pic_charge"),

      (call_script, "script_party_calculate_strength", "p_main_party", 1), #exclude player
      (assign, ":player_party_strength", reg0),

      (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
      (assign, ":enemy_party_strength", reg0),

      (party_collect_attachments_to_party, "p_main_party", "p_collective_ally"),
      (call_script, "script_party_calculate_strength", "p_collective_ally", 1), #exclude player
      (assign, ":total_player_and_followers_strength", reg0),

      (try_begin),
        (le, ":total_player_and_followers_strength", ":enemy_party_strength"),
        (assign, ":minimum_power", ":total_player_and_followers_strength"),
      (else_try),
        (assign, ":minimum_power", ":enemy_party_strength"),
      (try_end),

      (try_begin),
        (le, ":minimum_power", 25),
        (assign, ":division_constant", 1),
      (else_try),
        (le, ":minimum_power", 50),
        (assign, ":division_constant", 2),
      (else_try),
        (le, ":minimum_power", 75),
        (assign, ":division_constant", 3),
      (else_try),
        (le, ":minimum_power", 125),
        (assign, ":division_constant", 4),
      (else_try),
        (le, ":minimum_power", 200),
        (assign, ":division_constant", 5),
      (else_try),
        (le, ":minimum_power", 400),
        (assign, ":division_constant", 6),
      (else_try),
        (le, ":minimum_power", 800),
        (assign, ":division_constant", 7),
      (else_try),
        (le, ":minimum_power", 1600),
        (assign, ":division_constant", 8),
      (else_try),
        (le, ":minimum_power", 3200),
        (assign, ":division_constant", 9),
      (else_try),
        (le, ":minimum_power", 6400),
        (assign, ":division_constant", 10),
      (else_try),
        (le, ":minimum_power", 12800),
        (assign, ":division_constant", 11),
      (else_try),
        (le, ":minimum_power", 25600),
        (assign, ":division_constant", 12),
      (else_try),
        (le, ":minimum_power", 51200),
        (assign, ":division_constant", 13),
      (else_try),
        (le, ":minimum_power", 102400),
        (assign, ":division_constant", 14),
      (else_try),
        (assign, ":division_constant", 15),
      (try_end),

      (val_div, ":player_party_strength", ":division_constant"), #1.126, ":division_constant" was 5 before
      (val_max, ":player_party_strength", 1), #1.126
      (val_div, ":enemy_party_strength", ":division_constant"), #1.126, ":division_constant" was 5 before
      (val_max, ":enemy_party_strength", 1), #1.126
      (val_div, ":total_player_and_followers_strength", ":division_constant"), #1.126, ":division_constant" was 5 before
      (val_max, ":total_player_and_followers_strength", 1), #1.126

      (store_mul, "$g_strength_contribution_of_player", ":player_party_strength", 100),
      (val_div, "$g_strength_contribution_of_player", ":total_player_and_followers_strength"),

      (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength", "p_temp_casualties"),
      (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
      (str_store_string_reg, s8, s0),

      (try_begin),
        (ge, "$g_ally_party", 0),
        (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
        (str_store_string_reg, s8, s0),
      (try_end),

      (inflict_casualties_to_party_group, "$g_encountered_party", ":total_player_and_followers_strength", "p_temp_casualties"),

      #ozan begin
      (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties"),
      (try_for_range, ":stack_no", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties", ":stack_no"),
        (try_begin),
          (party_stack_get_size, ":stack_size", "p_temp_casualties", ":stack_no"),
          (gt, ":stack_size", 0),
          (party_add_members, "p_total_enemy_casualties", ":stack_troop", ":stack_size"), #addition_to_p_total_enemy_casualties
          (party_stack_get_num_wounded, ":stack_wounded_size", "p_temp_casualties", ":stack_no"),
          (gt, ":stack_wounded_size", 0),
          (party_wound_members, "p_total_enemy_casualties", ":stack_troop", ":stack_wounded_size"),
        (try_end),
      (try_end),
      #ozan end

      (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
      (str_store_string_reg, s9, s0),

      (party_collect_attachments_to_party, "$g_encountered_party", "p_collective_enemy"),
      (assign, "$no_soldiers_left", 0),
      (try_begin),
        (call_script, "script_party_count_members_with_full_health", "p_main_party"),
        (assign, ":num_our_regulars_remaining", reg0),
        (store_add, ":num_routed_us_plus_one", "$num_routed_us", 1),
        (le, ":num_our_regulars_remaining", ":num_routed_us_plus_one"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
        (assign, "$no_soldiers_left", 1),
        (str_store_string, s4, "str_order_attack_failure"),
      (else_try),
        (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
        (assign, ":num_enemy_regulars_remaining", reg0),
        (this_or_next|le, ":num_enemy_regulars_remaining", 0),
        (le, ":num_enemy_regulars_remaining", "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
        (assign, ":continue", 0),
        (party_get_num_companion_stacks, ":party_num_stacks", "p_collective_enemy"),
        (try_begin),
          (eq, ":party_num_stacks", 0),
          (assign, ":continue", 1),
        (else_try),
          (party_stack_get_troop_id, ":party_leader", "p_collective_enemy", 0),
          (try_begin),
            (neg|troop_is_hero, ":party_leader"),
            (assign, ":continue", 1),
          (else_try),
            (troop_is_wounded, ":party_leader"),
            (assign, ":continue", 1),
          (try_end),
        (try_end),
        (eq, ":continue", 1),
        (assign, "$g_battle_result", 1),
        (assign, "$no_soldiers_left", 1),
        (str_store_string, s4, "str_order_attack_success"),
      (else_try),
      (str_store_string, s4, "str_order_attack_continue"),
    (try_end),
    ],
    [
      ("order_attack_continue",[(eq, "$no_soldiers_left", 0)],"Order your soldiers to continue the attack.",[
          (jump_to_menu,"mnu_order_attack_2"),
          ]),
      ("order_retreat",[(eq, "$no_soldiers_left", 0)],"Call your soldiers back.",[
          (jump_to_menu,"mnu_simple_encounter"),
          ]),
      ("continue",[(eq, "$no_soldiers_left", 1)],"Continue...",[
          (jump_to_menu,"mnu_simple_encounter"),
          ]),
    ]
  ),

  (
    "battle_debrief",mnf_scale_picture|mnf_disable_all_keys,
    "{s11}^^Your Casualties:{s8}{s10}^^Enemy Casualties:{s9}",
    "none",
    [
     (try_begin),
       (eq, "$g_battle_result", 1),
       (call_script, "script_change_troop_renown", "trp_player", "$battle_renown_value"),
       #SB : also distribute amount to companions, maybe pretender/spouse in party as well
       (assign, ":amount", 0),
       (try_for_range, ":companions", companions_begin, companions_end),
         (main_party_has_troop, ":companions"),
         (val_add, ":amount", 1),
       (try_end),
       (try_begin),
         (gt, ":amount", 0),
         (store_div, ":amount", "$battle_renown_value", ":amount"),
         (val_max, ":amount", dplmc_companion_battle_renown),
         (try_for_range, ":companions", companions_begin, companions_end),
           (main_party_has_troop, ":companions"),
           # (neg|troop_is_wounded, ":companions"), #survived, or stayed at the back
           (call_script, "script_change_troop_renown", ":companions", ":amount"),
         (try_end),
       (try_end),

       (try_begin),
         (ge, "$g_encountered_party", 0),
         (party_is_active, "$g_encountered_party"),
         (party_get_template_id, ":encountered_party_template", "$g_encountered_party"),
         (eq, ":encountered_party_template", "pt_kingdom_caravan_party"),

         (get_achievement_stat, ":number_of_village_raids", ACHIEVEMENT_THE_BANDIT, 0),
         (get_achievement_stat, ":number_of_caravan_raids", ACHIEVEMENT_THE_BANDIT, 1),
         (val_add, ":number_of_caravan_raids", 1),
         (set_achievement_stat, ACHIEVEMENT_THE_BANDIT, 1, ":number_of_caravan_raids"),

         (try_begin),
           (ge, ":number_of_village_raids", 3),
           (ge, ":number_of_caravan_raids", 3),
           (unlock_achievement, ACHIEVEMENT_THE_BANDIT),
         (try_end),
       (try_end),

       (try_begin),
         (party_get_current_terrain, ":cur_terrain", "p_main_party"),
         (eq, ":cur_terrain", rt_snow),
         (get_achievement_stat, ":number_of_victories_at_snowy_lands", ACHIEVEMENT_BEST_SERVED_COLD, 0),
         (val_add, ":number_of_victories_at_snowy_lands", 1),
         (set_achievement_stat, ACHIEVEMENT_BEST_SERVED_COLD, 0, ":number_of_victories_at_snowy_lands"),

         (try_begin),
           (eq, ":number_of_victories_at_snowy_lands", 10),
           (unlock_achievement, ACHIEVEMENT_BEST_SERVED_COLD),
         (try_end),
       (try_end),

       (try_begin),
         (ge, "$g_enemy_party", 0),
         (party_is_active, "$g_enemy_party"),
         (party_stack_get_troop_id, ":stack_troop", "$g_enemy_party", 0),
         (eq, ":stack_troop", "trp_mountain_bandit"),

         (get_achievement_stat, ":number_of_victories_aganist_mountain_bandits", ACHIEVEMENT_MOUNTAIN_BLADE, 0),
         (val_add, ":number_of_victories_aganist_mountain_bandits", 1),
         (set_achievement_stat, ACHIEVEMENT_MOUNTAIN_BLADE, 0, ":number_of_victories_aganist_mountain_bandits"),

         (try_begin),
           (eq, ":number_of_victories_aganist_mountain_bandits", 10),
           (unlock_achievement, ACHIEVEMENT_MOUNTAIN_BLADE),
         (try_end),
       (try_end),

       (try_begin),
         (is_between, "$g_ally_party", walled_centers_begin, walled_centers_end),
         (unlock_achievement, ACHIEVEMENT_NONE_SHALL_PASS),
       (try_end),

       (try_begin),
         (eq, "$g_joined_battle_to_help", 1),
         (unlock_achievement, ACHIEVEMENT_GOOD_SAMARITAN),
       (try_end),
     (try_end),

     (assign, "$g_joined_battle_to_help", 0),
     (call_script, "script_count_casualties_and_adjust_morale"),#new
     (call_script, "script_encounter_calculate_fit"),

     (call_script, "script_party_count_fit_regulars", "p_main_party"),
     (assign, "$playerparty_postbattle_regulars", reg0),

     (try_begin),
       (eq, "$g_battle_result", 1),
       (eq, "$g_enemy_fit_for_battle", 0),
       (str_store_string, s11, "@You were victorious!"),
#       (play_track, "track_bogus"), #clear current track.
#       (call_script, "script_music_set_situation_with_culture", mtf_sit_victorious),
       (try_begin),
         (gt, "$g_friend_fit_for_battle", 1),
         (set_background_mesh, "mesh_pic_victory"),
       (try_end),
     (else_try),
       (eq, "$g_battle_result", -1),
       (ge, "$g_enemy_fit_for_battle",1),
       (this_or_next|le, "$g_friend_fit_for_battle",0),
       (le, "$playerparty_postbattle_regulars", 0),
       (str_store_string, s11, "@The battle was lost. Your forces were utterly crushed."), #SB : "The battle"
       (set_background_mesh, "mesh_pic_defeat"),
     (else_try),
       (eq, "$g_battle_result", -1),
       (str_store_string, s11, "@Your companions carry you away from the fighting."),
		 ##diplomacy start+ Test gender with script
       #(troop_get_type, ":is_female", "trp_player"),#<- replaced
       (try_begin),
         #(eq, ":is_female", 1),#<- replaced
         (eq, tf_female, "$character_gender"),#<- added
         (set_background_mesh, "mesh_pic_wounded_fem"),
       (else_try),
         (set_background_mesh, "mesh_pic_wounded"),
       (try_end),
		 ##diplomacy end+
     (else_try),
       (eq, "$g_battle_result", 1),
       (str_store_string, s11, "@You have defeated the enemy."),
       (try_begin),
         (gt, "$g_friend_fit_for_battle", 1),
         (set_background_mesh, "mesh_pic_victory"),
       (try_end),
     (else_try),
       (eq, "$g_battle_result", 0),
       (str_store_string, s11, "@You have retreated from the fight."),
     (try_end),
#NPC companion changes begin
##check for excessive casualties, more forgiving if battle result is good
     (try_begin),
        (gt, "$playerparty_prebattle_regulars", 9),
        (store_add, ":divisor", 3, "$g_battle_result"),
        (store_div, ":half_of_prebattle_regulars", "$playerparty_prebattle_regulars", ":divisor"),
        (lt, "$playerparty_postbattle_regulars", ":half_of_prebattle_regulars"),
        (call_script, "script_objectionable_action", tmt_egalitarian, "str_excessive_casualties"),
     (try_end),
#NPC companion changes end

     (call_script, "script_print_casualties_to_s0", "p_player_casualties", 0),
     (str_store_string_reg, s8, s0),
     (call_script, "script_print_casualties_to_s0", "p_enemy_casualties", 0),
     (str_store_string_reg, s9, s0),
     (str_clear, s10),
     (try_begin),
       (eq, "$any_allies_at_the_last_battle", 1),
       (call_script, "script_print_casualties_to_s0", "p_ally_casualties", 0),
       (str_store_string, s10, "@^^Ally Casualties:{s0}"),
     (try_end),
     ],
    [
      ("continue",[],"Continue...",[(jump_to_menu, "$g_next_menu"),]),
    ]
  ),



  (
    "total_victory", 0,
    "You shouldn't be reading this... {s9}",
    "none",
    [
        # We exploit the menu condition system below.
        # The conditions should make sure that always another screen or menu is called.
        (assign, ":break", 0),
        (try_begin),
          (eq, "$routed_party_added", 0), #new
          (assign, "$routed_party_added", 1),

           #add new party to map (routed_warriors)
          (call_script, "script_add_routed_party"),
        (try_end),

		(try_begin),
			(check_quest_active, "qst_track_down_bandits"),
			(neg|check_quest_succeeded, "qst_track_down_bandits"),
			(neg|check_quest_failed, "qst_track_down_bandits"),

			(quest_get_slot, ":quest_party", "qst_track_down_bandits", slot_quest_target_party),
			(party_is_active, ":quest_party"),
			(party_get_attached_to, ":quest_party_attached"),
			(this_or_next|eq, ":quest_party", "$g_enemy_party"),
				(eq, ":quest_party_attached", "$g_enemy_party"),
			(call_script, "script_succeed_quest", "qst_track_down_bandits"),
		(try_end),

		(try_begin),
			(gt, "$g_private_battle_with_troop", 0),
			(troop_slot_eq, "$g_private_battle_with_troop", slot_troop_leaded_party, "$g_encountered_party"),
			(assign, "$g_private_battle_with_troop", 0),
			##diplomacy start+
			#g_disable_condescending_comments is also used to track the "enhanced/diminished prejudice" setting
			(try_begin),
				(eq, "$g_disable_condescending_comments", 0),
				(assign, "$g_disable_condescending_comments", 1),
			(else_try),
				(eq, "$g_disable_condescending_comments", 2),
				(assign, "$g_disable_condescending_comments", 3),
			##diplomacy end+
			(try_end),
		(try_end),

        #new - begin
        (party_get_num_companion_stacks, ":num_stacks", "p_collective_enemy"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", "p_collective_enemy", ":i_stack"),
          (is_between, ":stack_troop", lords_begin, lords_end),
          (troop_is_wounded, ":stack_troop"),
          (party_add_members, "p_total_enemy_casualties", ":stack_troop", 1),
        (try_end),
        #new - end

        (try_begin),
          # Talk to ally leader
          (eq, "$thanked_by_ally_leader", 0),
          (assign, "$thanked_by_ally_leader", 1),

          (gt, "$g_ally_party", 0),
          #(store_add, ":total_str_without_player", "$g_starting_strength_ally_party", "$g_starting_strength_enemy_party"),

          (store_add, ":total_str_without_player", "$g_starting_strength_friends", "$g_starting_strength_enemy_party"),
          (val_sub, ":total_str_without_player", "$g_starting_strength_main_party"),

          (store_sub, ":ally_strength_without_player", "$g_starting_strength_friends", "$g_starting_strength_main_party"),

          (store_mul, ":ally_advantage", ":ally_strength_without_player", 100),
          (val_add, ":total_str_without_player", 1),
          (val_div, ":ally_advantage", ":total_str_without_player"),
          #Ally advantage=50  means battle was evenly matched

          (store_sub, ":enemy_advantage", 100, ":ally_advantage"),

          (store_mul, ":faction_reln_boost", ":enemy_advantage", "$g_starting_strength_enemy_party"),
          (val_div, ":faction_reln_boost", 3000),
          (val_min, ":faction_reln_boost", 4),

          (store_mul, "$g_relation_boost", ":enemy_advantage", ":enemy_advantage"),
          (val_div, "$g_relation_boost", 700),
          (val_clamp, "$g_relation_boost", 0, 20),

          (party_get_num_companion_stacks, ":num_ally_stacks", "$g_ally_party"),
          (gt, ":num_ally_stacks", 0),
          (store_faction_of_party, ":ally_faction","$g_ally_party"),
          (call_script, "script_change_player_relation_with_faction", ":ally_faction", ":faction_reln_boost"),
          (party_stack_get_troop_id, ":ally_leader", "$g_ally_party"),
          (party_stack_get_troop_dna, ":ally_leader_dna", "$g_ally_party", 0),
          (try_begin),
            (troop_is_hero, ":ally_leader"),
            (troop_get_slot, ":hero_relation", ":ally_leader", slot_troop_player_relation),
            (assign, ":rel_boost", "$g_relation_boost"),
            (try_begin),
              (lt, ":hero_relation", -5),
              (val_div, ":rel_boost", 3),
            (try_end),
            (call_script,"script_change_player_relation_with_troop", ":ally_leader", ":rel_boost"),
          (try_end),
          (assign, "$talk_context", tc_ally_thanks),
          (call_script, "script_setup_troop_meeting", ":ally_leader", ":ally_leader_dna"),
        (else_try),
          # Talk to enemy leaders
          (assign, ":break", 0),

          (party_get_num_companion_stacks, ":num_stacks", "p_total_enemy_casualties"), #p_encountered changed to total_enemy_casualties
          (try_for_range, ":stack_no", "$last_defeated_hero", ":num_stacks"), #May 31 bug note -- this now returns some heroes in victorious party as well as in the other party
            (eq, ":break", 0),
            (party_stack_get_troop_id, ":stack_troop", "p_total_enemy_casualties", ":stack_no"),
            (party_stack_get_troop_dna, ":stack_troop_dna", "p_total_enemy_casualties", ":stack_no"),

            (troop_is_hero, ":stack_troop"),

            (store_troop_faction, ":defeated_faction", ":stack_troop"),
            #steve post 0912 changes begin - removed, this is duplicated elsewhere in game menus
            #(call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":stack_troop", ":defeated_faction"),
            (try_begin),
   			  (store_relation, ":relation", ":defeated_faction", "fac_player_faction"),
			  (ge, ":relation", 0),
			  (str_store_troop_name, s4, ":stack_troop"),

			  (try_begin),
				(eq, "$cheat_mode", 1),
				(display_message, "@{!}{s4} skipped in p_total_enemy_casualties capture queue because is friendly"),
			  (try_end),
			(else_try),
              (try_begin),
                (party_stack_get_troop_id, ":party_leader", "$g_encountered_party", 0),
                (is_between, ":party_leader", active_npcs_begin, active_npcs_end),
                (troop_slot_eq, ":party_leader", slot_troop_occupation, slto_kingdom_hero),
                (store_sub, ":kingdom_hero_id", ":party_leader", active_npcs_begin),
                (get_achievement_stat, ":was_he_defeated_player_before", ACHIEVEMENT_BARON_GOT_BACK, ":kingdom_hero_id"),
                (eq, ":was_he_defeated_player_before", 1),

                (unlock_achievement, ACHIEVEMENT_BARON_GOT_BACK),
              (try_end),

              (store_add, "$last_defeated_hero", ":stack_no", 1),
              (call_script, "script_remove_troop_from_prison", ":stack_troop"),
              (troop_set_slot, ":stack_troop", slot_troop_leaded_party, -1),

              (call_script, "script_cf_check_hero_can_escape_from_player", ":stack_troop"),

              (str_store_troop_name, s1, ":stack_troop"),
              (str_store_faction_name, s3, ":defeated_faction"),
              (str_store_string, s17, "@{s1} of {s3} managed to escape."),
              (display_log_message, "@{!}{s17}"),
              (jump_to_menu, "mnu_enemy_slipped_away"),
              (assign, ":break", 1),
			(else_try),
              (store_add, "$last_defeated_hero", ":stack_no", 1),
              (call_script, "script_remove_troop_from_prison", ":stack_troop"),
              (troop_set_slot, ":stack_troop", slot_troop_leaded_party, -1),

              (assign, "$talk_context", tc_hero_defeated),

              (call_script, "script_setup_troop_meeting", ":stack_troop", ":stack_troop_dna"),
              (assign, ":break", 1),
            (try_end),
          (try_end),

          (eq, ":break", 1),
        (else_try),
          # Talk to freed heroes
          (assign, ":break", 0),
          (party_get_num_prisoner_stacks, ":num_prisoner_stacks", "p_collective_enemy"),
          (try_for_range, ":stack_no", "$last_freed_hero", ":num_prisoner_stacks"),
            (eq, ":break", 0),
            (party_prisoner_stack_get_troop_id, ":stack_troop", "p_collective_enemy", ":stack_no"),
            (troop_is_hero, ":stack_troop"),
            (party_prisoner_stack_get_troop_dna, ":stack_troop_dna", "p_collective_enemy", ":stack_no"),
            (store_add, "$last_freed_hero", ":stack_no", 1),
            (assign, "$talk_context", tc_hero_freed),
            (call_script, "script_setup_troop_meeting", ":stack_troop", ":stack_troop_dna"),
            (assign, ":break", 1),
          (try_end),
          (eq, ":break", 1),
        (else_try),
          (eq, "$capture_screen_shown", 0),
          (assign, "$capture_screen_shown", 1),
          (party_clear, "p_temp_party"),
          (assign, "$g_move_heroes", 0),
          #(call_script, "script_party_prisoners_add_party_companions", "p_temp_party", "p_collective_enemy"),

          #p_total_enemy_casualties deki yarali askerler p_temp_party'e prisoner olarak eklenecek.
          (call_script, "script_party_add_wounded_members_as_prisoners", "p_temp_party", "p_total_enemy_casualties"),

          (call_script, "script_party_add_party_prisoners", "p_temp_party", "p_collective_enemy"),
          (try_begin),
            (call_script, "script_party_calculate_strength", "p_collective_friends_backup",0),
            (assign,":total_initial_strength", reg(0)),
            (gt, ":total_initial_strength", 0),
            #(gt, "$g_ally_party", 0),
            (call_script, "script_party_calculate_strength", "p_main_party_backup",0),
            (assign,":player_party_initial_strength", reg(0)),
            # move ally_party_initial_strength/(player_party_initial_strength + ally_party_initial_strength) prisoners to ally party.
            # First we collect the share of prisoners of the ally party and distribute those among the allies.
            (store_sub, ":ally_party_initial_strength", ":total_initial_strength", ":player_party_initial_strength"),

            #(call_script, "script_party_calculate_strength", "p_ally_party_backup"),
            #(assign,":ally_party_initial_strength", reg(0)),
            #(store_add, ":total_initial_strength", ":player_party_initial_strength", ":ally_party_initial_strength"),
            (store_mul, ":ally_share", ":ally_party_initial_strength", 1000),
            (val_div, ":ally_share", ":total_initial_strength"),
            (assign, "$pin_number", ":ally_share"), #we send this as a parameter to the script.
            (party_clear, "p_temp_party_2"),
            (call_script, "script_move_members_with_ratio", "p_temp_party", "p_temp_party_2"),

            #TODO: This doesn't handle prisoners if our allies joined battle after us.
            (try_begin),
              (gt, "$g_ally_party", 0),
              (distribute_party_among_party_group, "p_temp_party_2", "$g_ally_party"),
            (try_end),
            #next if there's anything left, we'll open up the party exchange screen and offer them to the player.
          (try_end),
          (party_get_num_companions, ":num_rescued_prisoners", "p_temp_party"),
          (party_get_num_prisoners,  ":num_captured_enemies", "p_temp_party"),

          (store_add, ":total_capture_size", ":num_rescued_prisoners", ":num_captured_enemies"),

          (gt, ":total_capture_size", 0),
          (change_screen_exchange_with_party, "p_temp_party"),
        (else_try),
          (eq, "$loot_screen_shown", 0),
          (assign, "$loot_screen_shown", 1),
#          (try_begin),
#            (gt, "$g_ally_party", 0),
#            (call_script, "script_party_add_party", "$g_ally_party", "p_temp_party"), #Add remaining prisoners to ally TODO: FIX it.
#          (else_try),
#            (party_get_num_attached_parties, ":num_quick_attachments", "p_main_party"),
#            (gt, ":num_quick_attachments", 0),
#            (party_get_attached_party_with_rank, ":helper_party", "p_main_party", 0),
#            (call_script, "script_party_add_party", ":helper_party", "p_temp_party"), #Add remaining prisoners to our reinforcements
#          (try_end),
          (troop_clear_inventory, "trp_temp_troop"),
          (call_script, "script_party_calculate_loot", "p_total_enemy_casualties"), #p_encountered_party_backup changed to total_enemy_casualties
          (gt, reg0, 0),
          (troop_sort_inventory, "trp_temp_troop"),
		  ##diplomacy start+
		  #Here: we jump to rubik's autoloot from CC if applicable instead of using the standard loot screen
		  (try_begin),
			(call_script, "script_cf_dplmc_player_party_meets_autoloot_conditions"),
			(assign, "$dplmc_return_menu", "mnu_total_victory"),
			(assign, "$lord_selected", "trp_player"),
			(jump_to_menu, "mnu_dplmc_manage_loot_pool"),
		  (else_try),
			#Old behavior:
			(change_screen_loot, "trp_temp_troop"),
		  (try_end),
		  ##diplomacy end+
        (else_try),
          #finished all
          (try_begin),
            (le, "$g_ally_party", 0),
            (end_current_battle),
          (try_end),
          (call_script, "script_party_give_xp_and_gold", "p_total_enemy_casualties"), #p_encountered_party_backup changed to total_enemy_casualties
          (try_begin),
            (eq, "$g_enemy_party", 0),
            (display_message,"str_error_string"),
          (try_end),

		  (try_begin),
		    (party_is_active, "$g_ally_party"),
			(call_script, "script_battle_political_consequences", "$g_enemy_party", "$g_ally_party"),
		  (else_try),
			(call_script, "script_battle_political_consequences", "$g_enemy_party", "p_main_party"),
		  (try_end),

          (call_script, "script_event_player_defeated_enemy_party", "$g_enemy_party"),
          (call_script, "script_clear_party_group", "$g_enemy_party"),
          (try_begin),
            (eq, "$g_next_menu", -1),

            #NPC companion changes begin
            (call_script, "script_post_battle_personality_clash_check"),
            #NPC companion changes end

            #Post 0907 changes begin
            (party_stack_get_troop_id, ":enemy_leader", "p_encountered_party_backup",0),
            (try_begin),
              (is_between, ":enemy_leader", active_npcs_begin, active_npcs_end),
              (neg|is_between, "$g_encountered_party", centers_begin, centers_end),
              (store_troop_faction, ":enemy_leader_faction", ":enemy_leader"),

              (try_begin),
                (eq, "$g_ally_party", 0),
                (call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":enemy_leader", ":enemy_leader_faction"),
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (display_message, "@{!}Victory comment. Player was alone"),
                (try_end),
              (else_try),
                (ge, "$g_strength_contribution_of_player", 40),
                (call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":enemy_leader", ":enemy_leader_faction"),
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (display_message, "@{!}Ordinary victory comment. The player provided at least 40 percent forces."),
                (try_end),
              (else_try),
                (gt, "$g_starting_strength_enemy_party", 1000),
                (call_script, "script_get_closest_center", "p_main_party"),
                (assign, ":battle_of_where", reg0),
                (call_script, "script_add_log_entry", logent_player_participated_in_major_battle, "trp_player",  ":battle_of_where", -1, ":enemy_leader_faction"),
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (display_message, "@{!}Player participation comment. The enemy had at least 1k starting strength."),
                (try_end),
              (else_try),
                (eq, "$cheat_mode", 1),
                (display_message, "@{!}No victory comment. The battle was small, and the player provided less than 40 percent of allied strength"),
              (try_end),
            (try_end),
            #Post 0907 changes end
            (val_add, "$g_total_victories", 1),
            (leave_encounter),
            (change_screen_return),
          (else_try),
            (try_begin), #my kingdom
            ##diplomacy begin
              (eq, "$g_next_menu", "mnu_dplmc_town_riot_removed"),
              (jump_to_menu, "$g_next_menu"),
            (else_try),
            ##diplomacy end
              #(change_screen_return),
              (eq, "$g_next_menu", "mnu_castle_taken"),

              (call_script, "script_add_log_entry", logent_castle_captured_by_player, "trp_player", "$g_encountered_party", -1, "$g_encountered_party_faction"),
              (store_current_hours, ":hours"),
			  (faction_set_slot, "$players_kingdom", slot_faction_ai_last_decisive_event, ":hours"),

              (try_begin), #player took a walled center while he is a vassal of npc kingdom.
  			  ##diplomacy start+ Handle player is co-ruler of NPC faction
				(assign, ":is_coruler", 0),
                (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
                (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
                (ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
				(assign, ":is_coruler", 1),

				(assign, "$g_center_taken_by_player_faction", "$g_encountered_party"),
				(faction_get_slot, ":faction_leader", "fac_player_supporters_faction", slot_faction_leader),
				(try_begin),
					(eq, ":faction_leader", "trp_player"),
					(assign, ":faction_leader", heroes_end),
					(try_for_range, ":troop_no", heroes_begin, ":faction_leader"),
						(this_or_next|troop_slot_eq, slot_troop_spouse, "trp_player"),
							(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_no"),
						(neg|troop_slot_ge, ":faction_leader", slot_troop_prisoner_of_party, 0),#Not a prisoner
						(neg|troop_slot_ge, ":faction_leader", slot_troop_occupation, slto_retirement),#Not retired, exiled, dead
						(assign, ":faction_leader", ":troop_no"),#assign and break the loop
					(try_end),
				(try_end),

				(is_between, ":faction_leader", heroes_begin, heroes_end),#Not the player, and not a bogus value
				(neg|troop_slot_ge, ":faction_leader", slot_troop_prisoner_of_party, 0),#Not a prisoner
				(neg|troop_slot_ge, ":faction_leader", slot_troop_occupation, slto_retirement),#Not retired, exiled, dead

				(change_screen_return),
				(start_map_conversation, ":faction_leader", -1),
			  (else_try),
			  #player took a walled center while he is a vassal of npc kingdom.
			    (neq, ":is_coruler", 1),
			  ##diplomacy end+
                (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
                (jump_to_menu, "$g_next_menu"),
              (else_try), #player took a walled center while he is a vassal of rebels.
                (eq, "$players_kingdom", "fac_player_supporters_faction"),
                (assign, "$g_center_taken_by_player_faction", "$g_encountered_party"),
                (neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
                (faction_get_slot, ":faction_leader", "fac_player_supporters_faction", slot_faction_leader),
                (change_screen_return),
                # (start_map_conversation, ":faction_leader", -1), #SB : script call
                (assign, "$talk_context", tc_give_center_to_fief),
                (call_script, "script_start_court_conversation", ":faction_leader", "$current_town"),
              (else_try), #player took a walled center for player's kingdom
			    ##diplomacy start+ Handle player is co-ruler of faction
				(this_or_next|eq, ":is_coruler", 1),
				##diplomacy end+
                (neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
                (assign, "$g_center_taken_by_player_faction", "$g_encountered_party"),
                (assign, "$talk_context", tc_give_center_to_fief),
                (change_screen_return),

                (assign, ":best_troop", "trp_hired_blade"),
				##diplomacy start+
				#Trivial aesthetic change, change the default troop to be appropriate to the
				#culture of the player kingdom (instead of defaulting always to a Swadian troop).
				(assign, ":players_culture", "$players_kingdom"),
				(try_begin),
					#If not the co-ruler of an NPC kingdom, use the player faction culture.
				   (neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
				   # (assign, ":best_troop", "trp_mercenary_crossbowman"),#<- while we're at it, use a mercenary default #SB : hired blade
				   (assign, ":players_culture", "$g_player_culture"),
				   (this_or_next|is_between, ":players_culture", npc_kingdoms_begin, npc_kingdoms_end),
					(is_between, ":players_culture", cultures_begin, cultures_end),
				(else_try),
					#If not the co-ruler of an NPC kingdom, and there wasn't a valid player faction
					#culture, try to use the faction of the player's court.
					(neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
					(is_between, "$g_player_court", centers_begin, centers_end),
					(party_slot_ge, "$g_player_court", slot_center_original_faction, 1),
					(party_get_slot, ":players_culture", "$g_player_court", slot_center_original_faction),
				(try_end),
				(try_begin),
					#Resolve from kingdom to culture if necessary
				   (is_between, ":players_culture", kingdoms_begin, kingdoms_end),
				   (faction_get_slot, ":players_culture", ":players_culture", slot_faction_culture),
				(try_end),
				(try_begin),
					#If the final result is a culture, get the best troop if valid
				   (is_between, ":players_culture", cultures_begin, cultures_end),
				   # (neq, ":players_culture", "fac_culture_1"), #SB : allow swadian culture
				   (faction_get_slot, reg0, ":players_culture", slot_faction_guard_troop),
				   (ge, reg0, soldiers_begin),
				   (assign, ":best_troop", reg0),
				(try_end),
				##diplomacy end+
                #SB : fix this, otherwise previously calculated troop is useless
                (try_begin),
                  (neq, ":best_troop", "trp_hired_blade"),
                  (store_character_level, ":maximum_troop_score", ":best_troop"),
                (else_try),
                  (assign, ":maximum_troop_score", 0),
                (try_end),

                (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
                (try_for_range, ":stack_no", 0, ":num_stacks"),
                  (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
                  (neq, ":stack_troop", "trp_player"),

                  (party_stack_get_size, ":stack_size", "p_main_party", ":stack_no"),
                  (party_stack_get_num_wounded, ":num_wounded", "p_main_party", ":stack_no"),
                  (troop_get_slot, ":num_routed", "p_main_party", slot_troop_player_routed_agents),

                  (assign, ":continue", 0),
                  (try_begin),
                    (neg|troop_is_hero, ":stack_troop"),
                    (store_add, ":agents_which_cannot_speak", ":num_wounded", ":num_routed"),
                    (gt, ":stack_size", ":agents_which_cannot_speak"),
                    (assign, ":continue", 1),
                  (else_try),
                    (troop_is_hero, ":stack_troop"),
                    (neg|troop_is_wounded, ":stack_troop"),
                    (assign, ":continue", 1),
                  (try_end),
                  (eq, ":continue", 1),

                  (try_begin),
                    (troop_is_hero, ":stack_troop"),
                    (troop_get_slot, ":troop_renown", ":stack_troop", slot_troop_renown),
                    (store_mul, ":troop_score", ":troop_renown", 100),
                    (val_add, ":troop_score", 1000),
                  (else_try),
                    (store_character_level, ":troop_level", ":stack_troop"),
                    (assign, ":troop_score", ":troop_level"),
                  (try_end),

                  (try_begin),
                    (gt, ":troop_score", ":maximum_troop_score"),
                    (assign, ":maximum_troop_score", ":troop_score"),
                    (assign, ":best_troop", ":stack_troop"),
                    (party_stack_get_troop_dna, ":best_troop_dna", "p_main_party", ":stack_no"),
                  (try_end),
                (try_end),
                (call_script, "script_start_court_conversation", ":best_troop", "$current_town", ":best_troop_dna"),
                # (start_map_conversation, ":best_troop", ":best_troop_dna"),
              (try_end),
            (try_end),
          (try_end),
        (try_end),
      ],
    [
      ("continue",[],"Continue...",[]),
        ]
  ),

  (
    "enemy_slipped_away",0,
    "{s17}",
    "none",
    [],
    [
      ("continue",[],"Continue...",[(jump_to_menu,"mnu_total_victory")]),
    ]
  ),

  (
    "total_defeat",0,
    "{!}You shouldn't be reading this...",
    "none",
    [
        (play_track, "track_captured", 1),
           # Free prisoners
          (party_get_num_prisoner_stacks, ":num_prisoner_stacks","p_main_party"),
          (try_for_range, ":stack_no", 0, ":num_prisoner_stacks"),
            (party_prisoner_stack_get_troop_id, ":stack_troop","p_main_party",":stack_no"),
            (troop_is_hero, ":stack_troop"),
            (call_script, "script_remove_troop_from_prison", ":stack_troop"),
          (try_end),

		  (try_begin),
		    (party_is_active, "$g_ally_party"),
			(call_script, "script_battle_political_consequences", "$g_ally_party", "$g_enemy_party"),
		  (else_try),
			(call_script, "script_battle_political_consequences", "p_main_party", "$g_enemy_party"),
		  (try_end),

          (call_script, "script_loot_player_items", "$g_enemy_party"),

          (assign, "$g_move_heroes", 0),
          (party_clear, "p_temp_party"),
          (call_script, "script_party_add_party_prisoners", "p_temp_party", "p_main_party"),
          (call_script, "script_party_prisoners_add_party_companions", "p_temp_party", "p_main_party"),
          (distribute_party_among_party_group, "p_temp_party", "$g_enemy_party"),

          (assign, "$g_prison_heroes", 1),
          (call_script, "script_party_remove_all_companions", "p_main_party"),
          (assign, "$g_prison_heroes", 0),
          (assign, "$g_move_heroes", 1),
          (call_script, "script_party_remove_all_prisoners", "p_main_party"),

          (val_add, "$g_total_defeats", 1),

          (try_begin),
            (neq, "$g_player_surrenders", 1),
            (store_random_in_range, ":random_no", 0, 100),
            (ge, ":random_no", "$g_player_luck"),
            (jump_to_menu, "mnu_permanent_damage"),
          (else_try),
            (try_begin),
              (eq, "$g_next_menu", -1),
              (leave_encounter),
              (change_screen_return),
            (else_try),
              (jump_to_menu, "$g_next_menu"),
            (try_end),
          (try_end),
          (try_begin),
            (gt, "$g_ally_party", 0),
            (call_script, "script_party_wound_all_members", "$g_ally_party"),
          (try_end),

#Troop commentary changes begin
          (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
          (try_for_range, ":stack_no", 0, ":num_stacks"),
            (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
            (is_between, ":stack_troop", active_npcs_begin, active_npcs_end),
			(troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
            (store_troop_faction, ":victorious_faction", ":stack_troop"),
            (call_script, "script_add_log_entry", logent_player_defeated_by_lord, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
          (try_end),
#Troop commentary changes end

      ],
    []
  ),

  (
    "permanent_damage",mnf_disable_all_keys,
    "{s0}",
    "none",
    [
      (assign, ":end_cond", 1),
      (try_for_range, ":unused", 0, ":end_cond"),
        (store_random_in_range, ":random_attribute", 0, 4),
        (store_attribute_level, ":attr_level", "trp_player", ":random_attribute"),
        (try_begin),
          (gt, ":attr_level", 3),
          (neq, ":random_attribute", ca_charisma),
          (try_begin),
            (eq, ":random_attribute", ca_strength),
            (str_store_string, s0, "@Some of your tendons have been damaged in the battle. You lose 1 strength."),
          (else_try),
            (eq, ":random_attribute", ca_agility),
            (str_store_string, s0, "@You took a nasty wound which will cause you to limp slightly even after it heals. You lose 1 agility."),
##          (else_try),
##            (eq, ":random_attribute", ca_charisma),
##            (str_store_string, s0, "@After the battle you are aghast to find that one of the terrible blows you suffered has left a deep, disfiguring scar on your face, horrifying those around you. Your charisma is reduced by 1."),
          (else_try),
##            (eq, ":random_attribute", ca_intelligence),
            (str_store_string, s0, "@You have trouble thinking straight after the battle, perhaps from a particularly hard hit to your head, and frequent headaches now plague your existence. Your intelligence is reduced by 1."),
          (try_end),
        (else_try),
          (lt, ":end_cond", 200),
          (val_add, ":end_cond", 1),
        (try_end),
      (try_end),
      (try_begin),
        (eq, ":end_cond", 200),
        (try_begin),
          (eq, "$g_next_menu", -1),
          (leave_encounter),
          (change_screen_return),
        (else_try),
          (jump_to_menu, "$g_next_menu"),
        (try_end),
      (else_try),
        (troop_raise_attribute, "trp_player", ":random_attribute", -1),
      (try_end),
      ],
    [
      ("s0",
       [
         (store_random_in_range, ":random_no", 0, 4),
         (try_begin),
           (eq, ":random_no", 0),
           (str_store_string, s0, "@Perhaps I'm getting unlucky..."),
         (else_try),
           (eq, ":random_no", 1),
           (str_store_string, s0, "@Retirement is starting to sound better and better."),
         (else_try),
           (eq, ":random_no", 2),
           (str_store_string, s0, "@No matter! I will persevere!"),
         (else_try),
           (eq, ":random_no", 3),
			  ##diplomacy start+ Don't use troop_get_type for gender
			  #(troop_get_type, ":is_female", "trp_player"),#<- replaced
           (try_begin),
             #(eq, ":is_female", 1),#<- replaced
			 (eq, "$character_gender", tf_female),#<- added
             (str_store_string, s0, "@What did I do to deserve this?"),
           (else_try),
             (str_store_string, s0, "@I suppose it'll make for a good story, at least..."),
           (try_end),
			  ##diplomacy end+
         (try_end),
         ],
       "{s0}",
       [
         (try_begin),
           (eq, "$g_next_menu", -1),
           (leave_encounter),
           (change_screen_return),
         (else_try),
           (jump_to_menu, "$g_next_menu"),
         (try_end),
         ]),
      ]
  ),

  (
    "pre_join",0,
    "You come across a battle between {s2} and {s1}. You decide to...",
    "none",
    [
        (str_store_party_name, 1,"$g_encountered_party"),
        (str_store_party_name, 2,"$g_encountered_party_2"),
      ],
    [
      ("pre_join_help_attackers",[
          (store_faction_of_party, ":attacker_faction", "$g_encountered_party_2"),
          (store_relation, ":attacker_relation", ":attacker_faction", "fac_player_supporters_faction"),
          (store_faction_of_party, ":defender_faction", "$g_encountered_party"),
          (store_relation, ":defender_relation", ":defender_faction", "fac_player_supporters_faction"),
          (ge, ":attacker_relation", 0),
          (lt, ":defender_relation", 0),
          ],
          "Move in to help the {s2}.",[
              (select_enemy,0),
              (assign,"$g_enemy_party","$g_encountered_party"),
              (assign,"$g_ally_party","$g_encountered_party_2"),
              (jump_to_menu,"mnu_join_battle")]),
      ("pre_join_help_defenders",[
          (store_faction_of_party, ":attacker_faction", "$g_encountered_party_2"),
          (store_relation, ":attacker_relation", ":attacker_faction", "fac_player_supporters_faction"),
          (store_faction_of_party, ":defender_faction", "$g_encountered_party"),
          (store_relation, ":defender_relation", ":defender_faction", "fac_player_supporters_faction"),
          (ge, ":defender_relation", 0),
          (lt, ":attacker_relation", 0),
          ],
          "Rush to the aid of the {s1}.",[
              (select_enemy,1),
              (assign,"$g_enemy_party","$g_encountered_party_2"),
              (assign,"$g_ally_party","$g_encountered_party"),
              (jump_to_menu,"mnu_join_battle")]),
      ("pre_join_leave",[],"Don't get involved.",[(leave_encounter),(change_screen_return)]),
    ]
  ),

  (#SB : pic hotkeys
    "join_battle",mnf_enable_hot_keys,
    "You are helping the {s2} against the {s1}. You have {reg10} troops fit for battle against the enemy's {reg11}.",
    "none",
    [
        (str_store_party_name, 1,"$g_enemy_party"),
        (str_store_party_name, 2,"$g_ally_party"),

        (call_script, "script_encounter_calculate_fit"),

        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (call_script, "script_encounter_init_variables"),
        (else_try), #second or more turn
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (try_end),

        (try_begin),
          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
          (assign, ":num_enemy_regulars_remaining", reg0),
          (assign, ":enemy_finished",0),
          (try_begin),
            (eq, "$g_battle_result", 1),

            (this_or_next|le, ":num_enemy_regulars_remaining", 0), #battle won
            (le, ":num_enemy_regulars_remaining", "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

            (assign, ":enemy_finished",1),
          (else_try),
            (eq, "$g_engaged_enemy", 1),
            (le, "$g_enemy_fit_for_battle",0),
            (ge, "$g_friend_fit_for_battle",1),
            (assign, ":enemy_finished",1),
          (try_end),

          (this_or_next|eq, ":enemy_finished",1),
          (eq,"$g_enemy_surrenders",1),
          (assign, "$g_next_menu", -1),
          (jump_to_menu, "mnu_total_victory"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
          (assign, ":num_ally_regulars_remaining", reg0),
          (assign, ":battle_lost", 0),
          (try_begin),
            (eq, "$g_battle_result", -1),

            #(eq, ":num_ally_regulars_remaining", 0), #battle lost
            (le, ":num_ally_regulars_remaining",  "$num_routed_allies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

            (assign, ":battle_lost",1),
          (try_end),

          (this_or_next|eq, ":battle_lost",1),
          (eq,"$g_player_surrenders",1),
          (leave_encounter),
          (change_screen_return),
        (try_end),
      ],
    [
      ("join_attack",
      [
        (neg|troop_is_wounded, "trp_player"),
      ],
      "Charge the enemy.",
      [
        (assign, "$g_joined_battle_to_help", 1),
        (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
        (assign, "$g_battle_result", 0),
        
        (assign, "$player_deploy_troops", 1),
        
        (call_script, "script_calculate_renown_value"),
        (call_script, "script_calculate_battle_advantage"),
        (set_battle_advantage, reg0),
        (set_party_battle_mode),
        (set_jump_mission,"mt_lead_charge"),
        (call_script, "script_setup_random_scene"),
        (assign, "$g_next_menu", "mnu_join_battle"),
        (jump_to_menu, "mnu_battle_debrief"),
        (change_screen_mission),
      ]),

      ("join_order_attack",
      [
        (call_script, "script_party_count_members_with_full_health", "p_main_party"),
        (ge, reg0, 3),
      ],
      "Order your troops to attack with your allies while you stay back.",
      [
        (assign, "$g_joined_battle_to_help", 1),
        (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
        (jump_to_menu,"mnu_join_order_attack"),
      ]),

      ("join_leave",[],"Leave.",
      [
        (try_begin),
           (neg|troop_is_wounded, "trp_player"),
           (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
           (party_stack_get_troop_id, ":enemy_leader","$g_enemy_party",0),
		   (is_between, ":enemy_leader", active_npcs_begin, active_npcs_end),
           (call_script, "script_add_log_entry", logent_player_retreated_from_lord, "trp_player",  -1, ":enemy_leader", -1),
        (try_end),

        (leave_encounter),(change_screen_return)]),
      ]),

  (
    "join_order_attack",mnf_disable_all_keys,
    "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
    "none",
    [
      (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
      (assign, ":player_party_strength", reg0),
      (val_div, ":player_party_strength", 5),
      (call_script, "script_party_calculate_strength", "p_collective_friends", 0),
      (assign, ":friend_party_strength", reg0),
      (val_div, ":friend_party_strength", 5),

      (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
      (assign, ":enemy_party_strength", reg0),
      (val_div, ":enemy_party_strength", 5),

      (try_begin),
        (eq, ":friend_party_strength", 0),
        (store_div, ":enemy_party_strength_for_p", ":enemy_party_strength", 2),
      (else_try),
        (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
        (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
        (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),
      (try_end),

      (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),
      (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties"),
      (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
      (str_store_string_reg, s8, s0),

      (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties"),

      #ozan begin
      (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties"),
      (try_for_range, ":stack_no", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties", ":stack_no"),
        (try_begin),
          (party_stack_get_size, ":stack_size", "p_temp_casualties", ":stack_no"),
          (gt, ":stack_size", 0),
          (party_add_members, "p_total_enemy_casualties", ":stack_troop", ":stack_size"), #addition_to_p_total_enemy_casualties
          (party_stack_get_num_wounded, ":stack_wounded_size", "p_temp_casualties", ":stack_no"),
          (gt, ":stack_wounded_size", 0),
          (party_wound_members, "p_total_enemy_casualties", ":stack_troop", ":stack_wounded_size"),
        (try_end),
      (try_end),
      #ozan end

      (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
      (str_store_string_reg, s10, s0),

      (call_script, "script_collect_friendly_parties"),
      #(party_collect_attachments_to_party, "$g_ally_party", "p_collective_ally"),

      (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
      (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
      (str_store_string_reg, s9, s0),
      (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),

       #(assign, "$cant_leave_encounter", 0),
       (assign, "$no_soldiers_left", 0),
       (try_begin),
         (call_script, "script_party_count_members_with_full_health","p_main_party"),
         (assign, ":num_our_regulars_remaining", reg0),

         #(le, ":num_our_regulars_remaining", 0),
         (le, ":num_our_regulars_remaining", "$num_routed_us"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

         (assign, "$no_soldiers_left", 1),
         (str_store_string, s4, "str_join_order_attack_failure"),
       (else_try),
         (call_script, "script_party_count_members_with_full_health","p_collective_enemy"),
         (assign, ":num_enemy_regulars_remaining", reg0),

         (this_or_next|le, ":num_enemy_regulars_remaining", 0),
         (le, ":num_enemy_regulars_remaining", "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

         (assign, "$g_battle_result", 1),
         (assign, "$no_soldiers_left", 1),
         (str_store_string, s4, "str_join_order_attack_success"),
       (else_try),
         (str_store_string, s4, "str_join_order_attack_continue"),
       (try_end),
    ],
    [
      ("continue",[],"Continue...",
      [
        (jump_to_menu,"mnu_join_battle"),
      ]),
    ]
  ),


# Towns
  (
    "zendar",mnf_auto_enter,
    "You enter the town of Zendar.",
    "none",
    [(reset_price_rates,0),(set_price_rate_for_item,"itm_tools",70),(set_price_rate_for_item,"itm_salt",140)],
    [
      ("zendar_enter",[],"_",[(set_jump_mission,"mt_town_default"),(jump_to_scene,"scn_zendar_center"),(change_screen_mission)],"Door to the town center."),
      ("zendar_tavern",[],"_",[(set_jump_mission,"mt_town_default"),
                                                   (jump_to_scene,"scn_the_happy_boar"),
                                                   (change_screen_mission)],"Door to the tavern."),
      ("zendar_merchant",[],"_",[(set_jump_mission,"mt_town_default"),
                                                   (jump_to_scene,"scn_zendar_merchant"),
                                                   (change_screen_mission)],"Door to the merchant."),
      ("zendar_arena",[],"_",[(set_jump_mission,"mt_town_default"),
                                                   (jump_to_scene,"scn_zendar_arena"),
                                                   (change_screen_mission)],"Door to the arena."),
#      ("zendar_leave",[],"Leave town.",[[leave_encounter],[change_screen_return]]),
      ("town_1_leave",[],"_",[(leave_encounter),(change_screen_return)]),
    ]
  ),
  (
    "salt_mine",mnf_auto_enter,
    "You enter the salt mine.",
    "none",
    [(reset_price_rates,0),(set_price_rate_for_item,"itm_salt",55)],
    [
      ("enter",[],"Enter.",[(set_jump_mission,"mt_town_center"),(jump_to_scene,"scn_salt_mine"),(change_screen_mission)]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
  (
    "four_ways_inn",mnf_auto_enter,
    "You arrive at the Four Ways Inn.",
    "none",
    [],
    [

#      ("enter",[],"Enter.",[[set_jump_mission,"mt_town_default"],[jump_to_scene,"scn_conversation_scene"],[change_screen_mission]]),
      ("enter",[],"Enter.",[(set_jump_mission,"mt_ai_training"),(jump_to_scene,"scn_four_ways_inn"),(change_screen_mission)]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
  (
    "test_scene",0,
    "You enter the test scene.",
    "none",
    [],
    [

      ("enter",[],"Enter 1.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_multi_scene_1"],[change_screen_mission]]),
      ("enter",[],"Enter 2.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_multi_scene_2"],[change_screen_mission]]),
      ("enter",[],"Enter 3.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_multi_scene_3"],[change_screen_mission]]),
      ("enter",[],"Enter 4.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_multi_scene_4"],[change_screen_mission]]),
      ("enter",[],"Enter 5.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_multi_scene_5"],[change_screen_mission]]),
      ("enter",[],"Enter 6.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_multi_scene_6"],[change_screen_mission]]),
      ("enter",[],"Enter 7.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_test2"],[change_screen_mission]]),
      ("enter",[],"Enter 8.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_test3"],[change_screen_mission]]),
      ("enter",[],"Enter 9.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_multi_scene_13"],[change_screen_mission]]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
  (
    "battlefields",0,
    "{!}Select a field...",
    "none",
    [],
    [

      ("enter_f1",[],"{!}Field 1",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_1"],[change_screen_mission]]),
      ("enter_f2",[],"{!}Field 2",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_2"],[change_screen_mission]]),
      ("enter_f3",[],"{!}Field 3",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_3"],[change_screen_mission]]),
      ("enter_f4",[],"{!}Field 4",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_4"],[change_screen_mission]]),
      ("enter_f5",[],"{!}Field 5",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_5"],[change_screen_mission]]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
  (
    "dhorak_keep",0,
#    "Dhorak Keep, the stronghold of the bandits stands overlooking the barren wilderness.",
    "You enter the Dhorak Keep",
    "none",
    [],
    [
      ("enter",[],"Enter.",[(set_jump_mission,"mt_town_center"),(jump_to_scene,"scn_dhorak_keep"),(change_screen_mission)]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),

##  (
##    "center_under_attack_while_resting",0,
##    "{s1} has been besieged by {s2}, and the enemy seems to be preparing for an assault!\
## What will you do?",
##    "none",
##    [
##        (party_get_battle_opponent, ":besieger_party", "$auto_enter_town"),
##        (str_store_party_name, s1, "$auto_enter_town"),
##        (str_store_party_name, s2, ":besieger_party"),
##    ],
##    [
##      ("defend_against_siege", [],"Help the defenders of {s1}!",
##       [
##           (assign, "$g_last_player_do_nothing_against_siege_next_check", 0),
##           (rest_for_hours, 0, 0, 0),
##           (change_screen_return),
##           (start_encounter, "$auto_enter_town"),
##           ]),
##      ("do_not_defend_against_siege",[],"Find a secure place and wait there.",
##       [
##           (change_screen_return),
##           ]),
##    ]
##  ),

  (#SB : pic hotkeys
    "join_siege_outside",mnf_scale_picture|mnf_enable_hot_keys,
    "{s1} has come under siege by {s2}.",
    "none",
    [
        (str_store_party_name, s1, "$g_encountered_party"),
        (str_store_party_name, s2, "$g_encountered_party_2"),
		  ##diplomacy start+ Get gender from script
        #(troop_get_type, ":is_female", "trp_player"),#<- replaced
        (try_begin),
          #(eq, ":is_female", 1),#<- replaced
		  (eq, "$character_gender", tf_female),#<- added
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),
		  ##diplomacy end+
    ],
    [
      ("approach_besiegers",[(store_faction_of_party, ":faction_no", "$g_encountered_party_2"),
                             (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
                             (ge, ":relation", 0),
                             (store_faction_of_party, ":faction_no", "$g_encountered_party"),
                             (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
                             (lt, ":relation", 0),
                             ],"Approach the siege camp.",[
          (jump_to_menu, "mnu_besiegers_camp_with_allies"),
                                ]),
      ("pass_through_siege",[(store_faction_of_party, ":faction_no", "$g_encountered_party"),
                             (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
                             (ge, ":relation", 0),
                             ],"Pass through the siege lines and enter {s1}.",
       [
            (jump_to_menu,"mnu_cut_siege_without_fight"),
          ]),
      ("leave",[],"Leave.",[(leave_encounter),
                            (change_screen_return)]),
    ]
  ),
  (
    "cut_siege_without_fight",0,
    "The besiegers let you approach the gates without challenge.",
    "none",
    [],
    [
      ("continue",[],"Continue...",[(try_begin),
                                   (this_or_next|eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
                                   (eq, "$g_encountered_party_faction", "$players_kingdom"),
                                   (jump_to_menu, "mnu_town"),
                                 (else_try),
                                   (jump_to_menu, "mnu_castle_outside"),
                                 (try_end)]),
      ]
  ),
  ( #SB : pic hotkeys
    "besiegers_camp_with_allies",mnf_enable_hot_keys,
    "{s1} remains under siege. The banners of {s2} fly above the camp of the besiegers,\
 where you and your men are welcomed.",
    "none",
    [
        (str_store_party_name, s1, "$g_encountered_party"),
        (str_store_party_name, s2, "$g_encountered_party_2"),
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", "$g_encountered_party_2"),
        (select_enemy, 0),
        (call_script, "script_encounter_calculate_fit"),
        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
		  ###diplomacy start+
		  ##If terrain advantage is on, use siege settings
          #(assign, ":save_dplmc_terrain_advantage", "$g_dplmc_terrain_advantage"),
		  ##(assign, "$g_dplmc_terrain_advantage", ":save_dplmc_terrain_advantage"),
		  #(try_begin),
		  #   (eq, "$g_dplmc_terrain_advantage", TERRAIN_ADVANTAGE_ENABLE),
		  #   (assign, "$g_dplmc_terrain_advantage", TERRAIN_ADVANTAGE_FORCE_SIEGE),
		  #(try_end),
		  ###diplomacy end+
          (call_script, "script_encounter_init_variables"),
		  ###diplomacy start+
		  ##Revert terrain advantage setting
		  #(assign, "$g_dplmc_terrain_advantage", ":save_dplmc_terrain_advantage"),
		  ###diplomacy end+
        (try_end),

        (try_begin),
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (else_try),
          (assign, ":enemy_finished", 0),
          (try_begin),
            (eq, "$g_battle_result", 1),
            (assign, ":enemy_finished", 1),
          (else_try),
            (le, "$g_enemy_fit_for_battle", 0),
            (ge, "$g_friend_fit_for_battle", 1),
            (assign, ":enemy_finished", 1),
          (try_end),
          (this_or_next|eq, ":enemy_finished", 1),
          (eq, "$g_enemy_surrenders", 1),
##          (assign, "$g_next_menu", -1),#"mnu_castle_taken_by_friends"),
##          (jump_to_menu, "mnu_total_victory"),

          #SB : TODO : add prisoner train of unclaimed prisoners and such, succeed quests by proxy
          (party_get_num_prisoner_stacks, ":num_prisoner_stacks", "$g_enemy_party"),
          (try_for_range, ":stack_no", 0, ":num_prisoner_stacks"),
            # (eq, ":break", 0),
            (party_prisoner_stack_get_troop_id, ":stack_troop", "p_collective_enemy", ":stack_no"),
            (troop_is_hero, ":stack_troop"),
            (try_begin),
              (check_quest_active, "qst_rescue_prisoner"),
              (quest_slot_eq, "qst_rescue_prisoner", slot_quest_target_troop, ":stack_troop"),
              (call_script, "script_succeed_quest", "qst_rescue_prisoner"),
            (else_try),
              (check_quest_active, "qst_deliver_message_to_prisoner_lord"),
              (quest_slot_eq, "qst_deliver_message_to_prisoner_lord", slot_quest_target_troop, ":stack_troop"),
              (call_script, "script_end_quest", "qst_deliver_message_to_prisoner_lord"),
            (try_end),
          (try_end),
          (try_begin), #check if player gets a share of party prisoners, freed prisoners doesn't count
            (store_faction_of_party, ":faction_no", "$g_ally_party"),
            (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":faction_no"),
            (ge, reg0, DPLMC_FACTION_STANDING_MEMBER),
            #check relation with siege leader as well
            (party_stack_get_troop_id, ":leader","$g_encountered_party_2",0),
            (call_script, "script_troop_get_player_relation", ":leader"),
            (this_or_next|troop_slot_eq, ":leader", slot_lord_reputation_type, lrep_martial),
            (ge, reg0, -10),
            (eq, "$capture_screen_shown", 0),
            (assign, "$capture_screen_shown", 1),
            
            (party_clear, "p_temp_party"),
            (assign, "$g_move_heroes", 0),
            (change_screen_exchange_with_party, "p_temp_party"),
          (else_try), #check if player has seen the loot
            (eq, "$loot_screen_shown", 0),
            (assign, "$loot_screen_shown", 1),
            (troop_clear_inventory, "trp_temp_troop"),
            (call_script, "script_party_calculate_loot", "p_total_enemy_casualties"), #p_encountered_party_backup changed to total_enemy_casualties
            (gt, reg0, 0),
            (troop_sort_inventory, "trp_temp_troop"),
            (try_begin),
              (call_script, "script_cf_dplmc_player_party_meets_autoloot_conditions"),
              (assign, "$dplmc_return_menu", "$g_siege_final_menu"),
              (assign, "$lord_selected", "trp_player"),
              (jump_to_menu, "mnu_dplmc_manage_loot_pool"),
            (else_try),
              #Old behavior:
              (change_screen_loot, "trp_temp_troop"),
            (try_end),
          (else_try), #SB : increment globals, add exp
            (call_script, "script_party_give_xp_and_gold", "p_total_enemy_casualties"),
            (val_add, "$g_total_victories", 1),
            (call_script, "script_party_wound_all_members", "$g_enemy_party"),
            (leave_encounter),
            (change_screen_return),
          (try_end),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
          (assign, ":ally_num_soldiers", reg0),
          (eq, "$g_battle_result", -1),
          (eq, ":ally_num_soldiers", 0), #battle lost (TODO : also compare this with routed allies too like in other parts)
          (leave_encounter),
          (change_screen_return),
        (try_end),
        ],
    [
      ("talk_to_siege_commander",[]," Request a meeting with the commander.",[
                                (call_script, "script_get_meeting_scene"), (assign, ":meeting_scene", reg0),
                                (modify_visitors_at_site,":meeting_scene"),(reset_visitors),
                                (set_visitor,0,"trp_player"),
                                (party_stack_get_troop_id, ":siege_leader_id","$g_encountered_party_2",0),
                                (party_stack_get_troop_dna,":siege_leader_dna","$g_encountered_party_2",0),
                                (set_visitor,17,":siege_leader_id",":siege_leader_dna"),
                                (set_jump_mission,"mt_conversation_encounter"),
                                (jump_to_scene,":meeting_scene"),
                                (assign, "$talk_context", tc_siege_commander),
                                (change_screen_map_conversation, ":siege_leader_id")]),
      ("join_siege_with_allies",[(neg|troop_is_wounded, "trp_player")], "Join the next assault.",
       [
           (assign, "$g_joined_battle_to_help", 1),
           (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
           (try_begin),
             (check_quest_active, "qst_join_siege_with_army"),
             (quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, "$g_encountered_party"),
             (add_xp_as_reward, 250),
             (call_script, "script_end_quest", "qst_join_siege_with_army"),
             #Reactivating follow army quest
             (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
             (str_store_troop_name_link, s9, ":faction_marshall"),
             (setup_quest_text, "qst_follow_army"),
             ##diplomacy start+ fix pronoun
             (call_script, "script_dplmc_store_troop_is_female", ":faction_marshall"),
             (str_store_string, s2, "@{s9} wants you to follow {reg0?her:his} army until further notice."),
             ##diplomacy end+
             (call_script, "script_start_quest", "qst_follow_army", ":faction_marshall"),
             (assign, "$g_player_follow_army_warnings", 0),
           (try_end),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_walls),
           (else_try),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
           (try_end),
           (call_script, "script_calculate_battle_advantage"),
           (val_mul, reg0, 2),
           (val_div, reg0, 3), #scale down the advantage a bit in sieges.
           (set_battle_advantage, reg0),
           (set_party_battle_mode),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_center_siege_with_belfry, 1),
             (set_jump_mission,"mt_castle_attack_walls_belfry"),
           (else_try),
             (set_jump_mission,"mt_castle_attack_walls_ladder"),
           (try_end),
           (jump_to_scene,":battle_scene"),
           (assign, "$g_siege_final_menu", "mnu_besiegers_camp_with_allies"),
           (assign, "$g_siege_battle_state", 1),
           (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
           (jump_to_menu, "mnu_battle_debrief"),
           (change_screen_mission),
          ]),
      ("join_siege_stay_back", [(call_script, "script_party_count_members_with_full_health", "p_main_party"),
                                (ge, reg0, 3),
                                ],
       "Order your soldiers to join the next assault without you.",
       [
         (assign, "$g_joined_battle_to_help", 1),
         (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
         (try_begin),
           (check_quest_active, "qst_join_siege_with_army"),
           (quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, "$g_encountered_party"),
           (add_xp_as_reward, 100),
           (call_script, "script_end_quest", "qst_join_siege_with_army"),
           #Reactivating follow army quest
           (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
           (str_store_troop_name_link, s9, ":faction_marshall"),
           (setup_quest_text, "qst_follow_army"),
           ##diplomacy start+ fix pronoun
           (call_script, "script_dplmc_store_troop_is_female", ":faction_marshall"),
           (str_store_string, s2, "@{s9} wants you to follow {reg0?her:his} army until further notice."),
           ##diplomacy end+
           (call_script, "script_start_quest", "qst_follow_army", ":faction_marshall"),
           (assign, "$g_player_follow_army_warnings", 0),
         (try_end),
         (jump_to_menu,"mnu_castle_attack_walls_with_allies_simulate")]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),

  (
    "castle_outside",mnf_scale_picture,
    "You are outside {s2}.{s11} {s3} {s4}",
    "none",
    [
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", -1),
        (str_store_party_name, s2,"$g_encountered_party"),
        (call_script, "script_encounter_calculate_fit"),
        (assign,"$all_doors_locked",1),
        (assign, "$current_town","$g_encountered_party"),

        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (call_script, "script_let_nearby_parties_join_current_battle", 1, 0),
		  ###diplomacy start+
		  ##If terrain advantage is on, use siege settings for estimating strength
          #(assign, ":save_dplmc_terrain_advantage", "$g_dplmc_terrain_advantage"),
		  #(try_begin),
		  #   (eq, "$g_dplmc_terrain_advantage", TERRAIN_ADVANTAGE_ENABLE),
		  #   (assign, "$g_dplmc_terrain_advantage", TERRAIN_ADVANTAGE_FORCE_SIEGE),
		  #(try_end),
		  ###diplomacy end+
          (call_script, "script_encounter_init_variables"),
		  ###diplomacy start+
		  ##Revert terrain advantage settings
		  #(assign, "$g_dplmc_terrain_advantage", ":save_dplmc_terrain_advantage"),
		  ###diplomacy end+
          (assign, "$entry_to_town_forbidden",0),
         
         (try_begin),         #dckplmc: handle removing disguise here, bug with saving in-mission
             (gt, "$sneaked_into_town", disguise_none),
             (display_message, "@Removing disguise...", message_alert), #SB : colorize
             (try_begin),
               (eq, "$g_dplmc_player_disguise", 1),
               (set_show_messages, 0),
               #equipment is deposited back to inventory, it starts off blank
               (try_for_range, ":i_slot", ek_item_0, ek_food + 1),
                 (troop_get_inventory_slot, ":item", "trp_player", ":i_slot"),
                 (neq, ":item", -1),
                 (troop_get_inventory_slot_modifier, ":imod", "trp_player", ":i_slot"),
                 (troop_add_item, "trp_random_town_sequence", ":item", ":imod"),
               (try_end),
               #less efficient, but merge and respect original player inventory's order
               (call_script, "script_move_inventory_and_gold", "trp_player", "trp_random_town_sequence", 0), #do not move gold
               (call_script, "script_dplmc_copy_inventory", "trp_random_town_sequence", "trp_player"),
               (call_script, "script_troop_transfer_gold", "trp_random_town_sequence", "trp_player", 0), #move remaining gold now
               (set_show_messages, 1),
             (try_end),
             (assign, "$sneaked_into_town", disguise_none),
          (try_end),
          
          (assign, "$sneaked_into_town", disguise_none),
          (assign, "$town_entered", 0),
#          (assign, "$waiting_for_arena_fight_result", 0),
          (assign, "$encountered_party_hostile", 0),
          (assign, "$encountered_party_friendly", 0),
          (try_begin),
            (gt, "$g_player_besiege_town", 0),
            (neq,"$g_player_besiege_town","$g_encountered_party"),
            (party_slot_eq, "$g_player_besiege_town", slot_center_is_besieged_by, "p_main_party"),
            (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
            (assign,"$g_player_besiege_town",-1),
          (try_end),
          (try_begin),
            (lt, "$g_encountered_party_relation", 0),
            (assign, "$encountered_party_hostile", 1),
            (assign,"$entry_to_town_forbidden",1),
          (try_end),

          ##diplomacy begin
          (try_begin),
            (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
            (assign, "$encountered_party_hostile", 1),
            (assign,"$entry_to_town_forbidden",1),
          (try_end),
          ##diplomacy end

          (assign,"$cant_sneak_into_town",0),
          (try_begin),
            (eq,"$current_town","$last_sneak_attempt_town"),
            (store_current_hours,reg(2)),
            (val_sub,reg(2),"$last_sneak_attempt_time"),
            (lt,reg(2),12),
            (assign,"$cant_sneak_into_town",1),
          (try_end),
        (else_try), #second or more turn
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (try_end),

        (str_clear,s4),
        (try_begin),
          (eq,"$entry_to_town_forbidden",1),
          (try_begin),
            (eq,"$cant_sneak_into_town",1),
            (str_store_string,s4,"str_sneaking_to_town_impossible"),
          (else_try),
            (str_store_string,s4,"str_entrance_to_town_forbidden"),
          (try_end),
        (try_end),

        (party_get_slot, ":center_lord", "$current_town", slot_town_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name,s9,":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8,":center_lord"),
          (str_store_string,s7,"@{s8} of {s9}"),
        (try_end),
        ##diplomacy start+
        
        #SB : move coruler variable up here
		(assign, ":is_coruler", 0),
		(try_begin),
			(eq, "$g_encountered_party_faction", "$players_kingdom"),
			(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
			(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
			(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
			(assign, ":is_coruler", 1),
		(try_end),
		(assign, ":save_reg0", reg0),#save variables
		(assign, ":save_reg4", reg4),
		(assign, ":relation", 0),
		(assign, reg4, 0),
		(try_begin),#If there's a relation of some kind, write it to s11 (which we'll overwrite below)
			(lt, ":center_lord", 1),
		(else_try),
			#your relative
			(call_script, "script_troop_get_family_relation_to_troop", ":center_lord", "trp_player"),#outputs to s11, ":relation", and reg4
			(ge, ":relation", 1),#Fall through if this not a relative
		(else_try),
			#your current liege
			(eq, ":center_faction", "$players_kingdom"),
			(is_between, ":center_faction", kingdoms_begin, kingdoms_end),#include fac_player_supporters_faction for claimant quest
			(faction_slot_eq, ":center_faction", slot_faction_leader, ":center_lord"),
			(str_store_string, s11, "@liege"),
			(assign, ":relation", 1),
		(else_try),
			#your former liege if you renounced a kingdom
			(eq, ":center_faction", "$players_oath_renounced_against_kingdom"),
			(is_between, ":center_faction", npc_kingdoms_begin, npc_kingdoms_end),
			(faction_slot_eq, ":center_faction", slot_faction_leader, ":center_lord"),
			(str_store_string, s11, "@former liege"),
			(assign, ":relation", 1),
		(else_try),
			#stop here for lords you haven't met, or non-hero troops
			(this_or_next|neg|troop_is_hero, ":center_lord"),
			(troop_slot_eq, ":center_lord", slot_troop_met, 0),
		(else_try),
			#check for affiliates
			(call_script, "script_dplmc_is_affiliated_family_member", ":center_lord"),
			(ge, reg0, 1), #SB : substitute register
			(assign, ":relation", 1),
			(try_begin),
				(ge, "$g_encountered_party_relation", 0),#don't say "ally" when you might fight them, as that's confusing
				(str_store_string, s11, "str_dplmc_ally"),
			(else_try),
				(str_store_string, s11, "@affiliate"),
			(try_end),
		(else_try),
			#check for friends (former companions)
			(call_script, "script_troop_get_player_relation", ":center_lord"),
            (assign, ":relation", reg0),
			(is_between, ":center_lord", companions_begin, companions_end),
			(neg|troop_slot_eq, ":center_lord", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
			(try_begin),
			   (ge, "$g_encountered_party_relation", 0),#don't say "ally" when you might fight them, as that's confusing
			   (ge, ":relation", 50),
			   (str_store_string, s11, "str_dplmc_ally"),
			(else_try),
				(ge, "$g_encountered_party_relation", 0),
				(ge, ":relation", 20),
				(str_store_string, s11, "str_dplmc_friend"),
			(else_try),
				(str_store_string, s11, "@former companion"),
			(try_end),
			(assign, ":relation", 1),
		(else_try),
			#don't print "friend" if you might fight them
			(lt, "$g_encountered_party_relation", 0),
			(assign, ":relation", 0),
		(else_try),
			#check for friends
			# (val_div, ":relation", 50),#right now ":relation" holds the relation with the player
			(ge, ":relation", 50),
			(str_store_string, s11, "str_dplmc_friend"),
		(else_try),
			#check for marshall
			(eq, ":center_faction", "$players_kingdom"),
			(faction_slot_eq, ":center_faction", slot_faction_marshall, ":center_lord"),
			(str_store_string, s11, "@marshall"),
		(else_try), #SB : coruler check above
			# #check for vassal of player if nothing else to say
			# (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":center_faction"),
			# (val_add, ":relation", 1),
			# (val_sub, ":relation", DPLMC_FACTION_STANDING_LEADER_SPOUSE),
			(ge, ":is_coruler", 1),
			(str_store_string, s11, "@vassal"),
            (assign, ":relation", 1),
		(else_try),
			(assign, ":relation", 0),
		(try_end),
		##diplomacy end+
        (try_begin), # same mnu_town
          (party_slot_eq,"$current_town",slot_party_type, spt_castle),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the castle gate."),
		  ##diplomacy start+ If ":relation" > 0, a relation string was written to {s11} above
		  (else_try),
			(ge, ":relation", 1),
			(str_store_string, s11, "@ You see the banner of your {s11} {s7} over the castle gate."),
		  ##diplomacy end+
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string, s11,"@ You see the banner of {s7} over the castle gate."),
          (else_try),
		    (is_between, ":center_faction", kingdoms_begin, kingdoms_end),
            (str_store_string, s11,"str__this_castle_is_temporarily_under_royal_control"),
		  (else_try),
            (str_store_string, s11,"str__this_castle_does_not_seem_to_be_under_anyones_control"),
          (try_end),
        (else_try),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string, s11,"@ Your own banner flies over the town gates."),
		  ##diplomacy start+ If ":relation" > 0, a relation string was written to {s11} above
		  (else_try),
			(ge, ":relation", 1),
			(str_store_string, s11, "@ You see the banner of your {s11} {s7} over the town gates."),
		  ##diplomacy end+
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string, s11,"@ You see the banner of {s7} over the town gates."),
          (else_try),
		    (is_between, ":center_faction", kingdoms_begin, kingdoms_end),
            (str_store_string, s11,"str__this_town_is_temporarily_under_royal_control"),
		  (else_try),
            (str_store_string, s11,"str__the_townspeople_seem_to_have_declared_their_independence"),
          (try_end),
        (try_end),

        #SB : get rid of register usage
        (party_get_num_companions, ":num_enemies", "p_collective_enemy"),
        (assign,"$castle_undefended",0),
        (str_clear, s3),
        (try_begin),
          (eq, ":num_enemies", 0),
          (assign,"$castle_undefended",1),
#          (party_set_faction,"$g_encountered_party","fac_neutral"),
#          (party_set_slot, "$g_encountered_party", slot_town_lord, stl_unassigned),
          (str_store_string, s3, "str_castle_is_abondened"),
        (else_try),
        ##diplomacy begin
          (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
          (str_store_string, s3, "str_dplmc_place_is_occupied_by_insurgents"),
          #SB : assign globals, doesn't make senes
        (else_try),
        ##diplomacy end
		##diplomacy start+ Handle player is co-ruler of kingdom
		  (this_or_next|eq, ":is_coruler", 1),
		##diplomacy end+
          (eq,"$g_encountered_party_faction","fac_player_supporters_faction"),
          (str_store_string, s3, "str_place_is_occupied_by_player"),
        (else_try),
          (lt, "$g_encountered_party_relation", 0),
          (str_store_string, s3, "str_place_is_occupied_by_enemy"),
        (else_try),
#          (str_store_string, s3, "str_place_is_occupied_by_friendly"),
        (try_end),
		##diplomacy start+
		(assign, reg0, ":save_reg0"),#revert variables
		(assign, reg4, ":save_reg4"),
		##diplomacy end+

        (try_begin),
          (eq, "$g_leave_town_outside",1),
          (assign, "$g_leave_town_outside",0),
          (assign, "$g_permitted_to_center", 0),
          (change_screen_return),
        (else_try),
          (check_quest_active, "qst_escort_lady"),
          (quest_slot_eq, "qst_escort_lady", slot_quest_target_center, "$g_encountered_party"),
          (quest_get_slot, ":quest_object_troop", "qst_escort_lady", slot_quest_object_troop),
          # (call_script, "script_get_meeting_scene"), (assign, ":meeting_scene", reg0),
          # (modify_visitors_at_site,":meeting_scene"),
          # (reset_visitors),
          # (set_visitor,0, "trp_player"),
          # (set_visitor,17, ":quest_object_troop"),
          # (set_jump_mission, "mt_conversation_encounter"),
          # (jump_to_scene, ":meeting_scene"),
          (assign, "$talk_context", tc_entering_center_quest_talk),
          # (change_screen_map_conversation, ":quest_object_troop"),
          (call_script, "script_setup_troop_meeting", ":quest_object_troop", -1),
        (else_try),
          (check_quest_active, "qst_kidnapped_girl"),
          (quest_slot_eq, "qst_kidnapped_girl", slot_quest_giver_center, "$g_encountered_party"),
          (quest_slot_eq, "qst_kidnapped_girl", slot_quest_current_state, 3),
          # (call_script, "script_get_meeting_scene"), (assign, ":meeting_scene", reg0),
          # (modify_visitors_at_site,":meeting_scene"),
          # (reset_visitors),
          # (set_visitor,0, "trp_player"),
          # (set_visitor,17, "trp_kidnapped_girl"),
          # (set_jump_mission, "mt_conversation_encounter"),
          # (jump_to_scene, ":meeting_scene"),
          (assign, "$talk_context", tc_entering_center_quest_talk),
          # (change_screen_map_conversation, "trp_kidnapped_girl"),
          (call_script, "script_setup_troop_meeting", "trp_kidnapped_girl", -1),
        (else_try), #SB : automatically talk to caravans
          (check_quest_active, "qst_escort_merchant_caravan"),
          (quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
          (party_is_active, ":quest_target_party"),
          (quest_get_slot, ":quest_target_center", "qst_escort_merchant_caravan", slot_quest_target_center),
          (eq,"$current_town",":quest_target_center"),
          (quest_slot_eq, "qst_escort_merchant_caravan", slot_quest_current_state, 1),
          (store_distance_to_party_from_party, ":dist", ":quest_target_center",":quest_target_party"),
          (lt,":dist",4),
          # (start_encounter, ":quest_target_party"),
          (assign, "$talk_context", tc_party_encounter),
          (assign, "$g_encountered_party", ":quest_target_party"),
          (party_stack_get_troop_id, ":caravan_leader", ":quest_target_party", 0),
          (party_stack_get_troop_dna, ":caravan_leader_dna", ":quest_target_party", 0),
          (call_script, "script_setup_troop_meeting", ":caravan_leader", ":caravan_leader_dna"),
        (else_try), #SB : should really merge these quests, this is for older savegames
          (eq, "$caravan_escort_state",1),
          (party_is_active, "$caravan_escort_party_id"),
          (eq,"$current_town","$caravan_escort_destination_town"),
          (store_distance_to_party_from_party, ":dist", "$caravan_escort_destination_town", "$caravan_escort_party_id"),
          (lt,":dist", 5),
          # (store_distance_to_party_from_party, ":caravan_distance_to_player","p_main_party","$caravan_escort_party_id"),
          # (lt, ":caravan_distance_to_player", 5),
          # (start_encounter, "$caravan_escorted_party_id"),

          (assign, "$talk_context", tc_party_encounter),
          (assign, "$g_encountered_party", "$caravan_escort_party_id"),
          (party_stack_get_troop_id, ":caravan_leader", "$caravan_escort_party_id", 0),
          (party_stack_get_troop_dna, ":caravan_leader_dna", "$caravan_escort_party_id", 0),
          (call_script, "script_setup_troop_meeting", ":caravan_leader", ":caravan_leader_dna"),
          # (start_map_conversation, ":caravan_leader", ":caravan_leader_dna"),
          
##        (else_try),
##          (gt, "$lord_requested_to_talk_to", 0),
##          (store_current_hours, ":cur_hours"),
##          (neq, ":cur_hours", "$quest_given_time"),
##          (modify_visitors_at_site,"scn_conversation_scene"),
##          (reset_visitors),
##          (assign, ":cur_lord", "$lord_requested_to_talk_to"),
##          (assign, "$lord_requested_to_talk_to", 0),
##          (set_visitor,0,"trp_player"),
##          (set_visitor,17,":cur_lord"),
##          (set_jump_mission,"mt_conversation_encounter"),
##          (jump_to_scene,"scn_conversation_scene"),
##          (assign, "$talk_context", tc_castle_gate_lord),
##          (change_screen_map_conversation, ":cur_lord"),
        (else_try),
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
          (jump_to_menu,"mnu_town"),
        ##diplomacy begin
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
          (try_begin),
            (eq, "$g_player_besiege_town", "$g_encountered_party"),
            (jump_to_menu, "mnu_castle_besiege"),
          (try_end),
        ##diplomacy end
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
		  ##diplomacy start+ Handle player is co-ruler of kingdom
		  (assign, ":is_coruler",0),
	  	  (try_begin),
			(eq, "$g_encountered_party_faction", "$players_kingdom"),
			(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
			(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
			(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
			(assign, ":is_coruler", 1),
		  (try_end),
		  (this_or_next|eq, ":is_coruler", 1),
		  ##diplomacy end+
          (this_or_next|party_slot_eq, "$g_encountered_party", slot_town_lord, "trp_player"),
          (faction_slot_eq, "$g_encountered_party_faction", slot_faction_leader, "trp_player"),
          (jump_to_menu, "mnu_enter_your_own_castle"),
        (else_try),
          (party_slot_eq,"$g_encountered_party", slot_party_type,spt_castle),
          (ge, "$g_encountered_party_relation", 0),
          (this_or_next|eq,"$castle_undefended", 1),
          (this_or_next|eq, "$g_permitted_to_center", 1),
          (eq, "$g_encountered_party_faction", "$players_kingdom"),
          (jump_to_menu, "mnu_town"),
        (else_try),
          (party_slot_eq,"$g_encountered_party", slot_party_type,spt_town),
          (ge, "$g_encountered_party_relation", 0),
          (jump_to_menu, "mnu_town"),
        (else_try),
          (eq, "$g_player_besiege_town", "$g_encountered_party"),
          (jump_to_menu, "mnu_castle_besiege"),
        (try_end),

          ##diplomacy begin
          (try_begin),
            (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
            (set_background_mesh, "mesh_pic_townriot"),
          (else_try),
          ##diplomacy end
            (call_script, "script_set_town_picture"),
          ##diplomacy begin
          (try_end),
          ##diplomacy end
        ],
    [
#        ("talk_to_castle_commander",[
#            (party_get_num_companions, ":no_companions", "$g_encountered_party"),
#            (ge, ":no_companions", 1),
#            (eq,"$ruler_meeting_denied",0), #this variable is removed
#            ],
#         "Request a meeting with the lord of the castle.",[
#             (modify_visitors_at_site,"scn_conversation_scene"),(reset_visitors),
#             (set_visitor,0,"trp_player"),
#             (party_stack_get_troop_id, reg(6),"$g_encountered_party",0),
#             (party_stack_get_troop_dna,reg(7),"$g_encountered_party",0),
#             (set_visitor,17,reg(6),reg(7)),
#             (set_jump_mission,"mt_conversation_encounter"),
#             (jump_to_scene,"scn_conversation_scene"),
#             (assign, "$talk_context", tc_castle_commander),
#             (change_screen_map_conversation, reg(6))
#             ]),
      ("approach_gates",[(this_or_next|eq,"$entry_to_town_forbidden",1),
                          (party_slot_eq,"$g_encountered_party", slot_party_type,spt_castle),
                          #SB : not infested by peasants, they'd just kick you out
                          (neg|party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
                          ],
       "Approach the gates and hail the guard.",[
                                                  (jump_to_menu, "mnu_castle_guard"),
##                                                   (modify_visitors_at_site,"scn_conversation_scene"),(reset_visitors),
##                                                   (set_visitor,0,"trp_player"),
##                                                   (store_faction_of_party, ":cur_faction", "$g_encountered_party"),
##                                                   (faction_get_slot, ":cur_guard", ":cur_faction", slot_faction_guard_troop),
##                                                   (set_visitor,17,":cur_guard"),
##                                                   (set_jump_mission,"mt_conversation_encounter"),
##                                                   (jump_to_scene,"scn_conversation_scene"),
##                                                   (assign, "$talk_context", tc_castle_gate),
##                                                   (change_screen_map_conversation, ":cur_guard")
                                                   ]),

      ("town_sneak",
        [
          (try_begin),
            (party_slot_eq, "$g_encountered_party", slot_party_type,spt_town),
            (str_store_string, s7, "str_town"),
          (else_try),
            (str_store_string, s7, "str_castle"),
          (try_end),

          (eq, "$entry_to_town_forbidden", 1),
          (eq, "$cant_sneak_into_town", 0),
          #SB : do not let player in at all, because the garrison can be managed
          (neg|party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
        ],
       "Disguise yourself and try to sneak into the {s7}",
       [
       
         #SB : apply different disguises in new system, with outcomes
        (try_begin),
          (eq, "$g_dplmc_player_disguise", 1),
          (troop_get_slot, ":player_disguise", "trp_player", slot_troop_player_disguise_sets),
          (val_max, ":player_disguise", disguise_pilgrim),
          (troop_set_slot, "trp_player", slot_troop_player_disguise_sets, ":player_disguise"),
          # (assign, "$sneaked_into_town", disguise_none), #set no disguise
          (troop_clear_inventory, "trp_random_town_sequence"), # clear items to bring
          
          (try_for_range, ":i_slot", 0, ek_food + 1), #dckplmc: bugfix - clear equipped items
            (troop_set_inventory_slot, "trp_random_town_sequence", ":i_slot", -1),
          (try_end),
          
          (store_troop_gold, ":cur_amount", "trp_random_town_sequence"),
          (troop_remove_gold, "trp_random_town_sequence", ":cur_amount"),#clear gold
          (assign, "$temp", 0),
          (jump_to_menu, "mnu_dplmc_choose_disguise"),
        (else_try),
          (faction_get_slot, ":player_alarm", "$g_encountered_party_faction", slot_faction_player_alarm),
          (party_get_num_companions, ":num_men", "p_main_party"),
          (party_get_num_prisoners, ":num_prisoners", "p_main_party"),
          (val_add, ":num_men", ":num_prisoners"),
          (val_mul, ":num_men", 2),
          (val_div, ":num_men", 3),
          (store_add, ":get_caught_chance", ":player_alarm", ":num_men"),
          (store_random_in_range, ":random_chance", 0, 100),
          (try_begin),
            (this_or_next|ge, "$cheat_mode", 1),
            (this_or_next|ge, ":random_chance", ":get_caught_chance"),
            (eq, "$g_last_defeated_bandits_town", "$g_encountered_party"),
            (assign, "$g_last_defeated_bandits_town", 0),
            (assign, "$sneaked_into_town", disguise_pilgrim),
            (assign, "$town_entered", 1),
            (jump_to_menu,"mnu_sneak_into_town_suceeded"),
            (assign, "$g_mt_mode", tcm_disguised),
          (else_try),
            (jump_to_menu,"mnu_sneak_into_town_caught"),
          (try_end),
        (try_end),
        ]),
      ##diplomacy begin
      ("dplmc_riot_start_siege",
       [
           (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
           (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
           (lt, "$g_encountered_party_2", 1),
           (call_script, "script_party_count_fit_for_battle","p_main_party"),
           (gt, reg0, 5),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (assign, reg6, 1),
           (else_try),
             (assign, reg6, 0),
           (try_end),
           ],
       "Besiege the {reg6?town:castle} to counter the insurgency.",
       [
         (assign,"$g_player_besiege_town","$g_encountered_party"),
         (jump_to_menu, "mnu_castle_besiege"),
         ]),
       ("dplmc_riot_negotiate",
       [
           (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
           (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
           (lt, "$g_encountered_party_2", 1),
           (call_script, "script_party_count_fit_for_battle","p_main_party"),
           (gt, reg0, 5),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (assign, reg6, 1),
           (else_try),
             (assign, reg6, 0),
           (try_end),
           ],
       "Begin negotiations.",
       [
          (jump_to_menu, "mnu_dplmc_riot_negotiate"),
        ]),

     ##diplomacy end
      ("castle_start_siege",
       [
           ##diplomacy begin
           (neg|party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
           ##diplomacy end
           (this_or_next|party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
           (             party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
           (store_relation, ":reln", "$g_encountered_party_faction", "fac_player_supporters_faction"),
           (lt, ":reln", 0),
           (lt, "$g_encountered_party_2", 1),
           (call_script, "script_party_count_fit_for_battle","p_main_party"),
           (gt, reg(0), 5),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (assign, reg6, 1),
           (else_try),
             (assign, reg6, 0),
           (try_end),
           ],
       "Besiege the {reg6?town:castle}.",
       [
         (assign,"$g_player_besiege_town","$g_encountered_party"),
         (store_relation, ":relation", "fac_player_supporters_faction", "$g_encountered_party_faction"),
         (val_min, ":relation", -40),
         (call_script, "script_set_player_relation_with_faction", "$g_encountered_party_faction", ":relation"),
         (call_script, "script_update_all_notes"),
         (jump_to_menu, "mnu_castle_besiege"),
         ]),

      ("cheat_castle_start_siege",
       [
         (eq, "$cheat_mode", 1),
         (this_or_next|party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
         (             party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
         (store_relation, ":reln", "$g_encountered_party_faction", "fac_player_supporters_faction"),
         (ge, ":reln", 0),
         (lt, "$g_encountered_party_2", 1),
         (call_script, "script_party_count_fit_for_battle","p_main_party"),
         (gt, reg(0), 1),
         (try_begin),
           (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
           (assign, reg6, 1),
         (else_try),
           (assign, reg6, 0),
         (try_end),
           ],
       "{!}CHEAT: Besiege the {reg6?town:castle}...",
       [
           (assign,"$g_player_besiege_town","$g_encountered_party"),
           (jump_to_menu, "mnu_castle_besiege"),
           ]),

      ("castle_leave",[],"Leave.",[(change_screen_return,0)]),
      #SB : the three options below are covered in cheats
      ("castle_cheat", [(ge, "$cheat_mode", 1)], "{!}Use Cheats", [
        # (assign, "$sneaked_into_town", disguise_pilgrim),
        (assign, "$town_entered", 1),
        # (assign, "$g_mt_mode", tcm_disguised),
        (jump_to_menu, "mnu_town_cheats"),
      ]),
      
      # ("castle_cheat_interior",[(eq, "$cheat_mode", 1)], "{!}CHEAT! Interior.",[(set_jump_mission,"mt_ai_training"),
                                                       # (party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
                                                       # (jump_to_scene,":castle_scene"),
                                                       # (change_screen_mission)]),
      # ("castle_cheat_exterior",[(eq, "$cheat_mode", 1)], "{!}CHEAT! Exterior.",[
# #                                                       (set_jump_mission,"mt_town_default"),
                                                       # (set_jump_mission,"mt_ai_training"),
                                                       # (party_get_slot, ":castle_scene", "$current_town", slot_castle_exterior),
                                                       # (jump_to_scene,":castle_scene"),
                                                       # (change_screen_mission)]),
      # ("castle_cheat_town_walls",[(eq, "$cheat_mode", 1),(party_slot_eq,"$current_town",slot_party_type, spt_town),], "{!}CHEAT! Town Walls.",
       # [
         # (party_get_slot, ":scene", "$current_town", slot_town_walls),
         # (set_jump_mission,"mt_ai_training"),
         # (jump_to_scene,":scene"),
         # (change_screen_mission)]),

    ]
  ),
   (
    "castle_guard",mnf_scale_picture,
    "You approach the gate. The men on the walls watch you closely.",
    "none",
    [
        (call_script, "script_set_town_picture"),
    ],
    [
      ("request_shelter",[(party_slot_eq, "$g_encountered_party",slot_party_type, spt_castle),
                          (ge, "$g_encountered_party_relation", 0)],
       "Request entry to the castle.",
       [(party_get_slot, ":castle_lord", "$g_encountered_party", slot_town_lord),
        (try_begin),
          (lt, ":castle_lord", 0),
          (jump_to_menu, "mnu_castle_entry_granted"),
        (else_try),
          (call_script, "script_troop_get_player_relation", ":castle_lord"),
          (assign, ":castle_lord_relation", reg0),
          #(troop_get_slot, ":castle_lord_relation", ":castle_lord", slot_troop_player_relation),
          (try_begin),
            (gt, ":castle_lord_relation", -15),
            (jump_to_menu, "mnu_castle_entry_granted"),
          (else_try),
            (jump_to_menu, "mnu_castle_entry_denied"),
          (try_end),
        (try_end),
       ]),
      ("request_meeting_commander",[],
       "Request a meeting with someone.",
       [
          (jump_to_menu, "mnu_castle_meeting"),
       ]),
      ("guard_leave",[],
       "Leave.",
       [(change_screen_return,0)]),
    ]
  ),
  (
    "castle_entry_granted",mnf_scale_picture,
    "After a brief wait, the guards open the gates for you and allow your party inside.",
    "none",
    [
        (call_script, "script_set_town_picture"),
    ],
    [
      ("continue",[],
       "Continue...",
       [(jump_to_menu,"mnu_town")]),
    ]
  ),
  
  (
    "castle_entry_denied",mnf_scale_picture,
    "The lord of this castle has forbidden you from coming inside these walls,\
 and the guard sergeant informs you that his men will fire if you attempt to come any closer.",
    "none",
    [
        (call_script, "script_set_town_picture"),
    ],
    [
      ("continue",[],
       "Continue...",
       [(jump_to_menu,"mnu_castle_guard")]),
    ]
  ),
  
  #SB : restructue this to call new script
  # (
    # "castle_meeting",mnf_scale_picture,
    # "With whom do you want to meet?",
    # "none",
    # [
        # (assign, "$num_castle_meeting_troops", 0),
        # (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
          # (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          # (call_script, "script_get_troop_attached_party", ":troop_no"),
          # (eq, "$g_encountered_party", reg0),
          # (troop_set_slot, "trp_temp_array_a", "$num_castle_meeting_troops", ":troop_no"),
          # (val_add, "$num_castle_meeting_troops", 1),
        # (try_end),
        # (call_script, "script_set_town_picture"),
    # ],
    # [
      # ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 0),(troop_get_slot, ":troop_no", "trp_temp_array_a", 0),(str_store_troop_name, s5, ":troop_no")],
       # "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 0),(jump_to_menu,"mnu_castle_meeting_selected")]),
      # ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 1),(troop_get_slot, ":troop_no", "trp_temp_array_a", 1),(str_store_troop_name, s5, ":troop_no")],
       # "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 1),(jump_to_menu,"mnu_castle_meeting_selected")]),
      # ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 2),(troop_get_slot, ":troop_no", "trp_temp_array_a", 2),(str_store_troop_name, s5, ":troop_no")],
       # "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 2),(jump_to_menu,"mnu_castle_meeting_selected")]),
      # ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 3),(troop_get_slot, ":troop_no", "trp_temp_array_a", 3),(str_store_troop_name, s5, ":troop_no")],
       # "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 3),(jump_to_menu,"mnu_castle_meeting_selected")]),
      # ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 4),(troop_get_slot, ":troop_no", "trp_temp_array_a", 4),(str_store_troop_name, s5, ":troop_no")],
       # "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 4),(jump_to_menu,"mnu_castle_meeting_selected")]),
      # ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 5),(troop_get_slot, ":troop_no", "trp_temp_array_a", 5),(str_store_troop_name, s5, ":troop_no")],
       # "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 5),(jump_to_menu,"mnu_castle_meeting_selected")]),
      # ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 6),(troop_get_slot, ":troop_no", "trp_temp_array_a", 6),(str_store_troop_name, s5, ":troop_no")],
       # "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 6),(jump_to_menu,"mnu_castle_meeting_selected")]),
      # ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 7),(troop_get_slot, ":troop_no", "trp_temp_array_a", 7),(str_store_troop_name, s5, ":troop_no")],
       # "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 7),(jump_to_menu,"mnu_castle_meeting_selected")]),
      # ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 8),(troop_get_slot, ":troop_no", "trp_temp_array_a", 8),(str_store_troop_name, s5, ":troop_no")],
       # "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 8),(jump_to_menu,"mnu_castle_meeting_selected")]),
      # ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 9),(troop_get_slot, ":troop_no", "trp_temp_array_a", 9),(str_store_troop_name, s5, ":troop_no")],
       # "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 9),(jump_to_menu,"mnu_castle_meeting_selected")]),

      # ("forget_it",[],
       # "Forget it.",
       # [(jump_to_menu,"mnu_castle_guard")]),
    # ]
  # ),
  # (
    # "castle_meeting_selected",0,
    # "Your request for a meeting is relayed inside, and finally {s6} appears in the courtyard to speak with you.",
    # "none",
    # [(str_store_troop_name, s6, "$castle_meeting_selected_troop")],
    # [
      # ("continue",[],
       # "Continue...",
       # [(jump_to_menu, "mnu_castle_outside"),
        # (modify_visitors_at_site,"scn_conversation_scene"),(reset_visitors),
        # (set_visitor,0,"trp_player"),
        # (set_visitor,17,"$castle_meeting_selected_troop"),
        # (set_jump_mission,"mt_conversation_encounter"),
        # (jump_to_scene,"scn_conversation_scene"),
        # (assign, "$talk_context", tc_castle_gate),
        # (change_screen_map_conversation, "$castle_meeting_selected_troop"),
        # ]),
    # ]
  # ),
  (
    "castle_meeting",mnf_scale_picture,
    "With whom do you want to meet?",
    "none",
    [   (party_clear, "p_temp_party"),
        (call_script, "script_set_town_picture"),
        (call_script, "script_get_heroes_attached_to_center_aux", "$g_encountered_party", "p_temp_party"),#recursive call
        (party_get_num_companion_stacks, "$num_castle_meeting_troops", "p_temp_party"),
        (assign, "$talk_context", tc_castle_gate), #SB : move this up here
    ],
    [ ("guard_meet_"+str(x),[
        (gt, "$num_castle_meeting_troops", x),#test this out
        (party_stack_get_troop_id, ":troop_no", "p_temp_party", x),
        (is_between, ":troop_no", active_npcs_begin, active_npcs_end),
        (str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(party_stack_get_troop_id, "$castle_meeting_selected_troop", "p_temp_party", x),
       # (party_stack_get_troop_dna, "$temp_2", "p_temp_party", x),
       (jump_to_menu,"mnu_castle_meeting_selected")])
       for x in range(0, 8)
      ]

    +[("forget_it",[], "Forget it.", [(jump_to_menu,"mnu_castle_guard")]),]
  ),
  (
    "castle_meeting_selected",0,
    "Your request for a meeting is relayed inside, and finally {s6} appears in the courtyard to speak with you.",
    "none",
    [
    (try_begin),
		(eq, "$g_leave_encounter", 1),
		(change_screen_return),
	(try_end),

    (str_store_troop_name, s6, "$castle_meeting_selected_troop")],
    [
      ("continue",[],
       "Continue...",
       [(jump_to_menu, "mnu_castle_outside"),
        #do not set context here in case we need to use another one, set tc_castle_gate from parent menu
        (call_script, "script_start_courtyard_conversation", "$castle_meeting_selected_troop", "$current_town"),
        ]),
    ]
  ),

   ( #SB : pic hotkeys
    "castle_besiege",mnf_scale_picture|mnf_enable_hot_keys,
    "You are laying siege to {s1}. {s2} {s3}",
    "none",
    [
          ##diplomacy start+ test gender with script
        #(troop_get_type, ":is_female", "trp_player"),#<- replaced
        (try_begin),
          #(eq, ":is_female", 1),#<- replaced
          (eq, "$character_gender", tf_female),#<- added
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),
          ##diplomacy end+
        (assign, "$g_siege_force_wait", 0),
        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
          (party_set_slot, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
          (store_current_hours, ":cur_hours"),
          (party_set_slot, "$g_encountered_party", slot_center_siege_begin_hours, ":cur_hours"),
          (assign, "$g_siege_method", 0),
          (assign, "$g_siege_sallied_out_once", 0),
          #SB : also add sneak variables here
          (assign, "$last_sneak_attempt_town", "$g_encountered_party"),
          (assign, "$last_sneak_attempt_time", ":cur_hours"),
        (try_end),

        (party_get_slot, ":town_food_store", "$g_encountered_party", slot_party_food_store),
        (call_script, "script_center_get_food_consumption", "$g_encountered_party"),
        (assign, ":food_consumption", reg0),
        (assign, reg7, ":food_consumption"),
        (assign, reg8, ":town_food_store"),
        (store_div, reg3, ":town_food_store", ":food_consumption"),

        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (assign, reg6, 1),
        (else_try),
          (assign, reg6, 0),
        (try_end),

        (try_begin),
          (gt, reg3, 0),
          (str_store_string, s2, "@The {reg6?town's:castle's} food stores should last for {reg3} more days."),
        (else_try),
          (str_store_string, s2, "@The {reg6?town's:castle's} food stores have run out and the defenders are starving."),
        (try_end),

        (str_store_string, s3, "str_empty_string"),
        (try_begin),
          (ge, "$g_siege_method", 1),
          (store_current_hours, ":cur_hours"),
          (try_begin),
            (lt, ":cur_hours",  "$g_siege_method_finish_hours"),
            (store_sub, reg9, "$g_siege_method_finish_hours", ":cur_hours"),
            (try_begin),
              (eq, "$g_siege_method", 1),
              (str_store_string, s3, "@You're preparing to attack the walls, the work should finish in {reg9} hours."),
            (else_try),
              (eq, "$g_siege_method", 2),
              (str_store_string, s3, "@Your forces are building a siege tower. They estimate another {reg9} hours to complete construction."), #SB : "the build -> construction"
            (try_end),
          (else_try),
            (try_begin),
              (eq, "$g_siege_method", 1),
              (str_store_string, s3, "@You are ready to attack the walls at any time."),
            (else_try),
              (eq, "$g_siege_method", 2),
              (str_store_string, s3, "@The siege tower is built and ready to make an assault."),
            (try_end),
          (try_end),
        (try_end),

        #Check if enemy leaves the castle to us...
        (try_begin),
          (eq, "$g_castle_left_to_player",1), #we come here after dialog. Empty the castle and send parties away.
          (assign, "$g_castle_left_to_player",0),
          (store_faction_of_party, ":castle_faction", "$g_encountered_party"),
          (party_set_faction,"$g_encountered_party","fac_neutral"), #temporarily erase faction so that it is not the closest town
          (party_get_num_attached_parties, ":num_attached_parties_to_castle","$g_encountered_party"),
          (try_for_range_backwards, ":iap", 0, ":num_attached_parties_to_castle"),
            (party_get_attached_party_with_rank, ":attached_party", "$g_encountered_party", ":iap"),
            (party_detach, ":attached_party"),
            (party_get_slot, ":attached_party_type", ":attached_party", slot_party_type),
            (eq, ":attached_party_type", spt_kingdom_hero_party),
            (store_faction_of_party, ":attached_party_faction", ":attached_party"),
            (call_script, "script_get_closest_walled_center_of_faction", ":attached_party", ":attached_party_faction"),
            (try_begin),
              (gt, reg0, 0),
              (call_script, "script_party_set_ai_state", ":attached_party", spai_holding_center, reg0),
            (else_try),
              (call_script, "script_party_set_ai_state", ":attached_party", spai_patrolling_around_center, "$g_encountered_party"),
            (try_end),
          (try_end),
          (call_script, "script_party_remove_all_companions", "$g_encountered_party"),
          (change_screen_return),
          (party_collect_attachments_to_party, "$g_encountered_party", "p_collective_enemy"), #recalculate so that
          (call_script, "script_party_copy", "p_encountered_party_backup", "p_collective_enemy"), #leaving troops will not be considered as captured
          (party_set_faction,"$g_encountered_party",":castle_faction"),
        (try_end),

        #Check for victory or defeat....
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", -1),
        (str_store_party_name, 1,"$g_encountered_party"),
        (call_script, "script_encounter_calculate_fit"),

        (assign, reg11, "$g_enemy_fit_for_battle"),
        (assign, reg10, "$g_friend_fit_for_battle"),


        (try_begin),
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        ##diplomacy begin
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
          (call_script, "script_party_count_fit_regulars","p_collective_enemy"),
          (assign, ":enemy_finished", 0),
          (try_begin),
            (eq, "$g_battle_result", 1),
            (assign, ":enemy_finished", 1),
          (else_try),
            (le, "$g_enemy_fit_for_battle", 0),
            (ge, "$g_friend_fit_for_battle", 1),
            (assign, ":enemy_finished", 1),
          (try_end),
          (this_or_next|eq, ":enemy_finished", 1),
          (eq, "$g_enemy_surrenders", 1),
          (assign, "$g_next_menu", "mnu_dplmc_town_riot_removed"),
          (jump_to_menu, "mnu_total_victory"),
        ##diplomacy end
        (else_try),
          (call_script, "script_party_count_fit_regulars","p_collective_enemy"),
          (assign, ":enemy_finished", 0),
          (try_begin),
            (eq, "$g_battle_result", 1),
            (assign, ":enemy_finished", 1),
          (else_try),
            (le, "$g_enemy_fit_for_battle", 0),
            (ge, "$g_friend_fit_for_battle", 1),
            (assign, ":enemy_finished", 1),
          (try_end),
          (this_or_next|eq, ":enemy_finished", 1),
          (eq, "$g_enemy_surrenders", 1),

          (assign, "$g_next_menu", "mnu_castle_taken"),
          (jump_to_menu, "mnu_total_victory"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),
          (assign, ":main_party_fit_regulars", reg0),
          (eq, "$g_battle_result", -1),
          (eq, ":main_party_fit_regulars", 0), #all lost (TODO : )
          (assign, "$g_next_menu", "mnu_captivity_start_castle_defeat"),
          (jump_to_menu, "mnu_total_defeat"),
        (try_end),
    ],
    [
      ("siege_request_meeting",[(eq, "$cant_talk_to_enemy", 0)],"Call for a meeting with the castle commander.", [
          (assign, "$cant_talk_to_enemy", 1),
          (assign, "$g_enemy_surrenders",0),
          (assign, "$g_castle_left_to_player",0),
          (assign, "$talk_context", tc_castle_commander),
          (party_get_num_attached_parties, ":num_attached_parties_to_castle","$g_encountered_party"),
          #SB : use start_courtyard_conversation
          (try_begin),
            (gt, ":num_attached_parties_to_castle", 0),
            (party_get_attached_party_with_rank, ":leader_attached_party", "$g_encountered_party", 0),
            (party_stack_get_troop_id, ":leader",":leader_attached_party",0),
          (else_try),
            (party_stack_get_troop_id, ":leader","$g_encountered_party",0),
          (try_end),
          (call_script, "script_start_courtyard_conversation", ":leader", "$g_encountered_party"),
           ]),

      ("wait_24_hours",[],"Wait until tomorrow.", [
          (assign,"$auto_besiege_town","$g_encountered_party"),
          (assign, "$g_siege_force_wait", 1),
          (store_time_of_day,":cur_time_of_day"),
          (val_add, ":cur_time_of_day", 1),
          (assign, ":time_to_wait", 31),
          (val_sub,":time_to_wait",":cur_time_of_day"),
          (val_mod,":time_to_wait",24),
          (val_add, ":time_to_wait", 1),
          (rest_for_hours_interactive, ":time_to_wait", 5, 1), #rest while attackable
          (assign, "$cant_talk_to_enemy", 0),
          (change_screen_return),
          ]),


      ("castle_lead_attack",
       [
         (neg|troop_is_wounded, "trp_player"),
         (ge, "$g_siege_method", 1),
         (gt, "$g_friend_fit_for_battle", 3),
         (store_current_hours, ":cur_hours"),
         (ge, ":cur_hours", "$g_siege_method_finish_hours"),
       ],
       "Lead your soldiers in an assault.",
       [
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_walls),
           (else_try),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
           (try_end),

           (call_script, "script_calculate_renown_value"),
           (call_script, "script_calculate_battle_advantage"),
           (assign, ":battle_advantage", reg0),
           (val_mul, ":battle_advantage", 2),
           (val_div, ":battle_advantage", 3), #scale down the advantage a bit in sieges.
           (set_battle_advantage, ":battle_advantage"),
           (set_party_battle_mode),
           (assign, "$g_siege_battle_state", 1),
           (assign, ":siege_sally", 0),
           (try_begin),
             (le, ":battle_advantage", -4), #we are outnumbered, defenders sally out
             (eq, "$g_siege_sallied_out_once", 0),
             (set_jump_mission,"mt_castle_attack_walls_defenders_sally"),
             (assign, "$g_siege_battle_state", 0),
             (assign, ":siege_sally", 1),
           (else_try),
             (party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),
             (set_jump_mission,"mt_castle_attack_walls_belfry"),
           (else_try),
             (set_jump_mission,"mt_castle_attack_walls_ladder"),
           (try_end),
           (assign, "$cant_talk_to_enemy", 0),
           (assign, "$g_siege_final_menu", "mnu_castle_besiege"),
           (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
           (assign, "$g_siege_method", 0), #reset siege timer
           (jump_to_scene,":battle_scene"),
           (try_begin),
             (eq, ":siege_sally", 1),
             (jump_to_menu, "mnu_siege_attack_meets_sally"),
           (else_try),
             (jump_to_menu, "mnu_battle_debrief"),
             (change_screen_mission),
           (try_end),
       ]),
      ("attack_stay_back",
       [
         (ge, "$g_siege_method", 1),
         (gt, "$g_friend_fit_for_battle", 3),
         (store_current_hours, ":cur_hours"),
         (ge, ":cur_hours",  "$g_siege_method_finish_hours"),
         ],
       "Order your soldiers to attack while you stay back...", [(assign, "$cant_talk_to_enemy", 0),(jump_to_menu,"mnu_castle_attack_walls_simulate")]),

      ("build_ladders",[(party_slot_eq, "$current_town", slot_center_siege_with_belfry, 0),(eq, "$g_siege_method", 0)],
       "Prepare ladders to attack the walls.", [(jump_to_menu,"mnu_construct_ladders")]),

      ("build_siege_tower",[(party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),(eq, "$g_siege_method", 0)],
       "Build a siege tower.", [(jump_to_menu,"mnu_construct_siege_tower")]),
       
      ("siege_camp",[],"Walk around the siege camp.", #dckplmc
       [(set_jump_mission,"mt_camp"),
        (call_script, "script_setup_camp_scene"),
        (change_screen_mission),
        ]
       ),

      ("cheat_castle_lead_attack",[(eq, "$cheat_mode", 1),
                                   (eq, "$g_siege_method", 0)],
       "{!}CHEAT: Instant build equipments.",
       [
         (assign, "$g_siege_method", 1),
         (assign, "$g_siege_method_finish_hours", 0),
         (jump_to_menu, "mnu_castle_besiege"),
       ]),

      ("cheat_conquer_castle",[(eq, "$cheat_mode", 1),
                                   ],
       "{!}CHEAT: Instant conquer castle.",
       [
        (assign, "$g_next_menu", "mnu_castle_taken"),
        (jump_to_menu, "mnu_total_victory"),
       ]),

      ("lift_siege",[],"Abandon the siege.",
       [
         (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
         (assign,"$g_player_besiege_town", -1),
         (change_screen_return)]),
    ]
  ),

  (
    "siege_attack_meets_sally",mnf_scale_picture,
    "The defenders sally out to meet your assault.",
    "none",
    [
        (set_background_mesh, "mesh_pic_sally_out"),
    ],
    [
      ("continue",[],
       "Continue...",
       [
             (jump_to_menu, "mnu_battle_debrief"),
             (change_screen_mission),
       ]),
    ]
  ),

   (
    "castle_besiege_inner_battle",mnf_scale_picture,
    "{s1}",
    "none",
    [
		  # ##diplomacy start+ test gender with script
        # #(troop_get_type, ":is_female", "trp_player"),#<- replaced
        # (try_begin),
          # #(eq, ":is_female", 1),#<- replaced
		  # (eq, "$character_gender", tf_female),#<- added
          # (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        # (else_try),
          # (set_background_mesh, "mesh_pic_siege_sighted"),
        # (try_end),
		  # ##diplomacy end+
        #SB : sally picture more appropriate
        (set_background_mesh, "mesh_pic_sally_out"),
        (assign, ":result", "$g_battle_result"),#will be reset at script_encounter_calculate_fit
        (call_script, "script_encounter_calculate_fit"),

# TODO: To use for the future:
        (try_begin),
          (this_or_next|neq, ":result", 1),
          (this_or_next|le, "$g_friend_fit_for_battle", 0),
          (le, "$g_enemy_fit_for_battle", 0),
          (jump_to_menu, "$g_siege_final_menu"),
        (else_try),
          (call_script, "script_encounter_calculate_fit"),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (try_begin),
            (eq, "$g_siege_battle_state", 0),
            (eq, ":result", 1),
            (assign, "$g_battle_result", 0),
            (jump_to_menu, "$g_siege_final_menu"),
          (else_try),
            (eq, "$g_siege_battle_state", 1),
            (eq, ":result", 1),
            (try_begin), #SB : siege strings
              (eq, "$g_ally_party", "$g_encountered_party"),
              (str_store_string, s1, "@You've been driven away from the walls.\
 Now the attackers are pouring into the streets. If you can defeat them, you can perhaps turn the tide and save the day."),
            (else_try),
              (str_store_string, s1, "@You've breached the town walls,\
 but the stubborn defenders continue to resist you in the streets!\
 You'll have to deal with them before you can attack the keep at the heart of the town."),
            (try_end),
          (else_try),
            (eq, "$g_siege_battle_state", 2),
            (eq, ":result", 1),
            (try_begin), #SB : siege strings
              (eq, "$g_ally_party", "$g_encountered_party"),
              (str_store_string, s1, "@As a last defensive effort, you retreat to the main hall of the keep.\
 You and your remaining soldiers will put up a desperate fight here. If you are defeated, there's no other place to fall back to."),
            (else_try),
              (str_store_string, s1, "@The town centre is yours,\
 but the remaining defenders have retreated to the castle.\
 It must fall before you can complete your victory."),
            (try_end),
          (else_try),
            (jump_to_menu, "$g_siege_final_menu"),
          (try_end),
        (else_try),
          (try_begin),
            (eq, "$g_siege_battle_state", 0),
            (eq, ":result", 1),
            (assign, "$g_battle_result", 0),
            (jump_to_menu, "$g_siege_final_menu"),
          (else_try),
            (eq, "$g_siege_battle_state", 1),
            (eq, ":result", 1),
            (str_store_string, s1, "@The remaining defenders have retreated to the castle as a last defense. You must go in and crush any remaining resistance."),
          (else_try),
            (jump_to_menu, "$g_siege_final_menu"),
          (try_end),
        (try_end),
    ],
    [
      ("continue",[],
       "Continue...",
       [
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (try_begin),
               (eq, "$g_siege_battle_state", 1),
               (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_center),
               (set_jump_mission, "mt_besiege_inner_battle_town_center"),
             (else_try),
               (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_castle),
               (set_jump_mission, "mt_besiege_inner_battle_castle"),
             (try_end),
           (else_try),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_castle),
             (set_jump_mission, "mt_besiege_inner_battle_castle"),
           (try_end),
##           (call_script, "script_calculate_battle_advantage"),
##           (set_battle_advantage, reg0),
           (set_party_battle_mode),
           (jump_to_scene, ":battle_scene"),
           (val_add, "$g_siege_battle_state", 1),
           (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
           (jump_to_menu, "mnu_battle_debrief"),
           (change_screen_mission),
       ]),
    ]
  ),


  (
    "construct_ladders",0,
    "As the party member with the highest Engineer skill ({reg2}), {reg3?you estimate:{s3} estimates} that it will take\
 {reg4} hours to build enough scaling ladders for the assault.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),

     (store_sub, reg4, 14, ":max_skill"),
     (val_mul, reg4, 2),
     (val_div, reg4, 3),

     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
     
    #SB : add tableau
    (set_fixed_point_multiplier, 100),
    (position_set_x, pos0, 70),
    (position_set_y, pos0, 5),
    (position_set_z, pos0, 75),
    (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", ":max_skill_owner", pos0),
    ],
    [
      ("build_ladders_cont",[],
       "Do it.", [
           (assign, "$g_siege_method", 1),
           (store_current_hours, ":cur_hours"),
           (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
           (store_sub, ":hours_takes", 14, reg0),
           (val_mul, ":hours_takes", 2),
           (val_div, ":hours_takes", 3),
           (store_add, "$g_siege_method_finish_hours",":cur_hours", ":hours_takes"),
           (assign,"$auto_besiege_town","$current_town"),
           (rest_for_hours_interactive, 96, 5, 1), #rest while attackable. A trigger will divert control when attack is ready.
           (change_screen_return),
           ]),
      ("go_back",[],
       "Go back.", [(jump_to_menu,"mnu_castle_besiege")]),
        ],
  ),


  (
    "construct_siege_tower",0,
    "As the party member with the highest Engineer skill ({reg2}), {reg3?you estimate:{s3} estimates} that building a siege tower will take\
 {reg4} hours.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),

     (store_sub, reg4, 15, ":max_skill"),
     (val_mul, reg4, 6),

     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
     
    #SB : add tableau
    (set_fixed_point_multiplier, 100),
    (position_set_x, pos0, 70),
    (position_set_y, pos0, 5),
    (position_set_z, pos0, 75),
    (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", ":max_skill_owner", pos0),
    ],
    [
      ("build_siege_tower_cont",[],
       "Start building.", [
           (assign, "$g_siege_method", 2),
           (store_current_hours, ":cur_hours"),
           (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
           (store_sub, ":hours_takes", 15, reg0),
           (val_mul, ":hours_takes", 6),
           (store_add, "$g_siege_method_finish_hours",":cur_hours", ":hours_takes"),
           (assign,"$auto_besiege_town","$current_town"),
           (rest_for_hours_interactive, 240, 5, 1), #rest while attackable. A trigger will divert control when attack is ready.
           (change_screen_return),
           ]),
      ("go_back",[],
       "Go back.", [(jump_to_menu,"mnu_castle_besiege")]),
        ],
  ),

   (
    "castle_attack_walls_simulate",mnf_scale_picture|mnf_disable_all_keys,
    "{s4}^^Your casualties:{s8}^^Enemy casualties were: {s9}",
    "none",
    [
        (try_begin),
          (set_background_mesh, "mesh_pic_siege_attack"),
        (try_end),
        ###diplomacy start+
		##If terrain advantage is on, use siege settings
        #(assign, ":save_dplmc_terrain_advantage", "$g_dplmc_terrain_advantage"),
		##(assign, "$g_dplmc_terrain_advantage", ":save_dplmc_terrain_advantage"),
		#(try_begin),
		#   (eq, "$g_dplmc_terrain_advantage", TERRAIN_ADVANTAGE_ENABLE),
		#   (assign, "$g_dplmc_terrain_advantage", TERRAIN_ADVANTAGE_FORCE_SIEGE),
		#(try_end),
		###diplomacy end+
        (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
        (assign, ":player_party_strength", reg0),
        (val_div, ":player_party_strength", 10),

        (call_script, "script_party_calculate_strength", "$g_encountered_party", 0),
        (assign, ":enemy_party_strength", reg0),
        (val_div, ":enemy_party_strength", 4),

        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s8, s0),

        (inflict_casualties_to_party_group, "$g_encountered_party", ":player_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s9, s0),

        (assign, "$no_soldiers_left", 0),
        (try_begin),
          (call_script, "script_party_count_members_with_full_health","p_main_party"),
          (le, reg0, 0), #(TODO : compare with num_routed_us)
          (assign, "$no_soldiers_left", 1),
          (str_store_string, s4, "str_attack_walls_failure"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health","$g_encountered_party"),
          (le, reg0, 0), #(TODO : compare with num_routed_enemies)
          (assign, "$no_soldiers_left", 1),
          (assign, "$g_battle_result", 1),
          (str_store_string, s4, "str_attack_walls_success"),
        (else_try),
          (str_store_string, s4, "str_attack_walls_continue"),
        (try_end),
		##diplomacy start+
		#Revert terrain advantage settings
		#(assign, "$g_dplmc_terrain_advantage", ":save_dplmc_terrain_advantage"),
		##diplomacy end+
     ],
    [
##      ("lead_next_wave",[(eq, "$no_soldiers_left", 0)],"Lead the next wave of attack personally.", [
##           (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
##           (set_party_battle_mode),
##           (set_jump_mission,"mt_castle_attack_walls"),
##           (jump_to_scene,":battle_scene"),
##           (jump_to_menu,"mnu_castle_outside"),
##           (change_screen_mission),
##       ]),
##      ("continue_attacking",[(eq, "$no_soldiers_left", 0)],"Order your soldiers to keep attacking...", [
##                                    (jump_to_menu,"mnu_castle_attack_walls_3"),
##                                    ]),
##      ("call_soldiers_back",[(eq, "$no_soldiers_left", 0)],"Call your soldiers back.",[(jump_to_menu,"mnu_castle_outside")]),
      ("continue",[],"Continue...",[(jump_to_menu,"mnu_castle_besiege")]),
    ]
  ),

   (
    "castle_attack_walls_with_allies_simulate",mnf_scale_picture|mnf_disable_all_keys,
    "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
    "none",
    [
        (try_begin),
          (set_background_mesh, "mesh_pic_siege_attack"),
        (try_end),
        ###diplomacy start+
		##If terrain advantage is on, use siege settings
        #(assign, ":save_dplmc_terrain_advantage", "$g_dplmc_terrain_advantage"),
		#(try_begin),
		#   (eq, "$g_dplmc_terrain_advantage", TERRAIN_ADVANTAGE_ENABLE),
		#   (assign, "$g_dplmc_terrain_advantage", TERRAIN_ADVANTAGE_FORCE_SIEGE),
		#(try_end),
		###diplomacy end+
        (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
        (assign, ":player_party_strength", reg0),
        (val_div, ":player_party_strength", 10),
        (call_script, "script_party_calculate_strength", "p_collective_friends", 0),
        (assign, ":friend_party_strength", reg0),
        (val_div, ":friend_party_strength", 10),

        (val_max, ":friend_party_strength", 1),

        (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
        (assign, ":enemy_party_strength", reg0),
        (val_div, ":enemy_party_strength", 4),

##        (assign, reg0, ":player_party_strength"),
##        (assign, reg1, ":friend_party_strength"),
##        (assign, reg2, ":enemy_party_strength"),
##        (assign, reg3, "$g_enemy_party"),
##        (assign, reg4, "$g_ally_party"),
##        (display_message, "@{!}player_str={reg0} friend_str={reg1} enemy_str={reg2}"),
##        (display_message, "@{!}enemy_party={reg3} ally_party={reg4}"),

        (try_begin),
          (eq, ":friend_party_strength", 0),
          (store_div, ":enemy_party_strength_for_p", ":enemy_party_strength", 2),
        (else_try),
          (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
          (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
          (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),
        (try_end),

        (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),
        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s8, s0),

        (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s10, s0),

        (call_script, "script_collect_friendly_parties"),

        (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s9, s0),

        (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),

        (assign, "$no_soldiers_left", 0),
        (try_begin),
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),
          (le, reg0, 0), #(TODO : compare with num_routed_us)
          (assign, "$no_soldiers_left", 1),
          (str_store_string, s4, "str_attack_walls_failure"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
          (le, reg0, 0), #(TODO : compare with num_routed_enemies)
          (assign, "$no_soldiers_left", 1),
          (assign, "$g_battle_result", 1),
          (str_store_string, s4, "str_attack_walls_success"),
        (else_try),
          (str_store_string, s4, "str_attack_walls_continue"),
        (try_end),
		###diplomacy start+
		##Revert terrain advantage settings
		#(assign, "$g_dplmc_terrain_advantage", ":save_dplmc_terrain_advantage"),
		###diplomacy end+
     ],
    [
      ("continue",[],"Continue...",[(jump_to_menu,"mnu_besiegers_camp_with_allies")]),
    ]
  ),

  (
    "castle_taken_by_friends",0,
    "Nothing to see here.",
    "none",
    [
        (party_clear, "$g_encountered_party"),
        (party_stack_get_troop_id, ":leader", "$g_encountered_party_2", 0),
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, ":leader"),
        (store_troop_faction, ":faction_no", ":leader"),
        #Reduce prosperity of the center by 5
        (call_script, "script_change_center_prosperity", "$g_encountered_party", -5),
		(try_begin),
			(assign, ":damage", 20),
			(is_between, "$g_encountered_party", towns_begin, towns_end),
			(assign, ":damage", 40),
		(try_end),
		(try_begin),
			(neq, ":faction_no", "$g_encountered_party_faction"),
			(call_script, "script_faction_inflict_war_damage_on_faction", ":faction_no", "$g_encountered_party_faction", ":damage"),
		(try_end),

        (call_script, "script_give_center_to_faction", "$g_encountered_party", ":faction_no"),
        (call_script, "script_add_log_entry", logent_player_participated_in_siege, "trp_player",  "$g_encountered_party", 0, "$g_encountered_party_faction"),
##        (call_script, "script_change_troop_renown", "trp_player", 1),
        (change_screen_return),
    ],
    [
    ],
  ),


  (
    "castle_taken",mnf_disable_all_keys,
  ##diplomacy begin
    "{s3} has fallen to your troops, and you now have full control of the {reg2?town:castle}. You can plunder spoils of war worth {reg3} denars.\
{reg1? You may station troops here to defend it against enemies who may try to recapture it. Also, you should select now whether you will hold the {reg2?town:castle} yourself or give it to a faithful vassal...:}",# Only visible when castle is taken without being a vassal of a kingdom.
  ##diplomacy end
    "none",
    [
        (party_clear, "$g_encountered_party"),
        #SB : clear talk_context
        (try_begin),
          (eq, "$talk_context", tc_give_center_to_fief),
          (assign, "$talk_context", tc_town_talk),
        (try_end),
        ##diplomacy start+ Handle player is co-ruler of kingdom
        (assign, ":is_coruler", 0),
        (try_begin),
            (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
            (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
            (ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
            (assign, ":is_coruler", 1),
        (try_end),
        ##diplomacy end+
        (try_begin),
          ##diplomacy start+
          (this_or_next|eq, ":is_coruler", 1),
          ##diplomacy end+
          (eq, "$players_kingdom", "fac_player_supporters_faction"),
          (party_get_slot, ":new_owner", "$g_encountered_party", slot_town_lord),
          (neq, ":new_owner", "trp_player"),

          (try_for_range, ":unused", 0, 4),
            (call_script, "script_cf_reinforce_party", "$g_encountered_party"),
          (try_end),
        (try_end),

        (call_script, "script_lift_siege", "$g_encountered_party", 0),
        (assign, "$g_player_besiege_town", -1),

        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
        ##diplomacy start+ Set last taken time
        (store_current_hours, ":cur_hours"),
        (party_set_slot, "$g_encountered_party", dplmc_slot_center_last_transfer_time, ":cur_hours"),
        ##diplomacy end+
        ##diplomacy begin
        #Reduce prosperity of the center by 5
        #(call_script, "script_change_center_prosperity", "$g_encountered_party", -5),
         (try_begin),
             (is_between, "$g_encountered_party", towns_begin, towns_end),
             (store_random_in_range, ":random", 4000, 10000),
         (else_try),
           (store_random_in_range, ":random", 1000, 8000),
         (try_end),
         (val_div, ":random", 100),
         (val_mul, ":random", 100),
         (assign, "$diplomacy_var", ":random"),
         # (assign, reg3, "$diplomacy_var"), #SB : move variable to last place
        ##diplomacy end

        (call_script, "script_change_troop_renown", "trp_player", 5),

        (assign, ":damage", 20),
        (try_begin),
            (is_between, "$g_encountered_party", towns_begin, towns_end),
            (assign, ":damage", 40),
        (try_end),
        (call_script, "script_faction_inflict_war_damage_on_faction", "$players_kingdom", "$g_encountered_party_faction", ":damage"),

        #removed, is it duplicate (useless)? See 20 lines above.
        #(call_script, "script_add_log_entry", logent_castle_captured_by_player, "trp_player", "$g_encountered_party", -1, "$g_encountered_party_faction"),

        (try_begin),
          (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
          (neq, "$players_kingdom", "fac_player_supporters_faction"),
          (call_script, "script_give_center_to_faction", "$g_encountered_party", "$players_kingdom"),
          (call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "$players_kingdom"),
          (jump_to_menu, "mnu_castle_taken_2"),
        (else_try),
          (call_script, "script_give_center_to_faction", "$g_encountered_party", "fac_player_supporters_faction"),
          (call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "fac_player_supporters_faction"),
          (str_store_party_name, s3, "$g_encountered_party"),
          (assign, reg1, 0),
          (try_begin),
            (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
            (assign, reg1, 1),
          (try_end),
        #(party_set_slot, "$g_encountered_party", slot_town_lord, stl_unassigned),
        (try_end),
        (assign, reg2, 0),
        (try_begin),
          (is_between, "$g_encountered_party", towns_begin, towns_end),
          (assign, reg2, 1),
        (try_end),
        (assign, reg3, "$diplomacy_var"), #SB : registers last
    ],
    [
##diplomacy begin
      ("dplmc_spoils_yourself",[],"Plunder it and keep the spoils all for yourself.",
       [
         #SB : spawn some looters
         (call_script, "script_spawn_looters", "$g_encountered_party", 4),
         (call_script, "script_change_center_prosperity", "$g_encountered_party", -8),
		 ##diplomacy start+
		 (assign, ":is_kingdom_leader", 0),
		 (try_begin),
			(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
			(faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
			(ge, ":faction_leader", 0),
			(this_or_next|eq, ":faction_leader", "trp_player"),
			(this_or_next|troop_slot_eq, ":faction_leader", slot_troop_spouse, "trp_player"),
				(troop_slot_eq, "trp_player", slot_troop_spouse, ":faction_leader"),
			(assign, ":is_kingdom_leader", 1),
		 (else_try),
			(eq, "$players_kingdom", "fac_player_supporters_faction"),
			(assign, ":is_kingdom_leader", 1),
		 (try_end),
		 #Add support for promoted ladies
         #(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
         (try_for_range, ":troop_no", heroes_begin, heroes_end),
		 ##diplomacy end+
           (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
           (store_troop_faction, ":troop_faction_no", ":troop_no"),
		   ##diplomacy start+
		   (this_or_next|eq, "$players_kingdom", ":troop_faction_no"),
			  (eq, "fac_player_supporters_faction", ":troop_faction_no"),
		   (this_or_next|eq, ":is_kingdom_leader", 1),
		   ##diplomacy end+
           (eq, "fac_player_supporters_faction", ":troop_faction_no"),
           (call_script, "script_change_player_relation_with_troop", ":troop_no", -2),
         (try_end),
         (try_begin),
           (gt, "$g_player_chamberlain", 0),
           (call_script, "script_dplmc_pay_into_treasury", "$diplomacy_var"),
         (else_try),
           (troop_add_gold, "trp_player", "$diplomacy_var"),
         (try_end),
         (call_script, "script_change_player_honor", -3),
         (assign, "$auto_enter_town", "$g_encountered_party"),
         (change_screen_return),
        ]),
      ("dplmc_spoils_accompanying_vassals",
      [
		##nested diplomacy start+
		#Add support for being the ruler or co-ruler of an original kingdom
          (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
		  (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
		  (this_or_next|eq, ":faction_leader", "trp_player"),
		  (this_or_next|troop_slot_eq, ":faction_leader", slot_troop_spouse, "trp_player"),
  		##nested diplomacy end+
          (eq, "$players_kingdom", "fac_player_supporters_faction"),
          (assign, ":vassal_count", 0),
		##nested diplomacy start+ add support for kingdom ladies, and the other faction options
        # (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
		 (try_for_range, ":troop_no", heroes_begin, heroes_end),
  	    ##nested diplmacy end+
           (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
           (store_troop_faction, ":troop_faction_no", ":troop_no"),
		   ##nested diplomacy start+
		   (this_or_next|eq, "$players_kingdom", ":troop_faction_no"),
		   ##nested diplomacy end+
           (eq, "fac_player_supporters_faction", ":troop_faction_no"),
           (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
           (ge, ":party_no", 1),
           (store_distance_to_party_from_party, ":distance","p_main_party", ":party_no"),
           (le, ":distance", 25),
           (val_add, ":vassal_count", 1),
         (try_end),
		 (gt, ":vassal_count", 0),
      ],"Plunder it and share the spoils equally between the vassals accompanying you and yourself.",
       [
         (assign, ":vassal_count", 1),
		 ##nested diplomacy start+
		 ##OLD:
         #(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
         #  (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
         #  (store_troop_faction, ":troop_faction_no", ":troop_no"),
         #  (eq, "fac_player_supporters_faction", ":troop_faction_no"),
         #  (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
         #  (ge, ":party_no", 1),
         #  (store_distance_to_party_from_party, ":distance","p_main_party", ":party_no"),
         #  (le, ":distance", 25),
         #  (val_add, ":vassal_count", 1),
         #  (call_script, "script_change_player_relation_with_troop", ":troop_no", 3),
         #(try_end),
		 #
		 #NEW:
		 #first loop through to count
		 (try_for_range, ":troop_no", heroes_begin, heroes_end),#promoted lady support
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(store_troop_faction, ":troop_faction_no", ":troop_no"),
			(this_or_next|eq, "$players_kingdom", ":troop_faction_no"),#support for other faction arrangements
				(eq, "fac_player_supporters_faction", ":troop_faction_no"),
			(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
			(ge, ":party_no", 1),
			(store_distance_to_party_from_party, ":distance","p_main_party", ":party_no"),
			(le, ":distance", 25),
			(val_add, ":vassal_count", 1),
		 (try_end),
		 (store_div, ":gold_per_lord", "$diplomacy_var", ":vassal_count"),
		 #now loop through to add gold/relation
		 (try_for_range, ":troop_no", heroes_begin, heroes_end),#promoted lady support
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(store_troop_faction, ":troop_faction_no", ":troop_no"),
			(this_or_next|eq, "$players_kingdom", ":troop_faction_no"),#support for other faction arrangements
				(eq, "fac_player_supporters_faction", ":troop_faction_no"),
			(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
			(ge, ":party_no", 1),
			(store_distance_to_party_from_party, ":distance","p_main_party", ":party_no"),
			(le, ":distance", 25),
			#add gold
			(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", ":gold_per_lord", ":troop_no"),
			#Relation adjustment
			(store_random_in_range, reg0, 0, 1000),
			(val_add, reg0, ":gold_per_lord"),
			(val_div, reg0, 1000),
			(gt, reg0, 0),
			(val_min, reg0, 4),
			(assign, ":relation_change", reg0),
			#Modify for personality
			(try_begin),
				#Lords who dislike raiding will be displeased by looting a town (but not a castle)
				(party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
				(call_script, "script_dplmc_get_troop_morality_value", ":troop_no", tmt_humanitarian),
				(try_begin),
					(gt, reg0, 0),#Some lords like raiding settlements less than others
					(val_sub, ":relation_change", reg0),
					(val_min, ":relation_change", -1),
				(else_try),
					(lt, reg0, 0),#Some lords like raiding settlements more than others
					(val_sub, ":relation_change", reg0),
					(val_min, ":relation_change", 5),
				(else_try),
					(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_custodian),
					(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_benefactor),
						(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_moralist),
					(val_sub, ":relation_change", 1),
			    (try_end),
			(try_end),
			(call_script, "script_change_player_relation_with_troop", ":troop_no", ":relation_change"),
		 (try_end),
		 ##nested diplomacy end+
         # (store_random_in_range, ":num_looters", 0, ":vassal_count"),
         # (val_max, ":num_looters", 3),
         (call_script, "script_spawn_looters", "$g_encountered_party", 5), #SB : spawn some looters
         (val_div, "$diplomacy_var", ":vassal_count"),
         (try_begin),
           (gt, "$g_player_chamberlain", 0),
           (call_script, "script_dplmc_pay_into_treasury", "$diplomacy_var"),
         (else_try),
           (troop_add_gold, "trp_player", "$diplomacy_var"),
         (try_end),
         (call_script, "script_change_center_prosperity", "$g_encountered_party", -8),
         (call_script, "script_change_player_honor", -1),
         (assign, "$auto_enter_town", "$g_encountered_party"),
         (change_screen_return),
        ]),
      ("dplmc_spoils_all_vassals",
        [
          (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
          ##nested diplomacy start+
          #Support for being co-ruler of an original kingdom
          (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
          (this_or_next|eq, ":faction_leader", "trp_player"),
          (this_or_next|troop_slot_eq, ":faction_leader", slot_troop_spouse, "trp_player"),
          ##nested diplomacy end+
          (eq, "$players_kingdom", "fac_player_supporters_faction"),
          #SB : check if we even have any vassals
          (assign, ":end", heroes_end),
          (try_for_range, ":troop_no", heroes_begin, ":end"),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
            (store_troop_faction, ":troop_faction_no", ":troop_no"),
            (this_or_next|eq, ":troop_faction_no", "fac_player_supporters_faction"),
            (eq, ":troop_faction_no", "$players_kingdom"),
            (assign, ":end", heroes_begin),
          (try_end),
          (eq, ":end", heroes_begin),
          
      ],"Plunder it and share the spoils equally between your vassals and yourself.",
       [
         (assign, ":vassal_count", 1),
		 ##nested diplomacy start+
		 #OLD:
         #(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
         #  (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
         #  (store_troop_faction, ":troop_faction_no", ":troop_no"),
         #  (eq, "fac_player_supporters_faction", ":troop_faction_no"),
         #  (val_add, ":vassal_count", 1),
         #  (call_script, "script_change_player_relation_with_troop", ":troop_no", 2),
         #(try_end),
		 #
		 #NEW:
		 #  1. Actually give the gold to your vassals;
		 #  2. Support kingdom ladies as vassals
		 #  3. Support being the ruler or co-ruler of an original kingdom
		 #  4. The relationship gain should not exceed 1 per 1000 gold pieces.
		 (try_for_range, ":troop_no", heroes_begin, heroes_end),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(store_troop_faction, ":troop_faction_no", ":troop_no"),
			(this_or_next|eq, ":troop_faction_no", "fac_player_supporters_faction"),
				(eq, ":troop_faction_no", "$players_kingdom"),
			(val_add, ":vassal_count", 1),
		 (try_end),

		 (store_div, ":gold_per_lord", "$diplomacy_var", ":vassal_count"),
		 (try_for_range, ":troop_no", heroes_begin, heroes_end),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(store_troop_faction, ":troop_faction_no", ":troop_no"),
			(this_or_next|eq, ":troop_faction_no", "fac_player_supporters_faction"),
				(eq, ":troop_faction_no", "$players_kingdom"),
			(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", ":gold_per_lord", ":troop_no"),
			#Relation adjustment
			(store_random_in_range, reg0, 0, 1000),
			(val_add, reg0, ":gold_per_lord"),
			(val_div, reg0, 1000),
			(gt, reg0, 0),
			(val_min, reg0, 3),
			(assign, ":relation_change", reg0),
			#Modify for personality
			(try_begin),
				#Lords who dislike raiding will be displeased by looting a town (but not a castle)
				(party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
				(call_script, "script_dplmc_get_troop_morality_value", ":troop_no", tmt_humanitarian),
				(try_begin),
					(gt, reg0, 0),#Some lords like raiding settlements less than others
					(val_sub, ":relation_change", reg0),
					(val_min, ":relation_change", -1),
				(else_try),
					(lt, reg0, 0),#Some lords like raiding settlements more than others
					(val_sub, ":relation_change", reg0),
					(val_min, ":relation_change", 4),
				(else_try),
					(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_custodian),
					(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_benefactor),
						(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_moralist),
					(val_sub, ":relation_change", 1),
			    (try_end),
			(call_script, "script_change_player_relation_with_troop", ":troop_no", ":relation_change"),
 		    (try_end),
		 (try_end),
		 ##nested diplomacy end+
         (call_script, "script_spawn_looters", "$g_encountered_party", 4), #SB : spawn some looters
         (val_div, "$diplomacy_var", ":vassal_count"),
         (try_begin),
           (gt, "$g_player_chamberlain", 0),
           (call_script, "script_dplmc_pay_into_treasury", "$diplomacy_var"),
         (else_try),
           (troop_add_gold, "trp_player", "$diplomacy_var"),
         (try_end),
         (call_script, "script_change_center_prosperity", "$g_encountered_party", -8),
         (assign, "$auto_enter_town", "$g_encountered_party"),
         (change_screen_return),
        ]),
##diplomacy end
      ("continue",[],"Continue...",
       [
         ##diplomacy begin
         (call_script, "script_change_center_prosperity", "$g_encountered_party", -3),
         ##diplomacy end
         (assign, "$auto_enter_town", "$g_encountered_party"),
         (change_screen_return),
        ]),
    ],
  ),
  (
    "castle_taken_2",mnf_disable_all_keys,
    "{s3} has fallen to your troops, and you now have full control of the castle.\
 It is time to send word to {s9} about your victory. {s5}",
    "none",
    [
        (str_store_party_name, s3, "$g_encountered_party"),
        (str_clear, s5),
        (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
        (str_store_troop_name, s9, ":faction_leader"),
        (try_begin),
          (eq, "$player_has_homage", 0),
          (assign, reg8, 0),
          (try_begin),
		    ##diplomacy start+ FIX: Inserted missing argument
            #(party_slot_eq, "$g_encountered_party", spt_town),
			(party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
			##diplomacy end+
            (assign, reg8, 1),
          (try_end),
          ##diplomacy start+ fix gender of pronoun
          (call_script, "script_dplmc_store_troop_is_female", ":faction_leader"),
          (str_store_string, s5, "@However, since you are not a sworn {man/follower} of {s9}, there is no chance {reg0?she:he} would recognize you as the {lord/lady} of this {reg8?town:castle}."),
          ##diplomacy end+
        (try_end),
    ],
    [
        ("castle_taken_claim",[(eq, "$player_has_homage", 1)],
		"Request that {s3} be awarded to you.",
        [
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
        (assign, "$g_castle_requested_by_player", "$current_town"),
		(assign, "$g_castle_requested_for_troop", "trp_player"),
        (assign, "$auto_enter_town", "$g_encountered_party"),
        (change_screen_return),
        ]),

		("castle_taken_claim_2",[
		(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
		(is_between, ":spouse", active_npcs_begin, active_npcs_end),
		(troop_slot_eq, ":spouse", slot_troop_occupation, slto_kingdom_hero),
		(store_faction_of_troop, ":spouse_faction", ":spouse"),
		(eq, ":spouse_faction", "$players_kingdom"),
		],
		"Request that {s3} be awarded to your {wife/husband}.",
        [
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
        (assign, "$g_castle_requested_by_player", "$current_town"),
		(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
		(assign, "$g_castle_requested_for_troop", ":spouse"),
        (assign, "$auto_enter_town", "$g_encountered_party"),
        (change_screen_return),
        ]),



      ("castle_taken_no_claim",[],"Ask no rewards.",
       [
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, -1),
        (assign, "$auto_enter_town", "$g_encountered_party"),
        (change_screen_return),
#        (jump_to_menu, "mnu_town"),
        ]),
    ],
  ),

(
    "requested_castle_granted_to_player",mnf_scale_picture,
    "You receive a message from your liege, {s3}.^^\
 {reg4?She:He} has decided to grant {s2}{reg3? and the nearby village of {s4}:} to you, with all due incomes and titles, to hold in {reg4?her:his} name for as long as you maintain your oath of homage..",
    "none",
    [
		(set_background_mesh, "mesh_pic_messenger"),
		(faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
		(str_store_troop_name, s3, ":faction_leader"),
		(str_store_party_name, s2, "$g_center_to_give_to_player"),
		(try_begin),
			(party_slot_eq, "$g_center_to_give_to_player", slot_party_type, spt_castle),
			(assign, reg3, 1),
			(try_for_range, ":cur_village", villages_begin, villages_end),
				(party_slot_eq, ":cur_village", slot_village_bound_center, "$g_center_to_give_to_player"),
				(str_store_party_name, s4, ":cur_village"),
			(try_end),
		(else_try),
			(assign, reg3, 0),
		(try_end),
		##diplomacy start+ use script for gender
		#(troop_get_type, reg4, ":faction_leader"),#<- OLD
		(call_script, "script_dplmc_store_troop_is_female_reg", ":faction_leader", 4),
		##diplomacy end+
   ],
    [
		("continue",[],"Continue.",
			[
			(call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
			(jump_to_menu, "mnu_give_center_to_player_2"),
			],
		),
	]
),



(
    "requested_castle_granted_to_player_husband", mnf_scale_picture,
    "You receive a message from your liege, {s3}.^^\
 {reg4?She:He} has decided to grant {s2}{reg3? and the nearby village of {s4}:} to your husband, {s7}.",
    "none",
    [
		(set_background_mesh, "mesh_pic_messenger"),
		(faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
		(str_store_troop_name, s3, ":faction_leader"),
		(str_store_party_name, s2, "$g_center_to_give_to_player"),
		(try_begin),
			(party_slot_eq, "$g_center_to_give_to_player", slot_party_type, spt_castle),
			(assign, reg3, 1),
			(try_for_range, ":cur_village", villages_begin, villages_end),
				(party_slot_eq, ":cur_village", slot_village_bound_center, "$g_center_to_give_to_player"),
				(str_store_party_name, s4, ":cur_village"),
			(try_end),
		(else_try),
			(assign, reg3, 0),
		(try_end),
		##diplomacy start+ use script for gender
		#(troop_get_type, reg4, ":faction_leader"),#<- OLD
		(call_script, "script_dplmc_store_troop_is_female_reg", ":faction_leader", 4),
		##diplomacy end+

		(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
		(str_store_troop_name, s11, ":spouse"),
		(str_store_string, s7, "str_to_your_husband_s11"),
    ],
    [
		("continue",[],"Continue.",
			[
			(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
			(call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", ":spouse", 0),
			],
		),
	]
),







(
    "requested_castle_granted_to_another",mnf_scale_picture,
    "You receive a message from your monarch, {s3}.^^\
 'I was most pleased to hear of your valiant efforts in the capture of {s2}. Your victory has gladdened all our hearts.\
 You also requested me to give you ownership of the castle, but that is a favor which I fear I cannot grant,\
 as you already hold significant estates in my realm.\
 Instead I have sent you {reg6} denars to cover the expenses of your campaign, but {s2} I give to {s5}.'\
 ",
    "none",
    [(set_background_mesh, "mesh_pic_messenger"),
     (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
     (str_store_troop_name, s3, ":faction_leader"),
     (str_store_party_name, s2, "$g_center_to_give_to_player"),
     (party_get_slot, ":new_owner", "$g_center_to_give_to_player", slot_town_lord),
     (str_store_troop_name, s5, ":new_owner"),
     (assign, reg6, 900),

	 (assign, "$g_castle_requested_by_player", -1),
	 (assign, "$g_castle_requested_for_troop", -1),

    ],
    [
      ("accept_decision",[],"Accept the decision.",
       [
       (call_script, "script_troop_add_gold", "trp_player", reg6),
        ##diplomacy start+ Remove gold spent by liege
        (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
        (try_begin),
            (gt, ":faction_leader", 0),
            (neq, ":faction_leader", "trp_kingdom_heroes_including_player_begin"),
            (call_script, "script_dplmc_remove_gold_from_lord_and_holdings", reg6, ":faction_leader"),
        (try_end),
        ##diplomacy end+
       (change_screen_return),
       ]),

       ("leave_faction",[],"You have been wronged! Renounce your oath to your liege! ",
       [
         ##diplomacy start+ Remove gold spent by liege
         (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
         (try_begin),
            (gt, ":faction_leader", 0),
            (neq, ":faction_leader", "trp_kingdom_heroes_including_player_begin"),
            (call_script, "script_dplmc_remove_gold_from_lord_and_holdings", reg6, ":faction_leader"),
         (try_end),
         ##diplomacy end+
         (jump_to_menu, "mnu_leave_faction"),
         (call_script, "script_troop_add_gold", "trp_player", reg6),
        ]),
     ],
  ),


(
    "requested_castle_granted_to_another_female",mnf_scale_picture,
##diplomacy start+ make gender correct
    "You receive a message from your monarch, {s3}.^^\
 'I was most pleased to hear of your valiant efforts in the capture of {s2}. Your victory has gladdened all our hearts.\
 You also requested me to give ownership of the castle to your {wife/husband}, but that is a favor which I fear I cannot grant,\
 as {she/he} already holds significant estates in my realm.\
 Instead I have sent you {reg6} denars to cover the expenses of your campaign, but {s2} I give to {s5}.'\
 ",
##diplomacy end+
    "none",
    [(set_background_mesh, "mesh_pic_messenger"),
     (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
     (str_store_troop_name, s3, ":faction_leader"),
     (str_store_party_name, s2, "$g_center_to_give_to_player"),
     (party_get_slot, ":new_owner", "$g_center_to_give_to_player", slot_town_lord),
     (str_store_troop_name, s5, ":new_owner"),
     (assign, reg6, 900),

	 (assign, "$g_castle_requested_by_player", -1),
	 (assign, "$g_castle_requested_for_troop", -1),
    ],

    [
		("accept_decision",[],"Accept the decision.",
        [
        (call_script, "script_troop_add_gold", "trp_player", reg6),
        (change_screen_return),
        ]),
    ],
),




  (
    "leave_faction",0,
    "Renouncing your oath is a grave act. Your lord may condemn you and confiscate your lands and holdings.\
 However, if you return them of your own free will, he may let the betrayal go without a fight.",
    "none",
    [
    ],
    [
      ("leave_faction_give_back", [], "Renounce your oath and give up your holdings.",
       [
#Troop commentary changes begin
#        (call_script, "script_add_log_entry", logent_renounced_allegiance,   "trp_player",  -1, "$g_talk_troop", "$g_talk_troop_faction"),
#Troop commentary changes end
        (call_script, "script_player_leave_faction", 1), #1 means give back fiefs
        (change_screen_return),
        ]),
      ("leave_faction_hold", [
          (str_store_party_name, s2, "$g_center_to_give_to_player"),
          ], "Renounce your oath and rule your lands, including {s2}, in your own name.",
       [
        (call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0), #this should activate the player faction (it does not)
        (call_script, "script_player_leave_faction", 0), #"1" would mean give back fiefs
		(call_script, "script_activate_player_faction", "trp_player"), #Activating player faction should now work
        (change_screen_return),
        ]),
      ("leave_faction_cancel", [], "Remain loyal and accept the decision.",
       [
        (change_screen_return),
        ]),
    ],
  ),

  (
    "give_center_to_player",mnf_scale_picture,
##diplomacy start+ fix gender of pronoun
    "Your lord offers to extend your fiefs!\
 {s1} sends word that {reg4?she:he} is willing to grant {s2} to you in payment for your loyal service,\
 adding it to your holdings. What is your answer?",
##diplomacy end+
    "none",
    [(set_background_mesh, "mesh_pic_messenger"),
     (store_faction_of_party, ":center_faction", "$g_center_to_give_to_player"),
     (faction_get_slot, ":faction_leader", ":center_faction", slot_faction_leader),
     ##diplomacy start+ put king's gender in reg4
     (call_script, "script_dplmc_store_troop_is_female_reg", ":faction_leader", 4),
     ##diplomacy end+
     (str_store_troop_name, s1, ":faction_leader"),
     (str_store_party_name, s2, "$g_center_to_give_to_player"),
    ],
    [
      ("give_center_to_player_accept",[],"Accept the offer.",
       [(call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
        (jump_to_menu, "mnu_give_center_to_player_2"),
        ]),
      ("give_center_to_player_reject",[],"Reject. You have no interest in holding {s2}.",
       [(party_set_slot, "$g_center_to_give_to_player", slot_town_lord, stl_rejected_by_player),
        (change_screen_return),
        ]),
    ],
  ),

  (
    "give_center_to_player_2",0,
    "With a brief ceremony, you are officially confirmed as the new lord of {s2}{reg3? and its bound village {s4}:}.\
 {reg3?They:It} will make a fine part of your fiefdom.\
 You can now claim the rents and revenues from your personal estates there, draft soldiers from the populace,\
 and manage the lands as you see fit.\
 However, you are also expected to defend your fief and your people from harm,\
 as well as maintaining the rule of law and order.",
    "none",
    [
      (str_store_party_name, s2, "$g_center_to_give_to_player"),
      (assign, reg3, 0),
      (try_begin),
        (party_slot_eq, "$g_center_to_give_to_player", slot_party_type, spt_castle),
        (try_for_range, ":cur_village", villages_begin, villages_end),
          (party_slot_eq, ":cur_village", slot_village_bound_center, "$g_center_to_give_to_player"),
          (str_store_party_name, s4, ":cur_village"),
          (assign, reg3, 1),
        (try_end),
      (try_end),
    ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
    ],
  ),


  (
    "oath_fulfilled",0,
##diplomacy start+ fix gender of pronoun
    "You had a contract with {s1} to serve {reg4?her:him} for a certain duration.\
 Your contract has now expired. What will you do?",
##diplomacy end+
    "none",
    [
      (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
      ##diplomacy start+ load king's gender into reg4
      (call_script, "script_dplmc_store_troop_is_female", ":faction_leader"),
      (assign, reg4, reg0),
      ##diplomacy end+
      (str_store_troop_name, s1, ":faction_leader"),
     ],
    [
      ("renew_oath",[(faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
                     (str_store_troop_name, s1, ":faction_leader")], "Renew your contract with {s1} for another month.",
       [
         (store_current_day, ":cur_day"),
         (store_add, "$mercenary_service_next_renew_day", ":cur_day", 30),
         (change_screen_return),
         ]),
      ("dont_renew_oath",[],"Become free of your bond.",
       [
         (call_script, "script_player_leave_faction", 1), #1 means give back fiefs
         (change_screen_return),
         ]),
    ]
  ),


##  (
##    "castle_garrison_stationed",0,
###    "The rest of the castle garrison recognizes that their situation is hopeless and surrenders. {s1} is at your mercy now. What do you want to do with this castle?",
##    "_",
##    "none",
##    [
##        (jump_to_menu, "mnu_town"),
##    ],
##    [],
##  ),

##  (
##    "castle_choose_captain",0,
##    "You will need to assign one of your companions as the castellan. Who will it be?",
##    "none",
##    [
##        (try_for_range, ":slot_no", 0, 20),
##          (troop_set_slot, "trp_temp_troop", ":slot_no", 0),
##        (try_end),
##        (assign, ":num_captains", 0),
##        (party_clear, "p_temp_party"),
##        (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
##        (try_for_range, ":i_s", 1,":num_stacks"),
##          (party_stack_get_troop_id, ":companion","p_main_party", ":i_s"),
##          (troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),
##          (troop_set_slot, "trp_temp_troop", ":num_captains", ":companion"),
##        (try_end),
##    ],
##    [
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 0),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 0),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 1),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 1),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 2),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 2),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 3),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 3),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 4),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 4),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 5),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 5),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 6),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 6),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 7),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 7),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 8),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 8),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 9),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 9),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 10),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 10),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 11),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 11),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 12),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 12),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 13),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 13),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 14),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 14),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 15),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 15),(jump_to_menu,"mnu_castle_captain_chosen")]),
##
##      ("cancel",[],
##         "Cancel...",
##         [(jump_to_menu, "mnu_town")]),
##    ],
##  ),
##  (
##    "castle_captain_chosen",0,
##    "h this castle?",
##    "none",
##    [
##        (party_add_leader, "$g_encountered_party",  "$selected_castellan"),
##        (party_remove_members, "p_main_party", "$selected_castellan",1),
##        (party_set_slot, "$g_encountered_party", slot_town_lord, "trp_player"),
##        (party_set_faction, "$g_encountered_party", "fac_player_supporters_faction"),
##        (try_for_range, ":slot_no", 0, 20), #clear temp troop slots just in case
##          (troop_set_slot, "trp_temp_troop", ":slot_no", 0),
##        (try_end),
##        (jump_to_menu, "mnu_town"),
##        (change_screen_exchange_members,0),
##    ],
##    [],
##  ),

##  (
##    "under_siege_attacked_continue",0,
##    "Nothing to see here.",
##    "none",
##    [
##        (assign, "$g_enemy_party", "$g_encountered_party_2"),
##        (assign, "$g_ally_party", "$g_encountered_party"),
##        (party_set_next_battle_simulation_time, "$g_encountered_party", 0),
##        (call_script, "script_encounter_calculate_fit"),
##        (try_begin),
##          (call_script, "script_party_count_fit_regulars", "p_collective_enemy"),
##          (assign, ":num_enemy_regulars_remaining", reg(0)),
##          (assign, ":enemy_finished",0),
##          (try_begin),
##            (eq, "$g_battle_result", 1),
##            (eq, ":num_enemy_regulars_remaining", 0), #battle won
##            (assign, ":enemy_finished",1),
##          (else_try),
##            (eq, "$g_engaged_enemy", 1),
##            (le, "$g_enemy_fit_for_battle",0),
##            (ge, "$g_friend_fit_for_battle",1),
##            (assign, ":enemy_finished",1),
##          (try_end),
##          (this_or_next|eq, ":enemy_finished",1),
##          (eq,"$g_enemy_surrenders",1),
####          (assign, "$g_center_under_siege_battle", 0),
##          (assign, "$g_next_menu", -1),
##          (jump_to_menu, "mnu_total_victory"),
##        (else_try),
##          (assign, ":battle_lost", 0),
##          (try_begin),
##            (eq, "$g_battle_result", -1),
##            (assign, ":battle_lost",1),
##          (try_end),
##          (this_or_next|eq, ":battle_lost",1),
##          (eq,"$g_player_surrenders",1),
####          (assign, "$g_center_under_siege_battle", 0),
##          (assign, "$g_next_menu", "mnu_captivity_start_under_siege_defeat"),
##          (jump_to_menu, "mnu_total_defeat"),
##        (else_try),
##    # Ordinary victory.
##          (try_begin),
##          #check whether enemy retreats
##            (eq, "$g_battle_result", 1),
##            (store_mul, ":min_enemy_str", "$g_enemy_fit_for_battle", 2),
##            (lt, ":min_enemy_str", "$g_friend_fit_for_battle"),
##            (party_set_slot, "$g_enemy_party", slot_party_retreat_flag, 1),
##
##            (try_for_range, ":troop_no", kingdom_heroes_begin, kingdom_heroes_end),
##              (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
##              (troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
##              (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
##              (gt, ":party_no", 0),
##              (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
##              (party_slot_eq, ":party_no", slot_party_ai_object, "$g_encountered_party"),
##              (party_slot_eq, ":party_no", slot_party_ai_substate, 1),
##              (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
##              (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, ":center_no"),
##            (try_end),
##            (display_message, "@{!}TODO: Enemy retreated. The assault has ended, siege continues."),
##            (change_screen_return),
##          (try_end),
####          (assign, "$g_center_under_siege_battle", 0),
##        (try_end),
##        ],
##    [
##    ]
##  ),


  ( #SB : pic hotkeys
    "siege_started_defender",mnf_enable_hot_keys,
    "{s1} is launching an assault against the walls of {s2}. You have {reg10} troops fit for battle against the enemy's {reg11}. You decide to...",
    "none",
    [
        (select_enemy,1),
        (assign, "$g_enemy_party", "$g_encountered_party_2"),
        (assign, "$g_ally_party", "$g_encountered_party"),
        (str_store_party_name, s1, "$g_enemy_party"),
        (str_store_party_name, s2, "$g_ally_party"),
        (call_script, "script_encounter_calculate_fit"),
        (try_begin),
          (eq, "$g_siege_first_encounter", 1),
          (call_script, "script_let_nearby_parties_join_current_battle", 0, 1),
		  ###diplomacy start+
		  ##If terrain advantage is on, use siege settings
          #(assign, ":save_dplmc_terrain_advantage", "$g_dplmc_terrain_advantage"),
		  #(try_begin),
		  #   (eq, "$g_dplmc_terrain_advantage", TERRAIN_ADVANTAGE_ENABLE),
		  #   (assign, "$g_dplmc_terrain_advantage", TERRAIN_ADVANTAGE_FORCE_SIEGE),
		  #(try_end),
		  ###diplomacy end+
          (call_script, "script_encounter_init_variables"),
		  ###diplomacy start+
		  ##Revert terrain advantage settings
		  #(assign, "$g_dplmc_terrain_advantage", ":save_dplmc_terrain_advantage"),
		  ###diplmacy end+
        (try_end),

        (try_begin),
          (eq, "$g_siege_first_encounter", 0),
          (try_begin),
            (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
            (assign, ":num_enemy_regulars_remaining", reg0),
            (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
            (assign, ":num_ally_regulars_remaining", reg0),
            (assign, ":enemy_finished", 0),
            (try_begin),
              (eq, "$g_battle_result", 1),
              (eq, ":num_enemy_regulars_remaining", 0), #battle won (TODO : compare with num_routed_us)
              (assign, ":enemy_finished",1),
            (else_try),
              (eq, "$g_engaged_enemy", 1),
              (le, "$g_enemy_fit_for_battle",0),
              (ge, "$g_friend_fit_for_battle",1),
              (assign, ":enemy_finished",1),
            (try_end),
            (this_or_next|eq, ":enemy_finished",1),
            (eq,"$g_enemy_surrenders",1),
            (assign, "$g_next_menu", -1),
            (jump_to_menu, "mnu_total_victory"),
          (else_try),
            (assign, ":battle_lost", 0),
            (try_begin),
              (this_or_next|eq, "$g_battle_result", -1),
              (troop_is_wounded,  "trp_player"),
              (eq, ":num_ally_regulars_remaining", 0), #(TODO : compare with num_routed_allies)
              (assign, ":battle_lost",1),
            (try_end),
            (this_or_next|eq, ":battle_lost",1),
            (eq,"$g_player_surrenders",1),
            (assign, "$g_next_menu", "mnu_captivity_start_under_siege_defeat"),
            (jump_to_menu, "mnu_total_defeat"),
          (else_try),
            # Ordinary victory/defeat.
            (assign, ":attackers_retreat", 0),
            (try_begin),
            #check whether enemy retreats
              (eq, "$g_battle_result", 1),
  ##            (store_mul, ":min_enemy_str", "$g_enemy_fit_for_battle", 2),
  ##            (lt, ":min_enemy_str", "$g_friend_fit_for_battle"),
              (assign, ":attackers_retreat", 1),
            (else_try), #fix this
              (eq, "$g_battle_result", 0),
              (store_div, ":min_enemy_str", "$g_enemy_fit_for_battle", 3),
              (lt, ":min_enemy_str", "$g_friend_fit_for_battle"),
              (assign, ":attackers_retreat", 1),
            (else_try),
              (store_random_in_range, ":random_no", 0, 100),
              (store_mul, ":num_ally_regulars_remaining_multiplied", ":num_ally_regulars_remaining", 13),
              (val_div, ":num_ally_regulars_remaining_multiplied", 10),
              (ge, ":num_ally_regulars_remaining_multiplied", ":num_enemy_regulars_remaining"),
              (lt, ":random_no", 10),
              (neq, "$new_encounter", 1),
              (assign, ":attackers_retreat", 1),
            (try_end),
            (try_begin),
              (eq, ":attackers_retreat", 1),
              (party_get_slot, ":siege_hardness", "$g_encountered_party", slot_center_siege_hardness),
              (val_add, ":siege_hardness", 100),
              (party_set_slot, "$g_encountered_party", slot_center_siege_hardness, ":siege_hardness"),
              (party_set_slot, "$g_enemy_party", slot_party_retreat_flag, 1),

              (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
                (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
                #(troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
                (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
                (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
                (gt, ":party_no", 0),
                (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
                (party_slot_eq, ":party_no", slot_party_ai_object, "$g_encountered_party"),
                (party_slot_eq, ":party_no", slot_party_ai_substate, 1),
                (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
                (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, "$g_encountered_party"),
              (try_end),
              (display_message, "@The enemy has been forced to retreat. The assault is over, but the siege continues."),
              (assign, "$g_battle_simulation_cancel_for_party", "$g_encountered_party"),
              (leave_encounter),
              (change_screen_return),
              (assign, "$g_battle_simulation_auto_enter_town_after_battle", "$g_encountered_party"),
            (try_end),
          (try_end),
        (try_end),
        # (assign, "$g_siege_first_encounter", 0), #dckplmc - moved this down
        # (assign, "$new_encounter", 0),
        ],
    [
      ("siege_defender_castle",
      [

        #SB : some gender string tweaks
        (try_begin),
          (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
          (lt, ":town_lord", 0),
          (assign, reg4, 0), #default to lord
        (else_try),
          (call_script, "script_dplmc_store_troop_is_female_reg", ":town_lord", 4),
        (try_end),
        #possibly replace "the" with "your"
        ],"Go to the {reg4?Lady:Lord}'s hall.",
       [
             (call_script, "script_enter_court", "$current_town"),
        ], "Door to the castle."),
              
      #SB : add garrison management, maybe penalties if player disbands prisoners
      ("siege_defender_manage_troops",[
        (assign, ":player_can_draw_from_garrison", 0),
        (str_clear, s10),
        (party_get_slot, ":town_lord", "$g_encountered_party", slot_town_lord),
        
        (store_party_size_wo_prisoners, ":party_size", "$g_encountered_party"),
        (gt, ":party_size", 0),
        (try_begin), #option 1 - player is town lord
          (eq, ":town_lord", "trp_player"),
          (assign, ":player_can_draw_from_garrison", 1),
        (else_try), #option 2 - town is unassigned and part of the player faction
          (store_faction_of_party, ":faction", "$g_encountered_party"),
          (eq, ":faction", "fac_player_supporters_faction"),
          (neg|party_slot_ge, "$g_encountered_party", slot_town_lord, active_npcs_begin), #ie, zero or -1

          (assign, ":player_can_draw_from_garrison", 1),
        (else_try), #option 3 - town was captured by player
          (lt, ":town_lord", 0), #ie, unassigned
          (store_faction_of_party, ":castle_faction", "$g_encountered_party"),
          (eq, "$players_kingdom", ":castle_faction"),

          (eq, "$g_encountered_party", "$g_castle_requested_by_player"),

          (str_store_string, s10, "str_retrieve_garrison_warning"),
          (assign, ":player_can_draw_from_garrison", 1),
        # (else_try),
          # (lt, ":town_lord", 0), #ie, unassigned
          # (store_faction_of_party, ":castle_faction", "$g_encountered_party"),
          # (eq, "$players_kingdom", ":castle_faction"),

          # (store_party_size_wo_prisoners, ":party_size", "$g_encountered_party"),
          # (eq, ":party_size", 0),

          # (str_store_string, s10, "str_retrieve_garrison_warning"),
          # (assign, ":player_can_draw_from_garrison", 1),
        (else_try),
          (party_slot_ge, "$g_encountered_party", slot_town_lord, active_npcs_begin),
          (store_faction_of_party, ":castle_faction", "$g_encountered_party"),
          (eq, "$players_kingdom", ":castle_faction"),
          ##diplomacy start+ can arise if using this to represent polygamy
          (this_or_next|troop_slot_eq, ":town_lord", slot_troop_spouse, "trp_player"),
             (troop_slot_eq, "trp_player", slot_troop_spouse, ":town_lord"),
          (this_or_next|is_between, ":town_lord", heroes_begin, heroes_end),
          ##diplomacy end+
          (troop_slot_eq, "trp_player", slot_troop_spouse, ":town_lord"),

          (assign, ":player_can_draw_from_garrison", 1),
        (try_end),

        (eq, ":player_can_draw_from_garrison", 1),
      ],
          "Manage the garrison {s10}",[
              (change_screen_exchange_members,1),]),
    
     ##diplomacy begin
      ("dplmc_negotiate_with_besieger",
      [
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
        (party_slot_ge, "$current_town", slot_center_is_besieged_by, 1),
      ]
       ,"Negotiate with the besieger.",
       [
        (jump_to_menu, "mnu_dplmc_negotiate_besieger"),
        ]),
     ##diplomacy end
      ("siege_defender_join_battle",
       [
         (neg|troop_is_wounded, "trp_player"),
         ],
          "Join the battle.",[
          
              (try_begin),
                  (troop_is_wounded, "trp_player"),
                  (display_message,"@Your wounds are too severe to fight.",message_locked),
              (else_try),
                  (assign, "$g_siege_first_encounter", 0), #dckplmc - moved from main menu conditions
                  (assign, "$new_encounter", 0),
              
                  (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
                  (assign, "$g_battle_result", 0),
                  (try_begin),
                    (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                    (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_walls),
                  (else_try),
                    (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
                  (try_end),
                  (call_script, "script_calculate_battle_advantage"),
                  (val_mul, reg0, 2),
                  (val_div, reg0, 3), #scale down the advantage a bit.
                  (set_battle_advantage, reg0),
                  (set_party_battle_mode),
                  (try_begin),
                    (party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),
                    (set_jump_mission,"mt_castle_attack_walls_belfry"),
                  (else_try),
                    (set_jump_mission,"mt_castle_attack_walls_ladder"),
                  (try_end),
                  (jump_to_scene,":battle_scene"),
                  (assign, "$g_next_menu", "mnu_siege_started_defender"),
                  (jump_to_menu, "mnu_battle_debrief"),
                  (change_screen_mission),
              (try_end),
              ], "Join the defense."),
              
      ("siege_defender_join_battle",
       [
         (neg|troop_is_wounded, "trp_player"),
         ],
          "Sally out.",[
                  (assign, "$g_siege_first_encounter", 0), #dckplmc - moved from main menu conditions
                  (assign, "$new_encounter", 0),
              
                  (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
                  (assign, "$g_battle_result", 0),
                  (try_begin),
                    (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                    (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_walls),
                  (else_try),
                    (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
                  (try_end),
                  (call_script, "script_calculate_battle_advantage"),
                  (val_mul, reg0, 2),
                  (val_div, reg0, 3), #scale down the advantage a bit.
                  (set_battle_advantage, reg0),
                  (set_party_battle_mode),
                  (set_jump_mission,"mt_castle_attack_walls_defenders_sally"),
                  (jump_to_scene,":battle_scene"),
                  (assign, "$g_next_menu", "mnu_siege_started_defender"),
                  (jump_to_menu, "mnu_battle_debrief"),
                  (change_screen_mission),
              ]),
              
      ("siege_defender_troops_join_battle",[(call_script, "script_party_count_members_with_full_health", "p_main_party"),
                                            (this_or_next|troop_is_wounded,  "trp_player"),
                                            (ge, reg0, 3)],
          "Order your men to join the battle without you.",[
              (assign, "$g_siege_first_encounter", 0), #dckplmc - moved from main menu conditions
              (assign, "$new_encounter", 0),
          
              (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
              (select_enemy,1),
              (assign,"$g_enemy_party","$g_encountered_party_2"),
              (assign,"$g_ally_party","$g_encountered_party"),
              (assign,"$g_siege_join", 1),
              (jump_to_menu,"mnu_siege_join_defense")]),
              

    ]
  ),

  (
    "siege_join_defense",mnf_disable_all_keys,
    "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
    "none",
    [
	    ###diplomacy start+
		##If terrain advantage is on, use siege settings
        #(assign, ":save_dplmc_terrain_advantage", "$g_dplmc_terrain_advantage"),
		##(assign, "$g_dplmc_terrain_advantage", ":save_dplmc_terrain_advantage"),
		#(try_begin),
		#   (eq, "$g_dplmc_terrain_advantage", TERRAIN_ADVANTAGE_ENABLE),
		#   (assign, "$g_dplmc_terrain_advantage", TERRAIN_ADVANTAGE_FORCE_SIEGE),
		#(try_end),
		###diplomacy end+
        (try_begin),
          (eq, "$g_siege_join", 1),
          (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
          (assign, ":player_party_strength", reg0),
          (val_div, ":player_party_strength", 5),
        (else_try),
          (assign, ":player_party_strength", 0),
        (try_end),

        (call_script, "script_party_calculate_strength", "p_collective_ally", 0),
        (assign, ":ally_party_strength", reg0),
        (val_div, ":ally_party_strength", 5),
        (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
        (assign, ":enemy_party_strength", reg0),
        (val_div, ":enemy_party_strength", 10),

        (store_add, ":friend_party_strength", ":player_party_strength", ":ally_party_strength"),
        (try_begin),
          (eq, ":friend_party_strength", 0),
          (store_div, ":enemy_party_strength_for_p", ":enemy_party_strength", 2),
        (else_try),
          (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
          (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
          (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),
        (try_end),

        (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),
        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s8, s0),

        (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s9, s0),
        (party_collect_attachments_to_party, "$g_ally_party", "p_collective_ally"),

        (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s10, s0),
        (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),

        (try_begin),
          (call_script, "script_party_count_members_with_full_health","p_main_party"),
          (le, reg0, 0),
          (str_store_string, s4, "str_siege_defender_order_attack_failure"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health","p_collective_enemy"),
          (le, reg0, 0),
          (assign, "$g_battle_result", 1),
          (str_store_string, s4, "str_siege_defender_order_attack_success"),
        (else_try),
          (str_store_string, s4, "str_siege_defender_order_attack_continue"),
        (try_end),
		###diplomacy start+
		##Revert terrain advantage settings
		#(assign, "$g_dplmc_terrain_advantage", ":save_dplmc_terrain_advantage"),
		###diplomacy end+
    ],
    [
      ("continue",[],"Continue...",[
          (jump_to_menu,"mnu_siege_started_defender"),
          ]),
    ]
  ),

  (
    "enter_your_own_castle",0,
    "{s10}",
    "none",
    [
      (try_begin),
	  ##diplomacy start+ Add support for the player as co-ruler of an NPC faction
	    (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
		(neg|is_between, "$supported_pretender", pretenders_begin, pretenders_end), #SB : exception for honorific
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(try_begin),
			(eq, "$character_gender", tf_female),
			(call_script, "script_dplmc_print_cultural_word_to_sreg", "trp_player", DPLMC_CULTURAL_TERM_KING_FEMALE, s10),
		(else_try),
			(call_script, "script_dplmc_print_cultural_word_to_sreg", "trp_player", DPLMC_CULTURAL_TERM_KING, s10),
		(try_end),
		(str_store_string, s10, "@As you approach, you are spotted by the castle guards, who welcome you and open the gates for their {s10}."),
	  (else_try),
	  ##diplomacy end+
        (neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
        (faction_get_slot, ":faction_leader", "fac_player_supporters_faction", slot_faction_leader),
        (eq, ":faction_leader", "trp_player"),
        (str_store_string, s10, "@As you approach, you are spotted by the castle guards, who welcome you and open the gates for their {king/queen}."),
      (else_try),
        (str_store_string, s10, "@As you approach, you are spotted by the castle guards, who welcome you and open the gates for their {lord/lady}."),
      (try_end),

      (str_store_party_name, s2, "$current_town"),
    ],
    [
      ("continue",[],"Continue...",
       [ (jump_to_menu,"mnu_town"),
        ]),
    ],
  ),

  (
    "village",mnf_enable_hot_keys,
    "{s10} {s12}^{s11}^{s6}{s7}",
    "none",
    [
        (assign, "$current_town", "$g_encountered_party"),
        (call_script, "script_update_center_recon_notes", "$current_town"),

        (assign, "$g_defending_against_siege", 0), #required for bandit check
        (assign, "$g_battle_result", 0),
        (assign, "$qst_collect_taxes_currently_collecting", 0),
        (assign, "$qst_train_peasants_against_bandits_currently_training", 0),

        (try_begin),
          (gt, "$auto_enter_menu_in_center", 0),
          (jump_to_menu, "$auto_enter_menu_in_center"),
          (assign, "$auto_enter_menu_in_center", 0),
        (try_end),

        (try_begin),
          (neq, "$g_player_raiding_village",  "$current_town"),
          (assign, "$g_player_raiding_village", 0),
        (else_try),
          (jump_to_menu, "mnu_village_loot_continue"),
        (try_end),

        (try_begin),#Fix for collecting taxes
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
        (try_end),

        (str_store_party_name,s2, "$current_town"),
        (party_get_slot, ":center_lord", "$current_town", slot_town_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name,s9,":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8,":center_lord"),
          (str_store_string,s7,"@{s8} of {s9}"),
        (try_end),

        (str_clear, s10),
        (str_clear, s12),

        (try_begin),
          (neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
          (str_store_string, s60, s2),

          (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
		  (try_begin),
			(eq, "$cheat_mode", 1),
			(assign, reg4, ":prosperity",),
			(display_message, "@{!}Prosperity: {reg4}"),
		  (try_end),

		  #(val_add, ":prosperity", 5),
          (store_div, ":str_id", ":prosperity", 10),
		  (val_min, ":str_id", 9),
		  (val_add, ":str_id", "str_village_prosperity_0"),
          (str_store_string, s10, ":str_id"),


          (store_div, ":str_id", ":prosperity", 20),
		  (val_min, ":str_id", 4),
		  (try_begin),
			(is_between, "$current_town", "p_village_91", villages_end),
			(val_add, ":str_id", "str_oasis_village_alt_prosperity_0"),
		  (else_try),
			(val_add, ":str_id", "str_village_alt_prosperity_0"),
		  (try_end),

          (str_store_string, s12, ":str_id"),
        (try_end),

        (str_clear, s11),
        ##diplomacy start+
		(assign, ":save_reg0", reg0),#save variables
		(assign, ":save_reg4", reg4),
		(assign, reg0, 0),
		(assign, reg4, 0),
		(try_begin),#If there's a relation of some kind, write it to s11 (which we'll overwrite below)
			(lt, ":center_lord", 1),
		(else_try),
			#your relative
			(call_script, "script_troop_get_family_relation_to_troop", ":center_lord", "trp_player"),#outputs to s11, reg0, and reg4
			(ge, reg0, 1),#Fall through if this not a relative
		(else_try),
			#your current liege
			(eq, ":center_faction", "$players_kingdom"),
			(is_between, ":center_faction", kingdoms_begin, kingdoms_end),#include fac_player_supporters_faction for claimant quest
			(faction_slot_eq, ":center_faction", slot_faction_leader, ":center_lord"),
			(str_store_string, s11, "@liege"),
			(assign, reg0, 1),
		(else_try),
			#your former liege if you renounced a kingdom
			(eq, ":center_faction", "$players_oath_renounced_against_kingdom"),
			(is_between, ":center_faction", npc_kingdoms_begin, npc_kingdoms_end),
			(faction_slot_eq, ":center_faction", slot_faction_leader, ":center_lord"),
			(str_store_string, s11, "@former liege"),
			(assign, reg0, 1),
		(else_try),
			#stop here for lords you haven't met, or non-hero troops
			(this_or_next|neg|troop_is_hero, ":center_lord"),
			(troop_slot_eq, ":center_lord", slot_troop_met, 0),
		(else_try),
			#check for affiliates
			(call_script, "script_dplmc_is_affiliated_family_member", ":center_lord"),
			(ge, reg0, 1),
			(try_begin),
				(ge, "$g_encountered_party_relation", 0),#don't say "ally" when you might fight them, as that's confusing
				(str_store_string, s11, "str_dplmc_ally"),
			(else_try),
				(str_store_string, s11, "@affiliate"),
			(try_end),
		(else_try),
			#check for former companions
			(call_script, "script_troop_get_player_relation", ":center_lord"),
			(is_between, ":center_lord", companions_begin, companions_end),
			(neg|troop_slot_eq, ":center_lord", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
			(try_begin),
			   (ge, "$g_encountered_party_relation", 0),#don't say "ally" when you might fight them, as that's confusing
			   (ge, reg0, 50),
			   (str_store_string, s11, "str_dplmc_ally"),
			(else_try),
				(ge, "$g_encountered_party_relation", 0),
				(ge, reg0, 20),
				(str_store_string, s11, "str_dplmc_friend"),
			(else_try),
				(str_store_string, s11, "@former companion"),
			(try_end),
			(assign, reg0, 1),
		(else_try),
			#don't print "friend" if you might fight them
			(lt, "$g_encountered_party_relation", 0),
			(assign, reg0, 0),
		(else_try), #SB : local instead of reg
			#check for friends
            (call_script, "script_troop_get_player_relation", ":center_lord"),
			(store_div, ":relation", reg0, 50),#right now reg0 holds the relation with the player
			(gt, ":relation", 1),
			(str_store_string, s11, "str_dplmc_friend"),
            (assign, reg0, 1),
		(else_try),
			#check for marshall
			(eq, ":center_faction", "$players_kingdom"),
			(faction_slot_eq, ":center_faction", slot_faction_marshall, ":center_lord"),
			(str_store_string, s11, "@marshall"),
		(else_try),
			#check for vassal of player if nothing else to say
			(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":center_faction"),
			(val_add, reg0, 1),
			(val_sub, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
			(ge, reg0, 1),
			(str_store_string, s11, "@vassal"),
		(else_try),
			(assign, reg0, 0),
		(try_end),
		##diplomacy end+
        (try_begin),
          # (party_slot_eq, "$current_town", slot_village_state, svs_looted),
          # #SB : cancel string clear
          # (str_clear, s11),
        # (else_try),
          (eq, ":center_lord", "trp_player"),
          (str_store_string,s11,"@ This village and the surrounding lands belong to you."),
		##diplomacy start+ If reg0 > 0, a relation string has been written into s11
		(else_try),
		  (ge, reg0, 1),
		  (str_store_string,s11,"@ You remember that this village and the surrounding lands belong to your {s11} {s7}."),
		##diplomacy end+
        (else_try),
          (ge, ":center_lord", 0),
          (str_store_string,s11,"@ You remember that this village and the surrounding lands belong to {s7}."),
        (else_try),
          (str_store_string,s11,"@ These lands belong to no one."),
        (try_end),
		##diplomacy start+
		(assign, reg0, ":save_reg0"),#revert registers
		(assign, reg4, ":save_reg4"),
		##diplomacy end+

        (str_clear, s7),
        (try_begin),
          (neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
          (party_get_slot, ":center_relation", "$current_town", slot_center_player_relation),
          (call_script, "script_describe_center_relation_to_s3", ":center_relation"),
          (assign, reg9, ":center_relation"),
          (str_store_string, s7, "@{!} {s3} ({reg9})."),
        (try_end),
        (str_clear, s6),
        (try_begin),
          (party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
          (party_get_slot, ":bandit_troop", "$current_town", slot_village_infested_by_bandits),
          (store_character_level, ":player_level", "trp_player"),
          (val_min, ":player_level", 63),
          ## SB : adjust bandit levels to manageable levels, reinforcements based on party size - fuck off
          (store_add, "$qst_eliminate_bandits_infesting_village_num_bandits", ":player_level", 10),
          #(val_div, "$qst_eliminate_bandits_infesting_village_num_bandits", 2), literally for babies
          (faction_get_slot, ":limit", ":center_faction", dplmc_slot_faction_serfdom),
          #(options_get_campaign_ai, ":reduced"),
          #(val_mul, ":reduced", 3), #poor ai = more base bandits  terrible
          #(val_sub, ":reduced", ":limit"),
          (store_sub, ":limit", 6, ":limit"),
          (val_mul, ":limit", 2),
          (val_add, "$qst_eliminate_bandits_infesting_village_num_bandits", ":limit"),
          (val_mul, "$qst_eliminate_bandits_infesting_village_num_bandits", 120),
          (val_div, "$qst_eliminate_bandits_infesting_village_num_bandits", 100),
          (val_max, "$qst_eliminate_bandits_infesting_village_num_bandits", 10), #dckplmc - no less than 10 bandits
          
          # (party_get_num_companions, ":party_size", "$current_town"), #ideal size is 50
          (call_script, "script_party_count_fit_regulars", "$current_town"),
          (assign, ":party_size", reg0),
          (store_div, ":lower_size", ":party_size", 3), #about 2/3rd stay back
          (store_div, ":limit", ":center_relation", 5),
          (val_add, ":limit", 60),
          (store_random_in_range, "$qst_eliminate_bandits_infesting_village_num_villagers", ":lower_size", ":limit"),
          (val_min, "$qst_eliminate_bandits_infesting_village_num_villagers", ":party_size"),
          (assign, reg8, "$qst_eliminate_bandits_infesting_village_num_bandits"),
          (str_store_troop_name_by_count, s35, ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),
          (str_store_string, s6, "@ The village is infested by {reg8} {s35}."),

          (assign, "$g_enemy_party", -1), #new, no known enemy party while saving village from bandits
          (assign, "$g_ally_party", -1), #new, no known enemy party while saving village from bandits

          ## SB : adjust meshes as well
          (try_begin),
            (eq, ":bandit_troop", "trp_forest_bandit"),
            (set_background_mesh, "mesh_pic_forest_bandits"),
          (else_try),
            (this_or_next|eq, ":bandit_troop", "trp_steppe_bandit"),
            (eq, ":bandit_troop", "trp_desert_bandit"),
            (set_background_mesh, "mesh_pic_steppe_bandits"),
          (else_try),
            (this_or_next|eq, ":bandit_troop", "trp_steppe_bandit"),
            (eq, ":bandit_troop", "trp_taiga_bandit"),
            (set_background_mesh, "mesh_pic_mountain_bandits"),
          (else_try),
            (eq, ":bandit_troop", "trp_sea_raider"),
            (set_background_mesh, "mesh_pic_sea_raiders"),
          (else_try),
            (store_faction_of_troop, ":faction_no", ":bandit_troop"),
            (this_or_next|is_between, ":faction_no", kingdoms_begin, kingdoms_end),
            (eq, ":faction_no", "fac_deserters"),
            (set_background_mesh, "mesh_pic_deserters"),
          (else_try),
           ##diplmacy begin
            (eq, ":bandit_troop", "trp_peasant_woman"),
            #SB : preview actual amount of mercs
            (party_get_num_companions, reg8, "$current_town"),
            (party_count_members_of_type, ":amount", "$current_town", "trp_farmer"),
            (val_sub, reg8, ":amount"),
            (party_count_members_of_type, ":amount", "$current_town", "trp_peasant_woman"),
            (val_sub, reg8, ":amount"),
            (str_store_string, s6, "@ The peasants {reg8?hired {reg8} mercenaries and :}are rebelling against you."),
            (set_background_mesh, "mesh_pic_villageriot"),
          (else_try),
           ##diplomacy end
            (set_background_mesh, "mesh_pic_bandits"),
          (try_end),
        (else_try),
          (this_or_next|party_slot_eq, "$current_town", slot_village_state, svs_looted),
          (party_slot_eq, "$current_town", slot_village_state, svs_deserted),
          (str_store_string, s6, "@ The village has been looted. A handful of souls scatter as you pass through the burnt out houses."),
          (try_begin),
            (neq, "$g_player_raid_complete", 1),
            (play_track, "track_empty_village", 1),
          (try_end),
          (set_background_mesh, "mesh_pic_looted_village"),
        (else_try),
          (party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
          (str_store_string, s6, "@ The village is being raided."),
        (else_try), #SB : script call
          (call_script, "script_set_town_picture"),
        (try_end),

        (try_begin),
          (eq, "$g_player_raid_complete", 1),
          (try_begin), #SB : branching menu
            (party_slot_eq, "$current_town", slot_village_state, svs_looted),
            (jump_to_menu, "mnu_village_loot_complete"),
          (else_try), #stay on this menu
            (party_slot_eq, "$current_town", slot_village_state, svs_deserted),
            (jump_to_menu, "mnu_village_enslave_complete"),
          (try_end),
          (assign, "$g_player_raid_complete", 0),
          #SB : reinforce quest state
          (try_begin),
            (check_quest_active, "qst_hunt_down_fugitive"),
            (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
            (quest_set_slot, "qst_hunt_down_fugitive", slot_quest_current_state, 3),
          (try_end),
        (else_try),
          (party_get_slot, ":raider_party", "$current_town", slot_village_raided_by),
          (gt, ":raider_party", 0),
        # Process here...
        (try_end),

        (try_begin),
          (eq,"$g_leave_town",1),
          (assign,"$g_leave_town",0),
          (change_screen_return),
        (try_end),

        (try_begin),
          (store_time_of_day, ":cur_hour"),
          (ge, ":cur_hour", 5),
          (lt, ":cur_hour", 21),
          (assign, "$town_nighttime", 0),
        (else_try),
          (assign, "$town_nighttime", 1),
        (try_end),
    ],
    [
      ("village_manage",
      [
        (call_script, "script_cf_village_normal_cond", "$current_town"), #SB : script condition
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player")
        ]
       ,"Manage this village.",
       [
           (assign, "$g_next_menu", "mnu_village"),
           (jump_to_menu, "mnu_center_manage"),
        ]),
      ("recruit_volunteers",
      [
        (call_script, "script_cf_village_recruit_volunteers_cond"),
       ]
       ,"Recruit Volunteers.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (jump_to_menu, "mnu_recruit_volunteers"),
         (try_end),
        ]),
      ("village_center",[(call_script, "script_cf_village_normal_cond", "$current_town"), #SB : script condition
       ]
       ,"Go to the village center.",
       [
          (try_begin),
            (call_script, "script_cf_enter_center_location_bandit_check"),
          (else_try),
            (party_get_slot, ":village_scene", "$current_town", slot_castle_exterior),
            (modify_visitors_at_site,":village_scene"),
            (reset_visitors),
            (party_get_slot, ":village_elder_troop", "$current_town",slot_town_elder),
            (set_visitor, 11, ":village_elder_troop"),
            ##diplomacy begin
            (try_begin),
              (gt, "$g_player_chamberlain", 0),
              (call_script, "script_dplmc_appoint_chamberlain"),  #fix for wrong troops after update
              (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
              (eq, ":town_lord", "trp_player"),
              (set_visitor, 9, "$g_player_chamberlain"),
            (try_end),
            ##diplomacy end


           (call_script, "script_init_town_walkers"),

           (try_begin),
             (check_quest_active, "qst_hunt_down_fugitive"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
             (neg|check_quest_concluded, "qst_hunt_down_fugitive"), #SB : other condition
             (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
             (neg|check_quest_failed, "qst_hunt_down_fugitive"),
             (set_visitor, 45, "trp_fugitive"),
           (try_end),

           (set_jump_mission,"mt_village_center"),
           (jump_to_scene,":village_scene"),
           (change_screen_mission),
         (try_end),
        ],"Door to the village center."),
       ##diplomacy begin
      ("dplmc_village_elder_meeting",[
         (call_script, "script_cf_village_normal_cond", "$current_town"), #SB : conditional check
	   ##diplomacy start+
		#rubik had a good idea: only enable this after having met the village elder
		(party_get_slot, ":village_elder_troop", "$current_town",slot_town_elder),
		(gt, ":village_elder_troop", 0),
		(this_or_next|eq, "$cheat_mode", 1),#Always can jump to village elder in cheat mode
		(this_or_next|neq, "$cheat_mode", 1),#rubik's idea was crap, ALWAYS allow player to meet village elder
#		(this_or_next|eq, "$players_kingdom", "$g_encountered_party_faction"), #allow when member
        (troop_slot_ge,":village_elder_troop", slot_troop_met, 1),
		##diplomacy end+
       ]
       ,"Meet the Village Elder.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (party_get_slot, ":village_scene", "$current_town", slot_castle_exterior),
           (modify_visitors_at_site,":village_scene"),
           (reset_visitors),
           (party_get_slot, ":village_elder_troop", "$current_town",slot_town_elder),
           (set_visitor, 11, ":village_elder_troop"),
           (try_begin), #SB : supporting village_elder_found_chamberlain dialog option
              (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
              (eq, "$g_player_chamberlain", "trp_dplmc_chamberlain"),
              (set_visitor, 9, "$g_player_chamberlain"),
           (try_end),

           (set_jump_mission,"mt_village_center"),
           (jump_to_scene,":village_scene"),
           (change_screen_map_conversation, ":village_elder_troop"),
         (try_end),
        ]),
      ##diplomacy end
	##diplomacy start+
	#If you can't jump to the village elder, explain why
    ("dplmc_village_elder_meeting_denied",
	[
		#Only show this when the player would get the rest of the village menus
        (call_script, "script_cf_village_normal_cond", "$current_town"), #SB : script condition
	    #There is a valid village elder, and you haven't met him,
		#and there isn't another condition that enables the jump.
		(party_get_slot, ":village_elder_troop", "$current_town",slot_town_elder),
		(gt, ":village_elder_troop", 0),
		(eq, "$cheat_mode", 0),
		(troop_slot_eq, ":village_elder_troop", slot_troop_met, 0),
		(disable_menu_option),
		],
       "You have not met the village elder yet.",
       [
     ]),
	 ##diplomacy end+
      ("village_buy_food",[(party_slot_eq, "$current_town", slot_village_state, svs_normal),
                           (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
                           ],"Buy supplies from the peasants.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),

      #(try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
        #(store_sub, ":cur_good_price_slot", ":cur_goods", trade_goods_begin),
        #(val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
		#(party_get_slot, ":cur_price", "$current_town", ":cur_good_price_slot"),
	    #(call_script, "script_center_get_production", "$current_town", ":cur_goods"),
        #(assign, reg13, reg0),
	    #(call_script, "script_center_get_consumption", "$current_town", ":cur_goods"),
        #(str_store_party_name, s1, "$current_town"),
        #(str_store_item_name, s2, ":cur_goods"),
		#(assign, reg16, ":cur_price"),
        #(display_log_message, "@DEBUG:{s1}-{s2}, prd: {reg13}, con: {reg0}, raw: {reg1}, cns: {reg2}, fee: {reg16}"),
	  #(try_end),

           (change_screen_trade, ":merchant_troop"),
         (try_end),
         ]),
##diplomacy start+
#Import rubik's Auto-Sell options from Custom Commander
      ("dplmc_village_auto_sell",
        [
        (party_slot_eq, "$current_town", slot_village_state, svs_normal),
        (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
        (party_get_slot, ":village_elder_troop", "$current_town", slot_town_elder),
        (ge, ":village_elder_troop", 0),
        ],
       "Sell items automatically.",
       [
          (assign, "$g_next_menu", "mnu_village"),
          (jump_to_menu,"mnu_dplmc_trade_auto_sell_begin"),
        ]),

      ("dplmc_village_auto_buy_food",
        [
        (party_slot_eq, "$current_town", slot_village_state, svs_normal),
        (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
        (party_get_slot, ":village_elder_troop", "$current_town", slot_town_elder),
        (ge, ":village_elder_troop", 0),
        ],
       "Buy food automatically.",
       [
          (assign, "$g_next_menu", "mnu_village"),
          (jump_to_menu,"mnu_dplmc_trade_auto_buy_food_begin"),
        ]),
##diplomacy end+
      ("village_attack_bandits",[
        (party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
        ##diplomacy begin
        (neg|party_slot_eq, "$current_town", slot_village_infested_by_bandits, "trp_peasant_woman"),
        ##diplmacy end
        ],
       "Attack the bandits.",
       [(party_get_slot, ":bandit_troop", "$current_town", slot_village_infested_by_bandits),
        (party_get_slot, ":scene_to_use", "$current_town", slot_castle_exterior),
        (modify_visitors_at_site,":scene_to_use"),
        (reset_visitors),
        (set_visitors, 0, ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),
        (set_visitors, 2, "trp_farmer", "$qst_eliminate_bandits_infesting_village_num_villagers"),
        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission,"mt_village_attack_bandits"),
        (jump_to_scene, ":scene_to_use"),
        (assign, "$g_next_menu", "mnu_village_infest_bandits_result"),
        (jump_to_menu, "mnu_battle_debrief"),
        (assign, "$g_mt_mode", vba_normal),
        (change_screen_mission),
        ]),

      ("village_wait",
       [(party_slot_eq, "$current_town", slot_center_has_manor, 1),
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
        ],
         "Wait here for some time.",
         [
           (assign,"$auto_enter_town","$current_town"),
           (assign, "$g_last_rest_center", "$current_town"),

           (try_begin),
             (party_is_active, "p_main_party"),
             (party_get_current_terrain, ":cur_terrain", "p_main_party"),
             (try_begin),
               (eq, ":cur_terrain", rt_desert),
               (unlock_achievement, ACHIEVEMENT_SARRANIDIAN_NIGHTS),
             (try_end),
           (try_end),

           (rest_for_hours_interactive, 24 * 7, 5, 1), #rest while attackable

           (change_screen_return),
          ]),

       ##diplomacy begin
      ("dplmc_village_counter_insurgency",[
        (party_slot_eq, "$current_town", slot_village_infested_by_bandits, "trp_peasant_woman"),
        ],
       "Counter the insurgency.",
       [
          (store_random_in_range, ":enmity", -10, -5),
          (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
          (call_script, "script_calculate_battle_advantage"),
          (set_battle_advantage, reg0),
          (set_party_battle_mode),
          (assign, "$g_battle_result", 0),
          (assign, "$g_village_raid_evil", 1), #check
          (set_jump_mission,"mt_village_raid"),
          (party_get_slot, ":scene_to_use", "$current_town", slot_castle_exterior),
          (jump_to_scene, ":scene_to_use"),
          (assign, "$g_next_menu", "mnu_dplmc_village_riot_result"),

          # (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),
          #SB : more appropriate message for tax rebels
          (call_script, "script_objectionable_action", tmt_humanitarian, "str_repress_farmers"),
          (jump_to_menu, "mnu_battle_debrief"),
          (change_screen_mission),
        ]),

      ("dplmc_village_negotiate",[
        (party_slot_eq, "$current_town", slot_village_infested_by_bandits, "trp_peasant_woman"),
        ],
       "Begin negotiations.",
       [
          (jump_to_menu, "mnu_dplmc_riot_negotiate"),
        ]),
        ##diplomacy end

      ("collect_taxes_qst",[(party_slot_eq, "$current_town", slot_village_state, svs_normal),
                            (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
                            (check_quest_active, "qst_collect_taxes"),
                            (quest_get_slot, ":quest_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
                            (quest_slot_eq, "qst_collect_taxes", slot_quest_target_center, "$current_town"),
                            (neg|quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 4),
                            (str_store_troop_name, s1, ":quest_giver_troop"),
                            (quest_get_slot, reg5, "qst_collect_taxes", slot_quest_current_state),
                            ], "{reg5?Continue collecting taxes:Collect taxes} due to {s1}.",
       [(jump_to_menu, "mnu_collect_taxes"),]),

      ("train_peasants_against_bandits_qst",
       [
         (party_slot_eq, "$current_town", slot_village_state, svs_normal),
         (check_quest_active, "qst_train_peasants_against_bandits"),
         (neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
         (quest_slot_eq, "qst_train_peasants_against_bandits", slot_quest_target_center, "$current_town"),
         ], "Train the peasants.",
       [(jump_to_menu, "mnu_train_peasants_against_bandits"),]),

      ("village_hostile_action",[(party_slot_eq, "$current_town", slot_village_state, svs_normal),
                                 (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
                                 (party_slot_ge, "$current_town", slot_center_player_relation, -1), #relationship check, non-negative
                                 (check_quest_active, "qst_hunt_down_fugitive"),
                                 (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
                                 (neg|check_quest_concluded, "qst_hunt_down_fugitive"), #SB : other condition
                                 (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
                                 (neg|check_quest_failed, "qst_hunt_down_fugitive"),
                                 (quest_get_slot, ":quest_target_dna", "qst_hunt_down_fugitive", slot_quest_target_dna),
                                 (call_script, "script_get_name_from_dna_to_s50", ":quest_target_dna"),
								 ], "Demand to meet the family of {s50}.",
       [
       (call_script, "script_get_max_skill_of_player_party", "skl_persuasion"),
       (store_random_in_range, ":random_no", reg0, 100),
       #persuasion instead of straight out murdering everyone
       (call_script, "script_party_count_members_with_full_health","p_main_party"),
       (assign, ":player_party_size", reg0),
       (call_script, "script_party_count_members_with_full_health","$current_town"),
       (store_mul, ":villagers_party_size", reg0, 2), #twice the effective size
       (try_begin),
         (this_or_next|gt, ":random_no", 40),
         (gt, ":player_party_size", ":villagers_party_size"),
         (jump_to_menu, "mnu_village_hunt_down_fugitive_persuaded"),
       (else_try),
         (jump_to_menu,"mnu_village_start_attack"),
       (try_end),
           ]),

      ("village_hostile_action",[(party_slot_eq, "$current_town", slot_village_state, svs_normal),
                                 (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
								 (neq, "$players_kingdom", "$g_encountered_party_faction"),
								 ], "Take a hostile action.",
       [(jump_to_menu,"mnu_village_hostile_action"),
           ]),

      # ("village_reports",[(eq, "$cheat_mode", 1),], "{!}CHEAT! Show reports.",
       # [(jump_to_menu,"mnu_center_reports"),
           # ]),
      ("village_leave",[],"Leave...",[(change_screen_return,0),
	  ##diplomacy start+
	  ##Importing auto-purchase of food from rubik's Custom Commander
	  (try_begin),
		 (party_slot_eq, "$current_town", slot_village_state, svs_normal),
		 (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
		 (party_get_slot, ":merchant_troop", "$current_town",slot_town_elder),
		 (gt, ":merchant_troop", 0),
		 (call_script, "script_dplmc_initialize_autoloot", 0),#argument "0" means this does nothing if deemed unnecessary
		 (try_begin),
			(eq, "$g_dplmc_buy_food_when_leaving", 1),
			(call_script, "script_dplmc_auto_buy_food", "trp_player", ":merchant_troop"),
		 (try_end),
		 (try_begin),
			(eq, "$g_dplmc_sell_items_when_leaving", 1),
			(call_script, "script_dplmc_auto_sell", "trp_player", ":merchant_troop", "$g_dplmc_auto_sell_price_limit", all_items_begin, all_items_end, 2),
		 (try_end),
	  (try_end),
	  ##diplomacy end+
	  ]),
      #SB : consolidated cheats
      ("village_cheat", [(ge, "$cheat_mode", 1),],
      "Use cheats.",
      [(jump_to_menu, "mnu_town_cheats"),
      ]),
    ],
  ),

  (
    "village_hostile_action",0,
    "What action do you have in mind?",
    "none",
    [],
    [
      ("village_take_food",[
          (party_slot_eq, "$current_town", slot_village_state, svs_normal),
          (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
          (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
          #SB : loop break
          (assign, ":town_stores_not_empty", max_inventory_items + num_equipment_kinds),
          (try_for_range, ":slot_no", num_equipment_kinds, ":town_stores_not_empty"),
            (troop_get_inventory_slot, ":slot_item", ":merchant_troop", ":slot_no"),
            (ge, ":slot_item", 0),
            (assign, ":town_stores_not_empty", -1),
          (try_end),
          (eq, ":town_stores_not_empty", -1),
          ],"Force the peasants to give you supplies.",
       [
           (jump_to_menu, "mnu_village_take_food_confirm")
        ]),
      ("village_steal_cattle",
       [
          (party_slot_eq, "$current_town", slot_village_state, svs_normal),
          (party_slot_eq, "$current_town", slot_village_player_can_not_steal_cattle, 0),
          (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
          (party_get_slot, ":num_cattle", "$current_town", slot_village_number_of_cattle),
          (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
          (gt, ":num_cattle", 0),
          ],"Steal cattle.",
       [
           (jump_to_menu, "mnu_village_steal_cattle_confirm")
        ]),
      ("village_loot",[(party_slot_eq, "$current_town", slot_village_state, svs_normal),
                       (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
                       (store_faction_of_party, ":center_faction", "$current_town"),
                       (store_relation, ":reln", "fac_player_supporters_faction", ":center_faction"),
                       (lt, ":reln", 0),
                       ],
       "Loot and burn this village.",
       [
#           (party_clear, "$current_town"),
#           (party_add_template, "$current_town", "pt_villagers_in_raid"),
           (jump_to_menu, "mnu_village_start_attack"),
           ]),
      ("forget_it",[],
      "Forget it.",[(jump_to_menu,"mnu_village")]),
    ],
  ),

  (
    "recruit_volunteers",0,
    "{s18}",
    "none",
    [(party_get_slot, ":volunteer_troop", "$current_town", slot_center_volunteer_troop_type),
     (party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
     (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
     (store_troop_gold, ":gold", "trp_player"),
     (store_div, ":gold_capacity", ":gold", 10),#10 denars per man
     (assign, ":party_capacity", ":free_capacity"),
     (val_min, ":party_capacity", ":gold_capacity"),
     (try_begin),
       (gt, ":party_capacity", 0),
       (val_min, ":volunteer_amount", ":party_capacity"),
     (try_end),
     (assign, reg5, ":volunteer_amount"),
     (assign, reg7, 0),
     (try_begin),
       (gt, ":volunteer_amount", ":gold_capacity"),
       (assign, reg7, 1), #not enough money
     (try_end),
     (try_begin),
       (eq, ":volunteer_amount", 0),
       (str_store_string, s18, "@No one here seems to be willing to join your party."),
     (else_try),
       (store_mul, reg6, ":volunteer_amount", 10),#10 denars per man
       (str_store_troop_name_by_count, s3, ":volunteer_troop", ":volunteer_amount"),
       (try_begin),
         (eq, reg5, 1),
         (str_store_string, s18, "@One {s3} volunteers to follow you."),
       (else_try),
         (str_store_string, s18, "@{reg5} {s3} volunteer to follow you."),
       (try_end),
       (set_background_mesh, "mesh_pic_recruits"),
     (try_end),
    ],
    [


      ("continue",
      [
        (eq, reg7, 0),
        (eq, reg5, 0),
      ], #noone willing to join
      "Continue...",
      [
        (party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
        (jump_to_menu,"mnu_village"),
      ]),

      ("recruit_them",
      [
        (eq, reg7, 0),
        (gt, reg5, 0),
      ],
      "Recruit them ({reg6} denars).",
      [
        (call_script, "script_village_recruit_volunteers_recruit"),

        (jump_to_menu,"mnu_village"),
      ]),
      
      #SB : disable_menu_option
      ("continue_not_enough_gold",
      [
        (eq, reg7, 1),
        (disable_menu_option),
      ],
      "I don't have enough money...",
      [
        (jump_to_menu,"mnu_village"),
      ]),

      ("forget_it",
      [
      #SB : conditions now not applied
        # (eq, reg7, 0),
        # (gt, reg5, 0),
      ],
      "Forget it.",
      [
        (jump_to_menu,"mnu_village"),
      ]),
    ],
  ),

  (
    "village_hunt_down_fugitive_defeated",0,
    "A heavy blow from the fugitive sends you to the ground, and your vision spins and goes dark.\
 Time passes. When you open your eyes again you find yourself battered and bloody,\
 but luckily none of the wounds appear to be lethal.",
    "none",
    [
      (call_script, "script_fail_quest", "qst_hunt_down_fugitive"),
    ],
    [
      ("continue",[],"Continue...",[(jump_to_menu, "mnu_village"),
      #SB : renown loss for single target
      (call_script, "script_change_troop_renown", "trp_player", -2),
      # (party_remove_members, "$current_town", "trp_fugitive", 1),
      ]),
    ],
  ),

  (
    "village_hunt_down_fugitive_persuaded",0,
 "As the party member with the highest persuasion, {reg3?you:{s3}} managed to cajole the location of {s50} from his tight-lipped relatives. Backed with superior force of arms, your just argument seemed to take effect and the villagers grudgingly participate in the manhunt for the fugitive.\
 {reg4?But word of you arrival has reached the fugitive and he appears to have taken his own life:Within the hour, you've secured the fugitive on behalf of {s4}}.",
    "none",
    [   (call_script, "script_get_max_skill_of_player_party", "skl_persuasion"),
        (assign, ":max_skill_owner", reg1),
        (quest_get_slot, ":quest_target_dna", "qst_hunt_down_fugitive", slot_quest_target_dna),
        (call_script, "script_get_name_from_dna_to_s50", ":quest_target_dna"),
            
         #SB : tableau at bottom
         (try_begin),
           (eq, ":max_skill_owner", "trp_player"),
           (assign, reg3, 1),
         (else_try),
           (assign, reg3, 0),
           (str_store_troop_name, s3, ":max_skill_owner"),
           (call_script, "script_change_troop_renown", ":max_skill_owner", dplmc_companion_skill_renown),
         (try_end),
        
        (set_fixed_point_multiplier, 100),
        (position_set_x, pos0, 70),
        (position_set_y, pos0, 5),
        (position_set_z, pos0, 75),
        (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", ":max_skill_owner", pos0),
        (store_random_in_range, reg4, 0, 2), #TODO add some conditions, renown, time of day, etc
        (try_begin),
          (eq, reg4, 0),
          (party_force_add_prisoners, "p_main_party", "trp_fugitive", 1),
          (quest_get_slot, ":quest_giver_troop", "qst_hunt_down_fugitive", slot_quest_giver_troop),
          (str_store_troop_name, s4, ":quest_giver_troop"),
          (quest_set_slot, "qst_hunt_down_fugitive", slot_quest_current_state, 2),
        (else_try), #killed, player can claim credit
          (quest_set_slot, "qst_hunt_down_fugitive", slot_quest_current_state, 1),
        (try_end),
    ],
    
    [
      ("continue",[],"Continue...",[
        (call_script, "script_succeed_quest", "qst_hunt_down_fugitive"),
        (jump_to_menu, "mnu_village"),
        
      ]),
    ],
  ),
  
  (
    "village_infest_bandits_result",mnf_scale_picture,
    "{s9}",
    "none",
    [(try_begin),
       (eq, "$g_battle_result", 1),
       (jump_to_menu, "mnu_village_infestation_removed"),
     (else_try),
       (str_store_string, s9, "@Try as you might, you could not defeat the bandits.\
 Infuriated, they raze the village to the ground to punish the peasants,\
 and then leave the burning wasteland behind to find greener pastures to plunder."),
       (set_background_mesh, "mesh_pic_looted_village"),
     (try_end),
    ],
    [
      ("continue",[],"Continue...",
       [(party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
        (call_script, "script_village_set_state",  "$current_town", svs_looted),
        (party_set_slot, "$current_town", slot_village_raid_progress, 0),
        (party_set_slot, "$current_town", slot_village_recover_progress, 0),
        (try_begin),
          (check_quest_active, "qst_eliminate_bandits_infesting_village"),
          (quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, "$g_encountered_party"),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -5),
          (call_script, "script_fail_quest", "qst_eliminate_bandits_infesting_village"),
          (call_script, "script_end_quest", "qst_eliminate_bandits_infesting_village"),
        (else_try),
          (check_quest_active, "qst_deal_with_bandits_at_lords_village"),
          (quest_slot_eq, "qst_deal_with_bandits_at_lords_village", slot_quest_target_center, "$g_encountered_party"),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -4),
          (call_script, "script_fail_quest", "qst_deal_with_bandits_at_lords_village"),
          (call_script, "script_end_quest", "qst_deal_with_bandits_at_lords_village"),
        (else_try),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
        (try_end),
        (jump_to_menu, "mnu_village"),]),
    ],
  ),


  (
    "village_infestation_removed",mnf_disable_all_keys,
    "In a battle worthy of song, you and your men drive the bandits out of the village, making it safe once more.\
 The villagers have little left in the way of wealth after their ordeal, but they offer you {reg10?all they can find:a few heads of cattle}.",
    "none",
    [(party_get_slot, ":bandit_troop", "$g_encountered_party", slot_village_infested_by_bandits),
     (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
     (party_clear, "p_temp_party"),
     (party_add_members, "p_temp_party", ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),
     #SB : tweaked player contribution by whether village is the same faction
     (try_begin),
       (eq, "$players_kingdom", "$g_encountered_party_faction"),
       (assign, "$g_strength_contribution_of_player", 65),
     (else_try),
       (assign, "$g_strength_contribution_of_player", 50),
     (try_end),
     (call_script, "script_party_give_xp_and_gold", "p_temp_party"),
     (try_begin),
       (check_quest_active, "qst_eliminate_bandits_infesting_village"),
       (quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, "$g_encountered_party"),
       (call_script, "script_end_quest", "qst_eliminate_bandits_infesting_village"),
       #Add quest reward
       (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 5),
     (else_try),
       (check_quest_active, "qst_deal_with_bandits_at_lords_village"),
       (quest_slot_eq, "qst_deal_with_bandits_at_lords_village", slot_quest_target_center, "$g_encountered_party"),
       (call_script, "script_succeed_quest", "qst_deal_with_bandits_at_lords_village"),
       (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
     (else_try),
     #Add normal reward
       (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 4),
     (try_end),

     (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
     #SB : calculate amount of merchandise remaining
     (assign, ":num_items", 0),
     (try_for_range, ":slot_no", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
        (store_random_in_range, ":rand", 0, 100),
        (lt, ":rand", 70),
        (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
     (else_try),
        (troop_get_inventory_slot, ":item_no", ":merchant_troop", ":slot_no"),
        (gt, ":item_no", 0),
        (item_get_type, ":itp", ":item_no"),
        (eq, ":itp", itp_type_goods),
        (val_add, ":num_items", 1),
     (try_end),
     #SB : check before we disappoint the player
       # (store_free_inventory_capacity, ":capacity", ":merchant_troop"),
       # (eq, ":capacity", max_inventory_items),
     (assign, reg10, ":num_items"),
     #SB : background mesh
     #(set_background_mesh, "mesh_pic_mb_warrior_3"), #dckplmc - obscures text
    ],
    [
    #SB : add other option
      # ("village_bandits_defeated_accept_cattle",[(eq, reg10, 1)],"Looks like meat's back on the menu.",[(jump_to_menu, "mnu_village"),
                                                                         # (call_script, "script_create_cattle_herd", "$current_town", 1),
                                                                       # ]),
      ("village_bandits_defeated_accept",[],"Take it as your just due.",[(jump_to_menu, "mnu_village"),
                                                                         (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
                                                                         (troop_sort_inventory, ":merchant_troop"),
                                                                         (try_begin),
                                                                           (gt, reg10, 0),
                                                                           (change_screen_loot, ":merchant_troop"),
                                                                         (else_try), #arbitrary amount
                                                                           (store_random_in_range, reg10, 2, 5),
                                                                           (call_script, "script_create_cattle_herd", "$current_town", reg10),
                                                                         (try_end),
                                                                       ]),

      ("village_bandits_defeated_cont",[],  "Refuse, stating that they need these items more than you do.",
      [ 
        (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
        (call_script, "script_change_player_honor", 1),
        (jump_to_menu, "mnu_village")]),
    ],
  ),

  (
    "center_manage",0,
    "{s19}^{reg6?^^You are\
 currently building {s7}. The building will be completed after {reg8} day{reg9?s:}.:}",
    "none",
    [(assign, ":num_improvements", 0),
     (str_clear, s18),
     #SB : spt strings
     (try_begin),
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
       (assign, ":begin", village_improvements_begin),
       (assign, ":end", village_improvements_end),
       (str_store_string, s17, "@village"),
     (else_try),
       (assign, ":begin", walled_center_improvements_begin),
       (assign, ":end", walled_center_improvements_end),
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
       (str_store_string, s17, "@town"),
     (else_try),
       (str_store_string, s17, "@castle"),
     (try_end),

     (try_for_range, ":improvement_no", ":begin", ":end"),
       (party_slot_ge, "$g_encountered_party", ":improvement_no", 1),
       (val_add,  ":num_improvements", 1),
       (call_script, "script_get_improvement_details", ":improvement_no"),
       (try_begin),
         (eq,  ":num_improvements", 1),
         (str_store_string_reg, s18, s0),
       (else_try),
         (str_store_string, s18, "@{!}{s18}, {s0}"),
       (try_end),
     (try_end),

     (try_begin),
       (eq,  ":num_improvements", 0),
       (str_store_string, s19, "@The {s17} has no improvements."),
     (else_try),
       (str_store_string, s19, "@The {s17} has the following improvements:{s18}."),
     (try_end),

     (assign, reg6, 0),
     (try_begin),
       (party_get_slot, ":cur_improvement", "$g_encountered_party", slot_center_current_improvement),
       (gt, ":cur_improvement", 0),
       (call_script, "script_get_improvement_details", ":cur_improvement"),
       (str_store_string, s7, s0),
       (assign, reg6, 1),
       (store_current_hours, ":cur_hours"),
       (party_get_slot, ":finish_time", "$g_encountered_party", slot_center_improvement_end_hour),
       (val_sub, ":finish_time", ":cur_hours"),
       (store_div, reg8, ":finish_time", 24),
       (val_max, reg8, 1),
       (store_sub, reg9, reg8, 1),
     (try_end),
    ],
    [
      ("center_build_manor",[(eq, reg6, 0),
                             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                             (party_slot_eq, "$g_encountered_party", slot_center_has_manor, 0),
                                  ],
       "Build a manor.",[(assign, "$g_improvement_type", slot_center_has_manor),
                         (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_fish_pond",[(eq, reg6, 0),
                                 (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                 (party_slot_eq, "$g_encountered_party", slot_center_has_fish_pond, 0),
                                  ],
       "Build a mill.",[(assign, "$g_improvement_type", slot_center_has_fish_pond),
                             (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_watch_tower",[(eq, reg6, 0),
                                   (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                   (party_slot_eq, "$g_encountered_party", slot_center_has_watch_tower, 0),
                                  ],
       "Build a watch tower.",[(assign, "$g_improvement_type", slot_center_has_watch_tower),
                               (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_school",[(eq, reg6, 0),
                              (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                              (party_slot_eq, "$g_encountered_party", slot_center_has_school, 0),
                                  ],
       "Build a school.",[(assign, "$g_improvement_type", slot_center_has_school),
                          (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_messenger_post",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_messenger_post, 0),
                                       ],
       "Build a messenger post.",[(assign, "$g_improvement_type", slot_center_has_messenger_post),
                                  (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_prisoner_tower",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_prisoner_tower, 0),
                                       ],
       "Build a prisoner tower.",[(assign, "$g_improvement_type", slot_center_has_prisoner_tower),
                                  (jump_to_menu, "mnu_center_improve"),]),

      #SB: cancel current improvement
      ("center_cancel_build",[(eq, reg6, 1),],
      "Cancel building the {s7}.",[
        (call_script, "script_change_center_prosperity", "$current_town", -4),
        (call_script, "script_change_player_relation_with_center", "$current_town", -2),
        (party_set_slot, "$current_town", slot_center_current_improvement, 0),
        (party_set_slot, "$current_town", slot_village_recover_progress, 0),
        (party_get_slot, ":hours_left", "$current_town", slot_center_improvement_end_hour),

        #reinvest in economy, not household possessions
        # (party_get_slot, ":cur_wealth", "$current_town", slot_town_wealth),
        (try_begin),
          (is_between, "$current_town", towns_begin, towns_end),
          (party_get_slot, ":merchant_troop", "$current_town", slot_town_merchant),
          (troop_add_gold, ":merchant_troop", ":hours_left"),
        (else_try),
          (is_between, "$current_town", villages_begin, villages_end),
          (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
        (else_try),
          (assign, ":merchant_troop", -1),
        (try_end),
        
        (store_current_hours, ":cur_hours"),
        (val_sub, ":hours_left", ":cur_hours"),
        (val_mul, ":hours_left", 15), #a paltry sum
        (try_begin),
          (gt, ":merchant_troop", 0),
          (troop_add_gold, ":merchant_troop", ":hours_left"),
        (else_try), #castle has no seneschal
          (party_get_slot, ":cur_gold", "$current_town", slot_center_accumulated_tariffs),
          (val_add, ":cur_gold", ":hours_left"),
          (party_set_slot, "$current_town", slot_center_accumulated_tariffs, ":cur_gold"),
        (try_end),
        (jump_to_menu, "$g_next_menu"),
        ]),
      ("go_back_dot",[],"Go back.",[(jump_to_menu, "$g_next_menu")]),
    ],
  ),

  (
    "center_improve",0,
    "{s19} As the party member with the highest engineer skill ({reg2}), {reg3?you reckon:{s3} reckons} that building the {s4} will cost you\
 {reg5} denars and will take {reg6} days.",
    "none",
    [#SB : town pictures
     (call_script, "script_set_town_picture"),
     (call_script, "script_get_improvement_details", "$g_improvement_type"),
     (assign, ":improvement_cost", reg0),
     (str_store_string, s4, s0),
     (str_store_string, s19, s1),
     (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),

     (store_sub, ":multiplier", 20, ":max_skill"),
     (val_mul, ":improvement_cost", ":multiplier"),
     (val_div, ":improvement_cost", 20),

     (store_div, ":improvement_time", ":improvement_cost", 100),
     (val_add, ":improvement_time", 3),

     (assign, reg5, ":improvement_cost"),
     (assign, reg6, ":improvement_time"),

     #SB : tableau at bottom
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
    
    #SB : assign globals to be safe
    (assign, "$diplomacy_var", ":improvement_cost"),
    (assign, "$diplomacy_var2", ":improvement_time"),
    (assign, "$lord_selected", ":max_skill_owner"),
    (set_fixed_point_multiplier, 100),
    (position_set_x, pos0, 70),
    (position_set_y, pos0, 5),
    (position_set_z, pos0, 75),
    (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", ":max_skill_owner", pos0),
    ],
    [
      ##diplomacy begin
      ("dplmc_improve_cont",
      [
        (gt, "$g_player_chamberlain", 0),
        (store_troop_gold, ":cur_gold", "trp_household_possessions"),
        (ge, ":cur_gold", "$diplomacy_var"),
      ], "Go on. (Pay from treasury)",
        [
          (call_script, "script_dplmc_withdraw_from_treasury", "$diplomacy_var"),
          # (call_script, "script_get_max_skill_of_player_party", "skl_engineer"), #SB : re-fetch skill
          (call_script, "script_improve_center", "$g_encountered_party", "$lord_selected", "$diplomacy_var2"),
          (jump_to_menu,"mnu_center_manage"),
         ]
      ),
      ("improve_not_enough_gold",[(gt, "$g_player_chamberlain", 0),
                                  (store_troop_gold, ":cur_gold", "trp_household_possessions"),
                                  (lt, ":cur_gold", "$diplomacy_var"),
                                  #SB : disable_menu_option
                                  (disable_menu_option)],
       "Insufficient fund in the treasury.", []),
      ##diplomacy end
      
      ("improve_cont",[(store_troop_gold, ":cur_gold", "trp_player"),
                       (ge, ":cur_gold", "$diplomacy_var")],
       "Go on.", [
                  (try_begin), #fast build
                    (ge, "$cheat_mode", 1),
                    (assign, "$diplomacy_var2", 0),
                  (else_try),
                    (troop_remove_gold, "trp_player", "$diplomacy_var"),
                  (try_end),
                  (call_script, "script_improve_center", "$g_encountered_party", "$lord_selected", "$diplomacy_var2"),
                  (jump_to_menu,"mnu_center_manage"),
                  ]),
      ("improve_not_enough_gold",[(store_troop_gold, ":cur_gold", "trp_player"),
                                  (lt, ":cur_gold", "$diplomacy_var"),
                                  #SB : disable_menu_option
                                  (disable_menu_option)],
       "I don't have enough money for that.", []),
      ("forget_it",[], "Forget it.", [(jump_to_menu,"mnu_center_manage")]),

    ],
  ),

  (
    "town_bandits_failed",mnf_disable_all_keys,
    "{s4} {s5}",
    "none",
    [
#      (call_script, "script_loot_player_items", 0),
      (store_troop_gold, ":total_gold", "trp_player"),
      (store_div, ":gold_loss", ":total_gold", 30),
      (store_random_in_range, ":random_loss", 40, 100),
      (val_add, ":gold_loss", ":random_loss"),
      (val_min, ":gold_loss", ":total_gold"),
      (troop_remove_gold, "trp_player",":gold_loss"),
      (party_set_slot, "$current_town", slot_center_has_bandits, 0),
      (party_get_num_companions, ":num_companions", "p_main_party"),
      (str_store_string, s4, "@The assasins beat you down and leave you for dead. ."),
      (str_store_string, s4, "@You have fallen. The bandits quickly search your body for every coin they can find,\
 then vanish into the night. They have left you alive, if only barely."),
      (try_begin),
        (gt, ":num_companions", 2),
        (str_store_string, s5, "@Luckily some of your companions come to search for you when you do not return, and find you lying by the side of the road. They hurry you to safety and dress your wounds."),
      (else_try),
        (str_store_string, s5, "@Luckily some passing townspeople find you lying by the side of the road, and recognise you as something other than a simple beggar. They carry you to the nearest inn and dress your wounds."),
      (try_end),
    ],
    [
      ("continue",[],"Continue...",[(change_screen_return),
      #SB : lose renown for easy encounters
      (call_script, "script_change_troop_renown", "trp_player", -2),
      ]),
    ],
  ),

  (
    "town_bandits_succeeded",mnf_disable_all_keys,
    "The {s4} fall before you as wheat to a scythe! Soon you stand alone in the streets\
 while {reg4?most of your attackers: the bandit} lie unconscious, dead or dying.\
 Searching the {reg4?bodies:body}, you find a purse which must have belonged to a previous victim of {reg4?these brute:this lowlife}.\
 Or perhaps, it was {reg4?given to them:provided} by someone who wanted to arrange a suitable ending to your life.",
    "none",
    [
      # (party_set_slot, "$current_town", slot_center_has_bandits, 0), #we need this
      (party_get_slot, ":bandit_troop", "$current_town", slot_center_has_bandits),
      (assign, "$g_last_defeated_bandits_town", "$g_encountered_party"),
      (try_begin),
        (check_quest_active, "qst_deal_with_night_bandits"),
        (neg|check_quest_succeeded, "qst_deal_with_night_bandits"),
        (quest_slot_eq, "qst_deal_with_night_bandits", slot_quest_target_center, "$g_encountered_party"),
        (call_script, "script_succeed_quest", "qst_deal_with_night_bandits"),
      (try_end),
      #SB : variable rewards, since we have different bandits in play
      (call_script, "script_game_get_join_cost", ":bandit_troop"),
      (store_mul, ":xp_reward", "$num_center_bandits", reg0),
      (try_begin), #reduce bonus exp, since town missions troops don't use horses
        (troop_is_mounted, ":bandit_troop"),
        (val_div, ":xp_reward", 2),
      (try_end),
      (add_xp_to_troop, ":xp_reward", "trp_player"),
      (call_script, "script_game_get_upgrade_cost", ":bandit_troop"), #20, 40, 80
      (store_mul, ":gold_reward", "$num_center_bandits", reg0),
      (call_script, "script_troop_add_gold", "trp_player", ":gold_reward"),
      #SB : string setup
      (str_store_troop_name_by_count,s4, ":bandit_troop", "$num_center_bandits"),
      (store_sub, reg4, "$num_center_bandits", 1),
    ],
    [
      ("continue",[],"Continue...",[
        (party_set_slot, "$current_town", slot_center_has_bandits, 0),
        (change_screen_return),
      ]),
    ],
  ),


   (
    "village_steal_cattle_confirm",0,
    "As the party member with the highest looting skill ({reg2}), {reg3?you reckon:{s1} reckons} that you can steal as many as {reg4} heads of village's cattle.",
    "none",
    [
      (call_script, "script_get_max_skill_of_player_party", "skl_looting"),
      (assign, reg2, reg0),
      (assign, ":max_skill_owner", reg1),
      (try_begin),
        (eq, ":max_skill_owner", "trp_player"),
        (assign, reg3, 1),
      (else_try),
        (assign, reg3, 0),
        (str_store_troop_name, s1, ":max_skill_owner"),
      (try_end),
      (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
      (assign, reg4, reg0),
      ],
    [
      ("village_steal_cattle_confirm",[],"Go on.",
       [
         (rest_for_hours_interactive, 3, 5, 1), #rest while attackable
         (assign, "$auto_menu", "mnu_village_steal_cattle"),
         (change_screen_return),
       ]),
      ("forget_it",[],"Forget it.",[(change_screen_return)]),
    ],
  ),

  (
    "village_steal_cattle",mnf_disable_all_keys,
    "{s1}",
    "none",
    [
      (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
      (assign, ":max_value", reg0),
      (val_add, ":max_value", 1),
      (store_random_in_range, ":random_value", 0, ":max_value"),
      (party_set_slot, "$current_town", slot_village_player_can_not_steal_cattle, 1),
      (party_get_slot, ":lord", "$current_town", slot_town_lord),
      (try_begin),
        (le, ":random_value", 0),
        (call_script, "script_change_player_relation_with_center", "$current_town", -3),
        (str_store_string, s1, "@You fail to steal any cattle."),
      (else_try),
        (assign, reg17, ":random_value"),
        (store_sub, reg12, ":random_value", 1),
        (try_begin),
          (gt, ":lord", 0),
          (call_script, "script_change_player_relation_with_troop", ":lord", -3),
          (call_script, "script_add_log_entry", logent_player_stole_cattles_from_village, "trp_player",  "$current_town", ":lord", "$g_encountered_party_faction"),
        (try_end),
        (call_script, "script_change_player_relation_with_center", "$current_town", -5),
        (str_store_string, s1, "@You drive away {reg17} {reg12?heads:head} of cattle from the village's herd."),

        (try_begin),
          (eq, ":random_value", 3),
          (unlock_achievement, ACHIEVEMENT_GOT_MILK),
        (try_end),

        (call_script, "script_create_cattle_herd", "$current_town", ":random_value"),
        (party_get_slot, ":num_cattle", "$current_town", slot_village_number_of_cattle),
        (val_sub, ":num_cattle", ":random_value"),
        (party_set_slot, "$current_town", slot_village_number_of_cattle, ":num_cattle"),
        
        #SB : add lesser renown bonus
        (try_begin),
          (call_script, "script_get_max_skill_of_player_party", "skl_looting"),
          (neq, reg1, "trp_player"),
          (call_script, "script_change_troop_renown", reg1, dplmc_companion_skill_renown / 2),
        (try_end),        
      (try_end),
    ],
    [
      ("continue",[],"Continue...",
       [
         (change_screen_return),
         ]),
    ],
  ),


   (
    "village_take_food_confirm",0,
    "It will be difficult to force and threaten the peasants into giving their precious supplies. You think you will need at least one hour.",
    #TODO: mention looting skill?
    "none",
    [],
    [
      ("village_take_food_confirm",[],"Go ahead.",
       [
         (rest_for_hours_interactive, 1, 5, 0), #rest while not attackable
         (assign, "$auto_enter_town", "$current_town"),
         (assign, "$g_town_visit_after_rest", 1),
         (assign, "$auto_enter_menu_in_center", "mnu_village_take_food"),
         (change_screen_return),
         ]),
      ("forget_it",[],"Forget it.",[(jump_to_menu, "mnu_village_hostile_action")]),
    ],
  ),

  (
    "village_take_food",0,
    "The villagers grudgingly bring out what they have for you.",
    "none",
    [
       (call_script, "script_party_count_members_with_full_health","p_main_party"),
       (assign, ":player_party_size", reg0),
       (call_script, "script_party_count_members_with_full_health","$current_town"),
       (assign, ":villagers_party_size", reg0),
       (try_begin),
         (lt, ":player_party_size", 6),
         (ge, ":villagers_party_size", 40),
         (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
         (jump_to_menu, "mnu_village_start_attack"),
       (try_end),
    ],
    [
      ("take_supplies",[],"Take the supplies.",
       [
         (try_begin),
           (party_slot_ge, "$current_town", slot_center_player_relation, -55),
           (try_begin),
             (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
             (call_script, "script_change_player_relation_with_center", "$current_town", -1),
           (else_try),
             (call_script, "script_change_player_relation_with_center", "$current_town", -3),
           (try_end),
         (try_end),
         (party_get_slot, ":village_lord", "$current_town", slot_town_lord),
         (try_begin),
           (gt,  ":village_lord", 1),
           (call_script, "script_change_player_relation_with_troop", ":village_lord", -1),
          (try_end),
         (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
         (party_get_skill_level, ":player_party_looting", "p_main_party", "skl_looting"),
         (val_mul, ":player_party_looting", 3),
         (store_sub, ":random_chance", 70, ":player_party_looting"), #Increases the chance of looting by 3% per skill level
         (try_for_range, ":slot_no", num_equipment_kinds ,max_inventory_items + num_equipment_kinds),
           (store_random_in_range, ":rand", 0, 100),
           (lt, ":rand", ":random_chance"),
           (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
         (try_end),

###NPC companion changes begin
         (call_script, "script_objectionable_action", tmt_humanitarian, "str_steal_from_villagers"),
#NPC companion changes end
#Troop commentary changes begin
          (call_script, "script_add_log_entry", logent_village_extorted, "trp_player",  "$current_town", -1, -1),
          (store_faction_of_party,":village_faction",  "$current_town"),
          #SB : this war penalty should be lower for accosting farmers instead of raiding outright
          (call_script, "script_faction_inflict_war_damage_on_faction", "$players_kingdom", ":village_faction", 3),
#Troop commentary changes end

         #SB : sometimes this will actually be empty
         (jump_to_menu, "mnu_village"),
         (troop_sort_inventory, ":merchant_troop"),
         (change_screen_loot, ":merchant_troop"),
         ]),
      ("let_them_keep_it",[],"Let them keep it.",[(jump_to_menu, "mnu_village")]),
    ],
  ),


  ( #SB : added fugitive related strings
    "village_start_attack",mnf_disable_all_keys|mnf_scale_picture,
    "Some of the angry villagers grab their tools and prepare to resist you.\
 It looks like you'll have a fight on your hands if you continue.{s1}",
    "none",
    [
       (set_background_mesh, "mesh_pic_villageriot"),
       (call_script, "script_party_count_members_with_full_health","p_main_party"),
       (assign, ":player_party_size", reg0),
       (call_script, "script_party_count_members_with_full_health","$current_town"),
       (assign, ":villagers_party_size", reg0),

       (try_begin), #SB : tweak fight avoidance parameters
         #also if we lost but reduced their numbers, don't allow this condition to be true
         (neq, "$g_battle_result", -1),
         (this_or_next|le, ":villagers_party_size", 30),
         (gt, ":player_party_size", ":villagers_party_size"),
         (jump_to_menu, "mnu_village_loot_no_resist"),
       (else_try),
         (this_or_next|eq, ":villagers_party_size", 0),
         (eq, "$g_battle_result", 1),
         (try_begin),
           (eq, "$g_battle_result", 1),
           (store_random_in_range, ":enmity", -30, -15),
           (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
           (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
           (gt, ":town_lord", 0),
           (call_script, "script_change_player_relation_with_troop", ":town_lord", -3),
         (try_end),
         (jump_to_menu, "mnu_village_loot_no_resist"),
       (else_try),
         (eq, "$g_battle_result", -1),
         (try_begin), #if we did not knock him out or kill him, he escapes
           (check_quest_active, "qst_hunt_down_fugitive"),
           (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
           (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
           (jump_to_menu, "mnu_village_hunt_down_fugitive_defeated"),
         (else_try),
           (jump_to_menu, "mnu_village_loot_defeat"),
         (try_end),
       (try_end),
       
       #SB : display string indicating fugitive is here
      (try_begin), #if we did not knock him out or kill him, he escapes
        (check_quest_active, "qst_hunt_down_fugitive"),
        (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
        (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
        (quest_get_slot, ":quest_target_dna", "qst_hunt_down_fugitive", slot_quest_target_dna),
        (call_script, "script_get_name_from_dna_to_s50", ":quest_target_dna"),
        (str_store_string, s1, "@ From your vantage point you see a man matching the description of {s50} arming himself with a sword during the commotion. If you do not press on the fugitive will slip away!"),
      (else_try),
        (str_clear, s1),
      (try_end),
    ],
    [
      ("village_raid_attack",[],"Charge them.",[
          (store_random_in_range, ":enmity", -10, -5),
          (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
          (try_begin),
            (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
            (gt, ":town_lord", 0),
            (call_script, "script_change_player_relation_with_troop", ":town_lord", -3),
          (try_end),
          #SB : add fugitive as defender here
          (try_begin),
            (check_quest_active, "qst_hunt_down_fugitive"),
            (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
            (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
            (neg|check_quest_failed, "qst_hunt_down_fugitive"),
            (quest_set_slot, "qst_hunt_down_fugitive", slot_quest_current_state, 1), #normally this is activated in dialogs
            (party_add_members, "$current_town", "trp_fugitive", 1),
          (try_end),
          (call_script, "script_calculate_battle_advantage"),
          (set_battle_advantage, reg0),
          (set_party_battle_mode),
          (assign, "$g_battle_result", 0),
          (assign, "$g_village_raid_evil", 1),
          (set_jump_mission,"mt_village_raid"),
          (party_get_slot, ":scene_to_use", "$current_town", slot_castle_exterior),
          (jump_to_scene, ":scene_to_use"),
          (assign, "$g_next_menu", "mnu_village_start_attack"),

          (call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$g_encountered_party"),
###NPC companion changes begin
          (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),
#NPC companion changes end

          (jump_to_menu, "mnu_battle_debrief"),
          (change_screen_mission),
          ]),
      ("village_raid_leave",[],"Leave this village alone.",[(change_screen_return),
      #SB : fail fugitive quest if player backs away from demands
      (try_begin),
        (check_quest_active, "qst_hunt_down_fugitive"),
        (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
        (neg|check_quest_concluded, "qst_hunt_down_fugitive"),
        (call_script, "script_fail_quest", "qst_hunt_down_fugitive"),
      (try_end),
      
      ]),
    ],
  ),

  (
    "village_loot_no_resist",0,
    "The villagers here are few and frightened, and they quickly scatter and run before you.\
 The village is at your mercy.",
    "none",
    [
    #SB : if we just wanted to steal food, return to doing that instead of plundering
    (try_begin),
      (eq, "$auto_enter_menu_in_center", "mnu_village_take_food"),
      (jump_to_menu, "$auto_enter_menu_in_center"),
    (try_end),
    
    ],
    [
      ("village_loot",[], "Plunder the village, then raze it.",
        [
          (call_script, "script_village_set_state", "$current_town", svs_being_raided),
          (party_set_slot, "$current_town", slot_village_raided_by, "p_main_party"),
          (assign,"$g_player_raiding_village","$current_town"),

          (try_begin),
            (store_faction_of_party, ":village_faction", "$current_town"),
            (store_relation, ":relation", "$players_kingdom", ":village_faction"),
            (ge, ":relation", 0),
            (call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$current_town"),
          (try_end),

          (rest_for_hours, 3, 5, 1), #rest while attackable (3 hours will be extended by the trigger)
          (party_set_slot, "$current_town", slot_town_last_nearby_fire_time, 1), #raiding mode
          # (assign, "$g_village_raid_evil", 1), #SB : to differentiate between raiding
          (change_screen_return),
        ]),
        
        #SB : alternative option if that's your thing
      ("village_enslave", [
          (party_get_num_companions, ":amount", "$current_town"),
          (gt, ":amount", 0), #if we haven't killed them all in the first charge
          # (party_get_free_prisoners_capacity, ":capacity", "p_main_party"), #be slightly wary of this operation
          # (gt, ":capacity", 0), #if we have room
          (troops_can_join_as_prisoner, 1),
        ], "Chase after the remaining villagers and enslave them.",
        [
          (call_script, "script_village_set_state", "$current_town", svs_being_raided), #target is deserted, not looted
          (party_set_slot, "$current_town", slot_village_raided_by, "p_main_party"),
          (assign,"$g_player_raiding_village","$current_town"),

          (try_begin),
            (store_faction_of_party, ":village_faction", "$current_town"),
            (store_relation, ":relation", "$players_kingdom", ":village_faction"),
            (ge, ":relation", 0),
            (call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$current_town"),
          (try_end),
          
          #add a party template to represent hiding villagers so we don't go empty-handed
          (party_add_template, "$current_town", "pt_women"),
          (party_add_template, "$current_town", "pt_women"),
          #(party_add_template, "$current_town", "pt_village_defenders"),
          #add some smoke right away
          # (party_add_particle_system, "$current_town", "psys_map_village_fire"),

          (rest_for_hours, 3, 5, 1), #rest while attackable
          # (assign, "$g_village_raid_evil", 2),
          (party_set_slot, "$current_town", slot_town_last_nearby_fire_time, 2), #enslavement mode
          (assign, "$qst_eliminate_bandits_infesting_village_num_villagers", 0),
          (change_screen_return),
        ]),
      ("village_raid_leave",[],"Leave this village alone.",[(change_screen_return)]),
    ],
  ),
  (
    "village_loot_complete",mnf_disable_all_keys,
    "On your orders your troops sack the village, pillaging everything of any value,\
 and then put the buildings to the torch. From the coins and valuables that are found, you get your share of {reg1} denars.",
    "none",
    [
        (get_achievement_stat, ":number_of_village_raids", ACHIEVEMENT_THE_BANDIT, 0),
        (get_achievement_stat, ":number_of_caravan_raids", ACHIEVEMENT_THE_BANDIT, 1),
        (val_add, ":number_of_village_raids", 1),
        (set_achievement_stat, ACHIEVEMENT_THE_BANDIT, 0, ":number_of_village_raids"),

        (try_begin),
          (ge, ":number_of_village_raids", 3),
          (ge, ":number_of_caravan_raids", 3),
          (unlock_achievement, ACHIEVEMENT_THE_BANDIT),
        (try_end),

        (party_get_slot, ":village_lord", "$current_town", slot_town_lord),
        (try_begin),
          (gt,  ":village_lord", 0),
          (call_script, "script_change_player_relation_with_troop", ":village_lord", -5),
        (try_end),
        (store_random_in_range, ":enmity", -35, -25),
        (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),

        (store_faction_of_party, ":village_faction", "$current_town"),
        (store_relation, ":relation", ":village_faction", "fac_player_supporters_faction"),
        (try_begin),
          (lt, ":relation", 0),
          (call_script, "script_change_player_relation_with_faction", ":village_faction", -3),
        (try_end),

        (assign, ":money_gained", 50), #SB : change this to be somewhat based on actual wealth
        (party_get_slot, ":village_elder", "$current_town",slot_town_elder),
        (try_begin),
          (gt, ":village_elder", 0),
          (store_troop_gold, ":money_gained", ":village_elder"),
          (troop_remove_gold, ":village_elder", ":money_gained"),
          (val_div, ":money_gained", 2),
        (try_end),
        (val_max, ":money_gained", 50),
        (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
        (store_mul, ":prosperity_of_village_mul_5", ":prosperity", 5),
        (val_add, ":money_gained", ":prosperity_of_village_mul_5"),
        (call_script, "script_troop_add_gold", "trp_player", ":money_gained"),

        (assign, ":morale_increase", 3),
        (store_div, ":money_gained_div_100", ":money_gained", 100),
        (val_add, ":morale_increase", ":money_gained_div_100"),
        (call_script, "script_change_player_party_morale", ":morale_increase"),


        # (faction_get_slot, ":faction_morale", ":village_faction",  slot_faction_morale_of_player_troops),
        (store_mul, ":morale_decrease", ":morale_increase", -200),
        (call_script, "script_change_faction_troop_morale", ":village_faction", ":morale_decrease", 1), #SB : script call
        # (val_sub, ":faction_morale", ":morale_increase_mul_2"),
        # (faction_set_slot, ":village_faction",  slot_faction_morale_of_player_troops, ":faction_morale"),



#NPC companion changes begin
        (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),
#NPC companion changes end
        (assign, reg1, ":money_gained"),
      ],
    [
      ("continue",[], "Continue...",
       [
       (jump_to_menu, "mnu_close"),
          (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
          (assign, ":max_cattle", reg0),
          (val_mul, ":max_cattle", 3),
          (val_div, ":max_cattle", 2),
          (party_get_slot, ":num_cattle", "$current_town", slot_village_number_of_cattle),
          (val_min, ":max_cattle", ":num_cattle"),
          (val_add, ":max_cattle", 1),
          (store_random_in_range, ":random_value", 0, ":max_cattle"),
          (try_begin),
            (gt, ":random_value", 0),
            (call_script, "script_create_cattle_herd", "$current_town", ":random_value"),
            (val_sub, ":num_cattle", ":random_value"),
            (party_set_slot, "$current_town", slot_village_number_of_cattle, ":num_cattle"),
          (try_end),

          #below line changed with below lines to make plunder result more realistic. Now only items produced in bound town can be stolen after raid.
          #(reset_item_probabilities,100),

          #begin of changes
          (party_get_slot, ":bound_town", "$current_town", slot_village_bound_center),
          #the above line is the culprit for divide by zero
          # (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
          (assign, ":item_to_price_slot", slot_town_trade_good_prices_begin),
          (reset_item_probabilities,100),
          (assign, ":total_probability", 0),
          (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
            (party_get_slot, ":cur_price", ":bound_town", ":item_to_price_slot"),
            (val_add, ":item_to_price_slot", 1),
            (call_script, "script_center_get_production", ":bound_town", ":cur_goods"),
            (assign, ":cur_probability", reg0),
            (call_script, "script_center_get_consumption", ":bound_town", ":cur_goods"),
            (val_div, reg0, 3),
            (val_add, ":cur_probability", reg0),
            (val_mul, ":cur_probability", 4),
            (try_begin),
              (neq, ":cur_price", 0),
              (val_mul, ":cur_probability", average_price_factor),
              (val_div, ":cur_probability", ":cur_price"), #divide by zero error here
            (try_end),
            #first only simulation
            #(set_item_probability_in_merchandise,":cur_goods",":cur_probability"),
            (val_add, ":total_probability", ":cur_probability"),
            # (assign, reg1, ":total_probability"),
            # (assign, reg2, ":cur_price"),
            # (assign, reg3, ":cur_probability"),
            # (assign, reg4, ":item_to_price_slot"),
            # (str_store_item_name, s1, ":cur_goods"),
            # (display_message, "@{s1} price : {reg2} in slot {reg4}, probability: {reg3};{reg1} total"),
          (try_end),
          (assign, ":item_to_price_slot", slot_town_trade_good_prices_begin),
          (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
            (party_get_slot, ":cur_price", ":bound_town", ":item_to_price_slot"),
            (val_add, ":item_to_price_slot", 1),
            (call_script, "script_center_get_production", ":bound_town", ":cur_goods"),
            (assign, ":cur_probability", reg0),
            (call_script, "script_center_get_consumption", ":bound_town", ":cur_goods"),
            (val_div, reg0, 3),
            (val_add, ":cur_probability", reg0),
            (val_mul, ":cur_probability", 4),
            (try_begin),
              (neq, ":cur_price", 0),
              (val_mul, ":cur_probability", average_price_factor),
              (val_div, ":cur_probability", ":cur_price"), #divide by zero error here
            (try_end),

            (val_mul, ":cur_probability", num_merchandise_goods),
            (val_mul, ":cur_probability", 100),
            (val_div, ":cur_probability", ":total_probability"),

            (set_item_probability_in_merchandise,":cur_goods",":cur_probability"),
          (try_end),
          #end of changes

          (troop_add_merchandise,"trp_temp_troop",itp_type_goods,30),
          (troop_sort_inventory, "trp_temp_troop"),
          (change_screen_loot, "trp_temp_troop"),
        ]),
    ],
  ),

  (
    "village_enslave_complete",mnf_disable_all_keys,
    "On your orders your troops rampage through the village, dragging peasants from their hovels and stripping them of all possessions.\
 In the span of a few hours you've rounded up {reg1} prisoners, leaving the infirm and the younglings behind. As you march the trussed-up villagers away from the cooling ember of their broken hearths, you hear a distant howl...",
    "none",
    [
        (get_achievement_stat, ":number_of_village_raids", ACHIEVEMENT_THE_BANDIT, 0),
        (get_achievement_stat, ":number_of_caravan_raids", ACHIEVEMENT_THE_BANDIT, 1),
        (val_add, ":number_of_village_raids", 1),
        (set_achievement_stat, ACHIEVEMENT_THE_BANDIT, 0, ":number_of_village_raids"),

        (try_begin),
          (ge, ":number_of_village_raids", 3),
          (ge, ":number_of_caravan_raids", 3),
          (unlock_achievement, ACHIEVEMENT_THE_BANDIT),
        (try_end),
        
        (set_background_mesh, "mesh_pic_prisoner_wilderness"),
        (call_script, "script_objectionable_action", tmt_humanitarian, "str_sell_slavery"),

        # (party_get_slot, ":village_lord", "$current_town", slot_town_lord),
        # (try_begin),
          # (gt,  ":village_lord", 0),
          # (call_script, "script_change_player_relation_with_troop", ":village_lord", -5),
        # (try_end),
        (store_random_in_range, ":enmity", -35, -25),
        (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
        
        (party_add_particle_system, "$current_town", "psys_map_village_looted_smoke"),
        (store_faction_of_party, ":village_faction", "$current_town"),
        (store_relation, ":relation", ":village_faction", "fac_player_supporters_faction"),
        (try_begin),
          (lt, ":relation", 0),
          (call_script, "script_change_player_relation_with_faction", ":village_faction", -2),
        (try_end),

        (store_mul, ":morale_decrease", "$qst_eliminate_bandits_infesting_village_num_villagers", -150),
        (call_script, "script_change_faction_troop_morale", ":village_faction", ":morale_decrease", 1), #SB : script call
        (assign, reg1, "$qst_eliminate_bandits_infesting_village_num_villagers"),
      ],
    [
      ("continue",[], "Continue...",
       [
            (assign, "$g_leave_town", 1),
            (jump_to_menu, "mnu_village"),
        ]),
    ],
  ),

  (
    "village_loot_defeat",mnf_scale_picture,
    "Fighting with courage and determination, the villagers manage to hold together and drive off your forces.",
    "none",
    [
        (set_background_mesh, "mesh_pic_villageriot"),
    ],
    [
      ("continue",[],"Continue...",[(change_screen_return),
      #SB : renown loss
      (call_script, "script_change_troop_renown", "trp_player", -3),
      ]),
    ],
  ),

  (
    "village_loot_continue",0,
    "Do you wish to continue looting this village?",
    "none",
    [
    (set_background_mesh, "mesh_pic_looted_village"),
    ],
    [
      ("loot_yes",[],"Yes.",[ (rest_for_hours, 3, 5, 1), #rest while attackable (3 hours will be extended by the trigger)
                              #SB : resume hostilities
                              (call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$current_town"),
                              (change_screen_return),
                              ]),
      ("loot_no",[],"No.",[(call_script, "script_village_set_state", "$current_town", 0),
                            (party_set_slot, "$current_town", slot_village_raided_by, -1),
                            (assign, "$g_player_raiding_village", 0),
                            (assign, "$g_village_raid_evil", 0), #SB : reset global
                            (party_set_slot, "$current_town", slot_town_last_nearby_fire_time, 0),
                            (change_screen_return)]),
    ],
  ),

  (
    "close",0,
    "Nothing.",
    "none",
    [
        (change_screen_return),
      ],
    [],
  ),

  (
    "town",mnf_enable_hot_keys|mnf_scale_picture,
    "{s10} {s14}^{s11}{s12}{s13}",
    "none",
    [
        (try_begin),
          (gt, "$sneaked_into_town", disguise_none),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
        (else_try),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
        (try_end),
        (store_encountered_party, "$current_town"),
        (call_script, "script_update_center_recon_notes", "$current_town"),
        (assign, "$g_defending_against_siege", 0),
        (str_clear, s3),
        (party_get_battle_opponent, ":besieger_party", "$current_town"),
        (store_faction_of_party, ":encountered_faction", "$g_encountered_party"),
        (store_relation, ":faction_relation", ":encountered_faction", "fac_player_supporters_faction"),
        (try_begin),
          (gt, ":besieger_party", 0),
          (ge, ":faction_relation", 0),
          (store_faction_of_party, ":besieger_party_faction", ":besieger_party"),
          (store_relation, ":besieger_party_relation", ":besieger_party_faction", "fac_player_supporters_faction"),
          (lt, ":besieger_party_relation", 0),
          (assign, "$g_defending_against_siege", 1),
          (assign, "$g_siege_first_encounter", 1),
          (jump_to_menu, "mnu_siege_started_defender"),
        (try_end),

        (try_begin),
          (is_between, "$g_encountered_party", towns_begin, towns_end),
          (store_sub, ":encountered_town_no", "$g_encountered_party", towns_begin),
          (set_achievement_stat, ACHIEVEMENT_MIGRATING_COCONUTS, ":encountered_town_no", 1),

          (assign, ":there_are_villages_not_visited", 0),
          (try_for_range, ":cur_town", towns_begin, towns_end),
            (store_sub, ":encountered_town_no", ":cur_town", towns_begin),
            (get_achievement_stat, ":town_is_visited", ACHIEVEMENT_MIGRATING_COCONUTS, ":encountered_town_no"),
            (eq, ":town_is_visited", 0),
            (assign, ":there_are_villages_not_visited", 1),
          (try_end),

          (try_begin),
            (eq, ":there_are_villages_not_visited", 0),
            (unlock_achievement, ACHIEVEMENT_MIGRATING_COCONUTS),
          (try_end),
        (try_end),

        #Quest menus

        (assign, "$qst_collect_taxes_currently_collecting", 0),

        (try_begin),
          (gt, "$quest_auto_menu", 0),
          (jump_to_menu, "$quest_auto_menu"),
          (assign, "$quest_auto_menu", 0),
        (try_end),

        (try_begin),
##          (eq, "$g_center_under_siege_battle", 1),
##          (jump_to_menu,"mnu_siege_started_defender"),
##        (else_try),
          (eq, "$g_town_assess_trade_goods_after_rest", "$current_town"), #SB : loop fix
          (assign, "$g_town_assess_trade_goods_after_rest", 0),
          (jump_to_menu,"mnu_town_trade_assessment"),
        (try_end),

        (assign, "$talk_context", 0),
        (assign,"$all_doors_locked",0),

        (try_begin),
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
          (assign, "$town_entered", 1),
        (try_end),

        (try_begin),
          (eq,"$g_leave_town",1),
          (assign,"$g_leave_town",0),
          (assign,"$g_permitted_to_center",0),
          
          #SB : handle disguise removal here or in trigger
          
          
          (leave_encounter),
          (change_screen_return),
        (try_end),

        (str_store_party_name, s2, "$current_town"),
        (party_get_slot, ":center_lord", "$current_town", slot_town_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name, s9, ":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8,":center_lord"),
          (str_store_string,s7,"@{s8} of {s9}"),
        (try_end),

        (try_begin),
          (party_slot_eq,"$current_town",slot_party_type, spt_town),

          (str_store_string, s60, s2),

          (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
          (try_begin),
            (ge, "$cheat_mode", 1),
            (assign, reg4, ":prosperity",),
            (display_message, "@{!}DEBUG -- Prosperity: {reg4}"),
          (try_end),

     #          (val_add, ":prosperity", 5),
          (store_div, ":str_id", ":prosperity", 10),
          (val_min, ":str_id", 9),
          (val_add, ":str_id", "str_town_prosperity_0"),
          (str_store_string, s10, ":str_id"),

          (store_div, ":str_id", ":prosperity", 20),
          (val_min, ":str_id", 4),
          (val_add, ":str_id", "str_town_alt_prosperity_0"),

          (str_store_string, s14, ":str_id"),


        (else_try),
          (str_clear, s14),
          (str_store_string,s10,"@You are at {s2}."),
        (try_end),
        ##diplomacy start+
        (assign, ":save_reg0", reg0),#save variables
        (assign, ":save_reg4", reg4),
        (assign, reg0, 0),
        (assign, reg4, 0),
        (try_begin),#If there's a relation of some kind, write it to s11 (which we'll overwrite below)
            (lt, ":center_lord", 1),
        (else_try),
            #your relative
            (call_script, "script_troop_get_family_relation_to_troop", ":center_lord", "trp_player"),#outputs to s11, reg0, and reg4
            (ge, reg0, 1),#Fall through if this not a relative
        (else_try),
            #your current liege
            (eq, ":center_faction", "$players_kingdom"),
            (is_between, ":center_faction", kingdoms_begin, kingdoms_end),#include fac_player_supporters_faction for claimant quest
            (faction_slot_eq, ":center_faction", slot_faction_leader, ":center_lord"),
            (str_store_string, s11, "@liege"),
            (assign, reg0, 1),
        (else_try),
            #your former liege if you renounced a kingdom
            (eq, ":center_faction", "$players_oath_renounced_against_kingdom"),
            (is_between, ":center_faction", npc_kingdoms_begin, npc_kingdoms_end),
            (faction_slot_eq, ":center_faction", slot_faction_leader, ":center_lord"),
            (str_store_string, s11, "@former liege"),
            (assign, reg0, 1),
        (else_try),
            #stop here for lords you haven't met, or non-hero troops
            (this_or_next|neg|troop_is_hero, ":center_lord"),
            (troop_slot_eq, ":center_lord", slot_troop_met, 0),
        (else_try),
            #check for affiliates
            (call_script, "script_dplmc_is_affiliated_family_member", ":center_lord"),
            (ge, reg0, 1),
            (try_begin),
                (ge, "$g_encountered_party_relation", 0),#don't say "ally" when you might fight them, as that's confusing
                (str_store_string, s11, "str_dplmc_ally"),
            (else_try),
                (str_store_string, s11, "@affiliate"),
            (try_end),
        (else_try),
            #check for former companions
            (call_script, "script_troop_get_player_relation", ":center_lord"),
            (is_between, ":center_lord", companions_begin, companions_end),
            (neg|troop_slot_eq, ":center_lord", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
            (try_begin),
               (ge, "$g_encountered_party_relation", 0),#don't say "ally" when you might fight them, as that's confusing
               (ge, reg0, 50),
               (str_store_string, s11, "str_dplmc_ally"),
            (else_try),
                (ge, "$g_encountered_party_relation", 0),
                (ge, reg0, 20),
                (str_store_string, s11, "str_dplmc_friend"),
            (else_try),
                (str_store_string, s11, "@former companion"),
            (try_end),
            (assign, reg0, 1),
        (else_try),
            #don't print "friend" if you might fight them
            (lt, "$g_encountered_party_relation", 0),
            (assign, reg0, 0),
        (else_try),
            #check for friends
            (val_div, reg0, 50),#right now reg0 holds the relation with the player
            (ge, reg0, 1),
            (str_store_string, s11, "str_dplmc_friend"),
        (else_try),
            #check for marshall
            (eq, ":center_faction", "$players_kingdom"),
            (faction_slot_eq, ":center_faction", slot_faction_marshall, ":center_lord"),
            (str_store_string, s11, "@marshall"),
        (else_try),
            #check for vassal of player if nothing else to say
            (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":center_faction"),
            (val_add, reg0, 1),
            (val_sub, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
            (ge, reg0, 1),
            (str_store_string, s11, "@vassal"),
        (else_try),
            (assign, reg0, 0),
        (try_end),
        ##diplomacy end+
        (try_begin),
          (party_slot_eq,"$current_town",slot_party_type, spt_castle),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the castle gate."),
          ##diplomacy start+ If reg0 > 0, a relation string was written to {s11} above
          (else_try),
            (ge, reg0, 1),
            (str_store_string, s11, "@ You see the banner of your {s11} {s7} over the castle gate."),
          ##diplomacy end+
          (else_try),
            (gt, ":center_lord", -1),
            (troop_slot_eq, ":center_lord", slot_troop_spouse, "trp_player"),
            (str_store_string,s11,"str__you_see_the_banner_of_your_wifehusband_s7_over_the_castle_gate"),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the castle gate."),
          (else_try),
    ##            (str_store_string,s11,"@ This castle seems to belong to no one."),
            (str_store_string,s11,"@ This castle has no garrison."),
          (try_end),
        (else_try),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the town gates."),
          ##diplomacy start+ If reg0 > 0, a relation string was written to {s11} above
          (else_try),
            (ge, reg0, 1),
            (str_store_string, s11, "@ The banner of your {s11} {s7} flies over the town gates."),
          ##diplomacy end+
          (else_try),
            (gt, ":center_lord", -1),
            (troop_slot_eq, ":center_lord", slot_troop_spouse, "trp_player"),
            (str_store_string,s11,"str__the_banner_of_your_wifehusband_s7_flies_over_the_town_gates"),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the town gates."),
          (else_try),
    ##            (str_store_string,s11,"@ The townsfolk here have declared their independence."),
            (str_store_string,s11,"@ This town has no garrison."),
          (try_end),
        (try_end),
        ##diplomacy start+
        (assign, reg0, ":save_reg0"),#revert variables
        (assign, reg4, ":save_reg4"),
        ##diplomacy end+

        (str_clear, s12),
        (try_begin),
          (party_slot_eq,"$current_town",slot_party_type, spt_town),
          (party_get_slot, ":center_relation", "$current_town", slot_center_player_relation),
          (call_script, "script_describe_center_relation_to_s3", ":center_relation"),
          (assign, reg9, ":center_relation"),
          (str_store_string, s12, "@{!} {s3} ({reg9})."),
        (try_end),

        (str_clear, s13),
        (try_begin),
          (gt,"$entry_to_town_forbidden",0),
          (str_store_string, s13, "@ You have successfully sneaked in."),
        (else_try),
          (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
          (faction_slot_eq, ":center_faction", slot_faction_ai_object, "$current_town"),

          (str_store_string, s13, "str__the_lord_is_currently_holding_a_feast_in_his_hall"),
        (else_try), #SB : we use this incidental information to reflect on the player's residence/court
          (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
          (try_begin),
            (lt, ":player_spouse", 0), #to make registers work
            (assign, ":player_spouse", 0), 
          (else_try),
            (this_or_next|neg|troop_slot_eq, ":player_spouse", slot_troop_occupation, slto_kingdom_lady),
            (neg|troop_slot_eq, ":player_spouse", slot_troop_cur_center, "$current_town"),
            (assign, ":player_spouse", 0),
          (try_end),
          (try_begin),
            (eq, "$g_player_court", "$current_town"),
            (assign, reg0, ":player_spouse"),
            (store_and, reg1, "$players_kingdom_name_set", rename_center), #check if it's "court" or "capital"
            (str_store_troop_name, s0, ":player_spouse"),
            (str_store_string, s13, "@ Your {reg1?capital is:court can be found} here{reg0? with your spouse, {s0} in residence:}."),
          (else_try),
            (neq, "$g_player_court", "$current_town"),
            (gt, ":player_spouse", 0),
            (str_store_string, s13, "@ Your household can be found here."),
          (try_end),
        (try_end),

        #forbidden to enter?
        (try_begin),
          (store_time_of_day,reg(12)),
          (ge,reg(12),5),
          (lt,reg(12),21),
          (assign,"$town_nighttime",0),
        (else_try),
          (assign,"$town_nighttime",1),
          (party_slot_eq,"$current_town",slot_party_type, spt_town),
          (str_store_string, s13, "str_town_nighttime"),
        (try_end),

        (try_begin),
          (party_slot_ge, "$current_town", slot_town_has_tournament, 1),
          (neg|is_currently_night),
          (party_set_slot, "$current_town", slot_town_has_tournament, 1),
          (str_store_string, s13, "@{s13} A tournament will be held here soon."),
        (try_end),

        (assign,"$castle_undefended",0),
        (party_get_num_companions, ":castle_garrison_size", "p_collective_enemy"),
        (try_begin),
          (eq,":castle_garrison_size",0),
          (assign,"$castle_undefended",1),
        (try_end),

        (call_script, "script_set_town_picture"),

#		(str_clear, s5), #alert player that there are new rumors
#		(try_begin),
#			(eq, 1, 0),
#			(neg|is_currently_night),
#			(str_store_string, s5, "@^The buzz of excited voices as you come near the gate suggests to you that news of some import is circulating among the townsfolk."),
#			(lt, "$last_town_log_entry_checked", "$num_log_entries"),
#			(assign, "$g_town_rumor_log_entry", 0),
#			(try_for_range, ":log_entry", "$last_town_log_entry_checked", "$num_log_entries"),
#				(eq, ":log_entry", 4123), #placeholder to avoid having unused variable error message
#			(try_end),
#			(assign, "$last_town_log_entry_checked", "$num_log_entries"),
#		(try_end),
        ],
    [
      ("castle_castle",
      [
        (party_slot_eq,"$current_town",slot_party_type, spt_castle),

        (eq, "$sneaked_into_town", disguise_none),

        (str_clear, s1),
        (try_begin),
          (store_faction_of_party, ":center_faction", "$current_town"),
          (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
          (faction_slot_eq, ":center_faction", slot_faction_ai_object, "$current_town"),
          (str_store_string, s1, "str__join_the_feast"),
        (try_end),
        #SB : some gender string tweaks
        (try_begin),
          (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
          (lt, ":town_lord", 0),
          (assign, reg4, 0), #default to lord
        (else_try),
          (call_script, "script_dplmc_store_troop_is_female_reg", ":town_lord", 4),
        (try_end),
        #possibly replace "the" with "your"
        ],"Go to the {reg4?Lady:Lord}'s hall{s1}.",
       [
           (try_begin),
             (this_or_next|eq, "$all_doors_locked", 1),
             (gt, "$sneaked_into_town", disguise_none),
             (display_message,"str_door_locked",message_locked),
           (else_try),
             (this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
             (neg|troop_slot_ge, "trp_player", slot_troop_renown, 50),
             (neg|troop_slot_ge, "trp_player", slot_troop_renown, 125),
             (neq, "$g_player_eligible_feast_center_no", "$current_town"),

             (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, sfai_feast),
             (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),

             (neg|check_quest_active, "qst_wed_betrothed"),
             (neg|check_quest_active, "qst_wed_betrothed_female"),

             (neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin), #Married players always make the cut

             (jump_to_menu, "mnu_cannot_enter_court"),
           (else_try),
             (assign, "$town_entered", 1),
             (call_script, "script_enter_court", "$current_town"),
           (try_end),
        ], "Door to the castle."),

      ("join_tournament", [
        (neg|is_currently_night),
        (party_slot_ge, "$current_town", slot_town_has_tournament, 1),
        (eq,"$entry_to_town_forbidden",0), #SB : can't participate while disguised
        ]
       ,"Join the tournament.",
       [
           (call_script, "script_fill_tournament_participants_troop", "$current_town", 1),
           (assign, "$g_tournament_cur_tier", 0),
           (assign, "$g_tournament_player_team_won", -1),
           (assign, "$g_tournament_bet_placed", 0),
           (assign, "$g_tournament_bet_win_amount", 0),
           (assign, "$g_tournament_last_bet_tier", -1),
           (assign, "$g_tournament_next_num_teams", 0),
           (assign, "$g_tournament_next_team_size", 0),
           (jump_to_menu, "mnu_town_tournament"),
        ]),

      ("town_castle",[
          (party_slot_eq,"$current_town",slot_party_type, spt_town),
          (eq,"$entry_to_town_forbidden",0),
          (str_clear, s1),
          (try_begin),
            (store_faction_of_party, ":center_faction", "$current_town"),
            (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
            (faction_slot_eq, ":center_faction", slot_faction_ai_object, "$current_town"),
            (str_store_string, s1, "str__join_the_feast"),
          (try_end),

          ],"Go to the castle{s1}.",
       [
           (try_begin),
             (this_or_next|eq, "$all_doors_locked", 1),
             (gt, "$sneaked_into_town", disguise_none),
             (display_message,"str_door_locked",message_locked),
           (else_try),
             (this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
             (neg|troop_slot_ge, "trp_player", slot_troop_renown, 50),
             (neg|troop_slot_ge, "trp_player", slot_troop_renown, 125),
             (neq, "$g_player_eligible_feast_center_no", "$current_town"),

             (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, sfai_feast),
             (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),

             (neg|check_quest_active, "qst_wed_betrothed"),
             (neg|check_quest_active, "qst_wed_betrothed_female"),

             (neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin), #Married players always make the cut

             (jump_to_menu, "mnu_cannot_enter_court"),
            (else_try),
              (assign, "$town_entered", 1),
              (call_script, "script_enter_court", "$current_town"),
           (try_end),
        ], "Door to the castle."),

      ("town_center",
      [
        (party_slot_eq, "$current_town", slot_party_type, spt_town),
        (this_or_next|eq,"$entry_to_town_forbidden",0),
        (gt, "$sneaked_into_town", disguise_none), #SB : condition for disguise
      ],
      "Take a walk around the streets.",
       [
         #If the player is fighting his or her way out
         (try_begin),
           (eq, "$talk_context", tc_prison_break),
           (assign, "$talk_context", tc_escape),
           (assign, "$g_mt_mode", tcm_escape),
           (store_faction_of_party, ":town_faction", "$current_town"),
           (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_3_troop),
           (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
           (faction_get_slot, ":tier_4_troop", ":town_faction", slot_faction_tier_4_troop),
           (party_get_slot, ":town_scene", "$current_town", slot_town_center),
           (modify_visitors_at_site, ":town_scene"),
           (reset_visitors),
           #SB : TODO : take account slot_center_has_prisoner_tower
           #ideally we could alarm troops at locations
           (try_begin),
	         #if guards have not gone to some other important happening at nearby villages, then spawn 4 guards. (example : fire)
             (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),

             (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
             (store_time_of_day, ":cur_day_hour"),
             (try_begin), #there are 6 guards at day time (no fire ext)
               (ge, ":cur_day_hour", 6),
               (lt, ":cur_day_hour", 22),
               (set_visitors, 25, ":tier_2_troop", 2),
               (set_visitors, 26, ":tier_2_troop", 1),
               (set_visitors, 27, ":tier_3_troop", 2),
               (set_visitors, 28, ":tier_4_troop", 1),
             (else_try),  #only 4 guards because of night
               (set_visitors, 25, ":tier_2_troop", 1),
               (set_visitors, 26, ":tier_2_troop", 1),
               (set_visitors, 27, ":tier_3_troop", 1),
               (set_visitors, 28, ":tier_4_troop", 1),
             (try_end),
           (else_try),
	         #if guards have gone to some other important happening at nearby villages, then spawn only 1 guard. (example : fire)
             (store_time_of_day, ":cur_day_hour"),
             (try_begin), #only 2 guard because there is a fire at one owned village
               (ge, ":cur_day_hour", 6),
               (lt, ":cur_day_hour", 22),
               (set_visitors, 25, ":tier_2_troop", 1),
               (set_visitors, 26, ":tier_2_troop", 0),
               (set_visitors, 27, ":tier_3_troop", 1),
               (set_visitors, 28, ":tier_4_troop", 0),
             (else_try), #only 1 guard because both night and there is a fire at one owned village
               (set_visitors, 25, ":tier_2_troop", 1),
               (set_visitors, 26, ":tier_2_troop", 0),
               (set_visitors, 27, ":tier_3_troop", 0),
               (set_visitors, 28, ":tier_4_troop", 0),
             (try_end),
           (try_end),
           (set_jump_mission,"mt_town_center"),
           (try_begin),
             (gt, "$sneaked_into_town", disguise_none), #setup disguise
             (assign, ":override_state", af_override_everything),
           (try_end),
           #SB : override disguise and set flags for entries
           (try_for_range, ":entry_no", 0, 8),
			 (eq, "$g_dplmc_player_disguise", 1),
             (gt, "$sneaked_into_town", disguise_none),
             (mission_tpl_entry_set_override_flags, "mt_town_center", ":entry_no", ":override_state"),
             (call_script, "script_set_disguise_override_items", "mt_town_center", ":entry_no", 1),
           (try_end),
           
           (jump_to_scene, ":town_scene"),
           (change_screen_mission),
            #If you're already at escape, then talk context will reset
         (else_try),
           (assign, "$talk_context", 0),
           (call_script, "script_cf_enter_center_location_bandit_check"),
           #All other circumstances...
         (else_try),
           (party_get_slot, ":town_scene", "$current_town", slot_town_center),
           (modify_visitors_at_site, ":town_scene"),
           (reset_visitors),
           (assign, "$g_mt_mode", tcm_default),
           (store_faction_of_party, ":town_faction","$current_town"),

           (try_begin),
             (neq, ":town_faction", "fac_player_supporters_faction"),
             (faction_get_slot, ":troop_prison_guard", "$g_encountered_party_faction", slot_faction_prison_guard_troop),
             (faction_get_slot, ":troop_castle_guard", "$g_encountered_party_faction", slot_faction_castle_guard_troop),
             (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_2_troop),
             (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
           (else_try),
             (party_get_slot, ":town_original_faction", "$current_town", slot_center_original_faction),
             (faction_get_slot, ":troop_prison_guard", ":town_original_faction", slot_faction_prison_guard_troop),
             (faction_get_slot, ":troop_castle_guard", ":town_original_faction", slot_faction_castle_guard_troop),
             (faction_get_slot, ":tier_2_troop", ":town_original_faction", slot_faction_tier_2_troop),
             (faction_get_slot, ":tier_3_troop", ":town_original_faction", slot_faction_tier_3_troop),
           (try_end),
           (try_begin), #think about this, should castle guard have to go nearby fire too? If he do not go, killing 2 armored guard is too hard for player. For now he goes too.
             #if guards have not gone to some other important happening at nearby villages, then spawn 4 guards. (example : fire)
             (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),

             (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
             (set_visitor, 23, ":troop_castle_guard"),
           (try_end),
           (set_visitor, 24, ":troop_prison_guard"),

           (try_begin),
             (gt,":tier_2_troop", 0),
             (assign,reg0,":tier_3_troop"),
             (assign,reg1,":tier_3_troop"),
             (assign,reg2,":tier_2_troop"),
             (assign,reg3,":tier_2_troop"),
           (else_try),
             (assign,reg0,"trp_vaegir_infantry"),
             (assign,reg1,"trp_vaegir_infantry"),
             (assign,reg2,"trp_vaegir_archer"),
             (assign,reg3,"trp_vaegir_footman"),
           (try_end),
           (shuffle_range,0,4),

           (try_begin),
             #if guards have not gone to some other important happening at nearby villages, then spawn 4 guards. (example : fire)
             (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),

             (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
             (set_visitor,25,reg0),
             (set_visitor,26,reg1),
             (set_visitor,27,reg2),
             (set_visitor,28,reg3),
           (try_end),

           (party_get_slot, ":spawned_troop", "$current_town", slot_town_armorer),
           (set_visitor, 9, ":spawned_troop"),
           (party_get_slot, ":spawned_troop", "$current_town", slot_town_weaponsmith),
           (set_visitor, 10, ":spawned_troop"),
           (party_get_slot, ":spawned_troop", "$current_town", slot_town_elder),
           (set_visitor, 11, ":spawned_troop"),
           (party_get_slot, ":spawned_troop", "$current_town", slot_town_horse_merchant),
           (set_visitor, 12, ":spawned_troop"),
           (call_script, "script_init_town_walkers"),
           (set_jump_mission,"mt_town_center"),
           (assign, ":override_state", af_override_horse),
           (try_begin),
             (gt, "$sneaked_into_town", disguise_none), #setup disguise
             (assign, ":override_state", af_override_everything),
           (try_end),
           #SB : override disguise and set flags for entries
           (try_for_range, ":entry_no", 0, 8),
			 (neq, ":entry_no", 1), #dckplmc: we want to ride our horses
             (mission_tpl_entry_set_override_flags, "mt_town_center", ":entry_no", ":override_state"),
             (call_script, "script_set_disguise_override_items", "mt_town_center", ":entry_no", 1),
           (try_end),

           (try_begin),
             (eq, "$town_entered", 0),
             (assign, "$town_entered", 1),
             (eq, "$town_nighttime", 0),
             (set_jump_entry, 1),
           (try_end),
           (jump_to_scene, ":town_scene"),
           (change_screen_mission),
         (try_end),
      ],"Door to the town center."),

      ("town_tavern",[
          (party_slot_eq,"$current_town",slot_party_type, spt_town),
          (this_or_next|eq,"$entry_to_town_forbidden",0),
          (gt, "$sneaked_into_town", disguise_none),
#          (party_get_slot, ":scene", "$current_town", slot_town_tavern),
#          (scene_slot_eq, ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
          ]
       ,"Visit the tavern.",
       [
           (try_begin),
             (eq,"$all_doors_locked",1),
             (display_message,"str_door_locked",message_locked),
           (else_try),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             (assign, "$town_entered", 1),
             (set_jump_mission, "mt_town_default"),
             (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_horse),
             (try_begin), #SB : adjust sneaking overrides
               (gt, "$sneaked_into_town", disguise_none),
               (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_everything),
               (call_script, "script_set_disguise_override_items", "mt_town_default", 0, 1), #need weaposn for tavern fights
             (try_end),
             (party_get_slot, ":cur_scene", "$current_town", slot_town_tavern),
             (jump_to_scene, ":cur_scene"),
             (scene_set_slot, ":cur_scene", slot_scene_visited, 1),

             (assign, "$talk_context", tc_tavern_talk),
             (call_script, "script_initialize_tavern_variables"),

             (store_random_in_range, ":randomize_attacker_placement", 0, 4),

             (modify_visitors_at_site, ":cur_scene"),
             (reset_visitors),

             (assign, ":cur_entry", 17),

			 #this is just a cheat right now
             #(troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, "$g_encountered_party"),
			 (try_begin),
				(eq, "$cheat_mode", 1),
				(troop_get_slot, ":drunk_location", "trp_belligerent_drunk", slot_troop_cur_center),
				(try_begin),
					(eq, "$cheat_mode", 0),
				(else_try),
					(is_between, ":drunk_location", centers_begin, centers_end),
					(str_store_party_name, s4, ":drunk_location"),
					(display_message, "str_belligerent_drunk_in_s4"),
			    (else_try),
					(display_message, "str_belligerent_drunk_not_found"),
				(try_end),

				# (troop_get_slot, ":promoter_location", "trp_fight_promoter", slot_troop_cur_center),
				# (try_begin),
					# (eq, "$cheat_mode", 0),
				# (else_try),
					# (is_between, ":promoter_location", centers_begin, centers_end),
					# (str_store_party_name, s4, ":promoter_location"),
					# (display_message, "str_roughlooking_character_in_s4"),
			    # (else_try),
					# (display_message, "str_roughlooking_character_not_found"),
				# (try_end),
			 (try_end),

			 #this determines whether or not a lord who dislikes you will commission an assassin
			 (try_begin),
				(store_current_hours, ":hours"),
				(store_sub, ":hours_since_last_attempt", ":hours", "$g_last_assassination_attempt_time"),
				(gt, ":hours_since_last_attempt", 168),
				##diplomacy start+ Support ladies owning fiefs
				#(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
				(try_for_range, ":lord", heroes_begin, heroes_end),
					(this_or_next|is_between, ":lord", active_npcs_begin, active_npcs_end),
						(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
					#Make sure they're not retired or dead
					(neg|troop_slot_ge, ":lord", slot_troop_occupation, slto_retirement),
					#add support for non-noble personalities
					(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_ambitious),#"Lady MacBeth"
					(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_roguish),
					##diplomacy end+
					(troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_debauched),
					(troop_get_slot, ":led_party", ":lord", slot_troop_leaded_party),
					(party_is_active, ":led_party"),
					(party_get_attached_to, ":led_party_attached", ":led_party"),
					(eq, ":led_party_attached", "$g_encountered_party"),
					(call_script, "script_troop_get_relation_with_troop", "trp_player", ":lord"),
					(lt, reg0, -20),
					(assign, "$g_last_assassination_attempt_time", ":hours"),
#					(assign, "$g_last_assassination_attempt_location", "$g_encountered_party"),
#					(assign, "$g_last_assassination_attempt_perpetrator", ":lord"),

					(troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),
				(try_end),
				##diplomacy start+
				#"Lady MacBeth" noblewomen will also attempt to have people killed on their husbands' behalf.
				(lt, "$g_last_assassination_attempt_time", ":hours"),
				(neg|troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),
				(try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
					(troop_slot_eq, ":lady", slot_troop_cur_center, "$g_encountered_party"),
					(troop_slot_eq, ":lady", slot_lord_reputation_type, lrep_ambitious),#"Lady MacBeth"
					(troop_slot_eq, ":lady", slot_troop_occupation, slto_kingdom_lady),

					(call_script, "script_troop_get_player_relation", ":lady"),
					(lt, reg0, 1),
					#Will send an assassin if she doesn't like the player, and either she or her husband
					#is at -20 or worse with the player.
					(try_begin),
						(ge, reg0, -20),
						(troop_slot_ge, ":lady", slot_troop_spouse, 1),
						(troop_get_slot, reg0, ":lady", slot_troop_spouse),
						(call_script, "script_troop_get_player_relation", reg0),
					(try_end),
					(lt, reg0, -20),

					(assign, "$g_last_assassination_attempt_time", ":hours"),
					(troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),
				(try_end),
				##diplomacy end+
			 (try_end),

			 (try_begin),
				 (eq, ":randomize_attacker_placement", 0),
				 (call_script, "script_setup_tavern_attacker", ":cur_entry"),

				 (val_add, ":cur_entry", 1),
			 (try_end),

			 # (try_begin),
				# (eq, 1, 0),
				# (troop_slot_eq, "trp_fight_promoter", slot_troop_cur_center, "$current_town"),
                # (set_visitor, ":cur_entry", "trp_fight_promoter"),

                # (val_add, ":cur_entry", 1),
			 # (try_end),

             (party_get_slot, ":mercenary_troop", "$current_town", slot_center_mercenary_troop_type),
             (party_get_slot, ":mercenary_amount", "$current_town", slot_center_mercenary_troop_amount),
             (try_begin),
			   (gt, ":mercenary_troop", 0),
               (gt, ":mercenary_amount", 0),
               (set_visitor, ":cur_entry", ":mercenary_troop"),
               (val_add, ":cur_entry", 1),
             (try_end),

			 (try_begin),
				 (eq, ":randomize_attacker_placement", 1),
				 (call_script, "script_setup_tavern_attacker", ":cur_entry"),
				 (val_add, ":cur_entry", 1),
			 (try_end),

             (try_for_range, ":companion_candidate", companions_begin, companions_end),
               (troop_slot_eq, ":companion_candidate", slot_troop_occupation, 0),
               (troop_slot_eq, ":companion_candidate", slot_troop_cur_center, "$current_town"),
			   (neg|troop_slot_ge, ":companion_candidate", slot_troop_prisoner_of_party, centers_begin),

               (set_visitor, ":cur_entry", ":companion_candidate"),

               (val_add, ":cur_entry", 1),
             (try_end),

			 (try_begin),
				 (eq, ":randomize_attacker_placement", 2),
				 (call_script, "script_setup_tavern_attacker", ":cur_entry"),
				 (val_add, ":cur_entry", 1),
			 (try_end),

             (try_begin), #this doubles the incidence of ransom brokers and (below) minstrels
               (party_get_slot, ":ransom_broker", "$current_town", slot_center_ransom_broker),
               (gt, ":ransom_broker", 0),

               # (assign, reg0, ":ransom_broker"),
               # (assign, reg1, "$current_town"),

               (set_visitor, ":cur_entry", ":ransom_broker"),
               (val_add, ":cur_entry", 1),
             (else_try), #SB : move to script call
               # (is_between, "$g_talk_troop", ransom_brokers_begin, ransom_brokers_end), #wtf is this
               (call_script, "script_cf_find_alternative_town_for_taverngoers", "$current_town", 9),
               (assign, ":alternative_town", reg0),

               (party_get_slot, ":ransom_broker", ":alternative_town", slot_center_ransom_broker),
               (gt, ":ransom_broker", 0),
               (is_between, ":ransom_broker", ransom_brokers_begin, ransom_brokers_end), #prevent ramun and galeas from spawning other towns

               (set_visitor, ":cur_entry", ":ransom_broker"),
               (val_add, ":cur_entry", 1),
             (try_end),

             (try_begin),
               (party_get_slot, ":tavern_traveler", "$current_town", slot_center_tavern_traveler),
               (gt, ":tavern_traveler", 0),
               (set_visitor, ":cur_entry", ":tavern_traveler"),
               (val_add, ":cur_entry", 1),
             (try_end),

             (try_begin),
               (party_get_slot, ":tavern_minstrel", "$current_town", slot_center_tavern_minstrel),
               (gt, ":tavern_minstrel", 0),

               (set_visitor, ":cur_entry", ":tavern_minstrel"),
               (val_add, ":cur_entry", 1),
             (else_try), #SB : move to script call
               (call_script, "script_cf_find_alternative_town_for_taverngoers", "$current_town", 9),
               (assign, ":alternative_town", reg0),
               (party_get_slot, ":tavern_minstrel", ":alternative_town", slot_center_tavern_minstrel),
               (gt, ":tavern_minstrel", 0),

               (set_visitor, ":cur_entry", ":tavern_minstrel"),
               (val_add, ":cur_entry", 1),
             (try_end),

             (try_begin),
               (party_get_slot, ":tavern_bookseller", "$current_town", slot_center_tavern_bookseller),
               (gt, ":tavern_bookseller", 0),
               (set_visitor, ":cur_entry", ":tavern_bookseller"),
               (val_add, ":cur_entry", 1),
             (try_end),

			 (try_begin),
				 (eq, ":randomize_attacker_placement", 3),
				 (call_script, "script_setup_tavern_attacker", ":cur_entry"),
				 (val_add, ":cur_entry", 1),
			 (try_end),

             (try_begin),
               (neg|check_quest_active, "qst_eliminate_bandits_infesting_village"),
               (neg|check_quest_active, "qst_deal_with_bandits_at_lords_village"),
               (assign, ":end_cond", villages_end),
               (try_for_range, ":cur_village", villages_begin, ":end_cond"),
                 (party_slot_eq, ":cur_village", slot_village_bound_center, "$current_town"),
                 (party_slot_ge, ":cur_village", slot_village_infested_by_bandits, 1),
                 (neg|party_slot_eq, ":cur_village", slot_town_lord, "trp_player"),
                 (set_visitor, ":cur_entry", "trp_farmer_from_bandit_village"),
                 (val_add, ":cur_entry", 1),
                 (assign, ":end_cond", 0),
               (try_end),
             (try_end),

             (try_begin),
               (eq, "$g_starting_town", "$current_town"),

               (this_or_next|neg|check_quest_finished, "qst_collect_men"),
               (this_or_next|neg|check_quest_finished, "qst_learn_where_merchant_brother_is"),
               (this_or_next|neg|check_quest_finished, "qst_save_relative_of_merchant"),
               (this_or_next|neg|check_quest_finished, "qst_save_town_from_bandits"),
               (eq,  "$g_do_one_more_meeting_with_merchant", 1),

               #SB : offset for merchant troop
               (call_script, "script_get_troop_of_merchant"),
               (set_visitor, ":cur_entry", reg0),
               (val_add, ":cur_entry", 1),
             (try_end),
			 
			#dedal begin
			(party_get_slot, ":center_faction", "$current_town", slot_center_original_faction), #dckplmc - tavern patrons same culture as town
			(faction_get_slot, ":center_culture", ":center_faction", slot_faction_culture),
			(faction_get_slot, ":walker_troop_id", ":center_culture", slot_faction_town_walker_male_troop),
			(try_for_range,":entry",32,41),
						(store_random_in_range,":rand",0,2), #dckplmc - randomly male or female
						(store_add, ":town_walker", ":rand", ":walker_troop_id"),
						(store_random_in_range,":dna",0,1000),
						(mission_tpl_entry_clear_override_items,"mt_town_default",":entry"),
						(store_random_in_range,":r",0,10),
						(try_begin),
							(gt,":r",2),
							(mission_tpl_entry_add_override_item,"mt_town_default",":entry","itm_dedal_kufel"),
						(try_end),
						(set_visitor,":entry",":town_walker",":dna"),
                        
                        (troop_set_slot, "trp_temp_array_c", ":entry", ":dna"),
                        
			(try_end),
			#dedal end

             (change_screen_mission),
           (try_end),
        ],"Door to the tavern."),

#      ("town_smithy",[
#          (eq,"$entry_to_town_forbidden",0),
#          (eq,"$town_nighttime",0),
#          ],
#       "Visit the smithy.",
#       [
#           (set_jump_mission,"mt_town_default"),
#           (jump_to_scene,"$pout_scn_smithy"),
#           (change_screen_mission,0),
#        ]),


      ("town_merchant",
       [(party_slot_eq,"$current_town",slot_party_type, spt_town),
           (eq,"$town_nighttime",0),
           (this_or_next|eq,"$entry_to_town_forbidden",0),
           (gt, "$sneaked_into_town", disguise_none),
#           (party_get_slot, ":scene", "$current_town", slot_town_store),
#           (scene_slot_eq, ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
           ],
       "Speak with the merchant.",
       [
           (try_begin),
             (this_or_next|eq,"$all_doors_locked",1),
             (eq,"$town_nighttime",1),
             (display_message,"str_door_locked",message_locked),
           (else_try),
             (assign, "$town_entered", 1),
             (set_jump_mission, "mt_town_default"),
             (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_horse),
             (try_begin),
               #(gt, "$sneaked_into_town", disguise_none),
               #(mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_all),
               #SB : adjust sneaking overrides
               (gt, "$sneaked_into_town", disguise_none),
               (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_everything),
               (call_script, "script_set_disguise_override_items", "mt_town_default", 0, 1), #need weaposn for tavern fights
             (try_end),
             (party_get_slot, ":cur_scene", "$current_town", slot_town_store),
             (jump_to_scene, ":cur_scene"),
             (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
             (change_screen_mission),
           (try_end),
        ],"Door to the shop."),

      ("town_arena",
       [(party_slot_eq,"$current_town",slot_party_type, spt_town),
        (eq, "$sneaked_into_town", 0),
#           (party_get_slot, ":scene", "$current_town", slot_town_arena),
#           (scene_slot_eq,  ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
           ],
       "Enter the arena.",
       [
           (try_begin),
             (this_or_next|eq,"$all_doors_locked",1),
             (eq,"$town_nighttime",1),
             (display_message,"str_door_locked",message_locked),
           (else_try),
             (assign, "$g_mt_mode", abm_visit),
             (assign, "$town_entered", 1),
             (set_jump_mission, "mt_arena_melee_fight"),
             (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
             (modify_visitors_at_site, ":arena_scene"),
             (reset_visitors),
             (set_visitor, 43, "trp_veteran_fighter"),
             (set_visitor, 44, "trp_hired_blade"),
             (set_jump_entry, 50),
             (jump_to_scene, ":arena_scene"),
             (scene_set_slot, ":arena_scene", slot_scene_visited, 1),
             (change_screen_mission),
           (try_end),
        ],"Door to the arena."),
      ("town_dungeon",
       [(party_slot_eq, "$current_town", slot_town_lord, "trp_player"), #dckplmc: add quick access to dungeon for owner
        ],
       "Enter the prison.",
       [
           (try_begin),
		    (eq, "$talk_context", tc_prison_break),
			(gt, "$g_main_attacker_agent", 0),

		   	(neg|agent_is_alive, "$g_main_attacker_agent"),

			(agent_get_troop_id, ":agent_type", "$g_main_attacker_agent"),
			(try_begin),
			  (eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
			  (party_get_slot, ":prison_guard_faction", "$current_town", slot_center_original_faction),
			(else_try),
			  (assign, ":prison_guard_faction", "$g_encountered_party_faction"),
			(try_end),
			(faction_slot_eq, ":prison_guard_faction", slot_faction_prison_guard_troop, ":agent_type"),

			(call_script, "script_deduct_casualties_from_garrison"),
            (call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle"),

		   (else_try),
             (eq,"$all_doors_locked",1),
             (display_message,"str_door_locked",message_locked),
           (else_try),
             (this_or_next|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
             (eq, "$g_encountered_party_faction", "$players_kingdom"),
             (assign, "$town_entered", 1),
             (call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle"),
           (else_try),
             (display_message,"str_door_locked",message_locked),
           (try_end),
        ],"Door to the dungeon."),

      ("castle_inspect",
      [
         (party_slot_eq,"$current_town",slot_party_type, spt_castle),
      ],
       "Take a walk around the courtyard.",
       [
         (try_begin),
           (eq, "$talk_context", tc_prison_break),
           (assign, "$talk_context", tc_escape),

           (party_get_slot, ":cur_castle_exterior", "$current_town", slot_castle_exterior),
           (modify_visitors_at_site, ":cur_castle_exterior"),
           (reset_visitors),

           (assign, ":guard_no", 40),

           (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
           (try_for_range, ":troop_iterator", 0, ":num_stacks"),
             #nearby fire condition start
             (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),
             (this_or_next|eq, ":guard_no", 40),
             (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
             #nearby fire condition end

             (lt, ":guard_no", 47),
             (party_stack_get_troop_id, ":cur_troop_id", "$g_encountered_party", ":troop_iterator"),
             (neg|troop_is_hero, ":cur_troop_id"),
             (party_stack_get_size, ":stack_size","$g_encountered_party",":troop_iterator"),
             (party_stack_get_num_wounded, ":num_wounded","$g_encountered_party",":troop_iterator"),
             (val_sub, ":stack_size", ":num_wounded"),
             (gt, ":stack_size", 0),
             (party_stack_get_troop_dna,":troop_dna", "$g_encountered_party", ":troop_iterator"),
             (set_visitor, ":guard_no", ":cur_troop_id", ":troop_dna"),
             (val_add, ":guard_no", 1),
           (try_end),
           #(set_jump_entry, 1),
           (set_visitor, 7, "trp_player"), #SB : g_player_troop back to trp_player

           (set_jump_mission,"mt_castle_visit"),
           
           (try_begin),
             (gt, "$sneaked_into_town", disguise_none), #setup disguise
             (assign, ":override_state", af_override_everything),
           (try_end),
           #SB : override disguise and set flags for entries
           (try_for_range, ":entry_no", 0, 8),
			 (eq, "$g_dplmc_player_disguise", 1),
             (gt, "$sneaked_into_town", disguise_none),
             (mission_tpl_entry_set_override_flags, "mt_castle_visit", ":entry_no", ":override_state"),
             (call_script, "script_set_disguise_override_items", "mt_castle_visit", ":entry_no", 1),
           (try_end),
           
           (jump_to_scene, ":cur_castle_exterior"),
           (change_screen_mission),
            #If you're already at escape, then talk context will reset
         (else_try),
           (assign, "$talk_context", tc_town_talk),

           (assign, "$g_mt_mode", tcm_default),

           (party_get_slot, ":cur_castle_exterior", "$current_town", slot_castle_exterior),
           (modify_visitors_at_site,":cur_castle_exterior"),
           (reset_visitors),

           (try_begin),
             (neq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
             (faction_get_slot, ":troop_prison_guard", "$g_encountered_party_faction", slot_faction_prison_guard_troop),
           (else_try),
             (party_get_slot, ":town_original_faction", "$current_town", slot_center_original_faction),
             (faction_get_slot, ":troop_prison_guard", ":town_original_faction", slot_faction_prison_guard_troop),
           (try_end),
           (set_visitor, 24, ":troop_prison_guard"),

           (assign, ":guard_no", 40),

           (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
           (try_for_range, ":troop_iterator", 0, ":num_stacks"),
             #nearby fire condition start
             (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),
             (neg|is_between, ":cur_time", ":fire_finish_time", ":last_nearby_fire_time"),

             (lt, ":guard_no", 47),
             (party_stack_get_troop_id, ":cur_troop_id", "$g_encountered_party", ":troop_iterator"),
             (neg|troop_is_hero, ":cur_troop_id"),
             (party_stack_get_size, ":stack_size","$g_encountered_party",":troop_iterator"),
             (party_stack_get_num_wounded, ":num_wounded","$g_encountered_party",":troop_iterator"),
             (val_sub, ":stack_size", ":num_wounded"),
             (gt, ":stack_size", 0),
             (party_stack_get_troop_dna,":troop_dna","$g_encountered_party",":troop_iterator"),
             (set_visitor, ":guard_no", ":cur_troop_id", ":troop_dna"),

             (val_add, ":guard_no", 1),
           (try_end),

           (try_begin),
             (eq, "$town_entered", 0),
             (assign, "$town_entered", 1),
           (try_end),
           (set_jump_entry, 1),

           (assign, ":override_state", af_override_horse),
           (try_begin),
             (gt, "$sneaked_into_town", disguise_none), #setup disguise
             (assign, ":override_state", af_override_everything),
           (try_end),
           (set_jump_mission, "mt_castle_visit"),

           #SB : populate disguise and set flags for entries
           (try_for_range, ":entry_no", 0, 8),
             (mission_tpl_entry_set_override_flags, "mt_castle_visit", ":entry_no", ":override_state"),
             (call_script, "script_set_disguise_override_items", "mt_castle_visit", ":entry_no", 1),
           (try_end),
           # (mission_tpl_entry_set_override_flags, "mt_castle_visit", 0, ":override_state"),
           # (mission_tpl_entry_set_override_flags, "mt_castle_visit", 1, ":override_state"),
           # (mission_tpl_entry_set_override_flags, "mt_castle_visit", 2, ":override_state"),
           # (mission_tpl_entry_set_override_flags, "mt_castle_visit", 3, ":override_state"),
           # (mission_tpl_entry_set_override_flags, "mt_castle_visit", 4, ":override_state"),
           # (mission_tpl_entry_set_override_flags, "mt_castle_visit", 5, ":override_state"),
           # (mission_tpl_entry_set_override_flags, "mt_castle_visit", 6, ":override_state"),
           # (mission_tpl_entry_set_override_flags, "mt_castle_visit", 7, ":override_state"),

           (jump_to_scene, ":cur_castle_exterior"),
           (change_screen_mission),
         (try_end),
        ], "To the castle courtyard."),

     ("town_enterprise",
      [
        (party_slot_eq,"$current_town",slot_party_type, spt_town),
        (party_get_slot, ":item_produced", "$current_town", slot_center_player_enterprise),
		(gt, ":item_produced", 1),
        (eq,"$entry_to_town_forbidden",0),
		(call_script, "script_get_enterprise_name", ":item_produced"),
		(str_store_string, s3, reg0),
      ],
      "Visit your {s3}.",
      [
        (store_sub, ":town_order", "$current_town", towns_begin),
		(store_add, ":master_craftsman", "trp_town_1_master_craftsman", ":town_order"),
        (party_get_slot, ":item_produced", "$current_town", slot_center_player_enterprise),
		(assign, ":enterprise_scene", "scn_enterprise_mill"),
		(try_begin),
			(eq, ":item_produced", "itm_bread"),
			(assign, ":enterprise_scene", "scn_enterprise_mill"),
		(else_try),
			(eq, ":item_produced", "itm_ale"),
			(assign, ":enterprise_scene", "scn_enterprise_brewery"),
		(else_try),
			(eq, ":item_produced", "itm_oil"),
			(assign, ":enterprise_scene", "scn_enterprise_oil_press"),
		(else_try),
			(eq, ":item_produced", "itm_wine"),
			(assign, ":enterprise_scene", "scn_enterprise_winery"),
		(else_try),
			(eq, ":item_produced", "itm_leatherwork"),
			(assign, ":enterprise_scene", "scn_enterprise_tannery"),
		(else_try),
			(eq, ":item_produced", "itm_wool_cloth"),
			(assign, ":enterprise_scene", "scn_enterprise_wool_weavery"),
		(else_try),
			(eq, ":item_produced", "itm_linen"),
			(assign, ":enterprise_scene", "scn_enterprise_linen_weavery"),
		(else_try),
			(eq, ":item_produced", "itm_velvet"),
			(assign, ":enterprise_scene", "scn_enterprise_dyeworks"),
		(else_try),
			(eq, ":item_produced", "itm_tools"),
			(assign, ":enterprise_scene", "scn_enterprise_smithy"),
		(try_end),
        (modify_visitors_at_site,":enterprise_scene"),
		(reset_visitors),
        (set_visitor,0,"trp_player"),
        (set_visitor,17,":master_craftsman"),
        (set_jump_mission,"mt_town_default"),
        (jump_to_scene,":enterprise_scene"),
        (change_screen_mission),
      ],"Door to your enterprise."),
      
     ("town_brothel",
      [
        (party_slot_eq,"$current_town",slot_party_type, spt_town),
        (party_slot_eq, "$current_town", slot_town_has_brothel, 1),
        (eq,"$entry_to_town_forbidden",0),
      ],
      "Visit your tavern and bath-house.",
      [
        (assign, "$talk_context", tc_tavern_talk),
        
        (troop_set_type, "trp_brothel_madam", 1), #savegames
        (troop_set_type, "trp_prostitute", 3),
        (troop_set_type, "trp_courtesan", 3),
        (troop_set_type, "trp_townsman", 2),
      
        (modify_visitors_at_site,"scn_tavern"),
		(reset_visitors),
        (set_visitor,0,"trp_player"),
        (set_visitor,9,"trp_brothel_madam"),
        
        #dedal begin
        (party_get_slot, ":center_faction", "$current_town", slot_center_original_faction), #dckplmc - tavern patrons same culture as town
        (faction_get_slot, ":center_culture", ":center_faction", slot_faction_culture),
        (faction_get_slot, ":walker_troop_id", ":center_culture", slot_faction_town_walker_male_troop),
        (try_for_range,":entry",1,11),
            (neq, ":entry", 9),
            (store_random_in_range,":dna",0,1000),
            (mission_tpl_entry_clear_override_items,"mt_brothel",":entry"),
            (store_random_in_range,":r",0,10),
            (try_begin),
                (gt,":r",2),
                (mission_tpl_entry_add_override_item,"mt_brothel",":entry","itm_dedal_kufel"),
            (try_end),
            (set_visitor,":entry",":walker_troop_id",":dna"),
            
            (troop_set_slot, "trp_temp_array_c", ":entry", ":dna"),
        (try_end),
        #dedal end
        
        
        (assign, ":cur_entry", 40),
        (try_for_range, ":lady", heroes_begin, heroes_end),
            (try_begin),
                (gt, ":cur_entry", 25),
                (troop_slot_eq, ":lady", slot_troop_courtesan, "$g_encountered_party"),
                (troop_set_type, ":lady", 3),
                (set_visitor, ":cur_entry",":lady",),
                (val_add, ":cur_entry", 1),
                (set_visitor, ":cur_entry","trp_townsman"),
                (val_add, ":cur_entry", 1),
                (try_begin),
                    (ge, ":cur_entry", 48),
                    (assign, ":cur_entry", 18),
                (try_end),
            (else_try),
                (lt, ":cur_entry", 25),
                (troop_slot_eq, ":lady", slot_troop_courtesan, "$g_encountered_party"),
                (troop_set_type, ":lady", 3),
                (set_visitor, ":cur_entry",":lady",),
                (val_add, ":cur_entry", 1),
            (try_end),
        (try_end),
        
        (party_get_slot, ":num_workers", "$current_town", slot_town_brothel_num_workers),
        
        (try_for_range, ":worker", 0, 12),
            (try_begin),
                (gt, ":cur_entry", 25),
                (gt, ":num_workers", 0),
                (store_random_in_range,":dna",0,1000),
                (set_visitor, ":cur_entry","trp_prostitute",":dna"),
                (troop_set_slot, "trp_temp_array_c", ":cur_entry", ":dna"),
                (val_sub, ":num_workers", 1),
                (val_add, ":cur_entry", 1),
                (set_visitor, ":cur_entry","trp_townsman"),
                (val_add, ":cur_entry", 1),
                (try_begin),
                    (ge, ":cur_entry", 48),
                    (assign, ":cur_entry", 18),
                (try_end),
            (else_try),
                (lt, ":cur_entry", 25),
                (gt, ":num_workers", 0),
                (store_random_in_range,":dna",0,1000),
                (set_visitor, ":cur_entry","trp_prostitute",":dna"),
                (troop_set_slot, "trp_temp_array_c", ":cur_entry", ":dna"),
                (val_sub, ":num_workers", 1),
                (val_add, ":cur_entry", 1),
            (try_end),
        (try_end),
        
        (assign, ":cur_entry", 17),
        
        (store_random_in_range, ":minstrel_troop",tavern_minstrels_begin,tavern_minstrels_end),
        (set_visitor, ":cur_entry",":minstrel_troop"),
        (val_add, ":cur_entry", 1),
        
        (set_jump_mission,"mt_brothel"),
        (jump_to_scene,"scn_tavern"),
        (change_screen_mission),
      ],"Door to your enterprise."),

    ("visit_lady",
	[
  
  (this_or_next|eq, "$g_polygamy", 1),
	(neg|troop_slot_ge, "trp_player", slot_troop_spouse, kingdom_ladies_begin),

	(assign, "$love_interest_in_town", 0),
	(assign, "$love_interest_in_town_2", 0),
	(assign, "$love_interest_in_town_3", 0),
	(assign, "$love_interest_in_town_4", 0),
	(assign, "$love_interest_in_town_5", 0),
	(assign, "$love_interest_in_town_6", 0),
	(assign, "$love_interest_in_town_7", 0),
	(assign, "$love_interest_in_town_8", 0),

	(try_for_range, ":lady_no", kingdom_ladies_begin, kingdom_ladies_end),
		(troop_slot_eq, ":lady_no", slot_troop_cur_center, "$current_town"),
		(call_script, "script_get_kingdom_lady_social_determinants", ":lady_no"),
		(assign, ":lady_guardian", reg0),

		(troop_slot_eq, ":lady_no", slot_troop_spouse, -1),
		(ge, ":lady_guardian", 0), #not sure when this would not be the case


		#must have spoken to either father or lady
		(this_or_next|troop_slot_ge, ":lady_no", slot_troop_met, 2),
			(troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, 1),

		(neg|troop_slot_eq, ":lady_no", slot_troop_met, 4),

		#must have approached father
#		(this_or_next|troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, 1),
#			(troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, -1),


		(try_begin),
			(eq, "$love_interest_in_town", 0),
			(assign, "$love_interest_in_town", ":lady_no"),
		(else_try),
			(eq, "$love_interest_in_town_2", 0),
			(assign, "$love_interest_in_town_2", ":lady_no"),
		(else_try),
			(eq, "$love_interest_in_town_3", 0),
			(assign, "$love_interest_in_town_3", ":lady_no"),
		(else_try),
			(eq, "$love_interest_in_town_4", 0),
			(assign, "$love_interest_in_town_4", ":lady_no"),
		(else_try),
			(eq, "$love_interest_in_town_5", 0),
			(assign, "$love_interest_in_town_5", ":lady_no"),
		(else_try),
			(eq, "$love_interest_in_town_6", 0),
			(assign, "$love_interest_in_town_6", ":lady_no"),
		(else_try),
			(eq, "$love_interest_in_town_7", 0),
			(assign, "$love_interest_in_town_7", ":lady_no"),
		(else_try),
			(eq, "$love_interest_in_town_8", 0),
			(assign, "$love_interest_in_town_8", ":lady_no"),
		(try_end),
	(try_end),

	(gt, "$love_interest_in_town", 0),
	],
	  "Attempt to visit a lady",
       [
        (jump_to_menu, "mnu_lady_visit"),
        ], "Door to the garden."),

      ("trade_with_merchants",
       [
           (party_slot_eq,"$current_town",slot_party_type, spt_town)
        ],
         "Go to the marketplace.",
         [
           (try_begin),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             (jump_to_menu,"mnu_town_trade"),
           (try_end),
          ]),
      ("walled_center_manage",
      [
        (neg|party_slot_eq, "$current_town", slot_village_state, svs_under_siege),
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
        (assign, reg0, 1),
        (try_begin),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (assign, reg0, 0),
        (try_end),
       ],
       "Manage this {reg0?town:castle}.",
       [
           (assign, "$g_next_menu", "mnu_town"),
           (jump_to_menu, "mnu_center_manage"),
       ]),

      ("walled_center_move_court",
      [ #SB : move conditions around
        (neg|party_slot_eq, "$current_town", slot_village_state, svs_under_siege),
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
        (eq, "$g_encountered_party_faction", "$players_kingdom"),
        (neq, "$g_player_court", "$current_town"),
        ##diplomacy start+ Handle player is co-ruler of kingdom
        (assign, ":is_coruler", 0),
        (try_begin),
          (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
          (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
          (ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
          (assign, ":is_coruler", 1),
        (else_try),
          (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
          (eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
          (assign, ":is_coruler", 1),
        (try_end),
        (eq, ":is_coruler", 1),
        
      ],
      "Move your court here.",
      [
        (jump_to_menu, "mnu_establish_court"),
      ]),

      ("castle_station_troops",
      [
		(party_get_slot, ":town_lord", "$current_town", slot_town_lord),
	    (str_clear, s10),

	    (assign, ":player_can_draw_from_garrison", 0),
		(try_begin), #option 1 - player is town lord
		  (eq, ":town_lord", "trp_player"),
		  (assign, ":player_can_draw_from_garrison", 1),
		(else_try), #option 2 - town is unassigned and part of the player faction
		  (store_faction_of_party, ":faction", "$g_encountered_party"),
		  (eq, ":faction", "fac_player_supporters_faction"),
		  (neg|party_slot_ge, "$g_encountered_party", slot_town_lord, active_npcs_begin), #ie, zero or -1

		  (assign, ":player_can_draw_from_garrison", 1),
		(else_try), #option 3 - town was captured by player
		  (lt, ":town_lord", 0), #ie, unassigned
		  (store_faction_of_party, ":castle_faction", "$g_encountered_party"),
		  (eq, "$players_kingdom", ":castle_faction"),

		  (eq, "$g_encountered_party", "$g_castle_requested_by_player"),

		  (str_store_string, s10, "str_retrieve_garrison_warning"),
		  (assign, ":player_can_draw_from_garrison", 1),
		(else_try),
		  (lt, ":town_lord", 0), #ie, unassigned
		  (store_faction_of_party, ":castle_faction", "$g_encountered_party"),
		  (eq, "$players_kingdom", ":castle_faction"),

		  (store_party_size_wo_prisoners, ":party_size", "$g_encountered_party"),
		  (eq, ":party_size", 0),

		  (str_store_string, s10, "str_retrieve_garrison_warning"),
		  (assign, ":player_can_draw_from_garrison", 1),
		(else_try),
		  (party_slot_ge, "$g_encountered_party", slot_town_lord, active_npcs_begin),
		  (store_faction_of_party, ":castle_faction", "$g_encountered_party"),
		  (eq, "$players_kingdom", ":castle_faction"),
		  ##diplomacy start+ can arise if using this to represent polygamy
		  (this_or_next|troop_slot_eq, ":town_lord", slot_troop_spouse, "trp_player"),
		     (troop_slot_eq, "trp_player", slot_troop_spouse, ":town_lord"),
		  (this_or_next|is_between, ":town_lord", heroes_begin, heroes_end),
		  ##diplomacy end+
		  (troop_slot_eq, "trp_player", slot_troop_spouse, ":town_lord"),

		  (assign, ":player_can_draw_from_garrison", 1),
		(try_end),

        (eq, ":player_can_draw_from_garrison", 1),
      ],
      "Manage the garrison {s10}",
      [
        (change_screen_exchange_members,1),
      ]),
	  ##diplomacy start+
	  #Other option to add troops to garrison
      ("dplmc_castle_give_troops",
      [
		(party_get_slot, ":town_lord", "$current_town", slot_town_lord),
		(store_faction_of_party, ":castle_faction", "$g_encountered_party"),
		(is_between, ":castle_faction", kingdoms_begin, kingdoms_end),

		#The player can add troops but not remove them:
		#Not owned by the player
		(neq, ":town_lord", "trp_player"),
		#Not unassigned
		(ge, ":town_lord", heroes_begin),
		#Not owned by the player's spouse
		(neg|troop_slot_eq, "trp_player", slot_troop_spouse, ":town_lord"),
		(neg|troop_slot_eq, ":town_lord", slot_troop_spouse, "trp_player"),
		#But nevertheless the owner will accept troops
		(call_script, "script_dplmc_player_can_give_troops_to_troop", ":town_lord"),

        (ge, reg0, 1),
      ],
      "Give troops to the garrison (cannot remove)",
      [
        (change_screen_give_members, "$current_town"),
      ]),
      ##diplomacy end+

      ("castle_wait",
      [
        #(party_slot_eq,"$current_town",slot_party_type, spt_castle),
        (this_or_next|ge, "$g_encountered_party_relation", 0),
        (eq,"$castle_undefended",1),
        (assign, ":can_rest", 1),
        (str_clear, s1),
        (try_begin),
          (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
          (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
          (neg|party_slot_eq, "$current_town", slot_town_lord, ":player_spouse"),

          (party_slot_ge, "$current_town", slot_town_lord, "trp_player"), #can rest for free in castles and towns with unassigned lords
          (store_faction_of_party, ":current_town_faction", "$current_town"),
          (neq, ":current_town_faction", "fac_player_supporters_faction"),
          (party_get_num_companions, ":num_men", "p_main_party"),
          (store_div, reg1, ":num_men", 4),
          (val_add, reg1, 1),
          (str_store_string, s1, "@ ({reg1} denars per night)"),
          (store_troop_gold, ":gold", "trp_player"),
          (lt, ":gold", reg1),
          (assign, ":can_rest", 0),
        (try_end),
        (eq, ":can_rest", 1),
      ],
      "Wait here for some time{s1}.",
      [
        (assign, "$auto_enter_town", "$current_town"),
        (assign, "$g_town_visit_after_rest", 1),
        (assign, "$g_last_rest_center", "$current_town"),
        (assign, "$g_last_rest_payment_until", -1),

        (try_begin),
          (party_is_active, "p_main_party"),
          (party_get_current_terrain, ":cur_terrain", "p_main_party"),
          (try_begin),
            (eq, ":cur_terrain", rt_desert),
            (unlock_achievement, ACHIEVEMENT_SARRANIDIAN_NIGHTS),
          (try_end),
        (try_end),

        (rest_for_hours_interactive, 24 * 7, 5, 0), #rest while not attackable
        (change_screen_return),
      ]),

##      ("rest_until_morning",
##       [
##           (this_or_next|ge, "$g_encountered_party_relation", 0),
##           (eq,"$castle_undefended",1),
##           (store_time_of_day,reg(1)),(neg|is_between,reg(1), 5, 18),
##           (eq, "$g_defending_against_siege", 0),
##        ],
##         "Rest until morning.",
##         [
##           (store_time_of_day,reg(1)),
##           (assign, reg(2), 30),
##           (val_sub,reg(2),reg(1)),
##           (val_mod,reg(2),24),
##           (assign,"$auto_enter_town","$current_town"),
##           (assign, "$g_town_visit_after_rest", 1),
##           (rest_for_hours_interactive, reg(2)),
##           (change_screen_return),
##          ]),
##
##      ("rest_until_evening",
##       [
##           (this_or_next|ge, "$g_encountered_party_relation", 0),
##           (eq,"$castle_undefended",1),
##           (store_time_of_day,reg(1)), (is_between,reg(1), 5, 18),
##           (eq, "$g_defending_against_siege", 0),
##        ],
##         "Rest until evening.",
##         [
##           (store_time_of_day,reg(1)),
##           (assign, reg(2), 20),
##           (val_sub,reg(2),reg(1)),
##           (assign,"$auto_enter_town","$current_town"),
##           (assign, "$g_town_visit_after_rest", 1),
##           (rest_for_hours_interactive, reg(2)),
##           (change_screen_return),
##          ]),
      # ("town_alley",
      # [
        # (party_slot_eq,"$current_town",slot_party_type, spt_town),
        # (eq, "$cheat_mode", 1),
      # ],
      # "{!}CHEAT: Go to the alley.",
      # [
        # (party_get_slot, reg11, "$current_town", slot_town_alley),
        # (set_jump_mission, "mt_ai_training"),
        # (jump_to_scene, reg11),
        # (change_screen_mission),
      # ]),

      ("collect_taxes_qst",
      [
        (check_quest_active, "qst_collect_taxes"),
        (quest_slot_eq, "qst_collect_taxes", slot_quest_target_center, "$current_town"),
        (neg|quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 4),
        (quest_get_slot, ":quest_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
        (str_store_troop_name, s1, ":quest_giver_troop"),
        (quest_get_slot, reg5, "qst_collect_taxes", slot_quest_current_state),
      ],
      "{reg5?Continue collecting taxes:Collect taxes} due to {s1}.",
      [
        (jump_to_menu, "mnu_collect_taxes"),
      ]),
      ##diplomacy begin
      ("dplmc_guild_master_meeting",
       [(party_slot_eq,"$current_town",slot_party_type, spt_town),
	    ##nested diplomacy start+
		#rubik had a good idea: only enable this after meeting the guild master
		#^^ fuck that ^^ ALWAYS can jump to guild master
		(assign, ":can_meet_guild_master", 1),
	],
       "Meet the Guild Master.",
        [
          (try_begin),
            (call_script, "script_cf_enter_center_location_bandit_check"),
          (else_try), #SB : unified script call
            (call_script, "script_start_town_conversation", slot_town_elder, 11),
           # (party_get_slot, ":town_scene", "$current_town", slot_town_center),
           # (modify_visitors_at_site, ":town_scene"),
           # (reset_visitors),

           # (party_get_slot, ":guild_master_troop", "$current_town",slot_town_elder),
           # (set_visitor,11,":guild_master_troop"),

           # (set_jump_mission,"mt_town_center"),
           # (jump_to_scene, ":town_scene"),
           # (change_screen_map_conversation, ":guild_master_troop"),
          (try_end),
     ]),
	##nested diplomacy start+
	#If you can't jump to the guild master, explain why		
	 ##nested diplomacy end+
	  ##diplomacy end
      ("town_leave",[],"Leave...",
      [
        (assign, "$g_permitted_to_center",0),
        (change_screen_return,0),
		##diplomacy start+
		#Porting rubik's autobuy/autosell from Custom Commander
		(try_begin),
		  (eq, "$sneaked_into_town", disguise_none), #SB : disable while disguised
		  (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
		  (call_script, "script_dplmc_initialize_autoloot", 0),#argument "0" means this does nothing if deemed unnecessary
		  (try_begin),
			(eq, "$g_dplmc_buy_food_when_leaving", 1),
			(party_get_slot, ":merchant_troop", "$current_town", slot_town_merchant),
			(gt, ":merchant_troop", 0),
			(call_script, "script_dplmc_auto_buy_food", "trp_player", ":merchant_troop"),
		  (try_end),
		  (try_begin),
			(eq, "$g_dplmc_sell_items_when_leaving", 1),
			(call_script, "script_dplmc_player_auto_sell_at_center", "$current_town"),
		  (try_end),
		(else_try), #SB : process leaving town guard check
          (gt, "$sneaked_into_town", disguise_none),
        (try_end),
		##diplomacy end+
      ],"Leave Area."),

      #SB : consolidated cheat options 
      ("town_cheat", [(ge, "$cheat_mode", 1),],
      "Use cheats.",
      [(jump_to_menu, "mnu_town_cheats"),
      ]),
      # ("castle_cheat_interior",
      # [
        # (eq, "$cheat_mode", 1),
      # ],
      # "{!}CHEAT! Interior.",
      # [
        # (set_jump_mission,"mt_ai_training"),
        # (party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
        # (jump_to_scene,":castle_scene"),
        # (change_screen_mission),
      # ]),

      # ("castle_cheat_town_exterior",
      # [
        # (eq, "$cheat_mode", 1),
      # ],
      # "{!}CHEAT! Exterior.",
      # [
        # (try_begin),
          # (party_slot_eq, "$current_town",slot_party_type, spt_castle),
          # (party_get_slot, ":scene", "$current_town", slot_castle_exterior),
        # (else_try),
          # (party_get_slot, ":scene", "$current_town", slot_town_center),
        # (try_end),
        # (set_jump_mission,"mt_ai_training"),
        # (jump_to_scene,":scene"),
        # (change_screen_mission),
      # ]),

      # ("castle_cheat_dungeon",
      # [
        # (eq, "$cheat_mode", 1),
      # ],
      # "{!}CHEAT! Prison.",
      # [
        # (set_jump_mission,"mt_ai_training"),
        # (party_get_slot, ":castle_scene", "$current_town", slot_town_prison),
        # (jump_to_scene,":castle_scene"),
        # (change_screen_mission),
      # ]),

      # ("castle_cheat_town_walls",
      # [
        # (eq, "$cheat_mode", 1),
        # (party_slot_eq,"$current_town",slot_party_type, spt_town),
      # ],
      # "{!}CHEAT! Town Walls.",
      # [
        # (party_get_slot, ":scene", "$current_town", slot_town_walls),
        # (set_jump_mission,"mt_ai_training"),
        # (jump_to_scene,":scene"),
        # (change_screen_mission),
      # ]),

      # ("cheat_town_start_siege",
      # [
        # (eq, "$cheat_mode", 1),
        # (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
        # (lt, "$g_encountered_party_2", 1),
        # (call_script, "script_party_count_fit_for_battle","p_main_party"),
        # (gt, reg(0), 1),
        # (try_begin),
          # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          # (assign, reg6, 1),
        # (else_try),
          # (assign, reg6, 0),
        # (try_end),
      # ],
      # "{!}CHEAT: Besiege the {reg6?town:castle}...",
      # [
        # (assign,"$g_player_besiege_town","$g_encountered_party"),
        # (jump_to_menu, "mnu_castle_besiege"),
      # ]),

      # ("center_reports",
      # [
        # (eq, "$cheat_mode", 1),
      # ],
      # "{!}CHEAT! Show reports.",
      # [
        # (jump_to_menu,"mnu_center_reports"),
      # ]),

      # ("sail_from_port",
      # [
        # (party_slot_eq,"$current_town",slot_party_type, spt_town),
        # (eq, "$cheat_mode", 1),
        # #(party_slot_eq,"$current_town",slot_town_near_shore, 1),
      # ],
      # "{!}CHEAT: Sail from port.",
      # [
        # (assign, "$g_player_icon_state", pis_ship),
        # (party_set_flags, "p_main_party", pf_is_ship, 1),
        # (party_get_position, pos1, "p_main_party"),
        # (map_get_water_position_around_position, pos2, pos1, 6),
        # (party_set_position, "p_main_party", pos2),
        # (assign, "$g_main_ship_party", -1),
        # (change_screen_return),
      # ]),

    ]
   ),



  (
    "cannot_enter_court",0,
    "There is a feast in progress in the lord's hall, but you are not of sufficient status to be invited inside. Perhaps increasing your renown would win you admittance -- or you might also try distinguishing yourself at a tournament while the feast is in progress...",
    "none",
    [],
    [
    ("continue", [],"Continue",
       [
        (jump_to_menu, "mnu_town"),
        ]),
    ]),


  (
    "lady_visit",0,
    "Whom do you wish to visit?",
    "none",
    [],
    [

	("visit_lady_1", [
	(gt, "$love_interest_in_town", 0),
	(str_store_troop_name, s12, "$love_interest_in_town"),
	],
	  "Visit {s12}",
       [
	    (assign, "$love_interest_in_town", "$love_interest_in_town"),
        (jump_to_menu, "mnu_garden"),
        ]),



	("visit_lady_2", [
	(gt, "$love_interest_in_town_2", 0),
	(str_store_troop_name, s12, "$love_interest_in_town_2"),
	],
	  "Visit {s12}",
       [
	    (assign, "$love_interest_in_town", "$love_interest_in_town_2"),
        (jump_to_menu, "mnu_garden"),
        ]),

	("visit_lady_3", [
	(gt, "$love_interest_in_town_3", 0),
	(str_store_troop_name, s12, "$love_interest_in_town_3"),
	],
	  "Visit {s12}",
       [
	    (assign, "$love_interest_in_town", "$love_interest_in_town_3"),
        (jump_to_menu, "mnu_garden")], "Door to the garden."),


	("visit_lady_4", [(gt, "$love_interest_in_town_4", 0),(str_store_troop_name, s12, "$love_interest_in_town_4"),],
	"Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_4"),(jump_to_menu, "mnu_garden"),]),

	("visit_lady_5", [(gt, "$love_interest_in_town_5", 0),(str_store_troop_name, s12, "$love_interest_in_town_5"),],
	"Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_5"),(jump_to_menu, "mnu_garden"),]),

	("visit_lady_6",[(gt, "$love_interest_in_town_6", 0),(str_store_troop_name, s12, "$love_interest_in_town_6"),],
	"Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_6"),(jump_to_menu, "mnu_garden"),]),

	("visit_lady_7",[(gt, "$love_interest_in_town_7", 0),(str_store_troop_name, s12, "$love_interest_in_town_7"),],
	"Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_7"),(jump_to_menu, "mnu_garden"),]),

	("visit_lady_8",[(gt, "$love_interest_in_town_8", 0),(str_store_troop_name, s12, "$love_interest_in_town_8"),],
	"Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_8"),(jump_to_menu, "mnu_garden"),]),


	("leave",[], "Leave",[(jump_to_menu, "mnu_town")]),

    ]
	),


  (
    "town_tournament_lost",0,
    "You have been eliminated from the tournament.{s8}",
    "none",
    [
	(str_clear, s8),
	(try_begin),
		(this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
			(neg|troop_slot_ge, "trp_player", slot_troop_renown, 50),
		(neg|troop_slot_ge, "trp_player", slot_troop_renown, 125),
		(gt, "$g_player_tournament_placement", 4),
		(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, sfai_feast),
		(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),
		(str_store_string, s8, "str__however_you_have_sufficiently_distinguished_yourself_to_be_invited_to_attend_the_ongoing_feast_in_the_lords_castle"),
	(try_end),

        ],
    [
      ("continue", [], "Continue...",
       [(jump_to_menu, "mnu_town_tournament_won_by_another"),
        ]),
    ]
  ),

  (
    "orig_town_tournament_won",mnf_disable_all_keys,
    "You have won the tournament of {s3}! You are filled with pride as the crowd cheers your name.\
 In addition to honour, fame and glory, you earn a prize of {reg9} denars, as well as one mystery prize. {s8}",
    "none",
    [
        (str_store_party_name, s3, "$current_town"),
        (call_script, "script_change_troop_renown", "trp_player", 20),
        (call_script, "script_change_player_relation_with_center", "$current_town", 1),
        # (assign, reg9, 200),
        # (add_xp_to_troop, 250, "trp_player"),
        (assign, reg9, 1000),
        (add_xp_to_troop, 250, "trp_player"),
        (troop_add_gold, "trp_player", reg9),
        (str_clear, s8),
        (store_add, ":total_win", "$g_tournament_bet_placed", "$g_tournament_bet_win_amount"),
        (try_begin),
          (gt, "$g_tournament_bet_win_amount", 0),
          (assign, reg8, ":total_win"),
          (str_store_string, s8, "@Moreover, you earn {reg8} denars from the clever bets you placed on yourself..."),
        (try_end),
		(try_begin),
			(this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
				(neg|troop_slot_ge, "trp_player", slot_troop_renown, 70),
			(neg|troop_slot_ge, "trp_player", slot_troop_renown, 145),

			(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, sfai_feast),
			(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),
			(str_store_string, s8, "str_s8_you_are_also_invited_to_attend_the_ongoing_feast_in_the_castle"),
		(try_end),
        (troop_add_gold, "trp_player", ":total_win"),
        (assign, ":player_odds_sub", 0),
        (store_div, ":player_odds_sub", "$g_tournament_bet_win_amount", 5),
        (party_get_slot, ":player_odds", "$current_town", slot_town_player_odds),
        (val_sub, ":player_odds", ":player_odds_sub"),
        (val_max, ":player_odds", 250),

        (party_set_slot, "$current_town", slot_town_player_odds, ":player_odds"),
        (call_script, "script_play_victorious_sound"),

        (unlock_achievement, ACHIEVEMENT_MEDIEVAL_TIMES),
        #SB : stop arena loop sound if it leaks here
        (stop_all_sounds, 0),
        #also add background
        (set_background_mesh, "mesh_pic_payment"),
        #also gives bonus faction morale
        (call_script, "script_change_faction_troop_morale", "$g_encountered_party_faction", ":player_odds", 1),
        ],
    [
      ("continue", [], "Collect your prize...",
       [(jump_to_menu, "mnu_town"),
       (call_script, "script_get_random_tournament_prize", "$current_town"),
       (change_screen_loot, "trp_salt_mine_merchant"),
        ]),
    ]
  ),

  (
    "town_tournament_won_by_another",mnf_disable_all_keys,
    "As the only {reg3?fighter:man} to remain undefeated this day, {s1} wins the lists and the glory of this tournament.",
    "none",
    [
      (call_script, "script_get_num_tournament_participants"),
      (store_sub, ":needed_to_remove_randomly", reg0, 1),
      (try_begin),
        (troop_slot_eq, "trp_tournament_participants", 0, 0), #delete player from the participants
        (troop_set_slot, "trp_tournament_participants", 0, -1),
        (val_sub, ":needed_to_remove_randomly", 1),
      (try_end),
        (call_script, "script_remove_tournament_participants_randomly", ":needed_to_remove_randomly"),
        (call_script, "script_sort_tournament_participant_troops"),
        (troop_get_slot, ":winner_troop", "trp_tournament_participants", 0),
        (str_store_troop_name, s1, ":winner_troop"),
        (try_begin),
          (troop_is_hero, ":winner_troop"),
          (call_script, "script_change_troop_renown", ":winner_troop", 20),
        (try_end),
		  ##diplomacy start+ use script for gender
        #(troop_get_type, reg3, ":winner_troop"),#<- OLD
		(call_script, "script_dplmc_store_troop_is_female_reg", ":winner_troop", 3),
		  ##diplomacy end+
        #SB : stop arena sound if it leaks here
        (stop_all_sounds, 0),
        (set_background_mesh, "mesh_pic_payment"),
        ],
    [
      ("continue", [], "Continue...",
       [(jump_to_menu, "mnu_town"),
        ]),
    ]
  ),

  (
    "orig_town_tournament",mnf_disable_all_keys,
    "{s1}You are at tier {reg0} of the tournament, with {reg1} participants remaining. In the next round, there will be {reg2} teams with {reg3} {reg4?fighters:fighter} each.",
    "none",
    [
        (party_set_slot, "$current_town", slot_town_has_tournament, 0), #No way to return back if this menu is left
        (call_script, "script_sort_tournament_participant_troops"),#Moving trp_player to the top of the list
        (call_script, "script_get_num_tournament_participants"),
        (assign, ":num_participants", reg0),
        (try_begin),
          (neg|troop_slot_eq, "trp_tournament_participants", 0, 0),#Player is defeated

          (assign, ":player_odds_add", 0),
          (store_div, ":player_odds_add", "$g_tournament_bet_placed", 5),
          (party_get_slot, ":player_odds", "$current_town", slot_town_player_odds),
          (val_add, ":player_odds", ":player_odds_add"),
          (val_min, ":player_odds", 4000),
          (party_set_slot, "$current_town", slot_town_player_odds, ":player_odds"),

          (jump_to_menu, "mnu_town_tournament_lost"),
        (else_try),
          (eq, ":num_participants", 1),#Tournament won
          (jump_to_menu, "mnu_town_tournament_won"),
        (else_try),
          (try_begin),
            (le, "$g_tournament_next_num_teams", 0),
            (call_script, "script_get_random_tournament_team_amount_and_size"),
            (assign, "$g_tournament_next_num_teams", reg0),
            (assign, "$g_tournament_next_team_size", reg1),
          (try_end),
          (assign, reg2, "$g_tournament_next_num_teams"),
          (assign, reg3, "$g_tournament_next_team_size"),
          (store_sub, reg4, reg3, 1),
          (str_clear, s1),
          (try_begin),
            (eq, "$g_tournament_player_team_won", 1),
            (str_store_string, s1, "@Victory is yours! You have won this melee, but now you must prepare yourself for the next round. "),
          (else_try),
            (eq, "$g_tournament_player_team_won", 0),
            (str_store_string, s1, "@You have been bested in this melee, but the master of ceremonies declares a recognition of your skill and bravery, allowing you to take part in the next round. "),
          (try_end),
          (assign, reg1, ":num_participants"),
          (store_add, reg0, "$g_tournament_cur_tier", 1),
        (try_end),
        ],
    [
      ("host_tournament",
      [(ge, "$cheat_mode", 1),],
      "{!}Cheat : Win tournament",
      [
           (jump_to_menu, "mnu_town_tournament_won"),
           (assign, "$g_player_eligible_feast_center_no", "$current_town"),
		   (assign, "$g_player_tournament_placement", 100),
      ]),
      ("tournament_view_participants", [], "View participants.",
       [(jump_to_menu, "mnu_tournament_participants"),
        ]),
      ("tournament_bet", [(neq, "$g_tournament_cur_tier", "$g_tournament_last_bet_tier")], "Place a bet on yourself.",
       [(jump_to_menu, "mnu_tournament_bet"),
        ]),
      ("tournament_join_next_fight", [], "Fight in the next round.",
       [
           (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
           (modify_visitors_at_site, ":arena_scene"),
           (reset_visitors),
           #Assuming that there are enough participants for the teams
		   (assign, "$g_player_tournament_placement", "$g_tournament_cur_tier"),
		   (try_begin),
		     (gt, "$g_player_tournament_placement", 4),
		     (assign, "$g_player_eligible_feast_center_no", "$current_town"),
		   (try_end),
           (val_add, "$g_tournament_cur_tier", 1),

           (store_mul, "$g_tournament_num_participants_for_fight", "$g_tournament_next_num_teams", "$g_tournament_next_team_size"),
           (troop_set_slot, "trp_tournament_participants", 0, -1),#Removing trp_player from the list
           (troop_set_slot, "trp_temp_array_a", 0, "trp_player"),
           (try_for_range, ":slot_no", 1, "$g_tournament_num_participants_for_fight"),
             (call_script, "script_get_random_tournament_participant"),
             (troop_set_slot, "trp_temp_array_a", ":slot_no", reg0),
           (try_end),
           (call_script, "script_shuffle_troop_slots", "trp_temp_array_a", 0, "$g_tournament_num_participants_for_fight"),


           (try_for_range, ":slot_no", 0, 4),#shuffle teams
             (troop_set_slot, "trp_temp_array_b", ":slot_no", ":slot_no"),
           (try_end),
           (call_script, "script_shuffle_troop_slots", "trp_temp_array_b", 0, 4),

           (assign, ":cur_slot", 0),
           (assign, ":player_slot", -1), #SB : find player's slot
           (try_for_range, ":cur_team_offset", 0, "$g_tournament_next_num_teams"),
             (troop_get_slot, ":cur_team", "trp_temp_array_b", ":cur_team_offset"),

             (try_for_range, ":slot_no", 0, 8),#shuffle entry_points
               (troop_set_slot, "trp_temp_array_c", ":slot_no", ":slot_no"),
             (try_end),
             (call_script, "script_shuffle_troop_slots", "trp_temp_array_c", 0, 8),

             (try_for_range, ":cur_index", 0, "$g_tournament_next_team_size"),
               (store_mul, ":cur_entry_point", ":cur_team", 8),
               (troop_get_slot, ":entry_offset", "trp_temp_array_c", ":cur_index"),
               (val_add, ":cur_entry_point", ":entry_offset"),
               (troop_get_slot, ":troop_no", "trp_temp_array_a", ":cur_slot"),
               (set_visitor, ":cur_entry_point", ":troop_no"),
               (try_begin), #SB : set player's slot
                 (eq, ":troop_no", "trp_player"),
                 (assign, ":player_slot", ":cur_entry_point"),
               (try_end),
               (val_add, ":cur_slot", 1),
             (try_end),
           (try_end),

           (assign, "$g_tournament_next_num_teams", 0),
           (assign, "$g_tournament_next_team_size", 0),

           (assign, "$g_mt_mode", abm_tournament),
           #SB : pass on as global
           (try_begin),
             (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$g_encountered_party_faction"),
             (this_or_next|ge, reg0, DPLMC_FACTION_STANDING_MEMBER),
             (party_slot_ge, "$current_town", slot_center_player_relation, 15),
             (assign, "$g_player_entry_point", ":player_slot"),
           (else_try),
             (assign, "$g_player_entry_point", -1),
           (try_end),

           (party_get_slot, ":town_original_faction", "$current_town", slot_center_original_faction),
           (assign, ":town_index_within_faction", 0),
           (assign, ":end_cond", towns_end),
           (try_for_range, ":cur_town", towns_begin, ":end_cond"),
             (try_begin),
               (eq, ":cur_town", "$current_town"),
               (assign, ":end_cond", 0), #break
             (else_try),
               (party_slot_eq, ":cur_town", slot_center_original_faction, ":town_original_faction"),
               (val_add, ":town_index_within_faction", 1),
             (try_end),
           (try_end),

           (set_jump_mission, "mt_arena_melee_fight"),

           (try_begin),
             (eq, ":town_original_faction", "fac_kingdom_1"),
             #Swadia
             (store_mod, ":mod", ":town_index_within_faction", 4),
             (try_begin), #parameters: horse, lance, sword, axe, bow, javelin, horse-archer, crossbow, armor begin, helm begin
               (eq, ":mod", 0),
               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 0, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
             (else_try),
               (eq, ":mod", 1),
               (call_script, "script_set_items_for_tournament", 100, 100, 0, 0, 0, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
             (else_try),
               (eq, ":mod", 2),
               (call_script, "script_set_items_for_tournament", 100, 0, 100, 0, 0, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
             (else_try),
               (eq, ":mod", 3),
               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 40, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
             (try_end),
           (else_try),
             (eq, ":town_original_faction", "fac_kingdom_2"),
             #Vaegirs
             (store_mod, ":mod", ":town_index_within_faction", 4),
             (try_begin),
               (eq, ":mod", 0),
               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 0, 0, 0, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
             (else_try),
               (eq, ":mod", 1),
               (call_script, "script_set_items_for_tournament", 100, 50, 0, 0, 0, 20, 30, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
             (else_try),
               (eq, ":mod", 2),
               (call_script, "script_set_items_for_tournament", 100, 0, 50, 0, 0, 20, 30, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
             (else_try),
               (eq, ":mod", 3),
               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 30, 0, 60, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
             (try_end),
           (else_try),
             (eq, ":town_original_faction", "fac_kingdom_3"),
             #Khergit
             (store_mod, ":mod", ":town_index_within_faction", 2),
             (try_begin),
               (eq, ":mod", 0),
               (call_script, "script_set_items_for_tournament", 100, 0, 0, 0, 0, 40, 60, 0, "itm_arena_tunic_red", "itm_steppe_helmet_red"),
             (else_try),
               (eq, ":mod", 1),
               (call_script, "script_set_items_for_tournament", 100, 50, 25, 0, 0, 30, 50, 0, "itm_arena_tunic_red", "itm_steppe_helmet_red"),
             (try_end),
           (else_try),
             (eq, ":town_original_faction", "fac_kingdom_4"),
             #Nords
             (store_mod, ":mod", ":town_index_within_faction", 3),
             (try_begin),
               (eq, ":mod", 0),
               (call_script, "script_set_items_for_tournament", 0, 0, 50, 80, 0, 0, 0, 0, "itm_arena_armor_red", -1),
             (else_try),
               (eq, ":mod", 1),
               (call_script, "script_set_items_for_tournament", 0, 0, 50, 80, 50, 0, 0, 0, "itm_arena_armor_red", -1),
             (else_try),
               (eq, ":mod", 2),
               (call_script, "script_set_items_for_tournament", 40, 0, 0, 100, 0, 0, 0, 0, "itm_arena_armor_red", -1),
             (try_end),
           (else_try),
             #Rhodoks
             (eq, ":town_original_faction", "fac_kingdom_5"),
             (call_script, "script_set_items_for_tournament", 25, 100, 60, 0, 30, 0, 30, 50, "itm_arena_tunic_red", "itm_arena_helmet_red"),
           (else_try),
             #Sarranids
             (store_mod, ":mod", ":town_index_within_faction", 2),
             (try_begin),
               (eq, ":mod", 0),
               (call_script, "script_set_items_for_tournament", 100, 40, 60, 0, 30, 30, 0, 0, "itm_arena_tunic_red", "itm_arena_turban_red"),
             (else_try),
               (call_script, "script_set_items_for_tournament", 50, 0, 60, 0, 30, 30, 0, 0, "itm_arena_tunic_red", "itm_arena_turban_red"),
             (try_end),
           (try_end),
           (jump_to_scene, ":arena_scene"),
           (change_screen_mission),
        ]),
      ("leave_tournament",[],"Withdraw from the tournament.",
       [
           (jump_to_menu, "mnu_tournament_withdraw_verify"),
        ]),
    ]
  ),

  (
    "tournament_withdraw_verify",0,
    "Are you sure you want to withdraw from the tournament?",
    "none",
    [],
    [
      ("tournament_withdraw_yes", [], "Yes. This is a pointless affectation.",
       [(jump_to_menu, "mnu_town_tournament_won_by_another"),
        ]),
      ("tournament_withdraw_no", [], "No, not as long as there is a chance of victory!",
       [(jump_to_menu, "mnu_town_tournament"),
        ]),
    ]
  ),

  (
    "tournament_bet",0,
    "The odds against you are {reg5} to {reg6}.{reg1? You have already bet {reg1} denars on yourself, and if you win, you will earn {reg2} denars.:} How much do you want to bet?",
    "none",
    [
      (assign, reg1, "$g_tournament_bet_placed"),
      (store_add, reg2, "$g_tournament_bet_win_amount", "$g_tournament_bet_placed"),
      (call_script, "script_get_win_amount_for_tournament_bet"),
      (assign, ":player_odds", reg0),
      (assign, ":min_dif", 100000),
      (assign, ":min_dif_divisor", 1),
      (assign, ":min_dif_multiplier", 1),
      (try_for_range, ":cur_multiplier", 1, 50),
        (try_for_range, ":cur_divisor", 1, 50),
          (store_mul, ":result", 100, ":cur_multiplier"),
          (val_div, ":result", ":cur_divisor"),
          (store_sub, ":difference", ":player_odds", ":result"),
          (val_abs, ":difference"),
          (lt, ":difference", ":min_dif"),
          (assign, ":min_dif", ":difference"),
          (assign, ":min_dif_divisor", ":cur_divisor"),
          (assign, ":min_dif_multiplier", ":cur_multiplier"),
        (try_end),
      (try_end),
      (assign, reg5, ":min_dif_multiplier"),
      (assign, reg6, ":min_dif_divisor"),
      ],
    [
      ("bet_100_denars", [(store_troop_gold, ":gold", "trp_player"),
                          (ge, ":gold", 100)
                          ],
       "100 denars.",
       [
         (assign, "$temp", 100),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_50_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 50)
                         ],
       "50 denars.",
       [
         (assign, "$temp", 50),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_20_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 20)
                         ],
       "20 denars.",
       [
         (assign, "$temp", 20),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_10_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 10)
                         ],
       "10 denars.",
       [
         (assign, "$temp", 10),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_5_denars", [(store_troop_gold, ":gold", "trp_player"),
                        (ge, ":gold", 5)
                        ],
       "5 denars.",
       [
         (assign, "$temp", 5),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("go_back_dot", [], "Go back.",
       [
         (jump_to_menu, "mnu_town_tournament"),
        ]),
    ]
  ),

  (
    "tournament_bet_confirm",0,
    "If you bet {reg1} denars, you will earn {reg2} denars if you win the tournament. Is that all right?",
    "none",
    [
      (call_script, "script_get_win_amount_for_tournament_bet"),
      (assign, ":win_amount", reg0),
      (val_mul, ":win_amount", "$temp"),
      (val_div, ":win_amount", 100),
      (assign, reg1, "$temp"),
      (assign, reg2, ":win_amount"),
      ],
    [
      ("tournament_bet_accept", [],
       "Go ahead.",
       [
         (call_script, "script_tournament_place_bet", "$temp"),
         (jump_to_menu, "mnu_town_tournament"),
         ]),
      ("tournament_bet_cancel", [],
       "Forget it.",
       [
         (jump_to_menu, "mnu_tournament_bet"),
         ]),
    ]
  ),

  (
    "tournament_participants",0,
    "You ask one of the criers for the names of the tournament participants. They are:^{s11}",
    "none",
    [
        (str_clear, s11),
        (call_script, "script_sort_tournament_participant_troops"),
        (call_script, "script_get_num_tournament_participants"),
        (assign, ":num_participants", reg0),
        (try_for_range, ":cur_slot", 0, ":num_participants"),
          (troop_get_slot, ":troop_no", "trp_tournament_participants", ":cur_slot"),
          (str_store_troop_name, s12, ":troop_no"),
          (str_store_string, s11, "@{!}{s11}^{s12}"),
        (try_end),
        ],
    [
      ("go_back_dot", [], "Go back.",
       [(jump_to_menu, "mnu_town_tournament"),
        ]),
    ]
  ),


  (
    "collect_taxes",mnf_disable_all_keys,
    "As the party member with the highest trade skill ({reg2}), {reg3?you expect:{s1} expects} that collecting taxes from here will take {reg4} days...",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_trade"),
     (assign, ":max_skill", reg0),
     (assign, reg2, reg0),
     (assign, ":max_skill_owner", reg1),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s1, ":max_skill_owner"),
     (try_end),
     (assign, ":tax_quest_expected_revenue", 3000),
     (try_begin),
       (party_slot_eq, "$current_town", slot_party_type, spt_town),
       (assign, ":tax_quest_expected_revenue", 6000),
     (try_end),

     (try_begin),
       (quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 0),
       (store_add, ":max_skill_plus_thirty", ":max_skill", 30),
       (try_begin),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (store_div, "$qst_collect_taxes_total_hours", 24* 7 * 30, ":max_skill_plus_thirty"),
       (else_try),
         #Village
         (store_div, "$qst_collect_taxes_total_hours", 24 * 3 * 30, ":max_skill_plus_thirty"),
       (try_end),

       (call_script, "script_party_count_fit_for_battle", "p_main_party"),
       (val_add, reg0, 20),
       (val_mul, "$qst_collect_taxes_total_hours", 20),
       (val_div, "$qst_collect_taxes_total_hours", reg0),


       (quest_set_slot, "qst_collect_taxes", slot_quest_target_amount, "$qst_collect_taxes_total_hours"),
       (store_div, ":menu_begin_time", "$qst_collect_taxes_total_hours", 20),#between %5-%25
       (store_div, ":menu_end_time", "$qst_collect_taxes_total_hours", 4),
       (assign, ":unrest_begin_time", ":menu_end_time"),#between %25-%75
       (store_mul, ":unrest_end_time", "$qst_collect_taxes_total_hours", 3),
       (val_div, ":unrest_end_time", 4),

       (val_mul, ":tax_quest_expected_revenue", 2),
       (store_div, "$qst_collect_taxes_hourly_income", ":tax_quest_expected_revenue", "$qst_collect_taxes_total_hours"),

       (store_random_in_range, "$qst_collect_taxes_menu_counter", ":menu_begin_time", ":menu_end_time"),
       (store_random_in_range, "$qst_collect_taxes_unrest_counter", ":unrest_begin_time", ":unrest_end_time"),
       (assign, "$qst_collect_taxes_halve_taxes", 0),
     (try_end),
     (quest_get_slot, ":target_hours", "qst_collect_taxes", slot_quest_target_amount),
     (store_div, ":target_days", ":target_hours", 24),
     (val_mul, ":target_days", 24),
     (try_begin),
       (lt, ":target_days", ":target_hours"),
       (val_add, ":target_days", 24),
     (try_end),
     (val_div, ":target_days", 24),
     (assign, reg4, ":target_days"),
     ],
    [
      ("start_collecting", [], "Start collecting.",
       [(assign, "$qst_collect_taxes_currently_collecting", 1),
        (try_begin),
          (quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 0),
          (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 1),
        (try_end),
        (rest_for_hours_interactive, 1000, 5, 0), #rest while not attackable
        (assign,"$auto_enter_town","$current_town"),
        (assign, "$g_town_visit_after_rest", 1),
        (change_screen_return),
        ]),
      ("collect_later", [], "Put it off until later.",
       [(try_begin),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_town"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
        ]),
    ]
  ),

  (
    "collect_taxes_complete",mnf_disable_all_keys,
    ##diplomacy start+
    ##Replace "him" with "{reg4?her:him}"
    "You've collected {reg3} denars in taxes from {s3}. {s19} will be expecting you to take the money to {reg4?her:him}.",
    ##diplomacy end+
    "none",
    [(str_store_party_name, s3, "$current_town"),
     (quest_get_slot, ":quest_giver", "qst_collect_taxes", slot_quest_giver_troop),
     (str_store_troop_name, s19, ":quest_giver"),
     ##diplomacy start+

     (try_begin),
       (eq, "$qst_collect_taxes_halve_taxes", 0),
       (call_script, "script_change_player_relation_with_center", "$current_town", -2),
     (try_end),
     (call_script, "script_succeed_quest", "qst_collect_taxes"),
     
     #SB : add renown to tax collector
     (try_begin),
       (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
       (neq, reg1, "trp_player"),
       (call_script, "script_change_troop_renown", reg1, dplmc_companion_skill_renown),
     (try_end),
     
     (quest_get_slot, reg3, "qst_collect_taxes", slot_quest_gold_reward),
     ##Store quest giver gender to reg4
     (call_script, "script_dplmc_store_troop_is_female_reg", ":quest_giver", 4), #SB : use other script
     ##diplomacy end+
     ],
    [
      ("continue", [], "Continue...",
       [(change_screen_return),
        ]),
    ]
  ),

  (
    "collect_taxes_rebels_killed",0,
    "Your quick action and strong arm have successfully put down the revolt.\
 Surely, anyone with a mind to rebel against you will think better of it after this.",
    "none",
    [
    ],
    [
      ("continue", [], "Continue...",
       [(change_screen_map),
        ]),
    ]
  ),

  (
    "collect_taxes_failed",mnf_disable_all_keys,
##diplomacy start+ fix gender of pronoun
    "You could collect only {reg3} denars as tax from {s3} before the revolt broke out.\
 {s1} won't be happy, but some silver will placate {reg4?her:him} better than nothing at all...",
##diplomacy end+
    "none",
    [#SB : set up picture
     (try_begin),
       (eq, "$character_gender", tf_male),
       (set_background_mesh, "mesh_pic_escape_1"),
     (else_try),
       (eq, "$character_gender", tf_male),
       (set_background_mesh, "mesh_pic_escape_1_fem"),
     (try_end),
     (str_store_party_name, s3, "$current_town"),
     (quest_get_slot, ":quest_giver", "qst_collect_taxes", slot_quest_giver_troop),
     ##diplomacy start+ store gender of quest giver in reg4
     (call_script, "script_dplmc_store_troop_is_female", ":quest_giver"),
     (assign, reg4, reg0),
     ##diplomacy end+
     (str_store_troop_name, s1, ":quest_giver"),
     (quest_get_slot, reg3, "qst_collect_taxes", slot_quest_gold_reward),
     (call_script, "script_fail_quest", "qst_collect_taxes"),
     (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 4),
     (rest_for_hours, 0, 0, 0), #stop resting
     ],
    [
      ("continue", [], "Continue...",
        [#SB : lose renown
          (call_script, "script_change_troop_renown", "trp_player", -2),
          (change_screen_map),
        ]),
    ]
  ),

  (
    "collect_taxes_revolt_warning",0,
    "The people of {s3} are outraged at your demands and decry it as nothing more than extortion.\
 They're getting very restless, and they may react badly if you keep pressing them.",
    "none",
    [(str_store_party_name, s3, "$current_town"),
     ],
    [
      ("continue_collecting_taxes", [], "Ignore them and continue.",
       [ #SB : objectionable action
       (call_script, "script_objectionable_action", tmt_egalitarian, "str_repress_farmers"),
       (change_screen_return),]),
      ("halve_taxes", [(quest_get_slot, ":quest_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
                       (str_store_troop_name, s1, ":quest_giver_troop"),],
       "Agree to reduce your collection by half. ({s1} may be upset)",
       [(assign, "$qst_collect_taxes_halve_taxes", 1),
        (change_screen_return),
        ]),
    ]
  ),

  (
    "collect_taxes_revolt",0,
    "You are interrupted while collecting the taxes at {s3}. A large band of angry {reg9?peasants:townsmen} is marching nearer,\
 shouting about the exorbitant taxes and waving torches and weapons. It looks like they aim to fight you!",
    "none",
    [(str_store_party_name, s3, "$current_town"),
     #SB : town pictures
     (try_begin),
       (party_slot_eq, "$current_town", slot_party_type, spt_village),
       (assign, reg9, 1),
       (set_background_mesh, "mesh_pic_villageriot"),
     (else_try),
       (set_background_mesh, "mesh_pic_townriot"),
       (assign, reg9, 0),
     (try_end),
     ],
    [
      ("continue", [], "Continue...",
       [(set_jump_mission,"mt_back_alley_revolt"),
        (quest_get_slot, ":target_center", "qst_collect_taxes", slot_quest_target_center),
        (try_begin),
          (party_slot_eq, ":target_center", slot_party_type, spt_town),
          (party_get_slot, ":town_alley", ":target_center", slot_town_alley),
        (else_try),
          (party_get_slot, ":town_alley", ":target_center", slot_castle_exterior),
        (try_end),
        (modify_visitors_at_site,":town_alley"),
        (reset_visitors),
        (assign, ":num_rebels", 6),
        (store_character_level, ":level", "trp_player"),
        (val_div, ":level", 5),
        (val_add, ":num_rebels", ":level"),
        (set_visitors, 1, "trp_tax_rebel", ":num_rebels"),
        (jump_to_scene,":town_alley"),
        (change_screen_mission),
        ]),
    ]
  ),

# They must learn field discipline and the steadiness to follow orders in combat before they can be thought to use arms.",
  (
    "train_peasants_against_bandits",0,
    "As the party member with the highest training skill ({reg2}), {reg3?you expect:{s1} expects} that getting some peasants ready for practice will take {reg4} hours.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
     (assign, ":max_skill", reg0),
     (assign, reg2, reg0),
     (assign, ":max_skill_owner", reg1),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s1, ":max_skill_owner"),
     (try_end),
     (store_sub, ":needed_hours", 20, ":max_skill"),
     (val_mul, ":needed_hours", 3),
     (val_div, ":needed_hours", 5),
     (store_sub, reg4, ":needed_hours", "$qst_train_peasants_against_bandits_num_hours_trained"),
     ],
    [
      ("make_preparation", [], "Train them.",
       [
         (assign, "$qst_train_peasants_against_bandits_currently_training", 1),
         (rest_for_hours_interactive, 1000, 5, 0), #rest while not attackable
         (assign, "$auto_enter_town", "$current_town"),
         (assign, "$g_town_visit_after_rest", 1),
         (change_screen_return),
         ]),
      ("train_later", [], "Put it off until later.",
       [
         (jump_to_menu, "mnu_village"),
        ]),
    ]
  ),

  (
    "train_peasants_against_bandits_ready",0,
    "You put the peasants through the basics of soldiering, discipline and obedience.\
 You think {reg0} of them {reg1?have:has} fully grasped the training and {reg1?are:is} ready for some practice.",
    "none",
    [
      (store_character_level, ":level", "trp_player"),
      (val_div, ":level", 10),
      (val_add, ":level", 1),
      (quest_get_slot, ":quest_target_amount", "qst_train_peasants_against_bandits", slot_quest_target_amount),
      (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
      (val_sub, ":quest_target_amount", ":quest_current_state"),
      (assign, ":max_random", ":level"),
      (val_min, ":max_random", ":quest_target_amount"),
      (val_add, ":max_random", 1),
      (store_random_in_range, ":random_number", 1, ":max_random"),
      (assign, "$g_train_peasants_against_bandits_num_peasants", ":random_number"),
      (assign, reg0, ":random_number"),
      (store_sub, reg1, ":random_number", 1),
      (str_store_troop_name_by_count, s0, "trp_trainee_peasant", ":random_number"),
     ],
    [
      ("peasant_start_practice", [], "Start the practice fight.",
       [
         (set_jump_mission,"mt_village_training"),
         (quest_get_slot, ":target_center", "qst_train_peasants_against_bandits", slot_quest_target_center),
         (party_get_slot, ":village_scene", ":target_center", slot_castle_exterior),
         (modify_visitors_at_site, ":village_scene"),
         (reset_visitors),
         (set_visitor, 0, "trp_player"),
         (set_visitors, 1, "trp_trainee_peasant", "$g_train_peasants_against_bandits_num_peasants"),
         (set_jump_entry, 11),
         (jump_to_scene, ":village_scene"),
         (jump_to_menu, "mnu_train_peasants_against_bandits_training_result"),
         (music_set_situation, 0),
         (change_screen_mission),
         ]),
      ]
    ),

  (
    "train_peasants_against_bandits_training_result",mnf_disable_all_keys,
    "{s0}",
    "none",
    [
      (assign, reg5, "$g_train_peasants_against_bandits_num_peasants"),
      (str_store_troop_name_by_count, s0, "trp_trainee_peasant", "$g_train_peasants_against_bandits_num_peasants"),
      (try_begin),
        (eq, "$g_train_peasants_against_bandits_training_succeeded", 0),
        (str_store_string, s0, "@You were beaten. The peasants are heartened by their success, but the lesson you wanted to teach them probably didn't get through..."),
      (else_try),
        (str_store_string, s0, "@After beating your last opponent, you explain to the peasants how to better defend themselves against such an attack. Hopefully they'll take the experience on board and will be prepared next time."),
        (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
        (val_add, ":quest_current_state", "$g_train_peasants_against_bandits_num_peasants"),
        (quest_set_slot, "qst_train_peasants_against_bandits", slot_quest_current_state, ":quest_current_state"),
      (try_end),
     ],
    [
      ("continue", [], "Continue...",
       [
         (try_begin),
           (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
           (quest_slot_eq, "qst_train_peasants_against_bandits", slot_quest_target_amount, ":quest_current_state"),
           (jump_to_menu, "mnu_train_peasants_against_bandits_attack"),
         (else_try),
           (change_screen_map),
         (try_end),
         ]),
      ]
    ),

  (
    "train_peasants_against_bandits_attack",0,
    "As you get ready to continue the training, a sentry from the village runs up to you, shouting alarums.\
 The bandits have been spotted on the horizon, riding hard for {s3}.\
 The elder begs that you organize your newly-trained militia and face them.",
    "none",
    [
    (str_store_party_name, s3, "$current_town"),
     ],
    [
      ("peasants_against_bandits_attack_resist", [], "Prepare for a fight!",
       [ ## SB : use new bandit script
        # (store_random_in_range, ":random_no", 0, 3),
        # (try_begin),
          # (eq, ":random_no", 0),
          # (assign, ":bandit_troop", "trp_bandit"),
        # (else_try),
          # (eq, ":random_no", 1),
          # (assign, ":bandit_troop", "trp_mountain_bandit"),
        # (else_try),
          # (assign, ":bandit_troop", "trp_forest_bandit"),
        # (try_end),
        (call_script, "script_center_get_bandits", "$current_town", 0),
        (assign, ":bandit_troop", reg0),
        (party_get_slot, ":scene_to_use", "$g_encountered_party", slot_castle_exterior),
        (modify_visitors_at_site, ":scene_to_use"),
        (reset_visitors),
        (store_character_level, ":level", "trp_player"),
        (val_div, ":level", 2),
        (store_add, ":min_bandits", ":level", 16),
        (store_add, ":max_bandits", ":min_bandits", 6),
        (store_random_in_range, ":random_no", ":min_bandits", ":max_bandits"),
        (set_visitors, 0, ":bandit_troop", ":random_no"),
        # (assign, ":num_villagers", ":max_bandits"),
        #SB : more accurate count
        (party_count_members_of_type, ":num_villagers", "$current_town", "trp_farmer"), #disallow peasant woman
        (val_min, ":num_villagers", ":max_bandits"), #dckplmc
        (set_visitors, 2, "trp_trainee_peasant", ":num_villagers"),
        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission,"mt_village_attack_bandits"),
        (jump_to_scene, ":scene_to_use"),
        (assign, "$g_next_menu", "mnu_train_peasants_against_bandits_attack_result"),
        (jump_to_menu, "mnu_battle_debrief"),
        (assign, "$g_mt_mode", vba_after_training),
        (change_screen_mission),
        ]),
      ]
    ),

  (
    "train_peasants_against_bandits_attack_result",mnf_scale_picture|mnf_disable_all_keys,
    "{s9}",
    "none",
    [
      (try_begin),
        (eq, "$g_battle_result", 1),
        (str_store_string, s9, "@The bandits are broken!\
 Those few who remain alive and conscious run off with their tails between their legs,\
 terrified of the peasants and their new champion."),
        (call_script, "script_succeed_quest", "qst_train_peasants_against_bandits"),
        (jump_to_menu, "mnu_train_peasants_against_bandits_success"),
      (else_try),
        (call_script, "script_fail_quest", "qst_train_peasants_against_bandits"),
        (str_store_string, s9, "@Try as you might, you could not defeat the bandits.\
 Infuriated, they raze the village to the ground to punish the peasants,\
 and then leave the burning wasteland behind to find greener pastures to plunder."),
        (set_background_mesh, "mesh_pic_looted_village"),
      (try_end),
     ],
    [
      ("continue", [], "Continue...",
       [(try_begin),
          (call_script, "script_village_set_state",  "$current_town", svs_looted),
          (party_set_slot, "$current_town", slot_village_raid_progress, 0),
          (party_set_slot, "$current_town", slot_village_recover_progress, 0),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
          (call_script, "script_end_quest", "qst_train_peasants_against_bandits"),
        (try_end),
        (change_screen_map),
    ]),
      ]
    ),

   (
    "train_peasants_against_bandits_success",mnf_disable_all_keys,
    "The bandits are broken!\
 Those few who remain run off with their tails between their legs,\
 terrified of the peasants and their new champion.\
 The villagers have little left in the way of wealth after their ordeal,\
 but they offer you all they can find to show their gratitude.",
    "none",
    [(party_clear, "p_temp_party"),
     #SB : probably apply casualties before adding new troops?
     (quest_get_slot, ":amount_trained", "qst_train_peasants_against_bandits", slot_quest_target_amount),
     (store_faction_of_party, ":village_faction", "$current_town"), #assuming player trains them with local weapons
     (faction_get_slot, ":recruit_troop", ":village_faction", slot_faction_tier_1_troop),
     (party_add_members, "$current_town", ":recruit_troop", ":amount_trained"),
     (party_remove_members, "$current_town", "trp_farmer", ":amount_trained"),

     (call_script, "script_end_quest", "qst_train_peasants_against_bandits"),
     (call_script, "script_change_player_relation_with_center", "$current_town", 4),

     (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
     (try_for_range, ":slot_no", num_equipment_kinds ,max_inventory_items + num_equipment_kinds),
        (store_random_in_range, ":rand", 0, 100),
        (lt, ":rand", 50),
        (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
     (try_end),
     (call_script, "script_add_log_entry", logent_helped_peasants, "trp_player",  "$current_town", -1, -1),
     #(set_background_mesh, "mesh_pic_mb_warrior_3"), #SB : background mesh
    ],
    [
      ("village_bandits_defeated_accept",[],"Take it as your just due.",[(jump_to_menu, "mnu_auto_return_to_map"),
                                                                         (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
                                                                         (troop_sort_inventory, ":merchant_troop"),
                                                                         (change_screen_loot, ":merchant_troop"),
                                                                       ]),
      ("village_bandits_defeated_cont",[],  "Refuse, stating that they need these items more than you do.",[
      (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
      (call_script, "script_change_player_honor", 1),
      (change_screen_map)]),
    ],
  ),


  (
    "disembark",0,
    "Do you wish to disembark?",
    "none",
    [],
    [
      ("disembark_yes", [], "Yes.",
       [(assign, "$g_player_icon_state", pis_normal),
        (party_set_flags, "p_main_party", pf_is_ship, 0),
        (party_get_position, pos1, "p_main_party"),
        (party_set_position, "p_main_party", pos0),
        (try_begin),
          (le, "$g_main_ship_party", 0),
          (set_spawn_radius, 0),
          (spawn_around_party, "p_main_party", "pt_none"),
          (assign, "$g_main_ship_party", reg0),
          (party_set_flags, "$g_main_ship_party", pf_is_static|pf_always_visible|pf_hide_defenders|pf_is_ship, 1),
          (str_store_troop_name, s1, "trp_player"),
          (party_set_name, "$g_main_ship_party", "@{s1}'s Ship"),
          (party_set_icon, "$g_main_ship_party", "icon_ship"),
          (party_set_slot, "$g_main_ship_party", slot_party_type, spt_ship),
        (try_end),
        (enable_party, "$g_main_ship_party"),
        (party_set_position, "$g_main_ship_party", pos0),
        (party_set_icon, "$g_main_ship_party", "icon_ship_on_land"),
        (assign, "$g_main_ship_party", -1),
        (change_screen_return),
        ]),
      ("disembark_no", [], "No.",
       [(change_screen_return),
        ]),
    ]
  ),

  (
    "ship_reembark",0,
    "Do you wish to embark?",
    "none",
    [],
    [
      ("reembark_yes", [], "Yes.",
       [(assign, "$g_player_icon_state", pis_ship),
        (party_set_flags, "p_main_party", pf_is_ship, 1),
        (party_get_position, pos1, "p_main_party"),
        (map_get_water_position_around_position, pos2, pos1, 6),
        (party_set_position, "p_main_party", pos2),
        (assign, "$g_main_ship_party", "$g_encountered_party"),
        (disable_party, "$g_encountered_party"),
        (change_screen_return),
        ]),
      ("reembark_no", [], "No.",
       [(change_screen_return),
        ]),
    ]
  ),

  (
    "center_reports",0,
    "Town Name: {s1}^Rent Income: {reg1} denars^Tariff Income: {reg2} denars^Food Stock: for {reg3} days",
    "none",
    [(party_get_slot, ":town_food_store", "$g_encountered_party", slot_party_food_store),
     (call_script, "script_center_get_food_consumption", "$g_encountered_party"),
     (assign, ":food_consumption", reg0),
     (try_begin),
       (gt, ":food_consumption", 0),
       (store_div, reg3, ":town_food_store", ":food_consumption"),
     (else_try),
       (assign, reg3, 9999),
     (try_end),
     (str_store_party_name, s1, "$g_encountered_party"),
     (party_get_slot, reg1, "$g_encountered_party", slot_center_accumulated_rents),
     (party_get_slot, reg2, "$g_encountered_party", slot_center_accumulated_tariffs),
     ],
    [
      ("to_price_and_productions", [], "Show prices and productions.",
       [(jump_to_menu, "mnu_price_and_production"),
        ]),

      ("go_back_dot",[],"Go back.",
       [(try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
          (jump_to_menu, "mnu_village"),
        (else_try),
          (jump_to_menu, "mnu_town"),
        (try_end),
        ]),
    ]
  ),

  (
    "price_and_production",0,
    "Productions are:^(Note: base/modified by raw materials/modified by materials plus prosperity)^{s1}^^Price factors are:^{s2}",
    "none",
    [

	 (assign, ":calradian_average_urban_hardship", 0),
	 (assign, ":calradian_average_rural_hardship", 0),

	 (try_for_range, ":center", towns_begin, towns_end),
		(call_script, "script_center_get_goods_availability", ":center"),
		(val_add, ":calradian_average_urban_hardship", reg0),
	 (try_end),

	 (try_for_range, ":center", villages_begin, villages_end),
		(call_script, "script_center_get_goods_availability", ":center"),
		(val_add, ":calradian_average_rural_hardship", reg0),
	 (try_end),

	 (val_div, ":calradian_average_rural_hardship", 110),
	 (val_div, ":calradian_average_urban_hardship", 22),



	 (call_script, "script_center_get_goods_availability", "$g_encountered_party"),

	 (assign, reg1, ":calradian_average_urban_hardship"),
	 (assign, reg2, ":calradian_average_rural_hardship"),

	 (try_begin),
		(ge, "$cheat_mode", 1),
		(str_store_string, s1, "str___hardship_index_reg0_avg_towns_reg1_avg_villages_reg2__"),
		(display_message, "@{!}DEBUG - {s1}"),
	 (try_end),


     (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
	   (neq, ":cur_good", "itm_pork"), #tied to price of grain
	   (neq, ":cur_good", "itm_chicken"), #tied to price of grain
	   (neq, ":cur_good", "itm_butter"), #tied to price of cheese
	   (neq, ":cur_good", "itm_cattle_meat"),
	   (neq, ":cur_good", "itm_cabbages"), #possibly include later

	   (call_script, "script_center_get_production", "$g_encountered_party", ":cur_good"),
	   (assign, ":production", reg0),
	   (assign, ":base_production", reg2),
	   (assign, ":base_production_modded_by_raw_materials", reg1),

	   (call_script, "script_center_get_consumption", "$g_encountered_party", ":cur_good"),
	   (assign, ":consumer_consumption", reg2),
	   (assign, ":raw_material_consumption", reg1),
	   (assign, ":consumption", reg0),

       (store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
       (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
       (party_get_slot, ":price", "$g_encountered_party", ":cur_good_price_slot"),

	   (assign, ":total_centers", 0),
	   (assign, ":calradian_average_price", 0),
	   (assign, ":calradian_average_production", 0),
	   (assign, ":calradian_average_consumption", 0),

	   (try_for_range, ":center", centers_begin, centers_end),
		(neg|is_between, ":center", castles_begin, castles_end),
	    (val_add, ":total_centers", 1),
        (call_script, "script_center_get_production", ":center", ":cur_good"),
		(assign, ":center_production", reg2),
        (call_script, "script_center_get_consumption", ":center", ":cur_good"),
		(store_add, ":center_consumption", reg1, reg2),

        (party_get_slot, ":center_price", ":center", ":cur_good_price_slot"),
	    (val_add, ":calradian_average_price", ":center_price"),
	    (val_add, ":calradian_average_production", ":center_production"),
	    (val_add, ":calradian_average_consumption", ":center_consumption"),
	   (try_end),

	   (assign, ":calradian_total_production", ":calradian_average_production"),
	   (assign, ":calradian_total_consumption", ":calradian_average_consumption"),

	   (val_div, ":calradian_average_price", ":total_centers"),
	   (val_div, ":calradian_average_production", ":total_centers"),
	   (val_div, ":calradian_average_consumption", ":total_centers"),


       (str_store_item_name, s3, ":cur_good"),

       (assign, reg1, ":base_production"),
       (assign, reg2, ":base_production_modded_by_raw_materials"),
       (assign, reg3, ":production"),
       (assign, reg4, ":price"),

	   (assign, reg5, ":calradian_average_production"),
	   (assign, reg6, ":calradian_average_price"),

	   (assign, reg7, ":consumer_consumption"),
	   (assign, reg8, ":raw_material_consumption"),
	   (assign, reg9, ":consumption"),

	   (assign, reg10, ":calradian_average_consumption"),

	   (item_get_slot, ":production_slot", ":cur_good", slot_item_production_slot),
	   (party_get_slot, ":production_number", "$g_encountered_party", ":production_slot"),
	   (assign, reg11, ":production_number"),
	   (assign, reg12, ":calradian_total_production"),
	   (assign, reg13, ":calradian_total_consumption"),

	   (item_get_slot, ":production_string", ":cur_good", slot_item_production_string),
	   (str_store_string, s4, ":production_string"),

       (str_store_string, s1, "str___s3_price_=_reg4_calradian_average_reg6_capital_reg11_s4_base_reg1modified_by_raw_material_reg2modified_by_prosperity_reg3_calradian_average_production_base_reg5_total_reg12_consumed_reg7used_as_raw_material_reg8modified_total_reg9_calradian_consumption_base_reg10_total_reg13s1_"),
     (try_end),


     ],
    [
      ("go_back_dot",[],"Go back.",
       [(try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
          (jump_to_menu, "mnu_village"),
        (else_try),
          (jump_to_menu, "mnu_town"),
        (try_end),
        ]),
    ]
  ),

  (
    "town_trade",0,
    "You head towards the marketplace.",
    "none",
    [],
    [
      #SB : re-order dialog options for consistency, add talk instead of trade option
		##diplomacy start+
		#Begin auto-sell, credit rubik (Custom Commander)
      ## CC
      ("auto_sell",[],
       "Sell items automatically.",
       [
          (assign, "$g_next_menu", "mnu_town"),
          (jump_to_menu,"mnu_dplmc_trade_auto_sell_begin"),
        ]),

      ("auto_buy_food",[],
       "Buy food automatically.",
       [
          (assign, "$g_next_menu", "mnu_town"),
          (jump_to_menu,"mnu_dplmc_trade_auto_buy_food_begin"),
        ]),

      ## CC
		#End auto-sell, credit rubik (Custom Commander)
		##diplomacy start+
      ("assess_prices",
       [
         (store_faction_of_party, ":current_town_faction", "$current_town"),
         (store_relation, ":reln", ":current_town_faction", "fac_player_supporters_faction"),
         (ge, ":reln", 0),
         ],
       "Assess the local prices.",
       [
           (jump_to_menu,"mnu_town_trade_assessment_begin"),
        ]),
        
      ("trade_with_arms_merchant",[(party_slot_ge, "$current_town", slot_town_weaponsmith, 1)],
       "Trade with the arms merchant.",
       [
            (party_get_slot, ":merchant_troop", "$current_town", slot_town_weaponsmith),
            (assign, "$g_talk_troop", ":merchant_troop"),
            (try_begin),
              (this_or_next|key_is_down, key_left_shift),
              (key_is_down, key_right_shift),
              (call_script, "script_start_town_conversation", slot_town_weaponsmith, 10),
            (else_try),
              (troop_set_slot, ":merchant_troop", slot_troop_met, 1),
              (change_screen_trade, ":merchant_troop"),
            (try_end),
        ]),
      ("trade_with_armor_merchant",[(party_slot_ge, "$current_town", slot_town_armorer, 1)],
       "Trade with the armor merchant.",
       [
            (party_get_slot, ":merchant_troop", "$current_town", slot_town_armorer),
            (assign, "$g_talk_troop", ":merchant_troop"),
            (try_begin),
              (this_or_next|key_is_down, key_left_shift),
              (key_is_down, key_right_shift),
              (call_script, "script_start_town_conversation", slot_town_armorer, 9),
            (else_try),
              (troop_set_slot, ":merchant_troop", slot_troop_met, 1),
              (change_screen_trade, ":merchant_troop"),
            (try_end),
        ]),
      ("trade_with_horse_merchant",[(party_slot_ge, "$current_town", slot_town_horse_merchant, 1)],
       "Trade with the horse merchant.",
       [
            (party_get_slot, ":merchant_troop", "$current_town", slot_town_horse_merchant),
            (try_begin),
              (this_or_next|key_is_down, key_left_shift),
              (key_is_down, key_right_shift),
              (call_script, "script_start_town_conversation", slot_town_horse_merchant, 12),
            (else_try),
              (troop_set_slot, ":merchant_troop", slot_troop_met, 1),
              (change_screen_trade, ":merchant_troop"),
            (try_end),
        ]),
      ("trade_with_goods_merchant",[(party_slot_ge, "$current_town", slot_town_merchant, 1)],
       "Trade with the goods merchant.",
       [
            (party_get_slot, ":merchant_troop", "$current_town", slot_town_merchant),
            (assign, "$g_talk_troop", ":merchant_troop"),
            (try_begin),
              (this_or_next|key_is_down, key_left_shift),
              (key_is_down, key_right_shift),
              (call_script, "script_start_town_conversation", slot_town_merchant, 9),
            (else_try),
              (troop_set_slot, ":merchant_troop", slot_troop_met, 1),
              (change_screen_trade, ":merchant_troop"),
            (try_end),
        ]),

      ("back_to_town_menu",[],"Head back.",
       [
           (jump_to_menu,"mnu_town"),
        ]),
    ]
  ),

##diplomacy start+
##Begin auto-sell credit rubik (Custom Commander)
##Altered to only sell items from the player's inventory, not his companions'.
#
#Uses global variable $g_auto_sell_price_limit changed to $g_dplmc_auto_sell_price_limit
## CC
  (
    "dplmc_trade_auto_sell_begin",0,
    "Items in your inventory whose type is marked as sellable and whose prices \
are below {reg1} denars will be sold to the {reg2?appropriate merchants:elder} \
in the current {reg2?town:village} automatically.  Specifically food, trade \
goods, and books will never be sold. ^^You can change some settings here freely.",
    "none",
  [
	##dplmc+ added section begin
    (this_or_next|is_between, "$current_town", towns_begin, towns_end),
	    (is_between, "$current_town", villages_begin, villages_end),
	(call_script, "script_dplmc_initialize_autoloot", 0),#argument "0" means this does nothing if deemed unnecessary
	##dplmc+ added section end
    (assign, reg1, "$g_dplmc_auto_sell_price_limit"),
	 (assign, reg2, 0),
    (try_begin),
      (is_between, "$current_town", towns_begin, towns_end),
      (assign, reg2, 1),
    (try_end),
  ],
  [
    ("continue",[],"Continue...",
    [
      #(call_script, "script_auto_sell_all"),
	  (call_script, "script_dplmc_player_auto_sell_at_center", "$current_town"),
      (jump_to_menu, "$g_next_menu"),
      ]),
    ("change_settings",[],"Change settings.",[(start_presentation, "prsnt_dplmc_auto_sell_options"),]),
    ("go_back",[],"Go back",[(jump_to_menu, "$g_next_menu")]),
  ]
  ),

  (
    "dplmc_trade_auto_buy_food_begin",0,
    "You will automatically buy food according to your shopping list. Do you want to continue?^^You can view and configure the shopping list here.",
    "none", [],
  [
    ("continue",[
	  #dplmc+ added to check against weird conditions
 	  (assign, ":merchant_troop", -1),
	  (try_begin),
		  (is_between, "$current_town", towns_begin, towns_end),
        (party_get_slot, ":merchant_troop", "$current_town", slot_town_merchant),
     (else_try),
		  (is_between, "$current_town", villages_begin, villages_end),
        (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
     (try_end),
	  (ge, ":merchant_troop", 1),
	  #dplmc+ end addition
	 ],"Continue...",
    [
 	   (assign, ":merchant_troop", -1),
	   (try_begin),
		  (is_between, "$current_town", towns_begin, towns_end),
        (party_get_slot, ":merchant_troop", "$current_town", slot_town_merchant),
      (else_try),
		  (is_between, "$current_town", villages_begin, villages_end),
        (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
      (try_end),
	   (call_script, "script_dplmc_auto_buy_food", "trp_player", ":merchant_troop"),
      (jump_to_menu, "$g_next_menu"),
      ]),

    ("dplmc_change_shopping_list_of_food",[],"Configure your shopping list.",[(start_presentation, "prsnt_dplmc_shopping_list_of_food"),]),
    ("go_back",[],"Go back",[(jump_to_menu, "$g_next_menu")]),
   ]
  ),
## CC
##End auto-sell credit rubik (Custom Commander)
##diplomacy start+

  (
   "town_trade_assessment_begin",0,
   #"You overhear the following details about the roads out of town :^(experimental feature -- this may go into dialogs)^{s42}^You also overhear several discussions about the price of trade goods across the local area.^You listen closely, trying to work out the best deals around.",
   "You overhear several discussions about the price of trade goods across the local area.^You listen closely, trying to work out the best deals around.",
    "none",
    [
	(str_clear, s42),
##	(call_script, "script_merchant_road_info_to_s42", "$g_encountered_party"),

    ],

    [
      ("continue",[],"Continue...",
       [
           (assign,"$auto_enter_town", "$current_town"),
           (assign, "$g_town_assess_trade_goods_after_rest", "$current_town"), #SB : save this
           (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
           (val_div, reg0, 2),
           (store_sub, ":num_hours", 6, reg0),
           (assign, "$g_last_rest_center", "$current_town"),
           (assign, "$g_last_rest_payment_until", -1),
           (rest_for_hours, ":num_hours", 5, 0), #rest while not attackable
           (change_screen_return),
        ]),
      ("go_back_dot",[],"Go back.",
       [
           (jump_to_menu,"mnu_town_trade"),
        ]),
    ]
  ),

  (
    "town_trade_assessment",mnf_disable_all_keys,
    "As the party member with the highest trade skill ({reg2}), {reg3?you try to figure out:{s1} tries to figure out} the best goods to trade in. {s2}",
    "none",
    [

     (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),

     (assign, ":num_best_results", 0),
     (assign, ":best_result_1_item", -1),
     (assign, ":best_result_1_town", -1),
     (assign, ":best_result_1_profit", 0),
     (assign, ":best_result_2_item", -1),
     (assign, ":best_result_2_town", -1),
     (assign, ":best_result_2_profit", 0),
     (assign, ":best_result_3_item", -1),
     (assign, ":best_result_3_town", -1),
     (assign, ":best_result_3_profit", 0),
     (assign, ":best_result_4_item", -1),
     (assign, ":best_result_4_town", -1),
     (assign, ":best_result_4_profit", 0),
     (assign, ":best_result_5_item", -1),
     (assign, ":best_result_5_town", -1),
     (assign, ":best_result_5_profit", 0),

     (store_sub, ":num_towns", walled_centers_end, walled_centers_begin),
     (store_sub, ":num_goods", trade_goods_end, trade_goods_begin),
     (store_mul, ":max_iteration", ":num_towns", ":num_goods"),
     (val_mul, ":max_iteration", ":max_skill"),
     (val_div, ":max_iteration", 20),

     (assign, ":org_encountered_party", "$g_encountered_party"),

     (try_for_range, ":unused", 0, ":max_iteration"),
       (store_random_in_range, ":random_trade_good", trade_goods_begin, trade_goods_end),
       (store_random_in_range, ":random_town", towns_begin, towns_end),

       (party_get_slot, ":cur_merchant", ":org_encountered_party", slot_town_merchant),
	   (assign, ":num_items_in_town_inventory", 0),
       (try_for_range, ":i_slot", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
         (troop_get_inventory_slot, ":slot_item", ":cur_merchant", ":i_slot"),
         (try_begin),
           (eq, ":slot_item", ":random_trade_good"),
		   (val_add, ":num_items_in_town_inventory", 1),
         (try_end),
       (try_end),

       (ge, ":num_items_in_town_inventory", 1),

       (assign, ":already_best", 0),

       (try_begin),
         (eq, ":random_trade_good", ":best_result_1_item"),
         (eq, ":random_town", ":best_result_1_town"),
         (val_add, ":already_best", 1),
       (try_end),

	   (try_begin),
         (eq, ":random_trade_good", ":best_result_2_item"),
         (eq, ":random_town", ":best_result_2_town"),
         (val_add, ":already_best", 1),
       (try_end),

	   (try_begin),
         (eq, ":random_trade_good", ":best_result_3_item"),
         (eq, ":random_town", ":best_result_3_town"),
         (val_add, ":already_best", 1),
       (try_end),

	   (try_begin),
         (eq, ":random_trade_good", ":best_result_4_item"),
         (eq, ":random_town", ":best_result_4_town"),
         (val_add, ":already_best", 1),
       (try_end),

	   (try_begin),
         (eq, ":random_trade_good", ":best_result_5_item"),
         (eq, ":random_town", ":best_result_5_town"),
         (val_add, ":already_best", 1),
       (try_end),

       (le, ":already_best", 1),

       (store_item_value, ":random_trade_good_price", ":random_trade_good"),
       (assign, "$g_encountered_party", ":org_encountered_party"),
       (call_script, "script_game_get_item_buy_price_factor", ":random_trade_good"),
       (store_mul, ":random_trade_good_buy_price", ":random_trade_good_price", reg0),
       (val_div, ":random_trade_good_buy_price", 100),
       (val_max, ":random_trade_good_buy_price", 1),
       (assign, "$g_encountered_party", ":random_town"),
       (call_script, "script_game_get_item_sell_price_factor", ":random_trade_good"),
       (store_mul, ":random_trade_good_sell_price", ":random_trade_good_price", reg0),
       (val_div, ":random_trade_good_sell_price", 100),
       (val_max, ":random_trade_good_sell_price", 1),
       (store_sub, ":difference", ":random_trade_good_sell_price", ":random_trade_good_buy_price"),

       (try_begin),
	     (this_or_next|eq, ":best_result_1_item", ":random_trade_good"),
		 (this_or_next|eq, ":best_result_2_item", ":random_trade_good"),
		 (this_or_next|eq, ":best_result_3_item", ":random_trade_good"),
		 (this_or_next|eq, ":best_result_4_item", ":random_trade_good"),
		 (eq, ":best_result_5_item", ":random_trade_good"),

         (try_begin),
		   (eq, ":best_result_1_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_1_profit"),
           (assign, ":best_result_1_item", ":random_trade_good"),
           (assign, ":best_result_1_town", ":random_town"),
           (assign, ":best_result_1_profit", ":difference"),
         (else_try),
		   (eq, ":best_result_2_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_2_profit"),
           (assign, ":best_result_2_item", ":random_trade_good"),
           (assign, ":best_result_2_town", ":random_town"),
           (assign, ":best_result_2_profit", ":difference"),
		 (else_try),
		   (eq, ":best_result_3_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_3_profit"),
           (assign, ":best_result_3_item", ":random_trade_good"),
           (assign, ":best_result_3_town", ":random_town"),
           (assign, ":best_result_3_profit", ":difference"),
		 (else_try),
		   (eq, ":best_result_4_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":random_trade_good"),
           (assign, ":best_result_4_town", ":random_town"),
           (assign, ":best_result_4_profit", ":difference"),
		 (else_try),
		   (eq, ":best_result_5_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_5_profit"),
           (assign, ":best_result_5_item", ":random_trade_good"),
           (assign, ":best_result_5_town", ":random_town"),
           (assign, ":best_result_5_profit", ":difference"),
		 (try_end),
	   (else_try),
       (try_begin),
         (gt, ":difference", ":best_result_1_profit"),
         (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":best_result_3_item"),
           (assign, ":best_result_4_town", ":best_result_3_town"),
           (assign, ":best_result_4_profit", ":best_result_3_profit"),
         (assign, ":best_result_3_item", ":best_result_2_item"),
         (assign, ":best_result_3_town", ":best_result_2_town"),
         (assign, ":best_result_3_profit", ":best_result_2_profit"),
         (assign, ":best_result_2_item", ":best_result_1_item"),
         (assign, ":best_result_2_town", ":best_result_1_town"),
         (assign, ":best_result_2_profit", ":best_result_1_profit"),
         (assign, ":best_result_1_item", ":random_trade_good"),
         (assign, ":best_result_1_town", ":random_town"),
         (assign, ":best_result_1_profit", ":difference"),
       (else_try),
         (gt, ":difference", ":best_result_2_profit"),
         (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":best_result_3_item"),
           (assign, ":best_result_4_town", ":best_result_3_town"),
           (assign, ":best_result_4_profit", ":best_result_3_profit"),
         (assign, ":best_result_3_item", ":best_result_2_item"),
         (assign, ":best_result_3_town", ":best_result_2_town"),
         (assign, ":best_result_3_profit", ":best_result_2_profit"),
         (assign, ":best_result_2_item", ":random_trade_good"),
         (assign, ":best_result_2_town", ":random_town"),
         (assign, ":best_result_2_profit", ":difference"),
       (else_try),
         (gt, ":difference", ":best_result_3_profit"),
         (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":best_result_3_item"),
           (assign, ":best_result_4_town", ":best_result_3_town"),
           (assign, ":best_result_4_profit", ":best_result_3_profit"),
         (assign, ":best_result_3_item", ":random_trade_good"),
         (assign, ":best_result_3_town", ":random_town"),
         (assign, ":best_result_3_profit", ":difference"),
         (else_try),
           (gt, ":difference", ":best_result_4_profit"),
           (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":random_trade_good"),
           (assign, ":best_result_4_town", ":random_town"),
           (assign, ":best_result_4_profit", ":difference"),
         (else_try),
           (gt, ":difference", ":best_result_5_profit"),
           (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
         (try_end),
       (try_end),
     (try_end),

     (assign, "$g_encountered_party", ":org_encountered_party"),

     (str_clear, s3),

     (assign, reg2, ":max_skill"),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s1, ":max_skill_owner"),
     (try_end),
     (try_begin),
       (le, ":num_best_results", 0),
       (str_store_string, s2, "@However, {reg3?You are:{s1} is} unable to find any trade goods that would bring a profit."),
     (else_try),
        #SB : add lesser renown bonus
        (try_begin),
          (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
          (neq, reg1, "trp_player"),
          (call_script, "script_change_troop_renown", reg1, dplmc_companion_skill_renown / 2),
        (try_end),
       (try_begin),
         (ge, ":best_result_5_item", 0),
         (assign, reg6, ":best_result_5_profit"),
         (str_store_item_name, s4, ":best_result_5_item"),
         (str_store_party_name, s5, ":best_result_5_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_4_item", 0),
         (assign, reg6, ":best_result_4_profit"),
         (str_store_item_name, s4, ":best_result_4_item"),
         (str_store_party_name, s5, ":best_result_4_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_3_item", 0),
         (assign, reg6, ":best_result_3_profit"),
         (str_store_item_name, s4, ":best_result_3_item"),
         (str_store_party_name, s5, ":best_result_3_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_2_item", 0),
         (assign, reg6, ":best_result_2_profit"),
         (str_store_item_name, s4, ":best_result_2_item"),
         (str_store_party_name, s5, ":best_result_2_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_1_item", 0),
         (assign, reg6, ":best_result_1_profit"),
         (str_store_item_name, s4, ":best_result_1_item"),
         (str_store_party_name, s5, ":best_result_1_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (str_store_string, s2, "@{reg3?You find:{s1} finds} out the following:^{s3}"),
     (try_end),
     ],
    [
      ("continue",[],"Continue...",
       [
           (jump_to_menu,"mnu_town_trade"),
        ]),
    ]
  ),




  #SB : flavour text
  (
    "sneak_into_town_suceeded",0,
    "Disguised in the garments of a poor {reg1?cheater:{s1}}, you fool the guards and make your way into the town.",
    "none",
    [(assign, reg1, "$cheat_mode"),
     (call_script, "script_get_disguise_string", "$sneaked_into_town", 1),
     
     # (try_begin),
       # (eq, "$sneaked_into_town", disguise_pilgrim),
       # (assign, ":string", "str_pilgrim_disguise"),
     # (try_end),
    ],
    [
      ("continue",[],"Continue...",
       [
           # (assign, "$sneaked_into_town",1),
           (jump_to_menu,"mnu_town"),
        ]),
    ]
  ),
  (
    "sneak_into_town_caught",0,
    "As you try to sneak in, one of the guards recognizes you and raises the alarm!\
 You must flee back through the gates before all the guards in the town come down on you!",
    "none",
    [
       (assign,"$auto_menu","mnu_captivity_start_castle_surrender"),
    ],
    [
      ("sneak_caught_fight",[],"Try to fight your way out!",
       [
           (assign,"$all_doors_locked",1),
           (party_get_slot, ":sneak_scene", "$current_town", slot_town_center), # slot_town_gate),
           (modify_visitors_at_site,":sneak_scene"),
           (reset_visitors),

           (set_jump_mission, "mt_sneak_caught_fight"),
           
           (try_begin),
             (this_or_next|eq, "$talk_context", tc_escape),
             (eq, "$talk_context", tc_prison_break),
             (assign, ":entry_no", 7),
           (else_try),
             (party_slot_eq, "$current_town", slot_party_type, spt_town),
             #(set_visitor,0,"trp_player"),
             (assign, ":entry_no", 0),
           (else_try),
             #(set_visitor,1,"trp_player"),
             (assign, ":entry_no", 1),
           (try_end),
           
           (try_begin),
             (gt, "$sneaked_into_town", disguise_none), #setup disguise
             (assign, ":override_state", af_override_everything),
             (mission_tpl_entry_set_override_flags, "mt_sneak_caught_fight", ":entry_no", ":override_state"),
                        #SB : script call to assign correct disguise, with weapons
             (call_script, "script_set_disguise_override_items", "mt_sneak_caught_fight", ":entry_no", 1),
           (try_end),
           
           (set_jump_entry, ":entry_no"),
           
           #(store_faction_of_party, ":town_faction","$current_town"),
           #(faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_2_troop),
           #(faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
           #(try_begin),
           #  (gt, ":tier_2_troop", 0),
           #  (gt, ":tier_3_troop", 0),
           #  (assign,reg0,":tier_3_troop"),
           #  (assign,reg1,":tier_3_troop"),
           #  (assign,reg2,":tier_2_troop"),
           #  (assign,reg3,":tier_2_troop"),
           #(else_try),
           #  (assign,reg0,"trp_swadian_skirmisher"),
           #  (assign,reg1,"trp_swadian_crossbowman"),
           #  (assign,reg2,"trp_swadian_infantry"),
           #  (assign,reg3,"trp_swadian_crossbowman"),
           #(try_end),
           #(assign,reg4,-1),
           #(shuffle_range,0,5),
           #(set_visitor,2,reg0),
           #(set_visitor,3,reg1),
           #(set_visitor,4,reg2),
           #(set_visitor,5,reg3),
           

           #(set_jump_mission, "mt_sneak_caught_fight"),
           (set_passage_menu, "mnu_town"),
           (jump_to_scene,":sneak_scene"),
           (change_screen_mission),
        ]),
      ("sneak_caught_surrender",[],"Surrender.",
       [
           (jump_to_menu,"mnu_captivity_start_castle_surrender"),
        ]),
    ]
  ),
  (
    "sneak_into_town_caught_dispersed_guards",0,
    "You drive off the guards and cover your trail before running off, easily losing your pursuers in the maze of streets.",
    "none",
    [],
    [
      ("continue",[],"Continue...",
       [
           (try_begin),
               (eq, "$sneaked_into_town", 0),
               (assign, "$sneaked_into_town",1),
           (try_end),

           (assign, "$town_entered", 1),
           #(assign, "$g_mt_mode", tcm_disguised),
           (jump_to_menu,"mnu_town"),
        ]),
    ]
  ),

  (
    "sneak_into_town_caught_ran_away",0,
    "You make your way back through the gates and quickly retreat to the safety of the countryside.{s11}",
    "none",
    [

	(str_clear, s11),
	(assign, ":at_least_one_escaper_caught", 0),

	(assign, ":end_cond", kingdom_ladies_end),
	(try_for_range, ":prisoner", active_npcs_begin, ":end_cond"),
	  (try_begin),
        (troop_slot_eq, ":prisoner", slot_troop_mission_participation, mp_prison_break_escaped),
        (assign, "$talk_context", tc_hero_freed),
        (assign, reg14, ":prisoner"),
        (call_script, "script_setup_troop_meeting", ":prisoner", -1),
        (troop_set_slot, ":prisoner", slot_troop_mission_participation, -1),

        (troop_get_slot, ":prison_center", ":prisoner", slot_troop_prisoner_of_party),
        (party_remove_prisoners, ":prison_center", ":prisoner", 1),
        (troop_set_slot, ":prisoner", slot_troop_prisoner_of_party, -1),

        (assign, ":end_cond", -1), #maybe more than 1 should be able to escape?
	  (else_try),
		(troop_slot_eq, ":prisoner", slot_troop_mission_participation, mp_prison_break_caught),
		(str_store_troop_name, s12, ":prisoner"),
		(try_begin),
			(eq, ":at_least_one_escaper_caught", 0),
			(str_store_string, s11, "str_s11_unfortunately_s12_was_wounded_and_had_to_be_left_behind"),
		(else_try),
			(str_store_string, s11, "str_s11_also_s12_was_wounded_and_had_to_be_left_behind"),
		(try_end),
		(assign, ":at_least_one_escaper_caught", 1),
	  (try_end),

	  (troop_set_slot, ":prisoner", slot_troop_mission_participation, 0), #new
	(try_end),
	],
    [
      ("continue",[],"Continue...",
       [
           (assign,"$auto_menu",-1),
           (store_encountered_party,"$last_sneak_attempt_town"),
           (store_current_hours,"$last_sneak_attempt_time"),
           (change_screen_return),
        ]),
    ]
  ),


  (
    "enemy_offer_ransom_for_prisoner",0,
##diplomacy start+ Since s2 is the name of a kingdom rather than a person, change "sell him" to "sell them"
    "{s2} offers you a sum of {reg12} denars in silver if you are willing to sell them {s1}.",
##diplomacy end+
    "none",
    [ (call_script, "script_calculate_ransom_amount_for_troop", "$g_ransom_offer_troop"),
      (assign, reg12, reg0),
      (str_store_troop_name, s1, "$g_ransom_offer_troop"),
      (store_troop_faction, ":faction_no", "$g_ransom_offer_troop"),
      (str_store_faction_name, s2, ":faction_no"),
     
       #SB : add tableau
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 70),
      (position_set_y, pos0, 5),
      (position_set_z, pos0, 75),
      (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$g_ransom_offer_troop", pos0),
     ],
    [
      ("ransom_accept",[],"Accept the offer.",
       [ ##diplomacy begin
       
        (troop_set_slot, "$g_ransom_offer_troop", slot_troop_courtesan, -1),
        (try_begin),
          (gt, "$g_player_chamberlain", 0),
          (call_script, "script_dplmc_pay_into_treasury", reg12),
        (else_try),
        ##diplomacy end
          (troop_add_gold, "trp_player", reg12),
        ##diplomacy begin
        (try_end),
        ##diplomacy end
		##diplomacy start+
		#The enemy actually loses the gold paid.
		(assign, ":gold_paid", reg12),
		(assign, ":lord_who_pays", "$g_ransom_offer_troop"),
		(store_troop_faction, ":faction_no", "$g_ransom_offer_troop"),
		#For kingdom ladies, someone else might pay.
		(try_begin),
			(is_between, "$g_ransom_offer_troop", kingdom_ladies_begin, kingdom_ladies_end),
			(neg|troop_slot_eq, "$g_ransom_offer_troop", slot_troop_occupation, slto_kingdom_hero),#I think at this step even for heroes it's 0
			(neg|troop_slot_ge, "$g_ransom_offer_troop", slot_troop_wealth, 1),
			(try_begin),
				#Check spouse pays
				(troop_get_slot, ":lord", "$g_ransom_offer_troop", slot_troop_spouse),
				(this_or_next|is_between, ":lord", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
				(store_troop_faction, ":lord_faction", ":lord"),
				(eq, ":faction_no", ":lord_faction"),
				(neg|troop_slot_ge, ":lord", slot_troop_occupation, slto_retirement),
				(assign, ":lord_who_pays", ":lord"),
			(else_try),
				#Check father pays
				(troop_get_slot, ":lord", "$g_ransom_offer_troop", slot_troop_father),
				(this_or_next|is_between, ":lord", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
				(store_troop_faction, ":lord_faction", ":lord"),
				(eq, ":faction_no", ":lord_faction"),
				(neg|troop_slot_ge, ":lord", slot_troop_occupation, slto_retirement),
				(assign, ":lord_who_pays", ":lord"),
			(else_try),
				#Check guardian pays
				(troop_get_slot, ":lord", "$g_ransom_offer_troop", slot_troop_guardian),
				(this_or_next|is_between, ":lord", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
				(store_troop_faction, ":lord_faction", ":lord"),
				(eq, ":faction_no", ":lord_faction"),
				(neg|troop_slot_ge, ":lord", slot_troop_occupation, slto_retirement),
				(assign, ":lord_who_pays", ":lord"),
			(else_try),
				#Check mother pays
				(troop_get_slot, ":lord", "$g_ransom_offer_troop", slot_troop_mother),
				(this_or_next|is_between, ":lord", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
				(store_troop_faction, ":lord_faction", ":lord"),
				(eq, ":faction_no", ":lord_faction"),
				(neg|troop_slot_ge, ":lord", slot_troop_occupation, slto_retirement),
				(assign, ":lord_who_pays", ":lord"),
			(try_end),
            #SB : copy from dialogues
            (call_script, "script_get_kingdom_lady_social_determinants", "$g_ransom_offer_troop"),
            (assign, ":new_location", reg1),
            (troop_set_slot, "$g_ransom_offer_troop", slot_troop_cur_center, ":new_location"),
		(try_end),
		(try_begin),
			(ge, ":gold_paid", 0),
			(ge, ":lord_who_pays", 1),
			(troop_is_hero, ":lord_who_pays"),
			#Remove the gold.  The lady has her own funds (e.g. from her dower)
			#that will partially defray the expense to the lord, depending on
			#the campaign difficulty.
		    (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
		    (try_begin),
			   (eq, ":reduce_campaign_ai", 0), #hard: lord pays 50%, lady's resources pay for 50%
			   (val_div, ":gold_paid", 2),
		    (else_try),
			   (eq, ":reduce_campaign_ai", 1), #medium: lord pays 75%, lady's resources pay for 25%
			   (val_mul, ":gold_paid", 3),
			   (val_div, ":gold_paid", 4),
		    (try_end),#easy: lord pays 100%, lady pays nothing
			(call_script, "script_dplmc_remove_gold_from_lord_and_holdings", ":gold_paid", ":lord_who_pays"),
		(try_end),
		##diplomacy end+
        (party_remove_prisoners, "$g_ransom_offer_party", "$g_ransom_offer_troop", 1),
        (call_script, "script_remove_troop_from_prison", "$g_ransom_offer_troop"),
        (try_begin),
            (troop_get_type, ":is_female", "trp_player"),
            (eq, ":is_female", tf_female),
            #SB : add condition here
            (troop_get_type, ":is_female", "$g_ransom_offer_troop"),
            (eq, ":is_female", tf_male),
            (get_achievement_stat, ":number_of_lords_sold", ACHIEVEMENT_MAN_HANDLER, 0),
            (val_add, ":number_of_lords_sold", 1),
            (set_achievement_stat, ACHIEVEMENT_MAN_HANDLER, 0, ":number_of_lords_sold"),			

            (eq, ":number_of_lords_sold", 3),
            (unlock_achievement, ACHIEVEMENT_MAN_HANDLER),
        (try_end),

        (change_screen_return),
        ]),
      ("ransom_reject",[],"Reject the offer.",
       [
	    ##diplomacy start+
		#Relation loss altered by lord personality type.
		#OLD:
        #(call_script, "script_change_player_relation_with_troop", "$g_ransom_offer_troop", -4),
		#NEW:
		(try_begin),
			(troop_slot_eq, "$g_ransom_offer_troop", slot_lord_reputation_type, lrep_quarrelsome),
			(call_script, "script_change_player_relation_with_troop", "$g_ransom_offer_troop", -6),
		(else_try),
			(troop_slot_eq, "$g_ransom_offer_troop", slot_lord_reputation_type, lrep_debauched),
			(call_script, "script_change_player_relation_with_troop", "$g_ransom_offer_troop", -5),
		(else_try),
			(call_script, "script_change_player_relation_with_troop", "$g_ransom_offer_troop", -4),
		(try_end),
		##diplomacy end+
        (call_script, "script_change_player_honor", -1),
        (assign, "$g_ransom_offer_rejected", 1),
		##diplomacy start+
		#TODO: Review this, it was partway through a redesign when I stopped.
		#Also apply a negative reaction modifier to other lords
		(assign, ":save_reg0", reg0),

		(store_faction_of_troop, ":captive_faction", "$g_ransom_offer_troop"),
		#For kingdom ladies:
		(try_begin),
			(is_between, "$g_ransom_offer_troop", kingdom_ladies_begin, kingdom_ladies_end),
			#(troop_slot_eq, "$g_ransom_offer_troop", slot_troop_occupation, slto_kingdom_lady),
			(call_script, "script_get_kingdom_lady_social_determinants", "$g_talk_troop"),
			(assign, ":guardian", reg0),
			(store_faction_of_troop, ":captive_faction", ":guardian"),

			(try_for_range, ":troop_no", heroes_begin, heroes_end),
				(troop_slot_ge, ":troop_no", slot_troop_occupation, slto_kingdom_hero),#lowest valid
				(neg|troop_slot_ge, ":troop_no", slot_troop_occupation, slto_inactive_pretender),#end of valid range
				(neq, "$g_ransom_offer_troop", ":troop_no"),
				(store_faction_of_troop, ":troop_faction", ":troop_no"),

				(assign, ":disapproval_threshold", 20),
				(try_begin),
					(neq, ":troop_faction", ":captive_faction"),
					(neg|is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
					(assign, ":disapproval_threshold", 40),
				(try_end),
				#(this_or_next|is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
				#	(eq, ":troop_faction", ":captive_faction"),
				(assign, ":relation_change", 0),

				#family
				(try_begin),
					(this_or_next|troop_slot_eq, ":troop_no", slot_troop_spouse, "$g_ransom_offer_troop"),
					(this_or_next|troop_slot_eq, "$g_ransom_offer_troop", slot_troop_spouse, ":troop_no"),
					(eq, ":guardian", ":troop_no"),
					(assign, ":relation_change", -4),
				(else_try),
					(eq, ":troop_no", slot_troop_betrothed, "$g_ransom_offer_troop"),
					(assign, ":relation_change", -4),
				(else_try),
					(call_script, "script_troop_get_family_relation_to_troop", "$g_ransom_offer_troop", ":troop_no"),
					(ge, reg0, 14),
					(assign, ":relation_change", -3),
				(else_try),
					(ge, reg0, 10),
					(assign, ":relation_change", -2),
				(else_try),
					(ge, reg0, 2),
					(assign, ":relation_change", -1),
				(else_try),
					(call_script, "script_troop_get_relation_with_troop", ":troop_no", "$g_ransom_offer_troop"),
					(ge, reg0, ":disapproval_threshold"),
					(this_or_next|is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
						(eq, ":troop_faction", ":captive_faction"),
					(assign, ":relation_change", -1),
				(else_try),
					(ge, ":guardian", 1),
					(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":guardian"),
					(ge, reg0, ":disapproval_threshold"),
					(assign, ":relation_change", -1),
				(try_end),

				(lt, ":relation_change", 0),
				(try_begin),
					(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
					(val_mul, ":relation_change", 3),#-1 to -2, -2 to -3, -3 to -5, -4 to -6
					(val_sub, ":relation_change", 1),
					(val_div, ":relation_change", 2),
				(try_end),
				(call_script, "script_change_player_relation_with_troop", ":troop_no", ":relation_change"),
			(try_end),
		(else_try),
		#For others:
			(is_between, "$g_ransom_offer_troop", active_npcs_begin, active_npcs_end),
			(try_for_range, ":hero", heroes_begin, heroes_end),
				(this_or_next|is_between, ":hero", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":hero", slot_troop_occupation, slto_kingdom_hero),
				(neg|troop_slot_eq, ":hero", slot_troop_occupation, dplmc_slto_dead),
				(neg|troop_slot_ge, ":hero", slot_troop_occupation, slto_retirement),

				(neq, ":hero", "$g_ransom_offer_troop"),

				(store_faction_of_troop, ":troop_faction", ":hero"),

				(assign, ":relation_change", 0),

				(call_script, "script_troop_get_family_relation_to_troop", "$g_ransom_offer_troop", ":hero"),
				(try_begin),
					(ge, reg0, 10),
					(assign, ":relation_change", -1),
				(try_end),

				(call_script, "script_troop_get_relation_with_troop", ":hero", "$g_ransom_offer_troop"),
				(try_begin),
					(ge, reg0, 20),
					(eq, ":troop_faction", ":captive_faction"),
					(val_sub, ":relation_change", 1),
				(else_try),
					(ge, reg0, 40),
					(val_sub, ":relation_change", 1),
				(else_try),
					(lt, reg0, 0),
					(assign, ":relation_change", 0),
				(try_end),

				(lt, ":relation_change", 0),
				(try_begin),
					(troop_slot_eq, ":hero", slot_lord_reputation_type, lrep_quarrelsome),
					(val_mul, ":relation_change", 3),#-1 to -2, -2 to -3, -3 to -5, -4 to -6
					(val_sub, ":relation_change", 1),
					(val_div, ":relation_change", 2),
				(try_end),
				(call_script, "script_change_player_relation_with_troop", ":hero", ":relation_change"),
			(try_end),

			(try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
				(neg|troop_slot_eq, ":lady", slot_troop_occupation, slto_kingdom_hero),
				(neg|troop_slot_eq, ":lady", slot_troop_occupation, dplmc_slto_dead),
				(neg|troop_slot_ge, ":lady", slot_troop_occupation, slto_retirement),

				(neq, ":lady", "$g_ransom_offer_troop"),

				(assign, ":relation_change", 0),
				(call_script, "script_troop_get_family_relation_to_troop", ":lady", "$g_ransom_offer_troop"),
				(try_begin),
					(ge, reg0, 14),
					(assign, ":relation_change", -3),
				(else_try),
					(ge, reg0, 10),
					(assign, ":relation_change", -2),
				(else_try),
					(ge, reg0, 2),
					(assign, ":relation_change", -1),
				(else_try),
					(call_script, "script_troop_get_relation_with_troop", ":lady", "$g_ransom_offer_troop"),
					(ge, reg0, 20),
					(assign, ":relation_change", -1),
				(try_end),

				(lt, ":relation_change", 0),
				(call_script, "script_change_player_relation_with_troop", ":lady", ":relation_change"),
			(try_end),
		(try_end),

		(assign, reg0, ":save_reg0"),
		##diplomacy end+
        (change_screen_return),
        ]),
    ]
  ),


  (
    "training_ground",0,
    "You approach a training field where you can practice your martial skills. What kind of training do you want to do?",
    "none",
    [
      (try_begin), #SB : track slot
        (party_get_slot, ":scene_no", slot_grounds_track, "$g_encountered_party"),
        (le, ":scene_no", 0),
        (store_add, ":scene_no", "scn_training_ground_horse_track_1", "$g_encountered_party"),
        (val_sub, ":scene_no", training_grounds_begin),
        (party_set_slot, "$g_encountered_party", slot_grounds_track, ":scene_no"),
      (try_end),
      (try_begin), #SB : melee/ranged slot
        (party_get_slot, ":scene_no", slot_grounds_melee, "$g_encountered_party"),
        (le, ":scene_no", 0),
        (store_add, ":scene_no", "scn_training_ground_ranged_melee_1", "$g_encountered_party"),
        (val_sub, ":scene_no", training_grounds_begin),
        (party_set_slot, "$g_encountered_party", slot_grounds_melee, ":scene_no"),
      (try_end),
      (assign, "$g_training_ground_melee_training_scene", ":scene_no"),
      
      
      #SB : modify this interval
      (party_get_skill_level, ":training", "p_main_party", "skl_trainer"), #from 0 to 10
      (try_begin), #grab trainer troop if it isn't linked
        (party_get_slot, ":trainer_troop", "$g_encountered_party", slot_grounds_trainer),
        (try_begin),
          (le, ":trainer_troop", 0),
          (store_sub, ":trainer_troop", "$g_encountered_party", training_grounds_begin),
          (val_add, ":trainer_troop", training_ground_trainers_begin),
          (party_set_slot, "$g_encountered_party", slot_grounds_trainer, ":trainer_troop"),
        (try_end),
        (troop_get_slot, ":difficulty", ":trainer_troop", slot_troop_trainer_training_difficulty), #from 0 to 4
        (val_add, ":training", ":difficulty"), #0 to 14
      (try_end),
      (val_div, ":training", 2), #0 to 7
      (val_max, ":training", 3),
      (try_begin), #was $g_training_ground_training_count
        (party_slot_ge, "$g_encountered_party", slot_grounds_count, ":training"),
        (party_set_slot, "$g_encountered_party", slot_grounds_count, 0),
        # (assign, "$g_training_ground_training_count", 0),
        (rest_for_hours, 1, 5, 0), #rest while not attackable
        (assign, "$auto_enter_town", "$g_encountered_party"),
        (change_screen_return),
      (try_end),
      #SB : set background mesh, player troop
      (assign, "$g_player_troop", "trp_player"),
      (set_background_mesh, "mesh_pic_mb_warrior_1"),
      ],
    [
      ("camp_trainer",
       [], "Speak with the trainer.",
       [
         (set_jump_mission, "mt_training_ground_trainer_talk"),
         # no need to reset visitors, trainer is always there
         # (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
         # (reset_visitors),
         (set_jump_entry, 5),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         (change_screen_mission),
         (music_set_situation, 0),
         ]),
      ("camp_train_melee",
       [
         (neg|troop_is_wounded, "trp_player"),
         (call_script, "script_party_count_fit_for_battle", "p_main_party"),
         (gt, reg0, 1),
         ], "Sparring practice.",
       [
         (assign, "$g_mt_mode", ctm_melee),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_1"),
         (music_set_situation, 0),
         ]),
      ("camp_train_archery",[], "Ranged weapon practice.",
       [
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_1"),
         (music_set_situation, 0),
         ]),
      ("camp_train_mounted",[], "Horseback practice.",
       [
         (assign, "$g_mt_mode", ctm_mounted),
         (jump_to_menu, "mnu_training_ground_selection_details_mounted"),
         (music_set_situation, 0),
         ]),

      ("go_to_track",[(eq, "$cheat_mode", 1)],"{!}Cheat: Go to track.",
       [
         (set_jump_mission, "mt_ai_training"),
         (try_begin), #SB : slots
           (party_get_slot, ":scene_no", slot_grounds_track, "$g_encountered_party"),
           (le, ":scene_no", 0),
           (store_add, ":scene_no", "scn_training_ground_horse_track_1", "$g_encountered_party"),
           (val_sub, ":scene_no", training_grounds_begin),
         (try_end),
         (jump_to_scene, ":scene_no"),
         (change_screen_mission),
        ]
       ),
      ("go_to_range",[(eq, "$cheat_mode", 1)],"{!}Cheat: Go to range.",
       [
         (set_jump_mission, "mt_ai_training"),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         (change_screen_mission),
        ]
       ),
      ("leave",[],"Leave.",
       [(change_screen_return),
        ]),
    ]
  ),

  ("training_ground_selection_details_melee_1",0,
   "How many opponents will you go against?",
   "none",
   [
     (call_script, "script_write_fit_party_members_to_stack_selection", "p_main_party", 1),
     (troop_get_slot, "$temp", "trp_stack_selection_amounts", 1), #number of men fit
     (assign, "$temp_2", 1),
     ],
    [
      ("camp_train_melee_num_men_1",[(ge, "$temp", 1)], "One.",
       [
         (assign, "$temp", 1),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("camp_train_melee_num_men_2",[(ge, "$temp", 2)], "Two.",
       [
         (assign, "$temp", 2),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("camp_train_melee_num_men_3",[(ge, "$temp", 3)], "Three.",
       [
         (assign, "$temp", 3),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("camp_train_melee_num_men_4",[(ge, "$temp", 4)], "Four.",
       [
         (assign, "$temp", 4),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("go_back_dot",[],"Cancel.",
       [
         (jump_to_menu, "mnu_training_ground"),
        ]),
      ]
  ),

  ("training_ground_selection_details_melee_2",0,
   "Choose your opponent:^{s1}^{reg1}:",
   "none",
    [
      (assign, reg1, "$temp_2"),
      (troop_get_slot, "$temp_3", "trp_stack_selection_amounts", 0), #number of slots
      
      #SB : show current list
      (str_clear, s1),
      (store_sub, ":end", "$temp_2", 1),
      (try_for_range, ":slot_index", 0, ":end"),
        (store_add, reg0, ":slot_index", 1),
        (troop_get_slot, ":troop_id", "trp_temp_array_a", ":slot_index"),
        (gt, ":troop_id", 0),
        (str_store_troop_name, s2, ":troop_id"),
        (str_store_string, s1, "@{s1}^{reg0}: {s2}"),
      # (else_try),
        # (str_store_string, s1, "@{s1}^{reg0}:"),
      (try_end),
    ],
    [
      ("training_ground_selection_details_melee_random", [], "Choose randomly.",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", -1),]),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_training_ground"),]
       ), #SB : stack built from loop
      ]+
      [("stack"+str(x), [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", x),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", x),])
       for x in range(1, 20)]
  ),



  ("training_ground_selection_details_mounted",0,
   "What kind of weapon do you want to train with?",
   "none",
   [
   #SB : background mesh
   (set_background_mesh, "mesh_pic_mb_warrior_2"),
   ],
    [
      ("camp_train_mounted_details_1",[], "One handed weapon.",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_one_handed_wpn, 0),
         ]),
      ("camp_train_mounted_details_2",[], "Polearm.",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_polearm, 0),
         ]),
      ("camp_train_mounted_details_3",[], "Bow.",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_bow, 0),
         ]),
      ("camp_train_mounted_details_4",[], "Thrown weapon.",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_thrown, 0),
         ]),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  ("training_ground_selection_details_ranged_1",0,
   "What kind of ranged weapon do you want to train with?",
   "none",
   [
   (set_background_mesh, "mesh_pic_mb_warrior_4"), #SB : background mesh
   ],
    [
      ("camp_train_ranged_weapon_bow",[], "Bow and arrows.",
       [
         (assign, "$g_mt_mode", ctm_ranged),
         (assign, "$temp", itp_type_bow),
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_2"),
         ]),
      ("camp_train_ranged_weapon_crossbow",[], "Crossbow.",
       [
         (assign, "$g_mt_mode", ctm_ranged),
         (assign, "$temp", itp_type_crossbow),
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_2"),
         ]),
      ("camp_train_ranged_weapon_thrown",[], "Throwing Knives.",
       [
         (assign, "$g_mt_mode", ctm_ranged),
         (assign, "$temp", itp_type_thrown),
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_2"),
         ]),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  ("training_ground_selection_details_ranged_2",0,
   "What range do you want to practice at?",
   "none",
   [
   (set_background_mesh, "mesh_pic_mb_warrior_4"), #SB : background mesh
   ],
    [
      ("camp_train_ranged_details_1",[], "10 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 10),
         ]),
      ("camp_train_ranged_details_2",[], "20 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 20),
         ]),
      ("camp_train_ranged_details_3",[], "30 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 30),
         ]),
      ("camp_train_ranged_details_4",[], "40 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 40),
         ]),
      ("camp_train_ranged_details_5",[(eq, "$g_mt_mode", ctm_ranged),], "50 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 50),
         ]),
      ("camp_train_ranged_details_6",[(eq, "$g_mt_mode", ctm_ranged),], "60 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 60),
         ]),
      ("camp_train_ranged_details_7",[(eq, "$g_mt_mode", ctm_ranged),], "70 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 70),
         ]),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  ("training_ground_description",0,
   "{s0}",
   "none",
   [
   #Sb : format string here instead of script_start_training_at_training_ground
   (store_sub, reg0, "$g_training_ground_training_num_enemies", 1),
   (store_sub, ":string", "$g_mt_mode", 1),
   (val_add, ":string", "str_ctm_melee"),
   (str_store_string, s0, ":string"),
   
   ],
    [
      ("continue", [], "Continue...",
       [
         (jump_to_scene, "$g_training_ground_training_scene"),
         (change_screen_mission),
        ]
       ),
      ]
  ),

  ("training_ground_training_result",mnf_disable_all_keys,
   "{s7}{s2}",
   "none",
   [
     (store_skill_level, ":trainer_skill", "skl_trainer", "trp_player"),
     (store_add, ":trainer_skill_multiplier", 5, ":trainer_skill"),
     (call_script, "script_write_fit_party_members_to_stack_selection", "p_main_party", 1),
     (str_clear, s2),
     (troop_get_slot, ":num_fit", "trp_stack_selection_amounts", 1),
     (troop_get_slot, ":num_slots", "trp_stack_selection_amounts", 0),
     (try_begin),
       (gt, "$g_training_ground_training_success_ratio", 0),
       (store_mul, ":xp_ratio_to_add", "$g_training_ground_training_success_ratio", "$g_training_ground_training_success_ratio"),
       (try_begin),
         (eq, "$g_training_ground_training_success_ratio", 100),
         (val_mul, ":xp_ratio_to_add", 2), #2x when perfect
       (try_end),
       (try_begin),
         (eq, "$g_mt_mode", ctm_melee),
         (val_div, ":xp_ratio_to_add", 2),
       (try_end),
       (val_div, ":xp_ratio_to_add", 10), # value over 1000
       (try_begin),
         (gt, ":num_fit", 8),
         (val_mul, ":xp_ratio_to_add", 3),
         (assign, ":divisor", ":num_fit"),
         (convert_to_fixed_point, ":divisor"),
         (store_sqrt, ":divisor", ":divisor"),
         (convert_to_fixed_point, ":xp_ratio_to_add"),
         (val_div, ":xp_ratio_to_add", ":divisor"),
       (try_end),
##       (assign, reg0, ":xp_ratio_to_add"),
##       (display_message, "@xp earn ratio: {reg0}/1000"),
       (store_mul, ":xp_ratio_to_add_with_trainer_skill", ":xp_ratio_to_add", ":trainer_skill_multiplier"),
       (val_div, ":xp_ratio_to_add_with_trainer_skill", 10),
       (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
       (store_add, ":end_cond", ":num_slots", 2),
       (try_for_range, ":i_slot", 2, ":end_cond"),
         (troop_get_slot, ":amount", "trp_stack_selection_amounts", ":i_slot"),
         (troop_get_slot, ":troop_id", "trp_stack_selection_ids", ":i_slot"),
         (assign, ":end_cond_2", ":num_stacks"),
         (try_for_range, ":stack_no", 0, ":end_cond_2"),
           (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
           (eq, ":stack_troop", ":troop_id"),
           (assign, ":end_cond_2", 0), #break
           (call_script, "script_cf_training_ground_sub_routine_for_training_result", ":troop_id", ":stack_no", ":amount", ":xp_ratio_to_add_with_trainer_skill"),
           (str_store_troop_name_by_count, s1, ":troop_id", ":amount"),
           #SB : hero name count
           (try_begin),
             (troop_is_hero, ":troop_id"),
             (assign, reg2, 1),
           (else_try),
             (assign, reg2, 0),
             (assign, reg1, ":amount"),
           (try_end),
           (str_store_string, s2, "@{s2}^{reg2?:{reg1} }{s1} earned {reg0} experience."),
         (try_end),
       (try_end),
       (try_begin),
         (eq, "$g_mt_mode", ctm_melee),
         (store_mul, ":special_xp_ratio_to_add", ":xp_ratio_to_add", 3),
         (val_div, ":special_xp_ratio_to_add", 2),
         (try_for_range, ":enemy_index", 0, "$g_training_ground_training_num_enemies"),
           (troop_get_slot, ":troop_id", "trp_temp_array_a", ":enemy_index"),
           (assign, ":end_cond_2", ":num_stacks"),
           (try_for_range, ":stack_no", 0, ":end_cond_2"),
             (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
             (eq, ":stack_troop", ":troop_id"),
             (assign, ":end_cond_2", 0), #break
             (call_script, "script_cf_training_ground_sub_routine_for_training_result", ":troop_id", ":stack_no", 1, ":special_xp_ratio_to_add"),
             (str_store_troop_name, s1, ":troop_id"),
             (str_store_string, s2, "@{s2}^{s1} earned an additional {reg0} experience."),
           (try_end),
         (try_end),
       (try_end),
       (try_begin),
         (call_script, "script_cf_training_ground_sub_routine_for_training_result", "trp_player", -1, 1, ":xp_ratio_to_add"),
         (str_store_string, s2, "@^You earned {reg0} experience.{s2}"),
       (try_end),
     (try_end),
     (try_begin),
       (eq, "$g_training_ground_training_success_ratio", 0),
       (str_store_string, s7, "@The training didn't go well at all."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 25),
       (str_store_string, s7, "@The training didn't go well at all."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 50),
       (str_store_string, s7, "@The training didn't go very well."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 75),
       (str_store_string, s7, "@The training went quite well."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 99),
       (str_store_string, s7, "@The training went very well."),
     (else_try),
       (str_store_string, s7, "@The training went perfectly."),
     (try_end),

     ],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
   ),

  ("marshall_selection_candidate_ask",0,
   "{s15} will soon select a new marshall for {s23}. Some of the lords have suggested your name as a likely candidate.",
   "none",
   [
     (try_begin),
       (eq, "$g_presentation_marshall_selection_ended", 1),
       (change_screen_return),
     (try_end),
     (faction_get_slot, ":king", "$players_kingdom", slot_faction_leader),
     (str_store_troop_name, s15, ":king"),
     (str_store_faction_name, s23, "$players_kingdom"),
     ],
    [
      ("marshall_candidate_accept", [], "Let {s15} learn that you are willing to serve as marshall.",
       [
         (start_presentation, "prsnt_marshall_selection"),
        ]
       ),
      ("marshall_candidate_reject", [], "Tell everyone that you are too busy these days.",
       [
         (try_begin),
           (eq, "$g_presentation_marshall_selection_max_renown_2_troop", "trp_player"),
           (assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_3"),
           (assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_3_troop"),
         (else_try),
           (assign, "$g_presentation_marshall_selection_max_renown_1", "$g_presentation_marshall_selection_max_renown_2"),
           (assign, "$g_presentation_marshall_selection_max_renown_1_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
           (assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_3"),
           (assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_3_troop"),
         (try_end),
         (start_presentation, "prsnt_marshall_selection"),
        ]
       ),
      ]
  ),




##    [
##      ("renew_oath",[],"Renew your oath to {s1} for another month.",[
##          (store_current_day, ":cur_day"),
##          (store_add, "$g_oath_end_day", ":cur_day", 30),
##          (change_screen_return)]),
##      ("dont_renew_oath",[],"Become free of your bond.",[
##          (assign, "$players_kingdom",0),
##          (assign, "$g_player_permitted_castles", 0),
##          (change_screen_return)]),
##    ]
##  ),


#####################################################################
## Captivity....
#####################################################################
#####################################################################
#####################################################################
#####################################################################
  (
    "captivity_avoid_wilderness",0,
    "Suddenly all the world goes black around you.\
 Many hours later you regain your conciousness and find yourself at the spot you fell.\
 Your enemies must have taken you up for dead and left you there.\
 However, it seems that none of your wound were lethal,\
 and altough you feel awful, you find out that can still walk.\
 You get up and try to look for any other survivors from your party.",
    "none",
    [
      ],
    []
  ),

  (
    "captivity_start_wilderness",0,
    "Stub",
    "none",
    [
          (assign, "$g_player_is_captive", 1),
          (try_begin),
            (eq,"$g_player_surrenders",1),
            (jump_to_menu, "mnu_captivity_start_wilderness_surrender"),
          (else_try),
            (jump_to_menu, "mnu_captivity_start_wilderness_defeat"),
          (try_end),
      ],
    []
  ),

  (
    "captivity_start_wilderness_surrender",0,
    "Stub",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign,"$auto_menu",-1), #We need this since we may come here by something other than auto_menu
       (assign, "$capturer_party", "$g_encountered_party"),
       (jump_to_menu, "mnu_captivity_wilderness_taken_prisoner"),
      ],
    []
  ),
  (
    "captivity_start_wilderness_defeat",0,
    "Your enemies take you prisoner.",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign,"$auto_menu",-1),
       (assign, "$capturer_party", "$g_encountered_party"),

       (try_begin),
         (party_stack_get_troop_id, ":party_leader", "$g_encountered_party", 0),
         (is_between, ":party_leader", active_npcs_begin, active_npcs_end),
         (troop_slot_eq, ":party_leader", slot_troop_occupation, slto_kingdom_hero),
         (store_sub, ":kingdom_hero_id", ":party_leader", active_npcs_begin),
         (set_achievement_stat, ACHIEVEMENT_BARON_GOT_BACK, ":kingdom_hero_id", 1),
       (try_end),

       (jump_to_menu, "mnu_captivity_wilderness_taken_prisoner"),
    ],
    []
  ),
  #SB : impose various degrees of penalty through permanent wounding
  (
    "captivity_start_castle_surrender",0,
    "Stub",
    "none",
    [
        (assign, "$g_player_is_captive", 1),
        (assign,"$auto_menu",-1),
        (assign, "$capturer_party", "$g_encountered_party"),
        # (try_begin),
          # (store_random_in_range, ":random_no", -100, 100),
          # (ge, ":random_no", "$g_player_luck"),
          # (assign, "$g_next_menu", "mnu_captivity_castle_taken_prisoner"),
          # (jump_to_menu, "mnu_permanent_damage"),
        # (else_try),
          (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
        # (try_end),
      ],
    []
  ),
  ( #SB : defeat in castles has chance of wounding
    "captivity_start_castle_defeat",0,
    "Stub",
    "none",
    [
        (assign, "$g_player_is_captive", 1),
        (assign,"$auto_menu",-1),
        (assign, "$capturer_party", "$g_encountered_party"),
        (try_begin),
          (store_random_in_range, ":random_no", -50, 100),
          (ge, ":random_no", "$g_player_luck"),
          (assign, "$g_next_menu", "mnu_captivity_castle_taken_prisoner"),
          (jump_to_menu, "mnu_permanent_damage"),
        (else_try),
          (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
        (try_end),
      ],
    []
  ),
  ( #SB : defeat while defending has higher penalty
    "captivity_start_under_siege_defeat",0,
    "Your enemies take you prisoner.",
    "none",
    [
        (assign, "$g_player_is_captive", 1),
        (assign,"$auto_menu",-1),
        (assign, "$capturer_party", "$g_encountered_party"),
        (try_begin),
          (store_random_in_range, ":random_no", -50, 150),
          (ge, ":random_no", "$g_player_luck"),
          (assign, "$g_next_menu", "mnu_captivity_castle_taken_prisoner"),
          (jump_to_menu, "mnu_permanent_damage"),
        (else_try),
          (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
        (try_end),
    ],
    []
  ),

  (
    "captivity_wilderness_taken_prisoner",mnf_scale_picture,
    "Your enemies take you prisoner.",
    "none",
    [
        (set_background_mesh, "mesh_pic_prisoner_wilderness"),
     ],
    [
      ("continue",[],"Continue...",
       [
	     # Explanation of removing below code : heros are already being removed with 50% (was 75%, I decreased it) probability in mnu_total_defeat, why here there is additionally 30% removing of heros?
		 # See codes linked to "mnu_captivity_start_wilderness_surrender" and "mnu_captivity_start_wilderness_defeat" which is connected with here they all also enter 
		 # "mnu_total_defeat" and inside the "mnu_total_defeat" there is script_party_remove_all_companions which removes 50% (was 75%, I decreased it) of compainons from player party.

         #(try_for_range, ":npc", companions_begin, companions_end),
         #  (main_party_has_troop, ":npc"),
         #  (store_random_in_range, ":rand", 0, 100),
         #  (lt, ":rand", 30),
         #  (remove_member_from_party, ":npc", "p_main_party"),
         #  (troop_set_slot, ":npc", slot_troop_occupation, 0),
         #  (troop_set_slot, ":npc", slot_troop_playerparty_history, pp_history_scattered),
         #  (assign, "$last_lost_companion", ":npc"),
         #  (store_faction_of_party, ":victorious_faction", "$g_encountered_party"),
         #  (troop_set_slot, ":npc", slot_troop_playerparty_history_string, ":victorious_faction"),
         #  (troop_set_health, ":npc", 100),
         #  (store_random_in_range, ":rand_town", towns_begin, towns_end),
         #  (troop_set_slot, ":npc", slot_troop_cur_center, ":rand_town"),
         #  (assign, ":nearest_town_dist", 1000),
         #  (try_for_range, ":town_no", towns_begin, towns_end),
         #    (store_faction_of_party, ":town_fac", ":town_no"),
         #    (store_relation, ":reln", ":town_fac", "fac_player_faction"),
         #    (ge, ":reln", 0),
         #    (store_distance_to_party_from_party, ":dist", ":town_no", "p_main_party"),
         #    (lt, ":dist", ":nearest_town_dist"),
         #    (assign, ":nearest_town_dist", ":dist"),
         #    (troop_set_slot, ":npc", slot_troop_cur_center, ":town_no"),
         #  (try_end),
         #(try_end),

         # (set_camera_follow_party, "$capturer_party"),
         # (assign, "$g_player_is_captive", 1),
         # (store_random_in_range, ":random_hours", 18, 30),         
         # (call_script, "script_event_player_captured_as_prisoner"),
         # (call_script, "script_stay_captive_for_hours", ":random_hours"),
         # (assign,"$auto_menu","mnu_captivity_wilderness_check"),
         # (change_screen_return),


         (assign, "$talk_context", tc_player_defeated),
         
         (party_stack_get_troop_id, ":capturer_troop", "$capturer_party", 0),
         (party_stack_get_troop_dna, ":capturer_dna", "$capturer_party", 0),
         (party_get_template_id, ":template", "$capturer_party"),
         (store_faction_of_troop, ":troop_faction", ":capturer_troop"),
         
         (try_begin),     
             (eq, "$g_sexual_content", 2),
             (this_or_next|eq, ":template", "pt_deserters"),
             (this_or_next|eq, ":troop_faction", fac_outlaws),
             (this_or_next|eq, ":troop_faction", fac_forest_bandits),
             (this_or_next|eq, ":troop_faction", fac_mountain_bandits),
             (this_or_next|eq, ":troop_faction", fac_black_khergits),
             (this_or_next|eq, ":troop_faction", fac_dark_knights),
             (this_or_next|eq, "$g_encountered_party_faction", fac_outlaws),
             (this_or_next|eq, "$g_encountered_party_faction", fac_forest_bandits),
             (this_or_next|eq, "$g_encountered_party_faction", fac_mountain_bandits),
             (this_or_next|eq, "$g_encountered_party_faction", fac_black_khergits),
             (eq, "$g_encountered_party_faction", fac_dark_knights),
             (call_script, "script_setup_troop_meeting", ":capturer_troop", ":capturer_dna"),
         (else_try),
            (eq, "$g_sexual_content", 2),
            (is_between, ":capturer_troop", heroes_begin, heroes_end),
            (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_debauched),
            (call_script, "script_setup_troop_meeting", ":capturer_troop", -1),
         (else_try),
             (set_camera_follow_party, "$capturer_party"),
             (assign, "$g_player_is_captive", 1),
             (store_random_in_range, ":random_hours", 18, 30),         
             (call_script, "script_event_player_captured_as_prisoner"),
             (call_script, "script_stay_captive_for_hours", ":random_hours"),
             (assign,"$auto_menu","mnu_captivity_wilderness_check"),
             (change_screen_return),
         (try_end),
         ]),
      ]
  ),
  (
    "captivity_wilderness_check",0,
    "stub",
    "none",
    [(jump_to_menu,"mnu_captivity_end_wilderness_escape")],
    []
  ),
  (
    "captivity_end_wilderness_escape", mnf_scale_picture,
    "After painful days of being dragged about as a prisoner, you find a chance and escape from your captors!",
    "none",
    [
        (play_cue_track, "track_escape"),
          ##diplomacy start+ test gender with script
        #(troop_get_type, ":is_female", "trp_player"),#<- replaced
        (try_begin),
          #(eq, ":is_female", 1),#<- replaced
          (eq, "$character_gender", tf_female),#<- added
          (set_background_mesh, "mesh_pic_escape_1_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_escape_1"),
        (try_end),
          ##diplomacy end+
    ],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 0),
           (try_begin),
             (party_is_active, "$capturer_party"),
             (party_relocate_near_party, "p_main_party", "$capturer_party", 2),
           (try_end),
           (call_script, "script_set_parties_around_player_ignore_player", 8, 12), #it was radius:2 and hours:4, but players make lots of complains about consequent battle losses after releases from captivity then I changed this.
           (assign, "$g_player_icon_state", pis_normal),
           (set_camera_follow_party, "p_main_party"),
           (rest_for_hours, 0, 0, 0), #stop resting
           ##diplomacy begin
           #(assign, "$g_move_fast", 1),
           ##diplomacy end
           (change_screen_return),
        ]),
    ]
  ),
  (
    "captivity_castle_taken_prisoner",0,
    "You are quickly surrounded by guards who take away your weapons. With curses and insults, they throw you into the dungeon where you must while away the miserable days of your captivity.",
    "none",
    [
          ##diplomacy start+ test gender with script
        #(troop_get_type, ":is_female", "trp_player"),#<- replaced
        (try_begin),
          #(eq, ":is_female", 1),#<- replaced
          (eq, "$character_gender", tf_female),#<- added
          (set_background_mesh, "mesh_pic_prisoner_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_prisoner_man"),
        (try_end),
          ##diplomacy end+
        #SB : deduct relation here, probably
        (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -1),
    ],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 1),
           (store_random_in_range, ":random_hours", 16, 22),
           (call_script, "script_event_player_captured_as_prisoner"),
           (call_script, "script_stay_captive_for_hours", ":random_hours"),
           (assign,"$auto_menu", "mnu_captivity_castle_check"),
           (change_screen_return)
        ]),
    ]
  ),
  (
    "captivity_rescue_lord_taken_prisoner",0,
    "You remain in disguise for as long as possible before revealing yourself.\
 The guards are outraged and beat you savagely before throwing you back into the cell for God knows how long...",
    "none",
    [
		  ##diplomacy start+ test gender with script
        #(troop_get_type, ":is_female", "trp_player"),#<-replaced
        (try_begin),
          #(eq, ":is_female", 1),#<-replaced
		  (eq, "$character_gender", tf_female),#<- added
          (set_background_mesh, "mesh_pic_prisoner_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_prisoner_man"),
        (try_end),
		  ##diplomacy end+
   ],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 1),
           (store_random_in_range, ":random_hours", 16, 22),
           (call_script, "script_event_player_captured_as_prisoner"),
           (call_script, "script_stay_captive_for_hours", ":random_hours"),
           (assign,"$auto_menu", "mnu_captivity_castle_check"),
           (change_screen_return),
        ]),
    ]
  ),
  (
    "captivity_castle_check",0,
    "stub",
    "none",
    [
        (store_random_in_range, reg(7), 0, 100),
        (try_begin),
		  (party_is_active, "$capturer_party"),
		  (store_faction_of_party, ":capturer_faction", "$capturer_party"),
		  (is_between, ":capturer_faction", kingdoms_begin, kingdoms_end),
		  (store_relation, ":relation_w_player_faction", ":capturer_faction", "fac_player_faction"),
		  (ge, ":relation_w_player_faction", 0),
          #SB : this doesn't make much sense when the player is unaffiliated
          (jump_to_menu,"mnu_captivity_end_exchanged_with_prisoner"),
		(else_try),
          (lt, reg(7), 40),
          (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
          (val_mul, ":player_renown", 2),
          (store_character_level, ":player_level", "trp_player"),
          (store_mul, "$player_ransom_amount", ":player_level", 50),
          (val_add, "$player_ransom_amount", 100),
          (val_add, "$player_ransom_amount", ":player_renown"),
          (store_troop_gold, reg3, "trp_player"),
          (store_div, ":player_gold_div_20", reg3, 20),
          (val_add, "$player_ransom_amount", ":player_gold_div_20"),

          #(gt, reg3, "$player_ransom_amount"),
          (jump_to_menu,"mnu_captivity_end_propose_ransom"),
        (else_try),
          (lt, reg(7), 45), #4% chance to be set free
          (jump_to_menu,"mnu_captivity_end_exchanged_with_prisoner"),
        (else_try),
          (jump_to_menu,"mnu_captivity_castle_remain"),
        (try_end),
    ],
    []
  ),
  (
    "captivity_end_exchanged_with_prisoner",0,
    "After days of imprisonment, you are finally set free {s0}",
    "none",
    [
      (play_cue_track, "track_escape"),
      
      (try_begin),
		  (party_is_active, "$capturer_party"),
		  (store_faction_of_party, ":capturer_faction", "$capturer_party"),
		  (is_between, ":capturer_faction", kingdoms_begin, kingdoms_end),
		  (store_relation, ":relation_w_player_faction", ":capturer_faction", "fac_player_faction"),
		  (ge, ":relation_w_player_faction", 0),
          (str_store_party_name, s13, "$capturer_party"),
          (str_store_string, s0, "@as {s13} is no longer held by your enemies."),
      (else_try),
          (str_store_string, s0, "@when your captors exchange you with another prisoner."),
      (try_end),
      ],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 0),
           (try_begin),
             (party_is_active, "$capturer_party"),
             (party_relocate_near_party, "p_main_party", "$capturer_party", 2),
           (try_end),
           (call_script, "script_set_parties_around_player_ignore_player", 8, 12), #it was radius:2 and hours:12, but players make lots of complains about consequent battle losses after releases from captivity then I changed this.
           (assign, "$g_player_icon_state", pis_normal),
           (set_camera_follow_party, "p_main_party"),
           (rest_for_hours, 0, 0, 0), #stop resting
           (change_screen_return),
        ]),
    ]
  ),
  (
    "captivity_end_propose_ransom",0,
    "You spend long hours in the sunless dank of the dungeon, more than you can count.\
 Suddenly one of your captors enters your cell with an offer;\
 he proposes to free you in return for {reg5} denars of your hidden wealth. You decide to...",
    "none",
    [
      (assign, reg5, "$player_ransom_amount"),      
    ],
    [
      ("captivity_end_ransom_accept",
      [
        (store_troop_gold,":player_gold", "trp_player"),
        (ge, ":player_gold","$player_ransom_amount")
      ],"Accept the offer.",
      [
        (play_cue_track, "track_escape"),
        (assign, "$g_player_is_captive", 0),
        (troop_remove_gold, "trp_player", "$player_ransom_amount"),
        (try_begin),
          (party_is_active, "$capturer_party"),
          (party_relocate_near_party, "p_main_party", "$capturer_party", 1),
        (try_end),
        (call_script, "script_set_parties_around_player_ignore_player", 8, 12), #it was radius:2 and hours:6, but players make lots of complains about consequent battle losses after releases from captivity then I changed this.
        (assign, "$g_player_icon_state", pis_normal),
        (set_camera_follow_party, "p_main_party"),
        (rest_for_hours, 0, 0, 0), #stop resting
        (change_screen_return),
      ]),
      ("captivity_end_ransom_accept_2",
      [
        (store_troop_gold,":player_gold", "trp_player"),
        (lt, ":player_gold","$player_ransom_amount"),
      
        (try_begin),
          (store_troop_gold, ":player_gold", "trp_player"),
          (assign, reg6, ":player_gold"),
        (try_end),
      ],"Pay him {reg6} denars, promising to pay the rest when you are free.",
      [
        (play_cue_track, "track_escape"),
        (assign, "$g_player_is_captive", 0),
        
        (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
        (party_get_slot, ":guild_master_troop", "$current_town",slot_town_elder),
        
        (store_troop_gold,":player_gold", "trp_player"),
        (troop_remove_gold, "trp_player", ":player_gold"),
        (store_sub, ":new_debts", "$player_ransom_amount", ":player_gold"),
        (try_begin),
            (gt, ":town_lord", -1),
            (call_script, "script_change_debt_to_troop", ":town_lord", ":new_debts"),
        (else_try),
            (gt, ":guild_master_troop", -1),
            (call_script, "script_change_debt_to_troop", ":guild_master_troop", ":new_debts"),
        (try_end),
        
        (val_max, ":new_debts", 1),
        (val_div, ":new_debts", 200),
        (try_begin),
            (gt, ":new_debts", 0),
            (val_mul, ":new_debts", -1),
            (call_script, "script_change_troop_renown", "trp_player", ":new_debts"),
        (try_end),
        
        (try_begin),
          (party_is_active, "$capturer_party"),
          (party_relocate_near_party, "p_main_party", "$capturer_party", 1),
        (try_end),
        (call_script, "script_set_parties_around_player_ignore_player", 8, 12), #it was radius:2 and hours:6, but players make lots of complains about consequent battle losses after releases from captivity then I changed this.
        (assign, "$g_player_icon_state", pis_normal),
        (set_camera_follow_party, "p_main_party"),
        (rest_for_hours, 0, 0, 0), #stop resting
        (change_screen_return),
      ]),
      ("captivity_end_ransom_deny",
      [
      ],"Refuse him, wait for something better.",
      [
        (try_begin),
            (eq, "$g_sexual_content", 2),
            (jump_to_menu, "mnu_fucked_by_enemy_prison"),
        (else_try),
            (assign, "$g_player_is_captive", 1),
            (store_random_in_range, reg(8), 16, 22),
            (call_script, "script_stay_captive_for_hours", reg8),
            (assign,"$auto_menu", "mnu_captivity_castle_check"),
            (change_screen_return),
        (try_end),
      ]),
    ]
  ),
  (
    "captivity_castle_remain",mnf_scale_picture|mnf_disable_all_keys,
    "More days pass in the darkness of your cell. You get through them as best you can,\
 enduring the kicks and curses of the guards, watching your underfed body waste away more and more...",
    "none",
    [
		  ##diplomacy start+ test gender with script
        #(troop_get_type, ":is_female", "trp_player"),#<- replaced
        (try_begin),
          #(eq, ":is_female", 1),#<- replaced
		  (eq, "$character_gender", tf_female),#<- added
          (set_background_mesh, "mesh_pic_prisoner_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_prisoner_man"),
        (try_end),
		  ##diplomacy end+
        (store_random_in_range, ":random_hours", 16, 22),
        (call_script, "script_stay_captive_for_hours", ":random_hours"),
        (assign,"$auto_menu", "mnu_captivity_castle_check"),

    ],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 1),
           (change_screen_return),
        ]),
    ]
  ),

  (
##diplomacy end+ fix gender of pronoun
    "kingdom_army_quest_report_to_army",mnf_scale_picture,
    "{s8} sends word that {reg4?she:he} wishes you to join {reg4?her:his} new military campaign.\
 You need to bring at least {reg13} troops to the army,\
 and are instructed to raise more men with all due haste if you do not have enough.",
##diplomacy end+
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (quest_get_slot, ":quest_target_troop", "qst_report_to_army", slot_quest_target_troop),
        (quest_get_slot, ":quest_target_amount", "qst_report_to_army", slot_quest_target_amount),
        (call_script, "script_get_information_about_troops_position", ":quest_target_troop", 0),
        (str_clear, s9),
        (try_begin),
          (eq, reg0, 1), #troop is found and text is correct
          (str_store_string, s9, s1),
        (try_end),
        (str_store_troop_name, s8, ":quest_target_troop"),
        (assign, reg13, ":quest_target_amount"),
		##diplomacy start+
      #Set gender with script
		#(troop_get_type, reg4, ":quest_target_troop"), #<- OLD
		(call_script, "script_dplmc_store_troop_is_female_reg", ":quest_target_troop", 4),
		##diplomacy end+
      ],
    [
      ("continue",[],"Continue...",
       [
           (quest_get_slot, ":quest_target_troop", "qst_report_to_army", slot_quest_target_troop),
           (quest_get_slot, ":quest_target_amount", "qst_report_to_army", slot_quest_target_amount),
           (str_store_troop_name_link, s13, ":quest_target_troop"),
           (assign, reg13, ":quest_target_amount"),
           (setup_quest_text, "qst_report_to_army"),
           ##diplomacy start+ fix gender of pronoun
           (str_store_string, s2, "@{s13} asked you to report to {reg4?her:him} with at least {reg13} troops."),
           ##diplomacy end+
           (call_script, "script_start_quest", "qst_report_to_army", ":quest_target_troop"),
           (call_script, "script_report_quest_troop_positions", "qst_report_to_army", ":quest_target_troop", 3),
           (change_screen_return),
        ]),
     ]
  ),

  (
##diplomacy start+ fix gender of pronouns
    "kingdom_army_quest_messenger",mnf_scale_picture,
    "{s8} sends word that {reg4?she:he} wishes to speak with you about a task {reg4?she:he} needs performed.\
 {reg4?She:He} requests you to come and see {reg4?her:him} as soon as possible.",
##diplomacy end+
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
        ##diplomacy start+ put marshall's gender in reg4
        (call_script, "script_dplmc_store_troop_is_female", ":faction_marshall"),
        (assign, reg4, reg0),
        ##diplomacy end+
        (str_store_troop_name, s8, ":faction_marshall"),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "kingdom_army_quest_join_siege_order",mnf_scale_picture,
    "{s8} sends word that you are to join the siege of {s9} in preparation for a full assault.\
 Your troops are to take {s9} at all costs.",
    "none",
    [
		(set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
        (quest_get_slot, ":quest_target_center", "qst_join_siege_with_army", slot_quest_target_center),
        (str_store_troop_name, s8, ":faction_marshall"),
        (str_store_party_name, s9, ":quest_target_center"),
      ],
    [
      ("continue",[],"Continue...",
       [
           (call_script, "script_end_quest", "qst_follow_army"),
           (quest_get_slot, ":quest_target_center", "qst_join_siege_with_army", slot_quest_target_center),
           (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
           (str_store_troop_name_link, s13, ":faction_marshall"),
           (str_store_party_name_link, s14, ":quest_target_center"),
           (setup_quest_text, "qst_join_siege_with_army"),
           (str_store_string, s2, "@{s13} ordered you to join the assault against {s14}."),
           (call_script, "script_start_quest", "qst_join_siege_with_army", ":faction_marshall"),
           (change_screen_return),
        ]),
     ]
  ),

  (
    "kingdom_army_follow_failed",mnf_scale_picture,
    "You have failed to follow {s8}. The marshal assumes that you were otherwise engaged, but would have appreciated your support.",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
        (str_store_troop_name, s8, ":faction_marshall"),
        (call_script, "script_abort_quest", "qst_follow_army", 1),
#        (call_script, "script_change_player_relation_with_troop", ":faction_marshall", -3),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


  (
    "invite_player_to_faction_without_center",mnf_scale_picture,
##diplomacy start+ fix gender of pronouns
    "You receive an offer of vassalage!^^\
 {s8} of {s9} has sent a royal herald to bring you an invititation in {reg4?her:his} own hand.\
 You would be granted the honour of becoming a vassal {lord/lady} of {s9},\
 and in return {s8} asks you to swear an oath of homage to {reg4?her:him} and fight in {reg4?her:his} military campaigns,\
 although {reg4?she:he} offers you no lands or titles.\
 {reg4?She:He} will surely be offended if you do not take the offer...",
##diplomacy end+
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, "$g_invite_faction_lord", "$g_invite_faction", slot_faction_leader),
        ##diplomacy start+ store gender in reg4
        (call_script, "script_dplmc_store_troop_is_female", "$g_invite_faction_lord"),
        (assign, reg4, reg0),
        ##diplomacy start+
        (str_store_troop_name, s8, "$g_invite_faction_lord"),
        (str_store_faction_name, s9, "$g_invite_faction"),
      ],
    [
      ("faction_accept",[],"Accept!",
       [(str_store_troop_name,s1,"$g_invite_faction_lord"),
        (setup_quest_text,"qst_join_faction"),

        (str_store_troop_name_link, s3, "$g_invite_faction_lord"),
        (str_store_faction_name_link, s4, "$g_invite_faction"),
        (quest_set_slot, "qst_join_faction", slot_quest_giver_troop, "$g_invite_faction_lord"),
        (quest_set_slot, "qst_join_faction", slot_quest_expiration_days, 30),
		(quest_set_slot, "qst_join_faction", slot_quest_failure_consequence, 0),
	##diplomacy start+ fix gender of pronoun
        (str_store_string, s2, "@Find and speak with {s3} of {s4} to give {reg4?her:him} your oath of homage."),
        ##diplomacy end+
        (call_script, "script_start_quest", "qst_join_faction", "$g_invite_faction_lord"),
        (call_script, "script_report_quest_troop_positions", "qst_join_faction", "$g_invite_faction_lord", 3),
        (jump_to_menu, "mnu_invite_player_to_faction_accepted"),
        ]),
      ("faction_reject",[],"Decline the invitation.",
       [(call_script, "script_change_player_relation_with_troop", "$g_invite_faction_lord", -3),
        (call_script, "script_change_player_relation_with_faction", "$g_invite_faction", -10),
        (assign, "$g_invite_faction", 0),
        (assign, "$g_invite_faction_lord", 0),
        (assign, "$g_invite_offered_center", 0),
        (change_screen_return),
        ]),
     ]
  ),


  (
    "invite_player_to_faction",mnf_scale_picture,
##diplomacy start+ fix gender of pronouns
    "You receive an offer of vassalage!^^\
 {s8} of {s9} has sent a royal herald to bring you an invititation in {reg4?her:his} own hand.\
 You would be granted the honour of becoming a vassal {lord/lady} of {s9},\
 and in return {s8} asks you to swear an oath of homage to {reg4?her:him} and fight in {reg4?her:his} military campaigns,\
 offering you the fief of {s2} for your loyal service.\
 {reg4?She:He} will surely be offended if you do not take the offer...",
##diplomacy end+
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, "$g_invite_faction_lord", "$g_invite_faction", slot_faction_leader),
        ##diplomacy start+ store gender in reg4
        (call_script, "script_dplmc_store_troop_is_female", "$g_invite_faction_lord"),
        (assign, reg4, reg0),
        ##diplomacy start+
        (str_store_troop_name, s8, "$g_invite_faction_lord"),
        (str_store_faction_name, s9, "$g_invite_faction"),
        (str_store_party_name, s2, "$g_invite_offered_center"),
      ],
    [
      ("faction_accept",[],"Accept!",
       [(str_store_troop_name,s1,"$g_invite_faction_lord"),
        (setup_quest_text,"qst_join_faction"),

        (str_store_troop_name_link, s3, "$g_invite_faction_lord"),
        (str_store_faction_name_link, s4, "$g_invite_faction"),
        (quest_set_slot, "qst_join_faction", slot_quest_giver_troop, "$g_invite_faction_lord"),
        (quest_set_slot, "qst_join_faction", slot_quest_expiration_days, 30),
        ##diplomacy start+ fix gender of pronoun
        (str_store_string, s2, "@Find and speak with {s3} of {s4} to give {reg4?her:him} your oath of homage."),
        ##diplomacy end+
        (call_script, "script_start_quest", "qst_join_faction", "$g_invite_faction_lord"),
        (call_script, "script_report_quest_troop_positions", "qst_join_faction", "$g_invite_faction_lord", 3),
        (jump_to_menu, "mnu_invite_player_to_faction_accepted"),
        ]),
      ("faction_reject",[],"Decline the invitation.",
       [(call_script, "script_change_player_relation_with_troop", "$g_invite_faction_lord", -3),
        (assign, "$g_invite_faction", 0),
        (assign, "$g_invite_faction_lord", 0),
        (assign, "$g_invite_offered_center", 0),
        (change_screen_return),
        ]),
     ]
  ),

  (
    "invite_player_to_faction_accepted",0,
##diplomacy start+ fix gender of pronouns (king's gender should already be in reg4)
    "In order to become a vassal, you must swear an oath of homage to {s3}.\
 You shall have to find {reg4?her:him} and give {reg4?her:him} your oath in person. {s5}",
##diplomacy end+
    "none",
    [
        (call_script, "script_get_information_about_troops_position", "$g_invite_faction_lord", 0),
        (str_store_troop_name, s3, "$g_invite_faction_lord"),
        (str_store_string, s5, "@{!}{s1}"),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "question_peace_offer",0,
    "You Receive a Peace Offer^^The {s1} offers you a peace agreement. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),

      ##diplomacy begin
      (store_relation,  ":relation", "fac_player_supporters_faction", "$g_notification_menu_var1"),
      (try_begin),
        (ge, ":relation", 0),
        (change_screen_return),
      (try_end),
      ##diplomacy end
      ],
    [
      ("peace_offer_accept",[],"Accept",
       [
         (call_script, "script_diplomacy_start_peace_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (change_screen_return),
        ]),
        ##diplomacy begin
      ("dplmc_peace_offer_terms",[],"Dictate the peace terms",
       [
        (start_presentation, "prsnt_dplmc_peace_terms"),
        ]),
        ##diplomacy end
      ("peace_offer_reject",[],"Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -5),
         (change_screen_return),
        ]),
     ]
  ),

  (
    "notification_truce_expired",0,
    "Truce Has Expired^^The truce between {s1} and {s2} has expired.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue",
       [
	   (change_screen_return),
        ]),
     ]
  ),

  (
    "notification_feast_quest_expired",0,
    "{s10}",
    "none",
    [
    (str_store_string, s10, "str_feast_quest_expired"),
    ],
    [
      ("continue",[],"Continue",
       [
	   (change_screen_return),
        ]),
     ]
  ),

  (
    "notification_sortie_possible",0,
    "Enemy Sighted: Enemies have been sighted outside the walls of {s4}, and {s5} and others are preparing for a sortie. You may join them if you wish.",
    "none",
    [
	(str_store_party_name, s4, "$g_notification_menu_var1"),
	(party_stack_get_troop_id, ":leader", "$g_notification_menu_var2", 0),
	(str_store_troop_name, s5, ":leader"),
      ],
    [
      ("continue",[],"Continue",
       [
	   #stop auto-clock

	   (change_screen_return),
        ]),
     ]
  ),




  (
    "notification_casus_belli_expired",0,
    "Kingdom Fails to Respond^^The {s1} has not responded to the {s2}'s provocations, and {s3} suffers a loss of face among {reg4?her:his} more bellicose subjects...^",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
	  (faction_get_slot, ":faction_leader", "$g_notification_menu_var1", slot_faction_leader),
      (str_store_troop_name, s3, ":faction_leader"),
	  ##diplomacy start+ use a script for gender
	  #(troop_get_type, reg4, ":faction_leader"),#<- OLD
	  (call_script, "script_dplmc_store_troop_is_female_reg", ":faction_leader", 4),
     ##diplomacy end+

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue",
       [
	   (call_script, "script_faction_follows_controversial_policy", "$g_notification_menu_var1", logent_policy_ruler_ignores_provocation),
	   (change_screen_return),
        ]),
     ]
  ),

  (
    "notification_lord_defects",0,
##diplomacy start+ Fix gender of pronouns
    "Defection: {s4} has abandoned the {s5} and joined the {s7}, taking {reg4?her:his} fiefs with {reg4?her:him}",
##diplomacy end+
    "none",
	[
	  (assign, ":defecting_lord", "$g_notification_menu_var1"),
	  (assign, ":old_faction", "$g_notification_menu_var2"),
	  (str_store_troop_name, s4, ":defecting_lord"),
	  (str_store_faction_name, s5, ":old_faction"),
	  (store_faction_of_troop, ":new_faction", ":defecting_lord"),
	  (str_store_faction_name, s7, ":new_faction"),
	  ##diplomacy start+ get gender with script
	  #(troop_get_type, reg4, ":defecting_lord"),#<-OLD
	  (call_script, "script_dplmc_store_troop_is_female_reg", ":defecting_lord", 4),
	  ##diplomacy end+

	],
    [
      ("continue",[],"Continue",
       [
	   (change_screen_return),
        ]),
     ]
	),


  (
    "notification_treason_indictment",0,
    "Treason Indictment^^{s9}",
    "none",
    [
	  (assign, ":indicted_lord", "$g_notification_menu_var1"),
	  (assign, ":former_faction", "$g_notification_menu_var2"),
	  (faction_get_slot, ":former_faction_leader", ":former_faction", slot_faction_leader),

	  #Set up string
	  (try_begin),
			(eq, ":indicted_lord", "trp_player"),
			(str_store_troop_name, s7, ":former_faction_leader"),
			(str_store_string, s9, "str_you_have_been_indicted_for_treason_to_s7_your_properties_have_been_confiscated_and_you_would_be_well_advised_to_flee_for_your_life"),
	  (else_try),
			(str_store_troop_name_link, s4, ":indicted_lord"),
			(str_store_faction_name_link, s5, ":former_faction"),
			(str_store_troop_name_link, s6, ":former_faction_leader"),

		   ##diplomacy start+ get gender with script
			#(troop_get_type, reg4, ":indicted_lord"),#<-OLD
			(call_script, "script_dplmc_store_troop_is_female_reg", ":indicted_lord", 4),
			##diplomacy end+
			(store_faction_of_troop, ":new_faction", ":indicted_lord"),
			(try_begin),
				(is_between, ":new_faction", kingdoms_begin, kingdoms_end),
				(str_store_faction_name_link, s10, ":new_faction"),
				(str_store_string, s11, "str_with_the_s10"),
			(else_try),
				(str_store_string, s11, "str_outside_calradia"),
			(try_end),
			(str_store_string, s9, "str_by_order_of_s6_s4_of_the_s5_has_been_indicted_for_treason_the_lord_has_been_stripped_of_all_reg4herhis_properties_and_has_fled_for_reg4herhis_life_he_is_rumored_to_have_gone_into_exile_s11"),
		(try_end),


	],
    [
      ("continue",[],"Continue",
       [
	   (change_screen_return),
        ]),
     ]
	),



  (
    "notification_border_incident",0,
    "Border incident^^Word reaches you that {s9}. Though you don't know whether or not the rumors are true, you do know one thing -- this seemingly minor incident has raised passions among the {s4}, making it easier for them to go to war against the {s3}, if they want it...",
    "none",
    [
	  (assign, ":acting_village", "$g_notification_menu_var1"),
	  (assign, ":target_village", "$g_notification_menu_var2"),
	  (store_faction_of_party, ":acting_faction", ":acting_village"),

	  (try_begin),
			(eq, ":target_village", -1),
			(party_get_slot, ":target_faction", ":acting_village", slot_center_original_faction),
			(try_begin),
				(this_or_next|eq, ":target_faction", ":acting_faction"),
                              		(neg|faction_slot_eq, ":target_faction", slot_faction_state, sfs_active),
				(party_get_slot, ":target_faction", ":acting_village", slot_center_ex_faction),
			(try_end),

		    (str_store_party_name, s1, ":acting_village"),
		    (str_store_faction_name, s3, ":acting_faction"),
		    (str_store_faction_name, s4, ":target_faction"),
			(faction_get_slot, ":target_leader", ":target_faction", slot_faction_leader),
		    (str_store_troop_name, s5, ":target_leader"),

			(str_store_string, s9, "str_local_notables_from_s1_a_village_claimed_by_the_s4_have_been_mistreated_by_their_overlords_from_the_s3_and_petition_s5_for_protection"),
			(display_log_message, "@There has been an alleged border incident: {s9}"),

			(call_script, "script_add_log_entry", logent_border_incident_subjects_mistreated, ":acting_village", -1, -1, ":acting_faction"),


      (else_try),
			(store_faction_of_party, ":target_faction", ":target_village"),

		    (str_store_party_name, s1, ":acting_village"),
		    (str_store_party_name, s2, ":target_village"),

			(store_random_in_range, ":random", 0, 3),
			(try_begin),
				(eq, ":random", 0),

				(str_store_string, s9, "str_villagers_from_s1_stole_some_cattle_from_s2"),
				(display_log_message, "@There has been an alleged border incident: {s9}"),

				(call_script, "script_add_log_entry", logent_border_incident_cattle_stolen, ":acting_village", ":target_village", -1,":acting_faction"),

			(else_try),
				(eq, ":random", 1),

				(str_store_string, s9, "str_villagers_from_s1_abducted_a_woman_from_a_prominent_family_in_s2_to_marry_one_of_their_boys"),
				(display_log_message, "@There has been an alleged border incident: {s9}"),

				(call_script, "script_add_log_entry", logent_border_incident_bride_abducted, ":acting_village", ":target_village", -1, ":acting_faction"),
			(else_try),
				(eq, ":random", 2),

				(str_store_string, s9, "str_villagers_from_s1_killed_some_farmers_from_s2_in_a_fight_over_the_diversion_of_a_stream"),
				(display_log_message, "@There has been an alleged border incident: {s9}"),

			    (call_script, "script_add_log_entry", logent_border_incident_villagers_killed, ":acting_village", ":target_village", -1,":acting_faction"),
			(try_end),

	  (try_end),

	  (str_store_faction_name, s3, ":acting_faction"),
	  (str_store_faction_name, s4, ":target_faction"),

	  (store_add, ":slot_provocation_days", ":acting_faction", slot_faction_provocation_days_with_factions_begin),
	  (val_sub, ":slot_provocation_days", kingdoms_begin),
	  (faction_set_slot, ":target_faction", ":slot_provocation_days", 30),

      ],
    [
      ("continue",[],"Continue",
       [
	   (change_screen_return),
        ]),
     ]
  ),




  (
    "notification_player_faction_active",0,
    "You now possess land in your name, without being tied to any kingdom. This makes you a monarch in your own right, with your court temporarily located at {s12}. However, the other kings in Calradia will at first consider you a threat, for if any upstart warlord can grab a throne, then their own legitimacy is called into question.^^You may find it desirable at this time to pledge yourself to an existing kingdom. If you want to continue as a sovereign monarch, then your first priority should be to establish an independent right to rule. You can establish your right to rule through several means -- marrying into a high-born family, recruiting new lords, governing your lands, treating with other kings, or dispatching your companions on missions.^^At any rate, your first step should be to appoint a chief minister from among your companions, to handle affairs of state. Different companions have different capabilities.^You may appoint new ministers from time to time. You may also change the location of your court, by speaking to the minister.",
    "none",
    [
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", pos0),

      (unlock_achievement, ACHIEVEMENT_CALRADIAN_TEA_PARTY),
      (play_track, "track_coronation"),

	  (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
	    (lt, "$g_player_court", walled_centers_begin),
		(store_faction_of_party, ":walled_center_faction", ":walled_center"),
	    (eq, ":walled_center_faction", "fac_player_supporters_faction"),
		(assign, "$g_player_court", ":walled_center"),

		##diplomacy start+
		#OLD VERSION:
		#(try_begin),
		#	(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
		#	(is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
		#	(troop_set_slot, ":spouse", slot_troop_cur_center, "$g_player_court"),
		#(try_end),
		#
		#NEW VERSION:
		#For settings with polygamy, check all kingdom ladies to see if they are wives.
		#Also move unmarried daughters/sisters of the player if they exist (they cannot
		#in Native, but might in mods).
		(try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
			#Make sure the spouse hasn't been promoted, and is not a prisoner, and is not exiled/dead
			(troop_slot_eq, ":lady", slot_troop_occupation, slto_kingdom_lady),
			(neg|troop_slot_ge, ":lady", slot_troop_leaded_party, 0),
			#Make sure the lady isn't a prisoner
			(neg|troop_slot_ge, ":lady", slot_troop_prisoner_of_party, 0),
            (neg|main_party_has_troop, ":lady"),
			(try_begin),
				#Check if the lady is the player's spouse
				(this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, ":lady"),
					(troop_slot_eq, ":lady", slot_troop_spouse, "trp_player"),
				#Update location
				(troop_set_slot, ":lady", slot_troop_cur_center, "$g_player_court"),
			(else_try),
				#If the lady is unmarried, check if she is the player's dependent.
				(troop_slot_eq, ":lady", slot_troop_spouse, -1),
				(this_or_next|troop_slot_eq, ":lady", slot_troop_father, "trp_player"),
				(this_or_next|troop_slot_eq, ":lady", slot_troop_mother, "trp_player"),
					(troop_slot_eq, ":lady", slot_troop_guardian, "trp_player"),
				#Update location
				(troop_set_slot, ":lady", slot_troop_cur_center, "$g_player_court"),
			(try_end),
		(try_end),
		##diplomacy end+

		(str_store_party_name, s12, "$g_player_court"),
	  (try_end),

      ],
    [
	  ##diplomacy start+
	  #Make compatible with polygamy
      ("appoint_spouse",[
	  (troop_slot_ge, "trp_player", slot_troop_spouse, 1),
	  (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
	  (neg|troop_slot_eq, ":player_spouse", slot_troop_occupation, slto_kingdom_hero),
	  ##diplomacy start+
	  #Also do not appoint the missing or the dead
	  (neg|troop_slot_ge, ":player_spouse", slot_troop_occupation, slto_retirement),
	  (call_script, "script_dplmc_store_troop_is_female", ":player_spouse"),#reg0 make gender-correct
	  ##diplomacy end+
	  (str_store_troop_name, s10, ":player_spouse"),
	  ],"Appoint your {reg0?wife:husband}, {s10}...",
       [
	   (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
	   (assign, "$g_player_minister", ":player_spouse"),
	   (jump_to_menu, "mnu_minister_confirm"),
	   ]),
	  ##diplomacy end+

	  ##diplomacy start+
	  #Check for one additional spouse (polygamy may be enabled)
      ("dplmc_appoint_spouse_plus_1",[
	  (troop_slot_ge, "trp_player", slot_troop_spouse, 1),
	  (assign, ":player_spouse", -1),
	  (try_for_range_backwards, ":troop_no", heroes_begin, heroes_end),#Go backwards to ensure we end with the first match
		(troop_slot_eq, ":troop_no", slot_troop_spouse, "trp_player"),
		(neg|troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_no"),#Not ordinary spouse
		(neg|troop_slot_ge, ":troop_no", slot_troop_occupation, slto_retirement),#Not retired/dead/exiled
		(neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),#Not leading a party
		(assign, ":player_spouse", ":troop_no"),
	  (try_end),
	  (ge, ":player_spouse", 1),
	  (call_script, "script_dplmc_store_troop_is_female", ":player_spouse"),
	  (str_store_troop_name, s10, ":player_spouse"),
	  ],"Appoint your {reg0?wife:husband}, {s10}...",
       [
	   (assign, ":player_spouse", -1),
	   (try_for_range_backwards, ":troop_no", heroes_begin, heroes_end),#Go backwards to ensure we end with the first match
	     (troop_slot_eq, ":troop_no", slot_troop_spouse, "trp_player"),
		 (neg|troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_no"),#Not ordinary spouse
		 (neg|troop_slot_ge, ":troop_no", slot_troop_occupation, slto_retirement),#Not retired/dead/exiled
		 (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),#Not leading a party
		 (assign, ":player_spouse", ":troop_no"),
	   (try_end),
	   (try_begin),
		  (lt, ":player_spouse", 1),#This shouldn't be possible
		  (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
	   (try_end),

	   (assign, "$g_player_minister", ":player_spouse"),
	   (jump_to_menu, "mnu_minister_confirm"),
	   ]),
	  ##diplomacy end+
      ]+
      
    #SB : roll into loop
      [("appoint_npc"+str(x), [
      (main_party_has_troop, "trp_npc"+str(x)),
      (str_store_troop_name, s10, "trp_npc"+str(x)),
      ],"Appoint {s10}", [
       (assign, "$g_player_minister", "trp_npc"+str(x)),
       (jump_to_menu, "mnu_minister_confirm"),
      ]) for x in range (1, 17)]
      
    +[
      ("appoint_default",[],"Appoint a prominent citizen from the area...",
       [
	   (assign, "$g_player_minister", "trp_temporary_minister"),
	   (troop_set_faction, "trp_temporary_minister", "fac_player_supporters_faction"),
	   (jump_to_menu, "mnu_minister_confirm"),
        ]),
     ]
  ),

  (
    "minister_confirm",0,
    "{s9}can be found at your court in {s12}. You should consult {reg4?her:him} periodically, to avoid the accumulation of unresolved issues that may sap your authority...",
    "none",
    [
    (try_begin),
        (store_and, ":name_set", "$players_kingdom_name_set", rename_kingdom),
        (eq, ":name_set", rename_kingdom),
        (change_screen_return),
    (try_end),

	(try_begin),
		(eq, "$g_player_minister", "trp_temporary_minister"),
		(str_store_string, s9, "str_your_new_minister_"),
	(else_try),
		(str_store_troop_name, s10, "$g_player_minister"),
		(str_store_string, s9, "str_s10_is_your_new_minister_and_"),
	(try_end),

	(try_begin),
		(main_party_has_troop, "$g_player_minister"),
		(remove_member_from_party, "$g_player_minister", "p_main_party"),
	(try_end),
    
    #SB : tableau notes
    (set_fixed_point_multiplier, 100),
    (position_set_x, pos0, 70),
    (position_set_y, pos0, 5),
    (position_set_z, pos0, 75),
    (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$g_player_minister", pos0),
    #also gender string
    (call_script, "script_dplmc_store_troop_is_female_reg", "$g_player_minister", 4),
	],
    [
      ("continue",[],"Continue...",
       [
         #SB : explicitly state kingdom
         (assign, "$g_presentation_state", rename_kingdom),
         (start_presentation, "prsnt_name_kingdom"),
        ]),
     ]
  ),



  (
  "notification_court_lost",0,
  "{s12}",
  "none",
  [
    (try_begin),
		(is_between, "$g_player_court", centers_begin, centers_end),
		(str_store_party_name, s10, "$g_player_court"),
		(str_store_party_name, s11, "$g_player_court"),
	(else_try),
		(str_store_string, s10, "str_your_previous_court_some_time_ago"),
		(str_store_string, s11, "str_your_previous_court_some_time_ago"),
	(try_end),

	##diplomacy start+ Handle player is co-ruler of NPC kingdom
	(assign, ":alt_faction", "fac_player_supporters_faction"),
	(try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":alt_faction", "$players_kingdom"),
	(try_end),
	##diplomacy end+

    (try_begin), #SB : loss of court = loss of right to rule
      (store_and, ":name_set", "$players_kingdom_name_set", rename_center),
      (eq, ":name_set", rename_center),
      (call_script, "script_change_player_right_to_rule", -20),
      #the old "capital" should be stored so that this penalty does not apply twice
      #but we'll let the player name a new center
      (val_sub, "$players_kingdom_name_set", rename_center),
    (else_try), #need a court to lose one
      (is_between, "$g_player_court", centers_begin, centers_end),
      (call_script, "script_change_player_right_to_rule", -5),
    (try_end),
    (assign, "$g_player_court", -1),
	(str_store_string, s14, "str_after_to_the_fall_of_s11_your_court_has_nowhere_to_go"),
	(try_begin),
		##diplomacy start+  Handle player is co-ruler of NPC kingdom
		(this_or_next|neg|is_between, ":alt_faction", npc_kingdoms_begin, npc_kingdoms_end),
			(neg|faction_slot_eq, ":alt_faction", slot_faction_state, sfs_active),
		##diplomacy end+
		(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
		(str_store_string, s14, "str_as_you_no_longer_maintain_an_independent_kingdom_you_no_longer_maintain_a_court"),
	(try_end),

	(try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
		(eq, "$g_player_court", -1),
    ##diplomacy begin
    (neg|party_slot_eq, ":walled_center", slot_village_infested_by_bandits, "trp_peasant_woman"),
    ##diplomacy end
		(store_faction_of_party, ":walled_center_faction", ":walled_center"),
		##diplomacy start+ Handle player is co-ruler of NPC kingdom
		(this_or_next|eq, ":alt_faction", ":walled_center_faction"),
		##diplomacy end+
		(eq, ":walled_center_faction", "fac_player_supporters_faction"),
		(neg|party_slot_ge, ":walled_center", slot_town_lord, active_npcs_begin),

		(assign, "$g_player_court", ":walled_center"),
		(try_begin),
			(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
			(is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
			##diplomacy start+ Check that the spouse is not a hero, imprisoned (except by the player), or exiled/dead/etc.
            (try_begin),
                (neg|troop_slot_eq, ":spouse", slot_troop_occupation, slto_kingdom_hero),
                (neg|troop_slot_ge, ":spouse", slot_troop_occupation, slto_retirement),
                (neg|troop_slot_ge, ":spouse", slot_troop_prisoner_of_party, 1),
                ##diplomacy end+
                (neg|main_party_has_troop,":spouse"),
                (troop_set_slot, ":spouse", slot_troop_cur_center, "$g_player_court"),
            (try_end),
			(str_store_party_name, s11, "$g_player_court"),
		(try_end),

		(str_store_string, s14, "str_due_to_the_fall_of_s10_your_court_has_been_relocated_to_s12"), #actually s11
	(try_end),

	(try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
		(eq, "$g_player_court", -1),

		(store_faction_of_party, ":walled_center_faction", ":walled_center"),
		##diplomacy start+ Handle player is co-ruler of NPC kingdom
		(this_or_next|eq, ":alt_faction", ":walled_center_faction"),
		##diplomacy end+
		(eq, ":walled_center_faction", "fac_player_supporters_faction"),

		(assign, "$g_player_court", ":walled_center"),

		(try_begin),
			(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
			(is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
			##diplomacy start+ Check that the spouse is not a hero, imprisoned (except by the player), or exiled/dead/etc.
			(neg|troop_slot_eq, ":spouse", slot_troop_occupation, slto_kingdom_hero),
			(neg|troop_slot_ge, ":spouse", slot_troop_occupation, slto_retirement),
			(neg|troop_slot_ge, ":spouse", slot_troop_prisoner_of_party, 1),
			##diplomacy end+
			(troop_set_slot, ":spouse", slot_troop_cur_center, "$g_player_court"),
		(try_end),

		(party_get_slot, ":town_lord", ":walled_center", slot_town_lord),
		(str_store_party_name, s11, "$g_player_court"),
		(str_store_troop_name, s9, ":town_lord"),
		(str_store_string, s14, "str_after_to_the_fall_of_s10_your_faithful_vassal_s9_has_invited_your_court_to_s11_"),
	(try_end),

	(try_begin),
		##diplomacy start+  Handle player is co-ruler of NPC kingdom
		(this_or_next|neg|is_between, ":alt_faction", npc_kingdoms_begin, npc_kingdoms_end),
			(neg|faction_slot_eq, ":alt_faction", slot_faction_state, sfs_active),
		##diplomacy end+
		(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
		(str_store_string, s14, "str_as_you_no_longer_maintain_an_independent_kingdom_you_no_longer_maintain_a_court"),
	(try_end),
	(str_store_string, s12, s14),
  ],
  [
      ("continue",[],"Continue...",[
	  (change_screen_return),
	  ]),
     ],
  ),



  (
    "notification_player_faction_deactive",0,
    "Your kingdom no longer holds any land.",
    "none",
    [
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [
       (assign, "$g_player_minister", -1),
       (change_screen_return),
        ]),
     ]
  ),






  (
    "notification_player_wedding_day",mnf_scale_picture,
    "{s8} wishes to inform you that preparations for your wedding at {s10} have been complete, and that your presence is expected imminently .",
    "none",
    [
		(set_background_mesh, "mesh_pic_messenger"),
		(str_store_troop_name, s8, "$g_notification_menu_var1"),
		(str_store_party_name, s10, "$g_notification_menu_var2"),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


  (
    "notification_player_kingdom_holds_feast",mnf_scale_picture,
    "{s11}",
    "none",
    [
		(set_background_mesh, "mesh_pic_messenger"),

		(str_store_troop_name, s8, "$g_notification_menu_var1"),
		(store_faction_of_troop, ":host_faction", "$g_notification_menu_var1"),
		(str_store_faction_name, s9, ":host_faction"),

#		(str_store_faction_name, s9, "$players_kingdom"),
		(str_store_party_name, s10, "$g_notification_menu_var2"),

		(str_clear, s12),
		(try_begin),
			(check_quest_active, "qst_wed_betrothed"),
			(quest_get_slot, ":giver_troop", "qst_wed_betrothed", slot_quest_giver_troop),
			(store_faction_of_troop, ":giver_troop_faction", ":giver_troop"),
			(eq, ":giver_troop_faction", "$players_kingdom"),
			(str_store_string, s12, "str_feast_wedding_opportunity"),
		(try_end),



		(str_store_string, s11, "str_s8_wishes_to_inform_you_that_the_lords_of_s9_will_be_gathering_for_a_feast_at_his_great_hall_in_s10_and_invites_you_to_be_part_of_this_august_assembly"),
		(try_begin),
			(eq, "$g_notification_menu_var1", 0),
			(str_store_string, s11, "str_the_great_lords_of_your_kingdom_plan_to_gather_at_your_hall_in_s10_for_a_feast"),
		(try_end),
		(str_store_string, s11, "@{!}{s11}{s12}"),

		(try_begin),
			(ge, "$cheat_mode", 1),
			(store_current_hours, ":hours_since_last_feast"),
			(faction_get_slot, ":last_feast_start_time", "$players_kingdom", slot_faction_last_feast_start_time),
			(val_sub, ":hours_since_last_feast", ":last_feast_start_time"),
			(assign, reg4, ":hours_since_last_feast"),
			(display_message, "@{!}DEBUG -- Hours since last feast started: {reg4}"),
		(try_end),

      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


  (
    "notification_center_under_siege",0,
    "{s1} has been besieged by {s2} of {s3}!",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_troop_name, s2, "$g_notification_menu_var2"),
      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
      (str_store_faction_name, s3, ":troop_faction"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_village_raided",0,
    "Enemies have Laid Waste to a Fief^^{s1} has been raided by {s2} of {s3}!",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_troop_name, s2, "$g_notification_menu_var2"),
      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
      (str_store_faction_name, s3, ":troop_faction"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_village_raid_started",0,
    "Your Village is under Attack!^^{s2} of {s3} is laying waste to {s1}.",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_troop_name, s2, "$g_notification_menu_var2"),
      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
      (str_store_faction_name, s3, ":troop_faction"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_one_faction_left",0,
    "Calradia Conquered by One Kingdom^^{s1} has defeated all rivals and stands as the sole kingdom.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
	  (try_begin),
		(faction_slot_eq, "$g_notification_menu_var1", slot_faction_leader, "trp_player"),
		(unlock_achievement, ACHIEVEMENT_THE_GOLDEN_THRONE),
	  (else_try),
		(unlock_achievement, ACHIEVEMENT_MANIFEST_DESTINY),
	  (try_end),

        (try_begin),
            (troop_get_type, ":is_female", "trp_player"),
            (eq, ":is_female", 1),
            (unlock_achievement, ACHIEVEMENT_EMPRESS),
        (try_end),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_oath_renounced_faction_defeated",0,
    "Your Old Faction was Defeated^^You won the battle against {s1}! This ends your struggle which started after you renounced your oath to them.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_center_lost",0,
    "An Estate was Lost^^You have lost {s1} to {s2}.",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


  (
    "notification_troop_left_players_faction",0,
    "Betrayal!^^{s1} has left {s2} and joined {s3}.",
    "none",
    [
      (str_store_troop_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$players_kingdom"),
      (str_store_faction_name, s3, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 55),
      (position_set_y, pos0, 20),
      (position_set_z, pos0, 100),
      (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_troop_joined_players_faction",0,
    "Good news!^^ {s1} has left {s2} and joined {s3}.",
    "none",
    [
      (str_store_troop_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (str_store_faction_name, s3, "$players_kingdom"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 55),
      (position_set_y, pos0, 20),
      (position_set_z, pos0, 100),
      (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_war_declared",0,
    "Declaration of War^^{s1} has declared war against {s2}!",
    "none",
    [

#	  (try_begin),
#		(eq, "$g_include_diplo_explanation", "$g_notification_menu_var1"),
#		(assign, "$g_include_diplo_explanation", 0),
#		(str_store_string, s57, "$g_notification_menu_var1"),
#	  (else_try),
#	    (str_clear, s57),
#	  (try_end),


	#to do the reason, have war_damage = 0 yield pre-war reasons
      (try_begin),
#        (eq, "$g_notification_menu_var1", "fac_player_supporters_faction"),
#        (str_store_faction_name, s1, "$g_notification_menu_var2"),
#        (str_store_string, s2, "@you"),
#      (else_try),
#        (eq, "$g_notification_menu_var2", "fac_player_supporters_faction"),
#        (str_store_faction_name, s1, "$g_notification_menu_var1"),
#        (str_store_string, s2, "@you"),
#      (else_try),
        (str_store_faction_name, s1, "$g_notification_menu_var1"),
        (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (try_end),


      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_peace_declared",0,
    "Peace Agreement^^{s1} and {s2} have made peace!^{s57}",
    "none",
    [

	  (try_begin),
		(eq, 1, 0), #Alas, this does not seem to work
		(eq, "$g_include_diplo_explanation", "$g_notification_menu_var1"),
		(assign, "$g_include_diplo_explanation", 0),
	  (else_try),
	    (str_clear, s57),
	  (try_end),

	  (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


  (
    "notification_faction_defeated",0,
    "Faction Eliminated^^{s1} is no more!",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", npc_kingdoms_begin, kingdoms_end), #Excluding player kingdom
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      ],
    [
      ("continue",[],"Continue...",
       [
         (try_begin),
           (is_between, "$supported_pretender", pretenders_begin, pretenders_end),
           (troop_slot_eq, "$supported_pretender", slot_troop_original_faction, "$g_notification_menu_var1"),

           #All rebels switch to kingdom
           (try_for_range, ":cur_troop", heroes_begin, heroes_end),
             (this_or_next|troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
             (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_lady),
             (store_troop_faction, ":cur_faction", ":cur_troop"),
             (eq, ":cur_faction", "fac_player_supporters_faction"),
             (troop_set_faction, ":cur_troop", "$g_notification_menu_var1"),
             (call_script, "script_troop_set_title_according_to_faction", ":cur_troop", "$g_notification_menu_var1"),
             (try_begin),
               (this_or_next|eq, "$g_notification_menu_var1", "$players_kingdom"),
               (eq, "$g_notification_menu_var1", "fac_player_supporters_faction"),
               (call_script, "script_check_concilio_calradi_achievement"),
             (try_end),
           (else_try), #all loyal lords gain a small bonus with the player
             (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
             (store_troop_faction, ":cur_faction", ":cur_troop"),
             (eq, ":cur_faction", "$g_notification_menu_var1"),
             (call_script, "script_troop_change_relation_with_troop", ":cur_troop", "trp_player", 5),
           (try_end),

           (try_for_parties, ":cur_party"),
             (store_faction_of_party, ":cur_faction", ":cur_party"),
             (eq, ":cur_faction", "fac_player_supporters_faction"),
             (party_set_faction, ":cur_party", "$g_notification_menu_var1"),
           (try_end),

           (assign, "$players_kingdom", "$g_notification_menu_var1"),
           (try_begin),
            (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
            (is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
            (troop_set_faction, ":spouse", "$g_notification_menu_var1"),
           (try_end),


           (call_script, "script_add_notification_menu", "mnu_notification_rebels_switched_to_faction", "$g_notification_menu_var1", "$supported_pretender"),

           (faction_set_slot, "$g_notification_menu_var1", slot_faction_state, sfs_active),
           (faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),

           (faction_get_slot, ":old_leader", "$g_notification_menu_var1", slot_faction_leader),
           #(troop_set_slot, ":old_leader", slot_troop_change_to_faction, "fac_commoners"),
           (call_script, "script_change_troop_faction", ":old_leader", "fac_commoners"), #dckplmc - prevent possible respawn before actual faction changes
           #SB : renown loss of under 25%
           (troop_get_slot, ":old_renown", ":old_leader", slot_troop_renown),
           (store_random_in_range, ":renown_loss", 10, 25),
           (val_mul, ":renown_loss", ":old_renown"),
           (val_div, ":renown_loss", 100),
           (val_sub, ":old_renown", ":renown_loss"),
           (troop_set_slot, ":old_leader", slot_troop_renown, ":old_renown"),

           (faction_set_slot, "$g_notification_menu_var1", slot_faction_leader, "$supported_pretender"),
           (troop_set_faction, "$supported_pretender", "$g_notification_menu_var1"),

           (faction_get_slot, ":old_marshall", "$g_notification_menu_var1", slot_faction_marshall),
           (try_begin),
             (ge, ":old_marshall", 0),
             (troop_get_slot, ":old_marshall_party", ":old_marshall", slot_troop_leaded_party),
             (party_is_active, ":old_marshall_party"),
             (party_set_marshal, ":old_marshall_party", 0),
           (try_end),

           (faction_set_slot, "$g_notification_menu_var1", slot_faction_marshall, "trp_player"),
           (faction_set_slot, "$g_notification_menu_var1", slot_faction_ai_state, sfai_default),
           (faction_set_slot, "$g_notification_menu_var1", slot_faction_ai_object, -1),
           (troop_set_slot, "$supported_pretender", slot_troop_occupation, slto_kingdom_hero),
           (call_script, "script_change_troop_renown", "$supported_pretender", 1000), #SB : keep existing renown
           (val_div, ":renown_loss", 2), #and add to it half of what old king lost
           (call_script, "script_change_troop_renown", "$supported_pretender", ":renown_loss"), 
           # (troop_set_slot, "$supported_pretender", slot_troop_renown, 1000),

           (party_remove_members, "p_main_party", "$supported_pretender", 1),
           (call_script, "script_troop_set_title_according_to_faction", "$supported_pretender", "$g_notification_menu_var1"),
           (troop_set_auto_equip, "$supported_pretender",1), #SB : diplomacy suggestion: claimants
           (call_script, "script_set_player_relation_with_faction", "$g_notification_menu_var1", 12), #dckplmc
           (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
             (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
             (neq, ":cur_kingdom", "$g_notification_menu_var1"),
             (store_relation, ":reln", ":cur_kingdom", "fac_player_supporters_faction"),
             (set_relation, ":cur_kingdom", "$g_notification_menu_var1", ":reln"),
           (try_end),
           (assign, "$supported_pretender", 0),
           (assign, "$supported_pretender_old_faction", 0),
           (assign, "$g_recalculate_ais", 1),
           (call_script, "script_update_all_notes"),
         (try_end),
         (change_screen_return),
        ]),
     ]
  ),


  (
    "notification_rebels_switched_to_faction",0,
    "Rebellion Success^^ Your rebellion is victorious! Your faction now has the sole claim to the title of {s11}, with {s12} as the single ruler.",
    "none",
    [
      (str_store_faction_name, s11, "$g_notification_menu_var1"),
      (str_store_troop_name, s12, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", npc_kingdoms_begin, kingdoms_end), #Excluding player kingdom
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      ],
    [
      ("continue",[],"Continue...",
       [
         (assign, "$talk_context", tc_rebel_thanks),
         (start_map_conversation, "$g_notification_menu_var2", -1),
         (change_screen_return),
        ]),
     ]
  ),


  (
    "notification_player_should_consult",0,
##diplomacy start+ Replace "Your minister" with "{reg0?Your minister:{s11}}" and "him" with "{reg4?her:him}".
#Also "sends words" to "sends word"
    "{reg0?Your minister:{s11}} send word that there are problems brewing in the realm which, if left untreated, could sap your authority. You should consult with {reg4?her:him} at your earliest convenience",
	##diplomacy end+
    "none",
    [
      ],
    [
      ("continue",[],"Continue...",
       [
	    (setup_quest_text, "qst_consult_with_minister"),

        (str_store_troop_name, s11, "$g_player_minister"),
        (str_store_party_name, s12, "$g_player_court"),

		(str_store_string, s2, "str_consult_with_s11_at_your_court_in_s12"),
	    (call_script, "script_start_quest", "qst_consult_with_minister", -1),
		##diplomacy start+ Set minister gender and reg0 for generic vs specific
		(assign, reg4, 0),
		(try_begin),
			(call_script, "script_cf_dplmc_troop_is_female", "$g_player_minister"),
			(assign, reg4, 1),
		(try_end),
		(assign, reg0, 1),
		(try_begin),
			(is_between, "$g_player_minister", heroes_begin, heroes_end),
			(assign, reg0, 0),
		(try_end),
		##diplomacy end+

		(quest_set_slot, "qst_consult_with_minister", slot_quest_expiration_days, 30),
		(quest_set_slot, "qst_consult_with_minister", slot_quest_giver_troop, "$g_player_minister"),


	    (change_screen_return),
        ]),
     ]
  ),







  (
    "notification_player_feast_in_progress",0,
##diplomacy start+ make gender correct
    "Feast in Preparation^^Your {wife/husband} has started preparations for a feast in your hall in {s11}",
##diplomacy end+
    "none",
    [
    (str_store_party_name, s11, "$g_notification_menu_var1"),
    ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


  (
    "notification_lady_requests_visit",0, #add this once around seven days after the last visit, or three weeks, or three months
    "An elderly woman approaches your party and passes one of your men a letter, sealed in plain wax. It is addressed to you. When you break the seal, you see it is from {s15}. It reads, 'I so enjoyed your last visit. {s14} I am currently in {s10}.{s12}'",
    "none",
    [

      (assign, ":lady_no", "$g_notification_menu_var1"),
      (assign, ":center_no", "$g_notification_menu_var2"),

      (str_store_troop_name, s15, ":lady_no"),
      (str_store_party_name, s10, ":center_no"),

      (store_current_hours, ":hours_since_last_visit"),
      (troop_get_slot, ":last_visit_hours", ":lady_no", slot_troop_last_talk_time),
      (val_sub, ":hours_since_last_visit", ":last_visit_hours"),

      (call_script, "script_get_kingdom_lady_social_determinants", ":lady_no"),
      (assign, ":lady_guardian", reg0),

      (str_store_troop_name, s16, ":lady_guardian"),
      (call_script, "script_troop_get_family_relation_to_troop", ":lady_guardian", ":lady_no"),

      (str_clear, s14),
      (try_begin),
        (lt, ":hours_since_last_visit", 336),
        (try_begin),
            (troop_slot_eq, ":lady_no", slot_lord_reputation_type, lrep_otherworldly),
            (str_store_string, s14, "str_as_brief_as_our_separation_has_been_the_longing_in_my_heart_to_see_you_has_made_it_seem_as_many_years"),
        (else_try),
            (str_store_string, s14, "str_although_it_has_only_been_a_short_time_since_your_departure_but_i_would_be_most_pleased_to_see_you_again"),
        (try_end),
      (else_try),
        (ge, ":hours_since_last_visit", 336),
        (try_begin),
            (troop_slot_eq, ":lady_no", slot_lord_reputation_type, lrep_ambitious),
            (str_store_string, s14, "str_although_i_have_received_no_word_from_you_for_quite_some_time_i_am_sure_that_you_must_have_been_very_busy_and_that_your_failure_to_come_see_me_in_no_way_indicates_that_your_attentions_to_me_were_insincere_"),
        (else_try),
            (troop_slot_eq, ":lady_no", slot_lord_reputation_type, lrep_moralist),
            (str_store_string, s14, "str_i_trust_that_you_have_comported_yourself_in_a_manner_becoming_a_gentleman_during_our_long_separation_"),
        (else_try),
            (str_store_string, s14, "str_it_has_been_many_days_since_you_came_and_i_would_very_much_like_to_see_you_again"),
        (try_end),
      (try_end),


      (str_clear, s12),
      (str_clear, s18),
      ##diplomacy start+ Store gender in register for use below
      (assign, ":save_reg4", reg4),
      (call_script, "script_dplmc_store_troop_is_female_reg", ":lady_guardian", 4),
      ##diplomacy end+
      (try_begin),
        (troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, 0),
        (str_store_string, s12, "str__you_should_ask_my_s11_s16s_permission_but_i_have_no_reason_to_believe_that_he_will_prevent_you_from_coming_to_see_me"),
        (str_store_string, s18, "str__you_should_first_ask_her_s11_s16s_permission"),
      (else_try),
        (troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, -1),
        (str_store_string, s12, "str__alas_as_we_know_my_s11_s16_will_not_permit_me_to_see_you_however_i_believe_that_i_can_arrange_away_for_you_to_enter_undetected"),
      (else_try),
        (troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, 1),
        (str_store_string, s12, "str__as_my_s11_s16_has_already_granted_permission_for_you_to_see_me_i_shall_expect_your_imminent_arrival"),
      (try_end),
      ##diplomacy start+ Revert register
      (assign, reg4, ":save_reg4"),
      ##diplomacy end+
      
      #SB : add tableau for lady
      (set_fixed_point_multiplier, 100),
      (init_position, pos0),
      (position_set_x, pos0, 60),
      (position_set_y, pos0, 20),
      (position_set_z, pos0, 100),
      (set_game_menu_tableau_mesh, "tableau_dplmc_lord_profile", ":lady_no", pos0),
      ],
    [

      ("continue",[],"Tell the woman to inform her mistress that you will come shortly",
       [

        (assign, ":lady_to_visit", "$g_notification_menu_var1"),
        (str_store_troop_name_link, s3, ":lady_to_visit"),
        (str_store_party_name_link, s4, "$g_notification_menu_var2"),

        (str_store_string, s2, "str_visit_s3_who_was_last_at_s4s18"),
        (call_script, "script_start_quest", "qst_visit_lady", ":lady_to_visit"),
        (quest_set_slot, "qst_visit_lady", slot_quest_giver_troop, ":lady_to_visit"), #don't know why this is necessary

        (try_begin),
            (eq, "$cheat_mode", 1),
            (quest_get_slot, ":giver_troop", "qst_visit_lady", slot_quest_giver_troop),
            (str_store_troop_name, s2, ":giver_troop"),
            (display_message, "str_giver_troop_=_s2"),
        (try_end),

        (quest_set_slot, "qst_visit_lady", slot_quest_expiration_days, 30),
        (change_screen_return),
        ]),

      ("continue",[],"Tell the woman to inform her mistress that you are indisposed",
       [
        (troop_set_slot, "$g_notification_menu_var1", slot_lady_no_messages, 1),
        (change_screen_return),
        ]),
     ]
  ),



  ( #pre lady visit
    "garden",0,
    "{s12}",
    "none",
    [

    (call_script, "script_get_kingdom_lady_social_determinants", "$love_interest_in_town"),
	(assign, ":guardian_lord", reg0),
	(str_store_troop_name, s11, "$love_interest_in_town"),

	(try_begin),
		(call_script, "script_npc_decision_checklist_male_guardian_assess_suitor", ":guardian_lord", "trp_player"),
		(lt, reg0, 0),
		(troop_set_slot, ":guardian_lord", slot_lord_granted_courtship_permission, -1),
	(try_end),

	(assign, "$nurse_assists_entry", 0),
	(try_begin),
		(troop_slot_eq, ":guardian_lord", slot_lord_granted_courtship_permission, 1),
		(str_store_string, s12, "str_the_guards_at_the_gate_have_been_ordered_to_allow_you_through_you_might_be_imagining_things_but_you_think_one_of_them_may_have_given_you_a_wink"),
	(else_try), #the circumstances under which the lady arranges for a surreptitious entry
		(call_script, "script_troop_get_relation_with_troop", "trp_player", "$love_interest_in_town"),
		(gt, reg0, 0),

		(assign, ":player_completed_quest", 0),
		(try_begin),
			(check_quest_active, "qst_visit_lady"),
			(quest_slot_eq, "qst_visit_lady", slot_quest_giver_troop, "$love_interest_in_town"),
			(assign, ":player_completed_quest", 1),
		(else_try),
			(check_quest_active, "qst_formal_marriage_proposal"),
			(quest_slot_eq, "qst_formal_marriage_proposal", slot_quest_giver_troop, "$love_interest_in_town"),
			(this_or_next|check_quest_succeeded, "qst_formal_marriage_proposal"),
				(check_quest_failed, "qst_formal_marriage_proposal"),
			(assign, ":player_completed_quest", 1),
		(else_try),
			(check_quest_active, "qst_duel_courtship_rival"),
			(quest_slot_eq, "qst_duel_courtship_rival", slot_quest_giver_troop, "$love_interest_in_town"),
			(this_or_next|check_quest_succeeded, "qst_duel_courtship_rival"),
				(check_quest_failed, "qst_duel_courtship_rival"),
			(assign, ":player_completed_quest", 1),
		(try_end),

		(try_begin),
			(store_current_hours, ":hours_since_last_visit"),
			(troop_get_slot, ":last_visit_time", "$love_interest_in_town", slot_troop_last_talk_time),
			(val_sub, ":hours_since_last_visit", ":last_visit_time"),
			(this_or_next|ge, ":hours_since_last_visit", 96), #at least four days
				(eq, ":player_completed_quest", 1),

			(try_begin),
				(is_between, "$g_encountered_party", towns_begin, towns_end),
				(str_store_string, s12, "str_the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_don_this_dress_and_throw_the_hood_over_your_face_i_will_smuggle_you_inside_the_castle_to_meet_her_in_the_guise_of_a_skullery_maid__the_guards_will_not_look_too_carefully_but_i_beg_you_for_all_of_our_sakes_be_discrete"),
				(assign, "$nurse_assists_entry", 1),
			(else_try),
				(str_store_string, s12, "str_the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_wait_for_a_while_by_the_spring_outside_the_walls_i_will_smuggle_her_ladyship_out_to_meet_you_dressed_in_the_guise_of_a_shepherdess_but_i_beg_you_for_all_of_our_sakes_be_discrete"),
				(assign, "$nurse_assists_entry", 2),
			(try_end),
		(else_try),
			(str_store_string, s12, "str_the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_her_ladyship_asks_me_to_say_that_yearns_to_see_you_but_that_you_should_bide_your_time_a_bit_her_ladyship_says_that_to_arrange_a_clandestine_meeting_so_soon_after_your_last_encounter_would_be_too_dangerous"),
		(try_end),
	(else_try),
		(str_store_string, s12, "str_the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter"),
	(try_end),

	],
    [

	("enter",
	[
    (call_script, "script_get_kingdom_lady_social_determinants", "$love_interest_in_town"),
	(troop_slot_eq, reg0, slot_lord_granted_courtship_permission, 1)
	], "Enter",
	[
	(jump_to_menu, "mnu_town"),
	(call_script, "script_setup_meet_lady", "$love_interest_in_town", "$g_encountered_party"),
	]
	),

	("nurse",
	[
    (eq, "$nurse_assists_entry", 1),
	], "Go with the nurse",
	[
	(jump_to_menu, "mnu_town"),
	(call_script, "script_setup_meet_lady", "$love_interest_in_town", "$g_encountered_party"),
	]
	),


	("nurse",
	[
    (eq, "$nurse_assists_entry", 2),
	], "Wait by the spring",
	[
	(jump_to_menu, "mnu_town"),
	(call_script, "script_setup_meet_lady", "$love_interest_in_town", "$g_encountered_party"),
	]
	),

	("leave",
	[],
	"Leave",
	[(jump_to_menu, "mnu_town")]),

    ]


  ),


    (
    "kill_local_merchant_begin",0,
    "You spot your victim and follow him, observing as he turns a corner into a dark alley.\
 This will surely be your best opportunity to attack him.",
    "none",
    [
    ],
    [
      ("continue",[],"Continue...",
       [(set_jump_mission,"mt_back_alley_kill_local_merchant"),
        (party_get_slot, ":town_alley", "$qst_kill_local_merchant_center", slot_town_alley),
        (modify_visitors_at_site,":town_alley"),
        (reset_visitors),
        (set_visitor, 0, "trp_player"),
        (set_visitor, 1, "trp_local_merchant"),
        (jump_to_menu, "mnu_town"),
        (jump_to_scene,":town_alley"),
        (change_screen_mission),
        ]),
     ]
  ),


    (
    "debug_alert_from_s65",0,
    "DEBUG ALERT: {s65}",
    "none",
    [
    ],
    [
      ("continue",[],"Continue...",
       [
        (assign, "$debug_message_in_queue", 0),
        (change_screen_return),
        ]),
     ]
  ),

  (
    "auto_return_to_map",0,
    "stub",
    "none",
    [(change_screen_map)],
    []
  ),

    (
    "bandit_lair",0,
    "{s3}",
    "none",
    [
      (try_begin),
        (eq, "$loot_screen_shown", 1),

        (try_for_range, ":bandit_template", bandit_party_templates_begin, bandit_party_templates_end), #SB : template range
          (party_template_slot_eq, ":bandit_template", slot_party_template_lair_party, "$g_encountered_party"),
          (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, 0),
          
          #dckplmc
           (store_current_hours, ":cur_hours"),
           (val_add, ":cur_hours", 168), #spawn again 1 week later
           (party_template_set_slot, ":bandit_template", slot_party_template_lair_next_spawn, ":cur_hours"),
          
        (try_end),

        (try_begin),
          (ge, "$g_encountered_party", 0),
          (party_is_active, "$g_encountered_party"),
          (party_get_template_id, ":template", "$g_encountered_party"),
          (neq, ":template", "pt_looter_lair"),
          (remove_party, "$g_encountered_party"),
        (try_end),

        (assign, "$g_leave_encounter", 0),
        (change_screen_return),

      (else_try),
        (party_stack_get_troop_id, ":bandit_type", "$g_encountered_party", 0),
        (str_store_troop_name_plural, s4, ":bandit_type"),
        (str_store_string, s5, "str_bandit_approach_defile"),

        #SB : set pictures
        (try_begin),
          (eq, ":bandit_type", "trp_desert_bandit"),
          (str_store_string, s5, "str_bandit_approach_defile"),
        (else_try),
          (eq, ":bandit_type", "trp_mountain_bandit"),
          (str_store_string, s5, "str_bandit_approach_cliffs"),
          (set_background_mesh, "mesh_pic_mountain_bandits"),
        (else_try),
          (eq, ":bandit_type", "trp_forest_bandit"),
          (str_store_string, s5, "str_bandit_approach_swamp"),
          (set_background_mesh, "mesh_pic_forest_bandits"),
        (else_try),
          (eq, ":bandit_type", "trp_taiga_bandit"),
          (str_store_string, s5, "str_bandit_approach_swamp"),
          (set_background_mesh, "mesh_pic_steppe_bandits"),
        (else_try),
          (eq, ":bandit_type", "trp_steppe_bandit"),
          (str_store_string, s5, "str_bandit_approach_thickets"),
          (set_background_mesh, "mesh_pic_steppe_bandits"),
        (else_try),
          (eq, ":bandit_type", "trp_sea_raider"),
          (str_store_string, s5, "str_bandit_approach_cove"),
          (set_background_mesh, "mesh_pic_sea_raiders"),
        (try_end),

        
        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 0), #used in place of global variable
          (str_store_string, s3, "str_bandit_hideout_preattack"),
        (else_try),
          (party_get_template_id, ":template", "$g_encountered_party"),
          (eq, ":template", "pt_looter_lair"),
          (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 1), #used in place of global variable
          (str_store_string, s3, "str_lost_startup_hideout_attack"),
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 1), #used in place of global variable
          (str_store_string, s3, "str_bandit_hideout_failure"),
          (set_background_mesh, "mesh_pic_wounded"),
          (try_begin),
            (eq, "$character_gender", tf_female),
            (set_background_mesh, "mesh_pic_wounded_fem"),
          (try_end),
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 2), #used in place of global variable
          (str_store_string, s3, "str_bandit_hideout_success"),
          (set_background_mesh, "mesh_pic_victory"),
        (try_end),
      (try_end),
    ],
    [
      ("continue_1",
      [
        (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 0), #used in place of global variable
      ],
      "Attack the hideout...",

      [
        (party_set_slot, "$g_encountered_party", slot_party_ai_substate, 1),
        (party_get_template_id, ":template", "$g_encountered_party"),
        (assign, "$g_enemy_party", "$g_encountered_party"),

        (try_begin),
          (eq, ":template", "pt_sea_raider_lair"),
          (assign, ":bandit_troop", "trp_sea_raider"),
          (assign, ":scene_to_use", "scn_lair_sea_raiders"),
        (else_try),
          (eq, ":template", "pt_forest_bandit_lair"),
          (assign, ":bandit_troop", "trp_forest_bandit"),
          (assign, ":scene_to_use", "scn_lair_forest_bandits"),
        (else_try),
          (eq, ":template", "pt_desert_bandit_lair"),
          (assign, ":bandit_troop", "trp_desert_bandit"),
          (assign, ":scene_to_use", "scn_lair_desert_bandits"),
        (else_try),
          (eq, ":template", "pt_mountain_bandit_lair"),
          (assign, ":bandit_troop", "trp_mountain_bandit"),
          (assign, ":scene_to_use", "scn_lair_mountain_bandits"),
        (else_try),
          (eq, ":template", "pt_taiga_bandit_lair"),
          (assign, ":bandit_troop", "trp_taiga_bandit"),
          (assign, ":scene_to_use", "scn_lair_taiga_bandits"),
        (else_try),
          (eq, ":template", "pt_steppe_bandit_lair"),
          (assign, ":bandit_troop", "trp_steppe_bandit"),
          (assign, ":scene_to_use", "scn_lair_steppe_bandits"),
        (else_try),
          (eq, ":template", "pt_looter_lair"),
          (assign, ":bandit_troop", "trp_looter"),

          (store_faction_of_party, ":starting_town_faction", "$g_starting_town"),

          (try_begin),
            (eq, ":starting_town_faction", "fac_kingdom_1"), #player selected swadian city as starting town.
            (assign, ":scene_to_use", "scn_lair_forest_bandits"),
          (else_try),
            (eq, ":starting_town_faction", "fac_kingdom_2"), #player selected Vaegir city as starting town.
            (assign, ":scene_to_use", "scn_lair_taiga_bandits"),
          (else_try),
            (eq, ":starting_town_faction", "fac_kingdom_3"), #player selected Khergit city as starting town.
            (assign, ":scene_to_use", "scn_lair_steppe_bandits"),
          (else_try),
            (eq, ":starting_town_faction", "fac_kingdom_4"), #player selected Nord city as starting town.
            (assign, ":scene_to_use", "scn_lair_sea_raiders"),
          (else_try),
            (eq, ":starting_town_faction", "fac_kingdom_5"), #player selected Rhodok city as starting town.
            (assign, ":scene_to_use", "scn_lair_mountain_bandits"),
          (else_try),
            (eq, ":starting_town_faction", "fac_kingdom_6"), #player selected Sarranid city as starting town.
            (assign, ":scene_to_use", "scn_lair_desert_bandits"),
          (try_end),
        (try_end),

        (modify_visitors_at_site,":scene_to_use"),
        (reset_visitors),

        (store_character_level, ":player_level", "trp_player"),
        (store_add, ":number_of_bandits_will_be_spawned_at_each_period", 5, ":player_level"),
        (val_div, ":number_of_bandits_will_be_spawned_at_each_period", 3),

        (try_for_range, ":unused", 0, ":number_of_bandits_will_be_spawned_at_each_period"),
          (store_random_in_range, ":random_entry_point", 2, 11),
          (set_visitor, ":random_entry_point", ":bandit_troop", 1),
        (try_end),

        (party_clear, "p_temp_casualties"),

        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission,"mt_bandit_lair"),

        (jump_to_scene, ":scene_to_use"),
        (change_screen_mission),
      ]),

      ("leave_no_attack",
      [
        (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 0),
      ],
      "Leave...",
      [
        (change_screen_return),
      ]),

      ("leave_victory",
      [
        (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 2),
      ],
      "Continue...",
      [
        (try_for_range, ":bandit_template", bandit_party_templates_begin, bandit_party_templates_end), #SB : template range
          (party_template_slot_eq, ":bandit_template", slot_party_template_lair_party, "$g_encountered_party"),
          (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, 0),
        (try_end),

        (party_get_template_id, ":template", "$g_encountered_party"),
        (try_begin),
          (neq, ":template", "pt_looter_lair"),
          (check_quest_active, "qst_destroy_bandit_lair"),
          (quest_slot_eq, "qst_destroy_bandit_lair", slot_quest_target_party, "$g_encountered_party"),
          (call_script, "script_succeed_quest", "qst_destroy_bandit_lair"),
        (try_end),

        (assign, "$g_leave_encounter", 0),
        (change_screen_return),

        (try_begin),
          (eq, "$loot_screen_shown", 0),
          (assign, "$loot_screen_shown", 1),
#          (try_begin),
#            (gt, "$g_ally_party", 0),
#            (call_script, "script_party_add_party", "$g_ally_party", "p_temp_party"), #Add remaining prisoners to ally TODO: FIX it.
#          (else_try),
#            (party_get_num_attached_parties, ":num_quick_attachments", "p_main_party"),
#            (gt, ":num_quick_attachments", 0),
#            (party_get_attached_party_with_rank, ":helper_party", "p_main_party", 0),
#            (call_script, "script_party_add_party", ":helper_party", "p_temp_party"), #Add remaining prisoners to our reinforcements
#          (try_end),
          (troop_clear_inventory, "trp_temp_troop"),

          (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties"),
          (try_for_range, ":stack_no", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties", ":stack_no"),
            (try_begin),
              (party_stack_get_size, ":stack_size", "p_temp_casualties", ":stack_no"),
              (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties", ":stack_no"),
              (gt, ":stack_size", 0),
              (party_add_members, "p_total_enemy_casualties", ":stack_troop", ":stack_size"), #addition_to_p_total_enemy_casualties
              (party_stack_get_num_wounded, ":stack_wounded_size", "p_temp_casualties", ":stack_no"),
              (gt, ":stack_wounded_size", 0),
              (party_wound_members, "p_total_enemy_casualties", ":stack_troop", ":stack_wounded_size"),
            (try_end),
          (try_end),

          (call_script, "script_party_calculate_loot", "p_total_enemy_casualties"), #p_encountered_party_backup changed to total_enemy_casualties
          (gt, reg0, 0),
          (troop_sort_inventory, "trp_temp_troop"),
          ##diplomacy start+
          ##OLD:
          #(change_screen_loot, "trp_temp_troop"),
          ##NEW:
          ##jump to rubik's CC autoloot
          (try_begin),
            (call_script, "script_party_calculate_loot", "p_total_enemy_casualties"),
            (assign, "$dplmc_return_menu", "mnu_bandit_lair"),
            #SB : variable resets
            (assign, "$lord_selected", "trp_player"),
            (str_clear, dplmc_loot_string),
            (jump_to_menu, "mnu_dplmc_manage_loot_pool"),
          (else_try),
             #Fall back to old behavior
            (change_screen_loot, "trp_temp_troop"),
          (try_end),
          ##diplomacy end+
        (try_end),

        (try_begin),
          (ge, "$g_encountered_party", 0),
          (party_is_active, "$g_encountered_party"),
          (party_get_template_id, ":template", "$g_encountered_party"),
          (eq, ":template", "pt_looter_lair"),
          (remove_party, "$g_encountered_party"),
        (try_end),
      ]),

      ("leave_defeat",
      [
        (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 1),
      ],
      "Continue...",
      [
        (try_for_range, ":bandit_template", bandit_party_templates_begin, bandit_party_templates_end), #SB : template range
          (party_template_slot_eq, ":bandit_template", slot_party_template_lair_party, "$g_encountered_party"),
          (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, 0),
        (try_end),

        (try_begin),
          (party_get_template_id, ":template", "$g_encountered_party"),
          (neq, ":template", "pt_looter_lair"),
          (check_quest_active, "qst_destroy_bandit_lair"),
          (quest_slot_eq, "qst_destroy_bandit_lair", slot_quest_target_party, "$g_encountered_party"),
          (call_script, "script_fail_quest", "qst_destroy_bandit_lair"),
        (try_end),

        (try_begin),
          (ge, "$g_encountered_party", 0),
          (party_is_active, "$g_encountered_party"),
          (party_get_template_id, ":template", "$g_encountered_party"),
          (neq, ":template", "pt_looter_lair"),
          (remove_party, "$g_encountered_party"),
        (try_end),

        (assign, "$g_leave_encounter", 0),

        (try_begin),
            (party_is_active, "$g_encountered_party"),
            (party_set_slot, "$g_encountered_party", slot_party_ai_substate, 0),
        (try_end),

        (change_screen_return),
        ]),

     ]
  ),


  (
    "notification_player_faction_political_issue_resolved",0,
    "After consulting with the peers of the realm, {s10} has decided to confer {s11} on {s12}.",
    "none",
    [
    (assign, ":faction_issue_resolved", "$g_notification_menu_var1"),
    (assign, ":faction_decision", "$g_notification_menu_var2"),
    (faction_get_slot, ":leader", "$players_kingdom", slot_faction_leader),
    (str_store_troop_name, s10, ":leader"),
    (try_begin),
        (eq, ":faction_issue_resolved", 1),
        (str_store_string, s11, "str_the_marshalship"),
    (else_try),
        (str_store_party_name, s11, ":faction_issue_resolved"),
    (try_end),
    (str_store_troop_name, s12, ":faction_decision"),

    ],
    [
       ("continue",
       [],"Continue...",
       [
        (change_screen_return),
        ]),


    ]
  ),

  (
    "notification_player_faction_political_issue_resolved_for_player",0,
    "After consulting with the peers of the realm, {s10} has decided to confer {s11} on you. You may decline the honor, but it will probably mean that you will not receive other awards for a little while.{s12}",
    "none",
    [
    (faction_get_slot, ":leader", "$players_kingdom", slot_faction_leader),
    (str_store_troop_name, s10, ":leader"),
    (faction_get_slot, ":issue", "$players_kingdom", slot_faction_political_issue),
    (try_begin),
        (eq, ":issue", 1),
        (str_store_string, s11, "str_the_marshalship"),
        (str_store_string, s12, "@^^Note that so long as you remain marshal, the lords of the realm will be expecting you to lead them on campaign. So, if you are awaiting a feast, either for a wedding or for other purposes, you may wish to resign the marshalship by speaking to your liege."),
    (else_try),
        (str_clear, s12),
        (str_store_party_name, s11, ":issue"),
    (try_end),
    ],
    [
       ("accept",
       [],"Accept the honor",
       [
        (faction_get_slot, ":issue", "$players_kingdom", slot_faction_political_issue),

        (try_begin),
            (eq, ":issue", 1),
            (call_script, "script_check_and_finish_active_army_quests_for_faction", "$players_kingdom"),
            (call_script, "script_appoint_faction_marshall", "$players_kingdom", "trp_player"),
            (unlock_achievement, ACHIEVEMENT_AUTONOMOUS_COLLECTIVE),
        (else_try),
            (call_script, "script_give_center_to_lord", ":issue", "trp_player", 0), #Zero means don't add garrison
        (try_end),

        (faction_set_slot, "$players_kingdom", slot_faction_political_issue, 0),
        (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
            (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
            (eq, ":active_npc_faction", "$players_kingdom"),
            (troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
        (try_end),
        (change_screen_return),
        ]),

       ("decline",
       [],"Decline the honor",
       [
        (faction_get_slot, ":issue", "$players_kingdom", slot_faction_political_issue),
        (try_begin),
            (is_between, ":issue", centers_begin, centers_end),
            (assign, "$g_dont_give_fief_to_player_days", 30),
        (else_try),
            (assign, "$g_dont_give_marshalship_to_player_days", 30),
        (try_end),

        (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
            (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
            (eq, ":active_npc_faction", "$players_kingdom"),
            (troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
        (try_end),
        (change_screen_return),
        ]),
    ]
  ),

  ("start_phase_2_5",mnf_disable_all_keys,
    "{!}{s16}",
    "none",
    [
      (str_store_party_name, s1, "$g_starting_town"),
      (str_store_string, s16, "$g_journey_string"),
      (call_script, "script_player_arrived"),
    ],
    [
    #SB : skip quest
      ("skip_quest",[], "Take a nice long walk around {s1}...",
       [
        (assign, "$g_starting_town", -1), #this disables the startup merchant from taverns
        #let triggers load first
        (rest_for_hours, 3, 5, 0),
        (assign, "$auto_enter_town", "$current_town"),
        # (start_encounter, "$current_town"),
        (change_screen_return),
       ]),

      ("continue",[], "Go find an inn...",
       [
        (jump_to_menu, "mnu_start_phase_3"),
       ]),
    ]
  ),


  ("start_phase_3",mnf_disable_all_keys,
    "{s16}^^You are exhausted by the time you find the inn in {s1}, and fall asleep quickly. However, you awake before dawn and are eager to explore your surroundings. You venture out onto the streets, which are still deserted. All of a sudden, you hear a sound that stands the hairs of your neck on end -- the rasp of a blade sliding from its scabbard...",
    "none",
    [ 
      (assign, ":continue", 1),
      (try_begin),
        (eq, "$current_startup_quest_phase", 1),
        (try_begin),
          (eq, "$g_killed_first_bandit", 1),
          (str_store_string, s11, "str_killed_bandit_at_alley_fight"),
        (else_try),
          (str_store_string, s11, "str_wounded_by_bandit_at_alley_fight"),
        (try_end),
        (jump_to_menu, "mnu_start_phase_4"),
        (assign, ":continue", 0),
      (else_try),
        (eq, "$current_startup_quest_phase", 3),
        (try_begin),
          (eq, "$g_killed_first_bandit", 1),
          (str_store_string, s11, "str_killed_bandit_at_alley_fight"),
        (else_try),
          (str_store_string, s11, "str_wounded_by_bandit_at_alley_fight"),
        (try_end),
        (jump_to_menu, "mnu_start_phase_4"),
        (assign, ":continue", 0),
      (try_end),

      (str_store_party_name, s1, "$g_starting_town"),
      (str_clear, s16),
      (eq, ":continue", 1),
      
    ],
    [

      ("continue",[], "Continue...",
       [
         (assign, "$g_starting_town", "$current_town"),
         # (call_script, "script_player_arrived"),
         # (party_set_morale, "p_main_party", 100), #SB : roll this into previous script
         (set_encountered_party, "$current_town"),
         #SB : play sound
         (play_sound, "snd_draw_sword"),
         (call_script, "script_prepare_alley_to_fight"),
       ]),
    ]
  ),

  ("start_phase_4",mnf_disable_all_keys,
    "{s11}",
    "none",
    [
      (assign, ":continue", 1),
      (try_begin),
        (eq, "$current_startup_quest_phase", 2),
        (change_screen_return),
        (assign, ":continue", 0),
      (else_try),
        (eq, "$current_startup_quest_phase", 3),
        (str_store_string, s11, "str_merchant_and_you_call_some_townsmen_and_guards_to_get_ready_and_you_get_out_from_tavern"),
      (else_try),
        (eq, "$current_startup_quest_phase", 4),
        (try_begin),
          (eq, "$g_killed_first_bandit", 1),
          (str_store_string, s11, "str_town_fight_ended_you_and_citizens_cleaned_town_from_bandits"),
        (else_try),
          (str_store_string, s11, "str_town_fight_ended_you_and_citizens_cleaned_town_from_bandits_you_wounded"),
        (try_end),
      (try_end),

      (eq, ":continue", 1),
    ],
    [
      ("continue",
      [
        (this_or_next|eq, "$current_startup_quest_phase", 1),
        (eq, "$current_startup_quest_phase", 4),
      ],
      "Continue...",
      [
        (assign, "$town_entered", 1),

        (try_begin),
          (eq, "$current_town", "p_town_1"),
          (assign, ":town_merchant", "trp_nord_merchant"),
          (assign, ":town_room_scene", "scn_town_1_room"),
        (else_try),
          (eq, "$current_town", "p_town_5"),
          (assign, ":town_merchant", "trp_rhodok_merchant"),
          (assign, ":town_room_scene", "scn_town_5_room"),
        (else_try),
          (eq, "$current_town", "p_town_6"),
          (assign, ":town_merchant", "trp_swadian_merchant"),
          (assign, ":town_room_scene", "scn_town_6_room"),
        (else_try),
          (eq, "$current_town", "p_town_8"),
          (assign, ":town_merchant", "trp_vaegir_merchant"),
          (assign, ":town_room_scene", "scn_town_8_room"),
        (else_try),
          (eq, "$current_town", "p_town_10"),
          (assign, ":town_merchant", "trp_khergit_merchant"),
          (assign, ":town_room_scene", "scn_town_10_room"),
        (else_try),
          (eq, "$current_town", "p_town_19"),
          (assign, ":town_merchant", "trp_sarranid_merchant"),
          (assign, ":town_room_scene", "scn_town_19_room"),
        (try_end),

        (modify_visitors_at_site, ":town_room_scene"),
        (reset_visitors),
        (set_visitor, 0, "trp_player"),
        (set_visitor, 9, ":town_merchant"),

        (assign, "$talk_context", tc_merchants_house),

        (assign, "$dialog_with_merchant_ended", 0),

        (set_jump_mission, "mt_meeting_merchant"),

        (jump_to_scene, ":town_room_scene"),
        (change_screen_mission),
      ]),

      ("continue",
      [
        (eq, "$current_startup_quest_phase", 3),
      ],
      "Continue...",
      [
        (call_script, "script_prepare_town_to_fight"),
      ]),
    ]
  ),


  ("lost_tavern_duel",mnf_disable_all_keys,
    "{s11}{s12}",
    "none",
    [
    (str_clear, s11),
    (str_clear, s12),
    #use s11 as primary indicator string
	(try_begin),
		(agent_get_troop_id, ":type", "$g_main_attacker_agent"),
		(eq, ":type", "trp_belligerent_drunk"),
		(str_store_string, s11, "str_lost_tavern_duel_ordinary"),
	(else_try),
		(agent_get_troop_id, ":type", "$g_main_attacker_agent"),
		(eq, ":type", "trp_hired_assassin"),
		(str_store_string, s11, "str_lost_tavern_duel_assassin"),
	(try_end),
	(troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, -1),
	(troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, -1), #remove him for now
    
    #use s12 for additional info like lost purse, etc
    #SB : penalty for fighting while disguised
    (try_begin),
      (gt, "$sneaked_into_town", disguise_none),
      (store_random_in_range, ":random_no", -100, 200),
      # (ge, ":random_no", "$g_player_luck"),
      (ge, ":random_no", 0),
      (str_store_string, s12, "@ Unfortunately, when the guards inquired about the tavern brawl, your description was recognized and you were in no condition to fight them off."),
    (try_end),
    ],
    [
      ("continue",[(eq, "$sneaked_into_town", disguise_none),],"Continue...",
       [
         (jump_to_menu, "mnu_town"),
         (troop_set_health, "trp_player", 25),
         #SB : renown loss, less than losing to bandits
         (call_script, "script_change_troop_renown", "trp_player", -1),
       ]),
       
      ("surrender",[(gt, "$sneaked_into_town", disguise_none),],"Surrender...",
       [
         (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
       ]),
    ]
  ),


  ("establish_court",mnf_disable_all_keys,
    "To establish {s4} as your court will require a small refurbishment. In particular, you will need a set of tools and a bolt of velvet. it may also take a short while for some of your followers to relocate here. Do you wish to proceed?",
    "none",
    [
	(str_store_party_name, s4, "$g_encountered_party"),
	],

    [
      ("establish",[
	  (player_has_item, "itm_tools"),
	  (player_has_item, "itm_velvet"),
	  ],"Establish {s4} as your court",
       [
		(assign, "$g_player_court", "$current_town"),
	    (troop_remove_item, "trp_player", "itm_tools"),
	    (troop_remove_item, "trp_player", "itm_velvet"),
        (jump_to_menu, "mnu_town"),
       ]),
       
    ("capital_exists",
      [
        (store_and, ":name_set", "$players_kingdom_name_set", rename_center),
        (ge, ":name_set", rename_center),
        (str_store_party_name, s1, "$g_player_court"),
        (disable_menu_option),
      ],
       "You cannot move the court as your capital is at {s1}.",
       [
     ]),


      ("continue",[],"Hold off...",
       [
         (jump_to_menu, "mnu_town"),
       ]),
    ]
  ),

  ("notification_relieved_as_marshal", mnf_disable_all_keys,
    "{s4} wishes to inform you that your services as marshal are no longer required. In honor of valiant efforts on behalf of the realm over the last {reg4} days, however, {reg8?she:he} offers you a purse of {reg5} denars.",
    "none",
    [
	(assign, reg4, "$g_player_days_as_marshal"),



	(store_div, ":renown_gain", "$g_player_days_as_marshal",4),
	(val_min, ":renown_gain", 20),
	(store_mul, ":denar_gain", "$g_player_days_as_marshal", 50),
	(val_max, ":denar_gain", 200),
	(val_min, ":denar_gain", 4000),
	(troop_add_gold, "trp_player", ":denar_gain"),
	(call_script, "script_change_troop_renown", "trp_player", ":renown_gain"),
	(assign, "$g_player_days_as_marshal", 0),
	(assign, "$g_dont_give_marshalship_to_player_days", 15),
	(assign, reg5, ":denar_gain"),

	(faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
	(str_store_troop_name, s4, ":faction_leader"),
	##diplomacy start+ get gender with script
	#(troop_get_type, reg8, ":faction_leader"),#<- OLD
	(assign, ":save_reg0", reg0),
	(call_script, "script_dplmc_store_troop_is_female", ":faction_leader"),
	(assign, reg8, reg0),
	(assign, reg0, ":save_reg0"),
	##diplomacy end+
	],

	 [
      ("continue",[],"Continue",
       [
         (change_screen_return),
       ]),
    ]
  ),


  ##diplomacy begin
########################################################
# Autoloot Game Menus Begin
########################################################

	##########################################################
	# Inventory allocation / Loot allocation Game Menu  -  by Fisheye
	# Parameters:
	# $return_menu : return to this menu after managing loot.  0 if this menu is called via random encounter
	##diplomacy start+
	#Added "return_menu", renaming it to "$dplmc_return_menu"
	##diplomacy end+
	("dplmc_manage_loot_pool", mnf_enable_hot_keys,
		"{s10}^{s30}",
		"none",
		[
			##diplomacy start+
			#Use a different troop!
			#(assign, "$pool_troop", "trp_dplmc_chamberlain"),
			(assign, "$pool_troop", "trp_temp_troop"),
			#Make sure things are initialized
			(call_script, "script_dplmc_initialize_autoloot", 0),#argument "0" means this does nothing if deemed unnecessary
			##diplomacy end+
			(assign, reg20,0),
			(troop_get_inventory_capacity, ":inv_cap", "$pool_troop"),
			(try_for_range, ":i_slot", 0, ":inv_cap"),
				(troop_get_inventory_slot, ":item_id", "$pool_troop", ":i_slot"),
				(ge, ":item_id", 0),
				(neg|troop_has_item_equipped, "$pool_troop", ":item_id"),
				(val_add, reg20, 1),
			(try_end),
			# reg20 now contains number of items in loot pool
			(try_begin),
				(eq, reg20, 0),
				(str_store_string, s10, "str_dplmc_item_pool_no_items"),
				(str_store_string, s20, "str_dplmc_item_pool_leave"),
			(else_try),
				(eq, reg20, 1),
				(str_store_string, s10, "str_dplmc_item_pool_one_item"),
				(str_store_string, s20, "str_dplmc_item_pool_abandon"),
			(else_try),
				(str_store_string, s10, "str_dplmc_item_pool_many_items"),
				(str_store_string, s20, "str_dplmc_item_pool_abandon"),
			(try_end),
		  ## CC
			(try_begin), #only show when we don't have equipment logs
              (str_is_empty, dplmc_loot_string),
			  (set_fixed_point_multiplier, 100),
              (position_set_x, pos0, 20),
              (position_set_y, pos0, 30),
              (position_set_z, pos0, 80),
			  (set_game_menu_tableau_mesh, "tableau_game_character_sheet", "$lord_selected", pos0),
			(try_end),
		  ## CC
          
          #SB : str30 shows items looted after script_dplmc_auto_loot_troop was called
          # (try_begin),
            # (neg|str_is_empty, dplmc_loot_string),
            # (str_store_string, s10, "@{s10}^^{s30}"),
          # (try_end),
		],
		[
			("dplmc_auto_loot",
				[
					(eq, "$inventory_menu_offset",0),
					(store_free_inventory_capacity, ":space", "$pool_troop"),
					(ge, ":space", 10),
					(gt, reg20, 0),
				],
				##diplomacy start+
				#"Let your heroes select gear from the item pool.",
				"Let your heroes select gear from the items on the ground.",
				##diplomacy end+
				[
					# (set_player_troop, "trp_player"),
					# (assign, "$lord_selected", "trp_player"),
					##diplomacy start+
					(call_script, "script_dplmc_initialize_autoloot", 0),#argument "0" means this does nothing if deemed unnecessary
					##diplomacy end+
					(jump_to_menu, "mnu_dplmc_auto_loot")
				]
			),
			("dplmc_auto_loot_no",
				[
					(eq, "$inventory_menu_offset",0),
					(store_free_inventory_capacity, ":space", "$pool_troop"),
					(lt, ":space", 10),
					(disable_menu_option)
				],
				"Insufficient item pool space for auto-upgrade.",
				[]
			),
			("dplmc_loot",
				[],
				##diplomacy start+
				#"Access the item pool.",
				"Access the items on the ground.",
				##diplomacy end+
				[
					(change_screen_loot, "$pool_troop"),
				]
			),

            #SB : improve usability, if only change_screen_loot worked with the player
			("dplmc_loot_player",
				[(is_between, "$lord_selected", companions_begin, companions_end),],
				"Access the captain's inventory.",
                #can't use honorific, since the player troop is the companion and strings will be malformed
				[
					(set_player_troop, "trp_player"),
					(change_screen_equip_other, "$lord_selected"),
					(assign, "$lord_selected", "trp_player"),
				]
			),
      ("dplmc_auto_loot_upgrade_management", [],
##diplomacy start+
#        "Upgrade management of the NPC's equipments.",
         "Update management of NPCs' equipment.",
##diplomacy end+
        [
          (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
          ##nested diplomcy start+ Add error check.
          
          ##nested diplomacy end+
          (try_begin),
            (is_between, "$lord_selected", companions_begin, companions_end),
            (assign, "$temp", "$lord_selected"),
          (else_try),
            (assign, "$temp", -1),  
            (try_for_range, ":stack_no", 0, ":num_stacks"),
              (party_stack_get_troop_id,   ":stack_troop", "p_main_party", ":stack_no"),
              (is_between, ":stack_troop", companions_begin, companions_end),
              (assign, "$temp", ":stack_troop"),
              (assign, ":num_stacks", 0),
            (try_end),
          (try_end),
          ##nested diplomacy start+   Add error check.
          (call_script, "script_dplmc_initialize_autoloot", 0),#argument "0" means this does nothing if deemed unnecessary
          (try_begin),#<- dplmc+ added
            (ge, "$temp", 1),#<- dplmc+ added
            (assign, "$temp_2", -1), #SB : other globals
            (try_for_range, ":item_slot", ek_item_0, ek_food),
              (troop_set_slot, "trp_stack_selection_ids", ":item_slot", 0),
            (try_end),
            (str_clear, dplmc_loot_string),
            (start_presentation, "prsnt_dplmc_autoloot_upgrade_management"),
          (try_end),
          ##nested diplomacy end+
        ]
      ),
      
      #all other options will reset player eventually, this is for convenience
      ("dplmc_auto_loot_reset_player", [(neq, "$lord_selected", "trp_player")],
         "Reset current troop to the player",
        [
          (assign, "$lord_selected", "trp_player"),
          (set_player_troop, "$lord_selected"),
        ]
      ),
			("dplmc_leave",
				[],
				"{s20}",
				[
				##diplomacy start+
				#Actually abandon the lost loot
				(troop_get_inventory_capacity, ":inv_cap", "$pool_troop"),
				(try_for_range, ":i_slot", 10, ":inv_cap"),
					(troop_get_inventory_slot, ":item_id", "$pool_troop", ":i_slot"),
					(ge, ":item_id", 0),
					(neg|troop_has_item_equipped, "$pool_troop", ":item_id"),
					(troop_set_inventory_slot, "$pool_troop", ":i_slot", -1), #delete it
					(troop_inventory_slot_set_item_amount, "$pool_troop", ":i_slot", 0),
				(try_end),

				#(jump_to_menu, "mnu_camp"),
				(set_player_troop, "trp_player"),
				(jump_to_menu, "$dplmc_return_menu"),
				(assign, "$pool_troop", -1), #mark ending
				##diplomacy end+
				]
			),
			##nested diplomacy start+
			#Leave & take everything you can
			("dplmc_leave_and_take_a",
				[
				(store_free_inventory_capacity, ":space", "trp_player"),
				(lt, ":space", reg20),
				(gt, reg20, 0),
				(gt, ":space", 0),
				(assign, reg0, ":space"),
				],
				"Gather {reg0} of the {reg20} items on the ground and leave.",
				[
					(store_free_inventory_capacity, ":space", "trp_player"),
					#Take remaining items for player
					(troop_get_inventory_capacity, ":inv_cap", "$pool_troop"),
					(troop_sort_inventory, "$pool_troop"),
					(try_for_range, ":i_slot", 10, ":inv_cap"),
					    (gt, ":space", 0),
					    (troop_get_inventory_slot, ":item_id", "$pool_troop", ":i_slot"),
					    (ge, ":item_id", 0),
					    (neg|troop_has_item_equipped, "$pool_troop", ":item_id"),
					    (troop_get_inventory_slot_modifier, ":imod", "$pool_troop", ":i_slot"),
					    (troop_add_item, "trp_player", ":item_id", ":imod"),#give item to player
					    (val_sub, ":space", 1),
					    (troop_set_inventory_slot, "$pool_troop", ":i_slot", -1), #remove item from pool
					    (troop_inventory_slot_set_item_amount, "$pool_troop", ":i_slot", 0),
					(try_end),
					#(jump_to_menu, "mnu_camp"),
					(set_player_troop, "trp_player"),
					(jump_to_menu, "$dplmc_return_menu"),
					(assign, "$pool_troop", -1), #mark ending
				]
			),
			("dplmc_leave_and_take_b",
				[
				(store_free_inventory_capacity, ":space", "trp_player"),
				(ge, ":space", reg20),
				(gt, reg20, 0),#don't show if nothing is on the ground
				(store_sub, reg0, reg20, 1),
				],
				"Gather the remaining {reg20} {reg0?items:item} on the ground and leave.",
				[
					(store_free_inventory_capacity, ":space", "trp_player"),
					#Take remaining items for player
					(troop_get_inventory_capacity, ":inv_cap", "$pool_troop"),
					(try_for_range, ":i_slot", 10, ":inv_cap"),
					    (gt, ":space", 0),
					    (troop_get_inventory_slot, ":item_id", "$pool_troop", ":i_slot"),
					    (ge, ":item_id", 0),
					    (neg|troop_has_item_equipped, "$pool_troop", ":item_id"),
					    (troop_get_inventory_slot_modifier, ":imod", "$pool_troop", ":i_slot"),
					    (troop_add_item, "trp_player", ":item_id", ":imod"),#give item to player
					    (val_sub, ":space", 1),
					    (troop_set_inventory_slot, "$pool_troop", ":i_slot", -1), #remove item frlom pool
					    (troop_inventory_slot_set_item_amount, "$pool_troop", ":i_slot", 0),
					(try_end),
					(set_player_troop, "trp_player"),
					(jump_to_menu, "$dplmc_return_menu"),
					(assign, "$pool_troop", -1), #mark ending
				]
			),
			("dplmc_leave_and_take_c",
				[
				(store_free_inventory_capacity, ":space", "trp_player"),
				(eq, ":space", 0),
				(gt, reg20, 0),#don't show if nothing is on the ground
				(disable_menu_option),
				],
				"There is no space left in your bags.",
				[
				]
			),
			##nested diplomacy end+
		]
	),

	("dplmc_auto_loot",
		0,
##diplomacy start+
		"Your heroes will automatically grab items from the loot pool based on their pre-selected upgrade options. Heroes listed first in the party order will have first pick. Any equipment no longer needed will be dropped back into the loot pool. Any items in the loot pool will be lost when you leave.^ Are you sure you wish to do this?",
##diplomacy end+
		"none",
		[],
		[
			("dplmc_autoloot_no",
				[],
				"No, I've changed my mind.",
				[
					(jump_to_menu, "mnu_dplmc_manage_loot_pool"),
				]
			),
			("dplmc_autoloot_yes",
				[],
				"Yes, perform the upgrading.",
				[
					##diplomacy start+
					(call_script, "script_dplmc_initialize_autoloot", 0),#argument "0" means this does nothing if deemed unnecessary
					(assign, "$pool_troop", "trp_temp_troop"),
					#SB : reset variables
					(set_player_troop, "trp_player"),
					(assign, "$lord_selected", "trp_player"),
					##diplomacy end+
					(call_script, "script_dplmc_auto_loot_all", "trp_temp_troop", dplmc_loot_string),
					(jump_to_menu, "mnu_dplmc_manage_loot_pool"),
				]
			),
            
            #SB : individual looting
			("dplmc_autoloot_personal",
				[(is_between, "$lord_selected", companions_begin, companions_end),(str_store_troop_name, s1, "$lord_selected")],
				"Yes, only upgrade {s1}.",
				[
					##diplomacy start+
					(assign, "$pool_troop", "trp_temp_troop"),
					(call_script, "script_dplmc_auto_loot_troop", "$lord_selected", "$pool_troop", dplmc_loot_string),
					##diplomacy end+
					(jump_to_menu, "mnu_dplmc_manage_loot_pool"),
				]
			),
		]
	),


  (
    "dplmc_notification_alliance_declared",0,
    "Alliance Agreement^^{s1} and {s2} have formed an alliance!^{s57}",
    "none",
    [

	  (str_clear, s57),

	  (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("dplmc_continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_notification_defensive_declared",0,
    "Defensive Pact^^{s1} and {s2} have agreed to a defensive pact!^{s57}",
    "none",
    [

	  (str_clear, s57),

	  (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("dplmc_continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_notification_trade_declared",0,
    "Trade Agreement^^{s1} and {s2} have signed a trade agreement!^{s57}",
    "none",
    [

	  (str_clear, s57),

	  (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("dplmc_continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_notification_nonaggression_declared",0,
    "Non-aggression Treaty^^{s1} and {s2} have concluded a non-aggression treaty!^{s57}",
    "none",
    [
	  (str_clear, s57),

	  (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("dplmc_continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_question_alliance_offer",0,
    "You Receive an Alliance Offer^^The {s1} wants to form an alliance with you. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_alliance_offer_accept",[],"Accept",
       [
         (call_script, "script_dplmc_start_alliance_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (change_screen_return),
        ]),
      ("dplmc_alliance_offer_reject",[],"Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_question_defensive_offer",0,
    "You Receive a Pact Offer^^The {s1} offers you a defensive pact. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_defensive_offer_accept",[],"Accept",
       [
         (call_script, "script_dplmc_start_defensive_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (change_screen_return),
        ]),
      ("dplmc_defensive_offer_reject",[],"Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_question_trade_offer",0,
    "You Receive a Pact Offer^^The {s1} offers you a trade pact. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_trade_offer_accept",[],"Accept",
       [
         (call_script, "script_dplmc_start_trade_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (change_screen_return),
        ]),
      ("dplmc_trade_offer_reject",[],"Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_question_nonaggression_offer",0,
    "You Receive a Pact Offer^^The {s1} offers you a non-aggression treaty. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_nonaggression_offer_accept",[],"Accept",
       [
         (call_script, "script_dplmc_start_nonaggression_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (change_screen_return),
        ]),
      ("dplmc_nonaggression_offer_reject",[],"Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_notification_alliance_expired",0,
    "Alliance Has Expired^^The alliance between {s1} and {s2} has expired and was degraded to a defensive pact.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_continue",[],"Continue",
       [
	   (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_notification_defensive_expired",0,
    "Defensive Pact Has Expired^^The defensive pact between {s1} and {s2} has expired and was degraded to a trade agreement.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_continue",[],"Continue",
       [
	   (change_screen_return),
        ]),
     ]
  ),


  (
    "dplmc_notification_trade_expired",0,
    "Trade Agreement Has Expired^^The trade agreement between {s1} and {s2} has expired and was degraded to a non-aggression treaty.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_continue",[],"Continue",
       [
	   (change_screen_return),
        ]),
     ]
  ),

  ("dplmc_dictate_terms",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Dictate your peace terms.",
    "none",
    [(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),],
    [
      ("dplmc_demand_4000",[(gt, "$g_player_chamberlain", 0),],"Demand 4000 denars",
      [
        (call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "fac_player_supporters_faction", -1),
        (assign, ":goodwill", reg0),
        (store_random_in_range, ":random", 0, 4),

        (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -3),
        (try_begin),
          (le, ":random", ":goodwill"),
          (call_script, "script_dplmc_pay_into_treasury", 4000),
          (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "fac_player_supporters_faction", 1),
          (change_screen_return),
        (else_try),
          (jump_to_menu,"mnu_dplmc_deny_terms"),
        (try_end),
      ]),
      ("dplmc_demand_8000",[(gt, "$g_player_chamberlain", 0),],"Demand 8000 denars",
       [
         (call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "fac_player_supporters_faction", -1),
         (assign, ":goodwill", reg0),
         (val_mul, ":goodwill", 2),
				 (store_random_in_range, ":random", 0, 10),

         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -5),
				 (try_begin),
				   (le, ":random", ":goodwill"),
           (call_script, "script_dplmc_pay_into_treasury", 8000),
           (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "fac_player_supporters_faction", 1),
           (change_screen_return),
         (else_try),
             (jump_to_menu,"mnu_dplmc_deny_terms"),
         (try_end),
       ]),
      ("dplmc_demand_castle",[
        (assign, ":distance", 100),
        (assign, "$demanded_castle", -1),
		##diplomacy start+ Handle player is co-ruler of NPC kingdom
		(assign, ":alt_faction", "fac_player_supporters_faction"),
		(try_begin),
			(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
			(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
			(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
			(assign, ":alt_faction", "$players_kingdom"),
		(try_end),
		##diplomacy end+
        (try_for_range, ":castle", castles_begin, castles_end),
          (store_faction_of_party, ":castle_faction", ":castle"),
          (eq, ":castle_faction", "$g_notification_menu_var1"),
          (try_for_range, ":center", centers_begin, centers_end),
            (store_faction_of_party, ":center_faction", ":center"),
			##diplomacy start+
			(this_or_next|eq, ":alt_faction", ":center_faction"),
			##diplomacy end+
            (eq, ":center_faction", "fac_player_supporters_faction"),
            (store_distance_to_party_from_party, ":tmp_distance", ":center", ":castle"),

            (lt, ":tmp_distance", ":distance"),
            (assign, ":distance", ":tmp_distance"),
            (assign, "$demanded_castle", ":castle"),
            (str_store_party_name, s2, ":castle"),
          (try_end),
        (try_end),
        (is_between, "$demanded_castle", castles_begin,castles_end),
      ],"Demand {s2}.",
       [
        (call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "fac_player_supporters_faction", -1),
        (assign, ":goodwill", reg0),
        (val_mul, ":goodwill", 2),
        (store_random_in_range, ":random", 0, 12),

        (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -6),
        (try_begin),
          (le, ":random", ":goodwill"),
			 ##diplomacy start+
			 #Chance of veto based on ownership and difficulty setting.
			 (assign, ":did_veto", 0),
			 (try_begin),
					 (party_get_slot, ":castle_lord", "$demanded_castle", slot_town_lord),
					 (ge, ":castle_lord", 1),
					 (neg|troop_slot_ge, ":castle_lord", slot_troop_prisoner_of_party, 0),
					 (try_begin),
								(this_or_next|troop_slot_eq, ":castle_lord", slot_troop_home, "$demanded_castle"),
								(party_slot_eq, "$demanded_castle", dplmc_slot_center_original_lord, ":castle_lord"),
								(store_random_in_range, ":random", 0, 24),
								(assign, ":did_veto", 1),
								(le, ":random", ":goodwill"),
								(assign, ":did_veto", 0),
 					 (else_try),
								(troop_get_slot, ":castle_lord_original_faction", ":castle_lord", slot_troop_original_faction),
								(party_slot_eq, "$demanded_castle", slot_center_original_faction, ":castle_lord_original_faction"),
								(store_random_in_range, ":random", 0, 12),
								(assign, ":did_veto", 1),
								(le, ":random", ":goodwill"),
								(assign, ":did_veto", 0),
					 (try_end),
			 (try_end),
			 (eq, ":did_veto", 0),
		  ##Handle player is co-ruler of NPC kingdom
          ##OLD:
          #(call_script, "script_give_center_to_faction", "$demanded_castle", "fac_player_supporters_faction"),
          #(call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "fac_player_supporters_faction", 1),
		  ##NEW:
		  (assign, ":player_kingdom", "fac_player_supporters_faction"),
		  (try_begin),
		        (neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
				(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
				(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
				(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
				(assign, ":player_kingdom", "$players_kingdom"),
		  (try_end),
		  (call_script, "script_give_center_to_faction", "$demanded_castle", ":player_kingdom"),
          (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", ":player_kingdom", 1),
		  ##diplomacy end+
          (change_screen_return),
        (else_try),
          (jump_to_menu,"mnu_dplmc_deny_terms"),
        (try_end),        ]
       ),
	  ("dplmc_go_back",[],"Go back",
       [
	     (jump_to_menu,"mnu_question_peace_offer"),
       ]),
    ]
  ),

  ("dplmc_deny_terms",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "The {s1} refuses your terms and is breaking off of negotiations.",
    "none",
    [(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),],
    [
	  ("dplmc_continue",[],"Continue",
       [
       (change_screen_return),
       ]),
    ]
  ),

  (
    "dplmc_village_riot_result",mnf_scale_picture,
    "{s9}",
    "none",
    [(try_begin),
       (eq, "$g_battle_result", 1),
       (jump_to_menu, "mnu_dplmc_village_riot_removed"),
     (else_try),
       (set_background_mesh, "mesh_pic_villageriot"),
       (str_store_string, s9, "@Try as you might, you could not defeat the rebelling village."),
     (try_end),
    ],
    [
      ("dplmc_continue",[],"Continue...",
       [(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
        (call_script, "script_change_troop_renown", "trp_player", -5), #SB : renown loss highest here
        (jump_to_menu, "mnu_village"),]),
    ],
  ),

  (
    "dplmc_village_riot_removed",mnf_disable_all_keys,
    "In bloody battle you and your men slaughter the rebels and regain control over the village. But there is not much left you can control.",
    "none",
    [
     (set_background_mesh, "mesh_pic_looted_village"),
     (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
     (call_script, "script_village_set_state",  "$current_town", svs_looted),
    ],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (jump_to_menu, "mnu_village"),
       ]),
    ],
  ),

  (
    "dplmc_town_riot_removed",mnf_disable_all_keys,
    "In bloody battle you and your men slaughter the rebels and regain control over the town.",
    "none",
    [],
    [
      ("dplmc_continue",[],"Continue...",
       [
        (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
        (assign, "$new_encounter", 1),
        (try_begin),
          (party_get_slot, ":town_lord","$g_encountered_party", slot_town_lord),
          (troop_get_slot, ":cur_banner", ":town_lord", slot_troop_banner_scene_prop),
          (try_begin),
              (gt, ":cur_banner", 0),
              (val_sub, ":cur_banner", banner_scene_props_begin),
              (val_add, ":cur_banner", banner_map_icons_begin),
              (party_set_banner_icon, "$g_encountered_party", ":cur_banner"),
          (else_try),
              (eq, ":cur_banner", -1),
              (troop_get_slot, ":flag_icon", ":town_lord", slot_troop_custom_banner_map_flag_type),
              (try_begin),
                (ge, ":flag_icon", 0),
                (val_add, ":flag_icon", custom_banner_map_icons_begin),
                (party_set_banner_icon, "$g_encountered_party", ":flag_icon"),
              (try_end),
          (try_end), #custom_banner_begin
        (try_end),
        (jump_to_menu, "mnu_castle_outside"),
       ]),
    ],
  ),

  (
    "dplmc_riot_negotiate",mnf_disable_all_keys,
    "You approach the angry crowd and begin negotiations. The leader of the riot demands {reg0} denars. He agrees to lay down arms if you are willing to pay.",
    "none",
    [
      (party_get_slot, ":center_relation", "$g_encountered_party", slot_center_player_relation),
      (val_min, ":center_relation", 0),
      (try_begin),
        (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
        (val_sub, ":center_relation", 75),
        (set_background_mesh, "mesh_pic_townriot"),
      (else_try),
        (val_sub, ":center_relation", 50),
        (set_background_mesh, "mesh_pic_villageriot"),
      (try_end),

      (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
      (val_add, ":center_relation", ":persuasion_level"),
      (val_mul, ":center_relation", ":center_relation"),
      (assign, reg0, ":center_relation"),
    ],
    [
      ("dplmc_pay_riot_treasury",
      [
        (gt, "$g_player_chamberlain", 0),
        (store_troop_gold, ":gold", "trp_household_possessions"),
        (ge, ":gold", reg0),
      ],"Induce your chamberlain to pay the money from the treasury.",
       [
        (call_script, "script_dplmc_withdraw_from_treasury", reg0),
        (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (jump_to_menu, "mnu_castle_outside"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),

       ]),
       ("dplmc_pay_riot_cash",
      [
        (store_troop_gold, ":gold", "trp_player"),
        (ge, ":gold", reg0),
      ],"Pay cash.",
       [
        (troop_remove_gold, "trp_player", reg0),
        (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (jump_to_menu, "mnu_castle_outside"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),

       ]),

      ("dplmc_back",[],"Back...",
       [
        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (jump_to_menu, "mnu_castle_outside"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
       ]),
    ],
  ),

  (
    "dplmc_notification_riot",0,
    "The peasants of {s1} launched a riot against you! In a surprise attack, men loyal to you have been slain. The remainder joined the angry crowd.",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (try_begin),
        (party_slot_eq, "$g_notification_menu_var1", slot_party_type, spt_town),
        (set_background_mesh, "mesh_pic_townriot"),
      (else_try),
        (set_background_mesh, "mesh_pic_villageriot"),
      (try_end),
      ],
    [
      ("dplmc_continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_notification_appoint_chamberlain",0,
    "As a lord of a fief you can now appoint a chamberlain who resides at you court for a weekly salary of 15 denars. He will handle all financial affairs like collecting and determining taxes, paying wages and managing your estate. In addition he supervises money transfers between kingdoms giving you more diplomatic options.",
    "none",
    [],
    [

      ("dplmc_appoint_default",[],"Appoint a prominent nobleman from the area.",
       [
        (call_script, "script_dplmc_appoint_chamberlain"),
        (jump_to_menu, "mnu_dplmc_chamberlain_confirm"),
        ]),
      ("dplmc_continue",[],"Proceed without chamberlain.",
       [
         (assign, "$g_player_chamberlain", -1), #denied
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_chamberlain_confirm",0,
    "Your chamberlain can be found at your court. You should consult him if you want to give him any financial advice or you need greater amounts of money. You should always make sure that there is enough money in the treasury to pay for political affairs.",
    "none",
    [],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_notification_appoint_constable",0,
    "As a lord of a fief you can now appoint a constable who resides at you court for a weekly salary of 15 denars. He will recruit new troops and provide information about your army.",
    "none",
    [],
    [

      ("dplmc_appoint_default",[],"Appoint a prominent nobleman from the area.",
       [
        (call_script, "script_dplmc_appoint_constable"),
        (jump_to_menu, "mnu_dplmc_constable_confirm"),
        ]),
      ("dplmc_continue",[],"Proceed without constable.",
       [
         (assign, "$g_player_constable", -1), #denied
         (assign, "$g_constable_training_center", -1),
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_constable_confirm",0,
    "Your constable can be found at your court. You should consult him if you want to recruit new troops or get detailed information about your standing army.",
    "none",
    [],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),



  (
    "dplmc_notification_appoint_chancellor",0,
    "As a lord of a fief you can now appoint a chancellor who resides at you court for a weekly salary of 20 denars. He will be the keeper of your seal and conduct the correspondence between you and other important persons.",
    "none",
    [],
    [

      ("dplmc_appoint_default",[],"Appoint a prominent nobleman from the area.",
       [
        (call_script, "script_dplmc_appoint_chancellor"),
        (jump_to_menu, "mnu_dplmc_chancellor_confirm"),
        ]),
      ("dplmc_continue",[],"Proceed without chancellor.",
       [
         (assign, "$g_player_chancellor", -1), #denied
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_chancellor_confirm",0,
    "Your chancellor can be found at your court. You should consult him if you want to send messages or gifts.",
    "none",
    [],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),


  (
    "dplmc_deserters",0,
    "Some of your men don't believe that you will pay their wages and desert. Overall you lose: {s11} men.",
    "none",
    [
      (set_background_mesh, "mesh_pic_deserters"),
      (store_random_in_range, ":random", 1,  "$g_notification_menu_var1"),
      (call_script, "script_dplmc_player_troops_leave", ":random"),
      (str_store_string, s11, "@{reg0}"),
    ],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_negotiate_besieger",0,
    "You appear with a white flag at the top of the wall. After a while a negotiator of {s11} approaches you. He demands {s6} and all associated villages as well as {reg0} denars for safe conduct.",
    "none",
    [
      (party_get_slot, ":besieger", "$current_town", slot_center_is_besieged_by),
      (party_stack_get_troop_id, ":enemy_party_leader", ":besieger", 0),
      (str_store_troop_name, s11, ":enemy_party_leader"),
      (store_faction_of_troop, ":besieger_faction", ":enemy_party_leader"),

      ##diplomacy start+
	  #1) Support promoted kingdom ladies, mercenary parties, etc.
	  #2) Fix mistake with potentially not counting besieger party in the size calculation!
	  ##OLD:
	  #(assign, ":besieger_size", 0),
      #(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
      #  (store_faction_of_troop, ":lord_faction", ":lord"),
      #  (eq, ":lord_faction", ":besieger_faction"),
      #  (troop_get_slot, ":led_party", ":lord", slot_troop_leaded_party),
      ##NEW:
      (party_get_num_companions, ":besieger_size", ":besieger"),

	  (try_for_parties, ":led_party"),
        (ge, ":led_party", spawn_points_end),
        (neq, ":led_party", ":besieger"),#don't double count
        (store_faction_of_party, ":party_faction", ":led_party"),
        (eq, ":party_faction", ":besieger_faction"),
	  ##diplomacy end+
        (party_is_active, ":led_party"),

        (party_slot_eq, ":led_party", slot_party_ai_state, spai_accompanying_army),
        (party_slot_eq, ":led_party", slot_party_ai_object, ":besieger"),

        (party_is_active, ":besieger"),
        (store_distance_to_party_from_party, ":distance_to_marshal", ":led_party", ":besieger"),
        (lt, ":distance_to_marshal", 25),
        (party_get_num_companions, ":party_size", ":led_party"),
        (val_add, ":besieger_size", ":party_size"),
      (try_end),

      (assign, ":garrison_size", 0),
      (party_get_num_companion_stacks, ":num_stacks", "$current_town"),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_size, ":stack_size", "$current_town", ":i_stack"),
        (val_add, ":garrison_size", ":stack_size"),
      (try_end),
      (val_sub, ":besieger_size", ":garrison_size"),

      (store_skill_level, ":player_persuasion_skill", "skl_persuasion", "trp_player"),
      (val_mul, ":player_persuasion_skill", 10),
      (store_sub, "$diplomacy_var", ":besieger_size", ":player_persuasion_skill"),
      (val_mul, "$diplomacy_var", 4),
      ##diplomacy start+ : include ransom cost in calculation
      (call_script, "script_calculate_ransom_amount_for_troop", "trp_player"),
      (val_add, "$diplomacy_var", reg0),
      ##diplomacy end+
      (val_max,"$diplomacy_var",500),
      (val_div, "$diplomacy_var", 100),
      (val_mul, "$diplomacy_var", 100),
      (assign, reg0, "$diplomacy_var"),

      (str_store_party_name, s6, "$current_town"),

    ],
      [
      ("dplmc_comply_treasury",
      [
        (store_troop_gold, ":gold", "trp_household_possessions"),
        (ge, ":gold", "$diplomacy_var"),
      ],"Comply and induce your chamberlain to pay the money from the treasury.",
      [
        (call_script, "script_dplmc_withdraw_from_treasury", "$diplomacy_var"),
		##diplomacy start+ when the player pays, give the gold to the lord
		(party_get_slot, ":besieger", "$current_town", slot_center_is_besieged_by),
		(party_stack_get_troop_id, ":enemy_party_leader", ":besieger", 0),
		(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", "$diplomacy_var", ":enemy_party_leader"),
		##diplomacy end+
        (call_script, "script_dplmc_player_center_surrender", "$current_town"),
        (change_screen_return),
      ]),

      ("dplmc_comply",
      [
        (store_troop_gold, ":gold", "trp_player"),
        (ge, ":gold", "$diplomacy_var"),
      ],"Comply and pay the gold.",
      [
        (troop_remove_gold, "trp_player", "$diplomacy_var"),
		##diplomacy start+ when the player pays, give the gold to the lord
		(party_get_slot, ":besieger", "$current_town", slot_center_is_besieged_by),
		(party_stack_get_troop_id, ":enemy_party_leader", ":besieger", 0),
		(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", "$diplomacy_var", ":enemy_party_leader"),
		##diplomacy end+
        (call_script, "script_dplmc_player_center_surrender", "$current_town"),
        (change_screen_return),
      ]),

      ("dplmc_break_off",[],"Break off negotiations.",
       [
          (jump_to_menu, "mnu_town"),
        ]),
     ]
  ),


  (
    "dplmc_messenger",0,
##nested diplomacy start+ "His" to "{reg4?Her:His}"
    "Sire, I found {s10} and delivered your message. {reg4?Her:His} answer was {s11}.",
##nested diplomacy end+
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (str_store_troop_name, s10, "$g_notification_menu_var1"),
        (try_begin),
          (eq, "$g_notification_menu_var2", 1),
          (str_store_string, s11, "@positive"),
        (else_try),
          (str_store_string, s11, "@negative"),
        (try_end),
        ##nested diplomacy start+
        (try_begin),
           (call_script, "script_cf_dplmc_troop_is_female", "$g_notification_menu_var1"),
           (assign, reg4, 1),
        (else_try),
           (assign, reg4, 0),
        (try_end),
        ##nested diplomacy end+
    ],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_scout",0,
    "Your spy returned from {s10}^^{s11}{s12}",
    "none",
    [
    (set_background_mesh, "mesh_pic_messenger"),
    (str_store_party_name, s10, "$g_notification_menu_var1"),

    (call_script, "script_game_get_center_note", "$g_notification_menu_var1", 0),
    (str_store_string, s11, "@{!}{s0}"),
    (try_begin),
      (this_or_next|is_between, "$g_notification_menu_var1", towns_begin, towns_end),
      (is_between, "$g_notification_menu_var1", castles_begin, castles_end),
      (party_get_slot, ":center_food_store", "$g_notification_menu_var1", slot_party_food_store),
      (call_script, "script_center_get_food_consumption", "$g_notification_menu_var1"),
      (assign, ":food_consumption", reg0),
      (store_div, reg6, ":center_food_store", ":food_consumption"),
      (store_party_size, reg5, "$g_notification_menu_var1"),
      (str_store_string, s11, "@{s11}^^ The current garrison consists of {reg5} men.^The food stock lasts for {reg6} days."),
    (try_end),

    (str_clear, s12),
    (party_get_num_attached_parties, ":num_attached_parties", "$g_notification_menu_var1"),
    (try_begin),#<- dplmc+ unclosed try_begin!
      (gt, ":num_attached_parties", 0),
      (str_store_string, s12, "@^^Additional the following parties are currently inside:^"),
    (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
      (party_get_attached_party_with_rank, ":attached_party", "$g_notification_menu_var1", ":attached_party_rank"),
      (str_store_party_name, s3, ":attached_party"),
      (store_party_size, reg1, ":attached_party"),
      (str_store_string, s12, "@{s12} {s3} with {reg1} troops.^"),
    (try_end),
	##diplomacy start+
	#Add missing try-end for (gt, ":num_attached_parties", 0),
	(try_end),
	##diplomacy end+

    (call_script, "script_update_center_recon_notes", "$g_notification_menu_var1"),
    ],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_domestic_policy",0,
    "You can now shape the domestic policy of your kingdom. Do you want to change your policy now?",
    "none",
    [
      (try_begin),
          (eq, "$g_players_policy_set", 1),
          (change_screen_return),
      (try_end),

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", pos0),
    ],
    [
      ("dplmc_yes",[],"Yes, I want to change the domestic policy.",
       [
         (start_presentation, "prsnt_dplmc_policy_management"),
        ]),
      ("dplmc_no",[],"No, I don't want to change the domestic policy.",
       [
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_affiliate_end",0,
    "{!}{s11}",
    "none",
    [
      (set_background_mesh, "mesh_pic_messenger"),

      (str_store_troop_name, s9, "$g_notification_menu_var1"),
      (try_begin),
        ##nested diplomacy start+ (1) Fix a bug from the Diplomacy 3.3.2 version of this menu by getting your ex-affiliate
	    #from "$g_notification_menu_var2" instead of "$g_player_affiliated_troop".
        ##OLD: #(eq, "$g_player_affiliated_troop", "$g_notification_menu_var1"),
        (eq, "$g_notification_menu_var2", "$g_notification_menu_var1"),
        ##nested diplomacy end+
        (str_store_string, s11, "@{playername}, ^^I always knew you were a bad egg, since the day you have pledged allegiance to my clan. ^Did you really think you could set my family against me? You've dropped your mask, you snake! You are an infliction, and I will not bear it anymore. ^Hereby, I disown and ban you from my house. I have urged my family to fight you, and I will warn Calradia lords about your infamy. ^Tremble with fear, you have a deadly enemy! ^^{s9}."),
      (else_try),
        ##nested diplomacy start+ (2) Fix a bug from the Diplomacy 3.3.2 version of this menu by getting your ex-affiliate
	    #from "$g_notification_menu_var2" instead of "$g_player_affiliated_troop".
        ##OLD:
		#(is_between, "$g_player_affiliated_troop", lords_begin, kingdom_ladies_end),
        #(str_store_troop_name, s10, "$g_player_affiliated_troop"),
		##NEW:
		(ge, "$g_notification_menu_var2", walkers_end),
        (troop_is_hero, "$g_notification_menu_var2"),
		(str_store_troop_name, s10, "$g_notification_menu_var2"),
        ##### (3) Make the next line use correct pronouns, and correct term for king/queen.  TODO: Change some of the funny wording.
		##OLD:
        #(str_store_string, s11, "@{playername},^^ I've received a letter from {s9}, telling me about your disgracefull jiggery-pokery. In the present circumstances, {s9} could not provide evidence. But unlike you, {he/she} is a distinguished member of my family; and since all these years, I never had any reason to distrust {him/her}. I take {his/her} charges for granted. ^Hopefully, you failed to breakup my family unit. Hereby I reject your pledge : you are no longer related to my house. Each membership will retaliate against you in all conscience... ^I would be ashamed to confess how you maliciously fooled me, so I will not challenge you, to not be accountable for your death to my King. However I'm not used to report him every rat I crush while in wilderness, someday I may find you there ! ^^{s10}"),
		##NEW:
		(call_script, "script_dplmc_store_troop_is_female", "$g_notification_menu_var1"),
		(assign, reg1, reg0),#Move to reg1, because reg0 will be overwritten below
        (store_faction_of_troop, ":faction_var", "$g_notification_menu_var2"),
		(try_begin),
		   (gt, ":faction_var", 0),
		   (faction_get_slot, ":faction_var", ":faction_var", slot_faction_leader),
		   (gt, ":faction_var", 0),
		   (call_script, "script_dplmc_store_troop_is_female", ":faction_var"),
		   (eq, reg0, 1),
		   (call_script, "script_dplmc_print_cultural_word_to_sreg", "$g_notification_menu_var2", DPLMC_CULTURAL_TERM_KING_FEMALE, s11),
		   (assign, reg1, 1),#make sure the above didn't do anything funny with the register
		(else_try),
		   (call_script, "script_dplmc_print_cultural_word_to_sreg", "$g_notification_menu_var2", DPLMC_CULTURAL_TERM_KING, s11),
		   (assign, reg1, 0),#if there was no faction leader, reg0 might not have been initialized in the first place
		(try_end),
		#Aside from making the next line use the correct gender for the pronoun,
		#I made the wording a tiny bit less strange (although I left in "jiggery-pokery").
        (str_store_string, s11, "@{playername},^^ I've received a letter from {s9}, telling me about your disgraceful jiggery-pokery. In the present circumstances, {s9} could not provide evidence. But unlike you, {reg1?she:he} is a distinguished member of my family; and since all these years, I never had any reason to distrust {reg1?her:him}. I take {reg1?her:him} charges for granted. ^Hopefully, you failed to breakup my family unit. Hereby I reject your pledge : you are no longer related to my house. Each membership will retaliate against you in all conscience... ^I would be ashamed to confess how you maliciously fooled me, so I will not challenge you, to not be accountable for your death to my {s11}. However I'm not used to telling {reg0?her:him} about every rat I crush in the wilderness, and someday I may find you there ! ^^{s10}"),
        ##nested diplomacy end+
      (try_end),
    ],
    [
      ("dplmc_continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),

  (
    "dplmc_preferences",0,
	##diplomacy start+ alter for PBOD
    "Diplomacy "+DPLMC_DIPLOMACY_VERSION_STRING+" Preferences{s0}",##"Diplomacy preferences",
	##diplomacy end+
    "none",
    [
	##diplomacy start+
	(troop_get_slot, reg0, "trp_dplmc_chamberlain", dplmc_slot_troop_affiliated),
	(str_clear, s0),
	(try_begin),
		#Print a warning message for bad version numbers
		(neq, reg0, 0),
		(store_mod, ":verify", reg0, 128),
		(this_or_next|lt, reg0, 0),
			(neq, ":verify", DPLMC_VERSION_LOW_7_BITS),
		(str_store_string, s0, "@{!}{s0}^^ WARNING: Unexpected version value in slot dplmc_slot_troop_affiliated in trp_dplmc_chamberlain: {reg0}"),
	(else_try),
		#In cheat mode, print the diplomacy+ version
		(ge, "$cheat_mode", 1),
		(val_div, reg0, 128),
		(str_store_string, s0, "@{!}{s0}^^ DEBUG: Internal update code for current saved game is {reg0}.  Update code for the current release is "+str(DPLMC_CURRENT_VERSION_CODE)+"."),
	(try_end),
	##diplomacy end+
    
    ##SB : enable presentation to be launched again
    (try_begin),
      (eq, "$g_presentation_next_presentation", "prsnt_redefine_keys"),
      (start_presentation, "$g_presentation_next_presentation"),
    (try_end),
    ],
    [
    #SB : adjust menu options
      ("dplmc_cheat_mode",[(assign, reg0, "$cheat_mode")],"{reg0?Dis:En}able cheat mode.",
       [
           (val_clamp, "$cheat_mode", 0, 2), #in case of other values
           (store_sub, "$cheat_mode", 1, "$cheat_mode"),
           # (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
        #value = 0 is on by default
      ("dplmc_horse_speed",[(assign, reg0, "$g_dplmc_horse_speed"),],"{reg0?En:Dis}able Diplomacy horse speed.",
       [
           (val_clamp, "$g_dplmc_horse_speed", 0, 2), #in case of other values
           (store_sub, "$g_dplmc_horse_speed", 1, "$g_dplmc_horse_speed"),
           # (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
      # ("dplmc_enable_horse_speed",[(eq, "$g_dplmc_horse_speed", 1),],"Enable Diplomacy horse speed.",
       # [
           # (assign, "$g_dplmc_horse_speed", 0),
           # (jump_to_menu, "mnu_dplmc_preferences"),
        # ]),
        #value = 0 is on by default
      ("dplmc_battle_continuation",[(assign, reg0, "$g_dplmc_battle_continuation"),],"{reg0?En:Dis}able Diplomacy battle continuation.",
       [
           (val_clamp, "$g_dplmc_battle_continuation", 0, 2), #in case of other values
           (store_sub, "$g_dplmc_battle_continuation", 1, "$g_dplmc_battle_continuation"),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
      #SB : new option
      ("dplmc_player_disguise",[(assign, reg0, "$g_dplmc_player_disguise"),],"{reg0?Dis:En}able disguise system.",
       [
           (val_clamp, "$g_dplmc_player_disguise", 0, 2), #rare bug where disguise has strange values
           (store_sub, "$g_dplmc_player_disguise", 1, "$g_dplmc_player_disguise"),
           # (assign, reg1, "$g_dplmc_player_disguise"),
           # (display_message,"@{reg1}"),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),

      ## sb : charge + deathcam
      ("dplmc_charge_when_dead",[ (eq, "$g_dplmc_battle_continuation", 0),(assign, reg0, "$g_dplmc_charge_when_dead"),],
        "{reg0?Dis:En}able troops charging upon battle continuation.",
       [
           (val_clamp, "$g_dplmc_charge_when_dead", 0, 2), #in case of other values
           (store_sub, "$g_dplmc_charge_when_dead", 1, "$g_dplmc_charge_when_dead"),
           # (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
        
      ("dplmc_deathcam_keys",[ (eq, "$g_dplmc_battle_continuation", 0),],"Redefine camera keys.",
       [
           (assign, "$g_presentation_next_presentation", "prsnt_redefine_keys"),
           (start_presentation, "prsnt_redefine_keys"),
        ]),
        
      ##diplomacy start+
      #toggle terrain advantage
      ("dplmc_disable_terrain_advantage",[(eq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),],"Disable terrain advantage in Autocalc battles (currently this feature is Enabled).",
       [
           (assign, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_DISABLE),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
      ("dplmc_enable_terrain_advantage",[
		(eq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_DISABLE),],"Enable terrain advantage in Autocalc battles (currently this feature is Disabled).",
       [
           (assign, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
      ("dplmc_reset_terrain_advantage",[
		(neq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_DISABLE),
		(neq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
		(assign, reg0, "$g_dplmc_terrain_advantage")
		],"You used a saved game from another mod: g_dplmc_terrain_advantage = {reg0} (click to reset)",
       [
           (assign, "$g_dplmc_terrain_advantage", 0),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
	#toggle lord recycling
	  ("dplmc_toggle_lord_recycling_a",[
		(eq, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_DISABLE),
		],"Enable lords returning from exile and spawning without homes (currently disabled)",
       [
           (assign, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_ENABLE),
        ]),
	  ("dplmc_toggle_lord_recycling_b",[
		(this_or_next|eq, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_FREQUENT),#currently this setting is not distinct
		(eq, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_ENABLE),
		],"Disable lords returning from exile and spawning without homes (currently enabled)",
       [
	 	   (assign, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_DISABLE),
        ]),
      ("dplmc_toggle_lord_recycling_reset",
		[(neq, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_DISABLE), #SB : fix const
 		 (neq, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_ENABLE),
		 (neq, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_FREQUENT),
		 (assign, reg0, "$g_dplmc_lord_recycling"),],
			"You used a saved game from another mod: g_dplmc_lord_recycling = {reg0} (click to reset)",
       [
           (assign, "$g_dplmc_lord_recycling", 0),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
	#toggle AI changes
	  ("dplmc_toggle_ai_changes_a",[
		(eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_DISABLE),
		],"Enable AI changes (currently disabled)",
       [
           (assign, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
        ]),
	  ("dplmc_toggle_ai_changes_b",[
		(eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
		],"Increase AI changes (currently low)",
       [
	 	   (assign, "$g_dplmc_ai_changes",DPLMC_AI_CHANGES_MEDIUM),
        ]),

	  ("dplmc_toggle_ai_changes_c",[
		(eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
		],"Increase AI changes (currently medium)",
       [
	 	   (assign, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
        ]),
	  ("dplmc_toggle_ai_changes_d",[
		(eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
		],"Disable AI changes (currently high/experimental)",
       [
	 	   (assign, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_DISABLE),
        ]),
      ("dplmc_reset_ai_changes",
		[(neq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_DISABLE),
 		 (neq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
		 (neq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
		 (neq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
		 (assign, reg0, "$g_dplmc_ai_changes"),],
			"You used a saved game from another mod: g_dplmc_ai_changes = {reg0} (click to reset)",
       [
           (assign, "$g_dplmc_ai_changes", 0),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
	#toggle economics changes
	  ("dplmc_toggle_gold_changes_a",[
		(eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_DISABLE),
		],"Set economic & behavioral changes to low (current mode: disabled)",
       [
           (assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
        ]),
	  ("dplmc_toggle_gold_changes_b",[
		(eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
		],"Set economic & behavioral changes to medium (current mode: low)",
       [
	 	   (assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
        ]),
	  ("dplmc_toggle_gold_changes_c",[
		(eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
		],"Set economic & behavioral changes to high/experimental (current mode: medium)",
       [
	 	   (assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
        ]),
	  ("dplmc_toggle_gold_changes_d",[
		(eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
		],"Disable economic & behavioral changes (current mode: high/experimental)",
       [
	 	   (assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_DISABLE),
        ]),
      ("dplmc_reset_gold_changes",
		[(neq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_DISABLE),
 		 (neq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
		 (neq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
		 (neq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
		 (assign, reg0, "$g_dplmc_gold_changes"),],
			"You used a saved game from another mod: g_dplmc_gold_changes = {reg0} (click to reset)",
       [
           (assign, "$g_dplmc_gold_changes", 0),
           (jump_to_menu, "mnu_dplmc_preferences"),
        ]),
	#Toggle the default anti-woman prejudice.  This uses the already-existing
	#global variable "$g_disable_condescending_comments", and gives it additional
	#meaning.
		("dplmc_switch_woman_prejudice_1", [
			(this_or_next|eq, "$g_disable_condescending_comments", 0),
			(eq, "$g_disable_condescending_comments", 1)],
			"Change prejudice level (current level is default)",
			[(val_add, "$g_disable_condescending_comments", 2),
			(jump_to_menu, "mnu_dplmc_preferences"),]),
		("dplmc_switch_woman_prejudice_2", [
			(this_or_next|eq, "$g_disable_condescending_comments", 2),
			(eq, "$g_disable_condescending_comments", 3)],
			"Change prejudice level (current level is off)",
			[(val_sub, "$g_disable_condescending_comments", 4),
			(jump_to_menu, "mnu_dplmc_preferences"),]),
		("dplmc_switch_woman_prejudice_3", [
			(this_or_next|eq, "$g_disable_condescending_comments", -1),
			(eq, "$g_disable_condescending_comments", -2)],
			"Change prejudice level (current level is high)",
			[(val_add, "$g_disable_condescending_comments", 2),
			(jump_to_menu, "mnu_dplmc_preferences"),]),
##diplomacy end+
      ("dplmc_back",[],"Back...",
       [
           (jump_to_menu, "mnu_camp"),
        ]),
     ]
  ),

  ##diplomacy end
##diplomacy start+
  ("dplmc_affiliated_family_report",0,
   "{s0}",
   "none",
   [
    (str_clear, s0),
	(str_clear, s1),
	(try_for_range, ":troop_no", active_npcs_including_player_begin, heroes_end),
		(try_begin),
			(eq, ":troop_no", active_npcs_including_player_begin),
			(assign, ":troop_no", "trp_player"),
		(try_end),
		(call_script, "script_dplmc_store_troop_is_eligible_for_affiliate_messages", ":troop_no"),
		(this_or_next|eq, ":troop_no", "trp_player"),
           (ge, reg0, 1),

		(str_clear, s1),
		(str_store_string, s0, "str_dplmc_s0_newline_s1"),#add blank line to start

		#show name; (non-player) also show location
		(try_begin),
			(eq, ":troop_no", "trp_player"),
			(str_store_string, s1, "@{playername}"),
		(else_try),
			(call_script, "script_get_information_about_troops_position", ":troop_no", 0),#s1 = String, reg0 = knows-or-not
		(try_end),
		(str_store_string, s0, "str_dplmc_s0_newline_s1"),#add line

		#(non-player) show relation
		(try_begin),
			(neq, "trp_player", ":troop_no"),
			(call_script, "script_troop_get_player_relation", ":troop_no"),
			(assign, reg1, reg0) ,
			(str_store_string, s1, "str_relation_reg1"),
			(str_store_string, s0, "str_dplmc_s0_newline_s1"),#add line
		(try_end),

		#(non-prisoner) show party size
		(try_begin),
            (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
			(troop_get_slot, ":led_party", ":troop_no", slot_troop_leaded_party),
            (this_or_next|eq, ":led_party", 0),
			   (ge, ":led_party", spawn_points_end),
			(this_or_next|eq, ":troop_no", "trp_player"),
			   (neq, ":led_party", "p_main_party"),
			(party_is_active, ":led_party"),
			(assign, reg0, 0),
			(party_get_num_companions, reg1, ":led_party"),#number of troops
            (str_store_string, s1, "@Troops: {reg1}"),
			(str_store_string, s0, "str_dplmc_s0_newline_s1"),#add line
		(try_end),

	(try_end),
    ],
    [
	  ("lord_relations",[],"View list of all known lords by relation.",
       [
		(jump_to_menu, "mnu_lord_relations"),
        ]
       ),
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),

  ("dplmc_start_select_prejudice",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "In the traditional medieval society depicted in the game, war and politics are usually dominated by male members of the nobility.  Because of this, a female character can face initial prejudice, and some opportunities open to men will not be available (although a woman will also have some opportunities a man will not).  Some players might find distasteful, so if you want you can ignore that aspect of society in Calradia.^^You can later change your mind through the options in the Camp menu.",
    "none",
    [],
    [
      ("dplmc_start_prejudice_yes",[],"I do not mind encountering sexism.",
       [
         (assign, "$g_disable_condescending_comments", 0),#Default value
         (jump_to_menu,"mnu_start_character_1"),
        ]
       ),
      ("dplmc_start_prejudice_no",[],"I would prefer not to encounter as much sexism.",
       [
         (assign, "$g_disable_condescending_comments", 2),#Any value 2 or higher shuts off sexist setting elements
         (jump_to_menu, "mnu_start_character_1"),
       ]
       ),
	  ("go_back",[],"Go back",
       [
	     (jump_to_menu,"mnu_start_game_1"),
       ]),
    ]
  ),
  
  ##Economic report, currently just for debugging purposes
  ("dplmc_economic_report",0,
   "{s0}",
   "none",
   [
    (str_clear, s0),
    (str_clear, s1),
    (assign, reg0, 0),
    (str_store_string, s0, "@Prosperity Report^"),

    #Show average prosperity for each faction
    (try_for_range, ":faction", 0, kingdoms_end),
       (this_or_next|eq, ":faction", 0),
       (is_between, ":faction", kingdoms_begin, kingdoms_end),

       (this_or_next|eq, ":faction", 0),
       (faction_slot_eq, ":faction", slot_faction_state, sfs_active),
       
       (try_begin),
          (eq, ":faction", 0),
          (str_store_string, s1, "@Total"),
       (else_try),
          (faction_get_slot, reg0, ":faction", slot_faction_adjective),
          (gt, reg0, 0),
          (str_store_string, s1, reg0),
       (else_try),
          (str_store_faction_name, s1, ":faction"),
       (try_end),

       ##(1) Faction Prosperity, towns
       (assign, ":sum", 0),
       (assign, ":q_5", 0),
       (assign, ":q_4", 0),
       (assign, ":q_3", 0),
       (assign, ":q_2", 0),
       (assign, ":q_1", 0),
       (assign, ":num", 0),
       
       (try_for_range, ":center_no", towns_begin, towns_end),
          (store_faction_of_party, reg0, ":center_no"),
          (this_or_next|eq, ":faction", 0),
          (eq, reg0, ":faction"),
          (val_add, ":num", 1),
          (party_get_slot, reg0, ":center_no", slot_town_prosperity),
          (val_add, ":sum", reg0),
          (try_begin),
             (lt, reg0, 20),
             (val_add, ":q_1", 1),
          (else_try),
             (lt, reg0, 40),
             (val_add, ":q_2", 1),
          (else_try),
             (lt, reg0, 60),
             (val_add, ":q_3", 1),
          (else_try),
             (lt, reg0, 80),
             (val_add, ":q_4", 1),
          (else_try),
             (val_add, ":q_5", 1),
          (try_end),
       (try_end),
       
       (assign, reg0, ":num"),
       (val_max, reg0, 1),
       (store_div, reg0, ":sum", reg0),
       (str_store_string, s0, "@{s0}^{s1} Average Town Prosperity: {reg0}"),
       (assign, reg0, ":q_5"),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, reg0, 0),
          (str_store_string, s0, "@{s0}^{s1} towns with prosperity 80-100: {reg0}"),
       (try_end),
       (assign, reg0, ":q_4"),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, reg0, 0),
          (str_store_string, s0, "@{s0}^{s1} towns with prosperity 60-79: {reg0}"),
       (try_end),
       (assign, reg0, ":q_3"),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, reg0, 0),
          (str_store_string, s0, "@{s0}^{s1} towns with prosperity 40-59: {reg0}"),
       (try_end),
       (assign, reg0, ":q_2"),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, reg0, 0),
          (str_store_string, s0, "@{s0}^{s1} towns with prosperity 20-39: {reg0}"),
       (try_end),
       (assign, reg0, ":q_1"),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, reg0, 0),
          (str_store_string, s0, "@{s0}^{s1} towns with prosperity 0-19: {reg0}"),
       (try_end),
       
       (str_store_string, s0, "@{!}{s0}^"),

       ##(2) Faction Prosperity, villages
       (assign, ":sum", 0),
       (assign, ":q_5", 0),
       (assign, ":q_4", 0),
       (assign, ":q_3", 0),
       (assign, ":q_2", 0),
       (assign, ":q_1", 0),
       (assign, ":num", 0),
       
       (try_for_range, ":center_no", villages_begin, villages_end),
          (store_faction_of_party, reg0, ":center_no"),
          (this_or_next|eq, ":faction", 0),
          (eq, reg0, ":faction"),
          (val_add, ":num", 1),
          (party_get_slot, reg0, ":center_no", slot_town_prosperity),
          (val_add, ":sum", reg0),
          (try_begin),
             (lt, reg0, 20),
             (val_add, ":q_1", 1),
          (else_try),
             (lt, reg0, 40),
             (val_add, ":q_2", 1),
          (else_try),
             (lt, reg0, 60),
             (val_add, ":q_3", 1),
          (else_try),
             (lt, reg0, 80),
             (val_add, ":q_4", 1),
          (else_try),
             (val_add, ":q_5", 1),
          (try_end),
       (try_end),
       
       (assign, reg0, ":num"),
       (val_max, reg0, 1),
       (store_div, reg0, ":sum", reg0),
       (str_store_string, s0, "@{s0}^{s1} Average Village Prosperity: {reg0}"),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, ":q_5", 0),
          (assign, reg0, ":q_5"),
          (str_store_string, s0, "@{s0}^{s1} villages with prosperity 80-100: {reg0}"),
       (try_end),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, ":q_4", 0),
          (assign, reg0, ":q_4"),
          (str_store_string, s0, "@{s0}^{s1} villages with prosperity 60-79: {reg0}"),
       (try_end),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, ":q_3", 0),
          (assign, reg0, ":q_3"),
          (str_store_string, s0, "@{s0}^{s1} villages with prosperity 40-59: {reg0}"),
       (try_end),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, ":q_2", 0),
          (assign, reg0, ":q_2"),
          (str_store_string, s0, "@{s0}^{s1} villages with prosperity 20-39: {reg0}"),
       (try_end),
       (try_begin),
          (this_or_next|eq, ":faction", 0),
          (gt, ":q_1", 0),
          (assign, reg0, ":q_1"),
          (str_store_string, s0, "@{s0}^{s1} villages with prosperity 0-19: {reg0}"),
       (try_end),
       (str_store_string, s0, "@{!}{s0}^"),
    (try_end),
    ],
    [
      ("dplmc_back",[],"Continue...",
       [
           (jump_to_menu, "mnu_reports"),
        ]),
      ]
  ),
##diplomacy end+

#SB : secondary cheat menu

  (
    "town_cheats",0,
    "Select an option to interact with troops here",
    "none",[(call_script, "script_set_town_picture"),],
    [
      ("page",
      [],
      "Next Page.",
      [
        (jump_to_menu, "mnu_town_cheats_2"),
      ]),
      
      ("debug",
      [],
      "Party Cheats.",
      [
        (jump_to_menu, "mnu_party_cheat"),
      ]),
      ("host_tournament",
      [(party_slot_eq, "$current_town", slot_party_type, spt_town),],
      "Host a tournament",
      [
           (call_script, "script_fill_tournament_participants_troop", "$current_town", 1),
           (assign, "$g_tournament_cur_tier", 0),
           (assign, "$g_tournament_player_team_won", -1),
           (assign, "$g_tournament_bet_placed", 0),
           (assign, "$g_tournament_bet_win_amount", 0),
           (assign, "$g_tournament_last_bet_tier", -1),
           (assign, "$g_tournament_next_num_teams", 0),
           (assign, "$g_tournament_next_team_size", 0),
           (jump_to_menu, "mnu_town_tournament"),
      ]),

      ("camp_cheat_gather",[(party_slot_eq, "$current_town", slot_party_type, spt_town),],"Gather all inactive NPCs.",
       [ (assign, "$npc_to_rejoin_party", -1),
         (try_for_range, ":troop_no", companions_begin, companions_end),
           (neg|main_party_has_troop, ":troop_no"),
           (troop_slot_eq, ":troop_no", slot_troop_days_on_mission, 0),
           (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),
            # (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
           (troop_set_slot, ":troop_no", slot_troop_cur_center, "$current_town"),
           (troop_set_slot, ":troop_no", slot_troop_turned_down_twice, 0),
         (try_end),
         # (jump_to_menu, "mnu_camp_cheat"),
        ]
        ),

      # ("camp_cheat_gather",[(party_slot_eq, "$current_town", slot_party_type, spt_town),],"Gather all NPCs not in main party (cancel missions).",
       # [ (assign, "$npc_to_rejoin_party", -1),
         # (try_for_range, ":troop_no", companions_begin, companions_end),
            # (neg|main_party_has_troop, ":troop_no"),
            # (call_script, "script_remove_troop_from_prison", ":troop_no"),
            # (try_for_range, ":slots", slot_troop_days_on_mission, slot_troop_recruit_price),
              # (troop_set_slot, ":troop_no", ":slots", 0),
            # (try_end),
            # (troop_set_slot, ":troop_no", slot_troop_cur_center, "$current_town"),
         # (try_end),
        # ]
        # ),

      ("summon_drunk",
      [(party_slot_eq, "$current_town", slot_party_type, spt_town),
       # (troop_get_slot, ":town", "trp_belligerent_drunk", slot_troop_cur_center),
       (try_begin),
         # (is_between, ":town", towns_begin, towns_end),
         (troop_slot_eq, "trp_belligerent_drunk", slot_troop_cur_center, "$current_town"),
         (assign, reg10, 1),
       (else_try),
         (assign, reg10, 0),
       (try_end),
       ],
      "{reg10?Dismiss:Get} a drunkard.",
      [
        (try_begin),
          (eq, reg10, 1),
          (troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, -1),
        (else_try),
          (troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, "$current_town"),
        (try_end),
      ]),


      ("summon_ass",
      [(party_slot_eq, "$current_town", slot_party_type, spt_town),
       (try_begin),
         # (is_between, ":town", towns_begin, towns_end),
         (troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$current_town"),
         (assign, reg11, 1),
       (else_try),
         (assign, reg11, 0),
       (try_end),
      ],
      "{reg11?Scare away:Hire} an assassin.",
      [
        (try_begin),
          (eq, reg11, 1),
          (troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, -1),
        (else_try),
          (troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, "$current_town"),
        (try_end),
      ]),

      ("summon_bandit",
      [
       (neg|party_slot_eq, "$current_town", slot_party_type, spt_castle),
       (party_get_slot, reg12, "$current_town", slot_center_has_bandits),
       # (try_begin),
         # (party_slot_ge, "$current_town", slot_center_has_bandits, 1),
         # (assign, reg12, 1),
       # (else_try),
         # (assign, reg12, 0),
       # (try_end).
       (try_begin), #none present
         (eq, reg12, 0),
         (str_store_string, s12, "str_bandits"),
       (else_try),
         (str_store_troop_name_plural, s12, reg12),
       (try_end),
      ],
      "{reg12?Kick out:Get ambushed by} some {s12}.",
      [
       (try_begin), #cleanse
         (party_slot_ge, "$current_town", slot_center_has_bandits, 1),
         (party_set_slot, "$current_town", slot_center_has_bandits, 0),
       (else_try), #ambush
         (store_random_in_range, ":bandit", bandits_begin, bandits_end),
         (party_set_slot, "$current_town", slot_center_has_bandits, ":bandit"),
         (assign, "$town_nighttime", 1),
         (assign, "$sneaked_into_town", 0),
         (assign, "$g_defending_against_siege", 0),
         (call_script, "script_cf_enter_center_location_bandit_check"),
         # (assign, "$town_nighttime", 1),
       (try_end),
      ]),
      
      ("summon_village_bandit",
      [
       (party_slot_eq, "$current_town", slot_party_type, spt_village),
       (party_get_slot, reg13, "$current_town", slot_village_infested_by_bandits),
       (try_begin),
         (le, reg13, 0),
         (str_store_troop_name_plural, s13, "trp_bandit"),
       (else_try),
         (str_store_troop_name_plural, s13, reg13),
       (try_end),
      ],
      "{reg13?Cleanse:Infest} the village {reg13?of:with} {s13}.",
      [
        (try_begin), #cleanse
          (party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
          (party_set_slot, "$current_town", slot_village_infested_by_bandits, 0),
        (else_try), #infest
          (call_script, "script_center_get_bandits", "$current_town", 0),
          (party_set_slot, "$current_town", slot_village_infested_by_bandits, reg0),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]),
      
      ("summon_insurgent",
      [ (party_slot_eq, "$current_town", slot_village_infested_by_bandits, 0),
      ],
      "Spearhead a peasant revolution.",
      [
        (party_set_slot, "$current_town", slot_village_infested_by_bandits, "trp_peasant_woman"),

        #add additional troops
        (store_character_level, ":player_level", "trp_player"),
        (store_div, ":player_leveld2", ":player_level", 2),
        (store_mul, ":player_levelx2", ":player_level", 2),
        (try_begin),
          (is_between, "$current_town", villages_begin, villages_end),
          (store_random_in_range, ":random",0, ":player_level"),
          (party_add_members, "$current_town", "trp_mercenary_swordsman", ":random"),
          (store_random_in_range, ":random", 0, ":player_leveld2"),
          (party_add_members, "$current_town", "trp_hired_blade", ":random"),
        (else_try),
          (party_set_banner_icon, "$current_town", 0),
          (party_get_num_companion_stacks, ":num_stacks","$current_town"),
          (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_size, ":stack_size","$current_town",":i_stack"),
            (val_div, ":stack_size", 2),
            (party_stack_get_troop_id, ":troop_id", "$current_town", ":i_stack"),
            (party_remove_members, "$current_town", ":troop_id", ":stack_size"),
          (try_end),
          (store_random_in_range, ":random",":player_leveld2", ":player_levelx2"),
          (party_add_members, "$current_town", "trp_townsman", ":random"),
          (store_random_in_range, ":random",0, ":player_level"),
          (party_add_members, "$current_town", "trp_watchman", ":random"),
        (try_end),
      ]),

      ("center_refresh",
      [(party_slot_eq, "$current_town", slot_party_type, spt_town),],
      "Refresh merchants (global).",
      [
        # (party_get_slot, g.selected_troop,"$current_town", slot_town_weaponsmith),
        (call_script, "script_refresh_center_weaponsmiths"),
        # (party_get_slot, g.selected_troop,"$current_town", slot_town_armorer),
        (call_script, "script_refresh_center_armories"),
        # (party_get_slot, g.selected_troop,"$current_town", slot_town_horse_merchant),
        (call_script, "script_refresh_center_stables"),
        # (party_get_slot, g.selected_troop,"$current_town", slot_town_merchant),
        (call_script, "script_refresh_center_inventories"),
        # (assign, g.selected_troop, -1),
      ]),
      
      ("village_refresh",
      [(party_slot_eq, "$current_town", slot_party_type, spt_village),],
      "Refresh village goods.",
      [
        (call_script, "script_refresh_village_merchant_inventory", "$current_town"),
      ]),

      ("village_recruits",
      [(party_slot_eq, "$current_town", slot_party_type, spt_village),],
      "Refresh recruits.",
      [
        (call_script, "script_update_volunteer_troops_in_village", "$current_town"),
      ]),
      ("center_recruits",
      [(party_slot_eq, "$current_town", slot_party_type, spt_town),],
      "Refresh mercenaries.",
      [
        (store_random_in_range, ":troop_no", mercenary_troops_begin, mercenary_troops_end),
        (party_set_slot, "$current_town", slot_center_mercenary_troop_type, ":troop_no"),
        (store_random_in_range, ":amount", 3, 8),
        (try_begin),
          (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
          (store_character_level, ":level", "trp_player"), #increase limits a little bit as the game progresses.
          (store_add, ":level_factor", 80, ":level"),
          (val_mul, ":amount", ":level_factor"),
          (val_div, ":amount", 80),
        (try_end),
        (party_set_slot, "$current_town", slot_center_mercenary_troop_amount, ":amount"),
      ]),

      ("go_back",
      [(neg|party_slot_eq,"$current_town",slot_party_type, spt_village),],
      "Go Back.",
      [
        (jump_to_menu,"mnu_town"),
      ]),

      ("continue",
      [(party_slot_eq,"$current_town",slot_party_type, spt_village),],
      "Continue.",
      [
        (jump_to_menu,"mnu_village"),
      ]),
    ]),
    
  (
    "town_cheats_2",0,
    "Select an option to interact with the center itself. Prosperity is {reg1}, Relation is {reg2}, there are {reg3} parties in town.",
    "none",[
        (call_script, "script_set_town_picture"),
        (party_get_slot, reg1, "$current_town", slot_town_prosperity),
        (party_get_slot, reg2, "$current_town", slot_center_player_relation),
        
        (assign, ":count", 0),
        (try_for_parties, ":party_no"),
          (party_is_active, ":party_no"),
          (party_is_in_town, ":party_no", "$current_town"),
          (val_add, ":count", 1),
        (try_end),
        (assign, reg3, ":count"),
      ],
      [
          ("page",
          [],
          "Previous Page.",
          [
            (jump_to_menu, "mnu_town_cheats"),
          ]),

          ("toggle_state",
          [(party_slot_eq, "$current_town", slot_party_type, spt_village),
           (party_get_slot, reg1, "$current_town", slot_village_state),],
          "{reg1?Restore:Raze} this village.",
          [
            (try_begin),
              (party_slot_eq, "$current_town", slot_village_state, svs_normal),
              (call_script, "script_village_set_state", "$current_town", svs_looted),
            (else_try),
              (call_script, "script_village_set_state", "$current_town", svs_normal),
            (try_end),
          ]),

          ("village_manage",
          [], "Manage this center.",
          [
           (assign, "$g_next_menu", "mnu_town_cheats_2"),
           (jump_to_menu, "mnu_center_manage"),
          ]),
          ("increase_rel",
          [],
          "Increase Relation.",
          [
            (try_begin),
              (this_or_next|key_is_down, key_left_shift),
              (key_is_down, key_right_shift),
              (call_script, "script_change_player_relation_with_center", "$current_town", 1),
            (else_try),
              (call_script, "script_change_player_relation_with_center", "$current_town", 5),
            (try_end),
          ]),

          ("decrease_rel",
          [],
          "Decrease Relation.",
          [
            (try_begin),
              (this_or_next|key_is_down, key_left_shift),
              (key_is_down, key_right_shift),
              (call_script, "script_change_player_relation_with_center", "$current_town", -1),
            (else_try),
              (call_script, "script_change_player_relation_with_center", "$current_town", -5),
            (try_end),
          ]),

          ("increase_prosp",
          [],
          "Increase Prosperity.",
          [
            (try_begin),
              (this_or_next|key_is_down, key_left_shift),
              (key_is_down, key_right_shift),
              (call_script, "script_change_center_prosperity", "$current_town", 1),
            (else_try),
              (call_script, "script_change_center_prosperity", "$current_town", 5),
            (try_end),
          ]),

          ("decrease_prosp",
          [],
          "Decrease Prosperity.",
          [
            (try_begin),
              (this_or_next|key_is_down, key_left_shift),
              (key_is_down, key_right_shift),
              (call_script, "script_change_center_prosperity", "$current_town", -1),
            (else_try),
              (call_script, "script_change_center_prosperity", "$current_town", -5),
            (try_end),
          ]),

          ("castle_cheat_interior",
          [(neg|party_slot_eq, "$current_town", slot_party_type, spt_village)],
          "{!}Interior.",
          [
            (set_jump_mission,"mt_ai_training"),
            (party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
            (jump_to_scene,":castle_scene"),
            (change_screen_mission),
          ]),

          ("castle_cheat_town_exterior",
          [],
          "{!}Exterior.",
          [
            # (try_begin),
              # (party_slot_eq, "$current_town",slot_party_type, spt_castle),
              # (party_get_slot, ":scene", "$current_town", slot_castle_exterior),
            # (else_try),
              # (party_get_slot, ":scene", "$current_town", slot_town_center),
            # (try_end),
            (party_get_slot, ":scene", "$current_town", slot_town_center),
            (set_jump_mission,"mt_ai_training"),
            (jump_to_scene,":scene"),
            (change_screen_mission),
          ]),

          ("castle_cheat_dungeon",
          [(neg|party_slot_eq, "$current_town", slot_party_type, spt_village)],
          "{!}Prison.",
          [
            (set_jump_mission,"mt_ai_training"),
            (party_get_slot, ":castle_scene", "$current_town", slot_town_prison),
            (jump_to_scene,":castle_scene"),
            (change_screen_mission),
          ]),

          ("castle_cheat_town_walls",
          [
            (party_slot_eq,"$current_town",slot_party_type, spt_town),
          ],
          "{!}Town Walls.",
          [
            (party_get_slot, ":scene", "$current_town", slot_town_walls),
            (set_jump_mission,"mt_ai_training"),
            (jump_to_scene,":scene"),
            (change_screen_mission),
          ]),

          ("cheat_town_start_siege",
          [ (neg|party_slot_eq, "$current_town", slot_party_type, spt_village),
            (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
            (lt, "$g_encountered_party_2", 1),
            # (call_script, "script_party_count_fit_for_battle","p_main_party"),
            # (gt, reg(0), 1),
            # (try_begin),
              # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
              # (assign, reg6, 1),
            # (else_try),
              # (assign, reg6, 0),
            # (try_end),
          ],
          "Besiege the center...",
          [
            (assign,"$g_player_besiege_town","$g_encountered_party"),
            (jump_to_menu, "mnu_castle_besiege"),
          ]),

          ("center_reports",
          [],
          "Show reports.",
          [
            (jump_to_menu,"mnu_center_reports"),
          ]),

          ("sail_from_port",
          [
            (party_slot_eq,"$current_town",slot_party_type, spt_town),
            (party_get_position, pos1, "$current_town"),
            (map_get_water_position_around_position, pos2, pos1, 6),
            (get_distance_between_positions, ":dist", pos1, pos2),
            (lt, ":dist", 6),
            # (party_set_position, "p_main_party", pos2),
            (ge, "$cheat_mode", 1),
            #(party_slot_eq,"$current_town",slot_town_near_shore, 1),
          ],
          "{!}Sail from port.",
          [
            (assign, "$g_player_icon_state", pis_ship),
            (party_set_flags, "p_main_party", pf_is_ship, 1),
            # (party_get_position, pos1, "p_main_party"),
            # (map_get_water_position_around_position, pos2, pos1, 6),
            (party_set_position, "p_main_party", pos2),
            (assign, "$g_main_ship_party", -1),
            (change_screen_return),
          ]),
          
          
          ("go_back",
          [(neg|party_slot_eq,"$current_town",slot_party_type, spt_village),],
          "Go Back.",
          [
            (jump_to_menu,"mnu_town"),
          ]),

          ("continue",
          [(party_slot_eq,"$current_town",slot_party_type, spt_village),],
          "Continue.",
          [
            (jump_to_menu,"mnu_village"),
          ]),
      ]
    ),
  
  #rename_court to set a capital
  (
    "rename_court",0,
    "{!}This menu jumps to the rename presentation",
    "none",
    [
    # (call_script, "script_change_player_right_to_rule", 1), #handled in dialogues
    (assign, reg0, "$temp"),
    (display_message, "@{reg0}"),
    (try_begin),
        #(eq, "$temp", 1), #avoid menus getting stuck
        (jump_to_menu, "mnu_auto_return_to_map"),
    (try_end),
    (assign, "$g_presentation_state", rename_center),
    (call_script, "script_add_log_entry", logent_player_renamed_capital, "trp_player", "$g_player_court", -1, -1),
    (assign, "$temp", 1),
    (start_presentation, "prsnt_name_kingdom"),

    ],
    []),
  ( #export/import from prsnt_companion_overview
    "export_import", mnf_enable_hot_keys,
    "Press C to access {s1}'s character screen and then the statistics button on the bottom left.",
    "none",
    [
    (set_background_mesh, "mesh_pic_mb_warrior_1"),
    # # (set_player_troop, "trp_player"),
    # (change_screen_view_character),
    # # (change_screen_return),
    # (assign, "$talk_context", tc_town_talk),
    # (start_map_conversation, "$g_player_troop"),
    (set_player_troop, "$g_player_troop"),
    (str_store_troop_name_plural, s1, "$g_player_troop"),
    ],
    [
      ("rename",
      [],
      "I never liked the name {s1}...",
      [
        (assign, "$g_presentation_state", rename_companion),
        (start_presentation, "prsnt_name_kingdom"),
      ]),
      
      ("display_slots",
      [(ge, "$cheat_mode", 1)], "Show me all your secrets...",
      [ 
        (assign, "$g_talk_troop", "$g_player_troop"),
        (jump_to_menu, "mnu_display_troop_slots"),
      ]),
      ("continue",
      [],
      "Continue...",
      [ 
        (set_player_troop, "trp_player"),
        (jump_to_menu, "$g_next_menu"),
      ]),
    ]
  ),
  
  ( #helper menu to show all slots
    "display_party_slots", menu_text_color(0xFF990000),
    "{s1}",
    "none",
    [
    (set_background_mesh, "mesh_pic_messenger"),
    (str_store_party_name, s1, "$g_encountered_party"),
    (assign, reg1, "$g_encountered_party"),
    (assign, "$pout_party", 0),
    (try_for_parties, ":party_no"),
      # (assign, "$pout_party", ":party_no"),
      (party_is_active, ":party_no"),
      (gt, ":party_no", "$pout_party"),
      (assign, "$pout_party", ":party_no"),
    (try_end),
    (assign, reg2, "$pout_party"),
    (str_store_string, s1, "@{reg1}/{reg2}: {s1}"),
    #There's probably too many slots (and conflicting ones) to actually output the slot names to string
    (try_for_range, reg1, 0, 1000), #slot_town_trade_good_productions_begin
      (party_get_slot, reg0, "$g_encountered_party", reg1),
      (neq, reg0, 0), #if there's a value in here
      (str_store_string, s1, "@{s1}^{reg1}: {reg0}"),
    (try_end),
    
    # Process the prev and next parties
    # (assign, "$diplomacy_var",  "$g_encountered_party"),
    # (assign, "$diplomacy_var2", "$g_encountered_party"),
    # (try_for_parties, ":party_no"),
      # (party_is_active, ":party_no"),
      # (eq, "$diplomacy_var2", "$g_encountered_party"),
      # (try_begin), #find last party before current one
        # (lt, ":party_no", "$g_encountered_party"),
        # (assign, "$diplomacy_var", ":party_no"),
      # (else_try), #find first party after current one
        # (gt, ":party_no", "$g_encountered_party"),
        # (assign, "$diplomacy_var2", ":party_no"),
      # (try_end),
    # (try_end),
    (store_sub, "$diplomacy_var",  "$g_encountered_party", 1),
    (store_add, "$diplomacy_var2", "$g_encountered_party", 1),
    (try_begin), #find first
      (neg|party_is_active, "$diplomacy_var"),
      (assign, "$diplomacy_var", 0),
      (assign, ":end", "$g_encountered_party"),
      (try_for_range_backwards, ":party_no", 0, ":end"),
        (party_is_active, ":party_no"),
        (lt, ":party_no", "$g_encountered_party"),
        (gt, ":party_no", "$diplomacy_var"),
        (assign, "$diplomacy_var", ":party_no"),
        (assign, ":end", 0),
      (try_end),
    (try_end),
    # (val_max, "$diplomacy_var", "p_main_party"), #lock as first party
    
    (try_begin), #look for next
      (neg|party_is_active, "$diplomacy_var2"),
      (assign, "$diplomacy_var2", "$pout_party"), #this was previous checked as highest party
      (assign, ":end", "$pout_party"),
      (try_for_range, ":party_no", "$g_encountered_party", ":end"),
        (party_is_active, ":party_no"),
        (gt, ":party_no", "$g_encountered_party"),
        (le, ":party_no", "$diplomacy_var2"),
        (assign, "$diplomacy_var2", ":party_no"),
        (assign, ":end", "$g_encountered_party"),
      (try_end),
    (try_end),
    
    ],
    [
    
      ("notes",
      [(is_between, "$g_encountered_party", centers_begin, centers_end),],
      "View Notes.",
      [
        (change_screen_notes, 3, "$g_encountered_party"),
      ]),
      ("previous",
      [
        (ge, "$diplomacy_var", "p_main_party"),
        (lt, "$diplomacy_var", "$g_encountered_party"),
        (party_is_active, "$diplomacy_var"),
        (str_store_party_name, s2, "$diplomacy_var"),
      ],
      "Previous Party ({s2}).",
      [
        # (jump_to_menu, "mnu_party_cheat"),
        (assign, "$g_encountered_party", "$diplomacy_var"),
      ]),
      
      ("next",
      [
        (le, "$diplomacy_var2", "$pout_party"),
        (gt, "$diplomacy_var2", "$g_encountered_party"),
        (party_is_active, "$diplomacy_var2"),
        (str_store_party_name, s2, "$diplomacy_var2"),
      ],
      "Next Party ({s2}).",
      [
        (assign, "$g_encountered_party", "$diplomacy_var2"),
      ]),
      
      
      ("change",
      [],
      "Modify slots.",
      [
        (assign, "$g_presentation_state", 0), #start off at first slot
        (assign, "$g_presentation_input", rename_center),
        (start_presentation, "prsnt_modify_slots"),
      ]),
    
      ("continue",
      [],
      "Continue.",
      [
        # (jump_to_menu, "mnu_party_cheat"),
        (assign, "$new_encounter", 2),
        (set_encountered_party, "$g_encountered_party"),
        (call_script, "script_game_event_party_encounter", "$g_encountered_party", -1),
        # (change_screen_map),
        # (start_encounter, "$g_encountered_party"),
      ]),
    ]
  ),
  ( #exchange cheat from cmenu_encounter
    "party_cheat",0,
    "{!}{s10} is a {reg10?holding:member} of {s11} with relation {reg11}{reg6? (player relation {reg6}):} at ({reg8},{reg9}) {reg7} km away.^\
 It has {reg12}/{reg13} soldiers {reg13?in {reg14} stacks:}{reg15? and {reg15} prisoners in {reg16} stacks:{reg17? and {reg17} attached parties:}.^\
 AI Behaviour is {s13}{reg18? (currently {s14}):}, Object is {s15}{reg19? (currently {s16}):} at ({reg20},{reg21})",
    "none",
    [
    (assign, "$new_encounter", 0), #this undoes the cheat toggle global immediately
    (set_fixed_point_multiplier, 1000),
    #basic world info first line
    (str_store_party_name, s10, "$g_encountered_party"),
    (str_store_faction_name, s11, "$g_encountered_party_faction"),
    (try_begin),
      (this_or_next|is_between, "$g_encountered_party", centers_begin, centers_end),
      (is_between, "$g_encountered_party", training_grounds_begin, training_grounds_end),
      (assign, reg10, 1),
      (party_get_slot, reg6, "$g_encountered_party", slot_center_player_relation),
    (else_try),
      (assign, reg10, 0),
      (try_begin),
        (party_stack_get_troop_id, ":leader_troop", "$g_encountered_party", 0),
        (troop_is_hero, ":leader_troop"),
        (call_script, "script_troop_get_relation_with_troop", ":leader_troop", "trp_player"),
        (assign, reg6, reg0),
      (try_end),
    (try_end),
    (party_get_position, pos1, "$g_encountered_party"),
    (position_get_x, reg8, pos1),
    (position_get_y, reg9, pos1),
    (assign, reg11, "$g_encountered_party_relation"),
    (store_distance_to_party_from_party, reg7, "$g_encountered_party", "p_main_party"),
    
    #party composition second line
    (call_script, "script_party_count_fit_for_battle", "$g_encountered_party"),
    (assign, reg12, reg0),
    (party_get_num_companions, reg13, "$g_encountered_party"),
    (party_get_num_companion_stacks, reg14, "$g_encountered_party"),
    (party_get_num_prisoners, reg15, "$g_encountered_party"),
    (party_get_num_prisoner_stacks, reg16, "$g_encountered_party"),
    (party_get_num_attached_parties, reg17, "$g_encountered_party"),
    
    #AI info third line
    (get_party_ai_behavior, ":behaviour", "$g_encountered_party"),
    (val_add, ":behaviour", "str_ai_bhvr_hold"),
    (str_store_string, s13, ":behaviour"),
    (get_party_ai_current_behavior, ":cur_behaviour", "$g_encountered_party"),
    (val_add, ":cur_behaviour", "str_ai_bhvr_hold"),
    (try_begin),
      (neq, ":cur_behaviour", ":behaviour"),
      (str_store_string, s14, ":cur_behaviour"),
      (assign, reg18, 1),
    (else_try),
      (str_clear, s14),
      (assign, reg18, 0),
    (try_end),
    
    (get_party_ai_object, ":object", "$g_encountered_party"),
    (try_begin),
      (this_or_next|le, ":object", 0),
      (neg|party_is_active, ":object"),
      (str_store_string, s15, "str_dplmc_none"),
    (else_try),
      (str_store_party_name, s15, ":object"),
    (try_end),
    (get_party_ai_current_object, ":cur_object", "$g_encountered_party"),
    (assign, reg19, 1),
    (try_begin),
      (eq, ":cur_object", ":object"),
      (assign, reg19, 0), #disable display
    (else_try),
      (this_or_next|le, ":cur_object", 0),
      (neg|party_is_active, ":cur_object"),
      (str_store_string, s16, "str_dplmc_none"),
    (else_try),
      (str_store_party_name, s16, ":cur_object"),
    (try_end),
    
    (party_get_ai_target_position, pos2, "$g_encountered_party"),
    (position_get_x, reg20, pos2),
    (position_get_y, reg21, pos2),

    #grab the background mesh stuff
    (try_begin),
      (is_between, "$g_encountered_party", centers_begin, centers_end),
      (assign, "$current_town", "$g_encountered_party"),
      (call_script, "script_set_town_picture"),
    (else_try),
      (eq, "$g_encountered_party_template", "pt_looters"),
      (set_background_mesh, "mesh_pic_bandits"),
    (else_try),
      (eq, "$g_encountered_party_template", "pt_mountain_bandits"),
      (set_background_mesh, "mesh_pic_mountain_bandits"),
    (else_try),
      (eq, "$g_encountered_party_template", "pt_steppe_bandits"),
      (set_background_mesh, "mesh_pic_steppe_bandits"),
    (else_try),
      (eq, "$g_encountered_party_template", "pt_taiga_bandits"),
      (set_background_mesh, "mesh_pic_steppe_bandits"),
    (else_try),
      (eq, "$g_encountered_party_template", "pt_sea_raiders"),
      (set_background_mesh, "mesh_pic_sea_raiders"),
    (else_try),
      (eq, "$g_encountered_party_template", "pt_forest_bandits"),
      (set_background_mesh, "mesh_pic_forest_bandits"),
    (else_try),
      (this_or_next|eq, "$g_encountered_party_template", "pt_deserters"),
      (eq, "$g_encountered_party_template", "pt_routed_warriors"),
      (set_background_mesh, "mesh_pic_deserters"),
    #SB : dplmc party templates
    (else_try),
      (eq, "$g_encountered_party_template", "pt_center_reinforcements"),
      (set_background_mesh, "mesh_pic_recruits"),
    (else_try),
      (eq, "$g_encountered_party_template", "pt_kingdom_hero_party"),
      (party_stack_get_troop_id, ":leader_troop", "$g_encountered_party", 0),
      (ge, ":leader_troop", 1),
      (troop_get_slot, ":leader_troop_faction", ":leader_troop", slot_troop_original_faction),
      (try_begin),
        (eq, ":leader_troop_faction", fac_kingdom_1),
        (set_background_mesh, "mesh_pic_swad"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_2),
        (set_background_mesh, "mesh_pic_vaegir"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_3),
        (set_background_mesh, "mesh_pic_khergit"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_4),
        (set_background_mesh, "mesh_pic_nord"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_5),
        (set_background_mesh, "mesh_pic_rhodock"),
      (else_try),
        (eq, ":leader_troop_faction", fac_kingdom_6),
        (set_background_mesh, "mesh_pic_sarranid_encounter"),
      (try_end),
    (try_end),
    ],
    [
    
      ("talk",
      [],
      "Encounter the party.",
      [
        (call_script, "script_game_event_party_encounter", "$g_encountered_party", -1),
        # (change_screen_map),
      ]),
      
      ("slots",
      [],
      "Dump all slot values.",
      [ #g_encountered_party is the input
        (jump_to_menu, "mnu_display_party_slots"),
      ]),

      
      ("reinf",
      [],
      "Reinforce party.",
      [
      
      (try_begin),
        (is_between, "$g_encountered_party", villages_begin, villages_end),
        # (party_add_template, "$g_encountered_party", "pt_village_defenders"),
        (call_script, "script_refresh_village_defenders", "$g_encountered_party"),
      (else_try),
        (is_between, "$g_encountered_party_faction", kingdoms_begin, kingdoms_end),
        (call_script, "script_cf_reinforce_party", "$g_encountered_party"),
      (else_try), #if the above falls through by not reinforcing we grab a random template
        (this_or_next|eq, "$g_encountered_party_faction", "fac_deserters"),
        (is_between, "$g_encountered_party_faction", npc_kingdoms_begin, kingdoms_end),
        (party_stack_get_troop_id, ":troop_id", "$g_encountered_party", 0),
        (store_faction_of_troop, "$g_encountered_party_faction", ":troop_id"),
        (store_random_in_range, ":slot_no", slot_faction_reinforcements_a, slot_faction_num_armies),
        (faction_get_slot, ":party_template", "$g_encountered_party_faction", ":slot_no"),
        (party_add_template, "$g_encountered_party", ":party_template"),
      (else_try),
        # (this_or_next|eq, "$g_encountered_party_faction", "fac_outlaws"),
        # (is_between, "$g_encountered_party_faction", bandit_factions_begin, bandit_factions_end),
        (party_get_template_id, ":party_template", "$g_encountered_party"),
        (party_add_template, "$g_encountered_party", ":party_template"),
      (try_end),
      ]),
      
    ("exp",
      [],
      "Upgrade party.",
      [
        (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
        (party_clear, "p_temp_party"),
         (try_for_range_backwards, ":stack", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":id", "$g_encountered_party", ":stack"),
            (try_begin),
              (party_stack_get_size, ":size", "$g_encountered_party", ":stack"),
              # (call_script, "script_game_get_upgrade_xp", ":id"),
              # (store_mul, ":xp", reg0, ":size"),
              (try_begin),
                (troop_is_hero, ":id"),
                (store_character_level, ":level", ":id"),
                (assign, ":end", 100),
                (try_begin), #assign block of exp
                  (le, ":level", 10),
                  (assign, ":xp", 100),
                (else_try),
                  (le, ":level", 25),
                  (assign, ":xp", 1000),
                (else_try), #most people stop before level 30
                  (le, ":level", 35),
                  (assign, ":xp", 10000),
                (else_try),
                  (le, ":level", 50),
                  (assign, ":xp", 30000),
                (else_try),
                  (le, ":level", 60),
                  (assign, ":xp", 1000000),
                (else_try), #good luck, level caps at 63
                  (assign, ":xp", 10000000),
                (try_end),
                (try_for_range, ":unused", 0, ":end"),
                  (party_add_xp_to_stack, "$g_encountered_party", ":stack", ":xp"),
                  (add_xp_to_troop, 1, ":id"), #this actually upgrades the level
                  # (add_xp_as_reward, ":xp"),
                  (store_character_level, ":cur_level", ":id"),
                  (lt, ":level", ":cur_level"), #done
                  (assign, ":end", 0),
                (try_end),
              (else_try),
                (troop_get_upgrade_troop, ":upgrade_troop", ":id", 0),
                (gt, ":upgrade_troop", 0),
                (troop_get_upgrade_troop, ":upgrade_2", ":id", 1),
                (try_begin),
                  (gt, ":upgrade_2", 0),
                  (store_random_in_range, ":random_no", 0, 2),
                  (eq, ":random_no", 0),
                  (assign, ":upgrade_troop", ":upgrade_2"),
                (try_end),
                (party_add_members, "p_temp_party", ":upgrade_troop", ":size"),
                (party_stack_get_num_wounded, ":num_wounded", "$g_encountered_party", ":stack"),
                (party_wound_members, "p_temp_party", ":upgrade_troop", ":num_wounded"),
                (party_remove_members, "$g_encountered_party", ":id", ":size"),
                # (party_add_xp_to_stack, "$g_encountered_party", ":stack", ":xp"),
              (try_end),
            (try_end),
         (try_end),
         (call_script, "script_party_add_party_companions", "$g_encountered_party", "p_temp_party"),
      ]),

      ("wound",
      [],
      "Wound party.",
      [
        (call_script, "script_party_wound_all_members", "$g_encountered_party"),
      ]),
    ("heal",
      [],
      "Heal party.",
      [
        (call_script, "script_party_heal_all_members_aux", "$g_encountered_party"),
      ]),

     ("rename",[],"Rename party.",
       [(assign, "$g_presentation_state", rename_party),
       # (assign, "$g_encountered_party", "p_main_party"),
       (start_presentation, "prsnt_name_kingdom"),
       ]
       ),
      ("exchange",
      [],
      "Exchange with party.",
      [
        (change_screen_exchange_members,1),
      ]),
      
      ("bandits",
      [(is_between, "$g_encountered_party", centers_begin, centers_end),],
      "Spawn bandits nearby.",
      [
      (set_spawn_radius, 25),
      (try_for_range, ":unused", 0, 10),
        (store_random_in_range, ":party_template", bandit_party_templates_begin, bandit_party_templates_end),
        (spawn_around_party, "$g_encountered_party", ":party_template"),
      (try_end),
      ]),
      
      ("leave",[],"Leave.",
       [
        (assign, "$g_leave_encounter", 1),
        (change_screen_return),
       ]
      ),
    ]
  ),
  

  ( #helper menu to show all troop slots
    "display_troop_slots", menu_text_color(0xFF009900),
    "{s1}^{s2}",
    "none",
    [
    # (set_background_mesh, "mesh_pic_cattle"),
    (assign, reg1, "$g_talk_troop"),
    (str_store_troop_name, s1, "$g_talk_troop"),
    (str_store_troop_name_plural, s2, "$g_talk_troop"),
    (store_troop_faction, ":faction_no", "$g_talk_troop"),
    (str_store_faction_name, s3, ":faction_no"),
    (troop_get_class, ":class", "$g_talk_troop"),
    (str_store_class_name, s4, ":class"),
    (store_character_level, reg2, "$g_talk_troop"),
    (str_store_string, s1, "@{reg1}: {s1}, {s2} classified as level {reg2} {s3} {s4}"),
    (try_begin), #upgrades
      (neg|troop_is_hero, "$g_talk_troop"),
      (try_begin),
        (troop_get_upgrade_troop, ":upgrade_0", "$g_talk_troop", 0),
        (gt, ":upgrade_0", 0),
        (str_store_troop_name_plural, s2, ":upgrade_0"),
        (str_store_string, s1, "@{s1}^becomes {s2}"),
        (troop_get_upgrade_troop, ":upgrade_1", "$g_talk_troop", 1),
        (gt, ":upgrade_1", 0),
        (str_store_troop_name_plural, s2, ":upgrade_1"),
        (str_store_string, s1, "@{s1} and {s2}"),
      (try_end),
      
      (call_script, "script_game_get_upgrade_xp", "$g_talk_troop"),
      (assign, reg10, reg0),
      (call_script, "script_game_get_upgrade_cost", "$g_talk_troop"),
      (assign, reg11, reg0),
      (str_store_string, s1, "@{s1}^costs {reg11} to upgrade with {reg10} xp"),
      
      (call_script, "script_game_get_troop_wage", "$g_talk_troop", -1),
      (assign, reg12, reg0),
      (call_script, "script_game_get_join_cost", "$g_talk_troop"),
      (assign, reg13, reg0),
      
      #this is because this script ties a global to the price
      (assign, ":troop_no", "$g_talk_troop"),
      (assign, "$g_talk_troop", ransom_brokers_begin),
      (call_script, "script_game_get_prisoner_price", ":troop_no"),
      (assign, reg14, reg0),
      (assign, "$g_talk_troop", ":troop_no"),
      
      (str_store_string, s1, "@{s1}^wage of {reg12}, buy costs {reg13} sell costs {reg14}"),
    (else_try),
      (troop_is_hero, "$g_talk_troop"),
      (str_store_string, s2, "@hero"),
      (call_script, "script_cf_troop_debug_range", "$g_talk_troop", s2, 0),
      (str_store_string, s1, "@{s1} is a {s2}"),
      (try_begin),
        (store_troop_gold, ":gold", "$g_talk_troop"),
        (gt, ":gold", 0),
        (assign, reg1, ":gold"),
        (str_store_string, s1, "@{s1} with {reg1} gold"),
      (try_end),
      # (try_begin),
        # (store_partner_quest, ":quest_no"),
        # (ge, ":quest_no", 0),
        # (str_store_quest_name, s2, ":quest_no"),
        # (str_store_string, s1, "@{s1} tasking you with {s2}"),
      # (try_end),
    (try_end),
    
    (str_clear, s2),
    (try_for_range, reg1, 0, 1000),
      (troop_get_slot, reg0, "$g_talk_troop", reg1),
      (neq, reg0, 0), #if there's a value in here
      (str_store_string, s2, "@{s2}^{reg1}: {reg0}"),
    (try_end),
    
    (set_fixed_point_multiplier, 100),
    (init_position, pos0),
    (try_begin),
      (str_is_empty, s2),
      (position_set_x, pos0, 17),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 100),
    (else_try),
      (position_set_x, pos0, 60),
      (position_set_y, pos0, 20),
      (position_set_z, pos0, 100),
    (try_end),
    (store_mul, ":troop_no", "$g_talk_troop", 2),
    (set_game_menu_tableau_mesh, "tableau_game_party_window", ":troop_no", pos0),
    ],
    [
    
    #So apparently this one needs to re-jump to the menu
      ("notes",
      [(is_between, "$g_talk_troop", heroes_begin, heroes_end),],
      "View Notes.",
      [
        (change_screen_notes, 1, "$g_talk_troop"),
      ]),

      ("prev_range",
      [
        (gt, "$g_talk_troop", "trp_player"),
        (call_script, "script_cf_troop_debug_range", "$g_talk_troop", s3, -1),
        (str_store_troop_name, s3, reg0),
      ],
      "Head ({s3}).",
      [
        (call_script, "script_cf_troop_debug_range", "$g_talk_troop", s0, -1),
        (assign, "$g_talk_troop", reg0),
        (jump_to_menu, "mnu_display_troop_slots"),
      ]),
      
      ("next_range",
      [
        (call_script, "script_cf_troop_debug_range", "$g_talk_troop", s3, 1),
        (str_store_troop_name, s3, reg0),
      ],
      "Tail ({s3}).",
      [
        (call_script, "script_cf_troop_debug_range", "$g_talk_troop", s0, 1),
        (assign, "$g_talk_troop", reg0),
        (jump_to_menu, "mnu_display_troop_slots"),
      ]),
      
      ("prev",
      [
        (gt, "$g_talk_troop", "trp_player"),
        (store_sub, ":troop_no", "$g_talk_troop", 1),
        (str_store_troop_name, s2, ":troop_no"),
      ],
      "Previous Troop ({s2}).",
      [
        (val_sub, "$g_talk_troop", 1),
        (jump_to_menu, "mnu_display_troop_slots"),
      ]),
      
      ("next",
      [
        (lt, "$g_talk_troop", "trp_dplmc_recruiter"), #last troop apparently
        (store_add, ":troop_no", "$g_talk_troop", 1),
        (str_store_troop_name, s2, ":troop_no"),
      ],
      "Next Troop ({s2}).",
      [
        (val_add, "$g_talk_troop", 1),
        (jump_to_menu, "mnu_display_troop_slots"),
      ]),
      
      ("rename",
      [],
      "Rename.",
      [
        (assign, "$g_player_troop", "$g_talk_troop"),
        (assign, "$g_presentation_state", rename_companion),
        (start_presentation, "prsnt_name_kingdom"),
      ]),
      
      ("change",
      [],
      "Modify slots.",
      [
        (assign, "$g_presentation_state", 0), #start off at first slot
        (assign, "$g_presentation_input", rename_companion),
        (start_presentation, "prsnt_modify_slots"),
      ]),
      
      ("inventory",
      [],
      "Modify inventory.",
      [
        (change_screen_loot, "$g_talk_troop"),
      ]),
    
       ("gender",[], "Toggle gender.",
         [
           (try_begin),
             (eq, "$g_talk_troop", "trp_player"),
             (store_sub, "$character_gender", tf_female, "$character_gender"),
             (troop_set_type, "trp_player", "$character_gender"),
           (else_try),
             (troop_get_type, ":gender", "$g_talk_troop"),
             (store_sub, ":gender", tf_female, ":gender"),
             (troop_set_type, "$g_talk_troop", ":gender"),
           (try_end),
         ]
       ),

      ("continue",
      [],
      "Continue.",
      [
        (change_screen_map),
      ]),
    ]
  ),
  
  (
    "dplmc_choose_disguise", 0,
    "You are about to sneak into {s1}. Make sure you don't bring suspicious items or excess denars that might be confiscated. {s2}",
    "none",
    [
    
         (troop_get_inventory_capacity, ":inv_cap", "trp_random_town_sequence"),
         (assign, ":count", 0),
         (try_for_range, ":i_slot", ek_food + 1, ":inv_cap"),
           (troop_get_inventory_slot, ":cur_item", "trp_random_town_sequence", ":i_slot"),
           (gt, ":cur_item", -1),
           #(assign, reg3, ":cur_item"),
           #(display_message, "@{reg3}"),
           (val_add, ":count", 1),
         (try_end),
         # (assign, reg0, ":count"),
         # (assign, reg1, "$temp"),
         # (display_message, "@{reg0} , {reg1}"),
         (try_begin),
            (gt, ":count", "$temp"),
            #put stuff back
            (set_show_messages, 0), #move all gold
            (call_script, "script_move_inventory_and_gold", "trp_random_town_sequence", "trp_player", -1),
            (set_show_messages, 1),
            (display_message, "@You cannot bring that many items with you. Your items have been returned to your inventory."),
         (try_end),
        
        (str_store_party_name, s1, "$current_town"),
        #build text
        (try_begin),
          (eq, "$sneaked_into_town", disguise_none),
          (str_store_string, s2, "@Select a suitable disguise for this occasion."),
          (assign, "$temp", 0),
        (else_try),
          (eq, "$sneaked_into_town", disguise_pilgrim),
          (str_store_string, s2, "@As a poor pilgrim with a stout stick and a few tricks up your sleeve, you will be able to blend in with the crowds but not bring much of value with you."),
          (assign, "$temp", 6),
        (else_try),
          (eq, "$sneaked_into_town", disguise_farmer),
          (str_store_string, s2, "@As a farmer, you will be able to a wrangle livestock and smuggle articles of food through."),
          (assign, "$temp", 15),
        (else_try),
          (eq, "$sneaked_into_town", disguise_hunter),
          (str_store_string, s2, "@As a hunter, provisions and raw goods are expected as well as horseflesh."),
          (assign, "$temp", 12),
        (else_try),
          (eq, "$sneaked_into_town", disguise_guard),
          (str_store_string, s2, "@As a caravan guard, you will be able to bear weapons but bring only a few personal belongings."),
          (assign, "$temp", 6),
        (else_try),
          (eq, "$sneaked_into_town", disguise_merchant),
          (str_store_string, s2, "@As a merchant, you will be able to bring any assortment of goods."),
          (assign, "$temp", 32),
        (else_try),
          (eq, "$sneaked_into_town", disguise_bard),
          (str_store_string, s2, "@As a bard, you will be allowed some personal possessions and your instrument."),
          (assign, "$temp", 9),
        (try_end),
        (set_fixed_point_multiplier, 100),
        (init_position, pos0),
        (try_begin),
          (str_is_empty, s2),
          (position_set_x, pos0, 17),
          (position_set_y, pos0, 30),
          (position_set_z, pos0, 100),
        (else_try),
          (position_set_x, pos0, 60),
          (position_set_y, pos0, 20),
          (position_set_z, pos0, 100),
        (try_end),
        (set_game_menu_tableau_mesh, "tableau_game_inventory_window", "trp_player", pos0),
        (troop_get_slot, "$temp_2", "trp_player", slot_troop_player_disguise_sets),
    ],
    [
      ("continue",
      [(gt, "$temp", 0),
       (assign, reg1, "$temp"),],
      "Choose up to {reg1} items to bring.",
      [
        (change_screen_loot, "trp_random_town_sequence"),
      ]),
      
      ("continue",
      [(neq, "$sneaked_into_town", disguise_none)],
      "Select how much gold to carry.",
      [
        (assign, "$pool_troop", "trp_random_town_sequence"),
        (start_presentation, "prsnt_deposit_withdraw_money"),
      ]),
      
      ("continue",
      [(neq, "$sneaked_into_town", disguise_none)],
      "Attempt to sneak in...",
      [
        (set_show_messages, 0),
        
        #do inventory placeholder
        (troop_clear_inventory, "trp_temp_troop"),
        (call_script, "script_dplmc_copy_inventory", "trp_player", "trp_temp_troop"),
        (call_script, "script_dplmc_copy_inventory", "trp_random_town_sequence", "trp_player"),
        (call_script, "script_dplmc_copy_inventory", "trp_temp_troop", "trp_random_town_sequence"),
        #do gold swap
        (store_troop_gold, ":cur_amount", "trp_random_town_sequence"),
        (store_troop_gold, ":cur_gold", "trp_player"),
        (troop_remove_gold, "trp_player", ":cur_gold"),
        (troop_remove_gold, "trp_random_town_sequence", ":cur_amount"),
        (troop_add_gold, "trp_player", ":cur_amount"),
        (troop_add_gold, "trp_random_town_sequence", ":cur_gold"),
        
        (set_show_messages, 1),
        
        
        (faction_get_slot, ":player_alarm", "$g_encountered_party_faction", slot_faction_player_alarm),
        (party_get_num_companions, ":num_men", "p_main_party"),
        (party_get_num_prisoners, ":num_prisoners", "p_main_party"),
        (val_add, ":num_men", ":num_prisoners"),
        (val_mul, ":num_men", 2),
        (val_div, ":num_men", 3),
        (store_add, ":get_caught_chance", ":player_alarm", ":num_men"),
        (store_random_in_range, ":random_chance", 0, 100),
        (try_begin),
            (this_or_next|ge, "$cheat_mode", 1),
            (this_or_next|ge, ":random_chance", ":get_caught_chance"),
            (eq, "$g_last_defeated_bandits_town", "$g_encountered_party"),
            (assign, "$g_last_defeated_bandits_town", 0),              
            (assign, "$town_entered", 1), #dckplmc
            (assign, "$g_mt_mode", tcm_disguised),
            (jump_to_menu, "mnu_sneak_into_town_suceeded"),
        (else_try),
            (jump_to_menu,"mnu_sneak_into_town_caught"),
        (try_end),
      ]),
      
      ("disguise_pilgrim",
      [
        (neq, "$sneaked_into_town", disguise_pilgrim),
      ], "Don the robes of a poor pilgrim.",
      [ 
        (assign, "$sneaked_into_town", disguise_pilgrim),
      ]),
      
      #SB : todo, add peasant woman variant
      ("disguise_farmer",
      [(store_and, ":disguise", "$temp_2", disguise_farmer),
       (eq, ":disguise", disguise_farmer),
       (neq, "$sneaked_into_town", disguise_farmer),], 
      "Accept your fate as a downtrodden farmer.",
      [ 
        (assign, "$sneaked_into_town", disguise_farmer),
      ]),
      ("disguise_hunter",
      [(store_and, ":disguise", "$temp_2", disguise_hunter),
       (eq, ":disguise", disguise_hunter),
       (neq, "$sneaked_into_town", disguise_hunter),], 
      "Disguise yourself as a skilled {huntsman/huntress}.",
      [ 
        (assign, "$sneaked_into_town", disguise_hunter),
      ]),
      ("disguise_guard",
      [(store_and, ":disguise", "$temp_2", disguise_guard),
       (eq, ":disguise", disguise_guard),
       (neq, "$sneaked_into_town", disguise_guard),], 
      "Pass yourself off as a caravan guard.",
      [ 
        (assign, "$sneaked_into_town", disguise_guard),
      ]),
      ("disguise_merchant",
      [(store_and, ":disguise", "$temp_2", disguise_merchant),
       (eq, ":disguise", disguise_merchant),
       (neq, "$sneaked_into_town", disguise_merchant),], 
      "Adopt the guise of a trader.",
      [ 
        (assign, "$sneaked_into_town", disguise_merchant),
      ]),
      ("disguise_bard",
      [(store_and, ":disguise", "$temp_2", disguise_bard),
       (eq, ":disguise", disguise_bard),
       (neq, "$sneaked_into_town", disguise_bard),], 
      "Try your luck as a bard.",
      [ 
        (assign, "$sneaked_into_town", disguise_bard),
      ]),

      ("back",
      [],
      "Never mind...",
      [ 
        #put stuff back
        (set_show_messages, 0), #move all gold
        (call_script, "script_move_inventory_and_gold", "trp_random_town_sequence", "trp_player", -1),
        (set_show_messages, 1),
        
        (assign, "$sneaked_into_town", disguise_none),
        (jump_to_menu, "mnu_castle_outside"),
      ]),
    ]
  ),
  
  
  (
    "fuck",0,
    "Select a scene.",
    "none",
    [
	],
    [
      ("snow",[],"snow",[
		  (assign, "$g_training_ground_melee_training_scene", "scn_camp_scene_snow"),
		  (jump_to_menu,"mnu_fuck_2"),
	  ],"Snow."),
      ("desert",[],"desert",[
		  (assign, "$g_training_ground_melee_training_scene", "scn_camp_scene_desert"),
		  (jump_to_menu,"mnu_fuck_2"),
	  ],"Desert."),
      ("steppe",[],"steppe",[
		  (assign, "$g_training_ground_melee_training_scene", "scn_camp_scene_steppe"),
		  (jump_to_menu,"mnu_fuck_2"),
	  ],"Steppe."),
      ("plain",[],"plain",[
		  (assign, "$g_training_ground_melee_training_scene", "scn_camp_scene_plain"),
		  (jump_to_menu,"mnu_fuck_2"),
	  ],"Plain."),
      ("manor",[],"Manor",[
		  (assign, "$g_training_ground_melee_training_scene", "scn_manor"),
		  (jump_to_menu,"mnu_fuck_2"),
	  ],"Manor."),
      ("tavern",[],"Tavern",[
		  (assign, "$g_training_ground_melee_training_scene", "scn_tavern"),
		  (jump_to_menu,"mnu_fuck_2"),
	  ],"Tavern."),
      ("dungeon",[],"Dungeon",[
		  (assign, "$g_training_ground_melee_training_scene", "scn_dungeon"),
		  (jump_to_menu,"mnu_fuck_2"),
	  ],"Dungeon."),
#      ("zendar_leave",[],"Leave town.",[[leave_encounter],[change_screen_return]]),
      ("leave",[],"back",[(jump_to_menu, "mnu_camp")]),
    ]
  ),
  
  (
    "fuck_2",0,
    "Pick a position",
    "none",
    [(assign, "$g_sex_position", 0),
	 (assign, "$temp", 3),
	 (assign, "$temp_2", 1),
	 (call_script, "script_write_fit_party_members_to_stack_selection", "p_main_party", 1),
	],
    [
      ("op_1",[],"Riding",[
		  (assign, "$g_sex_position", 0),
		  (jump_to_menu,"mnu_fuck_3"),
	  ],"Riding"),
      ("op_2",[],"Fucking from behind",[
		  (assign, "$g_sex_position", 1),
		  (jump_to_menu,"mnu_fuck_3"),
	  ]),
      ("op_3",[],"Fucking both ends",[
		  (assign, "$g_sex_position", 2),
		  (assign, "$temp", 4),
		  (jump_to_menu,"mnu_fuck_3"),
	  ]),
      ("leave",[],"Go back.",[(jump_to_menu, "mnu_camp")]),
	]
  ),
  
  ("fuck_3",0,
   "Who will be {s4}?^{s1}^{reg1}:",
   "none",
    [
      (assign, reg1, "$temp_2"),
      (troop_get_slot, "$temp_3", "trp_stack_selection_amounts", 0), #number of slots
      
	  (str_clear, s4),
	  (try_begin),
		  (eq, "$temp_2", 1),
		  (str_store_string, s4, "@getting fucked"),
	  (else_try),
		  (eq, "$temp_2", 4),
		  (str_store_string, s4, "@fucking the mouth"),
	  (else_try),
		  (eq, "$temp_2", 3),
		  (str_store_string, s4, "@watching"),
	  (else_try),
		  (str_store_string, s4, "@fucking"),
	  (try_end),
	  
      #SB : show current list
      (str_clear, s1),
      (store_sub, ":end", "$temp_2", 1),
      (try_for_range, ":slot_index", 0, ":end"),
        (store_add, reg0, ":slot_index", 1),
        (troop_get_slot, ":troop_id", "trp_temp_array_a", ":slot_index"),
		(try_begin),
			(ge, ":troop_id", 0),
			(str_store_troop_name, s2, ":troop_id"),
			(str_store_string, s1, "@{s1}^{reg0}: {s2}"),
        (else_try),
			(str_store_string, s1, "@{s1}^{reg0}: No one"),
		(try_end),
      (try_end),
    ],
    [
      ("training_ground_selection_details_melee_random", [], "Choose randomly.",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details_fuck", -1),]),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_camp"),]
       ), #SB : stack built from loop
	  ("nobody", [], "No one.",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details_fuck", -2),]
	  ),
      ]+
      [("stack"+str(x), [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", x),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details_fuck", x),])
       for x in range(0, 20)]
  ),
  
  (
    "fucked_by_enemy",0,
    "Your enemies take you prisoner.",
    "none",
    [
         (set_camera_follow_party, "$capturer_party"),
         (assign, "$g_player_is_captive", 1),
         (store_random_in_range, ":random_hours", 18, 30),
         (call_script, "script_event_player_captured_as_prisoner"),
         (call_script, "script_stay_captive_for_hours", ":random_hours"),
         (assign,"$auto_menu","mnu_captivity_wilderness_check"),
         
        (call_script, "script_change_troop_renown", "trp_player", -10),
         
        (troop_get_slot, ":dna", "trp_temp_array_c", 17),
         
        (troop_set_slot, "trp_temp_array_a", 0, "trp_player"), 
        (troop_set_slot, "trp_temp_array_b", 0, -1), 
        (troop_set_slot, "trp_temp_array_a", 1, "$g_talk_troop"),
        (troop_set_slot, "trp_temp_array_b", 1, ":dna"), 
        (store_random_in_range, ":r", 0, 2),
        (assign, "$g_sex_position", ":r"),
        
          (party_get_current_terrain, ":terrain_type", "p_main_party"),
          (assign, ":scene_to_use", "scn_camp_scene_plain"),
          (try_begin),
            (this_or_next|eq, ":terrain_type", rt_steppe),
            (eq, ":terrain_type", rt_steppe_forest),
            (assign, ":scene_to_use", "scn_camp_scene_steppe"),
          (else_try),
            (this_or_next|eq, ":terrain_type", rt_plain),
            (eq, ":terrain_type", rt_forest),
            (assign, ":scene_to_use", "scn_camp_scene_plain"),
          (else_try),
            (this_or_next|eq, ":terrain_type", rt_snow),
            (eq, ":terrain_type", rt_snow_forest),
            (assign, ":scene_to_use", "scn_camp_scene_snow"),
          (else_try),
            (this_or_next|eq, ":terrain_type", rt_desert),
            (eq, ":terrain_type", rt_desert_forest),
            (assign, ":scene_to_use", "scn_camp_scene_desert"),
          # (else_try),
            # (eq, ":terrain_type", rt_water), #figure this out later
            # (assign, ":scene_to_use", "scn_camp_scene_plain"),
          (else_try),
            (eq, ":terrain_type", rt_bridge),
            (try_for_parties, ":party_no"),
                (is_between, ":party_no", "p_bridge_1", "p_looter_spawn_point"),
                (store_distance_to_party_from_party, ":distance", ":party_no", "p_main_party"),
                (lt, ":distance", 2),
                (party_get_icon, ":icon", ":party_no"),
                (try_begin),
                    (eq, ":icon", "icon_bridge_snow_a"),
                    (assign, ":scene_to_use", "scn_camp_scene_snow"),
                (else_try),
                    (assign, ":scene_to_use", "scn_camp_scene_plain"),
                (try_end),
            (try_end),
          (try_end),
        
        
        (call_script, "script_start_fucking", 2, ":scene_to_use"),
     ],
    [
      ("continue",[],"Continue...",
       [
         ]),
      ]
  ),
  
  (
    "fucked_by_enemy_prison",0,
    "The guards are infuriated by your refusal to pay the ransom.\
    They tell you that if you are not willing to pay, then there is no longer any reason to treat you humanely.\
    One of the guards then reaches for the keys to your cell, grins, and says that he is going to teach you a lesson.",
    "none",
    [
     ],
    [
      ("continue",[],"Continue...",
       [
       
            (assign, "$g_player_is_captive", 1),
            (store_random_in_range, reg(8), 16, 22),
            (call_script, "script_stay_captive_for_hours", reg8),
            (assign,"$auto_menu", "mnu_captivity_castle_check"),
            
		    (store_faction_of_party, ":capturer_faction", "$capturer_party"),
            
            (faction_get_slot, ":troop_prison_guard", ":capturer_faction", slot_faction_prison_guard_troop),
            (call_script, "script_change_troop_renown", "trp_player", -2),
            
            (try_begin),
                (eq, ":troop_prison_guard", -1),
                (assign, ":troop_prison_guard", "trp_hired_blade"),
            (try_end),
       
            (troop_set_slot, "trp_temp_array_a", 0, "trp_player"), 
            (troop_set_slot, "trp_temp_array_a", 1, ":troop_prison_guard"),
            (troop_set_slot, "trp_temp_array_a", 2, -1),
            (troop_set_slot, "trp_temp_array_a", 3, ":troop_prison_guard"),
            (assign, "$g_sex_position", 2),
            
            (call_script, "script_start_fucking", 4, "scn_dungeon"),

         ]),
      ]
  ),


  (
    "choose_banner",0,
    "Members of the nobility are each granted the right to carry their own banner. {s1} can either choose between the preset banners or design a custom banner.",
    "none",
    [
        (try_begin),
            (neq, "$g_edit_banner_troop", "trp_player"),
            (str_store_troop_name, s1, "$g_edit_banner_troop"),
        (else_try),
            (str_store_string, s1, "@You"),
        (try_end),
     ],
    [
      ("select_preset_banner",[],"Choose from preset banners.",
       [
           (jump_to_menu, "mnu_auto_return"),
           (start_presentation, "prsnt_banner_selection"),
        ]
       ),
      ("select_custom_banner",[],"Create a custom banner.",
       [
           (jump_to_menu, "mnu_auto_return"),
           (start_presentation, "prsnt_custom_banner"),
        ]
       ),
      ]
  ),
  
  ("content_options",0,
   "Diplomacy Content Options",
   "none",
   [],
    [
      ("camp_fuck_setting",[
        #(eq,0,1),
        (try_begin),
            (eq, "$g_sexual_content", 2),
            (str_store_string, s0, "@Consensual and non-consensual sex are enabled"),
        (else_try),
            (eq, "$g_sexual_content", 1),
            (str_store_string, s0, "@Consensual sex is enabled"),
        (else_try),
            (str_store_string, s0, "@Sexual content is disabled"),
        (try_end),
      ],"{s0}",
       [
       (try_begin),
            (ge, "$g_sexual_content", 2),
            (assign, "$g_sexual_content", 0),
       (else_try),
            (store_add, "$g_sexual_content", 1, "$g_sexual_content"),
       (try_end),
        ]
       ),
      ("camp_dark_hunters",[(assign, reg0, "$g_dark_hunters_enabled"),],"{reg0?Dis:En}able Dark Hunter's and Black Khergit Raider's spawning script",
       [
           (val_clamp, "$g_dark_hunters_enabled", 0, 2), #in case of other values
           (store_sub, "$g_dark_hunters_enabled", 1, "$g_dark_hunters_enabled"),
        ]
       ),
      ("camp_remove_dark_hunters",[(eq, "$g_dark_hunters_enabled", 0),],"Remove all Dark Hunters and Black Khergit Raider parties from the map",
       [
           (assign, ":removed", 0),
           (try_for_parties, ":party_no"),
                (party_get_template_id, ":ptid", ":party_no"),
                (this_or_next|eq, ":ptid", "pt_dark_hunters"),
                (eq, ":ptid", "pt_black_khergit_raiders"),
                (remove_party, ":party_no"),
                (val_add, ":removed", 1),
           (try_end),
           (assign, reg0, ":removed"),
           (display_message, "@{reg0} parties removed from the map."),
        ]
       ),
      ("camp_dark_hunters",[(assign, reg0, "$g_realistic_wounding"),],"{reg0?Dis:En}able realistic troop wounding system",
       [
           (val_clamp, "$g_realistic_wounding", 0, 2), #in case of other values
           (store_sub, "$g_realistic_wounding", 1, "$g_realistic_wounding"),
        ]
       ),
      ("camp_polygamy",[(assign, reg0, "$g_polygamy"),],"{reg0?Dis:En}able polygamy",
       [
           (val_clamp, "$g_polygamy", 0, 2), #in case of other values
           (store_sub, "$g_polygamy", 1, "$g_polygamy"),
        ]
       ),
      ("back",[],"Back",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),
  
  
  (
    "fuck_encounter",0,
    "Your enemies take you prisoner.",
    "none",
    [
        (troop_get_slot, ":dna", "trp_temp_array_c", 17),
         
        # (troop_set_slot, "trp_temp_array_a", 0, "trp_player"), 
        # (troop_set_slot, "trp_temp_array_b", 0, -1), 
        # (troop_set_slot, "trp_temp_array_a", 1, "$g_talk_troop"),
        # (troop_set_slot, "trp_temp_array_b", 1, ":dna"), 
        # (store_random_in_range, ":r", 0, 2),
        # (assign, "$g_sex_position", ":r"),
        
          (party_get_current_terrain, ":terrain_type", "p_main_party"),
          (assign, ":scene_to_use", "scn_camp_scene_plain"),
          (try_begin),
            (this_or_next|eq, ":terrain_type", rt_steppe),
            (eq, ":terrain_type", rt_steppe_forest),
            (assign, ":scene_to_use", "scn_camp_scene_steppe"),
          (else_try),
            (this_or_next|eq, ":terrain_type", rt_plain),
            (eq, ":terrain_type", rt_forest),
            (assign, ":scene_to_use", "scn_camp_scene_plain"),
          (else_try),
            (this_or_next|eq, ":terrain_type", rt_snow),
            (eq, ":terrain_type", rt_snow_forest),
            (assign, ":scene_to_use", "scn_camp_scene_snow"),
          (else_try),
            (this_or_next|eq, ":terrain_type", rt_desert),
            (eq, ":terrain_type", rt_desert_forest),
            (assign, ":scene_to_use", "scn_camp_scene_desert"),
          # (else_try),
            # (eq, ":terrain_type", rt_water), #figure this out later
            # (assign, ":scene_to_use", "scn_camp_scene_plain"),
          (else_try),
            (eq, ":terrain_type", rt_bridge),
            (try_for_parties, ":party_no"),
                (is_between, ":party_no", "p_bridge_1", "p_looter_spawn_point"),
                (store_distance_to_party_from_party, ":distance", ":party_no", "p_main_party"),
                (lt, ":distance", 2),
                (party_get_icon, ":icon", ":party_no"),
                (try_begin),
                    (eq, ":icon", "icon_bridge_snow_a"),
                    (assign, ":scene_to_use", "scn_camp_scene_snow"),
                (else_try),
                    (assign, ":scene_to_use", "scn_camp_scene_plain"),
                (try_end),
            (try_end),
          (try_end),
        
        
        (call_script, "script_start_fucking", 2, ":scene_to_use"),
     ],
    [
      ("continue",[],"Continue...",
       [
         ]),
      ]
  ),
 ]
# modmerger_start version=201 type=2
try:
    component_name = "game_menus"
    var_set = { "game_menus" : game_menus }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
