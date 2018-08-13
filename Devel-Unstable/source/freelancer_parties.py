# Freelancer (1.3) by Taragoth
# Released 11 July 2011
# Edits by Caba'drin 14 Dec 2011
# Mod-Merger'd by Windyplains, Monnikje and Caba'drin

from module_parties import *

parties = [ 
  ("freelancer_party_backup","{!}",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
 ]

   
from util_wrappers import *
from util_common import *

def modmerge_parties(orig_parties, check_duplicates = False):
	try:
		find_i = list_find_first_match_i( orig_parties, "zendar" )
		OpBlockWrapper(orig_parties).InsertBefore(find_i, parties)		
	except:
		import sys
		print "Injecton 1 failed:", sys.exc_info()[1]
		raise
	
# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "parties"
        orig_parties = var_set[var_name_1]
        modmerge_parties(orig_parties)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
