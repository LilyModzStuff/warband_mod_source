from header_quests import *

quests = [
  ("freelancer_enlisted", "Enlisted in the Party of {s13}", 0,
   "{!}You are currently enlisted in the party of {s13} of {s14}."),
  ("freelancer_vacation", "Enlisted: On Leave", 0,
   "{!}You have been granted leave from the party of {s13} of {s14}."),
  ("freelancer_captured", "Enlisted: Captured", 0,
   "{!}Your commander's party has been defeated and you have been captured. Return to the service of {s13} of {s14}."),
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