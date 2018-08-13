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

colour_varieties = collections.OrderedDict([
	("Red", collections.OrderedDict([
		("Indian Red", 0xCD5C5C),
		("Light Coral", 0xF08080),
		("Salmon", 0xFA8072),
		("Dark Salmon", 0xE9967A),
		("Light Salmon", 0xFFA07A),
		("Crimson", 0xDC143C),
		("Red", 0xFF0000),
		("Fire Brick", 0xB22222),
		("Dark Red", 0x8B0000)
	])),
	
	("Pink", collections.OrderedDict([
		("Pink", 0xFFC0CB),
		("Light Pink", 0xFFB6C1),
		("Hot Pink", 0xFF69B4),
		("Deep Pink", 0xFF1493),
		("Medium Violet Red", 0xC71585),
		("Pale Violet Red", 0xDB7093)
	])),
	
	("Orange", collections.OrderedDict([
		("Light Salmon", 0xFFA07A),
		("Coral", 0xFF7F50),
		("Tomato", 0xFF6347),
		("Orange Red", 0xFF4500),
		("Dark Orange", 0xFF8C00),
		("Orange", 0xFFA500)
	])),
	
	("Yellow", collections.OrderedDict([
		("Gold", 0xFFD700),
		("Yellow", 0xFFFF00),
		("Light Yellow", 0xFFFFE0),
		("Lemon Chiffon", 0xFFFACD),
		("Light Goldenrod Yellow", 0xFAFAD2),
		("Papaya Whip", 0xFFEFD5),
		("Moccasin", 0xFFE4B5),
		("Peach Puff", 0xFFDAB9),
		("Pale Goldenrod", 0xEEE8AA),
		("Khaki", 0xF0E68C),
		("Dark Khaki", 0xBDB76B)
	])),
	
	("Purple", collections.OrderedDict([
		("Lavender", 0xE6E6FA),
		("Thistle", 0xD8BFD8),
		("Plum", 0xDDA0DD),
		("Violet", 0xEE82EE),
		("Orchid", 0xDA70D6),
		("Fuchsia", 0xFF00FF),
		("Magenta", 0xFF00FF),
		("Medium Orchid", 0xBA55D3),
		("Medium Purple", 0x9370DB),
		("Rebecca Purple", 0x663399),
		("Blue Violet", 0x8A2BE2),
		("Dark Violet", 0x9400D3),
		("Dark Orchid", 0x9932CC),
		("Dark Magenta", 0x8B008B),
		("Purple", 0x800080),
		("Indigo", 0x4B0082),
		("Slate Blue", 0x6A5ACD),
		("Dark Slate Blue", 0x483D8B),
		("Medium Slate Blue", 0x7B68EE)
	])),
	
	("Green", collections.OrderedDict([
		("Green Yellow", 0xADFF2F),
		("Chartreuse", 0x7FFF00),
		("Lawn Green", 0x7CFC00),
		("Lime", 0x00FF00),
		("Lime Green", 0x32CD32),
		("Pale Green", 0x98FB98),
		("Light Green", 0x90EE90),
		("Medium Spring Green", 0x00FA9A),
		("Spring Green", 0x00FF7F),
		("Medium Sea Green", 0x3CB371),
		("Sea Green", 0x2E8B57),
		("Forest Green", 0x228B22),
		("Green", 0x008000),
		("Dark Green", 0x006400),
		("Yellow Green", 0x9ACD32),
		("Olive Drab", 0x6B8E23),
		("Olive", 0x808000),
		("Dark Olive Green", 0x556B2F),
		("Medium Aquamarine", 0x66CDAA),
		("Dark Sea Green", 0x8FBC8B),
		("Light Sea Green", 0x20B2AA),
		("Dark Cyan", 0x008B8B),
		("Teal", 0x008080)
	])),
	
	("Blue", collections.OrderedDict([
		("Aqua", 0x00FFFF),
		("Cyan", 0x00FFFF),
		("Light Cyan", 0xE0FFFF),
		("Pale Turquoise", 0xAFEEEE),
		("Aquamarine", 0x7FFFD4),
		("Turquoise", 0x40E0D0),
		("Medium Turquoise", 0x48D1CC),
		("Dark Turquoise", 0x00CED1),
		("Cadet Blue", 0x5F9EA0),
		("Steel Blue", 0x4682B4),
		("Light Steel Blue", 0xB0C4DE),
		("Powder Blue", 0xB0E0E6),
		("Light Blue", 0xADD8E6),
		("Sky Blue", 0x87CEEB),
		("Light Sky Blue", 0x87CEFA),
		("Deep Sky Blue", 0x00BFFF),
		("Dodger Blue", 0x1E90FF),
		("Cornflower Blue", 0x6495ED),
		("Medium Slate Blue", 0x7B68EE),
		("Royal Blue", 0x4169E1),
		("Blue", 0x0000FF),
		("Medium Blue", 0x0000CD),
		("Dark Blue", 0x00008B),
		("Navy", 0x000080),
		("Midnight Blue", 0x191970)
	])),
	
	("Brown", collections.OrderedDict([
		("Cornsilk", 0xFFF8DC),
		("Blanched Almond", 0xFFEBCD),
		("Bisque", 0xFFE4C4),
		("Navajo White", 0xFFDEAD),
		("Wheat", 0xF5DEB3),
		("Burlywood", 0xDEB887),
		("Tan", 0xD2B48C),
		("Rosy Brown", 0xBC8F8F),
		("Sandy Brown", 0xF4A460),
		("Goldenrod", 0xDAA520),
		("Dark Goldenrod", 0xB8860B),
		("Peru", 0xCD853F),
		("Chocolate", 0xD2691E),
		("Saddle Brown", 0x8B4513),
		("Sienna", 0xA0522D),
		("Brown", 0xA52A2A),
		("Maroon", 0x800000)
	])),
	
	("White", collections.OrderedDict([
		("White", 0xFFFFFF),
		("Snow", 0xFFFAFA),
		("Honeydew", 0xF0FFF0),
		("Mint Cream", 0xF5FFFA),
		("Azure", 0xF0FFFF),
		("Alice Blue", 0xF0F8FF),
		("Ghost White", 0xF8F8FF),
		("White Smoke", 0xF5F5F5),
		("Seashell", 0xFFF5EE),
		("Beige", 0xF5F5DC),
		("Old Lace", 0xFDF5E6),
		("Floral White", 0xFFFAF0),
		("Ivory", 0xFFFFF0),
		("Antique White", 0xFAEBD7),
		("Linen", 0xFAF0E6),
		("Lavender Blush", 0xFFF0F5),
		("Misty Rose", 0xFFE4E1)
	])),
	
	("Gray", collections.OrderedDict([
		("Gainsboro", 0xDCDCDC),
		("Light Gray", 0xD3D3D3),
		("Silver", 0xC0C0C0),
		("Dark Gray", 0xA9A9A9),
		("Gray", 0x808080),
		("Dim Gray", 0x696969),
		("Light Slate Gray", 0x778899),
		("Slate Gray", 0x708090),
		("Dark Slate Gray", 0x2F4F4F),
		("Black", 0x000000)
	])),
])

sample_list = list(colour_varieties.keys())
colours_sample = ", ".join(sample_list[0:-1]) + " and " + sample_list[-1]
colour_change_dialogs = [
	[anyone|plyr, "minister_talk",
		[
			(neg|is_between, "$g_constable_training_center", walled_centers_begin, walled_centers_end),
		],
		"I'd like to change our kingdom's colour.", "cstm_dplmc_constable_change_colour_ask",
		[]
	],
	
	[anyone, "cstm_dplmc_constable_change_colour_ask",
		[],
		"As you wish. There is a wide range of colours available for you to choose from, falling into the broad groups of %s.\
		You can make a quick selection of one of these colours or choose from more specific varieties of each. What would you like to do?" % (colours_sample), "cstm_dplmc_constable_change_colour_quick_or_specific",
		[]
	],
	
	[anyone|plyr, "cstm_dplmc_constable_change_colour_quick_or_specific",
		[],
		"I'd like to pick one of the colours mentioned", "cstm_dplmc_constable_change_colour_quick",
		[]
	],
	
	[anyone|plyr, "cstm_dplmc_constable_change_colour_quick_or_specific",
		[],
		"I'd like to make a more specific choice", "cstm_dplmc_constable_change_colour_specific",
		[]
	],
	
	[anyone, "cstm_dplmc_constable_change_colour_quick",
		[],
		"Which colour would you like?", "cstm_dplmc_constable_change_colour_quick_select",
		[]
	],
	
	[anyone, "cstm_dplmc_constable_change_colour_specific",
		[],
		"Which colour group would you like to choose from?", "cstm_dplmc_constable_change_colour_specific_group_select",
		[]
	],
]

for group_colour_text, colours in colour_varieties.iteritems():
	quick_colour = colours[group_colour_text]
	colour_change_dialogs.append([anyone|plyr, "cstm_dplmc_constable_change_colour_quick_select",
		[
			(faction_get_color, ":colour", "fac_player_supporters_faction"),
			(neq, ":colour", quick_colour),
		],
		group_colour_text, "minister_pretalk",
		[
			(faction_set_color, "fac_player_supporters_faction", quick_colour),
		]
	])
	
	colour_change_dialogs.append([anyone|plyr, "cstm_dplmc_constable_change_colour_specific_group_select",
		[],
		group_colour_text, "cstm_dplmc_constable_change_colour_specific_group_selected_" + group_colour_text.lower(),
		[]
	])
	
	colour_change_dialogs.append([anyone, "cstm_dplmc_constable_change_colour_specific_group_selected_" + group_colour_text.lower(),
		[],
		"Very well, what variety of %s would you like?" % (group_colour_text), "cstm_dplmc_constable_change_colour_specific_select_" + group_colour_text.lower(),
		[]
	])
	
	for specific_colour_text, colour in colours.iteritems():
		colour_change_dialogs.append([anyone|plyr, "cstm_dplmc_constable_change_colour_specific_select_" + group_colour_text.lower(),
			[
				(faction_get_color, ":colour", "fac_player_supporters_faction"),
				(neq, ":colour", colour),
			],
			specific_colour_text, "minister_pretalk",
			[
				(faction_set_color, "fac_player_supporters_faction", colour),
			]
		])
	
	colour_change_dialogs.append([anyone|plyr, "cstm_dplmc_constable_change_colour_specific_select_" + group_colour_text.lower(),
		[],
		"Never mind", "minister_pretalk",
		[]
	])

colour_change_dialogs.extend([
	[anyone|plyr, "cstm_dplmc_constable_change_colour_quick_or_specific",
		[],
		"Never mind", "minister_pretalk",
		[]
	],
	
	[anyone|plyr, "cstm_dplmc_constable_change_colour_quick_select",
		[],
		"Never mind", "minister_pretalk",
		[]
	],
	
	[anyone|plyr, "cstm_dplmc_constable_change_colour_specific_gruop_select",
		[],
		"Never mind", "minister_pretalk",
		[]
	],
	
	[anyone|plyr, "cstm_dplmc_constable_change_colour_specific_group_select",
		[],
		"Never mind", "minister_pretalk",
		[]
	],
])

def modmerge(var_set):
	try:
		var_name_1 = "dialogs"
		orig_dialogs = var_set[var_name_1]
		
		index = [i for i, dialog in enumerate(orig_dialogs) if dialog[1] == "minister_talk" and dialog[4] == "close_window"][0]
		orig_dialogs[index:index] = colour_change_dialogs
		
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)