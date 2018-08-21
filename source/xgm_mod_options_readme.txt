eXtended Game Mechanics : Mod Options

------------------------------------------------------------------------------
Mod Options module (1.0)
------------------------------------------------------------------------------
Allows user to expose their mod options/parameters via a generic presentation "MOD option" accessible from "Camp" menu.
The basic presentation is adapted from rubik's Custom Commander which is a toy-store of excellent features.

------------------------------------------------------------------------------
Prerequisites
------------------------------------------------------------------------------
1) Mount and Blade/Warband with module system
2) If intended to be used with modmerger, modmerger (0.2.3 and above) must be set up (instructions not here, see http://www.mbrepository.com/file.php?id=2151).
3) If manual installation, some experience with python is recommended, though a person who can follow instructions clearly may have less problems ;)  You STILL have to download modmerger from link above for some necessary utility files (but don't need to "install")
3) Patience and tolerance (This IS a WIP)

------------------------------------------------------------------------------
Installation (ModMerger version)
------------------------------------------------------------------------------
1) Requires modmerger 0.2.3 (see modmerger separately for installation)
2) place the following files in module system with modmerger

	xgm_mod_options_header				# defines constant values required by mod_options (but not by rest of module system)
	xgm_mod_options.py					# collates mod options
	xgm_mod_options_presentations.py	# generates the presentation for the mod options
	xgm_mod_options_game_menus.py		# inserts call to the mod options presentation in "camp" menu

3) Edit modmerger_options.py and add "xgm_mod_options" to the "mods_active" list.


------------------------------------------------------------------------------
Installation (Manual)
------------------------------------------------------------------------------
Note that this is not fully supported and not very recommended for most users, but included just for advanced modders.
Using manual method, you can only define mod options in xgm_mod_options.py (unlike the case with modmerger, where it will collect all {modname}_mod_options.py from active mods.)


1) Requires utility files in modmerger 0.2.3 (don't need to install, just place the util_*.py in same folder)

2) place the following files in module system folder

	xgm_mod_options_header				# defines constant values required by mod_options (but not by rest of module system)
	xgm_mod_options.py					# collates mod options
	xgm_mod_options_presentations.py	# generates the presentation for the mod options
	xgm_mod_options_game_menus.py		# inserts call to the mod options presentation in "camp" menu

3) Edit module_game_menus.py and add this to the bottom of the file:

---block start---
try:
    var_set = { "game_menus" : game_menus }
    from xgm_mod_options_game_menus import modmerge
    modmerge(var_set)
except:
    raise
---block end---

4) Edit module_presentations.py and add this to the bottom of the file:

---block start---
try:
    var_set = { "presentations" : presentations }
    from xgm_mod_options_presentations import modmerge
    modmerge(var_set)
except:
    raise
---block end---

5) Edit xgm_mod_options.py and COMMENT OUT/DELETE the following block (line ~48-86):
Note: might be a good idea to backup the file first, in case things get messed up.

---block start---
# collation of all *_mod_options.py from active mods
# import and merge related variables from all {active_mod}_mod_options.py for all active mods
try:
    from modmerger_options import options, mods_active
    from modmerger import mod_get_process_order, mod_is_active
    from util_common import add_objects
    modcomp_name = "mod_options"
    var_list = ["mod_options",]
    
    #from modmerger import modmerge
    #modmerge(var_set)

    mod_process_order = mod_get_process_order(modcomp_name)
    
    vars_to_import= ["mod_options"]
    
    for x in mod_process_order:
        if(mod_is_active(x) and x <> "xgm_mod_options"): # must exclude this file since we are using this file as base
            try:
                #mergefn_name = "modmerge_%s"%(modcomp_name)
                target_module_name = "%s_%s"%(x,modcomp_name)
                
                _temp = __import__( target_module_name , globals(), locals(), vars_to_import,-1)
                logger.info("Merging objects for component \"%s\" from mod \"%s\"..."%(modcomp_name,x))

                add_objects(mod_options, _temp.mod_options) # import from target module.

                # TODO: collect option pages

            except ImportError:
                errstring = "Failed importing for component \"%s\" for mod \"%s\"." % (modcomp_name, x)
                logger.debug(errstring)
        else:
            errstring = "Mod \"%s\" not active for Component \"%s\"." % (x, modcomp_name)
            logger.debug(errstring)

except:
    raise
---block end---


------------------------------------------------------------------------------
How to expose your mod options
------------------------------------------------------------------------------

To add an option not part of another modmerger modpack, edit "xgm_mod_options.py" and add to the list "mod_options" directly.
The structure of each tuple in the list is documented in the file, together with a sample that exposes the in-game cheat mode (replicated below for convenience)

---block start---
############################################################################
## 0) overlay id (not used atm, but can allow searches in future. just put something unique)
## 1) overlay type (defined in xgm_mod_options_header)
## 2) overlay type specific parameters (e.g. for number box, it can be lower/upper range, for cbobox, it would be the cbo items etc)
##    a) xgm_ov_numberbox : lower_bound(inclusive), upper_bound(exclusive). e.g. [0,101] for range of values from 0-100
##    b) xgm_ov_combolabel/xgm_ov_combobutton  : list of combo items. e.g. ["option1", "option2", "option3"]
##    c) xgm_ov_slider : lower_bound(inclusive), upper_bound(exclusive). e.g. [0,101] for range of values from 0-100
##    d) xgm_ov_checkbox : not used fttb. just leave empty. e.g. []
## 3) text label
## 4) reserved for text label flags
## 5) description (unused for now. may be used for stuff like tooltip in future)
## 6) reserved for description flags
## 7) initialization op block.  Used for updating the overlay values from game values. Must assign the desired value to reg1.
## 8) update op block.  Used for updating game values from overlay values. The overlay value is in reg1.
## 9) optional. reserved for option page id. unused for now. leave out for options using general page.
############################################################################
mod_options = [   
    # sample checkbox to switch the in-game cheat mode.  Comment out this if you don't want it.
    
    ( "op_cheatmode", xgm_ov_checkbox ,  [],
        "Enable cheat mode:", 0,        
        "This sets the in-game cheat mode", 0,
        [  # initialization block (set value in reg1)
            (assign, reg1, "$cheat_mode"),
        ], 
        [  # update block (value is in reg1)
            (assign, "$cheat_mode", reg1),            
        ], 
    ),
] # mod_options

---block end---

Explanations:
Think most of it is rather self explanatory, except for the initialization op block and update op block.

Basically, the initialization op block is used to set the overlay (numberbox/slider/combobox etc) values to the correct game value.  The modder can do whatever computations he requires inside the block, but must ultimately put the resultant value into reg1.  In the above example, the checkbox value is simply controlled by the global variable "$cheat_mode".  in the init block, I simply copy the value of "$cheat_mode" into reg1.

The update block is to opposite of the initialize block, as it will updates the game value with the overlay value.  At the start of the block, it can be assumed taht the corresponding value is already placed in reg1.  The modder simply make use of that value and update whatever game values he wants.  in the above example, I copy the updated value in reg1 back into "$cheat_mode" to reflect it to the rest of the game/script engine.

For adding mod options to other mods in using the modmerger framework, you should create a new file "{modname}_mod_options.py" where {modname} is the id of the mod. Edit the new file and copy and paste the following block into the file and save.

---block start---
from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
#import string

from xgm_mod_options_header import *

############################################################################
## 0) overlay id (not used atm, but can allow searches in future)
## 1) overlay type
## 2) overlay type specific parameters (e.g. for number box, it can be lower/upper range, for cbobox, it would be the cbo items etc)
##    a) xgm_ov_numberbox : lower_bound(inclusive), upper_bound(exclusive). e.g. [0,101] for range of values from 0-100
##    b) xgm_ov_combolabel/xgm_ov_combobutton  : list of combo items. e.g. ["option1", "option2", "option3"]
##    c) xgm_ov_slider : lower_bound(inclusive), upper_bound(exclusive). e.g. [0,101] for range of values from 0-100
##    d) xgm_ov_checkbox : not used fttb. just leave empty. e.g. []
## 3) text label
## 4) reserved for text label flags
## 5) description (unused for now. may be used for stuff like tooltip in future)
## 6) reserved for description flags
## 7) initialization op block.  Used for updating the overlay values from game values. Must assign the desired value to reg1.
## 8) update op block.  Used for updating game values from overlay values. The overlay value is in reg1.
## 9) reserved for option page id. unused for now. leave out for options using general page.
############################################################################

mod_options = [   
] # mod_options
---block end---

You may add to the "mod_options" using same method describe earlier.

If this mod is active (listed in "mods_active" in "modmerger_options.py"), the mod_options in "{modname}_mod_options.py" will automatically be collected if the file exists.


------------------------------------------------------------------------------
Notes
------------------------------------------------------------------------------
The manual instructions are theoretically correct but not actually tested!!! Please feedback if there are problems.
The next planned upgrade (but not sure when actual work can begin due to backlog of other stuff) will allow the mod options to be categorized into "pages", so that each page will contain a smaller number of options which are related.  pages can be set by person defining the mod_options (can be grouped by game function, or related mod name) or left out if it is to be added to general page.