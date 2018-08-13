from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *

import collections

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield

MAX_AGE = 0xfc

def age_code(age):
	return min(age, 0xff) << 220

def face_code_with_age(face_code, age):
	return (face_code & (face_code ^ (0xff << 220))) | age_code(age)

def average_face(face_1, face_2):
	age_and_skin_mask = 0xfffffffffffffffff00000000000000000000000000000000000000000000000
	average_features  = 0x000000000000000006db6db6db6db6db00000000000db6db0000000000000000
	return (((face_1 + face_2) / 2) & age_and_skin_mask) + average_features

class CustomTroopTree:
	def __init__(self, id, text, num_branches = 1, num_tiers = 5, levels_start = 4, levels_per_upgrade = 5):
		self.id = id
		self.text = text
		self.num_branches = num_branches
		self.num_tiers = num_tiers
		self.levels_start = levels_start
		self.levels_per_upgrade = levels_per_upgrade
	
	def get_custom_troop_id(self, skin, branch, tier):
		return "cstm_custom_troop_%s_%d_%d_%d" % (self.id, skin.id, branch, tier)
	
	def get_custom_troop_dummy_id(self, skin, branch, tier):
		return "cstm_custom_troop_%s_%d_%d_%d_dummy" % (self.id, skin.id, branch, tier)
	
	def get_custom_troop(self, skin, branch, tier):
		global MAX_AGE
		troop_label = chr(ord('A') + branch) + str(tier + 1)
		fc1 = face_code_with_age(skin.face_code_1, MAX_AGE * tier / self.num_tiers)
		fc2 = face_code_with_age(skin.face_code_2, MAX_AGE * (tier + 1) / self.num_tiers)
		troop_level = int(self.levels_start + tier * self.levels_per_upgrade)
		
		return [self.get_custom_troop_id(skin, branch, tier), "%s Troop" % (troop_label), "%s Troops" % (troop_label), tf_guarantee_all|skin.id, 0, 0, fac_player_supporters_faction, [], level(troop_level)|def_attrib, 0, 0, fc1, fc2]
	
	def get_custom_troop_dummy(self, skin, branch, tier):
		global MAX_AGE
		troop_label = chr(ord('A') + branch) + str(tier + 1)
		fc1 = face_code_with_age(skin.face_code_1, MAX_AGE * tier / self.num_tiers)
		fc2 = face_code_with_age(skin.face_code_2, MAX_AGE * (tier + 1) / self.num_tiers)
		facecode = average_face(fc1, fc2)
		troop_level = int(self.levels_start + tier * self.levels_per_upgrade)
		 
		return [self.get_custom_troop_dummy_id(skin, branch, tier), "%s Troop" % (troop_label), "%s Troops" % (troop_label), tf_guarantee_all|tf_hero|skin.id, 0, 0, fac_player_supporters_faction, [], level(troop_level)|def_attrib, 0, 0, facecode]
	
	def get_custom_troops_of_tier(self, skin, tier):
		troops = []
		
		for branch in xrange(min(tier, self.num_branches)):
			troops.append(self.get_custom_troop(skin, branch, tier - 1))
		
		return troops
	
	def add_to_troop_list_with_skin(self, troop_list, skin, insert_index):
		troops_added = 0
		for tier in xrange(self.num_tiers):
			for branch in xrange(min(tier + 1, self.num_branches)):
				custom_troop = self.get_custom_troop(skin, branch, tier)
				troop_list.insert(insert_index, custom_troop)
				insert_index += 1
				troops_added += 1
				#print custom_troop[0]
				#print "FC1: 0x" + format(custom_troop[11], '064x')
				#print "FC2: 0x" + format(custom_troop[12], '064x')
				
				custom_troop_dummy = self.get_custom_troop_dummy(skin, branch, tier)
				troop_list.append(custom_troop_dummy)
		
		# Update upgrade references, which will be off due to inserting in the middle
		for troop in troop_list[insert_index+1:]:
			if len(troop) >= 15:
				troop[14] += troops_added
				if len(troop) == 16 and troop[15] > 0:
					troop[15] += troops_added
		
		for tier in xrange(self.num_tiers - 1):
			for branch in xrange(min(tier + 1, self.num_branches)):
				if branch == tier and branch < self.num_branches - 1:
					#print "Upgrading %s to %s and %s" % (self.get_custom_troop(skin, branch, tier)[1], self.get_custom_troop(skin, branch, tier + 1)[1], self.get_custom_troop(skin, branch + 1, tier + 1)[1])
					upgrade2(troop_list, self.get_custom_troop_id(skin, branch, tier), self.get_custom_troop_id(skin, branch, tier + 1), self.get_custom_troop_id(skin, branch + 1, tier + 1))
				else:
					#print "Upgrading %s to %s" % (self.get_custom_troop(skin, branch, tier)[1], self.get_custom_troop(skin, branch, tier + 1)[1])
					upgrade(troop_list, self.get_custom_troop_id(skin, branch, tier), self.get_custom_troop_id(skin, branch, tier + 1))