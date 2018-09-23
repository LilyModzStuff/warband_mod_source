# Freelancer (1.3) by Taragoth
# Released 11 July 2011
# Edits by Caba'drin 14 Dec 2011
# Mod-Merger'd by Windyplains, Monnikje and Caba'drin

# -*- coding: cp1254 -*-
from header_common import *
from header_dialogs import *
from header_operations import *
from module_constants import *
from header_mission_templates import grc_infantry, grc_archers, grc_cavalry



####################################################################################################################
# During a dialog, the dialog lines are scanned from top to bottom.
# If the dialog-line is spoken by the player, all the matching lines are displayed for the player to pick from.
# If the dialog-line is spoken by another, the first (top-most) matching line is selected.
#
#  Each dialog line contains the following fields:
# 1) Dialogue partner: This should match the person player is talking to.
#    Usually this is a troop-id.
#    You can also use a party-template-id by appending '|party_tpl' to this field.
#    Use the constant 'anyone' if you'd like the line to match anybody.
#    Appending '|plyr' to this field means that the actual line is spoken by the player
#    Appending '|other(troop_id)' means that this line is spoken by a third person on the scene.
#       (You must make sure that this third person is present on the scene)
#
# 2) Starting dialog-state:
#    During a dialog there's always an active Dialog-state.
#    A dialog-line's starting dialog state must be the same as the active dialog state, for the line to be a possible candidate.
#    If the dialog is started by meeting a party on the map, initially, the active dialog state is "start"
#    If the dialog is started by speaking to an NPC in a town, initially, the active dialog state is "start"
#    If the dialog is started by helping a party defeat another party, initially, the active dialog state is "party_relieved"
#    If the dialog is started by liberating a prisoner, initially, the active dialog state is "prisoner_liberated"
#    If the dialog is started by defeating a party led by a hero, initially, the active dialog state is "enemy_defeated"
#    If the dialog is started by a trigger, initially, the active dialog state is "event_triggered"
# 3) Conditions block (list): This must be a valid operation block. See header_operations.py for reference.
# 4) Dialog Text (string):
# 5) Ending dialog-state:
#    If a dialog line is picked, the active dialog-state will become the picked line's ending dialog-state.
# 6) Consequences block (list): This must be a valid operation block. See header_operations.py for reference.
# 7) Voice-over (string): sound filename for the voice over. Leave here empty for no voice over
####################################################################################################################

#+freelancer start
lord_talk_addon = [
# dialog_ask_enlistment
    [anyone|plyr,"lord_talk", [
        (eq, "$freelancer_state", 0),
		(ge, "$g_talk_troop_faction_relation", 0),
        (neq, "$players_kingdom", "$g_talk_troop_faction"),
        (eq, "$players_kingdom", 0),
		(neg|troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0), 
     ],"My Lord, I would like to enlist in your army.", "lord_request_enlistment",[]],
	
	[anyone|plyr,"lord_talk", [
		(eq, "$g_talk_troop", "$enlisted_lord"),
        (eq, "$freelancer_state", 1),
		(neg|troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0), 
     ],"My Lord, I would like to be reassigned to another division.", "lord_request_reassignment",[]],
	
	# dialog_advise_retirement
    [anyone|plyr,"lord_talk", [
        (eq, "$g_talk_troop", "$enlisted_lord"),
		(neq, "$freelancer_state", 0),
        (ge, "$g_talk_troop_faction_relation", 0),
        (neq, "$players_kingdom", "$g_talk_troop_faction"),
        (eq, "$players_kingdom", 0),
		(neg|troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0), 
     ], "My Lord, I would like to retire from service.", "lord_request_retire",[]],
	
	#dialog_ask_leave
    [anyone|plyr,"lord_talk",[
		(eq, "$g_talk_troop", "$enlisted_lord"),
		(eq, "$freelancer_state", 1),
        (ge, "$g_talk_troop_faction_relation", 0),
        (neq, "$players_kingdom", "$g_talk_troop_faction"),
        (eq, "$players_kingdom", 0),
		(neg|troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0), 
     ], "My Lord, I would like to request some personal leave.", "lord_request_vacation",[]],  
		
	#dialog_ask_return_from_leave
	[anyone|plyr,"lord_talk",[
		(eq, "$g_talk_troop", "$enlisted_lord"),
		(eq, "$freelancer_state", 2),
        (ge, "$g_talk_troop_faction_relation", 0),
        (neq, "$players_kingdom", "$g_talk_troop_faction"),
        (eq, "$players_kingdom", 0),
		(neg|troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0), 
     ], "My Lord, I am ready to return to your command.", "ask_return_from_leave",[]],	
]
		
dialogs	= [   
# dialog_accept_enlistment
    [anyone,"lord_request_enlistment", [
        (ge, "$g_talk_troop_relation", 0),
		(try_begin),
			(neg|faction_slot_eq, "$g_talk_troop_faction", slot_faction_freelancer_troop, 0),
			(faction_get_slot, reg1, "$g_talk_troop_faction", slot_faction_freelancer_troop),
		(else_try),
			(faction_get_slot, reg1, "$g_talk_troop_faction", slot_faction_tier_1_troop),
		(try_end),
		(str_store_troop_name, s1, reg1),
		(store_character_level, reg1, reg1),
		(val_mul, reg1, 10),		
		(str_store_string, s2, "str_reg1_denars"),
    ], "I've got room in my ranks for a {man/woman} of your disposition, {playername}.  I can take you on as a {s1}, with a weekly pay of {s2}. And food, of course.  Plenty of room for promotion and you'll be equipped as befits your rank. You'll have your take of what you can scavange after battle, too.  What do you say?", "lord_request_enlistment_confirm", []],		
    [anyone|plyr,"lord_request_enlistment_confirm", [], "Seems a fair lot and steady work in these lands. I'm with you, my lord.", "close_window", [        (call_script, "script_freelancer_event_player_enlists"),
		(eq,"$talk_context",tc_party_encounter),
		(assign, "$g_leave_encounter", 1),
	 ]],
	[anyone|plyr,"lord_request_enlistment_confirm",[], "Well, on second thought my lord, I might try my luck alone a bit longer. My thanks.", "lord_pretalk",[]],
# dialog_reject_enlistment
    [anyone,"lord_request_enlistment", [(lt, "$g_talk_troop_relation", 0)], "I do not trust you enough to allow you to serve for me.", "lord_pretalk",[]],

	#reassignment
	[anyone,"lord_request_reassignment", [(store_current_day, ":service_length"),(quest_get_slot, reg0, "qst_freelancer_enlisted", slot_quest_freelancer_start_date),
        (val_sub, ":service_length", reg0),
		(gt, ":service_length", 14),
		(neg|faction_slot_eq, "$g_talk_troop_faction", slot_faction_tier_1_troop, "$player_cur_troop"), #served at least for 2 weeks, and have been upgraded once
	 ], "Reassignment, {playername}? Your current post doesn't suit you? Very well then. What were you thinking?", "lord_request_reassignment_select", 
	 [(call_script, "script_freelancer_list_faction_troops", "$g_talk_troop_faction", "trp_temp_array_a", "trp_temp_array_b")]],
	[anyone,"lord_request_reassignment", [], "Sorry, {lad/lass}, but I can't have my men changing their mind every day. Next you'll be asking for leave--or to retire!", "lord_pretalk", []],
	[anyone|plyr,"lord_request_reassignment_select", [(call_script, "script_cf_freelancer_get_reassign_troop", "trp_temp_array_a", grc_infantry),(assign, reg1, reg0),(str_store_troop_name, s1, reg0)], 
	  "A new role in the infantry: {s1}", "lord_request_reassignment_confirm", [(assign, "$temp", reg1)]],
	[anyone|plyr,"lord_request_reassignment_select", [(call_script, "script_cf_freelancer_get_reassign_troop", "trp_temp_array_a", grc_archers),(assign, reg2, reg0),(str_store_troop_name, s2, reg0)], 
	 "A position with your ranged troops: {s2}", "lord_request_reassignment_confirm", [(assign, "$temp", reg2)]],
	[anyone|plyr,"lord_request_reassignment_select", [(call_script, "script_cf_freelancer_get_reassign_troop", "trp_temp_array_a", grc_cavalry),(assign, reg3, reg0),(str_store_troop_name, s3, reg0)], 
	  "A spot amongst your horsemen: {s3}", "lord_request_reassignment_confirm", [(assign, "$temp", reg3)]],
    [anyone|plyr,"lord_request_reassignment_select", [], "I'd like to start with the recruits again.", "lord_request_reassignment_confirm", [(faction_get_slot, "$temp", "$g_talk_troop_faction", slot_faction_tier_1_troop)]],
	[anyone|plyr,"lord_request_reassignment_select", [(str_store_troop_name, s5, "$player_cur_troop")], "Actually...maybe not, milord. No. I'm fine as a {s5}", "lord_pretalk", []],
	[anyone,"lord_request_reassignment_confirm", [(str_store_troop_name, s4, "$temp"),(str_store_troop_name, s5, "$player_cur_troop")], 
	  "Alright, {playername}, you're sure I should have my Master-of-Arms begin your retraining as a {s4}?", "lord_request_reassignment_finish", []],
	[anyone|plyr,"lord_request_reassignment_finish", [], "Yes, I'd like to be retrained as a {s4}, sir.", "lord_pretalk", 
	  [ (call_script, "script_freelancer_unequip_troop", "$player_cur_troop"),
		(assign, "$player_cur_troop", "$temp"),
		(faction_set_slot, "$g_talk_troop_faction", slot_faction_freelancer_troop, "$player_cur_troop"),
		(call_script, "script_freelancer_equip_troop", "$player_cur_troop"),
		(str_store_troop_name, s5, "$player_cur_troop"),
		(str_store_troop_name_link, s13, "$enlisted_lord"),
		(str_store_faction_name_link, s14, "$g_talk_troop_faction"),
		(str_store_string, s1, "@Enlisted as a {s5} in the party of {s13} of {s14}."),
		(add_troop_note_from_sreg, "trp_player", 3, s1, 0),

		(str_store_string, s5, "@Current rank: {s5}"),
		(add_quest_note_from_sreg, "qst_freelancer_enlisted", 3, s5, 1),
		(troop_get_xp, reg0, "trp_player"),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_start_xp, reg0),
		
		(call_script, "script_freelancer_get_upgrade_xp", "$player_cur_troop"),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_upgrade_xp, reg0),	  
	  ]],
	[anyone|plyr,"lord_request_reassignment_finish", [], "Actually...maybe not, milord. No. I'm fine as a {s5}. Milord.", "lord_pretalk", []],
	
	
# dialog_lord_accept_retire 
    [anyone,"lord_request_retire",[], "Very well {playername}. You are relieved of duty.", "lord_pretalk",[
		(call_script, "script_freelancer_event_player_discharge"),
	 ]],	
#dialog_accept_leave  
    [anyone,"lord_request_vacation", [#(ge, "$g_talk_troop_relation", 0)
	   ],
    	"Very well {playername}. You shall take some time off from millitary duty. Return in two weeks.", "lord_pretalk",[
		(call_script, "script_freelancer_event_player_vacation"),
	 ]],
						
#dialog_accept_ask_return_from_leave
    [anyone,"ask_return_from_leave", [
        #(ge, "$g_talk_troop_relation", 0),
		(check_quest_active, "qst_freelancer_vacation"),
	 ], "Welcome back {playername}. Your regiment has missed you I daresay! Now return to your post.", "lord_pretalk",[
        (call_script, "script_freelancer_event_player_returns", plyr_mission_vacation),
	 ]],			
	[anyone,"ask_return_from_leave", [
        #(ge, "$g_talk_troop_relation", 0),
		(check_quest_active, "qst_freelancer_captured"),
		#(quest_get_slot, reg0, "qst_freelancer_captured", slot_quest_object_center),
		#(str_store_party_name, s1, reg0),
		(quest_get_slot, reg0, "qst_freelancer_captured", slot_quest_object_faction),
		(str_store_faction_name, s1, reg0),
	 ],
       "It is good to see you, {playername}. Was quite the ordeal we faced against the {s1}. Glad to have you back in the company.", "lord_pretalk",[
        (call_script, "script_freelancer_event_player_returns", plyr_mission_captured),
	 ]],	
#+freelancer end
]

from util_common import *
from util_wrappers import *

def dialogs_addendum(orig_dialogs):
	try:
		dialog = FindDialog(orig_dialogs, anyone|plyr, "lord_talk", "lord_request_mission_ask")
		codeblock = dialog.GetConditionBlock()
		codeblock.InsertBefore(0, not_enlisted)
		dialog = FindDialog(orig_dialogs, anyone|plyr, "lord_talk", "lord_ask_enter_service", "I have come")
		codeblock = dialog.GetConditionBlock()
		codeblock.InsertBefore(0, not_enlisted)
		dialog = FindDialog(orig_dialogs, anyone|plyr, "lord_talk", "lord_ask_enter_service", "I wish to become")
		codeblock = dialog.GetConditionBlock()
		codeblock.InsertBefore(0, not_enlisted)
	except:
		import sys
		print "Injecton 1 failed:", sys.exc_info()[1]
		raise

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
		var_name_1 = "dialogs"
		orig_dialogs = var_set[var_name_1]
		orig_dialogs.extend(dialogs)
		pos = FindDialog_i(orig_dialogs, anyone|plyr, "lord_talk", "lord_leave_prison")
		OpBlockWrapper(orig_dialogs).InsertBefore(pos, lord_talk_addon)
		##ORIG_DIALOGS is a list, can use OpBlockWrapper and other list operations.
		
		dialogs_addendum(orig_dialogs) #other dialog additions
		
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)