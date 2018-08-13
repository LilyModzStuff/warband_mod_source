from module_constants import *
from header_items import  *

from module_items import items

ID = 0
NAME = 1
MESHES = 2
FLAGS = 3
CAPABILITIES = 4
VALUE = 5
STATS = 6
MODBITS = 7
TRIGGERS = 8
FACTIONS = 9

def get_item_type(item):
	return item[FLAGS] & 0xff

def item_has_flag(item, flag):
	return (item[FLAGS] & flag) == flag

def item_has_secondary_mode(item):
	return item_has_flag(item, itp_next_item_as_melee) and itp_type_one_handed_wpn <= get_item_type(item) <= itp_type_thrown

## IT'S FROM THE BELOW LIST THAT THE ITEM ARRAYS PROVIDING EQUIPMENT OPTIONS ARE COMPILED
ordered_items = {}
ordered_item_ids = {}
for item_type in cstm_item_type_strings:
	ordered_items[item_type] = [item for item in items[1:] if get_item_type(item) == item_type and item[VALUE] > 0 and not item_has_secondary_mode(items[items.index(item) - 1]) and item_has_flag(item, itp_merchandise)]
	ordered_items[item_type].sort(key=lambda x: x[VALUE], reverse=True)
	
	ordered_item_ids[item_type] = [items.index(item) for item in ordered_items[item_type]]
	#print ["(%s: %d)" % (item[ID], item[VALUE]) for item in ordered_items[item_type]]