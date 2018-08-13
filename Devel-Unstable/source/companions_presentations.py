from header_common import *
from header_presentations import *
from header_mission_templates import *
from header_operations import *
from header_triggers import *
from header_items import *   # Added for Show all Items presentation.
from ID_meshes import *
from module_constants import *
from module_items import *   # Added for Show all Items presentation.
import string

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

presentations = [
####################################################################################################################################
# LAV MODIFICATIONS START (COMPANIONS OVERSEER MOD)
####################################################################################################################################

	# Reference on slot usage.
	#
	# Two troops are used by Companions Overseer. They are referenced in module_constants as lco_storage and lco_garbage.
	#
	# lco_garbage troop slots are only used to store the experience-needed-to-level table which is initialized once per game.
	#
	# lco_storage troop slots are filled with references dynamically at the start of presentation according to following schema:
	#   *. List of all troops to display is generated. Total amount is stored in $g_lco_heroes.
	#   1. Starting from 0, a total of $g_lco_heroes slots are used to store references to troop name panels (overlay_id's).
	#   2. After that, the same amount of slots is used to store references to troops (troop_id's).
	#
	# For equipment_overview presentation, additional slots are used:
	#
	#   3. After that, 11 slots are used to store references to hero equipment panels, and 11 more to store references to their respective text labels.
	#   4. After that, 9 slots are used to store references to player equipment panels, and 9 more to store references to their respective text labels.
	#   *. Number of player equipment slots is calculated and stored in $g_lco_inv_slots. Note that 10 first slots are actually equipment slots and are not included in the count.
	#   5. After that, a total of $g_lco_inv_slots slots are used to store references to player inventory panels, and $g_lco_inv_slots more to store references to their text labels.
	#
	# References to all other important overlays are stored in global variables. References to static overlays are not permanently stored.

    ("equipment_overview", 0, mesh_lco_background_split,
        [
            (ti_on_presentation_load,
                [

                    # PRESENTATION INITIALIZATION AND GENERIC ELEMENTS

                    (call_script, "script_lco_initialize_presentation"),

                    (call_script, "script_lco_create_label", "str_lco_i_title_companions", 250, 714, 1000, tf_center_justify),
                    (str_store_troop_name, s40, "trp_player"),
                    (call_script, "script_lco_create_label", "str_lco_s40", 750, 714, 1000, tf_center_justify),
                    (str_clear, s40),
                    (call_script, "script_lco_create_mesh", "mesh_pic_camp", -300, 138, 750, 750),
                    (call_script, "script_lco_create_mesh", "mesh_pic_messenger", 110, 138, 750, 750),

                    # PRESENTATION AUTO-EQUIP FORM

                    (call_script, "script_lco_create_label", "str_lco_i_ae_with", 275, 175, 750, 0),
                    (call_script, "script_lco_create_label", "str_lco_i_ae_with", 275, 175, 750, 0),
                    (call_script, "script_lco_create_checkbox", "str_lco_i_ae_with_horses",  275, 150, "$g_lco_auto_horses"),
                    (assign, "$g_lco_cb_0", reg0),
                    (call_script, "script_lco_create_checkbox", "str_lco_i_ae_with_armors",  375, 150, "$g_lco_auto_armors"),
                    (assign, "$g_lco_cb_1", reg0),
                    (call_script, "script_lco_create_checkbox", "str_lco_i_ae_with_shields", 275, 125, "$g_lco_auto_shields"),
                    (assign, "$g_lco_cb_2", reg0),

                    (call_script, "script_lco_create_button", "str_lco_i_ae_companion", 355, 75, 190, 42),
                    (assign, "$g_lco_auto_equip", reg0),
                    (call_script, "script_lco_create_button", "str_lco_i_ae_everyone", 355, 25, 190, 42),
                    (assign, "$g_lco_auto_equip_all", reg0),

                    # GENERATING HERO NAME PANELS

                    (call_script, "script_lco_create_label", "str_lco_i_hero_panel_title", 25, 652, 750, 0),
                    (call_script, "script_lco_create_label", "str_lco_i_hero_panel_title", 25, 652, 750, 0),

                    (call_script, "script_lco_create_container", 0, 125, 250, 525+2, 1),

                    (store_mul, ":base_y", "$g_lco_heroes", 25),
                    (val_sub, ":base_y", 25),
                    (val_max, ":base_y", 500),
                    (try_for_range, ":index", 0, "$g_lco_heroes"),
                        (troop_get_slot, ":troop_id", lco_storage, ":index"),
                        (store_add, ":offset", "$g_lco_heroes", ":index"),
                        (troop_set_slot, lco_storage, ":offset", ":troop_id"),
                        (store_mul, ":y", ":index", 25),
                        (store_sub, ":y", ":base_y", ":y"),
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 25, ":y", 310, 300),
                        (troop_set_slot, lco_storage, ":index", reg0),
                    (try_end),
                    (store_mul, ":y", "$g_lco_active_hero", 25),
                    (store_sub, ":y", ":base_y", ":y"),
                    (call_script, "script_lco_create_mesh", "mesh_lco_panel_down", 25, ":y", 310, 300),
                    (assign, "$g_lco_active_panel", reg0),
                    (val_add, ":base_y", 1),
                    (try_for_range, ":index", 0, "$g_lco_heroes"),
                        (store_add, ":offset", "$g_lco_heroes", ":index"),
                        (troop_get_slot, ":troop_id", lco_storage, ":offset"),
                        (store_mul, ":y", ":index", 25),
                        (store_sub, ":y", ":base_y", ":y"),
                        (call_script, "script_lco_troop_name_to_s40", ":troop_id"),
                        (call_script, "script_lco_create_label", "str_lco_s40", 30, ":y", 750, 0),
                    (try_end),
                    (str_clear, s40),
                    (set_container_overlay, -1),

                    # GENERATING HERO EQUIPMENT PANELS

                    # Weapons:
                    (store_mul, ":index", "$g_lco_heroes", 2),
                    (call_script, "script_lco_create_label", "str_lco_i_weapons", 272, 650, 750, 0),
                    (call_script, "script_lco_create_label", "str_lco_i_weapons", 272, 650, 750, 0),
                    (try_for_range, reg1, 0, 4),
                        (store_mul, ":y", reg1, 25),
                        (store_sub, ":y", 625, ":y"),
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 272, ":y", 310, 300),
                        (troop_set_slot, lco_storage, ":index", reg0),
                        (val_add, ":index", 1),
                    (try_end),
                    # Armor:
                    (call_script, "script_lco_create_label", "str_lco_i_armor", 272, 500, 750, 0),
                    (call_script, "script_lco_create_label", "str_lco_i_armor", 272, 500, 750, 0),
                    (try_for_range, reg1, 0, 4),
                        (store_mul, ":y", reg1, 25),
                        (store_sub, ":y", 475, ":y"),
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 272, ":y", 310, 300),
                        (troop_set_slot, lco_storage, ":index", reg0),
                        (val_add, ":index", 1),
                    (try_end),
                    # Horse:
                    (call_script, "script_lco_create_label", "str_lco_i_horse", 272, 350, 750, 0),
                    (call_script, "script_lco_create_label", "str_lco_i_horse", 272, 350, 750, 0),
                    (call_script, "script_lco_create_mesh", "mesh_lco_panel", 272, 325, 310, 300),
                    (troop_set_slot, lco_storage, ":index", reg0),
                    (val_add, ":index", 1),
                    # Books:
                    # Update V1.1. Disable book slots configuration variable
                    (try_begin),
                        (eq, "$g_lco_suppress_books", 0),
                        (call_script, "script_lco_create_label", "str_lco_i_books", 272, 275, 750, 0),
                        (call_script, "script_lco_create_label", "str_lco_i_books", 272, 275, 750, 0),
                        (try_for_range, reg1, 0, 2),
                            (store_mul, ":y", reg1, 25),
                            (store_sub, ":y", 250, ":y"),
                            (call_script, "script_lco_create_mesh", "mesh_lco_panel", 272, ":y", 310, 300),
                            (troop_set_slot, lco_storage, ":index", reg0),
                            (val_add, ":index", 1),
                        (try_end),
                    (else_try),
                        (val_add, ":index", 2),
                    (try_end),

                    # GENERATING HERO EQUIPMENT TEXT FIELDS

                    # Weapons:
                    (str_clear, s40),
                    (try_for_range, reg1, 0, 4),
                        (store_mul, ":y", reg1, 25),
                        (store_sub, ":y", 625+1, ":y"),
                        (call_script, "script_lco_create_label", s40, 277, ":y", 750, 0),
                        (troop_set_slot, lco_storage, ":index", reg0),
                        (val_add, ":index", 1),
                    (try_end),
                    # Armor:
                    (try_for_range, reg1, 0, 4),
                        (store_mul, ":y", reg1, 25),
                        (store_sub, ":y", 475+1, ":y"),
                        (call_script, "script_lco_create_label", s40, 277, ":y", 750, 0),
                        (troop_set_slot, lco_storage, ":index", reg0),
                        (val_add, ":index", 1),
                    (try_end),
                    # Horse:
                    (call_script, "script_lco_create_label", s40, 277, 325+1, 750, 0),
                    (troop_set_slot, lco_storage, ":index", reg0),
                    (val_add, ":index", 1),
                    # Books:
                    # Update V1.1. Disable book slots configuration variable
                    (try_begin),
                        (eq, "$g_lco_suppress_books", 0),
                        (try_for_range, reg1, 0, 2),
                            (store_mul, ":y", reg1, 25),
                            (store_sub, ":y", 250+1, ":y"),
                            (call_script, "script_lco_create_label", s40, 277, ":y", 750, 0),
                            (troop_set_slot, lco_storage, ":index", reg0),
                            (val_add, ":index", 1),
                        (try_end),
                    (else_try),
                        (val_add, ":index", 2),
                    (try_end),

                    # GENERATING PLAYER EQUIPMENT PANELS

                    # Weapons:
                    (call_script, "script_lco_create_label", "str_lco_i_weapons", 512, 650, 750, 0),
                    (call_script, "script_lco_create_label", "str_lco_i_weapons", 512, 650, 750, 0),
                    (try_for_range, reg1, 0, 4),
                        (store_mul, ":y", reg1, 25),
                        (store_sub, ":y", 625, ":y"),
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 512, ":y", 310, 300),
                        (troop_set_slot, lco_storage, ":index", reg0),
                        (val_add, ":index", 1),
                    (try_end),
                    # Armor:
                    (call_script, "script_lco_create_label", "str_lco_i_armor", 512, 500, 750, 0),
                    (call_script, "script_lco_create_label", "str_lco_i_armor", 512, 500, 750, 0),
                    (try_for_range, reg1, 0, 4),
                        (store_mul, ":y", reg1, 25),
                        (store_sub, ":y", 475, ":y"),
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 512, ":y", 310, 300),
                        (troop_set_slot, lco_storage, ":index", reg0),
                        (val_add, ":index", 1),
                    (try_end),
                    # Horse:
                    (call_script, "script_lco_create_label", "str_lco_i_horse", 512, 350, 750, 0),
                    (call_script, "script_lco_create_label", "str_lco_i_horse", 512, 350, 750, 0),
                    (call_script, "script_lco_create_mesh", "mesh_lco_panel", 512, 325, 310, 300),
                    (troop_set_slot, lco_storage, ":index", reg0),
                    (val_add, ":index", 1),

                    # GENERATING PLAYER EQUIPMENT TEXT FIELDS

                    # Weapons:
                    #(position_set_x, pos60, 517),
                    (try_for_range, reg1, 0, 4),
                        (store_mul, ":y", reg1, 25),
                        (store_sub, ":y", 625+1, ":y"),
                        (call_script, "script_lco_create_label", s40, 517, ":y", 750, 0),
                        (troop_set_slot, lco_storage, ":index", reg0),
                        (val_add, ":index", 1),
                    (try_end),
                    # Armor:
                    (try_for_range, reg1, 0, 4),
                        (store_mul, ":y", reg1, 25),
                        (store_sub, ":y", 475+1, ":y"),
                        (call_script, "script_lco_create_label", s40, 517, ":y", 750, 0),
                        (troop_set_slot, lco_storage, ":index", reg0),
                        (val_add, ":index", 1),
                    (try_end),
                    # Horse:
                    (call_script, "script_lco_create_label", s40, 517, 325+1, 750, 0),
                    (troop_set_slot, lco_storage, ":index", reg0),
                    (val_add, ":index", 1),

                    # GENERATING PLAYER INVENTORY PANELS

                    (call_script, "script_lco_create_label", "str_lco_i_inventory", 750, 652, 750, 0),
                    (call_script, "script_lco_create_label", "str_lco_i_inventory", 750, 652, 750, 0),
                    (call_script, "script_lco_create_image_button", "mesh_lco_sort_inventory", "mesh_lco_sort_inventory_down", 935, 655, 200, 200),
                    (assign, "$g_lco_sort_inventory", reg0),

                    (call_script, "script_lco_create_container", 750, 125, 215, 525+2, 1),

                    (store_mul, ":top", "$g_lco_inv_slots", 25),
                    (val_sub, ":top", 25),
                    (val_max, ":top", 500),
                    (try_for_range, reg1, 0, "$g_lco_inv_slots"),
                        (store_mul, ":y", reg1, 25),
                        (store_sub, ":y", ":top", ":y"),
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 0, ":y", 300, 300),
                        (troop_set_slot, lco_storage, ":index", reg0),
                        (val_add, ":index", 1),
                    (try_end),
                    (try_for_range, reg1, 0, "$g_lco_inv_slots"),
                        (store_mul, ":y", reg1, 25),
                        (store_sub, ":y", ":top", ":y"),
                        (val_add, ":y", 1),
                        (call_script, "script_lco_create_label", "str_empty_string", 5, ":y", 750, 0),
                        (troop_set_slot, lco_storage, ":index", reg0),
                        (val_add, ":index", 1),
                    (try_end),

                    (set_container_overlay, -1),

                    # GENERATING DISCARDED ITEMS INTERFACE

                    (call_script, "script_lco_create_label", "str_lco_i_discard", 512, 275, 750, 0),
                    (call_script, "script_lco_create_label", "str_lco_i_discard", 512, 275, 750, 0),
                    (call_script, "script_lco_create_button", "str_lco_i_retrieve", 605, 25, 190, 42),
                    (assign, "$g_lco_retrieve", reg0),
                    (call_script, "script_lco_create_container", 515, 75, 200, 200+2, 1),
                    (store_mul, ":top", "$g_lco_garb_slots", 25),
                    (val_sub, ":top", 25),
                    (val_max, ":top", 175),
                    (try_for_range, reg1, 0, "$g_lco_garb_slots"),
                        (store_mul, ":y", reg1, 25),
                        (store_sub, ":y", ":top", ":y"),
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 0, ":y", 282, 300),
                        (troop_set_slot, lco_storage, ":index", reg0),
                        (val_add, ":index", 1),
                    (try_end),
                    (val_add, ":top", 1),
                    (try_for_range, reg1, 0, "$g_lco_garb_slots"),
                        (store_mul, ":y", reg1, 25),
                        (store_sub, ":y", ":top", ":y"),
                        (call_script, "script_lco_create_label", "str_empty_string", 5, ":y", 750, 0),
                        (troop_set_slot, lco_storage, ":index", reg0),
                        (val_add, ":index", 1),
                    (try_end),
                    (set_container_overlay, -1),

                    #(call_script, "script_lco_create_mesh", "mesh_lco_garbage_area", 512, 150, 287, 205),
                    #(assign, "$g_lco_garbage_drop", reg0),
                    #(call_script, "script_lco_count_discarded"),
                    #(call_script, "script_lco_create_label", "str_lco_drop_here", 624, 215, 750, tf_center_justify | tf_vertical_align_center),
                    #(assign, "$g_lco_garbage_note", reg0),
                    #(overlay_set_color, "$g_lco_garbage_note", 0xFFFFFF),

                    # GENERATING PLAYER MONEY INDICATOR

                    (call_script, "script_lco_create_mesh", "mesh_lco_gold_icon", 775, 82, 250, 250),
                    (store_troop_gold, reg60, "trp_player"),
                    (call_script, "script_game_get_money_text", reg60),
                    (str_store_string_reg, s40, s1),
                    (call_script, "script_lco_create_label", "str_lco_s40", 810, 90, 850, 0),
                    (overlay_set_color, reg0, 0xFFFF00),
                    (call_script, "script_lco_create_label", "str_lco_s40", 810, 90, 850, 0),
                    (call_script, "script_lco_create_label", "str_lco_s40", 810, 90, 850, 0),

                    # GENERATING PANEL AND TEXT FOR DRAG-N-DROP ITEM

                    (call_script, "script_lco_create_container", 0, 0, 225, 27, 1),
                    (assign, "$g_lco_dragging_panel", reg0),
                    (overlay_set_display, "$g_lco_dragging_panel", 0),

                    (call_script, "script_lco_create_mesh", "mesh_lco_panel", 0, 0, 310, 300),
                    (call_script, "script_lco_create_label", s40, 5, 1, 750, 0),
                    (assign, "$g_lco_dragging_text", reg0),

                    (set_container_overlay, -1),

                    # FINALLY FILLING ALL THOSE PANELS WITH ACTUAL DATA

                    (call_script, "script_lco_fill_hero_panels"),
                    (call_script, "script_lco_fill_player_panels"),

                ]
            ),

            (ti_on_presentation_event_state_change,
                [
                    (store_trigger_param_1, ":overlay_id"),
                    (store_trigger_param_2, ":value"),
                    (try_begin),
                        (eq, ":overlay_id", "$g_lco_return"),
                        (try_begin),
                            (eq, "$g_lco_dragging", 1),
                            (call_script, "script_lco_cancel_drag_item"),
                        (try_end),
                        (try_begin),
                            (eq, "$g_lco_dragging", 1),
                            (display_message, "str_lco_error_drop_first", 0xFF4040),
                        (else_try),
                            (call_script, "script_lco_clear_all_items", "$g_lco_garbage_troop"),
                            (assign, "$g_lco_garbage_troop", lco_garbage),
                            (jump_to_menu, "mnu_lco_auto_return"),
                            (presentation_set_duration, 0),
                        (try_end),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_retrieve"),
                        (try_begin),
                            (this_or_next|key_is_down, key_left_control),
                            (key_is_down, key_right_control),
                            (call_script, "script_lco_retrieve_discarded_best"),
                        (else_try),
                            (call_script, "script_lco_retrieve_discarded"),
                        (try_end),
                        (call_script, "script_lco_fill_player_panels"),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_sort_inventory"),
                        (call_script, "script_lco_sort_player_inventory"),
                        (call_script, "script_lco_fill_player_panels"),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_cb_0"),
                        (assign, "$g_lco_auto_horses", ":value"),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_cb_1"),
                        (assign, "$g_lco_auto_armors", ":value"),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_cb_2"),
                        (assign, "$g_lco_auto_shields", ":value"),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_inc_0"),
                        (assign, "$g_lco_include_companions", ":value"),
                        (presentation_set_duration, 0),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_inc_1"),
                        (assign, "$g_lco_include_lords", ":value"),
                        (presentation_set_duration, 0),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_inc_2"),
                        (assign, "$g_lco_include_regulars", ":value"),
                        (presentation_set_duration, 0),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_switch_page_0"),
                        (assign, "$g_lco_page", 0),
                        (presentation_set_duration, 0),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_switch_page_1"),
                        (assign, "$g_lco_page", 1),
                        (presentation_set_duration, 0),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_switch_page_2"),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_auto_equip"),
                        (try_begin),
                            (store_add, ":hero_offset", "$g_lco_heroes", "$g_lco_active_hero"),
                            (troop_get_slot, ":troop_id", lco_storage, ":hero_offset"),
                            (call_script, "script_cf_lco_controllable", ":troop_id"),
                            (call_script, "script_lco_backup_inventory", ":troop_id"),
                            (call_script, "script_lco_hero_grab_equipment", ":troop_id"),
                            (troop_equip_items, ":troop_id"),
                            (call_script, "script_lco_hero_return_equipment", ":troop_id"),
                            (call_script, "script_lco_retrieve_inventory", ":troop_id"),
                            (troop_get_type, reg60, ":troop_id"),
                            (str_store_troop_name, s41, ":troop_id"),
                            (display_message, "str_lco_message_hero_ae"),
                            (call_script, "script_lco_fill_hero_panels"),
                            (call_script, "script_lco_fill_player_panels"),
                        (else_try),
                            (display_message, "str_lco_drop_error_control", 0xFF4040),
                        (try_end),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_auto_equip_all"),
                        (store_add, ":upper_range", "$g_lco_heroes", "$g_lco_heroes"),
                        (try_for_range, ":hero_offset", "$g_lco_heroes", ":upper_range"),
                            (troop_get_slot, ":troop_id", lco_storage, ":hero_offset"),
                            (call_script, "script_cf_lco_controllable", ":troop_id"),
                            (call_script, "script_lco_backup_inventory", ":troop_id"),
                            (call_script, "script_lco_hero_grab_equipment", ":troop_id"),
                            (troop_equip_items, ":troop_id"),
                            (call_script, "script_lco_hero_return_equipment", ":troop_id"),
                            (call_script, "script_lco_retrieve_inventory", ":troop_id"),
                        (try_end),
                        (display_message, "str_lco_message_all_heroes_ae"),
                        (call_script, "script_lco_fill_hero_panels"),
                        (call_script, "script_lco_fill_player_panels"),
                    (try_end),
                ]
            ),

            (ti_on_presentation_mouse_press,
                [
                    (store_trigger_param_1, ":overlay_id"),
                    (store_trigger_param_2, ":mouse_button"),
                    (try_begin),
                        (eq, ":mouse_button", 0), # Left mouse button

                        # Checking if it's one of hero panels
                        (try_begin),
                            (eq, "$g_lco_panel_found", 0),
                            (try_for_range, ":index", 0, "$g_lco_heroes"),
                                (troop_slot_eq, lco_storage, ":index", ":overlay_id"),
                                (assign, "$g_lco_panel_found", 1),
                                (try_begin),
                                    (this_or_next|key_is_down, key_left_control),
                                    (key_is_down, key_right_control),
                                    (try_begin),
                                        (eq, "$g_lco_dragging", 1),
                                        (store_add, ":hero_offset", "$g_lco_heroes", ":index"),
                                        (troop_get_slot, ":recipient_id", lco_storage, ":hero_offset"),
                                        (call_script, "script_cf_lco_controllable", ":recipient_id"),
                                        (try_begin),
                                            (call_script, "script_cf_lco_auto_offer_item", ":recipient_id", "$g_lco_drag_item", "$g_lco_drag_modifier", "$g_lco_drag_quantity"),
                                            (try_begin),
                                                (ge, reg0, 0),
                                                (assign, "$g_lco_drag_item", reg0),
                                                (assign, "$g_lco_drag_modifier", reg1),
                                                (assign, "$g_lco_drag_quantity", reg2),
                                                (assign, "$g_lco_drag_quantity_max", reg3),
                                                (call_script, "script_lco_item_name_to_s41", "$g_lco_drag_item", "$g_lco_drag_modifier", "$g_lco_drag_quantity", "$g_lco_drag_quantity_max"),
                                                (overlay_set_text, "$g_lco_dragging_text", s41),
                                            (else_try),
                                                (assign, "$g_lco_drag_item", -1),
                                                (assign, "$g_lco_drag_modifier", 0),
                                                (assign, "$g_lco_drag_quantity", 0),
                                                (assign, "$g_lco_drag_quantity_max", 0),
                                                (overlay_set_display, "$g_lco_dragging_panel", 0),
                                                (assign, "$g_lco_dragging", 0),
                                            (try_end),
                                            (call_script, "script_lco_fill_hero_panels"),
                                            (call_script, "script_lco_fill_player_panels"),
                                        (else_try),
                                            (str_store_troop_name, s40, ":recipient_id"),
                                            (call_script, "script_lco_item_name_to_s41", "$g_lco_drag_item", "$g_lco_drag_modifier", "$g_lco_drag_quantity", "$g_lco_drag_quantity_max"),
                                            (str_store_string, s40, "str_lco_message_hero_no_need"),
                                            (display_message, s40, 0xFF4040),
                                        (try_end),
                                    (try_end),
                                (else_try),
                                    (this_or_next|key_is_down, key_left_alt),
                                    (key_is_down, key_right_alt),
                                    (call_script, "script_lco_set_active_hero", ":index"),
                                    (try_begin),
                                        (eq, "$g_lco_dragging", 1),
                                        (display_message, "str_lco_error_drop_first", 0xFF4040),
                                    (else_try),
                                        (store_add, ":hero_offset", "$g_lco_heroes", ":index"),
                                        (troop_get_slot, "$g_lco_target", lco_storage, ":hero_offset"),
                                        (assign, "$g_lco_operation", lco_view_character),
                                        (jump_to_menu, "mnu_lco_auto_return"),
                                        (presentation_set_duration, 0),
                                    (try_end),
                                (else_try),
                                    (call_script, "script_lco_set_active_hero", ":index"),
                                (try_end),
                            (try_end),
                        (try_end),

                        # Checking if it's one of item panels
                        (try_begin),
                            (eq, "$g_lco_panel_found", 0),
                            (call_script, "script_cf_lco_is_active_panel", ":overlay_id"),
                            (assign, "$g_lco_panel_found", 1),
                            (call_script, "script_lco_get_slot_details_for_panel", ":overlay_id"),
                            (assign, ":troop_id", reg0),
                            (assign, ":slot_id", reg1),
                            (assign, ":item_id", reg2),
                            (assign, ":modifier", reg3),
                            (assign, ":quantity", reg4),
                            (assign, ":quantity_max", reg5),
                            (try_begin),
                                (eq, "$g_lco_dragging", 0), # We are currently not dragging anything, so either drag start or quick give or item offer
                                (try_begin),
                                    (ge, ":item_id", 0), # There is an item inside
                                    (try_begin),
                                        (this_or_next|key_is_down, key_left_control),
                                        (key_is_down, key_right_control),

                                        # This is a Ctrl-Click on an item while not dragging anything
                                        # For a player, this is an offer of an item to current hero
                                        # For a hero, this is a quick-move of item to player's inventory
                                        (try_begin),
                                            (eq, ":troop_id", "trp_player"), # Offering item to hero
                                            (store_add, ":hero_offset", "$g_lco_heroes", "$g_lco_active_hero"),
                                            (troop_get_slot, ":recipient_id", lco_storage, ":hero_offset"),
                                            (try_begin),
                                                (call_script, "script_cf_lco_auto_offer_item", ":recipient_id", ":item_id", ":modifier", ":quantity"),
                                                (try_begin),
                                                    (ge, reg0, 0),
                                                    (troop_set_inventory_slot, ":troop_id", ":slot_id", reg0),
                                                    (troop_set_inventory_slot_modifier, ":troop_id", ":slot_id", reg1),
                                                (else_try),
                                                    (troop_set_inventory_slot, ":troop_id", ":slot_id", -1),
                                                (try_end),
                                                (call_script, "script_lco_fill_hero_panels"),
                                                (call_script, "script_lco_fill_player_panels"),
                                            (else_try),
                                                (str_store_troop_name, s40, ":recipient_id"),
                                                (call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":quantity", ":quantity_max"),
                                                (str_store_string, s40, "str_lco_message_hero_no_need"),
                                                (display_message, s40, 0xFF4040),
                                            (try_end),
                                        (else_try),
                                            (assign, ":given", 0),
                                            (try_begin),
                                                (call_script, "script_cf_lco_controllable", ":troop_id"),
                                                (troop_get_inventory_capacity, ":capacity", "trp_player"),
                                                (try_for_range, ":index", num_equipment_kinds, ":capacity"),
                                                    (eq, ":given", 0), # Failsafe
                                                    (troop_get_inventory_slot, ":cur_item", "trp_player", ":index"),
                                                    (lt, ":cur_item", 0),
                                                    (troop_set_inventory_slot, "trp_player", ":index", ":item_id"),
                                                    (troop_set_inventory_slot_modifier, "trp_player", ":index", ":modifier"),
                                                    (try_begin),
                                                        (gt, ":quantity", 0),
                                                        (troop_inventory_slot_set_item_amount, ":quantity"),
                                                    (try_end),
                                                    (troop_set_inventory_slot, ":troop_id", ":slot_id", -1),
                                                    (assign, ":given", 1),
                                                    (assign, ":capacity", 0), # Break cycle
                                                (try_end),
                                                (try_begin),
                                                    (eq, ":given", 0),
                                                    (display_message, "str_lco_error_inv_full", 0xFF4040),
                                                (else_try),
                                                    (call_script, "script_lco_fill_hero_panels"),
                                                    (call_script, "script_lco_fill_player_panels"),
                                                (try_end),
                                            (else_try),
                                                (str_store_troop_name, s40, ":recipient_id"),
                                                (display_message, "str_lco_drop_error_control", 0xFF4040),
                                            (try_end),
                                        (try_end),

                                    (else_try),
                                        # Alt-Click means quick-deletion of object
                                        (this_or_next|key_is_down, key_left_alt),
                                        (key_is_down, key_right_alt),

                                        (try_begin),
                                            (call_script, "script_cf_lco_controllable", ":troop_id"),
                                            (neq, ":troop_id", "$g_lco_garbage_troop"),
                                            (call_script, "script_lco_discard_item", ":item_id", ":modifier", ":quantity"),
                                            (troop_set_inventory_slot, ":troop_id", ":slot_id", -1),
                                            (call_script, "script_lco_fill_hero_panels"),
                                            (call_script, "script_lco_fill_player_panels"),
                                        (try_end),


                                    (else_try),

                                        (this_or_next|key_is_down, key_left_shift),
                                        (key_is_down, key_right_shift),
                                        (eq, ":troop_id", "trp_player"),

                                        # This is a Shift-Click on a player's item while not dragging anything
                                        # This item will be offered to all heroes in sequence, swapping as appropriate.
                                        (assign, ":upper_range", "$g_lco_heroes"),
                                        (assign, ":any_changes", 0),
                                        (try_for_range, ":index", 0, ":upper_range"),
                                            (store_add, ":hero_offset", "$g_lco_heroes", ":index"),
                                            (troop_get_slot, ":recipient_id", lco_storage, ":hero_offset"),
                                            (call_script, "script_cf_lco_auto_offer_item", ":recipient_id", ":item_id", ":modifier", ":quantity"),
                                            (str_store_troop_name, s40, ":recipient_id"),
                                            (troop_get_type, reg4, ":recipient_id"),
                                            (call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":quantity", ":quantity_max"),
                                            (try_begin),
                                                (ge, reg0, 0), # Agent returned some item as well
                                                (str_store_string, s39, s41),
                                                (call_script, "script_lco_item_name_to_s41", reg0, reg1, reg2, reg3),
                                                (display_message, "str_lco_message_hero_replaced"),
                                            (else_try),
                                                (display_message, "str_lco_message_hero_equipped"),
                                                (assign, ":upper_range", 0), # Break cycle
                                            (try_end),
                                            (assign, ":item_id", reg0),
                                            (assign, ":modifier", reg1),
                                            (assign, ":quantity", reg2),
                                            (assign, ":quantity_max", reg3),
                                            (assign, ":any_changes", 1),
                                        (try_end),
                                        # Now we need to replace or remove the original item
                                        (try_begin),
                                            (ge, ":item_id", 0),
                                            (troop_set_inventory_slot, ":troop_id", ":slot_id", ":item_id"),
                                            (troop_set_inventory_slot_modifier, ":troop_id", ":slot_id", ":item_id"),
                                        (else_try),
                                            (troop_set_inventory_slot, ":troop_id", ":slot_id", -1),
                                        (try_end),
                                        (try_begin),
                                            (eq, ":any_changes", 1),
                                            (call_script, "script_lco_fill_hero_panels"),
                                            (call_script, "script_lco_fill_player_panels"),
                                        (else_try),
                                            (call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":quantity", ":quantity_max"),
                                            (display_message, "str_lco_message_nobody_needs", 0xFF4040),
                                        (try_end),

                                    (else_try),

                                        (call_script, "script_lco_drag_item", ":troop_id", ":slot_id"),
                                        (call_script, "script_lco_fill_hero_panels"),
                                        (call_script, "script_lco_fill_player_panels"),

                                    (try_end),
                                (try_end),
                            (else_try),
                                # Item panel was clicked while player is dragging an item
                                (try_begin),
                                    (call_script, "script_cf_lco_can_drop_item", ":troop_id", ":slot_id", "$g_lco_drag_item", "$g_lco_drag_modifier"),
                                    (call_script, "script_lco_drop_item", ":troop_id", ":slot_id"),
                                    (call_script, "script_lco_fill_hero_panels"),
                                    (call_script, "script_lco_fill_player_panels"),
                                (else_try),
                                    (display_message, reg0, 0xFF4040),
                                (try_end),
                            (try_end),
                        (try_end),

                    (else_try),
                        (eq, ":mouse_button", 1), # Right mouse button
                        (eq, "$g_lco_panel_found", 0), # Normal processing has not been prevented by trigger in ti_on_presentation_run
                        (eq, "$g_lco_dragging", 0), # We are currently not dragging anything
                        (call_script, "script_cf_lco_is_active_panel", ":overlay_id"),
                        (assign, "$g_lco_panel_found", 1),
                        (call_script, "script_lco_get_slot_details_for_panel", ":overlay_id"),
                        (eq, reg0, "trp_player"), # Right mouse button clicked on one of player's panels
                        (ge, reg1, num_equipment_kinds), # What's more, this is one of player's *inventory* panels which we can actually freeze!
                        (call_script, "script_lco_freeze_slot_toggle", reg1), # We switch frozen status for this slot
                        (call_script, "script_lco_fill_player_panels"), # And refresh the screen
                    (try_end),
                ]
            ),

            (ti_on_presentation_run,
                [
                    (set_fixed_point_multiplier, 1000),
                    (assign, "$g_lco_panel_found", 0), # We enable mouse click detection every frame, but it only works once per frame (see ti_on_presentation_mouse_press)
                    # ESC quits the presentation
                    (try_begin),
                        (key_clicked, key_escape),
                        (try_begin),
                            (eq, "$g_lco_dragging", 1),
                            (call_script, "script_lco_cancel_drag_item"),
                        (try_end),
                        (try_begin),
                            (eq, "$g_lco_dragging", 1),
                            (display_message, "str_lco_error_drop_first", 0xFF4040),
                        (else_try),
                            (call_script, "script_lco_clear_all_items", "$g_lco_garbage_troop"),
                            (assign, "$g_lco_garbage_troop", lco_garbage),
                            (jump_to_menu, "mnu_lco_auto_return"),
                            (presentation_set_duration, 0),
                        (try_end),
                    (try_end),
                    # TAB and SHIFT-TAB switch current hero
                    (try_begin),
                        (key_clicked, key_tab),
                        (try_begin),
                            (this_or_next|key_is_down, key_left_shift),
                            (key_is_down, key_right_shift),
                            (store_add, ":new_index", "$g_lco_active_hero", "$g_lco_heroes"),
                            (val_sub, ":new_index", 1),
                            (val_mod, ":new_index", "$g_lco_heroes"),
                            (call_script, "script_lco_set_active_hero", ":new_index"),
                        (else_try),
                            (this_or_next|key_is_down, key_left_control),
                            (key_is_down, key_right_control),
                            (assign, "$g_lco_page", 0),
                            (presentation_set_duration, 0),
                        (else_try),
                            (neg|key_is_down, key_left_alt),
                            (neg|key_is_down, key_right_alt),
                            (store_add, ":new_index", "$g_lco_active_hero", 1),
                            (val_mod, ":new_index", "$g_lco_heroes"),
                            (call_script, "script_lco_set_active_hero", ":new_index"),
                        (try_end),
                    (try_end),
                    # RIGHT MOUSE CLICK cancels dragging item, if there is any
                    (try_begin),
                        (key_clicked, key_right_mouse_button),
                        (eq, "$g_lco_dragging", 1),
                        (call_script, "script_lco_cancel_drag_item"),
                        (eq, "$g_lco_dragging", 0),
                        (call_script, "script_lco_fill_hero_panels"),
                        (call_script, "script_lco_fill_player_panels"),
                        (assign, "$g_lco_panel_found", 1), # If we cancelled drag, then on this frame we ignore any other effects of right mouse button
                    (try_end),
                    # When drag-n-drop is active, it must be displayed
                    (try_begin),
                        (eq, "$g_lco_dragging", 1),
                        (mouse_get_position, pos60),
                        (position_get_x, reg10, pos60),
                        (position_get_y, reg11, pos60),
                        (val_add, reg10, 15),
                        (val_sub, reg11, 40),
                        (position_set_x, pos60, reg10),
                        (position_set_y, pos60, reg11),
                        (overlay_set_position, "$g_lco_dragging_panel", pos60),
                    (try_end),
                    # When popup is active, it must be displayed
                    (try_begin),
                        (eq, "$g_lco_popup_active", 1),
                        (mouse_get_position, pos60),
                        (position_get_y, reg11, pos60),
                        (val_sub, reg11, 90),
                        (position_set_y, pos60, reg11),
                        # BugFix V1.1. Operation was called with incorrect price multiplier.
                        (show_item_details_with_modifier, "$g_lco_popup_item", "$g_lco_popup_modifier", pos60, 100),
                    (try_end),
                ]
            ),

            (ti_on_presentation_mouse_enter_leave,
                [
                    (store_trigger_param_1, ":overlay_id"),
                    (store_trigger_param_2, ":is_mouse_out"),
                    (try_begin),
                        (eq, ":is_mouse_out", 1),
                        (try_begin),
                            (eq, "$g_lco_popup_overlay", ":overlay_id"),
                            (try_begin),
                                (eq, "$g_lco_popup_active", 1),
                                (assign, "$g_lco_popup_active", 0),
                                (close_item_details),
                            (try_end),
                        (try_end),
                    (else_try),
                        # Is the object one of active panels?
                        (call_script, "script_cf_lco_is_active_panel", ":overlay_id"),
                        (call_script, "script_lco_get_slot_details_for_panel", ":overlay_id"),
                        (try_begin),
                            (ge, reg2, 0),
                            (assign, "$g_lco_popup_active", 1),
                            (assign, "$g_lco_popup_overlay", ":overlay_id"),
                            (assign, "$g_lco_popup_item", reg2),
                            (assign, "$g_lco_popup_modifier", reg3),
                        (else_try),
                            (eq, "$g_lco_popup_active", 1),
                            (assign, "$g_lco_popup_active", 0),
                            (close_item_details),
                        (try_end),
                    (try_end),
                ]
            ),

        ]
    ),

    ("companions_overview", 0, mesh_lco_background,
        [

            (ti_on_presentation_load,
                [

                    # PRESENTATION INITIALIZATION

                    (call_script, "script_lco_initialize_presentation"),

                    (call_script, "script_lco_create_mesh", "mesh_pic_camp", 0, 0, 1000, 1000),

                    (call_script, "script_lco_create_button", "str_lco_i_character", 355, 25, 190, 42),
                    (assign, "$g_lco_dialog", reg0),

                    # GENERATING CONTAINERS HIERARCHY AND MAJOR CONTROLS

                    (store_mul, ":viewport_height", "$g_lco_heroes", 25),
                    (val_add, ":viewport_height", 2),
                    (assign, ":viewport_bottom", 0),
                    (try_begin),
                        (lt, ":viewport_height", 525),
                        (store_sub, ":viewport_bottom", 525, ":viewport_height"),
                    (try_end),
                    (store_mul, ":top_y", "$g_lco_heroes", 25),
                    (val_max, ":top_y", 525),
                    (val_sub, ":top_y", 25),

                    # GENERATING MAIN CONTAINER

                    (call_script, "script_lco_create_label", "str_lco_i_hero_panel_title", 25, 652, 750, 0),
                    (call_script, "script_lco_create_label", "str_lco_i_hero_panel_title", 25, 652, 750, 0),

                    (call_script, "script_lco_create_container", 25, 125, 925, 525+2, 1),
                    (assign, "$g_lco_main_container", reg0),

                    # GENERATING HERO NAME PANELS AND ACTIVE HERO PANEL

                    (try_for_range, ":index", 0, "$g_lco_heroes"),
                        (troop_get_slot, ":troop_id", lco_storage, ":index"),
                        (store_add, ":hero_offset", "$g_lco_heroes", ":index"),
                        (troop_set_slot, lco_storage, ":hero_offset", ":troop_id"),
                        (store_mul, ":y", ":index", 25),
                        (store_sub, ":y", ":top_y", ":y"),
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 0, ":y", 310, 300),
                        (troop_set_slot, lco_storage, ":index", reg0),
                    (try_end),

                    (store_mul, ":y", "$g_lco_active_hero", 25),
                    (store_sub, ":y", ":top_y", ":y"),
                    (call_script, "script_lco_create_mesh", "mesh_lco_panel_down", 0, ":y", 310, 300),
                    (assign, "$g_lco_active_panel", reg0),

                    (val_add, ":top_y", 1),
                    (try_for_range, ":index", 0, "$g_lco_heroes"),
                        (store_add, ":hero_offset", "$g_lco_heroes", ":index"),
                        (troop_get_slot, ":troop_id", lco_storage, ":hero_offset"),
                        (store_mul, ":y", ":index", 25),
                        (store_sub, ":y", ":top_y", ":y"),
                        (call_script, "script_lco_troop_name_to_s40", ":troop_id"),
                        (call_script, "script_lco_create_label", "str_lco_s40", 5, ":y", 750, 0),
                    (try_end),

                    # GENERATING CONTENT CONTAINERS

                    (call_script, "script_lco_create_container", 225, ":viewport_bottom", 725, ":viewport_height", 0),
                    (assign, "$g_lco_attributes_1", reg0),
                    (call_script, "script_lco_create_container", 225, ":viewport_bottom", 725, ":viewport_height", 0),
                    (assign, "$g_lco_attributes_2", reg0),

                    # GENERATING HERO STATISTICS - FIRST PAGE

                    (set_container_overlay, "$g_lco_attributes_1"),

                    (try_for_range, ":index", 0, "$g_lco_heroes"),

                        (store_add, ":hero_offset", "$g_lco_heroes", ":index"),
                        (troop_get_slot, ":troop_id", lco_storage, ":hero_offset"),
                        (store_sub, ":y", "$g_lco_heroes", ":index"),
                        (val_sub, ":y", 1),
                        (val_mul, ":y", 25),
                        (store_add, ":yt", ":y", 1),

                        # Generating 1st block panel
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 0, ":y", 353, 300),
                        (store_character_level, reg40, ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 20, ":yt"),
                        (troop_get_xp, reg40, ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 65, ":yt"),
                        (call_script, "script_lco_xp_to_next_level", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 125, ":yt"),
                        (store_troop_health, reg40, ":troop_id", 1),
                        (store_troop_health, reg42, ":troop_id", 0),
                        (store_mul, reg41, reg40, 10000),
                        (val_div, reg41, reg42),
                        (val_add, reg41, 50),
                        (val_div, reg41, 100), # This and the previous line ensures correct rounding
                        (call_script, "script_lco_text_label", "str_lco_reg40_41", 180, ":yt"),
                        (try_begin),
                            (eq, ":troop_id", "trp_player"),
                            (assign, reg40, 100),
                        (else_try),
                            (call_script, "script_npc_morale", ":troop_id"),
                            (assign, reg40, reg0),
                        (try_end),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 225, ":yt"),

                        # Generating 2nd block panel
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 255, ":y", 183, 300),
                        (store_attribute_level, reg40, ":troop_id", ca_strength),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 275, ":yt"),
                        (store_attribute_level, reg40, ":troop_id", ca_agility),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 305, ":yt"),
                        (store_attribute_level, reg40, ":troop_id", ca_intelligence),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 335, ":yt"),
                        (store_attribute_level, reg40, ":troop_id", ca_charisma),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 365, ":yt"),

                        # Generating 3rd block panel
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 390, ":y", 183, 300),
                        (store_skill_level, reg40, "skl_ironflesh", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 410, ":yt"),
                        (store_skill_level, reg40, "skl_power_strike", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 440, ":yt"),
                        (store_skill_level, reg40, "skl_power_throw", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 470, ":yt"),
                        (store_skill_level, reg40, "skl_power_draw", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 500, ":yt"),

                        # Generating 4th block panel
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 525, ":y", 268, 300),
                        (store_skill_level, reg40, "skl_weapon_master", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 545, ":yt"),
                        (store_skill_level, reg40, "skl_shield", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 575, ":yt"),
                        (store_skill_level, reg40, "skl_athletics", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 605, ":yt"),
                        (store_skill_level, reg40, "skl_riding", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 635, ":yt"),
                        (store_skill_level, reg40, "skl_horse_archery", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 665, ":yt"),
                        (store_skill_level, reg40, "skl_looting", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 695, ":yt"),

                    (try_end),

                    # GENERATING HERO STATISTICS - SECOND PAGE

                    (set_container_overlay, "$g_lco_attributes_2"),

                    (try_for_range, ":index", 0, "$g_lco_heroes"),

                        (store_add, ":hero_offset", "$g_lco_heroes", ":index"),
                        (troop_get_slot, ":troop_id", lco_storage, ":hero_offset"),
                        (store_sub, ":y", "$g_lco_heroes", ":index"),
                        (val_mul, ":y", 25),
                        (val_sub, ":y", 25),
                        (store_add, ":yt", ":y", 1),

                        # Generating 5th block panel
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 0, ":y", 486, 300),
                        (store_skill_level, reg40, "skl_trainer", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 20, ":yt"),
                        (store_skill_level, reg40, "skl_tracking", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 50, ":yt"),
                        (store_skill_level, reg40, "skl_tactics", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 80, ":yt"),
                        (store_skill_level, reg40, "skl_pathfinding", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 110, ":yt"),
                        (store_skill_level, reg40, "skl_spotting", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 140, ":yt"),
                        (store_skill_level, reg40, "skl_inventory_management", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 170, ":yt"),
                        (store_skill_level, reg40, "skl_wound_treatment", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 200, ":yt"),
                        (store_skill_level, reg40, "skl_surgery", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 230, ":yt"),
                        (store_skill_level, reg40, "skl_first_aid", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 260, ":yt"),
                        (store_skill_level, reg40, "skl_engineer", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 290, ":yt"),
                        (store_skill_level, reg40, "skl_persuasion", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 320, ":yt"),

                        # Generating 6th block panel
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 350, ":y", 141, 300),
                        (store_skill_level, reg40, "skl_prisoner_management", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 370, ":yt"),
                        (store_skill_level, reg40, "skl_leadership", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 400, ":yt"),
                        (store_skill_level, reg40, "skl_trade", ":troop_id"),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 430, ":yt"),

                        # Generating 7th block panel
                        (call_script, "script_lco_create_mesh", "mesh_lco_panel", 455, ":y", 353, 300),
                        (store_proficiency_level, reg40, ":troop_id", wpt_one_handed_weapon),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 480, ":yt"),
                        (store_proficiency_level, reg40, ":troop_id", wpt_two_handed_weapon),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 520, ":yt"),
                        (store_proficiency_level, reg40, ":troop_id", wpt_polearm),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 560, ":yt"),
                        (store_proficiency_level, reg40, ":troop_id", wpt_archery),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 600, ":yt"),
                        (store_proficiency_level, reg40, ":troop_id", wpt_crossbow),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 640, ":yt"),
                        (store_proficiency_level, reg40, ":troop_id", wpt_throwing),
                        (call_script, "script_lco_text_label", "str_lco_reg40", 680, ":yt"),

                    (try_end),

                    (set_container_overlay, -1),

                    # GENERATING TITLES - FIRST PAGE

                    (call_script, "script_lco_create_container", 250, 655, 730, 95, 1),
                    (assign, "$g_lco_titles_1", reg0),

                    (str_store_string, s0, "str_lco_c_level"),
                    (call_script, "script_lco_text_caption", "str_s0", 20, 10),
                    (str_store_string, s0, "str_lco_c_xp"),
                    (call_script, "script_lco_text_caption", "str_s0", 65, 10),
                    (str_store_string, s0, "str_lco_c_xp2next_level"),
                    (call_script, "script_lco_text_caption", "str_s0", 125, 10),
                    (str_store_string, s0, "str_lco_c_hp"),
                    (call_script, "script_lco_text_caption", "str_s0", 180, 10),
                    (str_store_string, s0, "str_lco_c_morale"),
                    (call_script, "script_lco_text_caption", "str_s0", 225, 10),
                    (str_store_string, s0, "str_lco_c_str"),
                    (call_script, "script_lco_text_caption", "str_s0", 275, 10),
                    (str_store_string, s0, "str_lco_c_agi"),
                    (call_script, "script_lco_text_caption", "str_s0", 305, 10),
                    (str_store_string, s0, "str_lco_c_int"),
                    (call_script, "script_lco_text_caption", "str_s0", 335, 10),
                    (str_store_string, s0, "str_lco_c_cha"),
                    (call_script, "script_lco_text_caption", "str_s0", 365, 10),
                    (str_store_string, s0, "str_lco_c_ironflesh"),
                    (call_script, "script_lco_text_caption", "str_s0", 410, 10),
                    (str_store_string, s0, "str_lco_c_pstrike"),
                    (call_script, "script_lco_text_caption", "str_s0", 440, 10),
                    (str_store_string, s0, "str_lco_c_pthrow"),
                    (call_script, "script_lco_text_caption", "str_s0", 470, 10),
                    (str_store_string, s0, "str_lco_c_pdraw"),
                    (call_script, "script_lco_text_caption", "str_s0", 500, 10),
                    (str_store_string, s0, "str_lco_c_wmaster"),
                    (call_script, "script_lco_text_caption", "str_s0", 545, 10),
                    (str_store_string, s0, "str_lco_c_shield"),
                    (call_script, "script_lco_text_caption", "str_s0", 575, 10),
                    (str_store_string, s0, "str_lco_c_athletics"),
                    (call_script, "script_lco_text_caption", "str_s0", 605, 10),
                    (str_store_string, s0, "str_lco_c_riding"),
                    (call_script, "script_lco_text_caption", "str_s0", 635, 10),
                    (str_store_string, s0, "str_lco_c_harchery"),
                    (call_script, "script_lco_text_caption", "str_s0", 665, 10),
                    (str_store_string, s0, "str_lco_c_looting"),
                    (call_script, "script_lco_text_caption", "str_s0", 695, 10),

                    (set_container_overlay, -1),

                    # GENERATING TITLES - SECOND PAGE

                    (call_script, "script_lco_create_container", 250, 655, 730, 95, 1),
                    (assign, "$g_lco_titles_2", reg0),

                    (str_store_string, s0, "str_lco_c_trainer"),
                    (call_script, "script_lco_text_caption", "str_s0", 20, 10),
                    (str_store_string, s0, "str_lco_c_tracking"),
                    (call_script, "script_lco_text_caption", "str_s0", 50, 10),
                    (str_store_string, s0, "str_lco_c_tactics"),
                    (call_script, "script_lco_text_caption", "str_s0", 80, 10),
                    (str_store_string, s0, "str_lco_c_pathfinding"),
                    (call_script, "script_lco_text_caption", "str_s0", 110, 10),
                    (str_store_string, s0, "str_lco_c_spotting"),
                    (call_script, "script_lco_text_caption", "str_s0", 140, 10),
                    (str_store_string, s0, "str_lco_c_invmanage"),
                    (call_script, "script_lco_text_caption", "str_s0", 170, 10),
                    (str_store_string, s0, "str_lco_c_woundtreat"),
                    (call_script, "script_lco_text_caption", "str_s0", 200, 10),
                    (str_store_string, s0, "str_lco_c_surgery"),
                    (call_script, "script_lco_text_caption", "str_s0", 230, 10),
                    (str_store_string, s0, "str_lco_c_firstaid"),
                    (call_script, "script_lco_text_caption", "str_s0", 260, 10),
                    (str_store_string, s0, "str_lco_c_engineer"),
                    (call_script, "script_lco_text_caption", "str_s0", 290, 10),
                    (str_store_string, s0, "str_lco_c_persuasion"),
                    (call_script, "script_lco_text_caption", "str_s0", 320, 10),
                    (str_store_string, s0, "str_lco_c_pmanage"),
                    (call_script, "script_lco_text_caption", "str_s0", 370, 10),
                    (str_store_string, s0, "str_lco_c_leadership"),
                    (call_script, "script_lco_text_caption", "str_s0", 400, 10),
                    (str_store_string, s0, "str_lco_c_trade"),
                    (call_script, "script_lco_text_caption", "str_s0", 430, 10),
                    (str_store_string, s0, "str_lco_c_1hw"),
                    (call_script, "script_lco_text_caption", "str_s0", 480, 10),
                    (str_store_string, s0, "str_lco_c_2hw"),
                    (call_script, "script_lco_text_caption", "str_s0", 520, 10),
                    (str_store_string, s0, "str_lco_c_polearms"),
                    (call_script, "script_lco_text_caption", "str_s0", 560, 10),
                    (str_store_string, s0, "str_lco_c_bows"),
                    (call_script, "script_lco_text_caption", "str_s0", 600, 10),
                    (str_store_string, s0, "str_lco_c_xbows"),
                    (call_script, "script_lco_text_caption", "str_s0", 640, 10),
                    (str_store_string, s0, "str_lco_c_throwing"),
                    (call_script, "script_lco_text_caption", "str_s0", 680, 10),

                    (set_container_overlay, -1),

                    # APPLYING CURRENT PAGE SETTINGS

                    (try_begin),
                        (eq, "$g_lco_page", 0),
                        (overlay_set_display, "$g_lco_titles_1", 1),
                        (overlay_set_display, "$g_lco_attributes_1", 1),
                        (overlay_set_display, "$g_lco_titles_2", 0),
                        (overlay_set_display, "$g_lco_attributes_2", 0),
                    (else_try),
                        (overlay_set_display, "$g_lco_titles_1", 0),
                        (overlay_set_display, "$g_lco_attributes_1", 0),
                        (overlay_set_display, "$g_lco_titles_2", 1),
                        (overlay_set_display, "$g_lco_attributes_2", 1),
                    (try_end),

                ]
            ), # End of ti_on_presentation_load

            (ti_on_presentation_event_state_change,
                [
                    (store_trigger_param_1, ":overlay_id"),
                    (store_trigger_param_2, ":value"),
                    (try_begin),
                        (eq, ":overlay_id", "$g_lco_return"),
                        (call_script, "script_lco_clear_all_items", "$g_lco_garbage_troop"),
                        (assign, "$g_lco_garbage_troop", lco_garbage),
                        (jump_to_menu, "mnu_lco_auto_return"),
                        (presentation_set_duration, 0),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_dialog"),
                        (try_begin),
                            (gt, "$g_lco_heroes", 0), # Safety check
                            (store_add, ":hero_offset", "$g_lco_heroes", "$g_lco_active_hero"),
                            (troop_get_slot, "$g_lco_target", lco_storage, ":hero_offset"),
                            (assign, "$g_lco_operation", lco_view_character),
                            (jump_to_menu, "mnu_lco_auto_return"),
                            (presentation_set_duration, 0),
                        (try_end),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_inc_0"),
                        (assign, "$g_lco_include_companions", ":value"),
                        (presentation_set_duration, 0),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_inc_1"),
                        (assign, "$g_lco_include_lords", ":value"),
                        (presentation_set_duration, 0),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_inc_2"),
                        (assign, "$g_lco_include_regulars", ":value"),
                        (presentation_set_duration, 0),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_switch_page_0"),
                        (neq, "$g_lco_page", 0),
                        (assign, "$g_lco_page", 0),
                        (position_set_x, pos60, 25),
                        (position_set_y, pos60, 685),
                        (overlay_set_position, "$g_lco_selected_page", pos60),
                        (overlay_set_display, "$g_lco_titles_1", 1),
                        (overlay_set_display, "$g_lco_attributes_1", 1),
                        (overlay_set_display, "$g_lco_titles_2", 0),
                        (overlay_set_display, "$g_lco_attributes_2", 0),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_switch_page_1"),
                        (neq, "$g_lco_page", 1),
                        (assign, "$g_lco_page", 1),
                        (position_set_x, pos60, 55),
                        (position_set_y, pos60, 685),
                        (overlay_set_position, "$g_lco_selected_page", pos60),
                        (overlay_set_display, "$g_lco_titles_1", 0),
                        (overlay_set_display, "$g_lco_attributes_1", 0),
                        (overlay_set_display, "$g_lco_titles_2", 1),
                        (overlay_set_display, "$g_lco_attributes_2", 1),
                    (else_try),
                        (eq, ":overlay_id", "$g_lco_switch_page_2"),
                        (assign, "$g_lco_page", 2),
                        (presentation_set_duration, 0),
                    (try_end),
                ]
            ), # End of ti_on_presentation_event_state_change

            (ti_on_presentation_run,
                [
                    # ESC quits the presentation
                    (try_begin),
                        (key_clicked, key_escape),
                        (call_script, "script_lco_clear_all_items", "$g_lco_garbage_troop"),
                        (assign, "$g_lco_garbage_troop", lco_garbage),
                        (jump_to_menu, "mnu_lco_auto_return"),
                        (presentation_set_duration, 0),
                    (try_end),
                    # TAB switches between two pages of stats
                    (try_begin),
                        (key_clicked, key_tab),
                        (try_begin),
                            (this_or_next|key_is_down, key_left_control),
                            (key_is_down, key_right_control),
                            (assign, "$g_lco_page", 2),
                            (presentation_set_duration, 0),
                        (else_try),
                            (neg|key_is_down, key_left_alt),
                            (neg|key_is_down, key_right_alt),
                            (val_add, "$g_lco_page", 1),
                            (val_mod, "$g_lco_page", 2),
                            (try_begin),
                                (eq, "$g_lco_page", 0),
                                (position_set_x, pos60, 25),
                                (position_set_y, pos60, 685),
                                (overlay_set_position, "$g_lco_selected_page", pos60),
                                (overlay_set_display, "$g_lco_titles_1", 1),
                                (overlay_set_display, "$g_lco_attributes_1", 1),
                                (overlay_set_display, "$g_lco_titles_2", 0),
                                (overlay_set_display, "$g_lco_attributes_2", 0),
                            (else_try),
                                (position_set_x, pos60, 55),
                                (position_set_y, pos60, 685),
                                (overlay_set_position, "$g_lco_selected_page", pos60),
                                (overlay_set_display, "$g_lco_titles_1", 0),
                                (overlay_set_display, "$g_lco_attributes_1", 0),
                                (overlay_set_display, "$g_lco_titles_2", 1),
                                (overlay_set_display, "$g_lco_attributes_2", 1),
                            (try_end),
                        (try_end),
                    (try_end),
                ]
            ),

            (ti_on_presentation_mouse_press,
                [
                    (store_trigger_param_1, ":overlay_id"),
                    (store_trigger_param_2, ":mouse_button"),
                    (set_fixed_point_multiplier, 1000),
                    (try_begin),
                        (eq, ":mouse_button", 0), # Left mouse button

                        # Checking if it's one of hero panels
                        (try_begin),
                            (try_for_range, ":index", 0, "$g_lco_heroes"),
                                (troop_slot_eq, lco_storage, ":index", ":overlay_id"),
                                (assign, "$g_lco_active_hero", ":index"),
                                (set_container_overlay, "$g_lco_main_container"),
                                (store_mul, ":y", "$g_lco_active_hero", 25),
                                (assign, ":main_height_raw", 525),
                                (store_mul, ":top_y", "$g_lco_heroes", 25),
                                (val_max, ":top_y", ":main_height_raw"),
                                (val_sub, ":top_y", 25),
                                (store_sub, ":y", ":top_y", ":y"),
                                (position_set_x, pos60, 0),
                                (position_set_y, pos60, ":y"),
                                (overlay_set_position, "$g_lco_active_panel", pos60),
                                (try_begin),
                                    (this_or_next|key_is_down, key_left_alt),
                                    (key_is_down, key_right_alt),
                                    (store_add, ":hero_offset", "$g_lco_heroes", ":index"),
                                    (troop_get_slot, "$g_lco_target", lco_storage, ":hero_offset"),
                                    (assign, "$g_lco_operation", lco_view_character),
                                    (jump_to_menu, "mnu_lco_auto_return"),
                                    (presentation_set_duration, 0),
                                (try_end),
                            (try_end),
                        (try_end),
                    (try_end),
                ]
            ),

        ]
    ),

####################################################################################################################################
# LAV MODIFICATIONS END (COMPANIONS OVERSEER MOD)
####################################################################################################################################
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