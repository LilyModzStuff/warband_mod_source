# Tournament Play Enhancements (1.5) by Windyplains

from header_common import *
from header_dialogs import *
from header_operations import *
from header_parties import *
from header_item_modifiers import *
from header_skills import *
from header_triggers import *
from ID_troops import *
from ID_party_templates import *
##diplomacy start+
from header_troops import ca_intelligence
from header_terrain_types import *
from header_items import * #For ek_food, and so forth
##diplomacy end+
from module_constants import *
## CC
from header_items import *
from header_troops import *
## CC


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

dialogs	= [   
    ##### QUEST : FLORIS_ACTIVE_TOURNAMENT : BEGIN #####
	# [anyone,"start",
		# [
			# #(eq, "$g_talk_troop", "trp_custom_messenger"),
			# (eq, "$g_quest_attempt", "qst_floris_active_tournament"),
			# (neg|check_quest_active, "qst_floris_active_tournament"),
			# (quest_get_slot, ":troop_no", "qst_floris_active_tournament", slot_quest_giver_troop),
			# (str_store_troop_name, s21, ":troop_no"),
		# ], "Pardon, m'{Lord/Lady}, but I've been sent by {s21} to deliver this message to you.", "qp1_messenger_1", []],
		
    # [anyone|plyr,"qp1_messenger_1", [], "I see.  Let's see what this is about.", "qp1_messenger_2", []],
	
	# [anyone|plyr,"qp1_messenger_2", 
		# [
			# (quest_get_slot, ":troop_no", "qst_floris_active_tournament", slot_quest_giver_troop),
			# (str_store_troop_name, s21, ":troop_no"),
		# ], "Seems we have an engagement awaiting us in {s21}.", "close_window",
		# [
			# # Begin Quest
			# (change_screen_map),
		# ]],
	##### QUEST : FLORIS_ACTIVE_TOURNAMENT : END #####
	
]


lord_talk_addon	= [   
	##### QUEST : FLORIS_ACTIVE_TOURNAMENT : BEGIN #####
    [anyone,"lord_start",
		[
			(check_quest_active, "qst_floris_active_tournament"),
			(quest_get_slot, ":troop_no", "qst_floris_active_tournament", slot_quest_giver_troop),
			(eq, "$g_talk_troop", ":troop_no"),
			(quest_slot_eq, "qst_floris_active_tournament", slot_quest_current_state, qp1_tournament_message_received),
			(quest_set_slot, "qst_floris_active_tournament", slot_quest_current_state, 0),
			(str_store_troop_name, s21, ":troop_no"),
		], "I see you received my invitation to our games.  It is good to have you among us.", "lord_talk", []],
		
    [anyone,"lord_start",
		[
			(neg|check_quest_active, "qst_floris_active_tournament"),
			(quest_get_slot, ":troop_no", "qst_floris_active_tournament", slot_quest_giver_troop),
			(eq, "$g_talk_troop", ":troop_no"),
			(quest_slot_eq, "qst_floris_active_tournament", slot_quest_current_state, qp1_tournament_refused_invitation),
			(quest_set_slot, "qst_floris_active_tournament", slot_quest_current_state, 0),
			(str_store_troop_name, s21, ":troop_no"),
		], "So there you are.  It is a shame you couldn't make it out this way for the games.  I would have enjoyed a chance to cross swords with you.", "lord_talk", 
		[
			(try_begin),
				(ge, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_HIGH),
				(quest_get_slot, ":town_lord", "qst_floris_active_tournament", slot_quest_giver_troop),
				(call_script, "script_troop_change_relation_with_troop", "trp_player", ":town_lord", -1),
			(try_end),
		]],
		
    [anyone,"lord_start",
		[
			(check_quest_active, "qst_floris_active_tournament"),
			(quest_get_slot, ":troop_no", "qst_floris_active_tournament", slot_quest_giver_troop),
			(eq, "$g_talk_troop", ":troop_no"),
			(quest_slot_eq, "qst_floris_active_tournament", slot_quest_current_state, qp1_tournament_participated_in_tournament),
			(quest_set_slot, "qst_floris_active_tournament", slot_quest_current_state, 0),
			(str_store_troop_name, s21, ":troop_no"),
		], "It was an honor to have you among the participants for our games.", "lord_talk", 
		[
			(assign, ":relation_change", 0),
			(try_begin),
				(quest_slot_eq, "qst_floris_active_tournament", slot_quest_current_state, qp1_tournament_message_received), # If you weren't invited then no one should care if you don't attend.
				(ge, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_LOW),
				(val_add, ":relation_change", 1),
				(ge, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_MEDIUM),
				(val_add, ":relation_change", 1),
				(ge, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_HIGH),
				(val_add, ":relation_change", 1),
			(try_end),
			(quest_get_slot, ":town_lord", "qst_floris_active_tournament", slot_quest_giver_troop),
			(call_script, "script_troop_change_relation_with_troop", "trp_player", ":town_lord", ":relation_change"),
			(complete_quest, "qst_floris_active_tournament"),
		]],
	##### QUEST : FLORIS_ACTIVE_TOURNAMENT : END #####
]

from util_common import *
from util_wrappers import *

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
		var_name_1 = "dialogs"
		orig_dialogs = var_set[var_name_1]
		orig_dialogs.extend(dialogs)
		pos = FindDialog_i(orig_dialogs, anyone,"lord_start")
		OpBlockWrapper(orig_dialogs).InsertBefore(pos, lord_talk_addon)
		##ORIG_DIALOGS is a list, can use OpBlockWrapper and other list operations.
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)