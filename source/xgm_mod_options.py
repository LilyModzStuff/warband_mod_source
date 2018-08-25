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
    ("camp_fuck_setting", xgm_ov_combolabel, ["Disabled", "Consensual", "Consensual and non-consensual"], "Sex settings:", 0,
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

     ("camp_same_sex_on", xgm_ov_checkbox, [], "Same sex marriage:", 0,
	  "Toggles same sex marriage", 0,
        [(try_begin),
            (eq, "$g_disable_condescending_comments", 0),
            (assign, reg1, 0),
                        (else_try),
            (eq, "$g_disable_condescending_comments", 1),
            (assign, reg1, 1),
                (try_end),
             ],
     [
        (try_begin),
        (eq, reg1, 0), 
        (assign, "$g_disable_condescending_comments", 0),
        (else_try),
        (eq, reg1, 1),
        (assign, "$g_disable_condescending_comments", 2),
        (try_end),
        ],
),
    ("camp_polygamy", xgm_ov_checkbox, [], "Polygamy settings:", 0,
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

    ("camp_nohomobro", xgm_ov_checkbox, [], "Disable Gay", 0,
	  "Disables gay scenes.", 0,

		[
		(try_begin),
			(eq, "$g_nohomo", 0),
			(assign, reg1, 0),
		(else_try),
			(eq, "$g_nohomo", 1),
			(assign, reg1, 1),
		(try_end),
		],
		[
        (try_begin),
        (eq, reg1, 0), 
        (assign, "$g_nohomo", 0),
        (else_try),
        (eq, reg1, 1),
        (assign, "$g_nohomo", 1),
        (try_end),
        ],
	), 

    ("camp_dark_hunters", xgm_ov_checkbox, [], "Enable Black Khergits and Dark Hunters:", 0,
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
    ("camp_realistic_wounding", xgm_ov_checkbox, [], "Realistic wounding:", 0,
	  "Toggles realistic wounding", 0,
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
