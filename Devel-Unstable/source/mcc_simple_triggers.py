# Character Creation Presentation (1.0.3)

from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *
from module_quests import *
from module_constants import *

####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#  Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################



simple_triggers = [

## CCP 1.1+ ##
# TRIGGER: Warband 1.151 workaround to prompt a player without a banner to pick one post character creation.
(1,
	[
		(map_free),
		(eq, "$player_needs_a_banner", 1),
		(assign, "$player_needs_a_banner", 0),
		(start_presentation, "prsnt_custom_banner"), #I changed the var all by myself uwu ~Lily
	]),
## CCP 1.1- ##
]


# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "simple_triggers"
        orig_simple_triggers = var_set[var_name_1]
        orig_simple_triggers.extend(simple_triggers)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
