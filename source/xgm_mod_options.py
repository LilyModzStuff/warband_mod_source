from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
#import string

from xgm_mod_options_header import *

############################################################################
## 0) overlay id (not used atm, but can allow searches in future. just put something unique)
## 1) overlay type (defined in xgm_mod_options_header)
## 2) overlay type specific parameters (e.g. for number box, it can be lower/upper range, for cbobox, it would be the cbo items etc)
##    a) xgm_ov_numberbox : lower_bound(inclusive), upper_bound(exclusive). e.g. [0,101] for range of values from 0-100
##    b) xgm_ov_combolabel/xgm_ov_combobutton  : list of combo items. e.g. ["option1", "option2", "option3"]
##    c) xgm_ov_slider : lower_bound(inclusive), upper_bound(exclusive). e.g. [0,101] for range of values from 0-100
##    d) xgm_ov_checkbox : not used fttb. just leave empty. e.g. []
## 3) text label
## 4) reserved for text label flags
## 5) description (unused for now. may be used for stuff like tooltip in future)
## 6) reserved for description flags
## 7) initialization op block.  Used for updating the overlay values from game values. Must assign the desired value to reg1.
## 8) update op block.  Used for updating game values from overlay values. The overlay value is in reg1.
## 9) optional. reserved for option page id. unused for now. leave out for options using general page.
############################################################################

mod_options = [

    ("camp_fuck_setting", xgm_ov_combolabel, ["Disabled", "Consensual Only", "All Enabled"], "Sexual Content:", 0,
	  "Settings for sexual content in game.", 0,
            [(try_begin),
            (eq, "$g_sexual_content", 0),
            (assign, reg1, 0),
                        (else_try),
            (eq, "$g_sexual_content", 1),
            (assign, reg1, 1),
                        (else_try),
            (eq, "$g_sexual_content", 2),
            (assign, reg1, 2),
                (try_end),],
     [(try_begin),
        (eq, reg1, 0),
        (assign, "$g_sexual_content", 0),
        (else_try),
        (eq, reg1, 1),
        (assign, "$g_sexual_content", 1),
        (else_try),
        (eq, reg1, 2),
        (assign, "$g_sexual_content", 2),
      (try_end),
      ],

),

    ("dplmc_woman_prejudice", xgm_ov_combolabel, ["Historical", "Tolerant", "Utopian"], "Diplomacy - Prejudice:", 0,
	  "Setting for Diplomacy's prejudice changes.", 0,
		[
				(assign, reg1, "$g_disable_condescending_comments"),
		],
		[
				(assign, "$g_disable_condescending_comments", reg1),
		],
	),

    ("camp_polygamy", xgm_ov_checkbox, [], "Polygamy:", 0,
	  "Toggles polygamy settings", 0,

             [(try_begin),
            (eq, "$g_polygamy", 0),
            (assign, reg1, 0),
                        (else_try),
            (eq, "$g_polygamy", 1),
            (assign, reg1, 1),
                (try_end),
             ],
     [
        (try_begin),
        (eq, reg1, 0),
        (assign, "$g_polygamy", 0),
        (else_try),
        (eq, reg1, 1),
        (assign, "$g_polygamy", 1),
        (try_end),
        ],
),

    ( "camp_nohomobro", xgm_ov_checkbox ,  [],
        "Disable Gay:", 0,
        "Disables gay scenes.", 0,
        [  # initialization block (set value in reg1)
            (assign, reg1, "$g_nohomo"),
        ],
        [  # update block (value is in reg1)
            (assign, "$g_nohomo", reg1),
        ],
    ),

    ("camp_dark_hunters", xgm_ov_checkbox, [], "Black Khergits and Dark Hunters:", 0,
     "Settings for Dark Hunters and Black Khergits.", 0,
  [
            (try_begin),
            (eq, "$g_dark_hunters_enabled", 0),
            (assign, reg1, 0),
            (else_try),
            (eq, "$g_dark_hunters_enabled", 1),
            (assign, reg1, 1),
            (try_end),
   ],
        [
        (try_begin),
        (eq, reg1, 0),

        (assign, "$g_dark_hunters_enabled", 0),
        (assign, ":removed", 0),
        (try_for_parties, ":party_no"),
        (party_get_template_id, ":ptid", ":party_no"),
        (this_or_next|eq, ":ptid", "pt_dark_hunters"),
        (eq, ":ptid", "pt_black_khergit_raiders"),
        (remove_party, ":party_no"),
        (val_add, ":removed", 1),
        (try_end),
        (assign, reg0, ":removed"),
        (display_message, "@{reg0} parties removed from the map."),
        (else_try),
        (eq, reg1, 1),
        (assign, "$g_dark_hunters_enabled", 1),
      (try_end),
        ],
	),

    ( "keep_companions", xgm_ov_checkbox ,  [],
        "Keep Companions:", 0,
        "Setting for keeping companions after defeat", 0,
        [  # initialization block (set value in reg1)
            (assign, reg1, "$g_keep_companions"),
        ],
        [  # update block (value is in reg1)
            (assign, "$g_keep_companions", reg1),
        ],
    ),

    ( "disable_complaints", xgm_ov_checkbox ,  [],
        "Disable Complaints:", 0,
        "Setting for disabling companion complaints", 0,
        [  # initialization block (set value in reg1)
            (assign, reg1, "$disable_npc_complaints"),
        ],
        [  # update block (value is in reg1)
            (assign, "$disable_npc_complaints", reg1),
        ],
    ),

    ( "disable_bodyguard", xgm_ov_checkbox ,  [],
        "Disable Bodyguards:", 0,
        "Setting for disabling companions as bodyguards", 0,
        [  # initialization block (set value in reg1)
            (assign, reg1, "$disable_bodyguards"),
        ],
        [  # update block (value is in reg1)
            (assign, "$disable_bodyguards", reg1),
        ],
    ),

    ("camp_realistic_wounding", xgm_ov_checkbox, [], "Realistic Casualties:", 0,
	  "Toggles realistic wounding for other damage types", 0,
            [(try_begin),
            (eq, "$g_realistic_wounding", 0),
            (assign, reg1, 0),
                        (else_try),
            (eq, "$g_realistic_wounding", 1),
            (assign, reg1, 1),
                (try_end),
             ],
     [
        (try_begin),
        (eq, reg1, 0),
        (assign, "$g_realistic_wounding", 0),
        (else_try),
        (eq, reg1, 1),
        (assign, "$g_realistic_wounding", 1),
        (try_end),
        ],

),

    ("enable_shield_bash", xgm_ov_combolabel, ["Disabled", "Player Only", "All Combatants"], "Shield Bash:", 0,
	  "Setting for Diplomacy's prejudice changes.", 0,
		[
			(assign, reg1, "$g_enable_shield_bash"),
		],
		[
			(assign, "$g_enable_shield_bash", reg1),
		],
	),

    ("horizontal_divide", xgm_ov_line, [], "", 0,"", 0,[],[],),

    ( "dplmc_horsespeed", xgm_ov_checkbox ,  [],
        "Diplomacy - Horse Speed:", 0,
        "Setting for Diplomacy's horse speed changes", 0,
        [  # initialization block (set value in reg1)
			(store_sub,reg1,1,"$g_dplmc_horse_speed"),
        ],
        [  # update block (value is in reg1)
            (store_sub,"$g_dplmc_horse_speed",1,reg1),
        ],
    ),

    ( "dplmc_battlecontinue", xgm_ov_checkbox ,  [],
        "Diplomacy - Battle Continuation:", 0,
        "Setting for Diplomacy's battle continuation", 0,
        [  # initialization block (set value in reg1)
            (store_sub,reg1,1,"$g_dplmc_battle_continuation"),
        ],
        [  # update block (value is in reg1)
            (store_sub,"$g_dplmc_battle_continuation",1,reg1),
        ],
    ),

    ( "dplmc_disguise", xgm_ov_checkbox ,  [],
        "Diplomacy - Disguise System:", 0,
        "Setting for Diplomacy's disguise system", 0,
        [  # initialization block (set value in reg1)
            (assign, reg1, "$g_dplmc_player_disguise"),
        ],
        [  # update block (value is in reg1)
            (assign, "$g_dplmc_player_disguise", reg1),
        ],
    ),

    ( "dplmc_terrain_advantage", xgm_ov_checkbox ,  [],
        "Diplomacy - Autocalc Terrain Advantage:", 0,
        "Setting for Diplomacy's terrain advantage.", 0,
        [  # initialization block (set value in reg1)
		(try_begin),
            (eq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_DISABLE),
            (assign, reg1, 0),
         (else_try),
            (eq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
            (assign, reg1, 1),
        (try_end),
        ],
		[  # update block (value is in reg1)
        (try_begin),
        (eq, reg1, 0),
        (assign, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_DISABLE),
        (else_try),
        (eq, reg1, 1),
        (assign, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
        (try_end),
        ],
    ),

    ( "dplmc_lord_recycling", xgm_ov_checkbox ,  [],
        "Diplomacy - Returning From Exile:", 0,
        "Setting for Diplomacy's terrain advantage.", 0,
        [  # initialization block (set value in reg1)
		(try_begin),
            (eq, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_DISABLE),
            (assign, reg1, 0),
         (else_try),
            (eq, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_ENABLE),
            (assign, reg1, 1),
        (try_end),
        ],
		[  # update block (value is in reg1)
        (try_begin),
        (eq, reg1, 0),
        (assign, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_DISABLE),
        (else_try),
        (eq, reg1, 1),
        (assign, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_ENABLE),
        (try_end),
        ],
    ),

    ("dplmc_ai_changes_a", xgm_ov_combolabel, ["Disabled", "Low", "Medium", "High"], "Diplomacy - AI Changes:", 0,
	  "Setting for Diplomacy's AI changes.", 0,
		[
			(try_begin),
				(eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_DISABLE),
				(assign, reg1, 0),
			(else_try),
				(eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
				(assign, reg1, 1),
			(else_try),
				(eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
				(assign, reg1, 2),
			(else_try),
				(eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
				(assign, reg1, 3),
			(try_end),
		],
		[
			(try_begin),
				(eq, reg1, 0),
				(assign, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_DISABLE),
			(else_try),
				(eq, reg1, 1),
				(assign, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
			(else_try),
				(eq, reg1, 2),
				(assign, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
			(else_try),
				(eq, reg1, 3),
				(assign, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
			(try_end),
		],
	),

    ("dplmc_gold_changes", xgm_ov_combolabel, ["Disabled", "Low", "Medium", "High"], "Diplomacy - Economy Changes:", 0,
	  "Setting for Diplomacy's economy changes.", 0,
		[
			(try_begin),
				(eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_DISABLE),
				(assign, reg1, 0),
			(else_try),
				(eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
				(assign, reg1, 1),
			(else_try),
				(eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
				(assign, reg1, 2),
			(else_try),
				(eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
				(assign, reg1, 3),
			(try_end),
		],
		[
			(try_begin),
				(eq, reg1, 0),
				(assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_DISABLE),
			(else_try),
				(eq, reg1, 1),
				(assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
			(else_try),
				(eq, reg1, 2),
				(assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
			(else_try),
				(eq, reg1, 3),
				(assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
			(try_end),
		],
	),

    ("horizontal_divide", xgm_ov_line, [], "", 0,"", 0,[],[],),

    ("minimap_setting", xgm_ov_combolabel, ["Compass Style", "Small Minimap", "Medium Minimap", "Large Minimap", "Disabled"], "Battle Minimap Overlay:", 0,
	  "Setting for the minimap.", 0,
		[
			(try_begin),
				(eq, "$g_minimap_style", -1),
				(assign, reg1, 4),
			(else_try),
				(assign, reg1, "$g_minimap_style"),
			(try_end),
		],
		[
			(try_begin),
				(eq, reg1, 4),
				(assign, "$g_minimap_style", -1),
			(else_try),
				(assign, "$g_minimap_style", reg1),
			(try_end),
		],
	),

    ("minimap_setting", xgm_ov_combolabel, ["Disabled", "Only Allies", "Only Enemies", "All Troops"], "Troop HP Bars:", 0,
	  "Setting for troop HP bars.", 0,
		[
			(try_begin), # Ally
				(eq, "$g_hp_bar_enemy", 0),
				(eq, "$g_hp_bar_ally", 1),
				(assign, reg1, 1),
			(else_try), # Enemy
				(eq, "$g_hp_bar_enemy", 1),
				(eq, "$g_hp_bar_ally", 0),
				(assign, reg1, 2),
			(else_try), # Both
				(eq, "$g_hp_bar_enemy", 1),
				(eq, "$g_hp_bar_ally", 1),
				(assign, reg1, 3),
			(else_try), # None
				(assign, reg1, 0),
			(try_end),
		],
		[
			(try_begin), # Ally
				(eq, reg1, 1),
				(assign, "$g_hp_bar_enemy", 0),
				(assign, "$g_hp_bar_ally", 1),
			(else_try), # Enemy
				(eq, reg1, 2),
				(assign, "$g_hp_bar_enemy", 1),
				(assign, "$g_hp_bar_ally", 0),
			(else_try), # Both
				(eq, reg1, 3),
				(assign, "$g_hp_bar_enemy", 1),
				(assign, "$g_hp_bar_ally", 1),
			(else_try), # None
				(assign, "$g_hp_bar_enemy", 0),
				(assign, "$g_hp_bar_ally", 0),
			(try_end),
		],
	),

    ("minimap_setting", xgm_ov_numberbox, [3,81], "HP Bar Distance Limit:", 0,
	  "Setting for the HP Bars.", 0,
		[
			(assign, reg1, "$g_hp_bar_dis_limit"),
		],
		[
			(assign, "$g_hp_bar_dis_limit", reg1),
		],
	),

    ("camp_troop_ratio_bar", xgm_ov_checkbox, [], "Troop ratio bar:", 0,
	  "Toggles troop ratio bar", 0,

             [(try_begin),
            (eq, "$g_troop_ratio_bar", 0),
            (assign, reg1, 0),
                        (else_try),
            (eq, "$g_troop_ratio_bar", 1),
            (assign, reg1, 1),
                (try_end),
             ],
     [
        (try_begin),
        (eq, reg1, 0),
        (assign, "$g_troop_ratio_bar", 0),
        (else_try),
        (eq, reg1, 1),
        (assign, "$g_troop_ratio_bar", 1),
        (try_end),
        ],
),

    ("camp_decapitation", xgm_ov_checkbox, [], "Decapitation:", 0,
	  "Toggles Decapitation", 0,

             [(try_begin),
            (eq, "$g_decapitation_enabled", 0),
            (assign, reg1, 0),
                        (else_try),
            (eq, "$g_decapitation_enabled", 1),
            (assign, reg1, 1),
                (try_end),
             ],
     [
        (try_begin),
        (eq, reg1, 0),
        (assign, "$g_decapitation_enabled", 0),
        (else_try),
        (eq, reg1, 1),
        (assign, "$g_decapitation_enabled", 1),
        (try_end),
        ],
),

    ("horizontal_divide", xgm_ov_line, [], "", 0,"", 0,[],[],),

    ( "op_cheatmode", xgm_ov_checkbox ,  [],
        "Cheat mode:", 0,
        "This sets the in-game cheat mode", 0,
        [  # initialization block (set value in reg1)
            (assign, reg1, "$cheat_mode"),
        ],
        [  # update block (value is in reg1)
            (assign, "$cheat_mode", reg1),
        ],
    ),


] # mod_options


# TODO: add option pages here


# collation of all *_mod_options.py from active mods
# import and merge related variables from all {active_mod}_mod_options.py for all active mods
#try:
#    from modmerger_options import options, mods_active
#    from modmerger import mod_get_process_order, mod_is_active
#    from util_common import add_objects
#    modcomp_name = "mod_options"
#    var_list = ["mod_options",]

    #from modmerger import modmerge
    #modmerge(var_set)

#    mod_process_order = mod_get_process_order(modcomp_name)

#    vars_to_import= ["mod_options"]

#    for x in mod_process_order:
#        if(mod_is_active(x) and x <> "xgm_mod_options"): # must exclude this file since we are using this file as base
#            try:
                #mergefn_name = "modmerge_%s"%(modcomp_name)
#                target_module_name = "%s_%s"%(x,modcomp_name)

#                _temp = __import__( target_module_name , globals(), locals(), vars_to_import,-1)
#                logger.info("Merging objects for component \"%s\" from mod \"%s\"..."%(modcomp_name,x))
#
#                add_objects(mod_options, _temp.mod_options) # import from target module.
#
#                # TODO: collect option pages

#            except ImportError:
#                errstring = "Failed importing for component \"%s\" for mod \"%s\"." % (modcomp_name, x)
#                logger.debug(errstring)
#        else:
#            errstring = "Mod \"%s\" not active for Component \"%s\"." % (x, modcomp_name)
#            logger.debug(errstring)

#except:
#    raise
# collation end

# At this point, mod_options will contain the list of all mod_options specified.



## utility functions

from util_wrappers import *

# helper wrapper to access mod_options
class ModOptionWrapper(BaseWrapper):

    def __init__(self, _data):
        # verify _data
        if( not isinstance(_data,TupleType) or (len(_data)<2)):
            raise ValueError("ItemSetWrapper: Wrapped must be a tuple.")
        BaseWrapper.__init__(self,_data)


    def GetId(self):
        return self.data[0]

    def GetType(self):
        return self.data[1]

    def GetParameters(self):
        if len(self.data) >2:
            return self.data[2]
        return None

    def GetParameter(self, i):
        if len(self.data) >2:
            return self.data[2][i]
        return None

    def GetTextLabel(self):
        if len(self.data) >3:
            return self.data[3]
        return None

    def GetTextLabelFlags(self):
        if len(self.data) >4:
            return self.data[4]
        return None

    def GetDescription(self):
        if len(self.data) >5:
            return self.data[5]
        return None

    def GetDescriptionFlags(self):
        if len(self.data) >6:
            return self.data[6]
        return None

    def GetInitializeBlock(self):
        if len(self.data) >7:
            return OpBlockWrapper(self.data[7])
        return None

    def GetUpdateBlock(self):
        if len(self.data) >8:
            return OpBlockWrapper(self.data[8])
        return None

    def GetHeight(self):
        if self.GetType() == xgm_ov_line:
            return xgm_mod_options_line_height
        elif self.GetType() in [xgm_ov_checkbox, xgm_ov_numberbox, xgm_ov_combolabel]:
            return xgm_mod_options_property_height
        return 0 # no other types supported

## class ModOptionWrapper



# this function will compute the total height required for a list of mod_options.
def mod_options_get_total_height(_mod_options = mod_options):
    height = 0
    for x in _mod_options:
        aModOption = ModOptionWrapper(x)
        height += aModOption.GetHeight()
    # for x in _mod_options:
    return height;
## mod_options_get_total_height
