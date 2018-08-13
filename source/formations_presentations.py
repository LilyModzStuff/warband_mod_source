# Formations AI for Warband by Motomataru
# rel. 05/03/10
# EDIT FOR ORDER DISPLAY 11/19/10 by Caba'drin

from header_common import *
from header_presentations import *
from header_mission_templates import *
from header_operations import *
from header_triggers import *
from ID_meshes import *
from module_constants import *
import string

####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

# the following code block is to be inserted into "battle" presentation's trigger for ti_on_presentation_event_state_change
# just before the line (call_script, "script_update_order_flags_on_map"),
code_block1=[
# formations by motomataru
		  (assign, ":fixed_point_multiplier", 1),
		  (convert_to_fixed_point, ":fixed_point_multiplier"),
		  (set_fixed_point_multiplier, 100),
		  (call_script, "script_team_get_position_of_enemies", Enemy_Team_Pos, "$fplayer_team_no", grc_everyone),
		  
		  (try_for_range, ":division", 0, 9),
			(assign, ":do_it", 0),
			(try_begin),
				(eq, ":division", 0),
				(eq, "$g_formation_group0_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 1),
				(eq, "$g_formation_group1_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 2),
				(eq, "$g_formation_group2_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 3),
				(eq, "$g_formation_group3_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 4),
				(eq, "$g_formation_group4_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 5),
				(eq, "$g_formation_group5_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 6),
				(eq, "$g_formation_group6_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 7),
				(eq, "$g_formation_group7_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 8),
				(eq, "$g_formation_group8_selected", 1),
				(assign, ":do_it", 1),
			(try_end),
			(eq, ":do_it", 1),
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(neq, ":formation", formation_none),
			(copy_position, pos1, pos3),
			(call_script, "script_point_y_toward_position", pos1, Enemy_Team_Pos),			
			(call_script, "script_set_formation_destination", "$fplayer_team_no", ":division", pos1),
			
			(store_add, ":slot", slot_team_d0_size, ":division"),
			(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
			
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":spacing", "$fplayer_team_no", ":slot"),
			(call_script, "script_get_centering_amount", ":formation", ":troop_count", ":spacing"),
			(position_move_x, pos1, reg0),
			
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":spacing", ":formation"),
			(else_try),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":spacing"),
			(else_try),
				(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":spacing", ":formation"),
			(try_end),

			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", mordr_hold),	
		  (try_end),	#try_for_range ":division"
		  (set_fixed_point_multiplier, ":fixed_point_multiplier"),
# end formations
          (call_script, "script_update_order_flags_on_map"),
]


def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1127 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "presentations"
		orig_presentations = var_set[var_name_1]

		# START do your own stuff to do merging

		modmerge_formations_presentations(orig_presentations)

		# END do your own stuff
            
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)



from util_common import *
from util_wrappers import *
from util_presentations import *

def modmerge_formations_presentations(orig_presentations):
   # add_objects(orig_presentations, formations_presentations, True)	#add_presentations doesn't work
	
    # inject code into battle presentation
    try:
        find_i = list_find_first_match_i( orig_presentations, "battle" )
        battlep = PresentationWrapper(orig_presentations[find_i])
        codeblock = battlep.FindTrigger(ti_on_presentation_event_state_change).GetOpBlock()
        pos = codeblock.FindLineMatching( (call_script, "script_update_order_flags_on_map") )
        codeblock.InsertBefore(pos, code_block1)			
    except:
        import sys
        print "Injecton 1 failed:", sys.exc_info()[1]
        raise
