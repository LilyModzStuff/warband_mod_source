# Experimental utility scripts for animations
# by Caba'drin

from util_common import *

def find_animation(objlist, animation_id):
    return list_find_first_match_i(objlist, animation_id);

def add_anim(objlist, animation, dummy_anim):
	to_replace = list_find_first_containing_i(objlist, dummy_anim)
	objlist[to_replace] = animation

def add_animations(orig_animations, add_animations, horse = False, check_duplicates = False):
  if( not horse ):
    dummy_anim = "unused_human_anim_"
  else:
    dummy_anim = "unused_horse_anim_"
  if( not check_duplicates ):
	for i in range(len(add_animations)):
		add_anim(orig_animations, add_animations[i], dummy_anim) # Use this only if there are no replacements (i.e. no duplicated item names)
  else:
    # Use the following loop to replace existing entries with same id
    for i in range(len(add_animations)):
      find_index = find_animation(orig_animations, add_animations[i][0]); # find_object is from header_common.py
      if( find_index == -1 ):
        add_anim(orig_animations, add_animations[i], dummy_anim)
      else:
        orig_animations[find_index] = add_animations[i]