# Dynamic Troop Trees by Dunde, modified by Caba'drin.

from header_meshes import *

####################################################################################################################
#  Each mesh record contains the following fields:
#  1) Mesh id: used for referencing meshes in other files. The prefix mesh_ is automatically added before each mesh id.
#  2) Mesh flags. See header_meshes.py for a list of available flags
#  3) Mesh resource name: Resource name of the mesh
#  4) Mesh translation on x axis: Will be done automatically when the mesh is loaded
#  5) Mesh translation on y axis: Will be done automatically when the mesh is loaded
#  6) Mesh translation on z axis: Will be done automatically when the mesh is loaded
#  7) Mesh rotation angle over x axis: Will be done automatically when the mesh is loaded
#  8) Mesh rotation angle over y axis: Will be done automatically when the mesh is loaded
#  9) Mesh rotation angle over z axis: Will be done automatically when the mesh is loaded
#  10) Mesh x scale: Will be done automatically when the mesh is loaded
#  11) Mesh y scale: Will be done automatically when the mesh is loaded
#  12) Mesh z scale: Will be done automatically when the mesh is loaded
####################################################################################################################

meshes = [
  ("pic_arms_swadian", 0, "pic_arms_swadian", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_vaegir", 0, "pic_arms_vaegir", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_khergit", 0, "pic_arms_khergit", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_nord", 0, "pic_arms_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_rhodok", 0, "pic_arms_rhodok", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_sarranid_arms", 0, "pic_sarranid_arms", 0, 0, 0, 0, 0, 0, 1, 1, 1),
# Dunde's BEGIN  
  ("pic_swad", 0, "pic_swad", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_vaegir", 0, "pic_vaegir", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("pic_khergit", 0, "pic_khergit", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_nord", 0, "pic_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_rhodock", 0, "pic_rhodock", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_sarranid_encounter", 0, "pic_sarranid_encounter", 0, 0, 0, 0, 0, 0, 1, 1, 1),
# Dunde's END 

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