# Character Creation Presentation (1.0.2)
# Created by Windyplains.  Inspired by Dunde's character creation presentation in Custom Commander.



###########################################################################################################################
#####                                                MODULE SETTINGS                                                  #####
###########################################################################################################################



# script_mcc_generate_skill_set modes
limit_to_stats                         = 0
equip_the_player                       = 1

###########################################################################################################################
#####                                              CHARACTER BACKGROUNDS                                              #####
###########################################################################################################################

# character backgrounds
cb_noble = 6
cb_merchant = 5
cb_guard = 4
cb_forester = 3
cb_nomad = 2
cb_thief = 1
cb_priest = 0

cb2_page = 8
cb2_apprentice = 7
cb2_urchin  = 6
cb2_steppe_child = 5
cb2_merchants_helper = 4
##diplomacy start+ add background constants
dplmc_cb2_mummer = 3
dplmc_cb2_courtier = 2
dplmc_cb2_noble = 1
dplmc_cb2_acolyte = 0
##diplomacy end+

# diplomacy start+ add background constants
floris_cb3_slaver = 12
floris_cb3_bandit = 11
floris_cb3_gladiator = 10
floris_cb3_thief = 9
dplmc_cb3_bravo = 8
dplmc_cb3_merc = 7
# diplomacy end+
cb3_poacher = 6
cb3_craftsman = 5
cb3_peddler = 4
# diplomacy start+ add background constants
dplmc_cb3_preacher = 3
# diplomacy end+
cb3_troubadour = 2
cb3_student = 1
cb3_squire = 0
cb3_lady_in_waiting = 0

floris_cb4_duty = 6
cb4_revenge = 5
cb4_loss    = 4
cb4_wanderlust =  3
##diplomacy start+ add background constants
dplmc_cb4_fervor = 2
##diplomacy end+
cb4_disown  = 1
cb4_greed  = 0

kingdom_1 = 5
kingdom_2 = 4
kingdom_3 = 3
kingdom_4 = 2
kingdom_5 = 1
kingdom_6 = 0

###########################################################################################################################
#####                                            PRESENTATION DEFINITIONS                                             #####
###########################################################################################################################
# mcc_objects                            = "trp_tpe_presobj"
# mcc_data                               = "trp_tpe_xp_table"

# Slots of mcc_OBJECTS
mcc_obj_button_done                    = 1
mcc_obj_button_default                 = 2
mcc_obj_button_random                  = 3
mcc_obj_label_menus                    = 4
mcc_obj_label_story                    = 5
mcc_obj_label_gender                   = 6
mcc_obj_label_father                   = 7
mcc_obj_label_earlylife                = 8
mcc_obj_label_later                    = 9
mcc_obj_label_reason                   = 10
mcc_obj_menu_gender                    = 11
mcc_obj_menu_father                    = 12
mcc_obj_menu_earlylife                 = 13
mcc_obj_menu_later                     = 14
mcc_obj_menu_reason                    = 15
mcc_obj_label_options                  = 16
# mcc_obj_menu_trooptrees                = 17
# mcc_val_menu_trooptrees                = 18
# mcc_obj_checkbox_fogofwar              = 19
# mcc_val_checkbox_fogofwar              = 20
# mcc_obj_label_mtt                      = 21
# mcc_obj_checkbox_gather_npcs           = 22
# mcc_val_checkbox_gather_npcs           = 23
mcc_obj_menu_initial_region            = 24
mcc_val_menu_initial_region            = 25
mcc_obj_label_region                   = 26
mcc_obj_label_strength                 = 27
mcc_obj_stat_strength                  = 28
mcc_obj_label_agility                  = 29
mcc_obj_stat_agility                   = 30
mcc_obj_label_intelligence             = 31
mcc_obj_stat_intelligence              = 32
mcc_obj_label_charisma                 = 33
mcc_obj_stat_charisma                  = 34
mcc_obj_stat_gold                      = 35
mcc_obj_stat_renown                    = 36
mcc_obj_stat_weapon_onehand            = 37
mcc_obj_stat_weapon_twohand            = 38
mcc_obj_stat_weapon_polearm            = 39
mcc_obj_stat_weapon_archery            = 40
mcc_obj_stat_weapon_crossbow           = 41
mcc_obj_stat_weapon_throwing           = 42
mcc_obj_stat_container                 = 43
mcc_obj_button_back                    = 44

# Slots of mcc_DATA
# Slots 0-99 reserved.
mcc_item_storage_begin                 = 100
# Slots 101-120 reserved.
mcc_item_storage_end                   = 121
# Swadian items begin.
mcc_swadia_items_begin                 = 130
mcc_swadia_item_trade1                 = 130
mcc_swadia_item_trade2                 = 131
mcc_swadia_item_horse                  = 132
# mcc_swadia_item_richhorse              = 133
mcc_swadia_item_shield                 = 134
mcc_swadia_item_instrument             = 135
# mcc_swadia_item_poorboots              = 136
mcc_swadia_item_boots                  = 137
# mcc_swadia_item_richboots              = 138
# mcc_swadia_item_cloth                  = 139
# mcc_swadia_item_dress                  = 140
mcc_swadia_item_armor                  = 141
# mcc_swadia_item_gauntlets              = 142
# mcc_swadia_item_hood                   = 143
mcc_swadia_item_helmet                 = 144
# mcc_swadia_item_ladyhelmet             = 145
# mcc_swadia_item_axe                    = 146
# mcc_swadia_item_blunt                  = 147
mcc_swadia_item_dagger                 = 148
mcc_swadia_item_spear                  = 149
mcc_swadia_item_sword                  = 150
mcc_swadia_item_bow                    = 151
mcc_swadia_item_arrow                  = 152
mcc_swadia_item_throwing               = 153
mcc_swadia_items_end                   = 154
# slots 155-159 reserved for Swadia.
# Swadian items end.  Vaegir items begin.
mcc_vaegir_items_begin                 = 160
mcc_vaegir_item_trade1                 = 160
mcc_vaegir_item_trade2                 = 161
mcc_vaegir_item_horse                  = 162
# mcc_vaegir_item_richhorse              = 163
mcc_vaegir_item_shield                 = 164
mcc_vaegir_item_instrument             = 165
# mcc_vaegir_item_poorboots              = 166
mcc_vaegir_item_boots                  = 167
# mcc_vaegir_item_richboots              = 168
# mcc_vaegir_item_cloth                  = 169
# mcc_vaegir_item_dress                  = 170
mcc_vaegir_item_armor                  = 171
# mcc_vaegir_item_gauntlets              = 172
# mcc_vaegir_item_hood                   = 173
mcc_vaegir_item_helmet                 = 174
# mcc_vaegir_item_ladyhelmet             = 175
# mcc_vaegir_item_axe                    = 176
# mcc_vaegir_item_blunt                  = 177
mcc_vaegir_item_dagger                 = 178
mcc_vaegir_item_spear                  = 179
mcc_vaegir_item_sword                  = 180
mcc_vaegir_item_bow                    = 181
mcc_vaegir_item_arrow                  = 182
mcc_vaegir_item_throwing               = 183
mcc_vaegir_items_end                   = 184
# slots 185-189 reserved for Vaegir.
# Vaegir items end.  Khergit items begin.
mcc_khergit_items_begin                = 190
mcc_khergit_item_trade1                = 190
mcc_khergit_item_trade2                = 191
mcc_khergit_item_horse                 = 192
# mcc_khergit_item_richhorse             = 193
mcc_khergit_item_shield                = 194
mcc_khergit_item_instrument            = 195
# mcc_khergit_item_poorboots             = 196
mcc_khergit_item_boots                 = 197
# mcc_khergit_item_richboots             = 198
# mcc_khergit_item_cloth                 = 199
# mcc_khergit_item_dress                 = 200
mcc_khergit_item_armor                 = 201
# mcc_khergit_item_gauntlets             = 202
# mcc_khergit_item_hood                  = 203
mcc_khergit_item_helmet                = 204
# mcc_khergit_item_ladyhelmet            = 205
# mcc_khergit_item_axe                   = 206
# mcc_khergit_item_blunt                 = 207
mcc_khergit_item_dagger                = 208
mcc_khergit_item_spear                 = 209
mcc_khergit_item_sword                 = 210
mcc_khergit_item_bow                   = 211
mcc_khergit_item_arrow                 = 212
mcc_khergit_item_throwing              = 213
mcc_khergit_items_end                  = 214
# slots 215-219 reserved for Khergit.
# Khergit items end.  Nord items begin.
mcc_nord_items_begin                   = 220
mcc_nord_item_trade1                   = 220
mcc_nord_item_trade2                   = 221
mcc_nord_item_horse                    = 222
# mcc_nord_item_richhorse                = 223
mcc_nord_item_shield                   = 224
mcc_nord_item_instrument               = 225
# mcc_nord_item_poorboots                = 226
mcc_nord_item_boots                    = 227
# mcc_nord_item_richboots                = 228
# mcc_nord_item_cloth                    = 229
# mcc_nord_item_dress                    = 230
mcc_nord_item_armor                    = 231
mcc_nord_item_gauntlets                = 232
mcc_nord_item_hood                     = 233
mcc_nord_item_helmet                   = 234
# mcc_nord_item_ladyhelmet               = 235
# mcc_nord_item_axe                      = 236
# mcc_nord_item_blunt                    = 237
mcc_nord_item_dagger                   = 238
mcc_nord_item_spear                    = 239
mcc_nord_item_sword                    = 240
mcc_nord_item_bow                      = 241
mcc_nord_item_arrow                    = 242
mcc_nord_item_throwing                 = 243
mcc_nord_items_end                     = 244
# slots 245-249 reserved for Nord.
# Nord items end.  Rhodok items begin.
mcc_rhodok_items_begin                 = 250
mcc_rhodok_item_trade1                 = 250
mcc_rhodok_item_trade2                 = 251
mcc_rhodok_item_horse                  = 252
# mcc_rhodok_item_richhorse              = 253
mcc_rhodok_item_shield                 = 254
mcc_rhodok_item_instrument             = 255
# mcc_rhodok_item_poorboots              = 256
mcc_rhodok_item_boots                  = 257
# mcc_rhodok_item_richboots              = 258
# mcc_rhodok_item_cloth                  = 259
# mcc_rhodok_item_dress                  = 260
mcc_rhodok_item_armor                  = 261
# mcc_rhodok_item_gauntlets              = 262
# mcc_rhodok_item_hood                   = 263
mcc_rhodok_item_helmet                 = 264
# mcc_rhodok_item_ladyhelmet             = 265
# mcc_rhodok_item_axe                    = 266
# mcc_rhodok_item_blunt                  = 267
mcc_rhodok_item_dagger                 = 268
mcc_rhodok_item_spear                  = 269
mcc_rhodok_item_sword                  = 270
mcc_rhodok_item_bow                    = 271
mcc_rhodok_item_arrow                  = 272
mcc_rhodok_item_throwing               = 273
mcc_rhodok_items_end                   = 274
# slots 275-279 reserved for Rhodok.
# Rhodok items end.  Sarrand items begin.
mcc_sarrand_items_begin                = 280
mcc_sarrand_item_trade1                = 280
mcc_sarrand_item_trade2                = 281
mcc_sarrand_item_horse                 = 282
# mcc_sarrand_item_richhorse             = 283
mcc_sarrand_item_shield                = 284
mcc_sarrand_item_instrument            = 285
# mcc_sarrand_item_poorboots             = 286
mcc_sarrand_item_boots                 = 287
# mcc_sarrand_item_richboots             = 288
# mcc_sarrand_item_cloth                 = 289
# mcc_sarrand_item_dress                 = 290
mcc_sarrand_item_armor                 = 291
# mcc_sarrand_item_gauntlets             = 292
# mcc_sarrand_item_hood                  = 293
mcc_sarrand_item_helmet                = 294
# mcc_sarrand_item_ladyhelmet            = 295
# mcc_sarrand_item_axe                   = 296
# mcc_sarrand_item_blunt                 = 297
mcc_sarrand_item_dagger                = 298
mcc_sarrand_item_spear                 = 299
mcc_sarrand_item_sword                 = 300
mcc_sarrand_item_bow                   = 301
mcc_sarrand_item_arrow                 = 302
mcc_sarrand_item_throwing              = 303
mcc_sarrand_items_end                  = 304
# slots 305-309 reserved for Sarrand.
# Sarrand items end.

