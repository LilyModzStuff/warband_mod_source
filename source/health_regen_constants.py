# Killer Regeneration (1.1) by Windyplains
# Released 8/30/2011

# WHAT THIS FILE DOES:
# Sets health regeneration rates for each type of troop. (player, companion, hero, king, etc).
# Sets the difficulty adjustments if they are being used.

# INSTALLATION INSTRUCTIONS:
# 1) Ensure that constant "wp_hr_debug" at the very bottom is set to 0.  This will prevent debug messages from showing up in game in case I missed it.
# 2) IF you want to enable the difficulty scaling feature set "wp_hr_factor_difficulty" to 1.  Otherwise leave it as 0.

## KILLER REGENERATION (1.1) begin
#  Rates listed below are per kill, not based on duration.  They are also % of health, not exact values.
wp_hr_player_rate                  = 5
wp_hr_strength_factor              = 4   # This is the value STR is divided by.  So 4 = .25% per point of Strength.
wp_hr_leadership_factor            = 2   # This is the value Leadership is divided by.  Only non-heroes gain this.
wp_hr_lord_rate                    = 15
wp_hr_companion_rate               = 10
wp_hr_king_rate                    = 20
wp_hr_common_rate                  = 5
wp_hr_elite_rate                   = 15  # Currently unused.
wp_hr_factor_difficulty            = 0   # This turns ON (1) or OFF (0) any code changes based on difficulty.
wp_hr_diff_enemy_bonus             = 4   # Amount the health regeneration of enemies is boosted by per difficulty rank.
wp_hr_diff_ally_penalty            = -3  # Amount the health regeneration of allies is reduced by per difficulty rank.
wp_hr_debug                        = 0   # This turns ON (1) or OFF (0) all of the debug messages.
## KILLER REGENERATION end
