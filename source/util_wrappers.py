# Experimental utility scripts to wrap game lists
# by sphere

##Additions by Caba'drin 15 Dec 2011
## Added a wrapper for GameMenuOptions and Dialogs and a function to find
## a specific dialog similar to FindTrigger (though it isn't within a class)
## and a function to find the first "i" list item whose ID contains a value

##Notes from Caba'drin testing:
# The full Animations, Meshes, Dialogs, factions, troops, items, etc can be
# wrapped with the OpBlockWrapper (since they are lists of tuples) to access
# the additional InsertBefore/After type functions for lists
# Also, animations and dialogs are lists with nested lists, not tuples and can be treated
# as such.
#
# Changing elements in "immutable" tuples is possible by directly converting the
# object to a list, setting the element, and reverting back to a tuple, like so:
# ##Change re-arm interval to 0 (using work around to edit immutable tuple)
# orig_mission_templates[mt_i][5][trigger_i] = list(orig_mission_templates[mt_i][5][trigger_i])
# orig_mission_templates[mt_i][5][trigger_i][2] = 0
# orig_mission_templates[mt_i][5][trigger_i] = tuple(orig_mission_templates[mt_i][5][trigger_i])
# using a reference (for instance trigger = orig_mission_templates[mt_i][5][trigger_i] ) and then
# trying to convert the trigger reference to/from a list/tuple will NOT work

from types import *

class BaseWrapper:
    """Base wrapper for tuples/list used in"""
    """Mount and Blade: Warband ver 1143"""

    # _data cannot have default value, must wrap something
    def __init__(self, _data): 
        self.data = _data

    def Unwrap(self):
        return self.data

    def GetLength(self):
        return len(self.data)

    def GetElement(self, i):
        return self.data[i] # no range check.

    def SetElement(self, i, value): # NOTE: Can fail if data is tuple!!!
		self.data[i] = value # no range check.
		# try:
			# self.data[i] = value # no range check.
		# except TypeError: ##handle setting item in tuple #Caba'drin addition
			# block = list(self.Unwrap())
			# block[i] = value
			# self.data = list(self.data)
			# self.data[i] = value
			# self.data = tuple(self.data)

# op block directive masks
D_SEARCH_START_MASK  	= 0x000F
D_SEARCH_METHOD_MASK 	= 0x00F0
D_SEARCH_DIR_MASK        = 0x0F00
D_INSERT_METHOD_MASK 	= 0xF000

# op block search op_block_directives
D_SEARCH_START_TOP	= 0x0001 # default. indicates that search is from top
D_SEARCH_START_BOTTOM	= 0x0002 # indicates that search is from bottom

D_SEARCH_LINENUMBER 	= 0x0010 # default. flag indicating that <position_value_1> is integer that indicates number of lines, used with FROM_TOP/FROM_BOTTOM flags
D_SEARCH_SCRIPTLINE	= 0x0020 # flag indicating that <position_value_1> is script line (tuple) that is used for matching, used with FROM_TOP/FROM_BOTTOM flags

D_SEARCH_DOWN		    = 0x0100 # indicates search upwards
D_SEARCH_UP 		    = 0x0200 # indicates search upwards


D_SEARCH_FROM_TOP		= D_SEARCH_START_TOP | D_SEARCH_DOWN
D_SEARCH_FROM_BOTTOM	= D_SEARCH_START_BOTTOM | D_SEARCH_UP

# op block modifying op_block_directives

D_INSERT_BEFORE  	= 0x1000 # default.
D_INSERT_AFTER   	= 0x2000


class OpBlockWrapper(BaseWrapper):
    """a wrapper for simple trigger tuple"""
    """Mount and Blade: Warband ver 1143"""

    def __init__(self, _data):
        if( not isinstance(_data,ListType)):
            raise ValueError("OpBlockWrapper: Wrapped must be a list.")
        BaseWrapper.__init__(self,_data)
    
    
    # class constants

    def GetSearchMethodDirective(d):
        return d & D_SEARCH_START_MASK

    def GetSearchStartDirective(d):
        return d & D_SEARCH_METHOD_MASK
    
    def GetSearchDirectionDirective(d):
        return d & D_SEARCH_DIR_MASK
    
    def GetInsertMethodDirective(d):
        return d & D_INSERT_METHOD_MASK


    # read only. Get operation tuple at line number
    def GetLineContent(self, line_no):
        if( line_no >= 0 and line_no < self.GetLength()):
            return self.GetElement(line_no)
        # raise IndexError("OpBlockWrapper:Line number out of range")
        return None

    # replace operation at line number
    def SetLineContent(self, line_no, line_content):
        if( not isinstance(line_content,TupleType)):
            raise ValueError("OpBlockWrapper: Wrapped must be a list.")
        elif( line_no >= 0 and line_no < self.GetLength()):
            #self.data[line_no] = line_content
			self.SetElement(line_no, line_content)
        else:
			raise IndexError("OpBlockWrapper: Line number out of range")

    # search the op block according to some directives
    # Return: line no if found, -1 if not found
    def FindLine(self, search_directives, search_arg_1, search_arg_2):
        #i_search = op_block_search( self.Unwrap(), search_directives, search_arg1, search_arg2 )
        d_startpos 		= (search_directives & D_SEARCH_START_MASK)
        d_searchmethod 	= (search_directives & D_SEARCH_METHOD_MASK)
        d_searchdir 	= (search_directives & D_SEARCH_DIR_MASK)
        
        i_search = -1 # default to not found    	
        op_block = self.Unwrap()

        op_block_len = len(op_block)
        #print "op block length = ", op_block_len	
       
        
        # set up default for START_TOP and SEARCHDIR_DOWN
        search_begin = -1
        search_endi = -1
        searchstep = 0
                
        if( d_startpos == D_SEARCH_START_TOP ):
            #print "search top"
            search_begin = 0
            search_endi = op_block_len - 1
        elif( d_startpos == D_SEARCH_START_BOTTOM ):
            #print "search bottom"
            search_begin = op_block_len - 1
            search_endi = 0
        
        if( d_searchdir == D_SEARCH_DOWN ):
            #print "search down"
            searchstep = 1
        elif( d_searchdir == D_SEARCH_UP ):
            #print "search up"
            searchstep = -1	
            
        #print "d_searchmethod=%s, search_begin=%d search_end=%d searchstep=%d"%(hex(d_searchmethod), search_begin, search_endi, searchstep)# DEBUG
            
        # find position
        if( d_searchmethod == D_SEARCH_LINENUMBER ):
            num_lines = search_arg_1
            if( num_lines is None ): num_lines = 0
            i_search = search_begin + searchstep * num_lines
            if( i_search < 0 or i_search >= op_block_len ) : i_search = -1
        elif( d_searchmethod == D_SEARCH_SCRIPTLINE ):				
            searchtarget = search_arg_1
            skipcount = search_arg_2

            if( skipcount is None or skipcount < 0): 
                skipcount = 0
            i_result = -1
            i_search = search_begin
            #print "i_search =", i_search, "searchtarget =", searchtarget, "skipcount =", skipcount# DEBUG
            #print "d_searchmethod=%s, search_begin=%d search_end=%d searchstep=%d"%(hex(d_searchmethod), search_begin, search_endi, searchstep)# DEBUG
            #print (i_result == -1) ,(searchstep > 0 and i_search <= search_endi) , (searchstep < 0 and i_search >= search_endi)
            #print ( ((searchstep > 0) and (i_search <= search_endi)) or ((searchstep < 0) and (i_search >= search_endi)))
            while ( (searchstep >0 and i_search <= search_endi) or (searchstep < 0 and i_search >= search_endi)):
                #print "[%d] = " %(i_search), op_block[i_search],# DEBUG
                if( op_block[i_search] == searchtarget ): # found a matching instance
                    if( skipcount == 0 ): # if 0, this is the instance we want
                        #print "match!" # DEBUG  
                        i_result = i_search
                        break
                    else:					# otherwise, 
                        skipcount -= 1
                i_search += searchstep            
            # while 
            i_search = i_result

        return i_search

    # Seach for n-th line matching a line content
    # Return: line no if found, -1 if not found
    def FindLineMatching(self, line_content, matches_to_skip=0, directives = D_SEARCH_FROM_TOP ):
        return self.FindLine( (directives & ~D_SEARCH_METHOD_MASK) | D_SEARCH_SCRIPTLINE , line_content, matches_to_skip)
        
    def FindLastLine(self):
        return self.FindLine( D_SEARCH_FROM_BOTTOM | D_SEARCH_LINENUMBER , 0, None)



    # Inserts a op block before a line number
    # Return: True if successful, False if out of range
    def InsertBefore(self, line_no, op_block):
        #print "insertbefore"
        self_code_block = self.data
        if( isinstance(op_block, OpBlockWrapper)):
            op_block=op_block.Unwrap()
            # start of op injection
        if( line_no >= 0 and line_no <= self.GetLength() ):
            i_inject_code_line = len(op_block)-1
            while( i_inject_code_line >= 0 ):
                self_code_block.insert(line_no, op_block[i_inject_code_line])
                i_inject_code_line -= 1
            return True
        return False

    # Inserts a op block after a line number
    # Return: True if successful, False if out of range
    def InsertAfter(self, line_no, op_block):
        #print "insertafter"
        return self.InsertBefore(line_no+1, op_block)


    # Inserts a op block according to directives at a line
    # Return: True if successful, False if out of range
    def Insert(self, directive, line_no, op_block):
        if(directive & D_INSERT_BEFORE):
            #print "before"
            return self.InsertBefore(line_no, op_block)
        elif(directive & D_INSERT_AFTER):
            #print "after"
            return self.InsertAfter(line_no, op_block)

        #print "none"
        return self.InsertBefore(line_no+1, op_block)

    # Appends lines from an op block to the end
    # Return: True if successful.
    def Append(self, op_block):
        return self.InsertAfter(self.FindLastLine(), op_block)

    # Removes a number of lines before a line number
    # Return: actual number of lines removed
    def RemoveBefore(self, line_no, num_lines_to_remove):
        lines_removed = 0
        self_code_block = self.Unwrap()
        try:
            while( num_lines_to_remove > 0):
                line_no -= 1
                self_code_block.pop(line_no)
                lines_removed += 1
                num_lines_to_remove -= 1
        except IndexError:
            pass
        return lines_removed
      
      
      

    # Removes a number of lines after a line number
    # Return: actual number of lines removed
    def RemoveAfter(self, line_no, num_lines_to_remove):
        lines_removed = 0
        self_code_block = self.Unwrap()
        try:
            while( num_lines_to_remove > 0):
                self_code_block.pop(line_no+1)
                lines_removed += 1
                num_lines_to_remove -= 1
        except IndexError:
            pass
        return lines_removed

    # Removes a range of line numbers
    # line_no_start : line to start removing (inclusive)
    # line_no_end   : line to stop removing (not removed)
    # Return: actual number of lines removed
    def RemoveRange(self, line_no_start, line_no_end):
        if( line_no_end < line_no_start ):
            line_no_start, line_no_end = line_no_end + 1, line_no_start + 1
        num_lines_to_remove = line_no_end - line_no_start
        return self.RemoveAfter(line_no_start, num_lines_to_remove)

    # Removes a range of line numbers starting at a pos
    # line_no_start : line to start removing (inclusive)
    # num_lines_to_remove : number of lines to remove
    # Return: actual number of lines removed
    def RemoveAt(self, line_no_start, num_lines_to_remove = 1):
        return self.RemoveAfter(line_no_start-1, num_lines_to_remove)


    # Clear all lines
    def Clear(self):
        del self.data[:]

class SimpleTriggerWrapper(BaseWrapper):
        """a wrapper for simple trigger tuple"""
        """Mount and Blade: Warband ver 1143"""
        def __init__(self, _data):
            # verify _data
            if( not isinstance(_data,TupleType)) and len(_data) == 2:
                raise ValueError("SimpleTriggerWrapper: Wrapped must be a tuple.")
            BaseWrapper.__init__(self,_data)

        def GetInterval(self):
            return self.GetElement(0)

        # cannot write due to tuple being immutable
        # def SetInterval(self, value=0):
                # self.SetElement(0, value)

        def GetOpBlock(self):
            return OpBlockWrapper(self.GetElement(1))

        # cannot write due to tuple being immutable
        # def SetCodeBlock(self, value=[]):
                # if( isinstance(value, list)):
                        # self.SetElement(1, value)
                # elif( isinstance(value, OpBlockWrapper)):
                        # self.SetElement(1, value.Unwrap())
                # else:
                        # raise TypeError("SimpleTriggerWrapper:op block expected")



class TriggerWrapper(BaseWrapper):
        """a wrapper for trigger tuple"""
        """Mount and Blade: Warband ver 1143"""
        def __init__(self, _data):
            # verify _data
            if( not isinstance(_data,TupleType)) or len(_data) < 5:
                raise ValueError("TriggerWrapper: Wrapped must be a trigger record.")
            BaseWrapper.__init__(self,_data)

        def GetCheckInterval(self):
            return self.GetElement(0)

        def GetDelayInterval(self):
            return self.GetElement(1)

        def GetRearmInterval(self):
            return self.GetElement(2)

        def GetConditionBlock(self):
            return OpBlockWrapper(self.GetElement(3))

        def GetConsequenceBlock(self):
            return OpBlockWrapper(self.GetElement(4))

class PresentationWrapper(BaseWrapper):
        """a wrapper for presentation tuple"""
        """Mount and Blade: Warband ver 1143"""
        def __init__(self, _data=("",0,0,[])):
                BaseWrapper.__init__(self,_data)

        def GetName(self):
                return self.data[0]

        # # cannot write due to tuple being immutable
        # def SetName(self, name):
                # if(isinstance(name, str)):
                        # self.data[0] = name

        def GetFlags(self):
                return self.data[1]

        # # cannot write due to tuple being immutable
        # def SetFlags(self, flags):
                # self.data[1] = flags

        def GetBackgroundMesh(self):
                return self.data[2]

        # # cannot write due to tuple being immutable
        # def SetBackgroundMesh(self, mesh):
                # self.data[2] = mesh

        def GetTriggers(self):
                # return SimpleTriggerWrapper(self.data[3])
                return self.GetElement(3)

        def GetTrigger(self, i):
                # return SimpleTriggerWrapper(self.data[3])
                return SimpleTriggerWrapper(self.GetElement(3)[i]) # no range check

        def FindTrigger(self, interval=None, codeblock=None, start=0, end=None):
                search_end = end
                if( search_end is None or search_end > self.GetLength() ):
                        search_end = self.GetLength()
                i_search = start
                while( i_search < search_end ):
                        trigger = self.GetTrigger(i_search)
                        if( (interval is None or interval == trigger.GetInterval())
                                and (codeblock is None or codeblock == trigger.GetOpBlock()) ):
                                return trigger
                        i_search += 1
                # while
                return None

        # # cannot write due to tuple being immutable
        # def SetTriggers(self, value):
                # self.SetElement(3, value)

class ScriptWrapper(BaseWrapper):
        """a wrapper for script tuple"""
        """Mount and Blade: Warband ver 1143"""
        def __init__(self, _data):
            if( not isinstance(_data,TupleType)) and len(_data) == 2:                        
                raise ValueError("ScriptWrapper: Wrapped must be a tuple.")            
            BaseWrapper.__init__(self,_data)

        def GetName(self):
            return self.GetElement(0)

        def GetOpBlock(self):
            return OpBlockWrapper(self.GetElement(1))
    
 

class ItemWrapper(BaseWrapper):
        """a wrapper for item record"""
        """Mount and Blade: Warband ver 1143"""
        def __init__(self, _data):
            if( not isinstance(_data,ListType)) and len(_data) >= 8:
                raise ValueError("ScriptWrapper: Wrapped must be a item record.")            
            BaseWrapper.__init__(self,_data)

        def GetId(self):
            return self.GetElement(0)

        def GetName(self):
            return self.GetElement(1)

        def GetMeshList(self):
            return self.GetElement(2)

        def GetItemFlags(self):
            return self.GetElement(3)

        def GetItemCapabilities(self):
            return self.GetElement(4)

        def GetItemValue(self):
            return self.GetElement(5)

        def GetItemStats(self):
            return self.GetElement(6)
            
        def GetItemModifierBits(self):
            return self.GetElement(7)
            
        ##Caba`drin
        # def GetOpBlock(self):
            # return OpBlockWrapper(self.GetElement(1))
        def GetTriggers(self):
            while self.GetLength() < 9:
                self.Unwrap().append([])
            return self.GetElement(8)    		
			
        def GetItemTrigger(self, i):
            # return SimpleTriggerWrapper(self.data[3])
            return SimpleTriggerWrapper(self.GetTriggers()[i]) # no range check
		
        def GetItemFactions(self):
            while self.GetLength() < 10:
                self.Unwrap().append([])
            return OpBlockWrapper(self.GetElement(9))
    
 

class GameMenuWrapper(BaseWrapper):
        """a wrapper for game menu record"""
        """Mount and Blade: Warband ver 1143"""
        def __init__(self, _data):
            if( not isinstance(_data,TupleType)) and len(_data) < 6:
                raise ValueError("GameMenuWrapper: Wrapped must be a game menu record.")            
            BaseWrapper.__init__(self,_data)

        def GetId(self):
            return self.GetElement(0)

        def GetMenuFlags(self):
            return self.GetElement(1)

        def GetMenuText(self):
            return self.GetElement(2)

        def GetMeshName(self):
            return self.GetElement(3)

        def GetOpBlock(self):
            return OpBlockWrapper(self.GetElement(4))

        def GetMenuOptions(self):
            return self.GetElement(5)            

        def GetMenuOption(self, menu_option_id):
            from util_common import list_find_first_match_i
            find_i = list_find_first_match_i(self.GetMenuOptions(), menu_option_id)
            if find_i <> -1:
                #return self.GetMenuOptions()[find_i]
				return GameMenuOptionWrapper(self.GetMenuOptions()[find_i]) ##Caba'drin

            return None # cannot find the option
            

class MissionTemplateWrapper(BaseWrapper):
        """a wrapper for mission template record"""
        """Mount and Blade: Warband ver 1143"""
        def __init__(self, _data):
            if( not isinstance(_data,TupleType)) and len(_data) < 6:
                raise ValueError("MissionTemplateWrapper: Wrapped must be a mission template record.")            
            BaseWrapper.__init__(self,_data)

        def GetId(self):
            return self.GetElement(0)

        def GetMissionTemplateFlags(self):
            return self.GetElement(1)

        def GetMissionType(self):
            return self.GetElement(2)

        def GetMissionDescription(self):
            return self.GetElement(3)

        def GetSpawnRecords(self):
            return self.GetElement(4)

        def GetTriggers(self):
            return self.GetElement(5)

        def GetTrigger(self, i):
            # return SimpleTriggerWrapper(self.data[3])
            return TriggerWrapper(self.GetTriggers()[i]) # no range check

        def FindTrigger(self, cinterval=None, dinterval=None, rinterval=None, conditionblock=None, consequenceblock=None, start=0, end=None):
            search_end = end
            if( search_end is None or search_end > len(self.GetTriggers()) ):   ##Caba'drin fix, GetLength() didn't work for the list
                    search_end = len(self.GetTriggers())   ##Caba'drin fix, GetLength() didn't work for the list
            i_search = start
            while( i_search < search_end ):
                    trigger = self.GetTrigger(i_search)
                    if( (cinterval is None or cinterval == trigger.GetCheckInterval())
                        and (dinterval is None or dinterval == trigger.GetDelayInterval())
                        and (rinterval is None or rinterval == trigger.GetRearmInterval())
                        and (conditionblock is None or conditionblock == trigger.GetConditionBlock().Unwrap())  ##Caba'drin fix, add Unwrap
                        and (consequenceblock is None or consequenceblock == trigger.GetConsequenceBlock().Unwrap())  ##Caba'drin fix, add Unwrap
                        ):
                            return trigger
                    i_search += 1
            # while
            return None
		##Added by Caba'drin -- allows inserting a trigger above another trigger, for instance
        def FindTrigger_i(self, cinterval=None, dinterval=None, rinterval=None, conditionblock=None, consequenceblock=None, start=0, end=None):
            search_end = end
            if( search_end is None or search_end > len(self.GetTriggers()) ): ##Caba'drin fix, GetLength() didn't work for the list
                    search_end = len(self.GetTriggers())  ##Caba'drin fix, GetLength() didn't work for the list
            i_search = start
            while( i_search < search_end ):
                    trigger = self.GetTrigger(i_search)
                    if( (cinterval is None or cinterval == trigger.GetCheckInterval())
                        and (dinterval is None or dinterval == trigger.GetDelayInterval())
                        and (rinterval is None or rinterval == trigger.GetRearmInterval())
                        and (conditionblock is None or conditionblock == trigger.GetConditionBlock().Unwrap())  ##Caba'drin fix, add Unwrap
                        and (consequenceblock is None or consequenceblock == trigger.GetConsequenceBlock().Unwrap())  ##Caba'drin fix, add Unwrap
                        ): 
                            return i_search
                    i_search += 1
            # while
            return None

			
##Added by Caba`drin -- tested and functioning
class DialogWrapper(BaseWrapper):
		"""a wrapper for dialog tuple"""
		"""Mount and Blade: Warband ver 1143"""
		def __init__(self, _data):
            # verify _data
			if( not isinstance(_data,ListType)): #or len(_data) != 6) :	cannot get the length to check out for the life of me, so poor error handling
				raise ValueError("DialogWrapper: Wrapped must be a dialog record.")
			BaseWrapper.__init__(self,_data)

		def GetPartner(self):
			return self.GetElement(0)

		def GetStartState(self):
			return self.GetElement(1)

		def GetConditionBlock(self):
			return OpBlockWrapper(self.GetElement(2))
		
		def GetText(self):
			return self.GetElement(3)

		def GetEndState(self):
			return self.GetElement(4)

		def GetConsequenceBlock(self):
			return OpBlockWrapper(self.GetElement(5))
			
		def GetVoiceOver(self):
			return self.GetElement(6)


class GameMenuOptionWrapper(BaseWrapper):
		"""a wrapper for game menu record"""
		"""Mount and Blade: Warband ver 1143"""
		def __init__(self, _data):
			if( not isinstance(_data,TupleType)) and len(_data) < 4:
				raise ValueError("GameMenuOptionWrapper: Wrapped must be a game menu option record.")            
			BaseWrapper.__init__(self,_data)
		
		def GetId(self):
			return self.GetElement(0)

		def GetConditionBlock(self):
			return OpBlockWrapper(self.GetElement(1))

		def GetText(self):
			return self.GetElement(2)

		def GetConsequenceBlock(self):
			return OpBlockWrapper(self.GetElement(3))

def FindDialog_i(objlist, partner=None, ststate=None, endstate=None, text=None, conditionblock=None, consequenceblock=None, voiceover=None, start=0, end=None):
	search_end = end
	objlist = BaseWrapper(objlist)
	if( search_end is None or search_end > objlist.GetLength() ):
		search_end = objlist.GetLength()
	i_search = start
	while( i_search < search_end ):
			dialog = DialogWrapper(objlist.data[i_search])
			if( (partner is None or partner == dialog.GetPartner())
				and (ststate is None or ststate == dialog.GetStartState())
				and (endstate is None or endstate == dialog.GetEndState())
				and (text is None or text in dialog.GetText()) ##careful, don't need to duplicate text completely
				and (conditionblock is None or conditionblock == dialog.GetConditionBlock()) 
				and (consequenceblock is None or consequenceblock == dialog.GetConsequenceBlock()) 
				and (voiceover is None or voiceover == dialog.GetVoiceOver()) 
				):
					return i_search
			i_search += 1
	# while
	return None
	
def FindDialog(objlist, partner=None, ststate=None, endstate=None, text=None, conditionblock=None, consequenceblock=None, voiceover=None, start=0, end=None):
	search_end = end
	objlist = BaseWrapper(objlist)
	if( search_end is None or search_end > objlist.GetLength() ):
		search_end = objlist.GetLength()
	i_search = start
	while( i_search < search_end ):
			dialog = DialogWrapper(objlist.data[i_search])
			if( (partner is None or partner == dialog.GetPartner())
				and (ststate is None or ststate == dialog.GetStartState())
				and (endstate is None or endstate == dialog.GetEndState())
				and (text is None or text in dialog.GetText()) ##careful, don't need to duplicate text completely
				and (conditionblock is None or conditionblock == dialog.GetConditionBlock()) 
				and (consequenceblock is None or consequenceblock == dialog.GetConsequenceBlock()) 
				and (voiceover is None or voiceover == dialog.GetVoiceOver()) 
				):
					return dialog
			i_search += 1
	# while
	return None