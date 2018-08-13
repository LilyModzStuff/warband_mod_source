from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_scenes import *
from module_constants import *

from cstm_troop_trees import *

import collections

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield

## IT'S UNINTUITIVE BUT YOU CAN'T EDIT THE CUSTOM TROOPS IN ANY WAY HERE - CHECK OUT cstm_troop_trees.py

def blank_troop_with_flags(id, flags):
	return [id, id, id, flags, 0, 0, fac_player_supporters_faction, [], level(1)|def_attrib, 0, 0, 0, 0]

def blank_troop(id):
	return blank_troop_with_flags(id, tf_hero)

def modmerge(var_set):
	try:
		var_name_1 = "troops"
		orig_troops = var_set[var_name_1]
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)
	
	bandit_troop = -1
	try:
		bandit_troop = orig_troops[trp_looter][0]	# This just lets us check if the looter troop actually exists and raise an exception if it doesn't
		bandit_troop = "looter"
	except NameError:
		try:
			bandit_troop = bandits_begin[4:]
			print
			print "Looter not found, inserting custom troops before " + bandits_begin[4:]
		except NameError:
			print
			print "Couldn't find Looter or bandits_begin, adding custom troops at end of troop list"
			bandit_troop = -1
	
	# Add the custom troop trees from cstm_troop_trees.py
	for tree in CUSTOM_TROOP_TREES:
		for skin in CSTM_SKINS:
			faction_troops_end_index = find_troop(orig_troops, bandit_troop) if bandit_troop > 0 else -1
			tree.add_to_troop_list_with_skin(orig_troops, skin, faction_troops_end_index)
	
	faction_troops_end_index = find_troop(orig_troops, bandit_troop) if bandit_troop > 0 else -1
	for troop in orig_troops[faction_troops_end_index:]:
		if len(troop) >= 15:
			troop[14] += 1
			if len(troop) == 16 and troop[15] > 0:
				troop[15] += 1
	
	# Add presentation troops (just used in presentations for troop image, nothing else - used instead of dummies because of difference in equipment appearance of hero/non-hero troops)
	for skin in CSTM_SKINS:
		id = "cstm_presentation_troop_" + str(skin.id)
		orig_troops.append([id, id, id, skin.id|tf_guarantee_all, 0, 0, fac_commoners, [], level(1)|def_attrib, 0, 0, skin.face_code_1, skin.face_code_2])
	
	# Add markers of custom troops/dummies ending
	faction_troops_end_index = find_troop(orig_troops, bandit_troop) if bandit_troop > 0 else -1
	orig_troops.insert(faction_troops_end_index, blank_troop("cstm_custom_troops_end"))
	orig_troops.append(blank_troop("cstm_custom_troop_dummies_end"))
	
	# The following are essentially just used as arrays, storing values in their slots
	orig_troops.append(blank_troop("cstm_inventory_values"))
	orig_troops.append(blank_troop("cstm_proficiency_requirements"))
	
	for item_type in cstm_item_type_strings:
		orig_troops.append(blank_troop(cstm_items_array_id(item_type)))
	
	# These are also arrays, but used to store values of overlays in presentations (e.g. the associated item of an item image overlay)
	orig_troops.append(blank_troop("cstm_overlay_troops"))
	orig_troops.append(blank_troop("cstm_overlay_items"))
	orig_troops.append(blank_troop("cstm_overlay_is_store_item"))
	for string in ["attribute", "skill", "proficiency"]:
		orig_troops.append(blank_troop("cstm_overlay_is_%s_box" % (string)))
		orig_troops.append(blank_troop("cstm_overlay_%s" % (string)))
	
	# This troop is given an item and the game continually checks if it has disappeared. If it has, the game knows equipments have been reset and restores the custom troop inventories.
	orig_troops.append(blank_troop_with_flags("cstm_load_check", 0))