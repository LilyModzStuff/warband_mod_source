# Banking (2.0) by Lazeras
# Released 1 December 2011
from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *

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


# Manualy all lines under the `game_menus` into the bottom of the module_game_menus at the bottom
game_menus = [
########################################################################################################################
#  KAOS BANKING KIT START																							   #
########################################################################################################################
  ("Lazeras_banking_menu",0,
    "You visit the bank of {s1}.\
 Here you can deposit money and earn interest over time, or take a loan.\
 You currently have {reg6} denars deposited here.\
 You currently have {reg7} denars borrowed from this bank.",
    "none",
    [
	     (str_store_party_name,s1,"$current_town"),
	     (party_get_slot,"$g_player_debt","$current_town",slot_town_bank_debt),
	     (party_get_slot,"$g_player_deposit","$current_town",slot_town_bank_deposit),
	     (assign, reg6, "$g_player_deposit"),
	     (assign, reg7, "$g_player_debt"),
		 (str_store_party_name,s9, "$current_town"),
    ],
    [
      ("take_loan",
	  [
		  (store_troop_gold, ":player_wealth", "trp_player"),
		  (store_sub, ":player_real_wealth", ":player_wealth", "$g_player_debt"),
		  (gt,":player_real_wealth",100)
	  ],"Take a loan of 1000 denars.",
			[
			   (store_current_day, ":cur_day"),
			   (store_add, ":new_day", ":cur_day", 30),
			   (party_set_slot,"$current_town",slot_town_bank_debt_repayment_date,":new_day"),
			   (party_get_slot,":due_date","$current_town",slot_town_bank_debt_repayment_date),	
			   (assign, reg6, ":due_date"),
			   (display_log_message, "@{s9} Debt payment due in {reg6} days", 0xFF0000),
			   (troop_remove_gold, "trp_player", 100),
			   (troop_add_gold, "trp_player", 1000),
			   (val_add, "$g_player_debt", 1000),
			   (call_script, "script_bank_update_business"),
			   
			   (party_get_slot, ":wealth", "$current_town", slot_town_wealth),
			   (val_sub,":wealth", 10),
			   (party_set_slot, "$current_town", slot_town_wealth, ":wealth"),
			   (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
			   (val_sub,":prosperity", 3),
			   (party_set_slot, "$current_town", slot_town_prosperity, ":prosperity"),
			]),
      ("give_loan",
		  [
			  (store_troop_gold, ":player_wealth", "trp_player"),
			  (gt,":player_wealth",1000),
			  (gt,"$g_player_debt",1000)
		  ],
	   "Repay 1000 denars of your debt.",
       [
		  (troop_remove_gold, "trp_player", 1000),
		  (val_sub, "$g_player_debt", 1000),
		  (call_script, "script_bank_update_business"),
		  (store_current_day, ":cur_day"),
		  (store_add, ":due_date", ":cur_day", 30),
		  (party_set_slot,"$current_town",slot_town_bank_debt_repayment_effect, 0),
		  (try_begin),
			  (gt, "$g_player_debt", 0),
			  (party_set_slot,"$current_town",slot_town_bank_debt_repayment_date,":due_date"),
			  (assign, reg6, ":due_date"),
			  (display_log_message, "@Payment recieved Debt payment due in {reg6} days", 0xFF0000),
		  (else_try),
			  (party_set_slot,"$current_town",slot_town_bank_debt_repayment_date, 0),
			  (assign, reg6, ":due_date"),
			  (display_log_message, "@ You have no more debt owning", 0xFF0000),
		  (try_end),
			   (party_get_slot, ":wealth", "$current_town", slot_town_wealth),
			   (val_add,":wealth", 10),
			   (party_set_slot, "$current_town", slot_town_wealth, ":wealth"),
			   (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
			   (val_add,":prosperity", 3),
			   (party_set_slot, "$current_town", slot_town_prosperity, ":prosperity"),
        ]),
      ("give_loan_all",
			  [
			  (store_troop_gold, ":player_wealth", "trp_player"),
			  (gt,":player_wealth","$g_player_debt"),
			  (gt,"$g_player_debt",0)
		  ],
	   "Repay all of your debt.",
       [
		  (troop_remove_gold, "trp_player", "$g_player_debt"),
		  (val_sub, "$g_player_debt", "$g_player_debt"),
		  (call_script, "script_bank_update_business"),
		  (store_div, ":temp_holder", "$g_player_debt", 100),
		   (party_get_slot, ":wealth", "$current_town", slot_town_wealth),
		   (val_add,":wealth", ":temp_holder"),
		   (party_set_slot, "$current_town", slot_town_wealth, ":wealth"),
		   (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
		   (store_div, ":temp_holder", "$g_player_debt", 3),
		   (val_add,":prosperity", ":temp_holder"),
		   (party_set_slot, "$current_town", slot_town_prosperity, ":prosperity"),
        ]),
		
      ("give_deposit",
	  [
		  (store_troop_gold, ":player_wealth", "trp_player"),
		  (gt,":player_wealth",1000)
	  ],
	  "Deposit 1000 denars in the bank.",
       [
		  (troop_remove_gold, "trp_player", 1000),
		  (val_add, "$g_player_deposit", 1000),
		  (call_script, "script_bank_update_business"),
		   (party_get_slot, ":wealth", "$current_town", slot_town_wealth),
		   (val_add,":wealth", 10),
		   (party_set_slot, "$current_town", slot_town_wealth, ":wealth"),
		   (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
		   (val_add,":prosperity", 3),
		   (party_set_slot, "$current_town", slot_town_prosperity, ":prosperity"),
        ]),
      ("take_deposit",
	  [
	   (try_for_range, ":center_no", towns_begin, towns_end),
	       (eq, ":center_no", "$current_town"),
		   (store_faction_of_party, ":centre_faction", ":center_no"),
	       (is_between, ":centre_faction", "fac_kingdom_1", "fac_kingdom_6"),
		   (store_relation, ":player_relation", "$current_town", "trp_player"),
		   (store_relation, ":player_faction_relation", "fac_player_faction", ":centre_faction"),
	   (try_end),
	   #(party_get_slot, ":centre_owner", "$current_town", slot_town_lord),
	   (gt, ":player_faction_relation", -10),
	   (gt, ":player_relation", -4),
	   (ge,"$g_player_deposit",1000),
	  ],
	  "Withdraw 1000 denars from your deposit.",
       [
		  (troop_add_gold, "trp_player", 1000),
		  (val_sub, "$g_player_deposit", 1000),
		  (call_script, "script_bank_update_business"),
		   (party_get_slot, ":wealth", "$current_town", slot_town_wealth),
		   (val_sub,":wealth", 10),
		   (party_set_slot, "$current_town", slot_town_wealth, ":wealth"),
		   (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
		   (val_sub,":prosperity", 3),
		   (party_set_slot, "$current_town", slot_town_prosperity, ":prosperity"),
        ]),
		  ("take_deposit_all",
	   [
		   (store_faction_of_party, ":centre_faction", "$current_town"),
	       (is_between, ":centre_faction", "fac_kingdom_1", "fac_kingdom_6"),
		   (store_relation, ":player_relation", "$current_town", "trp_player"),
		   (store_relation, ":player_faction_relation", "fac_player_faction", ":centre_faction"),
		   (gt, ":player_faction_relation", -10),
		   (gt, ":player_relation", -4),
		   (ge,"$g_player_deposit",1000),
		   (ge,"$g_player_deposit",1)

	  ],
	  "Withdraw your entire deposit.",
       [
		  (troop_add_gold, "trp_player", reg6),
		  (val_sub, "$g_player_deposit", reg6),
		  (call_script, "script_bank_update_business"),
		  (store_div, ":temp_holder", "$g_player_deposit", 100),
		   (party_get_slot, ":wealth", "$current_town", slot_town_wealth),
		   (val_sub,":wealth", ":temp_holder"),
		   (party_set_slot, "$current_town", slot_town_wealth, ":wealth"),
		   (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
		   (store_div, ":temp_holder", "$g_player_debt", 3),
		   (val_sub,":prosperity", ":temp_holder"),
		   (party_set_slot, "$current_town", slot_town_prosperity, ":prosperity"),
        ]
	  
	  
	  ),
		 ("back_to_town_menu",[],"Head back.",
       [
           (jump_to_menu,"mnu_town"),
        ]),
    ]),







  ("KAOS_faction_banking_menu",0,
    "You visitbranch {s1} of {s2} Bank.\
 Here you can deposit money and earn interest over time, or take a loan.\
 You currently have {reg6} denars deposited here.\
 You currently have {reg7} denars borrowed from this bank.",
    "none",
    [
	     (str_store_party_name,s1,"$current_town"),
	     (str_store_faction_name, s2 ,"$current_town"),
		 (store_faction_of_party, ":centre_faction", "$current_town"),
	     (party_get_slot,"$g_player_debt",":centre_faction",slot_town_bank_debt),
	     (party_get_slot,"$g_player_deposit",":centre_faction",slot_town_bank_deposit),
	     (assign, reg6, "$g_player_deposit"),
	     (assign, reg7, "$g_player_debt"),
    ],
    [
      ("take_loan",
	  [
		  (store_troop_gold, ":player_wealth", "trp_player"),
		  (store_sub, ":player_real_wealth", ":player_wealth", "$g_player_debt"),
		  (gt,":player_real_wealth",100)
	  ],"Take a loan of 1000 denars.",
			[
			   (store_current_day, ":cur_day"),
			   (store_add, ":new_day", ":cur_day", 30),
		 	   (store_faction_of_party, ":centre_faction", "$current_town"),
			   (party_set_slot,":centre_faction",slot_town_bank_debt_repayment_date,":new_day"),
			   (party_get_slot,":due_date",":centre_faction",slot_town_bank_debt_repayment_date),	
			   (assign, reg6, ":due_date"),
			   (display_log_message, "@{s1} Debt payment due in {reg6} days", 0xFF0000),
			   (troop_remove_gold, "trp_player", 100),
			   (troop_add_gold, "trp_player", 1000),
			   (val_add, "$g_player_debt", 1000),
			   (call_script, "script_bank_update_business"),
			   
			   (party_get_slot, ":wealth", "$current_town", slot_town_wealth),
			   (val_sub,":wealth", 10),
			   (party_set_slot, "$current_town", slot_town_wealth, ":wealth"),
			   (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
			   (val_sub,":prosperity", 3),
			   (party_set_slot, "$current_town", slot_town_prosperity, ":prosperity"),
			]),
      ("give_loan",
		  [
			  (store_troop_gold, ":player_wealth", "trp_player"),
			  (gt,":player_wealth",1000),
			  (gt,"$g_player_debt",1000)
		  ],
	   "Repay 1000 denars of your debt.",
       [
		  (troop_remove_gold, "trp_player", 1000),
		  (val_sub, "$g_player_debt", 1000),
		  (call_script, "script_bank_update_business"),
		  (store_current_day, ":cur_day"),
		  (store_add, ":due_date", ":cur_day", 30),
		  (store_faction_of_party, ":centre_faction", "$current_town"),
		  (party_set_slot,":centre_faction",slot_town_bank_debt_repayment_effect, 0),
		  (try_begin),
			  (gt, "$g_player_debt", 0),
			  (party_set_slot,":centre_faction",slot_town_bank_debt_repayment_date,":due_date"),
			  (assign, reg6, ":due_date"),
			  (display_log_message, "@Payment recieved Debt payment due in {reg6} days", 0xFF0000),
		  (else_try),
			  (party_set_slot,":centre_faction",slot_town_bank_debt_repayment_date, 0),
			  (assign, reg6, ":due_date"),
			  (display_log_message, "@ You have no more debt owning", 0xFF0000),
		  (try_end),
			   (party_get_slot, ":wealth", "$current_town", slot_town_wealth),
			   (val_add,":wealth", 10),
			   (party_set_slot, "$current_town", slot_town_wealth, ":wealth"),
			   (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
			   (val_add,":prosperity", 3),
			   (party_set_slot, "$current_town", slot_town_prosperity, ":prosperity"),
        ]),
      ("give_loan_all",
			  [
			  (store_troop_gold, ":player_wealth", "trp_player"),
			  (gt,":player_wealth","$g_player_debt"),
			  (gt,"$g_player_debt",0)
		  ],
	   "Repay all of your debt.",
       [
		  (troop_remove_gold, "trp_player", "$g_player_debt"),
		  (val_sub, "$g_player_debt", "$g_player_debt"),
		  (call_script, "script_bank_update_business"),
		  (store_div, ":temp_holder", "$g_player_debt", 100),
		   (party_get_slot, ":wealth", "$current_town", slot_town_wealth),
		   (val_add,":wealth", ":temp_holder"),
		   (party_set_slot, "$current_town", slot_town_wealth, ":wealth"),
		   (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
		   (store_div, ":temp_holder", "$g_player_debt", 3),
		   (val_add,":prosperity", ":temp_holder"),
		   (party_set_slot, "$current_town", slot_town_prosperity, ":prosperity"),
        ]),
		
      ("give_deposit",
	  [
		  (store_troop_gold, ":player_wealth", "trp_player"),
		  (gt,":player_wealth",1000)
	  ],
	  "Deposit 1000 denars in the bank.",
       [
		  (troop_remove_gold, "trp_player", 1000),
		  (val_add, "$g_player_deposit", 1000),
		  (call_script, "script_bank_update_business"),
		   (party_get_slot, ":wealth", "$current_town", slot_town_wealth),
		   (val_add,":wealth", 10),
		   (party_set_slot, "$current_town", slot_town_wealth, ":wealth"),
		   (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
		   (val_add,":prosperity", 3),
		   (party_set_slot, "$current_town", slot_town_prosperity, ":prosperity"),
        ]),
      ("take_deposit",
	  [
	   (try_for_range, ":center_no", towns_begin, towns_end),
	       (eq, ":center_no", "$current_town"),
		   (store_faction_of_party, ":centre_faction", ":center_no"),
	       (is_between, ":centre_faction", "fac_kingdom_1", "fac_kingdom_6"),
		   (store_relation, ":player_relation", "$current_town", "trp_player"),
		   (store_relation, ":player_faction_relation", "fac_player_faction", ":centre_faction"),
	   (try_end),
	   #(party_get_slot, ":centre_owner", "$current_town", slot_town_lord),
	   (gt, ":player_faction_relation", -10),
	   (gt, ":player_relation", -4),
	   (ge,"$g_player_deposit",1000),
	  ],
	  "Withdraw 1000 denars from your deposit.",
       [
		  (troop_add_gold, "trp_player", 1000),
		  (val_sub, "$g_player_deposit", 1000),
		  (call_script, "script_bank_update_business"),
		   (party_get_slot, ":wealth", "$current_town", slot_town_wealth),
		   (val_sub,":wealth", 10),
		   (party_set_slot, "$current_town", slot_town_wealth, ":wealth"),
		   (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
		   (val_sub,":prosperity", 3),
		   (party_set_slot, "$current_town", slot_town_prosperity, ":prosperity"),
        ]),
		  ("take_deposit_all",
	   [
		   (store_faction_of_party, ":centre_faction", "$current_town"),
	       (is_between, ":centre_faction", "fac_kingdom_1", "fac_kingdom_6"),
		   (store_relation, ":player_relation", "$current_town", "trp_player"),
		   (store_relation, ":player_faction_relation", "fac_player_faction", ":centre_faction"),
		   (gt, ":player_faction_relation", -10),
		   (gt, ":player_relation", -4),
		   (ge,"$g_player_deposit",1000),
		   (ge,"$g_player_deposit",1)

	  ],
	  "Withdraw your entire deposit.",
       [
		  (troop_add_gold, "trp_player", reg6),
		  (val_sub, "$g_player_deposit", reg6),
		  (call_script, "script_bank_update_business"),
		  (store_div, ":temp_holder", "$g_player_deposit", 100),
		   (party_get_slot, ":wealth", "$current_town", slot_town_wealth),
		   (val_sub,":wealth", ":temp_holder"),
		   (party_set_slot, "$current_town", slot_town_wealth, ":wealth"),
		   (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
		   (store_div, ":temp_holder", "$g_player_debt", 3),
		   (val_sub,":prosperity", ":temp_holder"),
		   (party_set_slot, "$current_town", slot_town_prosperity, ":prosperity"),
        ]
	  
	  
	  ),
		 ("back_to_town_menu",[],"Head back.",
       [
           (jump_to_menu,"mnu_town"),
        ]),
    ]),
########################################################################################################################
#  KAOS BANKING KIT END																							       #
########################################################################################################################
 ]

# Manualy add these to module_game_menus search for "reports"
# add the lines in `bank_report` before "view_party_size_report"
bank_report = [
########################################################################################################################
#  KAOS BANKING KIT START																							   #
########################################################################################################################
		  ("view_bank_report",[],"View Banking report.",
			 [
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
#  KAOS BANKING KIT END																							       #
########################################################################################################################
]

# Manualy add these to module_game_menus search for "town"
# add the lines in `bank_menu` before "walled_center_manage"
bank_menu = [
########################################################################################################################
#  KAOS BANKING KIT START																							   #
########################################################################################################################
("kaoses_bank",
       [    
       		(try_begin),
				(eq, "$bank_availability", 0),
			    (party_get_slot, ":has_bank", "$current_town", slot_town_has_bank),
				(eq, ":has_bank", 1),
       		(else_try),
				(eq, "$bank_availability", 1),
			    (store_faction_of_party, ":centre_faction", "$current_town"),
			    (party_get_slot, ":has_bank", ":centre_faction", slot_town_has_bank),
       		(try_end),
			(is_between, "$current_town", towns_begin, towns_end),
       ],
       "Visit the bank.",
       [
       		(try_begin),
				(eq, "$bank_availability", 0),
				(jump_to_menu,"mnu_Lazeras_banking_menu"),
       		(else_try),
				(eq, "$bank_availability", 1),
				(jump_to_menu,"mnu_KAOS_faction_banking_menu"),
       		(try_end),
           
           

        ]),
########################################################################################################################
#  KAOS BANKING KIT END																							       #
########################################################################################################################
]

from util_common import *
from util_wrappers import *

def modmerge_game_menus(orig_game_menus, check_duplicates = False):
	if( not check_duplicates ):
		orig_game_menus.extend(game_menus) # Use this only if there are no replacements (i.e. no duplicated item names)
	else:
	# Use the following loop to replace existing entries with same id
		for i in range (0,len(game_menus)-1):
			find_index = find_object(orig_game_menus, game_menus[i][0]); # find_object is from header_common.py
			if( find_index == -1 ):
				orig_game_menus.append(game_menus[i])
			else:
				orig_game_menus[find_index] = game_menus[i]
	
	# splice this into "town" menu to call the center management hub.
	find_i = list_find_first_match_i( orig_game_menus, "town" )
	menuoptions = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
	find_i = list_find_first_match_i(menuoptions, "walled_center_manage")		
	OpBlockWrapper(menuoptions).InsertAfter(find_i, bank_menu)	
	
	# splice this into "town" menu to call the center management hub.
	find_i = list_find_first_match_i( orig_game_menus, "reports" )
	menuoptions = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
	find_i = list_find_first_match_i(menuoptions, "view_party_size_report")		
	OpBlockWrapper(menuoptions).InsertAfter(find_i, bank_report)	

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]
        modmerge_game_menus(orig_game_menus)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)