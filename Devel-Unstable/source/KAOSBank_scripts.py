# Banking (2.0) by Lazeras
# Released 1 December 2011
from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from ID_animations import *

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

# Manualy all lines under the `scripts` into the bottom of the module_scripts at the bottom of the file
scripts = [
########################################################################################################################
#  KAOS BANKING KIT START																							   #
########################################################################################################################

  # script_bank_update_business
  # Script for updating banking numbers
  # Input: none
  # Output: none
  ("bank_update_business",
    [
       		(try_begin),
				(eq, "$bank_availability", 0),
			    (party_set_slot,"$current_town",slot_town_bank_debt,"$g_player_debt"),
	   			(party_set_slot,"$current_town",slot_town_bank_deposit,"$g_player_deposit"),
       		(else_try),
				(eq, "$bank_availability", 1),
			    (store_faction_of_party, ":centre_faction", "$current_town"),
			    (party_set_slot,":centre_faction",slot_town_bank_debt,"$g_player_debt"),
			    (party_set_slot,":centre_faction",slot_town_bank_deposit,"$g_player_deposit"),
       		(try_end), 
    ]
   ), 
  # script_bank_get_tottal_wealth
  # Script for getting a players tottal wealth
  # Input: none
  # Output: reg0 = player_deposit_tottal
  ("bank_get_tottal_wealth",
    [
    		(assign, ":player_deposit_tottal", 0),
       		(try_begin),
			   (eq, "$bank_availability", 0),
			   (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),	  
				    (party_get_slot, ":has_bank", ":center_no", slot_town_has_bank),
				    (eq, ":has_bank", 1),     
		   		    (party_get_slot,":player_deposit",":center_no",slot_town_bank_deposit),
			   		(val_add, ":player_deposit_tottal", ":player_deposit"),
		       (try_end),
       		(else_try),
				(eq, "$bank_availability", 1),
			   (try_for_range, ":faction", kingdoms_begin, kingdoms_end),	  
				    (party_get_slot, ":has_bank", ":center_no", slot_town_has_bank),
				    (eq, ":has_bank", 1),     
		   		    (party_get_slot,":player_deposit",":faction",slot_town_bank_deposit),
			   		(val_add, ":player_deposit_tottal", ":player_deposit"),
		       (try_end),
       		(try_end), 
       		(assign, reg0, ":player_deposit_tottal"),
    ]
   ), 

  # script_bank_get_prosperity_extra_to_s49
  # Script gets extra prosperity information for the presentation
  # Input: arg1 = center_no
  # Output: returns a string to s49
  ("bank_get_prosperity_extra_to_s49",
    [
	     (store_script_param, ":center_no", 1),
	     (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
	     (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
         (assign, ":max_skill", reg0),
	     (store_div, ":prosperity_div", ":prosperity", 20),
         (assign, reg30, ":prosperity"),
	     (str_clear, s49),
	     (try_begin),
	       (eq, ":prosperity_div", 0), #0..19
	       (try_begin),
	       		(ge, ":max_skill", 5),
	       		(str_store_string, s49, "@Rating {reg30}"),
	       (else_try),
	       		(ge, ":max_skill", 1),
	       		(str_store_string, s49, "@0..19"),
	       (try_end),
	     (else_try),
	       (eq, ":prosperity_div", 1), #20..39
	       (str_store_string, s49, "@Poor"),
	       (try_begin),
	       		(ge, ":max_skill", 5),
	       		(str_store_string, s49, "@Rating {reg30}"),
	       (else_try),
	       		(ge, ":max_skill", 1),
	       		(str_store_string, s49, "@20..39"),
	       (try_end),
	     (else_try),
	       (eq, ":prosperity_div", 2), #40..59
	       (str_store_string, s49, "@Average"),
	       (try_begin),
	       		(ge, ":max_skill", 5),
	       		(str_store_string, s49, "@Rating {reg30}"),
	       (else_try),
	       		(ge, ":max_skill", 1),
	       		(str_store_string, s49, "@40..59"),
	       (try_end),
	     (else_try),
	       (eq, ":prosperity_div", 3), #60..79
	       (str_store_string, s49, "@Rich"),
	       (try_begin),
	       		(ge, ":max_skill", 5),
	       		(str_store_string, s49, "@Rating {reg30}"),
	       (else_try),
	       		(ge, ":max_skill", 1),
	       		(str_store_string, s49, "@60..79"),
	       (try_end),
	     (else_try),
	       (try_begin),
	       		(ge, ":max_skill", 5),
	       		(str_store_string, s49, "@Rating {reg30}"),
	       (else_try),
	       		(ge, ":max_skill", 1),
	       		(str_store_string, s49, "@80+"),
	       (try_end),
	     (try_end),
    ]
   ), 

  # script_bank_report_rates
  # Script calculates the current rates by applying prosperity changes to base rates
  # Input: arg1 = center_no, arg2 = class_no
  # Output: reg0 = player_debt_interest_rate,  reg1 = player_deposit_interest_rate   
  ("bank_report_rates",
    [
	   (store_script_param, ":center_no", 1),

       (assign, ":prosperity", 0),
       (assign, ":player_faction_relation", 0),
	   (assign, ":player_debt_interest_rate", "$g_bank_debt_interest_rate"),
	   (assign, ":player_deposit_interest_rate", "$g_bank_deposit_interest_rate"),
	   (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
	   (call_script, "script_get_center_ideal_prosperity", ":center_no"),
	   (assign, ":ideal_prosperity", reg0),
	   (store_sub, ":pros_dif", ":prosperity", ":ideal_prosperity"),
	   (store_faction_of_party, ":centre_faction", ":center_no"), 
	   (party_get_slot, ":player_relation", ":center_no", slot_center_player_relation),
	   (store_relation, ":player_faction_relation", ":centre_faction", "fac_player_supporters_faction"),
	   (party_get_slot,":debt_effect",":center_no",slot_town_bank_debt_repayment_effect),
	   (party_get_slot,":player_deposit",":center_no",slot_town_bank_deposit),

		##############################################################################	   
		#  USE PROSPERITY RANGES TO OBTAIN INTEREST MODIFIERS
		##############################################################################
	    (store_div, ":prosperity_div", ":prosperity", 20),
        (try_begin),
		# Very Poor PROSPERITY
          (eq, ":prosperity_div", 0), #0..19
		  (try_begin),
			  (lt, ":prosperity", 5),
			  (assign, ":player_prosperity_debt_effect", 15),
			  (assign, ":player_prosperity_deposit_effect", -4),
		  (else_try),
			  (lt, ":prosperity", 10),
			  (assign, ":player_prosperity_debt_effect", 14),
			  (assign, ":player_prosperity_deposit_effect", -4),
		  (else_try),
			  (lt, ":prosperity", 14),
			  (assign, ":player_prosperity_debt_effect", 13),
			  (assign, ":player_prosperity_deposit_effect", -3),
		  (else_try),
			  (assign, ":player_prosperity_debt_effect", 12),
			  (assign, ":player_prosperity_deposit_effect", -3),
		  (try_end),
        (else_try),
		#Poor PROSPERITY
          (eq, ":prosperity_div", 1), #20..39
		  (try_begin),
			  (lt, ":prosperity", 25),
			  (assign, ":player_prosperity_debt_effect", 12),
			  (assign, ":player_prosperity_deposit_effect", -3),
		  (else_try),
			  (lt, ":prosperity", 30),
			  (assign, ":player_prosperity_debt_effect", 12),
			  (assign, ":player_prosperity_deposit_effect", -3),
		  (else_try),
			  (lt, ":prosperity", 35),
			  (assign, ":player_prosperity_debt_effect", 11),
			  (assign, ":player_prosperity_deposit_effect", -2),
		  (else_try),
			  (assign, ":player_prosperity_debt_effect", 11),
			  (assign, ":player_prosperity_deposit_effect", -2),
		  (try_end),
        (else_try),
		#Average PROSPERITY
          (eq, ":prosperity_div", 2), #40..59
		  (try_begin),
			  (lt, ":prosperity", 45),
			  (assign, ":player_prosperity_debt_effect", 11),
			  (assign, ":player_prosperity_deposit_effect", -1),
		  (else_try),
			  (lt, ":prosperity", 50),
			  (assign, ":player_prosperity_debt_effect", 11),
			  (assign, ":player_prosperity_deposit_effect", -1),
		  (else_try),
			  (lt, ":prosperity", 55),
			  (assign, ":player_prosperity_debt_effect", 10),
			  (assign, ":player_prosperity_deposit_effect", 0),
		  (else_try),
			  (assign, ":player_prosperity_debt_effect", 10),
			  (assign, ":player_prosperity_deposit_effect", 0),
		  (try_end),
        (else_try),
		# Rich PROSPERITY
          (eq, ":prosperity_div", 3), #60..79
		  (try_begin),
			  (lt, ":prosperity", 45),
			  (assign, ":player_prosperity_debt_effect", 9),
			  (assign, ":player_prosperity_deposit_effect", 0),
		  (else_try),
			  (lt, ":prosperity", 50),
			  (assign, ":player_prosperity_debt_effect", 9),
			  (assign, ":player_prosperity_deposit_effect", 1),
		  (else_try),
			  (lt, ":prosperity", 55),
			  (assign, ":player_prosperity_debt_effect", 8),
			  (assign, ":player_prosperity_deposit_effect", 1),
		  (else_try),
			  (assign, ":player_prosperity_debt_effect", 8),
			  (assign, ":player_prosperity_deposit_effect", 1),
		  (try_end),
        (else_try),
		# Very Rich PROSPERITY
		  (try_begin),
			  (lt, ":prosperity", 85),
			  (assign, ":player_prosperity_debt_effect", 8),
			  (assign, ":player_prosperity_deposit_effect", 1),
		  (else_try),
			  (lt, ":prosperity", 90),
			  (assign, ":player_prosperity_debt_effect", 7),
			  (assign, ":player_prosperity_deposit_effect", 2),
		  (else_try),
			  (lt, ":prosperity", 95),
			  (assign, ":player_prosperity_debt_effect", 7),
			  (assign, ":player_prosperity_deposit_effect", 2),
		  (else_try),
			  (assign, ":player_prosperity_debt_effect", 7),
			  (assign, ":player_prosperity_deposit_effect", 3),
		  (try_end),
        (try_end),

        # ADD the prosperity factors to the deposit and debt rates
        (val_add, ":player_debt_interest_rate",":player_prosperity_debt_effect"),
        (val_add, ":player_deposit_interest_rate",":player_prosperity_deposit_effect"),

		   #########################################################################
		   # Determine prosperity effect
		   #########################################################################
		  (try_begin),
				(gt, ":pros_dif", 80),
				(assign, ":dif_effect", 10),
		  (else_try),
				(gt, ":pros_dif", 60),
				(assign, ":dif_effect", 8),
		  (else_try),
				(gt, ":pros_dif", 40),
				(assign, ":dif_effect", 6),
		  (else_try),
				(gt, ":pros_dif", 20),
				(assign, ":dif_effect", 4),
		  (else_try),
				(gt, ":pros_dif", 10),
				(assign, ":dif_effect", 2),
		  (else_try),
				(assign, ":dif_effect", 0),
		  (try_end),
		#SUBTRACT the effect of too large a deposit from the interest rate
		(store_sub, ":player_deposit_interest_rate", ":player_deposit_interest_rate", ":dif_effect"),


		   #########################################################################
		   # Modify Interest Rate depending on center relation
		   #########################################################################
		   (try_begin),
				(le, ":player_relation", -5), 
				(store_random_in_range, ":random_relation_interest_effect", -3, -7),
				(val_add, ":player_deposit_interest_rate", ":random_relation_interest_effect"),
			(else_try),
				(le, ":player_relation", 0), 
				(store_random_in_range, ":random_relation_interest_effect", -1, -3),
				(val_add, ":player_deposit_interest_rate", ":random_relation_interest_effect"),

			(else_try),
				(le, ":player_relation", 5), 
				(store_random_in_range, ":random_relation_interest_effect", 0, 2),
				(val_add, ":player_deposit_interest_rate",0),
			(else_try),
				(le, ":player_relation", 10), 
				(store_random_in_range, ":random_relation_interest_effect", 0, 3),
				(val_add, ":player_deposit_interest_rate", ":random_relation_interest_effect"),
			(try_end),

		   #########################################################################
		   # If debt repayments have been missed decrease deposit interest rate
		   #########################################################################
			(try_begin),
				(ge, ":debt_effect", 3),
				(store_random_in_range, ":random_nonpayment_interest_effect", 2, 4),
				(val_add, ":player_debt_interest_rate", ":random_nonpayment_interest_effect"),
				(val_sub, ":player_deposit_interest_rate", ":random_nonpayment_interest_effect"),

			(else_try),
				(ge, ":debt_effect", 2),
				(store_random_in_range, ":random_nonpayment_interest_effect", 1, 2),
				(val_add, ":player_debt_interest_rate", ":random_nonpayment_interest_effect"),	
				(val_sub, ":player_deposit_interest_rate", ":random_nonpayment_interest_effect"),
			(else_try),
				(ge, ":debt_effect", 1),
				(store_random_in_range, ":random_nonpayment_interest_effect", 0, 2),
				(val_add, ":player_debt_interest_rate", ":random_nonpayment_interest_effect"),
				(val_sub, ":player_deposit_interest_rate", ":random_nonpayment_interest_effect"),	
			(try_end),

	   #Modify interest rate depending on faction relations
	   (try_begin),
		   (neq, "fac_player_supporters_faction", ":centre_faction"),
		   (try_begin),
				(le, ":player_faction_relation", -40), 
				(store_random_in_range, ":random_relation_interest_effect", -5, -10),	
				(val_add, ":player_deposit_interest_rate", ":random_relation_interest_effect"),
				(store_mul, ":player_debt_interest_rate", ":player_debt_interest_rate", 2),
			(else_try),
				(le, ":player_faction_relation", -20), 
				(store_random_in_range, ":random_relation_interest_effect", -3, -7),
				(val_add, ":player_deposit_interest_rate", ":random_relation_interest_effect"),
			(else_try),
				(le, ":player_faction_relation", -10), 
				(store_random_in_range, ":random_relation_interest_effect", -1, -5),
				(val_add, ":player_deposit_interest_rate", ":random_relation_interest_effect"),
			(else_try),
				(le, ":player_faction_relation", 0), 
				(val_add, ":player_deposit_interest_rate",1),
			(else_try),
				(ge, ":player_faction_relation", 20), 
				(store_random_in_range, ":random_relation_interest_effect", 5, 10),
				(val_add, ":player_deposit_interest_rate", ":random_relation_interest_effect"),
				(val_sub, ":player_debt_interest_rate", 4),
			(else_try),
				(ge, ":player_faction_relation", 10), 
				(store_random_in_range, ":random_relation_interest_effect", 0, 5),
				(val_add, ":player_deposit_interest_rate", ":random_relation_interest_effect"),
				(val_sub, ":player_debt_interest_rate", 2),
			(try_end),
		(try_end),

	   #########################################################################
	   # Reduce interest rate by the difference between center wealth and player deposits. The biger the deposit than center wealth the more the interest rate declines
	   #########################################################################
		(party_get_slot, ":wealth", ":center_no", slot_town_wealth),
		(val_mul, ":wealth", 10),
	    (assign, reg6, ":wealth"),
		(try_begin),
			(gt, ":player_deposit", ":wealth"),
			(store_div, ":wealth_modifier", ":player_deposit", ":wealth"),
		(else_try),
		    (assign, ":wealth_modifier", 0),
		(try_end),

		(try_begin),
			(gt, ":wealth_modifier", 0),
			(store_sub, ":player_deposit_interest_rate", ":player_deposit_interest_rate", ":wealth_modifier"),
		(try_end),

	   #########################################################################
	   # If player faction is not the same as center faction increase interest rate else reduce interest rate
	   #########################################################################
		(try_begin),
			(eq, ":centre_faction", "fac_player_supporters_faction"),
			(val_add, ":player_deposit_interest_rate", 1),
		(else_try),
			(val_sub, ":player_deposit_interest_rate", 1),
		(try_end),

#####################  debugging messages ################################
      (try_begin),		
			(eq, "$kaos_debug_mode", 1),
			(assign, reg21, ":player_debt_interest_rate"),	
			(assign, reg22, ":player_deposit_interest_rate"),	
			(display_log_message, "@{!}script get rates player_debt_interest_rate {reg21}   player_deposit_interest_rate {reg22} ", 0xFF0000),
      (try_end),		
#####################  debugging messages ################################

		#Return values
	    (assign, reg0, ":player_debt_interest_rate"),
	    (assign, reg1, ":player_deposit_interest_rate"),
    ]
   ), 

  # script_bank_report_deposit
  # Script calculates the interest earned on deposits with the supplied rates. 
  # Also calculates the random liege tax
  # Input: arg1 = center_no, arg2 = player_deposit_interest_rate
  # Output: reg0 = player_deposit_interest,  reg1 =  player_deposit, reg2 = liege_tax
  ("bank_report_deposit",
    [
	    (store_script_param_1, ":center_no"),
		(store_script_param_2, ":player_deposit_interest_rate"),

	   (party_get_slot,":player_deposit",":center_no",slot_town_bank_deposit),
	   (party_get_slot, ":centre_owner", ":center_no", slot_town_lord),
	   (call_script, "script_troop_get_player_relation", ":centre_owner"),
	   (assign, ":player_owner_relation", reg0),
	   ## Devide debt by 100 to obtain 1 percent of tottal debt
	   (store_div, ":player_deposit_onepercent",":player_deposit",100),
	   (store_mul, ":player_deposit_interest", ":player_deposit_onepercent", ":player_deposit_interest_rate"),
	   (store_div, ":player_deposit_interest", ":player_deposit_interest", 12),
		
	   #########################################################################
	   # If relation with lord is to low random chance of him taxing deposits
	   #########################################################################
		(try_begin),
		   	(ge, "$g_apply_Kaoses_bank_report_to_gold", 1),
			(le, ":player_owner_relation", -6),
			(store_random_in_range, ":random_chance", 0, 9),
			(try_begin),
				(le, ":random_chance", 4),
				(store_mul, ":liege_tax", ":player_deposit_onepercent",":random_chance"),
			(try_end),
		(else_try),
		   	(ge, "$g_apply_Kaoses_bank_report_to_gold", 1),
			(le, ":player_owner_relation", -1),
			(store_random_in_range, ":random_chance", 0, 9),
			(try_begin),
				(le, ":random_chance", 2),
				(store_mul, ":liege_tax", ":player_deposit_onepercent",":random_chance"),
			(try_end),
		(try_end),


		(try_begin),
			(gt, ":liege_tax" , 0),
   			(ge, "$g_apply_Kaoses_bank_report_to_gold", 1),
			(val_sub, ":player_deposit", ":liege_tax"),	
		    (assign, reg6, ":liege_tax"),
			(str_store_party_name, s9, ":center_no"),
			(str_store_troop_name, s8, ":centre_owner"),
			(display_log_message, "@Due to the bad relation you have with {s8} you have lost {reg6} of your deposit at {s9}", 0xFF0000),
		(try_end),

	   #########################################################################
	   # Store all calculated values
	   #########################################################################
	   (try_begin),
	   			(ge, "$g_apply_Kaoses_bank_report_to_gold", 1),
	   			(val_add, ":player_deposit", ":player_deposit_interest"),
		        (party_set_slot,":center_no",slot_town_bank_deposit,":player_deposit"),
	   (try_end),

		#Return values
	    (assign, reg0, ":player_deposit_interest"),
	    (assign, reg1, ":player_deposit"),
	    (assign, reg2, ":liege_tax"),
    ]
   ), 

  # script_bank_report_debt
  # Script calculates the interest earned on deposits with the supplied rates. 
  # Also calculates the random liege tax
  # Input: arg1 = center_no, arg2 = player_debt_interest_rate
  # Output: reg0 = player_debt_interest,  reg1 = player_debt
  ("bank_report_debt",
    [
	    (store_script_param_1, ":center_no"),

		(store_script_param_2, ":player_debt_interest_rate"),
	    (party_get_slot,":player_debt",":center_no",slot_town_bank_debt),
	    (store_div, ":player_debt_onepercent",":player_debt",100),

	    (store_mul, ":player_debt_interest", ":player_debt_interest_rate",":player_debt_onepercent"),
	    (store_div, ":player_debt_interest", ":player_debt_interest", 12),

	    (try_begin),
	   			(ge, "$g_apply_Kaoses_bank_report_to_gold", 1),
	   			(val_add,":player_debt",":player_debt_interest"),
			    (party_set_slot,":center_no",slot_town_bank_debt,":player_debt"),
	    (try_end),

		#Return values
        (assign, reg0, ":player_debt_interest"),
   	    (assign, reg1, ":player_debt"),
    ]
   ), 

  # script_cf_bank_war_tax
  # Script applies a war tax on deposits if player or player faction is at war with the banks center. 
  # Input: arg1 = center_no 
  # Output: reg0 = player_debt_interest,  reg1 = player_debt
  ("cf_bank_war_tax",
    [
	   (store_script_param_1, ":center_no"),

	   (store_faction_of_party, ":centre_faction", ":center_no"),
	   (store_faction_of_party, ":player_faction", "trp_player"),
	   (store_relation, ":player_faction_relation", ":player_faction", ":centre_faction"),
	   (party_get_slot,":player_deposit",":center_no",slot_town_bank_deposit),
	   (store_div, ":player_deposit_onepercent",":player_deposit",100),
	   (str_store_party_name,s9, ":center_no"),
	   (str_store_faction_name, s10, ":centre_faction"),
	   (gt, ":player_deposit", 0),
       (assign, ":war_tax", 0),
	   (try_begin),
		   (neq, ":player_faction", ":centre_faction"),
		   (try_begin),
				(le, ":player_faction_relation", -40), 
				(store_random_in_range, ":random_deposit_effect", 50, 100),
				(store_mul, ":war_tax",":player_deposit_onepercent", ":random_deposit_effect"),
			(else_try),
				(le, ":player_faction_relation", -20), 
				(store_random_in_range, ":random_deposit_effect", 25, 75),
				(store_mul, ":war_tax",":player_deposit_onepercent", ":random_deposit_effect"),
			(else_try),
				(le, ":player_faction_relation", -10), 
				(store_random_in_range, ":random_deposit_effect", 15, 35),
				(store_mul, ":war_tax",":player_deposit_onepercent", ":random_deposit_effect"),
			(try_end),
		(try_end),
		(try_begin),
			(ge, ":war_tax", 0),
   			(ge, "$g_apply_Kaoses_bank_report_to_gold", 1),
			(val_sub, ":player_deposit", ":war_tax"),
            (party_set_slot,":center_no",slot_town_bank_deposit,":player_deposit"),
			(assign, reg6, ":war_tax"),
			(str_store_party_name, s9, ":center_no"),
			(str_store_faction_name, s10, ":player_faction"),
			(display_log_message, "@Due to the status of war between your faction and {s10} you have lost {reg6} Denars as a war tax from {s9}", 0xFF0000),
		(try_end),
    ]
   ), 

  # script_convert_to_faction
  # Script convert center banking to faction banking
  # Not currently implemented is a work in progress, need
  # to change game menus and presentation
  # Input: 
  # Output: 
  ("convert_to_faction",
    [
	   (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),	  
		    (party_get_slot, ":has_bank", ":center_no", slot_town_has_bank),
		    (eq, ":has_bank", 1),     
	   		(store_faction_of_party, ":centre_faction", ":center_no"),
	   		(party_get_slot,":player_debt",":center_no",slot_town_bank_debt),
   		    (party_get_slot,":player_deposit",":center_no",slot_town_bank_deposit),
	   		(party_get_slot,":debt_effect",":center_no",slot_town_bank_debt_repayment_effect),

	   		(party_get_slot,":fac_player_debt",":centre_faction",slot_town_bank_debt),
   		    (party_get_slot,":fac_player_deposit",":centre_faction",slot_town_bank_deposit),
	   		(party_get_slot,":fac_debt_effect",":centre_faction",slot_town_bank_debt_repayment_effect),

	   		(val_add, ":fac_player_debt", ":player_debt"),
	   		(val_add, ":fac_player_deposit", ":player_deposit"),
	   		(val_add, ":fac_debt_effect", ":debt_effect"),

            (party_set_slot,":centre_faction",slot_town_bank_debt,":fac_player_debt"),
            (party_set_slot,":centre_faction",slot_town_bank_deposit,":fac_player_deposit"),
            (party_set_slot,":centre_faction",slot_town_bank_debt_repayment_effect,":fac_debt_effect"),
       (try_end),
    ]
   ), 

  # script_convert_to_center
  # Script convert faction banking to center banking
  # Not currently implemented is a work in progress, need
  # to change game menus and presentation
  # Input: 
  # Output: 
  ("convert_to_center",
    [
	   (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),	  
		   (this_or_next|eq,":center_no","p_town_1"),
		   (this_or_next|eq,":center_no","p_town_5"),
		   (this_or_next|eq,":center_no","p_town_6"),
		   (this_or_next|eq,":center_no","p_town_8"),
		   (this_or_next|eq,":center_no","p_town_19"),
		   (eq,":center_no","p_town_10"),
		   (party_set_slot,":center_no", slot_town_has_bank,1),
    
	   		(store_faction_of_party, ":centre_faction", ":center_no"),
	   		(party_get_slot,":fac_player_debt",":centre_faction",slot_town_bank_debt),
   		    (party_get_slot,":fac_player_deposit",":centre_faction",slot_town_bank_deposit),
	   		(party_get_slot,":fac_debt_effect",":centre_faction",slot_town_bank_debt_repayment_effect),

            (party_set_slot,":center_no",slot_town_bank_debt,":fac_player_debt"),
            (party_set_slot,":center_no",slot_town_bank_deposit,":fac_player_deposit"),
            (party_set_slot,":center_no",slot_town_bank_debt_repayment_effect,":fac_debt_effect"),
       (try_end),
    ]
   ), 




  # script_bank_report_faction_deposit
  # Script calculates the interest earned on deposits with the supplied rates. 
  # Also calculates the random liege tax
  # Input: arg1 = faction, arg2 = player_deposit_interest_rate
  # Output: reg0 = player_deposit_interest,  reg1 =  player_deposit, reg2 = liege_tax
  ("bank_report_faction_deposit",
    [
	    (store_script_param_1, ":faction"),
		(store_script_param_2, ":player_deposit_interest_rate"),

	   (party_get_slot,":player_deposit",":faction",slot_town_bank_deposit),
	   (faction_get_slot, ":king", ":faction", slot_faction_leader),
	   (call_script, "script_troop_get_player_relation", ":king"),
	   (assign, ":player_owner_relation", reg0),
	   ## Devide debt by 100 to obtain 1 percent of tottal debt
	   (store_div, ":player_deposit_onepercent",":player_deposit",100),
	   (store_mul, ":player_deposit_interest", ":player_deposit_onepercent", ":player_deposit_interest_rate"),
	   (store_div, ":player_deposit_interest", ":player_deposit_interest", 12),
		
	   #########################################################################
	   # If relation with lord is to low random chance of him taxing deposits
	   #########################################################################
		(try_begin),
		   	(ge, "$g_apply_Kaoses_bank_report_to_gold", 1),
			(le, ":player_owner_relation", -6),
			(store_random_in_range, ":random_chance", 0, 9),
			(try_begin),
				(le, ":random_chance", 4),
				(store_mul, ":liege_tax", ":player_deposit_onepercent",":random_chance"),
			(try_end),
		(else_try),
		   	(ge, "$g_apply_Kaoses_bank_report_to_gold", 1),
			(le, ":player_owner_relation", -1),
			(store_random_in_range, ":random_chance", 0, 9),
			(try_begin),
				(le, ":random_chance", 2),
				(store_mul, ":liege_tax", ":player_deposit_onepercent",":random_chance"),
			(try_end),
		(try_end),


		(try_begin),
			(gt, ":liege_tax" , 0),
   			(ge, "$g_apply_Kaoses_bank_report_to_gold", 1),
			(val_sub, ":player_deposit", ":liege_tax"),	
		    (assign, reg6, ":liege_tax"),
		    (str_store_troop_name, s8, ":king"),
			(display_log_message, "@Due to the bad relation you have with {s8} you have lost {reg6} of your deposit ", 0xFF0000),
		(try_end),

	   #########################################################################
	   # Store all calculated values
	   #########################################################################
	   (try_begin),
	   			(ge, "$g_apply_Kaoses_bank_report_to_gold", 1),
	   			(val_add, ":player_deposit", ":player_deposit_interest"),
		        (party_set_slot,":faction",slot_town_bank_deposit,":player_deposit"),
	   (try_end),

		#Return values
	    (assign, reg0, ":player_deposit_interest"),
	    (assign, reg1, ":player_deposit"),
	    (assign, reg2, ":liege_tax"),
    ]
   ), 

  # script_bank_report_faction_debt
  # Script calculates the interest earned on deposits with the supplied rates. 
  # Also calculates the random liege tax
  # Input: arg1 = faction, arg2 = player_debt_interest_rate
  # Output: reg0 = player_debt_interest,  reg1 = player_debt
  ("bank_report_faction_debt",
    [
	    (store_script_param_1, ":faction"),
		(store_script_param_2, ":player_debt_interest_rate"),

	    (party_get_slot,":player_debt",":faction",slot_town_bank_debt),
	    (store_div, ":player_debt_onepercent",":player_debt",100),

	    (store_mul, ":player_debt_interest", ":player_debt_interest_rate",":player_debt_onepercent"),
	    (store_div, ":player_debt_interest", ":player_debt_interest", 12),

	    (try_begin),
	   			(ge, "$g_apply_Kaoses_bank_report_to_gold", 1),
	   			(val_add,":player_debt",":player_debt_interest"),
			    (party_set_slot,":faction",slot_town_bank_debt,":player_debt"),
	    (try_end),

		#Return values
        (assign, reg0, ":player_debt_interest"),
   	    (assign, reg1, ":player_debt"),
    ]
   ), 

  # script_cf_bank_war_faction_tax
  # Script applies a war tax on deposits if player or player faction is at war with the banks center. 
  # Input: arg1 = faction 
  # Output: reg0 = player_debt_interest,  reg1 = player_debt
  ("cf_bank_war_faction_tax",
    [
	   (store_script_param_1, ":centre_faction"),

	   (store_faction_of_party, ":player_faction", "trp_player"),
	   (store_relation, ":player_faction_relation", ":player_faction", ":centre_faction"),
	   (party_get_slot,":player_deposit",":centre_faction",slot_town_bank_deposit),
	   (store_div, ":player_deposit_onepercent",":player_deposit",100),
	   (gt, ":player_deposit", 0),
       (assign, ":war_tax", 0),
	   (try_begin),
		   (neq, ":player_faction", ":centre_faction"),
		   (try_begin),
				(le, ":player_faction_relation", -40), 
				(store_random_in_range, ":random_deposit_effect", 50, 100),
				(store_mul, ":war_tax",":player_deposit_onepercent", ":random_deposit_effect"),
			(else_try),
				(le, ":player_faction_relation", -20), 
				(store_random_in_range, ":random_deposit_effect", 25, 75),
				(store_mul, ":war_tax",":player_deposit_onepercent", ":random_deposit_effect"),
			(else_try),
				(le, ":player_faction_relation", -10), 
				(store_random_in_range, ":random_deposit_effect", 15, 35),
				(store_mul, ":war_tax",":player_deposit_onepercent", ":random_deposit_effect"),
			(try_end),
		(try_end),
		(try_begin),
			(ge, ":war_tax", 0),
   			(ge, "$g_apply_Kaoses_bank_report_to_gold", 1),
			(val_sub, ":player_deposit", ":war_tax"),
            (party_set_slot,":centre_faction",slot_town_bank_deposit,":player_deposit"),
			(assign, reg6, ":war_tax"),
			(str_store_faction_name, s10, ":centre_faction"),
			(display_log_message, "@Due to the status of war between your faction and {s10} you have lost {reg6} Denars as a war tax", 0xFF0000),
		(try_end),
    ]
   ), 





########################################################################################################################
#  KAOS BANKING KIT END																							       #
########################################################################################################################
] # scripts

# Manualy add these to module_scripts search for "process_sieges"
# add the lines in `process_sieges` insert after (ge, ":besieger_party", 0)
process_sieges = [
########################################################################################################################
#  KAOS BANKING KIT START																							   #
########################################################################################################################

       		(try_begin),
				(eq, "$bank_availability", 0),
	            (party_get_slot, ":has_bank", ":center_no", slot_town_has_bank),
				(try_begin),
					(eq, ":has_bank", 1),  
					(party_get_slot,":player_deposit",":center_no",slot_town_bank_deposit),
					(gt, ":player_deposit", 0),
					(str_store_party_name,s9, ":center_no"),
					(store_random_in_range, ":random_no", 5, 25),
					(store_div, ":deposit_percent", ":player_deposit", 100),
					(store_mul, ":siege_cost", ":deposit_percent", ":random_no"),
					(val_sub, ":player_deposit", ":siege_cost"),
					(party_set_slot,":center_no",slot_town_bank_deposit,":player_deposit"),
					(assign, reg6, ":siege_cost"),
					(assign, reg7, ":player_deposit"),
			        (display_log_message, "@{s9} Is under siege and you have lost {reg6} denars leaving a deposit of {reg7} Denars", 0xFF0000),  
				(try_end),
       		(else_try),
				(eq, "$bank_availability", 1),
			    (store_faction_of_party, ":centre_faction", ":center_no"),
					(party_get_slot,":player_deposit",":centre_faction",slot_town_bank_deposit),
					(gt, ":player_deposit", 0),
					(str_store_party_name,s9, ":center_no"),
					(store_random_in_range, ":random_no", 5, 25),
					(store_div, ":deposit_percent", ":player_deposit", 100),
					(store_mul, ":siege_cost", ":deposit_percent", ":random_no"),
					(val_sub, ":player_deposit", ":siege_cost"),
					(party_set_slot,":centre_faction",slot_town_bank_deposit,":player_deposit"),
					(assign, reg6, ":siege_cost"),
					(assign, reg7, ":player_deposit"),
			        (display_log_message, "@{s9} Is under siege and you have lost {reg6} denars leaving a deposit of {reg7} Denars", 0xFF0000),  
       		(try_end), 
########################################################################################################################
#  KAOS BANKING KIT END																							       #
########################################################################################################################
]

from util_wrappers import *
from util_scripts import *

# Manualy add these to module_scripts search for "game_start"
# add the lines in at the start of the script block
scripts_directives = [
	[SD_OP_BLOCK_INSERT, "game_start", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE, (faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),0,
	[
########################################################################################################################
#  KAOS BANKING KIT START																							   #
########################################################################################################################
		#only put banks in capitals
			 (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
				  (this_or_next|eq,":center_no","p_town_1"),
				  (this_or_next|eq,":center_no","p_town_5"),
				  (this_or_next|eq,":center_no","p_town_6"),
				  (this_or_next|eq,":center_no","p_town_8"),
				  (this_or_next|eq,":center_no","p_town_19"),
				  (eq,":center_no","p_town_10"),
				  (party_set_slot,":center_no", slot_town_has_bank,1),
			 (else_try),
				  (party_set_slot,":center_no", slot_town_has_bank,0),
			 (try_end),
			 (assign, "$g_apply_Kaoses_bank_report_to_gold", 0),
	   		 (assign, "$g_bank_debt_interest_rate", 14),
	   		 (assign, "$g_bank_deposit_interest_rate", 5),
	   		 #(assign, "$kaos_debug_mode", 0),
########################################################################################################################
#  KAOS BANKING KIT END																							       #
########################################################################################################################	
	], 15],

	[SD_OP_BLOCK_INSERT, "process_sieges", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER, (ge, ":besieger_party", 0),0,process_sieges],

]


# the following is a generic function expected by modmerger
# If not defined, it will only do the basic merging of adding the scripts in "scripts" to the orignal "scripts" in module_scripts.py
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "scripts"
        orig_scripts = var_set[var_name_1] # this is the ORIGINAL scripts from module_scripts.py

        # START do your own stuff to do merging

        # modify existing scripts according to script_directives above
        process_script_directives(orig_scripts, scripts_directives)

        add_objects(orig_scripts, scripts) # add new scripts, by default, scripts with same name will be replaced

        # END do your own stuff

    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
	