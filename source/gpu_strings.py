# Kingdom Management Tools (WIP) by Windyplains
# Released --/--/--

strings = [
###########################################################################################################################
#####                                                KMT 1.0 Additions                                                #####
###########################################################################################################################

	# Object Titles
	("kmt_reg0", "{reg0}"),
	("kmt_title_red", "Red"),
	("kmt_title_green", "Green"),
	("kmt_title_blue", "Blue"),
	("kmt_title_x_pos", "Pos X"),
	("kmt_title_y_pos", "Pos Y"),
	("kmt_title_x_size", "Size X"),
	("kmt_title_y_size", "Size Y"),
	("kmt_title_alpha", "Alpha"),
	("kmt_title_font_size", "Font Size"),
	("kmt_title_outline", "Outline Text"),
	("kmt_title_object_selected", "Selected Object #"),
	("kmt_title_RGB", "Color Changer"),
	("kmt_title_movement", "Object Movement"),
	("kmt_title_resizing", "Object Resizing"),
	("kmt_title_current_position", "Last Clicked Position:"),
	("kmt_reg1_reg2_pos", "( {reg1}, {reg2} )"),
	("kmt_undo", "Undo"),
	("kmt_hide", "Hide"),
	("kmt_show", "Show"),
]

from util_common import *

def modmerge_strings(orig_strings):
    # add remaining strings
    from util_common import add_objects
    num_appended, num_replaced, num_ignored = add_objects(orig_strings, strings)
    #print num_appended, num_replaced, num_ignored
	
	
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "strings"
        orig_strings = var_set[var_name_1]
        modmerge_strings(orig_strings)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)