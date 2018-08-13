# Banking (2.0) by Lazeras
# Released 1 December 2011
from header_common import *
from header_operations import *
from header_triggers import *
from module_constants import *

####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################

# Manualy all lines under the `triggers` into the bottom of the module_triggers at the bottom of the file
triggers = [
########################################################################################################################
#  KAOS BANKING KIT START                                                                                              #
########################################################################################################################
  (0.1, 0, ti_once, [(map_free,0)], 
  [
  	(assign, "$g_bank_debt_interest_rate", 15),
    (assign, "$g_bank_deposit_interest_rate", 5),
    (assign, "$bank_availability", 0),         
  ]),
########################################################################################################################
#  KAOS BANKING KIT END                                                                                                #
########################################################################################################################
]


# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "triggers"
        orig_triggers = var_set[var_name_1]
        orig_triggers.extend(triggers)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)