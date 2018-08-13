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
  
  ("mcc_character_creation", 0, 0, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
        
        (create_mesh_overlay, reg1, "mesh_load_window"),
        (position_set_x, pos1, 0),
        (position_set_y, pos1, 0),
        (overlay_set_position, reg1, pos1),
		
		## Done button
		(create_game_button_overlay, "$g_presentation_obj_1", "@Done"),
        (position_set_x, pos1, 875),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
		
		## Back button
		(create_game_button_overlay, "$g_presentation_obj_2", "@Back"),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
		
		## Default button
		(create_game_button_overlay, "$g_presentation_obj_3", "@Default"),
        (position_set_x, pos1, 125),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
		
		## title
        (create_text_overlay, reg1, "@Character Creation", tf_center_justify),
        (position_set_x, pos1, 1500),
        (position_set_y, pos1, 1500),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 690),
        (overlay_set_position, reg1, pos1),
		
		
		## background
        (create_text_overlay, reg1, "@Background:", tf_center_justify),
        (position_set_x, pos1, 1200),
        (position_set_y, pos1, 1200),
        (overlay_set_size, reg1, pos1),
		(position_set_x, pos1, 150),
        (position_set_y, pos1, 660),
        (overlay_set_position, reg1, pos1),
		
        (create_text_overlay, reg1, "@I am a...", tf_center_justify),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
		(position_set_x, pos1, 150),
        (position_set_y, pos1, 620),
        (overlay_set_position, reg1, pos1),
		
        (create_combo_button_overlay, "$g_presentation_obj_gender", tf_center_justify),
		(position_set_x, pos1, 175),
		(position_set_y, pos1, 590),
        (overlay_set_position, "$g_presentation_obj_gender", pos1),
		(position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_gender", pos1),
        (overlay_add_item, "$g_presentation_obj_gender", "@Man"),
		(overlay_add_item, "$g_presentation_obj_gender", "@Woman"),
        (overlay_set_val, "$g_presentation_obj_gender", "$character_gender"),
   

		
		(create_text_overlay, reg1, "@My father was...", tf_center_justify),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
		(position_set_x, pos1, 150),
        (position_set_y, pos1, 550),
        (overlay_set_position, reg1, pos1),
		
		(position_set_x, pos1, 175),
		(position_set_y, pos1, 520),
        (create_combo_button_overlay, "$g_presentation_obj_father"),
        (overlay_set_position, "$g_presentation_obj_father", pos1),
		(position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_father", pos1),
        (overlay_add_item, "$g_presentation_obj_father", "@a priest"),
        (overlay_add_item, "$g_presentation_obj_father", "@a thief"),
        (overlay_add_item, "$g_presentation_obj_father", "@a steppe nomad"),
        (overlay_add_item, "$g_presentation_obj_father", "@a hunter"),
        (overlay_add_item, "$g_presentation_obj_father", "@a veteran warrior"),
        (overlay_add_item, "$g_presentation_obj_father", "@a travelling merchant"),
        (overlay_add_item, "$g_presentation_obj_father", "@an impoverished noble"),
		(overlay_set_val, "$g_presentation_obj_father", "$background_type"),
		
		(create_text_overlay, reg1, "@Growing up I was...", tf_center_justify),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
		(position_set_x, pos1, 150),
        (position_set_y, pos1, 480),
        (overlay_set_position, reg1, pos1),
		
		(position_set_x, pos1, 175),
		(position_set_y, pos1, 450),
        (create_combo_button_overlay, "$g_presentation_obj_early"),
        (overlay_set_position, "$g_presentation_obj_early", pos1),
		(position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_early", pos1),
        (overlay_add_item, "$g_presentation_obj_early", "@an acolyte"),
        (overlay_add_item, "$g_presentation_obj_early", "@a noble in training"),
        (overlay_add_item, "$g_presentation_obj_early", "@a courtier"),
        (overlay_add_item, "$g_presentation_obj_early", "@a mummer"),
        (overlay_add_item, "$g_presentation_obj_early", "@a shop assistant"),
        (overlay_add_item, "$g_presentation_obj_early", "@a steppe child"),
        (overlay_add_item, "$g_presentation_obj_early", "@a street urchin"),
        (overlay_add_item, "$g_presentation_obj_early", "@a craftsman's apprentice"),
        (overlay_add_item, "$g_presentation_obj_early", "@a page at a nobleman's court"),
		(overlay_set_val, "$g_presentation_obj_early", "$background_answer_2"),
		
		(create_text_overlay, reg1, "@As an adult, I became...", tf_center_justify),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
		(position_set_x, pos1, 150),
        (position_set_y, pos1, 410),
        (overlay_set_position, reg1, pos1),
		
		(position_set_x, pos1, 175),
		(position_set_y, pos1, 380),
        (create_combo_button_overlay, "$g_presentation_obj_adult"),
        (overlay_set_position, "$g_presentation_obj_adult", pos1),
		(position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_adult", pos1),
        (try_begin),
          (eq,"$character_gender", tf_male),
          (overlay_add_item, "$g_presentation_obj_adult", "@a squire"),
        (else_try),
          (eq,"$character_gender", tf_female),
          (overlay_add_item, "$g_presentation_obj_adult", "@a lady-in-waiting"),
        (try_end),
		(overlay_add_item, "$g_presentation_obj_adult", "@a university student"),
		(overlay_add_item, "$g_presentation_obj_adult", "@a troubadour"),
		(overlay_add_item, "$g_presentation_obj_adult", "@a preacher"),
		(overlay_add_item, "$g_presentation_obj_adult", "@a goods peddler"),
        (overlay_add_item, "$g_presentation_obj_adult", "@a smith"),
        (overlay_add_item, "$g_presentation_obj_adult", "@a game poacher"),
        (overlay_add_item, "$g_presentation_obj_adult", "@a mercenary"),
		(overlay_add_item, "$g_presentation_obj_adult", "@a bravo"),
		(overlay_add_item, "$g_presentation_obj_adult", "@a thief"),
		(overlay_add_item, "$g_presentation_obj_adult", "@a gladiator"),
		(overlay_add_item, "$g_presentation_obj_adult", "@a bandit"),
		(overlay_add_item, "$g_presentation_obj_adult", "@a slave-trader"),
		(overlay_set_val, "$g_presentation_obj_adult", "$background_answer_3"),
		
		(create_text_overlay, reg1, "@I am adventuring...", tf_center_justify),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
		(position_set_x, pos1, 150),
        (position_set_y, pos1, 340),
        (overlay_set_position, reg1, pos1),
		
		(position_set_x, pos1, 175),
		(position_set_y, pos1, 310),
        (create_combo_button_overlay, "$g_presentation_obj_reason"),
        (overlay_set_position, "$g_presentation_obj_reason", pos1),
		(position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_reason", pos1),
		(overlay_add_item, "$g_presentation_obj_reason", "@for money and power"),
        (overlay_add_item, "$g_presentation_obj_reason", "@because I was forced out of my home"),
        (overlay_add_item, "$g_presentation_obj_reason", "@because of religious fervor"),
        (overlay_add_item, "$g_presentation_obj_reason", "@because of wanderlust"),
        (overlay_add_item, "$g_presentation_obj_reason", "@because I lost a loved one"),
        (overlay_add_item, "$g_presentation_obj_reason", "@for personal revenge"),
		(overlay_add_item, "$g_presentation_obj_reason", "@out of a sense of duty"),
		(overlay_set_val, "$g_presentation_obj_reason", "$background_answer_4"),
		
		(create_text_overlay, reg1, "@I am travelling to the...", tf_center_justify),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
		(position_set_x, pos1, 150),
        (position_set_y, pos1, 270),
        (overlay_set_position, reg1, pos1),
		
		(position_set_x, pos1, 175),
		(position_set_y, pos1, 240),
        (create_combo_button_overlay, "$g_presentation_obj_region"),
        (overlay_set_position, "$g_presentation_obj_region", pos1),
		(position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_region", pos1),
		(overlay_add_item, "$g_presentation_obj_region", "@Sarranid Sultanate"),
		(overlay_add_item, "$g_presentation_obj_region", "@Kingdom of the Rhodoks"),
		(overlay_add_item, "$g_presentation_obj_region", "@Kingdom of the Nords"),
		(overlay_add_item, "$g_presentation_obj_region", "@Khergit Khanate"),
		(overlay_add_item, "$g_presentation_obj_region", "@Kingdom of the Vaegirs"),
		(overlay_add_item, "$g_presentation_obj_region", "@Kingdom of Swadia"),
		(overlay_set_val, "$g_presentation_obj_region", "$background_answer_5"),
        


	

		## biography
        (create_text_overlay, reg1, "@Biography:", tf_center_justify),
        (position_set_x, pos1, 1200),
        (position_set_y, pos1, 1200),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 660),
        (overlay_set_position, reg1, pos1),
		
	    (call_script, "script_mcc_get_character_background_text"),
        (create_text_overlay, "$g_presentation_obj_story", "@{s1}", tf_double_space|tf_scrollable),
        (position_set_x, pos1, 320),
        (position_set_y, pos1, 90),
        (overlay_set_position, "$g_presentation_obj_story", pos1),
        (position_set_x, pos1, 340),
        (position_set_y, pos1, 520),
        (overlay_set_area_size, "$g_presentation_obj_story", pos1),
		
		## stat changes
        (create_text_overlay, reg1, "@Stat Changes:", tf_center_justify),
        (position_set_x, pos1, 1200),
        (position_set_y, pos1, 1200),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 835),
        (position_set_y, pos1, 660),
        (overlay_set_position, reg1, pos1),
		
		
		#(call_script, "script_mcc_initialize_faction_items"),
		##########################################################
		###                 GENERATE STAT INFO                 ###
		##########################################################
		(str_clear, reg5),
		
		 ### STRENGTH ###
		 # Label
		 (create_text_overlay, reg1, "@Str", tf_center_justify),
         (position_set_x, pos1, 900),
         (position_set_y, pos1, 900),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 760),
         (position_set_y, pos1, 620),
         (overlay_set_position, reg1, pos1),
		 
		 ## Value
		 (create_text_overlay, "$g_presentation_obj_strength", "str_mcc_zero", tf_center_justify),
         (position_set_x, pos1, 850),
         (position_set_y, pos1, 850),
         (overlay_set_size, "$g_presentation_obj_strength", pos1),
         (position_set_x, pos1, 760),
         (position_set_y, pos1, 595),
         (overlay_set_position, "$g_presentation_obj_strength", pos1),
		 
		 ### AGILITY ###
		 # Label
		 (create_text_overlay, reg1, "@Agi", tf_center_justify),
         (position_set_x, pos1, 900),
         (position_set_y, pos1, 900),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 805),
         (position_set_y, pos1, 620),
         (overlay_set_position, reg1, pos1),
		 
		 ## Value
		 (create_text_overlay, "$g_presentation_obj_agility", "str_mcc_zero", tf_center_justify),
         (position_set_x, pos1, 850),
         (position_set_y, pos1, 850),
         (overlay_set_size, "$g_presentation_obj_agility", pos1),
         (position_set_x, pos1, 805),
         (position_set_y, pos1, 595),
         (overlay_set_position, "$g_presentation_obj_agility", pos1),
		 
		 ### INTELLIGENCE ###
		 # Label
		 (create_text_overlay, reg1, "@Int", tf_center_justify),
         (position_set_x, pos1, 900),
         (position_set_y, pos1, 900),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 850),
         (position_set_y, pos1, 620),
         (overlay_set_position, reg1, pos1),
		 
		 ## Value
		 (create_text_overlay, "$g_presentation_obj_intel", "str_mcc_zero", tf_center_justify),
         (position_set_x, pos1, 850),
         (position_set_y, pos1, 850),
         (overlay_set_size, "$g_presentation_obj_intel", pos1),
         (position_set_x, pos1, 850),
         (position_set_y, pos1, 595),
         (overlay_set_position, "$g_presentation_obj_intel", pos1),
		 
		 ### CHARISMA ###
		 # Label
		 (create_text_overlay, reg1, "@Cha", tf_center_justify),
         (position_set_x, pos1, 900),
         (position_set_y, pos1, 900),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 895),
         (position_set_y, pos1, 620),
         (overlay_set_position, reg1, pos1),
		
		## Value
		 (create_text_overlay, "$g_presentation_obj_charisma", "str_mcc_zero", tf_center_justify),
         (position_set_x, pos1, 850),
         (position_set_y, pos1, 850),
         (overlay_set_size, "$g_presentation_obj_charisma", pos1),
         (position_set_x, pos1, 895),
         (position_set_y, pos1, 595),
         (overlay_set_position, "$g_presentation_obj_charisma", pos1),
		 
		 ### GOLD ###
		 # Label
		 (create_text_overlay, reg1, "@Gold"),
         (position_set_x, pos1, 900),
         (position_set_y, pos1, 900),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 695),
         (position_set_y, pos1, 520),
         (overlay_set_position, reg1, pos1),
		
		## Value
		 (create_text_overlay, "$g_presentation_obj_gold", "str_mcc_zero", tf_center_justify),
         (position_set_x, pos1, 850),
         (position_set_y, pos1, 850),
         (overlay_set_size, "$g_presentation_obj_gold", pos1),
         (position_set_x, pos1, 805),
         (position_set_y, pos1, 520),
         (overlay_set_position, "$g_presentation_obj_gold", pos1),
		 
		 ### RENOWN ###
		 # Label
		 (create_text_overlay, reg1, "@Renown"),
         (position_set_x, pos1, 900),
         (position_set_y, pos1, 900),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 695),
         (position_set_y, pos1, 500),
         (overlay_set_position, reg1, pos1),
		
		## Value
		 (create_text_overlay, "$g_presentation_obj_renown", "str_mcc_zero", tf_center_justify),
         (position_set_x, pos1, 850),
         (position_set_y, pos1, 850),
         (overlay_set_size, "$g_presentation_obj_renown", pos1),
         (position_set_x, pos1, 805),
         (position_set_y, pos1, 500),
         (overlay_set_position, "$g_presentation_obj_renown", pos1),
		 
		 ### WEAPON PROF - ONE HAND ###
		 # Label
		 (create_text_overlay, reg1, "@One Handed"),
         (position_set_x, pos1, 900),
         (position_set_y, pos1, 900),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 695),
         (position_set_y, pos1, 480),
         (overlay_set_position, reg1, pos1),
		
		## Value
		 (create_text_overlay, "$g_presentation_obj_onehand", "str_mcc_zero", tf_center_justify),
         (position_set_x, pos1, 850),
         (position_set_y, pos1, 850),
         (overlay_set_size, "$g_presentation_obj_onehand", pos1),
         (position_set_x, pos1, 805),
         (position_set_y, pos1, 480),
         (overlay_set_position, "$g_presentation_obj_onehand", pos1),
		 
		 ### WEAPON PROF - TWO HAND ###
		 # Label
		 (create_text_overlay, reg1, "@Two Handed"),
         (position_set_x, pos1, 900),
         (position_set_y, pos1, 900),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 695),
         (position_set_y, pos1, 460),
         (overlay_set_position, reg1, pos1),
		
		## Value
		 (create_text_overlay, "$g_presentation_obj_twohand", "str_mcc_zero", tf_center_justify),
         (position_set_x, pos1, 850),
         (position_set_y, pos1, 850),
         (overlay_set_size, "$g_presentation_obj_twohand", pos1),
         (position_set_x, pos1, 805),
         (position_set_y, pos1, 460),
         (overlay_set_position, "$g_presentation_obj_twohand", pos1),
		 
		 ### WEAPON PROF - POLEARMS ###
		 # Label
		 (create_text_overlay, reg1, "@Polearms"),
         (position_set_x, pos1, 900),
         (position_set_y, pos1, 900),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 695),
         (position_set_y, pos1, 440),
         (overlay_set_position, reg1, pos1),
		
		## Value
		 (create_text_overlay, "$g_presentation_obj_polearm", "str_mcc_zero", tf_center_justify),
         (position_set_x, pos1, 850),
         (position_set_y, pos1, 850),
         (overlay_set_size, "$g_presentation_obj_polearm", pos1),
         (position_set_x, pos1, 805),
         (position_set_y, pos1, 440),
         (overlay_set_position, "$g_presentation_obj_polearm", pos1),
		 
		 ### WEAPON PROF - ARCHERY ###
		 # Label
		 (create_text_overlay, reg1, "@Bows"),
         (position_set_x, pos1, 900),
         (position_set_y, pos1, 900),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 695),
         (position_set_y, pos1, 420),
         (overlay_set_position, reg1, pos1),
		
		## Value
		 (create_text_overlay, "$g_presentation_obj_bow", "str_mcc_zero", tf_center_justify),
         (position_set_x, pos1, 850),
         (position_set_y, pos1, 850),
         (overlay_set_size, "$g_presentation_obj_bow", pos1),
         (position_set_x, pos1, 805),
         (position_set_y, pos1, 420),
         (overlay_set_position, "$g_presentation_obj_bow", pos1),
		 
		 ### WEAPON PROF - CROSSBOW ###
		 # Label
		 (create_text_overlay, reg1, "@Crossbows"),
         (position_set_x, pos1, 900),
         (position_set_y, pos1, 900),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 695),
         (position_set_y, pos1, 400),
         (overlay_set_position, reg1, pos1),
		
		## Value
		 (create_text_overlay, "$g_presentation_obj_xbow", "str_mcc_zero", tf_center_justify),
         (position_set_x, pos1, 850),
         (position_set_y, pos1, 850),
         (overlay_set_size, "$g_presentation_obj_xbow", pos1),
         (position_set_x, pos1, 805),
         (position_set_y, pos1, 400),
         (overlay_set_position, "$g_presentation_obj_xbow", pos1),
		 
		 ### WEAPON PROF - THROWING ###
		 # Label
		 (create_text_overlay, reg1, "@Throwing"),
         (position_set_x, pos1, 900),
         (position_set_y, pos1, 900),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 695),
         (position_set_y, pos1, 380),
         (overlay_set_position, reg1, pos1),
		
		## Value
		 (create_text_overlay, "$g_presentation_obj_throw", "str_mcc_zero", tf_center_justify),
         (position_set_x, pos1, 850),
         (position_set_y, pos1, 850),
         (overlay_set_size, "$g_presentation_obj_throw", pos1),
         (position_set_x, pos1, 805),
         (position_set_y, pos1, 380),
         (overlay_set_position, "$g_presentation_obj_throw", pos1),
		 
		 
		 (call_script, "script_mcc_generate_skill_set", limit_to_stats),
		 
		 
					
		
    ]),
	 
	 
		
   (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
		
		(try_begin), ####### DONE BUTTON #######
			(eq, ":object", "$g_presentation_obj_1"),
			(call_script, "script_mcc_end_presentation_begin_game"),
			# Decide on whether to use a banner or not
			(try_begin),
			## mcc 1.1+ ## - Workaround for the Warband 1.151 broken banner presentation.
				# (eq, "$background_type", cb_noble),
				# (jump_to_menu, "mnu_auto_return"),
				# (start_presentation, "prsnt_banner_selection"),
			# (else_try),
			## mcc 1.1- ##
				(presentation_set_duration, 0),
				(jump_to_menu, "mnu_auto_return"),
			(else_try),
                (change_screen_return, 0),
			(try_end),

			#(jump_to_menu, "mnu_start_phase_2_5"),
			
		(else_try), ####### BACK BUTTON #######
          (eq, ":object", "$g_presentation_obj_2"),
		  (jump_to_menu, "mnu_start_game_0"),
		  (presentation_set_duration, 0),

			
		(else_try), ####### DEFAULT BUTTON #######]
			(eq, ":object", "$g_presentation_obj_3"),
			(call_script, "script_mcc_default_settings"),
			(start_presentation, "prsnt_mcc_character_creation"),
		  
		# (else_try), ####### RANDOMIZE BUTTON #######
			# (troop_slot_eq, mcc_objects, mcc_obj_button_random, ":object"),
			# (store_random_in_range, "$character_gender", 0, 2),    # Gender
			# (store_random_in_range, "$background_type", 0, 6),     # Father background
			# (store_random_in_range, "$background_answer_2", 0, 5), # Early life
			# (store_random_in_range, "$background_answer_3", 0, 6), # Later life
			# (store_random_in_range, "$background_answer_4", 0, 5), # Reason
            # (store_random_in_range, reg21, 0, 5), # Starting Region
			# (troop_set_slot, mcc_objects, mcc_val_menu_initial_region, reg21),
            # (start_presentation, "prsnt_mcc_character_creation"),
			
			
		(else_try), ####### GENDER MENU #######
			(eq, ":object", "$g_presentation_obj_gender"),
			(assign, "$character_gender", ":value"),
			(start_presentation, "prsnt_mcc_character_creation"),
			(assign, "$g_presentation_obj_gender", ":value"),
			
		(else_try), ####### FATHER BACKGROUND MENU #######
			(eq, ":object", "$g_presentation_obj_father"),
			(assign, "$background_type", ":value"),
			(start_presentation, "prsnt_mcc_character_creation"),
			(assign, "$g_presentation_obj_father", ":value"),
			
		(else_try), ####### EARLY LIFE BACKGROUND MENU #######
			(eq, ":object", "$g_presentation_obj_early"),
			(assign, "$background_answer_2", ":value"),
			(start_presentation, "prsnt_mcc_character_creation"),
			(assign, "$g_presentation_obj_early", ":value"),
			
		(else_try), ####### LATER LIFE BACKGROUND MENU #######
			(eq, ":object", "$g_presentation_obj_adult"),
			(assign, "$background_answer_3", ":value"),
			(start_presentation, "prsnt_mcc_character_creation"),
			(assign, "$g_presentation_obj_adult", ":value"),
			
		(else_try), ####### REASON BACKGROUND MENU #######
			(eq, ":object", "$g_presentation_obj_reason"),
			(assign, "$background_answer_4", ":value"),
			(start_presentation, "prsnt_mcc_character_creation"),
			(assign, "$g_presentation_obj_reason", ":value"),
			
		
		(else_try), ####### STARTING REGION MENU #######
			(eq, ":object", "$g_presentation_obj_region"),
			(assign, "$background_answer_5", ":value"),
			(start_presentation, "prsnt_mcc_character_creation"),
			(assign, "$g_presentation_obj_region", ":value"),
		(try_end),
      ]),
	  
	]),
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