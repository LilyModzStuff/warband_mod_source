# modmerger framework
# by sphere

# New method of installation: execute modmerger_installer.py


## The following snippet is to be inserted at the bottom of module_constants.py. (uncommment the copy of the block)
## This is the snippet that imports all symbols for the *_constants files for active mods.


## modmerger_start version=100
#try:
#    from util_common import logger
#    from modmerger_options import mods_active
#    modcomp_name = "constants"
#    for mod_name in mods_active:
#        try:
#            logger.info("Importing constants from mod \"%s\"..."%(mod_name))
#            code = "from %s_constants import *" % mod_name
#            exec code
#        except ImportError:
#            errstring = "Component \"%s\" not found for mod \"%s\"." % (modcomp_name, mod_name)
#            logger.debug(errstring)
#except:
#    raise
##modmerger_end
	
 
## The following snippet to be inserted at the bottom of other module_*.py (except module_info.py). (uncommment the copy of the block)

## modmerger_start version=100
#try:
#    import inspect, os.path, re,sys
#    module_name = os.path.basename(inspect.stack()[0][1])
#    result = re.match("^(module_([^.]*)).py", module_name)
#    if( result ):    
#        from modmerger import modmerge
#        modmerge(eval(result.group(2)))
#except:
#    raise
## modmerger_end





from modmerger_options import *
from util_common import *

# make sure the following are define (should be in options.py)
try:
    mods_active
except NameError:
    mods_active = []
    
try:
    mods_process_order
except NameError:
    mods_process_order = []
    
from modmerger_header import *




# Return if a mod is active.
def mod_is_active(modname):
    try:
        mods_active.index(modname)
        return True
    except ValueError, IndexError:
        return False
        

# modcomp_name : name of module component less the "module_" prefix, e.g. for "module_items", it will be "items"   
#   must be one of the values in mod_components
def mod_get_process_order(modcomp_name):
    from util_common import list_find_first_match_i

    find_i = list_find_first_match_i(mods_process_order, modcomp_name)
    if(find_i > -1):
        return mods_process_order[find_i][1]

    return mods_active
    
	
# generic function that calls the "modmerge_{component_name}" function in each of the mod python files.
def modmerge_( modcomp_name, orig_objects ):
    mod_process_order = mod_get_process_order(modcomp_name)
    
    for x in mod_process_order:
        if(mod_is_active(x)):
            try:
                mergefn_name = "modmerge_%s"%(modcomp_name)
                _temp = __import__( "%s_%s"%(x,modcomp_name) , globals(), locals(), [mergefn_name],-1)
                logger.info("Merging objects \"%s\" from mod \"%s\"..."%(modcomp_name,x))
                _temp.__dict__[mergefn_name](orig_objects)
            except ImportError:
                errstring = "Component \"%s\" not found for mod \"%s\"." % (modcomp_name, x)
                logger.debug(errstring)
        else:
            errstring = "Mod \"%s\" not active for Component \"%s\"." % (x, modcomp_name)
            logger.debug(errstring)
         


	
# default merging function for items if modmerge or modmerge_items not found in target {mod}_items.py
# Items need special processing due to need to preserve the dummy item marking the end
# mod_name : code name of the target mod
# var_dict : variable dictionary from the original module_{component}.py
# return true if successful. False otherwise
def modmerge_items(mod_name, var_dict):
    # manually import required variables from {mod}_items.py
    var_name = "items"    
    modcomp_name = var_name
    src_module_name = "%s_%s"%(mod_name,modcomp_name)
    vars_to_import= [var_name]
    try:
        orig_items = var_dict[var_name]
    except KeyError:
        errstring = "Expected variable \"%s\" not found in module \"%s\" for mod \"%s\"." % (var_name, src_module_name, mod_name)
        raise KeyError(errstring)    
    try:
        _temp = __import__( src_module_name , globals(), locals(), vars_to_import,-1)
        item_end = orig_items.pop() # temporary remove item_end
        num_appended, num_replaced, num_ignored = add_objects(orig_items, _temp.items)
        orig_items.append(item_end) # push back item_end
        logger.info("Merged \"items\" from %s: appended=%d, replaced=%d, ignored=%d" % (src_module_name, num_appended, num_replaced, num_ignored))
        return True
    except ImportError:
        errstring = "Failed importing for component \"%s\" for mod \"%s\"." % (modcomp_name, mod_name)
        logger.debug(errstring)
    
    return False        
        
 


# default merging function for items if modmerge not found in target {mod}_{component}.py
# This version is for those components with only 1 major variable same as the component name and the data should be a list of tuples/list where first element is id
# mod_name : code name of the target mod
# var_dict : variable dictionary from the original module_{component}.py
# return true if successful. False otherwise
def modmerge_generic(mod_name, var_dict, modcomp_name, src_module_name, var_name):
    # manually import required variables from {mod}_items.py
    
    #modcomp_name = "items"
    src_module_name = "%s_%s"%(mod_name,modcomp_name)
    vars_to_import= [var_name]
    try:
        orig_objects = var_dict[var_name]
    except KeyError:
        errstring = "Expected variable \"%s\" not found in module \"%s\" for mod \"%s\"." % (var_name, src_module_name, mod_name)
        raise KeyError(errstring)
    
    try:
        _temp = __import__( src_module_name , globals(), locals(), vars_to_import,-1)
        num_appended, num_replaced, num_ignored = add_objects(orig_objects, _temp.__dict__[var_name])
        logger.info("Merged \"%s\" from %s: appended=%d, replaced=%d, ignored=%d" % (var_name, src_module_name, num_appended, num_replaced, num_ignored))
        return True
    except ImportError:
        errstring = "Failed importing for component \"%s\" for mod \"%s\"." % (modcomp_name, mod_name)
        logger.debug(errstring)
    
    return False       



# 2nd default merging function for items if modmerge not found in target {mod}_{component}.py
# This version is for those components with only 1 major variable same as the component name and the data should be just be appended (usually no simple, e.g. simple_triggers)
# mod_name : code name of the target mod
# var_dict : variable dictionary from the original module_{component}.py
# return true if successful. False otherwise
def modmerge_generic2(mod_name, var_dict, modcomp_name, src_module_name, var_name):
    # manually import required variables from {mod}_items.py
    
    #modcomp_name = "items"
    src_module_name = "%s_%s"%(mod_name,modcomp_name)
    vars_to_import= [var_name]
    try:
        orig_objects = var_dict[var_name]
    except KeyError:
        errstring = "Expected variable \"%s\" not found in module \"%s\" for mod \"%s\"." % (var_name, src_module_name, mod_name)
        raise KeyError(errstring)
    
    try:
        _temp = __import__( src_module_name , globals(), locals(), vars_to_import,-1)
        num_appended, num_replaced, num_ignored = add_objects(orig_objects, _temp.__dict__[var_name], ADDMODE_APPEND)
        logger.info("Merged \"%s\" from %s: appended=%d, replaced=%d, ignored=%d" % (var_name, src_module_name, num_appended, num_replaced, num_ignored))
        return True
    except ImportError:
        errstring = "Failed importing for component \"%s\" for mod \"%s\"." % (modcomp_name, mod_name)
        logger.debug(errstring)
    
    return False      

# Generic merge function that tries to detect the component name currently merging from calling module
# Must be called from one of the "module_*.py" files where applicable
def modmerge_100(orig_objects):
	## verify modulename
    import inspect, os.path, re
    callermodule = os.path.basename(inspect.stack()[1][1])
    result = re.match("^(module_([^.]*)).py", callermodule)
    if(result):
        callermodule = result.group(1)
        modcomp_name = result.group(2)
        logger.info("Detected: module = \"%s\", component name = \"%s\""%(callermodule,modcomp_name))
        try:
            mod_components.index(modcomp_name)
            modmerge_(modcomp_name,orig_objects)
        except KeyError:
            raise ValueError("Component \"%s\" not recognized."%(modcomp_name))
    else:
        errstring = "Must be called from a module_*.py"
        logger.error(errstring)
        raise ValueError(errstring)            
        

# version 200/201 functions
# Generic function that calls the "modmerge(variable_set)}" function in each of the mod python files.
# If the modmerge() function is not found in target module, it will try to merge target components using the most common settings.
def modmerge__( modcomp_name, var_dict ):
    mod_process_order = mod_get_process_order(modcomp_name)
    
    for x in mod_process_order:
        if(mod_is_active(x)):
            done = False

            mod_name = x
            src_module_name = "%s_%s"%(x,modcomp_name)
            #print "src_module_name=",src_module_name ## debug
            
            # 1) try to get localized modmerge() from target module
            try:
                mergefn_name = "modmerge"
                _temp = __import__( src_module_name ,{} , {}, [mergefn_name],-1)
                logger.info("Merging objects \"%s\" from mod \"%s\"..."%(modcomp_name,x))
                _temp.__dict__[mergefn_name](var_dict)
                done = True
            except ImportError:
                errstring = "Module \"%s\" not found for mod \"%s\"." % (src_module_name, mod_name)
                logger.debug(errstring)
            except KeyError:
                errstring = "\"%s\" not found in \"%s\" not found for mod \"%s\"." % (mergefn_name, src_module_name, mod_name)
                logger.debug(errstring)
                
            # 2) if modmerge() not found, try general method (which just append/replace main array)
            if not done:
                # start of specialized switch case
                component_type = get_component_type(modcomp_name)
                
                if modcomp_name == "items": # item is special case for type 2
                    done = modmerge_items(mod_name, var_dict)
                elif modcomp_name == "factions": # put factions here although is of type 4, but left out "default_kingdom_relations"
                    done = modmerge_generic(mod_name, var_dict, modcomp_name, src_module_name, modcomp_name)            
                #elif modcomp_name == "scripts": # put factions here although is of type 4, but left out "default_kingdom_relations"
                    #pass #TODO
                elif (modcomp_name in ["dialogs", "triggers", "simple_triggers"]):
                    done = modmerge_generic2(mod_name, var_dict, modcomp_name, src_module_name, modcomp_name)                            
                elif component_type & 2 : 
                    done = modmerge_generic(mod_name, var_dict, modcomp_name, src_module_name, modcomp_name)            
        else:
            errstring = "Mod \"%s\" not active for Component \"%s\"." % (x, modcomp_name)
            logger.debug(errstring)

# Generic merge function that tries to detect the component name currently merging from calling module
# Must be called from one of the "module_*.py" files where applicable
def modmerge(var_dict, modcomp_name=None):
    from modmerger_header import mod_components
    ## verify modulename
    if  modcomp_name is None:
        import inspect, os.path, re
        callermodule = os.path.basename(inspect.stack()[1][1])
        result = re.match("^(module_([^.]*)).py", callermodule)
        if(result):
            callermodule = result.group(1)
            modcomp_name = result.group(2)
            logger.info("Detected: module = \"%s\", component name = \"%s\""%(callermodule,modcomp_name))    
            #try:
                #mod_components.index(modcomp_name)
            #except KeyError:
                #raise ValueError("Component \"%s\" not recognized."%(modcomp_name))
        else:
            errstring = "Must be called from a module_*.py, called from module: %s" % callermodule
            logger.error(errstring)
            raise ValueError(errstring)          
    else:
        try:
            mod_components.index(modcomp_name)
        except KeyError:
            raise ValueError("Component \"%s\" not recognized."%(modcomp_name))
    
    if not modcomp_name is None:
        try:	 
            mod_components.index(modcomp_name)
            modmerge__(modcomp_name,var_dict)
        except KeyError:
            raise ValueError("Component \"%s\" not recognized."%(modcomp_name))
    else:
        raise ValueError("Component not specified and cannot be detected.")

               

        