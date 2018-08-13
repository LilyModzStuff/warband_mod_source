# Banking (2.0) by Lazeras
# Released 1 December 2011
from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *
from module_constants import *

# Manualy all lines under the `simple_triggers` into the bottom of the module_simple_triggers at the bottom of the file
simple_triggers=[
########################################################################################################################
#  KAOS BANKING KIT START																							   #
########################################################################################################################
########################################################################################################################
#  Triggers the Banking report with apply changes active once a week.
########################################################################################################################
  (24 * 7,
   [
		(assign, "$g_apply_Kaoses_bank_report_to_gold", 1),
   		(try_begin),
			(eq, "$bank_availability", 0),
		    (start_presentation, "prsnt_Lazeras_bank_prsnt"),
		(else_try),
			(eq, "$bank_availability", 1),
		    (start_presentation, "prsnt_Lazeras_bank_faction_prsnt"),
   		(try_end),
   ]
  ),
	
########################################################################################################################
#  Once a day check if debt payment is overdue and if so apply penalties
########################################################################################################################
  (24,
   [
   		(try_begin),
			(eq, "$bank_availability", 0),
			(try_for_range, ":center_no", towns_begin, towns_end),
			   (party_get_slot, ":has_bank", ":center_no", slot_town_has_bank),
			   (party_get_slot,":player_debt",":center_no",slot_town_bank_debt),
			   (party_get_slot,":debt_effect",":center_no",slot_town_bank_debt_repayment_effect),
			   (eq, ":has_bank", 1),
			   (gt, ":player_debt", 0),
			   (str_store_party_name,s9, ":center_no"),     
			   (party_get_slot,":due_date",":center_no",slot_town_bank_debt_repayment_date),
			   (store_current_day, ":cur_day"),	
			   (store_sub, ":week_to_go", ":due_date", 7),
			   (party_get_slot, ":centre_owner", ":center_no", slot_town_lord),
			   (str_store_troop_name,s8,":centre_owner"),
			   
			   #########################################################################
			   # Checking for a week to go on a debt payment and notifying player
			   #########################################################################
			   (try_begin),
					(eq,":week_to_go",":cur_day"),
					(gt, ":player_debt", 0),
					(eq, ":debt_effect", 3),
					(display_log_message, "@A messenger informs you that you have a week to make a repayment of your debt .You have already missed the deadline multiple times"),
					(dialog_box, "@A messenger informs you that you have a week to make a repayment of you debt and that you have already missed severale payments "),
					#(display_log_message, "@ activated first try week to go!", 0xFF0000),
			   (else_try),
					(eq,":week_to_go",":cur_day"),
					(gt, ":player_debt", 0),
					(ge, ":debt_effect", 2),
					(display_log_message, "@A messenger informs you that you have a week to make a repayment of your debt .You have already missed the deadline more than once"),
					(dialog_box, "@A messenger informs you that you have a week to make a repayment of you debt and that you have already missed more than one payment "),
					#(display_log_message, "@ activated second try week to go!", 0xFF0000),
			   (else_try),
					(eq,":week_to_go",":cur_day"),
					(gt, ":player_debt", 0),
					(eq, ":debt_effect", 1),
					(display_log_message, "@A messenger informs you that you have a week to make a repayment of your debt. You have already missed the deadline once"),
					(dialog_box, "@A messenger informs you that you have a week to make a repayment of you debt and that you have already missed a payment"),
					#(display_log_message, "@ activated third try week to go!", 0xFF0000),
			   (else_try),
					(eq,":week_to_go",":cur_day"),
					(gt, ":player_debt", 0),
					(display_log_message, "@A messenger informs you that you have a week to make a repayment of your debt"),
					(dialog_box, "@A messenger informs you that you have a week to make a repayment of you debt "),
					#(display_log_message, "@ activated fourth try week to go!", 0xFF0000),
			   (try_end),

			   #########################################################################
			   # Checking if a debt payment is over due and if so apply penalties and inform player
			   #########################################################################	   
			   (try_begin),
					(eq,":cur_day",":due_date"),
					(gt,":player_debt", 0),
					(try_begin),
						(eq, ":debt_effect", 0),	
						(display_log_message, "@A messenger informs you that you have failed to make the required debt repayment and have lost 1 reputation with {s9} You have 20 days to make a payment "),
						(call_script, "script_change_player_relation_with_center", ":center_no", -1),
						(val_add, ":due_date", 20),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_effect, 2),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_date,":due_date"),
						#(display_log_message, "@ activated first try after due date!", 0xFF0000),				
					(else_try),
						(eq, ":debt_effect", 1),	
						(call_script, "script_change_player_relation_with_center", ":center_no", -1),
						(display_log_message, "@A messenger informs you that you have failed to make the required debt repayment and have lost 1 reputation with {s9} You have 20 days to make a payment "),
						(val_add, ":due_date", 20),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_effect, 2),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_date,":due_date"),	
						#(display_log_message, "@ activated second try after due date!", 0xFF0000),					
					(else_try),
						(eq, ":debt_effect", 2),
						(call_script, "script_change_player_relation_with_troop", ":centre_owner", -1),
						(call_script, "script_change_player_relation_with_center", ":center_no", -2),
						(display_log_message, "@A messenger informs you that you have failed to make the required debt repayment again and have lost 2 reputation with {s9} this has also caused you to lose 1 reputation with {s8} You have 15 days to make a payment "),	
						(val_add, ":due_date", 15),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_effect, 3),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_date,":due_date"),	
						#(display_log_message, "@ activated third try after due date!", 0xFF0000),			
					(else_try),
						(ge, ":debt_effect", 3),
						(call_script, "script_change_player_relation_with_troop", ":centre_owner", -2),
						(call_script, "script_change_player_relation_with_center", ":center_no", -3),
						(display_log_message, "@A messenger informs you that you have failed to make another required debt repayment again and have lost 3 reputation with {s9} this has also caused you to lose 1 reputation with {s8}. You have 15 days to make a payment "),	
						(val_add, ":due_date", 15),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_effect, 3),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_date,":due_date"),
						#(display_log_message, "@ activated forth try after due date!", 0xFF0000),	
				(try_end),
		   (try_end),
		(try_end),
		(else_try),
			(eq, "$bank_availability", 1),
			(try_for_range, ":faction", "fac_kingdom_1", kingdoms_end),
			   (party_get_slot,":player_debt",":faction",slot_town_bank_debt),
			   (party_get_slot,":debt_effect",":faction",slot_town_bank_debt_repayment_effect),
	   		   (faction_get_slot, ":king", ":faction", slot_faction_leader),
			   (gt, ":player_debt", 0),
			   (str_store_faction_name,s9, ":faction"),     
			   (party_get_slot,":due_date",":faction",slot_town_bank_debt_repayment_date),
			   (store_current_day, ":cur_day"),	
			   (store_sub, ":week_to_go", ":due_date", 7),
			   (str_store_troop_name,s8,":king"),
			   
			   #########################################################################
			   # Checking for a week to go on a debt payment and notifying player
			   #########################################################################
			   (try_begin),
					(eq,":week_to_go",":cur_day"),
					(gt, ":player_debt", 0),
					(eq, ":debt_effect", 3),
					(display_log_message, "@A messenger informs you that you have a week to make a repayment of your debt .You have already missed the deadline multiple times"),
					(dialog_box, "@A messenger informs you that you have a week to make a repayment of you debt and that you have already missed severale payments "),
					#(display_log_message, "@ activated first try week to go!", 0xFF0000),
			   (else_try),
					(eq,":week_to_go",":cur_day"),
					(gt, ":player_debt", 0),
					(ge, ":debt_effect", 2),
					(display_log_message, "@A messenger informs you that you have a week to make a repayment of your debt .You have already missed the deadline more than once"),
					(dialog_box, "@A messenger informs you that you have a week to make a repayment of you debt and that you have already missed more than one payment "),
					#(display_log_message, "@ activated second try week to go!", 0xFF0000),
			   (else_try),
					(eq,":week_to_go",":cur_day"),
					(gt, ":player_debt", 0),
					(eq, ":debt_effect", 1),
					(display_log_message, "@A messenger informs you that you have a week to make a repayment of your debt. You have already missed the deadline once"),
					(dialog_box, "@A messenger informs you that you have a week to make a repayment of you debt and that you have already missed a payment"),
					#(display_log_message, "@ activated third try week to go!", 0xFF0000),
			   (else_try),
					(eq,":week_to_go",":cur_day"),
					(gt, ":player_debt", 0),
					(display_log_message, "@A messenger informs you that you have a week to make a repayment of your debt"),
					(dialog_box, "@A messenger informs you that you have a week to make a repayment of you debt "),
					#(display_log_message, "@ activated fourth try week to go!", 0xFF0000),
			   (try_end),

			   #########################################################################
			   # Checking if a debt payment is over due and if so apply penalties and inform player
			   #########################################################################	   
			   (try_begin),
					(eq,":cur_day",":due_date"),
					(gt,":player_debt", 0),
					(try_begin),
						(eq, ":debt_effect", 0),	
						(display_log_message, "@A messenger informs you that you have failed to make the required debt repayment and have lost 1 reputation with {s9} You have 20 days to make a payment "),
						(call_script, "script_change_player_relation_with_center", ":center_no", -1),
						(val_add, ":due_date", 20),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_effect, 2),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_date,":due_date"),
						#(display_log_message, "@ activated first try after due date!", 0xFF0000),				
					(else_try),
						(eq, ":debt_effect", 1),	
						(call_script, "script_change_player_relation_with_center", ":center_no", -1),
						(display_log_message, "@A messenger informs you that you have failed to make the required debt repayment and have lost 1 reputation with {s9} You have 20 days to make a payment "),
						(val_add, ":due_date", 20),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_effect, 2),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_date,":due_date"),	
						#(display_log_message, "@ activated second try after due date!", 0xFF0000),					
					(else_try),
						(eq, ":debt_effect", 2),
						(call_script, "script_change_player_relation_with_troop", ":centre_owner", -1),
						(call_script, "script_change_player_relation_with_center", ":center_no", -2),
						(display_log_message, "@A messenger informs you that you have failed to make the required debt repayment again and have lost 2 reputation with {s9} this has also caused you to lose 1 reputation with {s8} You have 15 days to make a payment "),	
						(val_add, ":due_date", 15),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_effect, 3),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_date,":due_date"),	
						#(display_log_message, "@ activated third try after due date!", 0xFF0000),			
					(else_try),
						(ge, ":debt_effect", 3),
						(call_script, "script_change_player_relation_with_troop", ":centre_owner", -2),
						(call_script, "script_change_player_relation_with_center", ":center_no", -3),
						(display_log_message, "@A messenger informs you that you have failed to make another required debt repayment again and have lost 3 reputation with {s9} this has also caused you to lose 1 reputation with {s8}. You have 15 days to make a payment "),	
						(val_add, ":due_date", 15),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_effect, 3),
						(party_set_slot,":center_no",slot_town_bank_debt_repayment_date,":due_date"),
						#(display_log_message, "@ activated forth try after due date!", 0xFF0000),	
				(try_end),
		   (try_end),
   		(try_end),
    ]),
########################################################################################################################
#  KAOS BANKING KIT END																							       #
########################################################################################################################
]



from util_common import *
def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1127 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "simple_triggers"
		orig_simple_triggers = var_set[var_name_1]
		
		add_objects(orig_simple_triggers, simple_triggers, False)
		
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)