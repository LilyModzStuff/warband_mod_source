# Banking (2.0) by Lazeras
# Released 1 December 2011
from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
from header_items import *   # Added for Show all Items presentation.
from module_items import *   # Added for Show all Items presentation.
import string

####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

# Manualy add these to module_presentations add 
# these lines from `presentations` to bottom of the file
presentations = [
########################################################################################################################
#  KAOS BANKING KIT START																							   #
########################################################################################################################
("Lazeras_bank_prsnt", 0, mesh_load_window, 
   [
     (ti_on_presentation_load,
      [
		(presentation_set_duration, 999999),
	    (set_fixed_point_multiplier, 1000),
		#(assign, "$jq_just_visited_CO", 0),
		#(assign, "$jq_slot", 0),
		(assign, "$g_jq_Return_to_menu", 1013),#jibberish value, just for button assign
		
		#Back to menu - graphical button
		(create_game_button_overlay, "$g_jq_Return_to_menu", "@_Return to menu_"),	 
		(position_set_x, pos1, 500),
	    (position_set_y, pos1, 23),
	    (overlay_set_position, "$g_jq_Return_to_menu", pos1),
		#############################################################################################################
		#CREATE HEADLINES        																					#
		#############################################################################################################
		(assign, ":x_poshl", 165),
	 	(assign, ":y_pos", 581),
	 	(assign, ":jq_size", 0),
		(position_set_x, ":jq_size", 720),
	    (position_set_y, ":jq_size", 775),

		(create_text_overlay, reg2, "@Bank", tf_center_justify),
	    (overlay_set_size, reg2, ":jq_size"),
	 	(position_set_x, pos1, ":x_poshl"),
	    (position_set_y, pos1, ":y_pos"),
	    (overlay_set_position, reg2, pos1),

		(create_text_overlay, reg2, "@Prosperity", tf_center_justify),
	    (overlay_set_size, reg2, ":jq_size"),
		(val_add, ":x_poshl", 120),
	 	(position_set_x, pos1, ":x_poshl"),
	    (overlay_set_position, reg2, pos1),

		(create_text_overlay, reg2, "@Loan Amount", tf_center_justify),
	    (overlay_set_size, reg2, ":jq_size"),
		(val_add, ":x_poshl", 120),
	 	(position_set_x, pos1, ":x_poshl"),
	    (overlay_set_position, reg2, pos1),

		(create_text_overlay, reg2, "@Loan Interest", tf_center_justify),
	    (overlay_set_size, reg2, ":jq_size"),
		(val_add, ":x_poshl", 120),
		(position_set_x, pos1, ":x_poshl"),
	    (overlay_set_position, reg2, pos1),

		(create_text_overlay, reg2, "@Dsposit Amount", tf_center_justify),
	    (overlay_set_size, reg2, ":jq_size"),
		(val_add, ":x_poshl", 120),
	 	(position_set_x, pos1, ":x_poshl"),
	    (overlay_set_position, reg2, pos1),

		(create_text_overlay, reg2, "@Deposit Interest", tf_center_justify),
	    (overlay_set_size, reg2, ":jq_size"),
		(val_add, ":x_poshl", 120),
	 	(position_set_x, pos1, ":x_poshl"),
	    (overlay_set_position, reg2, pos1),

	    (assign, ":jq_value", 100),
	    (assign, ":jq_size", 0),
		(assign, ":x_pos", 25),
	    (assign, ":y_pos", 547),
	    (str_clear, s9),	
		(str_clear, s8),

		#############################################################################################################
		#END HEADLINES        																						#
		#############################################################################################################	

		(assign, reg15,0),#total_debt
		(assign, reg22,0),#weekly_debt_interest
		(assign, reg32,0),#total_deposit
		(assign, reg42,0),#monthly_deposit_interest
		(assign, ":tottal_debt",0),#total_debt
		(assign, ":tottal_debt_interest",0),#weekly_debt_interest
		(assign, ":tottal_deposit",0),#total_deposit
		(assign, ":tottal_deposit_interest",0),#monthly_deposit_interest
		(assign, ":center_no",0),#Centr Number
		(assign, ":liege_tax_tottal",0),#Centr Number
		
		 (try_for_range, ":center_no", towns_begin, towns_end),
		 	   ##############################################################################
			   # IF THE TOWN HAS A BANK THEN GET THE REQUIRED INFO
			   ##############################################################################
			   (party_get_slot, ":has_bank", ":center_no", slot_town_has_bank),
			   (eq, ":has_bank", 1),     
			   (str_store_party_name,s9, ":center_no"),
			   (call_script, "script_cf_bank_war_tax", ":center_no"),
		 	   ##############################################################################
			   # GET INTEREST RATES
			   ##############################################################################
			   (call_script, "script_bank_report_rates", ":center_no"),
			   (assign, ":player_debt_interest_rate", reg0),
			   (assign, ":player_deposit_interest_rate", reg1),	

#####################  debugging messages ################################
      (try_begin),		
			(eq, "$kaos_debug_mode", 1),	
			(display_log_message, "@{!} presentation INTEREST RATES player_debt_interest_rate is {reg0} and player_deposit_interest_rate is {reg1}", 0xFF0000),
      (try_end),		
#####################  debugging messages ################################

			  ############################################################################################################################################################
			  # IF THE TOWN SLOT HAS A DEBT GREATER THAN 0 LETS WORK WITH IT																							   #
		      ############################################################################################################################################################
	   	 	   (party_get_slot,":player_debt",":center_no",slot_town_bank_debt),
			   (try_begin),
				   (ge, ":player_debt", 0),   
				   (call_script, "script_bank_report_debt", ":center_no", ":player_debt_interest_rate"),
			       (assign, ":player_debt_interest", reg0),
			   	   (assign, ":player_debt", reg1),
				   (party_get_slot,":due_date",":center_no",slot_town_bank_debt_repayment_date),
				   (store_current_day, ":cur_day"),	
				   (store_sub, ":days_to_go", ":due_date", ":cur_day"),
				   (val_add, ":tottal_debt", ":player_debt"),
				   (val_add, ":tottal_debt_interest", ":player_debt_interest"),
#####################  debugging messages ################################
      (try_begin),		
			(eq, "$kaos_debug_mode", 1),	
			(display_log_message, "@{!} presentation DEBT player_debt_interest{reg0}  player_debt{reg1}", 0xFF0000),
      (try_end),		
#####################  debugging messages ################################
			   (try_end),
			  ############################################################################################################################################################
			  # END DEBT PROCCESSING																																	   #
			  ############################################################################################################################################################

			  ############################################################################################################################################################
			  # IF THE TOWN SLOT HAS A DEPOSIT GREATER THAN 0 LETS WORK WITH IT																						   #
			  ############################################################################################################################################################
	   		   (party_get_slot,":player_deposit",":center_no",slot_town_bank_deposit),
	   		   (party_get_slot,":debt_effect",":center_no",slot_town_bank_debt_repayment_effect),
			   (try_begin),
				   (ge, ":player_deposit", 0),
				   (call_script, "script_bank_report_deposit", ":center_no", ":player_deposit_interest_rate"),
				   (assign, ":player_deposit_interest", reg0),
				   (assign, ":player_deposit", reg1),
				   (assign, ":liege_tax", reg2),

				   (val_add, ":liege_tax_tottal", ":liege_tax"),
				   (val_add, ":tottal_deposit", ":player_deposit"),
				   (val_add, ":tottal_deposit_interest", ":player_deposit_interest"),
#####################  debugging messages ################################
      (try_begin),		
			(eq, "$kaos_debug_mode", 1),	
			(display_log_message, "@{!} presentation DEPOSIT player_deposit_interest{reg0}  player_deposit{reg1}", 0xFF0000),
      (try_end),		
#####################  debugging messages ################################
			   (try_end),
			  ############################################################################################################################################################
			  # END DEPOSIT PROCCESSING																																   #
			  ############################################################################################################################################################

#####################  debugging messages ################################
      (try_begin),		
			(eq, "$kaos_debug_mode", 1),
				   (val_add, reg30, ":tottal_debt"),
				   (val_add, reg31, ":tottal_debt_interest"),	
				   (val_add, reg32, ":tottal_deposit"),
				   (val_add, reg33, ":tottal_deposit_interest"),
			(display_log_message, "@{!} presentation tottals tottal_debt{reg30} tottal_debt_interest{reg31} tottal_deposit{reg32} tottal_deposit_interest{reg33}", 0xFF0000),
      (try_end),		
#####################  debugging messages ################################

				(val_add, ":jq_value", 1),
				###################################################################################################################
				#   BEGIN REPORT LINE GENERATION																				  #
				###################################################################################################################
				#center center name
				(val_add, ":x_pos", 110), 
			    (str_store_party_name,s9, ":center_no"),
				(str_store_string, s1, "@{s9} "),
				(create_text_overlay, reg1, s1, tf_left_align),
			    (position_set_x, pos3, ":x_pos"),
			    (position_set_y, pos3, ":y_pos"),
			    (overlay_set_position, reg1, pos3),
				(position_set_x, pos3, 750),
				(position_set_y, pos3, 850),
				(overlay_set_size, reg1, pos3),

				#center prosperity
				(val_add, ":x_pos", 90),  
				(call_script, "script_get_prosperity_text_to_s50", ":center_no"),
				(call_script, "script_bank_get_prosperity_extra_to_s49", ":center_no"),
#####################  debugging messages ################################
      (try_begin),		
			(eq, "$kaos_debug_mode", 1),
				   (val_add, reg30, ":tottal_debt"),
				   (val_add, reg31, ":tottal_debt_interest"),	
				   (val_add, reg32, ":tottal_deposit"),
				   (val_add, reg33, ":tottal_deposit_interest"),
			(display_log_message, "@{!} {s49}", 0xFF0000),
      (try_end),		
#####################  debugging messages ################################
				(str_store_string, s1, "@{s50} {s49}"),
				(create_text_overlay, reg1, s1, tf_left_align),
			    (position_set_x, pos3, ":x_pos"),
			    (position_set_y, pos3, ":y_pos"),
			    (overlay_set_position, reg1, pos3),
				(position_set_x, pos3, 750),
				(position_set_y, pos3, 850),
				(overlay_set_size, reg1, pos3),

				#city debt
				(val_add, ":x_pos", 140),  
				(assign, reg6, ":player_debt"),
				(str_store_string, s1, "@{reg6}"),
				(create_text_overlay, reg1, s1, tf_left_align),
			    (position_set_x, pos3, ":x_pos"),
			    (position_set_y, pos3, ":y_pos"),
			    (overlay_set_position, reg1, pos3),
				(position_set_x, pos3, 750),
				(position_set_y, pos3, 850),
				(overlay_set_size, reg1, pos3),

				#city debt_interest
				(val_add, ":x_pos", 115),  
				(assign, reg6, ":player_debt_interest"),
				(str_store_string, s1, "@{reg6}"),
				(create_text_overlay, reg1, s1, tf_left_align),
			    (position_set_x, pos3, ":x_pos"),
			    (position_set_y, pos3, ":y_pos"),
			    (overlay_set_position, reg1, pos3),
				(position_set_x, pos3, 750),
				(position_set_y, pos3, 850),
				(overlay_set_size, reg1, pos3),

				#city deposit
				(val_add, ":x_pos", 115),  
				(assign, reg6, ":player_deposit"),
				(str_store_string, s1, "@{reg6}"),
				(create_text_overlay, reg1, s1, tf_left_align),
			    (position_set_x, pos3, ":x_pos"),
			    (position_set_y, pos3, ":y_pos"),
			    (overlay_set_position, reg1, pos3),
				(position_set_x, pos3, 750),
				(position_set_y, pos3, 850),
				(overlay_set_size, reg1, pos3),

				#city varible_interest
				(val_add, ":x_pos", 115),  
				(assign, reg6, ":player_deposit_interest"),
				(str_store_string, s1, "@{reg6}"),
				(create_text_overlay, reg1, s1, tf_left_align),
			    (position_set_x, pos3, ":x_pos"),
			    (position_set_y, pos3, ":y_pos"),
			    (overlay_set_position, reg1, pos3),
				(position_set_x, pos3, 750),
				(position_set_y, pos3, 850),
				(overlay_set_size, reg1, pos3),

				(try_begin),
					(gt, ":player_debt", 0),
					(val_add, ":x_pos", 50), 
					(assign, reg6, ":days_to_go"),
					(assign, reg7, ":debt_effect"),
					(str_store_party_name,s9, ":center_no"),
					(str_store_string, s1, "@({reg6}) days to make a payment."),
					(create_text_overlay, reg1, s1, tf_left_align),
					(position_set_x, pos3, ":x_pos"),
					(position_set_y, pos3, ":y_pos"),
					(overlay_set_position, reg1, pos3),
					(position_set_x, pos3, 750),
					(position_set_y, pos3, 850),
					(overlay_set_size, reg1, pos3),
				(try_end),

				(try_begin),
					(gt, ":liege_tax", 0),
					(val_add, ":x_pos", 50), 
					(assign, reg6, ":liege_tax"),
					(str_store_string, s1, "@Liege tax of ({reg6}) ."),
					(create_text_overlay, reg1, s1, tf_left_align),
					(position_set_x, pos3, ":x_pos"),
					(position_set_y, pos3, ":y_pos"),
					(overlay_set_position, reg1, pos3),
					(position_set_x, pos3, 750),
					(position_set_y, pos3, 850),
					(overlay_set_size, reg1, pos3),
				(try_end),

				(assign, ":x_pos", 25),
				(assign, ":x_poshl", 165),
				(val_sub, ":y_pos", 23),#linebreak 
				(ge, ":x_pos", 950),
				(assign, ":x_pos", 25),
				(val_sub, ":y_pos", 23),
				###################################################################################################################
				#   END REPORT LINE GENERATION								   												      #
				###################################################################################################################
		(try_end),

		###################################################################################################################
		#   START REPORT LINE GENERATION								   												  #
		###################################################################################################################
		#Total Debt
		(val_add, ":x_pos", 110), 
		(val_sub, ":y_pos", 30), 
		(str_store_string, s1, "@Total Debt"),
		(create_text_overlay, reg1, s1, tf_left_align),
	    (position_set_x, pos3, ":x_pos"),
	    (position_set_y, pos3, ":y_pos"),
	    (overlay_set_position, reg1, pos3),
		(position_set_x, pos3, 750),
		(position_set_y, pos3, 850),
		(overlay_set_size, reg1, pos3),

		#total loans ":tottal_debt"
		(val_add, ":x_pos", 230), 
		(assign, reg6, ":tottal_debt"),
		(str_store_string, s1, "@{reg6}"),
		(create_text_overlay, reg1, s1, tf_left_align),
	    (position_set_x, pos3, ":x_pos"),
	    (position_set_y, pos3, ":y_pos"),
	    (overlay_set_position, reg1, pos3),
		(position_set_x, pos3, 750),
		(position_set_y, pos3, 850),
		(overlay_set_size, reg1, pos3),

		#total loans inte3rest ":tottal_debt_interest"
		(val_add, ":x_pos", 115), 
		(assign, reg6, ":tottal_debt_interest"),
		(str_store_string, s1, "@{reg6}"),
		(create_text_overlay, reg1, s1, tf_left_align),
	    (position_set_x, pos3, ":x_pos"),
	    (position_set_y, pos3, ":y_pos"),
	    (overlay_set_position, reg1, pos3),
		(position_set_x, pos3, 750),
		(position_set_y, pos3, 850),
		(overlay_set_size, reg1, pos3),
	   	 
		#Total Deposit
		(val_sub, ":x_pos", 344), 
		(val_sub, ":y_pos", 30), 
		(str_store_string, s1, "@Total Deposits"),
		(create_text_overlay, reg1, s1, tf_left_align),
	    (position_set_x, pos3, ":x_pos"),
	    (position_set_y, pos3, ":y_pos"),
	    (overlay_set_position, reg1, pos3),
		(position_set_x, pos3, 750),
		(position_set_y, pos3, 850),
		(overlay_set_size, reg1, pos3),

		#total deposits ":tottal_deposit"
		(val_add, ":x_pos", 470), 
		(assign, reg6, ":tottal_deposit"),
		(str_store_string, s1, "@{reg6}"),
		(create_text_overlay, reg1, s1, tf_left_align),
	    (position_set_x, pos3, ":x_pos"),
	    (position_set_y, pos3, ":y_pos"),
	    (overlay_set_position, reg1, pos3),
		(position_set_x, pos3, 750),
		(position_set_y, pos3, 850),
		(overlay_set_size, reg1, pos3),

	  	#total deposits inte3rest ":tottal_deposit_interest"
		(val_add, ":x_pos", 115), 
		(assign, reg6, ":tottal_deposit_interest"),
		(str_store_string, s1, "@{reg6}"),
		(create_text_overlay, reg1, s1, tf_left_align),
	    (position_set_x, pos3, ":x_pos"),
	    (position_set_y, pos3, ":y_pos"),
	    (overlay_set_position, reg1, pos3),
		(position_set_x, pos3, 750),
		(position_set_y, pos3, 850),
		(overlay_set_size, reg1, pos3),
			
		###################################################################################################################
		#   END REPORT LINE GENERATION								   												      #
		###################################################################################################################	

		(assign, "$g_apply_Kaoses_bank_report_to_gold", 0),
	]
), 


#Check for buttonpress
     (ti_on_presentation_event_state_change,
	      [
				(presentation_set_duration, 0),
		  ]
	 ),

		 (ti_on_presentation_run,
		       [
			       (try_begin),
				   (this_or_next|key_clicked, key_escape),
				   (key_clicked, key_right_mouse_button),
				   (presentation_set_duration, 0),
				   (jump_to_menu, "mnu_reports"),
		        ]
		  ),


     ]
),














  ("Lazeras_bank_faction_prsnt", 0, mesh_load_window, 
   [
     (ti_on_presentation_load,
      [
		(presentation_set_duration, 999999),
	    (set_fixed_point_multiplier, 1000),
		#(assign, "$jq_just_visited_CO", 0),
		#(assign, "$jq_slot", 0),
		(assign, "$g_jq_Return_to_menu", 1013),#jibberish value, just for button assign
		
		#Back to menu - graphical button
		(create_game_button_overlay, "$g_jq_Return_to_menu", "@_Return to menu_"),	 
		(position_set_x, pos1, 500),
	    (position_set_y, pos1, 23),
	    (overlay_set_position, "$g_jq_Return_to_menu", pos1),
		#############################################################################################################
		#CREATE HEADLINES        																					#
		#############################################################################################################
		(assign, ":x_poshl", 165),
	 	(assign, ":y_pos", 581),
	 	(assign, ":jq_size", 0),
		(position_set_x, ":jq_size", 720),
	    (position_set_y, ":jq_size", 775),

		(create_text_overlay, reg2, "@Bank", tf_center_justify),
	    (overlay_set_size, reg2, ":jq_size"),
	 	(position_set_x, pos1, ":x_poshl"),
	    (position_set_y, pos1, ":y_pos"),
	    (overlay_set_position, reg2, pos1),

		(create_text_overlay, reg2, "@Loan Amount", tf_center_justify),
	    (overlay_set_size, reg2, ":jq_size"),
		(val_add, ":x_poshl", 120),
	 	(position_set_x, pos1, ":x_poshl"),
	    (overlay_set_position, reg2, pos1),

		(create_text_overlay, reg2, "@Loan Interest", tf_center_justify),
	    (overlay_set_size, reg2, ":jq_size"),
		(val_add, ":x_poshl", 120),
		(position_set_x, pos1, ":x_poshl"),
	    (overlay_set_position, reg2, pos1),

		(create_text_overlay, reg2, "@Dsposit Amount", tf_center_justify),
	    (overlay_set_size, reg2, ":jq_size"),
		(val_add, ":x_poshl", 120),
	 	(position_set_x, pos1, ":x_poshl"),
	    (overlay_set_position, reg2, pos1),

		(create_text_overlay, reg2, "@Deposit Interest", tf_center_justify),
	    (overlay_set_size, reg2, ":jq_size"),
		(val_add, ":x_poshl", 120),
	 	(position_set_x, pos1, ":x_poshl"),
	    (overlay_set_position, reg2, pos1),

	    (assign, ":jq_value", 100),
	    (assign, ":jq_size", 0),
		(assign, ":x_pos", 25),
	    (assign, ":y_pos", 547),
	    (str_clear, s9),	
		(str_clear, s8),

		#############################################################################################################
		#END HEADLINES        																						#
		#############################################################################################################	

		(assign, reg15,0),#total_debt
		(assign, reg22,0),#weekly_debt_interest
		(assign, reg32,0),#total_deposit
		(assign, reg42,0),#monthly_deposit_interest
		(assign, ":tottal_debt",0),#total_debt
		(assign, ":tottal_debt_interest",0),#weekly_debt_interest
		(assign, ":tottal_deposit",0),#total_deposit
		(assign, ":tottal_deposit_interest",0),#monthly_deposit_interest
		(assign, ":center_no",0),#Centr Number
		(assign, ":liege_tax_tottal",0),#Centr Number
		

   		############################################################################################################################################################
		# BEGIN FACTION BANKING REPORT 									   																						   #
		############################################################################################################################################################
			(eq, "$bank_availability", 1),
			(try_for_range, ":faction", "fac_kingdom_1", kingdoms_end),
				   (str_store_faction_name,s9, ":faction"),
				   (call_script, "script_cf_bank_war_faction_tax", ":faction"),

				   (assign, ":player_debt_interest_rate", 0),
				   (assign, ":player_deposit_interest_rate", 0),
				   (assign, ":walled_center_count", 0),		

			 	   ##############################################################################
				   # GET INTEREST RATES for all waaled centers in faction
				   ##############################################################################
				   (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
					   (call_script, "script_bank_report_rates", ":center_no"),
					   (val_add, ":player_debt_interest_rate", reg0),
					   (val_add, ":player_deposit_interest_rate", reg1),	
					   (val_add, ":walled_center_count", 1),
				   (try_end),

			 	   ##############################################################################
				   # Average the INTEREST RATES by div tottal by number of centers calculated
				   ##############################################################################
				   (store_div, ":player_debt_interest_rate", ":player_debt_interest_rate", ":walled_center_count"),
				   (store_div, ":player_deposit_interest_rate", ":player_deposit_interest_rate", ":walled_center_count"),

	#####################  debugging messages ################################
	      (try_begin),		
				(eq, "$kaos_debug_mode", 1),	
				(display_log_message, "@{!} presentation INTEREST RATES player_debt_interest_rate is {reg0} and player_deposit_interest_rate is {reg1}", 0xFF0000),
	      (try_end),		
	#####################  debugging messages ################################

				  ############################################################################################################################################################
				  # IF THE TOWN SLOT HAS A DEBT GREATER THAN 0 LETS WORK WITH IT																							   #
			      ############################################################################################################################################################
		   	 	   (party_get_slot,":player_debt",":faction",slot_town_bank_debt),
				   (try_begin),
					   (ge, ":player_debt", 0),   
					   (call_script, "script_bank_report_faction_debt", ":faction", ":player_debt_interest_rate"),
				       (assign, ":player_debt_interest", reg0),
				   	   (assign, ":player_debt", reg1),
					   (party_get_slot,":due_date",":center_no",slot_town_bank_debt_repayment_date),
					   (store_current_day, ":cur_day"),	
					   (store_sub, ":days_to_go", ":due_date", ":cur_day"),
					   (val_add, ":tottal_debt", ":player_debt"),
					   (val_add, ":tottal_debt_interest", ":player_debt_interest"),
	#####################  debugging messages ################################
	      (try_begin),		
				(eq, "$kaos_debug_mode", 1),	
				(display_log_message, "@{!} presentation DEBT player_debt_interest{reg0}  player_debt{reg1}", 0xFF0000),
	      (try_end),		
	#####################  debugging messages ################################
				   (try_end),
				  ############################################################################################################################################################
				  # END DEBT PROCCESSING																																	   #
				  ############################################################################################################################################################

				  ############################################################################################################################################################
				  # IF THE TOWN SLOT HAS A DEPOSIT GREATER THAN 0 LETS WORK WITH IT																						   #
				  ############################################################################################################################################################
		   		   (party_get_slot,":player_deposit",":faction",slot_town_bank_deposit),
		   		   (party_get_slot,":debt_effect",":faction",slot_town_bank_debt_repayment_effect),
				   (try_begin),
					   (ge, ":player_deposit", 0),
					   (call_script, "script_bank_report_faction_deposit", ":faction", ":player_deposit_interest_rate"),
					   (assign, ":player_deposit_interest", reg0),
					   (assign, ":player_deposit", reg1),
					   (assign, ":liege_tax", reg2),

					   (val_add, ":liege_tax_tottal", ":liege_tax"),
					   (val_add, ":tottal_deposit", ":player_deposit"),
					   (val_add, ":tottal_deposit_interest", ":player_deposit_interest"),
	#####################  debugging messages ################################
	      (try_begin),		
				(eq, "$kaos_debug_mode", 1),	
				(display_log_message, "@{!} presentation DEPOSIT player_deposit_interest{reg0}  player_deposit{reg1}", 0xFF0000),
	      (try_end),		
	#####################  debugging messages ################################
				   (try_end),
				  ############################################################################################################################################################
				  # END DEPOSIT PROCCESSING																																   #
				  ############################################################################################################################################################

	#####################  debugging messages ################################
	      (try_begin),		
				(eq, "$kaos_debug_mode", 1),
					   (val_add, reg30, ":tottal_debt"),
					   (val_add, reg31, ":tottal_debt_interest"),	
					   (val_add, reg32, ":tottal_deposit"),
					   (val_add, reg33, ":tottal_deposit_interest"),
				(display_log_message, "@{!} presentation tottals tottal_debt{reg30} tottal_debt_interest{reg31} tottal_deposit{reg32} tottal_deposit_interest{reg33}", 0xFF0000),
	      (try_end),		
	#####################  debugging messages ################################

					(val_add, ":jq_value", 1),
					###################################################################################################################
					#   BEGIN REPORT LINE GENERATION																				  #
					###################################################################################################################
					#center center name
					(val_add, ":x_pos", 110), 
				    (str_store_faction_name,s9, ":faction"),
					(str_store_string, s1, "@{s9} "),
					(create_text_overlay, reg1, s1, tf_left_align),
				    (position_set_x, pos3, ":x_pos"),
				    (position_set_y, pos3, ":y_pos"),
				    (overlay_set_position, reg1, pos3),
					(position_set_x, pos3, 750),
					(position_set_y, pos3, 850),
					(overlay_set_size, reg1, pos3),

					#city debt
					(val_add, ":x_pos", 140),  
					(assign, reg6, ":player_debt"),
					(str_store_string, s1, "@{reg6}"),
					(create_text_overlay, reg1, s1, tf_left_align),
				    (position_set_x, pos3, ":x_pos"),
				    (position_set_y, pos3, ":y_pos"),
				    (overlay_set_position, reg1, pos3),
					(position_set_x, pos3, 750),
					(position_set_y, pos3, 850),
					(overlay_set_size, reg1, pos3),

					#city debt_interest
					(val_add, ":x_pos", 115),  
					(assign, reg6, ":player_debt_interest"),
					(str_store_string, s1, "@{reg6}"),
					(create_text_overlay, reg1, s1, tf_left_align),
				    (position_set_x, pos3, ":x_pos"),
				    (position_set_y, pos3, ":y_pos"),
				    (overlay_set_position, reg1, pos3),
					(position_set_x, pos3, 750),
					(position_set_y, pos3, 850),
					(overlay_set_size, reg1, pos3),

					#city deposit
					(val_add, ":x_pos", 115),  
					(assign, reg6, ":player_deposit"),
					(str_store_string, s1, "@{reg6}"),
					(create_text_overlay, reg1, s1, tf_left_align),
				    (position_set_x, pos3, ":x_pos"),
				    (position_set_y, pos3, ":y_pos"),
				    (overlay_set_position, reg1, pos3),
					(position_set_x, pos3, 750),
					(position_set_y, pos3, 850),
					(overlay_set_size, reg1, pos3),

					#city varible_interest
					(val_add, ":x_pos", 115),  
					(assign, reg6, ":player_deposit_interest"),
					(str_store_string, s1, "@{reg6}"),
					(create_text_overlay, reg1, s1, tf_left_align),
				    (position_set_x, pos3, ":x_pos"),
				    (position_set_y, pos3, ":y_pos"),
				    (overlay_set_position, reg1, pos3),
					(position_set_x, pos3, 750),
					(position_set_y, pos3, 850),
					(overlay_set_size, reg1, pos3),

					(try_begin),
						(gt, ":player_debt", 0),
						(val_add, ":x_pos", 50), 
						(assign, reg6, ":days_to_go"),
						(assign, reg7, ":debt_effect"),
						(str_store_party_name,s9, ":center_no"),
						(str_store_string, s1, "@({reg6}) days to make a payment."),
						(create_text_overlay, reg1, s1, tf_left_align),
						(position_set_x, pos3, ":x_pos"),
						(position_set_y, pos3, ":y_pos"),
						(overlay_set_position, reg1, pos3),
						(position_set_x, pos3, 750),
						(position_set_y, pos3, 850),
						(overlay_set_size, reg1, pos3),
					(try_end),

					(try_begin),
						(gt, ":liege_tax", 0),
						(val_add, ":x_pos", 50), 
						(assign, reg6, ":liege_tax"),
						(str_store_string, s1, "@Liege tax of ({reg6}) ."),
						(create_text_overlay, reg1, s1, tf_left_align),
						(position_set_x, pos3, ":x_pos"),
						(position_set_y, pos3, ":y_pos"),
						(overlay_set_position, reg1, pos3),
						(position_set_x, pos3, 750),
						(position_set_y, pos3, 850),
						(overlay_set_size, reg1, pos3),
					(try_end),

					(assign, ":x_pos", 25),
					(assign, ":x_poshl", 165),
					(val_sub, ":y_pos", 23),#linebreak 
					(ge, ":x_pos", 950),
					(assign, ":x_pos", 25),
					(val_sub, ":y_pos", 23),
					###################################################################################################################
					#   END REPORT LINE GENERATION								   												      #
					###################################################################################################################
			(try_end),

		###################################################################################################################
		#   START REPORT LINE GENERATION								   												  #
		###################################################################################################################
		#Total Debt
		(val_add, ":x_pos", 110), 
		(val_sub, ":y_pos", 30), 
		(str_store_string, s1, "@Total Debt"),
		(create_text_overlay, reg1, s1, tf_left_align),
	    (position_set_x, pos3, ":x_pos"),
	    (position_set_y, pos3, ":y_pos"),
	    (overlay_set_position, reg1, pos3),
		(position_set_x, pos3, 750),
		(position_set_y, pos3, 850),
		(overlay_set_size, reg1, pos3),

		#total loans ":tottal_debt"
		(val_add, ":x_pos", 230), 
		(assign, reg6, ":tottal_debt"),
		(str_store_string, s1, "@{reg6}"),
		(create_text_overlay, reg1, s1, tf_left_align),
	    (position_set_x, pos3, ":x_pos"),
	    (position_set_y, pos3, ":y_pos"),
	    (overlay_set_position, reg1, pos3),
		(position_set_x, pos3, 750),
		(position_set_y, pos3, 850),
		(overlay_set_size, reg1, pos3),

		#total loans inte3rest ":tottal_debt_interest"
		(val_add, ":x_pos", 115), 
		(assign, reg6, ":tottal_debt_interest"),
		(str_store_string, s1, "@{reg6}"),
		(create_text_overlay, reg1, s1, tf_left_align),
	    (position_set_x, pos3, ":x_pos"),
	    (position_set_y, pos3, ":y_pos"),
	    (overlay_set_position, reg1, pos3),
		(position_set_x, pos3, 750),
		(position_set_y, pos3, 850),
		(overlay_set_size, reg1, pos3),
	   	 
		#Total Deposit
		(val_sub, ":x_pos", 250), 
		(val_sub, ":y_pos", 30), 
		(str_store_string, s1, "@Total Deposits"),
		(create_text_overlay, reg1, s1, tf_left_align),
	    (position_set_x, pos3, ":x_pos"),
	    (position_set_y, pos3, ":y_pos"),
	    (overlay_set_position, reg1, pos3),
		(position_set_x, pos3, 750),
		(position_set_y, pos3, 850),
		(overlay_set_size, reg1, pos3),

		#total deposits ":tottal_deposit"
		(val_add, ":x_pos", 250), 
		(assign, reg6, ":tottal_deposit"),
		(str_store_string, s1, "@{reg6}"),
		(create_text_overlay, reg1, s1, tf_left_align),
	    (position_set_x, pos3, ":x_pos"),
	    (position_set_y, pos3, ":y_pos"),
	    (overlay_set_position, reg1, pos3),
		(position_set_x, pos3, 750),
		(position_set_y, pos3, 850),
		(overlay_set_size, reg1, pos3),

	  	#total deposits inte3rest ":tottal_deposit_interest"
		(val_add, ":x_pos", 115), 
		(assign, reg6, ":tottal_deposit_interest"),
		(str_store_string, s1, "@{reg6}"),
		(create_text_overlay, reg1, s1, tf_left_align),
	    (position_set_x, pos3, ":x_pos"),
	    (position_set_y, pos3, ":y_pos"),
	    (overlay_set_position, reg1, pos3),
		(position_set_x, pos3, 750),
		(position_set_y, pos3, 850),
		(overlay_set_size, reg1, pos3),
			
		###################################################################################################################
		#   END REPORT LINE GENERATION								   												      #
		###################################################################################################################	

		(assign, "$g_apply_Kaoses_bank_report_to_gold", 0),
	]
), 


#Check for buttonpress
     (ti_on_presentation_event_state_change,
	      [
				(presentation_set_duration, 0),
		  ]
	 ),

		 (ti_on_presentation_run,
		       [
			       (try_begin),
				   (this_or_next|key_clicked, key_escape),
				   (key_clicked, key_right_mouse_button),
				   (presentation_set_duration, 0),
				   (jump_to_menu, "mnu_reports"),
		        ]
		  ),


     ]
),
########################################################################################################################
#  KAOS BANKING KIT END																							       #
########################################################################################################################
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