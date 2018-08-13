# Tournament Play Enhancements (1.2) by Windyplains
# Released 9/22/2011

# WHAT THIS FILE DOES:
# Defines new "slot_troop" constants.   # 340-357
# Defines new "slot_center" constants.  # 233
# Defines what items will be considered normal or enhanced tier.

# INSTALLATION INSTRUCTIONS:
# 1) In module_constants.py you need to do the following:
#    a) Verify that the "slot_troop" numbers used below are not already used in your mod.  Presently this is 340-357.
# 2) In module_items.py you need to define what "normal" or "enhanced" weapons you want the mod to use.  I have designated items that are (non-standard)
#    as such next to their constant below.  Items listed as having a (team color) needs to have 4 of these items in the specific order of red, blue, green
#    and yellow.
# 3) Ensure that constant "wp_tpe_debug" at the very bottom is set to 0.  This prevents debug messages from showing up in game in case I missed it.
# 4) Ensure that the constants denoting "wp_tpe_bet_tier_#" fit for your module's economy.  To adjust them simply change the constant values for tiers 1-5.

###########################################################################################################################
#####                                                TPE 1.0 Additions                                                #####
###########################################################################################################################

wp_tpe_debug                           = 0   # This turns ON (1) or OFF (0) all of the debug messages.  Set to 2 will enable -very- verbose information.

slot_troop_tournament_begin            = 340
slot_troop_tournament_lance            = 340
slot_troop_tournament_bow              = 341
slot_troop_tournament_onehand          = 342
slot_troop_tournament_twohand          = 343
slot_troop_tournament_crossbow         = 344
slot_troop_tournament_throwing         = 345
slot_troop_tournament_polearm          = 346
slot_troop_tournament_horse            = 347
slot_troop_tournament_enhanced_horse   = 348
slot_troop_tournament_enhanced_armor   = 349
slot_troop_tournament_enhanced_weapons = 350
slot_troop_tournament_enhanced_shield  = 351
slot_troop_tournament_end              = 352

# NOTE: Items marked (team color) will check for four of these items in a row (red, blue, green, gold) in module_troops.py 
# so there needs to be either four of them OR comment out the line that reads "(val_add, ":team_armor", ":troop_team"),"
# for that entry.  All of the textures used in tournament_items.py are native ones.
wp_tpe_normal_shield                   = "itm_arena_shield_red" # (team color)
wp_tpe_enhanced_shield                 = "itm_tpe_enhanced_shield_red" # (team color) -> Included in tournament_items.py
wp_tpe_normal_armor                    = "itm_red_tpe_tunic" # (team color) (non-standard) -> Included in tournament_items.py
wp_tpe_enhanced_armor                  = "itm_red_tpe_armor" # (team color) (non-standard) -> Included in tournament_items.py
wp_tpe_normal_helmet                   = "itm_tourney_helm_red" # "itm_arena_helmet_red" # (team color)
wp_tpe_enhanced_helmet                 = "itm_tourney_helm_red" # (team color)
wp_tpe_normal_boots                    = "itm_tpe_normal_boots" # (non-standard) -> Included in tournament_items.py
wp_tpe_enhanced_boots                  = "itm_tpe_enhanced_boots" # (non-standard) -> Included in tournament_items.py
wp_tpe_normal_horse                    = "itm_practice_horse"
wp_tpe_enhanced_horse                  = "itm_tournament_warhorse" # Lily mod Made a new item just for tournaments with a riding skill of one instead of four 
wp_tpe_normal_lance                    = "itm_tpe_normal_lance" # (non-standard) -> Included in tournament_items.py
wp_tpe_enhanced_lance                  = "itm_tpe_enhanced_lance" # (non-standard) -> Included in tournament_items.py
wp_tpe_normal_bow                      = "itm_tpe_normal_bow" # (non-standard) -> Included in tournament_items.py
wp_tpe_enhanced_bow                    = "itm_tpe_enhanced_bow" # (non-standard) -> Included in tournament_items.py
wp_tpe_normal_sword                    = "itm_tpe_normal_sword" # (non-standard) -> Included in tournament_items.py
wp_tpe_enhanced_sword                  = "itm_tpe_enhanced_sword" # (non-standard) -> Included in tournament_items.py
wp_tpe_normal_greatsword               = "itm_tpe_normal_greatsword" # (non-standard) -> Included in tournament_items.py
wp_tpe_enhanced_greatsword             = "itm_tpe_enhanced_greatsword" # (non-standard) -> Included in tournament_items.py
wp_tpe_normal_crossbow                 = "itm_tpe_normal_crossbow" # (non-standard) -> Included in tournament_items.py
wp_tpe_enhanced_crossbow               = "itm_tpe_enhanced_crossbow" # (non-standard) -> Included in tournament_items.py
wp_tpe_normal_javelin                  = "itm_tpe_normal_javelin" # (non-standard) -> Included in tournament_items.py
wp_tpe_enhanced_javelin                = "itm_tpe_enhanced_javelin" # (non-standard) -> Included in tournament_items.py
wp_tpe_normal_polearm                  = "itm_tpe_normal_spear" # (non-standard) -> Included in tournament_items.py
wp_tpe_enhanced_polearm                = "itm_tpe_enhanced_spear" # (non-standard) -> Included in tournament_items.py

slot_troop_tournament_selections       = 353
slot_troop_tournament_bet_option       = 354
slot_troop_tournament_bet_amount       = 355
slot_troop_tournament_always_randomize = 356
slot_troop_tournament_never_spawn      = 357
# Renown Scaling
slot_center_tournament_wins            = 233  # This tallies each win so that subsequent wins gain more reputation as a "crowd favorite".
wp_tpe_max_renown                      = 80   # This sets a hard limit on how much renown can be gained at most.  Honestly you can't get this unless you're under level 5.
# Dynamic Weapons AI
wp_tpe_enemy_approaching_foot          = 700  # This sets the distance break between switching between melee or ranged weapons.
wp_tpe_enemy_approaching_mounted       = 1400 # Extra distance given to account for the speed of a mounted unit.

# COLOR CODE DEFINITIONS
wp_blue       = 0xFFAAAAFF
wp_light_blue = 0xFFAAD8FF
wp_red        = 0xFFFFAAAA
wp_yellow     = 0xFFFFFFAA
wp_pink       = 0xFFFFAAFF
wp_purple     = 0xFF6AAA89 # Used for WP DEBUG messages.
wp_black      = 0xFF000000
wp_white      = 0xFFFFFFFF
wp_green      = 0xFFAAFFAA
wp_brown      = 0xFF7A4800
# COLOR CODES end

###########################################################################################################################
#####                                                TPE 1.1 Additions                                                #####
###########################################################################################################################

# Persistent Betting
wp_tpe_bet_tier_1                      = 100 # Change this value to set the minimum bet per round. (Other than 0).
wp_tpe_bet_tier_2                      = 200
wp_tpe_bet_tier_3                      = 300
wp_tpe_bet_tier_4                      = 400
wp_tpe_bet_tier_5                      = 500 # change this value to set the maximum bet per round.

###########################################################################################################################
#####                                                TPE 1.2 Additions                                                #####
###########################################################################################################################
wp_tpe_player_can_disable              = 1   # Set this to 0 if you want to force players to use TPE only.  If this is set to 0 the g_wp_tpe_active global will be automatically set.
