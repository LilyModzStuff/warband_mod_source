# Formations AI for Warband by Motomataru
# rel. 03/03/11

from header_common import *
from header_operations import *
from header_mission_templates import *
from header_items import *
from header_presentations import *  # (COMPANIONS OVERSEER MOD)
from module_constants import *
from companions_constants import *  # (COMPANIONS OVERSEER MOD)

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

scripts = [
####################################################################################################################################
# LAV MODIFICATIONS START (COMPANIONS OVERSEER MOD)
####################################################################################################################################

    ("lco_item_name_to_s41",
        [
            (assign, ":ex_reg60", reg60),
            (assign, ":ex_reg61", reg61),
            (store_script_param, ":item_id", 1),
            (store_script_param, ":modifier", 2),
            (store_script_param, reg60, 3),
            (store_script_param, reg61, 4),
            (str_store_item_name, s41, ":item_id"),
            (try_begin),
                (gt, ":modifier", 0),
                (store_add, ":str_offset", "str_item_imod_name_0", ":modifier"),
                (str_store_string, s42, ":str_offset"),
                (str_store_string, s41, "str_lco_s42_s41"),
            (try_end),
            (try_begin),
                (gt, reg61, 1),
                (try_begin),
                    (item_get_type, ":item_type", ":item_id"),
                    (eq, ":item_type", itp_type_goods),
                    (str_store_string, s41, "str_lco_s41_reg60_reg61"),
                (else_try),
                    (str_store_string, s41, "str_lco_s41_reg60"),
                (try_end),
            (try_end),
            (assign, reg60, ":ex_reg60"),
            (assign, reg61, ":ex_reg61"),
        ]
    ),

    ("lco_fill_hero_panels",
        [
            (try_begin),
                (eq, "$g_lco_heroes", 0),
                (call_script, "script_lco_clear_all_items", lco_storage),
                (assign, ":troop_id", lco_storage),
            (else_try),
                (store_add, ":offset", "$g_lco_heroes", "$g_lco_active_hero"), # Slot ID where hero reference is stored
                (troop_get_slot, ":troop_id", lco_storage, ":offset"), # We got hero troop ID, now checking equipment
            (try_end),
            (store_mul, ":offset", "$g_lco_heroes", 2),
            (val_add, ":offset", 11), # Offset now points to first text overlay of hero equipment
            (str_clear, s40),
            (try_for_range, ":index", 0, 9),
                (store_add, ":overlay_offset", ":offset", ":index"),
                (troop_get_slot, ":overlay_id", lco_storage, ":overlay_offset"),
                (troop_get_inventory_slot, ":item_id", ":troop_id", ":index"),
                (try_begin),
                    (lt, ":item_id", 0),
                    (store_add, ":string_id", "str_lco_slot_name_0", ":index"),
                    (overlay_set_text, ":overlay_id", ":string_id"),
                    (overlay_set_color, ":overlay_id", 0x808080),
                (else_try),
                    (troop_get_inventory_slot_modifier, ":modifier", ":troop_id", ":index"),
                    (troop_inventory_slot_get_item_amount, ":qty", ":troop_id", ":index"),
                    (troop_inventory_slot_get_item_max_amount, ":qty_max", ":troop_id", ":index"),
                    (call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":qty", ":qty_max"),
                    (overlay_set_text, ":overlay_id", s41),
                    (overlay_set_color, ":overlay_id", 0x000000),
                (try_end),
            (try_end),
            # Update V1.1. Disable book slots configuration variable
            (try_begin),
                (eq, "$g_lco_suppress_books", 0),
                # Searching for books...
                (val_add, ":overlay_offset", 1),
                (assign, ":books_found", 0),
                (troop_get_inventory_capacity, ":capacity", ":troop_id"),
                (try_for_range, ":index", num_equipment_kinds, ":capacity"),
                    (troop_get_inventory_slot, ":item_id", ":troop_id", ":index"),
                    (ge, ":item_id", 0),
                    (item_get_type, ":item_type", ":item_id"),
                    (eq, ":item_type", itp_type_book),
                    (troop_get_inventory_slot_modifier, ":modifier", ":troop_id", ":index"),
                    (troop_inventory_slot_get_item_amount, ":qty", ":troop_id", ":index"),
                    (troop_inventory_slot_get_item_max_amount, ":qty_max", ":troop_id", ":index"),
                    (call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":qty", ":qty_max"),
                    (troop_get_slot, ":overlay_id", lco_storage, ":overlay_offset"),
                    (overlay_set_text, ":overlay_id", s41),
                    (overlay_set_color, ":overlay_id", 0x000000),
                    (val_add, ":overlay_offset", 1),
                    (val_add, ":books_found", 1),
                    (try_begin),
                        (gt, ":books_found", 1), # Found two books, so stopping
                        (assign, ":capacity", 0),
                    (try_end),
                (try_end),
                (try_for_range, ":index", ":books_found", 2),
                    (troop_get_slot, ":overlay_id", lco_storage, ":overlay_offset"),
                    (overlay_set_text, ":overlay_id", "str_lco_slot_name_9"),
                    (overlay_set_color, ":overlay_id", 0x808080),
                    (val_add, ":overlay_offset", 1),
                (try_end),
            (try_end),
        ]
    ),

    ("lco_fill_player_panels",
        [
            (store_mul, ":offset", "$g_lco_heroes", 2),
            (val_add, ":offset", 31), # Offset now points to first text overlay of player equipment
            (str_clear, s40),
            (try_for_range, ":index", 0, 9),
                (store_add, ":overlay_offset", ":offset", ":index"),
                (troop_get_slot, ":overlay_id", lco_storage, ":overlay_offset"),
                (troop_get_inventory_slot, ":item_id", "trp_player", ":index"),
                (try_begin),
                    (lt, ":item_id", 0),
                    (store_add, ":string_id", "str_lco_slot_name_0", ":index"),
                    (overlay_set_text, ":overlay_id", ":string_id"),
                    (overlay_set_color, ":overlay_id", 0x808080),
                (else_try),
                    (troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":index"),
                    (troop_inventory_slot_get_item_amount, ":qty", "trp_player", ":index"),
                    (troop_inventory_slot_get_item_max_amount, ":qty_max", "trp_player", ":index"),
                    (call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":qty", ":qty_max"),
                    (overlay_set_text, ":overlay_id", s41),
                    (overlay_set_color, ":overlay_id", 0x000000),
                (try_end),
            (try_end),
            # Displaying inventory
            (store_mul, ":offset", "$g_lco_heroes", 2),
            (val_add, ":offset", 40),
            (val_add, ":offset", "$g_lco_inv_slots"),
            (try_for_range, ":index", 0, "$g_lco_inv_slots"),
                (store_add, ":inventory_offset", ":index", num_equipment_kinds), # Actual inventory slot for player
                (store_add, ":overlay_offset", ":offset", ":index"),
                (troop_get_slot, ":overlay_id", lco_storage, ":overlay_offset"), # Text overlay for slot
                # Update V1.1. Checking slot frozen status and updating text color as necessary
                (try_begin),
                    (call_script, "script_cf_lco_slot_is_frozen", ":inventory_offset"),
                    (overlay_set_color, ":overlay_id", 0x000000FF),
                (else_try),
                    (overlay_set_color, ":overlay_id", 0x00000000),
                (try_end),
                (troop_get_inventory_slot, ":item_id", "trp_player", ":inventory_offset"),
                (try_begin),
                    (lt, ":item_id", 0),
                    (try_begin),
                        (call_script, "script_cf_lco_slot_is_frozen", ":inventory_offset"),
                        (overlay_set_color, ":overlay_id", 0x006060FF),
                        (overlay_set_text, ":overlay_id", "str_lco_slot_frozen"),
                    (else_try),
                        (overlay_set_text, ":overlay_id", s40),
                    (try_end),
                (else_try),
                    (troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":inventory_offset"),
                    (troop_inventory_slot_get_item_amount, ":qty", "trp_player", ":inventory_offset"),
                    (troop_inventory_slot_get_item_max_amount, ":qty_max", "trp_player", ":inventory_offset"),
                    (call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":qty", ":qty_max"),
                    (overlay_set_text, ":overlay_id", s41),
                (try_end),
            (try_end),
            # Displaying garbage/loot
            (val_add, ":offset", "$g_lco_inv_slots"),
            (val_add, ":offset", "$g_lco_garb_slots"),
            (try_for_range, ":index", 0, "$g_lco_garb_slots"),
                (store_add, ":overlay_offset", ":offset", ":index"),
                (troop_get_slot, ":overlay_id", lco_storage, ":overlay_offset"),
                (store_add, ":inventory_offset", ":index", num_equipment_kinds),
                (troop_get_inventory_slot, ":item_id", "$g_lco_garbage_troop", ":inventory_offset"),
                (try_begin),
                    (lt, ":item_id", 0),
                    (overlay_set_text, ":overlay_id", s40),
                (else_try),
                    (troop_get_inventory_slot_modifier, ":modifier", "$g_lco_garbage_troop", ":inventory_offset"),
                    (troop_inventory_slot_get_item_amount, ":qty", "$g_lco_garbage_troop", ":inventory_offset"),
                    (troop_inventory_slot_get_item_max_amount, ":qty_max", "$g_lco_garbage_troop", ":inventory_offset"),
                    (call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":qty", ":qty_max"),
                    (overlay_set_text, ":overlay_id", s41),
                (try_end),
            (try_end),
        ]
    ),

    ("cf_lco_is_active_panel",
        [
            (store_script_param_1, ":overlay"),
            (assign, ":found", 0),
            (store_mul, ":range1", "$g_lco_heroes", 2),
            (store_add, ":range2", ":range1", 11),
            # Checking hero equipment panels
            (try_for_range, ":index", ":range1", ":range2"),
                (troop_slot_eq, lco_storage, ":index", ":overlay"),
                (assign, ":found", 1),
            (try_end),
            # Checking player equipment panels
            (try_begin),
                (eq, ":found", 0),
                (val_add, ":range1", 22),
                (store_add, ":range2", ":range1", 9),
                (try_for_range, ":index", ":range1", ":range2"),
                    (troop_slot_eq, lco_storage, ":index", ":overlay"),
                    (assign, ":found", 1),
                (try_end),
            (try_end),
            # Checking player inventory panels
            (try_begin),
                (eq, ":found", 0),
                (val_add, ":range1", 18),
                (store_add, ":range2", ":range1", "$g_lco_inv_slots"),
                (try_for_range, ":index", ":range1", ":range2"),
                    (troop_slot_eq, lco_storage, ":index", ":overlay"),
                    (assign, ":found", 1),
                (try_end),
            (try_end),
            # Checking garbage/loot inventory panels
            (try_begin),
                (eq, ":found", 0),
                (val_add, ":range1", "$g_lco_inv_slots"), # Skipping player inventory panels
                (val_add, ":range1", "$g_lco_inv_slots"), # Skipping player inventory text labels
                (store_add, ":range2", ":range1", "$g_lco_garb_slots"),
                (try_for_range, ":index", ":range1", ":range2"),
                    (troop_slot_eq, lco_storage, ":index", ":overlay"),
                    (assign, ":found", 1),
                (try_end),
            (try_end),
            (eq, ":found", 1),
        ]
    ),

    ("lco_get_slot_details_for_panel",
        [
            (store_script_param_1, ":overlay"),
            (assign, reg0, -1),
            (assign, reg1, -1),
            (assign, reg2, -1),
            (assign, reg3, 0),
            (assign, reg4, 0),
            (assign, reg5, 0),
            (assign, ":found", 0),
            # Looking for hero equipment slots
            (store_mul, ":range1", "$g_lco_heroes", 2),
            (store_add, ":range2", ":range1", 11),
            (try_for_range, ":index", ":range1", ":range2"),
                (troop_slot_eq, lco_storage, ":index", ":overlay"),
                (store_add, ":hero_offset", "$g_lco_heroes", "$g_lco_active_hero"),
                (troop_get_slot, ":troop_id", lco_storage, ":hero_offset"),
                (store_sub, ":n_index", ":index", ":range1"),
                (try_begin),
                    (lt, ":n_index", 9),
                    (assign, reg0, ":troop_id"),
                    (assign, reg1, ":n_index"),
                (else_try),
                    (call_script, "script_lco_allocate_slots_for_books", ":troop_id"), # reg0 and reg1 now contain slot ids for first two books in inventory, or for empty slots
                    (try_begin),
                        (eq, ":n_index", 9),
                        (assign, reg1, reg0),
                    (try_end),
                    (assign, reg0, ":troop_id"),
                (try_end),
                (assign, ":found", 1),
            (try_end),
            # Looking for player equipment slots
            (try_begin),
                (eq, ":found", 0),
                (val_add, ":range1", 22),
                (store_add, ":range2", ":range1", 9),
                (try_for_range, ":index", ":range1", ":range2"),
                    (troop_slot_eq, lco_storage, ":index", ":overlay"),
                    (assign, reg0, "trp_player"),
                    (store_sub, reg1, ":index", ":range1"),
                    (assign, ":found", 1),
                (try_end),
            (try_end),
            # Looking for player inventory slots
            (try_begin),
                (eq, ":found", 0),
                (val_add, ":range1", 18),
                (store_add, ":range2", ":range1", "$g_lco_inv_slots"),
                (try_for_range, ":index", ":range1", ":range2"),
                    (troop_slot_eq, lco_storage, ":index", ":overlay"),
                    (assign, reg0, "trp_player"),
                    (store_sub, reg1, ":index", ":range1"),
                    (val_add, reg1, num_equipment_kinds),
                    (assign, ":found", 1),
                (try_end),
            (try_end),
            # Looking for garbage/loot inventory slots
            (try_begin),
                (eq, ":found", 0),
                (val_add, ":range1", "$g_lco_inv_slots"), # Skipping player inventory panels
                (val_add, ":range1", "$g_lco_inv_slots"), # Skipping player inventory text labels
                (store_add, ":range2", ":range1", "$g_lco_garb_slots"),
                (try_for_range, ":index", ":range1", ":range2"),
                    (troop_slot_eq, lco_storage, ":index", ":overlay"),
                    (assign, reg0, "$g_lco_garbage_troop"),
                    (store_sub, reg1, ":index", ":range1"),
                    (val_add, reg1, num_equipment_kinds),
                    (assign, ":found", 1),
                (try_end),
            (try_end),
            # Finally if found, filling item details
            (try_begin),
                (eq, ":found", 1),
                (troop_get_inventory_slot, reg2, reg0, reg1),
                (try_begin),
                    (ge, reg2, 0),
                    (troop_get_inventory_slot_modifier, reg3, reg0, reg1),
                    (troop_inventory_slot_get_item_amount, reg4, reg0, reg1),
                    (troop_inventory_slot_get_item_max_amount, reg5, reg0, reg1),
                (try_end),
            (try_end),
        ]
    ),

    # INPUT: arg1 = <troop_id>, arg2 = <slot_id>
    # OUTPUT: none, script modifies some $g_lco_* variables which are tracked by ti_on_presentation_run trigger in prsnt_overview_equipment
    ("lco_drag_item",
        [
            (store_script_param_1, ":troop_id"),
            (store_script_param_2, ":slot_id"),
            (try_begin),
                (call_script, "script_cf_lco_controllable", ":troop_id"),
                (troop_get_inventory_slot, ":item_id", ":troop_id", ":slot_id"),
                (try_begin),
                    (ge, ":item_id", 0),
                    (assign, "$g_lco_drag_item", ":item_id"),
                    (troop_get_inventory_slot_modifier, "$g_lco_drag_modifier", ":troop_id", ":slot_id"),
                    (troop_inventory_slot_get_item_amount, "$g_lco_drag_quantity", ":troop_id", ":slot_id"),
                    (troop_inventory_slot_get_item_max_amount, "$g_lco_drag_quantity_max", ":troop_id", ":slot_id"),
                    (assign, "$g_lco_dragging_from", ":troop_id"),
                    (assign, "$g_lco_dragging_from_slot", ":slot_id"),
                    # Displaying overlay
                    (call_script, "script_lco_item_name_to_s41", ":item_id", "$g_lco_drag_modifier", "$g_lco_drag_quantity", "$g_lco_drag_quantity_max"),
                    (overlay_set_text, "$g_lco_dragging_text", s41),
                    (overlay_set_display, "$g_lco_dragging_panel", 1),
                    (assign, "$g_lco_dragging", 1),
                    (troop_set_inventory_slot, ":troop_id", ":slot_id", -1),
                    (try_begin),
                        (eq, ":troop_id", "$g_lco_garbage_troop"),
                        (troop_sort_inventory, "$g_lco_garbage_troop"),
                    (try_end),
                (try_end),
            (else_try),
                (display_message, "str_lco_drop_error_control", 0xFF4040),
            (try_end),
        ]
    ),

    ("lco_cancel_drag_item",
        [
            (try_begin),
                (eq, "$g_lco_dragging", 1), # Safety check
                (try_begin),
                    # Trying to deposit the item where it originally belongs
                    (troop_get_inventory_slot, ":stored_id", "$g_lco_dragging_from", "$g_lco_dragging_from_slot"),
                    (lt, ":stored_id", 0),
                    (troop_set_inventory_slot, "$g_lco_dragging_from", "$g_lco_dragging_from_slot", "$g_lco_drag_item"),
                    (troop_set_inventory_slot_modifier, "$g_lco_dragging_from", "$g_lco_dragging_from_slot", "$g_lco_drag_modifier"),
                    (try_begin),
                        (gt, "$g_lco_drag_quantity", 0),
                        (troop_inventory_slot_set_item_amount, "$g_lco_dragging_from", "$g_lco_dragging_from_slot", "$g_lco_drag_quantity"),
                    (try_end),
                    (assign, "$g_lco_dragging", 0),
                (else_try),
                    # Original slot is occupied, so trying to drop the dragged item to player's inventory
                    (troop_get_inventory_capacity, ":capacity", "trp_player"),
                    (try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
                        (troop_get_inventory_slot, ":stored_id", "trp_player", ":slot_id"),
                        (lt, ":stored_id", 0),
                        (troop_set_inventory_slot, "trp_player", ":slot_id", "$g_lco_drag_item"),
                        (troop_set_inventory_slot_modifier, "trp_player", ":slot_id", "$g_lco_drag_modifier"),
                        (try_begin),
                            (gt, "$g_lco_drag_quantity", 0),
                            (troop_inventory_slot_set_item_amount, "trp_player", ":slot_id", "$g_lco_drag_quantity"),
                        (try_end),
                        (assign, "$g_lco_dragging", 0),
                        (assign, ":capacity", 0), # Break cycle
                    (try_end),
                    (eq, "$g_lco_dragging", 0), # Check for success
                (else_try),
                    # Player inventory is full, trying to deposit item to garbage
                    (troop_get_inventory_capacity, ":capacity", "$g_lco_garbage_troop"),
                    (try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
                        (troop_get_inventory_slot, ":stored_id", "$g_lco_garbage_troop", ":slot_id"),
                        (lt, ":stored_id", 0),
                        (troop_set_inventory_slot, "$g_lco_garbage_troop", ":slot_id", "$g_lco_drag_item"),
                        (troop_set_inventory_slot_modifier, "$g_lco_garbage_troop", ":slot_id", "$g_lco_drag_modifier"),
                        (try_begin),
                            (gt, "$g_lco_drag_quantity", 0),
                            (troop_inventory_slot_set_item_amount, "$g_lco_garbage_troop", ":slot_id", "$g_lco_drag_quantity"),
                        (try_end),
                        (assign, "$g_lco_dragging", 0),
                        (assign, ":capacity", 0), # Break cycle
                        (troop_sort_inventory, "$g_lco_garbage_troop"),
                    (try_end),
                (try_end),
                # If no longer dragging, we need to make proper modifications
                (try_begin),
                    (eq, "$g_lco_dragging", 0),
                    (assign, "$g_lco_dragging_from", 0),      # Troop ID of dragged item current owner
                    (assign, "$g_lco_dragging_from_slot", 0), # Slot ID of dragged item current owner
                    (assign, "$g_lco_drag_item", -1),         # Item type currently being dragged
                    (assign, "$g_lco_drag_modifier", 0),      # Modifier of item currently being dragged
                    (assign, "$g_lco_drag_quantity", 0),      # Quantity of item currently being dragged (for foods)
                    (assign, "$g_lco_drag_quantity_max", 0),  # Max quantity of item currently being dragged (for foods)
                    (overlay_set_display, "$g_lco_dragging_panel", 0),
                (try_end),
            (try_end),
        ]
    ),

    ("lco_drop_item",
        [
            (store_script_param_1, ":troop_id"),
            (store_script_param_2, ":slot_id"),
            (try_begin),
                # If user is dropping item to garbage, then we override normal procedure and just drop the item, even if player is clicking on a filled panel
                (eq, ":troop_id", "$g_lco_garbage_troop"),
                (call_script, "script_lco_discard_item", "$g_lco_drag_item", "$g_lco_drag_modifier", "$g_lco_drag_quantity"),
                (assign, "$g_lco_dragging_from", 0),      # Troop ID of dragged item current owner
                (assign, "$g_lco_dragging_from_slot", 0), # Slot ID of dragged item current owner
                (assign, "$g_lco_drag_item", -1),         # Item type currently being dragged
                (assign, "$g_lco_drag_modifier", 0),      # Modifier of item currently being dragged
                (assign, "$g_lco_drag_quantity", 0),      # Quantity of item currently being dragged (for foods)
                (assign, "$g_lco_drag_quantity_max", 0),  # Max quantity of item currently being dragged (for foods)
                (assign, "$g_lco_dragging", 0),
                (overlay_set_display, "$g_lco_dragging_panel", 0),
            (else_try),
                (call_script, "script_cf_lco_controllable", ":troop_id"),
                (troop_get_inventory_slot, ":ex_item_id", ":troop_id", ":slot_id"),
                (troop_get_inventory_slot_modifier, ":ex_modifier", ":troop_id", ":slot_id"),
                (troop_inventory_slot_get_item_amount, ":ex_quantity", ":troop_id", ":slot_id"),
                (troop_inventory_slot_get_item_max_amount, ":ex_quantity_max", ":troop_id", ":slot_id"),
                (troop_set_inventory_slot, ":troop_id", ":slot_id", "$g_lco_drag_item"),
                (troop_set_inventory_slot_modifier, ":troop_id", ":slot_id", "$g_lco_drag_modifier"),
                (try_begin),
                    (gt, "$g_lco_drag_quantity", 0),
                    (troop_inventory_slot_set_item_amount, ":troop_id", ":slot_id", "$g_lco_drag_quantity"),
                (try_end),
                (try_begin),
                    (ge, ":ex_item_id", 0),
                    (assign, "$g_lco_drag_item", ":ex_item_id"),
                    (assign, "$g_lco_drag_modifier", ":ex_modifier"),
                    (assign, "$g_lco_drag_quantity", ":ex_quantity"),
                    (assign, "$g_lco_drag_quantity_max", ":ex_quantity_max"),
                    (assign, "$g_lco_dragging_from", ":troop_id"),
                    (assign, "$g_lco_dragging_from_slot", ":slot_id"),
                    # Displaying overlay
                    (call_script, "script_lco_item_name_to_s41", "$g_lco_drag_item", "$g_lco_drag_modifier", "$g_lco_drag_quantity", "$g_lco_drag_quantity_max"),
                    (overlay_set_text, "$g_lco_dragging_text", s41),
                    (overlay_set_display, "$g_lco_dragging_panel", 1), # Not necessary but just in case
                    (assign, "$g_lco_dragging", 1), # Not necessary but just in case
                (else_try),
                    (assign, "$g_lco_dragging_from", 0),      # Troop ID of dragged item current owner
                    (assign, "$g_lco_dragging_from_slot", 0), # Slot ID of dragged item current owner
                    (assign, "$g_lco_drag_item", -1),         # Item type currently being dragged
                    (assign, "$g_lco_drag_modifier", 0),      # Modifier of item currently being dragged
                    (assign, "$g_lco_drag_quantity", 0),      # Quantity of item currently being dragged (for foods)
                    (assign, "$g_lco_drag_quantity_max", 0),  # Max quantity of item currently being dragged (for foods)
                    (assign, "$g_lco_dragging", 0),
                    (overlay_set_display, "$g_lco_dragging_panel", 0),
                (try_end),
            (else_try),
                (display_message, "str_lco_drop_error_control", 0xFF4040),
            (try_end),

        ]
    ),

    # OUTPUT: reg0 = error string if cannot drop
    ("cf_lco_can_drop_item",
        [
            (store_script_param, ":troop_id", 1),
            (store_script_param, ":slot_id", 2),
            (store_script_param, ":item_id", 3),
            (store_script_param, ":modifier", 4),

            (assign, reg0, "str_lco_drop_error_control"),
            (call_script, "script_cf_lco_controllable", ":troop_id"),

            (assign, ":can_drop", 0),
            (assign, ":result", "str_lco_drop_error_type"),
            (try_begin),
                (ge, ":slot_id", num_equipment_kinds),
                (try_begin),
                    (this_or_next|eq, ":troop_id", "trp_player"),
                    (eq, ":troop_id", "$g_lco_garbage_troop"),
                    (assign, ":can_drop", 1), # We can drop anything into player's inventory slots or to the garbage
                (else_try),
                    (item_get_type, ":type", ":item_id"),
                    (eq, ":type", itp_type_book), # We can only drop books into other companions inventory slots
                    # Update V1.1. Disable book slots configuration variable
                    (eq, "$g_lco_suppress_books", 0),
                    (assign, ":can_drop", 1),
                (try_end),
            (else_try),
                (item_get_type, ":type", ":item_id"),
                (try_begin),
                    (lt, ":slot_id", 4), # Weapon slot
                    (this_or_next|eq, ":type", itp_type_one_handed_wpn),
                    (this_or_next|eq, ":type", itp_type_two_handed_wpn),
                    (this_or_next|eq, ":type", itp_type_polearm),
                    (this_or_next|eq, ":type", itp_type_arrows),
                    (this_or_next|eq, ":type", itp_type_bolts),
                    (this_or_next|eq, ":type", itp_type_shield),
                    (this_or_next|eq, ":type", itp_type_bow),
                    (this_or_next|eq, ":type", itp_type_crossbow),
                    (this_or_next|eq, ":type", itp_type_thrown),
                    (this_or_next|eq, ":type", itp_type_pistol),
                    (this_or_next|eq, ":type", itp_type_musket),
                    (eq, ":type", itp_type_bullets),
                    (assign, ":can_drop", 1),
                (else_try),
                    (eq, ":slot_id", 4), # Head armor
                    (eq, ":type", itp_type_head_armor),
                    (assign, ":can_drop", 1),
                (else_try),
                    (eq, ":slot_id", 5), # Body armor
                    (eq, ":type", itp_type_body_armor),
                    (assign, ":can_drop", 1),
                (else_try),
                    (eq, ":slot_id", 6), # Leg armor
                    (eq, ":type", itp_type_foot_armor),
                    (assign, ":can_drop", 1),
                (else_try),
                    (eq, ":slot_id", 7), # Hand armor
                    (eq, ":type", itp_type_hand_armor),
                    (assign, ":can_drop", 1),
                (else_try),
                    (eq, ":slot_id", 8), # Horse
                    (eq, ":type", itp_type_horse),
                    (assign, ":can_drop", 1),
                (try_end),
                (try_begin),
                    (eq, ":can_drop", 1), # Item and slot match by type, but can the character actually equip this item?
                    (neq, ":type", itp_type_arrows),  # Do not check for ammo
                    (neq, ":type", itp_type_bolts),   # Do not check for ammo
                    (neq, ":type", itp_type_bullets), # Do not check for ammo
                    # BugFix V1.1. Shields are no longer exempt from prerequisite checks.
                    #(neq, ":type", itp_type_shield), # Do not check for shields
                    (assign, ":result", "str_lco_drop_error_reqs"),
                    (call_script, "script_lco_replicate_attributes", ":troop_id"),
                    (call_script, "script_lco_clear_all_items", lco_storage),
                    (troop_set_auto_equip, lco_storage, 0),
                    (troop_set_inventory_slot, lco_storage, num_equipment_kinds, ":item_id"),
                    (troop_set_inventory_slot_modifier, lco_storage, num_equipment_kinds, ":modifier"),
                    # BugFix V1.1. Shields require some additional care
                    (try_begin),
                        (eq, ":type", itp_type_shield),
                        (troop_add_item, lco_storage, "itm_tutorial_club", imod_plain), # So the testing troop has both weapon and shield and auto-equip will work properly.
                    (try_end),
                    (troop_equip_items, lco_storage),
                    (troop_get_inventory_slot, ":copy_item_id", lco_storage, num_equipment_kinds),
                    (call_script, "script_lco_clear_all_items", lco_storage),
                    (ge, ":copy_item_id", 0), # He did not equip it!
                    (assign, ":can_drop", 0), # Hence original troop cannot equip it either!
                (try_end),
            (try_end),
            (assign, reg0, ":result"),
            (eq, ":can_drop", 1),
        ]
    ),

    ("lco_set_active_hero",
        [
            (store_script_param_1, ":index"),
            (assign, "$g_lco_active_hero", ":index"),
            (position_set_x, pos60, 25),
            (store_mul, ":base_y", "$g_lco_heroes", 25),
            (val_sub, ":base_y", 25),
            (val_max, ":base_y", 500),
            (store_mul, ":y", "$g_lco_active_hero", 25),
            (store_sub, ":y", ":base_y", ":y"),
            (position_set_y, pos60, ":y"),
            (overlay_set_position, "$g_lco_active_panel", pos60),
            (call_script, "script_lco_fill_hero_panels"),
        ]
    ),

    # This script will scan hero inventory and will return his "book" slots.
    # Slot numbers of first two books found in character inventory are used as the book slots.
    # If less than two books are found, remaining ones are picked from free slots in character inventory.
    ("lco_allocate_slots_for_books",
        [
            (store_script_param_1, ":troop_id"),
            (troop_sort_inventory, ":troop_id"),
            (troop_get_inventory_capacity, ":capacity", ":troop_id"),
            (assign, reg0, -1),
            (assign, reg1, -1),
            (try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
                (troop_get_inventory_slot, ":item_id", ":troop_id", ":slot_id"),
                (try_begin),
                    (ge, ":item_id", 0),
                    (item_get_type, ":type", ":item_id"),
                    (eq, ":type", itp_type_book),
                    (try_begin),
                        (eq, reg0, -1),
                        (assign, reg0, ":slot_id"),
                    (else_try),
                        (eq, reg1, -1),
                        (assign, reg1, ":slot_id"),
                    (try_end),
                (try_end),
            (try_end),
            (try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
                (troop_get_inventory_slot, ":item_id", ":troop_id", ":slot_id"),
                (try_begin),
                    (lt, ":item_id", 0),
                    (try_begin),
                        (eq, reg0, -1),
                        (assign, reg0, ":slot_id"),
                    (else_try),
                        (eq, reg1, -1),
                        (assign, reg1, ":slot_id"),
                    (try_end),
                (try_end),
            (try_end),
        ]
    ),

    ("cf_lco_auto_offer_item",
        [
            (store_script_param, ":troop_id", 1),
            (store_script_param, ":item_id", 2),
            (store_script_param, ":modifier", 3),
            (store_script_param, ":quantity", 4),
            (item_get_type, ":type", ":item_id"),
            (assign, ":out_item_id", -1),
            (assign, ":out_modifier", 0),
            (assign, ":out_quantity", 0),
            (assign, ":out_quantity_max", 0),
            (assign, ":is_equipped", 0),

            (call_script, "script_cf_lco_controllable", ":troop_id"), # Automatic failure

            # First option: if item is a weapon, troop has a free slot and can equip the item, we equip it by default
            (try_begin),
                (this_or_next|is_between, ":type", itp_type_one_handed_wpn, itp_type_goods),
                (is_between, ":type", itp_type_pistol, itp_type_animal),
                (try_for_range, ":slot_id", 0, 4),
                    (eq, ":is_equipped", 0),
                    (troop_get_inventory_slot, ":eq_item_id", ":troop_id", ":slot_id"),
                    (lt, ":eq_item_id", 0),
                    (call_script, "script_cf_lco_can_drop_item", ":troop_id", ":slot_id", ":item_id", ":modifier"),
                    (troop_set_inventory_slot, ":troop_id", ":slot_id", ":item_id"),
                    (troop_set_inventory_slot_modifier, ":troop_id", ":slot_id", ":modifier"),
                    (try_begin),
                        (gt, ":quantity", 0),
                        (troop_inventory_slot_set_item_amount, ":troop_id", ":slot_id", ":quantity"),
                    (try_end),
                    (assign, ":is_equipped", 1),
                (try_end),
            (try_end),

            # Second option: if item is a book, we automatically give it to troop, sort the inventory and look for books.
            # If we find more than two, we'll return the third.
            # TODO: When companion book reading is implemented, need to make proper checks here.
            # Companion should not automatically give away a book he's currently reading.
            (try_begin),
                (eq, ":is_equipped", 0),
                (eq, ":type", itp_type_book),
                # Update V1.1. Disable book slots configuration variable
                (eq, "$g_lco_suppress_books", 0),
                (troop_add_item, ":troop_id", ":item_id", ":modifier"),
                (assign, ":is_equipped", 1),
                (troop_sort_inventory, ":troop_id"),
                (troop_get_inventory_capacity, ":capacity", ":troop_id"),
                (assign, ":books_found", 0),
                (try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
                    (troop_get_inventory_slot, ":cur_item_id", ":troop_id", ":slot_id"),
                    (ge, ":cur_item_id", 0),
                    (item_get_type, ":cur_type", ":cur_item_id"),
                    (eq, ":cur_type", itp_type_book),
                    (try_begin),
                        (lt, ":books_found", 2),
                        (val_add, ":books_found", 1),
                    (else_try),
                        (assign, ":out_item_id", ":cur_item_id"),
                        (troop_set_inventory_slot, ":troop_id", ":slot_id", -1), # Delete book from inventory
                        (assign, ":capacity", 0), # Break cycle
                    (try_end),
                (try_end),
            (try_end),

            # Third option: we create a duplicate, give him an item and check if he will equip it.
            # If he will not equip it, it's a failure
            # If he will equip it, there may be zero, one or more items lying in inventory.
            # If it's zero, fine.
            # If it's one, also fine, we return it as a compensation item
            # If it's more than one, then we sort inventory and add ammo/shield items to free slots while there are free slots
            # Then we sort again and retrieve the first item in inventory as compensation
            (try_begin),
                (eq, ":is_equipped", 0),
                (neq, ":type", itp_type_goods),
                (neq, ":type", itp_type_animal),
                (neq, ":type", itp_type_book),
                (call_script, "script_lco_clear_all_items", lco_storage),
                (call_script, "script_lco_replicate_attributes", ":troop_id"),
                (call_script, "script_lco_replicate_equipment", ":troop_id"),
                (troop_add_item, lco_storage, ":item_id", ":modifier"),
                (troop_equip_items, lco_storage),
                (troop_sort_inventory, lco_storage),
                # Checking if our item is lying in inventory
                (assign, ":is_equipped", 1),
                (troop_get_inventory_capacity, ":capacity", ":troop_id"),
                (try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
                    (troop_get_inventory_slot, ":inv_item_id", lco_storage, ":slot_id"),
                    (troop_get_inventory_slot_modifier, ":inv_modifier", lco_storage, ":slot_id"),
                    (eq, ":item_id", ":inv_item_id"),
                    (eq, ":modifier", ":inv_modifier"),
                    (assign, ":is_equipped", 0), # Troop refused to equip our item, so no sense checking further
                    (assign, ":capacity", 0), # Break cycle
                (try_end),
                # Since it's not, we are now looking for a slot to put the item in.
                (try_begin),
                    (eq, ":is_equipped", 1),
                    (assign, ":swap_slot", -1),
                    (try_begin),
                        (eq, ":type", itp_type_horse),
                        (assign, ":swap_slot", 8),
                    (else_try),
                        (is_between, ":type", itp_type_head_armor, itp_type_pistol),
                        (store_sub, ":swap_slot", ":type", 8),
                    (else_try),
                        # Our item is a weapon or ammo.
                        # This means we have at least one item in inventory (if there was an empty weapon slot it would be filled on first option).
                        # Now we look for the first item that is not ammo. If we find it, this is the swapped item.
                        (assign, ":swap_item_id", -1),
                        (assign, ":swap_item_mod", 0),
                        (try_for_range, ":slot_id", num_equipment_kinds, num_equipment_kinds+5), # Because there cannot be more items by code design
                            (eq, ":swap_item_id", -1), # Not yet found
                            (troop_get_inventory_slot, ":cur_item_id", lco_storage, ":slot_id"),
                            (ge, ":cur_item_id", 0), # Slot is not empty
                            (item_get_type, ":cur_type", ":cur_item_id"),
                            (this_or_next|is_between, ":cur_type", itp_type_one_handed_wpn, itp_type_arrows),
                            (this_or_next|is_between, ":cur_type", itp_type_bow, itp_type_goods),
                            (is_between, ":cur_type", itp_type_pistol, itp_type_bullets),
                            (assign, ":swap_item_id", ":cur_item_id"),
                            (troop_get_inventory_slot_modifier, ":swap_item_mod", lco_storage, ":slot_id"),
                        (try_end),
                        # If we didn't find a weapon, then we look for ammo and choose the last in the list (least expensive)
                        (try_for_range_backwards, ":slot_id", num_equipment_kinds, num_equipment_kinds+5), # Because there cannot be more items by code design
                            (eq, ":swap_item_id", -1), # Not yet found
                            (troop_get_inventory_slot, ":cur_item_id", lco_storage, ":slot_id"),
                            (ge, ":cur_item_id", 0), # Slot is not empty
                            (item_get_type, ":cur_type", ":cur_item_id"),
                            (this_or_next|eq, ":cur_type", itp_type_bullets),
                            (is_between, ":cur_type", itp_type_arrows, itp_type_shield),
                            (assign, ":swap_item_id", ":cur_item_id"),
                            (troop_get_inventory_slot_modifier, ":swap_item_mod", lco_storage, ":slot_id"),
                        (try_end),
                        # If we didn't find anything, that's an error and we report it. Otherwise, we are looking for swap_item slot in the original troop equipment
                        (try_begin),
                            (eq, ":swap_item_id", -1),
                            (display_message, "str_lco_impossible_error"),
                        (else_try),
                            (try_for_range, ":slot_id", 0, num_equipment_kinds),
                                (troop_get_inventory_slot, ":cur_item_id", ":troop_id", ":slot_id"),
                                (troop_get_inventory_slot_modifier, ":cur_item_mod", ":troop_id", ":slot_id"),
                                (eq, ":cur_item_id", ":swap_item_id"),
                                (eq, ":cur_item_mod", ":swap_item_mod"),
                                (assign, ":swap_slot", ":slot_id"),
                            (try_end),
                        (try_end),
                    (try_end),

                    # Now we have ":swap_slot" keeping the slot id in the original troop equipment that we are putting offered item to.
                    (try_begin),
                        (eq, ":swap_slot", -1),
                        (assign, ":is_equipped", 0),
                    (else_try),
                        (troop_get_inventory_slot, ":out_item_id", ":troop_id", ":swap_slot"),
                        (troop_get_inventory_slot_modifier, ":out_modifier", ":troop_id", ":swap_slot"),
                        (troop_inventory_slot_get_item_amount, ":out_quantity", ":troop_id", ":swap_slot"),
                        (troop_inventory_slot_get_item_max_amount, ":out_quantity", ":troop_id", ":swap_slot"),
                        (troop_set_inventory_slot, ":troop_id", ":swap_slot", ":item_id"),
                        (troop_set_inventory_slot_modifier, ":troop_id", ":swap_slot", ":modifier"),
                        (assign, ":is_equipped", 1),
                    (try_end),
                (try_end),
            (try_end),

            (eq, ":is_equipped", 1),
            (assign, reg0, ":out_item_id"),
            (assign, reg1, ":out_modifier"),
            (assign, reg2, ":out_quantity"),
            (assign, reg3, ":out_quantity_max"),
        ]
    ),

    ("lco_backup_inventory",
        [
            (store_script_param_1, ":troop_id"),
            (call_script, "script_lco_clear_all_items", lco_storage),
            (troop_set_auto_equip, lco_storage, 0),
            (troop_get_inventory_capacity, ":capacity", ":troop_id"),
            (assign, ":target_id", num_equipment_kinds),
            (try_for_range, ":source_id", num_equipment_kinds, ":capacity"),
                (troop_get_inventory_slot, ":item_id", ":troop_id", ":source_id"),
                (ge, ":item_id", 0),
                (troop_get_inventory_slot_modifier, ":modifier", ":troop_id", ":source_id"),
                (troop_inventory_slot_get_item_amount, ":qty", ":troop_id", ":source_id"),
                (troop_set_inventory_slot, lco_storage, ":target_id", ":item_id"),
                (troop_set_inventory_slot_modifier, lco_storage, ":target_id", ":modifier"),
                (try_begin),
                    (gt, ":qty", 0),
                    (troop_inventory_slot_set_item_amount, lco_storage, ":target_id", ":qty"),
                (try_end),
                (troop_set_inventory_slot, ":troop_id", ":source_id", -1),
                (val_add, ":target_id", 1),
            (try_end),
        ]
    ),

    ("lco_retrieve_inventory",
        [
            (store_script_param_1, ":troop_id"),
            (troop_sort_inventory, lco_storage),
            (troop_get_inventory_capacity, ":capacity", ":troop_id"),
            (assign, ":source_id", num_equipment_kinds),
            (try_for_range, ":target_id", num_equipment_kinds, ":capacity"),
                (troop_get_inventory_slot, ":cur_item_id", ":troop_id", ":target_id"),
                (lt, ":cur_item_id", 0), # Current slot empty?
                (troop_get_inventory_slot, ":item_id", lco_storage, ":source_id"),
                (ge, ":item_id", 0), # There is still an item in the storage?
                (troop_get_inventory_slot_modifier, ":modifier", lco_storage, ":source_id"),
                (troop_inventory_slot_get_item_amount, ":qty", lco_storage, ":source_id"),
                (troop_set_inventory_slot, ":troop_id", ":target_id", ":item_id"),
                (troop_set_inventory_slot_modifier, ":troop_id", ":target_id", ":modifier"),
                (try_begin),
                    (gt, ":qty", 0),
                    (troop_inventory_slot_set_item_amount, ":troop_id", ":target_id", ":qty"),
                (try_end),
                (val_add, ":source_id", 1),
            (try_end),
            (call_script, "script_lco_clear_all_items", lco_storage),
        ]
    ),

    ("lco_clear_all_items",
        [
            (store_script_param_1, ":troop_id"),
            (troop_clear_inventory, ":troop_id"),
            (try_for_range, ":index", 0, 9),
                (troop_set_inventory_slot, ":troop_id", ":index", -1), # Cleaning equipment
            (try_end),
        ]
    ),

    ("lco_replicate_attributes",
        [
            # BugFix V1.1. Added shield skill to the list of monitored skills and attributes.
            (store_script_param_1, ":troop_id"),
            (store_attribute_level, ":str", ":troop_id", ca_strength),
            (store_skill_level, ":pdraw", "skl_power_draw", ":troop_id"),
            (store_skill_level, ":pthrow", "skl_power_throw", ":troop_id"),
            (store_skill_level, ":riding", "skl_riding", ":troop_id"),
            (store_skill_level, ":shield", "skl_shield", ":troop_id"),
            (store_attribute_level, ":ex_str", lco_storage, ca_strength),
            (store_skill_level, ":ex_pdraw", "skl_power_draw", lco_storage),
            (store_skill_level, ":ex_pthrow", "skl_power_throw", lco_storage),
            (store_skill_level, ":ex_riding", "skl_riding", lco_storage),
            (store_skill_level, ":ex_shield", "skl_shield", lco_storage),
            (val_sub, ":str", ":ex_str"),
            (val_sub, ":pdraw", ":ex_pdraw"),
            (val_sub, ":pthrow", ":ex_pthrow"),
            (val_sub, ":riding", ":ex_riding"),
            (val_sub, ":shield", ":ex_shield"),
            (troop_raise_attribute, lco_storage, ca_strength, ":str"),
            (troop_raise_skill, lco_storage, "skl_power_draw", ":pdraw"),
            (troop_raise_skill, lco_storage, "skl_power_throw", ":pthrow"),
            (troop_raise_skill, lco_storage, "skl_riding", ":riding"),
            (troop_raise_skill, lco_storage, "skl_shield", ":shield"),
        ]
    ),

    ("lco_replicate_equipment",
        [
            (store_script_param_1, ":troop_id"),
            (try_for_range, ":index", 0, num_equipment_kinds),
                (troop_get_inventory_slot, ":item_id", ":troop_id", ":index"),
                (troop_get_inventory_slot_modifier, ":modifier", ":troop_id", ":index"),
                (troop_set_inventory_slot, lco_storage, ":index", ":item_id"),
                (troop_set_inventory_slot_modifier, lco_storage, ":index", ":modifier"),
            (try_end),
        ]
    ),

    ("lco_hero_grab_equipment",
        [
            (store_script_param, ":troop_id", 1),
            (assign, ":hero_offset", num_equipment_kinds),
            (troop_get_inventory_capacity, ":capacity", "trp_player"),
            (troop_get_inventory_capacity, ":hero_capacity", ":troop_id"),
            (try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
                (try_begin),
                    (call_script, "script_cf_lco_slot_is_frozen", ":slot_id"), # If current slot is frozen, we skip it in either case
                (else_try),
                    (troop_get_inventory_slot, ":item_id", "trp_player", ":slot_id"),
                    (ge, ":item_id", 0),
                    (assign, ":grab", 0),
                    (item_get_type, ":type", ":item_id"),
                    # Will companion grab this item?
                    (try_begin),
                        (eq, "$g_lco_auto_horses", 1),
                        (eq, ":type", itp_type_horse),
                        (assign, ":grab", 1),
                    (else_try),
                        (eq, "$g_lco_auto_armors", 1),
                        (this_or_next|eq, ":type", itp_type_head_armor),
                        (this_or_next|eq, ":type", itp_type_body_armor),
                        (this_or_next|eq, ":type", itp_type_foot_armor),
                        (eq, ":type", itp_type_hand_armor),
                        (assign, ":grab", 1),
                    (else_try),
                        (eq, "$g_lco_auto_shields", 1),
                        (eq, ":type", itp_type_shield),
                        (assign, ":grab", 1),
                    (try_end),
                    (this_or_next|eq, ":troop_id", lco_storage), # When this operation is used on lco_storage, this means we are sorting player's inventory, so just take everything
                    (eq, ":grab", 1),
                    (troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":slot_id"),
                    (troop_set_inventory_slot, ":troop_id", ":hero_offset", ":item_id"),
                    (troop_set_inventory_slot_modifier, ":troop_id", ":hero_offset", ":modifier"),
                    (troop_set_inventory_slot, "trp_player", ":slot_id", -1), # Remove item
                    (val_add, ":hero_offset", 1),
                    (ge, ":hero_offset", ":hero_capacity"),
                    (assign, ":capacity", 0), # Break cycle because companion has no space in inventory for more items
                (try_end),
            (try_end),
        ]
    ),

    ("lco_hero_return_equipment",
        [
            (store_script_param, ":troop_id", 1),
            (troop_sort_inventory, ":troop_id"),
            (troop_get_inventory_capacity, ":hero_capacity", ":troop_id"),
            # Companion is returning items to player
            (troop_get_inventory_capacity, ":capacity", "trp_player"),
            (assign, ":hero_offset", num_equipment_kinds),
            (try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
                (try_begin),
                    (call_script, "script_cf_lco_slot_is_frozen", ":slot_id"), # If current slot is frozen, we skip it
                (else_try),
                    (troop_get_inventory_slot, ":item_id", "trp_player", ":slot_id"),
                    (lt, ":item_id", 0), # Slot is empty, can get item back
                    (troop_get_inventory_slot, ":item_id", ":troop_id", ":hero_offset"),
                    (troop_get_inventory_slot_modifier, ":modifier", ":troop_id", ":hero_offset"),
                    (troop_set_inventory_slot, "trp_player", ":slot_id", ":item_id"),
                    (troop_set_inventory_slot_modifier, "trp_player", ":slot_id", ":modifier"),
                    (troop_set_inventory_slot, ":troop_id", ":hero_offset", -1), # Remove item
                    (val_add, ":hero_offset", 1),
                    (ge, ":hero_offset", ":hero_capacity"),
                    (assign, ":capacity", 0), # Break cycle because we reached the end of companion's inventory
                (try_end),
            (try_end),
            # If player's inventory is full and companion still has items in inventory, he will drop them to garbage
            (troop_get_inventory_capacity, ":capacity", "$g_lco_garbage_troop"),
            (assign, ":hero_offset", num_equipment_kinds),
            (try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
                (troop_get_inventory_slot, ":item_id", "$g_lco_garbage_troop", ":slot_id"),
                (lt, ":item_id", 0), # Slot is empty, can get item back
                (troop_get_inventory_slot, ":item_id", ":troop_id", ":hero_offset"),
                (troop_get_inventory_slot_modifier, ":modifier", ":troop_id", ":hero_offset"),
                (troop_set_inventory_slot, "$g_lco_garbage_troop", ":slot_id", ":item_id"),
                (troop_set_inventory_slot_modifier, "$g_lco_garbage_troop", ":slot_id", ":modifier"),
                (troop_set_inventory_slot, ":troop_id", ":hero_offset", -1), # Remove item
                (val_add, ":hero_offset", 1),
                (ge, ":hero_offset", ":hero_capacity"),
                (assign, ":capacity", 0), # Break cycle because we reached the end of companion's inventory
            (try_end),
            (troop_sort_inventory, "$g_lco_garbage_troop"),
        ]
    ),

    ("lco_text_label",
        [
            (store_script_param, ":string", 1),
            (store_script_param, ":x", 2),
            (store_script_param, ":y", 3),
            (val_sub, ":x", 1), # Compensation for bad looks
            (set_fixed_point_multiplier, 1000),
            (init_position, pos60),
            (init_position, pos62),
            (position_set_x, pos60, ":x"),
            (position_set_y, pos60, ":y"),
            (position_set_x, pos62, 750),
            (position_set_y, pos62, 750),
            (create_text_overlay, ":label", ":string", tf_center_justify),
            (overlay_set_position, ":label", pos60),
            (overlay_set_size, ":label", pos62),
            (assign, reg0, ":label"),
        ]
    ),

    ("lco_text_caption",
        [
            (store_script_param, ":string", 1),
            (store_script_param, ":x", 2),
            (store_script_param, ":y", 3),
            (val_sub, ":x", 1), # Compensation for bad looks
            (val_sub, ":y", 105),
            (set_fixed_point_multiplier, 1000),
            (init_position, pos60),
            (init_position, pos62),
            (position_set_x, pos60, ":x"),
            (position_set_y, pos60, ":y"),
            (position_rotate_z, pos60, 45),
            (position_set_x, pos62, 750),
            (position_set_y, pos62, 750),
            (create_text_overlay, ":label", ":string"),
            (overlay_set_size, ":label", pos62),
            (overlay_set_position, ":label", pos60),
            (overlay_set_mesh_rotation, ":label", pos60),
            (create_text_overlay, ":label", ":string"),
            (overlay_set_size, ":label", pos62),
            (overlay_set_position, ":label", pos60),
            (overlay_set_mesh_rotation, ":label", pos60),
            (assign, reg0, ":label"),
        ]
    ),

    ("lco_initialize_presentation",
        [

            (presentation_set_duration, 999999),
            (try_begin),
                (eq, "$g_lco_initialized", 0),
                (assign, "$g_lco_activate_troop", 0), # By default, we do not make a particular troop active
                (assign, "$g_lco_active_hero", 0),    # We show the first hero by default
                (assign, "$g_lco_page", 0),           # We show the first page by default
                (assign, "$g_lco_operation", 0),      # No special action by default
                (assign, "$g_lco_target", 0),         # No action target by default
                (assign, "$g_lco_auto_horses", 1),    # Horses are auto-equipped by default
                (assign, "$g_lco_auto_armors", 1),    # Same
                (assign, "$g_lco_auto_shields", 1),   # Same
                (assign, "$g_lco_include_companions", 1),
                (assign, "$g_lco_include_lords", 0),
                (assign, "$g_lco_include_regulars", 0),
                # BugFix V1.1. Do not overwrite $g_lco_garbage_troop on first run if it's already initialized.
                (try_begin),
                    (lt, "$g_lco_garbage_troop", 3),
                    (assign, "$g_lco_garbage_troop", lco_garbage), # This troop will be used for discarding items or looting, and it's inventory will be purged on exit
                (try_end),
                (assign, "$g_lco_initialized", 1),
                # BugFix V1.2. Hardcoded xp-to-level conversion table has been removed
            (try_end),

            # GLOBAL VARIABLES INITIALIZATION

            (assign, "$g_lco_heroes", 0),             # Total number of heroes in the party, excluding player
            (assign, "$g_lco_inv_slots", 0),          # Total number of slots in the player's inventory
            (assign, "$g_lco_dragging", 0),           # Currently not dragging anything
            (assign, "$g_lco_dragging_from", 0),      # Troop ID of dragged item current owner
            (assign, "$g_lco_dragging_from_slot", 0), # Slot ID of dragged item current owner
            (assign, "$g_lco_drag_item", -1),         # Item type currently being dragged
            (assign, "$g_lco_drag_modifier", 0),      # Modifier of item currently being dragged
            (assign, "$g_lco_drag_quantity", 0),      # Quantity of item currently being dragged (for foods)
            (assign, "$g_lco_drag_quantity_max", 0),  # Max quantity of item currently being dragged (for foods)
            (assign, "$g_lco_popup_active", 0),       # Whether or not there's an active popup with item details
            (assign, "$g_lco_popup_overlay", 0),      # Overlay ID that caused the popup to appear (to prevent popup from disappearing when mouseout happens on another overlay)
            (assign, "$g_lco_popup_item", 0),         # ID of the item to show in popup
            (assign, "$g_lco_popup_modifier", 0),     # ID of the modifier to show in popup
            (assign, "$g_lco_panel_found", 0),        # Variable is used to prevent a single click from affecting two panels simultaneously in equipment_overview

            (val_clamp, "$g_lco_auto_horses", 0, 2),
            (val_clamp, "$g_lco_auto_armors", 0, 2),
            (val_clamp, "$g_lco_auto_shields", 0, 2),
            (val_clamp, "$g_lco_include_companions", 0, 2),
            (val_clamp, "$g_lco_include_lords", 0, 2),
            (val_clamp, "$g_lco_include_regulars", 0, 2),
            (try_begin),
                (is_presentation_active, "prsnt_companions_overview"),
                (val_clamp, "$g_lco_page", 0, 2),   # Current page to display
            (try_end),

            # TROOP HANDLING

            (call_script, "script_lco_prepare_heroes"),
            (try_begin),
                # We are requested to make a particular troop active
                (gt, "$g_lco_activate_troop", 0),
                (try_for_range, reg0, 0, "$g_lco_heroes"),
                    (store_add, ":offset", reg0, "$g_lco_heroes"),
                    (troop_slot_eq, lco_storage, ":offset", "$g_lco_activate_troop"),
                    (assign, "$g_lco_active_hero", ":offset"),
                (try_end),
                (assign, "$g_lco_activate_troop", 0),
            (try_end),
            (val_clamp, "$g_lco_active_hero", 0, "$g_lco_heroes"), # Index of currently selected hero
            (troop_get_inventory_capacity, "$g_lco_inv_slots", "trp_player"),
            (val_sub, "$g_lco_inv_slots", num_equipment_kinds),
            (troop_get_inventory_capacity, "$g_lco_garb_slots", "$g_lco_garbage_troop"),
            (val_sub, "$g_lco_garb_slots", num_equipment_kinds),
            (troop_set_auto_equip, lco_storage, 0),
            (call_script, "script_lco_clear_all_items", lco_storage),
            (troop_set_auto_equip, "$g_lco_garbage_troop", 0),
            # We do not clear garbage troop because it may be used for looting

            # PRESENTATION SHARED BUTTONS AND INCLUSION FORM

            (call_script, "script_lco_create_button", "str_lco_i_return", 855, 25, 190, 42),
            (assign, "$g_lco_return", reg0),
            (call_script, "script_lco_create_checkbox", "str_lco_i_list_companions",  25, 75, "$g_lco_include_companions"),
            (assign, "$g_lco_inc_0", reg0),
            (call_script, "script_lco_create_checkbox", "str_lco_i_list_lords",  25, 50, "$g_lco_include_lords"),
            (assign, "$g_lco_inc_1", reg0),
            (call_script, "script_lco_create_checkbox", "str_lco_i_list_regulars",  25, 25, "$g_lco_include_regulars"),
            (assign, "$g_lco_inc_2", reg0),

            (call_script, "script_lco_create_image_button", "mesh_lco_square_button_up", "mesh_lco_square_button_down", 25, 685, 333, 400),
            (assign, "$g_lco_switch_page_0", reg0),
            (call_script, "script_lco_create_image_button", "mesh_lco_square_button_up", "mesh_lco_square_button_down", 55, 685, 333, 400),
            (assign, "$g_lco_switch_page_1", reg0),
            (call_script, "script_lco_create_image_button", "mesh_lco_square_button_up", "mesh_lco_square_button_down", 85, 685, 333, 400),
            (assign, "$g_lco_switch_page_2", reg0),
            (store_mul, ":x", "$g_lco_page", 30),
            (val_add, ":x", 25),
            (call_script, "script_lco_create_mesh", "mesh_lco_square_button_down", ":x", 685, 333, 400),
            (assign, "$g_lco_selected_page", reg0),
            (assign, reg40, 1),
            (call_script, "script_lco_create_label", "str_lco_reg40", 35, 702, 750, tf_center_justify | tf_vertical_align_center),
            (assign, reg40, 2),
            (call_script, "script_lco_create_label", "str_lco_reg40", 65, 702, 750, tf_center_justify | tf_vertical_align_center),
            (str_store_string, s40, "str_lco_i_ie_icon"),
            (call_script, "script_lco_create_label", "str_lco_s40",   95, 702, 750, tf_center_justify | tf_vertical_align_center),

            # DISPLAYING VERSION INFORMATION

            (call_script, "script_lco_create_label", "str_lco_version", 975, 5, 750, tf_right_align),

        ]
    ),

    ("lco_prepare_heroes",
        [
            (assign, "$g_lco_heroes", 0), # Total number of heroes in the party, excluding player
            # CALCULATING NUMBER OF HEROES
            (try_begin),
                (eq, "$g_lco_include_companions", 1),
                (party_get_num_companion_stacks, ":total_stacks", "p_main_party"),
                (try_for_range, reg0, 0, ":total_stacks"),
                    (party_stack_get_troop_id, ":troop_id", "p_main_party", reg0),
                    (is_between, ":troop_id", companions_begin, companions_end),
                    (troop_set_slot, lco_storage, "$g_lco_heroes", ":troop_id"),
                    (val_add, "$g_lco_heroes", 1),
                (try_end),
            (try_end),
            (try_begin),
                (eq, "$g_lco_include_lords", 1),
                (gt, "$players_kingdom", 0),
                (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
                (try_for_range, ":troop_id", active_npcs_begin, active_npcs_end),
                    (troop_slot_eq, ":troop_id", slot_troop_occupation, slto_kingdom_hero),
                    (troop_get_slot, ":party_no", ":troop_id", slot_troop_leaded_party),
                    (gt, ":party_no", 0),
                    (party_is_active, ":party_no"),
                    (troop_set_slot, lco_storage, "$g_lco_heroes", ":troop_id"),
                    (val_add, "$g_lco_heroes", 1),
                (try_end),
            (try_end),
            (try_begin),
                (eq, "$g_lco_include_regulars", 1),
                (party_get_num_companion_stacks, ":total_stacks", "p_main_party"),
                (try_for_range, reg0, 0, ":total_stacks"),
                    (party_stack_get_troop_id, ":troop_id", "p_main_party", reg0),
                    (neg|troop_is_hero, ":troop_id"),
                    (troop_set_slot, lco_storage, "$g_lco_heroes", ":troop_id"),
                    (val_add, "$g_lco_heroes", 1),
                (try_end),
            (try_end),
        ]
    ),

    ("cf_lco_controllable",
        [
            (store_script_param_1, ":troop_id"),
            (troop_is_hero, ":troop_id"), # We never have control over regulars
            (assign, ":control", 0),
            (try_begin),
                (this_or_next|eq, ":troop_id", "trp_player"),
                (eq, ":troop_id", "$g_lco_garbage_troop"),
                (assign, ":control", 1),
            (else_try),
                (gt, "$g_lco_heroes", 0),
                (is_between, ":troop_id", companions_begin, companions_end), # We do not provide control over lords
                (troop_slot_eq, ":troop_id", slot_troop_occupation, slto_player_companion),
                (assign, ":control", 1),
            (try_end),
            (eq, ":control", 1),
        ]
    ),

    ("lco_troop_name_to_s40",
        [
            (store_script_param_1, ":troop_id"),
            (try_begin),
                (troop_is_hero, ":troop_id"),
                (str_store_troop_name, s40, ":troop_id"),
            (else_try),
                (str_store_troop_name_plural, s40, ":troop_id"),
            (try_end),
        ]
    ),

    ("lco_discard_item",
        [
            (store_script_param, ":item_id", 1),
            (store_script_param, ":modifier", 2),
            (store_script_param, ":quantity", 3),
            (troop_sort_inventory, "$g_lco_garbage_troop"),
            (troop_get_inventory_capacity, ":capacity", "$g_lco_garbage_troop"),
            (store_sub, reg0, ":capacity", num_equipment_kinds),
            (assign, ":discarded", 0),
            (try_for_range, ":index", num_equipment_kinds, ":capacity"),
                (troop_get_inventory_slot, ":cur_item_id", "$g_lco_garbage_troop", ":index"),
                (lt, ":cur_item_id", 0),
                (troop_set_inventory_slot, "$g_lco_garbage_troop", ":index", ":item_id"),
                (troop_set_inventory_slot_modifier, "$g_lco_garbage_troop", ":index", ":modifier"),
                (try_begin),
                    (ge, ":quantity", 1),
                    (troop_inventory_slot_set_item_amount, "$g_lco_garbage_troop", ":index", ":quantity"),
                (try_end),
                (store_add, reg0, ":index", 1-num_equipment_kinds), # Total number of items in garbage
                (assign, ":capacity", 0), # Break cycle
                (assign, ":discarded", 1),
            (try_end),
            (try_begin),
                # If garbage troop inventory is full, we replace the last (cheapest) item
                (eq, ":discarded", 0),
                (assign, ":index", ":capacity"),
                (val_sub, ":index", 1),
                (troop_set_inventory_slot, "$g_lco_garbage_troop", ":index", ":item_id"),
                (troop_set_inventory_slot_modifier, "$g_lco_garbage_troop", ":index", ":modifier"),
                (try_begin),
                    (ge, ":quantity", 1),
                    (troop_inventory_slot_set_item_amount, "$g_lco_garbage_troop", ":index", ":quantity"),
                (try_end),
                (store_sub, reg0, ":capacity", num_equipment_kinds),
            (try_end),
            (troop_sort_inventory, "$g_lco_garbage_troop"),
        ]
    ),

    ("lco_retrieve_discarded",
        [
            (troop_sort_inventory, "$g_lco_garbage_troop"),
            (assign, ":hero_offset", num_equipment_kinds),
            (troop_get_inventory_capacity, ":capacity", "trp_player"),
            (troop_get_inventory_capacity, ":hero_capacity", "$g_lco_garbage_troop"),
            (try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
                (try_begin),
                    (call_script, "script_cf_lco_slot_is_frozen", ":slot_id"),
                (else_try),
                    (troop_get_inventory_slot, ":item_id", "trp_player", ":slot_id"),
                    (lt, ":item_id", 0), # Slot is empty, can get item back
                    (troop_get_inventory_slot, ":item_id", "$g_lco_garbage_troop", ":hero_offset"),
                    (troop_get_inventory_slot_modifier, ":modifier", "$g_lco_garbage_troop", ":hero_offset"),
                    (troop_inventory_slot_get_item_amount, ":quantity", "$g_lco_garbage_troop", ":hero_offset"),
                    (troop_set_inventory_slot, "trp_player", ":slot_id", ":item_id"),
                    (troop_set_inventory_slot_modifier, "trp_player", ":slot_id", ":modifier"),
                    (try_begin),
                        (ge, ":quantity", 1),
                        (troop_inventory_slot_set_item_amount, "trp_player", ":slot_id", ":quantity"),
                    (try_end),
                    (troop_set_inventory_slot, "$g_lco_garbage_troop", ":hero_offset", -1), # Remove item
                    (val_add, ":hero_offset", 1),
                    (ge, ":hero_offset", ":hero_capacity"),
                    (assign, ":capacity", 0),
                (try_end),
            (try_end),
            (call_script, "script_lco_count_discarded"),
        ]
    ),

    # Added in V1.20.
    ("lco_sort_player_inventory",
        [
            (call_script, "script_lco_clear_all_items", lco_storage),
            (call_script, "script_lco_hero_grab_equipment", lco_storage),
            (troop_sort_inventory, lco_storage),
            (call_script, "script_lco_hero_return_equipment", lco_storage),
        ]
    ),

    # Added in V1.20.
    # script_get_item_price
    # This script will return the price of an item in reg0
    # INPUT: <arg1> = item_type_id, <arg2> = item_modifier_id
    # OUTPUT: reg0 = nominal item price (price modifiers are ignored)
    ("lco_get_item_price",
        [
            (store_script_param, ":item_id", 1),
            (store_script_param, ":item_modifier", 2),
            (store_script_param, ":item_amount", 3),
            (troop_clear_inventory, "trp_temp_troop"),
            (troop_set_auto_equip, "trp_temp_troop", 0),
            (troop_set_inventory_slot, "trp_temp_troop", num_equipment_kinds, ":item_id"),
            (troop_set_inventory_slot_modifier, "trp_temp_troop", num_equipment_kinds, ":item_modifier"),
            (try_begin),
                (ge, ":item_amount", 1),
                (troop_inventory_slot_set_item_amount, "trp_temp_troop", num_equipment_kinds, ":item_amount"),
            (try_end),
            (troop_remove_items, "trp_temp_troop", ":item_id", 1),
        ]
    ), 

    # Added in V1.20.
    ("lco_retrieve_discarded_best",
        [
            (call_script, "script_lco_retrieve_discarded"),
            (try_begin),
                (gt, reg0, 0), # If there are still items in loot
                # Sort player inventory
                (call_script, "script_lco_sort_player_inventory"),
                # Process
                (assign, ":hero_offset", num_equipment_kinds), # Offset of item in loot that is currently processed
                (troop_get_inventory_capacity, ":capacity", "trp_player"),
                (troop_get_inventory_capacity, ":hero_capacity", "$g_lco_garbage_troop"),
                (try_for_range_backwards, ":slot_id", num_equipment_kinds, ":capacity"),
                    (try_begin),
                        (call_script, "script_cf_lco_slot_is_frozen", ":slot_id"), # Skipping over frozen slots
                    (else_try),
                        # Retrieving item from garbage troop's inventory
                        (troop_get_inventory_slot, ":loot_item_id", "$g_lco_garbage_troop", ":hero_offset"),
                        (ge, ":loot_item_id", 0), # Garbage troop has an item in currently processed slot
                        (troop_get_inventory_slot_modifier, ":loot_modifier", "$g_lco_garbage_troop", ":hero_offset"),
                        (troop_inventory_slot_get_item_amount, ":loot_quantity", "$g_lco_garbage_troop", ":hero_offset"),
                        (call_script, "script_lco_get_item_price", ":loot_item_id", ":loot_modifier", ":loot_quantity"),
                        (assign, ":loot_price", reg0),
                        # Retrieving item from player's inventory
                        (troop_get_inventory_slot, ":item_id", "trp_player", ":slot_id"),
                        (troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":slot_id"),
                        (troop_inventory_slot_get_item_amount, ":quantity", "trp_player", ":slot_id"),
                        (call_script, "script_lco_get_item_price", ":item_id", ":modifier", ":quantity"),
                        (assign, ":price", reg0),
                        # If price for loot item is greater than price for player item, we swap them.
                        # If it's equal or less, since both arrays are sorted, we quit the loop (subsequent loot items will be of same or lower price).
                        (try_begin),
                            (gt, ":loot_price", ":price"),
                            # Overwriting item in player's inventory
                            (troop_set_inventory_slot, "trp_player", ":slot_id", ":loot_item_id"),
                            (troop_set_inventory_slot_modifier, "trp_player", ":slot_id", ":loot_modifier"),
                            (try_begin),
                                (ge, ":loot_quantity", 1),
                                (troop_inventory_slot_set_item_amount, "trp_player", ":slot_id", ":loot_quantity"),
                            (try_end),
                            # Overwriting item in loot inventory
                            (troop_set_inventory_slot, "$g_lco_garbage_troop", ":hero_offset", ":item_id"),
                            (troop_set_inventory_slot_modifier, "$g_lco_garbage_troop", ":hero_offset", ":modifier"),
                            (try_begin),
                                (ge, ":quantity", 1),
                                (troop_inventory_slot_set_item_amount, "$g_lco_garbage_troop", ":hero_offset", ":quantity"),
                            (try_end),
                            (val_add, ":hero_offset", 1),
                        (else_try),
                            (assign, ":capacity", 0),
                        (try_end),
                        # Just in case, we are also checking for exceeding the loot troop inventory size
                        (ge, ":hero_offset", ":hero_capacity"),
                        (assign, ":capacity", 0),
                    (try_end),
                (try_end),
            (try_end),
            (call_script, "script_lco_sort_player_inventory"),
            (call_script, "script_lco_count_discarded"),
        ]
    ),

    ("lco_count_discarded",
        [
            (troop_get_inventory_capacity, ":hero_capacity", "$g_lco_garbage_troop"),
            (troop_sort_inventory, "$g_lco_garbage_troop"),
            (assign, reg0, 0),
            (try_for_range, ":slot_id", num_equipment_kinds, ":hero_capacity"),
                (troop_get_inventory_slot, ":item_id", "$g_lco_garbage_troop", ":slot_id"),
                (ge, ":item_id", 0), # Slot is not empty
                (val_add, reg0, 1),
            (try_end),
        ]
    ),

    # BugFix V1.20. Replacing hardcoded xp-to-level table with a call to standard game operation
    ("lco_xp_to_next_level",
        [
            (store_script_param_1, ":troop_id"),
            (store_character_level, ":level", ":troop_id"),
            (val_add, ":level", 1),
            (troop_get_xp, ":xp", ":troop_id"),
            (get_level_boundary, ":xp_needed", ":level"),
            (store_sub, reg40, ":xp_needed", ":xp"),
        ]
    ),

    ("lco_create_mesh",
        [
            (store_script_param, ":mesh", 1),
            (store_script_param, ":x", 2),
            (store_script_param, ":y", 3),
            (store_script_param, ":x_ratio", 4),
            (store_script_param, ":y_ratio", 5),
            (set_fixed_point_multiplier, 1000),
            (create_mesh_overlay, reg0, ":mesh"),
            (position_set_x, pos60, ":x"),
            (position_set_y, pos60, ":y"),
            (overlay_set_position, reg0, pos60),
            (position_set_x, pos61, ":x_ratio"),
            (position_set_y, pos61, ":y_ratio"),
            (overlay_set_size, reg0, pos61),
        ]
    ),

    ("lco_create_button",
        [
            (store_script_param, ":caption", 1),
            (store_script_param, ":x", 2),
            (store_script_param, ":y", 3),
            (store_script_param, ":x_size", 4),
            (store_script_param, ":y_size", 5),
            (set_fixed_point_multiplier, 1000),
            (create_game_button_overlay, reg0, ":caption"),
            (position_set_x, pos60, ":x"),
            (position_set_y, pos60, ":y"),
            (overlay_set_position, reg0, pos60),
            (position_set_x, pos61, ":x_size"),
            (position_set_y, pos61, ":y_size"),
            (overlay_set_size, reg0, pos61),
        ]
    ),

    ("lco_create_image_button",
        [
            (store_script_param, ":mesh", 1),
            (store_script_param, ":mesh_down", 2),
            (store_script_param, ":x", 3),
            (store_script_param, ":y", 4),
            (store_script_param, ":x_scale", 5),
            (store_script_param, ":y_scale", 6),
            (set_fixed_point_multiplier, 1000),
            (create_image_button_overlay, reg0, ":mesh", ":mesh_down"),
            (position_set_x, pos60, ":x"),
            (position_set_y, pos60, ":y"),
            (overlay_set_position, reg0, pos60),
            (position_set_x, pos61, ":x_scale"),
            (position_set_y, pos61, ":y_scale"),
            (overlay_set_size, reg0, pos61),
        ]
    ),

    ("lco_create_label",
        [
            (store_script_param, ":caption", 1),
            (store_script_param, ":x", 2),
            (store_script_param, ":y", 3),
            (store_script_param, ":scale", 4),
            (store_script_param, ":alignment", 5),
            (set_fixed_point_multiplier, 1000),
            (create_text_overlay, reg0, ":caption", ":alignment"),
            (position_set_x, pos60, ":x"),
            (position_set_y, pos60, ":y"),
            (overlay_set_position, reg0, pos60),
            (position_set_x, pos62, ":scale"),
            (position_set_y, pos62, ":scale"),
            (overlay_set_size, reg0, pos62),
        ]
    ),

    ("lco_create_checkbox",
        [
            (store_script_param, ":caption", 1),
            (store_script_param, ":x", 2),
            (store_script_param, ":y", 3),
            (store_script_param, ":value", 4),
            (set_fixed_point_multiplier, 1000),
            (create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"),
            (overlay_set_val, reg0, ":value"),
            (position_set_x, pos60, ":x"),
            (position_set_y, pos60, ":y"),
            (overlay_set_position, reg0, pos60),
            (create_text_overlay, reg1, ":caption"),
            (val_add, ":x", 25),
            (position_set_x, pos60, ":x"),
            (overlay_set_position, reg1, pos60),
            (position_set_x, pos62, 750),
            (position_set_y, pos62, 750),
            (overlay_set_size, reg1, pos62),
        ]
    ),

    ("lco_create_container",
        [
            (store_script_param, ":x", 1),
            (store_script_param, ":y", 2),
            (store_script_param, ":width", 3),
            (store_script_param, ":height", 4),
            (store_script_param, ":auto_start", 5),
            (set_fixed_point_multiplier, 1000),
            (str_clear, s40),
            (create_text_overlay, reg0, s40, tf_scrollable),
            (position_set_x, pos60, ":x"),
            (position_set_y, pos60, ":y"),
            (overlay_set_position, reg0, pos60),
            (position_set_x, pos61, ":width"),
            (position_set_y, pos61, ":height"),
            (overlay_set_area_size, reg0, pos61),
            (try_begin),
                (neq, ":auto_start", 0),
                (set_container_overlay, reg0),
            (try_end),
        ]
    ),

    ("lco_freeze_slot_toggle",
        [
            (store_script_param_1, ":slot_id"),
            #(val_add, ":slot_id", lco_frozen_slots_start), # Removed as of V1.20
            (troop_get_slot, reg0, lco_garbage, ":slot_id"),
            (store_sub, reg0, 1, reg0),
            (troop_set_slot, lco_garbage, ":slot_id", reg0),
        ]
    ),

    ("cf_lco_slot_is_frozen",
        [
            (store_script_param_1, ":slot_id"),
            #(val_add, ":slot_id", lco_frozen_slots_start), # Removed as of V1.20
            (troop_slot_eq, lco_garbage, ":slot_id", 1),
        ]
    ),

    ("lco_suppress_book_slots",
        [
            (store_script_param_1, "$g_lco_suppress_books"),
        ]
    ),

####################################################################################################################################
# LAV MODIFICATIONS END (COMPANIONS OVERSEER MOD)
####################################################################################################################################
]


from util_scripts import *

def modmerge_companions_scripts(orig_scripts):
	add_scripts(orig_scripts, scripts, True)
	
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "scripts"
        orig_scripts = var_set[var_name_1]
    
        
		# START do your own stuff to do merging
		
        modmerge_companions_scripts(orig_scripts)

		# END do your own stuff
        
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)