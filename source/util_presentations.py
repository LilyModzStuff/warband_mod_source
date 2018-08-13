# Experimental utility scripts for presentations
# by sphere

from util_common import *


def find_presentation(_presentations, presentation_id):
    return list_find_first_match_i(_presentations, presentation_id);

def add_presentations(orig_presentations, add_presentations, check_duplicates = False):
  if( not check_duplicates ):
    orig_presentations.extend(add_presentations) # Use this only if there are no replacements (i.e. no duplicated item names)
  else:
    # Use the following loop to replace existing entries with same id
    for i in range (0,len(add_presentations)-1):
      find_index = find_presentation(orig_presentations, add_presentations[i][0]); # find_object is from header_common.py
      if( find_index == -1 ):
        orig_presentations.append(add_presentations[i])
      else:
        orig_presentations[find_index] = add_presentations[i]