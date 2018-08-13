## Prebattle Orders & Deployment by Caba'drin
## v0.91
## 14 Dec 2011

from module_animations import *

animations=[
##Spear Bracing by Caba, animations by Papa Larazou
 ["spearwall_bracing", acf_thrust|acf_enforce_all|acf_align_with_ground, amf_priority_kick|amf_keep, #acf_rot_vertical_sword acf_thrust|acf_enforce_all|acf_align_with_ground |acf_lock_camera, amf_keep |amf_client_prediction amf_priority_kick amf_rider_rot_defend |amf_rider_rot_couched_lance
   [2.5, "pike_brace", 0, 190, arf_blend_in_1], #blend_in_ready
 ],
 ["spearwall_bracing_low", acf_thrust|acf_enforce_all|acf_align_with_ground, amf_priority_kick|amf_keep, #acf_thrust|acf_enforce_all|acf_align_with_ground |acf_lock_camera, amf_keep |amf_client_prediction amf_priority_kick
   [3.0, "pike_brace", 329, 535, arf_blend_in_1], #blend_in_ready
 ], 
 ["spearwall_bracing_recover", acf_enforce_all|acf_align_with_ground, amf_play|amf_priority_die, #acf_thrust|acf_enforce_all|acf_align_with_ground |acf_lock_camera, amf_keep |amf_client_prediction amf_priority_kick
   [1.5, "pike_brace", 191, 329, blend_in_ready], #blend_in_ready  |amf_start_instantly
 ],
 ["spearwall_bracing_recoil", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_kick|amf_use_weapon_speed|amf_play, #acf_thrust|acf_enforce_all|acf_align_with_ground |acf_lock_camera, amf_keep |amf_client_prediction amf_priority_kick
  [attack_parried_duration_thrust, "anim_human", combat+7316, combat+7313, arf_blend_in_2], 
 ],
##
 ##Shield Bash by Xeno, animation by Papa Larazou
 ["shield_bash", acf_enforce_all, amf_play|amf_priority_striked|amf_use_defend_speed|amf_client_owner_prediction,
  [0.75, "shield_bash", 0, 30, blend_in_defense],
   [0.75, "defend_shield_parry_all", 1, 50, blend_in_defense], #Adjust duration for balance.  Currently at 0.75 seconds, fixed.
   [0.75, "defend_shield_right", 1, 50, blend_in_defense],
   [0.75, "defend_shield_left", 1, 50, blend_in_defense],
   [0.75, "defend_shield_right", 1, 50, blend_in_defense],   
 ],
 ["shield_strike", acf_enforce_all|acf_align_with_ground, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
	[2, "anim_human", blow+5000, blow+5010, arf_blend_in_3|arf_make_custom_sound],  
	[2.5, "anim_human", blow+5400, blow+5453, arf_blend_in_2|arf_make_custom_sound], 
	[2.5, "anim_human", blow+5400, blow+5445, arf_blend_in_2|arf_make_custom_sound],   
   ],
##
 ]
 
from util_animations import *

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "animations"
        orig_animations = var_set[var_name_1]
        modmerge_animations(orig_animations)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
		
def modmerge_animations(orig_animations):
    try:
        add_animations(orig_animations, animations) 		
    except:
        import sys
        print "Injecton 1 failed:", sys.exc_info()[1]
        raise