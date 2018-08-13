## Prebattle Orders & Deployment by Caba'drin
## v0.91
## 14 Dec 2011

from header_meshes import *
meshes = [
  ## Prebatle Orders & Deployment Begin
  ("note_window_bottom", 0, "note_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("order_frame", 0, "order_frame", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag4", 0, "flag4", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag5", 0, "flag5", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag6", 0, "flag6", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag7", 0, "flag7", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag8", 0, "flag8", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag9", 0, "flag9", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ## Prebattle Orders & Deployment End
 ]
 
from util_common import *

def modmerge_meshes(orig_meshes):
    # add remaining meshes
    from util_common import add_objects
    num_appended, num_replaced, num_ignored = add_objects(orig_meshes, meshes)
    #print num_appended, num_replaced, num_ignored
	
	
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "meshes"
        orig_meshes = var_set[var_name_1]
        modmerge_meshes(orig_meshes)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)