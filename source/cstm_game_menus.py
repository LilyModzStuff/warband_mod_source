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

## NEW MENUS
troop_tree_options = []
for tree in CUSTOM_TROOP_TREES:
	troop_tree_options.append(("cstm_choose_troop_tree_" + tree.id, [], tree.text,
	[
		(assign, "$cstm_troops_begin", "trp_cstm_custom_troop_%s_%d_0_0" % (tree.id, CSTM_SKINS[0].id)),
		(assign, "$cstm_troops_end", "trp_cstm_custom_troop_%s_%d_0_0" % (tree.id, CSTM_SKINS[1].id)),
		
		(assign, "$cstm_reinforcement_templates_begin", "pt_cstm_kingdom_player_%s_%d_reinforcements_a" % (tree.id, CSTM_SKINS[0].id)),
		(assign, "$cstm_reinforcement_templates_end", "pt_cstm_kingdom_player_%s_%d_reinforcements_a" % (tree.id, CSTM_SKINS[1].id)),
		
		(assign, "$cstm_num_tiers", tree.num_tiers),
		
		(jump_to_menu, "mnu_cstm_choose_skin")
	]))

skin_options = []
for i in xrange(len(CSTM_SKINS)):
	skin = CSTM_SKINS[i]
	skin_options.append(("cstm_choose_skin_" + str(skin.id), [], skin.text,
	[
		# Set where the custom troops begin and end
		(store_sub, ":offset", "$cstm_troops_end", "$cstm_troops_begin"),
		(val_mul, ":offset", i),
		(val_add, "$cstm_troops_begin", ":offset"),
		(val_add, "$cstm_troops_end", ":offset"),
		
		# Set the reinforcement templates for AI lord/garrison recruitment
		(store_sub, ":offset", "$cstm_reinforcement_templates_end", "$cstm_reinforcement_templates_begin"),
		(val_mul, ":offset", i),
		(val_add, "$cstm_reinforcement_templates_begin", ":offset"),
		(val_add, "$cstm_reinforcement_templates_end", ":offset"),
		
		(assign, ":template", "$cstm_reinforcement_templates_begin"),
		(faction_set_slot, "fac_player_supporters_faction",  slot_faction_reinforcements_a, ":template"),
		(val_add, ":template", 1),
		(faction_set_slot, "fac_player_supporters_faction",  slot_faction_reinforcements_b, ":template"),
		(val_add, ":template", 1),
		(faction_set_slot, "fac_player_supporters_faction",  slot_faction_reinforcements_c, ":template"),
		
		# Set the troops to show up as guards in player faction controlled towns/castles
		(assign, ":troop", "$cstm_troops_begin"),
		(try_for_range, ":i", 0, 5),
			(gt, ":troop", 0),
			
			(store_add, ":slot", slot_faction_tier_1_troop, ":i"),
			(faction_set_slot, "fac_culture_player", ":slot", ":troop"),
			(faction_set_slot, "fac_player_faction", ":slot", ":troop"),
			(faction_set_slot, "fac_player_supporters_faction", ":slot", ":troop"),
			
			(troop_get_upgrade_troop, ":troop", ":troop", 0),
		(try_end),
		
		(store_sub, ":guard_troop", "$cstm_troops_end", 1),
		(faction_set_slot, "fac_culture_player", slot_faction_guard_troop, ":guard_troop"),
		(faction_set_slot, "fac_player_faction", slot_faction_guard_troop, ":guard_troop"),
		(faction_set_slot, "fac_player_supporters_faction", slot_faction_guard_troop, ":guard_troop"),
		
		(faction_set_slot, "fac_culture_player", slot_faction_prison_guard_troop, ":guard_troop"),
		(faction_set_slot, "fac_player_faction", slot_faction_prison_guard_troop, ":guard_troop"),
		(faction_set_slot, "fac_player_supporters_faction", slot_faction_prison_guard_troop, ":guard_troop"),
		
		(faction_set_slot, "fac_culture_player", slot_faction_castle_guard_troop, ":guard_troop"),
		(faction_set_slot, "fac_player_faction", slot_faction_castle_guard_troop, ":guard_troop"),
		(faction_set_slot, "fac_player_supporters_faction", slot_faction_castle_guard_troop, ":guard_troop"),
		
		# Set the troop whose image will be used in the customisation screen (the dummy troop can't be used because for reasons it appears naked instead of with the equipment selected)
		(assign, "$cstm_presentation_troop", "trp_cstm_presentation_troop_" + str(skin.id)),
		
		#(call_script, "script_cstm_add_troop_tree_to_main_party", "$cstm_troops_begin", 5),
		
		# Update village recruits
		(try_for_range, ":village", villages_begin, villages_end),
			(store_faction_of_party, ":faction", ":village"),
			(eq, ":faction", "fac_player_supporters_faction"),
			
			(call_script, "script_cstm_center_set_culture", ":village", "fac_culture_player"),
		(try_end),
		
		(call_script, "script_cstm_reset_lord_armies_in_player_faction"),
		(call_script, "script_cstm_reset_garrisons_in_player_faction"),
		
		# Jump to the custom troop tree viewer where troops can be selected for customisation
		(troop_set_name, cstm_troop_tree_prefix, "@Custom"),
		(start_presentation, "prsnt_cstm_view_custom_troop_tree"),
	]))

choose_troop_tree_menu = Menu("cstm_choose_troop_tree", mnf_disable_all_keys, 
	"As the ruler of your own kingdom, you can choose the types of troops that will be recruited and trained in your kingdom's\
 armies. To begin with, you must decide how diverse a set of training paths are available for the troops of your kingdom.\
 More options can help deal with a wider variety of battlefield scenarios, but you risk a jack of all trades, master of none\
 situation.\
 ^^Which kind of troop tree would you like for your kingdom's troop? Choose carefully, as you can only choose this once.", 
	"none", [], troop_tree_options)

choose_skin_menu = Menu("cstm_choose_skin", mnf_disable_all_keys, "What gender of troops would you like to form the army of your kingdom? Choose carefully, as you can only choose this once.", "none", [], skin_options)

## CUSTOMISE TROOPS TOWN MENU OPTION
customise_troops_town_option = ("cstm_customise_troop", [(eq, "$g_player_court", "$current_town")], "Customise your kingdom's troops",
	[
		(try_begin),
			(gt, "$cstm_troops_begin", 0),
			
			(assign, "$cstm_selected_troop", -1),
			(start_presentation, "prsnt_cstm_view_custom_troop_tree"),
		(else_try),
			(jump_to_menu, "mnu_cstm_choose_troop_tree"),
		(try_end),
	])

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
	
	# Add customise troops option to town menu in capital
	menus["center_manage"].insert_option_after(customise_troops_town_option, "walled_center_move_court")
	
	# Add custom troop menus
	menus[choose_troop_tree_menu.id] = choose_troop_tree_menu
	menus[choose_skin_menu.id] = choose_skin_menu
	
	# For some reason I can't stop the game from wanting to open the town menu when it starts no matter how much I want it to do otherwise, so let it open and redirect it the first time to kingdom naming
	menus["town"].operations[0:0] = [
		(try_begin),
			(eq, "$cstm_activate_kingdom_naming", 1),
			
			(assign, "$cstm_activate_kingdom_naming", 0),
			(start_presentation, "prsnt_cstm_start_name_kingdom"),
		(else_try),
			(eq, "$cstm_open_troop_tree_view", 1),
			
			(assign, "$cstm_open_troop_tree_view", 0),
			(try_begin), # Fix first time constable issue.
				(gt, "$cstm_troops_begin", 0),
				
				(assign, "$cstm_selected_troop", -1),
			(start_presentation, "prsnt_cstm_view_custom_troop_tree"),
			(else_try),
				(jump_to_menu, "mnu_cstm_choose_troop_tree"),
			(try_end),
		(try_end),
	]
	
	# Ensure custom troops show up in player faction controlled towns and castles
	old_consequences = menus["town"].options["town_center"].consequences
	#print "\n".join([str(x) for x in old_consequences if (type(x) == tuple and x[0] == neq and x[2] == "fac_player_supporters_faction")])
	menus["town"].options["town_center"].consequences = [x for x in old_consequences if not (type(x) == tuple and x[0] == neq and x[2] == "fac_player_supporters_faction")]	# Makes sure custom troops show up in player owned towns
	old_consequences = menus["town"].options["castle_inspect"].consequences
	#print "\n".join([str(x) for x in old_consequences if (type(x) == tuple and x[0] == neq and x[2] == "fac_player_supporters_faction")])
	menus["town"].options["castle_inspect"].consequences = [x for x in old_consequences if not (type(x) == tuple and x[0] == neq and x[2] == "fac_player_supporters_faction")]	# Makes sure custom troops show up in player owned castles
	
	#menus["camp"].add_option(("find_parties", [], "Find Parties With Wrong Troops",
	#[
	#	(try_for_parties, ":party"),
	#		(assign, ":displayed_party_name", 0),
	#		
	#		(party_get_num_companion_stacks, ":num_stacks", ":party"),
	#		(try_for_range, ":stack", 0, ":num_stacks"),
	#			(party_stack_get_troop_id, ":troop", ":party", ":stack"),
	#			(is_between, ":troop", cstm_troops_begin, cstm_troops_end),
	#			(neg|is_between, ":troop", "$cstm_troops_begin", "$cstm_troops_end"),
	#			
	#			(try_begin),
	#				(eq, ":displayed_party_name", 0),
	#				
	#				(str_store_party_name, s0, ":party"),
	#				(display_message, "@{s0}:"),
	#				(assign, ":displayed_party_name", 1),
	#			(try_end),
	#			
	#			(str_store_troop_name, s0, ":troop"),
	#			(display_message, "@{s0}"),
	#		(try_end),
	#		
	#		(eq, ":displayed_party_name", 1),
	#		(display_message, "@ "),
	#	(try_end),
	#]))
	
	del orig_menus[:]
	for menu_id in menus:
		orig_menus.append(menus[menu_id].convert_to_tuple())