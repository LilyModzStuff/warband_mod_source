# -*- coding: cp1252 -*-
from header_common import *
from header_scene_props import *
from header_operations import *
from header_triggers import *
from header_sounds import *
from module_constants import *
import string

from compiler import *
####################################################################################################################
#  Each scene prop record contains the following fields:
#  1) Scene prop id: used for referencing scene props in other files. The prefix spr_ is automatically added before each scene prop id.
#  2) Scene prop flags. See header_scene_props.py for a list of available flags
#  3) Mesh name: Name of the mesh.
#  4) Physics object name:
#  5) Triggers: Simple triggers that are associated with the scene prop
####################################################################################################################

check_item_use_trigger = (ti_on_scene_prop_use,
    [
      (store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),
      
      #for only server itself-----------------------------------------------------------------------------------------------
      (call_script, "script_use_item", ":instance_id", ":agent_id"),
      #for only server itself-----------------------------------------------------------------------------------------------
      (get_max_players, ":num_players"),                               
      (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
        (player_is_active, ":player_no"),
        (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_use_item, ":instance_id", ":agent_id"),
      (try_end),
    ])

check_sally_door_use_trigger_double = (ti_on_scene_prop_use,
    [
      (store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),

      (agent_get_position, pos1, ":agent_id"),
      (prop_instance_get_starting_position, pos2, ":instance_id"),
      
      (scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),

      (try_begin),
        #out doors like castle sally door can be opened only from inside, if door coordinate is behind your coordinate. Also it can be closed from both sides.
        
        (prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),
        
        (assign, ":can_open_door", 0),
        (try_begin),
          (neg|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
          (neg|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
          (neg|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
          (neg|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
          
          (position_is_behind_position, pos1, pos2),
          (assign, ":can_open_door", 1),
        (else_try),  
          (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
          (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
          (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
          (eq, ":scene_prop_id", "spr_earth_sally_gate_left"),

          (neg|position_is_behind_position, pos1, pos2),
          (assign, ":can_open_door", 1),
        (try_end),
        
        (this_or_next|eq, ":can_open_door", 1),
        (eq, ":opened_or_closed", 1),
      
        (try_begin),
          #for only server itself-----------------------------------------------------------------------------------------------
          (call_script, "script_use_item", ":instance_id", ":agent_id"),
          #for only server itself-----------------------------------------------------------------------------------------------
          (get_max_players, ":num_players"),                               
          (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
            (player_is_active, ":player_no"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_use_item, ":instance_id", ":agent_id"),
          (try_end),
        (try_end),
      (try_end),
    ])

check_sally_door_use_trigger = (ti_on_scene_prop_use,
    [
      (store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),

      (agent_get_position, pos1, ":agent_id"),
      (prop_instance_get_starting_position, pos2, ":instance_id"),
      
      (scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),

      (try_begin),
        #out doors like castle sally door can be opened only from inside, if door coordinate is behind your coordinate. Also it can be closed from both sides.
        (this_or_next|position_is_behind_position, pos1, pos2),
        (eq, ":opened_or_closed", 1),
      
        (try_begin),
          #for only server itself-----------------------------------------------------------------------------------------------
          (call_script, "script_use_item", ":instance_id", ":agent_id"),
          #for only server itself-----------------------------------------------------------------------------------------------
          (get_max_players, ":num_players"),                               
          (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
            (player_is_active, ":player_no"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_use_item, ":instance_id", ":agent_id"),
          (try_end),
        (try_end),
      (try_end),
    ])

check_castle_door_use_trigger = (ti_on_scene_prop_use,
    [
      (store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),

      (agent_get_position, pos1, ":agent_id"),
      (prop_instance_get_starting_position, pos2, ":instance_id"),
      
      (scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),

      (try_begin),
        (ge, ":agent_id", 0),
        (agent_get_team, ":agent_team", ":agent_id"),

        #in doors like castle room doors can be opened from both sides, but only defenders can open these doors. Also it can be closed from both sides.
        (this_or_next|eq, ":agent_team", 0),
        (eq, ":opened_or_closed", 1),
      
        (try_begin),
          #for only server itself-----------------------------------------------------------------------------------------------
          (call_script, "script_use_item", ":instance_id", ":agent_id"),
          #for only server itself-----------------------------------------------------------------------------------------------
          (get_max_players, ":num_players"),                               
          (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
            (player_is_active, ":player_no"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_use_item, ":instance_id", ":agent_id"),
          (try_end),
        (try_end),
      (try_end),
    ])

check_ladder_animate_trigger = (ti_on_scene_prop_is_animating,
    [      
      (store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":remaining_time"),

      (call_script, "script_check_creating_ladder_dust_effect", ":instance_id", ":remaining_time"),
      ])

check_ladder_animation_finish_trigger = (ti_on_scene_prop_animation_finished,
    [
      (store_trigger_param_1, ":instance_id"),

      (prop_instance_enable_physics, ":instance_id", 1),
      ])

scene_props = [
  ("invalid_object",0,"question_mark","0", []),
  ("inventory",sokf_type_container|sokf_place_at_origin,"package","bobaggage", []),
  ("empty", 0, "0", "0", []),
  ("chest_a",sokf_type_container,"chest_gothic","bochest_gothic", []),
  ("container_small_chest",sokf_type_container,"package","bobaggage", []),
  ("container_chest_b",sokf_type_container,"chest_b","bo_chest_b", []),
  ("container_chest_c",sokf_type_container,"chest_c","bo_chest_c", []),
  ("player_chest",sokf_type_container,"player_chest","bo_player_chest", []),
  ("locked_player_chest",0,"player_chest","bo_player_chest", []),

  ("light_sun",sokf_invisible,"light_sphere","0",  [
     (ti_on_init_scene_prop,
      [
          (neg|is_currently_night),
          (store_trigger_param_1, ":prop_instance_no"),
          (set_fixed_point_multiplier, 100),
          (prop_instance_get_scale, pos5, ":prop_instance_no"),
          (position_get_scale_x, ":scale", pos5),
          (store_time_of_day,reg(12)),
          (try_begin),
            (is_between,reg(12),5,20),
            (store_mul, ":red", 5 * 200, ":scale"),
            (store_mul, ":green", 5 * 193, ":scale"),
            (store_mul, ":blue", 5 * 180, ":scale"),
          (else_try),
            (store_mul, ":red", 5 * 90, ":scale"),
            (store_mul, ":green", 5 * 115, ":scale"),
            (store_mul, ":blue", 5 * 150, ":scale"),
          (try_end),
          (val_div, ":red", 100),
          (val_div, ":green", 100),
          (val_div, ":blue", 100),
          (set_current_color,":red", ":green", ":blue"),
          (set_position_delta,0,0,0),
          (add_point_light_to_entity, 0, 0),
      ]),
    ]),
  ("light",sokf_invisible,"light_sphere","0",  [
     (ti_on_init_scene_prop,
      [
          (store_trigger_param_1, ":prop_instance_no"),
          (set_fixed_point_multiplier, 100),
          (prop_instance_get_scale, pos5, ":prop_instance_no"),
          (position_get_scale_x, ":scale", pos5),
          (store_mul, ":red", 3 * 200, ":scale"),
          (store_mul, ":green", 3 * 145, ":scale"),
          (store_mul, ":blue", 3 * 45, ":scale"),
          (val_div, ":red", 100),
          (val_div, ":green", 100),
          (val_div, ":blue", 100),
          (set_current_color,":red", ":green", ":blue"),
          (set_position_delta,0,0,0),
          (add_point_light_to_entity, 10, 30),
      ]),
    ]),
  ("light_red",sokf_invisible,"light_sphere","0",  [
     (ti_on_init_scene_prop,
      [
          (store_trigger_param_1, ":prop_instance_no"),
          (set_fixed_point_multiplier, 100),
          (prop_instance_get_scale, pos5, ":prop_instance_no"),
          (position_get_scale_x, ":scale", pos5),
          (store_mul, ":red", 2 * 170, ":scale"),
          (store_mul, ":green", 2 * 100, ":scale"),
          (store_mul, ":blue", 2 * 30, ":scale"),
          (val_div, ":red", 100),
          (val_div, ":green", 100),
          (val_div, ":blue", 100),
          (set_current_color,":red", ":green", ":blue"),
          (set_position_delta,0,0,0),
          (add_point_light_to_entity, 20, 30),
      ]),
    ]),
  ("light_night",sokf_invisible,"light_sphere","0",  [
     (ti_on_init_scene_prop,
      [
#          (store_time_of_day,reg(12)),
#          (neg|is_between,reg(12),5,20),
          (is_currently_night, 0),
          (store_trigger_param_1, ":prop_instance_no"),
          (set_fixed_point_multiplier, 100),
          (prop_instance_get_scale, pos5, ":prop_instance_no"),
          (position_get_scale_x, ":scale", pos5),
          (store_mul, ":red", 3 * 160, ":scale"),
          (store_mul, ":green", 3 * 145, ":scale"),
          (store_mul, ":blue", 3 * 100, ":scale"),
          (val_div, ":red", 100),
          (val_div, ":green", 100),
          (val_div, ":blue", 100),
          (set_current_color,":red", ":green", ":blue"),
          (set_position_delta,0,0,0),
          (add_point_light_to_entity, 10, 30),
      ]),
    ]),
  ("torch",0,"torch_a","0",
   [
   (ti_on_init_scene_prop,
    [
        (set_position_delta,0,-35,48),
        (particle_system_add_new, "psys_torch_fire"),
        (particle_system_add_new, "psys_torch_smoke"),
        (particle_system_add_new, "psys_torch_fire_sparks"),

        (play_sound, "snd_torch_loop", 0),
        
        (set_position_delta,0,-35,56),
        (particle_system_add_new, "psys_fire_glow_1"),
#        (particle_system_emit, "psys_fire_glow_1",9000000),

#second method        
        (get_trigger_object_position, pos2),
        (set_position_delta,0,0,0),
        (position_move_y, pos2, -35),

        (position_move_z, pos2, 55),
        (particle_system_burst, "psys_fire_glow_fixed", pos2, 1),
    ]),
   ]),
  ("torch_night",0,"torch_a","0",
   [
   (ti_on_init_scene_prop,
    [
#        (store_time_of_day,reg(12)),
#        (neg|is_between,reg(12),5,20),
        (is_currently_night, 0),
        (set_position_delta,0,-35,48),
        (particle_system_add_new, "psys_torch_fire"),
        (particle_system_add_new, "psys_torch_smoke"),
        (particle_system_add_new, "psys_torch_fire_sparks"),
        (set_position_delta,0,-35,56),
        (particle_system_add_new, "psys_fire_glow_1"),
        (particle_system_emit, "psys_fire_glow_1",9000000),
        (play_sound, "snd_torch_loop", 0),
    ]),
   ]),
#  ("Baggage",sokf_place_at_origin|sokf_entity_body,"package","bobaggage"),
  ("barrier_20m",sokf_invisible|sokf_type_barrier,"barrier_20m","bo_barrier_20m", []),
  ("barrier_16m",sokf_invisible|sokf_type_barrier,"barrier_16m","bo_barrier_16m", []),
  ("barrier_8m" ,sokf_invisible|sokf_type_barrier,"barrier_8m" ,"bo_barrier_8m" , []),
  ("barrier_4m" ,sokf_invisible|sokf_type_barrier,"barrier_4m" ,"bo_barrier_4m" , []),
  ("barrier_2m" ,sokf_invisible|sokf_type_barrier,"barrier_2m" ,"bo_barrier_2m" , []),
  
  ("exit_4m" ,sokf_invisible|sokf_type_barrier_leave,"barrier_4m" ,"bo_barrier_4m" , []),
  ("exit_8m" ,sokf_invisible|sokf_type_barrier_leave,"barrier_8m" ,"bo_barrier_8m" , []),
  ("exit_16m" ,sokf_invisible|sokf_type_barrier_leave,"barrier_16m" ,"bo_barrier_16m" , []),

  ("ai_limiter_2m" ,sokf_invisible|sokf_type_ai_limiter,"barrier_2m" ,"bo_barrier_2m" , []),
  ("ai_limiter_4m" ,sokf_invisible|sokf_type_ai_limiter,"barrier_4m" ,"bo_barrier_4m" , []),
  ("ai_limiter_8m" ,sokf_invisible|sokf_type_ai_limiter,"barrier_8m" ,"bo_barrier_8m" , []),
  ("ai_limiter_16m",sokf_invisible|sokf_type_ai_limiter,"barrier_16m","bo_barrier_16m", []),
  ("Shield",sokf_dynamic,"0","boshield", []),
  ("shelves",0,"shelves","boshelves", []),
  ("table_tavern",0,"table_tavern","botable_tavern", []),
  ("table_castle_a",0,"table_castle_a","bo_table_castle_a", []),
  ("chair_castle_a",0,"chair_castle_a","bo_chair_castle_a", []),

  ("pillow_a",0,"pillow_a","bo_pillow", []),
  ("pillow_b",0,"pillow_b","bo_pillow", []),
  ("pillow_c",0,"pillow_c","0", []),


  ("interior_castle_g_square_keep_b",0,"interior_castle_g_square_keep_b","bo_interior_castle_g_square_keep_b", []),



  ("carpet_with_pillows_a",0,"carpet_with_pillows_a","bo_carpet_with_pillows", []),
  ("carpet_with_pillows_b",0,"carpet_with_pillows_b","bo_carpet_with_pillows", []),
  ("table_round_a",0,"table_round_a","bo_table_round_a", []),
  ("table_round_b",0,"table_round_b","bo_table_round_b", []),
  ("fireplace_b",0,"fireplace_b","bo_fireplace_b", []),
  ("fireplace_c",0,"fireplace_c","bo_fireplace_c", []),

  ("sofa_a",0,"sofa_a","bo_sofa", []),
  ("sofa_b",0,"sofa_b","bo_sofa", []),
  ("ewer_a",0,"ewer_a","bo_ewer_a", []),
  ("end_table_a",0,"end_table_a","bo_end_table_a", []),


  ("fake_houses_steppe_a",0,"fake_houses_steppe_a","0", []),
  ("fake_houses_steppe_b",0,"fake_houses_steppe_b","0", []),
  ("fake_houses_steppe_c",0,"fake_houses_steppe_c","0", []),

  ("boat_destroy",0,"boat_destroy","bo_boat_destroy", []),
  ("destroy_house_a",0,"destroy_house_a","bo_destroy_house_a", []),
  ("destroy_house_b",0,"destroy_house_b","bo_destroy_house_b", []),
  ("destroy_house_c",0,"destroy_house_c","bo_destroy_house_c", []),
  ("destroy_heap",0,"destroy_heap","bo_destroy_heap", []),
  ("destroy_castle_a",0,"destroy_castle_a","bo_destroy_castle_a", []),
  ("destroy_castle_b",0,"destroy_castle_b","bo_destroy_castle_b", []),
  
  ("destroy_castle_c",0,"destroy_castle_c","bo_destroy_castle_c", []),
  
  ("destroy_castle_d",0,"destroy_castle_d","bo_destroy_castle_d", []),
  ("destroy_windmill",0,"destroy_windmill","bo_destroy_windmill", []),
  ("destroy_tree_a",0,"destroy_tree_a","bo_destroy_tree_a", []),
  ("destroy_tree_b",0,"destroy_tree_b","bo_destroy_tree_b", []),  
  ("destroy_bridge_a",0,"destroy_bridge_a","bo_destroy_bridge_a", []),  
  ("destroy_bridge_b",0,"destroy_bridge_b","bo_destroy_bridge_b", []),  


  ("catapult",0,"Catapult","bo_Catapult", []),
  
  ("catapult_destructible",sokf_moveable|sokf_show_hit_point_bar|sokf_destructible,"Catapult","bo_Catapult", [
   (ti_on_init_scene_prop,
    [
      (store_trigger_param_1, ":instance_no"),
      (scene_prop_set_hit_points, ":instance_no", 1600),
    ]),
     
   (ti_on_scene_prop_destroy,
    [          
      (play_sound, "snd_dummy_destroyed"),

      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),


        (store_trigger_param_1, ":instance_no"),      
        (prop_instance_get_position, pos1, ":instance_no"),
        (particle_system_burst, "psys_dummy_smoke_big", pos1, 100),
        (particle_system_burst, "psys_dummy_straw_big", pos1, 100),      
        (position_move_z, pos1, -500),
        (position_rotate_x, pos1, 90),
        (prop_instance_animate_to_position, ":instance_no", pos1, 300), #animate to 6 meters below in 6 second

        (try_begin),
          (eq, "$g_round_ended", 0),
          (scene_prop_get_team, ":scene_prop_team_no", ":instance_no"),
          (try_begin),
            (eq, ":scene_prop_team_no", 0),
            (assign, ":scene_prop_team_no_multiplier", -1), 
          (else_try),
            (assign, ":scene_prop_team_no_multiplier", 1), 
          (try_end),

          (try_begin),
            (eq, "$g_number_of_targets_destroyed", 0),        
            (store_mul, ":target_no_mul_scene_prop_team", ":scene_prop_team_no_multiplier", 1), #1 means destroyed object is a catapult
            #for only server itself-----------------------------------------------------------------------------------------------                                                                                                      
            (call_script, "script_show_multiplayer_message", multiplayer_message_type_target_destroyed, ":target_no_mul_scene_prop_team"), 
            #for only server itself-----------------------------------------------------------------------------------------------     
            (get_max_players, ":num_players"),                               
            (try_for_range, ":player_no", 1, ":num_players"),
              (player_is_active, ":player_no"),
              (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_target_destroyed, ":target_no_mul_scene_prop_team"), 
            (try_end),
            (val_add, "$g_number_of_targets_destroyed", 1),
          (else_try),
            (store_mul, ":target_no_mul_scene_prop_team", ":scene_prop_team_no_multiplier", 9), #9 means attackers destroyed all targets
            #for only server itself-----------------------------------------------------------------------------------------------      
            (call_script, "script_show_multiplayer_message", multiplayer_message_type_target_destroyed, ":target_no_mul_scene_prop_team"), 
            #for only server itself-----------------------------------------------------------------------------------------------     
            (get_max_players, ":num_players"),                               
            (try_for_range, ":player_no", 1, ":num_players"),
              (player_is_active, ":player_no"),
              (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_target_destroyed, ":target_no_mul_scene_prop_team"), 
            (try_end),
            (val_add, "$g_number_of_targets_destroyed", 1),
          (try_end),
        (try_end),

        #giving gold for destroying target (for catapult)
        #step-1 calculating total damage given to that scene prop
        (assign, ":total_damage_given", 0),
        (get_max_players, ":num_players"),                               
        (try_for_range, ":player_no", 0, ":num_players"), 
          (player_is_active, ":player_no"),
          
          (try_begin),
            (eq, "spr_catapult_destructible", "$g_destructible_target_1"),
            (player_get_slot, ":damage_given", ":player_no", slot_player_damage_given_to_target_1),
          (else_try),
            (player_get_slot, ":damage_given", ":player_no", slot_player_damage_given_to_target_2),
          (try_end),

          (val_add, ":total_damage_given", ":damage_given"),
        (try_end),

        #step-2 sharing 1000 gold (if num active players < 20 then 50 * num active players) to players which gave damage with the damage amounts.
        (assign, ":destroy_money_addition", 0),
        (get_max_players, ":num_players"),                               
        (try_for_range, ":player_no", 0, ":num_players"), 
          (player_is_active, ":player_no"),
          (val_add, ":destroy_money_addition", 50),
        (try_end),
      
        (try_begin),
          (ge, ":destroy_money_addition", multi_destroy_target_money_add),
          (assign, ":destroy_money_addition", multi_destroy_target_money_add),
        (try_end),
        (val_mul, ":destroy_money_addition", "$g_multiplayer_battle_earnings_multiplier"),
        (val_div, ":destroy_money_addition", 100),
      
        (get_max_players, ":num_players"),                               
        (try_for_range, ":player_no", 0, ":num_players"), 
          (player_is_active, ":player_no"),
          
          (try_begin),
            (eq, "spr_catapult_destructible", "$g_destructible_target_1"),
            (player_get_slot, ":damage_given", ":player_no", slot_player_damage_given_to_target_1),
          (else_try),
            (player_get_slot, ":damage_given", ":player_no", slot_player_damage_given_to_target_2),
          (try_end),

          (player_get_gold, ":player_gold", ":player_no"), #give money to player which helped flag to be owned by new_flag_owner team

          (val_mul, ":damage_given", ":destroy_money_addition"),

          (try_begin),
            (ge, ":total_damage_given", ":damage_given"),
            (gt, ":damage_given", 0),
            (store_div, ":gold_earned", ":damage_given", ":total_damage_given"),
          (else_try),
            (assign, ":gold_earned", 0),
          (try_end),
        
          (val_add, ":player_gold", ":gold_earned"),
          (player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),              
        (try_end),
      (try_end),
    ]),     

    (ti_on_scene_prop_hit,
    [
      (store_trigger_param_1, ":instance_no"),       
      (store_trigger_param_2, ":damage"),
      
      (try_begin),
        (scene_prop_get_hit_points, ":hit_points", ":instance_no"),
        (val_sub, ":hit_points", ":damage"),
        (gt, ":hit_points", 0),
        (play_sound, "snd_dummy_hit"),
      (else_try),
        (neg|multiplayer_is_server),
        (play_sound, "snd_dummy_destroyed"),
      (try_end),

      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (particle_system_burst, "psys_dummy_smoke", pos1, 3),
        (particle_system_burst, "psys_dummy_straw", pos1, 10),
        (set_fixed_point_multiplier, 1),
        (position_get_x, ":attacker_agent_id", pos2),
        (try_begin),
          (ge, ":attacker_agent_id", 0),
          (agent_is_alive, ":attacker_agent_id"),
          (agent_is_human, ":attacker_agent_id"),
          (neg|agent_is_non_player, ":attacker_agent_id"),
          (agent_get_player_id, ":attacker_player_id", ":attacker_agent_id"),
          (ge, ":attacker_player_id", 0),
          (player_is_active, ":attacker_player_id"),        
          (try_begin),
            (eq, "spr_catapult_destructible", "$g_destructible_target_1"),
            (player_get_slot, ":damage_given", ":attacker_player_id", slot_player_damage_given_to_target_1),
            (val_add, ":damage_given", ":damage"),
            (player_set_slot, ":attacker_player_id", slot_player_damage_given_to_target_1, ":damage_given"),
          (else_try),
            (player_get_slot, ":damage_given", ":attacker_player_id", slot_player_damage_given_to_target_2),
            (val_add, ":damage_given", ":damage"),
            (player_set_slot, ":attacker_player_id", slot_player_damage_given_to_target_2, ":damage_given"),
          (try_end),
        (try_end),
      (try_end),
    ]),
  ]),
  
  ("broom",0,"broom","0", []),
  ("garlic",0,"garlic","0", []),
  ("garlic_b",0,"garlic_b","0", []),

  ("destroy_a",0,"destroy_a","0", []),
  ("destroy_b",0,"destroy_b","0", []),



  ("bridge_wooden",0,"bridge_wooden","bo_bridge_wooden", []),
  ("bridge_wooden_snowy",0,"bridge_wooden_snowy","bo_bridge_wooden", []),
  
  ("grave_a",0,"grave_a","bo_grave_a", []),

  
  ("village_house_e",0,"village_house_e","bo_village_house_e", []),
  ("village_house_f",0,"village_house_f","bo_village_house_f", []),
  ("village_house_g",0,"village_house_g","bo_village_house_g", []),
  ("village_house_h",0,"village_house_h","bo_village_house_h", []),
  ("village_house_i",0,"village_house_i","bo_village_house_i", []),
  ("village_house_j",0,"village_house_j","bo_village_house_j", []),
  ("village_wall_a",0,"village_wall_a","bo_village_wall_a", []),
  ("village_wall_b",0,"village_wall_b","bo_village_wall_b", []),

  ("village_snowy_house_a",0,"village_snowy_house_a","bo_village_snowy_house_a", []),  
  ("village_snowy_house_b",0,"village_snowy_house_b","bo_village_snowy_house_b", []),
  ("village_snowy_house_c",0,"village_snowy_house_c","bo_village_snowy_house_c", []),
  ("village_snowy_house_d",0,"village_snowy_house_d","bo_village_snowy_house_d", []),
  ("village_snowy_house_e",0,"village_snowy_house_e","bo_village_snowy_house_e", []),
  ("village_snowy_house_f",0,"village_snowy_house_f","bo_village_snowy_house_f", []),



  ("town_house_steppe_a",0,"town_house_steppe_a","bo_town_house_steppe_a", []),
  ("town_house_steppe_b",0,"town_house_steppe_b","bo_town_house_steppe_b", []),
  ("town_house_steppe_c",0,"town_house_steppe_c","bo_town_house_steppe_c", []),
  ("town_house_steppe_d",0,"town_house_steppe_d","bo_town_house_steppe_d", []),
  ("town_house_steppe_e",0,"town_house_steppe_e","bo_town_house_steppe_e", []),
  ("town_house_steppe_f",0,"town_house_steppe_f","bo_town_house_steppe_f", []),
  ("town_house_steppe_g",0,"town_house_steppe_g","bo_town_house_steppe_g", []),
  ("town_house_steppe_h",0,"town_house_steppe_h","bo_town_house_steppe_h", []),
  ("town_house_steppe_i",0,"town_house_steppe_i","bo_town_house_steppe_i", []),

  ("carpet_a",0,"carpet_a","0", []),
  ("carpet_b",0,"carpet_b","0", []),
  ("carpet_c",0,"carpet_c","0", []),
  ("carpet_d",0,"carpet_d","0", []),
  ("carpet_e",0,"carpet_e","0", []),
  ("carpet_f",0,"carpet_f","0", []),

  ("awning_a",0,"awning_a","bo_awning", []),
  ("awning_b",0,"awning_b","bo_awning", []),
  ("awning_c",0,"awning_c","bo_awning", []),
  ("awning_long",0,"awning_long","bo_awning_long", []),
  ("awning_long_b",0,"awning_long_b","bo_awning_long", []),
  ("awning_d",0,"awning_d","bo_awning_d", []),


  ("ship",0,"ship","bo_ship", []),

  ("ship_b",0,"ship_b","bo_ship_b", []),
  ("ship_c",0,"ship_c","bo_ship_c", []),



  ("ship_d",0,"ship_d","bo_ship_d", []),

  ("snowy_barrel_a",0,"snowy_barrel_a","bo_snowy_barrel_a", []),
  ("snowy_fence",0,"snowy_fence","bo_snowy_fence", []),
  ("snowy_wood_heap",0,"snowy_wood_heap","bo_snowy_wood_heap", []),

  ("village_snowy_stable_a",0,"village_snowy_stable_a","bo_village_snowy_stable_a", []),


  ("village_straw_house_a",0,"village_straw_house_a","bo_village_straw_house_a", []),
  ("village_stable_a",0,"village_stable_a","bo_village_stable_a", []),
  ("village_shed_a",0,"village_shed_a","bo_village_shed_a", []),
  ("village_shed_b",0,"village_shed_b","bo_village_shed_b", []),

  ("dungeon_door_cell_a",0,"dungeon_door_cell_a","bo_dungeon_door_cell_a", []),
  ("dungeon_door_cell_b",0,"dungeon_door_cell_b","bo_dungeon_door_cell_b", []),
  ("dungeon_door_entry_a",0,"dungeon_door_entry_a","bo_dungeon_door_entry_a", []),
  ("dungeon_door_entry_b",0,"dungeon_door_entry_b","bo_dungeon_door_entry_a", []),
  ("dungeon_door_entry_c",0,"dungeon_door_entry_c","bo_dungeon_door_entry_a", []),
  ("dungeon_door_direction_a",0,"dungeon_door_direction_a","bo_dungeon_door_direction_a", []),
  ("dungeon_door_direction_b",0,"dungeon_door_direction_b","bo_dungeon_door_direction_a", []),
  ("dungeon_door_stairs_a",0,"dungeon_door_stairs_a","bo_dungeon_door_stairs_a", []),
  ("dungeon_door_stairs_b",0,"dungeon_door_stairs_b","bo_dungeon_door_stairs_a", []),
  ("dungeon_bed_a",0,"dungeon_bed_a","0", []),
  ("dungeon_bed_b",0,"dungeon_bed_b","bo_dungeon_bed_b", []),
  ("torture_tool_a",0,"torture_tool_a","bo_torture_tool_a", []),
  ("torture_tool_b",0,"torture_tool_b","0", []),
  ("torture_tool_c",0,"torture_tool_c","bo_torture_tool_c", []),
  ("skeleton_head",0,"skeleton_head","0", []),
  ("skeleton_bone",0,"skeleton_bone","0", []),
  ("skeleton_a",0,"skeleton_a","bo_skeleton_a", []),
  ("dungeon_stairs_a",sokf_type_ladder,"dungeon_stairs_a","bo_dungeon_stairs_a", []),
  ("dungeon_stairs_b",sokf_type_ladder,"dungeon_stairs_b","bo_dungeon_stairs_a", []),
  ("dungeon_torture_room_a",0,"dungeon_torture_room_a","bo_dungeon_torture_room_a", []),
  ("dungeon_entry_a",0,"dungeon_entry_a","bo_dungeon_entry_a", []),
  ("dungeon_entry_b",0,"dungeon_entry_b","bo_dungeon_entry_b", []),
  ("dungeon_entry_c",0,"dungeon_entry_c","bo_dungeon_entry_c", []),
  ("dungeon_cell_a",0,"dungeon_cell_a","bo_dungeon_cell_a", []),
  ("dungeon_cell_b",0,"dungeon_cell_b","bo_dungeon_cell_b", []),
  ("dungeon_cell_c",0,"dungeon_cell_c","bo_dungeon_cell_c", []),
  ("dungeon_corridor_a",0,"dungeon_corridor_a","bo_dungeon_corridor_a", []),
  ("dungeon_corridor_b",0,"dungeon_corridor_b","bo_dungeon_corridor_b", []),
  ("dungeon_corridor_c",0,"dungeon_corridor_c","bo_dungeon_corridor_b", []),
  ("dungeon_corridor_d",0,"dungeon_corridor_d","bo_dungeon_corridor_b", []),
  ("dungeon_direction_a",0,"dungeon_direction_a","bo_dungeon_direction_a", []),
  ("dungeon_direction_b",0,"dungeon_direction_b","bo_dungeon_direction_a", []),
  ("dungeon_room_a",0,"dungeon_room_a","bo_dungeon_room_a", []),
  ("dungeon_tower_stairs_a",sokf_type_ladder,"dungeon_tower_stairs_a","bo_dungeon_tower_stairs_a", []),
  ("dungeon_tower_cell_a",0,"dungeon_tower_cell_a","bo_dungeon_tower_cell_a", []),
  ("tunnel_a",0,"tunnel_a","bo_tunnel_a", []),
  ("tunnel_salt",0,"tunnel_salt","bo_tunnel_salt", []),
  ("salt_a",0,"salt_a","bo_salt_a", []),

  ("door_destructible",sokf_moveable|sokf_show_hit_point_bar|sokf_destructible|spr_use_time(2),"tutorial_door_a","bo_tutorial_door_a", [
    check_item_use_trigger,

   (ti_on_init_scene_prop,
    [
      (store_trigger_param_1, ":instance_no"),
      (scene_prop_set_hit_points, ":instance_no", 2000),
    ]),
     
   (ti_on_scene_prop_destroy,
    [
      (play_sound, "snd_dummy_destroyed"),
      
      (assign, ":rotate_side", 86),
      
      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (store_trigger_param_1, ":instance_no"),      
        (store_trigger_param_2, ":attacker_agent_no"),

        (set_fixed_point_multiplier, 100),
        (prop_instance_get_position, pos1, ":instance_no"),

        (try_begin),
          (ge, ":attacker_agent_no", 0),
          (agent_get_position, pos2, ":attacker_agent_no"),
          (try_begin),
            (position_is_behind_position, pos2, pos1),
            (val_mul, ":rotate_side", -1),
          (try_end),
        (try_end),
      
        (init_position, pos3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (position_move_y, pos3, -100),
        (else_try),
          (position_move_y, pos3, 100),
        (try_end),
      
        (position_move_x, pos3, -50),
        (position_transform_position_to_parent, pos4, pos1, pos3),
        (position_move_z, pos4, 100),
        (position_get_distance_to_ground_level, ":height_to_terrain", pos4),
        (val_sub, ":height_to_terrain", 100),
        (assign, ":z_difference", ":height_to_terrain"),
        (val_div, ":z_difference", 3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (val_add, ":rotate_side", ":z_difference"),
        (else_try),
          (val_sub, ":rotate_side", ":z_difference"),
        (try_end),

        (position_rotate_x, pos1, ":rotate_side"),
        (prop_instance_animate_to_position, ":instance_no", pos1, 70), #animate to position 1 in 0.7 second
      (try_end),
    ]),       

    (ti_on_scene_prop_hit,
    [
      (play_sound, "snd_dummy_hit"),
      (particle_system_burst, "psys_dummy_smoke", pos1, 3),
      (particle_system_burst, "psys_dummy_straw", pos1, 10),      
    ]),
  ]),

  ("tutorial_door_a",sokf_moveable,"tutorial_door_a","bo_tutorial_door_a", []),

  ("tutorial_door_b",sokf_moveable,"tutorial_door_b","bo_tutorial_door_b", []),

  ("tutorial_flag_yellow",sokf_moveable|sokf_face_player,"tutorial_flag_yellow","0", []),
  ("tutorial_flag_red",sokf_moveable|sokf_face_player,"tutorial_flag_red","0", []),
  ("tutorial_flag_blue",sokf_moveable|sokf_face_player,"tutorial_flag_blue","0", []),

  ("interior_prison_a",0,"interior_prison_a","bo_interior_prison_a", []),
  ("interior_prison_b",0,"interior_prison_b","bo_interior_prison_b", []),
  ("interior_prison_cell_a",0,"interior_prison_cell_a","bo_interior_prison_cell_a", []),
  ("interior_prison_d",0,"interior_prison_d","bo_interior_prison_d", []),  

  ("arena_archery_target_a",0,"arena_archery_target_a","bo_arena_archery_target_a", []),
  ("archery_butt_a",0,"archery_butt","bo_archery_butt", [
   (ti_on_scene_prop_hit,
    [
        (store_trigger_param_1, ":instance_no"),
        (prop_instance_get_position, pos2, ":instance_no"),
        (get_player_agent_no, ":player_agent"),
        (agent_get_position, pos3, ":player_agent"),
        (get_distance_between_positions, ":player_distance", pos3, pos2),
        (position_transform_position_to_local, pos4, pos2, pos1),
        (position_set_y, pos4, 0),
        (position_set_x, pos2, 0),
        (position_set_y, pos2, 0),
        (position_set_z, pos2, 0),
        (get_distance_between_positions, ":target_distance", pos4, pos2),
        (assign, ":point_earned", 43), #Calculating a point between 0-12
        (val_sub, ":point_earned", ":target_distance"),
        (val_mul, ":point_earned", 1299),
        (val_div, ":point_earned", 4300),
        (try_begin),
          (lt, ":point_earned", 0),
          (assign, ":point_earned", 0),
        (try_end),
        (val_div, ":player_distance", 91), #Converting to yards
        (assign, reg60, ":point_earned"),
        (assign, reg61, ":player_distance"),
        (display_message, "str_archery_target_hit"),
    ]),
  ]),
  ("archery_target_with_hit_a",0,"arena_archery_target_a","bo_arena_archery_target_a", [
   (ti_on_scene_prop_hit,
    [
        (set_fixed_point_multiplier, 100),
        (store_trigger_param_1, ":instance_no"),
        (position_get_x, ":attacker_agent_id", pos2),
        (val_div, ":attacker_agent_id", 100),
        (get_player_agent_no, ":player_agent"),
        (try_begin),
          (eq, ":player_agent", ":attacker_agent_id"),
          (prop_instance_get_position, pos2, ":instance_no"),
          (agent_get_position, pos3, ":player_agent"),
          (get_distance_between_positions, ":player_distance", pos3, pos2),
          (position_transform_position_to_local, pos4, pos2, pos1),
          (position_set_y, pos4, 0),
          (position_set_x, pos2, 0),
          (position_set_y, pos2, 0),
          (position_set_z, pos2, 0),
          (get_distance_between_positions, ":target_distance", pos4, pos2),
          (assign, ":point_earned", 43), #Calculating a point between 0-12
          (val_sub, ":point_earned", ":target_distance"),
          (val_mul, ":point_earned", 1299),
          (val_div, ":point_earned", 4300),
          (try_begin),
            (lt, ":point_earned", 0),
            (assign, ":point_earned", 0),
          (try_end),
          (assign, "$g_last_archery_point_earned", ":point_earned"),
          (val_div, ":player_distance", 91), #Converting to yards
          (assign, reg60, ":point_earned"),
          (assign, reg61, ":player_distance"),
          (display_message, "str_archery_target_hit"),
          (eq, "$g_tutorial_training_ground_horseman_trainer_state", 6),
          (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 2),
          (prop_instance_get_variation_id_2, ":var_id_2", ":instance_no"),
          (val_sub, ":var_id_2", 1),
          (eq, "$g_tutorial_training_ground_current_score", ":var_id_2"),
          (val_add, "$g_tutorial_training_ground_current_score", 1),
        (try_end),
    ]),
  ]),
  ("dummy_a",sokf_destructible|sokf_moveable,"arena_archery_target_b","bo_arena_archery_target_b",   [
   (ti_on_scene_prop_destroy,
    [
        (store_trigger_param_1, ":instance_no"),
        (prop_instance_get_starting_position, pos1, ":instance_no"),
        (get_player_agent_no, ":player_agent"),
        (agent_get_position, 2, ":player_agent"),
        (assign, ":rotate_side", 80),
        (try_begin),
          (position_is_behind_position, 2, 1),
          (val_mul, ":rotate_side", -1),
        (try_end),
        (position_rotate_x, 1, ":rotate_side"),
        (prop_instance_animate_to_position, ":instance_no", 1, 70), #animate to position 1 in 0.7 second
        (val_add, "$tutorial_num_total_dummies_destroyed", 1),
        (play_sound, "snd_dummy_destroyed"),
    ]),
   (ti_on_scene_prop_hit,
    [
        (store_trigger_param_1, ":instance_no"),
        (store_trigger_param_2, ":damage"),
        (assign, reg60, ":damage"),
        (val_div, ":damage", 8),
        (prop_instance_get_position, pos2, ":instance_no"),
        (get_player_agent_no, ":player_agent"),
        (agent_get_position, pos3, ":player_agent"),
        (try_begin),
          (position_is_behind_position, pos3, pos2),
          (val_mul, ":damage", -1),
        (try_end),
        (position_rotate_x, 2, ":damage"),
        (display_message, "str_delivered_damage"),
        (prop_instance_animate_to_position, ":instance_no", 2, 30), #animate to position 1 in 0.3 second
        (play_sound, "snd_dummy_hit"),
        (particle_system_burst, "psys_dummy_smoke", pos1, 3),
        (particle_system_burst, "psys_dummy_straw", pos1, 10),
    ]),
  ]),

  ("band_a",0,"band_a","0", []),
  ("arena_sign",0,"arena_arms","0", []),

  ("castle_h_battlement_a",0,"castle_h_battlement_a","bo_castle_h_battlement_a", []),
  ("castle_h_battlement_b",0,"castle_h_battlement_b","bo_castle_h_battlement_b", []),
  ("castle_h_battlement_c",0,"castle_h_battlement_c","bo_castle_h_battlement_c", []),
  ("castle_h_battlement_a2",0,"castle_h_battlement_a2","bo_castle_h_battlement_a2", []),
  ("castle_h_battlement_b2",0,"castle_h_battlement_b2","bo_castle_h_battlement_b2", []),
  ("castle_h_corner_a",0,"castle_h_corner_a","bo_castle_h_corner_a", []),
  ("castle_h_corner_c",0,"castle_h_corner_c","bo_castle_h_corner_c", []),
  ("castle_h_stairs_a",sokf_type_ladder,"castle_h_stairs_a","bo_castle_h_stairs_a", []),
  ("castle_h_stairs_b",0,"castle_h_stairs_b","bo_castle_h_stairs_b", []),
  ("castle_h_gatehouse_a",0,"castle_h_gatehouse_a","bo_castle_h_gatehouse_a", []),
  ("castle_h_keep_a",0,"castle_h_keep_a","bo_castle_h_keep_a", []),
  ("castle_h_keep_b",0,"castle_h_keep_b","bo_castle_h_keep_b", []),
  ("castle_h_house_a",0,"castle_h_house_a","bo_castle_h_house_a", []),
  ("castle_h_house_b",0,"castle_h_house_b","bo_castle_h_house_b", []),
  ("castle_h_house_c",0,"castle_h_house_c","bo_castle_h_house_b", []),
  ("castle_h_battlement_barrier",0,"castle_h_battlement_barrier","bo_castle_h_battlement_barrier", []),




  ("full_keep_b",0,"full_keep_b","bo_full_keep_b", []),

  ("castle_f_keep_a",0,"castle_f_keep_a","bo_castle_f_keep_a", []),
  ("castle_f_battlement_a",0,"castle_f_battlement_a","bo_castle_f_battlement_a", []),
  ("castle_f_battlement_a_destroyed",0,"castle_f_battlement_a_destroyed","bo_castle_f_battlement_a_destroyed", []),
  ("castle_f_battlement_b",0,"castle_f_battlement_b","bo_castle_f_battlement_b", []),
  ("castle_f_battlement_c",0,"castle_f_battlement_c","bo_castle_f_battlement_c", []),
  ("castle_f_battlement_d",0,"castle_f_battlement_d","bo_castle_f_battlement_d", []),
  ("castle_f_battlement_e",0,"castle_f_battlement_e","bo_castle_f_battlement_e", []),
  ("castle_f_sally_port_elevation",0,"castle_f_sally_port_elevation","bo_castle_f_sally_port_elevation", []),
  ("castle_f_battlement_corner_a",0,"castle_f_battlement_corner_a","bo_castle_f_battlement_corner_a", []),
  ("castle_f_battlement_corner_b",0,"castle_f_battlement_corner_b","bo_castle_f_battlement_corner_b", []),
  ("castle_f_battlement_corner_c",0,"castle_f_battlement_corner_c","bo_castle_f_battlement_corner_c", []),
  
  ("castle_f_door_a",sokf_moveable|sokf_show_hit_point_bar|sokf_destructible|spr_use_time(0),"castle_f_door_a","bo_castle_f_door_a", [
    check_castle_door_use_trigger,

   (ti_on_init_scene_prop,
    [
      (store_trigger_param_1, ":instance_no"),
      (scene_prop_set_hit_points, ":instance_no", 1000),
    ]),
     
   (ti_on_scene_prop_destroy,
    [
      (play_sound, "snd_dummy_destroyed"),
      
      (assign, ":rotate_side", 86),
      
      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (store_trigger_param_1, ":instance_no"),      
        (store_trigger_param_2, ":attacker_agent_no"),

        (set_fixed_point_multiplier, 100),
        (prop_instance_get_position, pos1, ":instance_no"),

        (try_begin),
          (ge, ":attacker_agent_no", 0),
          (agent_get_position, pos2, ":attacker_agent_no"),
          (try_begin),
            (position_is_behind_position, pos2, pos1),
            (val_mul, ":rotate_side", -1),
          (try_end),
        (try_end),
      
        (init_position, pos3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (position_move_y, pos3, -100),
        (else_try),
          (position_move_y, pos3, 100),
        (try_end),
      
        (position_move_x, pos3, -50),
        (position_transform_position_to_parent, pos4, pos1, pos3),
        (position_move_z, pos4, 100),
        (position_get_distance_to_ground_level, ":height_to_terrain", pos4),
        (val_sub, ":height_to_terrain", 100),
        (assign, ":z_difference", ":height_to_terrain"),
        #(assign, reg0, ":z_difference"),
        #(display_message, "@{!}z dif : {reg0}"),
        (val_div, ":z_difference", 3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (val_add, ":rotate_side", ":z_difference"),
        (else_try),
          (val_sub, ":rotate_side", ":z_difference"),
        (try_end),

        (position_rotate_x, pos1, ":rotate_side"),
        (prop_instance_animate_to_position, ":instance_no", pos1, 70), #animate to position 1 in 0.7 second
      (try_end),
    ]),       
  
    (ti_on_scene_prop_hit,
    [
      (store_trigger_param_1, ":instance_no"),       
      (store_trigger_param_2, ":damage"),
      
      (try_begin),
        (scene_prop_get_hit_points, ":hit_points", ":instance_no"),
        (val_sub, ":hit_points", ":damage"),
        (gt, ":hit_points", 0),
        (play_sound, "snd_dummy_hit"),
      (else_try),
        (neg|multiplayer_is_server),
        (play_sound, "snd_dummy_destroyed"),
      (try_end),

      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (particle_system_burst, "psys_dummy_smoke", pos1, 3),
        (particle_system_burst, "psys_dummy_straw", pos1, 10),
      (try_end),      
    ]),
  ]),

  ("castle_f_doors_top_a",0,"castle_f_doors_top_a","bo_castle_f_doors_top_a", []),
    
  ("castle_f_sally_door_a",sokf_moveable|sokf_show_hit_point_bar|sokf_destructible|spr_use_time(0),"castle_f_sally_door_a","bo_castle_f_sally_door_a", [
    check_sally_door_use_trigger,

   (ti_on_init_scene_prop,
    [
      (store_trigger_param_1, ":instance_no"),
      (scene_prop_set_hit_points, ":instance_no", 1000),
    ]),
     
   (ti_on_scene_prop_destroy,
    [
      (play_sound, "snd_dummy_destroyed"),
      
      (assign, ":rotate_side", 86),
      
      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (store_trigger_param_1, ":instance_no"),      
        (store_trigger_param_2, ":attacker_agent_no"),

        (set_fixed_point_multiplier, 100),
        (prop_instance_get_position, pos1, ":instance_no"),

        (try_begin),
          (ge, ":attacker_agent_no", 0),
          (agent_get_position, pos2, ":attacker_agent_no"),
          (try_begin),
            (position_is_behind_position, pos2, pos1),
            (val_mul, ":rotate_side", -1),
          (try_end),
        (try_end),
      
        (init_position, pos3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (position_move_y, pos3, -100),
        (else_try),
          (position_move_y, pos3, 100),
        (try_end),
      
        (position_move_x, pos3, -50),
        (position_transform_position_to_parent, pos4, pos1, pos3),
        (position_move_z, pos4, 100),
        (position_get_distance_to_ground_level, ":height_to_terrain", pos4),
        (val_sub, ":height_to_terrain", 100),
        (assign, ":z_difference", ":height_to_terrain"),
        (val_div, ":z_difference", 3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (val_add, ":rotate_side", ":z_difference"),
        (else_try),
          (val_sub, ":rotate_side", ":z_difference"),
        (try_end),

        (position_rotate_x, pos1, ":rotate_side"),
        (prop_instance_animate_to_position, ":instance_no", pos1, 70), #animate to position 1 in 0.7 second
      (try_end),
    ]),       

    (ti_on_scene_prop_hit,
    [
      (store_trigger_param_1, ":instance_no"),       
      (store_trigger_param_2, ":damage"),
      
      (try_begin),
        (scene_prop_get_hit_points, ":hit_points", ":instance_no"),
        (val_sub, ":hit_points", ":damage"),
        (gt, ":hit_points", 0),
        (play_sound, "snd_dummy_hit"),
      (else_try),
        (neg|multiplayer_is_server),
        (play_sound, "snd_dummy_destroyed"),
      (try_end),

      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (particle_system_burst, "psys_dummy_smoke", pos1, 3),
        (particle_system_burst, "psys_dummy_straw", pos1, 10),
      (try_end),      
    ]),
  ]),

  ("castle_f_stairs_a",sokf_type_ladder,"castle_f_stairs_a","bo_castle_f_stairs_a", []),
  ("castle_f_tower_a",0,"castle_f_tower_a","bo_castle_f_tower_a", []),
  ("castle_f_wall_stairs_a",sokf_type_ladder,"castle_f_wall_stairs_a","bo_castle_f_wall_stairs_a", []),
  ("castle_f_wall_stairs_b",sokf_type_ladder,"castle_f_wall_stairs_b","bo_castle_f_wall_stairs_b", []),
  ("castle_f_wall_way_a",0,"castle_f_wall_way_a","bo_castle_f_wall_way_a", []),
  ("castle_f_wall_way_b",0,"castle_f_wall_way_b","bo_castle_f_wall_way_b", []),
  ("castle_f_gatehouse_a",0,"castle_f_gatehouse_a","bo_castle_f_gatehouse_a", []),

  ("castle_g_battlement_a",0,"castle_g_battlement_a","bo_castle_g_battlement_a", []),
  ("castle_g_battlement_a1",0,"castle_g_battlement_a1","bo_castle_g_battlement_a1", []),
  ("castle_g_battlement_c",0,"castle_g_battlement_c","bo_castle_g_battlement_c", []),
  ("castle_g_corner_a",0,"castle_g_corner_a","bo_castle_g_corner_a", []),
  ("castle_g_corner_c",0,"castle_g_corner_c","bo_castle_g_corner_c", []),  
  ("castle_g_tower_a",sokf_type_ladder,"castle_g_tower_a","bo_castle_g_tower_a", []),
  ("castle_g_gate_house",0,"castle_g_gate_house","bo_castle_g_gate_house", []),
  ("castle_g_gate_house_door_a",0,"castle_g_gate_house_door_a","bo_castle_g_gate_house_door_a", []),
  ("castle_g_gate_house_door_b",0,"castle_g_gate_house_door_b","bo_castle_g_gate_house_door_b", []),
  ("castle_g_square_keep_a",0,"castle_g_square_keep_a","bo_castle_g_square_keep_a", []),

  ("castle_i_battlement_a",0,"castle_i_battlement_a","bo_castle_i_battlement_a", []),
  ("castle_i_battlement_a1",0,"castle_i_battlement_a1","bo_castle_i_battlement_a1", []),
  ("castle_i_battlement_c",0,"castle_i_battlement_c","bo_castle_i_battlement_c", []),
  ("castle_i_corner_a",0,"castle_i_corner_a","bo_castle_i_corner_a", []),
  ("castle_i_corner_c",0,"castle_i_corner_c","bo_castle_i_corner_c", []),  
  ("castle_i_tower_a",sokf_type_ladder,"castle_i_tower_a","bo_castle_i_tower_a", []),
  ("castle_i_gate_house",0,"castle_i_gate_house","bo_castle_i_gate_house", []),
  ("castle_i_gate_house_door_a",0,"castle_i_gate_house_door_a","bo_castle_i_gate_house_door_a", []),
  ("castle_i_gate_house_door_b",0,"castle_i_gate_house_door_b","bo_castle_i_gate_house_door_b", []),
  ("castle_i_square_keep_a",0,"castle_i_square_keep_a","bo_castle_i_square_keep_a", []),





  ("mosque_a",0,"mosque_a","bo_mosque_a", []),
  ("stone_minaret_a",0,"stone_minaret_a","bo_stone_minaret_a", []),
  ("stone_house_a",0,"stone_house_a","bo_stone_house_a", []),
  ("stone_house_b",0,"stone_house_b","bo_stone_house_b", []),
  ("stone_house_c",0,"stone_house_c","bo_stone_house_c", []),
  ("stone_house_d",0,"stone_house_d","bo_stone_house_d", []),
  ("stone_house_e",0,"stone_house_e","bo_stone_house_e", []),
  ("stone_house_f",0,"stone_house_f","bo_stone_house_f", []),

  ("banner_pole", sokf_moveable, "banner_pole", "bo_banner_pole", []),

  ("custom_banner_01",0,"custom_banner_01","0",
   [
     (ti_on_init_scene_prop,
      [
        (party_get_slot, ":leader_troop", "$g_encountered_party", slot_town_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_scene_prop_set_tableau_material, "tableau_custom_banner_default", ":leader_troop"),
        (try_end),
        ]),
     ]),
  ("custom_banner_02",0,"custom_banner_02","0",
   [
     (ti_on_init_scene_prop,
      [
        (party_get_slot, ":leader_troop", "$g_encountered_party", slot_town_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_scene_prop_set_tableau_material, "tableau_custom_banner_default", ":leader_troop"),
        (try_end),
        ]),
     ]),

  ("banner_a",0,"banner_a01","0", []),
  ("banner_b",0,"banner_a02","0", []),
  ("banner_c",0,"banner_a03","0", []),
  ("banner_d",0,"banner_a04","0", []),
  ("banner_e",0,"banner_a05","0", []),
  ("banner_f",0,"banner_a06","0", []),
  ("banner_g",0,"banner_a07","0", []),
  ("banner_h",0,"banner_a08","0", []),
  ("banner_i",0,"banner_a09","0", []),
  ("banner_j",0,"banner_a10","0", []),
  ("banner_k",0,"banner_a11","0", []),
  ("banner_l",0,"banner_a12","0", []),
  ("banner_m",0,"banner_a13","0", []),
  ("banner_n",0,"banner_a14","0", []),
  ("banner_o",0,"banner_f21","0", []),
  ("banner_p",0,"banner_a16","0", []),
  ("banner_q",0,"banner_a17","0", []),
  ("banner_r",0,"banner_a18","0", []),
  ("banner_s",0,"banner_a19","0", []),
  ("banner_t",0,"banner_a20","0", []),
  ("banner_u",0,"banner_a21","0", []),
  ("banner_ba",0,"banner_b01","0", []),
  ("banner_bb",0,"banner_b02","0", []),
  ("banner_bc",0,"banner_b03","0", []),
  ("banner_bd",0,"banner_b04","0", []),
  ("banner_be",0,"banner_b05","0", []),
  ("banner_bf",0,"banner_b06","0", []),
  ("banner_bg",0,"banner_b07","0", []),
  ("banner_bh",0,"banner_b08","0", []),
  ("banner_bi",0,"banner_b09","0", []),
  ("banner_bj",0,"banner_b10","0", []),
  ("banner_bk",0,"banner_b11","0", []),
  ("banner_bl",0,"banner_b12","0", []),
  ("banner_bm",0,"banner_b13","0", []),
  ("banner_bn",0,"banner_b14","0", []),
  ("banner_bo",0,"banner_b15","0", []),
  ("banner_bp",0,"banner_b16","0", []),
  ("banner_bq",0,"banner_b17","0", []),
  ("banner_br",0,"banner_b18","0", []),
  ("banner_bs",0,"banner_b19","0", []),
  ("banner_bt",0,"banner_b20","0", []),
  ("banner_bu",0,"banner_b21","0", []),
  ("banner_ca",0,"banner_c01","0", []),
  ("banner_cb",0,"banner_c02","0", []),
  ("banner_cc",0,"banner_c03","0", []),
  ("banner_cd",0,"banner_c04","0", []),
  ("banner_ce",0,"banner_c05","0", []),
  ("banner_cf",0,"banner_c06","0", []),
  ("banner_cg",0,"banner_c07","0", []),
  ("banner_ch",0,"banner_c08","0", []),
  ("banner_ci",0,"banner_c09","0", []),
  ("banner_cj",0,"banner_c10","0", []),
  ("banner_ck",0,"banner_c11","0", []),
  ("banner_cl",0,"banner_c12","0", []),
  ("banner_cm",0,"banner_c13","0", []),
  ("banner_cn",0,"banner_c14","0", []),
  ("banner_co",0,"banner_c15","0", []),
  ("banner_cp",0,"banner_c16","0", []),
  ("banner_cq",0,"banner_c17","0", []),
  ("banner_cr",0,"banner_c18","0", []),
  ("banner_cs",0,"banner_c19","0", []),
  ("banner_ct",0,"banner_c20","0", []),
  ("banner_cu",0,"banner_c21","0", []),
  ("banner_da",0,"banner_d01","0", []),
  ("banner_db",0,"banner_d02","0", []),
  ("banner_dc",0,"banner_d03","0", []),
  ("banner_dd",0,"banner_d04","0", []),
  ("banner_de",0,"banner_d05","0", []),
  ("banner_df",0,"banner_d06","0", []),
  ("banner_dg",0,"banner_d07","0", []),
  ("banner_dh",0,"banner_d08","0", []),
  ("banner_di",0,"banner_d09","0", []),
  ("banner_dj",0,"banner_d10","0", []),
  ("banner_dk",0,"banner_d11","0", []),
  ("banner_dl",0,"banner_d12","0", []),
  ("banner_dm",0,"banner_d13","0", []),
  ("banner_dn",0,"banner_d14","0", []),
  ("banner_do",0,"banner_d15","0", []),
  ("banner_dp",0,"banner_d16","0", []),
  ("banner_dq",0,"banner_d17","0", []),
  ("banner_dr",0,"banner_d18","0", []),
  ("banner_ds",0,"banner_d19","0", []),
  ("banner_dt",0,"banner_d20","0", []),
  ("banner_du",0,"banner_d21","0", []),
  ("banner_ea",0,"banner_e01","0", []),
  ("banner_eb",0,"banner_e02","0", []),
  ("banner_ec",0,"banner_e03","0", []),
  ("banner_ed",0,"banner_e04","0", []),
  ("banner_ee",0,"banner_e05","0", []),
  ("banner_ef",0,"banner_e06","0", []),
  ("banner_eg",0,"banner_e07","0", []),
  ("banner_eh",0,"banner_e08","0", []),
  ("banner_ei",0,"banner_e09","0", []),
  ("banner_ej",0,"banner_e10","0", []),
  ("banner_ek",0,"banner_e11","0", []),
  ("banner_el",0,"banner_e12","0", []),
  ("banner_em",0,"banner_e13","0", []),
  ("banner_en",0,"banner_e14","0", []),
  ("banner_eo",0,"banner_e15","0", []),
  ("banner_ep",0,"banner_e16","0", []),
  ("banner_eq",0,"banner_e17","0", []),
  ("banner_er",0,"banner_e18","0", []),
  ("banner_es",0,"banner_e19","0", []),
  ("banner_et",0,"banner_e20","0", []),
  ("banner_eu",0,"banner_e21","0", []),

  ("banner_f01", 0, "banner_f01", "0", []),
  ("banner_f02", 0, "banner_f02", "0", []),
  ("banner_f03", 0, "banner_f03", "0", []),
  ("banner_f04", 0, "banner_f04", "0", []),
  ("banner_f05", 0, "banner_f05", "0", []),
  ("banner_f06", 0, "banner_f06", "0", []),
  ("banner_f07", 0, "banner_f07", "0", []),
  ("banner_f08", 0, "banner_f08", "0", []),
  ("banner_f09", 0, "banner_f09", "0", []),
  ("banner_f10", 0, "banner_f10", "0", []),
  ("banner_f11", 0, "banner_f11", "0", []),
  ("banner_f12", 0, "banner_f12", "0", []),
  ("banner_f13", 0, "banner_f13", "0", []),
  ("banner_f14", 0, "banner_f14", "0", []),
  ("banner_f15", 0, "banner_f15", "0", []),
  ("banner_f16", 0, "banner_f16", "0", []),
  ("banner_f17", 0, "banner_f17", "0", []),
  ("banner_f18", 0, "banner_f18", "0", []),
  ("banner_f19", 0, "banner_f19", "0", []),
  ("banner_f20", 0, "banner_f20", "0", []),
 
  ("banner_g01", 0, "banner_f01", "0", []),
  ("banner_g02", 0, "banner_f02", "0", []),
  ("banner_g03", 0, "banner_f03", "0", []),
  ("banner_g04", 0, "banner_f04", "0", []),
  ("banner_g05", 0, "banner_f05", "0", []),
  ("banner_g06", 0, "banner_f06", "0", []),
  ("banner_g07", 0, "banner_f07", "0", []),
  ("banner_g08", 0, "banner_f08", "0", []),
  ("banner_g09", 0, "banner_f09", "0", []),
  ("banner_g10", 0, "banner_f10", "0", []),

  ("banner_kingdom_a", 0, "banner_kingdom_a", "0", []),
  ("banner_kingdom_b", 0, "banner_kingdom_b", "0", []),
  ("banner_kingdom_c", 0, "banner_kingdom_c", "0", []),
  ("banner_kingdom_d", 0, "banner_kingdom_d", "0", []),
  ("banner_kingdom_e", 0, "banner_kingdom_e", "0", []),
  ("banner_kingdom_f", 0, "banner_kingdom_f", "0", []),
  ("banner_f21", 0, "banner_a15", "0", []),

  ("tavern_chair_a",0,"tavern_chair_a","bo_tavern_chair_a", []),
  ("tavern_chair_b",0,"tavern_chair_b","bo_tavern_chair_b", []),
  ("tavern_table_a",0,"tavern_table_a","bo_tavern_table_a", []),
  ("tavern_table_b",0,"tavern_table_b","bo_tavern_table_b", []),
  ("fireplace_a",0,"fireplace_a","bo_fireplace_a", []),
  ("barrel",0,"barrel","bobarrel", []),
  ("bench_tavern",0,"bench_tavern","bobench_tavern", []),
  ("bench_tavern_b",0,"bench_tavern_b","bo_bench_tavern_b", []),
  ("bowl_wood",0,"bowl_wood","0", []),
  ("chandelier_table",0,"chandelier_table","0", []),
  ("chandelier_tavern",0,"chandelier_tavern","0", []),
  ("chest_gothic",0,"chest_gothic","bochest_gothic", []),
  ("chest_b",0,"chest_b","bo_chest_b", []),
  ("chest_c",0,"chest_c","bo_chest_c", []),
  ("counter_tavern",0,"counter_tavern","bocounter_tavern", []),
  ("cup",0,"cup","0", []),
  ("dish_metal",0,"dish_metal","0", []),
  ("gothic_chair",0,"gothic_chair","bogothic_chair", []),
  ("gothic_stool",0,"gothic_stool","bogothic_stool", []),
  ("grate",0,"grate","bograte", []),
  ("jug",0,"jug","0", []),
  ("potlamp",0,"potlamp","0", []),
  ("weapon_rack",0,"weapon_rack","boweapon_rack", []),
  ("weapon_rack_big",0,"weapon_rack_big","boweapon_rack_big", []),
  ("tavern_barrel",0,"barrel","bobarrel", []),
  ("tavern_barrel_b",0,"tavern_barrel_b","bo_tavern_barrel_b", []),
  ("merchant_sign",0,"merchant_sign","bo_tavern_sign", []),
  ("tavern_sign",0,"tavern_sign","bo_tavern_sign", []),
  ("sack",0,"sack","0", []),
  ("skull_a",0,"skull_a","0", []),
  ("skull_b",0,"skull_b","0", []),
  ("skull_c",0,"skull_c","0", []),
  ("skull_d",0,"skull_d","0", []),
  ("skeleton_cow",0,"skeleton_cow","0", []),
  ("cupboard_a",0,"cupboard_a","bo_cupboard_a", []),
  ("box_a",0,"box_a","bo_box_a", []),
  ("bucket_a",0,"bucket_a","bo_bucket_a", []),
  ("straw_a",0,"straw_a","0", []),
  ("straw_b",0,"straw_b","0", []),
  ("straw_c",0,"straw_c","0", []),
  ("cloth_a",0,"cloth_a","0", []),
  ("cloth_b",0,"cloth_b","0", []),
  ("mat_a",0,"mat_a","0", []),
  ("mat_b",0,"mat_b","0", []),
  ("mat_c",0,"mat_c","0", []),
  ("mat_d",0,"mat_d","0", []),

  ("wood_a",0,"wood_a","bo_wood_a", []),
  ("wood_b",0,"wood_b","bo_wood_b", []),
  ("wood_heap",0,"wood_heap_a","bo_wood_heap_a", []),
  ("wood_heap_b",0,"wood_heap_b","bo_wood_heap_b", []),
  ("water_well_a",0,"water_well_a","bo_water_well_a", []),
  ("net_a",0,"net_a","bo_net_a", []),
  ("net_b",0,"net_b","0", []),

  ("meat_hook",0,"meat_hook","0", []),
  ("cooking_pole",0,"cooking_pole","0", []),
  ("bowl_a",0,"bowl_a","0", []),
  ("bucket_b",0,"bucket_b","0", []),
  ("washtub_a",0,"washtub_a","bo_washtub_a", []),
  ("washtub_b",0,"washtub_b","bo_washtub_b", []),

  ("table_trunk_a",0,"table_trunk_a","bo_table_trunk_a", []),
  ("chair_trunk_a",0,"chair_trunk_a","bo_chair_trunk_a", []),
  ("chair_trunk_b",0,"chair_trunk_b","bo_chair_trunk_b", []),
  ("chair_trunk_c",0,"chair_trunk_c","bo_chair_trunk_c", []),

  ("table_trestle_long",0,"table_trestle_long","bo_table_trestle_long", []),
  ("table_trestle_small",0,"table_trestle_small","bo_table_trestle_small", []),
  ("chair_trestle",0,"chair_trestle","bo_chair_trestle", []),

  ("wheel",0,"wheel","bo_wheel", []),
  ("ladder",sokf_type_ladder,"ladder","boladder", []),
  ("cart",0,"cart","bo_cart", []),
  ("village_stand",0,"village_stand","bovillage_stand", []),
  ("wooden_stand",0,"wooden_stand","bowooden_stand", []),
  ("table_small",0,"table_small","bo_table_small", []),
  ("table_small_b",0,"table_small_b","bo_table_small_b", []),
  ("small_timber_frame_house_a",0,"small_timber_frame_house_a","bo_small_timber_frame_house_a", []),
  ("timber_frame_house_b",0,"tf_house_b","bo_tf_house_b", []),
  ("timber_frame_house_c",0,"tf_house_c","bo_tf_house_c", []),
  ("timber_frame_extension_a",0,"timber_frame_extension_a","bo_timber_frame_extension_a", []),
  ("timber_frame_extension_b",0,"timber_frame_extension_b","bo_timber_frame_extension_b", []),
  ("stone_stairs_a",sokf_type_ladder,"stone_stairs_a","bo_stone_stairs_a", []),
  ("stone_stairs_b",sokf_type_ladder,"stone_stairs_b","bo_stone_stairs_b", []),
  ("railing_a",0,"railing_a","bo_railing_a", []),
  ("side_building_a",0,"side_building_a","bo_side_building_a", []),
  ("battlement_a",0,"battlement_a","bo_battlement_a", []),

  ("battlement_a_destroyed",0,"battlement_a_destroyed","bo_battlement_a_destroyed", []),


  ("round_tower_a",0,"round_tower_a","bo_round_tower_a", []),
  ("small_round_tower_a",0,"small_round_tower_a","bo_small_round_tower_a", []),
  ("small_round_tower_roof_a",0,"small_round_tower_roof_a","bo_small_round_tower_roof_a", []),
  ("square_keep_a",0,"square_keep_a","bo_square_keep_a", []),
  ("square_tower_roof_a",0,"square_tower_roof_a","0", []),
  ("gate_house_a",0,"gate_house_a","bo_gate_house_a", []),
  ("gate_house_b",0,"gate_house_b","bo_gate_house_b", []),
  ("small_wall_a",0,"small_wall_a","bo_small_wall_a", []),
  ("small_wall_b",0,"small_wall_b","bo_small_wall_b", []),
  ("small_wall_c",0,"small_wall_c","bo_small_wall_c", []),
  ("small_wall_c_destroy",0,"small_wall_c_destroy","bo_small_wall_c_destroy", []),
  ("small_wall_d",0,"small_wall_d","bo_small_wall_d", []),
  ("small_wall_e",0,"small_wall_e","bo_small_wall_d", []),
  ("small_wall_f",0,"small_wall_f","bo_small_wall_f", []),
  ("small_wall_f2",0,"small_wall_f2","bo_small_wall_f2", []),


  ("town_house_a",0,"town_house_a","bo_town_house_a", []),
  ("town_house_b",0,"town_house_b","bo_town_house_b", []),
  ("town_house_c",0,"town_house_c","bo_town_house_c", []),
  ("town_house_d",0,"town_house_d","bo_town_house_d", []),
  ("town_house_e",0,"town_house_e","bo_town_house_e", []),
  ("town_house_f",0,"town_house_f","bo_town_house_f", []),
  ("town_house_g",0,"town_house_g","bo_town_house_g", []),
  ("town_house_h",0,"town_house_h","bo_town_house_h", []),
  ("town_house_i",0,"town_house_i","bo_town_house_i", []),
  ("town_house_j",0,"town_house_j","bo_town_house_j", []),
  ("town_house_l",0,"town_house_l","bo_town_house_l", []),

  ("town_house_m",0,"town_house_m","bo_town_house_m", []),
  ("town_house_n",0,"town_house_n","bo_town_house_n", []),
  ("town_house_o",0,"town_house_o","bo_town_house_o", []),
  ("town_house_p",0,"town_house_p","bo_town_house_p", []),
  ("town_house_q",0,"town_house_q","bo_town_house_q", []),
  
  ("passage_house_a",0,"passage_house_a","bo_passage_house_a", []),
  ("passage_house_b",0,"passage_house_b","bo_passage_house_b", []),
  ("passage_house_c",0,"passage_house_c","bo_passage_house_c", []),
  ("passage_house_d",0,"passage_house_d","bo_passage_house_d", []),
  ("passage_house_c_door",0,"passage_house_c_door","bo_passage_house_c_door", []),

  ("house_extension_a",0,"house_extension_a","bo_house_extension_a", []),
  ("house_extension_b",0,"house_extension_b","bo_house_extension_b", []),
  ("house_extension_c",0,"house_extension_c","bo_house_extension_a", []),#reuse 
  ("house_extension_d",0,"house_extension_d","bo_house_extension_d", []),

  ("house_extension_e",0,"house_extension_e","bo_house_extension_e", []),
  ("house_extension_f",0,"house_extension_f","bo_house_extension_f", []),
  ("house_extension_f2",0,"house_extension_f2","bo_house_extension_f", []),
  ("house_extension_g",0,"house_extension_g","bo_house_extension_g", []),
  ("house_extension_g2",0,"house_extension_g2","bo_house_extension_g", []),
  ("house_extension_h",0,"house_extension_h","bo_house_extension_h", []),
  ("house_extension_i",0,"house_extension_i","bo_house_extension_i", []),

  ("house_roof_door",0,"house_roof_door","bo_house_roof_door", []),


  ("door_extension_a",0,"door_extension_a","bo_door_extension_a", []),
  ("stairs_arch_a",sokf_type_ladder,"stairs_arch_a","bo_stairs_arch_a", []),

  ("town_house_r",0,"town_house_r","bo_town_house_r", []),
  ("town_house_s",0,"town_house_s","bo_town_house_s", []),
  ("town_house_t",0,"town_house_t","bo_town_house_t", []),
  ("town_house_u",0,"town_house_u","bo_town_house_u", []),
  ("town_house_v",0,"town_house_v","bo_town_house_v", []),
  ("town_house_w",0,"town_house_w","bo_town_house_w", []),

  ("town_house_y",0,"town_house_y","bo_town_house_y", []),
  ("town_house_z",0,"town_house_z","bo_town_house_z", []),
  ("town_house_za",0,"town_house_za","bo_town_house_za", []),
  
  ("windmill",0,"windmill","bo_windmill", []),
  ("windmill_fan_turning",sokf_moveable,"windmill_fan_turning","bo_windmill_fan_turning", []),
  ("windmill_fan",0,"windmill_fan","bo_windmill_fan", []),
  ("fake_house_a",0,"fake_house_a","bo_fake_house_a", []),
  ("fake_house_b",0,"fake_house_b","bo_fake_house_b", []),
  ("fake_house_c",0,"fake_house_c","bo_fake_house_c", []),
  ("fake_house_d",0,"fake_house_d","bo_fake_house_d", []),
  ("fake_house_e",0,"fake_house_e","bo_fake_house_e", []),
  ("fake_house_f",0,"fake_house_f","bo_fake_house_f", []),

  ("fake_house_snowy_a",0,"fake_house_snowy_a","bo_fake_house_a", []),
  ("fake_house_snowy_b",0,"fake_house_snowy_b","bo_fake_house_b", []),
  ("fake_house_snowy_c",0,"fake_house_snowy_c","bo_fake_house_c", []),
  ("fake_house_snowy_d",0,"fake_house_snowy_d","bo_fake_house_d", []),


  ("fake_house_far_a",0,"fake_house_far_a","0", []),
  ("fake_house_far_b",0,"fake_house_far_b","0", []),
  ("fake_house_far_c",0,"fake_house_far_c","0", []),
  ("fake_house_far_d",0,"fake_house_far_d","0", []),
  ("fake_house_far_e",0,"fake_house_far_e","0", []),
  ("fake_house_far_f",0,"fake_house_far_f","0", []),

  ("fake_house_far_snowycrude_a",0,"fake_house_far_snowy_a","0", []),
  ("fake_house_far_snowy_b",0,"fake_house_far_snowy_b","0", []),
  ("fake_house_far_snowy_c",0,"fake_house_far_snowy_c","0", []),
  ("fake_house_far_snowy_d",0,"fake_house_far_snowy_d","0", []),

  ("earth_wall_a",0,"earth_wall_a","bo_earth_wall_a", []),
  ("earth_wall_a2",0,"earth_wall_a2","bo_earth_wall_a2", []),
  ("earth_wall_b",0,"earth_wall_b","bo_earth_wall_b", []),
  ("earth_wall_b2",0,"earth_wall_b2","bo_earth_wall_b2", []),
  ("earth_stairs_a",sokf_type_ladder,"earth_stairs_a","bo_earth_stairs_a", []),
  ("earth_stairs_b",sokf_type_ladder,"earth_stairs_b","bo_earth_stairs_b", []),
  ("earth_tower_small_a",0,"earth_tower_small_a","bo_earth_tower_small_a", []),
  ("earth_gate_house_a",0,"earth_gate_house_a","bo_earth_gate_house_a", []),
  ("earth_gate_a",0,"earth_gate_a","bo_earth_gate_a", []),
  ("earth_square_keep_a",0,"earth_square_keep_a","bo_earth_square_keep_a", []),
  ("earth_house_a",0,"earth_house_a","bo_earth_house_a", []),
  ("earth_house_b",0,"earth_house_b","bo_earth_house_b", []),
  ("earth_house_c",0,"earth_house_c","bo_earth_house_c", []),
  ("earth_house_d",0,"earth_house_d","bo_earth_house_d", []),

  ("village_steppe_a",0,"village_steppe_a","bo_village_steppe_a", []),
  ("village_steppe_b",0,"village_steppe_b","bo_village_steppe_b", []),
  ("village_steppe_c",0,"village_steppe_c","bo_village_steppe_c", []),
  ("village_steppe_d",0,"village_steppe_d","bo_village_steppe_d", []),
  ("village_steppe_e",0,"village_steppe_e","bo_village_steppe_e", []),
  ("village_steppe_f",0,"village_steppe_f","bo_village_steppe_f", []),
  ("town_house_aa",0,"town_house_aa","bo_town_house_aa", []),
  
  
  ("snowy_house_a",0,"snowy_house_a","bo_snowy_house_a", []),
  ("snowy_house_b",0,"snowy_house_b","bo_snowy_house_b", []),
  ("snowy_house_c",0,"snowy_house_c","bo_snowy_house_c", []),
  ("snowy_house_d",0,"snowy_house_d","bo_snowy_house_d", []),
  ("snowy_house_e",0,"snowy_house_e","bo_snowy_house_e", []),
  ("snowy_house_f",0,"snowy_house_f","bo_snowy_house_f", []),
  ("snowy_house_g",0,"snowy_house_g","bo_snowy_house_g", []),
  ("snowy_house_h",0,"snowy_house_h","bo_snowy_house_h", []),
  ("snowy_house_i",0,"snowy_house_i","bo_snowy_house_i", []),
  ("snowy_wall_a",0,"snowy_wall_a","bo_snowy_wall_a", []),

  ("snowy_stand",0,"snowy_stand","bo_snowy_stand", []),

  ("snowy_heap_a",0,"snowy_heap_a","bo_snowy_heap_a", []),
  ("snowy_trunks_a",0,"snowy_trunks_a","bo_snowy_trunks_a", []),

  ("snowy_castle_tower_a",0,"snowy_castle_tower_a","bo_snowy_castle_tower_a", []),
  ("snowy_castle_battlement_a",0,"snowy_castle_battlement_a","bo_snowy_castle_battlement_a", []),
  ("snowy_castle_battlement_a_destroyed",0,"snowy_castle_battlement_a_destroyed","bo_snowy_castle_battlement_a_destroyed", []),
 
  ("snowy_castle_battlement_b",0,"snowy_castle_battlement_b","bo_snowy_castle_battlement_b", []),
  ("snowy_castle_battlement_corner_a",0,"snowy_castle_battlement_corner_a","bo_snowy_castle_battlement_corner_a", []),
  ("snowy_castle_battlement_corner_b",0,"snowy_castle_battlement_corner_b","bo_snowy_castle_battlement_corner_b", []),
  ("snowy_castle_battlement_corner_c",0,"snowy_castle_battlement_corner_c","bo_snowy_castle_battlement_corner_c", []),
  ("snowy_castle_battlement_stairs_a",0,"snowy_castle_battlement_stairs_a","bo_snowy_castle_battlement_stairs_a", []),
  ("snowy_castle_battlement_stairs_b",0,"snowy_castle_battlement_stairs_b","bo_snowy_castle_battlement_stairs_b", []),
  ("snowy_castle_gate_house_a",0,"snowy_castle_gate_house_a","bo_snowy_castle_gate_house_a", []),
  ("snowy_castle_round_tower_a",0,"snowy_castle_round_tower_a","bo_snowy_castle_round_tower_a", []),
  ("snowy_castle_square_keep_a",0,"snowy_castle_square_keep_a","bo_snowy_castle_square_keep_a", []),
  ("snowy_castle_stairs_a",sokf_type_ladder,"snowy_castle_stairs_a","bo_snowy_castle_stairs_a", []),

  ("square_keep_b",0,"square_keep_b","bo_square_keep_b", []),
  ("square_keep_c",0,"square_keep_c","bo_square_keep_c", []),
  ("square_keep_d",0,"square_keep_d","bo_square_keep_d", []),
  ("square_keep_e",0,"square_keep_e","bo_square_keep_e", []),
  ("square_keep_f",0,"square_keep_f","bo_square_keep_f", []),


  ("square_extension_a",0,"square_extension_a","bo_square_extension_a", []),
  ("square_stairs_a",0,"square_stairs_a","bo_square_stairs_a", []),

  ("castle_courtyard_house_a",0,"castle_courtyard_house_a","bo_castle_courtyard_house_a", []),
  ("castle_courtyard_house_b",0,"castle_courtyard_house_b","bo_castle_courtyard_house_b", []),
  ("castle_courtyard_house_c",0,"castle_courtyard_house_c","bo_castle_courtyard_house_c", []),
  ("castle_courtyard_a",0,"castle_courtyard_a","bo_castle_courtyard_a", []),

  ("gatehouse_b",0,"gatehouse_b","bo_gatehouse_b", []),
  ("castle_gaillard",0,"castle_gaillard","bo_castle_gaillard", []),
  
  ("castle_e_battlement_a",0,"castle_e_battlement_a","bo_castle_e_battlement_a", []),
  ("castle_e_battlement_c",0,"castle_e_battlement_c","bo_castle_e_battlement_c", []),
  ("castle_e_battlement_a_destroyed",0,"castle_e_battlement_a_destroyed","bo_castle_e_battlement_a_destroyed", []),

  ("castle_e_sally_door_a",sokf_moveable|sokf_show_hit_point_bar|sokf_destructible|spr_use_time(0),"castle_e_sally_door_a","bo_castle_e_sally_door_a", [
    check_sally_door_use_trigger,

   (ti_on_init_scene_prop,
    [
      (store_trigger_param_1, ":instance_no"),
      (scene_prop_set_hit_points, ":instance_no", 3000),
    ]),
     
##   (ti_on_scene_prop_destroy,
##    [
##      (play_sound, "snd_dummy_destroyed"),
##      
##      (try_begin),
##        (multiplayer_is_server),
##        (store_trigger_param_1, ":instance_no"),      
##        (store_trigger_param_2, ":attacker_agent_no"),
##
##        (try_begin),
##          (ge, ":attacker_agent_no", 0),
##          (prop_instance_get_position, pos1, ":instance_no"),
##          (agent_get_position, pos2, ":attacker_agent_no"),
##          (assign, ":rotate_side", 80),
##          (try_begin),
##            (position_is_behind_position, pos2, pos1),
##            (val_mul, ":rotate_side", -1),
##          (try_end),
##        (else_try),
##          (assign, ":rotate_side", 80),
##        (try_end),
##      
##        (position_rotate_x, pos1, ":rotate_side"),
##        (prop_instance_animate_to_position, ":instance_no", pos1, 70), #animate to position 1 in 0.7 second
##      (try_end),
##    ]),     

   (ti_on_scene_prop_destroy,
    [
      (play_sound, "snd_dummy_destroyed"),
      
      (assign, ":rotate_side", 86),
      
      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),
		
        (store_trigger_param_1, ":instance_no"),      
        (store_trigger_param_2, ":attacker_agent_no"),

        (set_fixed_point_multiplier, 100),
        (prop_instance_get_position, pos1, ":instance_no"),

        (try_begin),
          (ge, ":attacker_agent_no", 0),
          (agent_get_position, pos2, ":attacker_agent_no"),
          (try_begin),
            (position_is_behind_position, pos2, pos1),
            (val_mul, ":rotate_side", -1),
          (try_end),
        (try_end),
      
        (init_position, pos3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (position_move_y, pos3, -100),
        (else_try),
          (position_move_y, pos3, 100),
        (try_end),
      
        (position_move_x, pos3, -50),
        (position_transform_position_to_parent, pos4, pos1, pos3),
        (position_move_z, pos4, 100),
        (position_get_distance_to_ground_level, ":height_to_terrain", pos4),
        (val_sub, ":height_to_terrain", 100),
        (assign, ":z_difference", ":height_to_terrain"),
        #(assign, reg0, ":z_difference"),
        #(display_message, "@{!}z dif : {reg0}"),
        (val_div, ":z_difference", 3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (val_add, ":rotate_side", ":z_difference"),
        (else_try),
          (val_sub, ":rotate_side", ":z_difference"),
        (try_end),

        (position_rotate_x, pos1, ":rotate_side"),
        (prop_instance_animate_to_position, ":instance_no", pos1, 70), #animate to position 1 in 0.7 second
      (try_end),
    ]),       

    (ti_on_scene_prop_hit,
    [
      (store_trigger_param_1, ":instance_no"),       
      (store_trigger_param_2, ":damage"),
      
      (try_begin),
        (scene_prop_get_hit_points, ":hit_points", ":instance_no"),
        (val_sub, ":hit_points", ":damage"),
        (gt, ":hit_points", 0),
        (play_sound, "snd_dummy_hit"),
      (else_try),
        (neg|multiplayer_is_server),
        (play_sound, "snd_dummy_destroyed"),
      (try_end),

      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (particle_system_burst, "psys_dummy_smoke", pos1, 3),
        (particle_system_burst, "psys_dummy_straw", pos1, 10),
      (try_end),      
    ]),
  ]),

  ("castle_e_corner",0,"castle_e_corner","bo_castle_e_corner", []),
  ("castle_e_corner_b",0,"castle_e_corner_b","bo_castle_e_corner_b", []),
  ("castle_e_corner_c",0,"castle_e_corner_c","bo_castle_e_corner_c", []),
  ("castle_e_stairs_a",0,"castle_e_stairs_a","bo_castle_e_stairs_a", []),
  ("castle_e_tower",0,"castle_e_tower","bo_castle_e_tower", []),
  ("castle_e_gate_house_a",0,"castle_e_gate_house_a","bo_castle_e_gate_house_a", []),
  ("castle_e_keep_a",0,"castle_e_keep_a","bo_castle_e_keep_a", []),
  ("stand_thatched",0,"stand_thatched","bo_stand_thatched", []),
  ("stand_cloth",0,"stand_cloth","bo_stand_cloth", []),
  ("castle_e_house_a",0,"castle_e_house_a","bo_castle_e_house_a", []),
  ("castle_e_house_b",0,"castle_e_house_b","bo_castle_e_house_b", []),

  
  ("arena_block_a",0,"arena_block_a","bo_arena_block_ab", []),
  ("arena_block_b",0,"arena_block_b","bo_arena_block_ab", []),
  ("arena_block_c",0,"arena_block_c","bo_arena_block_c", []),
  ("arena_block_d",0,"arena_block_d","bo_arena_block_def", []),
  ("arena_block_e",0,"arena_block_e","bo_arena_block_def", []),
  ("arena_block_f",0,"arena_block_f","bo_arena_block_def", []),
  ("arena_block_g",0,"arena_block_g","bo_arena_block_ghi", []),
  ("arena_block_h",0,"arena_block_h","bo_arena_block_ghi", []),
  ("arena_block_i",0,"arena_block_i","bo_arena_block_ghi", []),

  ("arena_block_j",0,"arena_block_j","bo_arena_block_j", []),
  ("arena_block_j_awning",0,"arena_block_j_awning","bo_arena_block_j_awning", []),



  ("arena_palisade_a",0,"arena_palisade_a","bo_arena_palisade_a", []),
  ("arena_wall_a",0,"arena_wall_a","bo_arena_wall_ab", []),
  ("arena_wall_b",0,"arena_wall_b","bo_arena_wall_ab", []),
  ("arena_barrier_a",0,"arena_barrier_a","bo_arena_barrier_a", []),
  ("arena_barrier_b",0,"arena_barrier_b","bo_arena_barrier_bc", []),
  ("arena_barrier_c",0,"arena_barrier_c","bo_arena_barrier_bc", []),
  ("arena_tower_a",0,"arena_tower_a","bo_arena_tower_abc", []),
  ("arena_tower_b",0,"arena_tower_b","bo_arena_tower_abc", []),
  ("arena_tower_c",0,"arena_tower_c","bo_arena_tower_abc", []),
  ("arena_spectator_a",0,"spectator_standing1","0", []),
  ("arena_spectator_b",0,"spectator_standing2","0", []),
  ("arena_spectator_c",0,"spectator_standing3","0", []),
  ("arena_spectator_sitting_a",0,"spectator_sitting1","0", []),
  ("arena_spectator_sitting_b",0,"spectator_sitting2","0", []),
  ("arena_spectator_sitting_c",0,"spectator_sitting3","0", []),


  ("courtyard_gate_a",0,"courtyard_entry_a","bo_courtyard_entry_a", []),
  ("courtyard_gate_b",0,"courtyard_entry_b","bo_courtyard_entry_b", []),
  ("courtyard_gate_c",0,"courtyard_entry_c","bo_courtyard_entry_c", []),
  ("courtyard_gate_snowy",0,"courtyard_entry_snowy","bo_courtyard_entry_a", []),

  ("castle_tower_a",0,"castle_tower_a","bo_castle_tower_a", []),
  ("castle_battlement_a",0,"castle_battlement_a","bo_castle_battlement_a", []),
  ("castle_battlement_b",0,"castle_battlement_b","bo_castle_battlement_b", []),
  ("castle_battlement_c",0,"castle_battlement_c","bo_castle_battlement_c", []),

  ("castle_battlement_a_destroyed",0,"castle_battlement_a_destroyed","bo_castle_battlement_a_destroyed", []),
  ("castle_battlement_b_destroyed",0,"castle_battlement_b_destroyed","bo_castle_battlement_b_destroyed", []),

  ("castle_battlement_corner_a",0,"castle_battlement_corner_a","bo_castle_battlement_corner_a", []),
  ("castle_battlement_corner_b",0,"castle_battlement_corner_b","bo_castle_battlement_corner_b", []),
  ("castle_battlement_corner_c",0,"castle_battlement_corner_c","bo_castle_battlement_corner_c", []),
  ("castle_battlement_stairs_a",0,"castle_battlement_stairs_a","bo_castle_battlement_stairs_a", []),
  ("castle_battlement_stairs_b",0,"castle_battlement_stairs_b","bo_castle_battlement_stairs_b", []),
  ("castle_gate_house_a",0,"castle_gate_house_a","bo_castle_gate_house_a", []),
  ("castle_round_tower_a",0,"castle_round_tower_a","bo_castle_round_tower_a", []),
  ("castle_square_keep_a",0,"castle_square_keep_a","bo_castle_square_keep_a", []),
  ("castle_stairs_a",sokf_type_ladder,"castle_stairs_a","bo_castle_stairs_a", []),

  ("castle_drawbridge_open",0,"castle_drawbridges_open","bo_castle_drawbridges_open", []),
  ("castle_drawbridge_closed",0,"castle_drawbridges_closed","bo_castle_drawbridges_closed", []),
  ("spike_group_a",0,"spike_group_a","bo_spike_group_a", []),
  ("spike_a",0,"spike_a","bo_spike_a", []),
  ("belfry_a",sokf_moveable,"belfry_a","bo_belfry_a", []),

  ("belfry_b",sokf_moveable,"belfry_b","bo_belfry_b", []),
  ("belfry_b_platform_a",sokf_moveable,"belfry_b_platform_a","bo_belfry_b_platform_a", []),



  ("belfry_old",0,"belfry_a","bo_belfry_a", []),
  ("belfry_platform_a",sokf_moveable,"belfry_platform_a","bo_belfry_platform_a", []),
  ("belfry_platform_b",sokf_moveable,"belfry_platform_b","bo_belfry_platform_b", []),
  ("belfry_platform_old",0,"belfry_platform_b","bo_belfry_platform_b", []),
  ("belfry_wheel",sokf_moveable,"belfry_wheel",0, []),
  ("belfry_wheel_old",0,"belfry_wheel",0, []),

  ("mangonel",0,"mangonel","bo_mangonel", []),
  ("trebuchet_old",0,"trebuchet_old","bo_trebuchet_old", []),
  ("trebuchet_new",0,"trebuchet_new","bo_trebuchet_old", []),

  ("trebuchet_destructible",sokf_moveable|sokf_show_hit_point_bar|sokf_destructible,"trebuchet_new","bo_trebuchet_old", [
   (ti_on_init_scene_prop,
    [
      (store_trigger_param_1, ":instance_no"),
      (scene_prop_set_hit_points, ":instance_no", 2400),
    ]),
     
   (ti_on_scene_prop_destroy,
    [          
      (play_sound, "snd_dummy_destroyed"),

      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (store_trigger_param_1, ":instance_no"),      
        (prop_instance_get_position, pos1, ":instance_no"),
        (particle_system_burst, "psys_dummy_smoke_big", pos1, 100),
        (particle_system_burst, "psys_dummy_straw_big", pos1, 100),      
        (position_move_z, pos1, -500),
        (position_rotate_x, pos1, 90),
        (prop_instance_animate_to_position, ":instance_no", pos1, 300), #animate to 6 meters below in 6 second

        (try_begin),
          (eq, "$g_round_ended", 0),
          (scene_prop_get_team, ":scene_prop_team_no", ":instance_no"),
          (try_begin),
            (eq, ":scene_prop_team_no", 0),
            (assign, ":scene_prop_team_no_multiplier", -1), 
          (else_try),
            (assign, ":scene_prop_team_no_multiplier", 1), 
          (try_end),

          (try_begin),
            (eq, "$g_number_of_targets_destroyed", 0),
            
            (store_mul, ":target_no_mul_scene_prop_team", ":scene_prop_team_no_multiplier", 2), #2 means destroyed object is a trebuchet

            #for only server itself-----------------------------------------------------------------------------------------------                                                                                                      
            (call_script, "script_show_multiplayer_message", multiplayer_message_type_target_destroyed, ":target_no_mul_scene_prop_team"), 
            #for only server itself-----------------------------------------------------------------------------------------------     
            (get_max_players, ":num_players"),                               
            (try_for_range, ":player_no", 1, ":num_players"),
              (player_is_active, ":player_no"),
              (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_target_destroyed, ":target_no_mul_scene_prop_team"), 
            (try_end),
            (val_add, "$g_number_of_targets_destroyed", 1),
          (else_try),
            (store_mul, ":target_no_mul_scene_prop_team", ":scene_prop_team_no_multiplier", 9), #9 means attackers destroyed all targets

            #for only server itself-----------------------------------------------------------------------------------------------      
            (call_script, "script_show_multiplayer_message", multiplayer_message_type_target_destroyed, ":target_no_mul_scene_prop_team"), 
            #for only server itself-----------------------------------------------------------------------------------------------     
            (get_max_players, ":num_players"),                                
            (try_for_range, ":player_no", 1, ":num_players"),
              (player_is_active, ":player_no"),
              (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_target_destroyed, ":target_no_mul_scene_prop_team"), 
            (try_end),
            (val_add, "$g_number_of_targets_destroyed", 1),
          (try_end),
        (try_end),

        #giving gold for destroying target (for trebuchet)
        #step-1 calculating total damage given to that scene prop
        (assign, ":total_damage_given", 0),
        (get_max_players, ":num_players"),                               
        (try_for_range, ":player_no", 0, ":num_players"), 
          (player_is_active, ":player_no"),
          
          (try_begin),
            (eq, "spr_trebuchet_destructible", "$g_destructible_target_1"),
            (player_get_slot, ":damage_given", ":player_no", slot_player_damage_given_to_target_1),
          (else_try),
            (player_get_slot, ":damage_given", ":player_no", slot_player_damage_given_to_target_2),
          (try_end),

          (val_add, ":total_damage_given", ":damage_given"),
        (try_end),

        #step-2 sharing 1000 gold (if num active players < 20 then 50 * num active players) to players which gave damage with the damage amounts.
        #(scene_prop_get_max_hit_points, ":max_hit_points", ":instance_no"),
        (assign, ":destroy_money_addition", 0),
        (get_max_players, ":num_players"),                               
        (try_for_range, ":player_no", 0, ":num_players"), 
          (player_is_active, ":player_no"),
          (val_add, ":destroy_money_addition", 50),
        (try_end),
      
        (try_begin),
          (ge, ":destroy_money_addition", multi_destroy_target_money_add),
          (assign, ":destroy_money_addition", multi_destroy_target_money_add),
        (try_end),
        (val_mul, ":destroy_money_addition", "$g_multiplayer_battle_earnings_multiplier"),
        (val_div, ":destroy_money_addition", 100),

        (get_max_players, ":num_players"),                               
        (try_for_range, ":player_no", 0, ":num_players"), 
          (player_is_active, ":player_no"),
          
          (try_begin),
            (eq, "spr_trebuchet_destructible", "$g_destructible_target_1"),
            (player_get_slot, ":damage_given", ":player_no", slot_player_damage_given_to_target_1),
          (else_try),
            (player_get_slot, ":damage_given", ":player_no", slot_player_damage_given_to_target_2),
          (try_end),

          (player_get_gold, ":player_gold", ":player_no"), #give money to player which helped flag to be owned by new_flag_owner team

          (val_mul, ":damage_given", ":destroy_money_addition"),
          (store_div, ":gold_earned", ":damage_given", ":total_damage_given"),
        
          (val_add, ":player_gold", ":gold_earned"),
          (player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),              
        (try_end),      
      (try_end),      
    ]),     

    (ti_on_scene_prop_hit,
    [
      (store_trigger_param_1, ":instance_no"),       
      (store_trigger_param_2, ":damage"),
      
      (try_begin),
        (scene_prop_get_hit_points, ":hit_points", ":instance_no"),
        (val_sub, ":hit_points", ":damage"),
        (gt, ":hit_points", 0),
        (play_sound, "snd_dummy_hit"),
      (else_try),
        (neg|multiplayer_is_server),
        (play_sound, "snd_dummy_destroyed"),
      (try_end),

      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (particle_system_burst, "psys_dummy_smoke", pos1, 3),
        (particle_system_burst, "psys_dummy_straw", pos1, 10),

        (set_fixed_point_multiplier, 1),
        (position_get_x, ":attacker_agent_id", pos2),
        (try_begin),
          (ge, ":attacker_agent_id", 0),
          (agent_is_alive, ":attacker_agent_id"),
          (agent_is_human, ":attacker_agent_id"),
          (neg|agent_is_non_player, ":attacker_agent_id"),
          (agent_get_player_id, ":attacker_player_id", ":attacker_agent_id"),
          (ge, ":attacker_player_id", 0),
          (player_is_active, ":attacker_player_id"),
          (try_begin),
            (eq, "spr_trebuchet_destructible", "$g_destructible_target_1"),
            (player_get_slot, ":damage_given", ":attacker_player_id", slot_player_damage_given_to_target_1),
            (val_add, ":damage_given", ":damage"),
            (player_set_slot, ":attacker_player_id", slot_player_damage_given_to_target_1, ":damage_given"),
          (else_try),
            (player_get_slot, ":damage_given", ":attacker_player_id", slot_player_damage_given_to_target_2),
            (val_add, ":damage_given", ":damage"),
            (player_set_slot, ":attacker_player_id", slot_player_damage_given_to_target_2, ":damage_given"),
          (try_end),
        (try_end),
      (try_end),
    ]),
  ]),


  ("stone_ball",0,"stone_ball","0", []),

  ("village_house_a",0,"village_house_a","bo_village_house_a", []),
  ("village_house_b",0,"village_house_b","bo_village_house_b", []),
  ("village_house_c",0,"village_house_c","bo_village_house_c", []),
  ("village_house_d",0,"village_house_d","bo_village_house_d", []),
  ("farm_house_a",0,"farm_house_a","bo_farm_house_a", []),
  ("farm_house_b",0,"farm_house_b","bo_farm_house_b", []),
  ("farm_house_c",0,"farm_house_c","bo_farm_house_c", []),
  ("mountain_house_a",0,"mountain_house_a","bo_mountain_house_a", []),
  ("mountain_house_b",0,"mountain_house_b","bo_mountain_house_b", []),
  ("village_hut_a",0,"village_hut_a","bo_village_hut_a", []),
  ("crude_fence",0,"fence","bo_fence", []),
  ("crude_fence_small",0,"crude_fence_small","bo_crude_fence_small", []),
  ("crude_fence_small_b",0,"crude_fence_small_b","bo_crude_fence_small_b", []),
  
  ("ramp_12m",0,"ramp_12m","bo_ramp_12m", []),
  ("ramp_14m",0,"ramp_14m","bo_ramp_14m", []),

  ("siege_ladder_6m",sokf_type_ladder,"siege_ladder_move_6m","bo_siege_ladder_move_6m", []), 
  ("siege_ladder_8m",sokf_type_ladder,"siege_ladder_move_8m","bo_siege_ladder_move_8m", []),
  ("siege_ladder_10m",sokf_type_ladder,"siege_ladder_move_10m","bo_siege_ladder_move_10m", []),
  ("siege_ladder_12m",sokf_type_ladder,"siege_ladder_12m","bo_siege_ladder_12m", []),
  ("siege_ladder_14m",sokf_type_ladder,"siege_ladder_14m","bo_siege_ladder_14m", []),

  ("siege_ladder_move_6m",sokf_type_ladder|sokf_moveable|spr_use_time(2),"siege_ladder_move_6m","bo_siege_ladder_move_6m", [    
   check_item_use_trigger,
   check_ladder_animate_trigger,
   check_ladder_animation_finish_trigger,
  ]),  

  ("siege_ladder_move_8m",sokf_type_ladder|sokf_moveable|spr_use_time(2),"siege_ladder_move_8m","bo_siege_ladder_move_8m", [    
   check_item_use_trigger,
   check_ladder_animate_trigger,
   check_ladder_animation_finish_trigger,
  ]),  

  ("siege_ladder_move_10m",sokf_type_ladder|sokf_moveable|spr_use_time(3),"siege_ladder_move_10m","bo_siege_ladder_move_10m", [    
   check_item_use_trigger,
   check_ladder_animate_trigger,
   check_ladder_animation_finish_trigger,
  ]),  

  ("siege_ladder_move_12m",sokf_type_ladder|sokf_moveable|spr_use_time(3),"siege_ladder_move_12m","bo_siege_ladder_move_12m", [    
   check_item_use_trigger,
   check_ladder_animate_trigger,
   check_ladder_animation_finish_trigger,
  ]),  

  ("siege_ladder_move_14m",sokf_type_ladder|sokf_moveable|spr_use_time(4),"siege_ladder_move_14m","bo_siege_ladder_move_14m", [    
   check_item_use_trigger,
   check_ladder_animate_trigger,
   check_ladder_animation_finish_trigger,
  ]),  

  ("portcullis",sokf_moveable,"portcullis_a","bo_portcullis_a", []),
  ("bed_a",0,"bed_a","bo_bed_a", []),
  ("bed_b",0,"bed_b","bo_bed_b", []),
  ("bed_c",0,"bed_c","bo_bed_c", []),
  ("bed_d",0,"bed_d","bo_bed_d", []),
  ("bed_e",0,"bed_e","bo_bed_e", []),

  ("bed_f",0,"bed_f","bo_bed_f", []),

  ("towngate_door_left",sokf_moveable,"door_g_left","bo_door_left", []),
  ("towngate_door_right",sokf_moveable,"door_g_right","bo_door_right", []),
  ("towngate_rectangle_door_left",sokf_moveable,"towngate_rectangle_door_left","bo_towngate_rectangle_door_left", []),
  ("towngate_rectangle_door_right",sokf_moveable,"towngate_rectangle_door_right","bo_towngate_rectangle_door_right", []),
  
  ("door_screen",sokf_moveable,"door_screen","0", []),
  ("door_a",sokf_moveable,"door_a","bo_door_a", []),
  ("door_b",sokf_moveable,"door_b","bo_door_a", []),
  ("door_c",sokf_moveable,"door_c","bo_door_a", []),
  ("door_d",sokf_moveable,"door_d","bo_door_a", []),
  ("tavern_door_a",sokf_moveable,"tavern_door_a","bo_tavern_door_a", []),
  ("tavern_door_b",sokf_moveable,"tavern_door_b","bo_tavern_door_a", []),
  ("door_e_left",sokf_moveable,"door_e_left","bo_door_left", []),
  ("door_e_right",sokf_moveable,"door_e_right","bo_door_right", []),
  ("door_f_left",sokf_moveable,"door_f_left","bo_door_left", []),
  ("door_f_right",sokf_moveable,"door_f_right","bo_door_right", []),
  ("door_h_left",sokf_moveable,"door_g_left","bo_door_left", []),
  ("door_h_right",sokf_moveable,"door_g_right","bo_door_right", []),
  ("draw_bridge_a",0,"draw_bridge_a","bo_draw_bridge_a", []),
  ("chain_1m",0,"chain_1m","0", []),
  ("chain_2m",0,"chain_2m","0", []),
  ("chain_5m",0,"chain_5m","0", []),
  ("chain_10m",0,"chain_10m","0", []),
  ("bridge_modular_a",0,"bridge_modular_a","bo_bridge_modular_a", []),
  ("bridge_modular_b",0,"bridge_modular_b","bo_bridge_modular_b", []),
  ("church_a",0,"church_a","bo_church_a", []),
  ("church_tower_a",0,"church_tower_a","bo_church_tower_a", []),
  ("stone_step_a",0,"floor_stone_a","bo_floor_stone_a", []),
  ("stone_step_b",0,"stone_step_b","0", []),
  ("stone_step_c",0,"stone_step_c","0", []),
  ("stone_heap",0,"stone_heap","bo_stone_heap", []),
  ("stone_heap_b",0,"stone_heap_b","bo_stone_heap", []),

  ("panel_door_a",0,"house_door_a","bo_house_door_a", []),
  ("panel_door_b",0,"house_door_b","bo_house_door_a", []),
  ("smoke_stain",0,"soot_a","0", []),
  ("brazier_with_fire",0,"brazier","bo_brazier",    [
   (ti_on_scene_prop_init,
    [
        (set_position_delta,0,0,85),
        (particle_system_add_new, "psys_brazier_fire_1"),
        (particle_system_add_new, "psys_fire_sparks_1"),

        (set_position_delta,0,0,100),
        (particle_system_add_new, "psys_fire_glow_1"),
        (particle_system_emit, "psys_fire_glow_1",9000000),
    ]),
   ]),

  ("cooking_fire",0,"fire_floor","0",
   [
   (ti_on_scene_prop_init,
    [
        (set_position_delta,0,0,12),
        (particle_system_add_new, "psys_cooking_fire_1"),
        (particle_system_add_new, "psys_fire_sparks_1"),
        (particle_system_add_new, "psys_cooking_smoke"),
        (set_position_delta,0,0,50),
        (particle_system_add_new, "psys_fire_glow_1"),
        (particle_system_emit, "psys_fire_glow_1",9000000),
    ]),
   ]),
  ("cauldron_a",0,"cauldron_a","bo_cauldron_a", []),
  ("fry_pan_a",0,"fry_pan_a","0", []),
  ("tripod_cauldron_a",0,"tripod_cauldron_a","bo_tripod_cauldron_a", []),
  ("tripod_cauldron_b",0,"tripod_cauldron_b","bo_tripod_cauldron_b", []),
  ("open_stable_a",0,"open_stable_a","bo_open_stable_a", []),
  ("open_stable_b",0,"open_stable_b","bo_open_stable_b", []),
  ("plate_a",0,"plate_a","0", []),
  ("plate_b",0,"plate_b","0", []),
  ("plate_c",0,"plate_c","0", []),
  ("lettuce",0,"lettuce","0", []),
  ("hanger",0,"hanger","0", []),
  ("knife_eating",0,"knife_eating","0", []),
  ("colander",0,"colander","0", []),
  ("ladle",0,"ladle","0", []),
  ("spoon",0,"spoon","0", []),
  ("skewer",0,"skewer","0", []),
  ("grape_a",0,"grape_a","0", []),
  ("grape_b",0,"grape_b","0", []),
  ("apple_a",0,"apple_a","0", []),
  ("apple_b",0,"apple_b","0", []),
  ("maize_a",0,"maize_a","0", []),
  ("maize_b",0,"maize_b","0", []),
  ("cabbage",0,"cabbage","0", []),
  ("flax_bundle",0,"raw_flax","0",[]),
  ("olive_plane",0,"olive_plane","0",[]),
  ("grapes_plane",0,"grapes_plane","0",[]),
  ("date_fruit_plane",0,"date_fruit_plane","0",[]),
  ("bowl",0,"bowl_big","0",[]),
  ("bowl_small",0,"bowl_small","0",[]),
  ("dye_blue",0,"raw_dye_blue","0",[]),
  ("dye_red",0,"raw_dye_red","0",[]),
  ("dye_yellow",0,"raw_dye_yellow","0",[]),
  ("basket",0,"basket_small","0",[]),
  ("basket_big",0,"basket_large","0",[]),
  ("basket_big_green",0,"basket_big","0",[]),
  ("leatherwork_frame",0,"leatherwork_frame","0", []),

  ("cabbage_b",0,"cabbage_b","0", []),
  ("bean",0,"bean","0", []),
  ("basket_a",0,"basket_a","bo_basket_a", []),
  ("feeding_trough_a",0,"feeding_trough_a","bo_feeding_trough_a", []),


  ("marrow_a",0,"marrow_a","0", []),
  ("marrow_b",0,"marrow_b","0", []),
  ("squash_plant",0,"marrow_c","0", []),


  ("gatehouse_new_a",0,"gatehouse_new_a","bo_gatehouse_new_a", []),
  ("gatehouse_new_b",0,"gatehouse_new_b","bo_gatehouse_new_b", []),
  ("gatehouse_new_snowy_a",0,"gatehouse_new_snowy_a","bo_gatehouse_new_b", []),

  ("winch",sokf_moveable,"winch","bo_winch", []),
  
  ("winch_b",sokf_moveable|spr_use_time(5),"winch_b","bo_winch", [
   (ti_on_scene_prop_use,
    [
      (store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),

      #for only server itself-----------------------------------------------------------------------------------------------
      (call_script, "script_use_item", ":instance_id", ":agent_id"),
      #for only server itself-----------------------------------------------------------------------------------------------
      (get_max_players, ":num_players"),                               
      (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
        (player_is_active, ":player_no"),
        (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_use_item, ":instance_id", ":agent_id"),
      (try_end),
    ]),
  ]),
  
  ("drawbridge",0,"drawbridge","bo_drawbridge", []),
  ("gatehouse_door_left",sokf_moveable,"gatehouse_door_left","bo_gatehouse_door_left", []),
  ("gatehouse_door_right",sokf_moveable,"gatehouse_door_right","bo_gatehouse_door_right", []),

  ("cheese_a",0,"cheese_a","0", []),
  ("cheese_b",0,"cheese_b","0", []),
  ("cheese_slice_a",0,"cheese_slice_a","0", []),
  ("bread_a",0,"bread_a","0", []),
  ("bread_b",0,"bread_b","0", []),
  ("bread_slice_a",0,"bread_slice_a","0", []),
  ("fish_a",0,"fish_a","0", []),
  ("fish_roasted_a",0,"fish_roasted_a","0", []),
  ("chicken_roasted",0,"chicken","0", []),
  ("food_steam",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
     (set_position_delta,0,0,0),
     (particle_system_add_new, "psys_food_steam"),
    ]),
   ]),
  ########################
  ("city_smoke",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
     (store_time_of_day,reg(12)),
     (neg|is_between,reg(12),5,20),
     (set_position_delta,0,0,0),
     (particle_system_add_new, "psys_night_smoke_1"),
    ]),
   ]),
    ("city_fire_fly_night",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
     (store_time_of_day,reg(12)),
     (neg|is_between,reg(12),5,20),
     (set_position_delta,0,0,0),
     (particle_system_add_new, "psys_fire_fly_1"),
    ]),
   ]),
    ("city_fly_day",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_bug_fly_1"),
    ]),
   ]),
    ("flue_smoke_tall",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_flue_smoke_tall"),
    ]),
   ]),
      ("flue_smoke_short",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_flue_smoke_short"),
    ]),
   ]),
      ("moon_beam",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_moon_beam_1"),
     (particle_system_add_new, "psys_moon_beam_paricle_1"),
    ]),
   ]),
    ("fire_small",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_fireplace_fire_small"),
    ]),
   ]),
  ("fire_big",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_fireplace_fire_big"),
    ]),
   ]),
    ("battle_field_smoke",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_war_smoke_tall"),
    ]),
   ]),
      ("Village_fire_big",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_village_fire_big"),
     (set_position_delta,0,0,100),
     (particle_system_add_new, "psys_village_fire_smoke_big"),
    ]),
   ]),
  #########################
  ("candle_a",0,"candle_a","0",
   [
   (ti_on_scene_prop_init,
    [
     (set_position_delta,0,0,27),
     (particle_system_add_new, "psys_candle_light"),
    ]),
   ]),
  ("candle_b",0,"candle_b","0",
   [
   (ti_on_scene_prop_init,
    [
     (set_position_delta,0,0,25),
     (particle_system_add_new, "psys_candle_light"),
    ]),
   ]),
  ("candle_c",0,"candle_c","0",   [
   (ti_on_scene_prop_init,
    [
     (set_position_delta,0,0,10),
     (particle_system_add_new, "psys_candle_light_small"),
    ]),
   ]),
  ("lamp_a",0,"lamp_a","0",   [
   (ti_on_scene_prop_init,
    [
     (set_position_delta,66,0,2),
     (particle_system_add_new, "psys_candle_light"),
    ]),
   ]),

  ("lamp_b",0,"lamp_b","0",   [
   (ti_on_scene_prop_init,
    [
     (set_position_delta,65,0,-7),
     (particle_system_add_new, "psys_lamp_fire"),
     (set_position_delta,70,0,-5),
     (particle_system_add_new, "psys_fire_glow_1"),
     (particle_system_emit, "psys_fire_glow_1",9000000),
     (play_sound, "snd_fire_loop", 0),
    ]),
   ]),

  ("hook_a",0,"hook_a","0", []),
  ("window_night",0,"window_night","0", []),
  ("fried_pig",0,"pork","0", []),
  ("village_oven",0,"village_oven","bo_village_oven", []),
  ("dungeon_water_drops",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_dungeon_water_drops"),
    ]),
   ]),
  ("shadow_circle_1",0,"shadow_circle_1","0", []),
  ("shadow_circle_2",0,"shadow_circle_2","0", []),
  ("shadow_square_1",0,"shadow_square_1","0", []),
  ("shadow_square_2",0,"shadow_square_2","0", []),
  ("wheelbarrow",0,"wheelbarrow","bo_wheelbarrow", []),
  ("gourd",sokf_moveable|sokf_destructible|spr_hit_points(1),"gourd","bo_gourd",
   [
     (ti_on_scene_prop_destroy,
      [
        (store_trigger_param_1, ":instance_no"),
        (val_add, "$g_last_destroyed_gourds", 1),
        (prop_instance_get_position, pos1, ":instance_no"),
        (copy_position, pos2, pos1),
        (position_set_z, pos2, -100000),
        (particle_system_burst, "psys_gourd_smoke", pos1, 2),
        (particle_system_burst, "psys_gourd_piece_1", pos1, 1),
        (particle_system_burst, "psys_gourd_piece_2", pos1, 5),
        (prop_instance_animate_to_position, ":instance_no", pos2, 1),
        (play_sound, "snd_gourd_destroyed"),
        ]),
     ]),

 ("gourd_spike",sokf_moveable,"gourd_spike","bo_gourd_spike",[]),

 ("obstacle_fence_1",0,"fence","bo_fence", []),
 ("obstacle_fallen_tree_a",0,"destroy_tree_a","bo_destroy_tree_a", []),
 ("obstacle_fallen_tree_b",0,"destroy_tree_b","bo_destroy_tree_b", []),
 ("siege_wall_a",0,"siege_wall_a","bo_siege_wall_a", []),
 ("siege_large_shield_a",0,"siege_large_shield_a","bo_siege_large_shield_a", []),
 ("granary_a",0,"granary_a","bo_granary_a", []),
 ("small_wall_connect_a",0,"small_wall_connect_a","bo_small_wall_connect_a", []),

 ("full_stable_a",0,"full_stable_a","bo_full_stable_a", []),
 ("full_stable_b",0,"full_stable_b","bo_full_stable_b", []),
 ("full_stable_c",0,"full_stable_c","bo_full_stable_c", []),
 ("full_stable_d",0,"full_stable_d","bo_full_stable_d", []),

 ("arabian_house_a",0,"arabian_house_a","bo_arabian_house_a", []),
 ("arabian_house_b",0,"arabian_house_b","bo_arabian_house_b", []),
 ("arabian_house_c",0,"arabian_house_c","bo_arabian_house_c", []),
 ("arabian_house_d",0,"arabian_house_d","bo_arabian_house_d", []),
 ("arabian_house_e",0,"arabian_house_e","bo_arabian_house_e", []),
 ("arabian_house_f",0,"arabian_house_f","bo_arabian_house_f", []),
 ("arabian_house_g",0,"arabian_house_g","bo_arabian_house_g", []),
 ("arabian_house_h",0,"arabian_house_h","bo_arabian_house_h", []),
 ("arabian_house_i",0,"arabian_house_i","bo_arabian_house_i", []),
 ("arabian_square_keep_a",0,"arabian_square_keep_a","bo_arabian_square_keep_a", []),
 ("arabian_passage_house_a",0,"arabian_passage_house_a","bo_arabian_passage_house_a", []),
 ("arabian_wall_a",0,"arabian_wall_a","bo_arabian_wall_a", []),
 ("arabian_wall_b",0,"arabian_wall_b","bo_arabian_wall_b", []),
 ("arabian_ground_a",0,"arabian_ground_a","bo_arabian_ground_a", []),
 ("arabian_parterre_a",0,"arabian_parterre_a","bo_arabian_parterre_a", []),
 ("well_shaft",0,"well_shaft","bo_well_shaft", []),
 ("horse_mill",0,"horse_mill","bo_horse_mill", []),
 ("horse_mill_collar",0,"horse_mill_collar","bo_horse_mill_collar", []),
 ("arabian_stable",0,"arabian_stable","bo_arabian_stable", []),
 ("arabian_tent",0,"arabian_tent","bo_arabian_tent", []),
 ("arabian_tent_b",0,"arabian_tent_b","bo_arabian_tent_b", []),
 ("desert_plant_a",0,"desert_plant_a","0", []),

 ("arabian_castle_battlement_a",0,"arabian_castle_battlement_a","bo_arabian_castle_battlement_a", []),
 ("arabian_castle_battlement_b_destroyed",0,"arabian_castle_battlement_b_destroyed","bo_arabian_castle_battlement_b_destroyed", []),
 ("arabian_castle_battlement_c",0,"arabian_castle_battlement_c","bo_arabian_castle_battlement_c", []),
 ("arabian_castle_battlement_d",0,"arabian_castle_battlement_d","bo_arabian_castle_battlement_d", []),
 ("arabian_castle_corner_a",0,"arabian_castle_corner_a","bo_arabian_castle_corner_a", []),
 ("arabian_castle_stairs",sokf_type_ladder,"arabian_castle_stairs","bo_arabian_castle_stairs", []),
 ("arabian_castle_stairs_b",sokf_type_ladder,"arabian_castle_stairs_b","bo_arabian_castle_stairs_b", []),
 ("arabian_castle_stairs_c",sokf_type_ladder,"arabian_castle_stairs_c","bo_arabian_castle_stairs_c", []),
 ("arabian_castle_battlement_section_a",0,"arabian_castle_battlement_section_a","bo_arabian_castle_battlement_section_a", []),
 ("arabian_castle_gate_house_a",0,"arabian_castle_gate_house_a","bo_arabian_castle_gate_house_a", []),
 ("arabian_castle_house_a",0,"arabian_castle_house_a","bo_arabian_castle_house_a", []),
 ("arabian_castle_house_b",0,"arabian_castle_house_b","bo_arabian_castle_house_b", []),
 ("arabian_castle_keep_a",0,"arabian_castle_keep_a","bo_arabian_castle_keep_a", []),


 ("arabian_house_a2",0,"arabian_house_a2","bo_arabian_house_a2", []),
 ("arabian_village_house_a",0,"arabian_village_house_a","bo_arabian_village_house_a", []),
 ("arabian_village_house_b",0,"arabian_village_house_b","bo_arabian_village_house_b", []),
 ("arabian_village_house_c",0,"arabian_village_house_c","bo_arabian_village_house_c", []),
 ("arabian_village_house_d",0,"arabian_village_house_d","bo_arabian_village_house_d", []),

 ("arabian_village_stable",0,"arabian_village_stable","bo_arabian_village_stable", []),
 ("arabian_village_hut",0,"arabian_village_hut","bo_arabian_village_hut", []),
 ("arabian_village_stairs",sokf_type_ladder,"arabian_village_stairs","bo_arabian_village_stairs", []),

 ("tree_a01",0,"tree_a01","bo_tree_a01", []),

 ("stairs_a",sokf_type_ladder,"stairs_a","bo_stairs_a", []),

 ("headquarters_flag_red",sokf_moveable|sokf_face_player,"tutorial_flag_red","0", []),
 ("headquarters_flag_blue",sokf_moveable|sokf_face_player,"tutorial_flag_blue","0", []),
 ("headquarters_flag_gray",sokf_moveable|sokf_face_player,"tutorial_flag_yellow","0", []),  

 ("headquarters_flag_red_code_only",sokf_moveable|sokf_face_player,"mp_flag_red","0", []),
 ("headquarters_flag_blue_code_only",sokf_moveable|sokf_face_player,"mp_flag_blue","0", []),
 ("headquarters_flag_gray_code_only",sokf_moveable|sokf_face_player,"mp_flag_white","0", []),  
 ("headquarters_pole_code_only",sokf_moveable,"mp_flag_pole","0", []),

 ("headquarters_flag_swadian",sokf_moveable|sokf_face_player,"flag_swadian","0", []),
 ("headquarters_flag_vaegir",sokf_moveable|sokf_face_player,"flag_vaegir","0", []),
 ("headquarters_flag_khergit",sokf_moveable|sokf_face_player,"flag_khergit","0", []),
 ("headquarters_flag_nord",sokf_moveable|sokf_face_player,"flag_nord","0", []),
 ("headquarters_flag_rhodok",sokf_moveable|sokf_face_player,"flag_rhodok","0", []),
 ("headquarters_flag_sarranid",sokf_moveable|sokf_face_player,"flag_sarranid","0", []),

 ("glow_a", 0, "glow_a", "0", []),
 ("glow_b", 0, "glow_b", "0", []),

 ("arabian_castle_corner_b",0,"arabian_castle_corner_b","bo_arabian_castle_corner_b", []),

  ("dummy_a_undestructable",sokf_destructible,"arena_archery_target_b","bo_arena_archery_target_b",
   [
     (ti_on_init_scene_prop,
      [
        (store_trigger_param_1, ":instance_no"),
        (scene_prop_set_hit_points, ":instance_no", 10000000),
        ]),
     (ti_on_scene_prop_hit,
      [
        (store_trigger_param_1, ":instance_no"),
        (store_trigger_param_2, ":damage"),
        (try_begin),
          (set_fixed_point_multiplier, 1),
          (position_get_x, ":attacker_agent_id", pos2),
          (get_player_agent_no, ":player_agent"),
          (eq, ":player_agent", ":attacker_agent_id"),
          (assign, reg60, ":damage"),
          (display_message, "str_delivered_damage"),
          (eq, "$g_tutorial_training_ground_horseman_trainer_state", 6),
          (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 1),
          (prop_instance_get_variation_id_2, ":var_id_2", ":instance_no"),
          (val_sub, ":var_id_2", 1),
          (eq, "$g_tutorial_training_ground_current_score", ":var_id_2"),
          (val_add, "$g_tutorial_training_ground_current_score", 1),
        (try_end),
        (play_sound, "snd_dummy_hit"),
        (particle_system_burst, "psys_dummy_smoke", pos1, 3),
        (particle_system_burst, "psys_dummy_straw", pos1, 10),
    ]),
  ]),
 ("cave_entrance_1",0,"cave_entrance_1","bo_cave_entrance_1", []),

  ("pointer_arrow", 0, "pointer_arrow", "0", []),
  ("fireplace_d_interior",0,"fireplace_d","bo_fireplace_d", []),
  ("ship_sail_off",0,"ship_sail_off","bo_ship_sail_off", []),
  ("ship_sail_off_b",0,"ship_sail_off_b","bo_ship_sail_off", []),
  ("ship_c_sail_off",0,"ship_c_sail_off","bo_ship_c_sail_off", []),
  ("ramp_small_a",0,"ramp_small_a","bo_ramp_small_a", []),
  ("castle_g_battlement_b",0,"castle_g_battlement_b","bo_castle_g_battlement_b", []),
  ("box_a_dynamic",sokf_moveable|sokf_dynamic_physics,"box_a","bo_box_a", []),

 ("desert_field",0,"desert_field","bo_desert_field", []),

 ("water_river",0,"water_plane","0", []),
 ("viking_house_a",0,"viking_house_a","bo_viking_house_a", []),
 ("viking_house_b",0,"viking_house_b","bo_viking_house_b", []),
 ("viking_house_c",0,"viking_house_c","bo_viking_house_c", []),
 ("viking_house_d",0,"viking_house_d","bo_viking_house_d", []),
 ("viking_house_e",0,"viking_house_e","bo_viking_house_e", []),
 ("viking_stable_a",0,"viking_stable_a","bo_viking_stable_a", []),
 ("viking_keep",0,"viking_keep","bo_viking_keep", []),

 ("viking_house_c_destroy",0,"viking_house_c_destroy","bo_viking_house_c_destroy", []),
 ("viking_house_b_destroy",0,"viking_house_b_destroy","bo_viking_house_b_destroy", []),

 ("harbour_a",0,"harbour_a","bo_harbour_a", []),
 ("sea_foam_a",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_sea_foam_a"),
    ]),
   ]),
   
 ("viking_keep_destroy",0,"viking_keep_destroy","bo_viking_keep_destroy", []),
 ("viking_keep_destroy_door",0,"viking_keep_destroy_door","bo_viking_keep_destroy_door", []),
 ("earth_tower_small_b",0,"earth_tower_small_b","bo_earth_tower_small_b", []),
 ("earth_gate_house_b",0,"earth_gate_house_b","bo_earth_gate_house_b", []),
 ("earth_tower_a",0,"earth_tower_a","bo_earth_tower_a", []),
 ("earth_stairs_c",0,"earth_stairs_c","bo_earth_stairs_c", []),
 
  ("earth_sally_gate_left",sokf_moveable|sokf_show_hit_point_bar|sokf_destructible|spr_use_time(0),"earth_sally_gate_left","bo_earth_sally_gate_left", [
    check_sally_door_use_trigger_double,

   (ti_on_init_scene_prop,
    [
      (store_trigger_param_1, ":instance_no"),
      (scene_prop_set_hit_points, ":instance_no", 2000),
    ]),
     
   (ti_on_scene_prop_destroy,
    [
      (play_sound, "snd_dummy_destroyed"),
      
      (assign, ":rotate_side", 86),
      
      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (store_trigger_param_1, ":instance_no"),      
        (store_trigger_param_2, ":attacker_agent_no"),

        (set_fixed_point_multiplier, 100),
        (prop_instance_get_position, pos1, ":instance_no"),

        (try_begin),
          (ge, ":attacker_agent_no", 0),
          (agent_get_position, pos2, ":attacker_agent_no"),
          (try_begin),
            (position_is_behind_position, pos2, pos1),
            (val_mul, ":rotate_side", -1),
          (try_end),
        (try_end),
      
        (init_position, pos3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (position_move_y, pos3, -100),
        (else_try),
          (position_move_y, pos3, 100),
        (try_end),
      
        (position_move_x, pos3, -50),
        (position_transform_position_to_parent, pos4, pos1, pos3),
        (position_move_z, pos4, 100),
        (position_get_distance_to_ground_level, ":height_to_terrain", pos4),
        (val_sub, ":height_to_terrain", 100),
        (assign, ":z_difference", ":height_to_terrain"),
        (val_div, ":z_difference", 3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (val_add, ":rotate_side", ":z_difference"),
        (else_try),
          (val_sub, ":rotate_side", ":z_difference"),
        (try_end),

        (position_rotate_x, pos1, ":rotate_side"),
        (prop_instance_animate_to_position, ":instance_no", pos1, 70), #animate to position 1 in 0.7 second
      (try_end),
    ]),       

    (ti_on_scene_prop_hit,
    [
      (store_trigger_param_1, ":instance_no"),       
      (store_trigger_param_2, ":damage"),
      
      (try_begin),
        (scene_prop_get_hit_points, ":hit_points", ":instance_no"),
        (val_sub, ":hit_points", ":damage"),
        (gt, ":hit_points", 0),
        (play_sound, "snd_dummy_hit"),
      (else_try),
        (neg|multiplayer_is_server),
        (play_sound, "snd_dummy_destroyed"),
      (try_end),

      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (particle_system_burst, "psys_dummy_smoke", pos1, 3),
        (particle_system_burst, "psys_dummy_straw", pos1, 10),
      (try_end),      
    ]),
  ]),

  ("earth_sally_gate_right",sokf_moveable|sokf_show_hit_point_bar|sokf_destructible|spr_use_time(0),"earth_sally_gate_right","bo_earth_sally_gate_right", [
    check_sally_door_use_trigger_double,

   (ti_on_init_scene_prop,
    [
      (store_trigger_param_1, ":instance_no"),
      (scene_prop_set_hit_points, ":instance_no", 2000),
    ]),
     
   (ti_on_scene_prop_destroy,
    [
      (play_sound, "snd_dummy_destroyed"),
      
      (assign, ":rotate_side", 86),
      
      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (store_trigger_param_1, ":instance_no"),      
        (store_trigger_param_2, ":attacker_agent_no"),

        (set_fixed_point_multiplier, 100),
        (prop_instance_get_position, pos1, ":instance_no"),

        (try_begin),
          (ge, ":attacker_agent_no", 0),
          (agent_get_position, pos2, ":attacker_agent_no"),
          (try_begin),
            (position_is_behind_position, pos2, pos1),
            (val_mul, ":rotate_side", -1),
          (try_end),
        (try_end),
      
        (init_position, pos3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (position_move_y, pos3, -100),
        (else_try),
          (position_move_y, pos3, 100),
        (try_end),
      
        (position_move_x, pos3, -50),
        (position_transform_position_to_parent, pos4, pos1, pos3),
        (position_move_z, pos4, 100),
        (position_get_distance_to_ground_level, ":height_to_terrain", pos4),
        (val_sub, ":height_to_terrain", 100),
        (assign, ":z_difference", ":height_to_terrain"),
        (val_div, ":z_difference", 3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (val_add, ":rotate_side", ":z_difference"),
        (else_try),
          (val_sub, ":rotate_side", ":z_difference"),
        (try_end),

        (position_rotate_x, pos1, ":rotate_side"),
        (prop_instance_animate_to_position, ":instance_no", pos1, 70), #animate to position 1 in 0.7 second
      (try_end),
    ]),       

    (ti_on_scene_prop_hit,
    [
      (store_trigger_param_1, ":instance_no"),       
      (store_trigger_param_2, ":damage"),
      
      (try_begin),
        (scene_prop_get_hit_points, ":hit_points", ":instance_no"),
        (val_sub, ":hit_points", ":damage"),
        (gt, ":hit_points", 0),
        (play_sound, "snd_dummy_hit"),
      (else_try),
        (neg|multiplayer_is_server),
        (play_sound, "snd_dummy_destroyed"),
      (try_end),

      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (particle_system_burst, "psys_dummy_smoke", pos1, 3),
        (particle_system_burst, "psys_dummy_straw", pos1, 10),
      (try_end),      
    ]),
  ]),

 #("earth_sally_gate_left",0,"earth_sally_gate_left","bo_earth_sally_gate_left", []),
 #("earth_sally_gate_right",0,"earth_sally_gate_right","bo_earth_sally_gate_right", []),


  ("barrier_box",sokf_invisible|sokf_type_barrier3d,"barrier_box","bo_barrier_box", []),
  ("barrier_capsule",sokf_invisible|sokf_type_barrier3d,"barrier_capsule","bo_barrier_capsule", []),
  ("barrier_cone" ,sokf_invisible|sokf_type_barrier3d,"barrier_cone" ,"bo_barrier_cone" , []),
  ("barrier_sphere" ,sokf_invisible|sokf_type_barrier3d,"barrier_sphere" ,"bo_barrier_sphere" , []),

  ("viking_keep_destroy_sally_door_right",sokf_moveable|sokf_show_hit_point_bar|sokf_destructible|spr_use_time(0),"viking_keep_destroy_sally_door_right","bo_viking_keep_destroy_sally_door_right", [
    check_sally_door_use_trigger_double,

   (ti_on_init_scene_prop,
    [
      (store_trigger_param_1, ":instance_no"),
      (scene_prop_set_hit_points, ":instance_no", 3000),
    ]),
     
   (ti_on_scene_prop_destroy,
    [
      (play_sound, "snd_dummy_destroyed"),
      
      (assign, ":rotate_side", 86),
      
      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (store_trigger_param_1, ":instance_no"),      
        (store_trigger_param_2, ":attacker_agent_no"),

        (set_fixed_point_multiplier, 100),
        (prop_instance_get_position, pos1, ":instance_no"),

        (try_begin),
          (ge, ":attacker_agent_no", 0),
          (agent_get_position, pos2, ":attacker_agent_no"),
          (try_begin),
            (position_is_behind_position, pos2, pos1),
            (val_mul, ":rotate_side", -1),
          (try_end),
        (try_end),
      
        (init_position, pos3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (position_move_y, pos3, -100),
        (else_try),
          (position_move_y, pos3, 100),
        (try_end),
      
        (position_move_x, pos3, -50),
        (position_transform_position_to_parent, pos4, pos1, pos3),
        (position_move_z, pos4, 100),
        (position_get_distance_to_ground_level, ":height_to_terrain", pos4),
        (val_sub, ":height_to_terrain", 100),
        (assign, ":z_difference", ":height_to_terrain"),
        (val_div, ":z_difference", 3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (val_add, ":rotate_side", ":z_difference"),
        (else_try),
          (val_sub, ":rotate_side", ":z_difference"),
        (try_end),

        (position_rotate_x, pos1, ":rotate_side"),
        (prop_instance_animate_to_position, ":instance_no", pos1, 70), #animate to position 1 in 0.7 second
      (try_end),
    ]),       

    (ti_on_scene_prop_hit,
    [
      (store_trigger_param_1, ":instance_no"),       
      (store_trigger_param_2, ":damage"),
      
      (try_begin),
        (scene_prop_get_hit_points, ":hit_points", ":instance_no"),
        (val_sub, ":hit_points", ":damage"),
        (gt, ":hit_points", 0),
        (play_sound, "snd_dummy_hit"),
      (else_try),
        (neg|multiplayer_is_server),
        (play_sound, "snd_dummy_destroyed"),
      (try_end),

      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (particle_system_burst, "psys_dummy_smoke", pos1, 3),
        (particle_system_burst, "psys_dummy_straw", pos1, 10),
      (try_end),      
    ]),
  ]),

  ("viking_keep_destroy_sally_door_left",sokf_moveable|sokf_show_hit_point_bar|sokf_destructible|spr_use_time(0),"viking_keep_destroy_sally_door_left","bo_viking_keep_destroy_sally_door_left", [
    check_sally_door_use_trigger_double,

   (ti_on_init_scene_prop,
    [
      (store_trigger_param_1, ":instance_no"),
      (scene_prop_set_hit_points, ":instance_no", 3000),
    ]),
     
   (ti_on_scene_prop_destroy,
    [
      (play_sound, "snd_dummy_destroyed"),
      
      (assign, ":rotate_side", 86),
      
      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (store_trigger_param_1, ":instance_no"),      
        (store_trigger_param_2, ":attacker_agent_no"),

        (set_fixed_point_multiplier, 100),
        (prop_instance_get_position, pos1, ":instance_no"),

        (try_begin),
          (ge, ":attacker_agent_no", 0),
          (agent_get_position, pos2, ":attacker_agent_no"),
          (try_begin),
            (position_is_behind_position, pos2, pos1),
            (val_mul, ":rotate_side", -1),
          (try_end),
        (try_end),
      
        (init_position, pos3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (position_move_y, pos3, -100),
        (else_try),
          (position_move_y, pos3, 100),
        (try_end),
      
        (position_move_x, pos3, -50),
        (position_transform_position_to_parent, pos4, pos1, pos3),
        (position_move_z, pos4, 100),
        (position_get_distance_to_ground_level, ":height_to_terrain", pos4),
        (val_sub, ":height_to_terrain", 100),
        (assign, ":z_difference", ":height_to_terrain"),
        (val_div, ":z_difference", 3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (val_add, ":rotate_side", ":z_difference"),
        (else_try),
          (val_sub, ":rotate_side", ":z_difference"),
        (try_end),

        (position_rotate_x, pos1, ":rotate_side"),
        (prop_instance_animate_to_position, ":instance_no", pos1, 70), #animate to position 1 in 0.7 second
      (try_end),
    ]),       

    (ti_on_scene_prop_hit,
    [
      (store_trigger_param_1, ":instance_no"),       
      (store_trigger_param_2, ":damage"),
      
      (try_begin),
        (scene_prop_get_hit_points, ":hit_points", ":instance_no"),
        (val_sub, ":hit_points", ":damage"),
        (gt, ":hit_points", 0),
        (play_sound, "snd_dummy_hit"),
      (else_try),
        (neg|multiplayer_is_server),
        (play_sound, "snd_dummy_destroyed"),
      (try_end),

      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (particle_system_burst, "psys_dummy_smoke", pos1, 3),
        (particle_system_burst, "psys_dummy_straw", pos1, 10),
      (try_end),      
    ]),
  ]),

  ("castle_f_door_b",sokf_moveable|sokf_show_hit_point_bar|sokf_destructible|spr_use_time(0),"castle_e_sally_door_a","bo_castle_e_sally_door_a", [
    check_castle_door_use_trigger,

   (ti_on_init_scene_prop,
    [
      (store_trigger_param_1, ":instance_no"),
      (scene_prop_set_hit_points, ":instance_no", 1000),
    ]),
     
   (ti_on_scene_prop_destroy,
    [
      (play_sound, "snd_dummy_destroyed"),
      
      (assign, ":rotate_side", 86),
      
      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (store_trigger_param_1, ":instance_no"),      
        (store_trigger_param_2, ":attacker_agent_no"),

        (set_fixed_point_multiplier, 100),
        (prop_instance_get_position, pos1, ":instance_no"),

        (try_begin),
          (ge, ":attacker_agent_no", 0),
          (agent_get_position, pos2, ":attacker_agent_no"),
          (try_begin),
            (position_is_behind_position, pos2, pos1),
            (val_mul, ":rotate_side", -1),
          (try_end),
        (try_end),
      
        (init_position, pos3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (position_move_y, pos3, -100),
        (else_try),
          (position_move_y, pos3, 100),
        (try_end),
      
        (position_move_x, pos3, -50),
        (position_transform_position_to_parent, pos4, pos1, pos3),
        (position_move_z, pos4, 100),
        (position_get_distance_to_ground_level, ":height_to_terrain", pos4),
        (val_sub, ":height_to_terrain", 100),
        (assign, ":z_difference", ":height_to_terrain"),
        #(assign, reg0, ":z_difference"),
        #(display_message, "@{!}z dif : {reg0}"),
        (val_div, ":z_difference", 3),

        (try_begin),
          (ge, ":rotate_side", 0),
          (val_add, ":rotate_side", ":z_difference"),
        (else_try),
          (val_sub, ":rotate_side", ":z_difference"),
        (try_end),

        (position_rotate_x, pos1, ":rotate_side"),
        (prop_instance_animate_to_position, ":instance_no", pos1, 70), #animate to position 1 in 0.7 second
      (try_end),
    ]),       
  
    (ti_on_scene_prop_hit,
    [
      (store_trigger_param_1, ":instance_no"),       
      (store_trigger_param_2, ":damage"),
      
      (try_begin),
        (scene_prop_get_hit_points, ":hit_points", ":instance_no"),
        (val_sub, ":hit_points", ":damage"),
        (gt, ":hit_points", 0),
        (play_sound, "snd_dummy_hit"),
      (else_try),
        (neg|multiplayer_is_server),
        (play_sound, "snd_dummy_destroyed"),
      (try_end),

      (try_begin),
        (this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),

        (particle_system_burst, "psys_dummy_smoke", pos1, 3),
        (particle_system_burst, "psys_dummy_straw", pos1, 10),
      (try_end),      
    ]),
  ]),

 ("ctf_flag_kingdom_1", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_1", "0", []),
 ("ctf_flag_kingdom_2", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_2", "0", []),
 ("ctf_flag_kingdom_3", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_3", "0", []),
 ("ctf_flag_kingdom_4", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_4", "0", []),
 ("ctf_flag_kingdom_5", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_5", "0", []),
 ("ctf_flag_kingdom_6", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_6", "0", []),
 ("ctf_flag_kingdom_7", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_7", "0", []),

 ("headquarters_flag_rebel",sokf_moveable|sokf_face_player,"flag_rebel","0", []),
  ("arabian_lighthouse_a",0,"arabian_lighthouse_a","bo_arabian_lighthouse_a", []),
  ("arabian_ramp_a",0,"arabian_ramp_a","bo_arabian_ramp_a", []),
  ("arabian_ramp_b",0,"arabian_ramp_b","bo_arabian_ramp_b", []),
  
  ("winery_interior",0,"winery_interior","bo_winery_interior", []),
  ("winery_barrel_shelf",0,"winery_barrel_shelf","bo_winery_barrel_shelf", []),
  ("winery_wall_shelf",0,"winery_wall_shelf","bo_winery_wall_shelf", []),
  ("winery_huge_barrel",0,"winery_huge_barrel","bo_winery_huge_barrel", []),
  ("winery_wine_press",0,"winery_wine_press","bo_winery_wine_press", []),
  ("winery_middle_barrel",0,"winery_middle_barrel","bo_winery_middle_barrel", []),
  ("winery_wine_cart_small_loaded",0,"winery_wine_cart_small_loaded","bo_winery_wine_cart_small_loaded", []),
  ("winery_wine_cart_small_empty",0,"winery_wine_cart_small_empty","bo_winery_wine_cart_small_empty", []),
  ("winery_wine_cart_empty",0,"winery_wine_cart_empty","bo_winery_wine_cart_empty", []),
  ("winery_wine_cart_loaded",0,"winery_wine_cart_loaded","bo_winery_wine_cart_loaded", []),
  
  ("weavery_interior",0,"weavery_interior","bo_weavery_interior", []),
  ("weavery_loom_a",0,"weavery_loom_a","bo_weavery_loom_a", []),
  ("weavery_spinning_wheel",0,"weavery_spinning_wheel","bo_weavery_spinning_wheel", []),
  
  ("mill_interior",0,"mill_interior","bo_mill_interior", []),
  ("mill_flour_sack", 0,"mill_flour_sack","bo_mill_flour_sack", []),
  ("mill_flour_sack_desk_a", 0,"mill_flour_sack_desk_a","bo_mill_flour_sack_desk_a", []),
  ("mill_flour_sack_desk_b", 0,"mill_flour_sack_desk_b","bo_mill_flour_sack_desk_b", []),
  
  ("smithy_interior", 0,"smithy_interior","bo_smithy_interior", []),
  ("smithy_grindstone_wheel", 0,"smithy_grindstone_wheel","bo_smithy_grindstone_wheel", []),
  ("smithy_forge_bellows", 0,"smithy_forge_bellows","bo_smithy_forge_bellows", []),
  ("smithy_forge", 0,"smithy_forge","bo_smithy_forge", []),
  ("smithy_anvil", 0,"smithy_anvil","bo_smithy_anvil", []),
  
  ("tannery_hide_a", 0,"tannery_hide_a","bo_tannery_hide_a", []),
  ("tannery_hide_b", 0,"tannery_hide_b","bo_tannery_hide_b", []),
  ("tannery_pools_a", 0,"tannery_pools_a","bo_tannery_pools_a", []),
  ("tannery_pools_b", 0,"tannery_pools_b","bo_tannery_pools_b", []),
  



  
  
 

 ("fountain", 0, "fountain", "bo_fountain", []),

 ("rhodok_houses_a",0,"rhodok_houses_a","bo_rhodok_houses_a", []),
 ("rhodok_houses_b",0,"rhodok_houses_b","bo_rhodok_houses_b", []),
 ("rhodok_houses_c",0,"rhodok_houses_c","bo_rhodok_houses_c", []),
 ("rhodok_houses_d",0,"rhodok_houses_d","bo_rhodok_houses_d", []),
 ("rhodok_houses_e",0,"rhodok_houses_e","bo_rhodok_houses_e", []),
 ("rhodok_house_passage_a",0,"rhodok_house_passage_a","bo_rhodok_house_passage_a", []),

 ("bridge_b",0,"bridge_b","bo_bridge_b", []),
 
("brewery_pool", 0,"brewery_pool","bo_brewery_pool", []),
("brewery_big_bucket", 0,"brewery_big_bucket","bo_brewery_big_bucket", []),
("brewery_interior", 0,"brewery_interior","bo_brewery_interior", []),
("brewery_bucket_platform_a", 0,"brewery_bucket_platform_a","bo_brewery_bucket_platform_a", []),
("brewery_bucket_platform_b", 0,"brewery_bucket_platform_b","bo_brewery_bucket_platform_b", []),


("weavery_dye_pool_r",0,"weavery_dye_pool_r","bo_weavery_dye_pool_r", []),
("weavery_dye_pool_y",0,"weavery_dye_pool_y","bo_weavery_dye_pool_y", []),
("weavery_dye_pool_b",0,"weavery_dye_pool_b","bo_weavery_dye_pool_b", []),
("weavery_dye_pool_p",0,"weavery_dye_pool_p","bo_weavery_dye_pool_p", []),
("weavery_dye_pool_g",0,"weavery_dye_pool_g","bo_weavery_dye_pool_g", []),

("oil_press_interior",0,"oil_press_interior","bo_oil_press_interior", []),

    ("city_swad_01" ,0,"city_swad_01" ,"bo_city_swad_01" , []),
    ("city_swad_02" ,0,"city_swad_02" ,"bo_city_swad_02" , []),
    ("city_swad_03" ,0,"city_swad_03" ,"bo_city_swad_03" , []),
    ("city_swad_04" ,0,"city_swad_04" ,"bo_city_swad_04" , []),
    ("city_swad_passage_01" ,0,"city_swad_passage_01" ,"bo_city_swad_passage_01" , []),
    ("city_swad_05" ,0,"city_swad_05" ,"bo_city_swad_05" , []),

  ("arena_block_j_a",0,"arena_block_j_a","bo_arena_block_j_a", []),
  ("arena_underway_a",0,"arena_underway_a","bo_arena_underway_a", []),
  ("arena_circle_a",0,"arena_circle_a","bo_arena_circle_a", []),

  ("rope_bridge_15m",0,"rope_bridge_15m","bo_rope_bridge_15m", []),
  ("tree_house_a",0,"tree_house_a","bo_tree_house_a", []),
  ("tree_house_guard_a",0,"tree_house_guard_a","bo_tree_house_guard_a", []),
  ("tree_house_guard_b",0,"tree_house_guard_b","bo_tree_house_guard_b", []),
  ("tree_shelter_a",0,"tree_shelter_a","bo_tree_shelter_a", []),
  ("yellow_fall_leafs_a",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_fall_leafs_a"),
    ]),
   ]),
   
 ("rock_bridge_a",0,"rock_bridge_a","bo_rock_bridge_a", []),
 ("suspension_bridge_a",0,"suspension_bridge_a","bo_suspension_bridge_a", []),
 ("mine_a",0,"mine_a","bo_mine_a", []),
 
 ("tent",0,"tent","bo_tent", []),
 ("sailing_plane",0,"sailing_plane",0,[]),
 ("boarding_plane",0,"boarding_plane",0,[]),
]
# modmerger_start version=201 type=2
try:
    component_name = "scene_props"
    var_set = { "scene_props" : scene_props }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
