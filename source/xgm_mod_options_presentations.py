from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
import string

## xgm stuff
from xgm_mod_options_header import *
from xgm_mod_options import *
##For the player banner
from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *
from module_constants import *


####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

presentations = [
  ("mod_option", 0, mesh_load_window, [


    (ti_on_presentation_load,
      [
 
      ]),


      #(ti_on_presentation_run,
        #[
        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_run"),
        ####### mouse fix pos system #######
      #]),


    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
 
        ## to be generated
 
      ]),
    ]),


] # presentations




from util_wrappers import *
from util_presentations import *

def generate_presentation_load_script(_mod_options = mod_options):
    opblock = OpBlockWrapper([])
    
    total_height = mod_options_get_total_height()
    if  total_height < xgm_mod_options_pane_height - xgm_mod_options_property_height/2:
        total_height = xgm_mod_options_pane_height - xgm_mod_options_property_height/2
	

    cur_posy = total_height
    cur_overlay_index = 0

    overlay_var = "$g_presentation_obj_%s" % cur_overlay_index

    opblock.Append([
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (str_clear, s0),
        (assign, overlay_var, 0), # forced initialization
        (create_text_overlay, overlay_var, s0, tf_scrollable),
        (position_set_x, pos1, xgm_mod_options_pane_posx),
        (position_set_y, pos1, xgm_mod_options_pane_posy),
        (overlay_set_position, overlay_var, pos1),
        (position_set_x, pos1, xgm_mod_options_pane_width),
        (position_set_y, pos1, xgm_mod_options_pane_height),
        (overlay_set_area_size, overlay_var, pos1),
        (set_container_overlay, overlay_var),

        (position_set_x, pos1, xgm_mod_options_property_posx),    
        #(assign, ":cur_posy", cur_posy),
    ])
    
    cur_overlay_index += 1    

### testline start
### this just adds vertical lines used for checking overlay alignments
    #opblock.Append([
        #(assign, ":size_x", 2),
        #(assign, ":size_y", total_height),
        #(assign, ":pos_x", xgm_mod_options_property_width - xgm_mod_options_property_value_width),
        #(assign, ":pos_y", 0),
#
        #(create_mesh_overlay, reg1, "mesh_white_plane"),
        #(val_mul, ":size_x", 50),
        #(val_mul, ":size_y", 50),
        #(position_set_x, pos1, ":size_x"),
        #(position_set_y, pos1, ":size_y"),
        #(overlay_set_size, reg1, pos1),
        #(position_set_x, pos1, ":pos_x"),
        #(position_set_y, pos1, ":pos_y"),
        #(overlay_set_position, reg1, pos1),
        #(overlay_set_color, reg1, 0x000000),
    #])
#
    #opblock.Append([
        #(assign, ":size_x", 2),
        #(assign, ":size_y", total_height),
        #(assign, ":pos_x", xgm_mod_options_property_width - xgm_mod_options_property_value_width/2),
        #(assign, ":pos_y", 0),
#
        #(create_mesh_overlay, reg1, "mesh_white_plane"),
        #(val_mul, ":size_x", 50),
        #(val_mul, ":size_y", 50),
        #(position_set_x, pos1, ":size_x"),
        #(position_set_y, pos1, ":size_y"),
        #(overlay_set_size, reg1, pos1),
        #(position_set_x, pos1, ":pos_x"),
        #(position_set_y, pos1, ":pos_y"),
        #(overlay_set_position, reg1, pos1),
        #(overlay_set_color, reg1, 0x000000),
    #])
#
    #opblock.Append([
        #(assign, ":size_x", 2),
        #(assign, ":size_y", total_height),
        #(assign, ":pos_x", xgm_mod_options_property_width),
        #(assign, ":pos_y", 0),
#
        #(create_mesh_overlay, reg1, "mesh_white_plane"),
        #(val_mul, ":size_x", 50),
        #(val_mul, ":size_y", 50),
        #(position_set_x, pos1, ":size_x"),
        #(position_set_y, pos1, ":size_y"),
        #(overlay_set_size, reg1, pos1),
        #(position_set_x, pos1, ":pos_x"),
        #(position_set_y, pos1, ":pos_y"),
        #(overlay_set_position, reg1, pos1),
        #(overlay_set_color, reg1, 0x000000),
    #])
#
### testline end



    for x in mod_options:
        aModOption = ModOptionWrapper(x)
        if aModOption.GetType() == xgm_ov_line:
            
            # Create line
            opblock.Append([
                (assign, ":size_x", xgm_mod_options_line_width),
                (assign, ":size_y", xgm_mod_options_line_height),
                (assign, ":pos_x", xgm_mod_options_line_posx),
                (assign, ":pos_y", cur_posy + xgm_mod_options_line_offsety),

                (create_mesh_overlay, reg1, "mesh_white_plane"),
                (val_mul, ":size_x", 50),
                (val_mul, ":size_y", 50),
                (position_set_x, pos1, ":size_x"),
                (position_set_y, pos1, ":size_y"),
                (overlay_set_size, reg1, pos1),
                (position_set_x, pos1, ":pos_x"),
                (position_set_y, pos1, ":pos_y"),
                (overlay_set_position, reg1, pos1),
                (overlay_set_color, reg1, 0x000000),
            ])
            #cur_posy -= xgm_mod_options_line_height # assume line don't take up height for now
            #opblock.Append([
                #(assign, ":cur_posy", cur_posy),
            #])
            
        elif aModOption.GetType() in [xgm_ov_checkbox, xgm_ov_numberbox, xgm_ov_combolabel, xgm_ov_combobutton, xgm_ov_slider]:    
            # Create label
            labeltext = aModOption.GetTextLabel()
	
            if  (not labeltext is None) and ( labeltext <> ""):	
                textflags = tf_vertical_align_center | aModOption.GetTextLabelFlags()                
                opblock.Append([
                    (position_set_x, pos1, xgm_mod_options_property_label_posx),
                    (create_text_overlay, reg0, "@%s" % aModOption.GetTextLabel(), tf_vertical_align_center),
                    (position_set_y, pos1, cur_posy),
                    (overlay_set_position, reg0, pos1),
                ])            
            # Create value           
            
            # Number box

            if( aModOption.GetType() == xgm_ov_numberbox ):
                overlay_var = "$g_presentation_obj_%s" % cur_overlay_index
                opblock.Append([                       
                    (assign, overlay_var, 0), # forced initialization
                    (position_set_x, pos1, xgm_mod_options_property_value_posx + xgm_ov_numberbox_offsetx),
                    (create_number_box_overlay, overlay_var, aModOption.GetParameter(0), aModOption.GetParameter(1)),
                    (position_set_y, pos1, cur_posy + xgm_ov_numberbox_offsety),
                    (overlay_set_position, overlay_var, pos1),
                    (position_set_x, pos1, xgm_ov_numberbox_scalex),
                    (position_set_y, pos1, xgm_ov_numberbox_scaley),
                    (overlay_set_size, overlay_var, pos1),

                ])            

                opblock.Append(aModOption.GetInitializeBlock()) # splice in initialize op block
                
                opblock.Append([                       
                    (overlay_set_val, overlay_var, reg1),
                ])                       
                cur_overlay_index += 1

            # slider
            elif( aModOption.GetType() == xgm_ov_slider ):
                overlay_var = "$g_presentation_obj_%s" % cur_overlay_index
                opblock.Append([                       
                    (assign, overlay_var, 0), # forced initialization
                    (position_set_x, pos1, xgm_mod_options_property_value_posx + xgm_ov_slider_offsetx),
                    (create_slider_overlay, overlay_var, aModOption.GetParameter(0), aModOption.GetParameter(1)),
                    (position_set_y, pos1, cur_posy + xgm_ov_slider_offsety),
                    (overlay_set_position, overlay_var, pos1),
                    (position_set_x, pos1, xgm_ov_slider_scalex),
                    (position_set_y, pos1, xgm_ov_slider_scaley),
                    (overlay_set_size, overlay_var, pos1),

                ])            

                opblock.Append(aModOption.GetInitializeBlock()) # splice in initialize op block
                
                opblock.Append([                       
                    (overlay_set_val, overlay_var, reg1),
                ])                       
                cur_overlay_index += 1

            # Check box
            elif( aModOption.GetType() == xgm_ov_checkbox ):
                overlay_var = "$g_presentation_obj_%s" % cur_overlay_index
                opblock.Append([                       
                    (assign, overlay_var, 0), # forced initialization
                    (position_set_x, pos1, xgm_mod_options_property_value_posx + xgm_ov_checkbox_offsetx),
                    (create_check_box_overlay, overlay_var, "mesh_checkbox_off", "mesh_checkbox_on"),
                    (position_set_y, pos1, cur_posy + xgm_ov_checkbox_offsety),
                    (overlay_set_position, overlay_var, pos1),
                ])            

                opblock.Append(aModOption.GetInitializeBlock()) # splice in initialize op block
                
                opblock.Append([                       
                    (overlay_set_val, overlay_var, reg1),
                    (position_set_x, pos1, xgm_ov_checkbox_scalex),
                    (position_set_y, pos1, xgm_ov_checkbox_scaley),
                    (overlay_set_size, overlay_var, pos1),
                ])                       
                cur_overlay_index += 1
            
            # Combo box (TODO: split label and button)
            
            elif( aModOption.GetType() == xgm_ov_combolabel ):
                overlay_var = "$g_presentation_obj_%s" % cur_overlay_index
                opblock.Append([                       
                    (assign, overlay_var, 0), # forced initialization
                    (position_set_x, pos1, xgm_mod_options_property_value_posx + xgm_ov_combolabel_offsetx),
                    (create_combo_label_overlay, overlay_var),
                    (position_set_y, pos1, cur_posy + xgm_ov_combolabel_offsety),
                    (overlay_set_position,  overlay_var, pos1),
                    (position_set_x, pos1, xgm_ov_combolabel_scalex),
                    (position_set_y, pos1, xgm_ov_combolabel_scaley),
                    (overlay_set_size, overlay_var, pos1),
                ])
                
                for aComboItem in aModOption.GetParameters():
                    opblock.Append([
                        (overlay_add_item, overlay_var, "@%s" % aComboItem),
                    ])

                opblock.Append(aModOption.GetInitializeBlock()) # splice in initialize op block
                
                opblock.Append([                       
                    (overlay_set_val, overlay_var, reg1),
                ])                       
                cur_overlay_index += 1

            elif( aModOption.GetType() == xgm_ov_combobutton ):
                overlay_var = "$g_presentation_obj_%s" % cur_overlay_index
                opblock.Append([                       
                    (assign, overlay_var, 0), # forced initialization
                    (position_set_x, pos1, xgm_mod_options_property_value_posx + xgm_ov_combobutton_offsetx),
                    (create_combo_button_overlay, overlay_var),
                    (position_set_y, pos1, cur_posy + xgm_ov_combobutton_offsety),
                    (overlay_set_position,  overlay_var, pos1),
                    (position_set_x, pos1, xgm_ov_combobutton_scalex),
                    (position_set_y, pos1, xgm_ov_combobutton_scaley),
                    (overlay_set_size, overlay_var, pos1),
                ])
                
                params = aModOption.GetParameters()
                #params.reverse()
                for aComboItem in params:
                    opblock.Append([
                        (overlay_add_item, overlay_var, "@%s" % aComboItem),
                    ])

                opblock.Append(aModOption.GetInitializeBlock()) # splice in initialize op block
                
                opblock.Append([                       
                    (overlay_set_val, overlay_var, reg1),
                ])                       
                cur_overlay_index += 1

            ## if
            
            
            
            cur_posy -= xgm_mod_options_property_height
            #opblock.Append([
                #(assign, ":cur_posy", cur_posy),
            #])
        ## if aModOption.GetType() == xgm_ov_line:
    # for

    overlay_var = "$g_presentation_obj_%s" % cur_overlay_index
    opblock.Append([                       
        (set_container_overlay, -1),

        # This is for Done button
        (assign, overlay_var, 0), # forced initialization
        (create_game_button_overlay, overlay_var, "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, overlay_var, pos1),
    ])    
    cur_overlay_index += 1  

    
    return opblock.Unwrap()
    

##############################    
def generate_presentation_event_state_change_script(_mod_options = mod_options):
    opblock = OpBlockWrapper([]) # this will contain the main switch handling changes from overlay values
    opblock2 = OpBlockWrapper([])  # This will refresh all overlay values using the initialize blocks
    
    cur_overlay_index = 1 # start from 1 since 0 is the base option object
    
    opblock.Append([
        #(store_trigger_param_1, ":object"),
        #(store_trigger_param_2, ":value"),

        (try_begin),
            (neq, 1, 1), # dummy
    ])
    
    for x in mod_options:
        aModOption = ModOptionWrapper(x)
        if aModOption.GetType() == xgm_ov_line:
            # Create line
            pass # noop                        
        elif aModOption.GetType() in [xgm_ov_checkbox, xgm_ov_numberbox, xgm_ov_combolabel, xgm_ov_combobutton, xgm_ov_slider]:
            # Number box

            #if( aModOption.GetType() == xgm_ov_numberbox or aModOption.GetType() == xgm_ov_slider):
            if aModOption.GetType() in [xgm_ov_numberbox, xgm_ov_checkbox, xgm_ov_combolabel, xgm_ov_combobutton, xgm_ov_slider]: # redundant condition. place holder for now
                overlay_var = "$g_presentation_obj_%s" % cur_overlay_index
                opblock.Append([                       
                    (else_try),                
                        (eq, ":object", overlay_var),
                        (assign, reg1, ":value"), # placed here instead of at the top in case reg1 is unknowingly overwritten
#(display_log_message, "@g_presentation_obj_%s={reg1}" % cur_overlay_index),                        
                ])            

                opblock.Append(aModOption.GetUpdateBlock()) # splice in update block
                
                opblock2.Append(aModOption.GetInitializeBlock())                
                opblock2.Append([                       
                    (overlay_set_val, overlay_var, reg1),
                ])                       

                cur_overlay_index += 1

            # Check box (below is duplicated but retained so that it mirrors presentation load script generation to ensure similar sequencing for cur_overlay_index

            #elif( aModOption.GetType() == xgm_ov_checkbox ):
                #opblock.Append([                       
                    #(else_try),                
                        #(eq, ":object", overlay_var),
                        #(assign, reg1, ":value"), # placed here instead of at the top in case reg1 is unknowingly overwritten
##(display_log_message, "@g_presentation_obj_%s={reg1}" % cur_overlay_index),                        
                #])            
#
                #opblock.Append(aModOption.GetUpdateBlock()) # splice in update block
                #
                #cur_overlay_index += 1
            #
            ## Combo box (below is duplicated but retained so that it mirrors presentation load script generation to ensure similar sequencing for cur_overlay_index
            #
            #elif( aModOption.GetType() == xgm_ov_combolabel ):
                #opblock.Append([                       
                    #(else_try),                
                        #(eq, ":object", overlay_var),
                        #(assign, reg1, ":value"), # placed here instead of at the top in case reg1 is unknowingly overwritten
##(display_log_message, "@g_presentation_obj_%s={reg1}" % cur_overlay_index),                        
                #])            
#
                #opblock.Append(aModOption.GetUpdateBlock()) # splice in update block
                #
                #cur_overlay_index += 1
            #elif( aModOption.GetType() == xgm_ov_combobutton ):
                #opblock.Append([                       
                    #(else_try),                
                        #(eq, ":object", overlay_var),
                        #(assign, reg1, ":value"), # placed here instead of at the top in case reg1 is unknowingly overwritten
##(display_log_message, "@g_presentation_obj_%s={reg1}" % cur_overlay_index),                        
                #])            
#
                #opblock.Append(aModOption.GetUpdateBlock()) # splice in update block
                #
                #cur_overlay_index += 1
#
            ## if
        # if aModOption.GetType() == xgm_ov_line:
    # for

    # This is for Done button
    overlay_var = "$g_presentation_obj_%s" % cur_overlay_index
    opblock.Append([                       
        (else_try),
          (eq, ":object", overlay_var),
          (presentation_set_duration, 0),
        (try_end),
    ])    
    cur_overlay_index += 1  

    
    return opblock.Unwrap()+opblock2.Unwrap()

##############################

from util_scripts import *

def generate_presentations():
    try:
        find_i = list_find_first_match_i( presentations, "mod_option" )
        prsnt_mod_option = PresentationWrapper(presentations[find_i])

        codeblock = prsnt_mod_option.FindTrigger(ti_on_presentation_load).GetOpBlock()
        codeblock.Append(
            generate_presentation_load_script()
        )
        

        codeblock = prsnt_mod_option.FindTrigger(ti_on_presentation_event_state_change).GetOpBlock()
        codeblock.Append(
            generate_presentation_event_state_change_script()
        )

        #print_opblock(codeblock.Unwrap())

    except:
        import sys
        print "Injecton failed:", sys.exc_info()[1]
        raise

##############################    


generate_presentations() # call to generate stuff
    

def modmerge_presentations(orig_presentations):
       
    # add remaining presentations
    from util_common import add_objects
    num_appended, num_replaced, num_ignored = add_objects(orig_presentations, presentations)
    #print num_appended, num_replaced, num_ignored


# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "presentations"
        orig_presentations = var_set[var_name_1]
    
        
		# START do your own stuff to do merging
		
        modmerge_presentations(orig_presentations)

		# END do your own stuff
        
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
    
