# -*- coding: cp1254 -*-
import module_skills
from module_constants import npc_kingdoms_begin, npc_kingdoms_end

import collections

new_strings = [
	("cstm_ca_strength", "STR"),
	("cstm_ca_agility", "AGI"),
	("cstm_ca_intelligence", "INT"),
	("cstm_ca_charisma", "CHA"),
	
	("cstm_wpt_one_handed_weapon", "1H Weapon"),
	("cstm_wpt_two_handed_weapon", "2H Weapon"),
	("cstm_wpt_polearm", "Polearm"),
	("cstm_wpt_archery", "Archery"),
	("cstm_wpt_crossbow", "Crossbow"),
	("cstm_wpt_throwing", "Throwing"),
	("cstm_wpt_firearm", "Firearm"),
	
	("cstm_skill_trade", "Trade"),
	("cstm_skill_leadership", "Leadership"),
	("cstm_skill_prisoner_management", "Pris Mgmt"), 
	("cstm_skill_reserved_1", "Reserved Skill 1"), 
	("cstm_skill_reserved_2", "Reserved Skill 2"), 
	("cstm_skill_reserved_3", "Reserved Skill 3"), 
	("cstm_skill_reserved_4", "Reserved Skill 4"), 
	("cstm_skill_persuasion", "Persuasion"),
	("cstm_skill_engineer", "Engineer"),
	("cstm_skill_first_aid", "First Aid"), 
	("cstm_skill_surgery", "Surgery"), 
	("cstm_skill_wound_treatment", "W. Treatment"), 
	("cstm_skill_inventory_management", "Inv Mgmt"), 
	("cstm_skill_spotting", "Spotting"),
	("cstm_skill_pathfinding","Path-finding"), 
	("cstm_skill_tactics", "Tactics"),
	("cstm_skill_tracking", "Tracking"),
	("cstm_skill_trainer", "Trainer"),
	("cstm_skill_reserved_5", "Reserved Skill 5"), 
	("cstm_skill_reserved_6", "Reserved Skill 6"), 
	("cstm_skill_reserved_7", "Reserved Skill 7"), 
	("cstm_skill_reserved_8", "Reserved Skill 8"), 
	("cstm_skill_looting", "Looting"), 
	("cstm_skill_horse_archery", "H. Archery"),
	("cstm_skill_riding", "Riding"),
	("cstm_skill_athletics", "Athletics"),
	("cstm_skill_shield", "Shield"),
	("cstm_skill_weapon_master", "W. Master"),
	("cstm_skill_reserved_9", "Reserved Skill 9"), 
	("cstm_skill_reserved_10", "Reserved Skill 10"), 
	("cstm_skill_reserved_11", "Reserved Skill 11"), 
	("cstm_skill_reserved_12", "Reserved Skill 12"), 
	("cstm_skill_reserved_13", "Reserved Skill 13"), 
	("cstm_skill_power_draw", "Power Draw"),
	("cstm_skill_power_throw", "Power Throw"),
	("cstm_skill_power_strike", "Power Strike"),
	("cstm_skill_ironflesh", "Ironflesh"), 
	("cstm_skill_reserved_14", "Reserved Skill 14"), 
	("cstm_skill_reserved_15", "Reserved Skill 15"), 
	("cstm_skill_reserved_16", "Reserved Skill 16"), 
	("cstm_skill_reserved_17", "Reserved Skill 17"), 
	("cstm_skill_reserved_18", "Reserved Skill 18"), 
	
	("cstm_imod_string_plain", "Plain"),
	("cstm_imod_string_cracked", "Cracked"),
	("cstm_imod_string_rusty", "Rusty"),
	("cstm_imod_string_bent", "Bent"),
	("cstm_imod_string_chipped", "Chipped"),
	("cstm_imod_string_battered", "Battered"),
	("cstm_imod_string_poor", "Poor"),
	("cstm_imod_string_crude", "Crude"),
	("cstm_imod_string_old", "Old"),
	("cstm_imod_string_cheap", "Cheap"),
	("cstm_imod_string_fine", "Fine"),
	("cstm_imod_string_well_made", "Well Made"),
	("cstm_imod_string_sharp", "Sharp"),
	("cstm_imod_string_balanced", "Balanced"),
	("cstm_imod_string_tempered", "Tempered"),
	("cstm_imod_string_deadly", "Deadly"),
	("cstm_imod_string_exquisite", "Exquisite"),
	("cstm_imod_string_masterwork", "Masterwork"),
	("cstm_imod_string_heavy", "Heavy"),
	("cstm_imod_string_strong", "Strong"),
	("cstm_imod_string_powerful", "Powerful"),
	("cstm_imod_string_tattered", "Tattered"),
	("cstm_imod_string_ragged", "Ragged"),
	("cstm_imod_string_rough", "Rough"),
	("cstm_imod_string_sturdy", "Sturdy"),
	("cstm_imod_string_thick", "Thick"),
	("cstm_imod_string_hardened", "Hardened"),
	("cstm_imod_string_reinforced", "Reinforced"),
	("cstm_imod_string_superb", "Superb"),
	("cstm_imod_string_lordly", "Lordly"),
	("cstm_imod_string_lame", "Lame"),
	("cstm_imod_string_swaybacked", "Swaybacked"),
	("cstm_imod_string_stubborn", "Stubborn"),
	("cstm_imod_string_timid", "Timid"),
	("cstm_imod_string_meek", "Meek"),
	("cstm_imod_string_spirited", "Spirited"),
	("cstm_imod_string_champion", "Champion"),
	("cstm_imod_string_fresh", "Fresh"),
	("cstm_imod_string_day_old", "Day Old"),
	("cstm_imod_string_two_day_old", "Two Day Old"),
	("cstm_imod_string_smelling", "Smelling"),
	("cstm_imod_string_rotten", "Rotten"),
	("cstm_imod_string_large_bag", "Large Bag"),
]

def modmerge(var_set):
	try:
		var_name_1 = "strings"
		orig_strings = var_set[var_name_1]
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)
	
	index = [i for i, string in enumerate(orig_strings) if string[0] == "kingdom_1_adjective"][0]
	orig_strings.insert(index, ("kingdom_player_adjective", "{s11}")),
	
	# Create and fill the ordered dictionary strings, not adding any duplicates
	strings = collections.OrderedDict()
	for orig_string in orig_strings:
		if orig_string[0] not in strings:
			strings[orig_string[0]] = orig_string
	
	# Clear orig_strings and refill it from the ordered dictionary with duplicates removed
	del orig_strings[:]
	for string_id in strings:
		orig_strings.append(strings[string_id])
	
	# Add the new strings
	orig_strings.extend(new_strings)