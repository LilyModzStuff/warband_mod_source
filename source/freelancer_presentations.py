# Freelancer (1.3) by Taragoth
# Released 11 July 2011
# Edits by Caba'drin 14 Dec 2011
# Mod-Merger'd by Windyplains, Monnikje and Caba'drin

from header_common import *
from header_presentations import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *



presentations = [
# __Freelancer Report: Commander_:Start_________________________________________________

  ("taragoth_lords_report", 0, mesh_load_window, [

	(ti_on_presentation_load,
	[
		(presentation_set_duration, 999999),
		(set_fixed_point_multiplier, 1000),

		#title
		(create_text_overlay, reg0, "@CURRENT COMMANDER'S REPORT!", tf_left_align),
		(position_set_x, pos1, 50),
		(position_set_y, pos1, 650),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 1500),
		(position_set_y, pos1, 1500),
		(overlay_set_size, reg0, pos1),
		
		#Player Name
		#(create_text_overlay, reg0, "@'{playername}'", tf_center_justify),
		#(position_set_x, pos1, 500),
		#(position_set_y, pos1, 615),
		#(overlay_set_position, reg0, pos1),

		(assign, ":cur_y_adder", 40),  #the amount of space between lines
		(assign, ":cur_y", 580),
		(position_set_x, pos1, 50),		
		
		#Commander_name
		(str_store_troop_name, s19, "$enlisted_lord"),
		(create_text_overlay, reg0, "@Your Commander: {s19}", tf_left_align),	
		(position_set_y, pos1, ":cur_y"),
		(overlay_set_position, reg0, pos1),
		(val_sub, ":cur_y", ":cur_y_adder"),

		#Player_Relation
		(call_script, "script_troop_get_player_relation", "$enlisted_lord"),
		#(assign, ":commander_relation", reg0),
		(create_text_overlay, reg0, "@Commander Relation: {reg0}", tf_left_align),
		(position_set_y, pos1, ":cur_y"),
		(overlay_set_position, reg0, pos1),
		(val_sub, ":cur_y", ":cur_y_adder"),

		#Faction_name
		(store_faction_of_troop, reg1, "$enlisted_lord"),
		(str_store_faction_name, s20, reg1),
		(create_text_overlay, reg0, "@Enlisted Faction: {s20}", tf_left_align),
		(position_set_y, pos1, ":cur_y"),
		(overlay_set_position, reg0, pos1),
		(val_sub, ":cur_y", ":cur_y_adder"),

		#Rank_name
		(str_store_troop_name, s21, "$player_cur_troop"),
		(create_text_overlay, reg0, "@Current Rank: {s21}", tf_left_align),
		(position_set_y, pos1, ":cur_y"),
		(overlay_set_position, reg0, pos1),
		(val_sub, ":cur_y", ":cur_y_adder"),
		
		#xp-to-next promotion
		(troop_get_slot, ":service_xp_start", "trp_player", slot_troop_freelancer_start_xp),
        (troop_get_xp, ":service_xp_cur", "trp_player"),
        (val_sub, ":service_xp_cur", ":service_xp_start"),
		(troop_get_upgrade_troop, ":upgrade_troop", "$player_cur_troop", 0),
		(str_store_string, s1, "@N/A"),
		(try_begin),
			(gt, ":upgrade_troop", 1), #make sure troop is valid and not player troop
			(call_script, "script_game_get_upgrade_xp", "$player_cur_troop"),
			(store_sub, reg0, reg0, ":service_xp_cur"), #required XP from script
			(gt, reg0, 0),
			(str_store_string, s1, "str_reg0"),
		(try_end),
		(create_text_overlay, reg0, "@Experience to next promotion: {s1}", tf_left_align),
		(position_set_y, pos1, ":cur_y"),
		(overlay_set_position, reg0, pos1),
		(val_sub, ":cur_y", ":cur_y_adder"),

		#enlisted_time
		(store_current_day, ":cur_day"),
		(troop_get_slot, ":service_day_start", "trp_player", slot_troop_freelancer_start_date),
		(store_sub, ":service_length", ":cur_day", ":service_day_start"),
		(assign, reg20, ":service_length"),
		(create_text_overlay, reg0, "@Days in service: {reg20}", tf_left_align),
		(position_set_y, pos1, ":cur_y"),
		(overlay_set_position, reg0, pos1),
		(val_sub, ":cur_y", ":cur_y_adder"),

		#current_wage
		(store_character_level, ":level", "$player_cur_troop"),
		#pays player 10 times the troop level
		(store_mul, ":weekly_pay", 10, ":level"),
		(assign, reg23, ":weekly_pay"),
		(create_text_overlay, reg0, "@Current Wage: {reg23} denars.", tf_left_align),
		(position_set_y, pos1, ":cur_y"),
		(overlay_set_position, reg0, pos1),
		(val_sub, ":cur_y", ":cur_y_adder"),
		
		#next_pay
		(str_store_date, s25, "$g_next_pay_time"),
		(create_text_overlay, reg0, "@Next Pay/Promotion day: {s25}", tf_left_align),
		(position_set_y, pos1, ":cur_y"),
		(overlay_set_position, reg0, pos1),
		(val_sub, ":cur_y", ":cur_y_adder"),

		#Commanders_troops size(right side)
		(store_party_size_wo_prisoners,":army_size","$enlisted_party"), 
		(assign, reg26, ":army_size"),
		(create_text_overlay, reg0, "@Army size: {reg26}", tf_left_align),
		(position_set_x, pos1, 800),
		(position_set_y, pos1, 60),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg0, pos1),

		#commanders_army_title
		(create_text_overlay, reg0, "@Commander's Army", tf_left_align),
		(position_set_x, pos1, 500),
		(position_set_y, pos1, 430),
		(overlay_set_position, reg0, pos1),

        #camp  pic		
		(create_mesh_overlay, reg0, "mesh_pic_camp"),
		(position_set_x, pos1, 450),
		(position_set_y, pos1, 380),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 500),
		(position_set_y, pos1, 500),
		(overlay_set_size, reg0, pos1),	
		 #Faction arms(try_end),
		 
		(store_faction_of_troop, ":cmdr_faction", "$enlisted_lord"),
		(try_begin),
			(eq, ":cmdr_faction","fac_kingdom_1"),
			(create_mesh_overlay, reg0, "mesh_pic_arms_swadian"),
		(else_try),
			(eq, ":cmdr_faction","fac_kingdom_2"),
			(create_mesh_overlay, reg0, "mesh_pic_arms_vaegir"),
		(else_try),
			(eq, ":cmdr_faction","fac_kingdom_3"),
			(create_mesh_overlay, reg0, "mesh_pic_arms_khergit"),
		(else_try),
			(eq, ":cmdr_faction","fac_kingdom_4"),
			(create_mesh_overlay, reg0, "mesh_pic_arms_nord"),
		(else_try),
			(eq, ":cmdr_faction","fac_kingdom_5"),
			(create_mesh_overlay, reg0, "mesh_pic_arms_rhodok"),
		(else_try),
			(eq, ":cmdr_faction","fac_kingdom_6"),
			(create_mesh_overlay, reg0, "mesh_pic_sarranid_arms"),
		(try_end),

		(position_set_x, pos1, 180),
		(position_set_y, pos1, 80),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 600),
		(position_set_y, pos1, 600),
		(overlay_set_size, reg0, pos1),

        (str_clear, s0),
        (create_text_overlay, "$g_presentation_obj_bugdet_report_container", s0, tf_scrollable_style_2),
        (position_set_x, pos1, 560),
        (position_set_y, pos1, 100),
        (overlay_set_position, "$g_presentation_obj_bugdet_report_container", pos1),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 300), 
        (overlay_set_area_size, "$g_presentation_obj_bugdet_report_container", pos1),
        (set_container_overlay, "$g_presentation_obj_bugdet_report_container"), #all of this above here puts the list of troops in a scrollable box

        (assign, ":cur_y_adder", 40),  #the amount of space between lines
        (party_get_num_companion_stacks, ":num_of_stacks", "$enlisted_party"),
        (store_mul, ":cur_y", ":num_of_stacks", ":cur_y_adder"),
  
		(try_for_range, ":i", 1, ":num_of_stacks"), #1, to skip the commander
			(party_stack_get_troop_id, ":troop_id", "$enlisted_party", ":i"),
			(party_stack_get_size, ":stack_size", "$enlisted_party", ":i"),
			(party_stack_get_num_wounded, ":stack_wounded", "$enlisted_party", ":i"),
			(val_sub, ":stack_size", ":stack_wounded"),
						
			(str_store_troop_name, s1, ":troop_id"),
			(create_text_overlay, reg0, s1),
			(position_set_x, pos1, 25),
			(position_set_y, pos1, ":cur_y"),
			(overlay_set_position, reg0, pos1),
			(position_set_x, pos1, 900),
			(position_set_y, pos1, 900),
			(overlay_set_size, reg0, pos1),
			
			
			(assign, reg0, ":stack_size"),
			(create_text_overlay, reg0, "str_reg0"),
			(position_set_x, pos1, 325),
			(position_set_y, pos1, ":cur_y"),
			(overlay_set_position, reg0, pos1),
			(position_set_x, pos1, 900),
            (position_set_y, pos1, 900),
            (overlay_set_size, reg0, pos1),

			
			(val_sub, ":cur_y", ":cur_y_adder"),
		(try_end), #End Stack/Troop Loop

		(set_container_overlay, -1), #end the box so you can keep putting other things elsewhere
    
		#done button
		(create_game_button_overlay, "$g_presentation_obj_custom_battle_designer_19", "@Done", tf_center_justify),
		(position_set_x, pos1, 500),
		(position_set_y, pos1, 25),
		(overlay_set_position, "$g_presentation_obj_custom_battle_designer_19", pos1),

	]),
	(ti_on_presentation_event_state_change,
	[
		(store_trigger_param_1, ":object"),
		(try_begin),
			(eq, ":object", "$g_presentation_obj_custom_battle_designer_19"),
			(presentation_set_duration, 0),
		(try_end),
	]),
   ]),

# _____________________________________________________________________________END______

 ]
	
# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "presentations"
        orig_presentations = var_set[var_name_1]
        orig_presentations.extend(presentations) 
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)