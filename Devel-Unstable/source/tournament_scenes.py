# Tournament Play Enhancements (1.5) by Windyplains

from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *

scenes = [
# ARENA OVERHAUL MOD SCENES to be used with TOURNAMENT PLAY ENHANCEMENTS - Windyplains
# Credit for scenes: Adorno
("town_1_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0xa0001d9300031ccb0000156f000048ba0000361c"			,[]											,[]											,"outer_terrain_thir_new"			),
("town_2_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0xa0001d9300031ccb0000156f000048ba0000361c"			,[]											,[]											,"outer_terrain_thir_new"			),
("town_3_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0xa0001d9300031ccb0000156f000048ba0000361c"			,[]											,[]											,"outer_terrain_plain_farmountain"	),
("town_4_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0xa0001d9300031ccb0000156f000048ba0000361c"			,[]											,[]											,"outer_terrain_plain"				),
("town_5_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0xa0001d9300031ccb0000156f000048ba0000361c"			,[]											,[]											,"outer_terrain_plain_farmountain"	),
("town_6_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0xa0001d9300031ccb0000156f000048ba0000361c"			,[]											,[]											,"outer_terrain_plain"				),
("town_7_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0xa0001d9300031ccb0000156f000048ba0000361c"			,[]											,[]											,"outer_terrain_plain"				),
("town_8_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0xa0001d9300031ccb0000156f000048ba0000361c"			,[]											,[]											,"outer_terrain_plain_farmountain"	),
("town_9_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0x40001d9300031ccb0000156f000048ba0000361c"			,[]											,[]											,"outer_terrain_snow_farmountain"	),
("town_10_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0x00000002200005000005f57b00005885000046bd00006d9c"	,[]											,[]											,"outer_terrain_steppe"				),
("town_11_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0x40001d9300031ccb0000156f000048ba0000361c"			,[]											,[]											,"outer_terrain_snow"				),
("town_12_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0xa0001d9300031ccb0000156f000048ba0000361c"			,[]											,[]											,"outer_terrain_thir_new"			),
("town_13_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0xa0001d9300031ccb0000156f000048ba0000361c"			,[]											,[]																				),
("town_14_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0x00000002200005000005f57b00005885000046bd00006d9c"	,[]											,[]											,"outer_terrain_steppe"				),
("town_15_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0xa0001d9300031ccb0000156f000048ba0000361c"			,[]											,[]											,"outer_terrain_plain"				),
("town_16_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0xa0001d9300031ccb0000156f000048ba0000361c"			,[]											,[]											,"outer_terrain_plain"				),
("town_17_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0x00000002200005000005f57b00005885000046bd00006d9c"	,[]											,[]											,"outer_terrain_steppe"				),
("town_18_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0x00000002200005000005f57b00005885000046bd00006d9c"	,[]											,[]											,"outer_terrain_steppe"				),
("town_19_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0x00000002200005000005f57b00005885000046bd00006d9c"	,[]											,[]											,"outer_terrain_desert"				),
("town_20_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0x00000002200005000005f57b00005885000046bd00006d9c"	,[]											,[]											,"outer_terrain_desert"				),
("town_21_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0x00000002200005000005f57b00005885000046bd00006d9c"	,[]											,[]											,"outer_terrain_desert"				),
("town_22_arena_alternate"			,sf_generate									,"none"								,"none"								,(0,0)			,(100,100)		,-100	,"0x00000002200005000005f57b00005885000046bd00006d9c"	,[]											,[]											,"outer_terrain_desert"				),

]

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "scenes"
        orig_scenes = var_set[var_name_1]
        orig_scenes.extend(scenes)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)