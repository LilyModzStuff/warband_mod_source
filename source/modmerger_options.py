# master options for modmerger framework
# by sphere

# -2 : print error only
# -1 : print errors and warnings
# 0 : print errors, warnings and info
# 1 : print all
DEBUG_MODE = -1

# fill this in yourself with the module system you are using, so that some mods can make smarter decisions on how to merge with your source.
module_sys_info = {
        "version": 1158,      # version number * 1000
}

options={

    "process_scripts_show_script_name": 0,     # for debugging. checked by modified process_scripts.py to show name of script being processed    
}

# List of active mod code names.
# This is also the default order during bulk processing
# The specific mod source files must be in the format "{modname}_????.py".  
# for example, the mod content corresponding to "items", for mod "fc" should be in the file "fc_items.py"

mods_active = [
	"cstm",
	"cstmmerge",
	"colour",
        "trees",
        "gpu",
        "array",
        "tournament",
        "freelancer",
        "mcc",
]


# Alternate process order for certain modules components
# Only need to be defined if order/combination is different from mods_active
# Each element in is is a tuple with the following elements
#
# 1) mod component name (less the "module_" prefix), e.g. for "module_items", it will be "items"
# 2) list of mod names in the order to be processed.  The mod names should be 
#      the ones used in mods_active, and will only be processed if they are in
#      mods_active.
#

mods_process_order=[
#    ("{component_name}", [{list of mod names}]),

]


# check and fill in defaults for certain required variables
try:
    module_sys_info["version"]
except KeyError:
    # assume version to be latest version that modmerger was tested on
    module_sys_info["version"] = 1143
