# Freelancer (1.3) by Taragoth
# Released 11 July 2011
# Edits by Caba'drin 14 Dec 2011
# Mod-Merger'd by Windyplains, Monnikje and Caba'drin

from module_constants import *

#+FREELANCER start
freelancer_version = 15
#Floris or no Diplomacy:
#freelancer_can_use_item  = "script_troop_can_use_item" 
#with Diplomacy: 
freelancer_can_use_item = "script_dplmc_troop_can_use_item"

#Party Slots #only used for freelancer_party_backup
slot_freelancer_equip_start = 100 #only used for freelancer_party_backup
slot_freelancer_version     = slot_freelancer_equip_start - 2 #only used for freelancer_party_backup

#Faction Slot
slot_faction_freelancer_troop = 101 #should be unused

#Quest Slots
#Only for Freelancer_Enlisted
slot_quest_freelancer_start_xp       = slot_quest_object_state 
slot_quest_freelancer_start_date     = slot_quest_target_state
slot_quest_freelancer_banner_backup  = slot_quest_object_faction
slot_quest_freelancer_next_payday    = slot_quest_target_item
slot_quest_freelancer_upgrade_xp     = slot_quest_target_dna 
slot_quest_freelancer_orig_morale    = slot_quest_giver_center

#Non-Slot Constants for Quests
freelancer_quests_begin = "qst_freelancer_enlisted"
freelancer_quests_end   = "qst_freelancer_end"
plyr_mission_vacation = 1
plyr_mission_captured = 2


#Slots -- deprecated; for the savegame transition
slot_party_orig_morale           = slot_party_ai_rationale
slot_troop_freelancer_start_xp   = slot_troop_signup   #110 -only used for player
slot_troop_freelancer_start_date = slot_troop_signup_2 #111 -only used for player
#+Freelancer end

#For ModMerger
from header_operations import neq, eq
not_in_party = [(neq, "$freelancer_state", 1),]
not_enlisted = [(eq,  "$freelancer_state", 0),]
