TOURNAMENT PLAY ENHANCEMENTS (1.2) by Windyplains
Released 9/21/11

###################################################################################################
                                           INSTRUCTIONS
###################################################################################################

INSTALLATION INSTRUCTIONS (with Modmerger):
1) Verify that you have modmerger framework 0.2.5 (last version since Aug 2010) installed.
2) Add the tournament_*.py files to the same directory as your module system *.py files.
3) In "modmerger_options.py" add (under the mods_active section):

   	"tournament",      # Tournament Play Enhancements (1.2)

4) Follow the rest of the file specific instructions listed below.  Some of these items
   should already be done, but are listed to help catch conflicts.

TOURNAMENT_CONSTANTS
1) In module_constants.py you need to do the following:
   a) Verify that the "slot_troop" numbers used below are not already used in your mod.
      This is presently slot #'s 340-357.
   b) Verify that the "slot_center" number used below is not already in use for your mod.
      This is presently slot # 233.
2) In module_items.py you need to define what "normal" or "enhanced" weapons you want the 
   mod to use.  I have designated items that are (non-standard) as such next to their 
   constant below.  Items listed as having a (team color) needs to have 4 of these items 
   in the specific order of red, blue, green and yellow.  The tournament_items.py file
   already includes all needed items (as specified in constants) if you do not wish to
   change them.
3) Ensure that the constants denoting "wp_tpe_bet_tier_#" fit for your module's economy.
   To adjust them simply change the constant values for tiers 1-5.
4) wp_tpe_player_can_disable is set to 1 by default.  This lets players chose if they want
   this mod activated or not.  You can force TPE to always be active by setting this to 0.

TOURNAMENT_GAME_MENUS
1) In module_game_menus.py you need to do the following:
   a) Rename "town_tournament_won" to "orig_town_tournament_won".
   b) Rename "town_tournament" to "orig_town_tournament".
   Note: The new name isn't as important as simply changing the old names so that the menus 
   are replaced on compile.  Yes, I am aware Modmerger should do this itself, but that 
   feature doesn't appear to function properly.  It simply doesn't add the menus if they are 
   duplicate instead of replacing the old ones.

VARIABLES.TXT
1) Add the following list of global variables:

   g_wp_tpe_active
   g_wp_tpe_renown_scaling
   g_wp_tpe_troop


###################################################################################################
                                          TROUBLESHOOTING
###################################################################################################

Problem:  I keep getting strange "DEBUG" messages showing up in game.
Answers:  In tournament_constants.py set wp_tpe_debug to 0 as I must have forgot to upon release.
          Sorry about that and please leave a comment to remind me to fix the download.

Problem:  Why do ranged characters under native rules now have swords instead of daggers?
Answers:  This isn't a bug.  It was intended so that the dynamic weapon AI feature will still work
          even under native rules.

Problem:  Why won't the tournament options menu show up when I join a tournament?
Answer:   Make sure you followed the instruction to rename "town_tournament_won" menu to
          "orig_town_tournament_won".  Otherwise the native version of that menu will take
          precedence.

Problem:  Is my version of modmerger framework up to date enough?
Answer:   Possibly.  Sphere had some odd version numbers listed in his code.  The easiest answer
          is if you have the formations modmerger kit installed then YES.  If not you need to look
          at the bottom of one of your module_game_menu/script/etc files and see if the modmerger
          code begins with "# modmerger_start version=201".  If not get his latest update on
          mbrepository.
          Modmerger: http://www.mbrepository.com/file.php?id=2151


###################################################################################################
                                         HISTORY OF CHANGES
###################################################################################################

Version 1.2  - 9/21/11
 * Completely redesigned the tournament options panel.
 * Added a help display on the tournament options panel that explains each setting.
 * Added the ability for a player to simply disable this mod if wished.  Certain parts of it will
   run in the background regardless, but it will look and feel like native.
 * Added menu options to the main tournament menu to enable or disable this mod returning it to
   native status.  These can be disabled in tournament_constants.py which will cause the mod to
   automatically activate itself.

Version 1.11 - 9/13/11
 * Fixed a bug where the never spawn feature wasn't working.  Simply forgot to copy it over.

Version 1.1  - 8/30/11
 * Fixed a bug where ladies were not gaining reputation upon a tournament win.
 * Fixed a bug where lords were not gaining reputation upon a tournament win.
 * Fixed a bug allowing tournament bets to be placed even when you did not have enough money to 
   do so.
 * Fixed a bug causing the AI to choose a melee weapon over their lance even when mounted.
 * Fixed an oversight where boots were not assigned correctly to troops.  No more shall the
   player run around in the arena hobbit-style.
 * Reworked betting amounts to be constants for easier editing.
 * Repackaged kit in Modmerger format.

Version 1.0  - 7/14/11
 * Initial release.


###################################################################################################
                                            FUTURE PLANS
###################################################################################################

 * Completely reworked ranking system for tournaments.  The plan is to redesign rankings to reflect
   accomplishment more than simply who was the last person or team standing.  This would hopefully
   alleviate the desire to save prior to joining and reload games until the tournament is won.
    * A point system would be utilized based on how many kills are scored (for the team and troop).
    * Points would be awarded to a team for each surviving member left at the end of a round.
    * Troops will not be eliminated for losing in a single round.
    * Tournament winners will simply be the top three ranked troops by point system at the end.

 * New types of tournaments added for variety.
    * Archery tournaments based on destroying an object with winner being the troop that does it
      in the least amount of time with time penalties based on shots attempted and missed.  This
      may include many objects and may be from horseback or not.
    * Jousting tournaments similar to archery design.
    * "Royal Rumble" style free for all matches. (maybe).
    * Animal spearing.  Similar to the archery design only with a moving target using throwing spears.

 * New in combat display showing each team that is active and how many points they have.

 * New display / menu between rounds showing the current standings for individuals.

 * Try to rework the lord's AI to ensure greater participation in tournaments.

 * An improved reward system for winning based on ranking 1st, 2nd or 3rd.

 * Difficulty settings will be implemented so that you can choose how many teams and how large
   they are no matter which town you are in.

 * Troop specialization will add the option to adjust what troops will default to based on what
   their best proficiencies are to improve challenge.