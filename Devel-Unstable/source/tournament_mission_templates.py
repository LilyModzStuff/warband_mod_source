# Tournament Play Enhancements (1.1) by Windyplains
# Released 8/30/2011

# WHAT THIS FILE DOES:
# Adds "AI_triggers" to module_mission_template.py's "tournament_triggers" to enable the "Dynamic Weapon AI" feature.

from header_common import *
from header_operations import *
from module_constants import *
from header_mission_templates import *


AI_triggers = [  
## TOURNAMENT PLAY ENHANCEMENTS (1.0) - Windyplains - Weapon AI
# If mounted -> equip lance if you have one.
# If enemy distant -> equip ranged weapon if you have one.
# if enemy close -> equip melee weapon.
(0, 0, 1, 
	[(eq, "$g_mt_mode", abm_tournament),],
	[
      # Run through all active NPCs on the tournament battle field.
      (try_for_agents, ":agent_self"),
        # Isn't a player.
        (agent_is_non_player, ":agent_self"),
        # Isn't a horse.
        (agent_is_human, ":agent_self"),
        # Hasn't been defeated.
        (agent_is_alive, ":agent_self"),
		# exclude tournament masters
		(agent_get_troop_id, ":troop_self", ":agent_self"),
		(neg|is_between, ":troop_self", "trp_town_1_arena_master", "trp_town_1_armorer"),
        # They riding a horse?
		(agent_get_horse, ":horse", ":agent_self"), # 0 - No, 1 - Yes
		
		# Determine closest enemy.
		(assign, ":shortest_distance", 10000),
		(str_store_string, s1, "@No one"),
		(str_store_troop_name, s2, ":troop_self"),
		(agent_get_position, pos1, ":agent_self"),
		(assign, ":distance", 10000),
		(try_for_agents, ":agent_enemy"),
			(agent_get_troop_id, ":troop_enemy", ":agent_enemy"),
			# Not looking at self.
			(neq, ":agent_enemy", ":agent_self"),
			# exclude tournament masters
			(neg|is_between, ":troop_enemy", "trp_town_1_arena_master", "trp_town_1_armorer"),
			# Not an ally
			(agent_get_team, ":team_self", ":agent_self"),
			(agent_get_team, ":team_enemy", ":agent_enemy"),
			(neq, ":team_self", ":team_enemy"),
			# Isn't a horse.
			(agent_is_human, ":agent_enemy"),
			# Hasn't been defeated.
			(agent_is_alive, ":agent_enemy"),
			
			(agent_get_position, pos2, ":agent_enemy"),
			(get_distance_between_positions,":distance",pos1,pos2),
			(try_begin),
				(lt, ":distance", ":shortest_distance"),
				(assign, ":shortest_distance", ":distance"),
				(str_store_troop_name, s1, ":troop_enemy"),
				(assign, reg0, ":shortest_distance"),
				(agent_get_horse, ":enemy_mounted", ":agent_enemy"),
			(try_end),
		(try_end),
		
		# If you enable this save yourself a headache and up the trigger timing.
		(try_begin), (eq, wp_tpe_debug, 2), (display_message, "@DEBUG (Weapon AI): {s2}'s closest enemy is {s1} at a distance of {reg0}."), (try_end),
		
		(assign, ":weapon_choice", 0),
		(try_begin),
			(ge, ":horse", 0),
			(this_or_next|agent_has_item_equipped,":agent_self",wp_tpe_normal_lance),
			(agent_has_item_equipped,":agent_self",wp_tpe_enhanced_lance),
			(assign, ":weapon_choice", 2), # Bypasses melee/ranged options.
		(else_try),
			(le, ":enemy_mounted", 0),
			(le, ":shortest_distance", wp_tpe_enemy_approaching_foot),
			(assign, ":weapon_choice", 1),
		(else_try),
			(ge, ":enemy_mounted", 1),
			(le, ":shortest_distance", wp_tpe_enemy_approaching_mounted),
			(assign, ":weapon_choice", 1),
		(try_end),
		
		(try_begin),
			(eq, ":weapon_choice", 1),
			(agent_set_wielded_item, ":agent_self", wp_tpe_normal_polearm),
			(agent_set_wielded_item, ":agent_self", wp_tpe_enhanced_polearm),
			(agent_set_wielded_item, ":agent_self", wp_tpe_normal_sword),
			(agent_set_wielded_item, ":agent_self", wp_tpe_enhanced_sword),
			(agent_set_wielded_item, ":agent_self", wp_tpe_normal_greatsword),
			(agent_set_wielded_item, ":agent_self", wp_tpe_enhanced_greatsword),
		(else_try),
			(eq, ":weapon_choice", 0),
			(agent_set_wielded_item, ":agent_self", wp_tpe_normal_bow),
			(agent_set_wielded_item, ":agent_self", wp_tpe_enhanced_bow),
			(agent_set_wielded_item, ":agent_self", wp_tpe_normal_crossbow),
			(agent_set_wielded_item, ":agent_self", wp_tpe_enhanced_crossbow),
			(agent_set_wielded_item, ":agent_self", wp_tpe_normal_javelin),
			(agent_set_wielded_item, ":agent_self", wp_tpe_enhanced_javelin),
		(else_try),
			(eq, ":weapon_choice", 2),
			(agent_set_wielded_item, ":agent_self", wp_tpe_normal_lance),
			(agent_set_wielded_item, ":agent_self", wp_tpe_enhanced_lance),
		(try_end),
      (try_end),
   ]),
   
(0, 0, ti_once, 
	[(eq, "$g_mt_mode", abm_tournament),],
	[
		# Run through all active NPCs on the tournament battle field.
		(try_for_agents, ":agent_self"),
			(agent_equip_item, ":agent_self", wp_tpe_normal_boots),
			(agent_equip_item, ":agent_self", wp_tpe_enhanced_boots),
		(try_end),
	]),
## TOURNAMENT PLAY ENHANCEMENTS end
]

def modmerge_mission_templates(orig_mission_templates):
	find_i = find_object( orig_mission_templates, "arena_melee_fight" )
	orig_mission_templates[find_i][5].extend(AI_triggers)

# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "mission_templates"
        orig_mission_templates = var_set[var_name_1]
        modmerge_mission_templates(orig_mission_templates)

    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)