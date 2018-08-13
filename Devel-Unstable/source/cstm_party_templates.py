from header_common import *
from header_parties import *
from header_troops import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *
from module_constants import *

from module_troops import troops

import math

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [

  #("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_recruit,5,10),(trp_swadian_militia,2,4)]),
  #("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,6),(trp_swadian_skirmisher,2,4)]),
  #("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,2,4),(trp_swadian_crossbowman,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)

  #("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_recruit,5,10),(trp_vaegir_footman,2,4)]),
  #("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,2,4),(trp_vaegir_skirmisher,2,4),(trp_vaegir_footman,1,2)]),
  #("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,2,3),(trp_vaegir_infantry,1,2)]),

  #("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_tribesman,3,5),(trp_khergit_skirmisher,4,9)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  #("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_khergit_horse_archer,2,4),(trp_khergit_skirmisher,1,2)]),
  #("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_khergit_veteran_horse_archer,2,3)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  #("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_footman,5,10),(trp_nord_recruit,2,4)]),
  #("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_huntsman,2,5),(trp_nord_archer,2,3),(trp_nord_footman,1,2)]),
  #("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_warrior,3,5)]),

  #("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_tribesman,5,10),(trp_rhodok_spearman,2,4)]),
  #("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_crossbowman,3,6),(trp_rhodok_trained_crossbowman,2,4)]),
  #("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_veteran_spearman,2,3),(trp_rhodok_veteran_crossbowman,1,2)]), 

  #("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sarranid_recruit,5,10),(trp_sarranid_footman,2,4)]),
  #("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sarranid_skirmisher,2,4),(trp_sarranid_veteran_footman,2,3),(trp_sarranid_footman,1,3)]),
  #("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarranid_horseman,3,5)]),

]

def troop_indexes_of_tier(skin, tier):
	return [find_troop(troops, troop[0]) for troop in tree.get_custom_troops_of_tier(skin, tier)]

def tier_stacks(skin, tier, min, max):
	troops = troop_indexes_of_tier(skin, tier)
	return [(troop, int(math.ceil(min * 1.0 / len(troops))), int(math.ceil(max * 1.0 / len(troops)))) for troop in troops]

for tree in CUSTOM_TROOP_TREES:
	for skin in CSTM_SKINS:
		id = "cstm_kingdom_player_%s_%d_reinforcements" % (tree.id, skin.id)
		
		party_templates.extend([
			(id + "_a", "{!}" + id + "_a", 0, 0, fac_commoners, 0, tier_stacks(skin, tier = 1, min = 5, max = 10) + tier_stacks(skin, tier = 2, min = 2, max = 4)),
			(id + "_b", "{!}" + id + "_b", 0, 0, fac_commoners, 0, tier_stacks(skin, tier = 3, min = 5, max = 10)),
			(id + "_c", "{!}" + id + "_c", 0, 0, fac_commoners, 0, tier_stacks(skin, tier = 4, min = 3, max = 5)),
		])

#for party_template in party_templates:
#	print ", ".join([party_template[0], party_template[1], ", ".join(["%d-%d %s" % (stack[1], stack[2], troops[stack[0]][2]) for stack in party_template[6]])])