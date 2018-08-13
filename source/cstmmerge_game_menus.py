import collections

from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *
from ID_menus import *
from module_constants import *

from cstm_troops import *
from cstm_header_game_menus import *

####################################################################################################################
#	(menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#	 Each game menu is a tuple that contains the following fields:
#	
#	1) Game-menu id (string): used for referencing game-menus in other files.
#		 The prefix menu_ is automatically added before each game-menu-id
#
#	2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#		 You can also specify menu text color here, with the menu_text_color macro
#	3) Game-menu text (string).
#	4) mesh-name (string). Not currently used. Must be the string "none"
#	5) Operations block (list). A list of operations. See header_operations.py for reference.
#		 The operations block is executed when the game menu is activated.
#	6) List of Menu options (List).
#		 Each menu-option record is a tuple containing the following fields:
#	 6.1) Menu-option-id (string) used for referencing game-menus in other files.
#				The prefix mno_ is automatically added before each menu-option.
#	 6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#				The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#	 6.3) Menu-option text (string).
#	 6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#				The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################

## START AS KING MENU OPTION
start_as_king_background_option = ("cstm_start_king", [], "An adventurer who became a king.", [
	(assign, "$background_type", cb_guard),
	(assign, reg3, "$character_gender"),
	(str_store_string,s10,"@Your father was a small time mercenary who escorted caravans for a pittance. One day,\
	fed up with this life, he struck out for adventure in the war-torn land of Calradia, leaving you and your mother\
	behind. Enough money made it back to get you a good education and a chance at minor nobility, but you heard little\
	from your father and assumed him dead when the money stopped coming. It was a shock then when a man in expensive armour\
	showed up at your door and announced himself a vassal of your father.^^Apparently he had made quite a name for himself\
	as a hunter of bandits, tournament champion and feared mercenary leader. Eventually, he hired enough of an army to carve\
	out his very own kingdom, hoping to unite the whole land under his leadership. He could not afford to keep sending money\
	as everything was invested in protecting his realm from enemies on all sides and he was eventually struck down in battle\
	before he could send for his family. With his dying breath he ordered that his {reg3?daughter:son} be brought forth to\
	continue his dynasty. But that is now, your life so far was certainly not one of royalty..."),
	
	(assign, "$cstm_start_as_king", 1),
	
	# Activate the player faction
	(faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_active),
	(faction_set_slot, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
	(faction_set_color, "fac_player_supporters_faction", 0xFF0000),
	(assign, "$players_kingdom", "fac_player_supporters_faction"),
	(assign, "$g_player_banner_granted", 1),
	(assign, "$g_player_minister", "trp_temporary_minister"),
	(troop_set_faction, "trp_temporary_minister", "fac_player_supporters_faction"),
	
	# Give player some right to rule and cash, renown and cash since your father was a king and all
	(call_script, "script_change_player_right_to_rule", 50),
	(troop_set_slot, "trp_player", slot_troop_renown, 250),
	(call_script, "script_troop_add_gold", "trp_player", 50000),
	
	(party_set_morale, "p_main_party", 80),
	(troop_add_item, "trp_player", "itm_raw_olives"),
	(troop_add_item, "trp_player", "itm_raw_grapes"),
	(troop_add_item, "trp_player", "itm_pork"),
	(troop_add_item, "trp_player", "itm_chicken"),
	(troop_add_item, "trp_player", "itm_cattle_meat"),
	(troop_add_item, "trp_player", "itm_honey"),
	(troop_add_item, "trp_player", "itm_sausages"),
	(troop_add_item, "trp_player", "itm_butter"),
	(troop_add_item, "trp_player", "itm_bread"),
	(troop_add_item, "trp_player", "itm_bread"),
	(troop_add_item, "trp_player", "itm_bread"),
	
	# Update notes and recalculate AI
	(call_script, "script_update_all_notes"),
	(assign, "$g_recalculate_ais", 1),
	
	# Continue character creation
	(jump_to_menu, "mnu_start_character_2"),
])

## ESTABLISH WHAT FIEFS THE PLAYER KINGDOM STARTS WITH USING START AS KING OPTION
player_kingdom_starting_fiefs = [
	"p_town_16",		# Dhirim
	"p_castle_6",		# Tilbaut Castle
	"p_castle_20",	# Derchios Castle
	"p_castle_24",	# Reindi Castle
	"p_castle_26",	# Senuzgda Castle
	"p_castle_27",	# Rindyar Castle
]

# The first fief in the list will be the capital, given to the player
capital = player_kingdom_starting_fiefs[0]
start_as_king_background_option[3].extend([
	#(str_store_party_name, s0, capital),
	#(display_message, "@Taking {s0}"),
	
	# Record the previous faction owner
	(store_faction_of_party, ":old_faction", capital),
	
	# Record village lords to add to player faction later
	(try_for_range, ":village", villages_begin, villages_end),
		(party_slot_eq, ":village", slot_village_bound_center, capital),
		
		(party_get_slot, ":lord", ":village", slot_town_lord),
		(is_between, ":lord", lords_begin, lords_end),
		
		#(str_store_troop_name, s0, ":lord"),
		#(str_store_party_name, s1, ":village"),
		#(display_message, "@Recording that {s1} belongs to {s0}"),
		(party_set_slot, ":village", cstm_slot_center_initial_lord, ":lord"),
	(try_end),
	
	# Current lord of capital loses it and gets moved away
	(party_get_slot, ":old_lord", capital, slot_town_lord),
	
	(call_script, "script_give_center_to_faction", capital, "fac_player_supporters_faction"),
	(party_set_slot, capital, slot_town_lord, "trp_player"),
	(assign, "$g_player_court", capital),
	(party_relocate_near_party, "p_main_party", capital, 2),
	
	(try_begin),
		(troop_get_slot, ":lord_party", ":old_lord", slot_troop_leaded_party),
		(party_detach, ":lord_party"),
		
		(call_script, "script_cf_select_random_walled_center_with_faction", ":old_faction"),
		(party_relocate_near_party, ":lord_party", reg0, 2),
	(else_try),
		(faction_get_slot, ":king", ":old_faction", slot_faction_leader),
		(troop_get_slot, ":king_party", ":king", slot_troop_leaded_party),
		
		(party_relocate_near_party, ":lord_party", ":king_party", 2),
	(try_end),
	
	# Set territorial dispute with old owner
	(party_set_slot, capital, slot_center_ex_faction, ":old_faction"),
])

for fief in player_kingdom_starting_fiefs[1:]:
	start_as_king_background_option[3].extend([
		#(display_message, "@^"),
		#(str_store_party_name, s0, fief),
		#(display_message, "@Taking {s0}"),
		
		# Record fief lord to add to player faction later
		(party_get_slot, ":lord", fief, slot_town_lord),
		(try_begin),
			(is_between, ":lord", lords_begin, lords_end),
			
			(party_set_slot, fief, cstm_slot_center_initial_lord, ":lord"),
		(try_end),
		
		# Record village lords to add to player faction later
		(try_for_range, ":village", villages_begin, villages_end),
			(party_slot_eq, ":village", slot_village_bound_center, fief),
			
			(party_get_slot, ":lord", ":village", slot_town_lord),
			(is_between, ":lord", lords_begin, lords_end),
			
			#(str_store_troop_name, s0, ":lord"),
			#(str_store_party_name, s1, ":village"),
			#(display_message, "@Recording that {s1} belongs to {s0}"),
			(party_set_slot, ":village", cstm_slot_center_initial_lord, ":lord"),
		(try_end),
	])

start_as_king_background_option[3].extend([
	# Add initial lords of player faction fiefs to player faction and restore fiefs
	(try_for_range, ":center", centers_begin, centers_end),
		(party_get_slot, ":lord", ":center", cstm_slot_center_initial_lord),
		(gt, ":lord", 0),
		
		(try_begin),
			(store_faction_of_troop, ":faction", ":lord"),
			(neq, ":faction", "fac_player_supporters_faction"),
			
			(try_for_range, ":center_2", walled_centers_begin, walled_centers_end),
				(neq, ":center_2", fief),
				(party_slot_eq, ":center_2", slot_town_lord, ":lord"),
				
				(party_set_slot, ":center_2", slot_town_lord, stl_unassigned),
			(try_end),
			
			(call_script, "script_change_troop_faction", ":lord", "fac_player_supporters_faction"),
			(troop_set_slot, ":lord", slot_troop_occupation, slto_kingdom_hero),
		(try_end),
		
		(try_begin),
			(neg|party_slot_eq, ":center", slot_party_type, spt_village),
			
			(call_script, "script_give_center_to_faction", ":center", "fac_player_supporters_faction"),
		(try_end),
		
		(party_set_slot, ":center", slot_town_lord, ":lord"),
	(try_end),
])

new_starting_option_texts = {
	"revenge": "@Only you know exactly what caused you to give up your old life and follow this strange man.\
	 Still, it was not a difficult choice to leave, with the rage burning brightly in your heart. You want \
	 vengeance. You want justice. What was done to your father cannot be undone, and these debts can only be \
	 paid in blood...",

	"death": "@Only you know exactly what caused you to give up your old life and follow this strange man.\
	 All you can say is that you couldn't bear to stay, not with the memories of those you loved so close and so\
	 painful. Perhaps your new life will let you forget, or honour the name that you can no longer bear to speak...",

	"wanderlust": "@Only you know exactly what caused you to give up your old life and follow this strange man.\
	 You're not even sure when your home became a prison, when the familiar became mundane, but your dreams of\
	 wandering have taken over your life. Whether you yearn for some faraway place or merely for the open road and the\
	 freedom to travel, you could no longer bear to stay in the same place. You simply went and never looked back...",

	"disown": "@Only you know exactly what caused you to give up your old life and follow this strange man.\
	 However, you know you cannot go back. There's nothing to go back to. Whatever home you may have had is gone\
	 now, and what better opportunity could you have to find a home if this man speaks the truth?",

	"greed": "@Only you know exactly what caused you to give up your old life and follow this strange man.\
	 To everyone else, it's clear that you're now motivated solely by personal gain.\
	 You want to be rich, powerful, respected, feared.\
	 You want to be the one whom others hurry to obey.\
	 You want people to know your name, and tremble whenever it is spoken.\
	 You want everything, and you won't let anyone stop you from having it..."
}

def modmerge(var_set):
	try:
		var_name_1 = "game_menus"
		orig_menus = var_set[var_name_1]
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)
	
	menus = collections.OrderedDict()
	for menu_tuple in orig_menus:
		menus[menu_tuple[0]] = Menu(*menu_tuple)
	
	# Add in start as king option
	menus["start_character_1"].insert_option_before(start_as_king_background_option, "start_noble")
	menus["start_phase_2"].operations[0:0] = [
		(try_begin),
			(eq, "$cstm_start_as_king", 1),
			
			(assign, "$cstm_activate_kingdom_naming", 1),
			(start_encounter, capital),
			(change_screen_return),
		(try_end),
	]
	
	# Change the text in the "why you left" menu and resulting options to better reflect coming as a king rather than an adventurer
	menus["start_character_4"].text = "{s12}^^But soon everything changed and you were on your way to a strange land to claim your title of {reg3?Queen:King}. What made you take this decision was..."
	menus["start_character_4"].operations.append((assign, reg3, "$character_gender"))
	for option_id, option_text in new_starting_option_texts.iteritems():
		if option_id in menus["start_character_4"].options:
			menus["start_character_4"].options[option_id].consequences.extend([
				(try_begin),
					(eq, "$cstm_start_as_king", 1),
					
					(str_store_string, s13, option_text),
				(try_end),
			])
		else:
			print "Could not find reason for setting out as adventurer option: %s. Discarding text." % (option_id)
	
	del orig_menus[:]
	for menu_id in menus:
		orig_menus.append(menus[menu_id].convert_to_tuple())