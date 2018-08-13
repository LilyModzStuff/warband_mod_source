# -*- coding: cp1254 -*-
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


####################################################################################################################
# During a dialog, the dialog lines are scanned from top to bottom.
# If the dialog-line is spoken by the player, all the matching lines are displayed for the player to pick from.
# If the dialog-line is spoken by another, the first (top-most) matching line is selected.
#
#	Each dialog line contains the following fields:
# 1) Dialogue partner: This should match the person player is talking to.
#		Usually this is a troop-id.
#		You can also use a party-template-id by appending '|party_tpl' to this field.
#		Use the constant 'anyone' if you'd like the line to match anybody.
#		Appending '|plyr' to this field means that the actual line is spoken by the player
#		Appending '|other(troop_id)' means that this line is spoken by a third person on the scene.
#			 (You must make sure that this third person is present on the scene)
#
# 2) Starting dialog-state:
#		During a dialog there's always an active Dialog-state.
#		A dialog-line's starting dialog state must be the same as the active dialog state, for the line to be a possible candidate.
#		If the dialog is started by meeting a party on the map, initially, the active dialog state is "start"
#		If the dialog is started by speaking to an NPC in a town, initially, the active dialog state is "start"
#		If the dialog is started by helping a party defeat another party, initially, the active dialog state is "party_relieved"
#		If the dialog is started by liberating a prisoner, initially, the active dialog state is "prisoner_liberated"
#		If the dialog is started by defeating a party led by a hero, initially, the active dialog state is "enemy_defeated"
#		If the dialog is started by a trigger, initially, the active dialog state is "event_triggered"
# 3) Conditions block (list): This must be a valid operation block. See header_operations.py for reference.
# 4) Dialog Text (string):
# 5) Ending dialog-state:
#		If a dialog line is picked, the active dialog-state will become the picked line's ending dialog-state.
# 6) Consequences block (list): This must be a valid operation block. See header_operations.py for reference.
# 7) Voice-over (string): sound filename for the voice over. Leave here empty for no voice over
####################################################################################################################

recruitment_dialogs = [

	[anyone|plyr, "dplmc_constable_recruit_select",
		[
			(str_store_troop_name, s11, cstm_troop_tree_prefix),
		],
		"{s11}.", "dplmc_constable_recruit_amount",
		[
			(assign, "$temp", "fac_player_supporters_faction"),
		]
	],
	
]

dplmc_customise_dialogs = [
	
	[anyone|plyr, "dplmc_constable_recruits_and_training",
		[
			(neg|is_between, "$g_constable_training_center", walled_centers_begin, walled_centers_end),
			(eq, "$players_kingdom", "fac_player_supporters_faction"),
			(faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
		],
		"I'd like to customise our kingdom's troops.", "cstm_dplmc_constable_customise_tree_ask",
		[]
	],
	
	[anyone, "cstm_dplmc_constable_customise_tree_ask",
		[],
		"As you wish.", "close_window",
		[
			(assign, "$cstm_open_troop_tree_view", 1),
			(finish_mission),
		]
	],

]

default_customise_dialogs = [
	
	[anyone|plyr, "minister_talk",
		[
			(neg|is_between, "$g_constable_training_center", walled_centers_begin, walled_centers_end),
		],
		"I'd like to customise our kingdom's troops.", "cstm_customise_tree_ask",
		[]
	],
	
	[anyone, "cstm_customise_tree_ask",
		[],
		"As you wish.", "close_window",
		[
			(assign, "$cstm_open_troop_tree_view", 1),
			(finish_mission),
		]
	],

]

def modmerge(var_set):
	try:
		var_name_1 = "dialogs"
		orig_dialogs = var_set[var_name_1]
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)
	
	orig_dialogs.extend(recruitment_dialogs)
	
	try:
		index = [i for i, dialog in enumerate(orig_dialogs) if dialog[1] == "dplmc_constable_recruits_and_training" and dialog[4] == "dplmc_constable_pretalk"][0]
		orig_dialogs[index:index] = dplmc_customise_dialogs
	except IndexError:
		print "Diplomacy Constable recruits and training dialog not found, giving customise tree dialog to Minister"
		try:
			index = [i for i, dialog in enumerate(orig_dialogs) if dialog[1] == "minister_talk" and dialog[4] == "close_window"][0]
			orig_dialogs[index:index] = default_customise_dialogs
		except IndexError:
			raise NameError("Could not find minister closing dialog")