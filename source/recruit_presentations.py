from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from header_items import *
from module_constants import *

####################################################################################################################
#	Each presentation record contains the following fields:
#	1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#	2) Presentation flags. See header_presentations.py for a list of available flags
#	3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#	4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

presentations = [
	
	("recruit_volunteers", 0, mesh_load_window,
	[
		(ti_on_presentation_load,
		[
			(party_get_slot, ":volunteer_troop", "$current_town", slot_center_volunteer_troop_type),
			(party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
			(party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
			(store_troop_gold, ":gold", "trp_player"),
			(store_div, ":gold_capacity", ":gold", 10),#10 denars per man
			(assign, ":party_capacity", ":free_capacity"),
			(val_min, ":party_capacity", ":gold_capacity"),
			
			## TITLE
			(str_store_string, s0, "@Hire Volunteers"),
			(call_script, "script_gpu_create_text_overlay", "str_s0", 500, 650, 2000, 900, 50, tf_center_justify),
			
			## EXPLANATION TEXT
			(assign, reg0, ":volunteer_amount"),
			(str_store_string, s0, "@Volunteers available: {reg0}"),
			(call_script, "script_gpu_create_text_overlay", "str_s0", 350, 450, 1000, 200, 50, tf_left_align),
			
			## NUMBER BOX
			(assign, ":max", ":volunteer_amount"),
			(val_min, ":max", ":party_capacity"),
			(val_add, ":max", 1),
			(store_sub, "$recruit_volunteer_amount", ":max", 1),
			
			(call_script, "script_gpu_create_number_box", 350, 400, 0, ":max"),
			(overlay_set_val, reg1, "$recruit_volunteer_amount"),
			(assign, "$recruit_volunteer_amount_box", reg1),
			
			## TROOP IMAGE
			(call_script, "script_gpu_create_troop_image", ":volunteer_troop", 550, 200, 1000),
			
			## RECRUIT BUTTON
			(str_store_string, s0, "@Recruit"),
			(call_script, "script_gpu_create_game_button_overlay", "str_s0", 500, 400),
			(assign, "$recruit_recruit_button", reg1),
			(position_set_x, pos1, 100),
			(position_set_y, pos1, 30),
			(overlay_set_size, "$recruit_recruit_button", pos1),
			
			## CANCEL BUTTON
			(str_store_string, s0, "@Cancel"),
			(call_script, "script_gpu_create_game_button_overlay", "str_s0", 425, 350),
			(assign, "$recruit_cancel_button", reg1),
			(position_set_x, pos1, 100),
			(position_set_y, pos1, 30),
			(overlay_set_size, "$recruit_cancel_button", pos1),
			
			(presentation_set_duration, 999999),
		]),
		
		(ti_on_presentation_run,
		[
			# Emergency escape option if buttons are bugging out - just hit ESC to close presentation at any time
			(try_begin),
				(key_clicked, key_escape),
				
				(presentation_set_duration, 0),
				(change_screen_return),
			(try_end),
		]),
		
		(ti_on_presentation_event_state_change,
		[
			(store_trigger_param_1, ":object"),
			(store_trigger_param_2, ":value"),
			
			(try_begin),
				(eq, ":object", "$recruit_recruit_button"),
				
				(party_get_slot, ":volunteer_troop", "$current_town", slot_center_volunteer_troop_type),
				(party_add_members, "p_main_party", ":volunteer_troop", "$recruit_volunteer_amount"),
				(try_begin),
					(party_slot_eq, "$current_town", slot_center_volunteer_troop_amount, "$recruit_volunteer_amount"),
					
					(party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
				(else_try),
					(party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
					(val_sub, ":volunteer_amount", "$recruit_volunteer_amount"),
					(party_set_slot, "$current_town", slot_center_volunteer_troop_amount, ":volunteer_amount"),
				(try_end),
				(store_mul, ":cost", "$recruit_volunteer_amount", 10),#10 denars per man
				(troop_remove_gold, "trp_player", ":cost"),
				
				(presentation_set_duration, 0),
				(change_screen_return),
			(else_try),
				(eq, ":object", "$recruit_volunteer_amount_box"),
				
				(assign, "$recruit_volunteer_amount", ":value"),
				(try_begin),
					(eq, "$recruit_volunteer_amount", 0),
					
					(overlay_set_display, "$recruit_recruit_button", 0),
				(else_try),
					(overlay_set_display, "$recruit_recruit_button", 1),
				(try_end),
			(else_try),
				## EXIT BUTTON PRESSED
				(eq, ":object", "$recruit_cancel_button"),
				
				(presentation_set_duration, 0),
				(change_screen_return),
			(try_end),
		]),
	])
	
]