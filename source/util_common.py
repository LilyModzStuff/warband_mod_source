from modmerger_options import *


try:
  DEBUG_MODE
except NameError:
  DEBUG_MODE = 0

try:
	logger
except NameError:
	import logging
	logger = logging.getLogger("mnb_warband") 
	if( DEBUG_MODE == 1):	
	    logger.setLevel(logging.DEBUG)
	elif( DEBUG_MODE == -1):	
	    logger.setLevel(logging.WARN)
	elif( DEBUG_MODE == -2):	
	    logger.setLevel(logging.ERROR)
	else:
	    logger.setLevel(logging.INFO)
	h = logging.StreamHandler()
	#f = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
	f = logging.Formatter("%(levelname)s %(message)s")
	h.setFormatter(f)
	logger.addHandler(h)



# add mode constants
ADDMODE_APPEND          = 0 # adds an element to a list regardless of whether it already exists in the list
ADDMODE_REPLACE_EXIST   = 1 # replaces existing element in a list
ADDMODE_IGNORE_IF_EXIST = 2 # if element key is found in list, it will be dropped

# copied from find_object in header_common.py to make this module independent
# does a case-insensitive search over a list of tuple/list which first elements matches obj_id
def list_find_first_match_i(objlist,obj_id):
  result = -1
  num_objects = len(objlist)
  i_object = 0
  object_id_lowercase = obj_id.lower()
  while (i_object < num_objects) and (result == -1):
    object = objlist[i_object]
    if (object[0].lower() == object_id_lowercase):
      result = i_object
    i_object += 1
  return result
  

# add a list of tuple/array objects to another, with first element as key
# dst_objects : destination object list
# add_objects : list of objects to add
# add_mode  : see add mode constants above
# Return : num_appended, num_replaced, num_ignored which are the number of objects being appended, replaced and ignored respectively
def add_objects(dst_objects, add_objects, add_mode = ADDMODE_REPLACE_EXIST):
  num_appended=0
  num_replaced=0
  num_ignored=0
  if(add_mode == ADDMODE_APPEND):
    dst_objects.extend(add_objects) # Use this only if there are no replacements (i.e. no duplicated item names)
    num_appended = len(add_objects)
  else:
    # Use the following loop to replace existing entries with same id
    for i in range (0,len(add_objects)):
      find_index = list_find_first_match_i(dst_objects, add_objects[i][0]);
      if( find_index == -1 ):
        dst_objects.append(add_objects[i])
        num_appended+=1
      elif(add_mode == ADDMODE_REPLACE_EXIST):
        dst_objects[find_index] = add_objects[i]
        num_replaced=0
    else:
      num_ignored=0  
  return num_appended, num_replaced, num_ignored


  



# move this to util_strings later
# removes vowels from a string
# Note: often used in place to "shorten" certain well known strings
def devowel(word, table=''.join(chr(i) for i in range(256)), vowels="aeiou"):
 return word.translate(table, vowels)
 
 
# inverts a dictionary with value as list of keys of original dictionary 
def inverted_list_dict(d):
    inv = {}
    for k, v in d.iteritems():
        keys = inv.setdefault(v, [])
        keys.append(k)
    return inv

# inverts a dictionary with value as a key of original dictionary 
# assumes 1-1 mapping between keys and values
def inverted_dict(d):
    return dict([v,k] for k,v in d.iteritems())

	
	
	

##Caba'drin Addition
def list_find_first_containing_i(objlist,obj_id):
  result = -1
  num_objects = len(objlist)
  i_object = 0
  object_id_lowercase = obj_id.lower()
  while (i_object < num_objects) and (result == -1):
    object = objlist[i_object]
    if (object_id_lowercase in object[0].lower()):
      result = i_object
    i_object += 1
  return result