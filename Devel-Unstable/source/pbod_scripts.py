## Prebattle Orders & Deployment by Caba'drin
## v0.92
## 20 Jan 2012

from header_common import *
from header_operations import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from ID_animations import *
from module_constants import *


#-- Dunde's Key Config BEGIN
# Slots Initilizations (Key Defs & Default Values) 
def set_key_config():
   key_config = []
   for i in xrange(len(keys_list)):
      key_config.append((troop_set_slot, key_config_data, slot_default_keys_begin+i, keys_list[i][1]))      
   for i in xrange(len(all_keys_list)):
      key_config.append((troop_set_slot, key_config_data, slot_key_defs_begin+i, all_keys_list[i]))
   return key_config[:]   

# Global Variables -> Slots   
def read_key_config():
   global_key = []
   for i in xrange(len(keys_list)):
      global_key.append((troop_set_slot, key_config_data, slot_keys_begin+i, keys_list[i][0]))      
   return global_key[:]   
   
# Slots -> Global Variables   
def write_key_config():
   global_key = []
   for i in xrange(len(keys_list)):
      global_key.append((troop_get_slot, keys_list[i][0], key_config_data, slot_keys_begin+i))      
   return global_key[:]      
#-- Dunde's Key Config END


from module_items import items 
def set_item_score():
  item_score = []
  for i_item in xrange(len(items)):
    # ## weight
    # item_score.append((item_set_slot, i_item, slot_item_weight, get_hrd_weight(items[i_item][6])))
    
    # ## difficulty
    # item_score.append((item_set_slot, i_item, slot_item_difficulty, get_difficulty(items[i_item][6])))
    
    # ## two hand/one hand
    # type = items[i_item][3] & 0x000000ff
    # if type == itp_type_two_handed_wpn and items[i_item][3] & itp_two_handed == 0:
      # item_score.append((item_set_slot, i_item, slot_item_two_hand_one_hand, 1))
    
    type = items[i_item][3] & 0x000000ff
    if type == itp_type_shield:
      item_score.append((item_set_slot, i_item, slot_item_length, get_weapon_length(items[i_item][6])))
      item_score.append((item_set_slot, i_item, slot_item_body_armor, get_body_armor(items[i_item][6])))
      item_score.append((item_set_slot, i_item, slot_item_speed, get_speed_rating(items[i_item][6])))
    elif type == itp_type_bow or type == itp_type_crossbow:
      item_score.append((item_set_slot, i_item, slot_item_thrust_damage, get_thrust_damage(items[i_item][6])))
      item_score.append((item_set_slot, i_item, slot_item_swing_damage, get_swing_damage(items[i_item][6])))
      item_score.append((item_set_slot, i_item, slot_item_speed, get_speed_rating(items[i_item][6])))
    elif type >= itp_type_one_handed_wpn and type <= itp_type_thrown:
      item_score.append((item_set_slot, i_item, slot_item_thrust_damage, get_thrust_damage(items[i_item][6])&0xff))
      item_score.append((item_set_slot, i_item, slot_item_swing_damage, get_swing_damage(items[i_item][6])&0xff))
      item_score.append((item_set_slot, i_item, slot_item_speed, get_speed_rating(items[i_item][6])))
      item_score.append((item_set_slot, i_item, slot_item_length, get_weapon_length(items[i_item][6])))
    elif type >= itp_type_head_armor and type <= itp_type_hand_armor:
      item_score.append((item_set_slot, i_item, slot_item_head_armor, get_head_armor(items[i_item][6])))
      item_score.append((item_set_slot, i_item, slot_item_body_armor, get_body_armor(items[i_item][6])))
      item_score.append((item_set_slot, i_item, slot_item_leg_armor, get_leg_armor(items[i_item][6])))
    elif type == itp_type_horse:
      item_score.append((item_set_slot, i_item, slot_item_horse_speed, get_missile_speed(items[i_item][6])))
      item_score.append((item_set_slot, i_item, slot_item_horse_armor, get_body_armor(items[i_item][6])))
      item_score.append((item_set_slot, i_item, slot_item_horse_charge, get_thrust_damage(items[i_item][6])))
	  
	## pike definition - CABA addition
    if type == itp_type_polearm and get_weapon_length(items[i_item][6]) >= 150 and (get_thrust_damage(items[i_item][6]) % 256) > (get_swing_damage(items[i_item][6]) % 256):
        item_score.append((item_set_slot, i_item, slot_item_pike, 1))
	
	# ## couchable - CABA addition
    if items[i_item][3] & itp_couchable == itp_couchable:
      item_score.append((item_set_slot, i_item, slot_item_couchable, 1))
	
    ## needs two hands - CABA addition
    item_score.append((item_set_slot, i_item, slot_item_needs_two_hands, items[i_item][3] & itp_two_handed))
    
    ## cant on horseback
    if items[i_item][3] & itp_cant_use_on_horseback == itp_cant_use_on_horseback or items[i_item][3] & itp_cant_reload_on_horseback == itp_cant_reload_on_horseback:
      item_score.append((item_set_slot, i_item, slot_item_cant_on_horseback, 1))
		

  # ## item_modifier
  # for i_modifier in xrange(len(modifiers)):
    # item_score.append((item_set_slot, i_modifier, slot_item_modifier_multiplier, modifiers[i_modifier][1]))
    
  return item_score[:]



## Prebattle Orders & Deployment Begin
scripts = [
  # script_prebattle_order_update_text_slot
  # Input: arg1 = order_column, arg2 = order_no, arg3 = num repeats
  # Output: none
 ("prebattle_order_update_text_slot", [
    (store_script_param_1, ":order_column"),
	(store_script_param_2, ":order_no"),
	(store_script_param, ":repeat", 3),
	
	(try_begin),
		(eq, ":order_no", -1),
		(str_store_string, s1, "str_space"),
	(else_try),
        (eq, ":order_column", 0),
		(try_begin),
            (eq, ":order_no", 0),
			(str_store_string, s1, "@Hold"),
          (else_try),
            (eq, ":order_no", 1),
			(str_store_string, s1, "@Follow Me"),
          (else_try),
            (eq, ":order_no", 2),
			(str_store_string, s1, "@Charge"),
		  (else_try),
            (eq, ":order_no", 3),
			(str_store_string, s1, "@Stand Ground"),
        (try_end),
    (else_try),
        (this_or_next|eq, ":order_column", 1),
		(eq, ":order_column", 2),
		(try_begin),
            (eq, ":order_no", 3),
			(str_store_string, s1, "@Mount"),
        (else_try),
            (eq, ":order_no", 4),
			(str_store_string, s1, "@Dismount"),
        (else_try),
            (eq, ":order_no", 5),
			(str_store_string, s1, "@Forward 10"),
        (else_try),
            (eq, ":order_no", 6),
			(str_store_string, s1, "@Back 10"),
        (else_try),
            (eq, ":order_no", 7),
			(str_store_string, s1, "@Stand Closer"),
        (else_try),
            (eq, ":order_no", 8),
		    (str_store_string, s1, "@Spread Out"),
		(try_end),  
        (neg|is_between, ":order_no", 3, 5), #Not Mount or Dismount		
		(gt, ":repeat", 1),
		(assign, reg0, ":repeat"),
		(str_store_string, s1, "@{s1} x{reg0}"),
	(else_try),
        (eq, ":order_column", 3),
		(try_begin),
		    (eq, ":order_no", formation_ranks),
			(str_store_string, s1, "@Ranks"),
        (else_try),
            (eq, ":order_no", formation_shield),
			(str_store_string, s1, "@Shieldwall"),
        (else_try),         
		    (eq, ":order_no", formation_wedge),
			(str_store_string, s1, "@Wedge"),
        (else_try),
            (eq, ":order_no", formation_square),
			(str_store_string, s1, "@Square"),
        (try_end),
    (else_try),
        (eq, ":order_column", 4),
		(try_begin),
		    (eq, ":order_no", 2),
			(str_store_string, s1, "@Hold Fire"),
        (else_try),
            (eq, ":order_no", 3),
			(str_store_string, s1, "@Fire at Will"),
        (else_try),         
		    (eq, ":order_no", 0),
			(str_store_string, s1, "@Any Weapon"),
        (else_try),
            (eq, ":order_no", 9),
			(str_store_string, s1, "@Blunt Weapons"),
        (try_end),
	(else_try),
        (eq, ":order_column", 5),
		(try_begin),
		    (eq, ":order_no", 1),
			(str_store_string, s1, "@One Handed"),
        (else_try),
            (eq, ":order_no", 2),
			(str_store_string, s1, "@Two Handed"),
        (else_try),         
		    (eq, ":order_no", 3),
			(str_store_string, s1, "@Polearms"),
        (else_try),
            (eq, ":order_no", 0),
			(str_store_string, s1, "@Ranged"),
        (try_end),
	(else_try),
        (eq, ":order_column", 6),
		(try_begin),
		    (eq, ":order_no", 4),
			(str_store_string, s1, "@Use Shield"),
        (else_try),
            (eq, ":order_no", 5),
			(str_store_string, s1, "@No Shields"),
        (try_end),
	(else_try),
        (eq, ":order_column", 7),
		(try_begin),
		    (eq, ":order_no", 1),
			(str_store_string, s1, "@Avoid Melee"),
        (try_end),
	(try_end),
	 	 
	(store_mul, ":column_order_array", ":order_column", 10),
	(val_add, ":column_order_array", slot_party_prebattle_order_array_begin),
	 	 
	(try_begin),
        (eq, "$group0_has_troops", 1),
	    (eq, "$g_formation_group0_selected", 1),
		(store_add, ":slot_order_array", ":column_order_array", 0),
	    (try_begin),
	        (eq, ":order_column", 0),
			(overlay_set_text, "$g_presentation_but0_movement", s1), #Movement=Initial
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
	    (else_try),
			(eq, ":order_column", 1),
			(overlay_set_text, "$g_presentation_but0_riding", s1),  #Riding=Position 1
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
			(eq, ":order_column", 2),
			(overlay_set_text, "$g_presentation_but0_weapon_usage", s1), #WeaponUsage=Position 2
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
			(eq, ":order_column", 3),
			(overlay_set_text, reg(6), s1), #Regs 6-14=Formation
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
			(eq, ":order_column", 4),
			(overlay_set_text, reg(15), s1), #Regs 15-23=Weapon Usage
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 5),
			(overlay_set_text, reg(24), s1),#Regs 24-32=Caba'drin WeaponType
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 6),
			(overlay_set_text, reg(33), s1), #Regs 33-41=Caba'drin Shield
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 7),
			(overlay_set_text, reg(42), s1), #Regs 42-50=Caba'drin Skirmish
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(try_end),
	(try_end),
	(try_begin),
        (eq, "$group1_has_troops", 1),
	    (eq, "$g_formation_group1_selected", 1),
		(store_add, ":slot_order_array", ":column_order_array", 1),
	    (try_begin),
	        (eq, ":order_column", 0),
			(overlay_set_text, "$g_presentation_but1_movement", s1), #Movement=Initial
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
	    (else_try),
	        (eq, ":order_column", 1),
			(overlay_set_text, "$g_presentation_but1_riding", s1),  #Riding=Position 1
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
	        (eq, ":order_column", 2),
			(overlay_set_text, "$g_presentation_but1_weapon_usage", s1), #WeaponUsage=Position 2
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
			(eq, ":order_column", 3),
			(overlay_set_text, reg(7), s1), #Regs 6-14=Formation
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 4),
			(overlay_set_text, reg(16), s1), #Regs 15-23=Weapon Usage
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 5),
			(overlay_set_text, reg(25), s1),#Regs 24-32=Caba'drin WeaponType
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 6),
			(overlay_set_text, reg(34), s1), #Regs 33-41=Caba'drin Shield
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 7),
			(overlay_set_text, reg(43), s1), #Regs 42-50=Caba'drin Skirmish
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(try_end),
	(try_end),
	(try_begin),
        (eq, "$group2_has_troops", 1),
	    (eq, "$g_formation_group2_selected", 1),
		(store_add, ":slot_order_array", ":column_order_array", 2),
	    (try_begin),
	        (eq, ":order_column", 0),
			(overlay_set_text, "$g_presentation_but2_movement", s1), #Movement=Initial
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
	    (else_try),
	        (eq, ":order_column", 1),
			(overlay_set_text, "$g_presentation_but2_riding", s1),  #Riding=Position 1
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
	        (eq, ":order_column", 2),
			(overlay_set_text, "$g_presentation_but2_weapon_usage", s1), #WeaponUsage=Position 2
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
			(eq, ":order_column", 3),
			(overlay_set_text, reg(8), s1), #Regs 6-14=Formation
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 4),
			(overlay_set_text, reg(17), s1), #Regs 15-23=Weapon Usage
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 5),
			(overlay_set_text, reg(26), s1),#Regs 24-32=Caba'drin WeaponType
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 6),
			(overlay_set_text, reg(35), s1), #Regs 33-41=Caba'drin Shield
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 7),
			(overlay_set_text, reg(44), s1), #Regs 42-50=Caba'drin Skirmish
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(try_end),
	(try_end),
	(try_begin),
        (eq, "$group3_has_troops", 1),
	    (eq, "$g_formation_group3_selected", 1),
		(store_add, ":slot_order_array", ":column_order_array", 3),
	    (try_begin),
	        (eq, ":order_column", 0),
			(overlay_set_text, "$g_presentation_but3_movement", s1), #Movement=Initial
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
	    (else_try),
	        (eq, ":order_column", 1),
			(overlay_set_text, "$g_presentation_but3_riding", s1),  #Riding=Position 1
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
	        (eq, ":order_column", 2),
			(overlay_set_text, "$g_presentation_but3_weapon_usage", s1), #WeaponUsage=Position 2
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
			(eq, ":order_column", 3),
			(overlay_set_text, reg(9), s1), #Regs 6-14=Formation
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 4),
			(overlay_set_text, reg(18), s1), #Regs 15-23=Weapon Usage
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 5),
			(overlay_set_text, reg(27), s1),#Regs 24-32=Caba'drin WeaponType
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 6),
			(overlay_set_text, reg(36), s1), #Regs 33-41=Caba'drin Shield
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 7),
			(overlay_set_text, reg(45), s1), #Regs 42-50=Caba'drin Skirmish
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(try_end),
	(try_end),
	(try_begin),
        (eq, "$group4_has_troops", 1),
	    (eq, "$g_formation_group4_selected", 1),
		(store_add, ":slot_order_array", ":column_order_array", 4),
	    (try_begin),
	        (eq, ":order_column", 0),
			(overlay_set_text, "$g_presentation_but4_movement", s1), #Movement=Initial
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
	    (else_try),
	        (eq, ":order_column", 1),
			(overlay_set_text, "$g_presentation_but4_riding", s1),  #Riding=Position 1
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
	        (eq, ":order_column", 2),
			(overlay_set_text, "$g_presentation_but4_weapon_usage", s1), #WeaponUsage=Position 2
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
			(eq, ":order_column", 3),
			(overlay_set_text, reg(10), s1), #Regs 6-14=Formation
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 4),
			(overlay_set_text, reg(19), s1), #Regs 15-23=Weapon Usage
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 5),
			(overlay_set_text, reg(28), s1),#Regs 24-32=Caba'drin WeaponType
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 6),
			(overlay_set_text, reg(37), s1), #Regs 33-41=Caba'drin Shield
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 7),
			(overlay_set_text, reg(46), s1), #Regs 42-50=Caba'drin Skirmish
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(try_end),
	(try_end),
	(try_begin),
        (eq, "$group5_has_troops", 1),
	    (eq, "$g_formation_group5_selected", 1),
		(store_add, ":slot_order_array", ":column_order_array", 5),
	    (try_begin),
	        (eq, ":order_column", 0),
			(overlay_set_text, "$g_presentation_but5_movement", s1), #Movement=Initial
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
	    (else_try),
	        (eq, ":order_column", 1),
			(overlay_set_text, "$g_presentation_but5_riding", s1),  #Riding=Position 1
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
	        (eq, ":order_column", 2),
			(overlay_set_text, "$g_presentation_but5_weapon_usage", s1), #WeaponUsage=Position 2
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
			(eq, ":order_column", 3),
			(overlay_set_text, reg(11), s1), #Regs 6-14=Formation
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 4),
			(overlay_set_text, reg(20), s1), #Regs 15-23=Weapon Usage
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 5),
			(overlay_set_text, reg(29), s1),#Regs 24-32=Caba'drin WeaponType
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 6),
			(overlay_set_text, reg(38), s1), #Regs 33-41=Caba'drin Shield
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 7),
			(overlay_set_text, reg(47), s1), #Regs 42-50=Caba'drin Skirmish
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(try_end),
	(try_end),
	(try_begin),
        (eq, "$group6_has_troops", 1),
	    (eq, "$g_formation_group6_selected", 1),
		(store_add, ":slot_order_array", ":column_order_array", 6),
	    (try_begin),
	        (eq, ":order_column", 0),
			(overlay_set_text, "$g_presentation_but6_movement", s1), #Movement=Initial
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
	    (else_try),
	        (eq, ":order_column", 1),
			(overlay_set_text, "$g_presentation_but6_riding", s1),  #Riding=Position 1
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
	        (eq, ":order_column", 2),
			(overlay_set_text, "$g_presentation_but6_weapon_usage", s1), #WeaponUsage=Position 2
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
			(eq, ":order_column", 3),
			(overlay_set_text, reg(12), s1), #Regs 6-14=Formation
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 4),
			(overlay_set_text, reg(21), s1), #Regs 15-23=Weapon Usage
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 5),
			(overlay_set_text, reg(30), s1),#Regs 24-32=Caba'drin WeaponType
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 6),
			(overlay_set_text, reg(39), s1), #Regs 33-41=Caba'drin Shield
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 7),
			(overlay_set_text, reg(48), s1), #Regs 42-50=Caba'drin Skirmish
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(try_end),
	(try_end),
	(try_begin),
        (eq, "$group7_has_troops", 1),
	    (eq, "$g_formation_group7_selected", 1),
		(store_add, ":slot_order_array", ":column_order_array", 7),
	    (try_begin),
	        (eq, ":order_column", 0),
			(overlay_set_text, "$g_presentation_but7_movement", s1), #Movement=Initial
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
	    (else_try),
	        (eq, ":order_column", 1),
			(overlay_set_text, "$g_presentation_but7_riding", s1),  #Riding=Position 1
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
	        (eq, ":order_column", 2),
			(overlay_set_text, "$g_presentation_but7_weapon_usage", s1), #WeaponUsage=Position 2
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
			(eq, ":order_column", 3),
			(overlay_set_text, reg(13), s1), #Regs 6-14=Formation
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 4),
			(overlay_set_text, reg(22), s1), #Regs 15-23=Weapon Usage
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 5),
			(overlay_set_text, reg(31), s1),#Regs 24-32=Caba'drin WeaponType
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 6),
			(overlay_set_text, reg(40), s1), #Regs 33-41=Caba'drin Shield
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 7),
			(overlay_set_text, reg(49), s1), #Regs 42-50=Caba'drin Skirmish
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(try_end),
	(try_end),
	(try_begin),
        (eq, "$group8_has_troops", 1),
	    (eq, "$g_formation_group8_selected", 1),
		(store_add, ":slot_order_array", ":column_order_array", 8),
	    (try_begin),
	        (eq, ":order_column", 0),
			(overlay_set_text, "$g_presentation_but8_movement", s1), #Movement=Initial
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
	    (else_try),
	        (eq, ":order_column", 1),
			(overlay_set_text, "$g_presentation_but8_riding", s1),  #Riding=Position 1
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
	        (eq, ":order_column", 2),
			(overlay_set_text, "$g_presentation_but8_weapon_usage", s1), #WeaponUsage=Position 2
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
			
			(store_add, ":repeat_slot", ":slot_order_array", 70),
			(party_set_slot, "p_main_party", ":repeat_slot", ":repeat"),
		(else_try),
			(eq, ":order_column", 3),
			(overlay_set_text, reg(14), s1), #Regs 6-14=Formation
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 4),
			(overlay_set_text, reg(23), s1), #Regs 15-23=Weapon Usage
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 5),
			(overlay_set_text, reg(32), s1),#Regs 24-32=Caba'drin WeaponType
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 6),
			(overlay_set_text, reg(41), s1), #Regs 33-41=Caba'drin Shield
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(else_try),
	        (eq, ":order_column", 7),
			(overlay_set_text, reg(50), s1), #Regs 42-50=Caba'drin Skirmish
			(party_set_slot, "p_main_party", ":slot_order_array", ":order_no"),
		(try_end),
	(try_end),
	]),

  # script_prebattle_order_preview_orders
  # Input: none
  # Output: none
 ("prebattle_order_preview_orders", [

	(assign, ":report_y", 690), #675
	(assign, ":orders_available", 8), #Beta, will be scaled by Tactics
	(try_for_range, ":group", 0, 9),
	 
	    (try_begin),
			(eq, ":group", 0),
			(assign, ":group_has_troops", "$group0_has_troops"),
		(try_end),
		(try_begin),
			(eq, ":group", 1),
			(assign, ":group_has_troops", "$group1_has_troops"),
		(try_end),
		(try_begin),
			(eq, ":group", 2),
			(assign, ":group_has_troops", "$group2_has_troops"),
		(try_end),
		(try_begin),
			(eq, ":group", 3),
			(assign, ":group_has_troops", "$group3_has_troops"),
		(try_end),
		(try_begin),
			(eq, ":group", 4),
			(assign, ":group_has_troops", "$group4_has_troops"),
		(try_end),
		(try_begin),
			(eq, ":group", 5),
			(assign, ":group_has_troops", "$group5_has_troops"),
		(try_end),
		(try_begin),
			(eq, ":group", 6),
			(assign, ":group_has_troops", "$group6_has_troops"),
		(try_end),
		(try_begin),
			(eq, ":group", 7),
			(assign, ":group_has_troops", "$group7_has_troops"),
		(try_end),
		(try_begin),
			(eq, ":group", 8),
			(assign, ":group_has_troops", "$group8_has_troops"),
		(try_end),	 
	 
	    (eq, ":group_has_troops", 1),
		(str_store_class_name, s1, ":group"),
		
        (create_text_overlay, reg2, s1), 
        (overlay_set_color, reg2, 0x767676),
		(position_set_y, pos1, ":report_y"),
        (position_set_x, pos1, 700),
        (overlay_set_position, reg2, pos1),
        (val_sub, ":report_y", 70),
		
		
		(try_for_range, ":n", 0, 2),
		    (try_begin),
			    (eq, ":n", 0),
                (assign, ":start", 0),
				(assign, ":end", 4),
			(else_try),
			    (assign, ":start", 4),
				(assign, ":end", ":orders_available"),
			(try_end),
            			
			(assign, ":line_count", 0),
			(str_clear, s2),
			(try_for_range, ":i", ":start", ":end"),
				(store_mul, ":slot_order_array", ":i", 10),
				(val_add, ":slot_order_array", slot_party_prebattle_order_array_begin),
				(val_add, ":slot_order_array", ":group"),
				(party_get_slot, ":order", "p_main_party", ":slot_order_array"),
				(ge, ":order", 0),
				(try_begin),
					(ge, ":slot_order_array", slot_party_prebattle_order_array_begin),
					(lt, ":slot_order_array", slot_party_prebattle_order_array_begin + 10),
					(assign, ":order_type", 1),
				(else_try),
					(ge, ":slot_order_array", slot_party_prebattle_order_array_begin + 10),
					(lt, ":slot_order_array", slot_party_prebattle_order_array_begin + 30),
					(assign, ":order_type", 2),
				(else_try),
					(ge, ":slot_order_array", slot_party_prebattle_order_array_begin + 30),
					(lt, ":slot_order_array", slot_party_prebattle_order_array_begin + 40),
					(assign, ":order_type", 4),
				(else_try),
					(ge, ":slot_order_array", slot_party_prebattle_order_array_begin + 40),
					(lt, ":slot_order_array", slot_party_prebattle_order_array_begin + 50),
					(assign, ":order_type", 3),
				(else_try),
					(ge, ":slot_order_array", slot_party_prebattle_order_array_begin + 50),
					(lt, ":slot_order_array", slot_party_prebattle_order_array_begin + 60),
					(assign, ":order_type", 5),
				(else_try),
					(ge, ":slot_order_array", slot_party_prebattle_order_array_begin + 60),
					(lt, ":slot_order_array", slot_party_prebattle_order_array_begin + 70),
					(assign, ":order_type", 6),
				(else_try),
					(ge, ":slot_order_array", slot_party_prebattle_order_array_begin + 70),
					(lt, ":slot_order_array", slot_party_prebattle_order_array_begin + 80),
					(assign, ":order_type", 7),
				(try_end),
				
				(try_begin),
					(eq, ":order_type", 1),
					(try_begin),
						(eq, ":order", 0),
						(str_store_string, s1, "@Hold Position"),
					(else_try),
						(eq, ":order", 1),
						(str_store_string, s1, "@Follow Me"),
					(else_try),
						(eq, ":order", 2),
						(str_store_string, s1, "@Charge"),
					(else_try),
						(eq, ":order", 3),
						(str_store_string, s1, "@Stand Ground"),
					(try_end),
				(else_try),
					(eq, ":order_type", 2),
					(try_begin),
						(eq, ":order", 3),
						(str_store_string, s1, "@Mount"),
					(else_try),
						(eq, ":order", 4),
						(str_store_string, s1, "@Dismount"),
					(else_try),
						(eq, ":order", 5),
						(str_store_string, s1, "@Forward 10"),
					(else_try),
						(eq, ":order", 6),
						(str_store_string, s1, "@Back 10 Paces"),
					(else_try),
						(eq, ":order", 7),
						(str_store_string, s1, "@Stand Closer"),
					(else_try),
						(eq, ":order", 8),
						(str_store_string, s1, "@Spread Out"),
					(try_end),
					(try_begin),
						(store_add, ":repeat_slot", ":slot_order_array", 70), #30
						(party_get_slot, ":repeat", "p_main_party", ":repeat_slot"),
						(gt, ":repeat", 1),
						(assign, reg0, ":repeat"),
						(str_store_string, s1, "@{s1} x{reg0}"),
					(try_end),
				(else_try),
					(eq, ":order_type", 4),
					(try_begin),
						(eq, ":order", formation_ranks),
						(str_store_string, s1, "@Ranks"),
					(else_try),
						(eq, ":order", formation_shield),
						(str_store_string, s1, "@Shieldwall"),
					(else_try),
						(eq, ":order", formation_wedge),
						(str_store_string, s1, "@Wedge"),
					(else_try),
						(eq, ":order", formation_square),
						(str_store_string, s1, "@Square"),
					(try_end),
				(else_try),
					(eq, ":order_type", 3),
					(try_begin),
						(eq, ":order", 0),
						(str_store_string, s1, "@Use Any Weapon"),
					(else_try),
						(eq, ":order", 9),
						(str_store_string, s1, "@Use Blunt Weapons"),
					(else_try),
						(eq, ":order", 2),
						(str_store_string, s1, "@Hold Fire"),
					(else_try),
						(eq, ":order", 3),
						(str_store_string, s1, "@Fire at Will"),
					(try_end),
				(else_try),
					(eq, ":order_type", 5),
					(try_begin),
						(eq, ":order", 1),
						(str_store_string, s1, "@One-Handed Weapons"),
					(else_try),
						(eq, ":order", 2),
						(str_store_string, s1, "@Two-Handed Weapons"),
					(else_try),
						(eq, ":order", 3),
						(str_store_string, s1, "@Polearms"),
					(else_try),
						(eq, ":order", 0),
						(str_store_string, s1, "@Ranged Weapons"),
					(try_end),
				(else_try),
					(eq, ":order_type", 6),
					(try_begin),
						(eq, ":order", 5),
						(str_store_string, s1, "@No Shields"),
					(else_try),
						(eq, ":order", 4),
						(str_store_string, s1, "@Use Shields"),
					(try_end),
				(else_try),
					(eq, ":order_type", 7),
					(eq, ":order", 1),
					(str_store_string, s1, "@Avoid Melee"),
				(try_end),

				(try_begin),
					(str_is_empty, s2),
					(str_store_string_reg, s2, s1),
				(else_try),
					(str_store_string, s2, "@{s2}^{s1}"),
				(try_end),			
				
				(val_add, ":line_count", 1),
			(try_end), # Order Column Loop
			
			(try_begin),
				(eq, ":line_count", 0),
				(try_begin),
				    (eq, ":n", 0),
				    (str_store_string, s2, "@No Position Orders"),
				(else_try),
				    (str_store_string, s2, "@No Weapons Orders"),
				(try_end),
			(try_end),
			
			(store_mul, ":shift_y", ":line_count", 7),
			(store_sub, ":shift_y", 50, ":shift_y"),		
			
			(store_add, ":y", ":report_y", ":shift_y"),
			(position_set_y, pos1, ":y"),
			(try_begin),
			    (eq, ":n", 0),
			    (position_set_x, pos1, 720),
			(else_try),
			    (position_set_x, pos1, 830),
            (try_end),				

			(try_begin),
				(eq, ":group", 0),
				(try_begin),
				    (eq, ":n", 0),
				    (overlay_set_text, "$g_presentation_obj_custom_battle_designer_1", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_1", pos1),
				(else_try),
					(overlay_set_text, "$g_presentation_obj_custom_battle_designer_11", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_11", pos1),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":group", 1),
				(try_begin),
				    (eq, ":n", 0),
				    (overlay_set_text, "$g_presentation_obj_custom_battle_designer_2", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_2", pos1),
				(else_try),
					(overlay_set_text, "$g_presentation_obj_custom_battle_designer_12", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_12", pos1),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":group", 2),
				(try_begin),
				    (eq, ":n", 0),
				    (overlay_set_text, "$g_presentation_obj_custom_battle_designer_3", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_3", pos1),
				(else_try),
					(overlay_set_text, "$g_presentation_obj_custom_battle_designer_13", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_13", pos1),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":group", 3),
				(try_begin),
				    (eq, ":n", 0),
				    (overlay_set_text, "$g_presentation_obj_custom_battle_designer_4", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_4", pos1),
				(else_try),
					(overlay_set_text, "$g_presentation_obj_custom_battle_designer_14", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_14", pos1),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":group", 4),
				(try_begin),
				    (eq, ":n", 0),
				    (overlay_set_text, "$g_presentation_obj_custom_battle_designer_5", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_5", pos1),
				(else_try),
					(overlay_set_text, "$g_presentation_obj_custom_battle_designer_15", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_15", pos1),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":group", 5),
				(try_begin),
				    (eq, ":n", 0),
				    (overlay_set_text, "$g_presentation_obj_custom_battle_designer_6", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_6", pos1),
				(else_try),
					(overlay_set_text, "$g_presentation_obj_custom_battle_designer_16", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_16", pos1),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":group", 6),
				(try_begin),
				    (eq, ":n", 0),
				    (overlay_set_text, "$g_presentation_obj_custom_battle_designer_7", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_7", pos1),
                (else_try),
					(overlay_set_text, "$g_presentation_obj_custom_battle_designer_17", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_17", pos1),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":group", 7),
				(try_begin),
				    (eq, ":n", 0),
				    (overlay_set_text, "$g_presentation_obj_custom_battle_designer_8", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_8", pos1),
				(else_try),
					(overlay_set_text, "$g_presentation_obj_custom_battle_designer_18", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_18", pos1),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":group", 8),
				(try_begin),
				    (eq, ":n", 0),
				    (overlay_set_text, "$g_presentation_obj_custom_battle_designer_9", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_9", pos1),
				(else_try),
					(overlay_set_text, "$g_presentation_obj_custom_battle_designer_19", s2),
				    (overlay_set_position, "$g_presentation_obj_custom_battle_designer_19", pos1),
				(try_end),
			(try_end),	 
	
	    (try_end), #Orders Twice Loop
	(try_end), # Group Loop
	]),
		
  # script_prebattle_order_store_orders
  # Input: none
  # Output: none
 ("prebattle_order_store_orders", [
     
	(assign, ":needs_delay", 0), #fix test
	(assign, ":num_orders", 0),
	(assign, ":highest_slot", 0),
	(assign, ":orders_available", 8), #Beta, will be scaled by Tactics
	(try_for_range, ":group", 0, 9),
	 
	    (try_begin),
			(eq, ":group", 0),
			(assign, ":group_has_troops", "$group0_has_troops"),
		(else_try),
			(eq, ":group", 1),
			(assign, ":group_has_troops", "$group1_has_troops"),
		(else_try),
			(eq, ":group", 2),
			(assign, ":group_has_troops", "$group2_has_troops"),
		(else_try),
			(eq, ":group", 3),
			(assign, ":group_has_troops", "$group3_has_troops"),
		(else_try),
			(eq, ":group", 4),
			(assign, ":group_has_troops", "$group4_has_troops"),
		(else_try),
			(eq, ":group", 5),
			(assign, ":group_has_troops", "$group5_has_troops"),
		(else_try),
			(eq, ":group", 6),
			(assign, ":group_has_troops", "$group6_has_troops"),
		(else_try),
			(eq, ":group", 7),
			(assign, ":group_has_troops", "$group7_has_troops"),
		(else_try),
			(eq, ":group", 8),
			(assign, ":group_has_troops", "$group8_has_troops"),
		(try_end),	 
	 
	    (eq, ":group_has_troops", 1),
	    (try_for_range, ":i", 0, ":orders_available"),
		    (store_mul, ":slot_order_array", ":i", 10),
			(val_add, ":slot_order_array", slot_party_prebattle_order_array_begin),
			(val_add, ":slot_order_array", ":group"),
			(party_get_slot, ":order", "p_main_party", ":slot_order_array"),
			(ge, ":order", 0),
			(try_begin),
				(gt, ":slot_order_array", ":highest_slot"),
				(assign, ":highest_slot", ":slot_order_array"),
			(try_end),
			(try_begin),
				(ge, ":slot_order_array", slot_party_prebattle_order_array_begin),
				(lt, ":slot_order_array", slot_party_prebattle_order_array_begin + 10),
				(assign, ":order_type", 1),
			(else_try),
				(ge, ":slot_order_array", slot_party_prebattle_order_array_begin + 10),
				(lt, ":slot_order_array", slot_party_prebattle_order_array_begin + 30),
				(assign, ":order_type", 2),
			(else_try),
				(ge, ":slot_order_array", slot_party_prebattle_order_array_begin + 30),
				(lt, ":slot_order_array", slot_party_prebattle_order_array_begin + 40),
				(assign, ":order_type", 4),
			(else_try),
				(ge, ":slot_order_array", slot_party_prebattle_order_array_begin + 40),
				(lt, ":slot_order_array", slot_party_prebattle_order_array_begin + 50),
				(assign, ":order_type", 3),
			(else_try),
				(ge, ":slot_order_array", slot_party_prebattle_order_array_begin + 50),
				(lt, ":slot_order_array", slot_party_prebattle_order_array_begin + 60),
				(assign, ":order_type", 5),
			(else_try),
				(ge, ":slot_order_array", slot_party_prebattle_order_array_begin + 60),
				(lt, ":slot_order_array", slot_party_prebattle_order_array_begin + 70),
				(assign, ":order_type", 6),
			(else_try),
				(ge, ":slot_order_array", slot_party_prebattle_order_array_begin + 70),
				(lt, ":slot_order_array", slot_party_prebattle_order_array_begin + 80),
				(assign, ":order_type", 7),
			(try_end),
			  
			(store_mul, ":order_group", ":group", 100),
			(val_mul, ":order_type", 10),
			(store_add, ":order_index", ":order_group", ":order_type"),
			(val_add, ":order_index", ":order"),	
		    (party_set_slot, "p_main_party", ":slot_order_array", ":order_index"),
			(val_add, ":num_orders", 1),
			
			(eq, ":needs_delay", 0), #fix test, here down
			(this_or_next|is_between, ":order_type", 50, 70), # 5 or 6; Caba Weapon and Shield orders
			(eq, ":order_type", 20), #Movement Orders
			(assign, ":needs_delay", 1),
			(eq, ":order_type", 20), #Movement Orders - only these 4 need delay, if not, no delay
			(neg|is_between, ":order", 5, 9), #5 - 8; Forward/Back 10 Paces, Stand Closer/Spread Out 
			(assign, ":needs_delay", 0),
		(try_end), # Order Column Loop
	(try_end), # Group Loop

	(try_begin), 
		(gt, ":num_orders", 0),
		(store_sub, ":num_slots", ":highest_slot", slot_party_prebattle_order_array_begin),
		(val_add, ":num_slots", 1), #for future loop iterations
	(else_try),
		(assign, ":num_slots", 0),
		(party_set_slot, "p_main_party", slot_party_prebattle_plan, 0),
	(try_end),
	(party_set_slot, "p_main_party", slot_party_prebattle_num_orders, ":num_slots"),
	(try_begin), #fix test, this block
	    (eq, ":needs_delay", 1),
		(party_set_slot, "p_main_party_backup", slot_party_prebattle_num_orders, ":num_slots"), 
	(else_try),
	    (party_set_slot, "p_main_party_backup", slot_party_prebattle_num_orders, 0), #not necessary, just safety
	(try_end),
  
  ]), 
 
  # script_prebattle_order_get_stored
  # Input: none
  # Output: none
 ("prebattle_order_get_stored", [
	(assign, ":orders_available", 8), #Beta, will be scaled by Tactics
	(store_mul, ":num_of_orders", ":orders_available", 10),
	
	(try_for_range, ":i", 0, ":num_of_orders"),    
		(store_add, ":ith_order_slot", ":i", slot_party_prebattle_order_array_begin),
        (party_get_slot, ":order_index", "p_main_party", ":ith_order_slot"),
		(try_begin),
			(ge, ":order_index", 10),
			
			#Take 3 digit order index and get component parts: group, type, order
			(store_div, ":ith_order_group", ":order_index", 100),
			(store_mul, ":ith_order_type", ":ith_order_group", 100),
			(val_sub, ":order_index", ":ith_order_type"),
			(store_div, ":ith_order_type", ":order_index", 10),
			(store_mul, ":ith_order", ":ith_order_type", 10),
			(store_sub, ":ith_order", ":order_index", ":ith_order"),
			
		(else_try),
		    (assign, ":ith_order", -1),
		(try_end),
		
		(try_begin),
			(ge, ":ith_order_slot", slot_party_prebattle_order_array_begin),
			(lt, ":ith_order_slot", slot_party_prebattle_order_array_begin + 10),
			(assign, ":order_column", 0),
		(else_try),
			(ge, ":ith_order_slot", slot_party_prebattle_order_array_begin + 10),
			(lt, ":ith_order_slot", slot_party_prebattle_order_array_begin + 20),
			(assign, ":order_column", 1),
		(else_try),
			(ge, ":ith_order_slot", slot_party_prebattle_order_array_begin + 20),
			(lt, ":ith_order_slot", slot_party_prebattle_order_array_begin + 30),
			(assign, ":order_column", 2),
		(else_try),
			(ge, ":ith_order_slot", slot_party_prebattle_order_array_begin + 30),
			(lt, ":ith_order_slot", slot_party_prebattle_order_array_begin + 40),
			(assign, ":order_column", 3),
		(else_try),
			(ge, ":ith_order_slot", slot_party_prebattle_order_array_begin + 40),
			(lt, ":ith_order_slot", slot_party_prebattle_order_array_begin + 50),
			(assign, ":order_column", 4),
		(else_try),
			(ge, ":ith_order_slot", slot_party_prebattle_order_array_begin + 50),
			(lt, ":ith_order_slot", slot_party_prebattle_order_array_begin + 60),
			(assign, ":order_column", 5),
		(else_try),
			(ge, ":ith_order_slot", slot_party_prebattle_order_array_begin + 60),
			(lt, ":ith_order_slot", slot_party_prebattle_order_array_begin + 70),
			(assign, ":order_column", 6),
		(else_try),
			(ge, ":ith_order_slot", slot_party_prebattle_order_array_begin + 70),
			(lt, ":ith_order_slot", slot_party_prebattle_order_array_begin + 80),
			(assign, ":order_column", 7),
		(try_end),
		(store_mul, ":column_offset", ":order_column", 10),
		(val_add, ":column_offset", slot_party_prebattle_order_array_begin),
		(store_sub, ":ith_order_group", ":ith_order_slot", ":column_offset"),
		
		(assign, ":repeat", 0),
		(try_begin),
			(neq, ":ith_order", -1),
			(this_or_next|eq, ":order_column", 1),
			(eq, ":order_column", 2),
			(store_add, ":repeat_slot", ":ith_order_slot", 70), #30
			(party_get_slot, ":repeat", "p_main_party", ":repeat_slot"),
			(val_max, ":repeat", 0),
		(try_end),
			
		(try_begin),
			(eq, ":ith_order_group", 0),
			(assign, "$g_formation_group0_selected", 1),
		(else_try),
			(eq, ":ith_order_group", 1),
			(assign, "$g_formation_group1_selected", 1),
		(else_try),
			(eq, ":ith_order_group", 2),
			(assign, "$g_formation_group2_selected", 1),
		(else_try),
			(eq, ":ith_order_group", 3),
			(assign, "$g_formation_group3_selected", 1),
		(else_try),
			(eq, ":ith_order_group", 4),
			(assign, "$g_formation_group4_selected", 1),
		(else_try),
			(eq, ":ith_order_group", 5),
			(assign, "$g_formation_group5_selected", 1),
		(else_try),
			(eq, ":ith_order_group", 6),
			(assign, "$g_formation_group6_selected", 1),
		(else_try),
			(eq, ":ith_order_group", 7),
			(assign, "$g_formation_group7_selected", 1),
		(else_try),
			(eq, ":ith_order_group", 8),
			(assign, "$g_formation_group8_selected", 1),
		(try_end),
		
		(call_script, "script_prebattle_order_update_text_slot", ":order_column", ":ith_order", ":repeat"),
		 
		(assign, "$g_formation_group0_selected", 0),
		(assign, "$g_formation_group1_selected", 0),
		(assign, "$g_formation_group2_selected", 0),
		(assign, "$g_formation_group3_selected", 0),
		(assign, "$g_formation_group4_selected", 0),
		(assign, "$g_formation_group5_selected", 0),
		(assign, "$g_formation_group6_selected", 0),
		(assign, "$g_formation_group7_selected", 0),
		(assign, "$g_formation_group8_selected", 0),
		
	(try_end),
   ]),
   
  # script_prebattle_order_clear_all
  # Input: none
  # Output: none
 ("prebattle_order_clear_all", [
 
    (try_begin),
	    (eq, "$group0_has_troops", 1),
	    (assign, "$g_formation_group0_selected", 1),
	(try_end),
	(try_begin),
	    (eq, "$group1_has_troops", 1),
	    (assign, "$g_formation_group1_selected", 1),
	(try_end),
	(try_begin),
	    (eq, "$group2_has_troops", 1),
	    (assign, "$g_formation_group2_selected", 1),
	(try_end),
	(try_begin),
	    (eq, "$group3_has_troops", 1),
	    (assign, "$g_formation_group3_selected", 1),
	(try_end),
	(try_begin),
	    (eq, "$group4_has_troops", 1),
	    (assign, "$g_formation_group4_selected", 1),
	(try_end),
	(try_begin),
	    (eq, "$group5_has_troops", 1),
	    (assign, "$g_formation_group5_selected", 1),
	(try_end),
	(try_begin),
	    (eq, "$group6_has_troops", 1),
	    (assign, "$g_formation_group6_selected", 1),
	(try_end),
	(try_begin),
	    (eq, "$group7_has_troops", 1),
	    (assign, "$g_formation_group7_selected", 1),
	(try_end),
	(try_begin),
	    (eq, "$group8_has_troops", 1),
	    (assign, "$g_formation_group8_selected", 1),
	(try_end),	
	
    (assign, ":orders_available", 8), #Beta, will be scaled by Tactics
	(try_for_range, ":column", 0, ":orders_available"),
	    (call_script, "script_prebattle_order_update_text_slot", ":column", -1, 0),
	(try_end),
	
	(try_for_range, ":repeat_slot", slot_party_prebattle_order_array_begin + 80, slot_party_prebattle_order_array_begin + 100),
	    (party_set_slot, "p_main_party", ":repeat_slot", 0),
	(try_end),
	(overlay_set_val, reg(51), 1),
	(overlay_set_val, reg(52), 1),
	(assign, reg53, 0),
	(assign, reg54, 0),
	
	(try_begin),
	    (eq, "$group0_has_troops", 1),
	    (assign, "$g_formation_group0_selected", 0),
		(overlay_set_val, "$g_presentation_obj_battle_check0", 0),
		(overlay_animate_to_alpha, "$g_presentation_obj_battle_but0", 250, 0),
	(try_end),
	(try_begin),
	    (eq, "$group1_has_troops", 1),
	    (assign, "$g_formation_group1_selected", 0),
		(overlay_set_val, "$g_presentation_obj_battle_check1", 0),
		(overlay_animate_to_alpha, "$g_presentation_obj_battle_but1", 250, 0),
	(try_end),
	(try_begin),
	    (eq, "$group2_has_troops", 1),
	    (assign, "$g_formation_group2_selected", 0),
		(overlay_set_val, "$g_presentation_obj_battle_check2", 0),
		(overlay_animate_to_alpha, "$g_presentation_obj_battle_but2", 250, 0),
	(try_end),
	(try_begin),
	    (eq, "$group3_has_troops", 1),
	    (assign, "$g_formation_group3_selected", 0),
		(overlay_set_val, "$g_presentation_obj_battle_check3", 0),
		(overlay_animate_to_alpha, "$g_presentation_obj_battle_but3", 250, 0),
	(try_end),
	(try_begin),
	    (eq, "$group4_has_troops", 1),
	    (assign, "$g_formation_group4_selected", 0),
		(overlay_set_val, "$g_presentation_obj_battle_check4", 0),
		(overlay_animate_to_alpha, "$g_presentation_obj_battle_but4", 250, 0),
	(try_end),
	(try_begin),
	    (eq, "$group5_has_troops", 1),
	    (assign, "$g_formation_group5_selected", 0),
		(overlay_set_val, "$g_presentation_obj_battle_check5", 0),
		(overlay_animate_to_alpha, "$g_presentation_obj_battle_but5", 250, 0),
	(try_end),
	(try_begin),
	    (eq, "$group6_has_troops", 1),
	    (assign, "$g_formation_group6_selected", 0),
		(overlay_set_val, "$g_presentation_obj_battle_check6", 0),
		(overlay_animate_to_alpha, "$g_presentation_obj_battle_but6", 250, 0),
	(try_end),
	(try_begin),
	    (eq, "$group7_has_troops", 1),
	    (assign, "$g_formation_group7_selected", 0),
		(overlay_set_val, "$g_presentation_obj_battle_check7", 0),
		(overlay_animate_to_alpha, "$g_presentation_obj_battle_but7", 250, 0),
	(try_end),
	(try_begin),
	    (eq, "$group8_has_troops", 1),
	    (assign, "$g_formation_group8_selected", 0),
		(overlay_set_val, "$g_presentation_obj_battle_check8", 0),
		(overlay_animate_to_alpha, "$g_presentation_obj_battle_but8", 250, 0),
	(try_end),

   ]),
	
  # script_prebattle_set_default_prefs
  # Input: None
  # Output: None
 ("prebattle_set_default_prefs", [ 
	(party_set_slot, "p_main_party", slot_party_pref_wu_lance, 1),
	(party_set_slot, "p_main_party", slot_party_pref_wu_harcher, 1),
	(party_set_slot, "p_main_party", slot_party_pref_wu_spear, 1),
	(party_set_slot, "p_main_party", slot_party_pref_dmg_tweaks, 1),
	
	(party_set_slot, "p_main_party", slot_party_pref_bodyguard, 1),
	(party_set_slot, "p_main_party", slot_party_pref_bc_continue, 1),
	(party_set_slot, "p_main_party", slot_party_pref_bc_charge_ko, 0),
	(party_set_slot, "p_main_party", slot_party_pref_div_dehorse, 9),
	(party_set_slot, "p_main_party", slot_party_pref_div_no_ammo, 9),
	(party_set_slot, "p_main_party", slot_party_pref_formations, 1), 
	(party_set_slot, "p_main_party", slot_party_pref_spear_brace, 0),
	(party_set_slot, "p_main_party", slot_party_pref_wp_prof_decrease, 1),
    ]),
	
## Caba'drin Orders Begin
  # script_weapon_use_backup_weapon
  # Input: arg1: agent; arg2: 1 - Include Two-Handers, 2 - One-hand only
  # Output: none
 ("weapon_use_backup_weapon",   
    [    
     # Find non-lance/spear/bow item in inventory
    (store_script_param_1, ":agent"),
	(store_script_param_2, ":inc_two_handers"),
	
    (assign,":has_choice",0),
	(assign, ":end", ek_head),
	(try_for_range, ":i", ek_item_0, ":end"),
		(agent_get_item_slot, ":item", ":agent",":i"),
		(gt, ":item", 0),
		(item_get_type, ":weapontype", ":item"),
		(try_begin),
			(eq, ":inc_two_handers", 0),
			(eq, ":weapontype", itp_type_one_handed_wpn),
			(assign, ":has_choice", 1),
			(assign, ":end", ek_item_0), #Loop breaker
		(else_try),
			(is_between, ":weapontype", itp_type_one_handed_wpn, itp_type_polearm),#one or two handed
			(assign,":has_choice",1),
			(assign, ":end", ek_item_0),#loop breaker
		(try_end),
	(try_end),
    (try_begin),# Equip their backup weapon.
        (eq, ":has_choice",1),
        (agent_set_wielded_item, ":agent", ":item"),
    (try_end),
    ]),    
   
  # script_weapon_use_classify_agent
  # Input: agent_no
  # Output: None
 ("weapon_use_classify_agent", [ 
    (store_script_param_1, ":agent"),
    (try_begin),
		(agent_is_alive, ":agent"),
		(agent_is_non_player, ":agent"),
		(try_begin),
			(agent_is_human, ":agent"),
			(agent_get_troop_id, ":troop",":agent"),
			(agent_get_wielded_item, ":wielded", ":agent", 0),
			(neg|troop_is_guarantee_ranged, ":troop"), #Not an archer
			(neg|troop_is_guarantee_horse, ":troop"), #Not Mounted
			(agent_get_ammo, ":has_ammo", ":agent", 0), #Double-check this one doesn't have throwing weapons, etc
			(le, ":has_ammo", 0), #Doesn't have ammo
			(try_begin),
				(gt, ":wielded", 0),
				(item_get_type, ":wielded_type", ":wielded"),
				(eq, ":wielded_type", itp_type_polearm),  # Is it a polearm?
				(agent_set_slot, ":agent", slot_agent_spear, ":wielded"), #Mark spearmen
			(else_try), #Check if there's a spear equipped, if not wielded
				(assign, ":end", ek_head),
				(try_for_range, ":i", ek_item_0, ":end"),
					(agent_get_item_slot, ":item", ":agent", ":i"),
					(gt, ":item", 0),
					(item_get_type, ":weapontype", ":item"),
					(eq, ":weapontype", itp_type_polearm),  # Is it a spear?
					(agent_set_slot, ":agent", slot_agent_spear, ":item"), #Mark spearmen
					(assign, ":end", ek_item_0), #loop Break
				(try_end),
			(try_end),
		(else_try),	
			(neg|agent_is_human, ":agent"), #Is Horse
			(assign, ":horse", ":agent"),
			(agent_get_rider, ":agent", ":horse"),
			(agent_is_active, ":agent"), 
			(agent_get_troop_id, ":troop",":agent"),
			(agent_get_wielded_item, ":wielded", ":agent", 0),
			(try_begin),
				(neg|troop_is_guarantee_ranged, ":troop"), # Not a horsearcher
				(try_begin),
					(gt, ":wielded", 0),
					(item_slot_eq, ":wielded", slot_item_couchable, 1),
					(agent_set_slot, ":agent", slot_agent_lance, ":wielded"),
					(agent_set_slot, ":agent", slot_agent_spear, 0), #double-check
				(else_try),    
	   # Force the NPC to wield a lance, but this will only happen if they
	   # actually have a lance equipped.  Otherwise this does nothing.
					(assign, ":end", ek_head),
					(try_for_range, ":i", ek_item_0, ":end"),
						(agent_get_item_slot, ":item", ":agent", ":i"),
						(gt, ":item", 0),
						(item_slot_eq, ":item", slot_item_couchable, 1),
						(agent_set_slot, ":agent", slot_agent_lance, ":item"),
						(agent_set_slot, ":agent", slot_agent_spear, 0), #double-check
						(agent_set_wielded_item, ":agent", ":item"),
						(assign, ":end", ek_item_0),
					(try_end),
				(try_end),
			(else_try),
				(troop_is_guarantee_ranged, ":troop"), # Is a horsearcher...redundant, but making sure
				(try_begin),
					(gt, ":wielded", 0),
					(item_get_type, ":type", ":wielded"),
					(this_or_next|eq, ":type", itp_type_bow),
					(eq, ":type", itp_type_crossbow),
					(neg|item_slot_eq, ":wielded", slot_item_cant_on_horseback, 1),
					(agent_set_slot, ":agent", slot_agent_horsebow, ":wielded"),
					(agent_set_slot, ":agent", slot_agent_spear, 0), #double-check
				(else_try), 
	   # Force the NPC to wield their bow, but this will only happen if they
	   # actually have a bow equipped.  Otherwise this does nothing.
					(assign, ":end", ek_head),
					(try_for_range, ":i", ek_item_0, ":end"),
						(agent_get_item_slot, ":item", ":agent", ":i"),
						(gt, ":item", 0),
						(item_get_type, ":type", ":item"),
						(this_or_next|eq, ":type", itp_type_bow),
						(eq, ":type", itp_type_crossbow),
						(neg|item_slot_eq, ":item", slot_item_cant_on_horseback, 1),
						(agent_set_wielded_item, ":agent", ":item"),
						(agent_set_slot, ":agent", slot_agent_horsebow, ":item"), #Mark horse archers for later use
						(agent_set_slot, ":agent", slot_agent_spear, 0), #double-check
						(assign, ":end", ek_item_0),#loop breaker      
					(try_end),
				(try_end),				
			(try_end), #Lancer or Horse Archer
		(try_end), #Human v Horse
	(try_end), #prevent failure
    ]),
   
  # script_order_set_team_slot
  # Input: Order Type ; team  
  # Output: Modified slot_team_d0_order_*
 ("order_set_team_slot", [
    (store_script_param_1, ":ordertype"),
	(store_script_param_2, ":team"),
	(assign, ":weapon_order", -2),
    (assign, ":shield_order", -2),
	(assign, ":skirmish_order", -2),
	(assign, ":volley_order", -2),
	(assign, ":brace_order", -2),
	
	(try_begin),
		(eq, ":ordertype", clear),
		(assign, ":weapon_order", clear),
		(assign, ":shield_order", clear),
	(else_try),
		(this_or_next|eq, ":ordertype", ranged),
     	(this_or_next|eq, ":ordertype", onehand),
		(eq, ":ordertype", polearm),
		(assign, ":weapon_order", ":ordertype"),
	(else_try),
		(eq, ":ordertype", twohands),
		(assign, ":weapon_order", twohands),
		(assign, ":shield_order", clear),
	(else_try),
		(eq, ":ordertype", shield),
		(assign, ":shield_order", 1),
	(else_try),
		(eq, ":ordertype", noshield),
		(assign, ":shield_order", 0),
	(else_try),
		(eq, ":ordertype", free),
		(assign, ":shield_order", clear),		
	(else_try),
		(eq, ":ordertype", 8), 
		(assign, ":skirmish_order", end),
	(else_try),
		(eq, ":ordertype", 9),
		(assign, ":skirmish_order", begin),
	(else_try),
		(eq, ":ordertype", 10), 
		(assign, ":volley_order", end),
	(else_try),
		(eq, ":ordertype", 11),
		(assign, ":volley_order", begin),
	(else_try),
		(eq, ":ordertype", 12), 
		(assign, ":brace_order", end),
	(else_try),
		(eq, ":ordertype", 13),
		(assign, ":brace_order", begin),
	(try_end),
	
	
	(try_for_range, ":class", 0, 9),
	    (class_is_listening_order, ":team", ":class"), #Listening to Order		
		
		(try_begin),
		    (neq, ":weapon_order", -2),
			(store_add, ":slot", slot_team_d0_order_weapon, ":class"),
		    (team_set_slot, ":team", ":slot", ":weapon_order"),
		(try_end),
		(try_begin),
		    (neq, ":shield_order", -2),
		    (store_add, ":slot", slot_team_d0_order_shield, ":class"),
		    (team_set_slot, ":team", ":slot", ":shield_order"),
		(try_end),
		(try_begin),
		    (neq, ":skirmish_order", -2),
			(store_add, ":slot", slot_team_d0_order_skirmish, ":class"),
		    (team_set_slot, ":team", ":slot", ":skirmish_order"),
		(try_end),
		(try_begin),
		    (neq, ":volley_order", -2),
			(store_add, ":slot", slot_team_d0_order_volley, ":class"),
		    (team_set_slot, ":team", ":slot", ":volley_order"),
		(try_end),
		(try_begin),
		    (neq, ":brace_order", -2),
			(store_add, ":slot", slot_team_d0_order_sp_brace, ":class"),
		    (team_set_slot, ":team", ":slot", ":brace_order"),
		(try_end),
	(try_end), #Class Loop
	
	]),

  # script_order_set_display_text
  # Input: Order Type   
  # Output: None
  # Display appropriate order text on screen.
 ("order_set_display_text", [
    (store_script_param_1, ":ordertype"),
	
	(try_begin),
	    (eq, ":ordertype", ranged),
        (str_store_string, s1, "@ready bows and missiles"),
	(else_try),
	    (eq, ":ordertype", onehand),
        (str_store_string, s1, "@ready side arms"),
	(else_try),
        (eq, ":ordertype", twohands),
        (str_store_string, s1, "@ready two-handers"),
	(else_try),
        (eq, ":ordertype", polearm),
        (str_store_string, s1, "@ready polearms"),
	(else_try),
	    (eq, ":ordertype", shield),
		(str_store_string, s1, "@brandish shields"),
	(else_try),			
	    (eq, ":ordertype", noshield),
		(str_store_string, s1, "@doff your shields"),
	(else_try),			
	    (eq, ":ordertype", free),
		(str_store_string, s1, "@shields at will"),
	(else_try),
		(eq, ":ordertype", 9),
		(str_store_string, s1, "@avoid melee"),
	(else_try),
	    (eq, ":ordertype", 8),
		(str_store_string, s1, "@stand and fight"),
	(else_try),
		(eq, ":ordertype", 11),
		(str_store_string, s1, "@prepare to volley"),
	(else_try),
	    (eq, ":ordertype", 10),
		(str_store_string, s1, "@end volley"),
	(else_try),
		(eq, ":ordertype", 13),
		(str_store_string, s1, "@brace for charge"),
	(else_try),
	    (eq, ":ordertype", 12),
		(str_store_string, s1, "@remove brace and fight"),
	(try_end), 
		 
	(try_for_range, ":division", 0, 9),
		(troop_set_slot, "trp_temp_array_a", ":division", 0),
		(troop_set_slot, "trp_temp_array_b", ":division", 0),
	(try_end),
	
	(party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),  #This doesn't mean that type of troop is actually present in the battle...
	(try_for_range, ":i", 0, ":num_of_stacks"),
		(party_stack_get_troop_id, ":troop", "p_main_party", ":i"),
		(neq, ":troop", "trp_player"),
		(troop_get_class, ":division", ":troop"),
	    (troop_set_slot, "trp_temp_array_a", ":division", 1), #In battle
        (class_is_listening_order, "$fplayer_team_no", ":division"), #Is the stack's class selected?
        (troop_set_slot, "trp_temp_array_b", ":division", 1), #Mark class as selected
	(try_end), #Stack Loop	 
		 
	(str_clear, s2),
    (str_clear, s3),
    (assign, ":count_possible", 0),
    (assign, ":count_selected", 0),
	(try_for_range, ":division", 0, 9),
		(troop_slot_eq, "trp_temp_array_a", ":division", 1), #in battle
		(val_add, ":count_possible", 1),
		(troop_slot_eq, "trp_temp_array_b", ":division", 1), #selected
		(val_add, ":count_selected", 1),
		(try_begin),
            (str_is_empty, s2),
			(str_store_class_name, s2, ":division"),
        (else_try),
            (str_store_class_name, s3, ":division"),
            (str_store_string, s2, "@{!}{s2}, {s3}"),
        (try_end),
	(try_end),
    (try_begin),
        (eq, ":count_selected", ":count_possible"),
        (str_store_string, s2, "@Everyone"),
    (try_end),
    (try_begin),
        (gt, ":count_selected", 0),
        (display_message, "@{!}{s2}, {s1}!", 0xFFDDDD66),
    (try_end),
    (str_clear, s2),
    (str_clear, s3),
   ]),

  # script_order_weapon_type_switch
  # Input: Order Type ; Team_No  
  # Output: Nothing
  # On key depression, try to switch division to appropriate weapon
 ("order_weapon_type_switch", [ 
    (store_script_param_1, ":ordertype"),
	(store_script_param_2, ":ordered_team"),
		
	(call_script, "script_order_set_team_slot", ":ordertype", ":ordered_team"),

	(try_for_agents, ":agent"),
        (agent_is_alive, ":agent"),
        (agent_is_human, ":agent"),
        (agent_is_non_player, ":agent"),
        (agent_get_team, ":team", ":agent"),
        (eq, ":team", ":ordered_team"), 
        (agent_get_division, ":class", ":agent"),
        (class_is_listening_order, ":team", ":class"), #Is the agent's class selected?
		(store_add, ":slot", slot_team_d0_order_shield, ":class"),
		(team_get_slot, ":shield_order", ":team", ":slot"),
        (assign, ":possible_shield", 0), #Added to force shield
		(assign, ":wielded_polearm", 0), #Added for polearm/shield combo
		(assign, ":end", ek_head),
		(try_for_range, ":i", ek_item_0, ":end"),
			(agent_get_item_slot, ":item", ":agent", ":i"),
			(gt, ":item", 0),
			(item_get_type, ":weapontype", ":item"),
			(try_begin),
				(eq, ":ordertype", ranged),
				(this_or_next|eq, ":weapontype", itp_type_bow),
				(this_or_next|eq, ":weapontype", itp_type_crossbow),
				(eq, ":weapontype", itp_type_thrown),
				(agent_set_wielded_item, ":agent", ":item"),
				(assign, ":end", ek_item_0),#loop breaker
			(else_try),
				(eq, ":ordertype", onehand),
				(eq, ":weapontype", itp_type_one_handed_wpn),
				(agent_set_wielded_item, ":agent", ":item"),
				(assign, ":end", ek_item_0),#loop breaker
			(else_try),  #Check shield orders for 2Handers/Polearms?
				(eq, ":ordertype", twohands),
				(eq, ":weapontype", itp_type_two_handed_wpn),
				(agent_set_wielded_item, ":agent", ":item"),
				(assign, ":end", ek_item_0),#loop breaker
				(agent_get_wielded_item, ":shield", ":agent", 1),
				(gt, ":shield", 0), #Has a shield wielded, after equipping 2hander/polearm
				(agent_unequip_item, ":agent", ":shield"), #Wield weapon with 2 hands,
				(agent_equip_item, ":agent", ":shield"), #Moves shield to back
			(else_try),
				(eq, ":ordertype", polearm),
				(try_begin),
					(neq, ":shield_order", 1), #Not ordered to use shields
					(eq, ":weapontype", itp_type_polearm),
					(agent_set_wielded_item, ":agent", ":item"),
					(assign, ":end", ek_item_0),#loop breaker
				(else_try),
					(eq, ":shield_order", 1), #Ordered to use shields
					(try_begin),
						(eq, ":wielded_polearm", 0),
						(eq, ":weapontype", itp_type_polearm),
						(agent_set_wielded_item, ":agent", ":item"),
						(assign, ":wielded_polearm", ":item"),
					(try_end),
					(try_begin),
						(eq, ":weapontype", itp_type_shield),
						(eq, ":possible_shield", 0),
						(assign, ":possible_shield", ":item"),
					(try_end),
					(gt, ":wielded_polearm", 0),
					(gt, ":possible_shield", 0),
					(agent_set_wielded_item, ":agent", ":possible_shield"),
					(assign, ":end", ek_item_0),#loop breaker
				(try_end),
			(else_try),
				(eq, ":ordertype", shield), #Ordered to use shields
				(agent_get_wielded_item, ":shield", ":agent", 1),
				(try_begin),
					(gt, ":shield", 0),
					(assign, ":end", ek_item_0),#loop breaker
				(else_try),
					(le, ":shield", 0), #No shield currently wielded
					(eq, ":weapontype", itp_type_shield),
					(assign, ":possible_shield", ":item"), #Track the shield. At end check that shield was actually equipped, force shields
					(agent_set_wielded_item, ":agent", ":item"), #Moves shield from back to hand
					(assign, ":end", ek_item_0),#loop breaker
				(try_end),
			(else_try),
				(eq, ":ordertype", noshield), #Ordered to NOT use shields
				(agent_get_wielded_item, ":shield", ":agent", 1),
				(gt, ":shield", 0), #Has a shield wielded
				(item_get_type, ":shield_type", ":shield"),
				(eq, ":shield_type", itp_type_shield),
				(agent_unequip_item, ":agent", ":shield"),
				(agent_equip_item, ":agent", ":shield"), #Moves shield to back
				(assign, ":end", ek_item_0),#loop breaker
			(try_end), #Order Type
		(try_end), #Item Loop
		(gt, ":possible_shield", 0), #A shield equipped and ordered to use shields
		(agent_get_wielded_item, ":shield", ":agent", 1),
		(le, ":shield", 0), #But, no shield currently wielded
		(assign, ":end", 2),
		(try_for_range, ":i", 0, ":end"),
			(agent_get_wielded_item, ":wielded", ":agent", 0),
			(gt, ":wielded", 0),
			(agent_unequip_item, ":agent", ":wielded"),
            (agent_equip_item, ":agent", ":wielded"), #Sheathes weapon
			(agent_set_wielded_item, ":agent", ":possible_shield"),
			(try_begin),
			    (eq, ":i", 0), #First time only
				(gt, ":wielded_polearm", 0),
			    (agent_set_wielded_item, ":agent", ":wielded_polearm"),
			(try_end),
			(agent_get_wielded_item, ":shield", ":agent", 1),
			(gt, ":shield", 0), #If shield equipped
			(assign, ":end", 0), #Then Break Loop, don't try again
		(try_end),
    (try_end), #Agent Loop
    ]),

  # script_cf_order_active_check
  # Input: Team Slot for Order division #0 (ex. slot_team_d0_order_skirmish)
  # Output: Nothing
  # Check for an active Special Order, in lieu of global variables
 ("cf_order_active_check", [ 
    (store_script_param_1, ":order_slot"),
    (assign, ":active", 0),
	(assign, ":end", 4),
	(store_add, ":end2", ":order_slot", 9),
    (try_for_range, ":team", 0, ":end"),
        (try_for_range, ":i", ":order_slot", ":end2"),
		    (team_slot_ge, ":team", ":i", 1),
		    (assign, ":active", 1),
			(assign, ":end", 0),
			(assign, ":end2", ":order_slot"),
		(try_end),
    (try_end),
	(try_begin),
	    (eq, ":order_slot", slot_team_d0_order_sp_brace),
		(neq, ":active", 1),
		(ge, "$fplayer_agent_no", 0), #For game start
		(agent_slot_eq, "$fplayer_agent_no", slot_agent_player_braced, 1),
		(assign, ":active", 1),
	(try_end),
    (eq, ":active", 1),
    ]),    

  # script_order_end_active_order
  # Input: Team_No
  # Output: Nothing
  # Check for an active Special order, and end it appropriately
 ("order_end_active_order", [ 
    (store_script_param_1, ":ordered_team"),
	
	(try_for_range, ":class", 0, 9),
	    (class_is_listening_order, ":ordered_team", ":class"),
		(store_add, ":slot", slot_team_d0_order_skirmish, ":class"),
		(try_begin),
		    (team_slot_ge, ":ordered_team", ":slot", 1), #Skirmish
			(call_script, "script_order_skirmish_begin_end", end, ":ordered_team"),
			(eq, ":ordered_team", "$fplayer_team_no"),
			(call_script, "script_order_set_display_text", end + 8),
		(else_try),
		    (val_add, ":slot", 9),
			(team_slot_ge, ":ordered_team", ":slot", 1), #Volley
			(call_script, "script_order_volley_begin_end", end, ":ordered_team"),
			(eq, ":ordered_team", "$fplayer_team_no"),
			(call_script, "script_order_set_display_text", end + 10),
		(else_try),
		    (val_add, ":slot", 9),
			(team_slot_ge, ":ordered_team", ":slot", 1), #Spear Brace
			(call_script, "script_order_sp_brace_begin_end", end, ":ordered_team"),	
			(eq, ":ordered_team", "$fplayer_team_no"),		
			(call_script, "script_order_set_display_text", end + 12),			
		(try_end),			
	(try_end),
  ]), 
	
  # script_order_sp_brace_begin_end
  # Input: 1 - Begin 0 - End ; Param2: Team_No
  # Output: Nothing
  # If ending, clear scripted behavior. If beginning, switch on
 ("order_sp_brace_begin_end", [ 
    (store_script_param_1, ":begin_end"),
	(store_script_param_2, ":ordered_team"),
	
	(store_add, ":spear_order_type", ":begin_end", 12),	  
	(call_script, "script_order_set_team_slot", ":spear_order_type", ":ordered_team"),	  	
	
    (try_begin),
        (eq, ":begin_end", end),		
	    (try_for_agents, ":agent"),
	        (agent_is_alive, ":agent"),
            (agent_is_human, ":agent"),
            (agent_is_non_player, ":agent"),
            (agent_get_team, ":team", ":agent"),
            (eq, ":team", ":ordered_team"),
            (agent_get_division, ":class", ":agent"),
		    (class_is_listening_order, ":team", ":class"), #Is the agent's division selected?
			(agent_slot_ge, ":agent", slot_agent_spearwall, 1),
			(agent_set_slot, ":agent", slot_agent_spearwall, 0),
			(agent_get_animation, ":anim", ":agent"), ## ADDED
			(this_or_next|eq, ":anim", "anim_spearwall_bracing"), ## ADDED
			(eq, ":anim", "anim_spearwall_bracing_low"), ## ADDED
			(agent_set_animation, ":agent", "anim_spearwall_bracing_recover"), ## ADDED
			(agent_clear_scripted_mode, ":agent"),
	    (try_end), #Agent loop
		
		(try_begin), ##tell them to wield shields again
			(neq, ":ordered_team", "$fplayer_team_no"),
			(call_script, "script_order_weapon_type_switch", shield, ":ordered_team"),
			(call_script, "script_order_set_team_slot", free, ":ordered_team"),
		(try_end),
		
		(set_show_messages, 0),
		(team_get_leader, ":team_leader", ":ordered_team"),
		(try_for_range, ":class", 0, 9), #resume previous formation if present
			(class_is_listening_order, ":ordered_team", ":class"),
			(store_add, ":slot", slot_team_d0_formation_to_resume, ":class"),
			(neg|team_slot_eq, ":ordered_team", ":slot", formation_none),
			(team_get_slot, ":formation", ":ordered_team", ":slot"),
			(team_set_slot, ":ordered_team", ":slot", formation_none), #clear

			#reform it
			(store_add, ":slot", slot_team_d0_formation, ":class"),
			(team_set_slot, ":ordered_team", ":slot", ":formation"),
			(store_add, ":slot", slot_team_d0_formation_space, ":class"),
			(team_get_slot, ":spacing", ":ordered_team", ":slot"),
			(call_script, "script_battlegroup_get_position", pos1, ":ordered_team", ":class"),
			(try_begin),
				(call_script, "script_team_get_position_of_enemies", Enemy_Team_Pos, ":ordered_team", grc_everyone),
				(neq, reg0, 0),	#more than 0 enemies still alive?
				(call_script, "script_point_y_toward_position", pos1, Enemy_Team_Pos),
			(try_end),
			(copy_position, pos61, pos1),
			(call_script, "script_form_infantry", ":ordered_team", ":class", ":team_leader", ":spacing", ":formation"),
			(store_add, ":slot", slot_team_d0_move_order, ":class"),
			(team_set_slot, ":ordered_team", ":slot", mordr_hold),
			(team_get_movement_order, reg0, ":ordered_team", ":class"),
			(try_begin),
				(neq, reg0, mordr_hold),
				(team_give_order, ":ordered_team", ":class", mordr_hold),
			(try_end),
			(call_script, "script_set_formation_destination", ":ordered_team", ":class", pos61),
		(try_end),
		(set_show_messages, 1),
	(else_try),
	    (eq, ":begin_end", begin), 
	    (call_script, "script_order_weapon_type_switch", noshield, ":ordered_team"), #until there is a shield-less version of the animation
		(try_for_range, ":class", 0, 9), #disable formation if present and mark to resume
			(class_is_listening_order, ":ordered_team", ":class"),
			(store_add, ":slot", slot_team_d0_formation, ":class"),
			(neg|team_slot_eq, ":ordered_team", ":slot", formation_none),
			(team_get_slot, ":formation", ":ordered_team", ":slot"),
			(store_add, ":slot", slot_team_d0_formation_to_resume, ":class"),
			(team_set_slot, ":ordered_team", ":slot", ":formation"),
			(call_script, "script_formation_end", ":ordered_team", ":class"), 
		(try_end),
		(neq, ":ordered_team", "$fplayer_team_no"),
		(store_add, ":slot", slot_team_d0_move_order, grc_infantry),
		(team_set_slot, ":ordered_team", ":slot", mordr_hold),
		(team_get_movement_order, reg0, ":ordered_team", grc_infantry),
		(try_begin),
			(neq, reg0, mordr_hold),
			(team_give_order, ":ordered_team", grc_infantry, mordr_hold),
		(try_end),
		(call_script, "script_set_formation_destination", ":ordered_team", grc_infantry, pos2),
    (try_end),	 
	]),	
	
  # script_order_volley_begin_end
  # Input: 1 - Begin volley; 0 - End volley ; Param2: Team_No
  # Output: Nothing
  # If ending, clear scripted behavior. If beginning, switch volley on
 ("order_volley_begin_end", [ 
    (store_script_param_1, ":begin_end"),
	(store_script_param_2, ":ordered_team"),
	
	(store_add, ":volley_order_type", ":begin_end", 10),	  
	(call_script, "script_order_set_team_slot", ":volley_order_type", ":ordered_team"),	  
	 
    (try_begin),
        (eq, ":begin_end", end),		
	    (try_for_agents, ":agent"),
	        (agent_is_alive, ":agent"),
            (agent_is_human, ":agent"),
            (agent_is_non_player, ":agent"),
            (agent_get_team, ":team", ":agent"),
            (eq, ":team", ":ordered_team"),
            (agent_get_division, ":class", ":agent"),
		    (class_is_listening_order, ":team", ":class"), #Is the agent's division selected?
			(agent_slot_ge, ":agent", slot_agent_volley_fire, 1),
			(agent_set_slot, ":agent", slot_agent_volley_fire, 0),
			(agent_set_attack_action, ":agent", 0, 0), #Release (if holding)
	    (try_end), #Agent loop
    (else_try), 	 
		(eq, ":begin_end", begin),
		(call_script, "script_order_skirmish_begin_end", end, ":ordered_team"), #Ensure that Skirmish and Volley aren't both active
		(try_for_agents, ":agent"),
			(agent_is_non_player, ":agent"),
			(agent_is_alive, ":agent"),
			(agent_is_human, ":agent"),
			(agent_slot_eq, ":agent", slot_agent_is_running_away, 0),
			(agent_get_team, ":team", ":agent"),
			(eq, ":team", ":ordered_team"),
			(agent_get_division, ":division", ":agent"),
			(class_is_listening_order, ":team", ":division"),
			(agent_get_horse, ":horse", ":agent"),
			(le, ":horse", 0), #Not Mounted
			
			(assign, ":volley_wpn_type", -1),
			(try_begin),
				(team_get_movement_order, ":mordr", ":team", ":division"),
				(this_or_next|eq, ":mordr", mordr_hold),
				(eq, ":mordr", mordr_stand_ground),
				
				(agent_get_wielded_item, ":wielded", ":agent", 0),
				(ge, ":wielded", 0),
				(item_get_type, ":type", ":wielded"),
				(try_begin),
					(this_or_next|eq, ":type", itp_type_bow),
					(eq, ":type", itp_type_crossbow),
					(assign, ":volley_wpn_type", ":type"),
				(else_try),
					(assign, ":end", ek_head),
					(try_for_range, ":i_slot", ek_item_0, ":end"),
						(agent_get_item_slot, ":item", ":agent", ":i_slot"),
						(ge, ":item", 0),
						(item_get_type, ":type", ":item"),
						(this_or_next|eq, ":type", itp_type_bow),
						(eq, ":type", itp_type_crossbow),
						(agent_set_wielded_item, ":agent", ":item"),
						(assign, ":volley_wpn_type", ":type"),
						(assign, ":end", ek_item_0),
					(try_end),
				(try_end),
			(try_end),
			(agent_set_slot, ":agent", slot_agent_volley_fire, ":volley_wpn_type"),
		(try_end), #Agent loop
    (try_end),	 
	]),
	
  # script_order_skirmish_begin_end
  # Input: 1 - Begin skirmish; 0 - End skirmish ; Param2: Team_No
  # Output: Nothing
  # On key depression, determine if beginning or ending skirmish
  # If ending, stop any retreating. If beginning, call order_skirmish_skirmish
 ("order_skirmish_begin_end", [ 
    (store_script_param_1, ":begin_end"),
	(store_script_param_2, ":ordered_team"),

	(store_add, ":skirmish_order_type", ":begin_end", 8),	  
	(call_script, "script_order_set_team_slot", ":skirmish_order_type", ":ordered_team"),	  
	 
    (try_begin),
        (eq, ":begin_end", end),		
	    (try_for_agents, ":agent"),
	        (agent_is_alive, ":agent"),
            (agent_is_human, ":agent"),
            (agent_is_non_player, ":agent"),
            (agent_get_team, ":team", ":agent"),
            (eq, ":team", ":ordered_team"),
            (agent_get_division, ":class", ":agent"),
		    (class_is_listening_order, ":team", ":class"), #Is the agent's division selected?
            (try_begin),
                (agent_slot_eq, ":agent", slot_agent_is_running_away, 0), #Is not routing or ordered to retreat		 
		        (agent_stop_running_away, ":agent"),
            (try_end),
	    (try_end), #Agent loop
    (else_try), 	 
		(eq, ":begin_end", begin),
		(call_script, "script_order_volley_begin_end", end, ":ordered_team"), #Ensure that Skirmish and Volley aren't both active
	    (call_script, "script_order_skirmish_skirmish"),
    (try_end),	 
	]),

  # script_order_skirmish_skirmish
  # Input: Nothing 
  # Output: Nothing
  # Cycle through agents, checking and maintaining distance
 ("order_skirmish_skirmish", [ 
	(set_fixed_point_multiplier, 1),	 
    (try_for_agents, ":agent"),
        (agent_is_alive, ":agent"),
        (agent_is_human, ":agent"),
        (agent_is_non_player, ":agent"),
        (agent_get_team, ":team", ":agent"),
        #(eq, ":team", "$fplayer_team_no"), #On Player's side?
		(agent_slot_eq, ":agent", slot_agent_is_running_away, 0), #Is not routing or ordered to retreat
		(agent_get_division, ":class", ":agent"),
		(store_add, ":slot", slot_team_d0_order_skirmish, ":class"),
		(team_slot_eq, ":team", ":slot", 1), #Division is skirmishing
		 
		(agent_get_position, pos1, ":agent"),   
		(position_get_x, ":agent_x", pos1),
		(position_get_y, ":agent_y", pos1),
		(store_sub, ":dist_right", ":agent_x", "$g_bound_right"),
		(store_sub, ":dist_top", ":agent_y", "$g_bound_top"),
		(store_sub, ":dist_left", "$g_bound_left", ":agent_x"),
		(store_sub, ":dist_bottom", "$g_bound_bottom", ":agent_y"),
		(agent_get_ammo, ":ammo", ":agent"),             
        (try_begin), #If agent is too close to edge of map, stop skirmishing. Will resume when back into map             
            (this_or_next|le, ":ammo", 0), #Stop skirmishing and resume orders if out of ammo
		    (this_or_next|le, ":dist_right", 25),  #Limits accidental routing, of cav in particular
			(this_or_next|le, ":dist_top", 25),
			(this_or_next|le, ":dist_left", 25),
			(le, ":dist_bottom", 25),
			(agent_stop_running_away, ":agent"),
			(agent_force_rethink, ":agent"), ###TEST FOR BOUNDARY BUGFIX
		(else_try),
	        (call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team", pos1), # Find distance of nearest 3 enemies
            (assign, ":avg_dist", reg0),
	        (assign, ":closest_dist", reg1),
	        (try_begin),
		        (this_or_next|lt, ":avg_dist", skirmish_min_distance),
			    (lt, ":closest_dist", 700), #If enemy group is getting near or an enemy is on top of agent
			    (agent_start_running_away, ":agent"),		 
		    (else_try),
		        (ge, ":avg_dist", skirmish_max_distance), #If distance from enemy is (too) large, resume previous order
                (agent_stop_running_away, ":agent"),		 
		    (try_end), #Distance to enemy
		(try_end), #Distance from edge
	(try_end), #Agent loop
    ]),
## Caba'drin Orders End

#Shield Bash Script - Xenoargh (Blood & Steel); edited/reworked per comments in the thread, etc, by Caba
 ("cf_shield_bash",
   [  
	(agent_get_animation, ":anim", "$fplayer_agent_no", 0),
	(neq, ":anim", "anim_shield_bash"),
	(agent_get_horse, ":horse", "$fplayer_agent_no"),
	(eq, ":horse", -1),
	(agent_get_defend_action, ":action", "$fplayer_agent_no"),
	(eq, ":action", 2), #Blocking.
	(agent_get_wielded_item, ":shield_item", "$fplayer_agent_no", 1),
	(gt, ":shield_item", itm_no_item),
	(item_get_type, ":type", ":shield_item"),
	(eq, ":type", itp_type_shield),
	(item_get_slot, ":shield_width", ":shield_item", slot_item_length),
	(ge, ":shield_width", 50), ##FLORIS, balance as needed

	#(set_fixed_point_multiplier, 100),
	##Fail above this point--don't allow fail after, so the failure/re-arm goes with the firing of the animation
	(agent_set_animation, "$fplayer_agent_no","anim_shield_bash"),
	(agent_get_position, pos63, "$fplayer_agent_no"),
	(position_move_y, pos63, 75),#75 cm directly ahead, so it's not a cuboid space around player center
	(agent_get_troop_id, ":id", "$fplayer_agent_no"),
	(troop_get_type, ":type", ":id"),
	(try_begin),
		(eq, ":type", tf_male),
		(agent_play_sound, "$fplayer_agent_no", "snd_man_yell"),
	(else_try),
		(agent_play_sound, "$fplayer_agent_no", "snd_man_yell"),		
	(try_end),

	(assign, ":victim", -1),
	(assign, ":closest_dist", 100),
	(try_for_agents,":agent"),
		(neq, ":agent", "$fplayer_agent_no"),
		(neg|agent_is_ally,":agent"),#don't bash allies
		(agent_is_human, ":agent"),#stop if not human			
		(agent_is_alive,":agent"),	
		(agent_get_horse, ":horse", ":agent"),
		(eq, ":horse", -1),		
		
		(agent_get_position,pos62,":agent"),
		(neg|position_is_behind_position, pos62, pos63),
		(get_distance_between_positions,":dist",pos63,pos62),		
		(le, ":dist", ":closest_dist"),				
		(assign, ":victim", ":agent"),
		(assign, ":closest_dist", ":dist"),
	(try_end),
	(try_begin),
		(ge, ":victim", 0),
		(agent_play_sound, "$fplayer_agent_no", "snd_wooden_hit_low_armor_high_damage"),				
		#(set_fixed_point_multiplier, 100),
		#(position_move_y,pos62,-25),			
		#(agent_set_position, ":victim", pos62),
		(agent_set_animation, ":victim", "anim_shield_strike"),		
	(try_end),
   ]),  
#End Shield Bash Script - Xenoargh


##Custom Camera Begin
 ("cust_cam_init_death_cam", [
    (store_script_param_1, ":mode"),

	(try_begin), #really initialize
		(neq, "$cam_free", 1),
		(assign, "$cam_free", 1),
		(mission_cam_set_mode, 1),
		(call_script, "script_cust_cam_cycle_forwards"), #So, on Follow, it doesn't begin with the player's dead body or have a script error
	(try_end),	
	
	(try_begin),
	    (eq, ":mode", cam_mode_free),
		(agent_get_position, pos1, "$fplayer_agent_no"),
		(position_get_x, ":pos_x", pos1),
		(position_get_y, ":pos_y", pos1),
		(init_position, cam_position),
		(position_set_x, cam_position, ":pos_x"),
		(position_set_y, cam_position, ":pos_y"),
		(position_set_z_to_ground_level, cam_position),
		(position_move_z, cam_position, 250),
		(mission_cam_set_mode, 1, 0, 0),
		(mission_cam_set_position, cam_position),
		(assign, "$g_camera_rotx", 0),
	(else_try),
		(eq, ":mode", cam_mode_follow),
		(assign, "$g_camera_z", 300),
		(assign, "$g_camera_y", -1000),
		(assign, "$g_camera_x", 0),
    (try_end),   
	(assign, "$cam_mode", ":mode"),
   ]),

  # Modified MartinF's code for DeathCam
  # script_cust_cam_cycle_forwards
  # Output: New $cust_cam_current_agent
  # Used to cycle forwards through valid agents
 ("cust_cam_cycle_forwards", [
	(assign, ":agent_moved", 0),
	(assign, ":first_agent", -1),
	(agent_get_team, ":prev_team", "$cam_current_agent"),
	(try_for_agents, ":agent_no"),
	    (neq, ":agent_moved", 1),
		(agent_is_human, ":agent_no"),
		(agent_is_alive, ":agent_no"),
		(agent_get_team, ":cur_team", ":agent_no"),
		(agent_get_troop_id, ":troop_id", ":agent_no"),
		(this_or_next|troop_is_hero, ":troop_id"),
		(neg|key_is_down, key_left_shift),
		(this_or_next|eq, ":cur_team", ":prev_team"),
		(neg|key_is_down, key_left_control),
		(this_or_next|neq, ":cur_team", ":prev_team"),
		(neg|key_is_down, key_left_alt),             
		(this_or_next|eq, "$cam_free", 1),         
		(eq, ":cur_team", "$fplayer_team_no"),
		(try_begin),
			(lt, ":first_agent", 0),                         # Find the 1st agent alive and (1 team or free mod)
			(assign, ":first_agent", ":agent_no"),
		(try_end),
		(gt, ":agent_no", "$cam_current_agent"),            # Find next agent  alive and (1 team or free mod)
		(assign, "$cam_current_agent", ":agent_no"),
		(assign, ":agent_moved", 1),
	(try_end),
	(try_begin),
	    (eq, ":agent_moved", 0),                            # Next Agent not found, but 1st agent found, then the next is the first one
		(neq, ":first_agent", -1),
		(assign, "$cam_current_agent", ":first_agent"),
		(assign, ":agent_moved", 1),       
	(else_try),
		(eq, ":agent_moved", 0),
		(eq, ":first_agent", -1),
		(display_message, "@No Troops Left."),
	(try_end),
	(try_begin),
		(eq, ":agent_moved", 1),                            # there is next one
		(try_begin),
			(agent_is_alive, "$fplayer_agent_no"),             # if player is still alive, push to mode 1
			(assign, "$cam_mode", 1),
			(mission_cam_set_mode, "$cam_mode"),
		(try_end),
		(str_store_agent_name, 1, "$cam_current_agent"),
	(try_end),
	]),
	   
	# script_cust_cam_cycle_backwards
	# Output: New $cust_cam_current_agent
	# Used to cycle backwards through valid agents
 ("cust_cam_cycle_backwards", [
    (assign, ":new_agent", -1),
	(assign, ":last_agent", -1),
	(agent_get_team, ":prev_team", "$cam_current_agent"),     
	(try_for_agents, ":agent_no"),
		(agent_is_human, ":agent_no"),
		(agent_is_alive, ":agent_no"),
		(agent_get_team, ":cur_team", ":agent_no"),
		(agent_get_troop_id, ":troop_id", ":agent_no"),
		(this_or_next|troop_is_hero, ":troop_id"),
		(neg|key_is_down, key_left_shift),
		(this_or_next|eq, ":cur_team", ":prev_team"),
		(neg|key_is_down, key_left_control),
		(this_or_next|neq, ":cur_team", ":prev_team"),
		(neg|key_is_down, key_left_alt),
		(this_or_next|eq, "$cam_free", 1),   
		(eq, ":cur_team", "$fplayer_team_no"),
		(assign, ":last_agent", ":agent_no"),          # Ok, the last
		(lt, ":agent_no", "$cam_current_agent"),
		(assign, ":new_agent", ":agent_no"),           # prev agent   
	(try_end),
	(try_begin),
		(eq, ":new_agent", -1),
		(neq, ":last_agent", -1),
		(assign, ":new_agent", ":last_agent"),               
	(else_try),
		(eq, ":new_agent", -1),
		(eq, ":last_agent", -1),
		(display_message, "@No Troops Left."),
	(try_end),
	(try_begin),
		(neq, ":new_agent", -1),                       # There is prev agent
		(assign, "$cam_current_agent", ":new_agent"),
		(try_begin),
			(agent_is_alive, "$fplayer_agent_no"),
			(assign, "$cam_mode", 1),
			(mission_cam_set_mode, "$cam_mode"),
		(try_end),
		(str_store_agent_name, 1, "$cam_current_agent"),
	(try_end), 
  ]),
##Custom Camera End

#-- Dunde's Key Config BEGIN
 ("update_key_config_buttons",
   [(try_for_range, ":no_key", slot_keys_begin, slot_keys_begin+number_of_keys),
       #(store_add, ":off", ":no_key", number_of_keys),
       (store_add, ":off_overlay",  ":no_key", number_of_keys),
       (troop_get_slot, ":ovr", key_config_data, ":off_overlay"), 
       (troop_get_slot, ":key", key_config_data, ":no_key"),
       (assign, ":found", 0), (assign, ":upper_limit", number_of_all_keys),
       (try_for_range, ":no", 0, ":upper_limit"),
          (store_add, ":off_all_keys", ":no", slot_key_defs_begin),
          (troop_slot_eq, key_config_data,  ":off_all_keys", ":key"),
          (store_add, ":off_strings", ":no", key_label_begin),          
          (overlay_set_text, ":ovr", ":off_strings", 0),
          (overlay_set_color, ":ovr", 0x0),
          (assign, ":found", ":no"),
          (assign, ":upper_limit", ":no"),
       (try_end),
       (try_begin),
          (neq, ":found", 0),
       (else_try),
          (eq, ":key", 0xff),
          (overlay_set_text, ":ovr", "@Disabled"),
          (overlay_set_color, ":ovr", 0x800000),
       (else_try),
          (overlay_set_text, ":ovr", "@Undefined!"),
          (overlay_set_color, ":ovr", 0xFF0000),       
       (try_end),          
    (try_end), 
   ]),
   
 ("init_key_config", set_key_config()),              # Slots Initilizations (Key Defs & Default Values) 
 ("set_config_slot_key_config", read_key_config()),  # Global Variables -> Slots
 ("set_global_var_key_config", write_key_config()),  # Slots            -> Global Variables

 ("reset_to_default_keys",                           # Default Slots    -> Working Slots
   [(try_for_range, ":no", 0, number_of_keys),
        (store_add, ":off", ":no", slot_default_keys_begin),
        (troop_get_slot, ":key", key_config_data, ":off"),
        (val_add, ":off", number_of_keys),
        (troop_set_slot, key_config_data, ":off", ":key"),
    (try_end), 
   ]),
  
 ("init_all_keys",
   [(call_script, "script_init_key_config"),
    (call_script, "script_reset_to_default_keys"),
    (call_script, "script_set_global_var_key_config"), 
    ]), 
#-- Dunde's Key Config END
   
 ("str_store_key_name", 
    #Be sure key_config_data is populated with the strings info 
	#with script_init_key_config before calling
   [
    (store_script_param_1, ":str_reg"), 
	(store_script_param_2, ":key"),
    (assign, ":end", number_of_all_keys),
    (try_for_range, ":i", 0, ":end"),
      (store_add, ":key_offset", slot_key_defs_begin, ":i"),
      (troop_slot_eq, key_config_data,  ":key_offset", ":key"),
      (store_add, ":strings_offset", key_label_begin, ":i"),          
      (assign, ":end", 0),
    (try_end),
    (try_begin),
      (eq, ":end", 0),
      (neq, ":key", 0xff),
      (str_store_string, ":str_reg", ":strings_offset"),
	(else_try),
	  (str_store_string, ":str_reg", "str_blank_string"),
    (try_end),
   ]),

 ("init_item_score", set_item_score()),
 
  #script_prebattle_split_troop_divisions
  #Input: nothing
  #Output: nothing (agent divisions changed, slot set)
  #Takes % value set in presentation "prebattle_custom_divisions" and changes appropriate number  
  #of agents' divisions, allowing the same troop type to be split into 2 divisions
  #Called from split division triggers in prebattle_deployment_triggers
 ("prebattle_split_troop_divisions",
   [
    #Loop through all troops in stack, clear counters
    (party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
	(try_for_range, ":i", 0, ":num_of_stacks"),
		(party_stack_get_troop_id, ":troop_id", "p_main_party", ":i"),
		(neq, ":troop_id", "trp_player"),
		(neg|troop_is_hero, ":troop_id"),
		(troop_set_slot, ":troop_id", slot_troop_prebattle_alt_division_amount, 0),
	(try_end),
        
    #Counting Loop
    (try_for_agents, ":agent"), 
		(agent_is_alive, ":agent"),
	    (agent_is_human, ":agent"),
	    (agent_is_non_player, ":agent"),
		(agent_get_party_id, ":party", ":agent"),
		(eq, ":party", "p_main_party"),
		(agent_slot_eq, ":agent", slot_agent_alt_div_check, 0),	#was slot_agent_is_not_reinforcement, but	
		(agent_get_troop_id, ":troop_id", ":agent"),      #had possible conflict with siege_move_arcers_to_archer_positions for defending class grc_archer agents
		(neg|troop_is_hero, ":troop_id"),
		(troop_slot_ge,  ":troop_id", slot_troop_prebattle_alt_division_percent, 1), #Has a split active
		(troop_get_slot, ":alt_division", ":troop_id", slot_troop_prebattle_alt_division),
		(is_between, ":alt_division", 0, 9), #Valid division
		(troop_get_class, ":class", ":troop_id"),
		(neq, ":class", ":alt_division"), #So there is an actual change to make
		
		(troop_get_slot, ":amount", ":troop_id", slot_troop_prebattle_alt_division_amount), #Count
		(val_add, ":amount", 1),
		(troop_set_slot, ":troop_id", slot_troop_prebattle_alt_division_amount, ":amount"),
    (try_end),  
	
	#Loop through all troops in stack, take "amount" and "percent" and convert to # to change
	(try_for_range, ":i", 0, ":num_of_stacks"),
		(party_stack_get_troop_id, ":troop_id", "p_main_party", ":i"),
		(neq, ":troop_id", "trp_player"),
		(neg|troop_is_hero, ":troop_id"),
		(troop_get_slot, ":number_spawned", ":troop_id", slot_troop_prebattle_alt_division_amount),
		(gt, ":number_spawned", 0), #If counted, must have split active
		(troop_get_slot, ":target_percent", ":troop_id", slot_troop_prebattle_alt_division_percent),		
		
		(store_mul, ":num_to_change", ":number_spawned", ":target_percent"),
		(val_div, ":num_to_change", 100),
		
		(troop_set_slot, ":troop_id", slot_troop_prebattle_alt_division_amount, ":num_to_change"),
	(try_end),	
	
	#(assign, reg1, 0),#debug
	#Actually Change Division Loop
	(try_for_agents, ":agent"), 
		(agent_is_alive, ":agent"),
	    (agent_is_human, ":agent"),
	    (agent_is_non_player, ":agent"),
		(agent_get_party_id, ":party", ":agent"),
		(eq, ":party", "p_main_party"), 
		(agent_slot_eq, ":agent", slot_agent_alt_div_check, 0),	
		(agent_set_slot, ":agent", slot_agent_alt_div_check, 1), 
		
		(agent_get_troop_id, ":troop_id", ":agent"),
	    (troop_slot_ge, ":troop_id", slot_troop_prebattle_alt_division_amount, 1),
	
	    (troop_get_slot, ":alt_division", ":troop_id", slot_troop_prebattle_alt_division),
	    (agent_set_division, ":agent", ":alt_division"),
		(agent_set_slot, ":agent", slot_agent_new_division, ":alt_division"), #so it can be maintained
	
	    (troop_get_slot, ":amount", ":troop_id", slot_troop_prebattle_alt_division_amount),
	    (val_sub, ":amount", 1),
	    (troop_set_slot, ":troop_id", slot_troop_prebattle_alt_division_amount, ":amount"),
		
		#(val_add, reg1, 1), #debug
    (try_end),  
	#(assign, reg0, ":num_to_change"),#debug
	#(display_message, "@{reg0} to change; {reg1} changed"),#debug
   ]),
 
  #script_prebattle_agent_fix_division
  #Input: agent_id
  #Output: nothing (agent divisions changed, slot set) 
  #To fix AI troop divisions from the engine applying player's party divisions on all agents
  #This is called after agent_reassign_team, so can safely assume correct team is set
 ("prebattle_agent_fix_division",
   [
    (store_script_param_1, ":agent"),	
	(agent_set_slot, ":agent", slot_agent_new_division, -1),	
	(get_player_agent_no, ":player"),	#after_mission_start triggers are called after spawn, so globals can't be used yet
	
	(try_begin),
	    (ge, ":player", 0),
		(agent_is_human, ":agent"),
		(agent_get_team, ":player_team", ":player"),
		(agent_get_team, ":team", ":agent"),
		(this_or_next|main_hero_fallen),
		(neq, ":team", ":player_team"),
		(agent_get_troop_id, ":troop", ":agent"),
		(try_begin),
			(troop_is_guarantee_horse, ":troop"),
			(assign, ":target_division", grc_cavalry),
		(else_try),
			(troop_is_guarantee_ranged, ":troop"),
			(assign, ":target_division", grc_archers),
		(else_try),
			(assign, ":target_division", grc_infantry),		
		(try_end),
		(agent_get_division, ":division", ":agent"),
		(neq, ":division", ":target_division"),
		(agent_set_division, ":agent", ":target_division"),
		(agent_set_slot, ":agent", slot_agent_new_division, ":target_division"),
	(try_end),
   ]),

 ("weather_change_rain_or_snow",
   [
    (party_get_current_terrain, ":terrain_type", "p_main_party"),
    (try_begin),
      (this_or_next|eq, ":terrain_type", rt_snow),
      (eq, ":terrain_type", rt_snow_forest),
      (assign, ":rain_type", 2),
    (else_try),
      (assign, ":rain_type", 1),
    (try_end),
    
    (assign, reg0, -1),
    (assign, reg1, -1),
    (store_random_in_range, ":rand_rain", 1, 100),
    (try_begin),
	  (lt, ":rand_rain", 50),
      (get_global_cloud_amount, ":clouds"),
      (ge, ":clouds", 40),
      (store_random_in_range, ":rand_rain_2", 1, 100),
      (store_mul, ":rand_strength", ":rand_rain", ":rand_rain_2"),
      (val_div, ":rand_strength", 100),
      (gt, ":rand_strength", 0),
      (set_rain, ":rain_type", ":rand_strength"),
      (assign, reg0, ":rain_type"),
      (assign, reg1, ":rand_strength"),
    (try_end),
  ]),
  
  #script_weather_affect_proficiency
  #INPUT: Rain type and strength
  #OUTPUT: none
 ("weather_affect_proficiency",
   [
    (store_script_param, ":rain_type", 1),
    (store_script_param, ":rain_strength", 2),
    
	(try_begin),
		(assign, ":night", 0),
		(try_begin),
			(is_currently_night),
			(assign, ":night", 1),
		(try_end),
		(get_global_haze_amount, ":fog"),
		
		(assign, ":prof_penalty", 0),
		(try_begin),
			(eq, ":night", 1),
			(val_add, ":prof_penalty", 15), #15% decrease for fighting at night
		(try_end),
		(try_begin),
			(ge, ":fog", 50),
			(val_sub, ":fog", 50),
			(val_div, ":fog", 5),
			(val_add, ":prof_penalty", ":fog"), #1% decrease for each 5% of fog over 50
		(try_end),
		(try_begin),
			(neq, ":rain_type", -1),
			(val_sub, ":rain_strength", 20),
			(val_div, ":rain_strength", 5), #1% decrease for each 5% of snow strength over 20
			(val_add, ":prof_penalty", ":rain_strength"),
			(eq, ":rain_type", 1), #another 1% decrease for each 5% of strength over 20 for rain
			(val_add, ":prof_penalty", ":rain_strength"), 
		(try_end),

		(val_min, ":prof_penalty", 51),
		(ge, ":prof_penalty", 15), #Make sure it is worth it
		(party_set_slot, "p_main_party", slot_party_pref_wp_prof_decrease, 2),
		
		(try_for_range, ":n", 0, 2),
			(try_begin),
				(eq, ":n", 0),
				(assign, ":party", "p_collective_enemy"),
			(else_try),
				(assign, ":party", "p_collective_friends"),
			(try_end),
			(party_get_num_companion_stacks, ":num_stacks", ":party"),
			(try_for_range, ":i", 0, ":num_stacks"),
				(party_stack_get_troop_id, ":troop_id", ":party", ":i"),
				#(neq, ":troop_id", "trp_player"), #Uncomment these lines if you think it appropriate
				#(neg|troop_is_hero, ":troop_id"), #I don't care myself. It works either way.
				(party_stack_get_size, ":size", ":party", ":i"),
				(party_stack_get_num_wounded, ":wounded", ":party", ":i"),
				(val_sub, ":size", ":wounded"),
				(gt, ":size", 0),            
				(troop_slot_eq, ":troop_id", slot_troop_proficiency_modified, 0),
				(call_script, "script_weather_troop_lower_proficiencies", ":troop_id", ":prof_penalty"),        
			(try_end), #Stack Loop
		(try_end), #Party Loop 
    (try_end),	
   ]),

  #script_weather_troop_lower_proficiencies
  #INPUT: troop id; proficiency penalty in %
  #OUTPUT: none
 ("weather_troop_lower_proficiencies",
   [
    (store_script_param, ":troop_id", 1),
    (store_script_param, ":prof_penalty", 2),

    (try_for_range, ":n", 0, 3),
        (try_begin),
            (eq, ":n", 0),
            (assign, ":proficiency", wpt_archery),
            #(assign, ":prof_item_type", itp_type_bow),
            (assign, ":prof_slot", slot_troop_orig_wpt_archery),
        (else_try),
            (eq, ":n", 1),
            (assign, ":proficiency", wpt_crossbow),
            #(assign, ":prof_item_type", itp_type_crossbow),
            (assign, ":prof_slot", slot_troop_orig_wpt_crossbow),
        (else_try),
            (eq, ":n", 2),
            (assign, ":proficiency", wpt_throwing),
            #(assign, ":prof_item_type", itp_type_thrown),
            (assign, ":prof_slot", slot_troop_orig_wpt_throwing),
        (try_end),
        
        (store_proficiency_level, ":orig_proficiency", ":troop_id", ":proficiency"),
        
        (store_mul, ":wp_prof_new", ":orig_proficiency", 100),
        (store_mul, ":wp_prof_decrease", ":orig_proficiency", ":prof_penalty"),
        (val_sub, ":wp_prof_new", ":wp_prof_decrease"),
        (val_div, ":wp_prof_new", 100),
            
        (troop_raise_proficiency_linear, ":troop_id", ":proficiency", -10000),
        (troop_raise_proficiency_linear, ":troop_id", ":proficiency", ":wp_prof_new"),
        
        (troop_set_slot, ":troop_id", ":prof_slot", ":orig_proficiency"),
		(try_begin), #stores changed proficiency for heroes to allow gains during battle
			(troop_is_hero, ":troop_id"),
			(val_add, ":prof_slot", 3), #bump to pnty_wpt slot
			(store_proficiency_level, ":wp_prof_new", ":troop_id", ":proficiency"),
			(troop_set_slot, ":troop_id", ":prof_slot", ":wp_prof_new"),
		(try_end),
        
        (try_begin),
            (eq, "$cheat_mode", 1),
            (store_proficiency_level, ":wp_prof_new", ":troop_id", ":proficiency"),
            (str_store_troop_name, s0, ":troop_id"),
            (assign, reg0, ":orig_proficiency"),
            (assign, reg1, ":wp_prof_new"),
            (assign, reg2, ":prof_penalty"),
            (display_message, "@DEBUG : Weather penalty {reg2}% - {s0}: {reg0} to {reg1}"),
        (try_end),
    (try_end), #Proficiency Loop
    (troop_set_slot, ":troop_id", slot_troop_proficiency_modified, 1),
   ]),
  
  #script_weather_restore_proficiencies
  #INPUT: none called from simple trigger post-battle
  #OUTPUT: none
 ("weather_restore_proficiencies",
   [
    (assign, ":end", pbod_last_troop),
    (val_add, ":end", 1),
    (try_for_range, ":troop_id", 0, ":end"),
        (troop_slot_eq, ":troop_id", slot_troop_proficiency_modified, 1),
        (try_for_range, ":n", 0, 3),
            (store_add, ":proficiency", wpt_archery, ":n"),
            (store_add, ":prof_slot", slot_troop_orig_wpt_archery, ":n"),
			
			(assign, ":orig_prof", -1),
            (store_proficiency_level, ":mod_proficiency", ":troop_id", ":proficiency"),
			(try_begin),
				(troop_is_hero, ":troop_id"),  
				(store_add, ":pnty_slot", ":prof_slot", 3), #trackign penalty level allows heroes WP gains during battle   ##BUG in Floris 2.5b2, missing argument
				(store_add, reg0, ":mod_proficiency", 1), #needed for ge rather than gt
				(this_or_next|troop_slot_ge, ":troop_id", ":prof_slot", reg0), #the original is bigger than it is currently (restoration needed, regardless of gain)
				(neg|troop_slot_ge, ":troop_id", ":pnty_slot", ":mod_proficiency"), #the penalty level is smaller than it is currently (there was a gain)
				
				(troop_get_slot, reg0, ":troop_id", ":pnty_slot"),
				(val_sub, ":mod_proficiency", reg0), #get the increase from the battle
				(val_max, ":mod_proficiency", 0), #ensure no further loss (shouldn't be possible, but you know)
				(troop_get_slot, ":orig_prof", ":troop_id", ":prof_slot"),
				(val_add, ":orig_prof", ":mod_proficiency"), #give gain
				(troop_set_slot, ":troop_id", ":pnty_slot", 0),
			(else_try),
				(neg|troop_is_hero, ":troop_id"),
				(val_add, ":mod_proficiency", 1),				
				(troop_slot_ge, ":troop_id", ":prof_slot", ":mod_proficiency"),
				(troop_get_slot, ":orig_prof", ":troop_id", ":prof_slot"),
			(try_end),
			(troop_set_slot, ":troop_id", ":prof_slot", 0),
			(gt, ":orig_prof", -1),
            (troop_raise_proficiency_linear, ":troop_id", ":proficiency", -10000),
            (troop_raise_proficiency_linear, ":troop_id", ":proficiency", ":orig_prof"),
            
            (try_begin),
                (eq, "$cheat_mode", 1),
                (str_store_troop_name, s0, ":troop_id"),
                (store_proficiency_level, ":wp_prof_new", ":troop_id", ":proficiency"),
                (assign, reg1, ":wp_prof_new"),
                (display_message, "@DEBUG : {s0} proficiency restored to: {reg1}"),
            (try_end),
        (try_end), #Proficiency Loop
        (troop_set_slot, ":troop_id", slot_troop_proficiency_modified, 0),
    (try_end), #Troop Loop
   ]), 

 ("prebattle_agents_set_start_positions", 
   [
    (store_script_param_1, ":team_no"),
	
	(team_get_leader, ":leader", ":team_no"),
	
	#set agent positions, based on the scripted_destinations set above
	(try_for_agents, ":agent"),
		(neq, ":agent", ":leader"),
		(agent_is_human, ":agent"),
		(agent_get_division, ":division", ":agent"),
		(try_begin), #Maintain any changed divisions from split division code
			(agent_slot_ge, ":agent", slot_agent_new_division, 0),
			(neg|agent_slot_eq, ":agent", slot_agent_new_division, ":division"),
			(agent_get_slot, ":division", ":agent", slot_agent_new_division),
			(agent_set_division, ":agent", ":division"),
		(try_end),
		(agent_is_in_special_mode, ":agent"),
		(agent_get_team, ":team", ":agent"),
		(eq, ":team", ":team_no"),
		(class_is_listening_order, ":team", ":division"),
		(agent_get_scripted_destination, pos1, ":agent"),
		(try_begin),
			(agent_get_horse, ":horse", ":agent"),
			(ge, ":horse", 0),
			(agent_set_position, ":horse", pos1),
		(else_try),
			(agent_set_position, ":agent", pos1),
		(try_end),

		(store_add, ":slot", slot_team_d0_formation, ":division"),
		(team_slot_eq, ":team", ":slot", formation_none),
		(agent_clear_scripted_mode, ":agent"),
		(agent_set_speed_limit, ":agent", 100),
		(agent_set_slot, ":agent", slot_agent_in_first_rank, 0),
		(agent_set_slot, ":agent", slot_agent_inside_formation, 0),
	(try_end),
   ]),  
   
]
## Prebattle Orders & Deployment End

update_order_flags_addon = [
	##PBOD Begin in "update_order_flags_on_map", add at end of script
    (assign, ":overlay", "$g_battle_map_cavalry_order_flag"),
    (try_for_range, ":class", 3, 9),
	  (val_add, ":overlay", 1),
	  (team_get_movement_order, ":cur_order", ":player_team", ":class"),
      (eq, ":cur_order", mordr_hold),
      (team_get_order_position, pos1, ":player_team", ":class"),
      (call_script, "script_convert_3d_pos_to_map_pos"),
      (overlay_set_alpha, ":overlay", 0xFF),
	  (try_begin),
		(neq, ":class", 8), #9
		(neq, ":class", 6), #7 fly the 'default' direction
		(position_get_x, reg0, pos0),
		(val_sub, reg0, 13),
		(position_set_x, pos0, reg0),
	  (else_try),
	    (eq, ":class", 8), #bump up a bit
		(position_get_y, reg0, pos0),
		(val_add, reg0, 8),
		(position_set_y, pos0, reg0),
	  (try_end),
      (overlay_set_position, ":overlay", pos0),
    (else_try),
      (overlay_set_alpha, ":overlay", 0),
    (try_end),
	##PBOD End
]


def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1143 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "scripts"
		orig_scripts = var_set[var_name_1]
		
		modmerge_pbod_scripts(orig_scripts)
		
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)

from util_wrappers import *
from util_scripts import *

scripts_directives = [
	[SD_OP_BLOCK_INSERT, "update_order_flags_on_map", D_SEARCH_FROM_BOTTOM | D_SEARCH_LINENUMBER | D_INSERT_BEFORE, 0, 0, update_order_flags_addon], #ADD TO END	
] 

def modmerge_pbod_scripts(orig_scripts):
	# process script directives first
	process_script_directives(orig_scripts, scripts_directives)
	# add remaining scripts
	add_scripts(orig_scripts, scripts, True)