from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from ID_animations import *

scripts = [

	###############
	("c3_defaults",
	[
		(assign, "$character_gender", 0), #man
		(assign, "$c3_status", 4), #commoner
		(assign, "$c3_start", 5), #swadia
	]),
	
	##########################
	#input: faction
	#output: none
	#what it does: starts player faction, generates player party & finds king of faction, removes king, gives king's town to player,
	#			   gives faction lords to player faction, sets relations with lords
	("c3_kingdom_monarch_of",
		[	(store_script_param,":selected_faction", 1),
			
			(call_script,"script_c3_start_player_faction"),
			(call_script,"script_c3_create_player_party",":selected_faction"),
			
			#deactive faction to be taken over
			(faction_set_slot,":selected_faction",slot_faction_state,sfs_inactive),
			#scans all npcs lords (including kings)
			(try_for_range,":npc",original_kingdom_heroes_begin,pretenders_begin),
				#stores faction of every npc 
				(store_faction_of_troop,":npc_faction",":npc"),
				#if npc faction is same as faction of choice
				(eq,":npc_faction",":selected_faction"),
				#if
				(try_begin),
					#the npc is leader (king)
					(faction_slot_eq,":npc_faction",slot_faction_leader,":npc"),
					#for clarity
					(assign,":king",":npc"),
					#get king party
					(troop_get_slot,":king_party",":king",slot_troop_leaded_party),
					#remove king party from game
					(remove_party,":king_party"),
					#scan all towns
					(try_for_range,":town",towns_begin,towns_end),
						#find king's town
						(party_slot_eq,":town",slot_town_lord,":king"),
						#give king's town to player
						(call_script,"script_give_center_to_lord",":town","trp_player",0),
						#assign town as player's court
						(assign,"$g_player_court",":town"),
						#set palyer to spawn around town
						(party_relocate_near_party,"p_main_party",":town",2),
					(try_end),
				#if (not king)
				(else_try),
					#they are lords (for clarity)
					(assign,":lords",":npc"),
					#assign lords to players faction
					(call_script,"script_change_troop_faction",":lords","fac_player_supporters_faction"),
					#assigns lords as subjects to the player
					(troop_set_slot, ":lords", slot_troop_occupation,slto_kingdom_hero),
					#sets lords as met, for reports menu
					(troop_set_slot,":lords",slot_troop_met,1),
					#stores random numbers
					(store_random_in_range,":rand",20,40),
					#increases relation with lords by random numbers
					(call_script,"script_troop_change_relation_with_troop","trp_player",":lords",":rand"),
				(try_end),
			(try_end),
			(assign, "$g_recalculate_ais",1),
			(call_script,"script_update_all_notes"),
		]),
	
	###################
	#input: faction
	#output: none
	#what it does: starts player faction, generates player party & randomly picks a town lord from selected faction, excluding faction leader, and transfers lord to player faction,
	#			   then transfers town to player and makes the town, player court
	("c3_principality_monarch_in",
		[	
			(store_script_param,":selected_faction", 1),
			
			(call_script,"script_c3_start_player_faction"),
			(call_script,"script_c3_create_player_party",":selected_faction"),
			
			#initialize first, weird things happen if don't
			(assign,":lord1",0),
			(assign,":lord2",0),
			(assign,":lord3",0),
			(assign,":limit",0),
			
			#finding town lords and their towns
			(try_for_range,":lord",lords_begin,lords_end),
				(store_faction_of_troop,":lord_faction",":lord"),
				(eq,":lord_faction",":selected_faction"),
				(try_for_range,":town",towns_begin,towns_end),
					(party_slot_eq,":town",slot_town_lord,":lord"),
					(try_begin),
						(eq,":lord1",0),
						(assign,":lord1",":lord"),
						(assign,":town1",":town"),
						(val_add,":limit",1),
					(else_try),
						(eq,":lord2",0),
						(neq,":lord",":lord1"),
						(assign,":lord2",":lord"),
						(assign,":town2",":town"),
						(val_add,":limit",1),
					(else_try),
						(eq,":lord3",0),
						(neq,":lord",":lord1"),
						(neq,":lord",":lord2"),
						(assign,":lord3",":lord"),
						(assign,":town3",":town"),
					(try_end),
					(try_begin),
						(gt,":lord3",0),
						(val_add,":limit",1),
					(try_end),
				(try_end),
			(try_end),
			
			#randomizing town lords
			(store_random_in_range,":unused",0,":limit"),
				(try_begin),
					(eq,":unused",0),
					(assign,":rand_lord",":lord1"),
					(assign,":random_town",":town1"),
				(else_try),
					(eq,":unused",1),
					(assign,":rand_lord",":lord2"),
					(assign,":random_town",":town2"),
				(else_try),
					(eq,":unused",2),
					(assign,":rand_lord",":lord3"),
					(assign,":random_town",":town3"),
				(try_end),
			
			#give lord to player faction
			(call_script,"script_change_troop_faction",":rand_lord","fac_player_supporters_faction"),
			#assign lord as vassal of player
			(troop_set_slot,":rand_lord",slot_troop_occupation,slto_kingdom_hero),
			#sets troop as already met, for reports menu
			(troop_set_slot,":rand_lord",slot_troop_met,1),
			#random number between the two
			(store_random_in_range,":no",20,40),
			#increase relation between lord and player by random number
			(call_script,"script_troop_change_relation_with_troop","trp_player",":rand_lord",":no"),
			#give lord's town to player
			(call_script,"script_give_center_to_lord",":random_town","trp_player",0),
			#town now becomes player's court
			(assign,"$g_player_court",":random_town"),
			#set spawn near town
			(party_relocate_near_party, "p_main_party",":random_town",2),
			
			(call_script, "script_update_all_notes"),
			(assign, "$g_recalculate_ais",1),
		]),
	
	##############################
	#input: faction
	#output: none
	#what it does: activates supporter faction (default Native stuff)
	("c3_start_player_faction",
		[
			#start faction (default Native)
			(faction_set_slot,"fac_player_supporters_faction",slot_faction_state,sfs_active),
			(faction_set_slot,"fac_player_supporters_faction",slot_faction_leader,"trp_player"),
			(faction_set_color,"fac_player_supporters_faction",0xFF0000),
			(assign,"$players_kingdom","fac_player_supporters_faction"),
			(assign,"$g_player_banner_granted",1),
		]),

	("c3_create_player_party",
		[
			(store_script_param,":selected_faction", 1),
			
			#party generator
			#first, get ideal party size
			#default limit is 30 for any party
			(assign,":limit",30),
			#each (leadership level) gives 5 to limit
			(store_skill_level,":skill","skl_leadership","trp_player"),
			(val_mul,":skill",5),
			(val_add,":limit",":skill"),
			#each (charisma level) gives 1 to limit
			(store_attribute_level,":charisma","trp_player",ca_charisma),
			(val_add,":limit",":charisma"),
			#each (25 renown) gives 1 to limit
			(troop_get_slot,":troop_renown","trp_player",slot_troop_renown),
			(store_div,":renown_bonus",":troop_renown",25),
			(val_add,":limit",":renown_bonus"),
			#output:base(30)+leadership+charisma+reknown-20(buffer)=ideal size
			(val_sub,":limit",20),
			(assign,":ideal_size",":limit"),
			#second, get party capacity
			(party_get_free_companions_capacity,":capacity","p_main_party"),
			#begin loop - generation
			(try_for_range,":unused",0,":capacity"),
				#keep refreshing current party size
				(party_get_num_companions,":party_size","p_main_party"),
				#if
				(try_begin),
					#current party size is less than ideal size, keep adding troops
					(lt,":party_size",":ideal_size"),
					#troop templates to use
					(faction_get_slot,":party_template_a",":selected_faction",slot_faction_reinforcements_a),
					(faction_get_slot,":party_template_b",":selected_faction",slot_faction_reinforcements_b),
					(faction_get_slot,":party_template_c",":selected_faction",slot_faction_reinforcements_c),
					#random number
					(store_random_in_range,":rand",0,10),
					# if
					(try_begin),
						# random number less than 2
						(lt,":rand",2),
						#add this template - this template has weak troops - percentage should stay low, unless want a lot of weak troops
						(party_add_template,"p_main_party",":party_template_a"),
					# if
					(else_try),
						# random number less than 5
						(lt,":rand",5),
						#add this template - this template has decent troops to start with
						(party_add_template,"p_main_party",":party_template_b"),
					# if, number is higher than 5
					(else_try),
						#add this template - this template has good troops to start with
						(party_add_template,"p_main_party",":party_template_c"),
					(try_end),
				(try_end),
			(try_end),
			#note about generator, numbers 0,1 & 2 will add both template_a & b, that's why template_c percentage is 40% - as it is, the result is nice
			#loop end
			#must have, if not set, party morale starts at 20 and seems bugged
			(party_set_morale,"p_main_party",100),
		]),
	
	###############
	#input: faction
	#output: none"
	#what it does: assigns player to the faction of choice (Native script) then finds the king and sets as met and gives a little relation and sets spawn close to king
	("c3_vassal_in",
		[
			(store_script_param,":selected_faction", 1),
			
			(call_script, "script_player_join_faction", ":selected_faction"),
			(call_script,"script_c3_create_player_party",":selected_faction"),
			
			#cycle through all npcs
			(try_for_range,":npc",original_kingdom_heroes_begin,pretenders_begin),
				#store faction of each npc
				(store_faction_of_troop,":npc_faction",":npc"),
			#(if) npc faction is the same as faction of choice
				(eq,":npc_faction",":selected_faction"),
				# & if
				(try_begin),
					# the npc faction and npc match and is the faction leader
					(faction_slot_eq,":npc_faction",slot_faction_leader,":npc"),
					#we have a king, this is to keep statements clear
					(assign,":king",":npc"),
					#set king as met, for reports menu
					(troop_set_slot,":king",slot_troop_met,1),
					#random number
					(store_random_in_range,":rand",5,15),
					#increase relation by random number value
					(call_script,"script_troop_change_relation_with_troop","trp_player",":king",":rand"),
					#get king's party
					(troop_get_slot,":king_party",":king",slot_troop_leaded_party),
					#spawn player near king's party because player doesn't always get a fief
					(party_relocate_near_party, "p_main_party",":king_party", 2),
				(try_end),
			(try_end),
			
			(call_script,"script_add_log_entry",logent_pledged_allegiance,"trp_player", -1, ":king", ":selected_faction"),
			(assign, "$player_has_homage" ,1),			
		]),
		
	################################
	#input: weapon proficiency level
	#output: reg0, points to return
	#output: reg1, new level (15) *not needed, could reset level at presentation, but this works as a check while here
	#what it does: cycles from current level down to level 15, returning points that it took to increase, pattern is from Native, add higher levels on top.
	("c3_reset_profiency",
		[	
			(store_script_param,":level", 1),
			(assign, ":points", 0),
			
			(try_begin), (eq, ":level", 140), (val_sub, ":level", 1), (val_add, ":points", 4), (try_end),
			(try_begin), (eq, ":level", 139), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 138), (val_sub, ":level", 1), (val_add, ":points", 4), (try_end),
			(try_begin), (eq, ":level", 137), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 136), (val_sub, ":level", 1), (val_add, ":points", 4), (try_end),
			(try_begin), (eq, ":level", 135), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 134), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 133), (val_sub, ":level", 1), (val_add, ":points", 4), (try_end),
			(try_begin), (eq, ":level", 132), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 131), (val_sub, ":level", 1), (val_add, ":points", 4), (try_end),
			(try_begin), (eq, ":level", 130), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 129), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 128), (val_sub, ":level", 1), (val_add, ":points", 4), (try_end),
			(try_begin), (eq, ":level", 127), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 126), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 125), (val_sub, ":level", 1), (val_add, ":points", 4), (try_end),
			(try_begin), (eq, ":level", 124), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 123), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 122), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 121), (val_sub, ":level", 1), (val_add, ":points", 4), (try_end),
			(try_begin), (eq, ":level", 120), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 119), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 118), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 117), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 116), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 115), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 114), (val_sub, ":level", 1), (val_add, ":points", 4), (try_end),
			(try_begin), (eq, ":level", 113), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 112), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 111), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 110), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 109), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 108), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 107), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 106), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 105), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 104), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 103), (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 102), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 101), (val_sub, ":level", 1), (val_add, ":points", 3), (try_end),
			(try_begin), (eq, ":level", 100), (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 99),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 98),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 97),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 96),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 95),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 94),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 93),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 92),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 91),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 90),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 89),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 88),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 87),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 86),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 85),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 84),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 83),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 82),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 81),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 80),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 79),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 78),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 77),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 76),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 75),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 74),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 73),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 72),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 71),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 70),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 69),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 68),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 67),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 66),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 65),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 64),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 63),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 62),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 61),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 60),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 59),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 58),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 57),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 56),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 55),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 54),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 53),  (val_sub, ":level", 1), (val_add, ":points", 2), (try_end),
			(try_begin), (eq, ":level", 52),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 51),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 50),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 49),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 48),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 47),  (val_sub, ":level", 2), (val_add, ":points", 1), (try_end), #no level 46
			(try_begin), (eq, ":level", 45),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 44),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 43),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 42),  (val_sub, ":level", 2), (val_add, ":points", 1), (try_end), #no level 41
			(try_begin), (eq, ":level", 40),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 39),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 38),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 37),  (val_sub, ":level", 2), (val_add, ":points", 1), (try_end), #no level 36
			(try_begin), (eq, ":level", 35),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 34),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 33),  (val_sub, ":level", 2), (val_add, ":points", 1), (try_end), #no level 32
			(try_begin), (eq, ":level", 31),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 30),  (val_sub, ":level", 2), (val_add, ":points", 1), (try_end), #no level 29
			(try_begin), (eq, ":level", 28),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 27),  (val_sub, ":level", 2), (val_add, ":points", 1), (try_end), #no level 26
			(try_begin), (eq, ":level", 25),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 24),  (val_sub, ":level", 2), (val_add, ":points", 1), (try_end), #no level 23
			(try_begin), (eq, ":level", 22),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 21),  (val_sub, ":level", 2), (val_add, ":points", 1), (try_end), #no level 20
			(try_begin), (eq, ":level", 19),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			(try_begin), (eq, ":level", 18),  (val_sub, ":level", 2), (val_add, ":points", 1), (try_end), #no level 17
			(try_begin), (eq, ":level", 16),  (val_sub, ":level", 1), (val_add, ":points", 1), (try_end),
			
			(assign, reg60, ":points"),
			(assign, reg61, ":level"),
		]),
		
		
	##########################
	#input: weapon proficiency level
	#output: reg58 new level
	#other: reg? is unassigned weapon points, when passing reg? into (script_param, ":points", 2) it doesn't work
	#what it does: finds current level and if has enough points, raises level and spends points
	("c3_increase_proficiency",
		[
			(store_script_param,":level", 1),
			
			# cost = the amount of points it takes to get from one proficiency level to the next
			# cost was copied from Native pattern of leveling up weapon proficiencies starting at level 15, which is always consistent
			#	if,			level == #	  	&  	points > cost, 	 	increase level      &  minus cost from points
			(try_begin), (eq, ":level", 139), (ge, reg34, 4), (val_add, ":level", 1), (val_sub, reg34, 4), (try_end),
			(try_begin), (eq, ":level", 138), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 137), (ge, reg34, 4), (val_add, ":level", 1), (val_sub, reg34, 4), (try_end),
			(try_begin), (eq, ":level", 136), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 135), (ge, reg34, 4), (val_add, ":level", 1), (val_sub, reg34, 4), (try_end),
			(try_begin), (eq, ":level", 134), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 133), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 132), (ge, reg34, 4), (val_add, ":level", 1), (val_sub, reg34, 4), (try_end),
			(try_begin), (eq, ":level", 131), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 130), (ge, reg34, 4), (val_add, ":level", 1), (val_sub, reg34, 4), (try_end),
			(try_begin), (eq, ":level", 129), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 128), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 127), (ge, reg34, 4), (val_add, ":level", 1), (val_sub, reg34, 4), (try_end),
			(try_begin), (eq, ":level", 126), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 125), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 124), (ge, reg34, 4), (val_add, ":level", 1), (val_sub, reg34, 4), (try_end),
			(try_begin), (eq, ":level", 123), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 122), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 121), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 120), (ge, reg34, 4), (val_add, ":level", 1), (val_sub, reg34, 4), (try_end),
			(try_begin), (eq, ":level", 119), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 118), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 117), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 116), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 115), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 114), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 113), (ge, reg34, 4), (val_add, ":level", 1), (val_sub, reg34, 4), (try_end),
			(try_begin), (eq, ":level", 112), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 111), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 110), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 109), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 108), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 107), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 106), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 105), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 104), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 103), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 102), (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 101), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 100), (ge, reg34, 3), (val_add, ":level", 1), (val_sub, reg34, 3), (try_end),
			(try_begin), (eq, ":level", 99),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 98),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 97),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 96),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 95),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 94),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 93),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 92),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 91),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 90),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 89),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 88),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 87),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 86),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 85),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 84),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 83),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 82),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 81),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 80),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 79),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 78),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 77),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 76),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 75),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 74),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 73),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 72),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 71),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 70),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 69),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 68),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 67),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 66),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 65),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 64),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 63),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 62),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 61),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 60),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 59),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 58),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 57),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 56),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 55),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 54),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 53),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 52),  (ge, reg34, 2), (val_add, ":level", 1), (val_sub, reg34, 2), (try_end),
			(try_begin), (eq, ":level", 51),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 50),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 49),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 48),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 47),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end), #no level 46
			(try_begin), (eq, ":level", 45),  (ge, reg34, 1), (val_add, ":level", 2), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 44),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 43),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 42),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end), #no level 41
			(try_begin), (eq, ":level", 40),  (ge, reg34, 1), (val_add, ":level", 2), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 39),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 38),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 37),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end), #no level 36
			(try_begin), (eq, ":level", 35),  (ge, reg34, 1), (val_add, ":level", 2), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 34),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 33),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end), #no level 32
			(try_begin), (eq, ":level", 31),  (ge, reg34, 1), (val_add, ":level", 2), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 30),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end), #no level 29
			(try_begin), (eq, ":level", 28),  (ge, reg34, 1), (val_add, ":level", 2), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 27),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end), #no level 26
			(try_begin), (eq, ":level", 25),  (ge, reg34, 1), (val_add, ":level", 2), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 24),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end), #no level 23
			(try_begin), (eq, ":level", 22),  (ge, reg34, 1), (val_add, ":level", 2), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 21),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end), #no level 20
			(try_begin), (eq, ":level", 19),  (ge, reg34, 1), (val_add, ":level", 2), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 18),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end), #no level 17
			(try_begin), (eq, ":level", 16),  (ge, reg34, 1), (val_add, ":level", 2), (val_sub, reg34, 1), (try_end),
			(try_begin), (eq, ":level", 15),  (ge, reg34, 1), (val_add, ":level", 1), (val_sub, reg34, 1), (try_end),
			
			(assign, reg58, ":level"),			
		]),
]


from util_wrappers import *
from util_scripts import *
                
def modmerge_scripts(orig_scripts):
	# process script directives first
	#process_script_directives(orig_scripts, scripts_directives)
	# add remaining scripts
	add_scripts(orig_scripts, scripts, True)
	
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "scripts"
        orig_scripts = var_set[var_name_1]
    
        
		# START do your own stuff to do merging
		
        modmerge_scripts(orig_scripts)

		# END do your own stuff
        
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)