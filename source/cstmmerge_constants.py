import math
from cstm_troop_trees import *

def equipment_funds_available(level):
	return round(240 * math.exp(level * 0.13) - 225, -1)

CUSTOM_TROOP_TREES = [
	CustomTroopTree(id = "1_tier", text = "1 Branch with 7 Tiers", num_branches = 1, num_tiers = 7, levels_start = 4, levels_per_upgrade = 5),
	CustomTroopTree(id = "2_tiers", text = "2 Branches with 6 Tiers", num_branches = 2, num_tiers = 6, levels_start = 4, levels_per_upgrade = 5.5),
	CustomTroopTree(id = "3_tiers", text = "3 Branches with 5 Tiers", num_branches = 3, num_tiers = 5, levels_start = 4, levels_per_upgrade = 6)
]

NEW_TROOP_SLOTS_BEGIN = 500
NEW_PARTY_SLOTS_BEGIN = 500

# Note that the below are for level 0 and before adding 1 to STR for males and 1 to AGI for females
CSTM_STR_START = 6
CSTM_AGI_START = 5
CSTM_INT_START = 6
CSTM_CHA_START = 5

CSTM_WP_LEVELS_START = 40			# Starting proficiency value for custom recruits
CSTM_WP_LEVELS_PER_WM = 15		# Bonus proficiency levels per point in Weapon Master (essentially, the points available to spend will start at the amount necessary to reach 40 in all stats at WM 0, then 55 at WM 1, etc)

CSTM_WP_POINTS_PER_LEVEL = 20	# Bonus Proficiency points available to spend per level
CSTM_WP_POINTS_PER_AGI = 10		# Bonus Proficiency points available to spend per point in AGI

CSTM_IMOD_COST_DIVISOR = 2

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000

woman_face_1 = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2 = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

class Skin:
	def __init__(self, id, text, face_code_1, face_code_2):
		self.id = id
		self.text = text
		self.face_code_1 = face_code_1
		self.face_code_2 = face_code_2

CSTM_SKINS = [
	Skin(tf_male, "Male", man_face_younger_1, man_face_younger_2),
	Skin(tf_female, "Female", woman_face_1, woman_face_2)
]

## ITEM TYPES AVAILABLE FOR EQUIPPING CUSTOM TROOPS
cstm_item_type_strings = {
	itp_type_horse: "Horses",
	itp_type_one_handed_wpn: "One Handed Weapons",
	itp_type_two_handed_wpn: "Two Handed Weapons",
	itp_type_polearm: "Polearms",
	itp_type_arrows: "Arrows",
	itp_type_bolts: "Bolts",
	itp_type_shield: "Shields",
	itp_type_bow: "Bows",
	itp_type_crossbow: "Crossbows",
	itp_type_thrown: "Throwing Weapons",
	itp_type_head_armor: "Caps and Helmets",
	itp_type_body_armor: "Body Armour",
	itp_type_foot_armor: "Boots and Greaves",
	itp_type_hand_armor: "Gloves and Gauntlets",
	itp_type_pistol: "Pistols",
	#itp_type_musket: "Muskets",
	itp_type_bullets: "Bullets"
}

## RANGES OF ATTRIUTES, SKILLS AND PROFICIENCIES THAT CAN BE MODIFIED (skills also need to be active in module_skills)
attributes_begin = ca_strength
attributes_end = ca_charisma + 1

skills_begin = skl_trade
skills_end = skl_reserved_18 + 1

proficiencies_begin = wpt_one_handed_weapon
proficiencies_end = wpt_firearm + 1