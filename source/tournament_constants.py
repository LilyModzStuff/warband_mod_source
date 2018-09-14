# Tournament Play Enhancements (1.5) by Windyplains

# WHAT THIS FILE DOES:
# Defines new "slot_troop" constants.   # 350-374
# Defines new "slot_center" constants.  # 233
# Defines what items will be considered normal or enhanced tier.

###########################################################################################################################
#####                                                MODULE SETTINGS                                                  #####
###########################################################################################################################

DEBUG_TPE_general                      = 0   # ON (1) / OFF (0) - Displays all of the undefined debug messages.  Set to 2 will enable -very- verbose information.
DEBUG_TPE_ai_behavior                  = 0   # ON (1) / OFF (0) - Displays AI behavioral debugging messages.
DEBUG_TPE_DESIGN                       = 0   # ON (1) / OFF (0) - Displays any debug messages associated with the Tournament Design System.
DEBUG_TPE_QUESTS                       = 0   # ON (1) / OFF (0) - Displays any debug messages associated with the Tournament Quest System.

# MOD DESIGNER OPTIONS
wp_tpe_mod_opt_player_can_disable      = 0   # Set this to 0 if you want to force players to use TPE only.  If this is set to 0 the g_wp_tpe_active global will be automatically set.
wp_tpe_mod_opt_actual_gear             = 0   # (0 - OFF / 1 - ON) Enabling this completely changes TPE design.  It will allow every troop to bring their regular equipment into the arena.
                                             # This will also remove any options regarding choosing of equipment from the TPE options display.
wp_tpe_mod_opt_renown_scale_enabled    = 0   # (0 - OFF / 1 - ON) Enabling this allows a player to choose if they want the renown scaling feature
	# Disabled to declutter menu. Renown scaling forced enabled. 

                                             # to work or not.  If it is disabled the feature option will not display and will be disabled by default.
wp_tpe_mod_opt_nobilty_reactions       = 1   # (0 - OFF / 1 - ON) This causes lords & ladies to react to your tournament win.
wp_tpe_mod_opt_payout_bonus            = 1   # (0 - OFF / 1 - ON) This provides a bonus to money earned based on difficulty.
wp_tpe_mod_opt_award_items_on_win      = 1   # (0 - OFF / 1 - ON) With this enabled players will earn items specifiec by script_tpe_setup_loot_table upon ranking in the top 3 tournament placements.
	# Need to get around to this, should wait until we have some fun items anyway though.

###########################################################################################################################
#####                                                 DEPENDENCY MODS                                                 #####
###########################################################################################################################
MOD_PBOD_INSTALLED                     = 0   # Caba'drin's Pre-Battle Orders & Deployment mod is installed.  Set to 0 if you do not use his mod.
MOD_CUSTOM_COMMANDER_INSTALLED         = 0   # Rubik's Custom Commander mod is installed.  Set to 0 if you do not use his mod.
MOD_FLORIS_INSTALLED                   = 0   # Set to 1 hides the tournament configuration menu since Floris already handles these changes.
MOD_ARENA_OVERHAUL_INSTALLED           = 1   # If Adorno's Arena Overhaul Mod is being used this should be set to 1.  If not, use 0.
tpe_default_arena_scene                = 0   # 0 = Native, 1 = Arena Overhaul Mod
###########################################################################################################################
#####                                              TROOP SLOT DEFINITIONS                                             #####
###########################################################################################################################

slot_troop_tournament_begin            = 350
slot_troop_tournament_lance            = 350
slot_troop_tournament_bow              = 351
slot_troop_tournament_onehand          = 352
slot_troop_tournament_twohand          = 353
slot_troop_tournament_crossbow         = 354
slot_troop_tournament_throwing         = 355
slot_troop_tournament_polearm          = 356
slot_troop_tournament_horse            = 357
slot_troop_tournament_enhanced_horse   = 358
slot_troop_tournament_enhanced_armor   = 359
slot_troop_tournament_enhanced_weapons = 360
slot_troop_tournament_enhanced_shield  = 361
slot_troop_tournament_end              = 362
slot_troop_tournament_selections       = 363
slot_troop_tournament_team_request     = 364 # TPE+ 1.3 (really only used by player)
slot_troop_tournament_bet_amount       = 365 # Depreciated in TPE 1.4.7
slot_troop_tournament_always_randomize = 366
slot_troop_tournament_never_spawn      = 367
slot_troop_tournament_round_points     = 368 # TPE+ 1.3  # This records how many points you gain per round of a tournament.
slot_troop_tournament_total_points     = 369 # TPE+ 1.3  # This records how many points you've earned across the entire tournament.
slot_troop_tournament_eliminated       = 370 # TPE+ 1.3  # This is initially set to 0.  When eliminated becomes 1.
slot_troop_tournament_participating    = 371 # TPE+ 1.3  # This goes from 0 to 1 if they join the tournament round.
slot_troop_tournament_odds_worth       = 372 # TPE+ 1.3  # This combines level & renown to account for betting odds.
slot_troop_tournament_awards           = 373 # TPE+ 1.3  # This was added to handle tie breakers.
slot_troop_tournament_image            = 374 # TPE+ 1.3  # This stores the object ID of the character's mesh image. (workaround for not being able to update mesh images)
# TPE reserves slots 375-379 as well in module_constants.

###########################################################################################################################
#####                                            CENTER SLOT DEFINITIONS                                              #####
###########################################################################################################################
slot_center_tournament_wins              = 233  # This tallies each win so that subsequent wins gain more reputation as a "crowd favorite".
slot_town_arena_alternate                = 234  # This is to old alternate arena scenes.  For Floris this currently means adding the native arena scenes back in.
slot_town_arena_option                   = 235  # This is the designated arena for this town based on options set in the Tournament Design Panel.
# slot_center_tournament_log_date        = 234  # The log slots will eventually point to party arrays used to keep past tournament performance.
# slot_center_tournament_log_level       = 235  # Date                Location         Level  Rank    Difficulty   Score       Total Earnings
# slot_center_tournament_log_ranking     = 236  # March 14th, 1267    Sargoth            2    19th        91%      7 points    5,400 denars
# slot_center_tournament_log_difficulty  = 237  # Based on difficulty slider (24/24 = 90->65%) + health bars (off = 10%) + level scaling (on = 0->25%)
# slot_center_tournament_log_earnings    = 238  # Shift 3% difficulty from slider -> level scaling per level gained.  Fully switch by level 9.

###########################################################################################################################
#####                                                ITEM DEFINITIONS                                                 #####
###########################################################################################################################

# NOTE: Items marked (team color) will check for four of these items in a row (red, blue, green, gold) in module_troops.py 
# so there needs to be either four of them OR comment out the line that reads "(val_add, ":team_armor", ":troop_team"),"
# for that entry.  All of the textures used in tournament_items.py are native ones.
# NOTE: Any constants uncommented here neeed to also be uncommented in "script_tdp_define_weapons" in order to work.

wp_tpe_normal_shield        = "itm_arena_shield_red" # (team color)
wp_tpe_enhanced_shield      = "itm_tpe_enhanced_shield_red" # (team color) -> Included in tournament_items.py
wp_tpe_default_armor        = "itm_red_tpe_tunic" # (team color) (non-standard) -> Included in tournament_items.py
wp_tpe_enhanced_armor       = "itm_red_tpe_armor" # (team color) (non-standard) -> Included in tournament_items.py
wp_tpe_normal_helmet        = "itm_arena_helmet_red" # "itm_arena_helmet_red" # (team color)
wp_tpe_enhanced_helmet      = "itm_tourney_helm_red" # (team color)
wp_tpe_normal_boots         = "itm_tpe_normal_boots" # (non-standard) -> Included in tournament_items.py
wp_tpe_enhanced_boots       = "itm_tpe_enhanced_boots" # (non-standard) -> Included in tournament_items.py

# Lances
wp_tpe_default_lance        = "itm_tpe_normal_lance"

# Bows
wp_tpe_default_bow          = "itm_tpe_normal_bow"

# One Handed Weapons
wp_tpe_default_onehand      = "itm_tpe_normal_sword"
wp_tpe_alt_onehand_1        = "itm_tpe_normal_axe"
wp_tpe_alt_onehand_2        = "itm_tpe_normal_scimitar"

# Two Handed Weapons
wp_tpe_default_twohand      = "itm_tpe_normal_greatsword"
wp_tpe_alt_twohand_1        = "itm_tpe_normal_greataxe"
# wp_tpe_alt_twohand_2        = ""

# Crossbows
wp_tpe_default_crossbow     = "itm_tpe_normal_crossbow"

# Thrown Weapons
wp_tpe_default_javelin      = "itm_tpe_normal_javelin"
wp_tpe_alt_throwing_1       = "itm_tpe_normal_throwing_axe"
wp_tpe_alt_throwing_2       = "itm_tpe_normal_throwing_daggers"

# Polearms
wp_tpe_default_polearm      = "itm_tpe_normal_spear"
wp_tpe_alt_polearm_1        = "itm_tpe_normal_quarterstaff"
# wp_tpe_alt_polearm_2        = ""

# Mounts
wp_tpe_default_horse        = "itm_tpe_normal_horse_red"

#### LOOT TABLE ####
# NOTE: These are commented out since they do not exist outside of Floris.  If you want to have items awarded as prizes you need to do the following:
#       1) Define these constants with items from your own game.
#       2) In tournament_scripts look for "script_tpe_setup_loot_table" and uncomment the lines of that script.
#       3) Above in this file, set "wp_tpe_mod_opt_award_items_on_win" to 1.
# # Low Range Items
tpe_loot_item_201           = "itm_wine"
tpe_loot_item_202           = "itm_wine"
tpe_loot_item_203           = "itm_furs"
tpe_loot_item_204           = "itm_furs"
tpe_loot_item_205           = "itm_sumpter_horse"
tpe_loot_item_206           = "itm_war_spear"
tpe_loot_item_207           = "itm_sword_medieval_b_small"
tpe_loot_item_208           = "itm_crossbow"
tpe_loot_item_209           = "itm_steppe_horse"
tpe_loot_item_210           = "itm_winged_mace"
# # Medium Range Items
tpe_loot_item_211           = "itm_tab_shield_heater_cav_a"
tpe_loot_item_212           = "itm_saddle_horse"
tpe_loot_item_213           = "itm_battle_axe"
tpe_loot_item_214           = "itm_archers_vest"
tpe_loot_item_215           = "itm_aketon_green"
tpe_loot_item_216           = "itm_glaive"
tpe_loot_item_217           = "itm_heavy_lance"
tpe_loot_item_218           = "itm_tab_shield_small_round_c"
tpe_loot_item_219           = "itm_tab_shield_pavise_d"
tpe_loot_item_220           = "itm_tab_shield_heater_cav_b"
tpe_loot_item_221           = "itm_strong_bow"
tpe_loot_item_222           = "itm_great_sword"
tpe_loot_item_223           = "itm_padded_leather"
tpe_loot_item_224           = "itm_arabian_horse_a"
tpe_loot_item_225           = "itm_guard_helmet"
tpe_loot_item_226           = "itm_courser"
tpe_loot_item_227           = "itm_nomad_robe"
tpe_loot_item_228           = "itm_long_axe_c"
# # Higher Range Items
tpe_loot_item_229           = "itm_war_bow"
tpe_loot_item_230           = "itm_hunter"
tpe_loot_item_231           = "itm_haubergeon"
tpe_loot_item_232           = "itm_sarranid_cavalry_robe"
tpe_loot_item_233           = "itm_khergit_sword_two_handed_b"
tpe_loot_item_234           = "itm_sword_two_handed_a"
tpe_loot_item_235           = "itm_warhorse"
tpe_loot_item_236           = "itm_mail_boots"
tpe_loot_item_237           = "itm_mail_with_surcoat"
tpe_loot_item_238           = "itm_iron_greaves"
tpe_loot_item_239           = "itm_plate_boots"
tpe_loot_item_240           = "itm_cuir_bouilli"
tpe_loot_item_241           = "itm_heraldic_mail_with_tunic"

		
###########################################################################################################################
#####                                               RENOWN SCALING                                                    #####
###########################################################################################################################
wp_tpe_max_renown                      = 50   # This sets a hard limit on how much renown can be gained at most.  
                                              # Honestly you can't get this high unless you're under level 5.

###########################################################################################################################
#####                                              DYNAMIC WEAPON AI                                                  #####
###########################################################################################################################
wp_tpe_enemy_approaching_foot          = 700  # This sets the distance break between switching between melee or ranged weapons.
wp_tpe_enemy_approaching_mounted       = 1400 # Extra distance given to account for the speed of a mounted unit.

###########################################################################################################################
#####                                           BETTING & PAYOUT OPTIONS                                              #####
###########################################################################################################################

### PERSISTENT BETTING ###
wp_tpe_bet_minimum                     = 0     # Change this value to set the minimum bet per round. (Other than 0).
wp_tpe_bet_maximum                     = 200   # Change this value to set your mod's upper limit for betting per round.
wp_tpe_maximum_odds                    = 6     # This sets a hard limit on odds which prevents some random chances of very favorable or unfavorable odds.
wp_tpe_maximum_payout_per_round        = 2500  # This is a hard limit on how much someone can win in a round regardless of settings.

### PAYOUT BONUS ###
# Note: Payout specifically deals with increasing the base xp & cash gained for winning a tournament, not gains via betting.
wp_tpe_payout_factor                   = 6     # Max payout possible is 24 (highest difficulty) * (Factor % + 100%) * 6 rounds
wp_tpe_payout_base_cash                = 200   # Native is 200.
wp_tpe_payout_base_xp                  = 250   # Native is 250.
wp_tpe_payout_cap_cash                 = 7500
wp_tpe_payout_cap_xp                   = 2500
wp_tpe_cap_increase_per_level          = 50    # This increase supports a level scaled cap before the hard limit kicks in.
wp_tpe_min_xp_gain                     = 250

###########################################################################################################################
#####                                                 QUEST OPTIONS                                                   #####
###########################################################################################################################

TPE_QUEST_REACTIONS_HIGH                        = 3
TPE_QUEST_REACTIONS_MEDIUM                      = 2
TPE_QUEST_REACTIONS_LOW                         = 1
TPE_QUEST_REACTIONS_OFF                         = 0

# Floris Active Tournament States 
qp1_tournament_message_received                 = 1
qp1_tournament_participated_in_tournament       = 2
qp1_tournament_refused_invitation               = 3
###########################################################################################################################
#####                                             LORD & LADY REACTIONS                                               #####
###########################################################################################################################
wp_tpe_male                             = 0
wp_tpe_female                           = 1

# BASE REACTION THRESHOLDS
wp_tpe_min_relation_to_be_lord_friend   = 5
wp_tpe_min_relation_to_be_lord_rival    = -5  # Note this MUST be less than the lord_friend value.
wp_tpe_min_relation_to_be_lady_friend   = 1
wp_tpe_min_relation_to_be_lady_rival    = -3  # Note this MUST be less than the lady_friend value.
wp_tpe_bonus_relation_from_vassals      = 2
wp_tpe_bonus_relation_for_courtship     = 2

# PERSONALITY REACTION MODIFIERS
### MARTIAL ### - chivalrous but not terribly empathetic or introspective
wp_tpe_gain_vs_martial_for_male         = 2
wp_tpe_loss_vs_martial_for_male         = 1
wp_tpe_gain_vs_martial_for_female       = 2
wp_tpe_loss_vs_martial_for_female       = 1

### QUARRELSOME ### - spiteful, cynical, a bit paranoid, possibly hotheaded
wp_tpe_gain_vs_quarrelsome_for_male     = 0
wp_tpe_loss_vs_quarrelsome_for_male     = 2
wp_tpe_gain_vs_quarrelsome_for_female   = 0
wp_tpe_loss_vs_quarrelsome_for_female   = 2

### SELF-RIGHTEOUS ### - coldblooded, moralizing, often cruel
wp_tpe_gain_vs_selfrighteous_for_male   = 1
wp_tpe_loss_vs_selfrighteous_for_male   = 1
wp_tpe_gain_vs_selfrighteous_for_female = 1
wp_tpe_loss_vs_selfrighteous_for_female = 1

### CUNNING ### - coldblooded, pragmatic, amoral
wp_tpe_gain_vs_cunning_for_male         = 1
wp_tpe_loss_vs_cunning_for_male         = 1
wp_tpe_gain_vs_cunning_for_female       = 1
wp_tpe_loss_vs_cunning_for_female       = 1

### DEBAUCHED ### - spiteful, amoral, sadistic
wp_tpe_gain_vs_debauched_for_male       = 1
wp_tpe_loss_vs_debauched_for_male       = 3
wp_tpe_gain_vs_debauched_for_female     = 1
wp_tpe_loss_vs_debauched_for_female     = 3

### GOOD NATURED ### - chivalrous, benevolent, perhaps a little too decent to be a good warlord
wp_tpe_gain_vs_goodnatured_for_male     = 2
wp_tpe_loss_vs_goodnatured_for_male     = 1
wp_tpe_gain_vs_goodnatured_for_female   = 2
wp_tpe_loss_vs_goodnatured_for_female   = 1

### UPSTANDING ### - moralizing, benevolent, pragmatic
wp_tpe_gain_vs_upstanding_for_male      = 1
wp_tpe_loss_vs_upstanding_for_male      = 1
wp_tpe_gain_vs_upstanding_for_female    = 1
wp_tpe_loss_vs_upstanding_for_female    = 1

### ROGUISH ### - used for commons, specifically ex-companions. Tries to live life as a lord to the full
wp_tpe_gain_vs_roguish_for_male         = 2
wp_tpe_loss_vs_roguish_for_male         = 1
wp_tpe_gain_vs_roguish_for_female       = 2
wp_tpe_loss_vs_roguish_for_female       = 1

### BENEFACTOR ### - used for commons, specifically ex-companions. Tries to improve lot of folks on land
wp_tpe_gain_vs_benefactor_for_male      = 1
wp_tpe_loss_vs_benefactor_for_male      = 1
wp_tpe_gain_vs_benefactor_for_female    = 1
wp_tpe_loss_vs_benefactor_for_female    = 1

### CUSTODIAN ### - used for commons, specifically ex-companions. Tries to maximize fief's earning potential
wp_tpe_gain_vs_custodian_for_male       = 1
wp_tpe_loss_vs_custodian_for_male       = 1
wp_tpe_gain_vs_custodian_for_female     = 1
wp_tpe_loss_vs_custodian_for_female     = 1

### CONVENTIONAL ### - Charlotte York in SATC seasons 1-2, probably most medieval aristocrats
wp_tpe_gain_vs_conventional_for_male    = 1
wp_tpe_loss_vs_conventional_for_male    = 0
wp_tpe_gain_vs_conventional_for_female  = 0
wp_tpe_loss_vs_conventional_for_female  = 2

### ADVENTUROUS ### - Tomboyish. However, this basically means that she likes to travel and hunt, and perhaps yearn for wider adventures. 
#                     However, medieval noblewomen who fight are rare, and those that attempt to live independently of a man are rarer still, 
#                     and best represented by pre-scripted individuals like companions
wp_tpe_gain_vs_adventurous_for_male     = 2
wp_tpe_loss_vs_adventurous_for_male     = 1
wp_tpe_gain_vs_adventurous_for_female   = 3
wp_tpe_loss_vs_adventurous_for_female   = 1

### OTHERWORLDLY ### - Prone to mysticism, romantic.
wp_tpe_gain_vs_otherworldly_for_male    = 2
wp_tpe_loss_vs_otherworldly_for_male    = 1
wp_tpe_gain_vs_otherworldly_for_female  = 1
wp_tpe_loss_vs_otherworldly_for_female  = 1

### AMBITIOUS ### - Lady Macbeth
wp_tpe_gain_vs_ambitious_for_male       = 2
wp_tpe_loss_vs_ambitious_for_male       = 1
wp_tpe_gain_vs_ambitious_for_female     = 0
wp_tpe_loss_vs_ambitious_for_female     = 2

### MORALIST ### - Equivalent of upstanding or benefactor -- takes nobless oblige, and her traditional role as repository of morality, very seriously.
wp_tpe_gain_vs_moralist_for_male        = 0
wp_tpe_loss_vs_moralist_for_male        = 1
wp_tpe_gain_vs_moralist_for_female      = 0
wp_tpe_loss_vs_moralist_for_female      = 2

###########################################################################################################################
#####                                               LEVEL SCALING                                                     #####
###########################################################################################################################
tpe_xp_table                            = "trp_tpe_xp_table"
tpe_scaled_troops_begin                 = "trp_tpe_generic_troop_1"
tpe_scaled_troops_end                   = "trp_tpe_generic_troop_32"
tpe_scaled_champions_begin              = tpe_scaled_troops_begin      # These are your Sir X of Y troops.
tpe_scaled_champions_end                = "trp_tpe_generic_troop_4"
tpe_scaled_veterans_begin               = tpe_scaled_champions_end     # These are your Sir X troops.
tpe_scaled_veterans_end                 = "trp_tpe_generic_troop_9"
tpe_scaled_normals_begin                = "trp_tpe_generic_troop_10"   # These are the standard generic troops.
wp_tpe_scaling_disabled_default_level   = 24
wp_tpe_attribute_per_level_numerator    = 2    # troop stat = (character level * numerator) / (denominator)
wp_tpe_attribute_per_level_denominator  = 3
wp_tpe_attribute_threshold              = 30   # This is the hard limit for stat improvement.
wp_tpe_skill_per_3_levels_numerator     = 4
wp_tpe_skill_per_3_levels_denominator   = 5
wp_tpe_skill_threshold                  = 10   # This is the hard limit for any skill.
wp_tpe_skill_minimum                    = 2
wp_tpe_proficiency_gain_per_level       = 7
wp_tpe_proficiency_threshold            = 400  # This is the hard limit for any weapon proficiency.
wp_tpe_proficiency_minimum              = 21
wp_tpe_level_bonus_for_title            = 9
wp_tpe_level_bonus_for_traveler         = 9
# Naming system
wp_tpe_male_names_begin                 = "str_tpe_name_00"
wp_tpe_male_names_end                   = "str_male_name_end"
# wp_tpe_female_names_begin               = "str_female_name_001"
# wp_tpe_female_names_end                 = "str_female_name_end"
wp_tpe_titles_begin                     = "str_tpe_title_captain"
wp_tpe_titles_end                       = "str_tpe_titles_end"
wp_tpe_max_distance_traveling_people    = 100  # This sets how far away a city can be chosen for "<person> of <city>" names.
# wp_tpe_chance_of_traveler               = 20   # This sets the % of participants that aren't local thus have a title.
# wp_tpe_chance_of_soldier                = 45   # This is checked after the one above.  So subtract that % from this one.
wp_tpe_easy_proficiency_bonus           = 0
wp_tpe_medium_proficiency_bonus         = 50
wp_tpe_hard_proficiency_bonus           = 100
wp_tpe_champion_damage_absorb_factor    = 30

# Faction Images
tpe_faction_6_lords_begin               = "trp_knight_6_1"
tpe_faction_6_lords_end                 = "trp_kingdom_1_pretender"
tpe_faction_5_lords_begin               = "trp_knight_5_1"
tpe_faction_5_lords_end                 = tpe_faction_6_lords_begin
tpe_faction_4_lords_begin               = "trp_knight_4_1"
tpe_faction_4_lords_end                 = tpe_faction_5_lords_begin
tpe_faction_3_lords_begin               = "trp_knight_3_1"
tpe_faction_3_lords_end                 = tpe_faction_4_lords_begin
tpe_faction_2_lords_begin               = "trp_knight_2_1"
tpe_faction_2_lords_end                 = tpe_faction_3_lords_begin
tpe_faction_1_lords_begin               = "trp_knight_1_1"
tpe_faction_1_lords_end                 = tpe_faction_2_lords_begin

###########################################################################################################################
#####                                            NEIGHBORING FACTIONS                                                 #####
###########################################################################################################################
# Setting these determines which neighboring factions a lord might consider attending a tournament at as long as they aren't at war.
DEBUG_TPE_general_neighboring_feasts         = 1
# Note: If you do not wish additional regions set then make that value -1.
# Swadia - fac_kingdom_1
wp_tpe_kingdom_1_neighbor_1             = "fac_kingdom_4"
wp_tpe_kingdom_1_neighbor_2             = "fac_kingdom_5"
wp_tpe_kingdom_1_neighbor_3             = "fac_kingdom_6"
wp_tpe_kingdom_1_neighbor_4             = "fac_kingdom_3"
# Vaegir - fac_kingdom_2
wp_tpe_kingdom_2_neighbor_1             = "fac_kingdom_4"
wp_tpe_kingdom_2_neighbor_2             = "fac_kingdom_3"
wp_tpe_kingdom_2_neighbor_3             = -1
wp_tpe_kingdom_2_neighbor_4             = -1
# Khergit - fac_kingdom_3
wp_tpe_kingdom_3_neighbor_1             = "fac_kingdom_4"
wp_tpe_kingdom_3_neighbor_2             = "fac_kingdom_2"
wp_tpe_kingdom_3_neighbor_3             = "fac_kingdom_1"
wp_tpe_kingdom_3_neighbor_4             = "fac_kingdom_6"
# Nord - fac_kingdom_4
wp_tpe_kingdom_4_neighbor_1             = "fac_kingdom_1"
wp_tpe_kingdom_4_neighbor_2             = "fac_kingdom_2"
wp_tpe_kingdom_4_neighbor_3             = "fac_kingdom_3"
wp_tpe_kingdom_4_neighbor_4             = -1
# Rhodoks - fac_kingdom_5
wp_tpe_kingdom_5_neighbor_1             = "fac_kingdom_1"
wp_tpe_kingdom_5_neighbor_2             = "fac_kingdom_6"
wp_tpe_kingdom_5_neighbor_3             = -1
wp_tpe_kingdom_5_neighbor_4             = -1
# Sarranid - fac_kingdom_6
wp_tpe_kingdom_6_neighbor_1             = "fac_kingdom_3"
wp_tpe_kingdom_6_neighbor_2             = "fac_kingdom_5"
wp_tpe_kingdom_6_neighbor_3             = "fac_kingdom_1"
wp_tpe_kingdom_6_neighbor_4             = -1


###########################################################################################################################
#####                                             AWARDS / ACHIEVEMENTS                                               #####
###########################################################################################################################
tpe_award_data          = "trp_tpe_array_tournament_stats"
tpe_award_scaled_xp_factor = 10 # Xp awards = (100 + level*factor) / 100
# TOURNAMENT STATS - Used with trp_tpe_array_tournament_stats
tpe_awards_begin        =  0
tpe_kill_count          =  0 # Many awards will use this value.
# Per Round Stats
tpe_first_blood         =  1 # First kill of the round grants an extra point.
tpe_most_kills          =  2 # Person with the most number of kills gain an extra point.
tpe_horse_slayer        =  3 # 5+ horses killed in the same round.  Just for kicks.
tpe_flawless_victory    =  4 # Every team member (on teams of 2+) survives the round.  Each person gains a point for each teammate (not counting themselves).
tpe_berserker_1         =  5 # 25% of kills (min 3) by one person.  Awards 1 point.
tpe_berserker_2         =  6 # Added in the event two people qualify.
tpe_berserker_3         =  7 # Added in the event three people qualify.
tpe_legendary_warrior_1 =  8 # 50% of kills (min 5) by one person.  Awards 3 points.
tpe_legendary_warrior_2 =  9 # Added in the event two people qualify.
tpe_data_most_kills     = 10 # Data storage for most kills #.
tpe_award_display_passes = 11 # This counts if awards already displayed at end of round to prevent repeated xp gains.
tpe_mythical_warrior    = 13 # You kill EVERYONE by yourself.  Good luck with that.  (shares minimum participants with legendary_warrior).
tpe_cautious_approach   = 14 # You managed to survive the round without defeating anyone.  You coward :P
tpe_awards_end          = 15
# slots 5-10 reserved
# Per Tournament Stats
tpe_survival_min_participants   = 3 # The extra 2 points awarded for surviving the round won't be awarded unless at least this many competitors exist.
tpe_most_kills_min_participants = 6 # The "fiercest competitor" award won't trigger unless at least this many competitors exist.
tpe_berserker_min_participants  = 12 # The 25% of kills award won't trigger unless at least this many competitors exist.
tpe_legendary_min_participants  = 10 # The 50% of kills award won't trigger unless at least this many competitors exist.
tpe_careful_min_participants    = 6  # There needs to be at least six people in the game to consider this award.
# TOURNAMENT STATS end

### ACHIEVEMENT REWARD DEFINITIONS ###
tpe_award_swiftest_cut_renown        = 2
tpe_award_swiftest_cut_xp            = 50
tpe_award_most_kills_renown          = 3
tpe_award_most_kills_xp              = 100
tpe_award_dominant_presence_renown   = 2
tpe_award_dominant_presence_xp       = 100
tpe_award_legendary_presence_renown  = 3
tpe_award_legendary_presence_xp      = 200
tpe_award_mythical_presence_renown   = 10
tpe_award_mythical_presence_xp       = 400
tpe_award_cautious_approach_renown   = -2

###########################################################################################################################
#####                                               VILLAGE BRAWLS                                                    #####
###########################################################################################################################
#wp_tpe_village_brawl_participant       = "trp_trainee_peasant"

# Archery contests
# Strength contests
###########################################################################################################################
#####                                        DEFINITIONS YOU SHOULDN'T CHANGE                                         #####
#####                            Seriously though, these ones if changed will cause errors.                           #####
###########################################################################################################################
wp_tpe_released_version                = 136  # This is to prevent features not yet ready for release from functioning.  No peeking :P
wp_tpe_max_tournament_participants     = 32
wp_tpe_max_tournament_tiers            = 6
wp_tpe_stalemate_timer_limit           = 30   # This cannot be set less than 10 or you'll have errors.  Ideally 30+.
tpe_ranking_array                      = "trp_tpe_array_sorted_troops"
tpe_tournament_roster                  = "trp_tpe_array_static_troops"
# Arena Battle Modes
# abm_fight                            = 0
# abm_training                         = 1
# abm_visit                            = 2
# abm_tournament                       = 3
abm_village_fist_fighting              = 4

# Team Assignments
wp_tpe_red_team                        = 0
wp_tpe_blue_team                       = 1
wp_tpe_green_team                      = 2
wp_tpe_yellow_team                     = 3
# In-Combat Display Types
wp_tpe_icd_rank                        = 1
wp_tpe_icd_award                       = 2
wp_tpe_icd_round_rank                  = 3
# Post Combat Display Types
wp_tpe_round_ranking                   = 0
wp_tpe_tournament_ranking              = 1
# Option Display Modes
wp_tpe_combat_settings                 = 0
wp_tpe_display_settings                = 1
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

# Point Award Strings
tpe_point_eliminated_opponent = 1
tpe_point_won_the_round       = 2
tpe_point_best_scoring_team   = 3

# ICD lifebar settings
tpe_lifebar_pip_size   = 20
tpe_lifebar_pip_width  = 5
tpe_lifebar_outer_width = 9

# PRESENTATION OBJECTS - Used with trp_tpe_presobj
tpe_icd_rank_1_points  = 1
tpe_icd_rank_2_points  = 2
tpe_icd_rank_3_points  = 3
tpe_icd_rank_4_points  = 4
tpe_icd_rank_5_points  = 5
tpe_icd_rank_1_troop   = 6
tpe_icd_rank_2_troop   = 7
tpe_icd_rank_3_troop   = 8
tpe_icd_rank_4_troop   = 9
tpe_icd_rank_5_troop   = 10
tpe_icd_rank_1_team    = 11
tpe_icd_rank_2_team    = 12
tpe_icd_rank_3_team    = 13
tpe_icd_rank_4_team    = 14
tpe_icd_rank_5_team    = 15
tpe_icd_label_points   = 16
tpe_icd_label_troop    = 17
tpe_icd_label_team     = 18
tpe_icd_stalemate_timer = 19
tpe_icd_stalemate_active = 20
#
tpe_icd_team_0_points  = 21
tpe_icd_team_1_points  = 22
tpe_icd_team_2_points  = 23
tpe_icd_team_3_points  = 24
# slots 25-30 reserved
tpe_icd_rank_1_state   = 31
tpe_icd_rank_2_state   = 32
tpe_icd_rank_3_state   = 33
# slots 34 - 40 reserved
tpe_debug_container    = 41
# slots_42 - 49 reserved
tpe_val_team_0_worth   = 50
tpe_val_team_1_worth   = 51
tpe_val_team_2_worth   = 52
tpe_val_team_3_worth   = 53
# slots 54 - 59 currently unused
tpe_obj_team_0_label   = 60
tpe_obj_team_1_label   = 61
tpe_obj_team_2_label   = 62
tpe_obj_team_3_label   = 63
# slots 64 - 69 reserved
tpe_obj_team_0_points  = 70
tpe_obj_team_1_points  = 71
tpe_obj_team_2_points  = 72
tpe_obj_team_3_points  = 73
# slots 74 - 79 reserved
tpe_obj_team_0_lifebar = 80
tpe_obj_team_1_lifebar = 81
tpe_obj_team_2_lifebar = 82
tpe_obj_team_3_lifebar = 83
# slots 84 - 89 reserved
tpe_obj_team_0_outerbar = 90
tpe_obj_team_1_outerbar = 91
tpe_obj_team_2_outerbar = 92
tpe_obj_team_3_outerbar = 93
# slots 94 - 100 currently unused
tpe_rankbox_1_rank     = 101
tpe_rankbox_1_image    = 102
tpe_rankbox_1_name     = 103
tpe_rankbox_1_title    = 104
tpe_rankbox_1_points   = 105
tpe_rankbox_1_pos_x    = 106
tpe_rankbox_1_pos_y    = 107
tpe_rankbox_1_type     = 108
tpe_rankbox_1_award    = 109
# slots 109-110 reserved
tpe_rankbox_2_rank     = 111
tpe_rankbox_2_image    = 112
tpe_rankbox_2_name     = 113
tpe_rankbox_2_title    = 114
tpe_rankbox_2_points   = 115
tpe_rankbox_2_pos_x    = 116
tpe_rankbox_2_pos_y    = 117
tpe_rankbox_2_type     = 118
tpe_rankbox_2_award    = 119
# slots 119-120 reserved
tpe_rankbox_3_rank     = 121
tpe_rankbox_3_image    = 122
tpe_rankbox_3_name     = 123
tpe_rankbox_3_title    = 124
tpe_rankbox_3_points   = 125
tpe_rankbox_3_pos_x    = 126
tpe_rankbox_3_pos_y    = 127
tpe_rankbox_3_type     = 128
tpe_rankbox_3_award    = 129
# slots 129-130 reserved
tpe_rankbox_4_rank     = 131
tpe_rankbox_4_image    = 132
tpe_rankbox_4_name     = 133
tpe_rankbox_4_title    = 134
tpe_rankbox_4_points   = 135

tpe_rankbox_4_award    = 139
# slots 136-140 reserved
tpe_rankbox_5_rank     = 141
tpe_rankbox_5_image    = 142
tpe_rankbox_5_name     = 143
tpe_rankbox_5_title    = 144
tpe_rankbox_5_points   = 145

tpe_rankbox_5_award    = 149
# slots 146-150 reserved
tpe_rankbox_6_rank     = 151
tpe_rankbox_6_image    = 152
tpe_rankbox_6_name     = 153
tpe_rankbox_6_title    = 154
tpe_rankbox_6_points   = 155

tpe_rankbox_6_award    = 159
# slots 156-160 reserved
tpe_rankbox_7_rank     = 161
tpe_rankbox_7_image    = 162
tpe_rankbox_7_name     = 163
tpe_rankbox_7_title    = 164
tpe_rankbox_7_points   = 165

tpe_rankbox_7_award    = 169
# slots 166-170 reserved
tpe_rankbox_8_rank     = 171
tpe_rankbox_8_image    = 172
tpe_rankbox_8_name     = 173
tpe_rankbox_8_title    = 174
tpe_rankbox_8_points   = 175

tpe_rankbox_8_award    = 179
# slots 176-180 reserved
tpe_rankbox_9_rank     = 181
tpe_rankbox_9_image    = 182
tpe_rankbox_9_name     = 183
tpe_rankbox_9_title    = 184
tpe_rankbox_9_points   = 185

tpe_rankbox_9_award    = 189
# slots 186-190 reserved
tpe_rankbox_10_rank    = 191
tpe_rankbox_10_image   = 192
tpe_rankbox_10_name    = 193
tpe_rankbox_10_title   = 194
tpe_rankbox_10_points  = 195

tpe_rankbox_10_award   = 199
# slots 196-200 reserved
tpe_rankbox_11_rank    = 201
tpe_rankbox_11_image   = 202
tpe_rankbox_11_name    = 203
tpe_rankbox_11_title   = 204
tpe_rankbox_11_points  = 205
# slots 206-210 reserved
tpe_checkbox_level_scale = 211
tpe_text_bid_payout      = 212
tpe_text_team_number     = 213
tpe_text_diff_payout     = 214
tpe_checkbox_opt_icd     = 215
tpe_checkbox_opt_damage  = 216
tpe_slider_bet_value     = 217
tpe_text_bet_value       = 218
tpe_slider_team_choice   = 219
tpe_text_team_choice     = 220
tpe_slider_difficulty    = 221
tpe_text_bid_amount      = 222
tpe_text_diff_setting    = 223
tpe_random_diff_enabled  = 224
tpe_options_display_mode = 225
tpe_checkbox_opt_awards  = 226
tpe_text_bet_payout      = 227
tpe_val_cumulative_diff  = 228
tpe_val_bet_odds_num     = 229
tpe_val_bet_odds_den     = 230
tpe_slider_bid_value     = 231
tpe_checkbox_opt_points  = 232
tpe_text_difficulty_score = 233
tpe_checkbox_renown_scale = 234
tpe_label_renown_scale   = 235
tpe_time_of_death        = 236
# slot 237 unused
tpe_checkbox_opt_teampoints = 238
# slot 239 unused
tpe_trigger_enable_icd   = 240
tpe_obj_match_timer      = 241
tpe_obj_menu_troop_pick  = 242
# slot 243 unused
tpe_text_cash_value      = 244
tpe_checkbox_show_health = 245
##
tpe_val_menu_troop_1     = 300
# Reserve slots 301 - 340
slot_agent_hp_bar_name_overlay_id  = 57
# PRESENTATION OBJECTS end

############################################################
#####      PLAYER OPTION SLOTS for TRP_TPE_OPTIONS     #####
############################################################
TPE_OPTIONS              = "trp_tpe_options"
tpe_val_level_scale      = 1 
tpe_val_menu_troop_pick  = 2
tpe_val_show_health      = 3
tpe_val_opt_teampoints   = 4
tpe_val_window_mode      = 5
tpe_val_opt_points       = 6
tpe_val_opt_awards       = 7
tpe_random_team_request  = 8
tpe_val_diff_setting     = 222 # Needs to be moved to tpe_options
tpe_val_bet_wager        = 10
tpe_val_bet_bid          = 11
tpe_val_payout_bonus     = 12

############################################################
##### Presentation Objects for Tournament Design Panel #####
############################################################
# Object definitions (tdp_objects)
tdp_obj_button_done                        = 1
tdp_obj_button_native_settings             = 2
tdp_obj_button_enable_all                  = 3
tdp_obj_label_center_name                  = 4
tdp_obj_label_faction_name                 = 5
tdp_obj_label_lance                        = 6
tdp_obj_label_archery                      = 7
tdp_obj_label_onehand                      = 8
tdp_obj_label_twohand                      = 9
tdp_obj_label_crossbow                     = 10
tdp_obj_label_throwing                     = 11
tdp_obj_label_polearm                      = 12
tdp_obj_label_horse                        = 13
tdp_obj_label_outfit                       = 14
tdp_obj_slider_lance                       = 15
tdp_obj_slider_archery                     = 16
tdp_obj_slider_onehand                     = 17
tdp_obj_slider_twohand                     = 18
tdp_obj_slider_crossbow                    = 19
tdp_obj_slider_throwing                    = 20
tdp_obj_slider_polearm                     = 21
tdp_obj_slider_horse                       = 22
tdp_obj_menu_scene                         = 23
tdp_obj_label_chance_of_lance              = 24
tdp_obj_label_chance_of_archery            = 25
tdp_obj_label_chance_of_onehand            = 26
tdp_obj_label_chance_of_twohand            = 27
tdp_obj_label_chance_of_crossbow           = 28
tdp_obj_label_chance_of_throwing           = 29
tdp_obj_label_chance_of_polearm            = 30
tdp_obj_label_chance_of_horse              = 31
tdp_obj_label_chance_of_outfit             = 32 # Unused
tdp_obj_menu_type_of_lance                 = 33
tdp_obj_menu_type_of_archery               = 34
tdp_obj_menu_type_of_onehand               = 35
tdp_obj_menu_type_of_twohand               = 36
tdp_obj_menu_type_of_crossbow              = 37
tdp_obj_menu_type_of_throwing              = 38
tdp_obj_menu_type_of_polearm               = 39
tdp_obj_menu_type_of_horse                 = 40
tdp_obj_menu_type_of_outfit                = 41
tdp_obj_label_real_chance_of_lance         = 42
tdp_obj_label_real_chance_of_archery       = 43
tdp_obj_label_real_chance_of_onehand       = 44
tdp_obj_label_real_chance_of_twohand       = 45
tdp_obj_label_real_chance_of_crossbow      = 46
tdp_obj_label_real_chance_of_throwing      = 47
tdp_obj_label_real_chance_of_polearm       = 48
tdp_obj_label_real_chance_of_mount         = 49
tdp_obj_button_disable_outfit              = 50 # Unused
tdp_obj_container_center_buttons           = 51
tdp_obj_button_test_scripts                = 52
tdp_obj_checkbox_affect_all_cities         = 53
tdp_val_checkbox_affect_all_cities         = 54


# Break in slots.
tdp_obj_centers_begin                      = 198
tdp_obj_centers_end                        = 199
tdp_obj_button_centers_begin               = 200
# Do not use any slots between 200 - 250 to accomodate 50 towns.  Native has 26 centers.

# Basic data storage
tdp_objects                                = "trp_tpe_presobj"      # These settings are temporary.
tpe_settings                               = "trp_tpe_settings"     # These settings are persistent.  % chance of loading an item type is stored here.
tpe_appearance                             = "trp_tpe_appearance"   # These settings are persistent.  Item IDs based on player settings are stored here.
tpe_weapons                                = "trp_tpe_weapons"      # These settings are persistent.  The basic definitions of what weapons are available to select are stored here.
tpe_menu_options                           = "trp_tpe_center_menus" # These settings are persistent.  The values for menu settings for each city are stored here.
# Slot offset.  Center #5 lance setting = (tdp_center_5_settings * 10) + tdp_obj_checkbox_center_allow_lance = (4 * 10) + 1 = Slot 41
tdp_val_setting_center_no                  = 0 # Shared by both tpe_appearance & tpe_settings
# Stored under tpe_settings.  These slots record the % chance of a given weapon type.
# Stored under tpe_appearance.  These slots record the desired style of weapon for a given weapon type.
tdp_val_setting_lance                      = 1
tdp_val_setting_archery                    = 2
tdp_val_setting_onehand                    = 3
tdp_val_setting_twohand                    = 4
tdp_val_setting_crossbow                   = 5
tdp_val_setting_throwing                   = 6
tdp_val_setting_polearm                    = 7
tdp_val_setting_horse                      = 8
tdp_val_setting_outfit                     = 9 # Unused.

# TPE WEAPONS Definitions
tpe_weapons_lance                          = 10
tpe_weapons_archery                        = 20
tpe_weapons_onehand                        = 30
tpe_weapons_twohand                        = 40
tpe_weapons_crossbow                       = 50
tpe_weapons_throwing                       = 60
tpe_weapons_polearm                        = 70
tpe_weapons_mount                          = 80
tpe_weapons_outfit                         = 90
tpe_weapons_end_of_normal_items            = 100
tpe_weapons_enhanced_lance                 = 110
tpe_weapons_enhanced_archery               = 120
tpe_weapons_enhanced_onehand               = 130
tpe_weapons_enhanced_twohand               = 140
tpe_weapons_enhanced_crossbow              = 150
tpe_weapons_enhanced_throwing              = 160
tpe_weapons_enhanced_polearm               = 170
tpe_weapons_enhanced_mount                 = 180
tpe_weapons_enhanced_outfit                = 190


##### End of Tournament Design Panel #####

###########################################################################################################################
#####                                   TOURNAMENT CREDITS & INFORMATION PANEL                                        #####
###########################################################################################################################
tci_objects                                = "trp_tpe_presobj"      # These settings are temporary.
tci_obj_button_exit                        = 1
tci_obj_button_main_topics                 = 2
tci_obj_label_main_title                   = 3
tci_obj_label_sub_title                    = 4
tci_obj_container_credits                  = 5
tci_obj_container_info                     = 6
tci_obj_topics_begin                       = 7
tci_obj_topics_end                         = 15
# reserve slots for another 10 topics so start next slot at #24.
tci_val_information_mode                   = 24
## TOURNAMENT PLAY ENHANCEMENTS end
