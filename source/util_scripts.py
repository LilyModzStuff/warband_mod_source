# Experimental utility scripts for scripts
# by sphere

#from header_common import *

# structure of script_directive:
# array with the following elements

#script directive code
SD_NONE     = 0x0000 # do nothing. dummy
SD_REMOVE   = 0x0001 # SD_REMOVE, <script_name> : removes script <scipt_name> (excludes "script_" prefix)
SD_RENAME   = 0x0002 # SD_RENAME, <script_name> <new_script_name> : renames script <scipt_name> to <new_script_name> (excludes "script_" prefix)
SD_ADD      = 0x0004 # SD_ADD, <script_name>, <op_block>, [<check_duplicate:True|False>].  Adds a new script.  If optional <check_duplicate> is True, will replace existing scripts, otherwise will append to end
SD_REPLACE_OPBLOCK  = 0x0008 # SD_REPLACE_OPBLOCK, <script_name>, <op_block> : replaces scripts's op block
SD_OP_BLOCK_INSERT  = 0x0010 # SD_OP_BLOCK_INSERT, <script_name>, <position_flags>, <position_value_1>, <position_value_2>, <op_block> : Inserts a op block according to position flag and value
SD_OP_BLOCK_REMOVE  = 0x0020 # <script_name>, <position_flags>, <position_value_1>, <position_value_2>, <lines_to_remove>(default 1)
SD_OP_BLOCK_REPLACE = 0x0040 # SD_OP_BLOCK_INSERT, <script_name>, <position_flags>, <position_value_1>, <position_value_2>, <op_block>,  <lines_to_remove>(default 1) : Inserts a op block according to position flag and value

THIS_OR_NEXT  = 0x1000 # or modifier indicates that if the directive is successful, will skip the next line(s) (until a line without THIS_OR_NEXT)

from header_operations import *
from util_common import *
#from util_op_block import *

# Replaces/Renames scripts based on script directive list
# orig_scripts : scripts (list) from module_scripts.py
# directives : list of script_directive
def process_script_directives( orig_scripts, directives ):
    import warnings
    from util_wrappers import OpBlockWrapper
    
    directives_end = len(directives)
	
    i_directives = 0
    skip = False
    while( i_directives < directives_end ):
      cur_directive = directives[i_directives]
      directive_code = cur_directive[0]
    
      # check if skipping
      if( skip ):
            if( directive_code & THIS_OR_NEXT ):  # if this directive also have THIS_OR_NEXT, continue skipping
              skip = True
            else:
              skip = False
      else: 
            skip = False
            # handle unconditional directives first
            if( directive_code & SD_ADD ): # adds script
              check_duplicate = False # default to not check duplicate
              if( len(cur_directive) >= 4 ): # if check_duplicate is specified, use it instead
                    check_duplicate = cur_durective[3]
              add_scripts(orig_scripts, [ (cur_directive[1], cur_directive[2]) ], check_duplicate)
              if( directive_code & THIS_OR_NEXT ): skip = True
            
            # handle search-base directives
            find_i = list_find_first_match_i(orig_scripts, cur_directive[1])
            if( find_i > -1 ):
              if( directive_code & THIS_OR_NEXT ): skip = True
              cur_script = orig_scripts[find_i]
              directive_code = cur_directive[0]
              

              if( directive_code & SD_REMOVE ):
                    orig_scripts.pop(find_i) # removes script
              elif( directive_code & SD_RENAME ):
                    # cur_script[0] = cur_directive[2] # renames script
					# tuples are immutable, so have to replace with a new tuple
					orig_scripts[find_i] = (cur_directive[2], cur_script[1])
              elif( directive_code & SD_REPLACE_OPBLOCK ):
                    # cur_script[1] = cur_directive[2] # replace op block
					# tuples are immutable, so have to replace with a new tuple
					orig_scripts[find_i] = (cur_script[0], cur_directive[2] )
              elif( directive_code & SD_OP_BLOCK_INSERT ):
                    search_directives = cur_directive[2]
                    op_block = OpBlockWrapper(orig_scripts[find_i][1])
                    #print "size=", len(op_block.Unwrap())
                    line_no = op_block.FindLine(search_directives, cur_directive[3], cur_directive[4])
                    #print "FindLine=",line_no
                    result = op_block.Insert( search_directives, line_no, cur_directive[5])                    
                    #result = op_block_inject(orig_scripts[find_i][1], cur_directive[2], cur_directive[3], cur_directive[4], cur_directive[5])
                    # print orig_scripts[find_i] # DEBUG
                    if( not result ):
                      warnings.warn("Error injecting code into: %s" % (cur_directive[1]) )
              elif( directive_code & SD_OP_BLOCK_REMOVE ):
                    search_directives = cur_directive[2]
                    op_block = OpBlockWrapper(orig_scripts[find_i][1])
                    line_no = op_block.FindLine(search_directives, cur_directive[3], cur_directive[4])
                    try:
                        lines_to_remove = cur_directive[5]
                    except IndexError:
                        lines_to_remove = 1
                    result = op_block.RemoveAt(line_no,lines_to_remove)
                    if( not result ):
                      warnings.warn("Error removing code from: %s" % (cur_directive[1]) )

              elif( directive_code & SD_OP_BLOCK_REPLACE ):
                    search_directives = cur_directive[2]
                    op_block = OpBlockWrapper(orig_scripts[find_i][1])
                    line_no = op_block.FindLine(search_directives, cur_directive[3], cur_directive[4])
                    try:
                        lines_to_remove = cur_directive[6]
                    except IndexError:
                        lines_to_remove = 1
                    result1 = op_block.RemoveAt(line_no,lines_to_remove)                    
                    if(result1): result2 = op_block.InsertBefore(line_no, cur_directive[5])
                    if( not result1 or not result2 ):
                      warnings.warn("Error replacing code from: %s" % (cur_directive[1]) )
                                       
              else: # unhandled directive code
                    print "process_script_directives: unhandled directive code: ", directive_code
                    warnings.warn("Unhandled script directive code: %d" % (directive_code) )
            else: # directive failed
              print "process_script_directives: Script not found: ", cur_directive[1]
              warnings.warn( "Script not found: %s" % (cur_directive[1]) )
      i_directives += 1
# end of process_script_directives

# Adds scripts from one list to another
# orig_scripts : scripts (list) from module_scripts.py, destination to be added
# add_scripts : list of scripts to add
# check_duplicates : if True, will do a detail search, and replaces those with same name.  if False, will just add to end of scripts list
def add_scripts(orig_scripts, add_scripts, check_duplicates = True):
    addmode = ADDMODE_REPLACE_EXIST
    if  not check_duplicates:
        addmode = ADDMODE_APPEND
	
    return add_objects(orig_scripts, add_scripts, addmode)
    
    
  #if( not check_duplicates ):
    #orig_scripts.extend(add_scripts) # Use this only if there are no replacements (i.e. no duplicated item names)
  #else:
    ## Use the following loop to replace existing entries with same id
    #for i in range (0,len(add_scripts)):
      #find_index = list_find_first_match_i(orig_scripts, add_scripts[i][0]); # list_find_first_match_i is from header_common.py
      #if( find_index == -1 ):
        #orig_scripts.append(add_scripts[i])
      #else:
        #orig_scripts[find_index] = add_scripts[i]
#
#


# search for a script by id and print the op block (raw)
def print_script(_scripts, script_id):
    find_i = list_find_first_match_i(_scripts, script_id)
    #cur_indent=0
    #next_indent=0
    try:
        target = _scripts[find_i]
        print ">>> start of script", script_id
        #for x in target[1]:
            #cur_indent = next_indent
            #if x == (try_begin):
                #next_indent = cur_indent + 1
            #elif x == (else_try):
                #cur_indent -= 1
                #next_indent = cur_indent + 1
            #elif x == (try_end):
                #cur_indent -= 1
                #next_indent = cur_indent
            #else:
                #next_indent = cur_indent
#
            #for i in range(cur_indent): print "  ",
            #print x
            
        print_opblock(target[1])
        print "<<< end of script", script_id

    except IndexError:
        print "script \"%s\" not found." % script_id
        
        
        

def print_opblock(opblock):
    cur_indent=0
    next_indent=0
    
       
    for x in opblock:
        cur_indent = next_indent
        if x == (try_begin):
            next_indent = cur_indent + 1
        elif x == (else_try):
            cur_indent -= 1
            next_indent = cur_indent + 1
        elif x == (try_end):
            cur_indent -= 1
            next_indent = cur_indent
        else:
            next_indent = cur_indent

        for i in range(cur_indent): print "  ",
        print x




### test
#test_scripts = [
#("test1",[
    #(100),(101),(102),(103),(104),(105),(106),(107),(108),(109),110,
    #]),
#]
#
#from util_wrappers import *
#
#test_script_directives=[
 #[SD_OP_BLOCK_REPLACE, "test1", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE, (105),0,[(201),(202),(203)],2]
#]
#
#print "old block"
#print_opblock(test_scripts[0][1])
#
#process_script_directives(test_scripts, test_script_directives)
##opblock = OpBlockWrapper(test_scripts[0][1])
##opblock.RemoveAt(5,1)
##
#print "new block"
#print_opblock(test_scripts[0][1])

