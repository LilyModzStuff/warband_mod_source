# Freelancer (1.3) by Taragoth
# Released 11 July 2011
# Edits by Caba'drin 14 Dec 2011
# Mod-Merger'd by Windyplains, Monnikje and Caba'drin

# -*- coding: cp1254 -*-
from header_common import *
from header_dialogs import *
from header_operations import *
from module_constants import *



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
        #(neq, "$players_kingdom", "$g_talk_troop_faction"),
        (eq, "$players_kingdom", 0),
        ],
    "My Lord, I would like to like to enlist in your army.", "lord_request_enlistment",[]],
	
	# dialog_advise_retirement

    [anyone|plyr,"lord_talk", [
        (eq, "$g_talk_troop", "$enlisted_lord"),
		(neq, "$freelancer_state", 0),
        (ge, "$g_talk_troop_faction_relation", 0),
        (neq, "$players_kingdom", "$g_talk_troop_faction"),
        (eq, "$players_kingdom", 0),
        ],
    "My Lord, I would like to like to retire from service.", "lord_request_retire",[]],
	
	#dialog_ask_leave
    [anyone|plyr,"lord_talk",[
		(eq, "$g_talk_troop", "$enlisted_lord"),
		(eq, "$freelancer_state", 1),
        (ge, "$g_talk_troop_faction_relation", 0),
        (neq, "$players_kingdom", "$g_talk_troop_faction"),
        (eq, "$players_kingdom", 0),
        ],
        "My Lord, I would like to request some personal leave", "lord_request_vacation",[]],  
		
	#dialog_ask_return_from_leave
		[anyone|plyr,"lord_talk",[
		(eq, "$g_talk_troop", "$enlisted_lord"),
		(eq, "$freelancer_state", 2),
        (ge, "$g_talk_troop_faction_relation", 0),
        (neq, "$players_kingdom", "$g_talk_troop_faction"),
        (eq, "$players_kingdom", 0),
        ],
        "My Lord, I am ready to return to your command.", "ask_return_from_leave",[]],	
]
		
dialogs	= [   
# dialog_accept_enlistment

    [anyone,"lord_request_enlistment",
    [
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
    ], "I've got room in my ranks for a {man/woman} of your disposition, {playername}.  I can take you on as a {s1}, with a weekly pay of {s2}. And food, of course.  Plenty of room for promotion and you'll be equipped as befits your rank. You'll have your take of what you can scavange in battle, too.  What do you say?", "lord_request_enlistment_confirm", []],
		
    [anyone|plyr,"lord_request_enlistment_confirm", [],
    "Seems a fair lot and steady work in these lands. I'm with you, my lord.", "close_window",
	[
	    (party_clear, "p_freelancer_party_backup"),
       	(call_script, "script_party_copy", "p_freelancer_party_backup", "p_main_party"),
		(remove_member_from_party, "trp_player","p_freelancer_party_backup"),
        (call_script, "script_event_player_enlists"),
		(assign, "$g_infinite_camping", 1),
        (rest_for_hours_interactive, 24 * 365, 5, 1),
		(eq,"$talk_context",tc_party_encounter),
		(assign, "$g_leave_encounter", 1),
	]],

	[anyone|plyr,"lord_request_enlistment_confirm",[],
    "Well, on second thought my lord, I might try my luck alone a bit longer. My thanks.", "lord_pretalk",[]],
	
# dialog_reject_enlistment

    [anyone,"lord_request_enlistment", [(lt, "$g_talk_troop_relation", 0)],
    "I do not trust you enough to allow you to serve for me.", "lord_pretalk",[]],

   

# dialog_lord_accept_retire 

    [anyone,"lord_request_retire",
    [		
    ],
    "Very well {playername}. You are relieved of duty.", "lord_pretalk",[
	(call_script, "script_event_player_discharge"),
	(call_script, "script_party_restore"),
	(change_screen_map),
	],
	],	
	
#dialog_accept_leave  
    [anyone,"lord_request_vacation",
        [
        (ge, "$g_talk_troop_relation", 0),
		],
            "Very well {playername}. You shall take some time off from millitary duty. Return in two weeks.", "lord_pretalk",[
		(call_script, "script_event_player_vacation"),
       	(call_script, "script_party_restore"),
		(change_screen_map),
		],
		],
					

				
	
#dialog_accept_ask_return_from_leave
        [anyone,"ask_return_from_leave",
        [
        (ge, "$g_talk_troop_relation", 0),
		],
        "Welcome back {playername}. Your regiment has missed you I daresay, Now return to your post.", "lord_pretalk",[
        (call_script, "script_party_copy", "p_freelancer_party_backup", "p_main_party"),
		(remove_member_from_party, "trp_player","p_freelancer_party_backup"),
        (call_script, "script_event_player_returns_vacation"),
		(change_screen_map),
		],
		],	
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