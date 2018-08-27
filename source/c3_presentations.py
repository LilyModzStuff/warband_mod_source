from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
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

  ("custom_character_creation", 0,mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
		
		(assign,reg46,4),
		(assign,reg30,reg1),(assign,reg31,reg2),(assign,reg32,reg3),(assign,reg33,reg4),
		(val_div,reg30,3),  (val_div,reg31,3),  (val_div,reg32,3),  (val_div,reg33,3),
		(try_begin),(lt,reg30,reg6),(val_sub,reg6,reg30),(val_add,reg5,reg6),(assign,reg6,reg30),(try_end),
		(try_begin),(lt,reg30,reg7),(val_sub,reg7,reg30),(val_add,reg5,reg7),(assign,reg7,reg30),(try_end),
		(try_begin),(lt,reg30,reg8),(val_sub,reg8,reg30),(val_add,reg5,reg8),(assign,reg8,reg30),(try_end),
		(try_begin),(lt,reg30,reg9),(val_sub,reg9,reg30),(val_add,reg5,reg9),(assign,reg9,reg30),(try_end),
		(try_begin),(lt,reg31,reg10),(val_sub,reg10,reg31),(val_add,reg5,reg10),(assign,reg10,reg31),(try_end),
		(try_begin),(lt,reg31,reg11),(val_sub,reg11,reg31),(val_add,reg5,reg11),(assign,reg11,reg31),(try_end),
		(try_begin),(lt,reg31,reg12),(val_sub,reg12,reg31),(val_add,reg5,reg12),(assign,reg12,reg31),(try_end),
		(try_begin),(lt,reg31,reg13),(val_sub,reg13,reg31),(val_add,reg5,reg13),(assign,reg13,reg31),(try_end),
		(try_begin),(lt,reg31,reg14),(val_sub,reg14,reg31),(val_add,reg5,reg14),(assign,reg14,reg31),(try_end),
		(try_begin),(lt,reg31,reg15),(val_sub,reg15,reg31),(val_add,reg5,reg15),(assign,reg15,reg31),(try_end),
		(try_begin),(lt,reg32,reg16),(val_sub,reg16,reg32),(val_add,reg5,reg16),(assign,reg16,reg32),(try_end),
		(try_begin),(lt,reg32,reg17),(val_sub,reg17,reg32),(val_add,reg5,reg17),(assign,reg17,reg32),(try_end),
		(try_begin),(lt,reg32,reg18),(val_sub,reg18,reg32),(val_add,reg5,reg18),(assign,reg18,reg32),(try_end),
		(try_begin),(lt,reg32,reg19),(val_sub,reg19,reg32),(val_add,reg5,reg19),(assign,reg19,reg32),(try_end),
		(try_begin),(lt,reg32,reg20),(val_sub,reg20,reg32),(val_add,reg5,reg20),(assign,reg20,reg32),(try_end),
		(try_begin),(lt,reg32,reg21),(val_sub,reg21,reg32),(val_add,reg5,reg21),(assign,reg21,reg32),(try_end),
		(try_begin),(lt,reg32,reg22),(val_sub,reg22,reg32),(val_add,reg5,reg22),(assign,reg22,reg32),(try_end),
		(try_begin),(lt,reg32,reg23),(val_sub,reg23,reg32),(val_add,reg5,reg23),(assign,reg23,reg32),(try_end),
		(try_begin),(lt,reg32,reg24),(val_sub,reg24,reg32),(val_add,reg5,reg24),(assign,reg24,reg32),(try_end),
		(try_begin),(lt,reg32,reg25),(val_sub,reg25,reg32),(val_add,reg5,reg25),(assign,reg25,reg32),(try_end),
		(try_begin),(lt,reg32,reg26),(val_sub,reg26,reg32),(val_add,reg5,reg26),(assign,reg26,reg32),(try_end),
		(try_begin),(lt,reg33,reg27),(val_sub,reg27,reg33),(val_add,reg5,reg27),(assign,reg27,reg33),(try_end),
		(try_begin),(lt,reg33,reg28),(val_sub,reg28,reg33),(val_add,reg5,reg28),(assign,reg28,reg33),(try_end),
		(try_begin),(lt,reg33,reg29),(val_sub,reg29,reg33),(val_add,reg5,reg29),(assign,reg29,reg33),(try_end),
		
		## title
        (create_text_overlay, reg63, "@Custom Character Creation", tf_center_justify),
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 690),
        (overlay_set_position, reg63, pos1),
        (position_set_x, pos1, 1500),
        (position_set_y, pos1, 1500),
        (overlay_set_size, reg63, pos1),
		
		## intro
		(create_text_overlay, reg63,	"@Welcome, adventurer, to Mount and Blade: Warband."
										"^To begin the game you must first create your character."
										"^In the traditional medieval society depicted in the game,"
										"^war and politics are usually dominated by noble men."
										"^However, that doesn't mean that you shouldn't choose"
										"^to play as a female, or one who is not of noble birth."
										"^Noble men may have a somewhat easier start, but"
										"^women and commoners can attain all of the same goals"
										"^and in fact, they may have a much more interesting"
										"^and more challenging early game.^"
										"^To create your character,"
										"^choose an option from each drop down menu"
										"^and use the provided points as desired.", tf_center_justify),
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 430),
        (overlay_set_position, reg63, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg63, pos1),
		
		## Gender
        (create_text_overlay, reg63, "@Gender", tf_center_justify),
		(position_set_x, pos1, 250),
        (position_set_y, pos1, 400),
        (overlay_set_position, reg63, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg63, pos1),
		
        (create_combo_button_overlay, "$c3_presentation_gender", tf_center_justify),
		(position_set_x, pos1, 275),
		(position_set_y, pos1, 370),
        (overlay_set_position, "$c3_presentation_gender", pos1),
		(position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$c3_presentation_gender", pos1),
        (overlay_add_item, "$c3_presentation_gender", "@Man"),
		(overlay_add_item, "$c3_presentation_gender", "@Woman"),
        (overlay_set_val, "$c3_presentation_gender", "$character_gender"),
		
		## Status
		(create_text_overlay, reg63, "@Status", tf_center_justify),
		(position_set_x, pos1, 250),
        (position_set_y, pos1, 340),
        (overlay_set_position, reg63, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg63, pos1),
		
		(create_combo_button_overlay, "$c3_presentation_status"),
		(position_set_x, pos1, 275),
		(position_set_y, pos1, 310),
        (overlay_set_position, "$c3_presentation_status", pos1),
		(position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$c3_presentation_status", pos1),
		(overlay_add_item, "$c3_presentation_status", "@Monarch (kingdom)"), #0
		(overlay_add_item, "$c3_presentation_status", "@Monarch (principality)"), #1
		(overlay_add_item, "$c3_presentation_status", "@Noble (vassal)"), #1 now 2
        (overlay_add_item, "$c3_presentation_status", "@Noble (free)"), #2 now 3
        (overlay_add_item, "$c3_presentation_status", "@Commoner"), #3 now 4
		(overlay_set_val, "$c3_presentation_status", "$c3_status"),
		
		## Start?
		(create_text_overlay, "$status_response", "@Traveling to?", tf_center_justify),
		(position_set_x, pos1, 250),
        (position_set_y, pos1, 280),
        (overlay_set_position, "$status_response", pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$status_response", pos1),
		
        (create_combo_button_overlay, "$c3_start_option"),
		(position_set_x, pos1, 275),
		(position_set_y, pos1, 250),
        (overlay_set_position, "$c3_start_option", pos1),
		(position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$c3_start_option", pos1),
		(overlay_add_item, "$c3_start_option", "@Sarranid Sultanate"), #0
		(overlay_add_item, "$c3_start_option", "@Kingdom of Rhodoks"), #1
		(overlay_add_item, "$c3_start_option", "@Kingdom of Nords"), #2
		(overlay_add_item, "$c3_start_option", "@Khergit Khanate"), #3
		(overlay_add_item, "$c3_start_option", "@Kingdom of Vaegir"), #4
        (overlay_add_item, "$c3_start_option", "@Kingdom of Swadia"), #5
		(overlay_set_val, "$c3_start_option", "$c3_start"),
		
		#status text response
		(try_begin), # if vassal noble or monarch (kingdom)
			(this_or_next|eq, "$c3_status", 0),
			(eq, "$c3_status", 2),
			(overlay_set_text, "$status_response", "@Of which faction?"),
		(else_try), # if monarch (principality)
			(eq, "$c3_status", 1),
			(overlay_set_text, "$status_response", "@Of which culture?"),
		(try_end),
		
		####################################################
		####              Attributes					####
		####################################################
		
		(create_text_overlay, reg63, "@Attributes", tf_center_justify),
		(position_set_x, pos1, 1100),
        (position_set_y, pos1, 1100),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 611),
        (position_set_y, pos1, 680),
        (overlay_set_position, reg63, pos1),
		(overlay_set_color, reg63, 0x000040),
		
		##########################
		####      strength    ####
		(create_button_overlay, "$strength_label", "@Str:", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$strength_label", pos1),
		(position_set_x, pos1, 502),
        (position_set_y, pos1, 660),
        (overlay_set_position, "$strength_label", pos1),
		#(overlay_set_color, "$strength_label", 0x000020),
		(overlay_set_hilight_color, "$strength_label", 0x0000FF),
		
		(create_text_overlay, reg63, "@{reg1}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 708),
        (position_set_y, pos1, 660), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$strength_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$strength_add", pos1),
		(position_set_x, pos1, 721),
        (position_set_y, pos1, 665), #+5
        (overlay_set_position, "$strength_add", pos1),
		
		(create_text_overlay, "$strength_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$strength_+", pos1),
		(position_set_x, pos1, 719),
        (position_set_y, pos1, 660), #same
        (overlay_set_position, "$strength_+", pos1),
		
		(create_text_overlay, "$strength_desc", "@Strength: Every point adds +1 to^hit points. The following skills can^not be developed beyond 1/3 of^Strength: Ironflesh, Power Strike,^Power Throw, Power Draw.", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$strength_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 467),
        (overlay_set_position, "$strength_desc", pos1),
		(overlay_set_display, "$strength_desc", 0),
		
		#############################
		######      agility		#####
		(create_button_overlay, "$agility_label", "@Agi:", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$agility_label", pos1),
		(position_set_x, pos1, 502),
        (position_set_y, pos1, 640),
        (overlay_set_position, "$agility_label", pos1),
		#(overlay_set_color, "$agility_label", 0x000020),
		(overlay_set_hilight_color, "$agility_label", 0x0000FF),
		
		(create_text_overlay, reg63, "@{reg2}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 708),
        (position_set_y, pos1, 640), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$agility_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$agility_add", pos1),
		(position_set_x, pos1, 721),
        (position_set_y, pos1, 645), #+5
        (overlay_set_position, "$agility_add", pos1),
		
		(create_text_overlay, "$agility_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$agility_+", pos1),
		(position_set_x, pos1, 719),
        (position_set_y, pos1, 640), #same
        (overlay_set_position, "$agility_+", pos1),
		
		(create_text_overlay, "$agility_desc", "@Agility: Each point gives five^weapon points and slightly^increases movement speed. The^following skills can not be^developed beyond 1/3 of Agility:^Weapon Master, Shield, Athletics,^Riding, Horse Archery, Looting.", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$agility_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 438),
        (overlay_set_position, "$agility_desc", pos1),
		(overlay_set_display, "$agility_desc", 0),
		
		#############################
		######   intelligence	#####
		(create_button_overlay, "$intelligence_label", "@Int:", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$intelligence_label", pos1),
		(position_set_x, pos1, 502),
        (position_set_y, pos1, 620),
        (overlay_set_position, "$intelligence_label", pos1),
		#(overlay_set_color, "$intelligence_label", 0x000020),
		(overlay_set_hilight_color, "$intelligence_label", 0x0000FF),
		
		(create_text_overlay, reg63, "@{reg3}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 708),
        (position_set_y, pos1, 620), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$intelligence_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$intelligence_add", pos1),
		(position_set_x, pos1, 721),
        (position_set_y, pos1, 625), #+5
        (overlay_set_position, "$intelligence_add", pos1),
		
		(create_text_overlay, "$intelligence_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$intelligence_+", pos1),
		(position_set_x, pos1, 719),
        (position_set_y, pos1, 620), #same
        (overlay_set_position, "$intelligence_+", pos1),
		
		(create_text_overlay, "$intelligence_desc", "@Intelligence: Every point gives one^extra skill point. The following^skills can not be developed^beyond 1/3 of Intelligence: Trainer,^Tracking, Tactics, Path-finding,^Spotting, Inventory Management,^Wount Treatment, Surgery,^First Aid, Engineer, Persuasion.^^*extra skill points will be given^on next screen", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$intelligence_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 381),
        (overlay_set_position, "$intelligence_desc", pos1),
		(overlay_set_display, "$intelligence_desc", 0),
		
		#############################
		######    charisma		#####
		(create_button_overlay, "$charisma_label", "@Cha:", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$charisma_label", pos1),
		(position_set_x, pos1, 502),
        (position_set_y, pos1, 600),
        (overlay_set_position, "$charisma_label", pos1),
		#(overlay_set_color, "$charisma_label", 0x000020),
		(overlay_set_hilight_color, "$charisma_label", 0x0000FF),
		
		(create_text_overlay, reg63, "@{reg4}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 708),
        (position_set_y, pos1, 600), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$charisma_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$charisma_add", pos1),
		(position_set_x, pos1, 721),
        (position_set_y, pos1, 605), #+5
        (overlay_set_position, "$charisma_add", pos1),
		
		(create_text_overlay, "$charisma_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$charisma_+", pos1),
		(position_set_x, pos1, 719),
        (position_set_y, pos1, 600), #same
        (overlay_set_position, "$charisma_+", pos1),
		
		(create_text_overlay, "$charisma_desc", "@Charisma: Each point increases^party size limit by +1. The^following skills can not be^developed beyond 1/3 of Charisma:^Prisoner Management, Leadership,^Trade.", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$charisma_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 452),
        (overlay_set_position, "$charisma_desc", pos1),
		(overlay_set_display, "$charisma_desc", 0),
		
		#############################
		######      points		#####
		(create_text_overlay, reg63, "@points:", tf_center_justify),
		(position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 601),
        (position_set_y, pos1, 580),
        (overlay_set_position, reg63, pos1),
		#(overlay_set_color, reg63, 0x000020),
		
		(create_text_overlay, reg63, "@{reg0}", tf_left_align),
		(position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 631),
        (position_set_y, pos1, 580),
        (overlay_set_position, reg63, pos1),
		
		####################################################
		####              Skills						####
		####################################################
		
		(create_text_overlay, reg63, "@Skills", tf_center_justify),
		(position_set_x, pos1, 1100),
        (position_set_y, pos1, 1100),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 850),
        (position_set_y, pos1, 680),
        (overlay_set_position, reg63, pos1),
		(overlay_set_color, reg63, 0x004000),
		
		#############################
		######    ironflesh		#####
		(create_button_overlay, "$ironflesh_label", "@Ironflesh", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$ironflesh_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 660),
        (overlay_set_position, "$ironflesh_label", pos1),
		#(overlay_set_color, "$ironflesh_label", 0x002000),
		(overlay_set_hilight_color, "$ironflesh_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg6}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 660), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$ironflesh_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$ironflesh_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 665), #+5
        (overlay_set_position, "$ironflesh_add", pos1),
		
		(create_text_overlay, "$ironflesh_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$ironflesh_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 660), #same
        (overlay_set_position, "$ironflesh_+", pos1),
		
		(create_text_overlay, "$ironflesh_desc", "@Each point to this skill increases ^hit points by +2.^(Personal skill)^^^^^^^^Base Attribute: Strength", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$ironflesh_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$ironflesh_desc", pos1),
		(overlay_set_display, "$ironflesh_desc", 0),
		
		# power strike
		(create_button_overlay, "$power_strike_label", "@Power Strike", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$power_strike_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 640),
        (overlay_set_position, "$power_strike_label", pos1),
		#(overlay_set_color, "$power_strike_label", 0x002000),
		(overlay_set_hilight_color, "$power_strike_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg7}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 640), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$power_strike_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$power_strike_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 645), #+5
        (overlay_set_position, "$power_strike_add", pos1),
		
		(create_text_overlay, "$power_strike_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$power_strike_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 640), #same
        (overlay_set_position, "$power_strike_+", pos1),
		
		(create_text_overlay, "$power_strike_desc", "@Each point to this skill increases ^melee damage by 8%.^(Personal skill)^^^^^^^^Base Attribute: Strength", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$power_strike_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$power_strike_desc", pos1),
		(overlay_set_display, "$power_strike_desc", 0),
		
		#power throw
		(create_button_overlay, "$power_throw_label", "@Power Throw", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$power_throw_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 620),
        (overlay_set_position, "$power_throw_label", pos1),
		#(overlay_set_color, "$power_throw_label", 0x002000),
		(overlay_set_hilight_color, "$power_throw_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg8}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 620), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$power_throw_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$power_throw_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 625), #+5
        (overlay_set_position, "$power_throw_add", pos1),
		
		(create_text_overlay, "$power_throw_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$power_throw_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 620), #same
        (overlay_set_position, "$power_throw_+", pos1),
		
		(create_text_overlay, "$power_throw_desc", "@Each point to this skill increases ^throwing damage by 10%.^(Personal skill)^^^^^^^^Base Attribute: Strength", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$power_throw_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$power_throw_desc", pos1),
		(overlay_set_display, "$power_throw_desc", 0),
		
		#power draw
		(create_button_overlay, "$power_draw_label", "@Power Draw", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$power_draw_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 600),
        (overlay_set_position, "$power_draw_label", pos1),
		#(overlay_set_color, "$power_draw_label", 0x002000),
		(overlay_set_hilight_color, "$power_draw_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg9}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 600), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$power_draw_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$power_draw_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 605), #+5
        (overlay_set_position, "$power_draw_add", pos1),
		
		(create_text_overlay, "$power_draw_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$power_draw_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 600), #same
        (overlay_set_position, "$power_draw_+", pos1),
		
		(create_text_overlay, "$power_draw_desc", "@Lets character use more powerful ^bows. Each point to this skill (up^to four plus power-draw^requirement of the bow)^increases bow damage by 14%.^(Personal skill)^^^^^Base Attribute: Strength", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$power_draw_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$power_draw_desc", pos1),
		(overlay_set_display, "$power_draw_desc", 0),
		
		#weapon master
		(create_button_overlay, "$weapon_master_label", "@Weapon Master", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$weapon_master_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 580),
        (overlay_set_position, "$weapon_master_label", pos1),
		#(overlay_set_color, "$weapon_master_label", 0x002000),
		(overlay_set_hilight_color, "$weapon_master_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg10}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 580), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$weapon_master_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$weapon_master_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 585), #+5
        (overlay_set_position, "$weapon_master_add", pos1),
		
		(create_text_overlay, "$weapon_master_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$weapon_master_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 580), #same
        (overlay_set_position, "$weapon_master_+", pos1),
		
		(create_text_overlay, "$weapon_master_desc", "@Makes it easier to learn weapon^proficiencies and increases the^proficiency limits. Limits go as:^60, 100, 140, 180, 220, 260, 300,^340, 380, 420.^(Personal skill)^^^^^Base Attribute: Agility", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$weapon_master_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$weapon_master_desc", pos1),
		(overlay_set_display, "$weapon_master_desc", 0),
		
		#shield
		(create_button_overlay, "$shield_label", "@Shield", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$shield_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 560),
        (overlay_set_position, "$shield_label", pos1),
		#(overlay_set_color, "$shield_label", 0x002000),
		(overlay_set_hilight_color, "$shield_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg11}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 560), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$shield_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$shield_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 565), #+5
        (overlay_set_position, "$shield_add", pos1),
		
		(create_text_overlay, "$shield_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$shield_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 560), #same
        (overlay_set_position, "$shield_+", pos1),
		
		(create_text_overlay, "$shield_desc", "@Reduces damage to shields (by 8%^per skill level) and improves^shield speed and coverage.^(Personal skill)^^^^^^^Base Attribute: Agility", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$shield_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$shield_desc", pos1),
		(overlay_set_display, "$shield_desc", 0),
		
		#athletics
		(create_button_overlay, "$athletics_label", "@Athletics", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$athletics_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 540),
        (overlay_set_position, "$athletics_label", pos1),
		#(overlay_set_color, "$athletics_label", 0x002000),
		(overlay_set_hilight_color, "$athletics_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg12}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 540), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$athletics_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$athletics_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 545), #+5
        (overlay_set_position, "$athletics_add", pos1),
		
		(create_text_overlay, "$athletics_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$athletics_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 540), #same
        (overlay_set_position, "$athletics_+", pos1),
		
		(create_text_overlay, "$athletics_desc", "@Improves your running speed.^(Personal skill)^^^^^^^^^Base Attribute: Agility", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$athletics_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$athletics_desc", pos1),
		(overlay_set_display, "$athletics_desc", 0),
		
		#riding
		(create_button_overlay, "$riding_label", "@Riding", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$riding_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 520),
        (overlay_set_position, "$riding_label", pos1),
		#(overlay_set_color, "$riding_label", 0x002000),
		(overlay_set_hilight_color, "$riding_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg13}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 520), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$riding_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$riding_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 525), #+5
        (overlay_set_position, "$riding_add", pos1),
		
		(create_text_overlay, "$riding_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$riding_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 520), #same
        (overlay_set_position, "$riding_+", pos1),
		
		(create_text_overlay, "$riding_desc", "@Enables you to ride horses of^higher difficulty levels and^increases your riding speed and^manuever.^(Personal skill)^^^^^^Base Attribute: Agility", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$riding_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$riding_desc", pos1),
		(overlay_set_display, "$riding_desc", 0),
		
		#horse archery
		(create_button_overlay, "$horse_archery_label", "@Horse Archery", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$horse_archery_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 500),
        (overlay_set_position, "$horse_archery_label", pos1),
		#(overlay_set_color, "$horse_archery_label", 0x002000),
		(overlay_set_hilight_color, "$horse_archery_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg14}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 500), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$horse_archery_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$horse_archery_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 505), #+5
        (overlay_set_position, "$horse_archery_add", pos1),
		
		(create_text_overlay, "$horse_archery_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$horse_archery_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 500), #same
        (overlay_set_position, "$horse_archery_+", pos1),
		
		(create_text_overlay, "$horse_archery_desc", "@Reduces damage and accuracy^penalties for archery and^throwing from horseback.^(Personal skill)^^^^^^^Base Attribute: Agility", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$horse_archery_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$horse_archery_desc", pos1),
		(overlay_set_display, "$horse_archery_desc", 0),
		
		#looting
		(create_button_overlay, "$looting_label", "@Looting", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$looting_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 480),
        (overlay_set_position, "$looting_label", pos1),
		#(overlay_set_color, "$looting_label", 0x002000),
		(overlay_set_hilight_color, "$looting_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg15}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 480), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$looting_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$looting_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 485), #+5
        (overlay_set_position, "$looting_add", pos1),
		
		(create_text_overlay, "$looting_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$looting_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 480), #same
        (overlay_set_position, "$looting_+", pos1),
		
		(create_text_overlay, "$looting_desc", "@This skill increases the amount^of loot obtained by 10% per^skill level.^(Party skill)^^^^^^^Base Attribute: Agility", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$looting_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$looting_desc", pos1),
		(overlay_set_display, "$looting_desc", 0),
		
		#trainer
		(create_button_overlay, "$trainer_label", "@Trainer", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$trainer_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 460),
        (overlay_set_position, "$trainer_label", pos1),
		#(overlay_set_color, "$trainer_label", 0x002000),
		(overlay_set_hilight_color, "$trainer_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg16}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 460), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$trainer_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$trainer_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 465), #+5
        (overlay_set_position, "$trainer_add", pos1),
		
		(create_text_overlay, "$trainer_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$trainer_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 460), #same
        (overlay_set_position, "$trainer_+", pos1),
		
		(create_text_overlay, "$trainer_desc", "@Every day, each hero with this^skill adds some experience to^every other member of the party^whose level is lower than his/hers.^Experience gained goes as: (0,4,10,^16,23,30,38,46,55,65,80)^(Personal skill)^^^^Base Attribute: Intelligence", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$trainer_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$trainer_desc", pos1),
		(overlay_set_display, "$trainer_desc", 0),
		
		#tracking
		(create_button_overlay, "$tracking_label", "@Tracking", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$tracking_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 440),
        (overlay_set_position, "$tracking_label", pos1),
		#(overlay_set_color, "$tracking_label", 0x002000),
		(overlay_set_hilight_color, "$tracking_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg17}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 440), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$tracking_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$tracking_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 445), #+5
        (overlay_set_position, "$tracking_add", pos1),
		
		(create_text_overlay, "$tracking_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$tracking_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 440), #same
        (overlay_set_position, "$tracking_+", pos1),
		
		(create_text_overlay, "$tracking_desc", "@Tracks become more informative.^(Party skill)^^^^^^^^^Base Attribute: Intelligence", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$tracking_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$tracking_desc", pos1),
		(overlay_set_display, "$tracking_desc", 0),
		
		#tactics
		(create_button_overlay, "$tactics_label", "@Tactics", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$tactics_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 420),
        (overlay_set_position, "$tactics_label", pos1),
		#(overlay_set_color, "$tactics_label", 0x002000),
		(overlay_set_hilight_color, "$tactics_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg18}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 420), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$tactics_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$tactics_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 425), #+5
        (overlay_set_position, "$tactics_add", pos1),
		
		(create_text_overlay, "$tactics_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$tactics_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 420), #same
        (overlay_set_position, "$tactics_+", pos1),
		
		(create_text_overlay, "$tactics_desc", "@Every two levels of this skill^increases starting battle^advantage by 1.^(Party skill)^^^^^^^Base Attribute: Intelligence", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$tactics_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$tactics_desc", pos1),
		(overlay_set_display, "$tactics_desc", 0),
		
		#path finding
		(create_button_overlay, "$path_finding_label", "@Path-finding", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$path_finding_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 400),
        (overlay_set_position, "$path_finding_label", pos1),
		#(overlay_set_color, "$path_finding_label", 0x002000),
		(overlay_set_hilight_color, "$path_finding_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg19}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 400), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$pathfinding_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$pathfinding_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 405), #+5
        (overlay_set_position, "$pathfinding_add", pos1),
		
		(create_text_overlay, "$pathfinding_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$pathfinding_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 400), #same
        (overlay_set_position, "$pathfinding_+", pos1),
		
		(create_text_overlay, "$path_finding_desc", "@Party map speed is increased by^3% per skill level.^(Party skill)^^^^^^^^Base Attribute: Intelligence", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$path_finding_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$path_finding_desc", pos1),
		(overlay_set_display, "$path_finding_desc", 0),
		
		#spotting
		(create_button_overlay, "$spotting_label", "@Spotting", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$spotting_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$spotting_label", pos1),
		#(overlay_set_color, "$spotting_label", 0x002000),
		(overlay_set_hilight_color, "$spotting_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg20}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 380), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$spotting_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$spotting_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 385), #+5
        (overlay_set_position, "$spotting_add", pos1),
		
		(create_text_overlay, "$spotting_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$spotting_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 380), #same
        (overlay_set_position, "$spotting_+", pos1),
		
		(create_text_overlay, "$spotting_desc", "@Party seeing range is increased by^10% per skill level.^(Party skill)^^^^^^^^Base Attribute: Intelligence", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$spotting_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$spotting_desc", pos1),
		(overlay_set_display, "$spotting_desc", 0),
		
		#inventory management
		(create_button_overlay, "$inventory_management_label", "@Inventory Management", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$inventory_management_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 360),
        (overlay_set_position, "$inventory_management_label", pos1),
		#(overlay_set_color, "$inventory_management_label", 0x002000),
		(overlay_set_hilight_color, "$inventory_management_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg21}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 360), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$inventory_management_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$inventory_management_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 365), #+5
        (overlay_set_position, "$inventory_management_add", pos1),
		
		(create_text_overlay, "$inventory_management_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$inventory_management_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 360), #same
        (overlay_set_position, "$inventory_management_+", pos1),
		
		(create_text_overlay, "$inventory_management_desc", "@Increases inventory capacity^by +6 per skill level.^(Leader skill)^^^^^^^^Base Attribute: Intelligence", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$inventory_management_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$inventory_management_desc", pos1),
		(overlay_set_display, "$inventory_management_desc", 0),
		
		# wound treatment
		(create_button_overlay, "$wound_treatment_label", "@Wound Treatment", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$wound_treatment_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 340),
        (overlay_set_position, "$wound_treatment_label", pos1),
		#(overlay_set_color, "$wound_treatment_label", 0x002000),
		(overlay_set_hilight_color, "$wound_treatment_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg22}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 340), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$wound_treatment_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$wound_treatment_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 345), #+5
        (overlay_set_position, "$wound_treatment_add", pos1),
		
		(create_text_overlay, "$wound_treatment_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$wound_treatment_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 340), #same
        (overlay_set_position, "$wound_treatment_+", pos1),
		
		(create_text_overlay, "$wound_treatment_desc", "@Party healing speed is increased^by 20% per level of this skill.^(Party skill)^^^^^^^^Base Attribute: Intelligence", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$wound_treatment_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$wound_treatment_desc", pos1),
		(overlay_set_display, "$wound_treatment_desc", 0),
		
		# surgery
		(create_button_overlay, "$surgery_label", "@Surgery", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$surgery_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 320),
        (overlay_set_position, "$surgery_label", pos1),
		#(overlay_set_color, "$surgery_label", 0x002000),
		(overlay_set_hilight_color, "$surgery_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg23}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 320), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$surgery_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$surgery_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 325), #+5
        (overlay_set_position, "$surgery_add", pos1),
		
		(create_text_overlay, "$surgery_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$surgery_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 320), #same
        (overlay_set_position, "$surgery_+", pos1),
		
		(create_text_overlay, "$surgery_desc", "@Each point to this skill gives a 4%^chance that a mortally struck^party member will be wounded^rather than killed.^(Party skill)^^^^^^Base Attribute: Intelligence", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$surgery_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$surgery_desc", pos1),
		(overlay_set_display, "$surgery_desc", 0),
		
		#first aid
		(create_button_overlay, "$first_aid_label", "@First Aid", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$first_aid_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$first_aid_label", pos1),
		#(overlay_set_color, "$first_aid_label", 0x002000),
		(overlay_set_hilight_color, "$first_aid_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg24}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 300), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$first_aid_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$first_aid_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 305), #+5
        (overlay_set_position, "$first_aid_add", pos1),
		
		(create_text_overlay, "$first_aid_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$first_aid_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 300), #same
        (overlay_set_position, "$first_aid_+", pos1),
		
		(create_text_overlay, "$first_aid_desc", "@Heroes regain 5% per skill level of^hit-points lost during mission.^(Party skill)^^^^^^^^Base Attribute: Intelligence", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$first_aid_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$first_aid_desc", pos1),
		(overlay_set_display, "$first_aid_desc", 0),
		
		# engineer
		(create_button_overlay, "$engineer_label", "@Engineer", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$engineer_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 280),
        (overlay_set_position, "$engineer_label", pos1),
		#(overlay_set_color, "$engineer_label", 0x002000),
		(overlay_set_hilight_color, "$engineer_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg25}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 280), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$engineer_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$engineer_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 285), #+5
        (overlay_set_position, "$engineer_add", pos1),
		
		(create_text_overlay, "$engineer_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$engineer_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 280), #same
        (overlay_set_position, "$engineer_+", pos1),
		
		(create_text_overlay, "$engineer_desc", "@This skill allows you to construct^siege equipment and fief^improvements more efficiently.^(Party skill)^^^^^^^Base Attribute: Intelligence", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$engineer_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$engineer_desc", pos1),
		(overlay_set_display, "$engineer_desc", 0),
		
		#persuasion
		(create_button_overlay, "$persuasion_label", "@Persuasion", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$persuasion_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 260),
        (overlay_set_position, "$persuasion_label", pos1),
		#(overlay_set_color, "$persuasion_label", 0x002000),
		(overlay_set_hilight_color, "$persuasion_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg26}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 260), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$persuasion_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$persuasion_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 265), #+5
        (overlay_set_position, "$persuasion_add", pos1),
		
		(create_text_overlay, "$persuasion_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$persuasion_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 260), #same
        (overlay_set_position, "$persuasion_+", pos1),
		
		(create_text_overlay, "$persuasion_desc", "@This skill helps you make other^people accept your point of view.^It also lowers the minimum level^of relationship needed to get^NPCs to do what you want.^(Personal skill)^^^^^Base Attribute: Intelligence", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$persuasion_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$persuasion_desc", pos1),
		(overlay_set_display, "$persuasion_desc", 0),
		
		#prisoner management
		(create_button_overlay, "$prisoner_management_label", "@Prisoner Management", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$prisoner_management_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 240),
        (overlay_set_position, "$prisoner_management_label", pos1),
		#(overlay_set_color, "$prisoner_management_label", 0x002000),
		(overlay_set_hilight_color, "$prisoner_management_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg27}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 240), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$prisoner_management_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$prisoner_management_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 245), #+5
        (overlay_set_position, "$prisoner_management_add", pos1),
		
		(create_text_overlay, "$prisoner_management_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$prisoner_management_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 240), #same
        (overlay_set_position, "$prisoner_management_+", pos1),
		
		(create_text_overlay, "$prisoner_management_desc", "@Every level of this skill increases^maximum number of prisoners^by 5.^(Leader skill)^^^^^^^Base Attribute: Charisma", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$prisoner_management_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$prisoner_management_desc", pos1),
		(overlay_set_display, "$prisoner_management_desc", 0),
		
		# leadership
		(create_button_overlay, "$leadership_label", "@Leadership", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$leadership_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 220),
        (overlay_set_position, "$leadership_label", pos1),
		#(overlay_set_color, "$leadership_label", 0x002000),
		(overlay_set_hilight_color, "$leadership_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg28}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 220), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$leadership_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$leadership_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 225), #+5
        (overlay_set_position, "$leadership_add", pos1),
		
		(create_text_overlay, "$leadership_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$leadership_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 220), #same
        (overlay_set_position, "$leadership_+", pos1),
		
		(create_text_overlay, "$leadership_desc", "@Every point increases maximum^number of troops you can^command by 5, increases your^party morale and reduces troop^wages by 5%.^(Leader skill)^^^^^Base Attribute: Charisma", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$leadership_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$leadership_desc", pos1),
		(overlay_set_display, "$leadership_desc", 0),
		
		#trade
		(create_button_overlay, "$trade_label", "@Trade", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$trade_label", pos1),
		(position_set_x, pos1, 741),
        (position_set_y, pos1, 200),
        (overlay_set_position, "$trade_label", pos1),
		#(overlay_set_color, "$trade_label", 0x002000),
		(overlay_set_hilight_color, "$trade_label", 0x00FF00),
		
		(create_text_overlay, reg63, "@{reg29}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 945),
        (position_set_y, pos1, 200), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$trade_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$trade_add", pos1),
		(position_set_x, pos1, 960),
        (position_set_y, pos1, 205), #+5
        (overlay_set_position, "$trade_add", pos1),
		
		(create_text_overlay, "$trade_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$trade_+", pos1),
		(position_set_x, pos1, 958),
        (position_set_y, pos1, 200), #same
        (overlay_set_position, "$trade_+", pos1),
		
		(create_text_overlay, "$trade_desc", "@Every level of this skill reduces^your trade penalty by 5%.^(Party skill)^^^^^^^^Base Attribute: Charisma", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$trade_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$trade_desc", pos1),
		(overlay_set_display, "$trade_desc", 0),
		
		#####    skill points     #####
		(create_text_overlay, reg63, "@points:", tf_center_justify),
		(position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 840),
        (position_set_y, pos1, 180),
        (overlay_set_position, reg63, pos1),
		#(overlay_set_color, reg63, 0x004000),
		
		(create_text_overlay, reg63, "@{reg5}", tf_left_align),
		(position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 870),
        (position_set_y, pos1, 180),
        (overlay_set_position, reg63, pos1),
		
		################################
		### increase attribute notes ###
		
		### strength ###
		(create_text_overlay, "$strength_note", "@(Raise Strength to raise this skill)", tf_left_align),
		(position_set_x, pos1, 750),
        (position_set_y, pos1, 750),
        (overlay_set_size, "$strength_note", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 410),
        (overlay_set_position, "$strength_note", pos1),
		(overlay_set_color, "$strength_note", 0x800000),
		(overlay_set_display, "$strength_note", 0),
		### agility ###
		(create_text_overlay, "$agility_note", "@(Raise Agility to raise this skill)", tf_left_align),
		(position_set_x, pos1, 750),
        (position_set_y, pos1, 750),
        (overlay_set_size, "$agility_note", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 410),
        (overlay_set_position, "$agility_note", pos1),
		(overlay_set_color, "$agility_note", 0x800000),
		(overlay_set_display, "$agility_note", 0),
		### intelligence ###
		(create_text_overlay, "$intelligence_note", "@(Raise Intelligence to raise this skill)", tf_left_align),
		(position_set_x, pos1, 750),
        (position_set_y, pos1, 750),
        (overlay_set_size, "$intelligence_note", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 410),
        (overlay_set_position, "$intelligence_note", pos1),
		(overlay_set_color, "$intelligence_note", 0x800000),
		(overlay_set_display, "$intelligence_note", 0),
		### charisma ###
		(create_text_overlay, "$charisma_note", "@(Raise Charisma to raise this skill)", tf_left_align),
		(position_set_x, pos1, 750),
        (position_set_y, pos1, 750),
        (overlay_set_size, "$charisma_note", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 410),
        (overlay_set_position, "$charisma_note", pos1),
		(overlay_set_color, "$charisma_note", 0x800000),
		(overlay_set_display, "$charisma_note", 0),
		
		####################################################
		####             Proficiencies					####
		####################################################
		
		(create_text_overlay, reg63, "@Proficiencies", tf_center_justify),
		(position_set_x, pos1, 1100),
        (position_set_y, pos1, 1100),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 611),
        (position_set_y, pos1, 320),
        (overlay_set_position, reg63, pos1),
		(overlay_set_color, reg63, 0x400000),
		
		# one handed weapons
		(create_button_overlay, "$one_hand_label", "@One Handed Weapons", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$one_hand_label", pos1),
		(position_set_x, pos1, 502),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$one_hand_label", pos1),
		#(overlay_set_color, "$one_hand_label", 0x200000),
		(overlay_set_hilight_color, "$one_hand_label", 0xFF0000),
		
		(create_text_overlay, reg63, "@{reg35}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 708),
        (position_set_y, pos1, 300), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$one_hand_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$one_hand_add", pos1),
		(position_set_x, pos1, 721),
        (position_set_y, pos1, 305), #+5
        (overlay_set_position, "$one_hand_add", pos1),
		
		(create_text_overlay, "$one_hand_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$one_hand_+", pos1),
		(position_set_x, pos1, 719),
        (position_set_y, pos1, 300), #same
        (overlay_set_position, "$one_hand_+", pos1),
		
		(create_text_overlay, "$one_handed_desc", "@Covers usage of one handed ^weapons", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$one_handed_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 510),
        (overlay_set_position, "$one_handed_desc", pos1),
		(overlay_set_display, "$one_handed_desc", 0),
		
		# two handed weapons
		(create_button_overlay, "$two_hand_label", "@Two Handed Weapons", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$two_hand_label", pos1),
		(position_set_x, pos1, 502),
        (position_set_y, pos1, 280),
        (overlay_set_position, "$two_hand_label", pos1),
		#(overlay_set_color, "$two_hand_label", 0x200000),
		(overlay_set_hilight_color, "$two_hand_label", 0xFF0000),
		
		(create_text_overlay, reg63, "@{reg36}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 708),
        (position_set_y, pos1, 280), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$two_hand_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$two_hand_add", pos1),
		(position_set_x, pos1, 721),
        (position_set_y, pos1, 285), #+5
        (overlay_set_position, "$two_hand_add", pos1),
		
		(create_text_overlay, "$two_hand_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$two_hand_+", pos1),
		(position_set_x, pos1, 719),
        (position_set_y, pos1, 280), #same
        (overlay_set_position, "$two_hand_+", pos1),
		
		(create_text_overlay, "$two_handed_desc", "@Covers usage of two handed ^weapons", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$two_handed_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 510),
        (overlay_set_position, "$two_handed_desc", pos1),
		(overlay_set_display, "$two_handed_desc", 0),
		
		# polearms
		(create_button_overlay, "$polearms_label", "@Polearms", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$polearms_label", pos1),
		(position_set_x, pos1, 502),
        (position_set_y, pos1, 260),
        (overlay_set_position, "$polearms_label", pos1),
		#(overlay_set_color, "$polearms_label", 0x200000),
		(overlay_set_hilight_color, "$polearms_label", 0xFF0000),
		
		(create_text_overlay, reg63, "@{reg37}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 708),
        (position_set_y, pos1, 260), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$polearms_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$polearms_add", pos1),
		(position_set_x, pos1, 721),
        (position_set_y, pos1, 265), #+5
        (overlay_set_position, "$polearms_add", pos1),
		
		(create_text_overlay, "$polearms_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$polearms_+", pos1),
		(position_set_x, pos1, 719),
        (position_set_y, pos1, 260), #same
        (overlay_set_position, "$polearms_+", pos1),
		
		(create_text_overlay, "$polearms_desc", "@Covers usage of pole weapons", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$polearms_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 524),
        (overlay_set_position, "$polearms_desc", pos1),
		(overlay_set_display, "$polearms_desc", 0),
		
		#archery
		(create_button_overlay, "$archery_label", "@Archery", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$archery_label", pos1),
		(position_set_x, pos1, 502),
        (position_set_y, pos1, 240),
        (overlay_set_position, "$archery_label", pos1),
		#(overlay_set_color, "$archery_label", 0x200000),
		(overlay_set_hilight_color, "$archery_label", 0xFF0000),
		
		(create_text_overlay, reg63, "@{reg38}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 708),
        (position_set_y, pos1, 240), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$archery_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$archery_add", pos1),
		(position_set_x, pos1, 721),
        (position_set_y, pos1, 245), #+5
        (overlay_set_position, "$archery_add", pos1),
		
		(create_text_overlay, "$archery_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$archery_+", pos1),
		(position_set_x, pos1, 719),
        (position_set_y, pos1, 240), #same
        (overlay_set_position, "$archery_+", pos1),
		
		(create_text_overlay, "$archery_desc", "@Covers usage of bows", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$archery_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 524),
        (overlay_set_position, "$archery_desc", pos1),
		(overlay_set_display, "$archery_desc", 0),
		
		# crossbows
		(create_button_overlay, "$crossbows_label", "@Crossbows", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$crossbows_label", pos1),
		(position_set_x, pos1, 502),
        (position_set_y, pos1, 220),
        (overlay_set_position, "$crossbows_label", pos1),
		#(overlay_set_color, "$crossbows_label", 0x200000),
		(overlay_set_hilight_color, "$crossbows_label", 0xFF0000),
		
		(create_text_overlay, reg63, "@{reg39}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 708),
        (position_set_y, pos1, 220), #change
        (overlay_set_position, reg63, pos1),
		
		(create_game_button_overlay,"$crossbows_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$crossbows_add", pos1),
		(position_set_x, pos1, 721),
        (position_set_y, pos1, 225), #+5
        (overlay_set_position, "$crossbows_add", pos1),
		
		(create_text_overlay, "$crossbows_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$crossbows_+", pos1),
		(position_set_x, pos1, 719),
        (position_set_y, pos1, 220), #same
        (overlay_set_position, "$crossbows_+", pos1),
		
		(create_text_overlay, "$crossbows_desc", "@Covers usage of crossbows", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$crossbows_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 524),
        (overlay_set_position, "$crossbows_desc", pos1),
		(overlay_set_display, "$crossbows_desc", 0),
		
		#throwing
		(create_button_overlay, "$throwing_label", "@Throwing", tf_left_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$throwing_label", pos1),
		(position_set_x, pos1, 502),
        (position_set_y, pos1, 200),
        (overlay_set_position, "$throwing_label", pos1),
		#(overlay_set_color, "$throwing_label", 0x200000),
		(overlay_set_hilight_color, "$throwing_label", 0xFF0000),
		
		(create_text_overlay, reg63, "@{reg40}", tf_right_align),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 708),
        (position_set_y, pos1, 200), #change
        (overlay_set_position, reg63, pos1),

		(create_game_button_overlay,"$throwing_add","@+"),
		(position_set_x, pos1, 14),
        (position_set_y, pos1, 14),
        (overlay_set_size, "$throwing_add", pos1),
		(position_set_x, pos1, 721),
        (position_set_y, pos1, 205), #+5
        (overlay_set_position, "$throwing_add", pos1),

		(create_text_overlay, "$throwing_+", "@+", tf_center_justify),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$throwing_+", pos1),
		(position_set_x, pos1, 719),
        (position_set_y, pos1, 200), #same
        (overlay_set_position, "$throwing_+", pos1),
		
		(create_text_overlay, "$throwing_desc", "@Covers usage of thrown weapons", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$throwing_desc", pos1),
		(position_set_x, pos1, 505),
        (position_set_y, pos1, 524),
        (overlay_set_position, "$throwing_desc", pos1),
		(overlay_set_display, "$throwing_desc", 0),
		
		#weapon points
		(create_text_overlay, reg63, "@points:", tf_center_justify),
		(position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 601),
        (position_set_y, pos1, 180),
        (overlay_set_position, reg63, pos1),
		#(overlay_set_color, reg63, 0x200000),
		
		(create_text_overlay, reg63, "@{reg34}", tf_left_align),
		(position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg63, pos1),
		(position_set_x, pos1, 631),
        (position_set_y, pos1, 180),
        (overlay_set_position, reg63, pos1),

		## Reset button
		(create_game_button_overlay, "$reset_button", "@Reset"),
		(position_set_x, pos1, 100),
        (position_set_y, pos1, 25),
        (overlay_set_size, "$reset_button", pos1),
        (position_set_x, pos1, 736),
        (position_set_y, pos1, 140),
        (overlay_set_position, "$reset_button", pos1),
		(overlay_set_display, "$reset_button", 0),
		
		## Done button
		(create_game_button_overlay, "$done_button", "@Done"),
        (position_set_x, pos1, 875),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$done_button", pos1),
		
		## Back button
		(create_game_button_overlay, "$back_button", "@Back"),
        (position_set_x, pos1, 125),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$back_button", pos1),
		
	(try_begin), ### reset button appears/disappears appropriately ###
		(this_or_next|gt, reg1, 4),
		(this_or_next|gt, reg2, 4),
		(this_or_next|gt, reg3, 4),
		(this_or_next|gt, reg4, 4),
		(this_or_next|gt, reg6, 0),
		(this_or_next|gt, reg7, 0),
		(this_or_next|gt, reg8, 0),
		(this_or_next|gt, reg9, 0),
		(this_or_next|gt, reg10, 0),
		(this_or_next|gt, reg11, 0),
		(this_or_next|gt, reg12, 0),
		(this_or_next|gt, reg13, 0),
		(this_or_next|gt, reg14, 0),
		(this_or_next|gt, reg15, 0),
		(this_or_next|gt, reg16, 0),
		(this_or_next|gt, reg17, 0),
		(this_or_next|gt, reg18, 0),
		(this_or_next|gt, reg19, 0),
		(this_or_next|gt, reg20, 0),
		(this_or_next|gt, reg21, 0),
		(this_or_next|gt, reg22, 0),
		(this_or_next|gt, reg23, 0),
		(this_or_next|gt, reg24, 0),
		(this_or_next|gt, reg25, 0),
		(this_or_next|gt, reg26, 0),
		(this_or_next|gt, reg27, 0),
		(this_or_next|gt, reg28, 0),
		(this_or_next|gt, reg29, 0),
		(this_or_next|gt, reg35, 15),
		(this_or_next|gt, reg36, 15),
		(this_or_next|gt, reg37, 15),
		(this_or_next|gt, reg38, 15),
		(this_or_next|gt, reg39, 15),
		(gt, reg40, 15),
		(overlay_set_display, "$reset_button", 1),
	(try_end),
		
	(try_begin), ### add buttons disappear if no points ###
		##################
		### attributes ###
		(eq,reg0,0),
		# strength buttons
		(overlay_set_display, "$strength_+", 0),
		(overlay_set_display, "$strength_add", 0),
		# agility buttons
		(overlay_set_display, "$agility_+", 0),
		(overlay_set_display, "$agility_add", 0),
		# intelligence buttons
		(overlay_set_display, "$intelligence_+", 0),
		(overlay_set_display, "$intelligence_add", 0),
		# charisma buttons
		(overlay_set_display, "$charisma_+", 0),
		(overlay_set_display, "$charisma_add", 0),
	(try_end),
	
	(try_begin), ### add buttons disappear if no points ###
		##############
		### skills ###
		(eq,reg5,0),
		# ironflesh buttons
		(overlay_set_display, "$ironflesh_+", 0),
		(overlay_set_display, "$ironflesh_add", 0),
		# power strike buttons
		(overlay_set_display, "$power_strike_+", 0),
		(overlay_set_display, "$power_strike_add", 0),
		# power throw buttons
		(overlay_set_display, "$power_throw_+", 0),
		(overlay_set_display, "$power_throw_add", 0),
		# power draw buttons
		(overlay_set_display, "$power_draw_+", 0),
		(overlay_set_display, "$power_draw_add", 0),
		# weapon master buttons
		(overlay_set_display, "$weapon_master_+", 0),
		(overlay_set_display, "$weapon_master_add", 0),
		# shield buttons
		(overlay_set_display, "$shield_+", 0),
		(overlay_set_display, "$shield_add", 0),
		# athletics buttons
		(overlay_set_display, "$athletics_+", 0),
		(overlay_set_display, "$athletics_add", 0),
		# riding buttons
		(overlay_set_display, "$riding_+", 0),
		(overlay_set_display, "$riding_add", 0),
		# horse archery buttons
		(overlay_set_display, "$horse_archery_+", 0),
		(overlay_set_display, "$horse_archery_add", 0),
		# looting buttons
		(overlay_set_display, "$looting_+", 0),
		(overlay_set_display, "$looting_add", 0),
		# trainer buttons
		(overlay_set_display, "$trainer_+", 0),
		(overlay_set_display, "$trainer_add", 0),
		# tracking buttons
		(overlay_set_display, "$tracking_+", 0),
		(overlay_set_display, "$tracking_add", 0),
		# tactics buttons
		(overlay_set_display, "$tactics_+", 0),
		(overlay_set_display, "$tactics_add", 0),
		# path finding buttons
		(overlay_set_display, "$pathfinding_+", 0),
		(overlay_set_display, "$pathfinding_add", 0),
		# spotting buttons
		(overlay_set_display, "$spotting_+", 0),
		(overlay_set_display, "$spotting_add", 0),
		# inventory management buttons
		(overlay_set_display, "$inventory_management_+", 0),
		(overlay_set_display, "$inventory_management_add", 0),
		# wound treatment buttons
		(overlay_set_display, "$wound_treatment_+", 0),
		(overlay_set_display, "$wound_treatment_add", 0),
		# surgery buttons
		(overlay_set_display, "$surgery_+", 0),
		(overlay_set_display, "$surgery_add", 0),
		# first aid buttons
		(overlay_set_display, "$first_aid_+", 0),
		(overlay_set_display, "$first_aid_add", 0),
		# engineer buttons
		(overlay_set_display, "$engineer_+", 0),
		(overlay_set_display, "$engineer_add", 0),
		# persuasion buttons
		(overlay_set_display, "$persuasion_+", 0),
		(overlay_set_display, "$persuasion_add", 0),
		# prisoner management buttons
		(overlay_set_display, "$prisoner_management_+", 0),
		(overlay_set_display, "$prisoner_management_add", 0),
		# leadership buttons
		(overlay_set_display, "$leadership_+", 0),
		(overlay_set_display, "$leadership_add", 0),
		# trade buttons
		(overlay_set_display, "$trade_+", 0),
		(overlay_set_display, "$trade_add", 0),
	(try_end),
	
	(try_begin), ### add buttons disappear if no points ###
	#####################
	### proficiencies ###
		(eq,reg34,0),
		# one handed buttons
		(overlay_set_display, "$one_hand_+", 0),
		(overlay_set_display, "$one_hand_add", 0),
		# two handed buttons
		(overlay_set_display, "$two_hand_+", 0),
		(overlay_set_display, "$two_hand_add", 0),
		# polearms buttons
		(overlay_set_display, "$polearms_+", 0),
		(overlay_set_display, "$polearms_add", 0),
		# archery buttons
		(overlay_set_display, "$archery_+", 0),
		(overlay_set_display, "$archery_add", 0),
		# crossbows buttons
		(overlay_set_display, "$crossbows_+", 0),
		(overlay_set_display, "$crossbows_add", 0),
		# throwing buttons
		(overlay_set_display, "$throwing_+", 0),
		(overlay_set_display, "$throwing_add", 0),
	(try_end),
	
	(try_begin), ### skill add buttons disappear if level is maxed ###
		# ironflesh buttons
		(eq,reg6,reg30),
		(overlay_set_display, "$ironflesh_+", 0),
		(overlay_set_display, "$ironflesh_add", 0),
	(try_end),
	(try_begin),
		# power strike buttons
		(eq,reg7,reg30),
		(overlay_set_display, "$power_strike_+", 0),
		(overlay_set_display, "$power_strike_add", 0),
	(try_end),
	(try_begin),
		# power throw buttons
		(eq,reg8,reg30),
		(overlay_set_display, "$power_throw_+", 0),
		(overlay_set_display, "$power_throw_add", 0),
	(try_end),
	(try_begin),
		# power draw buttons
		(eq,reg9,reg30),
		(overlay_set_display, "$power_draw_+", 0),
		(overlay_set_display, "$power_draw_add", 0),
	(try_end),
	(try_begin),
		# weapon master buttons
		(eq,reg10,reg31),
		(overlay_set_display, "$weapon_master_+", 0),
		(overlay_set_display, "$weapon_master_add", 0),
	(try_end),
	(try_begin),
		# shield buttons
		(eq,reg11,reg31),
		(overlay_set_display, "$shield_+", 0),
		(overlay_set_display, "$shield_add", 0),
	(try_end),
	(try_begin),
		# athletics buttons
		(eq,reg12,reg31),
		(overlay_set_display, "$athletics_+", 0),
		(overlay_set_display, "$athletics_add", 0),
	(try_end),
	(try_begin),
		# riding buttons
		(eq,reg13,reg31),
		(overlay_set_display, "$riding_+", 0),
		(overlay_set_display, "$riding_add", 0),
	(try_end),
	(try_begin),
		# horse archery buttons
		(eq,reg14,reg31),
		(overlay_set_display, "$horse_archery_+", 0),
		(overlay_set_display, "$horse_archery_add", 0),
	(try_end),
	(try_begin),
		# looting buttons
		(eq,reg15,reg31),
		(overlay_set_display, "$looting_+", 0),
		(overlay_set_display, "$looting_add", 0),
	(try_end),
	(try_begin),
		# trainer buttons
		(eq,reg16,reg32),
		(overlay_set_display, "$trainer_+", 0),
		(overlay_set_display, "$trainer_add", 0),
	(try_end),
	(try_begin),
		# tracking buttons
		(eq,reg17,reg32),
		(overlay_set_display, "$tracking_+", 0),
		(overlay_set_display, "$tracking_add", 0),
	(try_end),
	(try_begin),
		# tactics buttons
		(eq,reg18,reg32),
		(overlay_set_display, "$tactics_+", 0),
		(overlay_set_display, "$tactics_add", 0),
	(try_end),
	(try_begin),
		# path finding buttons
		(eq,reg19,reg32),
		(overlay_set_display, "$pathfinding_+", 0),
		(overlay_set_display, "$pathfinding_add", 0),
	(try_end),
	(try_begin),
		# spotting buttons
		(eq,reg20,reg32),
		(overlay_set_display, "$spotting_+", 0),
		(overlay_set_display, "$spotting_add", 0),
	(try_end),
	(try_begin),
		# inventory management buttons
		(eq,reg21,reg32),
		(overlay_set_display, "$inventory_management_+", 0),
		(overlay_set_display, "$inventory_management_add", 0),
	(try_end),
	(try_begin),
		# wound treatment buttons
		(eq,reg22,reg32),
		(overlay_set_display, "$wound_treatment_+", 0),
		(overlay_set_display, "$wound_treatment_add", 0),
	(try_end),
	(try_begin),
		# surgery buttons
		(eq,reg23,reg32),
		(overlay_set_display, "$surgery_+", 0),
		(overlay_set_display, "$surgery_add", 0),
	(try_end),
	(try_begin),
		# first aid buttons
		(eq,reg24,reg32),
		(overlay_set_display, "$first_aid_+", 0),
		(overlay_set_display, "$first_aid_add", 0),
	(try_end),
	(try_begin),
		# engineer buttons
		(eq,reg25,reg32),
		(overlay_set_display, "$engineer_+", 0),
		(overlay_set_display, "$engineer_add", 0),
	(try_end),
	(try_begin),
		# persuasion buttons
		(eq,reg26,reg32),
		(overlay_set_display, "$persuasion_+", 0),
		(overlay_set_display, "$persuasion_add", 0),
	(try_end),
	(try_begin),
		# prisoner management buttons
		(eq,reg27,reg33),
		(overlay_set_display, "$prisoner_management_+", 0),
		(overlay_set_display, "$prisoner_management_add", 0),
	(try_end),
	(try_begin),
		# leadership buttons
		(eq,reg28,reg33),
		(overlay_set_display, "$leadership_+", 0),
		(overlay_set_display, "$leadership_add", 0),
	(try_end),
	(try_begin),
		# trade buttons
		(eq,reg29,reg33),
		(overlay_set_display, "$trade_+", 0),
		(overlay_set_display, "$trade_add", 0),
	(try_end),
	
	### proficiency buttons disappear if maxed ###
	(try_begin), # one hand buttons
		(eq,reg35,reg41),
		(overlay_set_display, "$one_hand_+", 0),
		(overlay_set_display, "$one_hand_add", 0),
	(try_end),
	(try_begin), # two hand buttons
		(eq,reg36,reg41),
		(overlay_set_display, "$two_hand_+", 0),
		(overlay_set_display, "$two_hand_add", 0),
	(try_end),
	(try_begin), # polearms buttons
		(eq,reg37,reg41),
		(overlay_set_display, "$polearms_+", 0),
		(overlay_set_display, "$polearms_add", 0),
	(try_end),
	(try_begin), # archery buttons
		(eq,reg38,reg41),
		(overlay_set_display, "$archery_+", 0),
		(overlay_set_display, "$archery_add", 0),
	(try_end),
	(try_begin), # crossbows buttons
		(eq,reg39,reg41),
		(overlay_set_display, "$crossbows_+", 0),
		(overlay_set_display, "$crossbows_add", 0),
	(try_end),
	(try_begin), # throwing buttons
		(eq,reg40,reg41),
		(overlay_set_display, "$throwing_+", 0),
		(overlay_set_display, "$throwing_add", 0),
	(try_end),
    ]),
	 

	 
	 
	 
	(ti_on_presentation_mouse_enter_leave,
		[
			(store_trigger_param_1, ":object"),
			(store_trigger_param_2, ":enter_leave"),
			
			#############################
			######    attributes	#####
			
			(try_begin), ## strength description
				(this_or_next|eq, ":object", "$strength_add"),
				(eq, ":object", "$strength_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$strength_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$strength_add"),
				(eq, ":object", "$strength_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$strength_desc", 0),
			(else_try), ## agility description
				(this_or_next|eq, ":object", "$agility_add"),
				(eq, ":object", "$agility_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$agility_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$agility_add"),
				(eq, ":object", "$agility_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$agility_desc", 0),
			(else_try), ## intelligence description
				(this_or_next|eq, ":object", "$intelligence_add"),
				(eq, ":object", "$intelligence_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$intelligence_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$intelligence_add"),
				(eq, ":object", "$intelligence_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$intelligence_desc", 0),
			(else_try), ## charisma description
				(this_or_next|eq, ":object", "$charisma_add"),
				(eq, ":object", "$charisma_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$charisma_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$charisma_add"),
				(eq, ":object", "$charisma_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$charisma_desc", 0),
				
			#############################
			######     Skills		#####
			
			(else_try), ## ironflesh description
				(this_or_next|eq, ":object", "$ironflesh_add"),
				(eq, ":object", "$ironflesh_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$ironflesh_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$ironflesh_add"),
				(eq, ":object", "$ironflesh_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$ironflesh_desc", 0),
			(else_try), ## power strike description
				(this_or_next|eq, ":object", "$power_strike_add"),
				(eq, ":object", "$power_strike_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$power_strike_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$power_strike_add"),
				(eq, ":object", "$power_strike_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$power_strike_desc", 0),
			(else_try), ## power throw description
				(this_or_next|eq, ":object", "$power_throw_add"),
				(eq, ":object", "$power_throw_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$power_throw_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$power_throw_add"),
				(eq, ":object", "$power_throw_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$power_throw_desc", 0),
			(else_try), ## power draw description
				(this_or_next|eq, ":object", "$power_draw_add"),
				(eq, ":object", "$power_draw_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$power_draw_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$power_draw_add"),
				(eq, ":object", "$power_draw_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$power_draw_desc", 0),
			(else_try), ## weapon master description
				(this_or_next|eq, ":object", "$weapon_master_add"),
				(eq, ":object", "$weapon_master_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$weapon_master_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$weapon_master_add"),
				(eq, ":object", "$weapon_master_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$weapon_master_desc", 0),
			(else_try), ## shield description
				(this_or_next|eq, ":object", "$shield_add"),
				(eq, ":object", "$shield_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$shield_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$shield_add"),
				(eq, ":object", "$shield_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$shield_desc", 0),
			(else_try), ## athletics description
				(this_or_next|eq, ":object", "$athletics_add"),
				(eq, ":object", "$athletics_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$athletics_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$athletics_add"),
				(eq, ":object", "$athletics_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$athletics_desc", 0),
			(else_try), ## riding description
				(this_or_next|eq, ":object", "$riding_add"),
				(eq, ":object", "$riding_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$riding_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$riding_add"),
				(eq, ":object", "$riding_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$riding_desc", 0),
			(else_try), ## horse archery description
				(this_or_next|eq, ":object", "$horse_archery_add"),
				(eq, ":object", "$horse_archery_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$horse_archery_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$horse_archery_add"),
				(eq, ":object", "$horse_archery_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$horse_archery_desc", 0),
			(else_try), ## looting description
				(this_or_next|eq, ":object", "$looting_add"),
				(eq, ":object", "$looting_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$looting_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$looting_add"),
				(eq, ":object", "$looting_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$looting_desc", 0),
			(else_try), ## trainer description
				(this_or_next|eq, ":object", "$trainer_add"),
				(eq, ":object", "$trainer_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$trainer_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$trainer_add"),
				(eq, ":object", "$trainer_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$trainer_desc", 0),
			(else_try), ## tracking description
				(this_or_next|eq, ":object", "$tracking_add"),
				(eq, ":object", "$tracking_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$tracking_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$tracking_add"),
				(eq, ":object", "$tracking_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$tracking_desc", 0),
			(else_try), ## tactics description
				(this_or_next|eq, ":object", "$tactics_add"),
				(eq, ":object", "$tactics_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$tactics_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$tactics_add"),
				(eq, ":object", "$tactics_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$tactics_desc", 0),
			(else_try), ## path finding description
				(this_or_next|eq, ":object", "$pathfinding_add"),
				(eq, ":object", "$path_finding_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$path_finding_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$pathfinding_add"),
				(eq, ":object", "$path_finding_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$path_finding_desc", 0),
			(else_try), ## spotting description
				(this_or_next|eq, ":object", "$spotting_add"),
				(eq, ":object", "$spotting_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$spotting_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$spotting_add"),
				(eq, ":object", "$spotting_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$spotting_desc", 0),
			(else_try), ## inventory management description
				(this_or_next|eq, ":object", "$inventory_management_add"),
				(eq, ":object", "$inventory_management_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$inventory_management_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$inventory_management_add"),
				(eq, ":object", "$inventory_management_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$inventory_management_desc", 0),
			(else_try), ## wound treatment description
				(this_or_next|eq, ":object", "$wound_treatment_add"),
				(eq, ":object", "$wound_treatment_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$wound_treatment_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$wound_treatment_add"),
				(eq, ":object", "$wound_treatment_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$wound_treatment_desc", 0),
			(else_try), ## surgery description
				(this_or_next|eq, ":object", "$surgery_add"),
				(eq, ":object", "$surgery_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$surgery_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$surgery_add"),
				(eq, ":object", "$surgery_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$surgery_desc", 0),
			(else_try), ## first aid description
				(this_or_next|eq, ":object", "$first_aid_add"),
				(eq, ":object", "$first_aid_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$first_aid_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$first_aid_add"),
				(eq, ":object", "$first_aid_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$first_aid_desc", 0),
			(else_try), ## engineer description
				(this_or_next|eq, ":object", "$engineer_add"),
				(eq, ":object", "$engineer_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$engineer_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$engineer_add"),
				(eq, ":object", "$engineer_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$engineer_desc", 0),
			(else_try), ## persuasion description
				(this_or_next|eq, ":object", "$persuasion_add"),
				(eq, ":object", "$persuasion_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$persuasion_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$persuasion_add"),
				(eq, ":object", "$persuasion_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$persuasion_desc", 0),
			(else_try), ## prisoner management description
				(this_or_next|eq, ":object", "$prisoner_management_add"),
				(eq, ":object", "$prisoner_management_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$prisoner_management_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$prisoner_management_add"),
				(eq, ":object", "$prisoner_management_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$prisoner_management_desc", 0),
			(else_try), ## leadership description
				(this_or_next|eq, ":object", "$leadership_add"),
				(eq, ":object", "$leadership_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$leadership_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$leadership_add"),
				(eq, ":object", "$leadership_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$leadership_desc", 0),
			(else_try), ## trade description
				(this_or_next|eq, ":object", "$trade_add"),
				(eq, ":object", "$trade_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$trade_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$trade_add"),
				(eq, ":object", "$trade_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$trade_desc", 0),
				
			#############################
			######  proficiencies	#####
			(else_try), ## one handed description
				(this_or_next|eq, ":object", "$one_hand_add"),
				(eq, ":object", "$one_hand_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$one_handed_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$one_hand_add"),
				(eq, ":object", "$one_hand_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$one_handed_desc", 0),
			(else_try), ## two handed description
				(this_or_next|eq, ":object", "$two_hand_add"),
				(eq, ":object", "$two_hand_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$two_handed_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$two_hand_add"),
				(eq, ":object", "$two_hand_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$two_handed_desc", 0),
			(else_try), ## polearms description
				(this_or_next|eq, ":object", "$polearms_add"),
				(eq, ":object", "$polearms_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$polearms_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$polearms_add"),
				(eq, ":object", "$polearms_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$polearms_desc", 0),
			(else_try), ## archery description
				(this_or_next|eq, ":object", "$archery_add"),
				(eq, ":object", "$archery_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$archery_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$archery_add"),
				(eq, ":object", "$archery_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$archery_desc", 0),
			(else_try), ## crossbows description
				(this_or_next|eq, ":object", "$crossbows_add"),
				(eq, ":object", "$crossbows_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$crossbows_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$crossbows_add"),
				(eq, ":object", "$crossbows_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$crossbows_desc", 0),
			(else_try), ## throwing description
				(this_or_next|eq, ":object", "$throwing_add"),
				(eq, ":object", "$throwing_label"),
				(eq, ":enter_leave", 0),
				(overlay_set_display, "$throwing_desc", 1),
			(else_try),
				(this_or_next|eq, ":object", "$throwing_add"),
				(eq, ":object", "$throwing_label"),
				(eq, ":enter_leave", 1),
				(overlay_set_display, "$throwing_desc", 0),
			(try_end),
			
			### display skill note if level is maxed ###
			(try_begin), # ironflesh buttons
				(eq, ":object", "$ironflesh_label"),
				(eq, ":enter_leave", 0),
				(eq,reg6,reg30),
				(overlay_set_display, "$strength_note", 1),
			(else_try),
				(eq, ":object", "$ironflesh_label"),
				(eq, ":enter_leave", 1),
				(eq,reg6,reg30),
				(overlay_set_display, "$strength_note", 0),
			(else_try),# power strike buttons
				(eq, ":object", "$power_strike_label"),
				(eq, ":enter_leave", 0),
				(eq,reg7,reg30),
				(overlay_set_display, "$strength_note", 1),
			(else_try),
				(eq, ":object", "$power_strike_label"),
				(eq, ":enter_leave", 1),
				(eq,reg7,reg30),
				(overlay_set_display, "$strength_note", 0),
			(else_try),# power throw buttons
				(eq, ":object", "$power_throw_label"),
				(eq, ":enter_leave", 0),
				(eq,reg8,reg30),
				(overlay_set_display, "$strength_note", 1),
			(else_try),
				(eq, ":object", "$power_throw_label"),
				(eq, ":enter_leave", 1),
				(eq,reg8,reg30),
				(overlay_set_display, "$strength_note", 0),
			(else_try),# power draw buttons
				(eq, ":object", "$power_draw_label"),
				(eq, ":enter_leave", 0),
				(eq,reg9,reg30),
				(overlay_set_display, "$strength_note", 1),
			(else_try),
				(eq, ":object", "$power_draw_label"),
				(eq, ":enter_leave", 1),
				(eq,reg9,reg30),
				(overlay_set_display, "$strength_note", 0),
			(else_try),# weapon master buttons
				(eq, ":object", "$weapon_master_label"),
				(eq, ":enter_leave", 0),
				(eq,reg10,reg31),
				(overlay_set_display, "$agility_note", 1),
			(else_try),
				(eq, ":object", "$weapon_master_label"),
				(eq, ":enter_leave", 1),
				(eq,reg10,reg31),
				(overlay_set_display, "$agility_note", 0),
			(else_try),# shield buttons
				(eq, ":object", "$shield_label"),
				(eq, ":enter_leave", 0),
				(eq,reg11,reg31),
				(overlay_set_display, "$agility_note", 1),
			(else_try),
				(eq, ":object", "$shield_label"),
				(eq, ":enter_leave", 1),
				(eq,reg11,reg31),
				(overlay_set_display, "$agility_note", 0),
			(else_try),# athletics buttons
				(eq, ":object", "$athletics_label"),
				(eq, ":enter_leave", 0),
				(eq,reg12,reg31),
				(overlay_set_display, "$agility_note", 1),
			(else_try),
				(eq, ":object", "$athletics_label"),
				(eq, ":enter_leave", 1),
				(eq,reg12,reg31),
				(overlay_set_display, "$agility_note", 0),
			(else_try),# riding buttons
				(eq, ":object", "$riding_label"),
				(eq, ":enter_leave", 0),
				(eq,reg13,reg31),
				(overlay_set_display, "$agility_note", 1),
			(else_try),
				(eq, ":object", "$riding_label"),
				(eq, ":enter_leave", 1),
				(eq,reg13,reg31),
				(overlay_set_display, "$agility_note", 0),
			(else_try),# horse archery buttons
				(eq, ":object", "$horse_archery_label"),
				(eq, ":enter_leave", 0),
				(eq,reg14,reg31),
				(overlay_set_display, "$agility_note", 1),
			(else_try),
				(eq, ":object", "$horse_archery_label"),
				(eq, ":enter_leave", 1),
				(eq,reg14,reg31),
				(overlay_set_display, "$agility_note", 0),
			(else_try),# looting buttons
				(eq, ":object", "$looting_label"),
				(eq, ":enter_leave", 0),
				(eq,reg15,reg31),
				(overlay_set_display, "$agility_note", 1),
			(else_try),
				(eq, ":object", "$looting_label"),
				(eq, ":enter_leave", 1),
				(eq,reg15,reg31),
				(overlay_set_display, "$agility_note", 0),
			(else_try),# trainer buttons
				(eq, ":object", "$trainer_label"),
				(eq, ":enter_leave", 0),
				(eq,reg16,reg32),
				(overlay_set_display, "$intelligence_note", 1),
			(else_try),
				(eq, ":object", "$trainer_label"),
				(eq, ":enter_leave", 1),
				(eq,reg16,reg32),
				(overlay_set_display, "$intelligence_note", 0),
			(else_try),# tracking buttons
				(eq, ":object", "$tracking_label"),
				(eq, ":enter_leave", 0),
				(eq,reg17,reg32),
				(overlay_set_display, "$intelligence_note", 1),
			(else_try),
				(eq, ":object", "$tracking_label"),
				(eq, ":enter_leave", 1),
				(eq,reg17,reg32),
				(overlay_set_display, "$intelligence_note", 0),
			(else_try),# tactics buttons
				(eq, ":object", "$tactics_label"),
				(eq, ":enter_leave", 0),
				(eq,reg18,reg32),
				(overlay_set_display, "$intelligence_note", 1),
			(else_try),
				(eq, ":object", "$tactics_label"),
				(eq, ":enter_leave", 1),
				(eq,reg18,reg32),
				(overlay_set_display, "$intelligence_note", 0),
			(else_try),# path finding buttons
				(eq, ":object", "$path_finding_label"),
				(eq, ":enter_leave", 0),
				(eq,reg19,reg32),
				(overlay_set_display, "$intelligence_note", 1),
			(else_try),
				(eq, ":object", "$path_finding_label"),
				(eq, ":enter_leave", 1),
				(eq,reg19,reg32),
				(overlay_set_display, "$intelligence_note", 0),
			(else_try),# spotting buttons
				(eq, ":object", "$spotting_label"),
				(eq, ":enter_leave", 0),
				(eq,reg20,reg32),
				(overlay_set_display, "$intelligence_note", 1),
			(else_try),
				(eq, ":object", "$spotting_label"),
				(eq, ":enter_leave", 1),
				(eq,reg20,reg32),
				(overlay_set_display, "$intelligence_note", 0),
			(else_try),# inventory management buttons
				(eq, ":object", "$inventory_management_label"),
				(eq, ":enter_leave", 0),
				(eq,reg21,reg32),
				(overlay_set_display, "$intelligence_note", 1),
			(else_try),
				(eq, ":object", "$inventory_management_label"),
				(eq, ":enter_leave", 1),
				(eq,reg21,reg32),
				(overlay_set_display, "$intelligence_note", 0),
			(else_try),# wound treatment buttons
				(eq, ":object", "$wound_treatment_label"),
				(eq, ":enter_leave", 0),
				(eq,reg22,reg32),
				(overlay_set_display, "$intelligence_note", 1),
			(else_try),
				(eq, ":object", "$wound_treatment_label"),
				(eq, ":enter_leave", 1),
				(eq,reg22,reg32),
				(overlay_set_display, "$intelligence_note", 0),
			(else_try),# surgery buttons
				(eq, ":object", "$surgery_label"),
				(eq, ":enter_leave", 0),
				(eq,reg23,reg32),
				(overlay_set_display, "$intelligence_note", 1),
			(else_try),
				(eq, ":object", "$surgery_label"),
				(eq, ":enter_leave", 1),
				(eq,reg23,reg32),
				(overlay_set_display, "$intelligence_note", 0),
			(else_try),# first aid buttons
				(eq, ":object", "$first_aid_label"),
				(eq, ":enter_leave", 0),
				(eq,reg24,reg32),
				(overlay_set_display, "$intelligence_note", 1),
			(else_try),
				(eq, ":object", "$first_aid_label"),
				(eq, ":enter_leave", 1),
				(eq,reg24,reg32),
				(overlay_set_display, "$intelligence_note", 0),
			(else_try),# engineer buttons
				(eq, ":object", "$engineer_label"),
				(eq, ":enter_leave", 0),
				(eq,reg25,reg32),
				(overlay_set_display, "$intelligence_note", 1),
			(else_try),
				(eq, ":object", "$engineer_label"),
				(eq, ":enter_leave", 1),
				(eq,reg25,reg32),
				(overlay_set_display, "$intelligence_note", 0),
			(else_try),# persuasion buttons
				(eq, ":object", "$persuasion_label"),
				(eq, ":enter_leave", 0),
				(eq,reg26,reg32),
				(overlay_set_display, "$intelligence_note", 1),
			(else_try),
				(eq, ":object", "$persuasion_label"),
				(eq, ":enter_leave", 1),
				(eq,reg26,reg32),
				(overlay_set_display, "$intelligence_note", 0),
			(else_try),# prisoner management buttons
				(eq, ":object", "$prisoner_management_label"),
				(eq, ":enter_leave", 0),
				(eq,reg27,reg33),
				(overlay_set_display, "$charisma_note", 1),
			(else_try),
				(eq, ":object", "$prisoner_management_label"),
				(eq, ":enter_leave", 1),
				(eq,reg27,reg33),
				(overlay_set_display, "$charisma_note", 0),
			(else_try),# leadership buttons
				(eq, ":object", "$leadership_label"),
				(eq, ":enter_leave", 0),
				(eq,reg28,reg33),
				(overlay_set_display, "$charisma_note", 1),
			(else_try),
				(eq, ":object", "$leadership_label"),
				(eq, ":enter_leave", 1),
				(eq,reg28,reg33),
				(overlay_set_display, "$charisma_note", 0),
			(else_try),# trade buttons
				(eq, ":object", "$trade_label"),
				(eq, ":enter_leave", 0),
				(eq,reg29,reg33),
				(overlay_set_display, "$charisma_note", 1),
			(else_try),
				(eq, ":object", "$trade_label"),
				(eq, ":enter_leave", 1),
				(eq,reg29,reg33),
				(overlay_set_display, "$charisma_note", 0),
			(try_end),
			
		]),



		
   (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
		
		(try_begin), ####### DONE BUTTON #######
			(eq, ":object", "$done_button"),
			
			#Attributes
			# first, clear previous levels
			(troop_raise_attribute, "$g_talk_troop", ca_strength, -63),
			(troop_raise_attribute, "$g_talk_troop", ca_agility, -63),
			(troop_raise_attribute, "$g_talk_troop", ca_intelligence, -63),
			(troop_raise_attribute, "$g_talk_troop", ca_charisma, -63),
			# then, add to relfect what was changed
			(troop_raise_attribute, "$g_talk_troop", ca_strength, reg1),
			(troop_raise_attribute, "$g_talk_troop", ca_agility, reg2),
			(troop_raise_attribute, "$g_talk_troop", ca_intelligence, reg3),
			(troop_raise_attribute, "$g_talk_troop", ca_charisma, reg4),
			#Skills
			# first, clear previous levels
			(troop_raise_skill,"$g_talk_troop",skl_ironflesh,-10),
			(troop_raise_skill,"$g_talk_troop",skl_power_strike,-10),
			(troop_raise_skill,"$g_talk_troop",skl_power_throw,-10),
			(troop_raise_skill,"$g_talk_troop",skl_power_draw,-10),
			(troop_raise_skill,"$g_talk_troop",skl_weapon_master,-10),
			(troop_raise_skill,"$g_talk_troop",skl_shield,-10),
			(troop_raise_skill,"$g_talk_troop",skl_athletics,-10),
			(troop_raise_skill,"$g_talk_troop",skl_riding,-10),
			(troop_raise_skill,"$g_talk_troop",skl_horse_archery,-10),
			(troop_raise_skill,"$g_talk_troop",skl_looting,-10),
			(troop_raise_skill,"$g_talk_troop",skl_trainer,-10),
			(troop_raise_skill,"$g_talk_troop",skl_tracking,-10),
			(troop_raise_skill,"$g_talk_troop",skl_tactics,-10),
			(troop_raise_skill,"$g_talk_troop",skl_pathfinding,-10),
			(troop_raise_skill,"$g_talk_troop",skl_spotting,-10),
			(troop_raise_skill,"$g_talk_troop",skl_inventory_management,-10),
			(troop_raise_skill,"$g_talk_troop",skl_wound_treatment,-10),
			(troop_raise_skill,"$g_talk_troop",skl_surgery,-10),
			(troop_raise_skill,"$g_talk_troop",skl_first_aid,-10),
			(troop_raise_skill,"$g_talk_troop",skl_engineer,-10),
			(troop_raise_skill,"$g_talk_troop",skl_persuasion,-10),
			(troop_raise_skill,"$g_talk_troop",skl_prisoner_management,-10),
			(troop_raise_skill,"$g_talk_troop",skl_leadership,-10),
			(troop_raise_skill,"$g_talk_troop",skl_trade,-10),
			# then, add to reflect what was changed
			(troop_raise_skill,"$g_talk_troop",skl_ironflesh,reg6),
			(troop_raise_skill,"$g_talk_troop",skl_power_strike,reg7),
			(troop_raise_skill,"$g_talk_troop",skl_power_throw,reg8),
			(troop_raise_skill,"$g_talk_troop",skl_power_draw,reg9),
			(troop_raise_skill,"$g_talk_troop",skl_weapon_master,reg10),
			(troop_raise_skill,"$g_talk_troop",skl_shield,reg11),
			(troop_raise_skill,"$g_talk_troop",skl_athletics,reg12),
			(troop_raise_skill,"$g_talk_troop",skl_riding,reg13),
			(troop_raise_skill,"$g_talk_troop",skl_horse_archery,reg14),
			(troop_raise_skill,"$g_talk_troop",skl_looting,reg15),
			(troop_raise_skill,"$g_talk_troop",skl_trainer,reg16),
			(troop_raise_skill,"$g_talk_troop",skl_tracking,reg17),
			(troop_raise_skill,"$g_talk_troop",skl_tactics,reg18),
			(troop_raise_skill,"$g_talk_troop",skl_pathfinding,reg19),
			(troop_raise_skill,"$g_talk_troop",skl_spotting,reg20),
			(troop_raise_skill,"$g_talk_troop",skl_inventory_management,reg21),
			(troop_raise_skill,"$g_talk_troop",skl_wound_treatment,reg22),
			(troop_raise_skill,"$g_talk_troop",skl_surgery,reg23),
			(troop_raise_skill,"$g_talk_troop",skl_first_aid,reg24),
			(troop_raise_skill,"$g_talk_troop",skl_engineer,reg25),
			(troop_raise_skill,"$g_talk_troop",skl_persuasion,reg26),
			(troop_raise_skill,"$g_talk_troop",skl_prisoner_management,reg27),
			(troop_raise_skill,"$g_talk_troop",skl_leadership,reg28),
			(troop_raise_skill,"$g_talk_troop",skl_trade,reg29),
			#proficiencies
			# first, clear previous levels
			(troop_raise_proficiency_linear, "$g_talk_troop",wpt_one_handed_weapon, -1023),
			(troop_raise_proficiency_linear, "$g_talk_troop",wpt_two_handed_weapon, -1023),
			(troop_raise_proficiency_linear, "$g_talk_troop",wpt_polearm, -1023),
			(troop_raise_proficiency_linear, "$g_talk_troop",wpt_archery, -1023),
			(troop_raise_proficiency_linear, "$g_talk_troop",wpt_crossbow, -1023),
			(troop_raise_proficiency_linear, "$g_talk_troop",wpt_throwing, -1023),
			# then, add to reflect changes
			(troop_raise_proficiency_linear, "$g_talk_troop",wpt_one_handed_weapon,reg35),
			(troop_raise_proficiency_linear, "$g_talk_troop",wpt_two_handed_weapon,reg36),
			(troop_raise_proficiency_linear, "$g_talk_troop",wpt_polearm,reg37),
			(troop_raise_proficiency_linear, "$g_talk_troop",wpt_archery,reg38),
			(troop_raise_proficiency_linear, "$g_talk_troop",wpt_crossbow,reg39),
			(troop_raise_proficiency_linear, "$g_talk_troop",wpt_throwing,reg40),
			
			(try_begin), #route to menu, for better behavior
				(presentation_set_duration, 0),
				(jump_to_menu, "mnu_c3_finalize"),
			(try_end),
			
		(else_try), ####### back #######
			(eq, ":object", "$back_button"),
			(assign, "$quit_status", 1),
			(jump_to_menu, "mnu_start_game_0"),
			(presentation_set_duration, 0),			
			
		(else_try), ####### gender #######
			(eq, ":object", "$c3_presentation_gender"),
			(assign, "$character_gender", ":value"),
			(start_presentation, "prsnt_custom_character_creation"),
			(assign, "$c3_presentation_gender", ":value"),
			
		(else_try), ####### status #######
			(eq, ":object", "$c3_presentation_status"),
			(assign, "$c3_status", ":value"),
			(start_presentation, "prsnt_custom_character_creation"),
			(assign, "$c3_presentation_status", ":value"),
			
			
		(else_try), ####### start option #######
			(eq, ":object", "$c3_start_option"),
			(assign, "$c3_start", ":value"),
			(start_presentation, "prsnt_custom_character_creation"),
			(assign, "$c3_start_option", ":value"),
			
		####################################################
		####              Attributes					####
		####################################################
			
		(else_try), ####### strength #######
			(eq, ":object", "$strength_add"),
			(gt,reg0,0),(lt,reg1,63),(val_sub,reg0,1),(val_add,reg1,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### agility #######
			(eq, ":object", "$agility_add"),
			(gt,reg0,0),(lt,reg2,63),(val_sub,reg0,1),(val_add,reg2,1),(val_add,reg34,5), #last one adds +5 to wp's
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### intelligence #######
			(eq, ":object", "$intelligence_add"),
			(gt,reg0,0),(lt,reg3,63),(val_sub,reg0,1),(val_add,reg3,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### charisma #######
			(eq, ":object", "$charisma_add"),
			(gt,reg0,0),(lt,reg4,63),(val_sub,reg0,1),(val_add,reg4,1),
			(start_presentation, "prsnt_custom_character_creation"),		
			
		####################################################
		####              Skills						####
		####################################################
			
		(else_try), ####### ironflesh #######
			(eq, ":object", "$ironflesh_add"),
			(gt,reg5,0),(lt,reg6,reg30),(lt,reg6,10),(val_sub,reg5,1),(val_add,reg6,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### power strike #######
			(eq, ":object", "$power_strike_add"),
			(gt,reg5,0),(lt,reg7,reg30),(lt,reg7,10),(val_sub,reg5,1),(val_add,reg7,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### power throw #######
			(eq, ":object", "$power_throw_add"),
			(gt,reg5,0),(lt,reg8,reg30),(lt,reg8,10),(val_sub,reg5,1),(val_add,reg8,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### power draw #######
			(eq, ":object", "$power_draw_add"),
			(gt,reg5,0),(lt,reg9,reg30),(lt,reg9,10),(val_sub,reg5,1),(val_add,reg9,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### Weapon Master #######
			(eq, ":object", "$weapon_master_add"),
			(gt,reg5,0),(lt,reg10,reg31),(lt,reg10,10),(val_sub,reg5,1),(val_add,reg10,1),(val_add,reg41,40),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### shield #######
			(eq, ":object", "$shield_add"),
			(gt,reg5,0),(lt,reg11,reg31),(lt,reg11,10),(val_sub,reg5,1),(val_add,reg11,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### athletics #######
			(eq, ":object", "$athletics_add"),
			(gt,reg5,0),(lt,reg12,reg31),(lt,reg12,10),(val_sub,reg5,1),(val_add,reg12,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### riding #######
			(eq, ":object", "$riding_add"),
			(gt,reg5,0),(lt,reg13,reg31),(lt,reg13,10),(val_sub,reg5,1),(val_add,reg13,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### horse archery #######
			(eq, ":object", "$horse_archery_add"),
			(gt,reg5,0),(lt,reg14,reg31),(lt,reg14,10),(val_sub,reg5,1),(val_add,reg14,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### looting #######
			(eq, ":object", "$looting_add"),
			(gt,reg5,0),(lt,reg15,reg31),(lt,reg15,10),(val_sub,reg5,1),(val_add,reg15,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### trainer #######
			(eq, ":object", "$trainer_add"),
			(gt,reg5,0),(lt,reg16,reg32),(lt,reg16,10),(val_sub,reg5,1),(val_add,reg16,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### tracking #######
			(eq, ":object", "$tracking_add"),
			(gt,reg5,0),(lt,reg17,reg32),(lt,reg17,10),(val_sub,reg5,1),(val_add,reg17,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### tactics #######
			(eq, ":object", "$tactics_add"),
			(gt,reg5,0),(lt,reg18,reg32),(lt,reg18,10),(val_sub,reg5,1),(val_add,reg18,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### pathfinding #######
			(eq, ":object", "$pathfinding_add"),
			(gt,reg5,0),(lt,reg19,reg32),(lt,reg19,10),(val_sub,reg5,1),(val_add,reg19,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### spotting #######
			(eq, ":object", "$spotting_add"),
			(gt,reg5,0),(lt,reg20,reg32),(lt,reg20,10),(val_sub,reg5,1),(val_add,reg20,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### inventory management #######
			(eq, ":object", "$inventory_management_add"),
			(gt,reg5,0),(lt,reg21,reg32),(lt,reg21,10),(val_sub,reg5,1),(val_add,reg21,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### wound treatment #######
			(eq, ":object", "$wound_treatment_add"),
			(gt,reg5,0),(lt,reg22,reg32),(lt,reg22,10),(val_sub,reg5,1),(val_add,reg22,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### surgery #######
			(eq, ":object", "$surgery_add"),
			(gt,reg5,0),(lt,reg23,reg32),(lt,reg23,10),(val_sub,reg5,1),(val_add,reg23,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### first aid #######
			(eq, ":object", "$first_aid_add"),
			(gt,reg5,0),(lt,reg24,reg32),(lt,reg24,10),(val_sub,reg5,1),(val_add,reg24,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### engineer #######
			(eq, ":object", "$engineer_add"),
			(gt,reg5,0),(lt,reg25,reg32),(lt,reg25,10),(val_sub,reg5,1),(val_add,reg25,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### persuasion #######
			(eq, ":object", "$persuasion_add"),
			(gt,reg5,0),(lt,reg26,reg32),(lt,reg26,10),(val_sub,reg5,1),(val_add,reg26,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### prisoner management #######
			(eq, ":object", "$prisoner_management_add"),
			(gt,reg5,0),(lt,reg27,reg33),(lt,reg27,10),(val_sub,reg5,1),(val_add,reg27,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### leadership #######
			(eq, ":object", "$leadership_add"),
			(gt,reg5,0),(lt,reg28,reg33),(lt,reg28,10),(val_sub,reg5,1),(val_add,reg28,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### trade #######
			(eq, ":object", "$trade_add"),
			(gt,reg5,0),(lt,reg29,reg33),(lt,reg29,10),(val_sub,reg5,1),(val_add,reg29,1),
			(start_presentation, "prsnt_custom_character_creation"),
			
		####################################################
		####             Proficiencies					####
		####################################################
			
		(else_try), ####### one handed weapons #######
			(eq, ":object", "$one_hand_add"),
			(gt,reg34,0),(lt,reg35,reg41),(call_script,"script_c3_increase_proficiency",reg35),(assign,reg35,reg58),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### two handed weapons #######
			(eq, ":object", "$two_hand_add"),
			(gt,reg34,0),(lt,reg36,reg41),(call_script,"script_c3_increase_proficiency",reg36),(assign,reg36,reg58),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### polearms #######
			(eq, ":object", "$polearms_add"),
			(gt,reg34,0),(lt,reg37,reg41),(call_script,"script_c3_increase_proficiency",reg37),(assign,reg37,reg58),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### archery #######
			(eq, ":object", "$archery_add"),
			(gt,reg34,0),(lt,reg38,reg41),(call_script,"script_c3_increase_proficiency",reg38),(assign, reg38,reg58),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### crossbows #######
			(eq, ":object", "$crossbows_add"),
			(gt,reg34,0),(lt,reg39,reg41),(call_script,"script_c3_increase_proficiency",reg39),(assign,reg39,reg58),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### throwing #######
			(eq, ":object", "$throwing_add"),
			(gt,reg34,0),(lt,reg40,reg41),(call_script,"script_c3_increase_proficiency",reg40),(assign,reg40,reg58),
			(start_presentation, "prsnt_custom_character_creation"),
			
		(else_try), ####### reset button #######
			(eq, ":object", "$reset_button"),
			#attributes
			(try_begin),(gt,reg1,reg46),(val_sub,reg1,reg46),(val_add,reg0,reg1),(assign,reg1,reg46),(try_end),
			(try_begin),(gt,reg2,reg46),(val_sub,reg2,reg46),(val_add,reg0,reg2),(val_mul,reg2,5),(val_sub,reg34,reg2),(assign,reg2,reg46),(try_end),
			(try_begin),(gt,reg3,reg46),(val_sub,reg3,reg46),(val_add,reg0,reg3),(assign,reg3,reg46),(try_end),
			(try_begin),(gt,reg4,reg46),(val_sub,reg4,reg46),(val_add,reg0,reg4),(assign,reg4,reg46),(try_end),
			#skills
			(try_begin),(gt,reg6,0),(val_add,reg5,reg6),(assign,reg6,0),(try_end),
			(try_begin),(gt,reg7,0),(val_add,reg5,reg7),(assign,reg7,0),(try_end),
			(try_begin),(gt,reg8,0),(val_add,reg5,reg8),(assign,reg8,0),(try_end),
			(try_begin),(gt,reg9,0),(val_add,reg5,reg9),(assign,reg9,0),(try_end),
			(try_begin),(gt,reg10,0),(val_add,reg5,reg10),(val_mul,reg10,40),(val_sub,reg41,reg10),(assign,reg10,0),(try_end),
			(try_begin),(gt,reg11,0),(val_add,reg5,reg11),(assign,reg11,0),(try_end),
			(try_begin),(gt,reg12,0),(val_add,reg5,reg12),(assign,reg12,0),(try_end),
			(try_begin),(gt,reg13,0),(val_add,reg5,reg13),(assign,reg13,0),(try_end),
			(try_begin),(gt,reg14,0),(val_add,reg5,reg14),(assign,reg14,0),(try_end),
			(try_begin),(gt,reg15,0),(val_add,reg5,reg15),(assign,reg15,0),(try_end),
			(try_begin),(gt,reg16,0),(val_add,reg5,reg16),(assign,reg16,0),(try_end),
			(try_begin),(gt,reg17,0),(val_add,reg5,reg17),(assign,reg17,0),(try_end),
			(try_begin),(gt,reg18,0),(val_add,reg5,reg18),(assign,reg18,0),(try_end),
			(try_begin),(gt,reg19,0),(val_add,reg5,reg19),(assign,reg19,0),(try_end),
			(try_begin),(gt,reg20,0),(val_add,reg5,reg20),(assign,reg20,0),(try_end),
			(try_begin),(gt,reg21,0),(val_add,reg5,reg21),(assign,reg21,0),(try_end),
			(try_begin),(gt,reg22,0),(val_add,reg5,reg22),(assign,reg22,0),(try_end),
			(try_begin),(gt,reg23,0),(val_add,reg5,reg23),(assign,reg23,0),(try_end),
			(try_begin),(gt,reg24,0),(val_add,reg5,reg24),(assign,reg24,0),(try_end),
			(try_begin),(gt,reg25,0),(val_add,reg5,reg25),(assign,reg25,0),(try_end),
			(try_begin),(gt,reg26,0),(val_add,reg5,reg26),(assign,reg26,0),(try_end),
			(try_begin),(gt,reg27,0),(val_add,reg5,reg27),(assign,reg27,0),(try_end),
			(try_begin),(gt,reg28,0),(val_add,reg5,reg28),(assign,reg28,0),(try_end),
			(try_begin),(gt,reg29,0),(val_add,reg5,reg29),(assign,reg29,0),(try_end),
			#proficiencies
			(try_begin),(call_script, "script_c3_reset_profiency", reg35), (val_add, reg34, reg60), (assign, reg35, reg61), (try_end),
			(try_begin),(call_script, "script_c3_reset_profiency", reg36), (val_add, reg34, reg60), (assign, reg36, reg61), (try_end),
			(try_begin),(call_script, "script_c3_reset_profiency", reg37), (val_add, reg34, reg60), (assign, reg37, reg61), (try_end),
			(try_begin),(call_script, "script_c3_reset_profiency", reg38), (val_add, reg34, reg60), (assign, reg38, reg61), (try_end),
			(try_begin),(call_script, "script_c3_reset_profiency", reg39), (val_add, reg34, reg60), (assign, reg39, reg61), (try_end),
			(try_begin),(call_script, "script_c3_reset_profiency", reg40), (val_add, reg34, reg60), (assign, reg40, reg61), (try_end),
			
			(start_presentation, "prsnt_custom_character_creation"),
		(try_end),
      ]),
	]),
	
	("c3_kingdom_finalize",0,mesh_load_window,
		[
			(ti_on_presentation_load,
				[	
					(presentation_set_duration, 999999),
					(set_fixed_point_multiplier, 1000),
					
					#assign Lezalit as minister
					(assign,"$g_player_minister","trp_npc14"),
					(troop_set_faction,"trp_npc14","fac_player_supporters_faction"),
					(str_store_troop_name,s10,"$g_player_minister"),
					
					#find players court
					(try_for_range,":town",towns_begin,towns_end),
						(store_faction_of_party,":town_faction",":town"),
						(eq,":town_faction","fac_player_supporters_faction"),
						(eq,":town","$g_player_court"),
						(assign,"$g_player_court",":town"),
						(str_store_party_name,s12,":town"),
					(try_end),
					
					#king intro
					(create_text_overlay, reg1, "@As king, your first priority should be to establish a right to rule by marrying into a high-born family, recruiting new lords, governing your lands, treating with other kings, or dispatching your companions on missions. {s10}, your minister, can be found at your court in {s12}. Consult often, to avoid accumulating unresolved issues.", tf_center_justify),
					(position_set_x, pos1, 500),
					(position_set_y, pos1, 550),
					(overlay_set_position, reg1, pos1),
					
					#banner display right
					(create_mesh_overlay_with_tableau_material, reg1, -1, "tableau_faction_note_mesh_banner","fac_player_supporters_faction"),
					(position_set_x,pos1,690),
					(position_set_y,pos1,150),
					(overlay_set_position, reg1, pos1),
					(position_set_x, pos1, 1300),
					(position_set_y, pos1, 2000),
					(overlay_set_size, reg1, pos1),
					
					#banner display left
					(create_mesh_overlay_with_tableau_material, reg1, -1, "tableau_faction_note_mesh_banner","fac_player_supporters_faction"),
					(position_set_x,pos1,50),
					(position_set_y,pos1,150),
					(overlay_set_position, reg1, pos1),
					(position_set_x, pos1, 1300),
					(position_set_y, pos1, 2000),
					(overlay_set_size, reg1, pos1),
				
					#kingdom name
					(create_text_overlay, reg1, "@Name your kingdom", tf_center_justify),
					(position_set_x, pos1, 500),
					(position_set_y, pos1, 450),
					(overlay_set_position, reg1, pos1),
					(position_set_x, pos1, 1200),
					(position_set_y, pos1, 1200),
					(overlay_set_size, reg1, pos1),
					
					#kingdom name input
					(create_simple_text_box_overlay, "$g_presentation_obj_name_kingdom_1"),
					(position_set_x, pos1, 400),
					(position_set_y, pos1, 420),
					(overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),
				
					#stores faction name from either the input or from player name if no input
					(try_begin),
					  (eq, "$players_kingdom_name_set", 1),
					  (str_store_faction_name, s7, "fac_player_supporters_faction"),
					  (overlay_set_text, "$g_presentation_obj_name_kingdom_1", s7),
					(else_try),
					  (str_store_troop_name, s0, "trp_player"),
					  (overlay_set_text, "$g_presentation_obj_name_kingdom_1", "str_default_kingdom_name"),
					  (str_store_string, s7, "str_default_kingdom_name"),
					(try_end),
					
					#exit button
					(create_button_overlay, "$g_presentation_obj_name_kingdom_2", "@Continue...", tf_center_justify),
					(position_set_x, pos1, 500),
					(position_set_y, pos1, 300),
					(overlay_set_position, "$g_presentation_obj_name_kingdom_2", pos1),
				]
			),
		
			(ti_on_presentation_event_state_change,
				[
					(store_trigger_param_1, ":object"),
					
					(try_begin), 
						(eq, ":object", "$g_presentation_obj_name_kingdom_1"),
						(str_store_string, s7, s0),
					(else_try),
						(eq, ":object", "$g_presentation_obj_name_kingdom_2"),
						(faction_set_name, "fac_player_supporters_faction", s7),
						(faction_set_color, "fac_player_supporters_faction", 0xFF0000),
						(assign, "$players_kingdom_name_set", 1),
						(presentation_set_duration, 0),
						(jump_to_menu, "mnu_auto_return"),
					(try_end),
				]
			),
		]
	),
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