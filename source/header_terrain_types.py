rt_water = 0
rt_mountain = 1
rt_steppe = 2
rt_plain = 3
rt_snow = 4
rt_desert = 5
rt_bridge = 7
rt_river  = 8
rt_mountain_forest = 9
rt_steppe_forest = 10
rt_forest = 11
rt_snow_forest = 12
rt_desert_forest = 13

##diplomacy start+
#These aren't technically terrain types, but they're used as terrain codes by
#script_dplmc_get_terrain_code_for_battle and dplmc_party_calculate_strength_in_terrain,
#which otherwise use rt_* variables.

dplmc_terrain_code_none = -1 #apply no terrain modifiers
dplmc_terrain_code_siege = -2 #a siege of a castle or a town
dplmc_terrain_code_village = -3 #a battle at a village
dplmc_terrain_code_unknown = -4 #apply no specific terrain modifiers, but still apply hero modfiers

##diplomacy end+
