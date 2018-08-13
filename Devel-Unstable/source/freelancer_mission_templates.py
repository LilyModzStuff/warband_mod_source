# Freelancer (1.3) by Taragoth
# Released 11 July 2011
# Edits by Caba'drin 14 Dec 2011
# Mod-Merger'd by Windyplains, Monnikje and Caba'drin

from header_common import *
from header_operations import *
from header_mission_templates import *
from module_constants import *

from module_mission_templates import common_battle_mission_start #for freelancer siege triggers

####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id
#
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags
#  3) Mission-type(int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#     
#  4) Mission description text (string).
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) entry-no: Troops spawned from this spawn record will use this entry
#    5.2) spawn flags.
#    5.3) alter flags. which equipment will be overriden
#    5.4) ai flags.
#    5.5) Number of troops to spawn.
#    5.6) list of equipment to add to troops spawned from here (maximum 8).
#  6) List of triggers (list).
#     See module_triggers.py for infomation about triggers.
#
#  Please note that mission templates is work in progress and can be changed in the future versions.
# 
####################################################################################################################

		
freelancer_triggers = [

# (ti_on_agent_hit, 0, 0,
	   # [],
	# [   	    (store_trigger_param_1, ":unused"), 	 
			# (store_trigger_param_2, ":agent"), #Trigger parameter 2 for this trigger is the attacker agent. Parameter 1 is the hit agent.
			# (agent_is_human, ":agent"),
			# (agent_is_alive, ":agent"),
		
		# (agent_get_wielded_item,":breakweapon",":agent",0),
		
		# (is_between,":breakweapon","itm_wooden_stick","itm_awlpike_long"), #change this to set the items you want to break				
						
		# (store_random_in_range,":weaponbreakchance",1,150),
# #--Cabadrin imod Quality Modifier
	   # (agent_get_troop_id, ":troop_id", ":agent"),
	   # (try_begin),    #only heroes have item modifications
		   # (troop_is_hero, ":troop_id"),
		   # (try_for_range, ":item_slot", ek_item_0, ek_head),    # heroes have only 4 possible weapons (equipped)
			   # (troop_get_inventory_slot, reg8, ":troop_id", ":item_slot"),  #Find Item Slot with same item ID as Equipped Weapon
			   # (eq, reg8, ":breakweapon"),
			   # (troop_get_inventory_slot_modifier, ":imod", ":troop_id", ":item_slot"),
		   # (try_end),
	   # (else_try),
		   # (assign, ":imod", imodbit_plain),
	   # (try_end),
# #Better than Average
# #I know i'm totally wrong with most of them, just go on and edit the values as you want 
	   # (try_begin),
		   # (eq, imodbit_masterwork, ":imod"),
		   # (val_min,":weaponbreakchance",9),#1%
	   # (else_try),
		   # (eq, imodbit_tempered, ":imod"),
		   # (val_min,":weaponbreakchance",8),#2%
	   # (else_try),
		   # (eq, imodbit_balanced, ":imod"),
		   # (val_add,":weaponbreakchance",3),
	   # (else_try),
		   # (eq, imodbit_heavy, ":imod"),
		   # (val_add,":weaponbreakchance",2),
	   # (else_try),
		   # (eq, imodbit_plain, ":imod"),
		   # (val_add,":weaponbreakchance",1),
   # #Worse than Average
	   # (else_try),
		   # (eq, imodbit_bent, ":imod"),
		   # (val_add,":weaponbreakchance",4),
	   # (else_try),
		   # (eq, imodbit_rusty, ":imod"),
		   # (val_add,":weaponbreakchance",7),
	   # (else_try),
		   # (eq, imodbit_chipped, ":imod"),
		   # (val_add,":weaponbreakchance",8),
	   # (else_try),
		   # (eq, imodbit_cracked, ":imod"),
		   # (val_add,":weaponbreakchance",15),
	   # (try_end),
	# #--End imod Quality Modifier
			   # (try_begin),   
			# (ge,":weaponbreakchance",140),
			# (agent_unequip_item,":agent",":breakweapon"),
			# (str_store_item_name, s0, ":breakweapon"),
			# (try_begin),
				# (get_player_agent_no, ":player_agent"),
				# (eq, ":agent", ":player_agent"),
				# (troop_remove_item, "trp_player", ":breakweapon"),
				# (display_message, "@You broke your {s0}.",0xFF0000),
				# (else_try),
				   # #(agent_get_troop_id, ":troop", ":agent"),
				# (str_store_troop_name,s1,":troop_id"),
				# (display_message, "@{s1} broke his {s0}.",0x66FF33),
					# (agent_set_animation, ":agent", "anim_strike_chest_front"),
				# (assign, ":weapon_broke", 1),
							# (else_try),
								# (agent_get_horse,":horse",":agent"),
				   # #(agent_get_troop_id, ":troop", ":agent"),
								# (str_store_troop_name,s1,":troop_id"),
				# (display_message, "@{s1} broke his {s0}.",0x66FF33),
					# (agent_set_animation, ":agent", "anim_strike_chest_front"),#You need to replace this animation with the horseman's strike
				# (assign, ":weapon_broke", 1),
			# (try_end),
		# (try_end),  
	# ]),

 # (ti_on_agent_killed_or_wounded, 0, 0, [(store_trigger_param_2, ":killer_agent_no"),(eq, ":killer_agent_no", "$fplayer_agent_no")],
   # [
	# (store_trigger_param_1, ":dead_agent_no"),
	# (neg|agent_is_ally, ":dead_agent_no"),
	# (agent_is_human, ":dead_agent_no"),	
    # (val_add, "$killcount", 1),
   # ]),
	
# END OF FREELANCER TRIGGERS
]


freelancer_siege_triggers = [
	(ti_on_agent_spawn, 0, 0, [(eq, "$freelancer_state", 1)],
		[
			(get_player_agent_no, ":player"),
			(ge, ":player", 0),
			(agent_is_active, ":player"),
			(store_trigger_param_1, ":agent_no"),
			(eq, ":player", ":agent_no"),
			(agent_get_team, ":player_team", ":player"),
			(team_set_order_listener, ":player_team", -1),
			(val_add, ":player_team", 2),
			(agent_set_team, ":player", ":player_team"),
		]),
		
	common_battle_mission_start, #+Freelancer addition of native field battle trigger to sieges
]


from util_wrappers import *
from util_scripts import *

def modmerge_mission_templates(orig_mission_templates):
    ##FLORIS - disabled weapon breaking and kill_count (floris has its own kill count via CC)
	# for i in range (0,len(orig_mission_templates)):  
		# if( orig_mission_templates[i][1] & mtf_battle_mode ):
			# orig_mission_templates[i][5].extend(freelancer_triggers)
	find_i = find_object( orig_mission_templates, "besiege_inner_battle_castle" )
	orig_mission_templates[find_i][5].extend(freelancer_siege_triggers)
	find_i = find_object( orig_mission_templates, "besiege_inner_battle_town_center" )
	orig_mission_templates[find_i][5].extend(freelancer_siege_triggers)
	find_i = find_object( orig_mission_templates, "castle_attack_walls_belfry" )
	orig_mission_templates[find_i][5].extend(freelancer_siege_triggers)
	find_i = find_object( orig_mission_templates, "castle_attack_walls_ladder" )
	orig_mission_templates[find_i][5].extend(freelancer_siege_triggers)
			
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



