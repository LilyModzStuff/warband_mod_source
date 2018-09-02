# Tournament Play Enhancements (1.5) by Windyplains

from header_quests import *

quests = [
  ("floris_active_tournament", "Attend Tournament in {s13}", 0,
  "{!}A tournament of champions has begun in the town of {s13} where you should attend."
  ),
]
from util_common import *
from util_wrappers import *
def modmerge_quests(orig_quests):
    pos = list_find_first_match_i(orig_quests, "quests_end")
    OpBlockWrapper(orig_quests).InsertBefore(pos, quests)	
	
def modmerge(var_set):
    try:
        var_name_1 = "quests"
        orig_quests = var_set[var_name_1]
        modmerge_quests(orig_quests)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)