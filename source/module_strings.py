# -*- coding: cp1254 -*-
from module_skills import *
from compiler import *
#SB : skill strings from CC, see bottom
strings = [
  ("no_string", "NO STRING!"),
  ("empty_string", " "),
  ("yes", "Yes."),
  ("no", "No."),
# Strings before this point are hardwired.
  ("blank_string", " "),
  ("ERROR_string", "{!}ERROR!!!ERROR!!!!ERROR!!!ERROR!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!!"),
##  ("none", "none"),
  ("noone", "no one"),
##  ("nothing", "nothing"),
  ("s0", "{!}{s0}"),
  ("blank_s1", "{!} {s1}"),
  ("reg1", "{!}{reg1}"),
  ("s50_comma_s51", "{!}{s50}, {s51}"),
  ("s50_and_s51", "{s50} and {s51}"),
  ("s52_comma_s51", "{!}{s52}, {s51}"),
  ("s52_and_s51", "{s52} and {s51}"),
  ("s5_s_party", "{s5}'s Party"),

  ("given_by_s1_at_s2", "Given by {s1} at {s2}"),
  ("given_by_s1_in_wilderness", "Given by {s1} whilst in the field"),
  ("s7_raiders", "{s7} Raiders"),

  ("bandits_eliminated_by_another", "The troublesome bandits have been eliminated by another party."),
  ("msg_battle_won","Battle won! Press tab key to leave..."),
  ("tutorial_map1","You are now viewing the overland map. Left-click on the map to move your party to that location, enter the selected town, or pursue the selected party. Time will pause on the overland map if your party is not moving, waiting or resting. To wait anywhere simply press and hold down the space bar."),


  ("change_color_1", "{!}Change Color 1"),
  ("change_color_2", "{!}Change Color 2"),
  ("change_background", "{!}Change Background Pattern"),
  ("change_flag_type", "{!}Change Flag Type"),
  ("change_map_flag_type", "{!}Change Map Flag Type"),
  ("randomize", "Randomize"),
  ("sample_banner", "{!}Sample banner:"),
  ("sample_map_banner", "{!}Sample map banner:"),
  ("number_of_charges", "{!}Number of charges:"),
  ("change_charge_1",       "{!}Change Charge 1"),
  ("change_charge_1_color", "{!}Change Charge 1 Color"),
  ("change_charge_2",       "{!}Change Charge 2"),
  ("change_charge_2_color", "{!}Change Charge 2 Color"),
  ("change_charge_3",       "{!}Change Charge 3"),
  ("change_charge_3_color", "{!}Change Charge 3 Color"),
  ("change_charge_4",       "{!}Change Charge 4"),
  ("change_charge_4_color", "{!}Change Charge 4 Color"),
  ("change_charge_position", "{!}Change Charge Position"),
  ("choose_position", "{!}Choose position:"),
  ("choose_charge", "{!}Choose a charge:"),
  ("choose_background", "{!}Choose background pattern:"),
  ("choose_flag_type", "{!}Choose flag type:"),
  ("choose_map_flag_type", "{!}Choose map flag type:"),
  ("choose_color", "{!}Choose color:"),
  ("accept", "{!}Accept"),
  ("charge_no_1", "{!}Charge #1:"),
  ("charge_no_2", "{!}Charge #2:"),
  ("charge_no_3", "{!}Charge #3:"),
  ("charge_no_4", "{!}Charge #4:"),
  ("change", "{!}Change"),
  ("color_no_1", "{!}Color #1:"),
  ("color_no_2", "{!}Color #2:"),
  ("charge", "Charge"),
  ("color", "Color"),
  ("flip_horizontal", "Flip Horizontal"),
  ("flip_vertical", "Flip Vertical"),
  ("hold_fire", "Hold Fire"),
  ("blunt_hold_fire", "Blunt / Hold Fire"),

##  ("tutorial_camp1","This is training ground where you can learn the basics of the game. Use A, S, D, W keys to move and the mouse to look around."),
##  ("tutorial_camp2","F is the action key. You can open doors, talk to people and pick up objects with F key. If you wish to leave a town or retreat from a battle, press the TAB key."),
##  ("tutorial_camp3","Training Ground Master wishes to speak with you about your training. Go near him, look at him and press F when you see the word 'Talk' under his name. "),
##  ("tutorial_camp4","To see the in-game menu, press the Escape key. If you select Options, and then Controls from the in-game menu, you can see a complete list of key bindings."),
##  ("tutorial_camp6","You've received your first quest! You can take a look at your current quests by pressing the Q key. Do it now and check the details of your quest."),
##  ("tutorial_camp7","You've completed your quest! Go near Training Ground Master and speak with him about your reward."),
##  ("tutorial_camp8","You've gained some experience and weapon points! Press C key to view your character and increase your weapon proficiencies."),
##  ("tutorial_camp9","Congratulations! You've finished the tutorial of Mount&Blade. Press TAB key to leave the training ground."),

##  ("tutorial_enter_melee", "You are entering the melee weapon training area. The chest nearby contains various weapons which you can experiment with. If you wish to quit this tutorial, press TAB key."),
##  ("tutorial_enter_ranged", "You are entering the ranged weapon training area.  The chest nearby contains various ranged weapons which you can experiment with. If you wish to quit this tutorial, press TAB key."),
##  ("tutorial_enter_mounted", "You are entering the mounted training area. Here, you can try different kinds of weapons while riding a horse. If you wish to quit this tutorial, press TAB key."),

#  ("tutorial_usage_sword", "Sword is a very versatile weapon which is very fast in both attack and defense. Usage of one handed swords are affected by your one handed weapon proficiency. Focus on the sword and press F key to pick it up."),
#  ("tutorial_usage_axe", "Axe is a heavy (and therefore slow) weapon which can deal high damage to the opponent. Usage of one handed axes are affected by your one handed weapon proficiency. Focus on the axe and press F key to pick it up."),
#  ("tutorial_usage_club", "Club is a blunt weapon which deals less damage to the opponent than any other one handed weapon, but it knocks you opponents unconscious so that you can take them as a prisoner. Usage of clubs are affected by your one handed weapon proficiency. Focus on the club and press F key to pick it up."),
#  ("tutorial_usage_battle_axe", "Battle axe is a long weapon and it can deal high damage to the opponent. Usage of battle axes are affected by your two handed weapon proficiency. Focus on the battle axe and press F key to pick it up."),
#  ("tutorial_usage_spear", "Spear is a very long weapon which lets the wielder to strike the opponent earlier. Usage of the spears are affected by your polearm proficiency. Focus on the spear and press F key to pick it up."),
#  ("tutorial_usage_short_bow", "Short bow is a common ranged weapon which is easy to reload but hard to master at. Usage of short bows are affected by your archery proficiency. Focus on the short bow and arrows and press F key to pick them up."),
#  ("tutorial_usage_crossbow", "Crossbow is a heavy ranged weapon which is easy to use and deals high amount of damage to the opponent. Usage of crossbows are affected by your crossbow proficiency. Focus on the crossbow and bolts and press F key to pick them up."),
#  ("tutorial_usage_throwing_daggers", "Throwing daggers are easy to use and throwing them takes a very short time. But they deal light damage to the opponent. Usage of throwing daggers are affected byyour throwing weapon proficiency. Focus on the throwing daggers and press F key to pick it up."),
#  ("tutorial_usage_mounted", "You can use your weapons while you're mounted. Polearms like the lance here can be used for couched damage against opponents. In order to do that, ride your horse at a good speed and aim at your enemy. But do not press the attack button."),

##  ("tutorial_melee_chest", "The chest near you contains some of the melee weapons that can be used throughout the game. Look at the chest now and press F key to view its contents. Click on the weapons and move them to your Arms slots to be able to use them."),
##  ("tutorial_ranged_chest", "The chest near you contains some of the ranged weapons that can be used throughout the game. Look at the chest now and press F key to view its contents. Click on the weapons and move them to your Arms slots to be able to use them."),
##
##  ("tutorial_item_equipped", "You have equipped a weapon. Move your mouse scroll wheel up to wield your weapon. You can also switch between your weapons using your mouse scroll wheel."),

  ("tutorial_ammo_refilled", "Ammo refilled."),
  ("tutorial_failed", "You have been beaten this time, but don't worry. Follow the instructions carefully and you'll do better next time.\
 Press the Tab key to return to to the menu where you can retry this tutorial."),

  ("tutorial_1_msg_1","{!}In this tutorial you will learn the basics of movement and combat.\
 In Mount&Blade: Warband, you use the mouse to control where you are looking, and W, A, S, and D keys of your keyboard to move.\
 Your first task in the training is to locate the yellow flag in the room and move over it.\
 You can press the Tab key at any time to quit this tutorial or to exit any other area in the game.\
 Go to the yellow flag now."),
  ("tutorial_1_msg_2","{!}Well done. Next we will cover attacking with weapons.\
 For the purposes of this tutorial you have been equipped with bow and arrows, a sword and a shield.\
 You can draw different weapons from your weapon slots by using the scroll wheel of your mouse.\
 In the default configuration, scrolling up pulls out your next weapon, and scrolling down pulls out your shield.\
 If you are already holding a shield, scrolling down will put your shield away instead.\
 Try changing your wielded equipment with the scroll wheel now. When you are ready,\
 go to the yellow flag to move on to your next task."),
  ("tutorial_1_msg_3","{!}Excellent. The next part of this tutorial covers attacking with melee weapons.\
 You attack with your currently wielded weapon by using your left mouse button.\
 Press and hold the button to ready an attack, then release the button to strike.\
 If you hold down the left mouse button for a while before releasing, your attack will be more powerful.\
 Now draw your sword and destroy the four dummies in the room."),
  ("tutorial_1_msg_4","{!}Nice work! You've destroyed all four dummies. You can now move on to the next room."),
  ("tutorial_1_msg_5","{!}As you see, there is an archery target on the far side of the room.\
 Your next task is to use your bow to put three arrows into that target. Press and hold down the left mouse button to notch an arrow.\
 You can then fire the arrow by releasing the left mouse button. Note the targeting reticule in the centre of your screen,\
 which shows you the accuracy of your shot.\
 In order to achieve optimal accuracy, let fly your arrow when the reticule is at its smallest.\
 Try to shoot the target now."),
  ("tutorial_1_msg_6","{!}Well done! You've learned the basics of moving and attacking.\
 With a little bit of practice you will soon master them.\
 In the second tutorial you can learn more advanced combat skills and face armed opponents.\
 You can press the Tab key at any time to return to the tutorial menu."),

  ("tutorial_2_msg_1","{!}This tutorial will teach you how to defend yourself with a shield and how to battle armed opponents.\
 For the moment you are armed with nothing but a shield.\
 Your task is not to attack, but to successfully protect yourself from harm with your shield.\
 There is an armed opponent waiting for you in the next room.\
 He will try his best to knock you unconscious, while you must protect yourself with your shield\
 by pressing and holding the right mouse button.\
 Go into the next room now to face your opponent.\
 Remember that you can press the Tab key at any time to quit this tutorial or to exit any other area in the game."),
  ("tutorial_2_msg_2","{!}Press and hold down the right mouse button to raise your shield. Try to remain standing for twenty seconds. You have {reg3} seconds to go."),
  ("tutorial_2_msg_3","{!}Well done, you've succeeded in defending against an armed opponent.\
 The next phase of this tutorial will pit you and your shield against a force of enemy archers.\
 Move on to the next room when you're ready to face an archer."),
  ("tutorial_2_msg_4","{!}Defend yourself from arrows by raising your shield with the right mouse button. Try to remain standing for twenty seconds. You have {reg3} seconds to go."),
  ("tutorial_2_msg_5","{!}Excellent, you've put up a succesful defence against the archer.\
 There is a reward waiting for you in the next room."),
  ("tutorial_2_msg_6","{!}In the default configuration,\
 the F key on your keyboard is used for non-violent interaction with objects and humans in the gameworld.\
 To pick up the sword on the altar, look at it and press F when you see the word 'Equip'."),
  ("tutorial_2_msg_7","{!}A fine weapon! Now you can use it to deliver a bit of payback.\
 Go back through the door and dispose of the archer you faced earlier."),
  ("tutorial_2_msg_8","{!}Very good. Your last task before finishing this tutorial is to face the maceman.\
 Go through the door now and show him your steel!"),
  ("tutorial_2_msg_9","{!}Congratulations! You have now learned how to defend yourself with a shield and even had your first taste of combat with armed opponents.\
 Give it a bit more practice and you'll soon be a renowned swordsman.\
 The next tutorial covers directional defence, which is one of the most important elements of Mount&Blade: Warband combat.\
 You can press the Tab key at any time to return to the tutorial menu."),

  ("tutorial_3_msg_1","{!}This tutorial is intended to give you an overview of parrying and defence without a shield.\
 Parrying attacks with your weapon is a little bit more difficult than blocking them with a shield.\
 When you are defending with a weapon, you are only protected from one direction, the direction in which your weapon is set.\
 If you are blocking upwards, you will parry any overhead swings coming against you, but you will not stop thrusts or attacks to your sides.\
 Either of these attacks would still be able to hit you.\
 That's why, in order to survive without a shield, you must learn directional defence.\
 Go pick up the quarterstaff by pressing the F key now to begin practice."),
  ("tutorial_3_msg_2","{!}By default, the direction in which you defend (by clicking and holding your right mouse button) is determined by the attack direction of your closest opponent.\
 For example, if your opponent is readying a thrust attack, pressing and holding the right mouse button will parry thrust attacks, but not side or overhead attacks.\
 You must watch your opponent carefully and only initiate your parry AFTER the enemy starts to attack.\
 If you start BEFORE he readies an attack, you may parry the wrong way altogether!\
 Now it's time for you to move on to the next room, where you'll have to defend yourself against an armed opponent.\
 Your task is to defend yourself successfully for twenty seconds with no equipment other than a simple quarterstaff.\
 Your quarterstaff's attacks are disabled for this tutorial, so don't worry about attacking and focus on your defence instead.\
 Move on to the next room when you are ready to initiate the fight."),
  ("tutorial_3_msg_3","{!}Press and hold down the right mouse button to defend yourself with your staff after your opponent starts his attack.\
 Try to remain standing for twenty seconds. You have {reg3} seconds to go."),
  ("tutorial_3_msg_4","{!}Well done, you've succeeded this trial!\
 Now you will be pitted against a more challenging opponent that will make things more difficult for you.\
 Move on to the next room when you're ready to face him."),
  ("tutorial_3_msg_5","{!}Press and hold down the right mouse button to defend yourself with your staff after your opponent starts his attack.\
 Try to remain standing for twentys seconds. You have {reg3} seconds to go."),
  ("tutorial_3_msg_6","{!}Congratulations, you still stand despite the enemy's best efforts.\
 The time has now come to attack as well as defend.\
 Approach the door and press the F key when you see the text 'Next level'."),

  ("tutorial_3_2_msg_1","{!}Your staff's attacks have been enabled again. Your first opponent is waiting in the next room.\
 Defeat him by a combination of attack and defence."),
  ("tutorial_3_2_msg_2","{!}Defeat your opponent with your quarterstaff."),
  ("tutorial_3_2_msg_3","{!}Excellent. Now the only thing standing in your way is one last opponent.\
 He is in the next room. Move in and knock him down."),
  ("tutorial_3_2_msg_4","{!}Defeat your opponent with your quarterstaff."),
  ("tutorial_3_2_msg_5","{!}Well done! In this tutorial you have learned how to fight ably without a shield.\
 Train hard and train well, and no one shall be able to lay a stroke on you.\
 In the next tutorial you may learn horseback riding and cavalry combat.\
 You can press the Tab key at any time to return to the tutorial menu."),

  ("tutorial_4_msg_1","{!}Welcome to the fourth tutorial.\
 In this sequence you'll learn about riding a horse and how to perform various martial exercises on horseback.\
 We'll start by getting you mounted up.\
 Approach the horse, and press the 'F' key when you see the word 'Mount'."),
  ("tutorial_4_msg_2","{!}While on horseback, W, A, S, and D keys control your horse's movement, not your own.\
 Ride your horse and try to follow the yellow flag around the course.\
 When you reach the flag, it will move to the next waypoint on the course until you reach the finish."),
  ("tutorial_4_msg_3","{!}Very good. Next we'll cover attacking enemies from horseback. Approach the yellow flag now."),
  ("tutorial_4_msg_4","{!}Draw your sword (using the mouse wheel) and destroy the two targets.\
 Try hitting the dummies as you pass them at full gallop -- this provides an extra challenge,\
 but the additional speed added to your blow will allow you to do more damage.\
 The easiest way of doing this is by pressing and holding the left mouse button until the right moment,\
 releasing it just before you pass the target."),
  ("tutorial_4_msg_5","{!}Excellent work. Now let us try some target shooting from horseback. Go near the yellow flag now."),
  ("tutorial_4_msg_6","{!}Locate the archery target beside the riding course and shoot it three times with your bow.\
 Although you are not required to ride while shooting, it's recommended that you try to hit the target at various speeds and angles\
 to get a feel for how your horse's speed and course affects your aim."),
  ("tutorial_4_msg_7","{!}Congratulations, you have finished this tutorial.\
 You can press the Tab key at any time to return to the tutorial menu."),
# Ryan END

  ("tutorial_5_msg_1","{!}TODO: Follow order to the flag"),
  ("tutorial_5_msg_2","{!}TODO: Move to the flag, keep your units at this position"),
  ("tutorial_5_msg_3","{!}TODO: Move to the flag to get the archers"),
  ("tutorial_5_msg_4","{!}TODO: Move archers to flag1, infantry to flag2"),
  ("tutorial_5_msg_5","{!}TODO: Enemy is charging. Fight!"),
  ("tutorial_5_msg_6","{!}TODO: End of battle."),

  ("trainer_help_1", "{!}This is a training ground where you can learn the basics of the game. Use W, A, S, and D keys to move and the mouse to look around."),
  ("trainer_help_2", "{!}To speak with the trainer, go near him, look at him and press the 'F' key when you see the word 'Talk' under his name.\
 When you wish to leave this or any other area or retreat from a battle, you can press the TAB key."),

  ("custom_battle_1", "{!}Lord Haringoth of Swadia is travelling with his household knights when he spots a group of raiders preparing to attack a small hamlet.\
 Shouting out his warcry, he spurs his horse forward, and leads his loyal men to a fierce battle."),
  ("custom_battle_2", "{!}Lord Mleza is leading a patrol of horsemen and archers\
 in search of a group of bandits who plundered a caravan and ran away to the hills.\
 Unfortunately the bandits have recently met two other large groups who want a share of their booty,\
 and spotting the new threat, they decide to combine their forces."),
  ("custom_battle_3", "{!}Lady Brina is leading the defense of her castle against a Swadian army.\
 Now, as the besiegers prepare for a final assault on the walls, she must make sure the attack does not succeed."),
  ("custom_battle_4", "{!}When the scouts inform Lord Grainwad of the presence of an enemy war band,\
 he decides to act quickly and use the element of surprise against superior numbers."),
  ("custom_battle_5", "{!}Lord Haeda has brought his fierce huscarls into the south with the promise of plunder.\
 If he can make this castle fall to him today, he will settle in these lands and become the ruler of this valley."),

  ("finished", "(Finished)"),

  ("delivered_damage", "Delivered {reg60} damage."),
  ("archery_target_hit", "Distance: {reg61} yards. Score: {reg60}"),

  ("use_baggage_for_inventory","Use your baggage to access your inventory during battle (it's at your starting position)."),
##  ("cant_leave_now","Can't leave the area now."),
  ("cant_use_inventory_now","Can't access inventory now."),
  ("cant_use_inventory_arena","Can't access inventory in the arena."),
  ("cant_use_inventory_disguised","Can't access inventory while you're disguised."),
  ("cant_use_inventory_tutorial","Can't access inventory in the training camp."),
  ("1_denar", "1 denar"),
  ("reg1_denars", "{reg1} denars"),
  ("january_reg1_reg2", "January {reg1}, {reg2}"),
  ("february_reg1_reg2", "February {reg1}, {reg2}"),
  ("march_reg1_reg2", "March {reg1}, {reg2}"),
  ("april_reg1_reg2", "April {reg1}, {reg2}"),
  ("may_reg1_reg2", "May {reg1}, {reg2}"),
  ("june_reg1_reg2", "June {reg1}, {reg2}"),
  ("july_reg1_reg2", "July {reg1}, {reg2}"),
  ("august_reg1_reg2", "August {reg1}, {reg2}"),
  ("september_reg1_reg2", "September {reg1}, {reg2}"),
  ("october_reg1_reg2", "October {reg1}, {reg2}"),
  ("november_reg1_reg2", "November {reg1}, {reg2}"),
  ("december_reg1_reg2", "December {reg1}, {reg2}"),

##  ("you_approach_town","You approach the town of "),
##  ("you_are_in_town","You are in the town of "),
##  ("you_are_in_castle","You are at the castle of "),
##  ("you_sneaked_into_town","You have sneaked into the town of "),

  ("town_nighttime"," It is late at night and honest folk have abandoned the streets."),
  ("door_locked","The door is locked."),
  ("castle_is_abondened","The castle seems to be unoccupied."),
  ("town_is_abondened","The town has no garrison defending it."),
  ("place_is_occupied_by_player","The place is held by your own troops."),
  ("place_is_occupied_by_enemy", "The place is held by hostile troops."),
  ("place_is_occupied_by_friendly", "The place is held by friendly troops."),

  ("do_you_want_to_retreat", "Are you sure you want to retreat?"),
  ("give_up_fight", "Give up the fight?"),
  ("do_you_wish_to_leave_tutorial", "Do you wish to leave the tutorial?"),
  ("do_you_wish_to_surrender", "Do you wish to surrender?"),
  ("can_not_retreat", "Can't retreat, there are enemies nearby!"),
##  ("can_not_leave", "Can't leave. There are enemies nearby!"),

  ("s1_joined_battle_enemy", "{s1} has joined the battle on the enemy side."),
  ("s1_joined_battle_friend", "{s1} has joined the battle on your side."),

#  ("entrance_to_town_forbidden","It seems that the town guards have been warned of your presence and you won't be able to enter the town unchallenged."),
  ("entrance_to_town_forbidden","The town guards are on the lookout for intruders and it seems that you won't be able to pass through the gates unchallenged."),
  ("sneaking_to_town_impossible","The town guards are alarmed. You wouldn't be able to sneak through that gate no matter how well you disguised yourself."),

  ("battle_won", "You have won the battle!"),
  ("battle_lost", "You have lost the battle!"),

  ("attack_walls_success", "After a bloody fight, your brave soldiers manage to claim the walls from the enemy."),
  ("attack_walls_failure", "Your soldiers fall in waves as they charge the walls, and the few who remain alive soon rout and run away, never to be seen again."),
  ("attack_walls_continue", "A bloody battle ensues and both sides fight with equal valour. Despite the efforts of your troops, the castle remains in enemy hands."),

  ("order_attack_success", "Your men fight bravely and defeat the enemy."),
  ("order_attack_failure", "You watch the battle in despair as the enemy cuts your soldiers down, then easily drives off the few ragged survivors."),
  ("order_attack_continue", "Despite an extended skirmish, your troops were unable to win a decisive victory."),

  ("join_order_attack_success", "Your men fight well alongside your allies, sharing in the glory as your enemies are beaten."),
  ("join_order_attack_failure", "You watch the battle in despair as the enemy cuts your soldiers down, then easily drives off the few ragged survivors."),
  ("join_order_attack_continue", "Despite an extended skirmish, neither your troops nor your allies were able to win a decisive victory over the enemy."),

  ("siege_defender_order_attack_success", "The men of the garrison hold their walls with skill and courage, breaking the enemy assault and skillfully turning the defeat into a full-fledged rout."),
  ("siege_defender_order_attack_failure", "The assault quickly turns into a bloodbath. Valiant efforts are for naught; the overmatched garrison cannot hold the walls, and the enemy puts every last defender to the sword."),
  ("siege_defender_order_attack_continue", "Repeated, bloody attempts on the walls fail to gain any ground, but too many enemies remain for the defenders to claim a true victory. The siege continues."),


  ("hero_taken_prisoner", "{s1} of {s3} has been taken prisoner by {s2}."),
  ("hero_freed", "{s1} of {s3} has been freed from captivity by {s2}."),
  ("center_captured", "{s2} have taken {s1} from {s3}."),

  ("troop_relation_increased", "Your relation with {s1} has increased from {reg1} to {reg2}."),
  ("troop_relation_detoriated", "Your relation with {s1} has deteriorated from {reg1} to {reg2}."),
  ("faction_relation_increased", "Your relation with {s1} has increased from {reg1} to {reg2}."),
  ("faction_relation_detoriated", "Your relation with {s1} has deteriorated from {reg1} to {reg2}."),

  ("party_gained_morale", "Your party gains {reg1} morale."),
  ("party_lost_morale",   "Your party loses {reg1} morale."),
  ("other_party_gained_morale", "{s1} gains {reg1} morale."),
  ("other_party_lost_morale",   "{s1} loses {reg1} morale."),

  ("qst_follow_spy_noticed_you", "The spy has spotted you! He's making a run for it!"),
  ("father", "father"),
  ("husband", "husband"),
  ("wife", "wife"),
  ("daughter", "daughter"),
  ("mother", "mother"),
  ("son", "son"),
  ("brother", "brother"),
  ("sister", "sister"),
  ("he", "He"),
  ("she", "She"),
  ("s3s_s2", "{s3}'s {s2}"),
  ("s5_is_s51", "{s5} is {s51}."),
  ("s5_is_the_ruler_of_s51", "{s5} is the ruler of {s51}. "),
##diplomacy start+ make gender correct using reg4
  ("s5_is_a_nobleman_of_s6", "{s5} is a {reg4?noblewoman:nobleman} of {s6}. "),#-- update fix 2011-04-08, ternary was messed up
##diplomacy end+
##  ("your_debt_to_s1_is_changed_from_reg1_to_reg2", "Your debt to {s1} is changed from {reg1} to {reg2}."),

  ("relation_mnus_100", "Vengeful"), # -100..-94
  ("relation_mnus_90",  "Vengeful"),  # -95..-84
  ("relation_mnus_80",  "Vengeful"),
  ("relation_mnus_70",  "Hateful"),
  ("relation_mnus_60",  "Hateful"),
  ##diplomacy start+
  # What the hell?!  These stupid spaces make otherwise-useful constants unusable.
  # Changing them to strip out the space padding.
#  ("relation_mnus_50",  " Hostile"),
#  ("relation_mnus_40",  "  Angry"),
#  ("relation_mnus_30",  "    Resentful"),
#  ("relation_mnus_20",  "      Grumbling"),
#  ("relation_mnus_10",  "        Suspicious"),
#  ("relation_plus_0",   "         Indifferent"),# -5...4
#  ("relation_plus_10",  "          Cooperative"), # 5..14
#  ("relation_plus_20",  "           Welcoming"),
#  ("relation_plus_30",  "            Favorable"),
#  ("relation_plus_40",  "             Supportive"),
#  ("relation_plus_50",  "              Friendly"),
#  ("relation_plus_60",  "               Gracious"),
#  ("relation_plus_70",  "                 Fond"),
#  ("relation_plus_80",  "                  Loyal"),
#  ("relation_plus_90",  "                   Devoted"),
  ("relation_mnus_50",  " Hostile".strip()),
  ("relation_mnus_40",  "  Angry".strip()),
  ("relation_mnus_30",  "    Resentful".strip()),
  ("relation_mnus_20",  "      Grumbling".strip()),
  ("relation_mnus_10",  "        Suspicious".strip()),
  ("relation_plus_0",   "         Indifferent".strip()),# -5...4
  ("relation_plus_10",  "          Cooperative".strip()), # 5..14
  ("relation_plus_20",  "           Welcoming".strip()),
  ("relation_plus_30",  "            Favorable".strip()),
  ("relation_plus_40",  "             Supportive".strip()),
  ("relation_plus_50",  "              Friendly".strip()),
  ("relation_plus_60",  "               Gracious".strip()),
  ("relation_plus_70",  "                 Fond".strip()),
  ("relation_plus_80",  "                  Loyal".strip()),
  ("relation_plus_90",  "                   Devoted".strip()),
  ##diplomacy end+
  ("relation_mnus_100_ns", "{s60} is vengeful towards you."), # -100..-94
  ("relation_mnus_90_ns",  "{s60} is vengeful towards you."),  # -95..-84
  ("relation_mnus_80_ns",  "{s60} is vengeful towards you."),
  ("relation_mnus_70_ns",  "{s60} is hateful towards you."),
  ("relation_mnus_60_ns",  "{s60} is hateful towards you."),
  ("relation_mnus_50_ns",  "{s60} is hostile towards you."),
  ("relation_mnus_40_ns",  "{s60} is angry towards you."),
  ##diplomacy start+ fix preposition
  #("relation_mnus_30_ns",  "{s60} is resentful against you."),
  ("relation_mnus_30_ns",  "{s60} is resentful towards you."),
  ##diplomacy end+
  ("relation_mnus_20_ns",  "{s60} is grumbling against you."),
  ("relation_mnus_10_ns",  "{s60} is suspicious towards you."),
  ##diplomacy start+ fix preposition
  #("relation_plus_0_ns",   "{s60} is indifferent against you."),# -5...4
  ("relation_plus_0_ns",   "{s60} is indifferent towards you."),# -5...4
  ##diplomacy end+
  ("relation_plus_10_ns",  "{s60} is cooperative towards you."), # 5..14
  ("relation_plus_20_ns",  "{s60} is welcoming towards you."),
  ("relation_plus_30_ns",  "{s60} is favorable to you."),
  ("relation_plus_40_ns",  "{s60} is supportive to you."),
  ("relation_plus_50_ns",  "{s60} is friendly to you."),
  ("relation_plus_60_ns",  "{s60} is gracious to you."),
  ("relation_plus_70_ns",  "{s60} is fond of you."),
  ("relation_plus_80_ns",  "{s60} is loyal to you."),
  ("relation_plus_90_ns",  "{s60} is devoted to you."),

  ("relation_reg1", " Relation: {reg1}"),

  ("center_relation_mnus_100", "The populace hates you with a passion"), # -100..-94
  ("center_relation_mnus_90",  "The populace hates you intensely"), # -95..-84
  ("center_relation_mnus_80",  "The populace hates you strongly"),
  ("center_relation_mnus_70",  "The populace hates you"),
  ("center_relation_mnus_60",  "The populace is hateful to you"),
  ("center_relation_mnus_50",  "The populace is extremely hostile to you"),
  ("center_relation_mnus_40",  "The populace is very hostile to you"),
  ("center_relation_mnus_30",  "The populace is hostile to you"),
  ("center_relation_mnus_20",  "The populace is against you"),
  ("center_relation_mnus_10",  "The populace is opposed to you"),
  ("center_relation_plus_0",   "The populace is indifferent to you"),
  ("center_relation_plus_10",  "The populace is acceptive of you"),
  ("center_relation_plus_20",  "The populace is cooperative to you"),
  ("center_relation_plus_30",  "The populace is somewhat supportive of you"),
  ("center_relation_plus_40",  "The populace is supportive of you"),
  ("center_relation_plus_50",  "The populace is very supportive of you"),
  ("center_relation_plus_60",  "The populace is loyal to you"),
  ("center_relation_plus_70",  "The populace is highly loyal to you"),
  ("center_relation_plus_80",  "The populace is devoted to you"),
  ("center_relation_plus_90",  "The populace is fiercely devoted to you"),

  ("town_prosperity_0",   "The poverty of the town of {s60} is unbearable"),
  ("town_prosperity_10",   "The squalorous town of {s60} is all but deserted."),
  ("town_prosperity_20",   "The town of {s60} looks a wretched, desolate place."),
  ("town_prosperity_30",   "The town of {s60} looks poor and neglected."),
  ("town_prosperity_40",   "The town of {s60} appears to be struggling."),
  ("town_prosperity_50",   "The town of {s60} seems unremarkable."),
  ("town_prosperity_60",   "The town of {s60} seems to be flourishing."),
  ("town_prosperity_70",   "The prosperous town of {s60} is bustling with activity."),
  ("town_prosperity_80",   "The town of {s60} looks rich and well-maintained."),
  ("town_prosperity_90",   "The town of {s60} is opulent and crowded with well-to-do people."),
  ("town_prosperity_100",  "The glittering town of {s60} openly flaunts its great wealth."),

  ("village_prosperity_0",   "The poverty of the village of {s60} is unbearable."),
  ("village_prosperity_10",  "The village of {s60} looks wretchedly poor and miserable."),
  ("village_prosperity_20",  "The village of {s60} looks very poor and desolate."),
  ("village_prosperity_30",  "The village of {s60} looks poor and neglected."),
  ("village_prosperity_40",  "The village of {s60} appears to be somewhat poor and struggling."),
  ("village_prosperity_50",  "The village of {s60} seems unremarkable."),
  ("village_prosperity_60",  "The village of {s60} seems to be flourishing."),
  ("village_prosperity_70",  "The village of {s60} appears to be thriving."),
  ("village_prosperity_80",  "The village of {s60} looks rich and well-maintained."),
  ("village_prosperity_90",  "The village of {s60} looks very rich and prosperous."),
  ("village_prosperity_100", "The village of {s60}, surrounded by vast, fertile fields, looks immensely rich."),

  #Alternatives
  ("town_alt_prosperity_0",   "Those few items sold in the market appear to be priced well out of the range of the inhabitants. The people are malnourished, their animals are sick or dying, and the tools of their trade appear to be broken. The back alleys have been abandoned to flies and mangy dogs."),
  ("town_alt_prosperity_20",   "You hear grumbling in the marketplace about the price of everyday items and the shops are half empty. You see the signs of malnourishment on both people and animals, and both buildings and tools suffer from lack of repair. Many may already have migrated to seek work elsewhere."),
  ("town_alt_prosperity_40",   "You hear the occasional grumble in the marketplace about the price of everyday items, but there appear to be a reasonable amount of goods for sale. You see the occasional abandoned building, shop, or cart, but nothing more than the ordinary."),
  ("town_alt_prosperity_60",   "The people look well-fed and relatively content. Craftsmen do a thriving business, and some migrants appear to be coming here from other regions to seek their luck."),
  ("town_alt_prosperity_80",   "The walls, streets, and homes are well-maintained. The markets are thronged with migrants from the nearby regions drawn here by the availability of both goods and work. The rhythm of hammers and looms speak to the business of the artisans' workshops."),

  ("village_alt_prosperity_0",   "Only a handful of people are strong enough to work in the fields, many of which are becoming overgrown with weeds. The rest are weak and malnourished, or have already fled elsewhere. The draft animals have long since starved or were eaten, although a few carcasses still lie on the outskirts, their bones knawed by wild beasts."),
  ("village_alt_prosperity_20",   "Some farmers and animals are out in the fields, but their small numbers suggest that some villagers may be emigrating in search of food. Farm implements look rusty and broken. Brush and weeds seem to be reclaiming some of the outermost fields."),
  ("village_alt_prosperity_40",   "The fields and orchards are busy, with villagers engaged in the tasks of the seasons. Humans and animals alike look relatively healthy and well-fed. However, a small number of the outermost fields are left unsewn, and some walls are in ill repair, suggesting that there are still not quite enough hands to do all the work which needs to be done."),
  ("village_alt_prosperity_60",   "The fields and orchards are humming with activity, with filled sacks of grain and drying meat testifying to the productivity of the village's cropland and pastureland."),
  ("village_alt_prosperity_80",   "The fields and orchards are humming with activity, with freshly dug irrigation ditches suggest that the farmers have enough spare time and energy to expand area under cultivation. Seasonal laborers appear to be flocking here to help with the work and join in the general prosperity."),

  ("oasis_village_alt_prosperity_0",   "The palm groves are virtually abandoned, and the canals which irrigate them are clogged with silt. The handful of villagers you see look malnourished and restless. The draft animals have long since starved or were eaten, although a few carcasses still lie on the outskirts, their bones knawed by the wild jackals of the desert."),
  ("oasis_village_alt_prosperity_20",   "Few villagers can be seen tending to the palm groves, and in places, the desert dunes appear to be encroaching on the gardens. Many of the canals are clogged with silt, and the wells and cisterns are filled with sand."),
  ("oasis_village_alt_prosperity_40",   "Men and women are busy tending the palm groves, climbing to the tops of trees to pollinate the fruit. Healthy animals draw the pumps and wheels that bring water to the fields. Some of the irrigation canals and cisterns, however, could use some maintenance."),
  ("oasis_village_alt_prosperity_60",   "The palm groves and orchards are humming with activity. Farmers call to each other cheerfully from the tops of the trees, where they pollinate the date fruit. The creak of wooden pumps, the bellowing of draft animals, and the rush of flowing water speak of an irrigation system that is thriving under the villagers' attention."),
  ("oasis_village_alt_prosperity_80",   "The palm groves are humming with activity, as farmers load up a bumper crop of dates for sale to the market. Men and women are hard at work digging new wells and canals, to bring additional land under irrigation."),



  ("acres_grain",       "acres of grainfields"),
  ("acres_orchard",     "acres of orchards and vineyards"),
  ("acres_oasis",       "acres of irrigated oasis gardens"),


  ("looms",     		"looms"),
  ("boats",     		"boats"),
  ("head_cattle",       "head of cattle"),
  ("head_sheep",        "head of sheep"),

  ("mills",     "mills"),
  ("kilns",     "kilns"),
  ("pans",      "pans"),
  ("deposits",  "deposits"),
  ("hives",     "hives"),
  ("breweries", "breweries"),
  ("presses",   "presses"),
  ("smithies",  "smithies"),
  ("caravans",  "overland caravans"),
  ("traps",     "traps"),
  ("gardens",   "small gardens"),
  ("tanneries", "tanning vats"),

  ("master_miller",  "Master miller"),
  ("master_brewer",  "Master brewer"),
  ("master_presser", "Master presser"),
  ("master_smith",   "Master smith"),
  ("master_tanner",  "Master tanner"),
  ("master_weaver",  "Master weaver"),
  ("master_dyer",    "Master dyer"),



  ("war_report_minus_4",   "we are about to lose the war"),
  ("war_report_minus_3",   "the situation looks bleak"),
  ("war_report_minus_2",   "things aren't going too well for us"),
  ("war_report_minus_1",   "we can still win the war if we rally"),
  ("war_report_0",   "we are evenly matched with the enemy"),
  ("war_report_plus_1",   "we have a fair chance of winning the war"),
  ("war_report_plus_2",   "things are going quite well"),
  ("war_report_plus_3",   "we should have no difficulty defeating them"),
  ("war_report_plus_4",   "we are about to win the war"),


  ("persuasion_summary_very_bad", "You try your best to persuade {s50},\
 but none of your arguments seem to come out right. Every time you start to make sense,\
 you seem to say something entirely wrong that puts you off track.\
 By the time you finish speaking you've failed to form a single coherent point in your own favor,\
 and you realise that all you've done was dig yourself deeper into a hole.\
 Unsurprisingly, {s50} does not look impressed."),
  ("persuasion_summary_bad",      "You try to persuade {s50}, but {reg51?she:he} outmanoeuvres you from the very start.\
 Even your best arguments sound hollow to your own ears. {s50}, likewise,\
 has not formed a very high opinion of what you had to say."),
  ("persuasion_summary_average",  "{s50} turns out to be a skilled speaker with a keen mind,\
 and you can't seem to bring forth anything concrete that {reg51?she:he} cannot counter with a rational point.\
 In the end, neither of you manage to gain any ground in this discussion."),
  ("persuasion_summary_good",     "Through quick thinking and smooth argumentation, you manage to state your case well,\
 forcing {s50} to concede on several points. However, {reg51?she:he} still expresses doubts about your request."),
  ("persuasion_summary_very_good","You deliver an impassioned speech that echoes through all listening ears like poetry.\
 The world itself seems to quiet down in order to hear you better .\
 The inspiring words have moved {s50} deeply, and {reg51?she:he} looks much more well-disposed towards helping you."),


# meet_spy_in_enemy_town quest secret sentences
  ("secret_sign_1",  "The armoire dances at midnight..."),
  ("secret_sign_2",  "I am selling these fine Khergit tapestries. Would you like to buy some?"),
  ("secret_sign_3",  "The friend of a friend sent me..."),
  ("secret_sign_4",  "The wind blows hard from the east and the river runs red..."),

  ("countersign_1",  "But does he dance for the dresser or the candlestick?"),
  ("countersign_2",  "Yes I would, do you have any in blue?"),
  ("countersign_3",  "But, my friend, your friend's friend will never have a friend like me."),
  ("countersign_4",  "Have you been sick?"),

# Names
  ("name_1",  "Albard"),
  ("name_2",  "Euscarl"),
  ("name_3",  "Sigmar"),
  ("name_4",  "Talesqe"),
  ("name_5",  "Ritmand"),
  ("name_6",  "Aels"),
  ("name_7",  "Raurqe"),
  ("name_8",  "Bragamus"),
  ("name_9",  "Taarl"),
  ("name_10", "Ramin"),
  ("name_11", "Shulk"),
  ("name_12", "Putar"),
  ("name_13", "Tamus"),
  ("name_14", "Reichad"),
  ("name_15", "Walcheas"),
  ("name_16", "Rulkh"),
  ("name_17", "Marlund"),
  ("name_18", "Auguryn"),
  ("name_19", "Daynad"),
  ("name_20", "Joayah"),
  ("name_21", "Ramar"),
  ("name_22", "Caldaran"),
  ("name_23", "Brabas"),
  ("name_24", "Kundrin"),
  ("name_25", "Pechnak"),

# Surname
  ("surname_1",  "{s50} of Uxhal"),
  ("surname_2",  "{s50} of Wercheg"),
  ("surname_3",  "{s50} of Reyvadin"),
  ("surname_4",  "{s50} of Suno"),
  ("surname_5",  "{s50} of Jelkala"),
  ("surname_6",  "{s50} of Veluca"),
  ("surname_7",  "{s50} of Halmar"),
  ("surname_8",  "{s50} of Curaw"),
  ("surname_9",  "{s50} of Sargoth"),
  ("surname_10", "{s50} of Tihr"),
  ("surname_11", "{s50} of Zendar"),
  ("surname_12", "{s50} of Rivacheg"),
  ("surname_13", "{s50} of Wercheg"),
  ("surname_14", "{s50} of Ehlerdag"),
  ("surname_15", "{s50} of Yaragar"),
  ("surname_16", "{s50} of Burglen"),
  ("surname_17", "{s50} of Shapeshte"),
  ("surname_18", "{s50} of Hanun"),
  ("surname_19", "{s50} of Saren"),
  ("surname_20", "{s50} of Tosdhar"),
  ("surname_21", "{s50} the Long"),
  ("surname_22", "{s50} the Gaunt"),
  ("surname_23", "{s50} Silkybeard"),
  ("surname_24", "{s50} the Sparrow"),
  ("surname_25", "{s50} the Pauper"),
  ("surname_26", "{s50} the Scarred"),
  ("surname_27", "{s50} the Fair"),
  ("surname_28", "{s50} the Grim"),
  ("surname_29", "{s50} the Red"),
  ("surname_30", "{s50} the Black"),
  ("surname_31", "{s50} the Tall"),
  ("surname_32", "{s50} Star-Eyed"),
  ("surname_33", "{s50} the Fearless"),
  ("surname_34", "{s50} the Valorous"),
  ("surname_35", "{s50} the Cunning"),
  ("surname_36", "{s50} the Coward"),
  ("surname_37", "{s50} Bright"),
  ("surname_38", "{s50} the Quick"),
  ("surname_39", "{s50} the Minstrel"),
  ("surname_40", "{s50} the Bold"),
  ("surname_41", "{s50} Hot-Head"),

  ("surnames_end", "surnames_end"),


  ("number_of_troops_killed_reg1", "Number of troops killed: {reg1}"),
  ("number_of_troops_wounded_reg1", "Number of troops wounded: {reg1}"),
  ("number_of_own_troops_killed_reg1", "Number of friendly troops killed: {reg1}"),
  ("number_of_own_troops_wounded_reg1", "Number of friendly troops wounded: {reg1}"),

  ("retreat", "Retreat!"),
  ("siege_continues", "Fighting Continues..."),
  ("casualty_display", "Your casualties: {s10}^Enemy casualties: {s11}{s12}"),
  ("casualty_display_hp", "^You were wounded for {reg1} hit points."),

# Quest log texts
  ("quest_log_updated", "Quest log has been updated..."),

  ("banner_selection_text", "You have been awarded the right to carry a banner.\
 Your banner will signify your status and bring you honour. Which banner do you want to choose?"),


# Retirement Texts: s7=village name; s8=castle name; s9=town name
  ("retirement_text_1", "Only too late do you realise that your money won't last.\
 It doesn't take you long to fritter away what little you bothered to save,\
 and you fare poorly in several desperate attempts to start adventuring again.\
 You end up a beggar in {s9}, living on alms and the charity of the church."),
  ("retirement_text_2", "Only too late do you realise that your money won't last.\
 It doesn't take you long to fritter away what little you bothered to save.\
 Once every denar has evaporated in your hands you are forced to start a life of crime in the backstreets of {s9},\
 using your skills to eke out a living robbing coppers from women and poor townsmen."),
  ("retirement_text_3", "Only too late do you realise that your money won't last.\
 It doesn't take you long to fritter away what little you bothered to save,\
 and you end up a penniless drifter, going from tavern to tavern\
 blagging drinks from indulgent patrons by regaling them with war stories that no one ever believes."),
  ("retirement_text_4", "The silver you've saved doesn't last long,\
 but you manage to put together enough to buy some land near the village of {s7}.\
 There you become a free farmer, and you soon begin to attract potential {wives/husbands}.\
 In time the villagers come to treat you as their local hero.\
 You always receive a place of honour at feasts, and your exploits are told and retold in the pubs and taverns\
 so that the children may keep a memory of you for ever and ever."),
  ("retirement_text_5", "The silver you've saved doesn't last long,\
 but it's enough to buy a small tavern in {s9}. Although the locals are wary of you at first,\
 they soon accept you into their midst. In time your growing tavern becomes a popular feasthall and meeting place.\
 People come for miles to eat or stay there due to your sheer renown and the epic stories you tell of your adventuring days."),
  ("retirement_text_6", "You've saved wisely throughout your career,\
 and now your silver and your intelligence allow you to make some excellent investments to cement your future.\
 After buying several shops and warehouses in {s9}, your shrewdness turns you into one of the most prominent merchants in town,\
 and you soon become a wealthy {man/woman} known as much for your trading empire as your exploits in battle."),
  ("retirement_text_7", "As a landed noble, however minor, your future is all but assured.\
 You settle in your holdfast at {s7}, administrating the village and fields,\
 adjudicating the local courts and fulfilling your obligations to your liege lord.\
 Occasionally your liege calls you to muster and command in his campaigns, but these stints are brief,\
 and you never truly return to the adventuring of your younger days. You have already made your fortune.\
 With your own hall and holdings, you've few wants that your personal wealth and the income of your lands cannot afford you."),
  ("retirement_text_8", "There is no question that you've done very well for yourself.\
 Your extensive holdings and adventuring wealth are enough to guarantee you a rich and easy life for the rest of your days.\
 Retiring to your noble seat in {s8}, you exchange adventure for politics,\
 and you soon establish yourself as a considerable power in your liege lord's kingdom.\
 With intrigue to busy yourself with, your own forests to hunt, a hall to feast in and a hundred fine war stories to tell,\
 you have little trouble making the best of the years that follow."),
  ("retirement_text_9", "As a reward for your competent and loyal service,\
 your liege lord decrees that you be given a hereditary title, joining the major nobility of the realm.\
 Soon you complete your investitute as baron of {s7}, and you become one of your liege's close advisors\
 and adjutants. Your renown garners you much subtle pull and influence as well as overt political power.\
 Now you spend your days playing the games of power, administering your great fiefs,\
 and recounting the old times of adventure and glory."),
  ("retirement_text_10", "Though you started from humble beginnings, your liege lord holds you in high esteem,\
 and a ripple of shock passes through the realm when he names you to the hereditary title of {count/countess} of {s9}.\
 Vast fiefs and fortunes are now yours to rule. You quickly become your liege's most trusted advisor,\
 almost his equal and charged with much of the running of his realm,\
 and you sit a throne in your own splendourous palace as one of the most powerful figures in Calradia."),


#NPC companion changes begin


# Objectionable actions

# humanitarian
  ("loot_village", "attack innocent villagers"),
  ("steal_from_villagers", "steal from poor villagers"),
  ("rob_caravan", "rob a merchant caravan"), # possibly remove
  ("sell_slavery", "sell people into slavery"),
  ("force_into_party", "force peasants into the party"),

# egalitarian
  ("men_hungry", "run out of food"), ##Done - simple triggers
  ("men_unpaid", "not be able to pay the men"),
#  ("party_crushed", "get ourselves slaughtered"), ##Done - game menus
  ("excessive_casualties", "turn every battle into a bloodbath for our side"),

# chivalric
  ("surrender", "surrender to the enemy"), ##Done - game menus
  ("flee_battle", "run from battle"), ##Done - game menus
  ("pay_bandits", "pay off common bandits"),

# honest
  ("fail_quest", "fail a quest which we undertook on word of honour"),

# quest-related strings
  ("squander_money", "squander money given to us in trust"),
  ("murder_merchant", "involve ourselves in cold-blooded murder"),
  ("round_up_serfs", "round up serfs on behalf of some noble"),


# Fates suffered by companions in battle
  ("battle_fate_1", "We were separated in the heat of battle"),
  ("battle_fate_2", "I was wounded and left for dead"),
  ("battle_fate_3", "I was knocked senseless by the enemy"),
  ("battle_fate_4", "I was taken and held for ransom"),
  ("battle_fate_5", "I got captured, but later managed to escape"),


# strings for opinion
  ("npc_morale_report", "I'm {s6} your choice of companions, {s7} your style of leadership, and {s8} the general state of affairs"),
  ("happy", "happy about"),
  ("content", "content with"),
  ("concerned", "concerned about"),
  ("not_happy", "not at all happy about"),
  ("miserable", "downright appalled at"),


  ("morale_reg1",    " Morale: {reg1}"),
  ("bar_enthusiastic", "                   Enthusiastic"),
  ("bar_content",      "              Content"),
  ("bar_weary",        "          Weary"),
  ("bar_disgruntled",  "     Disgruntled"),
  ("bar_miserable",    "  Miserable"),


#other strings
  ("here_plus_space", "here "),


#NPC strings
#npc1 = borcha
#npc2 = marnid
#npc3 = ymira
#npc4 = rolf
#npc5 = baheshtur
#npc6 = firentis
#npc7 = deshavi
#npc8 = matheld
#npc9 = alayen
#npc10 = bunduk
#npc11 = katrin
#npc12 = jeremus
#npc13 = nizar
#npc14 = lazalit
#npc15 = artimenner
#npc16 = klethi

  ("npc1_intro", "Ho there, traveller. You wouldn't by chance be in the market for a tracker, would you?"),
  ("npc2_intro", "Hello. Would you be so kind as to have a cup with me? I'm down to my last five denars and I'd rather not drink alone."),
  ("npc3_intro", "Good day to you!"),
  ("npc4_intro", "Greetings. I am Rolf, son of Rolf, of the most ancient and puissant House of Rolf."),
  ("npc5_intro", "Greetings, traveller. Would you join me for a drink?"),
  ("npc6_intro", "I am lost... Lost..."),
  ("npc7_intro", "Yes? Keep your distance, by the way."),
  ("npc8_intro", "What do you want?"),
  ("npc9_intro", "You there, good {man/woman}, be so kind as to fetch me another drink, eh?"),
  ("npc10_intro", "Greetings there, {Brother/Sister}! Here's to the doom and downfall of all high-born lords and ladies!"),
  ("npc11_intro", "Hello there, {laddie/lassie}. Have a drink on me."),
  ("npc12_intro", "Greetings, fellow traveller. Perhaps you can help me."),
  ("npc13_intro", "Greetings, traveller. I am Nizar. No doubt you will have heard of me."),
  ("npc14_intro", "Yes? What is it you wish?"),
  ("npc15_intro", "Oh! Say, friend, are you by chance heading out of town anytime soon?"),
  ("npc16_intro", "Hello there. From the look of you, I'd say you're expecting to get into some fights in the near future. Are you by any chance looking for some help?"),

  ("npc1_intro_response_1", "Perhaps. What's the urgency?"),
  ("npc2_intro_response_1", "Your last five denars? What happened to you?"),
  ("npc3_intro_response_1", "Hello. What's a clearly well-brought up young lady like you doing in a place like this?"),
  ("npc4_intro_response_1", "Hmm... I have never heard of the House of Rolf."),
  ("npc5_intro_response_1", "Certainly. With whom do I have the pleasure of drinking?"),
  ("npc6_intro_response_1", "Why so gloomy, friend?"),
  ("npc7_intro_response_1", "My apologies. I was merely going to say that you look a bit down on your luck."),
  ("npc8_intro_response_1", "Merely to pass the time of day, ma'am, if you're not otherwise engaged."),
  ("npc9_intro_response_1", "You must have me confused with the tavernkeep, sir."),
  ("npc10_intro_response_1", "Why do you say that, sir?"),
  ("npc11_intro_response_1", "What's the occasion?"),
  ("npc12_intro_response_1", "How is that?"),
  ("npc13_intro_response_1", "Um... I don't think so."),
  ("npc14_intro_response_1", "To pass the time of day with a fellow traveller, if you permit."),
  ("npc15_intro_response_1", "I am. What concern is it of your, may I ask?"),
  ("npc16_intro_response_1", "I could be. What's your story?"),

  ("npc1_intro_response_2", "Step back, sir, and keep your hand away from my purse."),
  ("npc2_intro_response_2", "I have better things to do."),
  ("npc3_intro_response_2", "Run along now, girl. I have work to do."),
  ("npc4_intro_response_2", "Eh? No thanks, we don't want any."),
  ("npc5_intro_response_2", "I have no time for that."),
  ("npc6_intro_response_2", "No doubt. Well, good luck getting found."),
  ("npc7_intro_response_2", "Right. I'll not bother you, then."),
  ("npc8_intro_response_2", "Nothing at all, from one so clearly disinclined to pleasantries. Good day to you."),
  ("npc9_intro_response_2", "Fetch it yourself!"),
  ("npc10_intro_response_2", "That's rebel talk, and I'll hear none of it. Good day to you."),
  ("npc11_intro_response_2", "I think not, madame."),
  ("npc12_intro_response_2", "Sorry, I am afraid that I am otherwise engaged right now."),
  ("npc13_intro_response_2", "No, and I can't say that I much want to make your acquaintance."),
  ("npc14_intro_response_2", "Nothing at all. My apologies."),
  ("npc15_intro_response_2", "I'd be obliged if you minded your own business, sir."),
  ("npc16_intro_response_2", "Mind your own business, lass."),

#backstory intro
  ("npc1_backstory_a", "Well, {sir/madame}, it's a long story..."),
  ("npc2_backstory_a", "It's a tragic tale, sir."),
  ("npc3_backstory_a", "A good question, and I shall tell you!"),
  ("npc4_backstory_a", "Really? Well, perhaps your ignorance can be forgiven. Our ancestral lands are far away, over the mountains."),
  ("npc5_backstory_a", "I am Baheshtur, son of Azabei, grandson of Badzan. Were you not a barbarian, you would likely know from my lineage that I am a Roan Horse Khergit of the highlands, of the tribe of Shamir, of the clan of Dulam, of the family of Ubayn, from the Pantash valley, and you might be able to guess why I am so far from home."),
  ("npc6_backstory_a", "I have commited the greatest of sins, {sir/madame}, and it is to my shame that I must appoint you my confessor, if you should like to hear it."),
  ("npc7_backstory_a", "My luck? You could say that."),
  ("npc8_backstory_a", "Ah. Well, if you must know, I shall tell you."),
  ("npc9_backstory_a", "My most humble apologies. It is sometimes hard to recognize folk amid the smoke and gloom here. I still cannot believe that I must make my home in such a place."),
  ("npc10_backstory_a", "It's a long story, but if you get yourself a drink, I'll be glad to tell it."),
  ("npc11_backstory_a", "Why, I managed to sell my wagon and pots, {lad/lass}. For once I've got money to spend and I intend to make the best of it."),
  ("npc12_backstory_a", "I shall tell you -- but know that it is a tale of gross iniquity. I warn you in advance, lest you are of a choleric temperament, and so become incensed at the injustice done unto me that you do yourself a mischief."),
  ("npc13_backstory_a", "You have not? Then perhaps you will have heard of my steed, who cuts across the Calradian plains like a beam of moonlight? Or of my sword, a connoisseur of the blood of the highest-born princes of the land?"),
  ("npc14_backstory_a", "Very well. I do not mind. My name is Lazalit."),
  ("npc15_backstory_a", "I'm an engineer, specialized in the art of fortification. If you need a wall knocked down, I can do that, given enough time. If you need a wall built back up, I can do that too, although it will take longer and cost you more. And you can't cut costs, either, unless you want your new edifice coming down underneath you, as someone around here has just found out."),
  ("npc16_backstory_a", "Well, {sir/madame}, as long as I can remember I've had a weakness for pretty things, and it's gotten me into trouble, you see."),

#backstory main body
  ("npc1_backstory_b", "I had a bit of a misunderstanding {s19}in {s20} about a horse that I found tied up outside the inn. It was the spitting image of a beast that threw me a few days back and ran off. Naturally I untied it for a closer look. As it turns out, the horse belonged to a merchant, a pinch-faced old goat who wouldn't accept that it all was a simple misunderstanding, and went off to get the guard."),
  ("npc2_backstory_b", "A while back, I left Geroia with a caravan of goods. I was hoping to sell it all in Sargoth and make a hefty sum. But, what do you know... we were ambushed by a party of Khergit raiders who rode away with most of the horses and goods. And two days later, my own caravan guards ran away with the rest of what I had."),
  ("npc3_backstory_b", "My father, a well-known merchant {s19}in {s20}, decided that I should be married to one of his business partners, a man well past the age of 30. I have been an obedient daughter all of my life, but it was a ridiculous and horrid proposition. So I ran away!"),
  ("npc4_backstory_b", "Like all the men of my family, I have come to a foreign land to make a name for myself in the profession of arms before returning home to take over custodianship of my estates. Unfortunately, the authorities in these lands have little understanding of the warrior code, and have chosen to call me a bandit and brigand, and put a price on my head -- a most unfair libel to throw at a gentleman adventurer, you will surely agree."),
  ("npc5_backstory_b", "For as long as any one can remember, our people have feuded with the tribe of Humyan, many of whom have settled in the next valley over. Many men have died in this feud, on both sides, including two of my brothers. The Khan himself has ordered us to cease, to save men for the wars in Calradia. But I know my rights, and my brothers' blood cries out for vengeance. I waylaid and killed a Humyan on a track over the mountains, and I rode out of our village the same night, without even having had the chance to bid farewell to my father. I will bide my time in Calradia, for a year or two, then return home when the Khan's men have forgotten. The Humyan will not forget, of course, but such is the price of honour."),
  ("npc6_backstory_b", "I was a captain of horse in the service of the lord {s19}in {s20}, and my brother served with me. But we were both in love with the same woman, a courtesan -- a temptress, who played upon our jealousies! My brother and I quarreled. I had drunk too much. He slapped me with his glove, and I spit him upon my sword... My own brother! My sword-arm was stained with the blood of my kin!"),
  ("npc7_backstory_b", "It was my bad luck to be born to a weak father who married me off to a drunken layabout who beat me. It was my bad luck, when I ran away from my husband, to be taken by a group of bandits. It was my bad luck that the only one among them who was kind to me, who taught me to hunt and to fight, inspired the jealousy of the others, who knifed him and forced me to run away again."),
  ("npc8_backstory_b", "I am from an old family in the northern lands, the daughter of a thane and also wife to one. I fought by my husband's side, his partner both in war and in peace. But my husband died of the plague, when I was still childless. My husband had decreed that I should inherit his lands, in the absence of an heir. My brother-in-law, cursed be his name, said that it was not our custom that women could inherit a thanedom. That was nonsense, but his gold bought the loyalties of enough of my husband's faithless servants for him to install himself in my hall. So I fled, something I was raised never to do, and something I hope never to do again."),
  ("npc9_backstory_b", "I was my father's first son, and his heir. But my mother died, and my father remarried. His new wife thought that her son should inherit. She could not move against me openly, but the other day I fed a pot of suet that had been left out for me to one of my hounds, and it keeled over. I accused my stepmother, but my father, befuddled by her witchcraft, refused to believe me and ordered me to leave his sight."),
  ("npc10_backstory_b", "A sergeant I was, in the garrison {s19} at {s20}. Twenty years I stood guard for the city, taking many a hard knock in many a tough fight, until they appointed a snot-nosed, downy-lipped princeling, barely out of his mother's cradle, as commander of the garrison. He came upon me standing watch atop the tower, with my crossbow unstrung -- on account of the rain, you see... Can't have the cord loosen... But Little Prince Snot-Nose tells me that an unstrung bow is dereliction of duty. Says he'll have me horsewhipped. And something in me snapped. So I walked off my post."),
  ("npc11_backstory_b", "For 30 years I followed the armies of this land, selling them victuals and drink, watching their games of dice and finding them girls, and nary a denar was left in my purse at the end."),
  ("npc12_backstory_b", "I am by training a natural philosopher, but condemned by the jealousy of the thick-headed doctors of my university to make my living as an itinerant surgeon. I was hired by a merchant of this city to cure his son, who fell into a coma after a fall from his balcony. I successfully trepanned the patient's skull to reduce the cranial swelling, but the family ignored my advice to treat the ensuing fevers with a tincture of willow bark, and the boy died. The father, rather than reward me for my efforts, charged me with sorcery -- me, a philosopher of nature! Such is the ignorance and ingratitude of mankind."),
  ("npc13_backstory_b", "I am a warrior by profession. But perhaps you may also have heard of my prowess as a poet, who can move the iciest of maidens to swoon. Or of my prowess in the art of the bedchamber, in which I must confess a modest degree of skill. I confess a modest affection for Calradia, and for the past several years have visited its towns, castles, and villages, making the most of my talents."),
  ("npc14_backstory_b", "I am the second son of the count of Geroia, of whom you have no doubt heard. Having no inheritance of my own, I came here to seek my fortune in Calradia, training men in the art of battle. Unfortunately, the lord here in {s20} has no taste for the disciplinary methods needed to turn rabble into soldiers. I told him it was wiser to flog them now, then bury them later. But he would not listen, and I was told to take my services elsewhere."),
  #SB : replace cash with silver
  ("npc15_backstory_b", "The castellan {s19}in {s20} wanted a new tower added to the wall. Trouble is, he ran out of silver halfway through the process, before I could complete the supports. I told him that it would collapse, and it did. Unfortunately he was standing on it, at the time. The new castellan didn't feel like honouring his predecessor's debts and implied that I might find myself charged with murder if I push the point."),
  ("npc16_backstory_b", "I grew up in Malayurg castle as a bonded servant, working alongside my mother in the kitchens. I would amuse myself by hunting mice through the pantries and sculleries. I was so good at it that I put the castle cats out of a job, and eventually the lord realized that I might also be employed to track down bigger game, on certain errands of a type perhaps better left unsaid. Needless to say, I found a number of opportunities to avail myself of trinkets that had formerly belonged to my lord's enemies. So I was able to buy myself out of bondage, and find hire as a free agent. My last job was {s19}in {s20}."),

#backstory recruit pitch
  ("npc1_backstory_c", "But if I was with a larger group who could vouch for me, they might let it pass. I'd be very grateful to you."),
  ("npc2_backstory_c", "So here I am, no money and no way home."),
  ("npc3_backstory_c", "I shall marry whom I want, when I want. Moreover, regardless of what my father might think, I am perfectly capable of taking care of myself. I was thinking that I should perhaps join a band of gypsies, or perhaps a troop of mercenaries!"),
  ("npc4_backstory_c", "But I am anxious to avoid any further trouble, so if you knew of any company of fighting men where I might enlist, I would be most grateful."),
  ("npc5_backstory_c", "In the meantime, any opportunities to earn a living with my sword would be most welcome."),
  ("npc6_backstory_c", "Do you believe there is hope for a man like me? Can I find the path of righteousness, or am I doomed to follow the demons that dwell inside of me?"),
  ("npc7_backstory_c", "But I do not count myself unlucky, stranger, no more than any other woman of Calradia, this fetid backwater, this dungheap among the nations, populated by apes and jackals."),
  ("npc8_backstory_c", "When I have enough gold to raise an army I shall go back and take what it is mine."),
  ("npc9_backstory_c", "I hope to offer my sword to some worthy captain, as it is the only honourable profession for a man of my birth apart from owning land, but in the meantime I am condemned to make my bed among thieves, vagabonds, merchants, and the other riff-raff of the road."),
  ("npc10_backstory_c", "Now I'm here getting drunk, and the Devil take tomorrow."),
  ("npc11_backstory_c", "It's no kind of life, victualling the armies. You earn a bit here and a bit there as the soldiers spend their money, and then along comes one defeat and you have to start over, endebting yourself to buy a new wagon and new oxen. So I've decided to get out of the business, but army life is all I know."),
  ("npc12_backstory_c", "The lord of this castle is reluctant to place me under arrest, but I am anxious to move on elsewhere."),
  ("npc13_backstory_c", "Which reminds me -- somewhere out there in the city is a rather irate husband. I don't suppose you might consider helping me leave town?"),
  ("npc14_backstory_c", "So, if you know of any commander who believes that his purpose is to win battles, rather than pamper his soldiers, I would be pleased if you directed me to him."),
  ("npc15_backstory_c", "More fool me for having taken the contract without an advance, I suppose, but the end of it all is that I'm in a difficult spot, with the roads full of bandits and no money to pay for an escort. So I'd be much obliged if a well-armed party heading out in the next few days could take me along."),
  ("npc16_backstory_c", "Unfortunately, my last employer's wife had a lovely amulet, of a kind I simply could not resist. She doesn't know it's missing, yet, but she might soon. So tell me, are you looking for helpers?"),


### use these if there is a short period of time between the last meeting
  ("npc1_backstory_later", "I've been here and about, you know, doing my best to keep out of trouble. I'm desperately in need of work, however."),
  ("npc2_backstory_later", "I sold my boots and have managed to make a few denars peddling goods from town to town, but it's a hard living."),
  ("npc3_backstory_later", "I hired myself on as a cook for some passing caravans, and that at least keeps me fed. But it is rough company on the road, and I grow weary of fighting off guards and others who would try to take liberties. I was thinking that if I could find work as a warrior, men would know to leave me alone."),
  ("npc4_backstory_later", "I went back to my ancestral barony, to inspect my lands. But we had locusts, you see, and bad rains, and other things, so here I am again, looking for work."),
  ("npc5_backstory_later", "I've been wandering through this war-torn land, looking for a leader who is worth following."),
  ("npc6_backstory_later", "I have been wandering Calradia, but have yet to find redemption."),
  ("npc7_backstory_later", "I have been wandering, looking for work as a tracker, but it has not been easy. Calradians are mostly ill-bred, lice-ridden, and ignorant, and it is not easy to work with such people."),
  ("npc8_backstory_later", "I am still seeking a war leader in whose shield wall I would fight. But I need gold, and fast, and the lords of this land as often as not prefer to stay behind the walls of their fortresses, rather march out to where glory and riches can be won."),
  ("npc9_backstory_later", "I've offered my sword to a few lords in these parts. But I find as often as not they'll ask me to run messages, or train peasants, or some other job not fit for a gentleman."),
  ("npc10_backstory_later", "I don't know if I told you or not, but I deserted my unit after I struck a young noble who had ordered me to be horsewhipped without cause. Since then I've been laying low. Thankfully I had the wit to pilfer my captain's purse before heading out, but the money is running low."),
  ("npc11_backstory_later", "I've been around and about. But it's a rare captain who'll take on an old bag of bones like me as a fighter, even if I could whip half the boys in his outfit."),
  ("npc12_backstory_later", "I have been here and about, tending to the sick and taking what reward I can. But the people of these parts are ignorant, and have little respect for my craft. The few denars I make are barely enough for me to replenish my stock of medicine. I should be grateful for the chance to find other work."),
  ("npc13_backstory_later", "I have been wandering through the cities of Calradia, leaving a string of love-sick women and cuckolded husbands in my wake. But I grow weary of such simple challenges, and had been thinking of turning myself to more martial pastimes."),
  ("npc14_backstory_later", "I have gone from court to court, but I have not yet found a lord who is to my liking."),
  ("npc15_backstory_later", "I've been going from castle to castle, looking to see if walls or towers need repair. But either the lord's away, or he's got other things on his mind, or I run into his creditors on the street, begging for change, and I realize that here's one job not to take. So if you hear of anything, let me know."),
  ("npc16_backstory_later", "I do the odd job from time to time. But there's naught like steady employment, and a regular run of corpses to loot."),


  ("npc1_backstory_response_1", "Perhaps. But how do I know that there won't be a 'misunderstanding' about one of my horses?"),
  ("npc2_backstory_response_1", "Well, perhaps I could offer you work. Can you fight?"),
  ("npc3_backstory_response_1", "Well, as it happens I run a company of mercenaries."),
  ("npc4_backstory_response_1", "I run such a company, and might be able to hire an extra hand."),
  ("npc5_backstory_response_1", "That's the spirit! I might be able to offer you something."),
  ("npc6_backstory_response_1", "You could join us. Right wrongs, fight oppressors, redeem yourself, that kind of thing."),
  ("npc7_backstory_response_1", "Hmm... Are you by any chance looking for work?"),
  ("npc8_backstory_response_1", "I can offer you opportunities to make money through good honest fighting and pillaging."),
  ("npc9_backstory_response_1", "Perhaps you would like to join my company for a while."),
  ("npc10_backstory_response_1", "If you're looking for work, I can use experienced fighters."),
  ("npc11_backstory_response_1", "What will you do now?"),
  ("npc12_backstory_response_1", "Well, you could travel with us, but you'd have to be able to fight in our battle line."),
  ("npc13_backstory_response_1", "I might be able to use an extra sword in my company."),
  ("npc14_backstory_response_1", "I might be able to use you in my company."),
  ("npc15_backstory_response_1", "Where do you need to go?"),
  ("npc16_backstory_response_1", "I might be. What can you do?"),

  ("npc1_backstory_response_2", "I'll do no such thing. I have better things to do then to help thieves avoid justice."),
  ("npc2_backstory_response_2", "Hard luck, friend. Good day to you."),
  ("npc3_backstory_response_2", "Go back to your family, lass. Fathers must always be obeyed."),
  ("npc4_backstory_response_2", "No, sorry, I haven't heard of one."),
  ("npc5_backstory_response_2", "Sigh.. So long as you hill clans fight tribe against tribe, you will remain a silly, weak people."),
  ("npc6_backstory_response_2", "Away with you, accursed fraticide!"),
  ("npc7_backstory_response_2", "Actually, I'm rather fond of the place. Good day to you."),
  ("npc8_backstory_response_2", "Your brother-in-law was right -- women should not rule. Go back home and tend your hearth."),
  ("npc9_backstory_response_2", "Some of my best friends are riff-raff. Good day to you, sir."),
  ("npc10_backstory_response_2", "No doubt you'll wake up with your head in a noose, and you'll deserve it. Good day."),
  ("npc11_backstory_response_2", "Very interesting, madame, but I have work to do."),
  ("npc12_backstory_response_2", "Sorry. I can't take on any new hands."),
  ("npc13_backstory_response_2", "No, sorry. Nothing I can do for you."),
  ("npc14_backstory_response_2", "I'll let you know if I hear of anything. Good day."),
  ("npc15_backstory_response_2", "Sorry. I've got all the men that I can manage right now."),
  ("npc16_backstory_response_2", "Sorry, lass. You sound like you might be trouble."),

  ("npc1_signup", "{Sir/Madame} -- I'm offended that you would even think such a thing. I'd be most indebted to you, and you'll see that I show my gratitude."),
  ("npc2_signup", "Well, I will confess that I am not a warrior by trade."),
  ("npc3_signup", "Do you? Well, I am in no position to be picky! I would be pleased to join you."),
  ("npc4_signup", "Good! I look forward to vanquishing your enemies."),
  ("npc5_signup", "Why, that is a most generous offer."),
  ("npc6_signup", "Yes! You must have been sent by divine providence! Lead me -- lead me away from darkness!"),
  ("npc7_signup", "I might be. I could certainly use the money."),
  ("npc8_signup", "Can you? I shall accept your offer."),
  ("npc9_signup", "I would very much like that, {sir/madame}"),
  ("npc10_signup", "Are you, now? Well, that's a sight better than swinging from a gibbet for desertion."),
  ("npc11_signup", "Why, I'll be a soldier myself! Help my old hands to a bit of loot to comfort me in my retirement. Two boys I bore, both soldiers' brats, and they became soldiers themselves. One had his head split by a Khergit war club, the other died of the pox, but at least they didn't die hungry."),
  ("npc12_signup", "As I told you, I am a surgeon, not some silk-robed university physician who has never touched a body. I can get my hands dirty."),
  ("npc13_signup", "Indeed? You would do well to enlist me."),
  ("npc14_signup", "I would be pleased to ride with you, at least for a little while, for pay and a share of any loot."),
  ("npc15_signup", "Geroia, eventually, but I'd welcome the opportunity to get a few denars in my pocket, first, so I don't come home empty handed. So if you promise me food and a share of the loot, I'd be happy to fight with you for a while."),
  ("npc16_signup", "Well, {sir/madame}, let me tell you. I may not know how to read and write, but I know the quickest way to a man's heart is between his fourth and fifth rib, if you understand me. "),

  ("npc1_signup_2", "I've ridden over a fair amount of rough country in my time, more often than not in a hurry. I'm a good tracker and I've got a good eye for terrain. So what do you say?"),
  ("npc2_signup_2", "I'm a fast learner. I can ride, and know a fair bit about trade, prices and such."),
  ("npc3_signup_2", "I think you would find I would be a most valuable addition to your ranks. I am well versed in the classics of literature and can declaim several of the epic poems of my people. I play the lute and am a skilled manager of household servants."),
  ("npc4_signup_2", "Note however that as a gentleman and the holder of a barony, I expect to be in a position of command, and not be treated as one of the common soldiers."),
  ("npc5_signup_2", "I shall not betray you -- so long, of course, as you do your duty to me by feeding me, paying me, and not dragging my miserable hide into a battle where there is no chance of winning. Hand me some salt, if you will -- it is the custom of our people to take salt from our captains, as a token of their concern for our well-being."),
  ("npc6_signup_2", "I am well practiced in the arts of war -- but I beg you, {sir/madame}, I wish to use my skills to defend the innocent, the pure, and the defenseless, not to be a common brigand and wreak more misery than I have already wrought."),
  ("npc7_signup_2", "But let your followers know that I do not suffer louts and brutes. Anyone who misbehaves around me will quickly find an arrow in their gullet."),
  ("npc8_signup_2", "I shall be pleased to fight in your shield wall. But I warn you -- if you ask me to gather the firewood, or cook a meal, you will not like the consequences."),
  ("npc9_signup_2", "I am a gentleman, and prefer to fight with sword and lance. I recognize that you are of lower birth than I, there is no shame for me to serve under an experienced captain -- presuming, of course, that your followers do not become too familiar with me. I assume that will not be a problem?"),
  ("npc10_signup_2", "You won't regret taking me on, {Brother/Sister}. I'm a dead eye with a crossbow -- a beautiful weapon, it can right punch through a nobleman's armour and spill his blue blood upon the ground. And I've trained more raw recruits than you've had hot dinners, begging your pardon. I don't toadie to the high-born."),
  ("npc11_signup_2", "I know how to swing a blade, staunch a wound, and feed an army on the march. It would be a foolish captain who passed up the opportunity to hire an experienced campaigner like me! Say, {laddie/lassie}, don't you command a war party of your own, now?"),
  ("npc12_signup_2", "I have treated every variety of wound that can be inflicted by the hand of man. Before I was a surgeon, I was a student, so you may be sure that I have inflicted wounds as well as healed them."),
  ("npc13_signup_2", "Sword, lance, the bow -- my skill in all such martial pursuits is the stuff of epic verse.  Together we will perform such feats as will be recounted in festivals and campfires, in filthy taverns and in the halls of kings, for many generations to come."),
  ("npc14_signup_2", "I am a skilled swordsman, and I can also instruct your men in fighting. But I warn you that I do not care to fight for a leader who is lax in discipline with {his/her} men, for in the long run they will not respect a soft hand. "),
  ("npc15_signup_2", "Siegework is my speciality, although I reckon can handle myself well enough in an open battle, if need be."),
  ("npc16_signup_2", "I can throw knives, in addition to stabbing with them, and I'm slippery as quicksilver. You'll find me useful in a fight, I'll warrant."),


  ("npc1_signup_response_1", "Good. You can be useful to us."),
  ("npc2_signup_response_1", "That will do."),
  ("npc3_signup_response_1", "Um, that's a start. We can teach you the rest."),
  ("npc4_signup_response_1", "Very well. I'll be glad to have you with us, um, 'Baron.'"),
  ("npc5_signup_response_1", "Certainly. Here, have some salt."),
  ("npc6_signup_response_1", "Happy to be of service! Get your things together, and we shall be on our way."),
  ("npc7_signup_response_1", "I will hire you. Try not to shoot anyone on your first day."),
  ("npc8_signup_response_1", "No fear, ma'am. You're the widow and the daughter of a thane, and you'll be treated as such."),
  ("npc9_signup_response_1", "Well, it shouldn't be. I'll have a talk with them."),
  ("npc10_signup_response_1", "Good man. We'll treat you with the respect you deserve."),
  ("npc11_signup_response_1", "It sounds like you'll be useful. You are hired."),
  ("npc12_signup_response_1", "Then welcome to our company, doctor"),
  ("npc13_signup_response_1", "Good. Make yourself ready, and we'll be on our way. "),
  ("npc14_signup_response_1", "Good. I'll be happy to hire someone like you."),
  ("npc15_signup_response_1", "That works for me. I will be pleased to hire you."),
  ("npc16_signup_response_1", "It sounds like you can do the job. I will hire you."),

#11
  ("npc1_signup_response_2", "I'd prefer not to take the risk. Good day, sir."),
  ("npc2_signup_response_2", "I'm afraid I'm only looking for men with some experience. Good day to you."),
  ("npc3_signup_response_2", "Actually, we were looking for a slightly different skill-set."),
  ("npc4_signup_response_2", "Actually, we are not in the habit of hiring bandits with invented pedigrees. Good day, sir."),
  ("npc5_signup_response_2", "Actually, on second thought, I prefer to keep more civilized company."),
  ("npc6_signup_response_2", "On second thought, maybe a mercenary company is not what you need right now."),
  ("npc7_signup_response_2", "Actually, on second thought, you sound like you might be trouble. Good day to you. "),
  ("npc8_signup_response_2", "Ah. Actually, if you don't do whatever I order you to do, you'd best seek your fortune elsewhere."),
  ("npc9_signup_response_2", "You assume wrong, sir. In my company we respect courage and skill, rather than noble birth."),
  ("npc10_signup_response_2", "On second thought, we value discipline pretty highly in our company. Good day to you."),
  ("npc11_signup_response_2", "Sorry, madame. We've already got as many in our company as we can handle."),
  ("npc12_signup_response_2", "A battle is not the same thing as a tavern brawl. Perhaps you should look elsewhere for work."),
  ("npc13_signup_response_2", "Actually, on second thought, a fighter overeager for glory is dangerous to have in one's company."),
  ("npc14_signup_response_2", "Actually, I have no wish to provoke a mutiny in my ranks. Good day, sir."),
  ("npc15_signup_response_2", "Actually, I need a different kind of expertise. My apologies."),
  ("npc16_signup_response_2", "To be honest, I'd prefer someone who was a little less tempted to larceny."),

  ("npc1_payment", "I will be very useful to you, {sir/madame}, you can bet on that. Just one more thing before we leave, would you mind lending me {reg3} denars? I am ashamed to say it, but I have made myself a bit of debt here, staying in this tavern over the last few weeks and the tavern owners no longer believe that I am loaded with gold as I used to tell them. You know, things could get ugly here if they see me leaving with you before paying them."),
  ("npc2_payment", "{!}."),
  ("npc3_payment", "{!}."),
  ("npc4_payment", "Excellent. Before we depart, would you be so kind to lend me {reg3} denars? I had to pawn a family heirloom at a pawnbroker here in {s20}, and I would like to retrieve it before we leave."),
  ("npc5_payment", "Thank you. Now, to seal off our agreement, I ask for {reg3} denars from you. It's an advice my father gave me. He told me 'Baheshtur, never fight for a barbarian before {he/she} pays you your worth of gold first'."),
  ("npc6_payment", "{!}."),
  ("npc7_payment", "All right then. I will come with you. But I want a payment of {reg3} denars first. You aren't expecting me to work for free, do you?"),
  ("npc8_payment", "Then I will fight your enemies for you. But first I want a bounty of {reg3} denars. If you are a worthy captain who can lead {his/her} company to riches and plunder, you should have no trouble paying. I cannot afford to follow a pauper."),
  ("npc9_payment", "That's very good of you. And before I join, can you lend me {reg3} denars, so that I can buy some proper clothing that befits a gentleman of noble birth such as myself. The coat on me has been worn down badly due to my recent bad fortune, and I cannot let common soldiers mistake me as one of their own."),
  ("npc10_payment", "That's good news. But I'll ask for one last thing, captain. I have a woman here in {s20}, a tavern wench, and she says she has my child in her belly. I want to give her some money before I leave... for the child, you know. Do you think you can spare {reg3} denars?"),
  ("npc11_payment", "Hey thank you captain. But before joining up with you, I would ask for a payment of {reg3} denars. I know that in war parties soldiers can go on for weeks without seeing any wages. I am wise enough not to sign anywhere without having myself covered."),
  ("npc12_payment", "{!}."),
  ("npc13_payment", "Before I sign up, there is the small matter of some expenses I have incurred while staying here -- {reg3} denars. Do you think that you could cover those for me, as a gesture of friendship?"),
  ("npc14_payment", "Ah, one last thing. I would ask for an initial bounty of {reg3} denars before I join your command. It's my principle never to enter someone's service without receiving the payment I deserve."),
  ("npc15_payment", "Good. By the way, as a skilled engineer I would expect a payment for my services. A signing bonus of {reg3} denars would be fair, I think."),
  ("npc16_payment", "Now, that's good news, captain. So, how about paying me a little something to seal off our agreement? A mere {reg3} would be enough. Please don't take this the wrong way, but I've had some bad luck with employers in the past. "),

  ("npc1_payment_response", "Very well, here's {reg3} denars. Now, fall in with the rest."),
  ("npc2_payment_response", "{!}."),
  ("npc3_payment_response", "{!}."),
  ("npc4_payment_response", "Certainly. Here's {reg3} denars."),
  ("npc5_payment_response", "Well... here's {reg3} denars, then. Your first payment."),
  ("npc6_payment_response", "{!}."),
  ("npc7_payment_response", "No, of course not. Here's {reg3} denars."),
  ("npc8_payment_response", "Oh, I am no pauper, madame. Here's {reg3} denars for you."),
  ("npc9_payment_response", "Very well, here's {reg3} denars."),
  ("npc10_payment_response", "Of course. Here, {reg3} denars."),
  ("npc11_payment_response", "Very well, here's {reg3} denars. Make yourself ready. We leave soon."),
  ("npc12_payment_response", "{!}."),
  ("npc13_payment_response", "Of course, here's {reg3} denars. Make ready to leave soon."),
  ("npc14_payment_response", "All right, here's {reg3} denars. You are most welcome in our company."),
  ("npc15_payment_response", "All right, here's {reg3} denars. Glad to have you with us."),
  ("npc16_payment_response", "All right, here's {reg3} denars for you. Make yourself ready."),




  ("npc1_morality_speech", "Oy -- boss. Please don't take this the wrong way, but it's a hard life and it's a bit much that we {s21}. Take a little more care in the future, captain, if you don't mind my saying."),
  ("npc2_morality_speech", "I hope you don't mind my saying so, but it's a bit hard for me to see us {s21}. Maybe I ought to try to be more of a hardened soldier, but if we could try to exercise a little mercy from time to time, I'd sleep better."),
  ("npc3_morality_speech", "Perhaps it is not my place to say so, {sir/madame}, but I confess that I am somewhat shocked that we {s21}. Of course I realize that war is cruel, but there is no need to make it more cruel than necessary."),
  ("npc4_morality_speech", "Your pardon -- just so you know, the men of the House of Rolf do not care to {s21}. I will not be pleased if you continue to take this course."),
  ("npc5_morality_speech", "Pardon me, captain. It is not good to {s21}. Your first duty is to the men who have taken your salt. The least they can expect is food, pay, the opportunity to loot, and that you not waste their lives needlessly."),
  ("npc6_morality_speech", "Excuse me, {sir/madame}. As you know, I joined with you to right wrongs, protect the innocent, and make amends for my sin. I did not expect to {s21}."),
  ("npc7_morality_speech", "Captain -- I do not like to see us {s21}. Such are the actions of a common bandit chief, with no regard for his followers."),
  ("npc8_morality_speech", "I was not pleased that you decided to {s21}. To fall in battle is an honour, but to fight in a warband led by a coward is a disgrace."),
  ("npc9_morality_speech", "{Sir/Madame} -- it is not my way to {s21}. Men of my house will accept death but not dishonour. Please do not make me ashamed to serve under you."),
  ("npc10_morality_speech", "Begging your pardon, captain. I can't say that I'm happy to see us {s21}. Those are just simple people, trying to make a living. If we could try to go easy on the poor wretches, captain, I'd feel much better."),
  ("npc11_morality_speech", "Excuse me, captain. It's not good that we {s21}. I've followed armies and warbands for 30 years, and the least the soldiers expect of a leader is to feed them, pay them, and do {his/her} best to keep their sorry skins intact as best {he/she} can."),
  ("npc12_morality_speech", "Captain -- I do not like to see us {s21}. I am prepared to be a warrior, but not a brigand. Pray let us try to show a little more compassion."),
  ("npc13_morality_speech", "Captain, if we can avoid it, I'd prefer not to {s21}. Calradia is a small place, and one's reputation is precious. I would not care for one of my rivals to include this latest unfortunate incident in a satirical verse."),
  ("npc14_morality_speech", "I do not care to {s21}. No one with a reputation for cowardice will be properly feared by his men."),
  ("npc15_morality_speech", "{Sir/Madame} -- just so you know my opinion, any commander with sense will not let his company {s21}.I hope you don't mind me speaking so bluntly."),
  ("npc16_morality_speech", "Captain. I don't like to {s21}. So many throats left uncut, and so many purses left unexplored..."),


  ("npc1_2ary_morality_speech", "Boss -- just so you know, I've got no problem if we {s21}. Living to fight another day makes good sense to me."),
  ("npc2_2ary_morality_speech", "{Sir/Madame} -- I'm not altogether happy that we {s21}. I'm a merchant, and in our business one is bonded by one's word. I don't want a reputation for dishonesty -- that would spell my end as a trader, {sir/madame}."),
  ("npc3_2ary_morality_speech", "{Sir/Madame} -- I think it was a brave decision you took to {s21}. There is no shame in finding a way to avoid the spilling of blood."),
  ("npc4_2ary_morality_speech", "Your pardon -- whatever anyone else says, I think nothing of it that you {s21}. You should adopt whatever ruse you need to survive in these troubled times."),
  ("npc5_2ary_morality_speech", "{!}[No secondary moral code]"),
  ("npc6_2ary_morality_speech", "{Sir/Madame} -- you may choose to {s21}, but would prefer to have no part in it. Such is not the path to my redemption."),
  ("npc7_2ary_morality_speech", "{!}[No secondary moral code]"),
  ("npc8_2ary_morality_speech", "{!}[No secondary moral code]"),
  ("npc9_2ary_morality_speech", "Captain, I am dismayed that you {s21}. A {gentleman/gentlewoman} such as yourself should exhibit the highest standards of honour at all times."),
  ("npc10_2ary_morality_speech", "{Brother/Sister} -- I can't say I like to see us {s21}. You should treat your men well, and they'll repay with interest."),
  ("npc11_2ary_morality_speech", "{!}[No secondary moral code]"),
  ("npc12_2ary_morality_speech", "{!}[No secondary moral code]"),
  ("npc13_2ary_morality_speech", "{!}[No secondary moral code]"),
  ("npc14_2ary_morality_speech", "Captain -- you should not let it bother you that you {s21}. Armies are made to do their leaders' bidding, and hardships are part of a soldier's life."),
  ("npc15_2ary_morality_speech", "You know, friend {playername}, it's none too reassuring to see how you just {s21}. If you can break your word to them, you can break your word to me, is how I figure it."),
  ("npc16_2ary_morality_speech", "Captain -- just so you know, it's no problem by me that we {s21}. We do what we need to do to live, and they'd do the same to us if they were in our shoes."),

  ("npc1_personalityclash_speech", "Captain -- no offense, but I'm a bit tired of {s11}, who puts on airs like she's something better than your humble servant Borcha."),
  ("npc2_personalityclash_speech", "{Sir/Madame} -- as you recall I was a merchant before I signed on with you. I respect men who make their living peacefully, risking all to bring goods for far away lands."),
  ("npc3_personalityclash_speech", "Captain -- in my opinion, {s11} is a hard and cruel man. He speaks of nothing but the need to flog, beat, and hang his fellow soldiers."),
  ("npc4_personalityclash_speech", "{Sir/Madame}. The House of Rolf is one of the most ancient and respected families in this part of the world, with a provenance dating back to the Old Calradic Empire. Yet {s11} openly shows me disrespect, and casts doubt on the provenance of my house."),
  ("npc5_personalityclash_speech", "A moment of your time, captain. {s11} seems to think me a common bandit, just because I have rewarded myself in the past to the legitimate spoils of war from caravans passing through my family's lands."),
  ("npc6_personalityclash_speech", "Your pardon, {sir/madame}, but I cannot keep my tongue stilled any longer. That harlot, {s11} -- every time she sees me she points the five fingers of her hand at me -- a peasant's sign to ward off evil."),
  ("npc7_personalityclash_speech", "Captain, I have done my best to put up with your followers' rude talk and filthy habits. But that one who calls himself {s11} is beyond tolerance."),
  ("npc8_personalityclash_speech", "Just so you know, I cannot abide that insolent mountebank {s11}. Some minutes ago, I was remarking to our companions how the peasants of this region were more than usually slack-jawed and beetle-browed, and speculated that perhaps they had bred with apes."),
  ("npc9_personalityclash_speech", "Sir -- {s11} is a base braggart, a man with no respect for the honour of women. I am tired of hearing how he conquered this or that damsel."),
  ("npc10_personalityclash_speech", "Excuse me, captain. I hate to trouble you with such things, but I just wanted to let you know that I can't abide that fellow Rolf, the one who calls himself a baron."),
  ("npc11_personalityclash_speech", "Begging your pardon, captain, but I can't keep silent. That man, {s11} -- he killed his own brother."),
  ("npc12_personalityclash_speech", "My lord. The barbarian woman, {s11}, complained of headaches -- a possible symptom of excess of sanguinity. I thought to apply my leeches."),
  ("npc13_personalityclash_speech", "Captain, I weary of {s11}, who talks of nothing but chivalry and feats of arms."),
  ("npc14_personalityclash_speech", "Excuse me, captain. A few minutes ago, I had expressed the opinion that liberal use of the lash and occasional use of the gallows is essential to keep soldiers in line. Men without a healthy fear of their commanders are more likely to run from battle."),
  ("npc15_personalityclash_speech", "Excuse me. I hope you don't mind me telling you that in my opinion, that girl {s11} is a danger to the party. She's a feral brat, disrespectful of authority and the basic principles of the military art."),
  ("npc16_personalityclash_speech", "Oy, captain. Just so you know -- there's something funny about {s11}. He makes strange scrawlings in the dirt, and mutters to himself."),

  ("npc1_personalityclash_speech_b", "She's a common bandit, just like myself, and she has no right to tell me to keep my distance from her, as she did just now."),
  ("npc2_personalityclash_speech_b", "I don't much care to hear {s11} gloat about the caravans he has looted, or he plans to loot, like he has no respect for good honest trade."),
  ("npc3_personalityclash_speech_b", "I know that an army is not a nursery, and that strong discipline is important, but I do believe that man enjoys cruelty for cruelty's sake. I hope you do not mind me saying so."),
  ("npc4_personalityclash_speech_b", "{Sir/Madame}, these are indeed sorry days if common folk are allowed to mock their betters. That is all."),
  ("npc5_personalityclash_speech_b", "I told him that if the warrior's way bothers him so much, that he become a priest or a beggar and so not have to worry about such things. I hope you do not mind that I said such things."),
  ("npc6_personalityclash_speech_b", "I know the crime I committed was an abomination, but I am seeking repentance, and I deserve better than to be the object of some witch's superstition. I just thought you should know."),
  ("npc7_personalityclash_speech_b", "I do not care for how he stares at me around the campfire after a meal, as he picks his teeth. I believe I recognize him from my days as a bandit. He is base and ignorant. I do not care to travel with such people."),
  ("npc8_personalityclash_speech_b", "{s11}, that font of impudence, overheard me, and called me ignorant, and a savage, and other words I do not care to repeat. It was only out of respect for you that I refrained from cutting his throat then and there. I thought it only fit that I should warn you."),
  ("npc9_personalityclash_speech_b", "If he persists, I shall tell him that he is a base varlot, and if it comes to blows I will not apologize. That is all, {sir/madame}."),
  ("npc10_personalityclash_speech_b", "He's just a simple brigand, as far as I can tell. House of Rolf, my arse. Genuine blue-bloods are bad enough, but those who pretend to be blue-bloods are bloody intolerable. Anyway, I might have said something a bit sharp to him a minute ago. He seemed to take offense, anyway. I just thought you should know."),
  ("npc11_personalityclash_speech_b", "He's a kinslayer, cursed by heaven, and he'll bring misfortune and sorrow upon us, that's for certain. I don't like being around him and I don't think he should be with us. That's all. Sorry for troubling you."),
  ("npc12_personalityclash_speech_b", "But when I tried to afix them, she recoiled and struck me, and accused me of witchcraft. Captain, I am deeply tired of attending to the complaints of such an ungrateful and ignorant lot."),
  ("npc13_personalityclash_speech_b", "Valorous deeds are all very well, but they are not the only goals worth pursuing in life. Personally, I never trust any man who has not at least once woken up drunk in a ditch, or been beaten by the slipper of his lover."),
  ("npc14_personalityclash_speech_b", "That chit {s11} saw fit to admonish me for this. I will not have my methods questioned in front of the men, and I will not serve any commander who tolerates such insubordination in his company. Thank you for allowing me to speak my peace."),
  ("npc15_personalityclash_speech_b", "What's more, I suspect she's a thief. I found her going through my baggage and pawing some of my schematics, and she pulled a knife on me when I thought fit to object. A wise captain would not allow her in his company."),
  ("npc16_personalityclash_speech_b", "Fearing witchcraft, I asked him about it, and he told me that a chit of a girl like myself should mind her own business. So I had a look in his baggage, and found strange plans and diagrams. I think he's a sorceror, {sir/madame}, and if I catch him trying to hex me he'll have a knife in his throat."),


### set off by behavior after victorious battle
  ("npc1_personalityclash2_speech", "Oy -- boss, I don't fancy myself a sensitive soul, but I don't particularly like how {s11} went about cutting the throats of the enemy wounded, back there."),
  ("npc2_personalityclash2_speech", "{Sir/Madame}. If you don't mind, I'd prefer not to be deployed anywhere near {s11}, after what he said to me during that last battle."),
  ("npc3_personalityclash2_speech", "{Sir/Madame}. Since I have joined your company, I have tried hard to learn how to live like a soldier, and how to honour the warrior's code. If I occasionally make mistakes, I would hope to be forgiven."),
  ("npc4_personalityclash2_speech", "{Sir/Madame}. I happened to exchange a few words with {s11} as we were dividing up the spoils of battle. Please inform her that when she speaks to me, she should call me 'Baron' or perhaps 'Baron Rolf,' or 'Your Grace,' but certainly not just 'Rolf.'"),
  ("npc5_personalityclash2_speech", "Captain. {s11} needs to have her tongue cut out."),
  ("npc6_personalityclash2_speech", "My lord. Did you see {s11} during that last battle? He taunts the fallen foe as they lay stricken and helpless on the battlefield, mocking their parentage, their foolishness for having fought us."),
  ("npc7_personalityclash2_speech", "Captain -- I have been searching my mind trying to remember where I have seen {s11}, the one who calls himself a baron. As I watched him in action during that last battle, I suddenly remembered. He is a good fighter, but also a vicious one."),
  ("npc8_personalityclash2_speech", "Captain. {s11} is a most insolent girl. I have tried to be polite, even friendly, only to have her rebuff me."),
  ("npc9_personalityclash2_speech", "{Sir/My lady}, I hope you do not mind me telling you this, but in my opinion {s11}, the merchant, does not know his place. During that last battle, he cut in front of me to engage a foe whom I had marked for my own."),
  ("npc10_personalityclash2_speech", "{Brother/Sister} -- a question for you. Are you in charge of this company, or is it {s11}?"),
  ("npc11_personalityclash2_speech", "Captain. I don't much care for that {s11}. After that last battle, he went around muttering some heathen incantation, as he went through the slain looking for loot."),
  ("npc12_personalityclash2_speech", "Captain. I can no longer abide the rank ignorance of {s11}. As I was treating the wounded during our last battle, he saw fit to disparage my use of laudanum in relieving the pain while I conducted surgery, and of treating wounds with a poultice of honey."),
  ("npc13_personalityclash2_speech", "Hello, captain! {s11} is a temperamental one, isn't he? During that last battle, I was merely having a friendly chat with our foes about their mothers as we exchanged swordblows, and it caused him to throw a fit!"),
  ("npc14_personalityclash2_speech", "Sir. {s11} is incorrigibly indisciplined. During that skirmish, I called out to him that he should hold ranks with the rest of our battle array. He called back to me that I should 'get stuffed.'"),
  ("npc15_personalityclash2_speech", "Captain -- I must tell you that I question {s11}'s medical credentials. As he was tending to our wounded after that last battle, I saw fit to remind him that the peerless Galerian often advocated administering a distillation of beetroot, to restore the humor imbalance brought by loss of sanguinity."),
  ("npc16_personalityclash2_speech", "Beg your pardon, {sir/ma'am}. {s11} might have been a very good thief, but he's not got the stomach to be a warrior, if you ask me."),

  ("npc1_personalityclash2_speech_b", "The way she whistles cheerfully as she does it -- it puts a chill down my spine, it does."),#borcha - klethi
  ("npc2_personalityclash2_speech_b", "The enemy was bearing down on us, and he says, 'Step aside, merchant, this is knight's work.' Next time I will step aside, and let him take a spear in the gut."), #marnid - alayen
  ("npc3_personalityclash2_speech_b", "After our last victory I was picking through the slain, and availed myself of one of our foe's purses. No sooner had I done so then {s11} came up behind me and struck it from my hands, saying that it was she who had made the kill, and thus she deserved the spoils. My lord, I could not tell in the heat of battle who had struck whom. If {s11} had simply told me that she deserved the purse, I would gladly have given it to her."),#Ymira - matheld
  ("npc4_personalityclash2_speech_b", "I am of noble blood, and she is of the basest birth. She must remember her place."),#Rolf - deshavi
  ("npc5_personalityclash2_speech_b", "When the loot was piled up after the last battle, I found among the enemy's baggage a very decent cooking pot. Often I had wished to find such a pot, so I could boil some of the stews that my people use to warm their bellies during the winter months. But {s11} grabs the pot, and tells me that I will not be allowed to 'taint' it with heathen food, and that it should properly belong to her. I yielded the pot to her, but I will not tolerate such disrespect in the future."), #beheshtur- katrin
  ("npc6_personalityclash2_speech_b", "My lord -- such hubris will not be overlooked by Heaven, and I fear we shall all of us pay the price."), #firentis - nizar
  ("npc7_personalityclash2_speech_b", "Back when I lived in the ravines, we would sometimes fight with a rival band called the Brethen of the Woods. Captain -- I would not trust any man who hides his origins, and particularly would not trust a common bandit who calls himself a lord."),#deshavi - rolf
  ("npc8_personalityclash2_speech_b",  "As we were cleaning our weapons after that last battle, I remarked that I thought her a handsome girl, and after I regained my lands I would happily find her a match with one of my warriors. I thought it was a very generous offer, as a woman disinherited by her father is hardly going to find herself awash in prospects. But rather than thank me, she simply turned her back without a word. It was only out of respect for your leadership that I did not immediately try to teach her some manners."),  #matheld - ymira
  ("npc9_personalityclash2_speech_b", "I appreciate that he is willing to risk his life in battle, but that alone does not make a gentleman. He is not of noble birth, and his family's wealth comes from commerce and usury. He may fight with us as an auxiliary, but should not attempt to steal glory from his betters."),# alayen - marnid
  ("npc10_personalityclash2_speech_b", "In that last battle he was shouting at me: 'Go forward, go back, hold the line.' When I told him to mind his own trimming he said he'd have me flogged.  Captain, that man is looking for a crossbow bolt in his chest, begging your pardon."),
  ("npc11_personalityclash2_speech_b", "He said it was a prayer of thanksgiving for victory, but it didn't sound like that to me. Captain, I don't want him raising up the ghosts of the dead to make trouble for us on our travels. I think you had best be rid of him"),
  ("npc12_personalityclash2_speech_b", "Captain, if that man knew the slightest thing about medical matters, he would know that one should never undermine a patient's confidence in his doctor, particularly not during a complicated operation. If you would be kind enough to dismiss him from this company, you would be doing all of us a great service."), # jeremenus - artimenner
  ("npc13_personalityclash2_speech_b", "When all the dust settled, {s11} turned on me and told me not to 'tempt the wrath of the Heavens' with my 'hubris.' I responded that at least I hadn't killed my own brother, which I think bothers the Heavens a lot more than battlefield small talk. {s11} turns red like a baboon's arse and would have struck me had I not artfully dodged out of his away. Tell him to lighten up, will you?"), #nizar - firentis
  ("npc14_personalityclash2_speech_b", "{Sir/Madame}, such defiance of proper authority is a corrosive influence on our company, and I shall have him flogged if he does so again."), #lazalit - bunduk
  ("npc15_personalityclash2_speech_b", "{s11} responded that Galenian was an 'antiquated know-nothing.' Captain, no true doctor would have such disrespect for the great masters of the past. I do not believe you should employ such an obvious impostor."), #artimenner - jeremus
  ("npc16_personalityclash2_speech_b", "After our last scrap, I was slicing open the guts of some our foes to check for hidden gold, as a girl who counts her pennies ought. He gagged and muttered that I was an 'animal.' I'll inspect his innards for contraband if he doesn't keep a civil tongue in his head."), #klethi - borcha


  ("npc1_personalitymatch_speech", "Boss. {s11} back there didn't do badly in that last fight at all. He's a good egg, too."),
  ("npc2_personalitymatch_speech", "{Sir/Madame}. I just wanted to tell you that {s11} may be a rough sort, and I'll venture a thoroughgoing rogue as well, but I'm proud to call him my companion."),
  ("npc3_personalitymatch_speech", "Hello, {sir/madame}! I had just wanted to tell you that {s11} is a most gallant knight. Did you see him in our last battle?"),
  ("npc4_personalitymatch_speech", "Excuse me, {sir/madame}. I just wanted to say a word in praise of {s11}. He did well in that last battle."),
  ("npc5_personalitymatch_speech", "That was a fine battle, {playername} Bahadur! {s11} is a good man to have by our side in a fight."),
  ("npc6_personalitymatch_speech", "Captain. Sometimes I am troubled by all this bloodshed, although I know that proud warlords must be humbled, and cruel bandits tamed, if we are to restore peace to Calradia."),
  ("npc7_personalitymatch_speech", "Captain. I was just talking to {s11}. She may be a bit savage, but I believe that she is a faithful friend."),
  ("npc8_personalitymatch_speech", "A fine battle that was, captain. And I have to say, I admire the taunts that {s11} hurled at our enemy."),
  ("npc9_personalitymatch_speech", "Captain. {s11} acquitted herself well in that fight back there. A fine, modest maiden she is, if I dare say so myself."),
  ("npc10_personalitymatch_speech", "Ahoy, Brother! I wish you joy of your victory! Say, old Mother {s11}'s not bad in a scrap, is she, for a woman of her years? Although I'm getting to be a bit of an old dog myself, now."),
  ("npc11_personalitymatch_speech", "Ach, captain! A fight like that one sets my old joints a-creaking. Still, we licked them pretty good, didn't we?"),
  ("npc12_personalitymatch_speech", "A bloody business, captain, a bloody business -- although a necessary one, of course. {s11}, I believe, shares my ambivalence about this constant fighting."),
  ("npc13_personalitymatch_speech", "You have earned your name today, oh valorous one! And {s11}, too! I like that one. She sings the songs of her people as she goes into battle, which appeals to an artistic soul like my own."),
  ("npc14_personalitymatch_speech", "Captain. It is a pleasure going into battle with men like {s11} by my side."),
  ("npc15_personalitymatch_speech", "Captain. I was just having a word with {s11} after our last battle, and it strikes me that the man has got a good head on his shoulders."),
  ("npc16_personalitymatch_speech", "Oy -- captain. I was just having a chat with {s11}, as we picked through the bodies after our last little scrap."),

  ("npc1_personalitymatch_speech_b", "Without good honest souls like him to bring silver into Calradia, scoundrels like me would have a hard time in life, I'll warrant. I'm glad to have him with us."),
  ("npc2_personalitymatch_speech_b", "Based on how he did in that last fight, I'd say that I'd trust my back to him any day, although I'd still keep a hand on my purse."),
  ("npc3_personalitymatch_speech_b", "I also confess that I find him a truly delightful companion, a man of both wit and manners. Perhaps, perhaps... Ah, but I say too much. Good day, {sir/madame}."),
  ("npc4_personalitymatch_speech_b", "You chose well to enlist him in our company. He knows a thing or two about a fight, and also knows the importance of respecting his comrades-in-arms, unlike some others I might mention."),
  ("npc5_personalitymatch_speech_b", "As for his other attributes, I doubt that he is any more a Baron than I am, but I have to admire the brazen way he makes that claim."),
  ("npc6_personalitymatch_speech_b", "I must say that {s11} is a source of great comfort to me. I have told him of my sin, and he said to me that Heaven will forgive my transgression, if I truly repent and truly desire such forgiveness. He is wise, and I am glad that he is with us."),
  ("npc7_personalitymatch_speech_b", "At some point in the future, if you have no need of our services, she has promised to go back to the ravines with me and find the bandits who murdered my lover, and help me take my revenge. It was a kind offer. I am glad that she is with us."),
  ("npc8_personalitymatch_speech_b", "He managed to include their geneology, their appearance, and their eating habits in a well-framed Old Calradic quatrain. I personally prefer the saga, but we Nords respect poetic craftwork when we hear it."),
  ("npc9_personalitymatch_speech_b", "Were she of noble blood, I might ask for her hand. It is a pity that she is a merchant's daughter. But speaking with her is a pleasant way to pass time on the march."),
  ("npc10_personalitymatch_speech_b", "Heh. It just goes to show that youth ain't everything, that experience also wins battles. I reckon she and I could teach the young puppies of the world a thing or two, couldn't we?"),
  ("npc11_personalitymatch_speech_b", "Old {s11} in particular showed them a thing or two, I thought. Not bad for the pair of us, I thought, given that between us we've probably seen close to a hundred winters."),
  ("npc12_personalitymatch_speech_b", "It saddens him deeply to take the lives of his fellow men, however just the cause. He and I have talked together of a brighter future, of the need to unite these petty warring kingdoms of Calradia, so that we may bring this time of troubles to an end."),
  ("npc13_personalitymatch_speech_b", "Also, although I normally prefer the coy to the Amazonesque, I confess that I have also noticed the femininity she tries to hide beneath her martial demeanour. True, she is a bit aloof on the march and in camp, but perhaps my fair words can melt the Nordic ice around her heart."),
  ("npc14_personalitymatch_speech_b", "He is a professional soldier, and though he may not be as fast on his feet as some others, he knows the wisdom of holding together in a disciplined battle-line. You showed good sense in bringing him into this company."),
  ("npc15_personalitymatch_speech_b", "War, like any other affair, requires careful planning and preparation, and a firm grasp of strategic principals. All other things being equal, the best trained army will win the battle, an observation that I think our last fight bears out. The men may curse him now, but they'll learn to thank him, I'll warrant."),
  ("npc16_personalitymatch_speech_b", "Have you heard her story? Can you believe the wrongs done to her? I tell you, it makes my blood boil. I want to cut off all the little bits of those bastards who mistreated her -- and I'll do it, too, if we ever run into them in our travels."),


  ("npc1_retirement_speech", "I'm a bit tired of marching up and down the land, shedding my blood for someone else's cause. The loot is good, but I think I've got enough of that, now. I'm going to head back to my village, take a wife, settle down, maybe raise horses if I can afford it."),
  ("npc2_retirement_speech", "I'm getting a bit tired of the warrior's life. I'm going to invest my share of our loot into a cargo of goods -- furs, linens, velvets, probably -- and take them back over the mountains. I would like to thank you again for taking me on, and wish you the best of luck."),
  ("npc3_retirement_speech", "I am afraid I have something to tell you. I have decided that the warrior's life is not for me. I think it is probably too late for me to find a good marriage -- no one of my people would take a wife who had served with a company of soldiers -- but I may have enough money to start myself up as a merchant. I hope you will not be angry, {sir/madame}."),
  ("npc4_retirement_speech", "I have fought with you honourably, as befits a son of the House of Rolf, but I am not altogether satisfied with your leadership. I will go home to my ancestral estates, which are much in need of my services."),
  ("npc5_retirement_speech", "Bahadur -- since I have taken your salt, I have fought for you fiercely, and loyally. But you have not always repayed my service with the kind of leadership that I deserve. So I am going home, in the hope that the Khan's men have forgotten me, to see my father and brothers again."),
  ("npc6_retirement_speech", "I joined this company in the hope that you would lead me out of darkness, and indeed I have found a measure of peace here. But I have some qualms about your leadership, and have begun to suspect that the path to redemption can be found elsewhere."),
  ("npc7_retirement_speech", "I am tired of this squalid life of endless warfare, seeing men debased by fear, greed, lust, and a hundred other sins. I have money in my purse. I am going overseas to look for a better land than Calradia. I assume that you will fare well without me."),
  ("npc8_retirement_speech", "I have fought in your shield wall, and done well by it. But your leadership is not always to my liking, and anyways I have another task. I will take what plunder I have won and raise a warband of my own and sail to Nordland to take back my husband's hall from my treacherous brother-in-law. I wish you well."),
  ("npc9_retirement_speech", "We have fought well together, and earned ourselves much glory. But I have some reservations about your leadership, and at any rate have my patrimony to reclaim. I will be leaving you. Perhaps we will meet again."),
  ("npc10_retirement_speech", "I've had enough of tromping up and down the length and breadth of Calradia. I've got enough to buy a small bit of land somewhere, so I think I'll give that a try. So long, and best of luck to you."),
  ("npc11_retirement_speech", "You did an old woman a great service by taking her into your company. But I'm afraid I'm finding this life no more to my liking than driving a wagon. Too much cold, too much hunger, and at the end all I see in front of me is a hole in the ground. So I'll be off, although I don't know where."),
  ("npc12_retirement_speech", "I've done all right in your company. I filled my belly, put some gold in my purse, and broadened my knowledge of wounds and injury -- I can't complain about that! But I think right now that service in this company is holding me back. I have a duty to share my findings with other surgeons, and for that I need to hire scribes, who are rare in Calradia. I shall be going home"),
  ("npc13_retirement_speech", "As the luster of your name grows ever brighter, I fear that my own reputation will seem pale in comparison, as the moon is outshined by the sun. I have decided to strike out on my own. The very best of luck to you!"),
  ("npc14_retirement_speech", "I would like to inform you that I wish to sever our relationship. I intend to seek alternative employment."),
  ("npc15_retirement_speech", "I appreciate that you took me on, but I'm not altogether happy about how things have worked out. I'm going to head off elsewhere -- maybe go home, maybe find another job, I haven't quite decided yet."),
  ("npc16_retirement_speech", "I've had good times in this company, and I've found myself a pretty trinket or two on the battlefield, but right now it isn't working out. I'm leaving you to go offer my talents to someone else."),

  ("npc1_rehire_speech", "Boss -- it's good to see you again. I know we had our differences in the past, but to tell you the truth, those were some of the best days I've known. And, to tell you the truth, I've had a bit of difficulty finding work. Listen, if you'd be willing to have me back, I'd be willing to sign up with your company again."),
  ("npc2_rehire_speech", "{Sir/Madame}! It's good to see you again. But I'll confess -- I've been looking for you. I bought a load of goods like I told you I would, loaded them up, and took them back across the steppe -- but wouldn't you know it, I was hit again by Khergits, and lost it all. I guess I'm just destined to fight for my fortune. Also, people tell me that you've done very well for yourself. So tell me, {sir/madame}, would you have me back?"),
  ("npc3_rehire_speech", "Well, hello {sir/madame}! It is very good to see you again. I have not fared so well since we parted, I am afraid. My mother's family. whom I hoped would give me a start in trading, have not been as welcoming as I have hoped. I receive nothing but lectures from my aunts, on how I have ruined my prospects for marriage by taking service in a mercenary company. Perhaps I am better suited to war than to commerce, to share a meal over a campfire with rough fellows than to drink wine with the burghers of Veluca. {Sir/Madame}, I must ask you -- will you take me back?"),
  ("npc4_rehire_speech", "Why hello, captain. It's been a while. You've done well for yourself, I hear. For my part, I've been having some difficulties coaxing a living from my estates -- locusts, bad rains, unruly serfs, that sort of thing. I thought I might take up the sword once more. I know there's been some bad blood between us, but I'd be honoured to fight in your ranks once again."),
  ("npc5_rehire_speech", "{playername} Bahadur! Your fame grows ever greater -- even as far as my homeland, beyond the mountains. I'd returned there, hoping that the Khan's men had forgotten. Well, they had not -- even before I set foot in my valley, I had word from my family that both the Khan and the Humyan were looking for me. So I came back again, hoping you might forget any harsh words I had spoken, to see if I could fight with you once again."),
  ("npc6_rehire_speech", "It is good to see you, {sir/madame}. Everywhere I go, men are in awe of your deeds. I have not had it so well since I left. Wherever I go, I feel my demons returning. My soul is in turmoil. For reasons that I cannot fully explain, I had found peace in your company, even if I had questions about your leadership. Will you allow me to serve with you once again?"),
  ("npc7_rehire_speech", "Captain! It is good to see you. Forgive what I may have said when we parted. I took a ship out of Wercheg, bound for the east, but it was taken by pirates and after my ransom I was set ashore back here. There may be better places in the world than Calradia, but I have yet to see them. So I think, if it is my lot to live here, then your company is as good a livelihood as any. Will you have me back?"),
  ("npc8_rehire_speech", "Greetings to you, {playername}. I was wondering if the harsh words spoken between us in the past could be forgotten. I have been hunting among the Nords here, to see if I could find enough men to take back my husband's hall. But I could not find enough men to crew a longship, and those whom I gathered quickly got bored and wandered off -- not, I will add, before they drank away such gold as I had accumulated. So I thought back to the battles we fought together. Those were good days, and profitable ones too."),
  ("npc9_rehire_speech", "My dear, dear {man/lady}! So good it is to see you! I have sought service with the lords of this land, but have been most grieviously disappointed. Half of them ask me to collect debts from fellow lords, as though I were a banker's errand boy, or chase down his serfs, as though I were a farm overseer. One even asked me to murder one of his creditors! I have looked for you, to see if you would wish me to join you again."), #Alayen
  ("npc10_rehire_speech", "Captain! It's good to see you. You see, it turns out I'm not much of a farmer. Too soft on the hired hands, I figure. I let them rob me blind. I guess fighting is what I know best. So tell me, captain, are you still looking for good men?"),
  ("npc11_rehire_speech", "Captain! So good to see you! People say that you've been making gold hand over foot. I'm a fidgety old bag of bones, I'll admit. I left you because I wasn't satisfied with the warrior's life, but I spend a bit of time in town and I realize that there are worse things in life than a full belly, honest companions, and the joy of seeing the enemy run before you. So, would you be hiring again"),
  ("npc12_rehire_speech", "Captain! It's a fine thing to see an honest face like yours. This world is full of lies. I went home to publish my findings, hired some scribes and made a handful of codices, and waited for the commissions. But it turns out that the universities don't care about real medical knowledge rather than warmed-over Galerian. And publishers -- let me tell you, you never saw anyone so unscrupulous. They rent the books out chapter to by chapter to students to copy, but half of them aren't returned, and those that are have pages soaked in wine, and there's no longer a complete copy of my work anywhere. I'll keep trying, but first I need a bit of money in my pocket, first. Are you looking for a surgeon?"),
  ("npc13_rehire_speech", "Well hello there, oh valorous one. I had been hoping to see you again. Everywhere I go, I hear tales and songs of your deeds. I will admit that I felt a twinge of regret that we had parted ways, and, I'll confess, a twinge of jealousy as well at your reputation. I thought that once again I might fight by your side, and thus bask in the reflection of your glory. Perhaps we might ride together again, for a little while?"),
  ("npc14_rehire_speech", "Captain. It is good to see you. When last we parted, I was ready to swear that I would not serve you again, but perhaps I judged you too harshly. All over Calradia, men sing your praises. I have tried serving in other lords' armies, and believe me, what I have seen of them restores my opinion of your leadership. If you would have me in your company, I would fight for you again."),
  ("npc15_rehire_speech", "Why hello, {playername}. I can't say I'm entirely displeased to see you. You see, I took on another contract before I left, and sure enough, when it came time to collect the pay, the lord had nothing but talk and excuses and petty little complaints about my handiwork. I can't say I was always happy in your company, but at least I put gold directly into my purse after every battle. You still offering work?"),
  ("npc16_rehire_speech", "Captain! They say that you've done well for yourself since we last met. I'll come out and admit that I cursed your name when we parted ways, but thinking back on it you weren't all that bad. All these lords, they're glad enough to send me on little side errands, but they don't much care to have me in their main battle-line. Apparently I spook the men. I've heard it muttered that I'm a witch, or that I eat men's hearts after killing them, or other rot. Not that I mind stabbing a man while he's asleep, but it's a lot more gratifying when he's awake and kicking. So I thought I'd try to find you again, see if you'll take me on."),

#local color strings
  ("npc1_home_intro", "Boss -- did you know that I was born around here, in the high steppe? This is where I got my eye for horseflesh, because this is good land for horses, although a hard land for men. I suppose that's why the Khergits like it."),
  ("npc2_home_intro", "We're approaching Sargoth. That's where I was headed when the Khergits got me."),
  ("npc3_home_intro", "Can you smell that? Lemon trees, apples and crocus flowers, it's the scent of Veluca. I spent many a happy summer here when I was a girl, playing in the gardens of my mother's family while my father was away trading."),
  ("npc4_home_intro", "The Woods of Ehlerdah. Bah. This place is thick with bandits and outlaws."),
  ("npc5_home_intro", "Bahadur, we are nearing Halmar, largest town in the lower steppe. My mother's sister went here to marry a townsman and I thought to seek service with the lord here. That is when I ran into you."),
  ("npc6_home_intro", "I can see by the vines and terraces on the hillside that I am near home. I have no wish to see my family, so I will linger outside the walls if you go into town. I am sure that you will understand."),
  ("npc7_home_intro", "Do you smell that? Salt fish, rotting flax and river mud. The smells of my childhood. I want to retch."),
  ("npc8_home_intro", "Hmf. Do you hear that? It must be the crash of waves on the headland. We must be near Gundig's Point."),
  ("npc9_home_intro", "Behold the Rock of Rivacheg! The strongest fortress in Calradia. My father was one of those who held the line here against the Nords, when they first tried to push inland from the coast."),
  ("npc10_home_intro", "D'you smell that fresh air, Brother? This was my home, before I went abroad in search of coin. It's good to be up in the hills again. It's the smell of freedom. This is the cradle of Rhodok liberty, here under Grunwalder Castle"),
  ("npc11_home_intro", "I see the mountains. We must be getting near home."),
  ("npc12_home_intro", "We're passing by the site of one of my greatest medical triumphs, if that interests you."),
  ("npc13_home_intro", "Ah, Castle Ergellon! Such a lovely spot, at the foot of the Rhodok highlands. Such happy days I spent here, the summer before last."),
  ("npc14_home_intro", "Do you see that fortress up there, on the spur over the valley? Ismirala? I spent a winter there some years back, trying to train the lord's men."),
  ("npc15_home_intro", "You see that castle up on the hill? Culmarr Castle, it's called. I did some work there, not long ago. It's not as showy as some of the other castles in this land, but it's the finest stonework you ever saw."),
  ("npc16_home_intro", "Aye, captain, do you see those? Those are hare tracks in the snow. We must be getting near to my birthplace."),


  ("npc1_home_description", "Well, Khergits always lived here, even back in the old days, as the Emperor gave them gold and lands to keep out the other tribes. I'm told my grandfather was a Khergit chieftain, although my mother didn't know him, any more than I knew my father. When my mother was a lass, the Khergit started coming over the mountains in larger numbers, and now there's a Khergit Khan in Tulga."),
  ("npc2_home_description", "People say that the Nords are a bunch of bloodthirsty barbarians, but they have a good head for trade, if you ask me. They make the people up and down the coast grow flax, which they weave here into linen. It can't compete with Jelkala silks and velvets as a luxury fabric, but it makes good summertime wear and you can use it for the sails of ships. More importantly, linen was one of the few goods that someone else in Calradia wasn't already making."),
  ("npc3_home_description", "Veluca has wet winters and hot summers, but the people here build great cisterns to water their crops. They grow grapes -- Velucan wine is famous, {sir/madame} -- and those who can afford it make walled gardens, where fruit trees grow in abundance, and we sit at night listening to music, or playing chess, or merely sniff the night air."),
  ("npc4_home_description", "Well, you see, the King of Swadia declared this to be his personal hunting preserve, and said he'd kill any man who as much as strung his bow here. So what happens? Some family goes hungry, and succumbs to the temptation to poach, and the king's sheriff comes along and strings him up and takes his land. His sons, rather than starve, go bandit. And so naturally anyone in the whole valley who feels the need to run away from a debt or a nagging wife or a vengeful noble comes up here to join them, living on wild pigs and berries and the purses of unwary travellers."),
  ("npc5_home_description", "Khergits had always come here, to trade and raid, and in the last days of the Empire we began to settle. Just like the Vaegirs, Swadians, Rhodoks, Nords and the House of Sarran, we took the Emperor's coin to keep the other tribes at bay. But when the Great Horde attacked our homeland in my grandfather's day, we moved into this region in force. We pushed the Vaegirs back, and made their fortresses our own."),
  ("npc6_home_description", "Here in the Vale of Suno, our dialect and customs are closer than anywhere else in Calradia to those of the old Calrad Empire. We grow olives and wine, both crops brought to this land from overseas by the emperors, and also follow the old Calradic ways. We keep our pledges and pay our debts."),
  ("npc7_home_description", "Before I was married off, and before I was taken by bandits, I lived here. I was born in a hovel and spent my childhood in the fields. Our landlords were Nord, but we never saw them, merely their cursed minions and overseers. My father, coward that he was, cringed before them."),
  ("npc8_home_description", "You haven't heard the story? When Gundig Hairy-Breeks came to Calradia from Nordland, he planted his banner on the headland and said that it would remain there until he recaptured his 'inheritance.' His 'inheritance', he called it. Gundig believed the skalds who told him that the Emperor had bequeathed Calradia to the Nords, when in fact he just gave us a small strip of land along the coast, so that we would crew his galleys."),
  ("npc9_home_description", "The Nords would sail up the river in their longships. The townsmen of the coast could have stopped them, but they were cowards then, as they are today, and paid them a yearly stipend, known as the Nordgeld, to be let in peace. But the Vaegir king would not pay. My father decided to come over the mountains, to fight with the Vaegir hosts. Three summers in a row they tried to take the Rock, and each time the Vaegir lords held them back."),
  ("npc10_home_description", "In my father's day the Swadians would come calling, thinking to make us knuckle our foreheads and call them their overlords. But Grunwalder, an old veteran of the wars from the hills, showed us how to form a battleline with spear and crossbow that could break a Swadian charge. He fell in battle, but the people gave his name to the castle that was built here, where he fell, so that we would remember, and always stand firm against the horsemens' onslaught."),
  ("npc11_home_description", "I'm from Uxkhal. You know the saying, {sir/madame} -- 'Barley grown in Uxkhal is made into ale in Praven, and we're all the better for it.' Not sure what that means, {sir/madame}, but it's true about the barley. And wheat, and oats. We grow more grain here in the Vale of Uxkhal then all the rest of Calradia put together, and our ale is the best, too. You can see it in the soil here -- rich and black, and smells of good harvests and full bellies."),
  ("npc12_home_description", "The lord over there in Almerra Castle had the dropsy, and had requested a doctor from Uxkhal to treat him. Like a typical university-educated doctor, he went right to Galerian for a cure. Galerian commends sun-metal for dropsy. Now most of Galerian's writings were useless back in the days of the Calradic emperors when they were first written down, and they're doubly worthless today, but sometimes he hits upon the right cure by chance: sun-metal does cure some kinds of dropsy in small doses. However, sun-metal in large doses is poison, something that the Galerian-worshippers never grasped."),
#  ("npc13_home_description", "I had come up here with a small Swadian force, but they were caught by the Rhodoks in the woods and their horsemen cut down amid the trees. I fled and found shelter by the lake, in the arms of the comeliest cowherd you ever saw. She took me to a cave near the high pastures, and would bring me cheese and berries, and tell me the tale from the hills. They say the lake is a gateway to the underworld, and sometimes on the fringes you can the noxious fumes beneath bubbling up to the surface. Such rustics they are!"),
  ("npc13_home_description", "I had come up here with a small Swadian force, but they were caught by the Rhodoks in the woods and their horsemen cut down amid the trees. I fled and found shelter up in the high valleys, in the arms of the comeliest cowherd you ever saw. She took me to a cave near the high pastures, and would bring me cheese and berries, and tell me the tales from the hills -- of playful goat-men who guide lost animals back to their flocks, or of ghostly huntsmen who ride the winds, chasing stormclouds. Such rustics they are!"),
  ("npc14_home_description", "I say 'trying' because in my opinion, Vaegirs don't take well to discipline. Finest archers you ever saw, and good riders too, but they have no stomach for fighting in ranks. Their skills serve them well enough against Khergits and Nords, particularly when they can hide behind walls, but Sarranids can match them arrow for arrow, and I've seen Swadian knights cut through Vaegirs like a knife through butter. Now, a Rhodok spear-wall is designed to stop a Swadian charge in its tracks, and usually does."),
  ("npc15_home_description", "Like most castles that last around here, it's got foundations that are old Imperial Calradic. You can't see them any more with all the rebuilding, but the slabs are the size of a house. They must have been real sorcerors back in those days, because I don't see how they moved those things otherwise. Beautiful location, too -- Culmarr sits right in front of the pass leading out of Calradia, which allows the lord to charge a pretty penny in tolls during the three months of the year that it's not snowed in."),
  ("npc16_home_description", "The snows in these valleys don't melt until late in the year, and the land is hard to plough. You can grow a bit of barley, but not much else. But there's wealth here in the woods: deer, rabbit and lynx, meat and furs, and the mountains have iron, and traders would ship enough saltfish up the river from the coast to keep the people fed for the winter."),

  ("npc1_home_description_2", "They go easy on us farming folk, and don't ask for much in tax -- not that we would be able to pay in any case. The land isn't good enough for most crops. Frankly, it's only good for horse-rearing, and that only for half of the year, in the winter after the rains. In the summer they take their herds back into the mountains. Caravans come over the hills and bring spice to Tulga, but we don't see much of that money down in the villages."),
  ("npc2_home_description_2", "I had loaded up on saffron, cinnamon, cloves, pepper and other spices and a chest full of denars. I estimated that I could buy linens, furs, velvet, iron and wool, and the extra horses to carry them back, and I'd still make a profit. I just hadn't figured in the Khergits, who apparently don't care for others cutting in on their monopoly."),
  ("npc3_home_description_2", "The poets call Veluca a paradise, and I think for once that they do not exaggerate."),
  ("npc4_home_description_2", "How do I know this, you ask? Well... I was taken by them, and held for ransom, but I got away. That's really all there is to tell."),
  ("npc5_home_description_2", "Of course, you know how things go. My father's generation were hard warriors from the cold lands across the mountains, but this generation all has houses in the town and great estates and spend time as much trading as they do practicing archery. The next generation will grow soft on Velucan wine and will lose their lands to the next batch of illiterate hill-raiders to come over the mountains, just you watch. It's how things always were, and how things always will be."),
  ("npc6_home_description_2", "We men of Suno also never forget an insult, and avenge any wrong done unto us. Old-fashioned Calradic honour, I dare say, has brought me to my current fallen state. But despite that, I am proud to be from this region. Our lord is a vassal of the Swadian king in Praven, but as far as we are concerned he is just yet another barbarian chieftain, and we are the Empire's true heirs."),
  ("npc7_home_description_2", "We were allowed to fish the river, raise pigs amid the reedbeds, and grow whatever we could in our private plots, but in the open fields we were only permitted to grow flax, to be taken to Sargoth and woven into linen. So we were always hungry, and weak, and never had the courage to rebel."),
  ("npc8_home_description_2", "The skalds' tales at least gave Gundig an excuse to raise a warband -- not that we Nords ever need an excuse, mind. He sailed across the sea, rallied the Calradian Nords to his banner, and marched on the Rock of Rivacheg. The Vaegirs killed him, and threw his banner into the surf. But the Nords keep coming, and some day all of Calradia will be ours."),
  ("npc9_home_description_2", "Just as the Nords can call on their kinfolk overseas, so does the Vaegir king call on his kinfolk from over the mountains. Had my father not disinherited me, I would also have taken an oath of fealty to the lord of Reyvadin. But just as I was shorn of my inheritance, so also was I shown of my obligations, and it is the Vaegir king's loss."),
  ("npc10_home_description_2", "We grow mulberry trees here for silk and kermes too for the dye. We take it to Jelkala where they weave it into the finest velvet -- not that I have ever had enough denars in my pocket to buy velvet, mind. But the craftsmen of Jelkala also make good crossbows, and for that I'll not begrudge them their little luxuries"),
  ("npc11_home_description_2", "The Swadian king will tell you that Praven was the biggest city in Calradia back under the Empire, and that's why he should rule the whole land today. Mind you, I don't care much about politics, {sir/madame} -- I've sold provisions to every army that ever marched in Calradia, and I tell you that I wouldn't give a single one of them a single biscuit unless I had the cold, hard denars in my hand first. Why these high and mighty kings and nobles can't pay their bills, I'll never know. But I prattle on a bit, there, don't I?"),
  ("npc12_home_description_2", "The difference between poison and cure is the dose. You tell that to everyone you meet, and tell them you heard it first from Jeremus the Great. People think that all the wisdom worth knowing was written in Old Calradic, but I say you can learn twice as much from village midwives and careful examination of nature than from the entire imperial corpus. That's why they threw me out of the university, although in retrospect that was a blessing. Anyway, I put that lord back on his feet, and he availed me of a sack of gold and the corpse of a freshly hanged criminal to dissect. Ha! To think of the lengths I had to go to get specimens back in those days."),
  ("npc13_home_description_2", "Eventually I had to leave, and sometimes I wonder if there is a little herdsboy swaddled on her back, as she takes the cows up to pasture each morning. I'd be tempted to try to find her -- but no, no, one should never look back."),
  ("npc14_home_description_2", "If anyone were ever to unify this little land of ours, I'd sign up to serve them, free of charge. I'd put together an army of Rhodok spears with Nord footmen on the flanks and Vaegir archers in front, take along some Khergit scouts to find and fix the enemy, and some Swadian lancers and Sarranid mamlukes to finish them off. I'd take that army over the mountains and make the whole world kneel to Calradia.... Of course, that's what the Emperors thought, and in the end the tribes took away their Empire."),
  ("npc15_home_description_2", "And here's the funny thing -- when the Rhodok lands first rebelled against the Swadians, they all said they weren't going to have any noble lords ruling over them. You can guess how long that lasted. One Rhodok hill chieftain sets himself up in Culmarr, calls himself 'Count', and the good burghers of Jelkala and Veluca have to lick his boots if they want to sell their wine and velvet outside Calradia. And if you want to keep the counts under control, and the peasants providing the towns with food rather than selling to the highest bidder, then you need a King too, don't you? The Rhodok lands are no different than anyone else, whatever guff they talk about 'ancient liberties' and 'freedom.'"),
  ("npc16_home_description_2", "Still, it was a thin living, and there were always too many mouths around to feed. The Vaegir king and the Khergit khan don't make life any easier for us, squeezing for tax money the villages they control, and raiding for plunder the villages they don't. Of course, I can't say I wouldn't do the same if I had a castle and an army all of my own. The mighty do whatever they can, and the humble do whatever they must."),

  ("npc1_home_recap", "I'm from the high steppe, near {s21}."),
  ("npc2_home_recap", "I was born over the mountains.  I'm a merchant, the son of a merchant, and the grandson of a merchant."),
  ("npc3_home_recap", "I used to live in my father's house in {s20}, but I spent much of my childhood in {s21}."),
  ("npc4_home_recap", "Our ancestral barony is over the mountains, across the Culdarr pass."),
  ("npc5_home_recap", "I was born in the highlands on the other side of the mountains, past Tulga, but I have relatives in {s21}."),
  ("npc6_home_recap", "My family lives in {s21}, but I cannot bear to face them."),
  ("npc7_home_recap", "I was born in a hovel in the fens, not far from {s21}."),
  ("npc8_home_recap", "I was born overseas, in Nordland, and my husband's hall also was in Nordland."),
  ("npc9_home_recap", "I am from the Vaegir homeland over the mountains, where the Vaegir lords lived before the Emperor brought them in Calradia."),
  ("npc10_home_recap", "Born and raised in Jelkala, {Brother/Sister}, and I hope some day to buy land there. But I had a mind to see a bit of the world first, so I took my crossbow and went off to the wars."),
  ("npc11_home_recap", "I was born in the train of an army, and lived all my days in the train of an army. My folk are from Praven, however, so I guess that's as much home to me as anywhere."),
  ("npc12_home_recap", "I come from overseas. I travel the world in search of medical lore."),
  ("npc13_home_recap", "Oh, far away from here, my {lord/lady}, else you would already have heard about me, and would not need to ask such things."),
  ("npc14_home_recap", "I am the younger son of the Count of Geroia."),
  ("npc15_home_recap", "I'm from over the hills. But Calradia is where the money is to be made, these days, if your trade is siegecraft."),
  ("npc16_home_recap", "Why, captain, I was born in Uslum village, but my mother lost her land to a scheming relative and had to put herself in bond to a nearby lord."),

  ("npc1_honorific", "boss"), #Borcha
  ("npc2_honorific", "{sir/madame}"), #marnid
  ("npc3_honorific", "{sir/madame}"), #ymira
  ("npc4_honorific", "captain"), #rolf
  ("npc5_honorific", "{playername} Bahadur"), #beheshtur
  ("npc6_honorific", "captain"), #firentis
  ("npc7_honorific", "captain"), #deshavi
  ("npc8_honorific", "{playername}"), #matheld
  ("npc9_honorific", "{my good sir/my good lady}"), #Alayen
  ("npc10_honorific", "{Brother/Sister}"), #Bunduk
  ("npc11_honorific", "{laddie/lassie} -- I mean Captain"), #katrin
  ("npc12_honorific", "captain"),
  ("npc13_honorific", "oh valorous one"), #nizar
  ("npc14_honorific", "commander"), #lazalit
  ("npc15_honorific", "captain"), #artimenner
  ("npc16_honorific", "captain"), #klethi

  ("npc1_kingsupport_1", "That's a great idea, Boss. All these kings and khans and landed nobles who rule now, with their prisons and gibbets and scaffolds, the whippings and brandings and hangings for any man who might be driven by the crying of his children to steal a loaf of bread, or maybe a horse -- Calradia deserves something better."), #Borcha
  ("npc2_kingsupport_1", "Well, captain -- I'd support you. I think you'd give Calradia the kind of enlightened rule which it has long needed."), #marnid
  ("npc3_kingsupport_1", "Well, my lord -- I would worry for you. Our histories tell us that power tends to corrupt. But in the end, I am comforted by the mercy and judgment you have shown as captain of this company."), #ymira
  ("npc4_kingsupport_1", "Well, captain, I think that you would be the kind of {king/queen} that well-born gentlemen such as myself would be proud to follow into battle..."), #rolf
  ("npc5_kingsupport_1", "A fine idea, Bahadur - you have shown that you know how to govern men. Mind that you govern them justly, though..."), #beheshtur
  ("npc6_kingsupport_1", "I cannot judge the legal merits of your claim. However, I think that unlike the other kings here, you have the capacity to unify this land -- and that would put a stop to these endless wars, between kingdom and kingdom, noble and noble, and brother and brother, that have brought us all into disgrace in the eyes of the heavens."), #firentis
  ("npc7_kingsupport_1", "Aye -- you'll do well. You know how to treat bandits and ruffians."), #deshavi
  ("npc8_kingsupport_1", "The saga of Bjernstad tells us that a man who does great deeds, beyond those of the other men of his time, may claim the throne. I'd say that you could make that claim."), #matheld
  ("npc9_kingsupport_1", "Very good, my lord. I'm a Vaegir by blood, but Yaroglek never stood for me when I was cheated of my inheritance. So I don't owe him anything, and I say, 'Let the throne go to the most valiant!' Which would be you, {sir/my lady}."), #Alayen
  ("npc10_kingsupport_1", "Well, {Brother/Sister}, I suppose there must be {kings/kings and queens}, and if there must be {kings/kings and queens}, then you would be as good a {king/queen} as any..."),#Bunduk
  ("npc11_kingsupport_1", "Why, that's a fine idea, {laddie/lassie}! I suppose I shall have to learn to call you 'Majesty', or 'Your Grace', then..."), #katrin
  ("npc12_kingsupport_1", "I am sure that you would make a fine king, captain. I flatter myself that I am a good judge of character, and you have demonstrated a capacity for compassion that far exceeds that of these others who call themselves monarchs."), #jeremus
  ("npc13_kingsupport_1", "That would be a fine thing, {sir/my lady}! Many is the tale of the hero who has proven his worthiness to wear a crown through valor. Perhaps you know the song of Antaran son of Ashdab, who rose from obscurity to become king of Dabarah. A splendid tale!"), #nizar
  ("npc14_kingsupport_1", "Well, sir, the heavens have instituted a hierarchy in this world, and normally I would have no truck with usurpation. But I also think that the kings of this land are a weak and sorry lot, not worthy of the name of king, and that leaves the crown free to be taken by a better {man/ruler}, such as yourself."), #lezalit
  ("npc15_kingsupport_1", "Well, you pay your men on time, when you can, generally speaking. That's the best qualification for kingship there is, in my book. You show some respect for the rights of others."), #artimenner
  ("npc16_kingsupport_1", "Why not, captain? I'm sure you'd make a fine {king/queen} -- and of course I'd hope you remember the little people like myself who did you a pretty turn on your scramble to the throne."), #klethi


  ("npc1_kingsupport_2", "Sure would, Boss. But let me tell you what might bring others to your cause -- particularly us poor folk. They tell us that in the old days, each new Emperor who took the throne would issue a great amnesty for all but the worst prisoners in his dungeons, give people a second chance to make something of themselves -- like you gave me a second chance, Boss."), #Borcha
  ("npc2_kingsupport_2", "Most of the lords of this land -- well, let's just say that they never held a denar that they didn't collect as rent or take as pillage. You, on the other hand, have some experience of commerce and trade, of the effort and risk involved in making sure that men don't go hungry in Sargoth while there's a glut of grain in Praven, to give an example.... If you like, captain, I reckon I could find some support for you among the merchants and burghers of this realm."), #marnid
  ("npc3_kingsupport_2", "I would, {my lord/my lady}. But I would strongly recommend that you reinstitute an old Calradic imperial tradition -- the council of lords and commons, drawn from both the nobles of the land and well-educated men of property, with the power to overrule any new taxes or other tyrannical measures that might tempt you. It would be for your own good, {sir/my lady}."), #ymira
  ("npc4_kingsupport_2", "Of course, {captain/my lady}. The trick is now to get others to follow you. As you know, one's lineage is a great determinant of one's worthiness. Perhaps you have a long-lost ancestor of whom you have not told me?"), #rolf
  ("npc5_kingsupport_2", "Ay, Bahadur, I would. But there is something I should say, on behalf of the men of the steppes such as myself. It would bring great joy to us, to hear from the lips of one who would be khan, that you would restore an anicent right. From the days of the old emperors, the men of the steppes have enjoyed the right to bring their flocks to new pastures or to market, which necessarily involves the crossing of lands owned by the great lords of this realm."), #beheshtur
  ("npc6_kingsupport_2", "I would. I would tell anyone who listens of your deeds on behalf of the weak and helpless, of your ability to lead men against great odds and triumph, and tell them that if you were to become {king/queen}, there would be one law and one peace -- from the Rhodok highlands to the Vaegir wastes, from the high steppe to the Nordic shore."), #firentis
  ("npc7_kingsupport_2", "Yes, captain, I would. A {king/queen}'s duty is to keep the roads safe for decent folk, make it so a woman can gather the firewood or draw the water without being accosted by some drooling, scabby ape of an outlaw. Anyway, you've split the skulls of a number of such brutes in your time. Men would fear to even meet the eyes of a woman on the road, if you were {king/queen}."), #deshavi
  ("npc8_kingsupport_2", "I would -- on one condition. You'd be king in Praven or Sargoth or wherever you want to rule, but I'd rule my own hall. And if I had a dispute with any other of your thegns, be it over land, livestock, or blood, you'd let us settle it sword to sword, according to the old ways, and let the heavens decide who is in the right."), #matheld
  ("npc9_kingsupport_2", "I would, {sir/madame}, and others would too. But here's what I think -- you need to show the noble lords that you'll uphold their ancient rights. Right now, Calradia's a mess -- the lord owns the land, except it's the king who owns the forest, but the city has the right to levy tax at its gates, and the commons can use the pastures on odd Tuesdays, except in Rivacheg when it's Wednesday. Who can remember? So I say you make things simple, like it was in the old days -- first the {king/sovereign}, then the lords, then everyone else."), #Alayen
  ("npc10_kingsupport_2", "Certainly, {Brother/Sister}. But I'd ask that you consider a thought of mine. If you became {king/queen}, then I'd ask you open your court to the common folks, and not just to the lords and blue-bloods. I'd ask you to let it be known that should any man be judged and sentenced, that he have the right to appeal to you directly. Right now, the lords have the right -- I say every man in Calradia should have it, too."), #Bunduk
  ("npc11_kingsupport_2", "Of course, I would! Let me see your hand, there... Aha! You've got the 'Mark of Kings.' That's what we call it in Praven, anyway. I hear in Suno it's the 'Emperor's Line,' but they call everything differently, over there. Anyway, yours is very long -- I'd say that it means that you're meant to rule! It's your destiny! In fact, I think I can even recall a prophecy to that effect. Hmm, how did it go..."), #katrin
  ("npc12_kingsupport_2", "Of course, captain.  But if I have learned anything in my travels in this land, it is that Calradians are sticklers for precedent. Everything must be done as it was done in the days of the old Empire -- even though not more than one in a hundred of them can read enough Old Calradic to understand the chronicles! Veluca merchants marry their daughters according to the 'imperial' rite. Rivacheg cattle herders churn 'imperial' butter. And of course, every king must be crowned according to 'imperial' law."), #jeremus
  ("npc13_kingsupport_2", "Of course, {my lord/my lady}. Also, as we learn from the tale of Antaran, when claiming a throne, it does not hurt to be the subject of an epic, recited around campfires and hearthfires, describing one's deeds. As you no doubt know, I fancy myself a fair crafter of couplets."), #nizar
  ("npc14_kingsupport_2", "I would indeed, sir. I think you can unite this land, and then we'll be able to raise an army such as Calradia has not seen for many generations -- Swadian lances, Vaegir archers, Rhodok spears, Sarranid swords, Nord axes, and Khergit skirmishers, and take it over the mountains to subdue all the lands that the Calradic emperors once held sway."), #lazalit
  ("npc15_kingsupport_2", "I would. People might say that you don't have royal blood in your veins. But as far as I've seen, royal blood makes you a skinflint. Kings and nobles will take out loans or commission building projects without half a thought to how they're ever going to pay back all those commoners who expect to eat after an honest day's work. If you ask me, an honest tongue makes a {man/woman} a {king/queen}, not a fancy pedigree."), #artimenner
  ("npc16_kingsupport_2", "Of course, my {lord/lady}. And what's more, I figure a girl like me could do you a bit of a service raising support with the lords of this land. I may have only had a small part in their schemes and intrigues over the years, but I think I know what they want. And given what I know of their secrets, they'd not want to be denying me admission to their halls, now would they?"), #klethi

  ("npc1_kingsupport_2a", "Please go on..."), #Borcha
  ("npc2_kingsupport_2a", "Please continue..."), #marnid
  ("npc3_kingsupport_2a", "Please continue..."), #ymira
  ("npc4_kingsupport_2a", "Of course - let me tell you all about him."),
  ("npc5_kingsupport_2a", "Please go on..."), #beheshtur
  ("npc6_kingsupport_2a", "Splendid"), #firentis
  ("npc7_kingsupport_2a", "Well, yes, I will try to keep order..."), #deshavi
  ("npc8_kingsupport_2a", "Fair enough"), #matheld
  ("npc9_kingsupport_2a", "That seems sensible enough..."), #Alayen
  ("npc10_kingsupport_2a", "Of course - I would give my subjects that right"), #Bunduk
  ("npc11_kingsupport_2a", "See if you can recall that prophesy."), #katrin
  ("npc12_kingsupport_2a", "Interesting. Please go on..."), #jeremus
  ("npc13_kingsupport_2a", "Why, yes, that you are."), #nizar
  ("npc14_kingsupport_2a", "Please go on..."), #lazalit
  ("npc15_kingsupport_2a", "Well-spoken, my good man"), #artimenner
  ("npc16_kingsupport_2a", "Interesting... Please continue"), #klethi

  ("npc1_kingsupport_2b", "Well. We saw how that turned out..."), #Borcha
  ("npc2_kingsupport_2b", "I do not ask for their support, as they would no doubt wish to make a profit on the transaction."), #marnid
  ("npc3_kingsupport_2b", "I have no intention of hobbling myself in that way."), #ymira
  ("npc4_kingsupport_2b", "I will have no part of this"), #rolf
  ("npc5_kingsupport_2b", "I said that I wished to be {king/queen}, not that I wished to involve myself in the minutiae of nomadism"), #beheshtur
  ("npc6_kingsupport_2b", "I'm not sure that I can quite deliver all that"), #firentis
  ("npc7_kingsupport_2b", "I think you're maybe taking the idea of the king's peace a bit too far, there"), #deshavi
  ("npc8_kingsupport_2b", "That's a pretty tall condition"), #matheld
  ("npc9_kingsupport_2b", "I'm not sure that implementing your idea would be as 'simple' as you think"), #Alayen
  ("npc10_kingsupport_2b", "Hmm. Let me think it over."), #Bunduk
  ("npc11_kingsupport_2b", "Ah... I'll have my hand back, please."), #katrin
  ("npc12_kingsupport_2b", "Enough, sir. I will not have you mock our traditions"), #jeremus
  ("npc13_kingsupport_2b", "Hmm. I'm not sure about that."), #nizar
  ("npc14_kingsupport_2b", "Actually, I was looking forward to a bit of rest after becoming {king/queen}..."), #lazalit
  ("npc15_kingsupport_2b", "{King/Queen} of the Clerks, maybe, Enough of such talk"), #artimenner
  ("npc16_kingsupport_2b", "No offense, but I'm not sure that's the approach I'd take"), #klethi

  ("npc1_kingsupport_3", "If I could go about this land for a few weeks, telling the common folk that you were going to amnesty their kinfolk like the emperors of old -- well, they would start talking of you as the Emperor, and that would pave your way to the throne. Shall I do that, Boss?"), #Borcha
  ("npc2_kingsupport_3", "If you like, captain, I can take a few weeks to visit the guildhalls and caravanseries where I have contacts, and explain to them that, in you, they will have a {king/ruler} who will check the rapacious nobles, who, with their tariffs and taxes, would strangle commerce for the sake of a few extra denars to spend on their wars and their feasts. What do you say to that, captain?"), #marnid
  ("npc3_kingsupport_3", "If you were to make such a pledge, {sir/madame}, I think that it would help many of the lords of this land overcome any reluctance that they might have. If your aim is to restore the old Calradic system, then arguably you are a more legitimate {king/ruler} then any of these come-lately usurpers. Give me leave for several weeks, {sir/madame}, and I will let it be known in the noble courts and merchant houses of this land that you intend to restore their ancient rights."), #ymira
  ("npc4_kingsupport_3", "Yes -- I think I have heard of that line, In fact, I can envision {his/her} entire genealogy. If you give me leave, 'Majesty', I shall travel about the villages and castles of this realm over the next several weeks, spreading word of your royal birth. Of course, I would hope that you would remember your faithful subject, when it comes to distributing lands..."),
  ("npc5_kingsupport_3", "Anyway, lord, in these sorry times the men of the great estates have taken to blocking our passage, charging us huge fees to cross. It is a great burden on my people, Bahadur. If I could take a few weeks to let the men of the steppes know that you would support the restoration of our ancient rights, well, then, I think you would find many who would support you as khan, And when men speak of you as khan, that's the first step to becoming one."), #beheshtur
  ("npc6_kingsupport_3", "Very well. Although I am now a stranger to my family, I have entered many a noble's hall in your train, and I reckon I would be welcome again. I shall go about this land and tell the nobles that when you are {king/queen}, you will strive your hardest to protect the weak and to crush discord, so that no man will raise his hand against another with impunity, and one day, perhaps, the sin of fraticide will be no more."), #firentis
  ("npc7_kingsupport_3", "I'll tell you what, captain. Give me a few weeks and I'll go to some of these villages -- stinking hovels that they are, but I reckon I can take care of myself these days. I'll tell the people there that once you unify this land, you'll wipe it clean of banditry. You'll erect gallows along the roads and keep them well-stocked with broken-necked thieves, so that every passerby knows that the wages of indecency is death."), #deshavi
  ("npc8_kingsupport_3", "Good! Then give me a few weeks and I'll go about the courts of this land, letting it be known that you're a {king/ruler} who respects the thegns and their ancient rights. You won't go sticking your royal nose where it doesn't belong, and Calradia will be the better for it."), #matheld
  ("npc9_kingsupport_3", "It's perfectly sensible, {sir/madame} -- and we'll be free of those cursed writs and burghers' petitions and scrolls that take up all of my time and yours, when we should both be out fighting for the glory of your kingdom. Give me leave and I'll spread word among the noble lords of this land that you're here to restore the old ways, and I'll bet there will plenty who will follow you into battle."), #Alayen
  ("npc10_kingsupport_3", "Well then, {Brother/Sister}, give me leave for a few weeks and I can go about this land, letting the common folk know that you will rule justly and equitably, and that lord and common alike should be one before your law. Men will speak of you as {king/queen}, and that's a good start to becoming one..."), #Bunduk
  ("npc11_kingsupport_3", "I can't recall now, but if you let me go back to my home, I could find an old greybeard who remembers it in full. And, I could put it around that you've got the mark of kings on your hand! There's many where I come from who are waiting for a just ruler, and a man's hands tell all that's worth knowing about him. Give me a few weeks, and I'll reckon I can have quite a few expecting you to be their next {king/queen}."), #katrin
  ("npc12_kingsupport_3", "But you know what? There was no 'imperial' law when it came to the crown. Sometimes one emperor handed the empire to his son. Sometimes he split it between his generals. Sometimes one emperor murdered the last. There's no right 'Calradic' way to crown a {king/king or queen}, and thus it makes sense that the crown should go to the one most fit to govern -- which would be you, naturally. Give me a couple of weeks, and I'll write a tract which proves it and find a copyist to post a version in every town tavern in the land. What do you say to that idea, captain?"),
  ("npc13_kingsupport_3", "Then give me leave for a few weeks, oh gallant one, and I will spin such a tale as would stir even the dullest heart, inspiring admiration for your virtues, compassion for your hardships, and indignation at those who would stand in your way. I assume, of course, that I would be able to take a certain amount of poetic license with the details?"), #nizar
  ("npc14_kingsupport_3", "Give me leave for a few weeks, {sir/madame}, and I will let all the worthy men of this land know that you are the one to unite not just Calradia, but all the other Calradic dominions. For according to my thinking, no one should be {king/king or queen} here unless they have the capacity to rule the entirety of the realm -- and you alone have demonstrated such a capacity, {sir/madame}."), #lazalit
  ("npc15_kingsupport_3", "I'm glad you think so. Here's what I suggest. I know men in the guilds here, men like me, who've been shafted and shaken down until they can take no more. Here's what I'll tell them -- you're honest. You respect the burghers. You'll pay your debts. You won't beggar your subjects."), #artimenner
  ("npc16_kingsupport_3", "Give me leave for a few weeks, and I'll do a little tour of my former employers' castles. I'll sing them a pretty song about what you'll do as {king/queen}, about all the ancient freedoms you'll restore -- let them rob their tenants and tax the merchants and fight their wars and spend themselves silly without a thought to tomorrow, as a noble ought! What do you say to that, captain?"), #klethi

  ("npc1_kingsupport_objection", "Boss -- you've given leave to Alayen to go tell the nobles that they will have rights over pasture, market, and forest? I can't say I like that. Give him his way, and he'll set up gibbets in every village in the land, where there will dangle some poor sod like me who thought he might pick up a bow, head to the woods and put a bit of meat on his table."), #Borcha
  ("npc2_kingsupport_objection", "Um, captain. Matheld has ridden off to tell the lords of this land that you'll let them settle their quarrels by force and violence. You know they rarely actually fight each other, right? Most of the time, it's the traders and travellers on the roads between their castles that get clobbered in their petty disputes. Any excuse to shake down a caravan, they'll take. I really hope that she misunderstood you, sir."), #marnid
  ("npc3_kingsupport_objection", "Captain -- Deshavi has set off on some sort of expedition, which she says that you countenanced. She says that she will go about the villages of this land, telling the poor villagers that once you are {king/queen}, you intend to hang all thieves and bandits. {Sir/Madame}, I am a merchant's daughter, and know well the scourge of banditry. I also know that Deshavi has suffered great wrongs. But surely you do not intend to hang men indiscriminately. There must be some place for mercy in your kingdom"),
  ("npc4_kingsupport_objection", "Captain. Artimenner has set off on a journey, telling the burghers that you claim the throne because you know how to balance your accounts. That's nonsense. Nobles and kings fight and rule. If they had to haggle over wages and overruns with every passing vagabond who ever did a scrap of work on their estates, then there would be nothing but disorder and chaos."),
  ("npc5_kingsupport_objection", "{playername} Bahadur -- I overhead what you told Ymira. But I wonder -- if the lords who live from farming, and the merchants who earn from trade, are allowed to determine what taxes will be leveed, then who will be taxed? Those who live from flocks, of course -- my people, the people of the steppes. I would have nothing to do with these councils, Bahadur -- all free men should be one, under the khan, and that is the end of it."), #beheshtur
  ("npc6_kingsupport_objection", "I understand that you have dispatched Rolf to fabricate a claim of royal descent. I have to tell you, {sir/madame} -- I do not think that the heavens will smile on such an attempt to take the throne by fraud."), #firentis
  ("npc7_kingsupport_objection", "I have heard what you told Bunduk, about giving every common criminal the right of appeal to the {king/ruler}. I do not approve. Bandits should be hanged when caught. Give them a trial or an appeal, and they will talk their way out of the noose. Bunduk is a good man, but no man can fully understand what these wolves in human form do to women"), #deshavi
  ("npc8_kingsupport_objection", "Captain -- you have dispatched Firentis to tell the lords of this land that you intend to impose a peace, under which no one should settle their disputes by the sword. Would you have us all die in our beds, then? That is a great shame, for my people. A {king/sovereign}'s duty is to lead us into battle, not to tell us how to handle our quarrels and differences."), #matheld
  ("npc9_kingsupport_objection", "{Sir/Madame} -- it is with great regret that I have learned that you have told Baheshtur to let his people know that you will allow them to lead their flocks over the lands of their betters. I hope that I am mistaken about this, sir. The money we demand is but small compensation for the damage they cause to our flocks and the pollution of our water sources. My {lord/lady}, if your future kingdom is to be some nomads' paradise, then I for one do not look forward to it."), #alayen

  ("npc10_kingsupport_objection", "I hear that you've got Nizar spinning poems to justify your ascent to the throne. I can't say I approve, {Brother/Sister}. If men fight for a {king/sovereign}, it should be because they know they're going to get something good out of it, not because they've taken a liking to a silly song."), #Bunduk
  ("npc11_kingsupport_objection", "I hear that Lezalit is off and about telling folks that you're going to make yourself {king/queen} and then lead an army over the mountains. Shall there be no end to these wars, {laddie/lassie}? I was thinking that if you made yourself {king/queen}, then maybe you'd give us a bit of peace. But I guess the heavens have made Calradian blood to be spilt, and Calradian bones to be broken, and there's no getting round their decree."), #katrin
  ("npc12_kingsupport_objection", "Captain. I hear that you've gone and made Klethi, of all people, some sort of ambassador to the aristocracy. I shudder to think of what that amoral girl might be promising them on your behalf -- and dignifying all these gross indulgences by calling them 'ancient freedoms.' By doing this, you mock those of us who who had hoped that you would have helped Calradia escape its bloody past, and move towards a new age of peace and learning. Enough, I have said my peace."), #jeremus
  ("npc13_kingsupport_objection", "Oh valiant one -- I hear that you have given leave to Jeremus to produce some testily-worded dissertation that undermines everything the people of this land hold dear, and accuses the old emperors of murder and usurpation. Captain -- I know as a poet that people must have heroes to emulate, and a golden age to restore. Will you create a kingdom in which cynics and scholars tell us what we must believe? I can think of nothing more dull."), #nizar
  ("npc14_kingsupport_objection", "I understand that you've sent your man Borcha to proclaim to all Calradia that you intend to free all the miscreants of this land upon your accession to the throne. What a foul idea... Men must be governed, {sir/madame} -- with whips and chains and the noose, if necessary. You'll find that out the hard way if you become {king/queen}, I'll warrant."), #lezalit
  ("npc15_kingsupport_objection", "I understand that you've given leave to Katrin to spread some nonsense about marks on your hands. I just want to say that, as an educated man, I find it disturbing that you would resort to old women's superstitions to back your claim. Village women will believe one thing one day, another thing the next. Now a horoscope, properly cast by an astrologer at a royal university with a reputation to uphold, might tell you something worth knowing, but those have not been performed in Calradia for some time."), #artimenner
  ("npc16_kingsupport_objection", "Oy -- Captain! I hear that Marnid's gone off to sing a pretty song to the merchants, on how you'll hand them Calradia on a silver platter for them to feast upon, smack their lips, and suck the marrow from the bones. I hope that's just a tale you're telling. A noble lord will at least toss a few coppers to the poor when he holds his feasts, and will make sure that the servants go home with full bellies. A merchant marries his daughter, and you'd be lucky to get a few crusts and scraps of gristle from the table. That's my experience, anyway."), #klethi

#
  ("npc1_intel_mission", "Well, Boss, as it happens, I have a few cousins over in {s17}, and unlike some in my family, they can still stand the sight of me. They deal in horses --- I've even been able to supply them with stock from time to time -- and so they get to pick up a bit of the gossip round the castles and great halls of the {s18}. I could go over there for a few days and tell you what I find out."), #Borcha
  ("npc2_intel_mission", "{Sir/My lady}, if you're interested in events in {s18}, I can still make contact with my old trading partners in {s17}. They're usually well-informed about political events."), #marnid
  ("npc3_intel_mission", "Captain, although I cannot return to my father's house in {s17}, I still may make contact with my sister. She will be privy to the councils of the great merchant houses, and may tell us much about the state of the {s18}."), #ymira
  ("npc4_intel_mission", "Captain, if you could spare me for a few days, I would like to look up an old comrade-in-arms in {s17}, who has from time to time led a small company in the pay of the {s18}. He is a good man, the kind who speaks little and listens much. I'm sure over a drink or two he might let us know which way the political winds are blowing in those parts."), #rolf - men whom i fought with
  ("npc5_intel_mission", "If you like, {playername} Bahadur, I can take a few days to visit my mother's sister's people. They work in a caravanserie in {s17}, and hear the news from all across the {s18}. They may have some gossip about the feuds and rivaries of the great lords, if that is of interest to you."), #beheshtur
  ("npc6_intel_mission", "Captain -- while I am not strictly welcome in {s17}, I would be able to make contact with some former tenants of an estate of mine nearby. I granted them ownership after my abrupt departure, and they are now well-placed in society, and also less inclined than most to hold my crime against me. If you give me a few days, I may be able to collect some interesting information about the {s18}."), #firentis
  ("npc7_intel_mission", "Captain. When I left my former home in {s17}, I had promised myself that I would never return, except for the purposes of taking out vengeance on those who wronged me. Perhaps I was rash. I am occasionally curious as to how my family is getting along. Perhaps I can bring them some gifts, to let them know what I have made of myself! Any rate, they are wretched people, but just as a cringing dog keeps its ear to the wind, so do they. They may have useful information about the {s18}, if you would give me a few days to pay them a visit."), #deshavi
  ("npc8_intel_mission", "If you have any interest in the events in the {s18}, a former shield-companion of mine retired and now keeps a farm near {s17}. He keeps in contact with a number of other old warriors. I could visit him for a few days, and learn more about what is going on there."), #matheld
  ("npc9_intel_mission", "{Sir/My lady} -- it has been some time since I sampled the delights of {s17}, where gentlefolk such as myself are wont to partake of the hospitality of the most puissant and generous lord. If you wish, I could perhaps go there, and let you know something about the concerns that weigh on the minds of the great peers of the {s18}."), #Alayen
  ("npc10_intel_mission", "Captain -- I was thinking that some of my old mates in the garrison at {s17} would be glad to see me. They are good lads, and would never betray the city, but like me they have no particular affection for the bluebloods that command them, and may be willing to slip a little political gossip our way. The gentry are always falling out over one little thing or the other, but the lads might be able to know if there's real dissent brewing."), #Bunduk
  ("npc11_intel_mission", "{Laddie/Lassie} -- I was thinking that it's been a while since I visited my kinfolk in {s17}. They've been kind enough to me over the years, helping me out during the lean times, so I feel I'd like to share some of my newfound fortune with them. I've also bought wholesale enough times from the {s17} grain merchants for them to trust me. I'd reckon they might be persuaded to spill a few tidbits about events in the {s18}, if that would interest you."), #katrin
  ("npc12_intel_mission", "If you wish, Captain, I would not mind taking the time to pay a visit to a pupil of mine, now employed by the lord of {s17}. I had great hopes for him, but I have heard that he has lately endorsed the use of muskmelon for the treatment of palsy, on the grounds that its cold essence offsets an abundance of yellow bile. This is a travesty of medicine, and I must journey there swiftly to correct him. While I am there, if you wish, I could question him on the latest trends within the {s18}, a matter which may interest you."), #jeremus
  ("npc13_intel_mission", "Oh valiant one! With your permission, I was thinking that I might pay a visit to the dales near {s17}. I try not to revisit old pastures, but I must confess a certain curiosity as to how a comely shepherdess of my former acquaintance is getting along. On the way, I may attempt to stop in at the castle. I suspect that it would not be terribly difficult for me to charm my way into the lord's hall, and I may be able to provide you with the latest news from the {s18}."), #nizar
  ("npc14_intel_mission", "Captain... As you may know, I helped train the garrison of {s17}. One of their number has lately been in touch with me, and suggests that if I were to visit him, he could pass me information on events within the {s18}. I am willing to do this, if you can spare me. While it is a great disgrace to be a traitor, there is no dishonor in making use of one."), #lazalit
  ("npc15_intel_mission", "Captain. As you may know, I have for some time harbored a wish to go to {s17}, and study the masonry -- one of the finest examples of the old Calradic style. As it happens, one of my colleagues is currently engaged there doing repair work on the curtain wall. While his sense of professional obligation I think would prevent him, rightfully, from disclosing to me any weaknesses in its defenses, I suspect that he would not be averse to offering up his opinion on the general state of the {s18}, if that is of interest to you."), #artimenner
  ("npc16_intel_mission", "Oy, Captain! I had a mind to pay a visit to my old haunts at {s17}. Let's just say that the lord and lady of the place had commissioned a certain service from me, and had been a bit lax about payment. However, a certain sparkly bauble in the lady's possession will fit the bill nicely. I see no need to trouble them by letting them know about my visit, but I could have a wee chat with my old friend the castle steward, who'll be letting me into the place, about goings-on in the {s18}."), #klethi


  ("npc1_fief_acceptance", "You'd make me lord of {s17}, Boss? Well, that would be the kindest thing that anyone has ever done for me in a long time. Heh. I'll make the most of it -- you can count on that. I have to say, though -- I'm not sure how the other lords of this realm will react, when they find old Borcha in their august company."), #Borcha
  ("npc2_fief_acceptance", "{s17} as a fief? Well, I've always thought in terms of buying and selling goods, not in terms of governing anything. But now that you mention it, I bet I could make that place turn a fair bit of revenue. I thank you, {my Lord/my lady} -- this is a very kind turn that you have done me."), #marnid
  ("npc3_fief_acceptance", "{Sire/My lady}, it is most generous of you to offer me {s17}. I would be pleased to hold it, and dedicate myself to the moral and material uplift of its inhabitants."), #ymira
  ("npc4_fief_acceptance", "It is good of you to grant me {s17} as a fief -- and most appropriate. Proud indeed is the king who has a baron of the House of Rolf as {his/her} vassal."), #rolf
  ("npc5_fief_acceptance", "Bahadur -- I would be most pleased to hold {s17}. I will send word to the hills, to my kinsmen, and let them know that there is honorable gold to be earned serving under me in your armies -- and they will come flocking to fight for you!"), #beheshtur
  ("npc6_fief_acceptance", "{Sir/Lady} -- I am surprised that you find me worthy to govern men, as I am just beginning to learn to govern myself. But if you indeed wish it, I would be most honored to hold {s17} in your name, and dedicate myself to the protection of those who live there."), #firentis
  ("npc7_fief_acceptance", "Aye, I'll hold {s17} -- and give it a reputation that strikes fear in the hearts of thieves and brigands across Calradia. Thank you, {sire/madame}, for this opportunity."), #deshavi
  ("npc8_fief_acceptance", "You'd make me a thegn? Well, I suppose that I can postpone reclaiming my inheritance for a little while longer, and make my great hall at {s17}. Some day, I may travel over the seas to take back what is mine, but until then, I would be pleased to raise a band of battle-hardened Nords to fight under your banner."), #matheld
  ("npc9_fief_acceptance", "{Sire/My lady}, I was cheated of my inheritance -- but now, with this offer of this estate, you make right what was wrong. It would give me the greatest honor to serve you, to fight for you, and to hold this land in fief to you."), #alayen
  ("npc10_fief_acceptance", "You'd make me a lord? Well, no thank you -- but if you would call me 'tribune' -- the tribunes being the people's servants in the old times -- then I suppose I could bring myself to run {s17} for you. I'd put food in the bellies of the hungry, and raise a fine force of Rhodok foot to fight on your behalf, {Brother/Sister}. But I can't promise that the real blue-bloods will enjoy rubbing shoulders with me in your councils."), #bunduk
  ("npc11_fief_acceptance", "Ay! You'd grant old Katrin a title of nobility? Well, I'd be daft to turn you down, now wouldn't I? My, the strange turns that life takes... Fancy this old bag of bones becoming a great peer of the realm of Calradia."), #katrin
  ("npc12_fief_acceptance", "Well, {sire/my lady}, I'd have you know that don't believe in the holding of land in fief to the king. Farmers and landholders should govern their own affairs, under the distant watch of the sovereign. That being said, Calradia has seen far too much bloodshed for us to turn the social order on its head right now. Give me that land, and I'll endeavor to prepare it for a brighter future -- if not in this generation, than perhaps in the next."), #jeremus
  ("npc13_fief_acceptance", "How generous and kind of you, {sire/my lady}. Allow me to express the utmost reverence for your wisdom in selecting me. Truly, your perspicacity exceeds that of King Laminur, who could read the character of a man from a single hair of his head. Your judgment surpasses that of the Emperor Akembra, to whom even the jinns submitted their disputes. Anyway, I accept."), #nizar
  ("npc14_fief_acceptance", "You do me a great honor, captain. In Geroia, a youngest son such as myself has few opportunities to earn a fief of his own. But here, in Calradia, there is still the chance for a man to win with his sword what was denied him by his birth! I shall hold {s17} as your vassal, and raise an army to fight for your glory and for mine."), #lazalit
  ("npc15_fief_acceptance", "Well, {sir/my lady}, that's a gracious act, and marks you as the kind of monarch who can save this sorry land from the incompetence of the current batch. I suspect a lot of the noble lords around here will think that a commoner like me isn't fit to hold a fief. Well, when they see what I do with it, and what revenues I can bring in, they'll change their tune!"), #artimenner
  ("npc16_fief_acceptance", "Oh, that's most generous of you, {sire/my lady}. I've been in and out of many a great hall or manor -- not always with the master's permission, I should add -- but I never thought I'd own one myself. Let me think... When I collect my first year's rents, what baubles shall I buy myself?"), #klethi

  ("npc1_woman_to_woman", "{!}."), #Borcha
  ("npc2_woman_to_woman", "{!}."), #marnid
  ("npc3_woman_to_woman", "My lady, if you don't mind me saying -- I think by now you have proven yourself to be one of the great warriors of this realm. Yet strangely, no king has come forward to offer you a fief. Perhaps it is because you are a woman. No matter -- I personally believe that you will take your place among the great lords of this realm, even if you have to fight twice as long and twice as hard to receive your due!"), #ymira
  ("npc4_woman_to_woman", "{!}."), #rolf
  ("npc5_woman_to_woman", "{!}."), #beheshtur
  ("npc6_woman_to_woman", "{!}."), #firentis
  ("npc7_woman_to_woman", "Captain. If you don't mind me saying, you have fought long and hard against the scum of Calradia, and with their defeat, you make this land a better place. You are well deserving of a fief of your own -- and I suspect that if you were not a woman, a king would have offered you one by now. That is the way of the men in this sorry land: they let us stand in the front of the battleline to take the enemy's blows, but when it comes to a division of the spoils, they expect us to head to the rear."), #deshavi
  ("npc8_woman_to_woman", "Excuse me, {playername}. I would like to offer you my congratulations -- it seems that you are well on your way to making a name for yourself as a warrior to be feared. If you were a man, I suspect the kings of this land would be falling over themselves to make you their vassal. Alas, in this world, women like ourselves must fight twice as hard to receive what is only our due."), #matheld
  ("npc9_woman_to_woman", "{!}."), #alayen
  ("npc10_woman_to_woman", "{!}."), #bunduk
  ("npc11_woman_to_woman", "Aye, lassie, I just can't help thinking to myself -- you've made quite a name for yourself, haven't you? Fighting and marching up and down the length of the land. Why, I suspect if you were a man, some king would have offered you a fief by now. Well, you may still get what you deserve -- you'll just have to prove yourself a bit more."), #katrin
  ("npc12_woman_to_woman", "{!}."), #jeremus
  ("npc13_woman_to_woman", "{!}."), #nizar
  ("npc14_woman_to_woman", "{!}."), #lazalit
  ("npc15_woman_to_woman", "{!}."), #artimenner
  ("npc16_woman_to_woman", "Oy, Captain -- if you don't mind me saying, you've made quite a name for yourself in these parts. I suspect that if you were a man, a king would have offered you a fief by now. But we ladies should come to expect things like that. Men will find any excuse not to reward us for our work, so if we take a fancy to a bit of land somewhere, maybe we should just reach out and take it. That's the way I look at the world, anyway."), #klethi

  ("npc1_turn_against", "I'm sorry that we meet like this, boss. There's no question that I owe my rise in life to you. You doubtless think me ungrateful. However, one has to follow one's destiny -- isn't that correct?"), #Borcha
  ("npc2_turn_against", "This is a sad day. I never thought that I might meet my old captain on the field of battle. Even if I triumph, it will bring me no joy."), #marnid
  ("npc3_turn_against", "Oh {playername} -- what a tragic turn our lives have taken! I can only hope that the tides of war that have made us enemies, will one day allow us to be friends."), #ymira
  ("npc4_turn_against", "Aye, well.... I'm not sure what to say. If we must fight, let's get it over with."), #rolf
  ("npc5_turn_against", "{playername} Bahadur! I took your salt, and was well rewarded for it! However, I will remind you of an old truth -- that while a Khergit may be an ardent follower, and a devoted friend, he will never be your slave.... Anyway, today I come against you with my sword raised. But I hope that one day we raise a glass together, to a friendship renewed."), #beheshtur
  ("npc6_turn_against", "It grieves me more than anything I can say to meet you like this, {playername}. I shall not dwell on the circumstances that have led us to this point. I can only hope that we may one day be reconciled."), #firentis
  ("npc7_turn_against", "Well, captain. You made of me a great lady, and for that I am grateful. However, you did not buy me, and now the circumstances have caused us our interests to clash, I can meet you in battle with a clear conscience. Still, I hope some day that circumstances may change again, and we may meet as friends."), #deshavi
  ("npc8_turn_against", "So we now we meet as enemies, and may shortly face each other over the rims of our shields. A grim day this is. Sometimes, the spinners of our fate have a dark sense of humor."), #matheld
  ("npc9_turn_against", "I will not accept fault for the circumstances which have led us to become enemies. I want you to know that my conscience is clear, although my heart is heavy."), #alayen
  ("npc10_turn_against", "Well, it looks like the tides of fate have led me to make war on my old captain. Maybe things started to go wrong when you became my liege -- I suppose I was never much suited to vassalage. Anyway, here we are now. Maybe, when the world is changed and there are no more masters and servants, or lords and vassals, then we can meet together as friends."), #bunduk
  ("npc11_turn_against", "Great heaven, {laddie/lassie}. So now it looks like you and I are enemies. Didn't I say that life takes us on some very strange turns? Destiny sometimes has a cruel sense of humor -- I'll say that much."), #katrin
  ("npc12_turn_against", "So, it seems we must fight. I would have you know, {sir/my lady}, that I have not betrayed you. I had never served you as a man, but served the principles which I believed you upheld. As you no longer uphold them, I must do my best to thwart you. But I bear you no ill will, and I hope that we can meet again some day as friends"), #jeremus
  ("npc13_turn_against", "It is sad to meet you as my enemy, Captain -- but on the other hand, to meet such a titan of the battlefield as yourself in combat is a rare privilege. Truly, the news of our contest today shall keep the bards and poets of Calradia in wine and silver for months to come, do you think?"), #nizar
  ("npc14_turn_against", "Well, {playername}. We meet as enemies. I confess that I have mixed feelings. It grieves me to make war on you, but if we meet in battle and I prevail, I will have defeated the worthiest foe in all Calradia, and I will know that my mastery of the military art is complete!"), #lazalit
  ("npc15_turn_against", "Ah... I have not been looking forward to this day. I just want to say that in my sight, if you'd kept your faith in me, things would never have come to this. But no doubt you see it differently."), #artimenner
  ("npc16_turn_against", "Hello, Captain! So, I guess we're enemies! One small word of warning if we end up fighting each other -- once the rage of battle hits me, I can't always account for my actions. Just know that whatever I do, it's not personal. Maybe if we both walk away from this, we can meet once more as friends?"), #klethi

#NPC companion changes end





#Troop Commentaries begin
#Tags for comments are = allied/enemy, friendly/unfriendly, and then those related to specific reputations
#Also, there are four other tags which refer to groups of two or more reputations (spiteful, benevolent, chivalrous, and coldblooded)
#The game will select the first comment in each block which meets all the tag requirements

#Beginning of game comments
("comment_intro_liege_affiliated", "I am told that you are pledged to one of the pretenders who disputes my claim to the crown of Calradia. But we may still talk."),
##diplomacy start+ (documentation only)
#NOTE:
#  The comment_* strings below are used with script_lord_comment_to_s43
#  Some of the suffixes differ from the ones used in the personality codes.  The equivalencies are:
#     liege       = lrep_none
#     martial     = lrep_martial
#     badtempered = lrep_quarrelsome
#     pitiless    = lrep_selfrighteous
#     cunning     = lrep_cunning
#     sadistic    = lrep_debauched
#     goodnatured = lrep_goodnatured
#     upstanding  = lrep_upstanding
##diplomacy end+ (documentation only)
("comment_intro_famous_liege", "Your fame runs before you! Perhaps it is time that you sought a liege worthy of your valor."),
("comment_intro_famous_martial", "Your fame runs before you! Perhaps we shall test each other's valor in a tournament, or on the battlefield!"),
("comment_intro_famous_badtempered", "I've heard of you. Well, I'm not one for bandying words, so if you have anything to say, out with it."),
("comment_intro_famous_pitiless", "I know your name. It strikes fear in men's hearts. That is good. Perhaps we should speak together, some time."),
("comment_intro_famous_cunning", "Ah, yes. At last we meet. You sound like a good {man/woman} to know. Let us speak together, from time to time."),
("comment_intro_famous_sadistic", "I know your name -- and from what I hear, I'll warrant that many a grieving widow knows too. But that is no concern of mine."),
("comment_intro_famous_goodnatured", "I've heard of you! It's very good to finally make your acquaintance."),
("comment_intro_famous_upstanding", "I know your name. They say you are a most valiant warrior. I can only hope that your honour and mercy matches your valor."),

("comment_intro_noble_liege", "I see that you carry a {nobleman's/noble's} banner, although I do not recognize the device. Know that I am always looking for good {men/warriors} to fight for me, once they prove themselves to be worthy of my trust."),
("comment_intro_noble_martial", "I see that you carry a nobleman's banner, but I do not recognize the device. No matter -- a brave {man's/warrior's} home is all the world, or so they say!"),
("comment_intro_noble_badtempered", "I don't recognize the device on your banner. No doubt another foreigner come to our lands, as if we didn't have so many here already."),
("comment_intro_noble_pitiless", "I see that you carry a nobleman's banner, but I do not recognize the device. Another vulture come to grow fat on the leftovers of war, no doubt!"),
("comment_intro_noble_cunning", "I see that you carry a nobleman's banner, but I do not recognize the device. Still, it is always worthwhile to make the acquaintance of {men/women} who may one day prove themselves to be great warriors."),
("comment_intro_noble_sadistic", "I see that you carry a nobleman's banner, but I do not recognize the device. Perhaps you are the bastard {son/daughter} of a puffed-up cattle thief? Or perhaps you stole it?"),
("comment_intro_noble_goodnatured", "I see that you carry a nobleman's banner, but I do not recognize the device. Forgive my ignorance, {sir/my lady}! It is good to make your acquaintance."),
("comment_intro_noble_upstanding", "I see that you carry a nobleman's banner, but I do not recognize the device. No doubt you have come to Calradia in search of wealth and glory. If this indeed is the case, then I only ask that you show mercy to those poor souls caught in the path of war."),


("comment_intro_common_liege", "You may be of common birth, but know that I am always looking for good men to fight for me, if they can prove themselves to be worthy of my trust."),
("comment_intro_common_martial", "Perhaps you are not of gentle birth, but even a commoner, be {he/she} of sufficient valor, may make something of {himself/herself} some day."),
("comment_intro_common_badtempered", "Speak quickly, if you have anything to say, for I have no time to be bandying words with common soldiers of fortune."),
("comment_intro_common_pitiless", "You have the look of a mercenary, another vulture come to grow fat on the misery of this land."),
("comment_intro_common_cunning", "Well... I have not heard of you, but you have the look of a {man/woman} who might make something of {himself/herself}, some day."),
("comment_intro_common_sadistic", "Normally I cut the throats of impudent commoners who barge into my presence uninvited, but I am in a good mood today."),
("comment_intro_common_goodnatured", "Well, you look like a good enough sort."),
("comment_intro_common_upstanding", "Peace to you, and always remember to temper your valor with mercy, your courage with honour."),


##diplomacy start+
#Change female intros and rejoiners to be prejudiced against whatever sex the player happens to be
#(This will be invisible to the player by default, since ordinarily these are never spoken to
#make players, but it allows a reversal of the convention.  TODO: add documentation of xxx

#famous
##dplmc+ changes to include female-to-male versions
("comment_intro_female_famous_liege", "I have heard much about you. Some {women/men} may fear a {man/woman} who is versed in the art of war, but I for one will not turn away hands that can grip a sword, should their owner be brave and loyal."),
("comment_intro_female_famous_martial", "I have heard much about you. They say that you are the equal of even the bravest of {women/men} in your prowess at arms. Perhaps one day I shall try my valor against yours, either in a tournament or on the battlefield!"),
("comment_intro_female_famous_badtempered", "I've heard of talk of you -- the {man/woman} who knows how to fight like a {woman/man}."),
("comment_intro_female_famous_pitiless", "I know your name. It strikes fear in {women/men}'s hearts. That is good. Perhaps we should speak together, some time."),
("comment_intro_female_famous_cunning", "Ah, yes. At last we meet. You sound like a good {man/woman} to know. Let us speak together, from time to time."),
("comment_intro_female_famous_sadistic", "I know your name -- and from what I hear, I'll warrant that many a grieving widow knows too. But that is no concern of mine."),
("comment_intro_female_famous_goodnatured", "I've heard of you! It's very good to finally make your acquaintance."),
("comment_intro_female_famous_upstanding", "I know your name. They say you are a most valiant warrior. I can only hope that your honour and mercy matches your valor."),


#aristocratic
##(... continuing dplmc+ changes to include female-to-male versions ...)
("comment_intro_female_noble_liege", "It is not often that I meet a {male/woman} who aspires to lead {warriors/men} into battle. But these are dark and troubled times, and I for one will not turn away hands that can grip a sword, should their owner be brave and loyal."),
("comment_intro_female_noble_martial", "I do not recognize the device on your banner, but clearly you are a {boy/lady} of rank. Please consider me your most humble servant."),
("comment_intro_female_noble_badtempered", "I don't recognize the device on that banner. Clearly another foreigner come to our lands, bringing their strange ways."),
("comment_intro_female_noble_pitiless", "I see that you carry a noble's banner, but I do not recognize the device... You should know, {boy/lady}, that in Calradia it is the {women/men} to ride to war, and if you seek to overturn the natural order of things, you will find your fair head stuck on a pike -- like that of any other rebel!"),
("comment_intro_female_noble_cunning", "It is not unheard-of for a {male/woman} to seek {his/her} fortune on the battlefields of Calradia, but neither is it usual. I shall be most interested in your progress."),
("comment_intro_female_noble_sadistic", "You appear to be of noble rank, but I don't recognize your banner. Clearly, another foreigner come to our shores -- no doubt from a land where {women/men} are weak, and the {men/women} ride to war in their place!"),
("comment_intro_female_noble_goodnatured", "I see that you carry a {noblewoman/nobleman}'s banner, but I do not recognize the device. Forgive my ignorance, {dear boy/my lady}! It is good to make your acquaintance."),
("comment_intro_female_noble_upstanding", "It is not every day that we see a {male/woman} caparisoned for war. Please do not take this amiss, {dear boy/my lady}, for you have every right to protect yourself, but I cannot pretend to be fully comfortable with your decision to fight in battle. I would prefer that {males/women} be untouched by these wars, as I believe the {male/female} to be the custodian of what little gentility and tenderness remains to us."),


#admiring
##(... continuing dplmc+ changes to include female-to-male versions ...)
("comment_intro_female_admiring_liege", "It is not often that I meet a {male/woman} who aspires to lead {warriors/men} into battle. But these are dark and troubled times, and I for one will not turn away hands that can grip a sword, should their owner be brave and loyal."),
("comment_intro_female_admiring_martial", "Greetings, {dear boy/my lady}. Although I see from your demeanor that you are not a conventional {boy/maiden}, I hope that you are not averse to a declaration of admiration from me, your most humble servant."),
("comment_intro_female_badtempered_admiring", "Heh. Fancy this -- a {pretty boy/maiden}, all equipped for war. Well, it's a strange sight, but in your case, I can imagine that it might grow on me."),
("comment_intro_female_pitiless_admiring", "It is unusual to see a {male/woman} girt for war. Be careful, {dear boy/my lady} -- it is a harsh world, and it would be a shame to see such beauty marred by a sword-blow."),
#Next line deliberately doesn't switch the gender of daughter in the female-to-male version (the implication is that the amazon wants her warrior daughters to have similar bravery)
("comment_intro_female_cunning_admiring", "Greetings, {dear boy/my lady}. Please do not think it forward, if I say that it is unusual to see a {male/woman} caparisoned for war. I hope that one day I may be the {mother/father} of a daughter possessed of such bravery and spirit."),
("comment_intro_female_sadistic_admiring", "What have we here! A {pretty boy/woman}, caparisoned for war! Well, I dare say that one as fair as you could lend a touch of {delicacy/femininity} even to a mail hauberk."),
("comment_intro_female_admiring_goodnatured", "{Dear boy/My lady}, if you are skilled as arms as you are fair in countenance, then your enemies should indeed fear you!"),
("comment_intro_female_admiring_upstanding", "Greetings, {dear boy/my lady}. Even with the dust of the march upon your clothes and gear, I can see that you are not lacking in the graces of your noble sex."),

#common
##(... continuing dplmc+ changes to include female-to-male versions ...)
("comment_intro_female_common_liege", "It is not often that I meet a {male/woman} who aspires to lead {warriors/men} into battle. But these are dark and troubled times, and I for one will not turn away hands that can grip a sword, should their owner be brave and loyal."),
("comment_intro_female_common_martial", "I must say, {dear boy/my lady} -- do be careful, riding about this dangerous land. If you ever wished to seek a more... em... settled life, I'm sure I could find you a worthy {wife/husband} from among my {warriors/men}."),
("comment_intro_female_common_badtempered", "By the way, {boy/girl} -- does your {mistress/husband} know that you nicked {her/his} weapons and armor? I'll bet you're in for a right old beating when you get home!"),
("comment_intro_female_common_pitiless", "These are fallen times indeed, when even {males/women} turn brigand, to pick the leavings from the wreckage of war."),
("comment_intro_female_common_cunning", "It is not unheard-of for a {male/woman} to seek {his/her} fortune on the battlefields of Calradia, but neither is it usual. I shall be most interested in your progress."),
("comment_intro_female_common_sadistic", "A {male/woman}, caparisoned for war! Well, I suppose that you're {not much less/no more} womanly than most of those in my service who call themselves warriors."),
("comment_intro_female_common_goodnatured", "From the look of you, I suppose you can handle yourself, but do be careful out there, {dear boy/my lady}."),
("comment_intro_female_common_upstanding", "It is not every day that we see a {male/woman} caparisoned for war. Please do not take this amiss, {dear boy/my lady}, for you have every right to protect yourself, but I cannot pretend to be fully comfortable with your decision to fight in battle. I would prefer that {males/women} be untouched by these wars, as I believe the {male/female} to be the custodian of what little gentility and tenderness remains to us."),

#Rejoinder
##(... continuing dplmc+ changes to include female-to-male versions ...)
("rejoinder_intro_female_common_badtempered", "I won my weapons in battle. Would you care to test their edge?"),
("rejoinder_intro_female_noble_sadistic", "Never mind my country. Here in Calradia, it seems, dogs lead {soldiers/men} to war."),
("rejoinder_intro_female_common_sadistic", "And you, {madam/sir}, are no more bestial than my horse."),
("rejoinder_intro_female_noble_pitiless", "I would restore the natural order, so that you no longer speak from your arse."),
("rejoinder_intro_female_common_pitiless", "Indeed, these are fallen times, when brigands call themselves 'Lord'."),

("rejoinder_intro_noble_sadistic", "Maybe now I'll take your banner. And your cattle. And your life."),


("rejoinder_intro_female_pitiless_admiring", "I would be delighted to mar your {pretty face/handsome nose}, {madam/sir}."),
("rejoinder_intro_female_common_upstanding", "Would you like to feel the tenderness of my steel?"),
("rejoinder_intro_female_noble_upstanding", "Would you like to feel the tenderness of my steel?"),
("rejoinder_intro_female_common_martial", "I could find worthier {wives/husbands} than those in a kennel."),
("rejoinder_intro_female_sadistic_admiring", "You could add a touch of humanity to a horse's harness, but just a touch."),
("rejoinder_intro_female_badtempered_admiring", "If you're disturbed by the sight of me, I'd be pleased to put out your eyes."),
##(end dplmc+ changes to include female-to-male versions)
##diplomacy end+

#("comment_defer_fief_to_woman", "Were you a man, I would gladly have granted you land, and counted you as one of my bravest vassals. But you see, this has never before happened in Calradia. We have had women serve in our armies, and sometimes, a woman who is the inheritor of her husband or father will lead her retainers into battle to uphold her family obligation. But to enfief a woman for having proved herself in battle? I, for one, have not heard of this."),

#("comment_defer_fief_to_woman_2", "Do not think that I am slave to tradition, if it comes between me and the crown which is rightully mine. But a monarch also cannot appear weak..."),






#Actions vis-a-vis civilians
  ("comment_you_raided_my_village_enemy_benevolent",    "You have attacked innocent farmers under my protection in the village of {s51}. I will punish you for your misdeeds!"),
  ("comment_you_raided_my_village_enemy_spiteful",      "You have raided my village of {s51}, destroying my property and killing the tenants. I will take my compensation in blood!"),
  ("comment_you_raided_my_village_enemy_coldblooded",   "You have raided my village of {s51}, destroying my property and killing the tenants. I will make you think twice before you disrupt my revenues like that again."),
  ("comment_you_raided_my_village_enemy",               "You have raided my village of {s51}, destroying my property and killing tenants under my protection. You will pay the price for your crime!"),
  ("comment_you_raided_my_village_unfriendly_spiteful", "You have raided my village of {s51}. Do it again and I'll gut you like a fish."),
  ("comment_you_raided_my_village_friendly",            "You have raided my village of {s51}. This will place a grave strain on our friendship."),
  ("comment_you_raided_my_village_default",             "You have raided my village of {s51}. If you continue to behave this way, we may soon come to blows."),

  #SB : remove "stolen from my property", cattles -> cattle
  ("comment_you_stole_cattles_from_my_village_enemy_benevolent",    "I have heard that you have stolen cattle from innocent farmers under my protection in the village of {s51}. I will punish you for your misdeeds!"),
  ("comment_you_stole_cattles_from_my_village_enemy_spiteful",      "I have heard that you have stolen cattle from my villagers living at {s51}. You will pay results of this dishonorable act!"),
  ("comment_you_stole_cattles_from_my_village_enemy_coldblooded",   "I have heard that you have stolen cattle from my villagers living at {s51}. I will make you think twice before you disrupt my revenues like that again."),
  ("comment_you_stole_cattles_from_my_village_enemy",               "I have heard that you have stolen cattle from my villagers living at {s51}. You will pay results of this dishonorable act!"),
  ("comment_you_stole_cattles_from_my_village_unfriendly_spiteful", "I have heard that you have stolen cattle from my villagers living at {s51}. Do it again and I'll gut you like a fish."),
  ("comment_you_stole_cattles_from_my_village_friendly",            "I have heard that you have stolen cattle from my villagers living at {s51}. This will place a grave strain on our friendship."),
  ("comment_you_stole_cattles_from_my_village_default",             "I have heard that you have stolen cattle from my villagers living at {s51}. If you continue to behave this way, we may soon come to blows."),

  ("comment_you_robbed_my_village_enemy_coldblooded", "You have robbed my tenants in the village of {s51}. I take that as a personal insult."),
  ("comment_you_robbed_my_village_enemy",             "You have robbed innocent farmers under my protection in the village of {s51}. I will punish you for your misdeeds!"),
  ("comment_you_robbed_my_village_friendly_spiteful", "I have heard that you pinched some food from my tenants at {s51}. Well, I'll not begrudge you a scrap or two, but keep in mind that I'm the one who must listen to their whining afterward."),
  ("comment_you_robbed_my_village_friendly",          "I have heard that you requisitioned supplies from my tenants at {s51}. I am sure that you would not have done so were you not desperately in need."),
  ("comment_you_robbed_my_village_default",           "You have robbed my tenants in the village of {s51}. If you continue to behave this way, we may soon come to blows."),

  ("comment_you_accosted_my_caravan_enemy",          "You have been accosting caravans under my protection. But your trail of brigandage will soon come to an end."),
  ("comment_you_accosted_my_caravan_default",        "You have been accosting caravans under my protection. This sort of behavior must stop."),

  ("comment_you_helped_villagers_benevolent",                "I heard that you gave charity to my tenants in the village of {s51}. I had been neglectful in my duties as lord and protector, and I appreciate what you have done."),
  ("comment_you_helped_villagers_friendly_cruel",            "I heard that you gave charity to my tenants in the village of {s51}. I appreciate that you meant well, but I'd rather you not undercut my authority like that."),
  ("comment_you_helped_villagers_friendly",                  "I heard that you gave charity to my tenants in the village of {s51}. Times are hard, and I know that you mean well, so I will not object to you providing them with assistance."),
  ("comment_you_helped_villagers_unfriendly_spiteful",       "I heard that you gave charity to my tenants in the village of {s51}. As amusing as it is to see you grubbing for favor among my vassals, I would ask you to mind your own business."),
  ("comment_you_helped_villagers_cruel",                     "I heard that you gave charity to my tenants in the village of {s51}. As the peasants' lord and protector, it is most properly my duty to assist them in times of hardship. You may mean well, but your actions still undercut my authority. I would thank you to leave them alone."),
  ("comment_you_helped_villagers_default",                   "I heard that you gave charity to my tenants in the village of {s51}. Times are hard, and I know that you mean well, but try not to make a habit of it. I am their lord and protector, and I would rather not have them go looking to strangers for assistance."),

#Awarding fief-related events
  ("comment_you_give_castle_in_my_control",                    "You won't regret your decision to give {s51} to me. You can count on me to protect it."),
  #can be added some more here acc. characteristic.

#Combat-related events
  ("comment_you_captured_a_castle_allied_friendly",            "I heard that you have besieged and taken {s51}. That was a great dead, and I am proud to call you my friend!"),
  ("comment_you_captured_a_castle_allied_spiteful",            "I heard that you have besieged and taken {s51}. Good work! Soon, we will have all their fortresses to despoil, their treasuries to ransack, their grieving widows to serve us our wine."),
  ("comment_you_captured_a_castle_allied_unfriendly_spiteful", "I heard that you have besieged and taken {s51}. Well, every dog has his day, or so they say. Enjoy it while you can, until your betters kick you back out in the cold where you belong."),
  ("comment_you_captured_a_castle_allied_unfriendly",          "I heard that you have besieged and taken {s51}. Whatever our differences in the past, I must offer you my congratulations."),
  ("comment_you_captured_a_castle_allied",                     "I heard that you have besieged and taken {s51}. We have them on the run!"),

  ("comment_you_captured_my_castle_enemy_spiteful",            "I hear that you have broken into my home at {s51}. I hope the dungeon is to your liking, as you will be spending much time there in the years to come."),
  ("comment_you_captured_my_castle_enemy_chivalrous",          "You hold {s51}, my rightful fief. I hope you will give me the chance to win it back!"),
  ("comment_you_captured_my_castle_enemy",                     "You have something that belongs to me -- {s51}. I will make you relinquish it."),

###Add some variation to these
  ("comment_we_defeated_a_lord_unfriendly_spiteful",           "I suppose you will want to drink to the memory of our victory over {s54}. Well, save your wine -- it will take more than that to wipe out the stain of your earlier disgraces."),
  ("comment_we_defeated_a_lord_unfriendly",                    "I will not forget how we fought together against {s54}, but I can also not forget the other matters that lie between us."),
  ("comment_we_defeated_a_lord_cruel",                         "That was a great victory over {s54}, wasn't it? We made of his army a feast for the crows!"),
  ("comment_we_defeated_a_lord_quarrelsome",                   "I won't forget how we whipped {s54}? I enjoyed that."),
  ("comment_we_defeated_a_lord_upstanding",                    "I will not forget our victory over {s54}. Let us once again give thanks to heaven, and pray that we not grow too proud."),
  ("comment_we_defeated_a_lord_default",                       "That was a great victory over {s54}, wasn't it? I am honoured to have fought by your side."),

  ("comment_we_fought_in_siege_unfriendly_spiteful",           "I suppose you will want to drink to the memory of our capture of {s51}. Well, save your wine -- it will take more than that to wipe out the stain of your earlier disgraces."),
  ("comment_we_fought_in_siege_unfriendly",                    "I will not forget how we together we stormed {s51}, but I can also not forget the other matters that lie between us."),
  ("comment_we_fought_in_siege_cruel",                         "I won't forget how we broke through the walls of {s51} and put its defenders to the sword. It is a sweet memory."),
  ("comment_we_fought_in_siege_quarrelsome",                   "Remember how the enemy squealed when we came over the walls of {s51}? They had thought they were safe! We wiped the smug smiles of their faces!"),
  ("comment_we_fought_in_siege_upstanding",                    "I will not forget our capture of {s51}. Let us once again give thanks to heaven, and pray that we not grow too proud."),
  ("comment_we_fought_in_siege_default",                       "I will not forget how together we captured {s51}. I am honoured to have fought by your side."),

  ("comment_we_fought_in_major_battle_unfriendly_spiteful",    "I suppose you will want to drink to the memory of our great victory near {s51}. Well, save your wine -- it will take more than that to wipe out the stain of your earlier disgraces."),
  ("comment_we_fought_in_major_battle_unfriendly",             "I will not forget how we fought together in the great battle near {s51}, but I can also not forget the other matters that lie between us."),
  ("comment_we_fought_in_major_battle_cruel",                  "I won't forget the great battle near {s51}, when we broke through the enemy lines and they ran screaming before us. It is a sweet memory."),
  ("comment_we_fought_in_major_battle_quarrelsome",            "That was a fine fight near {s51}, when we made those bastards run!"),
  ("comment_we_fought_in_major_battle_upstanding",             "I will not forget how we fought side by side at the great battle near {s51}. Let us once again give thanks to heaven, and pray that we not grow too proud."),
  ("comment_we_fought_in_major_battle_default",                "I will not forget how we fought side by side at the great battle near {s51}. I am honoured to have fought by your side."),



  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s54.  Making this work required altering script_get_relevant_comment_to_s42
  ("comment_you_defeated_a_lord_allied_liege",                   "So, you crossed swords with that rascal they call {s54}, and emerged victorious. I am very happy to hear that."),
  ("comment_you_defeated_a_lord_allied_unfriendly_spiteful",     "I heard that you fought and defeated {s54}. Every dog has its day, I suppose."),
  ("comment_you_defeated_a_lord_allied_spiteful",                "I heard that you fought and defeated that dog {s54}. Ah, if only I could have heard {reg4?her:him} whimpering for mercy."),
  ("comment_you_defeated_a_lord_allied_unfriendly_chivalrous",   "I heard that you fought and defeated {s54}. I hope that you did not use dishonourable means to do so."),
  ("comment_you_defeated_a_lord_allied",                         "I heard that you fought and defeated {s54}. I wish you joy of your victory."),
  ##diplomacy end+

  ("comment_you_defeated_me_enemy_chivalrous", "I will not begrudge you your victory the last time that we met, but I am anxious for another round!"),
  ("comment_you_defeated_me_enemy_spiteful",   "I have been looking forward to meeting you again. Your tricks will not deceive me a second time, and I will relish hearing your cries for mercy."),
  ("comment_you_defeated_me_enemy",            "When last we met, {playername}, you had the better of me. But I assure you that it will not happen again!"),

  ("comment_I_defeated_you_enemy_spiteful",          "Back for more? Make me fight you again, and I'll feed your bowels to my hounds."),
  ("comment_I_defeated_you_enemy_chivalrous",        "Come to test your valor against me again, {playername}?"),
  ("comment_I_defeated_you_enemy_benevolent",        "So once again you come at me? Will you ever learn?"),
  ("comment_I_defeated_you_enemy_coldblooded",       "You are persistent, but a nuisance."),
  ("comment_I_defeated_you_enemy",                   "How many times must I chastise you before you learn to keep your distance?"),

  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s54.  Making this work required altering script_get_relevant_comment_to_s42
  #Replacing "men" with "warriors" when the enemy leader was female in case it was an all-female band.
  ("comment_we_were_defeated_unfriendly_spiteful",   "Last I saw you, you had been struck down by the {reg4?warriors:men} of {s54}. I blame you for that disaster. What a pity to see that you survived."),
  ("comment_we_were_defeated_unfriendly",            "Last I saw you, you had been struck down by the {reg4?warriors:men} of {s54}. Well, I see that you survived."),
  ("comment_we_were_defeated_cruel",                 "Last I saw you, you had been struck down by the {reg4?warriors:men} of {s54}. Don't worry -- we'll find {reg4?her:him}, and make {reg4?her:him} choke on {reg4?her:her} victory."),
  ("comment_we_were_defeated_default",               "Last I saw you, you had been struck down by the {reg4?warriors:men} of {s54}. It is good to see you alive and well."),
  ##diplomacy end+

  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s54.  Making this work required altering script_get_relevant_comment_to_s42
  ("comment_you_were_defeated_allied_friendly_spiteful",      "I heard that {s54} gave you a hard time. Don't worry, friend -- I'll find {reg4?her:him} for you, and make you a gift of {reg4?her:his} head."),
  ("comment_you_were_defeated_allied_unfriendly_cruel",       "I had heard that {s54} slaughtered your men like sheep. But here you are, alive. Such a disappointment!"),
  ("comment_you_were_defeated_allied_spiteful",               "I heard that {s54} crushed you underfoot like an ant. Hah! Children should not play games made for grown-ups, little {boy/girl}!"),
  ("comment_you_were_defeated_allied_pitiless",               "I heard that {s54} defeated you, and scattered your forces. That is most disappointing..."),
  ("comment_you_were_defeated_allied_unfriendly_upstanding",  "I heard that {s54} defeated you. Perhaps you should consider if you have considered any misdeeds, that might cause heaven to rebuke you in this way."),
  ("comment_you_were_defeated_allied_unfriendly",             "I heard that {s54} defeated you. Look, try not to get too many of our men killed, will you?"),
  ("comment_you_were_defeated_allied",                        "I heard that {s54} defeated you. But take heart -- the tables will soon be turned!"),
  ##diplomacy end+

  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s54.  Making this work required altering script_get_relevant_comment_to_s42
  ("comment_you_helped_my_ally_unfriendly_chivalrous",        "I heard that you saved {s54} from likely defeat. Whatever else I may think of you, I must at least commend you for that."),
  ("comment_you_helped_my_ally_unfriendly",                   "{!}[revelance should be zero, and this message should not appear]"),
  ("comment_you_helped_my_ally_liege",                        "I heard that you saved my vassal {s54} from likely defeat. "),
  ("comment_you_helped_my_ally_unfriendly_spiteful",          "I heard that you rode to the rescue of our poor {s54}. Did you think {reg4?her:him} a damsel in distress? No matter -- it's a common mistake."),
  ("comment_you_helped_my_ally_spiteful",                     "I heard that you saved {s54} from a whipping. You should have let {reg4?her:him} learn {reg4?her:his} lesson, in my opinion."),
  ("comment_you_helped_my_ally_chivalrous",                   "I heard that you got {s54} out of a tight spot. That was a noble deed."),
  ("comment_you_helped_my_ally_default",                   "I heard that you got {s54} out of a tight spot. Good work!"),
  ##diplomacy end+

  ("comment_you_were_defeated_allied_unfriendly",             "I heard that {s54} defeated you. Look, try not to get too many of our men killed, will you?"),
  ("comment_you_were_defeated_allied",                        "I heard that {s54} defeated you. But take heart -- the tables will soon be turned!"),

  ("comment_you_abandoned_us_unfriendly_spiteful",     "You worm! You left us alone to face {s54}, didn't you? I spit at you."),
  ("comment_you_abandoned_us_unfriendly_pitiless",     "Well... You abandoned me in the middle of a battle with {s54}, didn't you? I'll see you buried in a traitor's grave."),
  ("comment_you_abandoned_us_spiteful",                "You disappeared in the middle of that battle with {s54}... I hope you have a good explanation. Did your bowels give out? Were you shaking too hard with fear to hold your weapon?"),
  ("comment_you_abandoned_us_chivalrous",              "What happened? You disappeared in the middle of that battle against {s54}. I can only hope that you were too badly wounded to stand, for I would be ashamed to have gone into battle alongside a coward."),
  ("comment_you_abandoned_us_benefitofdoubt",          "What happened? You disappeared in the middle of that battle against {s54}. I assume that you must have been wounded, but it did look suspicious."),
  ("comment_you_abandoned_us_default",                 "What happened? One moment you were fighting with us against {s54}, the next moment you were nowhere to be found?"),

  ("comment_you_ran_from_me_enemy_spiteful",          "Last time we met, you ran from me like a whipped dog. Have you come back to bark at me again, or to whine for mercy?"),
  ("comment_you_ran_from_me_enemy_chivalrous",        "Last time we met, you fled from me. Learn to stand and fight like a gentleman!"),
  ("comment_you_ran_from_me_enemy_benevolent",        "When I saw you flee the last time that we met, I had hoped that I would not have to fight you again."),
  ("comment_you_ran_from_me_enemy_coldblooded",       "Last time we met, you fled from me. That was a wise decision"),
  ("comment_you_ran_from_me_enemy",                   "You may have been able to escape the last time we crossed paths, but the next time I doubt that you be so lucky."),

  ("comment_you_ran_from_foe_allied_chivalrous",      "They say that you fled from {s54}, leaving your men behind. I pray that this is not true, for such conduct does dishonour to us all."),
  ("comment_you_ran_from_foe_allied_upstanding",      "They say that you fled from {s54}, leaving your men behind. I do not always believe such rumors, and I also know that desperate straits call for desperate measures. But I beg you to take more care of your good name, for men will not fight in our armies if they hear that we abandon them on the field of battle."),
  ("comment_you_ran_from_foe_allied_spiteful",        "By the way, they said that you ran away from {s54} like a quaking little rabbit, leaving your men behind to be butchered. Ha! What a sight that would have been to see!"),


  ("comment_you_defeated_my_friend_enemy_pragmatic",  "You may have bested {s54}, but you cannot defeat us all."),
  ("comment_you_defeated_my_friend_enemy_chivalrous", "I have heard that you defeated {s54}, and ever since have been anxious to cross swords with you."),
  ("comment_you_defeated_my_friend_enemy_spiteful",   "Your fame runs before you, {playername}. {s54} may have fallen for your tricks, but if you fight me, you'll find a me a much more slippery foe."),
  ("comment_you_defeated_my_friend_enemy",            "They say that you have defeated {s54}. But I will be a truer test of your skill at arms."),

  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s54.  Making this work required altering script_get_relevant_comment_to_s42
  ("comment_you_captured_a_lord_allied_friendly_spiteful",   "I heard that you captured {s54}. I hope that you squeezed {reg4?her:him} for every denar."),
  ("comment_you_captured_a_lord_allied_unfriendly_spiteful", "I heard that you captured {s54}. Your coffers must be well-bloated with ransom by now. Such a pity that money cannot transform a low-born cur into a {gentleman/gentlewoman}!"),#also gentleman -> {gentleman/gentlewoman}
  ("comment_you_captured_a_lord_allied_chivalrous",          "I heard that you captured {s54}. Well done. I assume, of course, that {reg4?she:he} has been been treated with the honours due {reg4?her:his} rank."),
  ("comment_you_captured_a_lord_allied",                     "I heard that you captured {s54}. Well done. {reg4?Her:His} ransom must be worth quite something."),
  ##diplomacy end+

  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s54.  Making this work required altering script_get_relevant_comment_to_s42
  ("comment_you_let_go_a_lord_allied_chivalrous",            "I heard that you captured {s54}, but then let {reg4?her:him} go. Such chivalry does a credit to our cause."),
  ("comment_you_let_go_a_lord_allied_upstanding",            "I heard that you captured {s54}, but then let {reg4?her:him} go. Well, that was an honourable course of action, if possibly also a dangerous one."),
  ("comment_you_let_go_a_lord_allied_coldblooded",           "I heard that you captured {s54}, but then let {reg4?her:him} go. That was most chivalrous of you, but chivalry does not win wars."),
  ("comment_you_let_go_a_lord_allied_unfriendly_spiteful",   "I heard that you captured {s54}, but then let {reg4?her:him} go. How very chivalrous of you! No doubt the widows and orphans {reg4?she:he} leaves in {reg4?her:his} wake will want to commend you in person."),
  ("comment_you_let_go_a_lord_allied",                       "I heard that you captured {s54}, but then let {reg4?her:him} go. Well, I will not tell you what to do with your own prisoners."),
  ##diplomacy end+

  ("comment_you_let_me_go_spiteful",                    "When last we met, you had me at your mercy and allowed me to go free. I hope you enjoyed toying with me, like a cat with a mouse, because soon I will have you at my mercy, to slay or humiliate according to my fancy."),
  ("comment_you_let_me_go_enemy_chivalrous",            "When last we met, you had me at your mercy and allowed me to go free. That was most chivalrous of you, and I will not forget. But I also must remember my oath to my liege, and our kingdoms are still at war."),
  ("comment_you_let_me_go_enemy_coldblooded",           "When last we met, you had me at your mercy and allowed me to go free. But we are still enemies, and I cannot promise to repay your mercy in kind."),
  ("comment_you_let_me_go_enemy",                       "When last we met, you had me at your mercy and allowed me to go free. That was kind of you. But we are still at war."),
  ("comment_you_let_me_go_default",                     "When last we met, you had me at your mercy and allowed me to go free. That was kind of you, and I am glad that our kingdoms are no longer at war."),


#Internal faction events
  ("comment_pledged_allegiance_allied_martial_unfriendly",             "I heard that you have pledged allegiance to our lord, {s54}. Pray do not disgrace us by behaving in a cowardly fashion."),
  ("comment_pledged_allegiance_allied_martial",                        "I heard that you have pledged allegiance to our lord, {s54}. I look forward to fighting alongside you against our foes."),
  ("comment_pledged_allegiance_allied_quarrelsome_unfriendly",         "I heard that you have pledged allegiance to our lord, {s54}. Bah. Do yourself a favor, and stay out of my way."),
  ("comment_pledged_allegiance_allied_quarrelsome",                    "I heard that you have pledged allegiance to our lord, {s54}. Fight hard against our foes, respect your betters, and don't cross me, and we'll get along fine."),
  ("comment_pledged_allegiance_allied_selfrighteous_unfriendly",       "I heard that you have pledged allegiance to our lord, {s54}. If I were he, I would not trust you to clean the sculleries."),
  ("comment_pledged_allegiance_allied_selfrighteous",                  "I heard that you have pledged allegiance to our lord, {s54}. Fight bravely and you will be well-rewarded. Betray us, and we shall make of you the kind of example that will not soon be forgotten."),
  ("comment_pledged_allegiance_allied_cunning_unfriendly",             "I heard that you have pledged allegiance to our lord, {s54}. I do not pretend to be happy about his decision, but perhaps it is better to have you inside our tent pissing out, than the other way around."),
  ("comment_pledged_allegiance_allied_cunning",                        "I heard that you have pledged allegiance to our lord, {s54}. That is good. The more skilled fighters we have with us in these troubled times, the better. I shall be watching your progress."),
  ("comment_pledged_allegiance_allied_debauched_unfriendly",           "I heard that you have pledged allegiance to our lord, {s54}. No doubt you will soon betray him, and I will have the pleasure of watching you die a traitor's death."),
  ("comment_pledged_allegiance_allied_debauched",                      "I heard that you have pledged allegiance to our lord, {s54}. Excellent... I am sure that you and I will become very good friends. But remember -- if you betray us, it will be the biggest mistake you will ever make."),
  ("comment_pledged_allegiance_allied_goodnatured_unfriendly",         "I heard that you have pledged allegiance to our lord, {s54}. Well, I can't say that I would have trusted you, but perhaps you deserve the benefit of the doubt."),
  ("comment_pledged_allegiance_allied_goodnatured",                    "I heard that you have pledged allegiance to our lord, {s54}. Good {man/woman}! Our lord is a noble soul, and rewards loyalty and valor with kindness and generosity."),
  ("comment_pledged_allegiance_allied_upstanding_unfriendly",          "I heard that you have pledged allegiance to our lord, {s54}. Alas, from what I know of you I fear that you will disgrace us, but I will be happy if you prove me wrong."),
  ("comment_pledged_allegiance_allied_upstanding",                     "I heard that you have pledged allegiance to our lord, {s54}. Fight against our foes with valor, but also with honour and compassion. A good name is as valuable as a sharp sword or a swift horse in affairs of arms."),


  ("comment_our_king_granted_you_a_fief_allied_friendly_cruel",     "I heard that {s54} granted you {s51} as a fief. Don't forget -- spare the whip and spoil the peasant!"),
  ("comment_our_king_granted_you_a_fief_allied_friendly_cynical",   "I heard that {s54} granted you {s51} as a fief. I am glad to see you prosper -- but be careful. Men are vipers, envious and covetous of their neighbours' wealth. Stay close to me, and I'll watch your back."),

  ("comment_our_king_granted_you_a_fief_allied_friendly",              "I heard that {s54} granted you {s51} as a fief. May your new lands prosper."),
  ("comment_our_king_granted_you_a_fief_allied_unfriendly_upstanding", "I heard that {s54} granted you {s51} as a fief. But keep in mind that pride goes before a fall."),
  ("comment_our_king_granted_you_a_fief_allied_unfriendly_spiteful",   "I heard that {s54} granted you {s51} as a fief. I suspect, however, that fortune is only raising you up so as to humble you even more, when it casts you back into the dung from whence you came."),
  ("comment_our_king_granted_you_a_fief_allied_spiteful",              "I heard that {s54} granted you {s51} as a fief. Let's hope you are indeed deserving of our lord's favor."),

  ("comment_our_king_granted_you_a_fief_allied",                       "I heard that {s54} granted you {s51} as a fief. You seem to be doing very well for yourself."),

  ("comment_you_renounced_your_alliegance_enemy_friendly",             "I heard that you renounced your allegiance to our lord, {s54}. It grieves me that we must now meet on the field of battle."),
  ("comment_you_renounced_your_alliegance_friendly",                   "I heard that you renounced your allegiance to our lord, {s54}. Let us pray that we may not come to blows."),
  ("comment_you_renounced_your_alliegance_unfriendly_spiteful",        "I always had you figured for a traitor to {s54}, and now it seems I was proven right. I hope you are prepared to die a traitor's death!"),
  ("comment_you_renounced_your_alliegance_unfriendly_moralizing",      "I heard that you renounced your allegiance to our lord, {s54}. I am forced to consider you a traitor."),
  ("comment_you_renounced_your_alliegance_enemy",                      "I heard that you renounced your allegiance to our lord, {s54}. Well, it is the way of the world for old comrades to become enemies."),
  ("comment_you_renounced_your_alliegance_default",                    "I heard that you renounced your allegiance to our lord, {s54}. Well, that is your decision, but do not expect me to go easy on you when we meet on the battlefield."),

#player claim throne statements
  ("comment_you_claimed_the_throne_1_player_liege",             "My informants tell me that some people in this realm are speaking of you as the next king. I assume that you will quickly put a stop to such idle and dangerous talk."),
  ("comment_you_claimed_the_throne_2_player_liege",             "My informants tell me that some of your companions have telling the peasants that you have a claim to the throne. I sincerely hope that they have been acting without your orders."),

#new political comments
##diplomacy start+
#Note that the following are not called from the conversation-starting invocation of script_get_relevant_comment_to_s42
##diplomacy end+
  ("comment_lord_intervened_against_me", "It is well known that I had quarreled with {s54}, and {s50} ruled in my rival's favor."),
  ("comment_i_protested_marshall_appointment", "It is well known that I had protested {s54}'s decision to appoint {s51} as marshal."),
  ("comment_i_blamed_defeat", "It is well known that I am dissatisfied with {s54} for the favor shown to {s51}, who led us to defeat against the {s56}."),
  ("comment_i_was_entitled_to_fief", "It is well known that I am disappointed that {s54} received the fief of {s51}, which should have gone to me."),

##diplomacy start+
#Altered to use reg3 for gender of s51, reg4 for gender of s54, and reg65 for gender of speaker
#Note that some of these are not called from the conversation-starting invocation of script_get_relevant_comment_to_s42
  ("comment_i_quarreled_with_troop_over_woman", "It is well known that {s51} paid suit to {s54}, while I was also courting {reg4?her:him}. {reg3?She:He} is unworthy of {reg4?her:his} attentions, and I intend to teach {reg3?her:him} to keep {reg3?her:his} distance from {reg4?her:him}."),

  ("comment_i_quarreled_with_you_over_woman_default", "I hear that you have been paying suit to {s54}. I do not believe that you are worthy of a fair {reg4?lady:lad} such as {reg4?her:him}, and would strongly encourage you to cease pursuing {reg4?her:him}."),

  ("comment_i_quarreled_with_you_over_woman_derisive", "I hear that you have been paying suit to {s54}. Let me tell you something -- I've had my eye on that one ever since I was a {reg65?lass:lad}, and {reg4?she:he} was a {reg4?lass:lad}. {reg4?She:he}'s a high-born {reg4?lady:scion} of this realm, and should not be demeaned by a foreigner's crude attentions. Keep away from {reg4?her:him}, or expect to pay the price!"),
##diplomacy end+

  ("comment_player_suggestion_succeeded", "I followed your suggestion, and profited much by your advice."),
  ("comment_player_suggestion_failed", "I followed your suggestion and met with disaster, and I hold you responsible."),

  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s54.  Making this work required altering script_get_relevant_comment_to_s42
  ("comment_you_enfiefed_a_commoner_hesitant",  "I understand that you have given {s51} to a commoner who calls {reg4?herself:himself} {s54}. Be careful. To learn the art of governance is no easy task, and perhaps it is best that fathers pass it on to their sons. I advise you against tampering with the institution of lordship."),
  ("comment_you_enfiefed_a_commoner_derisive",   "I understand that you have given {s51} to a commoner who calls {reg4?herself:himself} {s54}. Do not the ancients warn us against making royal robes out of the hides of pigs?"),
  ("comment_you_enfiefed_a_commoner_nasty",      "I understand that you have given {s51} to a commoner who has taken the name of {s54}. Have a care! A dog may turn on its master."),
  ##diplomacy end+

  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s50.  Making this work required altering script_get_relevant_comment_to_s42
  #Don't change the order of the following strings!  (Refer to script_get_relevant_comment_to_s42 if you must)
  ("comment_marriage_normal_family",  "Congratulations on your marriage to my {s11} {s50}. You may now consider yourself part of the family!"),
  ("comment_marriage_normal",         "Congratulations on your marriage to {s50}. The news does credit to you both."),
  ("comment_marriage_normal_nasty",   "Well -- I see that you have married {s50}. (reg4?She:He} was always a silly {reg4?girl:boy}, with appalling judgment."),

  ("comment_marriage_elopement_family",  "Well... You somehow persuaded my {s11} {s50} to marry you. I don't know what you did to make {reg4?her:him} accept you, but our family will not forget this humiliation."),
  ("comment_marriage_elopement_liege",   "I hear that you have eloped with {s50}, against {reg4?her:his} family's wishes. I am not pleased. {reg4?Her:His} family are among the great lords of my realm, and I do not like to see them made to look like fools."),
  ##diplomacy end+

  ("comment_you_broke_truce_as_my_vassal",  		"I hear that you have broken my truce by attacking {s55}. Do you know how this makes me look? If you were acting under my orders, I appear dishonorable. If you were not, I look weak. I have half a mind to indict you for treason here and now."),
  ("comment_you_attacked_neutral_as_my_vassal", "I hear that you have attacked subjects of the {s55}. You have given them an excuse to attack me, if they want... We shall see what comes of this. A fine day's work you have done!"),



  ("personality_archetypes",   "liege"),
  ("martial",                  "martial"),
  ("quarrelsome",              "bad-tempered"),
  ("selfrighteous",            "pitiless"),
  ("cunning",                  "cunning"),
  ("debauched",                "sadistic"),
  ("goodnatured",              "good-natured"),
  ("upstanding",               "upstanding"),
  ("roguish",                  "roguish"),
  ("benevolent",               "benevolent"),
  ("mercantile",               "mercantile"),

  ("surrender_demand_default",        "Yield or die!"),
  ("surrender_demand_martial",        "The odds are not in your favor today. You may fight us, but there is also no shame if you yield now."),
  ("surrender_demand_quarrelsome",    "I've got you cornered. Give up, or I'll ride you down like a dog."),
  ("surrender_demand_pitiless",       "You cannot defeat me, and I'll teach you a painful lesson if you try. Yield!"),
  ("surrender_demand_cunning",        "You are outmatched today. Give up -- if not for your own sake, then think of your men!"),
  ("surrender_demand_sadistic",       "Surrender or I'll gut you like a fish!"),
  ("surrender_demand_goodnatured",    "We have the advantage of you. Yield, and you will be well-treated."),
  ("surrender_demand_upstanding",     "You may fight us, but many of your men will be killed, and you will probably lose. Yield, and spare us both the unnecessary bloodshed."),

  ("surrender_offer_default",        "Stop! I yield!"),
  ("surrender_offer_martial",        "Stop! I yield!"),
  ("surrender_offer_quarrelsome",    "Enough! You win today, you dog! Ach, the shame of it!"),
  ("surrender_offer_pitiless",       "I yield! You have won. Cursed be this day!"),
  ("surrender_offer_cunning",        "Stop! I yield to you!"),
  ("surrender_offer_sadistic",       "I give up! I give up! Call back your dogs!"),
  ("surrender_offer_goodnatured",    "I yield! Congratulations on your victory, {sir/madame}!"),
  ("surrender_offer_upstanding",     "I yield! Grant me the honours of war, and do yourself credit!"),


  ("lord_declines_negotiation_offer_default",     "That may be, but I wish to fight with you"),
  ("lord_declines_negotiation_offer_martial",     "That may be, but it is my duty to fight with you"),
  ("lord_declines_negotiation_offer_quarrelsome", "Hah! I want to fight with you"),
  ("lord_declines_negotiation_offer_pitiless",    "Why should I care? I wish to fight with you"),
  ("lord_declines_negotiation_offer_cunning",     "Ah. Unfortunately, you see, I wish to fight with you"),
  ("lord_declines_negotiation_offer_sadistic",    "Still your tongue! You will have need of it shortly, while begging for mercy"),
  ("lord_declines_negotiation_offer_goodnatured", "I'm sorry -- I can't just let you ride away. No hard feelings?"),
  ("lord_declines_negotiation_offer_upstanding",  "That may be, but my duty to my liege requires me to fight with you"),


  ("prisoner_released_default",       "You have my gratitude, {sir/madame}. I shall not forget your kindness."),
  ("prisoner_released_martial",       "You are indeed a {man/woman} of honour, {sir/madame}. I shall not forget this!"),
  ("prisoner_released_quarrelsome",   "I'm free? Well... Good bye, then."),
  ("prisoner_released_pitiless",      "Thank you. When you are finally defeated, I will request for your death to be swift and merciful. Unless, that is, you care to join us... Good bye, for now."),
  ("prisoner_released_cunning",       "Am I? You are a good {man/woman}. I will try to find a way to repay you."),
  ("prisoner_released_sadistic",      "Am I? So refined is your cruelty, that you would rather see me free and humiliated, than in chains. Enjoy your triumph!"),
  ("prisoner_released_goodnatured",   "You are indeed a {man/woman} of honour, {sir/madame}. I shall not forget this!"),
  ("prisoner_released_upstanding",    "You are indeed a {man/woman} of honour, {sir/madame}. I shall not forget this!"),

#Post 0907 changes begin
  ("enemy_meet_default",              "Who are you, that comes in arms against me?"),
  ("enemy_meet_martial",              "What is your name, {sir/madame}? If we come to blows, I would know whom I fight."),
  ("enemy_meet_quarrelsome",          "Who the hell are you?"),
  ("enemy_meet_pitiless",             "Who are you? Speak, so that I may know whom I slay."),
  ("enemy_meet_cunning",              "Tell me your name. It is always good to know your enemy."),
  ("enemy_meet_sadistic",             "Who are you? Speak quick, before I cut your tongue out."),
  ("enemy_meet_goodnatured",          "What is your name, {sir/madame}? If we come to blows, I would know whom I fight."),
  ("enemy_meet_upstanding",           "Who are you, who would come in arms to dispute our righteous cause?"),

  ("battle_won_default",              "You have proven yourself a most valued ally, today."),
  ("battle_won_martial",              "There is no greater fortune than the chance to show one's valor on the field of arms!"),
  ("battle_won_quarrelsome",          "Hah! We showed those bastards a thing or two, there, didn't we?"),
  ("battle_won_pitiless",             "Together, we will make the foe learn to fear our names, and to quail at our coming!"),
  ("battle_won_cunning",              "Now, we must be sure to press our advantage, so that the blood shed today is not wasted."),
  ("battle_won_sadistic",             "Now let us strip their dead and leave them for the crows, so that all will know the fate of those who come against us."),
  ("battle_won_goodnatured",          "That was a good scrap! No joy like the joy of victory, eh?"),
  ("battle_won_upstanding",           "Now, let us give thanks to the heavens for our victory, and mourn the many fine men who have fallen today."),

  ("battle_won_grudging_default",     "You helped turn the tide on the field, today. Whatever I may think of you, I cannot fault you for your valor."),
  ("battle_won_grudging_martial",     "{playername} -- you have shown yourself a worthy {man/woman} today, whatever your misdeeds in the past."),
  ("battle_won_grudging_quarrelsome", "Hmf. Yours is not a face which I normally like to see, but I suppose today I should thank you for your help."),
  ("battle_won_grudging_pitiless",    "Your help was most valuable today. I would not imagine that you came to help me out of kindness, but I nonetheless thank you."),
  ("battle_won_grudging_cunning",     "It would be unwise of me not to thank you for coming to help me in my hour of need. So... You have my gratitude."),
  ("battle_won_grudging_sadistic",    "Well! How touching! {playername} has come to rescue me."),
  ("battle_won_grudging_goodnatured", "{playername}! I can't say that we've always gotten along in the past, but you fought well today. My thanks to you!"),
  ("battle_won_grudging_upstanding",  "Perhaps I was wrong about you. Your arrival was most timely. You have my gratitude."),

  ("battle_won_unfriendly_default",         "So you're here. Well, better late than never, I suppose."),
  ("battle_won_unfriendly_martial",         "We have hard harsh words in the past, but for now let us simply enjoy our victory."),
  ("battle_won_unfriendly_quarrelsome",     "If you're standing there waiting for thanks, you can keep waiting. Your help wasn't really needed, but I guess you had nothing better to do, right?"),
  ("battle_won_unfriendly_pitiless",        "You have come here, like a jackal to a lion's kill. Very well then, help yourself to the spoils. I shall not stop you."),
  ("battle_won_unfriendly_cunning",         "{playername}... Well, I suppose your arrival didn't hurt, although I won't pretend that I'm happy to see you."),
  ("battle_won_unfriendly_sadistic",        "Back off, carrion fowl! This was my victory, however hard you try to steal the glory for yourself."),
  ("battle_won_unfriendly_goodnatured",     "Oh, it's you. Well, I suppose I should thank you for your help."),
  ("battle_won_unfriendly_upstanding",      "Thank you for coming to my support. Now I will be off, before I say something that I regret."),

  ("troop_train_request_default",               "I need someone like you to knock them into shape."),
  ("troop_train_request_martial",               "They need someone to show them the meaning of valor."),
  ("troop_train_request_quarrelsome",           "Fat lazy bastards. They make me puke."),
  ("troop_train_request_pitiless",              "They are more afraid of the enemy than they are of me, and this will not do."),
  ("troop_train_request_cunning",               "But men, like swords, are tempered and hardened by fire."),
  ("troop_train_request_sadistic",              "They need someone with steel in his back to flog some courage into them, or kill them trying."),
  ("troop_train_request_goodnatured",           "They're good enough lads, but I am afraid that they are not quite ready for a battle just yet."),
  ("troop_train_request_upstanding",            "It would be tantamount to murder for me to lead them into combat in their current state."),

  ("unprovoked_attack_default",               "What? Why do you attack us? Speak, you rascal!"),
  ("unprovoked_attack_martial",               "I have no objection to a trial of arms, but I would ask you for what reason you attack us?"),
  ("unprovoked_attack_quarrelsome",           "You're making a big mistake, {boy/girl}. What do you think you're doing?"),
  ("unprovoked_attack_pitiless",              "Indeed? If you really want to die today, I'd be more than happy to oblige you, but I am curious as to what you hope to accomplish."),
  ("unprovoked_attack_cunning",               "Really? I think that you are acting most unwisely. What do you hope to gain by this?"),
  ("unprovoked_attack_sadistic",              "What's this? Do you enjoy having your eyes put out?"),
  ("unprovoked_attack_goodnatured",           "Why do you do this? We've got no quarrel, {sir/madame}."),
  ("unprovoked_attack_upstanding",            "I consider this an unprovoked assault, and will protest to your king. Why do you do this?"),

  ("unnecessary_attack_default",               "I will not hesitate to cut you down if pressed, but I will offer you the chance to ride away from this."),
  ("unnecessary_attack_martial",               "I am eager to take you up on your challenge, {sir/madame}, although I will give you a minute to reconsider."),
  ("unnecessary_attack_quarrelsome",           "Bah! I'm in no mood for this nonsense today. Get out of my way."),
  ("unnecessary_attack_pitiless",              "I am in a merciful mood today. I will pretend that I did not hear you."),
  ("unnecessary_attack_cunning",               "I don't see what you have to gain by making an enemy of me. Maybe you should just ride away."),
  ("unnecessary_attack_sadistic",              "I have no time to waste on a worm like you. Get out of my way."),
  ("unnecessary_attack_goodnatured",           "I don't see what you have to gain by picking a fight, {sir/madame}. You can still ride away."),
  ("unnecessary_attack_upstanding",            "If a fight is what you wish, {sir/madame}, then you will have one, but I will yet offer you the chance to back down."),

  ("lord_challenged_default",                   "As you wish. Prepare to die!"),
  ("lord_challenged_martial",                   "So be it. Defend yourself!"),
  ("lord_challenged_quarrelsome",               "You impudent whelp! I'll crush you!"),
  ("lord_challenged_pitiless",                  "If you so badly wish to die, then I have no choice but to oblige you."),
  ("lord_challenged_cunning",                   "Well, if you leave me no choice..."),
  ("lord_challenged_sadistic",                  "You heap of filth! I'll make you wish you'd never been born."),
  ("lord_challenged_goodnatured",               "Very well. I had hoped that we might avoid coming to blows, but I see that have no choice."),
  ("lord_challenged_upstanding",                "So be it. It saddens me that you cannot be made to see reason."),

  ("lord_mission_failed_default",               "Well, I am disappointed, but I am sure that you will have many chances to redeem yourself."),
  ("lord_mission_failed_martial",               "There is no honour in failing a quest which you endeavoured to take, but I will accept your word on it."),
  ("lord_mission_failed_quarrelsome",           "You failed? Bah. I should have expected as much from the likes of you."),
  ("lord_mission_failed_pitiless",              "You failed? Well. You disappoint me. That is a most unwise thing to do."),
  ("lord_mission_failed_cunning",               "Well, I am disappointed, but no one can guarantee that the winds of fortune will always blow their way."),
  ("lord_mission_failed_sadistic",              "Indeed? Those who fail me do not always live to regret it."),
  ("lord_mission_failed_goodnatured",           "Oh well. It was a long shot, anyway. Thank you for making an effort."),
  ("lord_mission_failed_upstanding",            "Very well. I am sure that you gave it your best effort."),

  ("lord_follow_refusal_default",       "Follow you? You forget your station, {sir/madame}."),
  ("lord_follow_refusal_martial",       "Perhaps if you one day prove yourself a valorous and honourable warrior, then I would follow you. But not today."),
  ("lord_follow_refusal_quarrelsome",   "Follow someone like you? I don't think so."),
  ("lord_follow_refusal_pitiless",      "Lords like me do not follow people like you, {sir/madame}."),
  ("lord_follow_refusal_cunning",       "First show me that you are the type of {man/woman} who will not lead me into disaster, and then perhaps I will follow you."),
  ("lord_follow_refusal_sadistic",      "I think not! Rather, you should follow me, as a whipped cur follows {his/her} master."),
  ("lord_follow_refusal_goodnatured",   "Um, I am a bit pressed with errands right now. Perhaps at a later date."),
  ("lord_follow_refusal_upstanding",    "First show me that you are worthy to lead, and then perhaps I will follow."),



  ("lord_insult_default",               "base varlot"),
  ("lord_insult_martial",               "dishonourable knave"),
  ("lord_insult_quarrelsome",           "filth-swilling bastard"),
  ("lord_insult_pitiless",              "low-born worm"),
  ("lord_insult_cunning",               "careless oaf"),
  ("lord_insult_sadistic",              "sniveling cur"),
  ("lord_insult_goodnatured",           "unpleasant fellow"),
  ("lord_insult_upstanding",            "disgraceful scoundrel"),


  ("lord_derogatory_default",               "base and vile"),
  ("lord_derogatory_martial",               "bullheaded"),
  ("lord_derogatory_quarrelsome",           "quarrelsome and divisive"),
  ("lord_derogatory_pitiless",              "cruel, tyrannical"),
  ("lord_derogatory_cunning",               "unscrupulous and manipulative"),
  ("lord_derogatory_sadistic",              "vile and dishonorable"),
  ("lord_derogatory_goodnatured",           "hopelessly naive"),
  ("lord_derogatory_upstanding",            "stiffnecked and sanctimonious"),

  ("lord_derogatory_result",                "bring us to ruin"),
  ("lord_derogatory_martial_action",        "attack the enemy without thought or plan, and throw away the lives of your men"),
  ("lord_derogatory_quarrelsome_action",    "pick fights with other lords, leaving us divided and weak"),
  ("lord_derogatory_pitiles_action",        "alienate the commons, provoking revolt and mutiny"),
  ("lord_derogatory_cunning_action",        "cut a deal with the enemy behind our back"),
  ("lord_derogatory_sadistic_action",       "bring shame upon our cause and our realm"),
  ("lord_derogatory_goodnatured_action",    "take pity on our enemies, rather than fight them"),
  ("lord_derogatory_upstanding_action",     "place your own exaggerated sense of honor above the needs of the realm"),



  #SB : gender strings - reg4 as current liege, reg3 as proposed liege
  ("rebellion_dilemma_default",                 "{!}[liege]"),
  ("rebellion_dilemma_martial",                 "{s45} was clearly wronged. Although I gave an oath to {s46}, it does not bind me to support {reg4?her:him} if {reg4?she:he} usurped the throne illegally."),
  ("rebellion_dilemma_quarrelsome",             "Hmm. {s46} has never given me my due, so I don't figure I owe him much. However, maybe {s45} will be no better, and {s46} has at least shown {reg4?her:him}self."),
  ("rebellion_dilemma_pitiless",                "Hmm. {s45} says {reg3?she:he} is the rightful heir to the throne. That is good -- it absolves me of my oath to {s46}. But still I must weight my decision carefully."),
  ("rebellion_dilemma_cunning",                 "Hmm. I gave an oath of homage to {s46}, yet the powerful are not bound by their oaths as our ordinary people. Our duty is to our own ability to rule, to impose order and prevent the war of all against all."),
  ("rebellion_dilemma_sadistic",                "Hmm. In this vile world, a wise {reg65?woman:man} must think of {reg65?her:him}self, for no one else will. So -- what's in it for me?"),
  ("rebellion_dilemma_goodnatured",             "I do not know what to say. I gave an oath to {s46} as the lawful ruler, but if he is not the lawful ruler, I don't know if I am still bound."),
  ("rebellion_dilemma_upstanding",              "This is troublesome. It is a grave thing to declare my homage to {s46} to be null and void, and dissolve the bonds which keep our land from sinking into anarchy. Yet I am also pledged to support the legitimacy of the succession, and {s45} also has a valid claim to the throne."),

  ("rebellion_dilemma_2_default",               "{!}[liege]"),
  ("rebellion_dilemma_2_martial",               "On the other hand, {s46} has led us in war and peace, and I am loathe to renounce my allegiance."),
  ("rebellion_dilemma_2_quarrelsome",           "So tell me, why should I turn my back on the {reg4?bitch:bastard} I know, in favor of {reg3?a woman:the bastard} I don't know?"),
  ("rebellion_dilemma_2_pitiless",              "It is a most perilous position to be in, to be asked whom I would make {reg3?ruler:king} of this land. Yet it is also a time of opportunity, for me to reap the rewards that have always been my due!"),
  ("rebellion_dilemma_2_cunning",               "{s46} has been challenged, and thus {reg4?she:he} will never be able to rule as strongly as one whose claim has never been questioned. Yet if {s45} takes the throne by force, {reg3?she:he} will not be as strong as one who succeeded peacefully."),
  ("rebellion_dilemma_2_sadistic",              "Perhaps if I join {s45} while {reg3?she:he} is still weak {reg3?she:he} will enrich me, but perhaps if I bring {s46} your head {reg4?she:he} will give me an even greater reward."),
  ("rebellion_dilemma_2_goodnatured",           "{s46} has always treated me decently, yet it's true that {reg4?she:he} did wrong to {s45}. I hesitate to renounce my homage to {s46}, yet I also don't think it's right to support injustice."),
  ("rebellion_dilemma_2_upstanding",            "I feel that I must do whatever is best for the realm, to avoid it being laid waste by civil war and ravaged by its enemies."),


  ("political_philosophy_default",               "{!}[liege]"),
  ("political_philosophy_martial",               "My sword is at the disposal of my rightful liege, so long as he upholds his duty to me."),
  ("political_philosophy_quarrelsome",           "Bah. They're all a bunch of bastards. I try to make sure that the ones who wrong me learn to regret it."),
  ("political_philosophy_pitiless",              "Men will always try to cheat others of their rightful due. In this faithless world, each must remain vigilant of his own rights."),
  ("political_philosophy_cunning",               "Well, it's a harsh world, and it is our lot to face harsh choices. Sometimes one must serve a tyrant to keep the peace, but sometimes a bit of rebellion keeps the kings honest. Circumstance is all."),
  ("political_philosophy_sadistic",              "My philosophy is simple: it is better to be the wolf than the lamb."),
  ("political_philosophy_goodnatured",           "Well, you should keep faith with your promises, and not do injustice to others. Sometimes it's hard to balance those. Stick with people you trust, I think, and it's hard to go far wrong."),
  ("political_philosophy_upstanding",            "Kingship and lordship have been instituted to keep the peace and prevent the war of all against all, yet that must not blind us to the possibility of injustice."),
  ("political_philosophy_roguish",               "Hmm.. I guess I'm thinking that it's good to be a lord."),
  ("political_philosophy_benefactor",            "A good ruler makes sure all are treated justly. Personally, I intend to use my authority to better the lot of those who live in my demesne."),
  ("political_philosophy_custodian",             "A good ruler creates the proper conditions for people to prosper. Personally, I intend to use my wealth to create more wealth, for myself and for the common benefit."),



  ("rebellion_prior_argument_very_favorable",   "I have already heard some arguments for supporting your candidate for the throne, and I tend to agree with them."),
  ("rebellion_prior_argument_favorable",        "I have already heard some arguments for supporting your candidate for the throne, and I tend to agree with them."),
  ("rebellion_prior_argument_unfavorable",      "I have already heard some arguments for supporting your candidate for the throne, but I do not find them convincing."),
  ("rebellion_prior_argument_very_unfavorable", "I have already heard some arguments for supporting your candidate for the throne, but I disagree with most of them."),

  ("rebellion_rival_default",                   "{!}[liege]"),
  ("rebellion_rival_martial",                   "{s49} your ally {s44} once questioned my honour and my bravery. It's not often I get the chance to face him in battle, and make him retract his statement."),
  ("rebellion_rival_quarrelsome",               "{s49} you're working with {s44}. He's a crafty weasel, and I don't trust him one bit."),
  ("rebellion_rival_pitiless",                  "{s49} you seem to have enlisted the support of {s44} -- who is soft, and weak, and not fit to govern a fief, and whom I have always detested."),
  ("rebellion_rival_cunning",                   "{s49} {s44}, who has already joined you, is headstrong and quarrelsome, and a bit of liability."),
  ("rebellion_rival_sadistic",                  "{s49} I have no desire to fight alongside your ally {s44}, who puts on such a nauseating display of virtue."),
  ("rebellion_rival_goodnatured",               "{s49} I'd be reluctant to be on the same side as {s44}, who has quite a reputation for cruelty."),
  ("rebellion_rival_upstanding",                "{s49} your ally {s44} is in my opinion a dangerous, unreliable, and highly unprincipled man."),

  ("rebellion_argument_favorable",              "I respect your line of argument"),
  ("rebellion_argument_neutral",                "I find your line of argument only moderately compelling"),
  ("rebellion_argument_unfavorable",            "I do not find your line of argument compelling"),

  ("rebellion_persuasion_favorable",            "you state your case eloquently"),
  ("rebellion_persuasion_neutral",              "you make a reasonable case"),
  ("rebellion_persuasion_unfavorable",          "you make an unconvincing case"),

  ("rebellion_relation_very_favorable",         "I have the greatest respect for you personally."),
  ("rebellion_relation_favorable",              "I know and respect you personally."),
  ("rebellion_relation_neutral",                "I do not know you as well as I might like."),
  ("rebellion_relation_unfavorable",            "I do not trust you."),

  ("and_comma_3", "Furthermore, "),
  ("but_comma_3", "However,"),

  ("and_comma_1", ", and "),
  ("but_comma_1", ", but "),

  ("and_comma_2", ". Moreover, "),
  ("but_comma_2", ". Nonetheless, "),

  ("rebellion_agree_default",               "Very well -- I am ready to pledge myself to {s45} as my {reg3?queen:king}."),
  ("rebellion_agree_martial",               "I have decided. I will back {s45} as the rightful heir."),
  ("rebellion_agree_quarrelsome",           "Ahh, I've thought long enough. I never did like {s46} much anyway. Let's go take his throne away from {reg4?her:him}."),
  ("rebellion_agree_pitiless",              "You are fortunate. I have decided to join your cause. Pray do not give me cause to regret this decision."),
  ("rebellion_agree_cunning",               "This is a most dangerous decision, but after careful consideration, I have decided that I will join you. Let's hope it is for the best."),
  ("rebellion_agree_sadistic",              "Well then. I will back {reg5?you:your {reg3?woman:man} {s45}}. But you'd best make sure that {reg5?I'm rewarded:{reg3?she:he} rewards me} well!"),
  ("rebellion_agree_goodnatured",           "All right. I think {reg5?you:your {reg3?woman:man}} will be a good ruler. I'll be part of your cause."),
  #SB : remove "so be it" since it's used in subsequent strings to avoid awkwardness
  ("rebellion_agree_upstanding",            "May the Heavens forgive me if I do wrong. My first duty is to this realm, and to save it from lawlessness I will back {s45} and renounce my homage to {s46}."),


  #SB : fix some identifiers
  ("rebellion_refuse_default",              "{!}[liege]"),
  ("rebellion_refuse_martial",              "I am sorry. {s45} has a good claim, but it's not enough for me to turn my back on {s46}. I will remain loyal to my liege."),
  ("rebellion_refuse_quarrelsome",          "Nah. Your whelp {s45} doesn't have what it takes to rule this realm. I'm sticking with {s46}."),
  ("rebellion_refuse_pitiless",              "No. I will not join your rebellion. I count it little more than the tantrum of a child, denied a bauble which {reg3?she:he} thinks should be {reg3?hers:his}. I will stick with {s46}, whose ability to rule is well-tested."),
  ("rebellion_refuse_cunning",               "I am sorry. You do not give me reason for confidence that you will win. Many will die, but I do not wish to be among them. I will continue to back {s46}."),
  ("rebellion_refuse_sadistic",              "No. I won't play your little game. You grasp at a crown, but I think instead you'll get a quick trip to the scaffold, and I'll be there by {s46}'s side to watch the headsman's axe drop."),
  ("rebellion_refuse_goodnatured",           "I am sorry. I don't feel right turning my back on {s46}. No hard feelings when me meet on the battlefield."),
  ("rebellion_refuse_upstanding",            "I am sorry. {s45}'s claim is not strong enough for me to inflict the curse of civil disorder on the poor wretches of this land. I will continue to back {s46}. May the Heavens forgive me if I do wrong."),

  ("talk_later_default",                    "{!}[liege]"),
  ("talk_later_martial",                    "Now is not the time to talk politics! I am here today with my fellow lords, armed for battle. You'd better prepare to fight."),
  ("talk_later_quarrelsome",                "Do you expect me to discuss betraying my liege with you, while we are surrounded by his army? What do you take me for, a bloody idiot?"),
  ("talk_later_pitiless",                   "Still your tongue! Whatever I have to say on this matter, I will not say it here and now, while we are in the midst of our army."),
  ("talk_later_cunning",                    "This is hardly the time or the place for such a discussion. Perhaps we can discuss it at a later time and a different place, but for now we're still foes."),
  ("talk_later_sadistic",                   "You should have your mouth sewn shut! Can you imagine what would happen if the other vassals see me talking to you of treason?"),
  ("talk_later_goodnatured",                "So you wish to discuss your rebellion with me? Try that again when we aren't surrounded by my liege's army, and I will hear what you have to say."),
  ("talk_later_upstanding",                 "Whatever my thoughts on the legitimacy of the succession, I am not about to discuss them here and now. If we meet again when we can talk in privacy, I will hear what you have to say on the matter. But for now, consider me your enemy."),

  ("npc_claim_throne_liege",                    "{!}[placeholder - i am already king]"),
  ("npc_claim_throne_liege_martial",            "{!}[it is my right by birth]."),
  ("npc_claim_throne_liege_quarrelsome",        "{!}[in this life, you take power when you can get it]"),
  ("npc_claim_throne_liege_pitiless",           "{!}[it is my right by birth]."),
  ("npc_claim_throne_liege_cunning",            "{!}[i suppose there comes a time in a man's life when you should grasp at a crown, as you'll always regret not doing it]."),
  ("npc_claim_throne_liege_sadistic",           "{!}[i will show those who despise me]."),
  ("npc_claim_throne_liege_goodnatured",        "{!}[if you really think that i have the best claim]."),
  ("npc_claim_throne_liege_upstanding",         "{!}[i could do much good]."),
#


##diplomacy start+ Change the next line
#  ("gossip_about_character_default",        "They say that {s6} doesn't possess any interesting character traits."),
  ("gossip_about_character_default",        "There aren't many recent rumors about {s6}'s personal life."),
##diplomacy end+
  ("gossip_about_character_martial",        "They say that {s6} loves nothing more than war."),
  ##diplomacy start+ make pronouns gender-correct (reg4)
  ("gossip_about_character_quarrelsome",    "They say that {s6} almost came to blows with another lord lately, because the man made a joke about {reg4?her:his} nose."),
  ("gossip_about_character_selfrighteous",  "I heard that {s6} had a squire executed because the unfortunate man killed a deer in {reg4?her:his} forest."),
  ("gossip_about_character_cunning",        "They say that {s6} is a cunning opponent."),
  ("gossip_about_character_sadistic",       "They say that {s6} likes to torture {reg4?her:his} enemies. I wouldn't want to get on the bad side of that {reg4?woman:man}."),
  ("gossip_about_character_goodnatured",    "They say that {s6} is a good {reg4?woman:man} and treats people living in {reg4?her:his} lands decently. That is more than what can be said for most of the nobles."),
  ("gossip_about_character_upstanding",     "People say that it is good to be in the service of {s6}. {reg4?She:He} is good to {reg4?her:his} followers, and rewards them if they work well."),
  ##diplomacy end+
  ("latest_rumor",        "The latest rumor you heard about {s6} was:"),





#steve lord recruitment changes begin
  ("changed_my_mind_default",                   "{!}[liege]"),
  ("changed_my_mind_martial",                   "However, your stirring words make me reconsider my position."),
  ("changed_my_mind_quarrelsome",               "But I think you've talked me into it anyway, you bastard. I'm still listening"),
  ("changed_my_mind_pitiless",                  "But when you plea like that, I will deign to reconsider."),
  ("changed_my_mind_cunning",                   "But you know, you're a well-spoken bastard. That impresses me. I'm still listening."),
  ("changed_my_mind_sadistic",                  "But as your silver tongue sings so pretty a song on your behalf, I will not dismiss the idea just yet."),
  ("changed_my_mind_goodnatured",               "But you make a good case, so I'll try to keep an open mind."),
  ("changed_my_mind_upstanding",                "However, you make an eloquent case. I am still listening."),
#steve lord recruitment changes end

#steve post 0912 changes begin

  ("swadian_rebellion_pretender_intro",    "I am Isolla, rightful Queen of the Swadians."),
  ("vaegir_rebellion_pretender_intro",     "My name is Valdym. Some men call me 'the Bastard.' I am a prince of the Vaegirs, but by all rights I should be their king, instead of my cousin Yaroglek."),
  ("khergit_rebellion_pretender_intro",    "I am Dustum Khan, son of Janakir Khan, and rightful Khan of the Khergits."),
  ("nord_rebellion_pretender_intro",       "I am Lethwin Far-Seeker, son of Hakrim the Old, who should be king of the Nords of Calradia."),
  ("rhodok_rebellion_pretender_intro",     "I am Lord Kastor, the rightful King of the Rhodoks, who will free them from tyranny."),
  ("sarranid_rebellion_pretender_intro", "I am Arwa, whom they call the Pearled One, Mother of the Sarranids and their rightful Queen."),



  ("swadian_rebellion_pretender_story_1",  "I was the only child of my father, King Esterich. Although I am a woman, he loved me like a son and named me his heir -- not once, but several times, before the grandest nobles of the land so that none could doubt his intention. There is no law that bars a woman from ruling -- indeed, we Swadians tell tales of warrior queens who ruled us in our distant past."),
  ("vaegir_rebellion_pretender_story_1",   "My father died when I was young, leaving me in the care of his brother, the regent Burelek. But rather than hold the throne until I came of age, this usurper used his newfound power to accuse my mother of adultery, and to claim that I was not my father's son. She was executed for treason, and I was declared a bastard."),
  ("khergit_rebellion_pretender_story_1",  "Sanjar Khan and I are brothers, sons of the old Janakir Khan, although of different mothers. Although I was the younger brother, all those who knew the old Khan will testify that throughout my father's life, I was his favorite, entrusted with the responsibilities of government. Sanjar busied himself with hunts and feasts to win the affection of the more dissolate of my father's commanders."),
  ("nord_rebellion_pretender_story_1",     "I am called the Far-Seeker because I have travelled great distances, even by the standards of the Nords, in search of knowledge. Before I came of age, my father sent me abroad on a tour of study at the courts and universities in the lands overseas. If the Nords are to call themselves the heirs of the Calradian empire, then they must act the part, and know something of law and letters, and not call themselves content merely to fight, plunder, and drink."),
  ("rhodok_rebellion_pretender_story_1",   "The Rhodoks are a free people, and not slaves to any hereditary monarch. The king must be chosen from one of the leading noble families of the land, by a council drawn by lot from the patricians of the cities of Jelkala, Veluca, and Yalen. The council meets on a field before Jelkala, and no man is allowed to appear in arms during their deliberations, on pain of death."),
 ("sarranid_rebellion_pretender_story_1", "I was born in a faraway land, to a humble family, and made a slave when I was but a girl -- but there is no shame in that, for the mothers of many of our kings were slaves. The old Sultan, Ayzar, spotted me in the markets and was struck by my beauty. I entered his household, and there he also learned to respect my intelligence. As he grew older, he allowed me to govern in his stead. First I managed the affairs of the palace, and later those of the realm."),

  ("swadian_rebellion_pretender_story_2",  "Yet when my father died, his cousin Harlaus convinced the nobles that no Swadian king of sound mind could name a woman as his heir. Harlaus said that his designation of me was the act of a madman, and thus had no legal standing, and that he, as my father's closest male relative, should take the throne."),
  ("vaegir_rebellion_pretender_story_2",   "I was smuggled abroad by a faithful servant, but now I am of age and have returned to reclaim what is rightfully mine. Burelek died soon after his act of perfidy -- the judgment of heaven, no doubt. His son Yaroglek now calls himself king, but as his claim is tainted, he is no less a usurper than his father, and I will topple him from his throne."),
  ("khergit_rebellion_pretender_story_2",  "According to Khergit custom, when a man dies his herds are split between all his sons, equally. So too it is with the khanate. When I heard of my father's death, I was away inspecting our borders, but I hurried home to Tulga, ready to give Sanjar his due and share the khanate with him. But when I arrived, I found that he rushed his supporters to the court, to have himself proclaimed as the sole khan."),
  ("nord_rebellion_pretender_story_2",     "My father died however before I completed my course of study, and as I hurried home to claim his throne my ship was wrecked by a storm. One of my father's thanes, Ragnar, seized this opportunity and spread rumors that I had died abroad. He summoned a gathering of his supporters to have himself proclaimed king, and has taken the past few years to consolidate his power."),
  ("rhodok_rebellion_pretender_story_2",   "During the last selection, there were but two candidates, myself, and Lord Graveth. While the council was deliberating, Graveth appeared, sword in hand, telling them that a Swadian raiding party was about to descend on the field of deliberation -- which was true, by the way -- and if he were not elected king, then he would leave them to their fate."),
 ("sarranid_rebellion_pretender_story_2", "When Sultan Ayzar died, it seemed to the emirs of the realm only natural that I should succeed him as ruler, thus avoiding any danger of civil war. They insisted, however, that I should marry one of his generals, the Emir Baybak. The emirs then lined up to give us the oath of allegiance together -- to Baybak as Commander of the Armies, and to me as Mother of the Realm. For the brief time that we ruled, our realm prospered."),

  ("swadian_rebellion_pretender_story_3",  "I will admit that I did my cause no good by cursing Harlaus and all who listened to him as traitors, but I also believe that the magistrates who ruled in his favor were bought. No matter -- I will raise an army of loyal subjects, who would honour their old king's memory and will. And if anyone doubts that a woman can wield power, then I will prove them wrong by taking Harlaus' ill-gotten crown away from him."),
  ("vaegir_rebellion_pretender_story_3",   "Until I have my rights restored in the sight of all the Vaegirs, I will bear the sobriquet, 'the Bastard', to remind me of what I must do."),
  ("khergit_rebellion_pretender_story_3",  "My brother thinks that Khergits will only respect strength: a leader who takes what he wants, when he wants it. But I think that he misreads the spirit of our people.--we admire a resolute leader, but even more we a just one, and we know that a man who does not respect his own brother's rights will not respect the rights of his followers."),
  ("nord_rebellion_pretender_story_3",     "So I remain in exile -- except now I am not looking for sages to tutor me in the wisdom of faraway lands, but warriors, to come with me back to the land of the Nords and regain my throne. If Ragnar doubts my ability to rule, then let him say so face to face, as we stare at each other over the rims of our shields. For a warrior can be a scholar, and a scholar a warrior, and to my mind, only one who combines the two is fit to be king!"),
  ("rhodok_rebellion_pretender_story_3",   "Well, Graveth defeated the Swadians, and for that, as a Rhodok, I am grateful. When I am king, I will myself place the wreath of victory on his head. But after that I will have it separated from his shoulders, for by his actions he has shown himself a traitor to the Rhodok confederacy and its sacred custom."),
  ("sarranid_rebellion_pretender_story_3", "But alas, Baybak himself was soon killed in a skirmish with the Khergits. Had I known of his death in time, I would have been able to prepare myself against any possibility of betrayal. But alas, my husband's treacherous nephew Hakim came riding with his men, still covered with the dust of the battlefield, and drove me from the palace at swordpoint and proclaimed himself sultan. So be it -- I shall gather an army of my own, and return him the favor."),

  ("swadian_rebellion_monarch_response_1", "Isolla thinks she should be Queen of the Swadians? Well, King Esterich had a kind heart, and doted on his daughter, but a good-hearted king who doesn't use his head can be a curse to his people. Isolla may tell you stories of warrior queens of old, but you might also recall that all the old legends end in the same way -- with the Swadians crushed underfoot by the armies of the Calradic Emperor."),
  ("vaegir_rebellion_monarch_response_1",  "Were Valdym to come to me in peace, I would laden him with titles and honours, and he would become the greatest of my vassals. But as he comes in war, I will drag him before me in chains and make him acknowledge me as rightful sovereign, then cut his tongue from his mouth so that he cannot recant."),
  ("khergit_rebellion_monarch_response_1", "My brother Dustum has perhaps told you of his insistence upon splitting the khanate, as though it were a herd of sheep. Let me tell you something. Ever since the Khergits established themselves on this land, the death of every khan has had the same result -- the land was divided, the khan's sons went to war, and the strongest took it all anyway. I simply had the foresight to stave off the civil war in advance."),
  ("nord_rebellion_monarch_response_1",    "Lethwin 'Far-Seeker'? Lethwin Inkfingers, is more like it. Perhaps you have heard the expression, 'Unhappy is the land whose king is a child.' Unhappy too is the land whose king is a student. You want the Nords to be ruled by a beardless youth, whose hand bears no callouses left by a sword's grip, who has never stood in a shield wall? If Lethwin were king, his thanes would laugh at him to his face!"),
  ("rhodok_rebellion_monarch_response_1",  "No doubt Lord Kastor told you that I defiled the hallowed Rhodok custom by interfering with the patricians' election of a king. Well, let me tell you something. The patricians of the towns make longwinded speeches about our ancient liberties, but then choose as their king whichever noble last sat in their villa and sipped a fine wine and promised to overlook their unpaid taxes."),
  ("sarranid_rebellion_monarch_response_1", "Our scholars have long agreed that there is one overriding principle in politics. Men should accept the authority of the ruler, because tyranny is better than civil war. It was for that reason that I accepted the authority of both Baybak and Arwa, to whom I gave my oath as co-rulers."),

  ("swadian_rebellion_monarch_response_2", "Those who weep for the plight of a Swadian princess denied her father's throne should reflect instead on the fate of a Swadian herdswoman seized by a Vaegir raider and taken as chattel to the slave markets. Talk to me of queens and old stories when our warlike neighbors are vanquished, and our land is at peace."),
  ("vaegir_rebellion_monarch_response_2",  "Whatever my father may or may not have done to secure the throne does not matter. I have inherited it, and that is final. If every old claim were to be brought up anew, if every man's inheritance could be called into question at any time, then it would be the end of the institution of kingship, and we would live in a state of constant civil war."),
  ("khergit_rebellion_monarch_response_2", "Dustum would make a fine assessor of flocks, or adjudicator of land disputes. But can you imagine such a man as khan? We would be run off of our land in no time by our neighbors, and return to our old days of starving and freezing on the steppe."),
  ("nord_rebellion_monarch_response_2",    "Old Hakrim may have had fancy ideas about how to dispose of his kingdom, but it is not just royal blood that makes a King of the Nords. I am king by acclamation of the thanes, and by right of being the strongest. That counts for more than blood, and woe to any man in this land who says otherwise."),
  ("rhodok_rebellion_monarch_response_2",  "The only liberty that concerns them is their liberty to grow fat. Meanwhile, my men sleep out on the steppe, and eat dry bread and salt fish, and scan the horizon for burning villages, and shed our blood to keep the caravan routes open. Here's an idea -- if I ever meet a merchant who limps from a Khergit arrow-wound or a Swadian sword-stroke, then I'll say, 'Here's a man whose counsel is worth taking.'"),
  ("sarranid_rebellion_monarch_response_2", "You should know, however, that Arwa was not chosen as Baybak's partner because of her wisdom or love of justice. No, she was chosen because she was a witch, who could transform men like Ayzar and Baybak into stammering fools. No matter -- I was true to my oath, and respected her usurpation, until the very hour that it was invalidated by the death of her puppet. Now she must respect mine."),

#steve post 0912 changes end

#courtship
  ("courtship_comment_conventional_generic",  "is a very well-bred sort"),
  ("courtship_comment_adventurous_generic",   "seems decent enough"),
  ("courtship_comment_otherworldly_generic",  "is most polite and attentive"),
  ("courtship_comment_ambitious_generic",     "lacks drive -- but perhaps that may be remedied"),
  ("courtship_comment_moralist_generic",      "seems to be a man of good character"),

  ("feast_description", 					  "scant"),
  ("feast_description_2", 					  "meager"),
  ("feast_description_3", 					  "barely adequate"),
  ("feast_description_4", 					  "sufficient"),
  ("feast_description_5", 					  "bountiful"),
  ("feast_description_6", 					  "magnificent"),

  ("feast_lengthy_description_1", 			  "The food you provided was insufficient for your guests and their retinues, forcing them to purchase their sustenance from the surrounding countryside at grossly inflated prices. The consensus among those who attended was that you failed to do your duty as a host, diminishing both their trust in you and your overall reputation."),
  ("feast_lengthy_description_2", 			  "The food and drink you provided eventually ran out, forcing some guests to either buy their own from passing peddlars, or send some of their retinue home early. The more charitable attributed the shortfall to poor planning rather than meanness, but either way, it did your reputation no good."),
  ("feast_lengthy_description_3", 			  "The food and drink you provided was adequate for your noble guests, although some of the commoners in their retinues went without. You are establishing a reputation as one who has at least a grasp of your social obligations as a noble."),
  ("feast_lengthy_description_4", 		      "You have provided enough food and drink, and with sufficient varieties, to do yourself credit. The food, drink, and merriment have loosened your guests tongues, allowing them to converse candidly about the matters of the realm, and deepening their trust in you."),
  ("feast_lengthy_description_5", 			  "You have provided a bountiful table not just for your noble guests but for their retinues, with food left over to be distributed to the poor. Your guests lavish praise upon you for your generosity, and for your understanding of the social obligations of your rank. The conversation, fueled by the food and drink, has been merry, strengthening the bonds between those who attended."),
  ("feast_lengthy_description_6", 			  "The realm will be speaking of the bounty of your table for months to come, and it will become the standard to which all other feasts will aspire. You have filled the bellies not just of your noble guests and their retinues, but also of the poor who flocked to the gates. "),


  ("kingdom_1_adjective",                     "Swadian"),
  ("kingdom_2_adjective",                     "Vaegir"),
  ("kingdom_3_adjective",                     "Khergit"),
  ("kingdom_4_adjective",                     "Nord"),
  ("kingdom_5_adjective",                     "Rhodok"),
  ("kingdom_6_adjective",                     "Sarranid"),


  ("credits_1", "Mount&Blade: Warband Copyright 2008-2015 Taleworlds Entertainment"),
  ("credits_2", "Game design:^Armagan Yavuz^Steve Negus^Cem Cimenbicer"),
  ("credits_3", "Programming:^Armagan Yavuz^Cem Cimenbicer^Serdar Kocdemir^Ozan Gumus^Mustafa Korkmaz^^Additional Programming:^Gokhan Uras^M. Furkan Yilmaz"),
  ("credits_4", "CG Artists:^Ozgur Saral^Mustafa Ozturk^Pinar Cekic^Ozan Unlu^Yigit Savtur^Umit Singil"),
  ("credits_5", "Concept Artist:^Ganbat Badamkhand"),
  ("credits_6", "Writing:^Steve Negus^Armagan Yavuz^Ryan A. Span"),
  ("credits_7", "Original Music:^Jesse Hopkins"),
  ("credits_8", "Voice Talent:^Tassilo Egloffstein"),
  ("credits_9", "This game has been supported by The Scientific and Technological Research Council of Turkey.^^\
Tutorial written by:^Steve Negus^Armagan Yavuz^Edward Spoerl^^\
Horse Motion Capture Animation Supplied by:^Richard Widgery & Kinetic Impulse^^\
Physics:^Havok^^\
Sound and Music Program Library:^FMODex Sound System by Firelight Technologies^^\
Skybox Textures:^Jay Weston^^\
Chinese Translation:^Hetairoi; Gaodatailang; silentjealousy; Ginn; fallout13; James; D.Kaede; Kan2; alixyang; muyiboy^^\
TaleWorlds Director of Communications:^Ali Erkin^^\
TaleWorlds Forum Programming:^Brett Flannigan ^^^\
TaleWorlds.com Forum Administrators and Moderators:^\
Janus^\
Archonsod^\
Narcissus^\
Nairagorn^\
Lost Lamb^\
Deus Ex^\
Merentha^\
Volkier^\
Instag0^\
Ativan^\
ego^\
Guspav^\
Hallequin^\
Invictus^\
okiN^\
Raz^\
rejenorst^\
Skyrage^\
ThVaz^^^\
Mount&Blade Community Suggestions and Feedback:^\
A_Mustang^\
adamlug^\
Adorno^\
alden^\
Alhanalem^\
amade^\
Anthallas^\
Alkhadias Master^\
Arch3r^\
Archevious^\
Arcas Nebun^\
Arcon^\
Arcturus^\
ares007^\
Arjihad^\
BadabombadaBang^\
Badun^\
BaronAsh^\
Berserker Pride^\
bgfan^\
bierdopjeee^\
Big_Mac^\
Binboy^\
blink180heights^\
BlodsHammar^\
Bloid^\
Brandon^\
Brego^\
chenjielian^\
cifre^\
COGlory^\
Corinthian Hoplite^\
Crazed Rabbit^\
CryptoCactus^\
CtrlAltDe1337^\
Cuther^\
Da-V-Man^\
dimitrischris^\
dstemmer^\
EasyCo506^\
Egbert^\
ethneldryt^\
eudaimondaimon^\
Faranox^\
Fawzia dokhtar-i-Sanjar^\
Fei Dao^\
Gabeed^\
GeN76^\
General_Hospital^\
GhosTR^\
glustrod^\
Gubbo^\
guspav^\
Halcyon^\
Harn^\
Hethwill^\
Highelfwarrior^\
HULKSMASH^\
Iberon^\
ignoble^\
Jack_Merchantson^\
JoG^\
Jov^\
Kazzan^\
King Jonathan the Great^\
Kleidophoros^\
knight^\
Kong Burger^\
Kristiania^\
l3asu^\
Larkraxm^\
Leandro1021DX^\
lighthaze^\
Llew2^\
Lord Rich^\
lordum_ediz^\
Lucke189^\
Mabons^\
MacPharlan^\
Madnes5^\
MagicMaster^\
Makh^\
ManiK^\
Manitas^\
Marin Peace Bringer^\
Martinet^\
MAXHARDMAN^\
Merlkir^\
miguel8500^\
Mithras^\
Moddan^\
Nate^\
Nemeo^\
Nite/m4re^\
noobalicous^\
Nord Champion^\
okiN^\
Orion^\
OTuphlos^\
Papa Lazarou^\
Phallas^\
Plazek^\
Prcin^\
PSYCHO78^\
PsykoOps^\
Reapy^\
Red River^\
Rhizobium^\
Riggea^\
Rongar^\
Ros^\
sadnhappy^\
Sarejo^\
ScientiaExcelsa^\
Scorch!^\
Seawied86^\
sebal87^\
shikamaru 1993^\
Shun^\
silentdawn^\
Sir Gowe^\
Skyrage^\
Slawomir of Aaarrghh^\
SoloSebo^\
SovietSoldier^\
Stabbing Hobo^\
Stratigos001^\
Styo^\
TalonAquila^\
test^\
The Yogi^\
Thundertrod^\
Thyr^\
Tim^\
Titanshoe^\
tmos^\
Toffey^\
Tonttu^\
Trenalok^\
Tronde^\
UberWiggett^\
Urist^\
Ursca^\
urtzi^\
Vermin^\
Viajero^\
Vincenzo^\
Vulkan^\
Warcat92^\
Welcome_To_Hell^\
Wheem^\
Wu-long^\
Yellonet^\
Yobbo^\
Yoshi Murasaki^\
Yoshiboy^\
Zyconnic^^^\
Special Thanks to Toby Lee for his ideas and in depth feedback on the combat system.^\
...and many many other wonderful Mount&Blade players!^^\
(This is only a small sample of all the players who have contributed to the game by providing suggestions and feedback.^\
This list has been compiled by sampling only a few threads in the Taleworlds Forums.^\
Unfortunately compiling an exhaustive list is almost impossible.^\
We apologize sincerely if you contributed your suggestions and feedback but were not listed here, and please know that we are grateful to you all the same...)\
"),
  ("credits_10", "Paradox Interactive^^President and CEO:^Theodore Bergqvist^^Executive Vice President:^Fredrik Wester\
^^Chief Financial Officer:^Lena Eriksson^^Finance & Accounting:^Annlouise Larsson^^VP Sales & Marketing US:^Reena M. Miranda\
^^VP Sales & Marketing EU:^Martin Sirc^^Distribution Manager Nordic:^Erik Helmfridsson^^Director of PR & Marketing:^Susana Meza\
^^PR & Marketing:^Sofia Forsgren^^Product Manager:^Boel Bermann\
"),
  ("credits_11", "Logotype:^Jason Brown^^Cover Art:^Piotr Fox Wysocki\
^^Layout:^Christian Sabe^Melina Grundel^^Poster:^Piotr Fox Wysocki^^Map & Concept Art:^Ganbat Badamkhand\
^^Manual Editing:^Digital Wordsmithing: Ryan Newman, Nick Stewart^^Web:^Martin Ericsson^^Marketing Assets:^2Coats\
^^Localization:^S&H Entertainment Localization^^GamersGate:^Ulf Hedblom^Andreas Pousette^Martin Ericson^Christoffer Lindberg\
"),
  ("credits_12", "Thanks to all of our partners worldwide, in particular long-term partners:\
^Koch Media (Germany & UK)^Blue Label (Italy & France)^Friendware (Spain)^New Era Interactive Media Co. Ltd. (Asia)\
^Snowball (Russia)^Pinnacle (UK)^Porto Editora (Portugal)^Hell-Tech (Greece)^CD Projekt (Poland, Czech Republic, Slovakia & Hungary)\
^Paradox Scandinavian Distribution (Scandinavia)\
"),

#### Warband added texts

#multiplayer scene names
  ("multi_scene_1", "Ruins"),
  ("multi_scene_2", "Village"),
  ("multi_scene_3", "Hailes Castle"), #Castle 1
  ("multi_scene_4", "Ruined Fort"),
  ("multi_scene_5", "Scene 5"), #not ready yet
  ("multi_scene_6", "Scene 6"), #not ready yet
  ("multi_scene_7", "Field by the River"),
  ("multi_scene_8", "Rudkhan Castle"), #Castle 2
  ("multi_scene_9", "Snowy Village"),
  ("multi_scene_10", "Turin Castle"), #Castle 3
  ("multi_scene_11", "Nord Town"),
  ("multi_scene_16", "Port Assault"),
  ("multi_scene_17", "Brunwud Castle"), #Castle 4
  ("multi_scene_18", "Battle on Ice"),
  ("multi_scene_19", "Mahdaar Castle"), #Castle 5
  ("multi_scene_20", "Jameyyed Castle"), #Castle 6
  ("multi_scene_21", "The Arena"),
  ("multi_scene_22", "Forest Hideout"),
  ("multi_scene_23", "Canyon"),
  ("multi_scene_24", "Desert Town"),
  ("multi_scene_12", "Random Plains (Medium)"),
  ("multi_scene_13", "Random Plains (Large)"),
  ("multi_scene_14", "Random Steppe (Medium)"),
  ("multi_scene_15", "Random Steppe (Large)"),
  ("multi_scene_end", "multi_scene_end"),

#multiplayer game type names
  ("multi_game_type_1", "Deathmatch"),
  ("multi_game_type_2", "Team Deathmatch"),
  ("multi_game_type_3", "Battle"),
  ("multi_game_type_4", "Fight and Destroy"),
  ("multi_game_type_5", "Capture the Flag"),
  ("multi_game_type_6", "Conquest"),
  ("multi_game_type_7", "Siege"),
  ("multi_game_type_8", "Duel"),
  ("multi_game_types_end", "multi_game_types_end"),

  ("poll_kick_player_s1_by_s0", "{s0} started a poll to kick player {s1}."),
  ("poll_ban_player_s1_by_s0", "{s0} started a poll to ban player {s1}."),
  ("poll_change_map_to_s1_by_s0", "{s0} started a poll to change map to {s1}."),
  ("poll_change_map_to_s1_and_factions_to_s2_and_s3_by_s0", "{s0} started a poll to change map to {s1} and factions to {s2} and {s3}."),
  ("poll_change_number_of_bots_to_reg0_and_reg1_by_s0", "{s0} started a poll to change bot counts to {reg0} and {reg1}."),

  ("poll_kick_player", "Poll to kick player {s0}: 1 = Accept, 2 = Decline"),
  ("poll_ban_player", "Poll to ban player {s0}: 1 = Accept, 2 = Decline"),
  ("poll_change_map", "Poll to change map to {s0}: 1 = Accept, 2 = Decline"),
  ("poll_change_map_with_faction", "Poll to change map to {s0} and factions to {s1} versus {s2}: 1 = Accept, 2 = Decline"),
  ("poll_change_number_of_bots", "Poll to change number of bots to {reg0} for {s0} and {reg1} for {s1}: 1 = Accept, 2 = Decline"),
  ("poll_time_left", "({reg0} seconds left)"),
  ("poll_result_yes", "The poll is accepted by the majority."),
  ("poll_result_no", "The poll is rejected by the majority."),

  ("total_item_cost_reg0", "Total cost: {reg0}"),

  ("server_name", "Server name:"),
  ("game_password", "Game password:"),
  ("map", "Map:"),
  ("game_type", "Game type:"),
  ("max_number_of_players", "Maximum number of players:"),
  ("number_of_bots_in_team_reg1", "Number of bots in team {reg1}:"),
  ("team_reg1_faction", "Team {reg1} faction:"),
  ("enable_valve_anti_cheat", "Enable Valve Anti-cheat (Requires valid Steam account)"),
  ("allow_friendly_fire", "Allow ranged friendly fire"),
  ("allow_melee_friendly_fire", "Allow melee friendly fire"),
  ("friendly_fire_damage_self_ratio", "Friendly fire damage self (%):"),
  ("friendly_fire_damage_friend_ratio", "Friendly fire damage friend (%):"),
  ("spectator_camera", "Spectator camera:"),
  ("control_block_direction", "Control block direction:"),
  ("map_time_limit", "Map time limit (minutes):"),
  ("round_time_limit", "Round time limit (seconds):"),
  ("players_take_control_of_a_bot_after_death", "Switch to bot on death:"),
  ("team_points_limit", "Team point limit:"),
  ("point_gained_from_flags", "Team points gained for flags (%):"),
  ("point_gained_from_capturing_flag", "Points gained for capturing flags:"),
  ("respawn_period", "Respawn period (seconds):"),
  ("add_to_official_game_servers_list", "Add to official game servers list"),
  ("combat_speed", "Combat_speed:"),
  ("combat_speed_0", "Slowest"),
  ("combat_speed_1", "Slower"),
  ("combat_speed_2", "Medium"),
  ("combat_speed_3", "Faster"),
  ("combat_speed_4", "Fastest"),
  ("off", "Off"),
  ("on", "On"),
  ("defender_spawn_count_limit", "Defender spawn count:"),
  ("unlimited", "Unlimited"),
  ("automatic", "Automatic"),
  ("by_mouse_movement", "By mouse movement"),
  ("free", "Free"),
  ("stick_to_any_player", "Lock to any player"),
  ("stick_to_team_members", "Lock to team members"),
  ("stick_to_team_members_view", "Lock to team members' view"),
  ("make_factions_voteable", "Allow polls to change factions"),
  ("make_kick_voteable", "Allow polls to kick players"),
  ("make_ban_voteable", "Allow polls to ban players"),
  ("bots_upper_limit_for_votes", "Bot count limit for polls:"),
  ("make_maps_voteable", "Allow polls to change maps"),
  ("valid_vote_ratio", "Poll accept threshold (%):"),
  ("auto_team_balance_limit", "Auto team balance threshold (diff.):"),
  ("welcome_message", "Welcome message:"),
  ("initial_gold_multiplier", "Starting gold (%):"),
  ("battle_earnings_multiplier", "Combat gold bonus (%):"),
  ("round_earnings_multiplier", "Round gold bonus (%):"),
  ("allow_player_banners", "Allow individual banners"),
  ("force_default_armor", "Force minimum armor"),

  ("reg0", "{!}{reg0}"),
  ("s0_reg0", "{!}{s0} {reg0}"),
  ("s0_s1", "{!}{s0} {s1}"),
  ("reg0_dd_reg1reg2", "{!}{reg0}:{reg1}{reg2}"),
  ("s0_dd_reg0", "{!}{s0}: {reg0}"),
  ("respawning_in_reg0_seconds", "Respawning in {reg0} seconds..."),
  ("no_more_respawns_remained_this_round", "No lives left for this round"),
  ("reg0_respawns_remained", "({reg0} lives remaining)"),
  ("this_is_your_last_respawn", "(This is your last life)"),
  ("wait_next_round", "(Wait for the next round)"),

  ("yes_wo_dot", "Yes"),
  ("no_wo_dot", "No"),

  ("we_resign", "We have no strength left to put up a fight. We surrender to you, {playername}."),
  ("i_resign", "I don't want to die today. I surrender."),

  ("s1_returned_flag", "{s1} has returned their flag to their base!"),
  ("s1_auto_returned_flag", "{s1} flag automatically returned to their base!"),
  ("s1_captured_flag", "{s1} has captured the enemy flag!"),
  ("s1_taken_flag", "{s1} has taken the enemy flag!"),
  ("s1_neutralized_flag_reg0", "{s1} has neutralized flag {reg0}."),
  ("s1_captured_flag_reg0", "{s1} has captured flag {reg0}!"),
  ("s1_pulling_flag_reg0", "{s1} has started pulling flag {reg0}."),

  ("s1_destroyed_target_0", "{s1} destroyed target A!"),
  ("s1_destroyed_target_1", "{s1} destroyed target B!"),
  ("s1_destroyed_catapult", "{s1} destroyed the catapult!"),
  ("s1_destroyed_trebuchet", "{s1} destroyed the trebuchet!"),
  ("s1_destroyed_all_targets", "{s1} destroyed all targets!"),
  ("s1_saved_1_target", "{s1} saved one target."),
  ("s1_saved_2_targets", "{s1} saved all targets."),

  ("s1_defended_castle", "{s1} defended their castle!"),
  ("s1_captured_castle", "{s1} captured the castle!"),

  ("auto_team_balance_in_20_seconds", "Auto-balance will be done in 20 seconds."),
  ("auto_team_balance_next_round", "Auto-balance will be done next round."),
  ("auto_team_balance_done", "Teams have been auto-balanced."),
  ("s1_won_round", "{s1} has won the round!"),
  ("round_draw", "Time is up. Round draw."),
  ("round_draw_no_one_remained", "No one left. Round draw."),
  ("death_mode_started", "Hurry! Become master of the field!"),

  ("reset_to_default", "Reset to Default"),
  ("done", "Done"),
  ("player_name", "Player Name"),
  ("kills", "Kills"),
  ("deaths", "Deaths"),
  ("ping", "Ping"),
  ("dead", "Dead"),
  ("reg0_dead", "{reg0} Dead"),
  ("bots_reg0_agents", "Bots ({reg0} agents)"),
  ("bot_1_agent", "Bot (1 agent)"),
  ("score", "Score"),
  ("score_reg0", "Score: {reg0}"),
  ("flags_reg0", "(Flags: {reg0})"),
  ("reg0_players", "({reg0} players)"),
  ("reg0_player", "({reg0} player)"),

  ("open_gate", "Open Gate"),
  ("close_gate", "Close Gate"),
  ("open_door", "Open Door"),
  ("close_door", "Close Door"),
  ("raise_ladder", "Raise Ladder"),
  ("drop_ladder", "Drop Ladder"),

  ("back", "Back"),
  ("start_map", "Start Map"),

  ("choose_an_option", "Choose an option:"),
  ("choose_a_poll_type", "Choose a poll type:"),
  ("choose_faction", "Choose Faction"),
  ("choose_a_faction", "Choose a faction:"),
  ("choose_troop", "Choose Troop"),
  ("choose_a_troop", "Choose a troop class:"),
  ("choose_items", "Choose Equipment"),
  ("options", "Options"),
  ("redefine_keys", "Redefine Keys"),
  ("submit_a_poll", "Submit a Poll"),
  ("administrator_panel", "Administrator Panel"),
  ("kick_player", "Kick Player"),
  ("ban_player", "Ban Player"),
  ("mute_player", "Mute Player"),
  ("unmute_player", "Unmute Player"),
  ("quit", "Quit"),
  ("poll_for_changing_the_map", "Change the map"),
  ("poll_for_changing_the_map_and_factions", "Change the map and factions"),
  ("poll_for_changing_number_of_bots", "Change number of bots in teams"),
  ("poll_for_kicking_a_player", "Kick a player"),
  ("poll_for_banning_a_player", "Ban a player"),
  ("choose_a_player", "Choose a player:"),
  ("choose_a_map", "Choose a map:"),
  ("choose_a_faction_for_team_reg0", "Choose a faction for team {reg0}:"),
  ("choose_number_of_bots_for_team_reg0", "Choose number of bots for team {reg0}:"),
  ("spectator", "Spectator"),
  ("spectators", "Spectators"),
  ("score", "Score"),
  ("command", "Command:"),
  ("profile_banner_selection_text", "Choose a banner for your profile:"),
  ("use_default_banner", "Use Faction's Banner"),

  ("party_morale_is_low", "Morale of some troops are low!"),
  ("weekly_report", "Weekly Report"),
  ("has_deserted_the_party", "has deserted the party."),
  ("have_deserted_the_party", "have deserted the party."),

  ("space", " "),
  #new auto generated strings which taken from quick strings.
  ("us_", "Us "),
  ("allies_", "Allies "),
  ("enemies_", "Enemies "),
  ("routed", "Routed"),
  ("weekly_budget", "Weekly Budget"),
  ("income_from_s0", "Income from {s0}:"),
  ("mercenary_payment_from_s0", "Mercenary payment from {s0}:"),
  ("s0s_party", "{s0}'s Party"),
  ("loss_due_to_tax_inefficiency", "Loss due to tax inefficiency:"),
  ("wages_for_s0", "Wages for {s0}:"),
  ("earlier_debts", "Earlier debts:"),
  ("net_change", "Net change:"),
  ("earlier_wealth", "Earlier wealth:"),
  ("new_wealth", "New wealth:"),
  ("new_debts", "New debts:"),
  ("completed_faction_troop_assignments_cheat_mode_reg3", "{!}Completed faction troop assignments, cheat mode: {reg3}"),
  ("completed_political_events_cheat_mode_reg3", "{!}Completed political events, cheat mode: {reg3}"),
  ("assigned_love_interests_attraction_seed_reg3", "{!}Assigned love interests. Attraction seed: {reg3}"),
  ("located_kingdom_ladies_cheat_mode_reg3", "{!}Located kingdom ladies, cheat mode: {reg3}"),
  ("team_reg0_bot_count_is_reg1", "{!}Team {reg0} bot count is {reg1}."),
  ("input_is_not_correct_for_the_command_type_help_for_more_information", "{!}Input is not correct for the command. Type 'help' for more information."),
  ("maximum_seconds_for_round_is_reg0", "Maximum seconds for round is {reg0}."),
  ("respawn_period_is_reg0_seconds", "Respawn period is {reg0} seconds."),
  ("bots_upper_limit_for_votes_is_reg0", "Bots upper limit for votes is {reg0}."),
  ("map_is_voteable", "Map is voteable."),
  ("map_is_not_voteable", "Map is not voteable."),
  ("factions_are_voteable", "Factions are voteable."),
  ("factions_are_not_voteable", "Factions are not voteable."),
  ("players_respawn_as_bot", "Players respawn as bot."),
  ("players_do_not_respawn_as_bot", "Players do not respawn as bot."),
  ("kicking_a_player_is_voteable", "Kicking a player is voteable."),
  ("kicking_a_player_is_not_voteable", "Kicking a player is not voteable."),
  ("banning_a_player_is_voteable", "Banning a player is voteable."),
  ("banning_a_player_is_not_voteable", "Banning a player is not voteable."),
  ("player_banners_are_allowed", "Player banners are allowed."),
  ("player_banners_are_not_allowed", "Player banners are not allowed."),
  ("default_armor_is_forced", "Default armor is forced."),
  ("default_armor_is_not_forced", "Default armor is not forced."),
  ("percentage_of_yes_votes_required_for_a_poll_to_get_accepted_is_reg0", "Percentage of yes votes required for a poll to get accepted is {reg0}%."),
  ("auto_team_balance_threshold_is_reg0", "Auto team balance threshold is {reg0}."),
  ("starting_gold_ratio_is_reg0", "Starting gold ratio is {reg0}%."),
  ("combat_gold_bonus_ratio_is_reg0", "Combat gold bonus ratio is {reg0}%."),
  ("round_gold_bonus_ratio_is_reg0", "Round gold bonus ratio is {reg0}%."),
  ("point_gained_from_flags_is_reg0", "Team points gained for flags is {reg0}%."),
  ("point_gained_from_capturing_flag_is_reg0", "Points gained for capturing flags is {reg0}%."),
  ("map_time_limit_is_reg0", "Map time limit is {reg0} minutes."),
  ("team_points_limit_is_reg0", "Team point limit is {reg0}."),
  ("defender_spawn_count_limit_is_s1", "Defender spawn count is {s1}."),
  ("system_error", "SYSTEM ERROR!"),
  ("prisoner_granted_parole", "Prisoner granted parole"),
  ("prisoner_not_offered_parole", "Prisoner not offered parole"),
  ("_age_reg1_family_", "^Age: {reg1}^Family:"),
  ("s49_s12_s11_rel_reg0", "{s49} {s12} ({s11}, rel: {reg0}),"),
  ("s49_s12_s11", "{s49} {s12} ({s11}),"),
  #SB : add wealth, remove later, also add marshal indicator
  ("lord_info_string", "{reg6?:{reg4?{s54} is the ruler of {s56}.^:{s54} is {reg5?the marshal for:a vassal of} {s55} of {s56}.^}}Renown: {reg15}. Controversy: {reg16}. Wealth: {reg17}.^{reg9?{reg3?She:He} is the {reg3?lady:lord} of {s58}.:{reg3?She:He} has no fiefs.}{s59}^{s49}"),
  ("updating_faction_notes_for_s14_temp_=_reg4", "{!}Updating faction notes for {s14}, temp = {reg4}"),
  ("foreign_relations__", "{s20}^Foreign relations: ^"), #SB : insert domestic policy string
  ("s21__the_s5_is_at_war_with_the_s14", "{s21}^* The {s5} is at war with the {s14}."),
  ("s21_the_s5_has_had_the_upper_hand_in_the_fighting", "{s21} The {s5} has had the upper hand in the fighting."),
  ("s21_the_s5_has_gotten_the_worst_of_the_fighting", "{s21} The {s5} has gotten the worst of the fighting."),
  ("s21_the_fighting_has_gone_on_for_some_time_and_the_war_may_end_soon_with_a_truce", "{s21} The fighting has gone on for some time, and the war may end soon with a truce."),
  ("s21_the_fighting_has_begun_relatively_recently_and_the_war_may_continue_for_some_time", "{s21} The fighting has begun relatively recently, and the war may continue for some time."),
  ("s21_reg4reg5", "{!}{s21} ({reg4}/{reg5})"),
  ("_however_the_truce_is_no_longer_binding_on_the_s14", " However, the truce is no longer binding on the {s14}"),
  ("s21__the_s5_is_bound_by_truce_not_to_attack_the_s14s18_the_truce_will_expire_in_reg1_days", "{s21}^* The {s5} is bound by truce not to attack the {s14}.{s18} The truce will expire in {reg1} days."),
  ("s21__the_s5_has_recently_suffered_provocation_by_subjects_of_the_s14_and_there_is_a_risk_of_war", "{s21}^* The {s5} has recently suffered provocation by subjects of the {s14}, and there is a risk of war."),
  ("s21__the_s5_has_no_outstanding_issues_with_the_s14", "{s21}^* The {s5} has no outstanding issues with the {s14}."),
  ("s21_the_s14_was_recently_provoked_by_subjects_of_the_s5_and_there_is_a_risk_of_war_", "{s21} The {s14} was recently provoked by subjects of the {s5}, and there is a risk of war.^"),
  ("s21_cheat_mode_assessment_s14_", "{!}{s21}^CHEAT MODE ASSESSMENT: {s14}^"),
  ("the_s5_is_ruled_by_s6_it_occupies_s8_its_vassals_are_s10__s21", "The {s5} is ruled by {s6}.^It occupies {s8}.^Its vassals are {s10}.^^{s21}"),
  ("assigned_lord_reputation_and_relations_cheat_mode_reg3", "{!}Assigned lord reputation and relations, cheat mode: {reg3}"),
  ("caravan_trades_in_s5_originally_from_s4_", "{!}Caravan trades in {s5}, originally from {s4} "),
  ("your_hero_prisoned_at_s1", "{!}your hero prisoned at {s1}."),
  ("old_morale_is_reg0_new_morale_is_reg1", "{!}old morale is {reg0}, new morale is {reg1}"),
  ("our_per_person__reg0_num_people__reg1_total_gain__reg2", "{!}[our] per person : {reg0}, num people : {reg1}, total gain : {reg2}"),
  ("ene_per_person__reg0_num_people__reg1_total_gain__reg2", "{!}[ene] per person : {reg0}, num people : {reg1}, total gain : {reg2}"),
  ("all_per_person__reg0_num_people__reg1_total_gain__reg2", "{!}[all] per person : {reg0}, num people : {reg1}, total gain : {reg2}"),
  ("loss_ratio_is_reg1", "{!}loss ratio is {reg1}"),
  ("total_enemy_morale_gain__reg6_last_total_enemy_morale_gain__reg7_remaining_enemy_population__reg5", "{!}total enemy morale gain : {reg6}, last total enemy morale gain : {reg7}, remaining enemy population : {reg5}"),
  ("reg4_killed_reg5_wounded_reg6_routed", "{reg4} killed, {reg5} wounded, {reg6} routed"),
  ("reg4_killed_reg5_routed", "{reg4} killed, {reg5} routed"),
  ("reg4_killed_reg5_wounded", "{reg4} killed, {reg5} wounded"),
  ("reg4_wounded_reg5_routed", "{reg4} wounded, {reg5} routed"),
  ("routed", "routed"),
  ("caravan_in_s10_considers_s11_total_price_dif_=_reg3", "{!}Caravan in {s10} considers {s11}, total price dif = {reg3}"),
  ("test__caravan_in_s3_selects_for_s4_trade_score_reg3", "{!}TEST - Caravan in {s3} selects for {s4}, trade score: {reg3}"),
  ("prisoner_relative_is_reg0", "{!}prisoner relative is {reg0}"),
  ("test_diagnosis__traveller_attacks_for_s4", "{!}Test diagnosis -- traveller attacks for {s4}"),
  ("traveller_attack_found", "{!}Traveller attack found"),
  ("s42", "{s42}"),
  ("test_diagnostic_quest_found_for_s4", "{!}Test diagnostic: Quest found for {s4}"),
  ("s4_changing_sides_aborts_quest", "{!}{s4} changing sides aborts quest"),
  ("s4_awarded_to_s5", "{s4} awarded to {s5}"),
  ("s11_reacts_to_granting_of_s12_to_s10", "{!}{s11} reacts to granting of {s12} to {s10}"),
  ("debug__hiring_men_to_s7_ideal_size__reg6_ideal_top_size__reg7_hiring_budget__reg8", "{!}DEBUG : hiring men to {s7} ideal size : {reg6}, ideal top size : {reg7}, hiring budget : {reg8}"),
  ("debug__hiring_men_to_party_for_s0", "{!}DEBUG : hiring men to party for {s0}"),
  ("calculating_sortie_for_s4_strength_of_reg3_vs_reg4_enemies", "Calculating sortie for {s4}, strength of {reg3} vs {reg4} enemies"),
  ("s4_sorties", "{!}{s4} sorties"),
  ("current_wealth_reg1_taxes_last_collected_from_s4", "Current wealth: {reg1}. Taxes last collected from {s4}"),
  ("s4_considers_going_to_s5_to_pay_court_to_s6", "{!}{s4} considers going to {s5} to pay court to {s6}"),
  ("relation_with_1_bug_found_here__probably_because_s5_has_just_been_captured", "{!}Relation with -1 bug found here - probably because {s5} has just been captured"),
  ("s4_has_reg4_chance_of_going_to_home_center", "{!}{s4} has {reg4} chance of going to home center"),
  ("s4_has_reg4_chance_of_recruiting_troops", "{s4} has {reg4} chance of recruiting troops"),
  ("s4_has_reg4_chance_of_going_to_s5", "{s4} has {reg4} chance of going to {s5}"),
  ("s4_has_reg5_chance_of_patrolling_s6", "{s4} has {reg5} chance of patrolling {s6}"),
  ("s4_has_reg5_chance_of_raiding_s6", "{s4} has {reg5} chance of raiding {s6}"),
  ("s4_has_reg5_chance_of_besieging_s6", "{s4} has {reg5} chance of besieging {s6}"),
  ("sum_chances_reg6", "Sum chances: {reg6}"),
  ("deciding_faction_ai_for_s3", "Deciding faction AI for {s3}"),
  ("s5_decides_s14", "{!}{s5} decides: {s14}"),
  ("lords_of_the_s1_gather_for_a_feast_at_s2", "Lords of the {s1} gather for a feast at {s2}."),
  ("s5_begins_offensive", "{!}{s5} begins offensive"),
  ("renown_change_of_reg4_reduced_to_reg5_because_of_high_existing_renown", "{!}Renown change of {reg4} reduced to {reg5}, because of high existing renown"),
  ("s14", "{!}{s14}"),
  ("players_kingdom_has_had_reg3_days_of_peace", "Player's kingdom has had {reg3} days of peace"),
  ("s4_is_present_at_the_center_and_in_place_of_honor", "{!}{s4} is present at the center and in place of honor"),
  ("s4_is_present_at_the_center_as_a_refugee", "{!}{s4} is present at the center as a refugee"),
  ("s4_is_present_at_the_center_and_not_attending_the_feast", "{!}{s4} is present at the center and not attending the feast"),
  ("s4_is_present_at_the_center_and_is_married", "{!}{s4} is present at the center and is married"),
  ("s4_is_present_at_the_center_and_is_attending_the_feast", "{s4} is present at the center and is attending the feast"),
  ("s4_is_present_at_the_center_and_is_awaiting_the_player_in_private", "{s4} is present at the center and is awaiting the player in private"),
  ("s4_is_present_at_the_center_and_is_allowed_to_meet_the_player", "{s4} is present at the center and is allowed to meet the player"),
  ("s4_is_present_at_the_center_and_is_not_allowed_to_meet_the_player", "{s4} is present at the center and is not allowed to meet the player"),

  #Relative types
  ("no_relation", "no relation"),
  ("wife", "wife"),
  ("husband", "husband"),
  ("father", "father"),
  ("mother", "mother"),
  ("daughter", "daughter"),
  ("son", "son"),
  ("sister", "sister"),
  ("brother", "brother"),
  ("niece", "niece"),
  ("nephew", "nephew"),
  ("aunt", "aunt"),
  ("uncle", "uncle"),
  ("cousin", "cousin"),
  ("daughterinlaw", "daughter-in-law"),
  ("soninlaw", "son-in-law"),
  ("motherinlaw", "mother-in-law"),
  ("fatherinlaw", "father-in-law"),
  ("sisterinlaw", "sister-in-law"),
  ("brotherinlaw", "brother-in-law"),
  ("print_party_members_entered", "print party members entered"),
  ("num_companion_stacks_=_reg10", "num companion stacks = {reg10}"),
  ("someone", "someone"),

  #Trade explanations
##diplomacy start+ replace {sir/madame} with {s0} so it can be "my lord" or "your highness"
  ("i_take_what_work_i_can_sirmadame_i_carry_water_or_help_the_merchants_with_their_loads_or_help_build_things_if_theres_things_to_be_built", "I take what work I can, {s0}. I carry water, or help the merchants with their loads, or help build things, if there are things to be built."),
##diplomacy end+
  ("dna_reg4_total_production_reg5_modula_reg7", "{!}DNA: {reg4}, total production: {reg5}, modula: {reg7}"),
  ("agent_produces_s9", "{!}Agent produces {s9}"),
##diplomacy start+ replace {sir/madame} with {s0} so it can be "my lord" or "your highness"
  ("im_not_doing_anything_sirmadame_theres_no_work_to_be_had_around_here_these_days", "I'm not doing anything, {s0}. There's no work to be had around here these days."),
  ("im_not_doing_anything_sirmadame_i_have_no_land_of_my_own_and_theres_no_work_to_be_had_around_here_these_days", "I'm not doing anything, {s0}. I have no land of my own, and there's no work to be had around here these days."),
  ("why_im_still_living_off_of_your_kindness_and_goodness_sirmadame_hopefully_there_will_be_work_shortly", "Why, I'm still living off of your kindness and goodness, {s0}. Hopefully there will be work, shortly."),
##diplomacy end+
  ("i_work_in_the_fields_just_outside_the_walls_where_they_grow_grain_we_dont_quite_grow_enough_to_meet_our_needs_though_and_have_to_import_grain_from_the_surrounding_countryside", "I work in the fields, just outside the walls, where they grow grain. We don't quite grow enough to meet our needs, though, and have to import grain from the surrounding countryside."),
  ("i_work_mostly_in_the_fields_growing_grain_in_the_town_they_grind_it_to_make_bread_or_ale_and_we_can_also_boil_it_as_a_porridge", "I work mostly in the fields, growing grain. In the town they grind it to make bread or ale, and we can also boil it as a porridge."),
  ("i_work_in_the_breweries_making_ale_the_poor_folk_drink_a_lot_of_it_as_its_cheaper_than_wine_we_make_it_with_grain_brought_in_from_the_countryside", "I work in the breweries, making ale. The poor folk drink a lot of it, as it's cheaper than wine. We make it with grain brought in from the countryside."),
  ("i_work_in_a_mill_grinding_flour_to_make_bread_bread_is_cheap_keeps_well_and_fills_the_stomach", "I work in a mill, grinding flour to make bread. Bread is cheap, keeps well, and fills the stomach."),
  ("i_tend_cattle_we_dry_and_salt_meat_to_preserve_it_and_make_cheese_from_the_milk", "I tend cattle. We dry and salt meat to preserve it, and send the hides to the towns to be made into leather. We also make cheese from the milk."),
  ("i_tend_cattle_we_dry_and_salt_meat_to_preserve_it_and_make_cheese_from_the_milk_so_it_doesnt_spoil", "I tend cattle. We dry and salt meat to preserve it, and send the hides to the towns to be made into leather. We also make cheese from the milk."),
  ("i_tend_sheep_we_send_the_wool_to_the_cities_to_be_woven_into_cloth_and_make_mutton_sausage_when_we_cull_the_herds", "I tend sheep. We send the wool to the cities to be woven into cloth, and make mutton sausage when we cull the herds."),
  ("i_work_at_a_loom_spinning_cloth_from_wool_wool_is_some_of_the_cheapest_cloth_you_can_buy_but_it_will_still_keep_you_warm", "I work at a loom, spinning cloth from wool. Wool is some of the cheapest cloth you can buy, but it will still keep you warm."),
  ("i_crew_a_fishing_boat_we_salt_and_smoke_the_flesh_to_sell_it_far_inland", "I crew a fishing boat. We salt and smoke the flesh, to sell it far inland."),
  ("i_sift_salt_from_a_nearby_flat_they_need_salt_everywhere_to_preserve_meat_and_fish", "I sift salt from a nearby flat. They need salt everywhere, to preserve meat and fish."),
  ("i_mine_iron_from_a_vein_in_a_nearby_cliffside_they_use_it_to_make_tools_arms_and_other_goods", "I mine iron from a vein in a nearby cliffside. They use it to make tools, arms, and other goods."),
  ("i_make_pottery_which_people_use_to_store_grain_and_carry_water", "I make pottery, which people use to store grain and carry water."),

##diplomacy start+ replace {sir/madame} with {s0} so it can be "my lord" or "your highness"
  ("trade_explanation_tools", "I work in a smithy, {s0}, making all sorts of ironware -- knives, axes, pots, plough-blades, scythes, hammers, anvils, tongs, adzes, saws, nails, horseshoes, firesteel, braziers, and of course arms and armor for your excellencies."),
##diplomacy end+
  ("trade_explanation_oil", "I work in an oil press, making oil from olives brought in from the countryside. If you can afford it, our oil has a hundred uses -- in cooking, lamps, even for easing childbirth."),
##diplomacy start+ replace {sir/madame} with {s0} so it can be "my lord" or "your highness"
  ("trade_explanation_linen", "I weave linen, using flax brought in from the surrounding countryside. It's makes a tough, light fabric, {s0} -- good for summer clothing, sails for boats, and the like."),
##diplomacy end+
  ("trade_explanation_velvet", "I work in one of this town's great weaveries, carefully making the velvet for which we are known. We use silks brought from across the mountains, and dyes from the far corners of the earth, and make of it the finest and most expensive fabric that can be found in the land."),
  ("trade_explanation_spice", "I work in the caravanserie, helping the merchants unload the spice they bring from across the mountains. Pepper, cinnamon, cloves, saffron... The rich mark their wealth by the amount of spices in their food, and they say that for every ailment, there's a spice which cures it."),
  ("trade_explanation_apples", "I'm just coming in from the orchards, where we grow apples. We dry them for storage, or they can also be made into cider or vinegar."),

  ("trade_explanation_grapes", "I work in the vineyards on the hillsides, growing grapes to be made into fine wines for the tables of the lords, ladies, and merchants, and cheap wine to be mixed with water to quench the thirst of the commons."),
  ("trade_explanation_dyes", "I work in the caravanseries, unloading dyes brought in from the lands outside Calradia -- the crimson of oak beetles and the red roots of madder, the blue of indigo and woad shrubs, the yellow of weld root and greenweed. The weavers use it to color the silks and velvets of the great lords of the realm."),
##diplomacy start+ replace {sir/my lady} with {s0} so it can be "my lord" or "your highness"
  ("trade_explanation_leatherwork", "I work in the tanneries outside the walls, turning cured hides from the countryside into good, supple leather. It's foul work, and I come home stinking of urine, dung, and lime -- but that's where your boots, saddles, and bridles come from, {s0}."),
  ("trade_explanation_flax", "I sew and harvest linseed, and rot the stems to make flax fibers. That's the source of your fine linens, {s0} -- a rotting pit on the edge of a field."),
##diplomacy end+
  #SB : differentiate between two sources of dates
  ("trade_explanation_dates_village", "I tend to a grove of date palms. I hope you don't mind me saying so, {s0}, but it takes great skill to tend them, as we must climb to the tops of the palms to ensure that the trees will flower. We export the fruit far and wide, as they keep for many months when properly dried. As sweet as honey, and they grant the eater health and strength."),
  ("trade_explanation_dates_town", "I tend to a grove of date palms. We grow them using well-water, and export the fruit far and wide, as they keep for many months when properly dried. As sweet as honey, and they grant the eater health and vigor."),
  ("trade_explanation_olives", "I tend to a grove of olive trees. You can eat the fruit or preserve it in brine, but we end up sending most of it to be pressed, to be made into oil."),





  ("s10_has_reg4_needs_reg5", "{!}{s10} has {reg4}, needs {reg5}"),
  ("s14_i_hear_that_you_can_find_a_good_price_for_it_in_s15", "{s14}. I hear that you can find a good price for it in {s15}."),
  ("s1_reg1", "{!}{s1} ({reg1})"),
  ("s1_reg2", "{!}{s1} ({reg2})"),
  ("s1_reg3", "{!}{s1} ({reg3})"),
  ("s1_reg4", "{!}{s1} ({reg4})"),
  ("s1_reg5", "{!}{s1} ({reg5})"),
  ("s1_reg6", "{!}{s1} ({reg6})"),
  ("s1_reg7", "{!}{s1} ({reg7})"),
  ("s1_reg8", "{!}{s1} ({reg8})"),
  ("s1_reg9", "{!}{s1} ({reg9})"),
  ("reg13", "{!}{reg13}"),
  ("reg14", "{!}{reg14}"),
  ("reg15", "{!}{reg15}"),
  ("reg16", "{!}{reg16}"),
  ("reg17", "{!}{reg17}"),
  ("reg18", "{!}{reg18}"),
  ("reg19", "{!}{reg19}"),
  ("reg20", "{!}{reg20}"),
  ("reg21", "{!}{reg21}"),
  ("assigning_lords_to_empty_centers", "{!}ASSIGNING LORDS TO EMPTY CENTERS"),
  ("assign_lords_to_empty_centers_just_happened", "{!}Assign lords to empty centers just happened"),
  ("s4_of_the_s5_is_unassigned", "{!}{s4} of the {s5} is unassigned"),
  ("s4_of_the_s5_is_reserved_for_player", "{!}{s4} of the {s5} is reserved for player"),
  ("s4_of_the_s5_has_no_fiefs", "{!}{s4} of the {s5} has no fiefs"),
  ("s4_unassigned_centers_plus_landless_lords_=_reg4", "{!}{s4}: unassigned centers plus landless lords = {reg4}"),
  ("s4_holds_s5_in_reserve", "{!}{s4} holds {s5} in reserve"),
  ("s2s_rebellion", "{s2}'s Rebellion"),
  ("political_suggestion", "Political suggestion"),
  ("updating_volunteers_for_s4_faction_is_s5", "{!}Updating volunteers for {s4}, faction is {s5}"),
  ("shuffling_companion_locations", "{!}Shuffling companion locations"),
  ("s4_is_at_s5", "{s4} is at {s5}"), #SB : translate string
  ("instability_reg0_of_lords_are_disgruntled_reg1_are_restless", "Instability: {reg0}% of lords are disgruntled, {reg1}% are restless"),
  ("reg1shehe_is_prisoner_of_s1", "{reg1?She:He} is prisoner of {s1}."),
  ("s39_rival", "{s39} (rival)"),
  ("s40", "{!}{s40}"),
  ("s41_s39_rival", "{s41}, {s39} (rival)"),
  ("reputation_cheat_mode_only_martial_", "{!}Reputation (cheat mode only): Martial^"),
  ("reputation_cheat_mode_only_debauched_", "{!}Reputation (cheat mode only): Debauched^"),
  ("reputation_cheat_mode_only_pitiless_", "{!}Reputation (cheat mode only): Pitiless^"),
  ("reputation_cheat_mode_only_calculating_", "{!}Reputation (cheat mode only): Calculating^"),
  ("reputation_cheat_mode_only_quarrelsome_", "{!}Reputation (cheat mode only): Quarrelsome^"),
  ("reputation_cheat_mode_only_goodnatured_", "{!}Reputation (cheat mode only): Good-natured^"),
  ("reputation_cheat_mode_only_upstanding_", "{!}Reputation (cheat mode only): Upstanding^"),
  ("reputation_cheat_mode_only_conventional_", "{!}Reputation (cheat mode only): Conventional^"),
  ("reputation_cheat_mode_only_adventurous_", "{!}Reputation (cheat mode only): Adventurous^"),
  ("reputation_cheat_mode_only_romantic_", "{!}Reputation (cheat mode only): Romantic^"),
  ("reputation_cheat_mode_only_moralist_", "{!}Reputation (cheat mode only): Moralist^"),
  ("reputation_cheat_mode_only_ambitious_", "{!}Reputation (cheat mode only): Ambitious^"),
  ("reputation_cheat_mode_only_reg11_", "{!}Reputation (cheat mode only): {reg11}^"),
  ("love_interest", "love interest"),
  ("betrothed", "betrothed"),
  ("s40_s39_s2_reg0", "{!}{s40}, {s39} ({s2}, {reg0})"),
  ("other_relations_s40_", "Other relations: {s40}^"),
  ("relation_with_liege_reg0_", "Relation with liege: {reg0}^"),
  ("sense_of_security_military_reg1_court_position_reg3_", "Sense of security: military {reg1}, court position {reg3}^"),
  ("s46s45s44s48", "{!}{s46}{s45}{s44}{s48}"),
  ("political_details_s47_", "Political details:^{s47}^"),
  ("checking_volunteer_availability_script", "{!}Checking volunteer availability script"),
  ("center_relation_at_least_zero", "{!}Center relation at least zero"),
  ("relationfaction_conditions_met", "{!}Relation/faction conditions met"),
  ("troops_available", "{!}Troops available"),
  ("party_has_capacity", "{!}Party has capacity"),
  ("personality_clash_conversation_begins", "{!}Personality clash conversation begins"),
  ("personality_match_conversation_begins", "{!}Personality match conversation begins"),
  ("the_s55", "the {s55}"),

  ("travellers_on_the_road", "travellers on the road"),
  ("attack_on_travellers_found_reg3_hours_ago", "{!}Attack on travellers found, {reg3} hours ago"),
  ("trade_event_found_reg3_hours_ago", "{!}Trade event found, {reg3} hours ago"),
  ("a_short_while_ago", "a short while ago"),
  ("one_day_ago", "one day ago"),
  ("two_days_day_ago", "two days day ago"),
  ("earlier_this_week", "earlier this week"),
  ("about_a_week_ago", "about a week ago"),
  ("about_two_weeks_ago", "about two weeks ago"),
  ("several_weeks_ago", "several weeks ago"),
  ("unknown_assailants", "unknown assailants"),

  #Faction descriptors
  ("swadians", "Swadians"),
  ("vaegirs", "Vaegirs"),
  ("khergits", "Khergits"),
  ("nords", "Nords"),
  ("rhodoks", "Rhodoks"),
  ("sarranids", "Sarranids"),
  ("bandits", "bandits"),
  ("deserters", "deserters"),
  ("your_followers", "your followers"),


  ("we_have_heard_that_travellers_heading_to_s40_were_attacked_on_the_road_s46_by_s39", "We have heard that travellers heading to {s40} were attacked on the road {s46} by {s39}"),
  ("s43_s44", "{!}{s43}^{s44}"),
  ("we_have_heard_that_travellers_coming_from_s40_were_attacked_on_the_road_s46_by_s39", "We have heard that travellers coming from {s40} were attacked on the road {s46} by {s39}"),
  ("travellers_coming_from_s40_traded_here_s46", "Travellers coming from {s40} traded here {s46}"),
  ("s44", "{!}{s44}"),
  ("it_is_still_early_in_the_caravan_season_so_we_have_seen_little_tradings42", "It is still early in the caravan season, so we have seen little trading.{s42}"),
  ("there_has_been_very_little_trading_activity_here_recentlys42", "There has been very little trading activity here recently.{s42}"),
  ("there_has_some_trading_activity_here_recently_but_not_enoughs42", "There has some trading activity here recently, but not enough.{s42}"),
  ("there_has_some_trading_activity_here_recently_but_the_roads_are_dangerouss42", "There has some trading activity here recently, but the roads are dangerous.{s42}"),
  ("the_roads_around_here_are_very_dangerouss42", "The roads around here are very dangerous.{s42}"),
  ("we_have_received_many_traders_in_town_here_although_there_is_some_danger_on_the_roadss42", "We have received many traders in town here, although there is some danger on the roads.{s42}"),
  ("we_have_received_many_traders_in_town_heres42", "We have received many traders in town here.{s42}"),
  ("s44_s41", "{!}{s44}, {s41}"),
  ("s41", "{!}{s41}"),
  ("there_is_little_news_about_the_caravan_routes_to_the_towns_of_s44_and_nearby_parts_but_no_news_is_good_news_and_those_are_therefore_considered_safe", "There is little news about the caravan routes to the towns of {s44} and nearby parts. But no news is good news, and those are therefore considered safe."),
  ("s47_also_the_roads_to_the_villages_of_s44_and_other_outlying_hamlets_are_considered_safe", "{s47} Also, the roads to the villages of {s44} and other outlying hamlets are considered safe."),
  ("however_the_roads_to_the_villages_of_s44_and_other_outlying_hamlets_are_considered_safe", "However, the roads to the villages of {s44} and other outlying hamlets are considered safe."),
  ("we_have_shortages_of", "We have shortages of"),
  ("s33_s34_reg1", "{!}{s33} {s34} ({reg1}),"),
  ("we_have_adequate_stores_of_all_commodities", "We have adequate stores of all commodities"),
  ("s33_and_some_other_commodities", "{s33} and some other commodities"),
  ("the_roads_are_full_of_brigands_friend_but_that_name_in_particular_does_not_sound_familiar_good_hunting_to_you_nonetheless", "The roads are full of brigands, friend, but that name in particular does not sound familiar. Good hunting to you, nonetheless."),
  ("less_than_an_hour_ago", "less than an hour ago"),
  ("maybe_reg3_hours_ago", "maybe {reg3} hours ago"),
  ("reg3_days_ago", "{reg3} days ago"),
  ("youre_in_luck_we_sighted_those_bastards_s16_near_s17_hurry_and_you_might_be_able_to_pick_up_their_trail_while_its_still_hot", "You're in luck. We sighted those bastards {s16} near {s17}. Hurry, and you might be able to pick up their trail while it's still hot."),
  ("you_speak_of_claims_to_the_throne_good_there_is_nothing_id_rather_do_than_fight_for_a_good_cause", "You speak of claims to the throne. Good. There is nothing I'd rather do than fight for a good cause."),
  ("you_speak_of_claims_to_the_throne_well_there_is_nothing_id_rather_do_than_fight_for_a_good_cause_but_the_claim_you_make_seems_somewhat_weak", "You speak of claims to the throne. Well, there is nothing I'd rather do than fight for a good cause, but the claim you make seems somewhat weak."),
  ("i_am_pleased_that_you_speak_of_upholding_my_ancient_rights_which_are_sometimes_trod_upon_in_these_sorry_days", "I am pleased that you speak of upholding my ancient rights, which are sometimes trod upon in these sorry days."),
##diplomacy start+: change "king" to "{s14}" #("i_am_pleased_that_you_speak_of_upholding_my_ancient_rights_but_sometimes_men_make_pledges_before_they_are_king_which_they_cannot_keep_once_they_take_the_throne", "I am pleased that you speak of upholding my ancient rights. But sometimes men make pledges before they are king, which they cannot keep once they take the throne."),
  ("i_am_pleased_that_you_speak_of_upholding_my_ancient_rights_but_sometimes_men_make_pledges_before_they_are_king_which_they_cannot_keep_once_they_take_the_throne", "I am pleased that you speak of upholding my ancient rights. But sometimes men make pledges before they are {s14}, which they cannot keep once they take the throne."),
##Change "swing my sword" to "{s14}"
#  ("you_speak_of_protecting_the_commons_well_i_supposed_thats_good_but_sometimes_the_commons_overstep_their_boundaries_im_more_concerned_that_your_claim_be_legal_so_i_can_swing_my_sword_with_a_good_conscience", "You speak of protecting the commons. Well, I supposed that's good, but sometimes the commons overstep their boundaries. I'm more concerned that your claim be legal, so I can swing my sword with a good conscience."),
  ("you_speak_of_protecting_the_commons_well_i_supposed_thats_good_but_sometimes_the_commons_overstep_their_boundaries_im_more_concerned_that_your_claim_be_legal_so_i_can_swing_my_sword_with_a_good_conscience", "You speak of protecting the commons. Well, I supposed that's good, but sometimes the commons overstep their boundaries. I'm more concerned that your claim be legal, so I can {s14} with a good conscience."),
##diplomacy end+
  ("you_speak_of_giving_me_land_good_i_ask_for_no_more_than_my_due", "You speak of giving me land. Good. I ask for no more than my due."),
  ("you_speak_of_giving_me_land_unfortunately_you_are_not_wellknown_for_rewarding_those_to_whom_you_have_made_such_offers", "You speak of giving me land. Unfortunately, you are not well-known for rewarding those to whom you have made such offers."),
  ("you_speak_of_unifying_calradia_well_i_believe_that_well_always_be_fighting__its_important_that_we_fight_for_a_rightful_cause", "You speak of unifying Calradia. Well, I believe that we'll always be fighting - it's important that we fight for a rightful cause."),
  ("you_talk_of_claims_to_the_throne_but_i_leave_bickering_about_legalities_to_the_lawyers_and_clerks", "You talk of claims to the throne, but I leave bickering about legalities to the lawyers and clerks."),
##diplomacy start+: change "king" to "{s14}"
#  ("you_speak_of_ruling_justly_hah_ill_believe_theres_such_a_thing_as_a_just_king_when_i_see_one", "You speak of ruling justly. Hah! I'll believe there's such a thing as a just king when I see one."),
  ("you_speak_of_ruling_justly_hah_ill_believe_theres_such_a_thing_as_a_just_king_when_i_see_one", "You speak of ruling justly. Hah! I'll believe there's such a thing as a just {s14} when I see one."),
#  ("you_spoke_of_protecting_the_rights_of_the_nobles_if_you_did_youd_be_the_first_king_to_do_so_in_a_very_long_time", "You spoke of protecting the rights of the nobles. If you did, you'd be the first king to do so in a very long time."),
  ("you_spoke_of_protecting_the_rights_of_the_nobles_if_you_did_youd_be_the_first_king_to_do_so_in_a_very_long_time", "You spoke of protecting the rights of the nobles. If you did, you'd be the first {s14} to do so in a very long time."),
##diplomacy end+
  ("you_speak_of_giving_me_land_ay_well_lets_see_if_you_deliver", "You speak of giving me land. Ay, well, let's see if you deliver."),
  ("you_speak_of_giving_me_land_bah_youre_not_known_for_delivering_on_your_pledges", "You speak of giving me land. Bah. You're not known for delivering on your pledges."),
  ("you_speak_of_unifying_calradia_well_youve_done_a_good_job_at_making_calradia_bend_its_knee_to_you_so_maybe_thats_not_just_talk", "You speak of unifying Calradia. Well, you've done a good job at making Calradia bend its knee to you, so maybe that's not just talk."),
  ("you_speak_of_unifying_calradia_id_be_impressed_if_i_thought_you_could_do_it_but_unfortunately_you_dont", "You speak of unifying Calradia. I'd be impressed if I thought you could do it. But unfortunately, you don't."),
  ("you_speak_of_claims_to_the_throne_well_any_peasant_can_claim_to_be_a_kings_bastard", "You speak of claims to the throne. Well, any peasant can claim to be a king's bastard"),
  ("well_its_a_fine_thing_to_court_the_commons_with_promises_but_what_do_you_have_to_offer_me", "Well, it's a fine thing to court the commons with promises, but what do you have to offer me?"),
##diplomacy start+: change "lords" to "{s15}", and "lord" to "{s14}"
#  ("you_speak_of_protecting_the_rights_of_lords_that_would_make_a_fine_change_if_my_rights_as_lord_would_be_respected", "You speak of protecting the rights of lords. That would make a fine change, if my rights as lord would be respected."),
  ("you_speak_of_protecting_the_rights_of_lords_that_would_make_a_fine_change_if_my_rights_as_lord_would_be_respected", "You speak of protecting the rights of {s15}. That would make a fine change, if my rights as {s14} would be respected."),
#  ("you_speak_of_protecting_the_rights_of_lords_that_would_make_a_fine_change_if_my_rights_as_lord_would_be_respected_however_it_is_easy_for_you_to_make_promises_while_you_are_weak_that_you_have_no_intention_of_keeping_when_you_are_strong", "You speak of protecting the rights of lords. That would make a fine change, if my rights as lord would be respected. However, it is easy for you to make promises while you are weak, that you have no intention of keeping when you are strong."),
  ("you_speak_of_protecting_the_rights_of_lords_that_would_make_a_fine_change_if_my_rights_as_lord_would_be_respected_however_it_is_easy_for_you_to_make_promises_while_you_are_weak_that_you_have_no_intention_of_keeping_when_you_are_strong", "You speak of protecting the rights of {s15}. That would make a fine change, if my rights as {s14} would be respected. However, it is easy for you to make promises while you are weak, that you have no intention of keeping when you are strong."),
##diplomacy end+
  ("you_speak_of_giving_me_land_well_my_family_is_of_ancient_and_noble_lineage_so_you_promise_me_no_more_than_my_due_still_your_gesture_is_appreciated", "You speak of giving me land. Well, my family is of ancient and noble lineage, so you promise me no more than my due. Still, your gesture is appreciated."),
  ("you_speak_of_giving_me_land_well_you_make_that_pledge_but_i_am_not_impressed", "You speak of giving me land. Well, you make that pledge, but I am not impressed."),
  ("you_speak_of_unifying_calradia_well_much_of_this_land_now_bends_its_knee_to_you_so_perhaps_that_is_not_just_talk", "You speak of unifying Calradia. Well, much of this land now bends its knee to you, so perhaps that is not just talk."),
  ("you_speak_of_unifying_calradia_but_right_now_yours_is_just_one_squabbling_faction_among_many", "You speak of unifying Calradia, but right now yours is just one squabbling faction among many."),
  ("you_speak_of_claims_well_no_offense_but_a_claim_unsupported_by_might_rarely_prospers", "You speak of claims. Well, no offense, but a claim unsupported by might rarely prospers."),
  ("you_speak_of_protecting_the_commons_well_i_suppose_that_will_make_for_a_more_prosperous_realm_ive_always_tried_to_treat_my_peasants_decently_saves_going_to_bed_worrying_about_whether_youll_wake_up_with_the_roof_on_fire", "You speak of protecting the commons. Well, I suppose that will make for a more prosperous realm. I've always tried to treat my peasants decently. Saves going to bed worrying about whether you'll wake up with the roof on fire."),
  ("you_speak_of_protecting_the_commons_very_well_but_remember_that_peasants_are_more_likely_to_cause_trouble_if_you_make_promises_then_dont_deliver_than_if_you_never_made_the_promise_in_the_first_place", "You speak of protecting the commons. Very well. But remember that peasants are more likely to cause trouble if you make promises then don't deliver, than if you never made the promise in the first place."),
##diplomacy start+: change "lords" to "{s14}", and "king" to "{s15}"
#  ("you_speak_of_protecting_the_rights_of_lords_good_youd_be_well_advised_to_do_that__men_fight_better_for_a_king_wholl_respect_their_rights", "You speak of protecting the rights of lords. Good. You'd be well advised to do that -- men fight better for a king who'll respect their rights."),
  ("you_speak_of_protecting_the_rights_of_lords_good_youd_be_well_advised_to_do_that__men_fight_better_for_a_king_wholl_respect_their_rights", "You speak of protecting the rights of {s14}. Good. You'd be well advised to do that -- men fight better for a {s15} who'll respect their rights."),
#  ("you_speak_of_protecting_the_rights_of_lords_very_well_but_remember__failing_to_keep_promises_which_you_made_while_scrambling_up_the_throne_is_the_quickest_way_to_topple_off_of_it_once_you_get_there", "You speak of protecting the rights of lords. Very well. But remember -- failing to keep promises which you made while scrambling up the throne is the quickest way to topple off of it once you get there."),
  ("you_speak_of_protecting_the_rights_of_lords_very_well_but_remember__failing_to_keep_promises_which_you_made_while_scrambling_up_the_throne_is_the_quickest_way_to_topple_off_of_it_once_you_get_there", "You speak of protecting the rights of {s14}. Very well. But remember -- failing to keep promises which you made while scrambling up the throne is the quickest way to topple off of it once you get there."),
##diplomacy end+
  ("you_speak_of_giving_me_land_very_good_but_often_i_find_that_when_a_man_makes_too_many_promises_trying_to_get_to_the_top_he_has_trouble_keeping_them_once_he_reaches_it", "You speak of giving me land. Very good, but often I find that when a man makes too many promises trying to get to the top, he has trouble keeping them once he reaches it."),
  ("you_speak_of_unifying_calradia_well_many_have_said_that_you_might_very_well_be_the_one_to_do_it", "You speak of unifying Calradia. Well, many have said that, you might very well be the one to do it."),
  ("you_speak_of_unifying_calradia_well_all_the_kings_say_that_im_not_sure_that_you_will_succeed_while_they_fail", "You speak of unifying Calradia. Well, all the kings say that. I'm not sure that you will succeed while they fail."),
  ("you_speak_of_claims_do_you_think_i_care_for_the_nattering_of_lawyers", "You speak of claims. Do you think I care for the nattering of lawyers?"),
##diplomacy start+
##Replace "swineherd" with "{s14}"
#  ("you_speak_of_protecting_the_commons_how_kind_of_you_i_shall_tell_my_swineherd_all_about_your_sweet_promises_no_doubt_he_will_become_your_most_faithful_vassal", "You speak of protecting the commons. How kind of you! I shall tell my swineherd all about your sweet promises. No doubt he will become your most faithful vassal."),
  ("you_speak_of_protecting_the_commons_how_kind_of_you_i_shall_tell_my_swineherd_all_about_your_sweet_promises_no_doubt_he_will_become_your_most_faithful_vassal", "You speak of protecting the commons. How kind of you! I shall tell my {s14} all about your sweet promises. No doubt he will become your most faithful vassal."),
##Replace "lords" with "{s14}"
#  ("you_speak_of_protecing_the_rights_of_lords_such_sweet_words_but_ill_tell_you_this__the_only_rights_that_are_respected_in_this_world_are_the_rights_to_dominate_whoever_is_weaker_and_to_submit_to_whoever_is_stronger", "You speak of protecing the rights of lords. Such sweet words! But I'll tell you this -- the only rights that are respected in this world are the rights to dominate whoever is weaker, and to submit to whoever is stronger."),
  ("you_speak_of_protecing_the_rights_of_lords_such_sweet_words_but_ill_tell_you_this__the_only_rights_that_are_respected_in_this_world_are_the_rights_to_dominate_whoever_is_weaker_and_to_submit_to_whoever_is_stronger", "You speak of protecing the rights of {s14}. Such sweet words! But I'll tell you this -- the only rights that are respected in this world are the rights to dominate whoever is weaker, and to submit to whoever is stronger."),
##diplomacy end+
  ("you_speak_of_giving_me_land_yes_very_good__but_you_had_best_deliver", "You speak of giving me land. Yes, very good -- but you had best deliver."),
  ("you_speak_of_giving_me_land_hah_perhaps_all_those_others_to_whom_you_promised_lands_will_simply_step_aside", "You speak of giving me land. Hah! Perhaps all those others to whom you promised lands will simply step aside?"),
  ("you_speak_of_unifying_calradia_you_may_indeed_humble_the_other_kings_of_this_land_and_in_that_case_i_would_hope_that_you_would_remember_me_as_your_faithful_servant", "You speak of unifying Calradia. You may indeed humble the other kings of this land, and in that case I would hope that you would remember me as your faithful servant."),
  ("you_speak_of_unifying_calradia_but_you_are_weak_and_i_think_that_you_will_remain_weak", "You speak of unifying Calradia. But you are weak, and I think that you will remain weak."),
##diplomacy start+: replace "king" with "{s14}", and remove extraneous space
#  ("you_speak_of_claims_its_good_for_a_king_to_have_a_strong_claim_although_admittedly_im_more_concerned_that_he_rules_just_ly_than_with_legalities_anyway_your_claim_seems_wellfounded_to_me", "You speak of claims. It's good for a king to have a strong claim, although admittedly I'm more concerned that he rules just ly than with legalities. Anyway, your claim seems well-founded to me."),
  ("you_speak_of_claims_its_good_for_a_king_to_have_a_strong_claim_although_admittedly_im_more_concerned_that_he_rules_just_ly_than_with_legalities_anyway_your_claim_seems_wellfounded_to_me", "You speak of claims. It's good for a {s14} to have a strong claim, although admittedly I'm more concerned that he rules justly than with legalities. Anyway, your claim seems well-founded to me."),
##diplomacy end+
  ("you_speak_of_claims_but_your_claim_seems_a_bit_weak_to_me", "You speak of claims, but your claim seems a bit weak to me."),
  ("you_speak_of_protecting_the_commons_i_like_that_my_tenants_are_a_happy_lot_i_think_but_i_hear_of_others_in_other_estates_that_arent_so_fortunate", "You speak of protecting the commons. I like that. My tenants are a happy lot, I think, but I hear of others in other estates that aren't so fortunate."),
  ("you_speak_of_protecting_the_commons_im_glad_to_hear_you_say_that_but_do_me_a_favor__dont_promise_the_commons_anything_you_cant_deliver_thats_a_sure_way_to_get_them_to_rebel_and_it_breaks_my_heart_to_have_to_put_them_down", "You speak of protecting the commons. I'm glad to hear you say that. But do me a favor -- don't promise the commons anything you can't deliver. That's a sure way to get them to rebel, and it breaks my heart to have to put them down."),
##diplomacy start+: replace "lords" with "{s14}", and "king" with "{s15}"
#  ("you_speak_of_protecting_the_rights_of_lords_well_very_good_i_suppose_but_you_know__we_lords_can_take_of_ourselves_its_the_common_folk_who_need_a_strong_king_to_look_out_for_them_to_my_mind", "You speak of protecting the rights of lords. Well, very good, I suppose. But you know -- we lords can take of ourselves. It's the common folk who need a strong king to look out for them, to my mind."),
  ("you_speak_of_protecting_the_rights_of_lords_well_very_good_i_suppose_but_you_know__we_lords_can_take_of_ourselves_its_the_common_folk_who_need_a_strong_king_to_look_out_for_them_to_my_mind", "You speak of protecting the rights of {s14}. Well, very good, I suppose. But you know -- we {s14} can take of ourselves. It's the common folk who need a strong {s15} to look out for them, to my mind."),
##diplomacy end+
  ("you_speak_of_giving_me_land_its_kind_of_you_really_though_that_is_not_necessary", "You speak of giving me land. It's kind of you. Really, though, that is not necessary."),
##diplomacy start+: replace "by the sword" with "by the {s14}"
#  ("you_speak_of_unifying_calradia_well_maybe_you_can_unite_this_land_by_the_sword_but_im_not_sure_that_this_will_make_you_a_good_ruler", "You speak of unifying Calradia. Well, maybe you can unite this land by the sword. But I'm not sure that this will make you a good ruler."),
  ("you_speak_of_unifying_calradia_well_maybe_you_can_unite_this_land_by_the_sword_but_im_not_sure_that_this_will_make_you_a_good_ruler", "You speak of unifying Calradia. Well, maybe you can unite this land by the {s14}. But I'm not sure that this will make you a good ruler."),
##Replace "king" with "{s14}"
#  ("you_speak_of_claims_a_king_must_have_a_strong_legal_claim_for_there_not_to_be_chaos_in_the_realm_and_yours_is_wellestablished", "You speak of claims. A king must have a strong legal claim for there not to be chaos in the realm, and yours is well-established."),
  ("you_speak_of_claims_a_king_must_have_a_strong_legal_claim_for_there_not_to_be_chaos_in_the_realm_and_yours_is_wellestablished", "You speak of claims. A {s14} must have a strong legal claim for there not to be chaos in the realm, and yours is well-established."),
#  ("you_speak_of_claims_a_king_must_have_a_strong_legal_claim_for_there_not_to_be_chaos_in_the_realm_but_your_claim_is_not_so_strong", "You speak of claims. A king must have a strong legal claim for there not to be chaos in the realm, but your claim is not so strong."),
  ("you_speak_of_claims_a_king_must_have_a_strong_legal_claim_for_there_not_to_be_chaos_in_the_realm_but_your_claim_is_not_so_strong", "You speak of claims. A {s14} must have a strong legal claim for there not to be chaos in the realm, but your claim is not so strong."),
##Replace "king" with "{s14}", and "lords" with "{s15}"
#  ("you_speak_of_protecting_the_rights_of_lords_it_is_of_course_important_that_a_king_respect_the_rights_of_his_vassals_although_i_worry_that_a_king_who_took_a_throne_without_proper_cause_would_not_rule_with_justice", "You speak of protecting the rights of lords. It is of course important that a king respect the rights of his vassals, although I worry that a king who took a throne without proper cause would not rule with justice."),
  ("you_speak_of_protecting_the_rights_of_lords_it_is_of_course_important_that_a_king_respect_the_rights_of_his_vassals_although_i_worry_that_a_king_who_took_a_throne_without_proper_cause_would_not_rule_with_justice", "You speak of protecting the rights of lords. It is of course important that a {s14} respect the rights of his vassals, although I worry that a {s14} who took a throne without proper cause would not rule with justice."),
#  ("you_speak_of_protecting_the_rights_of_lords_it_is_of_course_important_that_a_king_respect_the_rights_of_his_vassals_however_i_would_like_to_know_that_you_would_indeed_deliver_on_your_promises", "You speak of protecting the rights of lords. It is of course important that a king respect the rights of his vassals. However, I would like to know that you would indeed deliver on your promises."),
  ("you_speak_of_protecting_the_rights_of_lords_it_is_of_course_important_that_a_king_respect_the_rights_of_his_vassals_however_i_would_like_to_know_that_you_would_indeed_deliver_on_your_promises", "You speak of protecting the rights of {s15}. It is of course important that a {s14} respect the rights of his vassals. However, I would like to know that you would indeed deliver on your promises."),

#  ("you_speak_of_protecting_the_commons_i_would_be_pleased_to_serve_a_king_who_respected_the_rights_of_his_subjects_although_i_worry_that_a_king_who_took_a_throne_without_proper_cause_would_not_rule_with_justice", "You speak of protecting the commons. I would be pleased to serve a king who respected the rights of his subjects, although I worry that a king who took a throne without proper cause would not rule with justice."),
  ("you_speak_of_protecting_the_commons_i_would_be_pleased_to_serve_a_king_who_respected_the_rights_of_his_subjects_although_i_worry_that_a_king_who_took_a_throne_without_proper_cause_would_not_rule_with_justice", "You speak of protecting the commons. I would be pleased to serve a {s14} who respected the rights of his subjects, although I worry that a {s14} who took a throne without proper cause would not rule with justice."),

#  ("you_speak_of_protecting_the_commons_i_would_be_pleased_to_serve_a_king_who_respected_the_rights_of_his_subjects_however_i_would_like_to_know_that_you_would_indeed_deliver_on_your_promises", "You speak of protecting the commons. I would be pleased to serve a king who respected the rights of his subjects. However, I would like to know that you would indeed deliver on your promises."),
  ("you_speak_of_protecting_the_commons_i_would_be_pleased_to_serve_a_king_who_respected_the_rights_of_his_subjects_however_i_would_like_to_know_that_you_would_indeed_deliver_on_your_promises", "You speak of protecting the commons. I would be pleased to serve a {s14} who respected the rights of his subjects. However, I would like to know that you would indeed deliver on your promises."),
##diplomacy end+ (finish adding alternate cultural terms)
  ("i_am_not_swayed_by_promises_of_reward", "I am not swayed by promises of reward"),
  ("you_speak_of_unifying_calradia_it_would_be_good_to_bring_peace_to_the_realm_and_i_believe_that_you_are_strong_enough_to_do_so", "You speak of unifying Calradia. It would be good to bring peace to the realm, and I believe that you are strong enough to do so."),
  ("you_speak_of_unifying_calradia_it_would_be_good_to_bring_peace_the_realm_but_with_your_kingdom_in_its_current_state_i_worry_that_you_are_just_bringing_more_discord", "You speak of unifying Calradia. It would be good to bring peace the realm, but with your kingdom in its current state, I worry that you are just bringing more discord."),
##diplomacy start+ duplicate definition of s15...
#at the very least, fix its defects
#  ("s15", "{!}{s15"),
  ("s15", "{!}{s15}"),
##diplomacy end+
  ("my_s11_s15", "my {s11} {s15}"),
  ("stop_gap__s15_is_the_rival_of_s16", "{!}STOP GAP - {s15} is the rival of {s16}"),
  ("my_s11_s18", "My {s11} {s18}"),
  ("the_socalled_s11_s18", "The so-called {s11} {s18}"),
##diplomacy start+ make pronouns gender-correct
#reg3 refers to the gender of the lord being spoken about, reg65 is the speaker's
  ("s18_would_cheat_me_of_my_inheritance_by_heaven_i_know_my_rights_and_im_not_going_to_back_down", "{s18} would cheat me of my inheritance. By heaven, I know my rights, and I'm not going to back down."),
  ("s18_once_questioned_my_honour_and_my_bravery_i_long_for_the_day_when_i_can_meet_him_in_battle_and_make_him_retract_his_statement", "{s18} once questioned my honour and my bravery. I long for the day when I can meet {reg3?her:him} in battle, and make {reg3?her:him} retract {reg3?her:his} statement."),
  ("s18_once_questioned_my_judgment_in_battle_by_heaven_would_he_have_us_shirk_our_duty_to_smite_our_sovereigns_foes", "{s18} once questioned my judgment in battle. By heaven, would {reg3?she:he} have us shirk our duty to smite our sovereign's foes?"),
  ("s18_seems_to_think_he_has_the_right_to_some_of_my_property_well_he_does_not", "{s18} seems to think {reg3?she:he} has the right to some of my property. Well, {reg3?she:he} does not."),
  ("s18_once_took_something_i_said_amiss_stubborn_bastard_wont_give_it_up_and_keeps_trying_to_get_me_to_recant_my_words", "{s18} once took something I said amiss. Stubborn {reg3?bitch:bastard} won't give it up, and keeps trying to get me to recant my words."),
  ("s18_is_a_crafty_weasel_and_i_dont_trust_him_one_bit", "{s18} is a crafty weasel, and I don't trust {reg3?her:him} one bit."),
  ("s18_i_despite_him_he_puts_on_such_a_nauseating_display_of_virtue_and_thinks_nothing_of_insulting_his_betters", "{s18}? I despise {reg3?her:him}. {reg3?She:He} puts on such a nauseating display of virtue, and thinks nothing of insulting {reg3?her:his} betters."),
  ("s18_entered_into_a_little_deal_with_me_and_is_now_trying_to_wriggle_out_of_it", "{s18} entered into a little deal with me and is now trying to wriggle out of it."),
  ("s18_once_ran_an_errand_for_me_and_now_thinks_i_owe_him_something_i_owe_his_ilk_nothing", "{s18} once ran an errand for me, and now thinks I owe {reg3?her:him} something. I owe {reg3?her:his} ilk nothing."),
  ("s18_is_soft_and_weak_and_not_fit_to_govern_a_fief_and_i_have_always_detested_him", "{s18} is soft, and weak, and not fit to govern a fief, and I have always detested {reg3?her:him}."),
  ("s18_is_a_quarrelsome_oaf_and_a_liability_in_my_opinion_and_ive_let_him_know_as_much", "{s18} is a quarrelsome oaf and a liability, in my opinion, and I've let {reg3?her:him} know as much."),
  ("s18_i_am_sorry_to_say_is_far_too_softhearted_a_man_to_be_given_any_kind_of_responsibility_his_chivalry_will_allow_the_enemy_to_flee_to_fight_another_day_and_will_cost_the_lives_of_my_own_faithful_men", "{s18}, I am sorry to say, is far too softhearted a {reg3?woman:man} to be given any kind of responsibility. {reg3?Her:His} chivalry will allow the enemy to flee to fight another day, and will cost the lives of my own faithful {reg65?soldiers:men}."),
  ("s18_seems_to_have_something_against_me_for_some_reason_i_dont_like_to_talk_ill_of_people_but_i_think_hes_can_be_a_bit_of_a_cad_sometimes", "{s18} seems to have something against me, for some reason. I don't like to talk ill of people, but I think {reg3?she:he} can be a bit of a cad, sometimes."),#also removed improper "'s"
  ("s18_has_always_treated_me_contemptuously_although_i_have_done_him_no_wrong", "{s18} has always treated me contemptuously, although I have done {reg3?her:him} no wrong."),
  ("s18_is_thoroughly_dishonorable_and_a_compulsive_spinner_of_intrigues_which_i_fear_will_drag_us_into_wars_or_incite_rebellions", "{s18} is thoroughly dishonorable, and a compulsive spinner of intrigues which I fear will drag us into wars or incite rebellions."),
  ("s18_disappoints_me_i_once_scolded_for_his_rashness_in_battle_and_he_took_offense_i_do_not_care_to_apologize_for_my_efforts_to_save_his_life_and_the_lives_of_his_men", "{s18} disappoints me. I once scolded {reg3?her:him} for {reg3?her:his} rashness in battle, and {reg3?she:he} took offense. I do not care to apologize for my efforts to save {reg3?her:his} life, and the lives of {reg3?her:his} {reg3?soldiers:men}."),#also added missing pronoun
  ("s18_squanders_money_and_carouses_in_a_way_most_unbefitting_a_noble_by_doing_so_he_disgraces_us_all", "{s18} squanders money and carouses in a way most unbefitting a noble. By doing so, {reg3?she:he} disgraces us all."),
  ("s18_has_been_speaking_ill_of_me_behind_my_back_or_so_they_say", "{s18} has been speaking ill of me behind my back, or so they say."),
  ("s18_is_a_disgrace_reg3shehe_consorts_with_merchants_lends_money_at_interest_uses_coarse_language_and_shows_no_attempt_to_uphold_the_dignity_of_the_honor_bestowed_upon_reg3herhim", "{s18} is a disgrace. {reg3?She:He} consorts with merchants, lends money at interest, uses coarse language, and shows no attempt to uphold the dignity of the honor bestowed upon {reg3?her:him}."),
  ("s18_has_condemned_me_for_engaging_in_commerce_what_could_possibly_be_wrong_with_that", "{s18} has condemned me for engaging in commerce. What could possibly be wrong with that?"),
  ("s18_i_have_heard_has_been_encouraging_seditious_ideas_among_the_peasantry__a_foolish_move_which_endangers_us_all", "{s18}, I have heard, has been encouraging seditious ideas among the peasantry -- a foolish move which endangers us all."),
  ("s18_has_called_me_out_for_the_way_i_deal_with_my_tenants_well_so_be_it_if_i_teach_them_that_they_are_the_equal_of_anyone_with_socalled_gentle_blood_what_is_it_to_reg3herhim", "{s18} has called me out for the way I deal with my tenants. Well, so be it. If I teach them that they are the equal of anyone with so-called 'gentle' blood, what is it to {reg3?her:him}?"),
  ("a_most_gallant_gentleman_who_knows_how_to_treat_a_lady", "a most gallant {reg3?gentlewoman:gentleman}, who knows how to treat a {reg65?lady:young man}"),
  ("a_base_cad", "a base cad"),
  ("a_man_who_treats_me_as_his_equal_which_is_rare", "{reg3?{reg65?someone:a woman}:a man} who treats me as {reg3?her:his} equal, which is rare"),
  ("appears_to_value_me_with_his_estate_and_his_horse_as_prizes_worth_having", "appears to value me with {reg3?her:his} estate and {reg3?her:his} horse as prizes worth having"),
  ("a_bit_dull_but_what_can_you_expect", "a bit dull, but what can you expect..."),
  ("the_man_whom_destiny_intends_for_me", "the {reg3?one:man} whom destiny intends for me"),
  ("is_not_right_for_me__i_cannot_say_why_but_he_makes_my_skin_crawl", "is not right for me - I cannot say why, but {reg3?she:he} makes my skin crawl"),
  ("is_a_man_who_clearly_intends_to_make_his_mark_in_the_world", "is a {reg3?woman:man} who clearly intends to make {reg3?her:his} mark in the world"),
  ("is_a_layabout_a_naif_prey_for_others_who_are_cleverer_than_he", "is a lay-about, a naif, prey for others who are cleverer than {reg3?she:he}"),
  ("is_a_man_of_stalwart_character", "is a {reg3?woman:man} of stalwart character"),
  ("appears_to_be_a_man_of_low_morals", "appears to be a {reg3?woman:man} of low morals"),
  ("appears_to_be_a_man_who_lacks_selfdiscipline", "appears to be a {reg3?woman:man} who lacks self-discipline"),
##diplomacy end+
  ("check_reg8_s4_reconciles_s5_and_s6_", "{!}Check #{reg8}: {s4} reconciles {s5} and {s6} "),
  ("diagnostic__player_should_receive_consultation_quest_here_if_not_already_active", "{!}Diagnostic -- Player should receive consultation quest here, if not already active"),
  ("check_reg8_s4_rules_in_s5s_favor_in_quarrel_with_s6_", "{!}Check #{reg8}: {s4} rules in {s5}'s favor in quarrel with {s6} "),
  ("check_reg8_new_rivalry_generated_between_s5_and_s6", "{!}Check #{reg8}: New rivalry generated between {s5} and {s6}"),
  ("check_reg8_s5_attempts_to_win_over_s6", "{!}Check #{reg8}: {s5} attempts to win over {s6}"),
  ("s1_has_no_lords", "{!}{s1} has no lords"),
  ("do_political_consequences_for_s4_victory_over_s5", "{!}Do political consequences for {s4} victory over {s5}"),
  ("bandits_attacked_a_party_on_the_roads_so_a_bounty_is_probably_available", "Bandits attacked a party on the roads, so a bounty is probably available"),
  ("travellers_attacked_on_road_from_s15_to_s16", "{!}Travellers attacked on road from {s15} to {s16}"),
  ("s15_shares_joy_of_victory_with_s16", "{!}{s15} shares joy of victory with {s16}"),
  ("faction_marshall_s15_involved_in_defeat", "{!}Faction marshall {s15} involved in defeat"),
  ("player_faction_marshall_involved_in_defeat", "{!}Player faction marshall involved in defeat"),
  ("s14_of_s15_defeated_in_battle_loses_one_point_relation_with_liege", "{!}{s14} of {s15} defeated in battle, loses one point relation with liege"),
  ("s14_defeated_in_battle_by_s15_loses_one_point_relation", "{!}{s14} defeated in battle by {s15}, loses one point relation"),
  ("s14_blames_s15_for_defeat", "{!}{s14} blames {s15} for defeat"),
  ("s32_is_undeclared_rebel", "{!}{s32} is undeclared rebel"),
  ("small_bonus_for_no_base", "{!}Small bonus for no base"),
  ("s15_considered_member_of_faction_s20_weight_of_reg15", "{!}{s15} considered member of faction {s20}, weight of {reg15}"),
  ("checking_for_recruitment_argument_reg24", "{!}Checking for recruitment argument #{reg24}"),
  ("g_talk_troop_s20_evaluates_being_vassal_to_s22_of_s21", "{!} G talk troop {s20} evaluates being vassal to {s22} of {s21}"),
  ("base_result_for_security_reg1", "{!}Base result for security: {reg1}"),
  ("result_for_security_weighted_by_personality_reg2", "{!}Result for security weighted by personality: {reg2}"),
  ("base_result_for_political_connections_reg3", "{!}Base result for political connections: {reg3}"),
  ("result_for_political_connections_weighted_by_personality_reg4", "{!}Result for political connections weighted by personality: {reg4}"),
  ("result_for_argument_strength_reg7", "{!}Result for argument strength: {reg7}"),
  ("result_for_argument_appeal_reg17", "{!}Result for argument appeal: {reg17}"),
  ("combined_result_for_argument_modified_by_persuasion_reg8", "{!}Combined result for argument modified by persuasion: {reg8}"),
  ("base_changing_sides_penalty_reg9", "{!}Base changing sides penalty: {reg9}"),
  ("changing_sides_penalty_weighted_by_personality_reg10", "{!}Changing sides penalty weighted by personality: {reg10}"),
  ("combined_bonuses_and_penalties_=_reg0", "{!}Combined bonuses and penalties = {reg0}"),
  ("intrigue_test_troop_party_is_active", "{!}Intrigue test: Troop party is active"),
  ("intrigue_test_troop_party_is_not_in_battle", "{!}Intrigue test: Troop party is not in battle"),
  ("intrigue_test_troop_is_not_prisoner", "{!}Intrigue test: Troop is not prisoner"),
  ("intrigue_test_troop_is_nearby", "{!}Intrigue test: Troop is nearby"),
  ("s20_relation_with_s15_changed_by_reg4_to_reg14", "{!}{s20} relation with {s15} changed by {reg4} to {reg14}"),
  ("total_additions_reg4", "Total additions: {reg4}"),
  ("total_subtractions_reg4", "Total subtractions: {reg4}"),
  ("checking_lord_reactions_in_s15", "{!}Checking lord reactions in {s15}"),
  ("s14_protests_the_appointment_of_s15_as_marshall", "{!}{s14} protests the appointment of {s15} as marshall"),
  ("s11_relocates_to_s10", "{s11} relocates to {s10}."),
  ("checking_s3_at_s5_with_s11_relationship_with_s4_score_reg0", "{!}Checking {s3} at {s5} with {s11} relationship with {s4} (score {reg0})"),
  ("s3_feast_concludes_at_s4", "{!}{s3} feast concludes at {s4}"),
  ("attendance_reg3_nobles_out_of_reg4", "{!}Attendance: {reg3} nobles out of {reg4}"),
  ("romantic_chemistry_reg0", "{!}DEBUG : Romantic chemistry: {reg0}"),
  ("personality_modifier_reg2", "{!}Personality modifier: {reg2}"),
  ("renown_modifier_reg3", "{!}Renown modifier: {reg3}"),
  ("final_score_reg0", "{!}Final score: {reg0}"),
  ("s4_pursues_suit_with_s5_in_s7", "{!}{s4} pursues suit with {s5} in {s7}"),
  ("note__favor_event_logged", "{!}NOTE - Favor event logged"),
  ("result_lady_forced_to_agree_to_engagement", "{!}Result: lady forced to agree to engagement"),
  ("result_lady_rejects_suitor", "{!}Result: lady rejects suitor"),
  ("result_happy_engagement_between_s4_and_s5", "{!}Result: happy engagement between {s4} and {s5}"),
  ("result_s4_elopes_with_s5", "{!}Result: {s4} elopes with {s5}"),
  ("result_s4_reluctantly_agrees_to_engagement_with_s5", "{!}Result: {s4} reluctantly agrees to engagement with {s5}"),
  ("result_stalemate_patience_roll_=_reg3", "{!}Result: stalemate, patience roll = {reg3}"),
  ("s3_marries_s4_at_s5", "{s3} marries {s4} at {s5}"),
  ("_i_must_attend_to_this_matter_before_i_worry_about_the_affairs_of_the_realm", " I must attend to this matter before I worry about the affairs of the realm."),
  ("the_other_matter_took_precedence", "The other matter took precedence."),
  ("i_cannot_leave_this_fortress_now_as_it_is_under_siege", "I cannot leave this fortress now, as it is under siege."),
  ("after_all_we_are_under_siege", "After all, we are under siege."),
  ("we_are_not_strong_enough_to_face_the_enemy_out_in_the_open", "We are not strong enough to face the enemy out in the open."),
  ("i_should_probably_seek_shelter_behind_some_stout_walls", "I should probably seek shelter behind some stout walls."),
  ("enemies_are_reported_to_be_nearby_and_we_should_stand_ready_to_either_man_the_walls_or_sortie_out_to_do_battle", "Enemies are reported to be nearby, and we should stand ready to either man the walls or sortie out to do battle."),
  ("the_enemy_is_nearby", "The enemy is nearby."),
  ("as_the_marshall_i_am_assembling_the_army_of_the_realm", "As the marshal, I am assembling the army of the realm."),
  ("as_the_marshall_i_am_assembling_the_army_of_the_realm_and_travel_to_lands_near_s10_to_inform_more_vassals", "As the marshal, I am assembling the army of the realm. We are travelling to the region of {s10} to inform more vassals."),
  ("i_intend_to_assemble_the_army_of_the_realm", "I intend to assemble the army of the realm."),
  ("as_the_marshall_i_am_leading_the_siege", "As the marshal, I am leading the siege."),
  ("i_intend_to_begin_the_siege", "I intend to begin the siege."),
  ("as_the_marshall_i_am_leading_our_raid", "As the marshal, I am leading our raid."),
  ("i_intend_to_start_our_raid", "I intend to start our raid."),
  ("as_the_marshall_i_am_leading_our_forces_in_search_of_the_enemy", "As the marshal, I am leading our forces in search of the enemy."),
  ("i_intend_to_lead_our_forces_out_to_find_the_enemy", "I intend to lead our forces out to find the enemy."),
  ("as_the_marshall_i_am_leading_our_forces_to_engage_the_enemy_in_battle", "As the marshal, I am leading our forces to engage the enemy in battle."),
  ("i_intend_to_lead_our_forces_out_to_engage_the_enemy", "I intend to lead our forces out to engage the enemy."),
  ("i_dont_have_enough_troops_and_i_need_to_get_some_more", "I don't have enough troops, and I need to get some more."),
  ("i_am_running_low_on_troops", "I am running low on troops."),
  ("we_are_following_your_direction", "We are following your direction."),
  ("i_need_to_make_preparations_for_your_wedding", "I need to make preparations for your wedding."),
  ("after_all_i_need_to_make_preparations_for_your_wedding", "After all, I need to make preparations for your wedding."),
  ("i_am_heading_to_the_site_of_our_wedding", "I am heading to the site of our wedding."),
  ("after_all_we_are_soon_to_be_wed", "After all, we are soon to be wed!"),
  ("i_am_hosting_a_feast_there", "I am hosting a feast there."),
  ("i_have_a_feast_to_host", "I have a feast to host."),
  ("i_am_to_be_the_bridegroom_there", "I am to be the bridegroom there."),
  ("my_wedding_day_draws_near", "My wedding day draws near."),
  ("i_have_too_much_loot_and_too_many_prisoners_and_need_to_secure_them", "I have too much loot and too many prisoners, and need to secure them."),
  ("i_should_think_of_dropping_off_some_of_my_prisoners", "I should think of dropping off some of my prisoners."),
  ("i_need_to_reinforce_it_as_it_is_poorly_garrisoned", "I need to reinforce it, as it is poorly garrisoned."),
  ("there_is_a_hole_in_our_defenses", "There is a hole in our defenses."),
  ("i_am_following_the_marshals_orders", "I am following the marshal's orders."),
  ("the_marshal_has_given_me_this_command", "The marshal has given me this command."),
  ("i_am_answering_the_marshals_summons", "I am answering the marshal's summons."),
  ("our_realm_needs_my_support_there_is_enemy_raiding_one_of_our_villages_which_is_not_to_far_from_here_i_am_going_there", "Our realm needs my support. There is enemy raiding one of our villages which is not to far from here. I am going there."),
  ("the_marshal_has_issued_a_summons", "The marshal has issued a summons."),
  ("comradeinarms", "comrade-in-arms."),
  ("i_am_supporting_my_s11_s10", "I am supporting my {s11} {s10}."),
  ("i_believe_that_one_of_my_comrades_is_in_need", "I believe that one of my comrades is in need."),
  ("s20_decided_to_attack_s21", "{!}{s20} decided to attack {s21}."),
  ("a_fortress_is_vulnerable", "A fortress is vulnerable."),
  ("i_believe_that_the_enemy_may_be_vulnerable", "I believe that the enemy may be vulnerable."),
  ("i_need_to_inspect_my_properties_and_collect_my_dues", "I need to inspect my properties and collect my dues."),
  ("it_has_been_too_long_since_i_have_inspected_my_estates", "It has been too long since I have inspected my estates."),
  ("my_men_are_weary_so_we_are_returning_home", "My men are weary, so we are returning home."),
  ("my_men_are_becoming_weary", "My men are becoming weary."),
  ("i_have_a_score_to_settle_with_the_lord_there", "I have a score to settle with the lord there."),
  ("i_am_thinking_of_settling_an_old_score", "I am thinking of settling an old score."),
  ("i_am_short_of_money_and_i_hear_that_there_is_much_wealth_there", "I am short of money, and I hear that there is much wealth there."),
  ("i_need_to_refill_my_purse_preferably_with_the_enemys_money", "I need to refill my purse, preferably with the enemy's money."),
  ("by_striking_at_the_enemys_richest_lands_perhaps_i_can_draw_them_out_to_battle", "By striking at the enemy's richest lands, perhaps I can draw them out to battle!"),
  ("i_am_thinking_of_going_on_the_attack", "I am thinking of going on the attack."),
  ("perhaps_if_i_strike_one_more_blow_we_may_end_this_war_on_our_terms_", "Perhaps, if I strike one more blow, we may end this war on our terms. "),
  ("we_may_be_able_to_bring_this_war_to_a_close_with_a_few_more_blows", "We may be able to bring this war to a close with a few more blows."),
  ("i_wish_to_attend_the_feast_there", "I wish to attend the feast there."),
  ("there_is_a_feast_which_i_wish_to_attend", "There is a feast which I wish to attend."),
  ("there_is_a_fair_lady_there_whom_i_wish_to_court", "There is a fair lady there, whom I wish to court."),
  ("i_have_the_inclination_to_pay_court_to_a_fair_lady", "I have the inclination to pay court to a fair lady."),
  ("we_have_heard_reports_that_the_enemy_is_in_the_area", "We have heard reports that the enemy is in the area."),
  ("i_have_heard_reports_of_enemy_incursions_into_our_territory", "I have heard reports of enemy incursions into our territory."),
  ("i_need_to_spend_some_time_with_my_household", "I need to spend some time with my household."),
  ("it_has_been_a_long_time_since_i_have_been_able_to_spend_time_with_my_household", "It has been a long time since I have been able to spend time with my household."),
  ("i_am_watching_the_borders", "I am watching the borders."),
  ("i_may_be_needed_to_watch_the_borders", "I may be needed to watch the borders."),
  ("i_will_guard_the_areas_near_my_home", "I will guard the areas near my home..."),
  ("i_am_perhaps_needed_most_at_home", "I am perhaps needed most at home."),
  ("i_cant_think_of_anything_better_to_do", "I can't think of anything better to do..."),
  ("i_am_completing_what_i_have_already_begun", "I am completing what I have already begun."),
  ("i_dont_even_have_a_home_to_which_to_return", "I don't even have a home to which to return."),
  ("debug__s10_decides_s14_faction_ai_s15", "{!}DEBUG : {s10} decides: {s14} (faction AI: {s15})"),
  ("_i_am_acting_independently_because_no_marshal_is_appointed", " I am acting independently, because no marshal is appointed."),
  ("_i_am_acting_independently_because_our_marshal_is_currently_indisposed", " I am acting independently, because our marshal is currently indisposed."),
  ("_i_am_acting_independently_because_our_realm_is_currently_not_on_campaign", " I am acting independently, because our realm is currently not on campaign."),
  ("_i_am_not_accompanying_the_marshal_because_i_fear_that_he_may_lead_us_into_disaster", " I am not accompanying the marshal, because I fear that he may lead us into disaster."),
  ("i_am_not_accompanying_the_marshal_because_i_question_his_judgment", " I am not accompanying the marshal, because I question his judgment."),
  ("i_am_not_accompanying_the_marshal_because_i_can_do_greater_deeds", " I am not accompanying the marshal, because I can do greater deeds."),
  ("_s16_has_kept_us_on_campaign_on_far_too_long_and_there_are_other_pressing_matters_to_which_i_must_attend", " {s16} has kept us on campaign on far too long, and there are other pressing matters to which I must attend."),
  ("_i_am_not_participating_in_the_marshals_campaign_because_i_do_not_know_where_to_find_our_main_army", " I am not participating in the marshal's campaign, because I do not know where to find our main army."),
  ("_i_am_acting_independently_although_some_enemies_have_been_spotted_within_our_borders_they_havent_come_in_force_and_the_local_troops_should_be_able_to_dispatch_them", " I am acting independently. Although some enemies have been spotted within our borders, they haven't come in force and the local troops should be able to dispatch them."),
  ("_the_needs_of_the_realm_must_come_first", " The needs of the realm must come first."),
  ("we_are_likely_to_be_overwhelmed_by_the_s9_let_each_defend_their_own", "We are likely to be overwhelmed by the {s9}. Let each defend their own."),
  ("we_should_see_this_siege_through", "We should see this siege through."),
  ("we_should_prepare_to_defend_s21_but_we_should_gather_our_forces_until_we_are_strong_enough_to_engage_them", "We should prepare to defend {s21}, but we should gather our forces until we are strong enough to engage them."),
  ("we_should_prepare_to_defend_s21_but_first_we_have_to_gather", "We should prepare to defend {s21}. But first we have to gather our army."),
  ("we_should_ride_to_break_the_siege_of_s21", "We should ride to break the siege of {s21}."),
  ("we_should_ride_to_defeat_the_enemy_gathered_near_s21", "We should ride to defeat the enemy gathered near {s21}."),
  ("we_have_located_s21s_army_and_we_should_engage_it", "We have located {s21}'s army, and we should engage it."),
  ("this_offensive_needs_to_wind_down_soon_so_the_vassals_can_attend_to_their_own_business", "This offensive needs to wind down soon, so the vassals can attend to their own business."),
  ("the_vassals_are_tired_we_let_them_rest_for_some_time", "The vassals are tired of campaigning. We should let them rest for some time."),
  ("the_vassals_still_need_time_to_attend_to_their_own_business", "The vassals still need time to attend to their own business."),
  ("it_is_time_to_go_on_the_offensive_and_we_must_first_assemble_the_army", "It is time to go on the offensive, and we must first assemble the army."),
  ("we_must_continue_to_gather_the_army_before_we_ride_forth_on_an_offensive_operation", "We have only assembled a few vassals, but we must continue to gather the army before we ride forth on an offensive operation."),
  #("there_is_no_need_to_beat_around_the_borders__we_can_take_them_out_with_a_strike_to_the_heart", "There is no need to beat around the borders, we can take them out with a strike to the heart!"),
  ("there_is_no_need_to_beat_around_the_borders__we_can_take_one_of_their_important_towns", "There is no need to beat around the borders, we can take one of their important towns."),
  ("we_should_exploit_our_success_over_s21_by_seizing_one_of_their_fortresses", "We should exploit our success over {s21} by seizing one of their fortresses."),
  ("we_shall_leave_a_fiery_trail_through_the_heart_of_the_enemys_lands_targeting_the_wealthy_settlements_if_we_can", "We shall leave a fiery trail through the heart of the enemy's lands, targeting the wealthy settlements if we can."),
  ("the_army_will_be_disbanded_because_we_have_been_waiting_too_long_without_a_target", "The army will be disbanded, because we have been waiting too long without a target."),
  ("it_is_time_for_the_feast_to_conclude", "It is time for the feast to conclude."),
  ("we_should_continue_the_feast_unless_there_is_an_emergency", "We should continue the feast, unless there is an emergency."),
  ("you_had_wished_to_hold_a_feast", "You had wished to hold a feast."),
  ("your_wedding_day_approaches_my_lady", "Your wedding day approaches, my lady."),
  ("your_wedding_day_approaches", "Your wedding day approaches."),
  ("s22_and_s23_wish_to_marry", "{s22} and {s23} wish to marry."),
  ("it_has_been_a_long_time_since_the_lords_of_the_realm_gathered_for_a_feast", "It has been a long time since the lords of the realm gathered for a feast."),
  ("the_circumstances_which_led_to_this_decision_no_longer_apply_so_we_should_stop_and_reconsider_shortly", "The circumstances which led to this decision no longer apply, so we should stop and reconsider shortly."),
  ("we_cant_think_of_anything_to_do", "{!}ERROR -- We can't think of anything to do."),
  ("s15_is_at_war_with_s16_", "{s15} is at war with {s16}. "),
  ("in_the_short_term_s15_has_a_truce_with_s16_as_a_matter_of_general_policy_", "In the short term, {s15} has a truce with {s16}. As a matter of general policy, "),
  ("in_the_short_term_s15_was_recently_provoked_by_s16_and_is_under_pressure_to_declare_war_as_a_matter_of_general_policy_", "In the short term, {s15} was recently provoked by {s16}, and is under pressure to declare war. As a matter of general policy, "),
  ("envoymodified_diplomacy_score_honor_plus_relation_plus_envoy_persuasion_=_reg4", "{!}Envoy-modified diplomacy score (honor plus relation plus envoy persuasion) = {reg4}"),
  ("s12s15_cannot_negotiate_with_s16_as_to_do_so_would_undermine_reg4herhis_own_claim_to_the_throne_this_civil_war_must_almost_certainly_end_with_the_defeat_of_one_side_or_another", "{s12}{s15} cannot negotiate with {s16}, as to do so would undermine {reg4?her:his} own claim to the throne. This civil war must almost certainly end with the defeat of one side or another."),
  ("s12s15_considers_s16_to_be_dangerous_and_untrustworthy_and_shehe_wants_to_bring_s16_down", "{s12}{s15} considers {s16} to be dangerous and untrustworthy, and {reg4?she:he} wants to bring {s16} down."),
  ("s12s15_is_anxious_to_reclaim_old_lands_such_as_s18_now_held_by_s16", "{s12}{s15} is anxious to reclaim old lands such as {s18}, now held by {s16}."),
  ("s12s15_feels_that_reg4shehe_is_winning_the_war_against_s16_and_sees_no_reason_not_to_continue", "{s12}{s15} feels that {reg4?she:he} is winning the war against {s16}, and sees no reason not to continue."),
  ("s12s15_faces_too_much_internal_discontent_to_feel_comfortable_ignoring_recent_provocations_by_s16s_subjects", "{s12}{s15} faces too much internal discontent to feel comfortable ignoring recent provocations by {s16}'s subjects."),
  ("s12even_though_reg4shehe_is_fighting_on_two_fronts_s15_is_inclined_to_continue_the_war_against_s16_for_a_little_while_longer_for_the_sake_of_honor", "{s12}Even though {reg4?she:he} is fighting on two fronts, {s15} is inclined to continue the war against {s16} for a little while longer, for the sake of honor."),
  ("s12s15_feels_that_reg4shehe_must_pursue_the_war_against_s16_for_a_little_while_longer_for_the_sake_of_honor", "{s12}{s15} feels that {reg4?she:he} must pursue the war against {s16} for a little while longer, for the sake of honor."),
  ("s12s15_is_currently_on_the_offensive_against_s17_now_held_by_s16_and_reluctant_to_negotiate", "{s12}{s15} is currently on the offensive against {s17}, now held by {s16}, and reluctant to negotiate."),
  ("s12s15_is_alarmed_by_the_growing_power_of_s16", "{s12}{s15} is alarmed by the growing power of {s16}."),
  ("s12s15_distrusts_s16_and_fears_that_any_deals_struck_between_the_two_realms_will_not_be_kept", "{s12}{s15} distrusts {s16}, and fears that any deals struck between the two realms will not be kept."),
  ("s12s15_is_at_war_on_too_many_fronts_and_eager_to_make_peace_with_s16", "{s12}{s15} is at war on too many fronts, and eager to make peace with {s16}."),
  ("s12s15_seems_to_think_that_s16_and_reg4shehe_have_a_common_enemy_in_the_s17", "{s12}{s15} seems to think that {s16} and {reg4?she:he} have a common enemy in the {s17}."),
  ("s12s15_feels_frustrated_by_reg4herhis_inability_to_strike_a_decisive_blow_against_s16", "{s12}{s15} feels frustrated by {reg4?her:his} inability to strike a decisive blow against {s16}."),
  ("s12s15_has_suffered_enough_in_the_war_with_s16_for_too_little_gain_and_is_ready_to_pursue_a_peace", "{s12}{s15} has suffered enough in the war with {s16}, for too little gain, and is ready to pursue a peace."),
  ("s12s15_would_like_to_firm_up_a_truce_with_s16_to_respond_to_the_threat_from_the_s17", "{s12}{s15} would like to firm up a truce with {s16} to respond to the threat from the {s17}."),
  ("s12s15_wishes_to_be_at_peace_with_s16_so_as_to_pursue_the_war_against_the_s17", "{s12}{s15} wishes to be at peace with {s16} so as to pursue the war against the {s17}."),
  ("s12s15_seems_to_be_intimidated_by_s16_and_would_like_to_avoid_hostilities", "{s12}{s15} seems to be intimidated by {s16}, and would like to avoid hostilities."),
  ("s12s15_has_no_particular_reason_to_continue_the_war_with_s16_and_would_probably_make_peace_if_given_the_opportunity", "{s12}{s15} has no particular reason to continue the war with {s16}, and would probably make peace if given the opportunity."),
  ("s12s15_seems_to_be_willing_to_improve_relations_with_s16", "{s12}{s15} seems to be willing to improve relations with {s16}."),
  ("excuse_me_how_can_you_possibly_imagine_yourself_worthy_to_marry_into_our_family", "Excuse me? How can you possibly imagine yourself worthy to marry into our family?"),
  ("em_with_regard_to_her_ladyship_we_were_looking_specifically_for_a_groom_of_some_distinction_fight_hard_count_your_dinars_and_perhaps_some_day_in_the_future_we_may_speak_of_such_things_my_good_man", "Em... With regard to her ladyship, we were looking specifically for a {groom/bride} of some distinction. Fight hard, count your denars, and perhaps some day in the future we may speak of such things, my good {man/woman}!"), #dckplmc start+
  ("em_with_regard_to_her_ladyship_we_were_looking_specifically_for_a_groom_of_some_distinction", "Em... With regard to her ladyship, we were looking specifically for a {groom/bride} of some distinction."),
  ("it_is_too_early_for_you_to_be_speaking_of_such_things_you_are_still_making_your_mark_in_the_world", "It is too early for you to be speaking of such things. You are still making your mark in the world."),
  ("you_dont_serve_the_s4_so_id_say_no_one_day_we_may_be_at_war_and_i_prefer_not_to_have_to_kill_my_inlaws_if_at_all_possible", "You don't serve the {s4}, so I'd say no. One day we may be at war, and I prefer not to have to kill my in-laws, if at all possible."),
  ("as_you_are_not_a_vassal_of_the_s4_i_must_decline_your_request_the_twists_of_fate_may_mean_that_we_will_one_day_cross_swords_and_i_would_hope_not_to_make_a_widow_of_a_lady_whom_i_am_obligated_to_protect", "As you are not a vassal of the {s4}, I must decline your request. The twists of fate may mean that we will one day cross swords, and I would hope not to make a widow of a lady whom I am obligated to protect."),
  ("as_you_are_not_a_pledged_vassal_of_our_liege_with_the_right_to_hold_land_i_must_refuse_your_request_to_marry_into_our_family", "As you are not a pledged vassal of our liege, with the right to hold land, I must refuse your request to marry into our family."),
  ("look_here_lad__the_young_s14_has_been_paying_court_to_s16_and_youll_have_to_admit__hes_a_finer_catch_for_her_than_you_so_lets_have_no_more_of_this_talk_shall_we", "Look here, {lad/lass} -- the young {s14} has been paying court to {s16}, and you'll have to admit -- he's a finer catch for her than you. So let's have no more of this talk, shall we?"),
  ("i_do_not_care_for_you_sir_and_i_consider_it_my_duty_to_protect_the_ladies_of_my_household_from_undesirable_suitors", "I do not care for you, {sir/madam}, and I consider it my duty to protect the ladies of my household from undesirable suitors..."),
  ("hmm_young_girls_may_easily_be_led_astray_so_out_of_a_sense_of_duty_to_the_ladies_of_my_household_i_think_i_would_like_to_get_to_know_you_a_bit_better_we_may_speak_of_this_at_a_later_date", "Hmm. Young girls may easily be led astray, so out of a sense of duty to the ladies of my household, I think I would like to get to know you a bit better. We may speak of this at a later date."), #dckplmc end+
  ("you_may_indeed_make_a_fine_match_for_the_young_mistress", "You may indeed make a fine match for the young mistress."),
#diplomacy start+ (players of either gender may marry opposite-gender lords)
  ("madame__given_our_relations_in_the_past_this_proposal_is_most_surprising_i_do_not_think_that_you_are_the_kind_of_woman_who_can_be_bent_to_a_hushands_will_and_i_would_prefer_not_to_have_our_married_life_be_a_source_of_constant_acrimony", "{Sir/Madame} -- given our relations in the past, this proposal is most surprising. I do not think that you are the kind of {man/woman} who can be bent to a {wife/husband}'s will, and I would prefer not to have our married life be a source of constant acrimony."),
  ("i_would_prefer_to_marry_a_proper_maiden_who_will_obey_her_husband_and_is_not_likely_to_split_his_head_with_a_sword", "I would prefer to marry a proper {lord/maiden} who will {cherish/obey} {his/her} {wife/husband}, and is not likely to split {her/his} head with a sword."),
  ("my_lady_while_i_admire_your_valor_you_will_forgive_me_if_i_tell_you_that_a_woman_like_you_does_not_uphold_to_my_ideal_of_the_feminine_of_the_delicate_and_of_the_pure", "My {lord/lady}, while I admire your valor and your beauty, you will forgive me if I tell you that a {man/woman} like you does not uphold to my ideal of a {husband/wife}: {masculine/feminine}, delicate, and pure."),#this sounds ridiculous -- don't use the male version
  ("nah_i_want_a_woman_wholl_keep_quiet_and_do_what_shes_told_i_dont_think_thats_you", "Nah. I want a {man/woman} who'll keep quiet and do what {he/she}'s told. I don't think that's you."),
  ("my_lady_you_are_possessed_of_great_charms_but_no_properties_until_you_obtain_some_to_marry_you_would_be_an_act_of_ingratitude_towards_my_ancestors_and_my_lineage", "My {lord/lady}, you are possessed of great charms, but no properties. Until you obtain some, to marry you would be an act of ingratitude towards my ancestors and my lineage."),
  ("my_lady_you_are_a_woman_of_no_known_family_of_no_possessions__in_short_a_nobody_do_you_think_that_you_are_fit_to_marry_into_may_family", "My {lord/lady}, you are a {man/woman} of no known family, of no possessions -- in short, a nobody. Do you think that you are fit to marry into may family?"),
  ("my_lady__forgive_me__the_quality_of_our_bond_is_not_of_the_sort_which_the_poets_tell_us_is_necessary_to_sustain_a_happy_marriage", "My {lord/lady} -- forgive me -- the quality of our bond is not of the sort which the poets tell us is necessary to sustain a happy marriage."),
  ("um_i_think_that_if_i_want_to_stay_on_s4s_good_side_id_best_not_marry_you", "Um, I think that if I want to stay on {s4}'s good side, I'd best not marry you."),
  ("you_serve_another_realm_i_dont_see_s4_granting_reg4herhis_blessing_to_our_union", "You serve another realm. I don't see {s4} granting {reg4?her:his} blessing to our union."),
  ("madame_my_heart_currently_belongs_to_s4", "{Sir/Madame}, my heart currently belongs to {s4}."),
  ("my_lady_you_are_a_woman_of_great_spirit_and_bravery_possessed_of_beauty_grace_and_wit_i_shall_give_your_proposal_consideration", "My {lord/lady}, you are a {man/woman} of great spirit and bravery, possessed of {strength/beauty}, {courage/grace}, and wit. I shall give your proposal consideration."),
  ("my_lady_you_are_a_woman_of_great_spirit_and_bravery_possessed_of_beauty_grace_and_wit_i_would_be_most_honored_were_you_to_become_my_wife", "My {lord/lady}, you are a {man/woman} of great spirit and bravery, possessed of {strength/beauty}, {courage/grace}, and wit. I would be most honored were you to become my {husband/wife}."),
#diplomacy end+
  ("poem_choice_reg4_lady_rep_reg5", "{!}Poem choice: {reg4}, lady rep: {reg5}"),
  ("ah__kais_and_layali__such_a_sad_tale_many_a_time_has_it_been_recounted_for_my_family_by_the_wandering_poets_who_come_to_our_home_and_it_has_never_failed_to_bring_tears_to_our_eyes", "Ah -- 'Kais and Layali' -- such a sad tale. Many a time has it been recounted for my family by the wandering poets who come to our home, and it has never failed to bring tears to our eyes."),
  ("kais_and_layali_three_hundred_stanzas_of_pathetic_sniveling_if_you_ask_me_if_kais_wanted_to_escape_heartbreak_he_should_have_learned_to_live_within_his_station_and_not_yearn_for_what_he_cannot_have", "'Kais and Layali'? Three hundred stanzas of pathetic sniveling, if you ask me. If Kais wanted to escape heartbreak, he should have learned to live within his station, and not yearn for what he cannot have."),
  ("kais_and_layali_no_one_should_ever_have_written_such_a_sad_poem_if_it_was_the_destiny_of_kais_and_layali_to_be_together_than_their_love_should_have_conquered_all_obstacles", "'Kais and Layali'? No one should ever have written such a sad poem! If it was the destiny of Kais and Layali to be together, than their love should have conquered all obstacles!"),
  ("ah_kais_and_layali_a_very_old_standby_but_moving_in_its_way", "Ah, 'Kais and Layali.' A very old stand-by, but moving, in its way."),
  ("the_saga_of_helgered_and_kara_such_happy_times_in_which_our_ancestors_lived_women_like_kara_could_venture_out_into_the_world_like_men_win_a_name_for_themselves_and_not_linger_in_their_husbands_shadow", "The saga of 'Helgered and Kara'? Such happy times in which our ancestors lived! Women like Kara could venture out into the world like men, win a name for themselves, and not linger in their husbands' shadow."),
  ("ah_the_saga_of_helgered_and_kara_now_there_was_a_lady_who_knew_what_she_wanted_and_was_not_afraid_to_obtain_it", "Ah, the saga of 'Helgered and Kara'. Now there was a lady who knew what she wanted, and was not afraid to obtain it."),
  ("the_saga_of_helgered_and_kara_a_terrible_tale__but_it_speaks_of_a_very_great_love_if_she_were_willing_to_make_war_on_her_own_family", "The saga of 'Helgered and Kara'? A terrible tale - but it speaks of a very great love, if she were willing to make war on her own family."),
  ("the_saga_of_helgered_and_kara_as_i_recall_kara_valued_her_own_base_passions_over_duty_to_her_family_that_she_made_war_on_her_own_father_i_have_no_time_for_a_poem_which_praises_such_a_woman", "The saga of 'Helgered and Kara'? As I recall, Kara valued her own base passions over duty to her family that she made war on her own father. I have no time for a poem which praises such a woman!"),
  ("the_saga_of_helgered_and_kara_how_could_a_woman_don_armor_and_carry_a_sword_how_could_a_man_love_so_ungentle_a_creature", "The saga of 'Helgered and Kara'? How could a woman don armor and carry a sword! How could a man love so ungentle a creature!"),
  ("a_conversation_in_the_garden_i_cannot_understand_the_lady_in_that_poem_if_she_loves_the_man_why_does_she_tease_him_so", "'A Conversation in the Garden'? I cannot understand the lady in that poem. If she loves the man, why does she tease him so?"),
  ("a_conversation_in_the_garden_let_us_see__it_is_morally_unedifying_it_exalts_deception_it_ends_with_a_maiden_surrendering_to_her_base_passions_and_yet_i_cannot_help_but_find_it_charming_perhaps_because_it_tells_us_that_love_need_not_be_tragic_to_be_memorable", "'A Conversation in the Garden'? Let us see -- it is morally unedifying, it exalts deception, it ends with a maiden surrendering to her base passions... And yet I cannot help but find it charming, perhaps because it tells us that love need not be tragic to be memorable."),
  ("a_conversation_in_the_garden_now_that_is_a_tale_every_lady_should_know_by_heart_to_learn_the_subtleties_of_the_politics_she_must_practice", "'A Conversation in the Garden'? Now that is a tale every lady should know by heart, to learn the subtleties of the politics she must practice!"),
  ("a_conversation_in_the_garden_it_is_droll_i_suppose__although_there_is_nothing_there_that_truly_stirs_my_soul", "'A Conversation in the Garden'? It is droll, I suppose -- although there is nothing there that truly stirs my soul."),
  ("storming_the_fortress_of_love_ah_yes_the_lady_sits_within_doing_nothing_while_the_man_is_the_one_who_strives_and_achieves_i_have_enough_of_that_in_my_daily_life_why_listen_to_poems_about_it", "'Storming the Fortress of Love'? Ah, yes. The lady sits within doing nothing, while the man is the one who strives and achieves. I have enough of that in my daily life. Why listen to poems about it?"),
  ("storming_the_fortress_of_love_ah_yes_an_uplifting_tribute_to_the_separate_virtues_of_man_and_woman", "'Storming the Fortress of Love'? Ah, yes. An uplifting tribute to the separate virtues of man and woman."),
  ("storming_the_fortress_of_love_ah_yes_but_although_it_is_a_fine_tale_of_virtues_it_speaks_nothing_of_passion", "'Storming the Fortress of Love'? Ah, yes. But although it is a fine tale of virtues, it speaks nothing of passion!"),
  ("storming_the_fortress_of_love_ah_a_sermon_dressed_up_as_a_love_poem_if_you_ask_me", "'Storming the Fortress of Love'? Ah... A sermon dressed up as a love poem, if you ask me."),
  ("a_hearts_desire_ah_such_a_beautiful_account_of_the_perfect_perfect_love_to_love_like_that_must_be_to_truly_know_rapture", "'A Heart's Desire'? Ah, such a beautiful account of the perfect, perfect love! To love like that must be to truly know rapture!"),
  ("a_hearts_desire_silly_if_you_ask_me_if_the_poet_desires_a_lady_then_he_should_endeavor_to_win_her__and_not_dress_up_his_desire_with_a_pretense_of_piety", "'A Heart's Desire'? Silly, if you ask me. If the poet desires a lady, then he should endeavor to win her -- and not dress up his desire with a pretense of piety!"),
  ("a_hearts_desire_hmm__it_is_an_interesting_exploration_of_earthly_and_divine_love_it_does_speak_of_the_spiritual_quest_which_brings_out_the_best_in_man_but_i_wonder_if_the_poet_has_not_confused_his_yearning_for_higher_things_with_his_baser_passions", "'A Heart's Desire'? Hmm -- it is an interesting exploration of earthly and divine love. It does speak of the spiritual quest which brings out the best in man, but I wonder if the poet has not confused his yearning for higher things with his baser passions."),
  ("a_hearts_desire_oh_yes__it_is_very_worthy_and_philosophical_but_if_i_am_to_listen_to_a_bard_strum_a_lute_for_three_hours_i_personally_prefer_there_to_be_a_bit_of_a_story", "'A Heart's Desire'? Oh, yes -- it is very worthy and philosophical. But if I am to listen to a bard strum a lute for three hours, I personally prefer there to be a bit of a story."),
  ("result_reg4_string_s11", "{!}Result: {reg4}. String: {s11}"),
  ("calculating_effect_for_policy_for_s3", "{!}Calculating effect for policy for {s3}"),
  ("reg3_units_of_s4_for_reg5_guests_and_retinue", "{reg3} units of {s4} for {reg5} guests and retinue"),
  ("reg3_units_of_spice_of_reg5_to_be_consumed", "{reg3} units of spice of {reg5} to be consumed"),
  ("reg3_units_of_oil_of_reg5_to_be_consumed", "{reg3} units of oil of {reg5} to be consumed"),
  ("of_food_which_must_come_before_everything_else_the_amount_is_s8", "Of food, which must come before everything else, the amount is {s8}"),
  ("s9_and_the_variety_is_s8_", "{s9} and the variety is {s8}. "),
  ("s9_of_drink_which_guests_will_expect_in_great_abundance_the_amount_is_s8", "{s9} Of drink, which guests will expect in great abundance, the amount is {s8}"),
  ("s9_of_spice_which_is_essential_to_demonstrate_that_we_spare_no_expense_as_hosts_the_amount_is_s8_", "{s9} Of spice, which is essential to demonstrate that we spare no expense as hosts, the amount is {s8}. "),
  ("s9_of_oil_which_we_shall_require_to_light_the_lamps_the_amount_is_s8", "{s9} Of oil, which we shall require to light the lamps, the amount is {s8}."),
  ("s9_overall_our_table_will_be_considered_s8", "{s9} Overall, our table will be considered {s8}."),
  ("rebel", "rebel"),
  ("bandit", "bandit"),
  ("relation_of_prisoner_with_captor_is_reg0", "relation of prisoner with captor is {reg0}"),
  ("s5_suffers_attrition_reg3_x_s4", "{s5} suffers attrition: {reg3} x {s4}"),
  ("s65", "{!}{s65}"),
  ("s10_said_on_s1_s11__", "{s10} said on {s1}: {s11}^^"),
  ("rumor_note_to_s3s_slot_reg4_s5", "{!}Rumor note to {s3}'s slot {reg4}: {s5}"),
  ("totalling_casualties_caused_during_mission", "Totalling casualties caused during mission..."),
  ("removing_s4_from_s5", "Removing {s4} from {s5}"),
  ("s4_joins_prison_break", "{s4} joins prison break"),
  ("helper_is_spawned", "helper is spawned."),
  ("leaving_area_during_prison_break", "Leaving area during prison break"),
  ("talk_to_the_trainer", "Talk to the trainer."),
  ("woman", "woman"),
  ("man", "man"),
  ("noble", "noble"),
  ("common", "common"),
  ("may_find_that_you_are_able_to_take_your_place_among_calradias_great_lords_relatively_quickly", "may find that you are able to take your place among Calradia's great lords relatively quickly"),
  ("may_face_some_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords", "may face some difficulties establishing yourself as an equal among Calradia's great lords"),
  ("may_face_great_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords", "may face great difficulties establishing yourself as an equal among Calradia's great lords"),
  ("current_party_morale_is_reg5_current_party_morale_modifiers_are__base_morale__50_party_size_s2reg1_leadership_s3reg2_food_variety_s4reg3s5s6_recent_events_s7reg4_total__reg5___", "Current party morale is {reg5}.^Current party morale modifiers are:^^Base morale:  +{reg6}^Party size: {s2}{reg1}^Leadership: {s3}{reg2}^Food variety: {s4}{reg3}{s5}{s6}^Recent events: {s7}{reg4}^TOTAL:  {reg5}^^^"),
  ("s1extra_morale_for_s9_troops__reg6_", "{s1}Extra morale for {s9} troops : {reg6}^"),
  ("courtships_in_progress_", "Courtships in progress:^"),
  ("s1_s2_relation_reg3_last_visit_reg4_days_ago", "{s1}^{s2}, relation {reg3}, last visit {reg4} days ago"),
  ("s1__poems_known", "{s1}^^Poems known:"),
  ("s1_storming_the_castle_of_love_allegoric", "{s1}^Storming the Castle of Love (Allegoric)"),
  ("s1_kais_and_layali_tragic", "{s1}^Kais and Layali (Tragic)"),
  ("s1_a_conversation_in_the_garden_comic", "{s1}^A Conversation in the Garden (Comic)"),
  ("s1_helgered_and_kara_epic", "{s1}^Helgered and Kara (Epic)"),
  ("s1_a_hearts_desire_mystic", "{s1}^A Heart's Desire (Mystic)"),
  ("no_companions_in_service", "No companions in service"),
  ("gathering_support", "Gathering support"),
  ("expected_back_imminently", "Expected back imminently"),
  ("expected_back_in_approximately_reg3_days", "Expected back in approximately {reg3} days"),
  ("gathering_intelligence", "Gathering intelligence in {s9}"), #SB : in {s9}
  ("diplomatic_embassy_to_s9", "Diplomatic embassy to {s9}"),
  ("serving_as_minister", "Serving as minister"),
  ("in_your_court_at_s9", "In your court at {s9}"),
  ("under_arms", "Under arms"),
  ("in_your_party", "In your party"),
  ("s4_s8_s5", "{!}{s4}: {s8} ({s5})"),
  ("s2_s3", "{!}{s2}^{s3}"),
  ("attacking_enemy_army_near_s11", "Attacking enemy army near {s11}"),
  ("holding_feast_at_s11", "Holding feast at {s11}"),
  ("sfai_reg4", "{!}SFAI: {reg4}"),
  ("s9s10_current_state_s11_hours_at_current_state_reg3_current_strategic_thinking_s14_marshall_s12_since_the_last_offensive_ended_reg4_hours_since_the_decisive_event_reg10_hours_since_the_last_rest_reg9_hours_since_the_last_feast_ended_reg5_hours_percent_disgruntled_lords_reg7_percent_restless_lords_reg8__", "{s9}{s10}^Current state: {s11}^Hours at current state: {reg3}^Current strategic thinking: {s14}^Marshall: {s12}^Since the last offensive ended: {reg4} hours^Since the decisive event: {reg10} hours^Since the last 18+ hour rest: {reg9} hours^Since the last feast ended: {reg5} hours^Percent disgruntled lords: {reg7}%^Percent restless lords: {reg8}%^^"),
  ("_right_to_rule_reg12", "^Right to rule: {reg12}."),
  ("political_arguments_made_legality_reg3_rights_of_lords_reg4_unificationpeace_reg5_rights_of_commons_reg6_fief_pledges_reg7", "Political arguments made:^Legality: {reg3}^Rights of lords: {reg4}^Unification/peace: {reg5}^Rights of commons: {reg6}^Fief pledges: {reg7}"),
  ("renown_reg2_honour_rating_reg3s12_friends_s8_enemies_s6_s9", "Renown: {reg2}.^Honour rating: {reg3}.{s12}^Friends: {s8}.^Enemies: {s6}.^{s9}"),
  ("you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel", "You lie stunned for several minutes, then stagger to your feet, to find your {s10} standing over you. You have lost the duel."),
  ("s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel", "{s10} lies in the arena's dust for several minutes, then staggers to his feet. You have won the duel"),
  ("debug__you_fought_with_a_center_so_no_change_in_morale", "{!}DEBUG : You fought with a center so no change in morale."),
  ("_this_castle_is_temporarily_under_royal_control", " This castle is temporarily under royal control."),
  ("_this_castle_does_not_seem_to_be_under_anyones_control", " This castle does not seem to be under anyone's control."),
  ("_this_town_is_temporarily_under_royal_control", " This town is temporarily under royal control."),
  ("_the_townspeople_seem_to_have_declared_their_independence", " The townspeople seem to have declared their independence."),
  ("to_your_husband_s11", "to your husband, {s11}."),
  ("_you_see_the_banner_of_your_wifehusband_s7_over_the_castle_gate", " You see the banner of your {wife/husband}, {s7}, over the castle gate."),
  ("_the_banner_of_your_wifehusband_s7_flies_over_the_town_gates", " The banner of your {wife/husband}, {s7}, flies over the town gates."),
  ("_the_lord_is_currently_holding_a_feast_in_his_hall", "^The lord is currently holding a feast in his hall."),
  ("_join_the_feast", " (join the feast)"),
  ("belligerent_drunk_in_s4", "Belligerent drunk in {s4}"),
  ("belligerent_drunk_not_found", "Belligerent drunk not found"),
  ("roughlooking_character_in_s4", "Rough-looking character in {s4}"),
  ("roughlooking_character_not_found", "Rough-looking character not found"),
  ("_however_you_have_sufficiently_distinguished_yourself_to_be_invited_to_attend_the_ongoing_feast_in_the_lords_castle", ". However, you have sufficiently distinguished yourself to be invited to attend the ongoing feast in the lord's castle."),
  ("s8_you_are_also_invited_to_attend_the_ongoing_feast_in_the_castle", "{s8}. You are also invited to attend the ongoing feast in the castle."),
  ("__hardship_index_reg0_avg_towns_reg1_avg_villages_reg2__", "{!}^^Hardship index: {reg0}, avg towns: {reg1}, avg villages: {reg2}^^"),
  ("__s3_price_=_reg4_calradian_average_reg6_capital_reg11_s4_base_reg1modified_by_raw_material_reg2modified_by_prosperity_reg3_calradian_average_production_base_reg5_total_reg12_consumed_reg7used_as_raw_material_reg8modified_total_reg9_calradian_consumption_base_reg10_total_reg13s1_", "{!}^^{s3}^Price = {reg4} (Calradian average {reg6})^Capital: {reg11} {s4}^Base {reg1}/modified by raw material {reg2}/modified by prosperity {reg3}^(Calradian average production, base {reg5}, total {reg12}).^Consumed {reg7}/used as raw material {reg8}/modified total {reg9}^(Calradian consumption, base: {reg10}, total: {reg13}){s1}^"),
  ("s11_unfortunately_s12_was_wounded_and_had_to_be_left_behind", "{s11} Unfortunately, {s12} was wounded and had to be left behind."),
  ("s11_also_s12_was_wounded_and_had_to_be_left_behind", "{s11} Also, {s12} was wounded and had to be left behind."),
  ("trial_influences_s17s_relation_with_s18_by_reg3", "{!}Trial influences {s17}'s relation with {s18} by {reg3}"),
  ("with_the_s10", "with the {s10}"),
  ("outside_calradia", "outside Calradia."),
  ("you_have_been_indicted_for_treason_to_s7_your_properties_have_been_confiscated_and_you_would_be_well_advised_to_flee_for_your_life", "You have been indicted for treason to {s7}. Your properties have been confiscated, and you would be well advised to flee for your life."),
##diplomacy start+ replaced "He" with "{reg4?She:He}"
  ("by_order_of_s6_s4_of_the_s5_has_been_indicted_for_treason_the_lord_has_been_stripped_of_all_reg4herhis_properties_and_has_fled_for_reg4herhis_life_he_is_rumored_to_have_gone_into_exile_s11", "By order of {s6}, {s4} of the {s5} has been indicted for treason. The {reg4?lady:lord} has been stripped of all {reg4?her:his} properties, and has fled for {reg4?her:his} life. {reg4?She:He} is rumored to have gone into exile {s11}."),
##diplomacy end+
  ("local_notables_from_s1_a_village_claimed_by_the_s4_have_been_mistreated_by_their_overlords_from_the_s3_and_petition_s5_for_protection", "local notables from {s1}, a village claimed by the {s4}, have been mistreated by their overlords from the {s3} and petition {s5} for protection"),
  ("villagers_from_s1_stole_some_cattle_from_s2", "villagers from {s1} stole some cattle from {s2}"),
  ("villagers_from_s1_abducted_a_woman_from_a_prominent_family_in_s2_to_marry_one_of_their_boys", "villagers from {s1} abducted a woman from a prominent family in {s2} to marry one of their boys"),
  ("villagers_from_s1_killed_some_farmers_from_s2_in_a_fight_over_the_diversion_of_a_stream", "villagers from {s1} killed some farmers from {s2} in a fight over the diversion of a stream"),
  ("your_new_minister_", "Your new minister "),
  ("s10_is_your_new_minister_and_", "{s10} is your new minister, and "),
  ("due_to_the_fall_of_s10_your_court_has_been_relocated_to_s12", "Due to the loss of {s10}, your court has been relocated to {s11}"),
  ("after_to_the_fall_of_s10_your_faithful_vassal_s9_has_invited_your_court_to_s11_", "After to the loss of {s10}, your faithful vassal {s9} has invited your court to {s11} "),
  ("after_to_the_fall_of_s11_your_court_has_nowhere_to_go", "After the loss of {s11}, your court has nowhere to go"),
  ("s8_wishes_to_inform_you_that_the_lords_of_s9_will_be_gathering_for_a_feast_at_his_great_hall_in_s10_and_invites_you_to_be_part_of_this_august_assembly", "{s8} wishes to inform you that the lords of {s9} will be gathering for a feast at his great hall in {s10}, and invites you to be part of this exalted assembly."),
  ("consult_with_s11_at_your_court_in_s12", "Consult with {s11} at your court in {s12}"),
  ("as_brief_as_our_separation_has_been_the_longing_in_my_heart_to_see_you_has_made_it_seem_as_many_years", "As brief as our separation has been, the longing in my heart to see you has made it seem as many years."),
  ("although_it_has_only_been_a_short_time_since_your_departure_but_i_would_be_most_pleased_to_see_you_again", "Although it has only been a short time since your departure, I would be most pleased to see you again."),
  ("although_i_have_received_no_word_from_you_for_quite_some_time_i_am_sure_that_you_must_have_been_very_busy_and_that_your_failure_to_come_see_me_in_no_way_indicates_that_your_attentions_to_me_were_insincere_", "Although I have received no word from you for quite some time, I am sure that you must have been very busy, and that your failure to come see me in no way indicates that your attentions to me were insincere."),
  ##diplomacy start+
  #Correct the gender of the below
  ("i_trust_that_you_have_comported_yourself_in_a_manner_becoming_a_gentleman_during_our_long_separation_", "I trust that you have comported yourself in a manner becoming a {gentleman/lady} during our long separation."),#gentleman -> {gentleman/lady}
  ("it_has_been_many_days_since_you_came_and_i_would_very_much_like_to_see_you_again", "It has been many days since you came, and I would very much like to see you again."),
  ("_you_should_ask_my_s11_s16s_permission_but_i_have_no_reason_to_believe_that_he_will_prevent_you_from_coming_to_see_me", " You should ask my {s11} {s16}'s permission, but I have no reason to believe that he will prevent you from coming to see me."),
  ("_you_should_first_ask_her_s11_s16s_permission", ". You should first ask her {s11} {s16}'s permission"),
  ("_alas_as_we_know_my_s11_s16_will_not_permit_me_to_see_you_however_i_believe_that_i_can_arrange_away_for_you_to_enter_undetected", " Alas, as we know, my {s11} {s16} will not permit me to see you. However, I believe that I can arrange a way for you to enter undetected."),
  ("_as_my_s11_s16_has_already_granted_permission_for_you_to_see_me_i_shall_expect_your_imminent_arrival", " As my {s11} {s16} has already granted permission for you to see me, I shall expect your imminent arrival."),
  ("visit_s3_who_was_last_at_s4s18", "Visit {s3}, who was last at {s4}{s18}"),
  ("giver_troop_=_s2", "{!}Giver troop = {s2}"),
  ("the_guards_at_the_gate_have_been_ordered_to_allow_you_through_you_might_be_imagining_things_but_you_think_one_of_them_may_have_given_you_a_wink", "The guards at the gate have been ordered to allow you through. You might be imagining things, but you think one of them may have given you a wink"),
  ("the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_don_this_dress_and_throw_the_hood_over_your_face_i_will_smuggle_you_inside_the_castle_to_meet_her_in_the_guise_of_a_skullery_maid__the_guards_will_not_look_too_carefully_but_i_beg_you_for_all_of_our_sakes_be_discrete", "The guards glare at you, and you know better than to ask permission to enter. However, as you walk back towards your lodgings, an elderly lady dressed in black approaches you. 'I am {s11}'s nurse,' she whispers urgently. 'Don this dress, and throw the hood over your face. I will smuggle you inside the castle to meet her in the guise of a scullery maid -- the guards will not look too carefully. But I beg you, for all of our sakes, be discreet!"),
  ("the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_wait_for_a_while_by_the_spring_outside_the_walls_i_will_smuggle_her_ladyship_out_to_meet_you_dressed_in_the_guise_of_a_shepherdess_but_i_beg_you_for_all_of_our_sakes_be_discrete", "The guards glare at you, and you know better than to ask permission to enter. However, as you walk back towards your lodgings, an elderly lady dressed in black approaches you. 'I am {s11}'s nurse,' she whispers urgently. 'Wait for a while by the spring outside the walls. I will smuggle her ladyship out to meet you, dressed in the guise of a shepherdess. But I beg you, for all of our sakes, be discreet!"),
  ("the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_her_ladyship_asks_me_to_say_that_yearns_to_see_you_but_that_you_should_bide_your_time_a_bit_her_ladyship_says_that_to_arrange_a_clandestine_meeting_so_soon_after_your_last_encounter_would_be_too_dangerous", "The guards glare at you, and you know better than to ask permission to enter. However, as you walk back towards your lodgings, an elderly lady dressed in black approaches you.^'I am {s11}'s nurse,' she whispers urgently. 'Her ladyship asks me to say that she yearns to see you, but that you should bide your time a bit. Her ladyship says that to arrange a clandestine meeting so soon after your last encounter would be too dangerous.'"),
  ##diplomacy end+
  ("the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter", "The guards glare at you, and you know better than to ask permission to enter."),
  ("s3_commander_of_party_reg4_which_is_not_his_troop_leaded_party_reg5", "{!}{s3} commander of party #{reg4} which is not his troop leaded party {reg5}"),
  ("party_with_commander_mismatch__check_log_for_details_", "Party with commander mismatch - check log for details "),
  ("s4_adds_wealth_has_reg4_wealth_accumulated", "{!}{s4} adds wealth, has {reg4} wealth accumulated"),
  ("doing_political_calculations_for_s9", "Doing political calculations for {s9}"),
  ("s9_does_not_have_a_fief", "{!}{s9} does not have a fief"),
  ("current_wealth_reg1", "Current wealth: {reg1}"),
  ("debug__attempting_to_spawn_s4", "{!}DEBUG : Attempting to spawn {s4}"),
  ("debug__s0_is_spawning_around_party__s7", "{!}DEBUG : {s0} is spawning around party : {s7}"),
  ("no_trigger_noted", "{!}(No trigger noted"),
  ("triggered_by_npc_is_quitting", "{!}(Triggered by NPC is quitting"),
  ("triggered_by_npc_has_grievance", "{!}(Triggered by NPC has grievance"),
  ("triggered_by_npc_has_personality_clash", "{!}(Triggered by NPC has personality clash"),
  ("triggered_by_npc_has_political_grievance", "{!}(Triggered by NPC has political grievance"),
  ("triggered_by_npc_to_rejoin_party", "{!}(Triggered by NPC to rejoin party"),
  ("triggered_by_npc_has_sisterly_advice", "{!}(Triggered by NPC has sisterly advice)"),
  ("triggered_by_local_histories", "{!}(Triggered by local histories)"),
  ("s1_reg0_s2", "{!}{s1}, {reg0} {s2}"),
  ("s3_reg0_s2", "{!}{s3} {reg0} {s2}"),
  ("s1_s2", "{!}{s1} {s2}"),
  ("wanted_bandits_spotted_by_s4", "Wanted bandits spotted by {s4}"),
  ("s4_ready_to_voice_objection_to_s3s_mission_if_in_party", "{s4} ready to voice objection to {s3}'s mission, if in party"),
  ("test_effective_relation_=_reg3", "{!}DEBUG : Effective relation = {reg3}"),
  ("g_talk_troop_=_reg0__g_encountered_party_=_reg1__slot_value_=_reg2", "{!}g talk troop = {reg0} , g encountered party = {reg1} , slot value = {reg2}"),
  ("strange_that_one_didnt_seem_like_your_ordenary_troublemaker_he_didnt_drink_all_that_much__he_just_stood_there_quietly_and_watched_the_door_you_may_wish_to_consider_whether_you_have_any_enemies_who_know_you_are_in_town_a_pity_that_blood_had_to_be_spilled_in_my_establishment", "Strange. That one didn't seem like your ordinary troublemaker. He didn't drink all that much -- he just stood there, quietly, and watched the door. You may wish to consider whether you have any enemies who know you are in town... A pity that blood had to be spilled in my establishment..."),
  ("wielded_item_reg3", "{!}Wielded item: {reg3}"),
  ("you_never_let_him_draw_his_weapon_still_it_looked_like_he_was_going_to_kill_you_take_his_sword_and_purse_i_suppose_he_was_trouble_but_its_not_good_for_an_establishment_to_get_a_name_as_a_place_where_men_are_killed", "You never let him draw his weapon.... Still, it looked like he was going to kill you. Take his sword and purse, I suppose. He was trouble, but it's not good for an establishment to get a name as a place where men are killed."),
  ("well_id_say_that_he_started_it_that_entitles_you_to_his_sword_and_purse_i_suppose_have_a_drink_on_the_house_as_i_daresay_youve_saved_a_patron_or_two_a_broken_skull_still_i_hope_he_still_has_a_pulse_its_not_good_for_an_establishment_to_get_a_name_as_a_place_where_men_are_killed", "Well... I'd say that he started it. That entitles you to his sword and purse, I suppose. Have a drink on the house, as I daresay you've saved a patron or two a broken skull. Still, I hope he still has a pulse. It's not good for an establishment to get a name as a place where men are killed."),
  ("stop_no_shooting_no_shooting", "Stop! No shooting! No shooting!"),
  ("em_ill_stay_out_of_this", "Em... I'll stay out of this."),
  ("the_s12_is_a_labyrinth_of_rivalries_and_grudges_lords_ignore_their_lieges_summons_and_many_are_ripe_to_defect", "The {s12} is a labyrinth of rivalries and grudges. Lords ignore their liege's summons, and many are ripe to defect."),
  ("the_s12_is_shaky_many_lords_do_not_cooperate_with_each_other_and_some_might_be_tempted_to_defect_to_a_liege_that_they_consider_more_worthy", "The {s12} is shaky. Many lords do not cooperate with each other, and some might be tempted to defect to a liege that they consider more worthy."),
  ("the_s12_is_fairly_solid_some_lords_bear_enmities_for_each_other_but_they_tend_to_stand_together_against_outside_enemies", "The {s12} is fairly solid. Some lords bear enmities for each other, but they tend to stand together against outside enemies."),
  ("the_s12_is_a_rock_of_stability_politically_speaking_whatever_the_lords_may_think_of_each_other_they_fight_as_one_against_the_common_foe", "The {s12} is a rock of stability, politically speaking. Whatever the lords may think of each other, they fight as one against the common foe."),
  ("tribune_s12", "Tribune {s12}"),
  ("lady_s12", "Lady {s12}"),
  ("lord_s12", "Lord {s12}"),
  ("resolve_the_dispute_between_s11_and_s12", "Resolve the dispute between {s11} and {s12}"),
  ("in_doing_so_you_will_be_in_violation_of_your_truce_is_that_what_you_want", "In doing so, you will be in violation of your truce. Is that what you want?"),
  ("if_you_attack_without_provocation_some_of_your_vassals_may_consider_you_to_be_too_warlike_is_that_what_you_want", "If you attack without provocation, some of your vassals may consider you to be too warlike. Is that what you want?"),
  ("our_men_are_ready_to_ride_forth_at_your_bidding_are_you_sure_this_is_what_you_want", "Our men are ready to ride forth at your bidding... Are you sure this is what you want?"),
  ("seek_recognition", "seek recognition"),
  ("seek_vassalhood", "seek vassalhood"),
  ("seek_a_truce", "seek a truce"),
  ("_promised_fief", " (promised fief)"),
  ("no_fiefss12", "(no fiefs){s12}"),
  ("fiefs_s0s12", "(fiefs: {s0}{s12})"),
  ("please_s65_", "Please {s65}, "),
  ("_s15_is_also_being_held_here_and_you_may_wish_to_see_if_reg4shehe_will_join_us", " {s15} is also being held here, and you may wish to see if {reg4?she:he} will join us."),
  ("one_thing_in_our_favor_is_that_s12s_grip_is_very_shaky_he_rules_over_a_labyrinth_of_rivalries_and_grudges_lords_often_fail_to_cooperate_and_many_would_happily_seek_a_better_liege", "One thing in our favor is that {s12}'s grip is very shaky. He rules over a labyrinth of rivalries and grudges. Lords often fail to cooperate, and many would happily seek a better liege."),
  ("thankfully_s12s_grip_is_fairly_shaky_many_lords_do_not_cooperate_with_each_other_and_some_might_be_tempted_to_seek_a_better_liege", "Thankfully, {s12}'s grip is fairly shaky. Many lords do not cooperate with each other, and some might be tempted to seek a better liege."),
  ("unfortunately_s12s_grip_is_fairly_strong_until_we_can_shake_it_we_may_have_to_look_long_and_hard_for_allies", "Unfortunately, {s12}'s grip is fairly strong. Until we can shake it, we may have to look long and hard for allies."),
  ("unfortunately_s12s_grip_is_very_strong_unless_we_can_loosen_it_it_may_be_difficult_to_find_allies", "Unfortunately, {s12}'s grip is very strong. Unless we can loosen it, it may be difficult to find allies."),
  ("playername_come_to_plague_me_some_more_have_you", "{playername}... Come to plague me some more, have you?"),
  ("ah_it_is_you_again", "Ah. It is you again..."),
  ("well_playername", "Well, {playername}"),
  ("comment_found_s1", "{!}Comment found: {s1}"),
  ("rejoinder_noted", "{!}Rejoinder noted"),
  ("s11", "{!}{s11}"),
  ("flagon_of_mead", "flagon of mead"),
  ("skin_of_kumis", "skin of kumis"),
  ("mug_of_kvass", "mug of kvass"),
  ("cup_of_wine", "cup of wine"),
##diplomacy start+ Make gender-correct using reg4
  ("you_intend_to_challenge_s13_to_force_him_to_retract_an_insult", "You intend to challenge {s13} to force {reg4?her:him} to retract an insult."),
##diplomacy end+
  ("intrigue_impatience=_reg3_must_be_less_than_100", "{!}Intrigue impatience= {reg3}, must be less than 100"),
  ("youll_have_to_speak_to_me_at_some_other_time_then", "You'll have to speak to me at some other time, then."),
  ("this_is_no_time_for_words", "This is no time for words!"),
  ("lord_not_alone", "{!}Lord not alone"),
##diplomacy start+ (players of either gender may marry opposite-gender lords)
  ("of_course_my_wife", "Of course, my {husband/wife}."),
  ("perhaps_not_our_marriage_has_become_a_bit_strained_dont_you_think", "Perhaps not. Our marriage has become a bit strained, don't you think?"),
  ("why_is_that_my_wife_actually_our_marriage_has_become_such_that_i_prefer_to_have_a_witness_for_all_of_our_converations", "Why is that, my {husband/wife}? Actually, our marriage has become such that I prefer to have a witness for all of our converations."),
##diplomacy end+
  ("all_right_then_what_do_you_have_to_say_out_with_it", "All right then. What do you have to say? Out with it."),
  ("bah__im_in_no_mood_for_whispering_in_the_corner", "Bah -- I'm in no mood for whispering in the corner."),
  ("bah_i_dont_like_you_that_much_im_not_going_to_go_plot_with_you_in_some_corner", "Bah. I don't like you that much. I'm not going to go plot with you in some corner."),
  ("well__now_what_do_you_have_to_propose", "Well -- now what do you have to propose?"),
  ("trying_our_hand_at_intrigue_are_we_i_think_not", "Trying our hand at intrigue, are we? I think not"),
  ("hah_i_trust_you_as_a_i_would_a_serpent_i_think_not", "Hah! I trust you as a I would a serpent. I think not."),
  ("i_do_not_like_to_conduct_my_business_in_the_shadows_but_sometimes_it_must_be_done_what_do_you_have_to_say", "I do not like to conduct my business in the shadows, but sometimes it must be done. What do you have to say?"),
  ("i_would_prefer_to_conduct_our_affairs_out_in_the_open", "I would prefer to conduct our affairs out in the open."),
  ("do_not_take_this_amiss_but_with_you_i_would_prefer_to_conduct_our_affairs_out_in_the_open", "Do not take this amiss, but with you, I would prefer to conduct our affairs out in the open."),
  ("hmm_you_have_piqued_my_interest_what_do_you_have_to_say", "Hmm. You have piqued my interest. What do you have to say?"),
  ("em_lets_keep_our_affairs_out_in_the_open_for_the_time_being", "Em... Let's keep our affairs out in the open, for the time being."),
  ("thats_sensible__the_world_is_full_of_churls_who_poke_their_noses_into_their_betters_business_now_tell_me_what_it_is_that_you_have_to_say", "That's sensible -- the world is full of churls who poke their noses into their betters' business. Now tell me what it is that you have to say."),
  ("what_do_you_take_me_for_a_plotter", "What do you take me for? A plotter?"),
  ("well_i_normally_like_to_keep_things_out_in_the_open_but_im_sure_someone_like_you_would_not_want_to_talk_in_private_unless_heshe_had_a_good_reason_what_is_it", "Well, I normally like to keep things out in the open, but I'm sure someone like you would not want to talk in private unless {he/she} had a good reason. What is it?"),
  ("surely_we_can_discuss_whatever_you_want_to_discuss_out_here_in_the_open_cant_we", "Surely we can discuss whatever you want to discuss out here in the open, can't we?"),
  ##diplomacy start+ make gender-correct using reg65
  ("im_a_simple__man_not_one_for_intrigue_but_id_guess_that_you_have_something_worthwhile_to_say_what_is_it", "I'm a simple {reg65?woman:man}, not one for intrigue, but I'd guess that you have something worthwhile to say. What is it?"),
  ##diplomacy end+
  ("forgive_me_but_im_not_one_for_going_off_in_corners_to_plot", "Forgive me, but I'm not one for going off in corners to plot."),
  ("please_do_not_take_this_amiss_but_i_do_not_trust_you", "Please do not take this amiss, but I do not trust you."),
  ("certainly_playername_what_is_it", "Certainly, {playername}. What is it?"),
  ("forgive_me_but_id_prefer_to_keep_our_conversations_in_the_open", "Forgive me, but I'd prefer to keep our conversations in the open."),
  ("please_do_not_take_this_amiss_but_im_not_sure_you_and_i_are_still_on_those_terms", "Please do not take this amiss, but I'm not sure you and I are still on those terms."),
  ("persuasion__relation_less_than_5", "{!}Persuasion + relation less than -5)"),
  ("s15", "{!}{s15}"),
  ("persuasion__2__lord_reputation_modifier__relation_less_than_10", "{!}Persuasion * 2 + lord reputation modifier + relation less than 10)"),
  ("s13", "{!}{s13}"),
  ("placeholder", "{!}[placeholder]..."),
  ##diplomacy start+ Replace "queen" with "{s0}"
  ("really_well_this_is_the_first_i_have_heard_of_it_unless_you_build_up_support_for_that_claim_you_may_find_it_difficult_to_find_allies_however_whenever_you_see_fit_to_declare_yourself_publically_as_queen_i_should_be_honored_to_be_your_consort", "Really? Well, this is the first I have heard of it. Unless you build up support for that claim, you may find it difficult to find allies. However, whenever you see fit to declare yourself publically as {s0}, I should be honored to be your consort."),
  ##diplomacy end+
  ("yes_i_have_heard_such_talk_while_it_is_good_that_you_are_building_up_your_support_i_do_not_think_that_you_are_quite_ready_to_proclaim_yourself_yet_however_i_will_let_you_be_the_judge_of_that_and_when_you_decide_i_should_be_honored_to_be_your_consort", "Yes... I have heard such talk. While it is good that you are building up your support, I do not think that you are quite ready to proclaim yourself yet. However, I will let you be the judge of that, and when you decide, I should be honored to be your consort."),
  ("yes_and_many_others_in_calradia_think_so_as_well_perhaps_it_is_time_that_you_declared_yourself_and_we_shall_ride_forth_together_to_claim_your_throne_i_should_be_honored_to_be_your_consort", "Yes... and many others in Calradia think so as well. Perhaps it is time that you declared yourself, and we shall ride forth together to claim your throne. I should be honored to be your consort."),
  ("i_am_disturbed_about_my_lord_s15s_choice_of_companions", "I am disturbed about my lord {s15}'s choice of companions."),
  ("well_ill_be_honest_i_feel_that_sometimes_s15_overlooks_my_rights_and_extends_his_protection_to_the_unworthy", "Well, I'll be honest. I feel that sometimes {s15} overlooks my rights, and extends {reg15?her:his} protection to the unworthy."),
  ("heh_one_thing_that_ill_say_about_s15_is_that_he_has_a_ripe_batch_of_bastards_in_his_court", "Heh. One thing that I'll say about {s15} is that {reg15?she:he} has a ripe batch of bastards in {reg15?her:his} court."),
  ("well_sometimes_i_have_to_say_that_i_question_s15s_judgment_regarding_those_who_he_keeps_in_his_court", "Well, sometimes I have to say that I question {s15}'s judgment regarding those whom {reg15?she:he} keeps in his court."),
  ("s15_is_a_weak_man_who_too_easily_lends_his_ear_to_evil_council_and_gives_his_protection_to_some_who_have_done_me_wrong", "{s15} is a weak ruler, who too easily lends an ear to evil council, and gives protection to some who have done me wrong."),
  ("i_will_confess_that_sometimes_i_worry_about_s15s_judgment_particularly_in_the_matter_of_the_counsel_that_he_keeps", "I will confess that sometimes I worry about {s15}'s judgment, particularly in the matter of the counsel that {reg15?she:he} keeps.."),
  ("what_do_i_think_i_think_that_s15_is_a_vile_pretender_a_friend_to_the_flatterer_and_the_hypocrite", "What do I think? I think that {s15} is a vile pretender, a friend to the flatterer and the hypocrite."),
  ("well_s15_is_not_like_you_ill_say_that_much", "Well, {s15} is not like you. I'll say that much."),
  ("s15_long_may_he_live", "{s15}? Long may {reg15?she:he} live!"),
  ("he_is_my_liege_that_is_all_that_i_will_say_on_this_matter", "{s15} is my liege. That is all that I will say on this matter."),
  ("that_you_are_the_rightful_heir_to_the_throne_of_calradia", "That you are the rightful heir to the throne of Calradia?"),
  ("that_s14_is_the_rightful_ruler_of_calradia", "That {s14} is the rightful ruler of Calradia?"),
  ("that_s14_will_rule_this_land_justly", "That {s14} will rule this land justly?"),
  ("that_s14_will_protect_our_rights_as_nobles", "That {s14} will protect our rights as nobles?"),
  ("that_s14_will_unify_this_land_and_end_this_war", "That {s14} will unify this land and end this war?"),
  ("that_s14_will_reward_me_with_a_fief", "That {s14} will reward me with a fief?"),
  #("prior_arguments", "Prior arguments:"),
  #("legal_reg3", "Legal: {reg3}"),
  #("just_king_reg3", "Just king: {reg3}"),
  #("bring_peace_reg3", "Bring peace: {reg3}"),
  #("only_best_counsel_reg3", "Only best counsel: {reg3}"),
  #("reward_lords_reg3", "Reward lords: {reg3}"),
  ("he", "he"),
  ("king", "king"),
  ("she", "she"),
  ("queen", "queen"),
  ("khan", "khan"),
  ("i", "I"),
  ("according_to_the_ancient_law_and_custom_of_the_calradians_s45_should_be_s47", "According to the ancient law and custom of the Calradians, {s45} should be {s47}"),
  ("because_s44_is_the_rightful_s47_of_the_s46", "Because {s44} is the rightful {s47} of the {s46}"),
  ("you_speak_of_claims_and_legalities_yet_to_others_you_talk_of_bringing_peace_by_force", "You speak of claims and legalities, yet to others you talk of bringing peace by force"),
  ("you_speak_of_bringing_peace_by_force_yet_to_others_you_make_legal_claims", "You speak of bringing peace by force, yet to others you make legal claims."),
  ("you_speak_to_some_of_upholding_the_rights_of_the_commons_yet_you_speak_to_others_of_uphold_the_rights_of_nobles_what_if_those_rights_are_in_conflict", "You speak to some of upholding the rights of the commons, yet you speak to others of uphold the rights of nobles. What if those rights are in conflict?"),
##diplomacy start+
#Replace "lord" with {s12}
#  ("you_speak_to_me_of_upholding_my_rights_as_a_lord_but_to_others_you_talk_of_upholding_the_rights_of_all_commons_what_if_those_rights_come_into_conflict", "You speak to me of upholding my rights as a lord, but to others you talk of upholding the rights of all commons. What if those rights come into conflict?"),
  ("you_speak_to_me_of_upholding_my_rights_as_a_lord_but_to_others_you_talk_of_upholding_the_rights_of_all_commons_what_if_those_rights_come_into_conflict", "You speak to me of upholding my rights as a {s12}, but to others you talk of upholding the rights of all commons. What if those rights come into conflict?"),
##diplomacy end+
  ("a_claim_should_be_strong_indeed_before_one_starts_talking_about_it", "A claim should be strong indeed before one starts talking about it."),
##diplomacy start+: Replace "king" with {s12}, and "pigherd" with {s14}
##OLD:
#  ("a_king_should_prove_his_valor_beyond_any_doubt_before_he_starts_talking_about_a_claim_to_the_throne", "A king should prove his valor beyond any doubt before he starts talking about a claim to the throne."),
#  ("you_must_prove_yourself_a_great_warrior_before_men_will_follow_you_as_king", "You must prove yourself a great warrior before men will follow you as king."),
#  ("a_claim_to_the_throne_should_be_strong_indeed_before_one_presses_it", "A claim to the throne should be strong indeed before one presses it."),
#  ("indeed_but_a_man_must_also_prove_himself_a_great_warrior_before_men_will_follow_you_as_king", "Indeed. But a man must also prove himself a great warrior before men will follow you as king."),
#  ("my_pigherd_can_declare_himself_king_if_he_takes_he_fancy_i_think_you_need_to_break_a_few_more_heads_on_tbe_battlefield_before_men_will_follow_you", "My pigherd can declare himself king, if he takes he fancy. I think you need to break a few more heads on tbe battlefield before men will follow you."),
##NEW: Replace "king" with {s12}, and "pigherd" with {s14}
  ("a_king_should_prove_his_valor_beyond_any_doubt_before_he_starts_talking_about_a_claim_to_the_throne", "A {s12} should prove his valor beyond any doubt before he starts talking about a claim to the throne."),
  ("you_must_prove_yourself_a_great_warrior_before_men_will_follow_you_as_king", "You must prove yourself a great warrior before men will follow you as {s12}."),
  ("a_claim_to_the_throne_should_be_strong_indeed_before_one_presses_it", "A claim to the throne should be strong indeed before one presses it."),
  ("indeed_but_a_man_must_also_prove_himself_a_great_warrior_before_men_will_follow_you_as_king", "Indeed. But a man must also prove himself a great warrior before men will follow you as {s12}."),
  ("my_pigherd_can_declare_himself_king_if_he_takes_he_fancy_i_think_you_need_to_break_a_few_more_heads_on_tbe_battlefield_before_men_will_follow_you", "My {s14} can declare himself {s12}, if he takes he fancy. I think you need to break a few more heads on tbe battlefield before men will follow you."),
##diplomacy end+
  ("if_you_do_not_wish_to_die_on_a_scaffold_like_so_many_failed_pretenders_before_you_i_would_suggest_that_you_to_build_your_claim_on_stronger_foundations_so_that_men_will_follow_you", "If you do not wish to die on a scaffold, like so many failed pretenders before you, I would suggest that you to build your claim on stronger foundations, so that men will follow you."),
  ("if_you_do_not_wish_to_die_on_a_scaffold_like_so_many_failed_pretenders_before_you_i_would_advise_you_prove_yourself_on_the_field_of_battle_so_that_men_will_follow_you", "If you do not wish to die on a scaffold, like so many failed pretenders before you, I would advise you prove yourself on the field of battle, so that men will follow you."),
  ##diplomacy start+ replace "with their swords" with "with their {s12}", and "Real kings" with "Real {s14}"
#  ("talk_is_for_heralds_and_lawyers_real_kings_prove_themselves_with_their_swords", "Talk is for heralds and lawyers. Real kings prove themselves with their swords."),
  ("talk_is_for_heralds_and_lawyers_real_kings_prove_themselves_with_their_swords", "Talk is for heralds and lawyers. Real {s14} prove themselves with their {s12}."),
  ##diplomacy end+
  ("i_were_you_i_would_try_to_prove_myself_a_bit_more_before_i_went_about_pressing_my_claim", "If I were you, I would try to prove myself a bit more before I went about pressing my claim."),
  ("trump_check_random_reg4_skill_reg3", "{!}DEBUG : Trump check: random {reg4}, skill {reg3}"),
  ("s12_s43", "{!}{s12} {s43}"),
  ("indeed_please_continue", "Indeed. Please continue."),
  ("me", "me"),
  ("preliminary_result_for_political_=_reg4", "{!}DEBUG : Preliminary result for political = {reg4}"),
  ("i_worry_about_those_with_whom_you_have_chosen_to_surround_yourself", "I worry about those with whom you have chosen to surround yourself."),
  ("there_are_some_outstanding_matters_between_me_and_some_of_your_vassals_", "There are some outstanding matters between me and some of your vassals. "),
  ("result_for_political_=_reg41", "{!}DEBUG : Result for political = {reg41}"),
  ("my_liege_has_his_faults_but_i_dont_care_for_your_toadies", "My liege has his faults but I don't care for your toadies."),
  ("i_think_youre_a_good_man_but_im_worried_that_you_might_be_pushed_in_the_wrong_direction_by_some_of_those_around_you", "I think you're a good man, but I'm worried that you might be pushed in the wrong direction by some of those around you."),
  ("i_am_loathe_to_fight_alongside_you_so_long_as_you_take_under_your_wing_varlots_and_base_men", "I am loathe to fight alongside you, so long as you take under your wing varlots and base men."),
  ("ill_be_honest__with_some_of_those_who_follow_you_i_think_id_be_more_comfortable_fighting_against_you_than_with_you", "I'll be honest -- with some of those who follow you, I think I'd be more comfortable fighting against you than with you."),
  ("i_say_that_you_can_judge_a_man_by_the_company_he_keeps_and_you_have_surrounded_yourself_with_vipers_and_vultures", "I say that you can judge a man by the company he keeps, and you have surrounded yourself with vipers and vultures."),
  ("you_know_that_i_have_always_had_a_problem_with_some_of_our_companions", "You know that I have always had a problem with some of our companions."),
  ("politically_i_would_be_a_better_position_in_the_court_of_my_current_liege_than_in_yours", "Politically, I would be a better position in the court of my current liege, than in yours."),
  ("i_am_more_comfortable_with_you_and_your_companions_than_with_my_current_liege", "I am more comfortable with you and your companions than with my current liege"),
  ("militarily_youre_in_no_position_to_protect_me_should_i_be_attacked_id_be_reluctant_to_join_you_until_you_could", "Militarily, you're in no position to protect me, should I be attacked. I'd be reluctant to join you until you could."),
  ("militarily_when_i_consider_the_lay_of_the_land_i_realize_that_to_pledge_myself_to_you_now_would_endanger_my_faithful_retainers_and_my_family", "Militarily, when I consider the lay of the land, I realize that to pledge myself to you now would endanger my faithful retainers and my family."),
  ("militarily_youre_in_no_position_to_come_to_my_help_if_someone_attacked_me_i_dont_mind_a_good_fight_but_i_like_to_have_a_chance_of_winning", "Militarily, you're in no position to come to my help, if someone attacked me. I don't mind a good fight, but I like to have a chance of winning."),
  ("militarily_you_would_have_me_join_you_only_to_find_myself_isolated_amid_a_sea_of_enemies", "Militarily, you would have me join you, only to find myself isolated amid a sea of enemies."),
  ("militarily_youre_in_no_position_to_come_to_my_help_if_someone_attacked_me_youd_let_me_be_cut_down_like_a_dog_id_bet", "Militarily, you're in no position to come to my help, if someone attacked me. You'd let me be cut down like a dog, I'd bet."),
  ("militarily_i_wouldnt_be_any_safer_if_i_joined_you", "Militarily, I wouldn't be any safer if I joined you."),
  ("militarily_i_might_be_safer_if_i_joined_you", "Militarily, I might be safer if I joined you."),
  ("finally_there_is_a_cost_to_ones_reputation_to_change_sides_in_this_case_the_cost_would_be_very_high", "Finally, one should always think carefully about retracting one's allegiance, even if there is good reason, as it is not good to get a name as one who changes lieges easily. In this case, the cost to my reputation would be very high."),
  ("finally_there_is_a_cost_to_ones_reputation_to_change_sides_in_this_case_the_cost_would_be_significant", "Finally, one should always think carefully about retracting one's allegiance, even if there is good reason, as it is not good to get a name as one who changes lieges easily. In this case, the cost to my reputation would be significant."),
  ("finally_there_is_a_cost_to_ones_reputation_to_change_sides_in_this_case_however_many_men_would_understand", "Finally, one should always think carefully about retracting one's allegiance, even if there is good reason, as it is not good to get a name as one who changes lieges easily. In this case, however, many men would understand."),
  ("chance_of_success_=_reg1", "{!}DEBUG : Chance of success = {reg1}%"),
  ("random_=_reg3", "{!}DEBUG : Random = {reg3}"),
  ("i_will_not_have_it_be_said_about_me_that_i_am_a_traitor_that_is_my_final_decision_i_have_nothing_more_to_say_on_this_matter", "I will not have it be said about me that I am a traitor. That is my final decision. I have nothing more to say on this matter."),
  ("i_am_pledged_to_defend_s14_i_am_sorry_though_we_may_meet_on_the_battlefield_i_hope_that_we_will_still_be_friends", "I am pledged to defend {s14}. I am sorry. Though we may meet on the battlefield, I hope that we will still be friends."),
  ("i_really_cannot_bring_myself_to_renounce_s14_i_am_sorry_please_lets_not_talk_about_this_any_more", "I really cannot bring myself to renounce {s14}. I am sorry. Please, let's not talk about this any more."),
  ("however_i_have_decided_that_i_must_remain_loyal_to_s14_i_am_sorry", "However, I have decided that I must remain loyal to {s14}. I am sorry."),
  ("however_i_will_not_let_you_lead_me_into_treason_do_not_talk_to_me_of_this_again", "However, I will not let you lead me into treason. Do not talk to me of this again."),
  ("its_not_good_to_get_a_reputation_as_one_who_abandons_his_liege_that_is_my_decision_let_us_speak_no_more_of_this_matter", "It's not good to get a reputation as one who abandons his liege. That is my decision. Let us speak no more of this matter."),
  ("ive_decided_to_stick_with_s14_i_dont_want_to_talk_about_this_matter_any_more", "I've decided to stick with {s14}. I don't want to talk about this matter any more."),
  ("lord_pledges_to_s4", "{!}DEBUG : Lord pledges to {s4}"),
  ("lord_recruitment_provokes_home_faction", "{!}DEBUG : Lord recruitment provokes home faction"),
  ("ERROR__wrong_quest_type", "{!}ERROR - Wrong quest type"),
  ("you_are_challenging_me_to_a_duel_how_droll_as_you_wish_playername_it_will_be_good_sport_to_bash_your_head_in", "You are challenging me to a duel? How droll! As you wish, {playername}, it will be good sport to bash your head in."),
  ("call_me_coward_very_well_you_leave_me_no_choice", "Call me coward? Very well, you leave me no choice."),
  ("reg3_hours", "{reg3} hours."),
  ("hour", "hour."),
  ("however_circumstances_have_changed_since_we_made_that_decision_and_i_may_reconsider_shortly_s16", "However, circumstances have changed since we made that decision, and I may reconsider shortly. {s16}"),
  ("i_wish_to_marry_your_s11_s10_i_ask_for_your_blessing", "I wish to marry your {s11}, {s10}. I ask for your blessing."),
  ("i_wish_to_marry_your_s11_s10_i_ask_for_your_help", "I wish to marry your {s11}, {s10}. I ask for your help."),
  ("you_plan_to_marry_s3_at_a_feast_hosted_by_s4_in_s5_you_should_be_notifed_of_the_feast_as_soon_as_it_is_held", "You plan to marry {s3} at a feast hosted by {s4} in {s5}. You should be notifed of the feast as soon as it is held."),
  ("your_s11_", "your {s11}, "),
  ("i_ask_again_may", "I ask again: may"),
  ("may", "May"),
  ("very_well_as_far_as_im_concerned_i_suppose_she_can_see_most_anyone_she_likes__within_reason_of_course", "Very well. As far as I'm concerned, I suppose she can see most anyone she likes - within reason, of course."),
  ("very_well_an_alliance_with_you_could_be_valuable_go_chat_with_her_and_see_if_you_can_get_her_to_take_a_fancy_to_you_if_she_doesnt_and_if_we_still_want_to_conclude_this_business_then_i_can_make_her_see_reason", "Very well. An alliance with you could be valuable. Go chat with her, and see if you can get her to take a fancy to you. If she doesn't, and if we still want to conclude this business, then I can make her see reason."),
  ("you_have_my_blessing_to_pay_suit_to_her__so_long_as_your_intentions_are_honorable_of_course_depending_on_how_things_proceed_between_you_two_we_may_have_more_to_discuss_at_a_later_date", "You have my blessing to pay suit to her -- so long as your intentions are honorable, of course. Depending on how things proceed between you two, we may have more to discuss at a later date."),
  ("war_damage_inflicted_reg3_suffered_reg4_ratio_reg5", "{!}DEBUG : War damage inflicted: {reg3}, suffered: {reg4}, ratio: {reg5}"),
  ("ERROR__did_not_calculate_war_progress_string_properly", "{!}ERROR - did not calculate war progress string properly"),
  ("the_war_has_barely_begun_so_and_it_is_too_early_to_say_who_is_winning_and_who_is_losing", "The war has barely begun, so and it is too early to say who is winning and who is losing."),
  ("we_have_been_hitting_them_very_hard_and_giving_them_little_chance_to_recover", "We have been hitting them very hard, and giving them little chance to recover."),
  ("the_fighting_has_been_hard_but_we_have_definitely_been_getting_the_better_of_them", "The fighting has been hard, but we have definitely been getting the better of them."),
  ("they_have_been_hitting_us_very_hard_and_causing_great_suffering", "They have been hitting us very hard, and causing great suffering."),
  ("the_fighting_has_been_hard_and_i_am_afraid_that_we_have_been_having_the_worst_of_it", "The fighting has been hard, and I am afraid that we have been having the worst of it."),
  ("both_sides_have_suffered_in_the_fighting", "Both sides have suffered in the fighting."),
  ("no_clear_winner_has_yet_emerged_in_the_fighting_but_i_think_we_are_getting_the_better_of_them", "No clear winner has yet emerged in the fighting, but I think we are getting the better of them."),
  ("no_clear_winner_has_yet_emerged_in_the_fighting_but_i_fear_they_may_be_getting_the_better_of_us", "No clear winner has yet emerged in the fighting, but I fear they may be getting the better of us."),
  ("no_clear_winner_has_yet_emerged_in_the_fighting", "No clear winner has yet emerged in the fighting."),
  ("s9_s14", "{!}{s9} {s14}"),
  ("there_is_no_campaign_currently_in_progress", "There is no campaign currently in progress."),
  ("we_are_assembling_the_army", "We are assembling the army."),
  ("we_aim_to_take_the_fortress_of_s8", "We aim to take the fortress of {s8}."),
  ("we_are_on_a_raid_and_are_now_targeting_s8", "We are on a raid, and are now targeting {s8}."),
  ("we_are_trying_to_seek_out_and_defeat_s8", "We are trying to seek out and defeat {s8}."),
  ("we_are_riding_to_the_defense_of_s8", "We are riding to the defense of {s8}."),
  ("we_are_gathering_for_a_feast_at_s8", "We are gathering for a feast at {s8}."),
  ("_however_that_may_change_shortly_s14", " However, that may change shortly. {s14}"),
  ("it_is_our_custom_to_seal_any_such_alliances_with_marriage_and_in_fact_we_have_been_looking_for_a_suitable_groom_for_my_s11_s14", "It is our custom to seal any such alliances with marriage, and in fact, we have been looking for a suitable {groom/bride} for my {s11}, {s14}."),
  ("once_again_", "once again "),
  ("cheat__marriage_proposal", "Cheat - marriage proposal"),
##diplomacy start+ gender correction
  ("you_plan_to_marry_s4_as_you_have_no_family_in_calradia_he_will_organize_the_wedding_feast", "You plan to marry {s4}. As you have no family in Calradia, {she/he} will organize the wedding feast."),
##diplomacy end+
  ("s43_just_so_you_know_if_you_attack_me_you_will_be_in_violation_of_the_truce_you_signed_with_the_s34", "{s43} Just so you know, if you attack me, you will be in violation of the truce you signed with the {s34}"),
##diplomacy start+ gender correction
  ("very_well__you_are_now_my_liege_as_well_as_my_husband", "We can keep this short: you are now my liege, as well as my {wife/husband}, with all the mutual obligations which that entails."),
  ("i_thank_you_reg39my_ladylord", "I thank you, {reg39?my lady:lord}."),
  ("now_some_might_say_that_women_have_no_business_leading_mercenary_companies_but_i_suspect_that_you_would_prove_them_wrong_what_do_you_say", "Now, some might say that {males/women} have no business leading mercenary companies, but I suspect that you would prove them wrong. What do you say?"),
##diplomacy end+
  ("what_do_you_say_to_entering_the_service_of_s9_as_a_mercenary_captain_i_have_no_doubt_that_you_would_be_up_to_the_task", "What do you say to entering the service of {s9} as a mercenary captain? I have no doubt that you would be up to the task."),
  ("s9_asked_you_to_rescue_s13_who_is_prisoner_at_s24", "{s9} asked you to rescue {s13}, who is prisoner at {s24}."),
  ("s9_asked_you_to_attack_a_village_or_some_caravans_as_to_provoke_a_war_with_s13", "{s9} asked you to attack a village or some caravans as to provoke a war with {s13}."),
  ("s9_asked_you_to_catch_the_three_groups_of_runaway_serfs_and_bring_them_back_to_s4_alive_and_breathing_he_said_that_all_three_groups_are_heading_towards_s3", "{s9} asked you to catch the three groups of runaway serfs and bring them back to {s4}, alive and breathing. He said that all three groups are heading towards {s3}."),
  ("ERROR__player_not_logged_as_groom", "{!}ERROR - Player not logged as groom"),
  ("you_intend_to_bring_goods_to_s9_in_preparation_for_the_feast_which_will_be_held_as_soon_as_conditions_permit", "You intend to bring goods to {s9} in preparation for the feast, which will be held as soon as conditions permit."),
  ("hello_playername", "Hello, {playername}"),
  ("ah_my_gentle_playername_how_much_good_it_does_my_heart_to_see_you_again", " How much good it does my heart to see you again! Sometimes, I feel that there is a mystic bond between us that transcends the distance."),
  ("playername__i_am_so_glad_to_see_you_again_i_must_say_i_do_envy_your_freedom_to_ride_out_and_experience_the_world", " I must say, I do envy your freedom to ride out and experience the world."),
  ("playername__i_am_so_glad_to_see_you_i_trust_that_you_have_been_behaving_honorably_since_last_we_met", " I trust that you have been behaving honorably since last we met."),
  ("playername__i_am_so_glad_that_you_were_able_to_come", " I am so glad that you were able to come."),
##diplomacy start+ make both-gender versions (reg65 is speaker's gender)
  ("i_do_enjoy_speaking_to_you_but_i_am_sure_you_understand_that_our_people_cluck_their_tongues_at_a_woman_to_spend_too_long_conversing_with_a_man_outside_her_family__although_the_heavens_know_its_never_the_man_who_is_held_to_blame_", "I do enjoy speaking to you. But I am sure you understand that our people cluck their tongues at a {reg65?woman:boy} to spend too long conversing with a {man/woman} outside {reg65?her:his} family -- although the heavens know it's never the {man/woman} who is held to blame. "),
  ("as_much_as_i_enjoy_speaking_to_you_i_do_not_care_to_be_gossiped_about_by_others_who_might_lack_my_grace_and_beauty_", "As much as I enjoy speaking to you, I do not care to be gossiped about by others who might lack my grace and beauty. "),
  ("i_do_so_enjoy_speaking_to_you_but_as_a_daughter_of_one_of_the_great_families_of_this_land_i_must_set_an_example_of_propriety_", "I do so enjoy speaking to you. But as a {reg65?daughter:scion} of one of the great families of this land, I must set an example of propriety. "),
  ("i_do_so_enjoy_speaking_to_you_but_as_a_daughter_of_good_family_i_must_protect_my_reputation_", "I do so enjoy speaking to you. But as a {reg65?daughter:son} of good family, I must protect my reputation. "),
  ("although_it_is_kind_of_you_to_pay_me_such_attentions_i_suspect_that_you_might_find_other_ladies_who_may_be_more_inclined_to_return_your_affection", "Although it is kind of you to pay me such attentions, I suspect that you might find other {reg65?ladies:young men} who may be more inclined to return your affection."),
  ("as_flattered_as_i_am_by_your_attentions_perhaps_you_should_seek_out_another_lady_of_somewhat_shall_we_say_different_tastes", "As flattered as I am by your attentions, perhaps you should seek out another {reg65?lady:boy} of somewhat... shall we say... different tastes."),
  ("as_flattered_as_i_am_by_your_attentions_i_am_a_daughter_of_good_family_and_must_be_aware_of_my_reputation_it_is_not_seemly_that_i_converse_too_much_at_one_time_with_one_man_i_am_sure_you_understand_now_if_you_will_excuse_me", "As flattered as I am by your attentions, I am a {reg65?daughter:scion} of good family and must be aware of my reputation. It is not seemly that I converse too much at one time with one {man/woman}. I am sure you understand. Now, if you will excuse me..."),
##diplomacy end+ (making both-gender version)
  ("very_well__i_will_let_you_choose_the_time", "Very well -- I will let you choose the time."),
  ("good_i_am_glad_that_you_have_abandoned_the_notion_of_pushing_me_into_marriage_before_i_was_ready", "Good! I am glad that you have abandoned the notion of pushing me into marriage before I was ready."),
  ("rival_found_s4_reg0_relation", "{!}DEBUG : Rival found: {s4} ({reg0} relation)"),
  ("i_am", "I am"),
  ("s12", "{!}{s12},"),
  ("s12_s11_to_s14", "{s12} {s11} to {s14}"),
  ("s12", "{!}{s12}."),
  ("s12_i_am_here_for_the_feast", "{s12}. I am here for the feast."),
  ("another_tournament_dedication_oh_i_suppose_it_is_always_flattering", "Another tournament dedication? Oh, I suppose it is always flattering..."),
  ("do_you_why_what_a_most_gallant_thing_to_say", "Do you? Why, what a most gallant thing to say."),
  ("hmm_i_cannot_say_that_i_altogether_approve_of_such_frivolity_but_i_must_confess_myself_a_bit_flattered", "Hmm.. I cannot say that I altogether approve of such frivolity, but I must confess myself a bit flattered."),
  ("why_thank_you_you_are_most_kind_to_do_so", "Why, thank you. You are most kind to do so."),
  ("you_are_most_courteous_and_courtesy_is_a_fine_virtue_", "You are most courteous, and courtesy is a fine virtue. "),
  ("hmm_youre_a_bold_one_but_i_like_that_", "Hmm. You're a bold one, but I like that. "),
  ("ah_well_they_all_say_that_but_no_matter_a_compliment_well_delivered_is_at_least_a_good_start_", "Ah, well, they all say that. But no matter. A compliment well delivered is at least a good start. "),
  ("oh_do_you_mean_that_such_a_kind_thing_to_say", "Oh! Do you mean that? Such a kind thing to say!"),
##diplomacy start+ make gender correct
  ("you_are_a_most_gallant_young_man_", "You are a most gallant young {man/woman}. "),
##diplomacy end+
  ("_do_come_and_see_me_again_soon", " Do come and see me again soon."),
  ("you_intend_to_ask_s12_for_permission_to_marry_s15", "You intend to ask {s12} for permission to marry {s15}."),
  ("you_intend_to_ask_s12_to_pressure_s10_to_marry_you", "You intend to ask {s12} to pressure {s10} to marry you."),
  ("do_be_careful_i_am_so_much_endebted_to_you_for_this", "Do be careful! I am so much endebted to you for this..."),
  ("go_then__we_shall_see_which_of_you_triumphs", "Go, then -- we shall see which of you triumphs..."),
##diplomacy start+ make gender correct
  ("sigh_i_will_never_truly_understand_men_and_their_rash_actions", "Sigh... I will never truly understand {men/women}, and their rash actions..."),
  ("you_intend_to_challenge_s13_to_force_him_to_relinquish_his_suit_of_s11", "You intend to challenge {s13} to force {reg4?her:him} to relinquish his suit of {s11}."),
##diplomacy end+
  ("farewell", "Farewell."),
  ("farewell_playername", "Farewell, {playername}."),
  ("__we_believe_that_there_is_money_to_be_made_selling_", "  We believe that there is money to be made selling "),
  ("s14s15_", "{!}{s14}{s15}, "),
  ("_we_carry_a_selection_of_goods_although_the_difference_in_prices_for_each_is_not_so_great_we_hope_to_make_a_profit_off_of_the_whole", " We carry a selection of goods. Although the difference in prices for each is not so great, we hope to make a profit off of the whole."),
  ("s14and_other_goods", "{s14}and other goods."),
  ("_have_you_not_signed_a_truce_with_our_lord", " Have you not signed a truce with our lord?"),
  ("parole", "parole"),
  ("normal", "normal"),
  ("s51", "{!}{s51}"),
  ("_meanwhile_s51_reg2areis_being_held_in_the_castle_but_reg2havehas_made_pledges_not_to_escape_and_reg2areis_being_held_in_more_comfortable_quarters", " Meanwhile, {s51} {reg2?are:is} being held in the castle, but {reg2?have:has} made pledges not to escape, and {reg2?are:is} being held in more comfortable quarters."),
  ("you_may_be_aware_my_lord_of_the_quarrel_between_s4_and_s5_which_is_damaging_the_unity_of_this_realm_and_sapping_your_authority_if_you_could_persuade_the_lords_to_reconcile_it_would_boost_your_own_standing_however_in_taking_this_on_you_run_the_risk_of_one_the_lords_deciding_that_you_have_taken_the_rivals_side", "You may be aware, {sire/my lady}, of the quarrel between {s4} and {s5} which is damaging the unity of this realm and sapping your authority. If you could persuade the lords to reconcile, it would boost your own standing. However, in taking this on, you run the risk of one the lords deciding that you have taken the rival's side."),
  ("you_may_be_aware_my_lord_of_the_quarrel_between_s4_and_s5_which_is_damaging_the_unity_of_this_realm_and_sapping_your_authority_if_you_could_persuade_the_lords_to_reconcile_i_imagine_that_s7_would_be_most_pleased_however_in_taking_this_on_you_run_the_risk_of_one_the_lords_deciding_that_you_have_taken_the_rivals_side", "You may be aware, {my lord/my lady}, of the quarrel between {s4} and {s5} which is damaging the unity of this realm. If you could persuade the lords to reconcile, I imagine that {s7} would be most pleased. However, in taking this on, you run the risk of one the lords deciding that you have taken the rival's side."),
  ("_of_course_the_land_is_currently_at_peace_so_you_may_have_better_luck_in_other_realms", " Of course, the land is currently at peace, so you may have better luck in other realms."),
  ("here", "here"),
  ("over", "over"),
  ("s8_in_s12", "{s8} in {s12}"),
  ("_has_put_together_a_bounty_on_some_bandits_who_have_been_attacking_travellers_in_the_area", " has put together a bounty on some bandits who have been attacking travellers in the area."),
  ("_is_looking_for_a_way_to_avoid_an_impending_war", " is looking for a way to avoid an impending war."),
  ("_may_need_help_rescuing_an_imprisoned_family_member", " may need help rescuing an imprisoned family member."),
##diplomacy start+ fix pronoun with reg4
  ("_has_been_asking_around_for_someone_who_might_want_work_id_watch_yourself_with_him_though", " has been asking around for someone who might want work. I'd watch yourself with {reg4?her:him}, though."),
##diplomacy end+
  ("town", "town"),
  ("castle", "castle"),
  ("_but_he_is_holding_there_as_a_prisoner_at_dungeon_of_s13", " But {reg4?she:he} is being held there as a prisoner in the {s13} dungeon."), #SB : the town/castle
  ("log_entry_type_reg4_for_s4_total_entries_reg5", "{!}DEBUG : Log entry type: {reg4} for {s4}, total entries: {reg5}"),
  ("ERROR__reputation_type_for_s9_not_within_range", "{!}ERROR - reputation type for {s9} not within range"),
##diplomacy start+ make gender-flipped versions, using reg4 for gender of s9
#xxx yyy zzz TODO: make sure you set reg4 before calling this!
  ("they_say_that_s9_is_a_most_conventional_maiden__devoted_to_her_family_of_a_kind_and_gentle_temperament_a_lady_in_all_her_way", "They say that {s9} is a most conventional {reg4?maiden:lad} - devoted to {reg4?her:his} family, of a kind and gentle temperament, a {reg4?lady:young gentleman} in all {reg4?her:his} way."),
  ("they_say_that_s9_is_a_bit_of_a_romantic_a_dreamer__of_a_gentle_temperament_yet_unpredictable_she_is_likely_to_be_led_by_her_passions_and_will_be_trouble_for_her_family_ill_wager", "They say that {s9} is a bit of a romantic, a dreamer -- of a gentle temperament, yet unpredictable. {reg4?She:He} is likely to be led by {reg4?her:his} passions, and will be trouble for {reg4?her:his} family, I'll wager."),
  ("they_say_that_s9_is_determined_to_marry_well_and_make_her_mark_in_the_world_she_may_be_a_tremendous_asset_for_her_husband__provided_he_can_satisfy_her_ambition", "They say that {s9} is determined to marry well and make {reg4?her:his} mark in the world. {reg4?She:He} may be a tremendous asset for {reg4?her husband:his wife} -- provided {reg4?he:she} can satisfy {reg4?her:his} ambition!"),
  ("they_say_that_s9_loves_to_hunt_and_ride_maybe_she_wishes_she_were_a_man_whoever_she_marries_will_have_a_tough_job_keeping_the_upper_hand_i_would_say", "They say that {s9} loves to hunt and ride. Maybe {reg4?she:he} wishes {reg4?she:he} were a {reg4?man:woman}! Whoever {reg4?she:he} marries will have a tough job keeping the upper hand, I would say."),
  ("they_say_that_s9_is_a_lady_of_the_highest_moral_standards_very_admirable_very_admirable__and_very_hard_to_please_ill_warrant", "They say that {s9} is a {reg4?lady:young gentleman} of the highest moral standards. Very admirable, very admirable -- and very hard to please, I'll warrant."),
  ("s9_is_now_betrothed_to_s11_soon_we_believe_there_shall_be_a_wedding", "{s9} is now betrothed to {s11}. Soon, we believe, there shall be a wedding!"),
  ("i_have_not_heard_any_news_about_her", "I have not heard any news about {reg4?her:him}."),
  ("searching_for_rumors_for_s9", "{!}DEBUG : Searching for rumors for {s9}"),
  ("they_say_that_s9_has_shown_favor_to_s11_perhaps_it_will_not_be_long_until_they_are_betrothed__if_her_family_permits", "They say that {s9} has shown favor to {s11}. Perhaps it will not be long until they are betrothed -- if {reg4?her:his} family permits."),
  ("they_say_that_s9_has_been_forced_by_her_family_into_betrothal_with_s11", "They say that {s9} has been forced by {reg4?her:his} family into betrothal with {s11}."),
  ("they_say_that_s9_has_agreed_to_s11s_suit_and_the_two_are_now_betrothed", "They say that {s9} has agreed to {s11}'s suit, and the two are now betrothed."),
  ("they_say_that_s9_under_pressure_from_her_family_has_agreed_to_betrothal_with_s11", "They say that {s9}, under pressure from {reg4?her:his} family, has agreed to betrothal with {s11}."),
  ("they_say_that_s9_has_refused_s11s_suit", "They say that {s9} has refused {s11}'s suit."),
  ("they_say_that_s11_has_tired_of_pursuing_s9", "They say that {s11} has tired of pursuing {s9}."),
  ("they_say_that_s9s_family_has_forced_her_to_renounce_s11_whom_she_much_loved", "They say that {s9}'s family has forced {reg4?her:him} to renounce {s11}, whom {reg4?she:he} much loved."),
  ("they_say_that_s9_has_run_away_with_s11_causing_her_family_much_grievance", "They say that {s9} has run away with {s11}, causing {reg4?her:his} family much grievance."),
##Finished with gender-flipped versions
##diplomacy end+
  ("they_say_that_s9_and_s11_have_wed", "They say that {s9} and {s11} have wed."),
  ("they_say_that_s9_was_recently_visited_by_s11_who_knows_where_that_might_lead", "They say that {s9} was recently visited by {s11}. Who knows where that might lead!"),
  ("there_is_not_much_to_tell_but_it_is_still_early_in_the_season", "There is not much to tell, but it is still early in the season"),
  ("ERROR_lady_selected_=_s9", "{!}ERROR: lady selected = {s9}"),
  ("s12there_is_a_feast_of_the_s3_in_progress_at_s4_but_it_has_been_going_on_for_a_couple_of_days_and_is_about_to_end_", "{s12}There is a feast of the {s3} in progress at {s4}, but it has been going on for a couple of days and is about to end. "),
  ("s12there_is_a_feast_of_the_s3_in_progress_at_s4_which_should_last_for_at_least_another_day_", "{s12}There is a feast of the {s3} in progress at {s4}, which should last for at least another day. "),
  ("s12there_is_a_feast_of_the_s3_in_progress_at_s4_which_has_only_just_begun_", "{s12}There is a feast of the {s3} in progress at {s4}, which has only just begun. "),
  ("not_at_this_time_no", "Not at this time, no."),
  ("s12the_great_lords_bring_their_daughters_and_sisters_to_these_occasions_to_see_and_be_seen_so_they_represent_an_excellent_opportunity_to_make_a_ladys_acquaintance", "{s12}The great lords bring their daughters and sisters to these occasions to see and be seen, so they represent an excellent opportunity to make a lady's acquaintance."),
  ("you_will_not_be_disappointed_sirmadam_you_will_not_find_better_warriors_in_all_calradia", "You will not be disappointed {sir/madam}. You will not find better warriors in all Calradia."),
  ("your_excellency", "your excellency"),
  ("s10_and_s11", "{s10} and {s11}"),
  ("your_loyal_subjects", "your loyal subjects"),
  ("loyal_subjects_of_s10", "loyal subjects of {s10}"),
  ("the", "the"),
  ("we", "we"),
  ("track_down_s7_and_defeat_him_defusing_calls_for_war_within_the_s11", "Track down {s7} and defeat him, defusing calls for war within the {s11}."),
  ("track_down_the_s9_who_attacked_travellers_near_s8_then_report_back_to_the_town", "Track down the {s9} who attacked travellers near {s8}, then report back to the town."),
  ("fire_time__reg0_cur_time__reg1", "{!}DEBUG : fire time : {reg0}, cur time : {reg1}"),
  ("fire_set_up_time_at_city_reg0_is_reg1", "{!}fire set up time at city {reg0} is {reg1}"),
  ("our_power__reg3__enemy_power__reg4", "{!}our power : {reg3}, enemy power : {reg4}"),
  #end new auto generated strings

  ("do_you_wish_to_award_it_to_one_of_your_vassals", "Do you wish to award it to one of your vassals?"),
  ("who_do_you_wish_to_give_it_to", "Who do you wish to give it to?"),
  ("sire_my_lady_we_have_taken_s1_s2", "{Sire/My lady}, we have taken {s1}. {s2}"),
  ("s12i_want_to_have_s1_for_myself", "{s12}I want to have {s1} for myself. {s2}"),
  ("fiefs_s0", "(fiefs: {s0})"),

  #reserved strigs
  ("reserved_001", "{!}Reserved 001"),
  #reserved strings end

  ("production_setting_buy_from_market",      "We are buying raw materials from the market."),
  ("production_setting_buy_from_inventory",   "We are only using the raw materials in our inventory."),
  ("production_setting_produce_to_inventory", "We are putting our output into the inventory."),
  ("production_setting_produce_to_market",    "We are selling our output directly into the inventory."),



  #Strings to add...
  #Strings for political quest outcomes

  #Notes on companions
  #Pretender and companion strings
  #Redo map color strings


#STRINGS ADDED AFTER THE FREEZE
  ("feast_quest_expired", "You were unable to hold a feast as planned. Most likely, major faction campaigns or other events intervened. You may attempt to hold the feast again, if you wish."),
  ("whereabouts_unknown", "Whereabouts unknown."),
  ("mulberry_groves", "acres of mulberry groves"),
  ("olive_groves", "acres of olive groves"),
  ("acres_flax", "acres of flax fields"),
  ("enterprise_enemy_realm", "{Sir/Madame}, you are an enemy of this realm. We cannot allow you to buy land here."),
  ("intrigue_success_chance", "{!}Your modified relation: {reg5}, {s4}'s relation: {reg4}"),

  ("you_intend_to_denounce_s14_to_s13_on_behalf_of_s12", "You intend to privately denounce {s14} to {s13} on behalf of {s12}"),
  ("you_intend_to_denounce_s14_to_his_face_on_behalf_of_s14", "You intend to openly denounce {s14} to his face, on behalf of {s12}"),
  ("you_intend_to_bring_gift_for_s14", "You intend to bring velvet and furs to {s12}. Then, speak to {s14}, to see if {s12} was able to arrange a reconciliation."),

  #Strategy AI string
  ("we_will_gather_the_army_but_not_ride_until_we_have_an_objective", "We will gather the army, but not ride forth until we have an objective."),
  ("we_shall_lay_siege_to_an_easy_fortress_to_capture", "We are concentrating out forces on their most vulnerable fortress."),
  ("we_shall_strike_at_the_heart_of_our_foe_and_seize_the_fortress_of_s14", "We intend to strike a blow which will do them the greatest damage."),
  ("we_shall_take_the_fortress_of_s14_which_appears_easily_defensible", "We aim to take a fortress which is easy for us to defend."),
  ("we_shall_cut_a_fiery_trail_through_their_richest_lands_to_draw_them_out_to_battle", "We leave a fiery trail through their richest lands to draw them out to battle."),

  #Strategy AI string
  ("strategy_criticism_rash",     "I believe that this strategy is rash, and needlessly exposes our forces to danger."),
  ("strategy_criticism_cautious", "I believe that this strategy is overly cautious, and will see our army melt away from boredom without us achieving any successes."),


  ("tavernkeeper_invalid_quest", " had some sort of business going on, but I'm having trouble remembering the details."),


  ("faction_title_male_player", "Lord {s0}"),
  ("faction_title_male_1", "Count {s0}"),
  ("faction_title_male_2", "Boyar {s0}"),
  ("faction_title_male_3", "{s0} Noyan"),
  ("faction_title_male_4", "Jarl {s0}"),
  ("faction_title_male_5", "Count {s0}"),
  ("faction_title_male_6", "Emir {s0}"),

  ("faction_title_female_player", "Lady {s0}"),
  ("faction_title_female_1", "Countess {s0}"),
  ("faction_title_female_2", "Boyarina {s0}"),
  ("faction_title_female_3", "{s0} Hatun"),
  ("faction_title_female_4", "Grevinne {s0}"),
  ("faction_title_female_5", "Countess {s0}"),
  ("faction_title_female_6", "Sayeda {s0}"),

  ("faction_leader_title_male_player", "King {s0}"),
  ("faction_leader_title_male_1", "King {s0}"),
  ("faction_leader_title_male_2", "King {s0}"),
  ("faction_leader_title_male_3", "{s0} Khan"),
  ("faction_leader_title_male_4", "King {s0}"),
  ("faction_leader_title_male_5", "King {s0}"),
  ("faction_leader_title_male_6", "Sultan {s0}"),

  ("faction_leader_title_female_player", "Queen {s0}"),
  ("faction_leader_title_female_1", "Queen {s0}"),
  ("faction_leader_title_female_2", "Queen {s0}"),
  ("faction_leader_title_female_3", "{s0} Khatun"),
  ("faction_leader_title_female_4", "Queen {s0}"),
  ("faction_leader_title_female_5", "Queen {s0}"),
  ("faction_leader_title_female_6", "Sultana {s0}"),

  ("name_kingdom_text", "What will be the name of your kingdom?"),
  ("default_kingdom_name", "{s0}'s Kingdom"),

  #Defector joining
  ("lord_defects_ordinary", "Lord Defects^^{s1} has renounced {reg4?her:his} allegiance to the {s3}, and joined the {s2}"),
##diplomacy start+ fix gender of pronouns
  ("lord_defects_player",   "Lord Defects^^{s1} has renounced {reg4?her:his} allegiance to the {s3}. {reg4?She:He} has tentatively joined your kingdom. You may go to your court to receive a pledge, if you wish."),
  ("lord_defects_player_faction",   "Lord Defects^^{s1} has renounced {reg4?her:his} allegiance to the {s3}. {reg4?She:He} has tentatively joined your kingdom. You may go to your court to receive a pledge, if you wish."),
  ("lord_indicted_player_faction", "By order of {s6}, {s4} of the {s5} has been indicted for treason. The lord has been stripped of all {reg4?her:his} properties, and has fled for {reg4?her:his} life. {reg4?She:He} wishes to join your kingdom. You may find {reg4?her:him} in your court to receive {reg?her:his} allegiance, if you wish it."),
##diplomacy end+
  ("lord_indicted_dialog_approach", "Greetings, {my lord/my lady}. You may have heard of my ill treatment at the hands of {s10}. You have a reputation as one who treats {his/her} vassals well, and if you will have me, I would be honored to pledge myself as your vassal."),
  ("lord_indicted_dialog_approach_yes", "And I would be honored to accept your pledge."),
  ("lord_indicted_dialog_approach_no", "I'm sorry. Your service is not required."),
  ("lord_indicted_dialog_rejected",    "Indeed? Well, perhaps your reputation is misleading. Good day, {my lord/my lady} -- I go to see if another ruler in Calradia is more appreciative of my talents."),

##diplomacy start+ fix gender of pronouns with reg4
  ("_has_been_worried_about_bandits_establishing_a_hideout_near_his_home", " has been worried about bandits establishing a hideout in {reg4?her:his} area."),
##diplomacy end+
  ("bandit_lair_quest_description", "Find and destroy the {s9}, and report back to {s11}."),

  ("bandit_hideout_preattack", "You approach the hideout. The {s4} don't appear to have spotted you yet, and you could still sneak away unnoticed. The difficult approach to the site -- {s5} -- means that only a handful of troops in your party will be able to join the attack, and they will be unable to bring their horses. If your initial attack fails, the {s4} will easily be able to make their escape and disperse. Do you wish to attack the hideout, or wait for another occasion?"),
  ("bandit_hideout_failure", "The {s4} beat back your attack. You regroup, and advance again to find that they have dispersed and vanished into the surrounding countryside, where no doubt they will continue to threaten travellers."),
  ("bandit_hideout_success", "With their retreat cut off, the {s4} fall one by one to your determined attack. Their hideout, and their ill-gotten gains, as now yours."),

  ("bandit_approach_defile", "down a narrow defile"),
  ("bandit_approach_swamp", "through a pine swamp"),
  ("bandit_approach_thickets", "through a series of dense thickets"),
  ("bandit_approach_cliffs", "up a path along the side of a cliff"),
  ("bandit_approach_cove", "down a stream bed cutting through the sea-cliffs"),

  ("political_explanation_lord_lacks_center", "In this case, the fief should go to a lord who has no land and no income."),
  ("political_explanation_lord_took_center", "In this case, the fortress should go to the one who captured it."),
  ("political_explanation_most_deserving_friend", "In this case, I looked to my close friends and companions, and decided to give the fief to the most deserving."),
  ("political_explanation_most_deserving_in_faction", "In this case, I looked to all the lords of the realm, and decided to give the fief to the most deserving."),
  ("political_explanation_self", "In the absence of any clear other candidate, I nominate myself."),
  ("political_explanation_marshal", "I chose the most valiant of our nobles, whom I trust, and whose name is not currently tainted by controversy."),

  ("prisoner_at_large", "large, after the captors were defeated in battle. I expect your friend will resurface shortly."),

  ("quick_battle_scene_1", "Farmhouse"),
  ("quick_battle_scene_2", "Oasis"),
  ("quick_battle_scene_3", "Tulbuk's Pass"),
  ("quick_battle_scene_4", "Haima Castle"),
  ("quick_battle_scene_5", "Ulbas Castle"),

  ("quick_battle_troop_1", "There is a reason no one goes about the cities without armed guards once the sun sets, and that reason is Rodrigo de Braganca. Once a bright eyed merchant who arrived at Tihr with a small fortune in rubies and a dream to corner the velvet market, he was soon reduced to a pauper, having lost everything to cutthroat competition with the colluding Rhodok merchant guilds. But he soon turned measuring scales into swords, and applied his considerable business smarts into building up the deadliest criminal enterprise in Veluca, with hideouts and operations in every major town. He has attained his goal, for the price on his head is greater than the riches he once pursued. Now he takes great pleasure in relieving his former competitors of their worldly goods -� and worries."),
  ("quick_battle_troop_2", "Usiatra usurped leadership of the group of bandits that occupied Siri, a rural village in the southern deserts outside the realm of Calradia, in a curt and bloody fashion when she was seventeen years old. Under her direction, the band of ruffians quickly expanded their operations across the southlands. Her shrewd, decisive manner, combined with her merciless ambition which she acts upon with inhuman composure and cruelty, garners fanatic admiration from those that follow her. As such, amongst her own she lives a decadent, spoilt lifestyle -- built upon the violent plundering she exacts in her travels. Her military strength and natural strategic wit allowed her outfit to remain undealt with in her homeland, and now she turns her eye towards the rich lands of Calradia to sustain her war band."),
  ("quick_battle_troop_3", "The second son of a minor noble living near Uxkhal, Hegen was educated in the art of war and single combat. After being knighted he served as a paid knight in the army of the lord of Uxkhal and fought against the Vaegirs before leading a group of outriders that defeated a Khergit raid near Amere. The ensuing counter raid and the following two campaigns earned him glory and fame as a warrior. Unfortunately, he lost any chance of further prestige when peace was declared and he was discharged. With no hope of inheriting and his skills at war languishing in peace, he assembled other young warriors and set out as a mercenary captain. He now hopes to take advantage of the fact that Calradia never lacks warring states in need of mercenaries."),
  ("quick_battle_troop_4", "Konrad is a professional mercenary from the distant land of Balion, far beyond the vast western ocean. Having spent most of his years on campaign and seen countless battles, Konrad has grown to love his life as a soldier of fortune. Though he once had his nose flattened by a mace blow and has received many wounds, he has nevertheless survived this harsh existence through the strength of his arm, innate cunning and pure luck. Hearing of the lucrative career opportunities awaiting a man of his talents in Calradia, Konrad chartered a vessel and crossed the sea with his men in search of new wars to fight in. A sellsword with no ties to any of the Calradian states, he is more than happy to offer his services to any lord with a fat enough coin-purse."),
  ("quick_battle_troop_5", "Sverre is one of the so-called sea raiders -- freebooters and lawless men from the icy realm of Jumne beyond the North Sea, also said to be the ancestral home of the Nords. Already as a young man he has been along on many raids against both his distant cousins in the Wercheg region and the Vaegirs. However, Sverre was always a sharp lad, and it didn't take him long to see that Calradia was a far more prosperous land than his own, and that he could have a better life here than among his own people. During a raid on Jayek, Sverre stole away while his comrades were busy looting the village and taking captives. Passing himself off as a yokel from the Chalbek mountains, Sverre quickly built up a reputation for himself as a fierce fighter, and he now seeks his fortune at the head of a mercenary band."),
  ("quick_battle_troop_6", "Hailing from Charnye, in the far reaches of the Vaegir tundra, Borislav is a hunter. For all of his life he has tracked the beasts of the wild for their meat and fur, living off the land just as his forefathers had done in happier days, before the endless wars. Now, the game is quick to take fright from the constant sounds of battle, and the wanton slaughter of animals by soldiers has left empty those forests that have not been burnt down. Facing starvation, Borislav chose to turn his great skill with bow and spear, learned from hunting stag, wolf, and bear, to the practice of hunting men, and his steady hand and keen eye have claimed many lives. Borislav does not care much for the disputes of kingdoms, and is only really interested in keeping himself and his men fed."),
  ("quick_battle_troop_7", "Stavros was born in the independent city-state of Zendar, and spent much of his adult life serving in the town watch under the famous constable Hareck. Stavros' leadership and prowess were instrumental in ridding the area of the dreaded river pirates, but even he was powerless against the calamity that befell the city. When Zendar was razed to the ground by a great horde of sea raiders, Stavros fled the burning city in a crowd of refugees. After a brief period of wandering and odd jobs, he found a place in a mercenary company, eventually rising to become its leader due to his dedication and tactical aptitude. He now devotes most of his efforts to working with manhunters and local authorities against the sea raiders and other outlaws, trying to keep the land safe for travelers."),
  ("quick_battle_troop_8", "Growing up with one of the nomadic tribes deep in the desert beyond Sarranid lands, Gamara learned early on how to hunt with sling and spear. However, the simple life and pitiless conditions in the desert did not satisfy her, and she burned with a desire to see the great world beyond that she had heard so many wondrous tales about. Life is not easy for an adventuring young woman, and Gamara had to learn the ways of Calradia quickly. Taking the weapons and armor of a soldier who had attacked her after a dispute, Gamara now hides her beauty under thick Sarranid garb, and many never even suspect she is a woman �- certainly as a force on the battlefield she is as dangerous as any man. She has gathered about her a group of followers, and together they wander the war-torn land in search of glory."),
  ("quick_battle_troop_9", "Aethrod is not a noble person. He's changed his name twice, and is blamed for most of the crimes on Vaegir territory. True or not, he claims to never have taken an innocent man's life, and considers himself a patriotic citizen, several times bringing his band or renegades to the assistance of his faction, when it is threatened. In times of peace, however, most lords must be careful when he is in the vicinity due to his daring personality and willingness to challenge a lord. Born and rasied in the slums of Reyvadin, he learned how to use a bow at an early age and ran away from home a fourteen. Now at thirty two, his archery skills are near perfect and though he can't ride a horse well, he can hit one at the furthest of distances. Tough as nails and sharp as a hawk, he is a true local legend."),
  ("quick_battle_troop_10", "Being the daughter of one of the most infamous bandit leaders in the Sarranid realm isn't always easy, but Zaira seems to have managed quite well. Unlike most women she grew up learning the ways of the desert warrior and is deadly with the sword as well as the bow. While the other girls her age learned how to manage the household, Zaira learned how to best gut a merchant before taking his money. At the age of sixteen Zaira had killed more men than the average veteran in the Sultan's army. Just before her twentieth brithday her father was killed in brawl with another bandit leader. As the only child, Zaira now took control of her father's band. After avenging her father, she quickly picked up where he had left. Now she's on a good way of establishing her own reputation has a bandit leader."),
  ("quick_battle_troop_11", "Argo Sendnar had quite a diversified life. When he arrived at Calradia, working as a trader, he hoped for more income than in Lokti. Little did he know, that the wartorn Calradia was a wasps' nest for bandits and cutthroats that made trading a lot more complicated than in Lokti. Being bought out by another competeting trader, after losing all his goods and money due to caravan raids, he was forced to serve as a caravan guard to make a living. Despite his pathetic fighting skills, he soon found an employment on one of the more dangerous routes through Calradia. Due to sheer luck he managed to stay alive long enough to aquire enough combat experience and money to start his own buisness as a caravan master, offering his services to traders in need of defense for their goods."),
  ("quick_battle_troops_end", "{!}quick_battle_troops_end"),

  ("tutorial_training_ground_intro_message", "Walk around the training field and speak with the fighters to practice various aspects of Mount&Blade combat. You can use ASDW keys to move around. To talk to a character, approach him until his name appears on your screen, and then press the F key. You can also use the F key to pick up items, open doors and interact with objects. Press the Tab key to exit the tutorial any time you like."),

  ("map_basic", "Map"),
  ("game_type_basic", "Game Type"),
  ("battle", "Battle"),
  ("siege_offense", "Siege (Offense)"),
  ("siege_defense", "Siege (Defense)"),
  ("character", "Character"),
  ("biography", "Background"),
  ("player", "Player"),
  ("enemy", "Enemy"),
  ("faction", "Faction"),
  ("army_composition", "Army Composition"),
  ("army_size", "Army Size"),
  ("reg0_percent", "{!}{reg0}%"),
  ("reg0_men", "{reg0} men"),
  ("start", "Start"),
  ("i_need_to_raise_some_men_before_attempting_anything_else", "I need to raise some men before attempting anything else"),
  ("we_are_currently_at_peace", "We are currently at peace."),
  ("the_marshalship", "the marshalship"),

  ("you", "you"),
  ("myself", "myself"),
  ("my_friend_s15", "my friend {s15}"),
  ("custom_battle", "Custom Battle"),

  ("comment_intro_liege_affiliated_to_player", "I am told that you would dispute my claim to the crown of Calradia. Needless to say, I am not pleased by this news. However, we may still talk."),

  ("s21_the_s8_declared_war_out_of_personal_enmity", "{s21} The {s8} declared war out of personal enmity"),
  ("s21_the_s8_declared_war_in_response_to_border_provocations", "{s21} The {s8} declared war in response to border provocations"),
  ("s21_the_s8_declared_war_to_curb_the_other_realms_power", "{s21} The {s8} declared war to curb the other realm's power"),
  ("s21_the_s8_declared_war_to_regain_lost_territory", "{s21} The {s8} declared war to regain lost territory"),

  ("_family_", "^Family: "),

  ("we_are_conducting_recce", "We will first scout the area, and then decide what to do."),

  ("_family_", "^Family:"),
  ("s49_s12_s11_end", "{s49} {s12} ({s11})."),

  ("center_party_not_active", "is not our target, because we don't have a leader who has taken the field."),
  ("center_is_friendly", "is not our enemy."),
  ("center_is_already_besieged", "is already under siege."),
  ("center_is_looted_or_raided_already", "is already been laid waste."),
  ("center_marshal_does_not_want_to_attack_innocents", "is inhabited by common folk, who would suffer the most if the land is laid waste."),
  ("center_we_have_already_committed_too_much_time_to_our_present_siege_to_move_elsewhere", "is already under siege, so it would be a mistake to move elsewhere."),
  ("center_we_are_already_here_we_should_at_least_loot_the_village", "is close at hand, we should take hold of its wealth and lay waste to the rest."),

  ("center_far_away_we_can_reconnoiter_but_will_delay_decision_until_we_get_close", "NOT USED"),
  ("center_far_away_our_cautious_marshal_does_not_wish_to_reconnoiter", "is too far away, even to reconnoiter."),
  ("center_far_away_even_for_our_aggressive_marshal_to_reconnoiter", "is too far away, even to reconnoiter."),

  ("center_far_away_reason", "{s6} is further than {s5} to our centers, therefore it will be harder for us to protect after taking it."),
  ("center_closer_but_this_is_not_enought", "{s6} is closer than {s5} to our borders, but because of other reasons we are not attacking {s6} for now."),

  ("center_protected_by_enemy_army_aggressive", "is protected by enemy forces, which we believe to be substantially stronger than our own."),
  ("center_protected_by_enemy_army_cautious", "is protected by an enemy army, which we believe to be too strong to engage with confidence of victory."),

  ("center_cautious_marshal_believes_center_too_difficult_to_capture", "would require a bloody and risky siege."),
  ("center_even_aggressive_marshal_believes_center_too_difficult_to_capture", "is too heavily defended to capture."),

  ("center_value_outweighed_by_difficulty_of_capture", "is not of sufficient value to justify the difficulty of attacking it"),
  ("center_value_justifies_the_difficulty_of_capture", "can be taken, and is of sufficient value to justify an attack."),

  ("center_is_indefensible", "is too far away from our other fortresses to be defended."),
  ("we_are_waiting_for_selection_of_marshal", "We are waiting for the selection of a marshal"),
  ("best_to_attack_the_enemy_lands", "Given the size of our forces, we believe the best approach is to attack the enemy's lands."),
  ("we_believe_the_fortress_will_be_worth_the_effort_to_take_it", "We believe the fortress will be worth the effort to take it."),
  ("we_will_gather_to_defend_the_beleaguered_fortress", "We will gather to defend the beleaguered fortress"),
  ("the_enemy_temporarily_has_the_field", "The enemy temporarily has the field, and we should seek refuge until the storm passes"),
  ("center_has_not_been_scouted", "has not been recently scouted by our forces, but we can go there, and decide what to do when we get close."),
  ("we_have_assembled_some_vassals", "We have assembled some of the vassals, but we will wait until we have more before venturing into enemy territory."),

  ("we_are_waiting_here_for_vassals", "We are waiting for the vassals to join us."),
  ("we_are_travelling_to_s11_for_vassals", "We are travelling to {s11}, so that the vassals may more easily join our host before we ride forth."),

  ("center_strength_not_scouted", "We have not scouted it recently, and do not know how strongly it is defended"),
  ("center_strength_strongly_defended", "We believe it to be strongly defended"),
  ("center_strength_moderately_defended", "We believe it to be moderately well defended"),
  ("center_strength_weakly_defended", "We believe it to be weakly defended"),

  ("center_distant_from_concentration", "is close to us than it is to the main enemy army, which we have located. It could be attacked and destroyed before they are able to respond"),

  ("plus", "+"),
  ("minus", "-"),

  ("tutorial_training_ground_warning_no_weapon", "Hey, don't you think you need some sort of weapon before we try that? There should be some spare weapons over there. Just go pick one up."),
  ("tutorial_training_ground_warning_shield", "You need to put down your shield first. Scroll down with the mouse scroll-wheel to put down your shield."),
  ("tutorial_training_ground_warning_melee_with_parry", "You need to wield a melee weapon for this exercise. "),
  ("tutorial_training_ground_warning_melee", "Scroll up with your mouse wheel to equip a weapon. Scrolling up will equip next weapon while scrollng down will equip next shield."),
  ("tutorial_training_ground_attack_training", "Number of successful attacks: {reg0} / 5^Number of unsuccessful attacks: {reg1}^{s0}"),
  ("tutorial_training_ground_attack_training_down", "Make a thrust attack! (Move your mouse down while pressing the left mouse button)"),
  ("tutorial_training_ground_attack_training_up", "Make an overhead attack! (Move your mouse up while pressing the left mouse button)"),
  ("tutorial_training_ground_attack_training_left", "Attack from left! (Move your mouse left while pressing the left mouse button)"),
  ("tutorial_training_ground_attack_training_right", "Attack from right! (Move your mouse right while pressing the left mouse button)"),
  ("tutorial_training_ground_parry_training", "Number of successful parries: {reg0} / 5"),
  ("tutorial_training_ground_chamber_training", "Number of successful chambering blocks: {reg0} / 5"),
  ("tutorial_training_ground_archer_training", "Number of nice shots: {reg0} / 3^{s0}"),
  ("tutorial_training_ground_ammo_refill", "Your missiles are refilled for the tutorial."),
  ("tutorial_training_ground_archer_text_1", "Approach the {s0} and press F to pick it up."),
  ("tutorial_training_ground_archer_text_2", "Shoot the targets now."),
  ("tutorial_training_ground_archer_text_3", "The size of the targeting reticule indicates your accuracy. Press and hold down the left mouse button until the reticule shrinks down to its minimum size. Release the left mouse button when the reticule is at its smallest. If you wait too long the reticule will expand again."),
  ("tutorial_training_ground_archer_text_4", "Press R to toggle first person view. First person view makes it easier to aim with ranged weapons."),
  ("tutorial_training_ground_archer_text_5", "You have shot all the targets. Now talk to the trainer again."),
  ("tutorial_training_ground_horseman_text_1", "Go near the {s0} and press F to pick it up."),
  ("tutorial_training_ground_horseman_text_2", "Approach the horse and press F to mount."),
  ("tutorial_training_ground_horseman_text_3", "Ride towards the next waypoint."),
  ("tutorial_training_ground_horseman_text_4", "Strike the next dummy that has an arrow on top of it!"),
  ("tutorial_training_ground_horseman_text_5", "Shoot at the archery target that has an arrow on top of it!"),
  ("tutorial_training_ground_horseman_text_6", "You have finished the exercise successfully. Now go back to the trainer and talk to him."),

  ("the_great_lords_of_your_kingdom_plan_to_gather_at_your_hall_in_s10_for_a_feast", "The great lords of your kingdom plan to gather at your hall in {s10} for a feast"),
  ("your_previous_court_some_time_ago", "your previous court some time ago,"),
  ("awaiting_the_capture_of_a_fortress_which_can_serve_as_your_court", "awaiting the recapture of a fortress which can serve as your court."),
  ("but_if_this_goes_badly", " I value your advice. But if this goes badly, I shall hold you responsible."),

  ("i_realize_that_you_are_on_good_terms_with_s4_but_we_ask_you_to_do_this_for_the_good_of_the_realm", " I realize that you are on good terms with {s4}, but this is all for the good of the realm"),
##diplomacy start+ todo xxx gender correct ##diplomacy end+
  ("i_realize_that_you_are_on_good_terms_with_s4_but_the_blow_will_hurt_him_more", "I realize that you are on good terms with {s4} -- but this only means that your blow will hit him even harder!"),

  ("killed_bandit_at_alley_fight", "The merchant takes you to his house. Once inside, he stands by the door for a while checking the street, and then, finally convinced you have not been followed, comes near you to speak..."),
  ("wounded_by_bandit_at_alley_fight", "You are struck down. However, before you lose consciousness, you hear shouts and a rush of footfalls... You awake to find yourself indoors, weak but alive."),

  ("cannot_leave_now", "Cannot leave now."),
  ("press_tab_to_exit_from_town", "Press Tab to leave now. You can press Tab key to quickly exit any location in the game."),
  ("find_the_lair_near_s9_and_free_the_brother_of_the_prominent_s10_merchant", "Find the bandit lair near {s9}, and free the brother of the {s10} merchant."),
  ("please_sir_my_lady_go_find_some_volunteers_i_do_not_know_how_much_time_we_have", "{Sir/My lady} -- if you want to justify the trust which I have placed in you, then make a bit of haste. Go find some volunteers. I'm not sure how much time we have."),
  ("you_need_more_men_sir_my_lady", "Look -- you need more men. Right now, you have only {reg0} in your party. If you attack them with too few men, you may find their hideout by getting yourself dragged up to it in fetters, and that's not the plan. Do not take that risk. Go out and visit some more villages to find more volunteers, and then you can start paying them back in their own coin."),
  ("good_you_have_enough_men", "Good, good. You did well. You have enough men. Now, go and knock some of those robbers over the head, and make them tell you how to find their hideout."),
  ("do_not_waste_time_go_and_learn_where_my_brother_is", "Look, {sir/my lady}. Time is at a bit of premium, here. Now, if you could go find out where they are hiding my brother, that would be appreciated."),

  ("start_up_quest_message_1", "{s9} wants you to collect at least five men from nearby villages. After you collect these men, find and speak with him. He is in the tavern at {s1}"),
  ("start_up_quest_message_2", "Find and defeat a group of bandits lurking near {s9}, and learn where your employer's brother has been taken."),
  ("start_up_quest_message_3", "Rescue the merchant's brother from the robber's hideout located near {s9}."),
  ("start_up_first_quest", "You have taken your first quest. You may view your quest log by pressing 'Q' anytime in the game."),

  ("reason_1", "Our current objective is of greater value."),
  ("reason_2", "An attack on {s8} poses a greater danger to our realm."),
  ("reason_3", "We believe that {s8} faces a more immediate threat"),
  ("reason_4", "It may be because of the size of the enemy forces in the area."),
  ("reason_5", "I'm not sure."),
  ("reason_6", "We do not know how strongly it is defended."),
  ("reason_7", "We believe it to be strongly defended."),
  ("reason_8", "We believe it to be moderately well defended."),
  ("reason_9", "We believe it to be weakly defended."),

  ("has_decided_that_an_attack_on_", "has decided to attack"),
  ("this_would_be_better_worth_the_effort", "This would be better worth the effort, taking into consideration its value, and its distance, and the likely number of defenders."),
  ("has_decided_to_defend_", "has decided to defend"),
  ("before_going_offensive_we_should_protect_our_lands_if_there_is_any_threat_so_this_can_be_reason_marshall_choosed_defending_s4", "Before going offensive we should protect our lands if there is any threat. So this can be reason marshall choosed defending {s4}."),

  ("are_you_all_right", "Now... Let me explain my proposition"),
  ("you_are_awake", "Ah -- you're awake. It's good to see that you can still walk. You're lucky that we came along. I had been speaking with the watch, when we heard the sounds of a fight and ran to see what was happening. We didn't arrive in time to prevent you getting knocked down, but we may have saved you from getting your throat cut... Now... Maybe you can help me..."),
  ("save_town_from_bandits", "Save {s9} from bandits."),

  ("you_fought_well_at_town_fight_survived", "Hah! Well done -- I saw at least three of the enemy go down before you. Keep fighting like that, and you'll make quite a name for yourself in this land. "),
  ("you_fought_normal_at_town_fight_survived", "Well done! I hear you accounted for one or two of the bastards, and you're still on your feet. You can't ask for a better outcome of a battle than that..."),
  ("you_fought_bad_at_town_fight_survived", "Well, the enemy is in flight, and it looks like you're still on your feet. At the end of the day, that's all that's important in a battle."),

  ("you_fought_well_at_town_fight", "Ah! You're awake. You took quite a blow, there. But good news! We defeated them -- and you did them some real damage before you went down. If you hadn't been here, it could have gone very baldy. I'm grateful to you..."),
  ("you_wounded_at_town_fight", "Ah! You're alive. That's a relief. You took quite a blow, there. I'm not sure that you got any of them yourself, but thankfully, the rest of us were able to beat them. We'll need to see about getting you some treatment.... "),

  ("you_fought_well_at_town_fight_survived_answer", "Let every villain learn to fear the name {playername}!"),
  ("you_fought_normal_at_town_fight_survived_answer", "Ah, well, I'm proud to have done my bit along with the rest..."),
  ("you_fought_bad_at_town_fight_survived_answer", "Well, I was about to strike one down, but I slipped in some blood, you see..."),
  ("you_fought_well_at_town_fight_answer", "Ah well. I guess I don't mind a blow taken in a good cause."),
  ("you_wounded_at_town_fight_answer", "Right. I suppose I should be more careful."),

  ("unfortunately_reg0_civilians_wounded_during_fight_more", " Unfortunately, about {reg0} of my lads got themselves wounded. I should go look on on them."),
  ("unfortunately_reg0_civilians_wounded_during_fight", " Unfortunately, one of my lads took a pretty nasty blow. I should go see how he is doing."),
  ("also_one_another_good_news_is_any_civilians_did_not_wounded_during_fight", " Also, no one on our side was hurt very seriously. That's good news"),

  ("merchant_and_you_call_some_townsmen_and_guards_to_get_ready_and_you_get_out_from_tavern", "You leave the tavern and go out to the streets. Nervous looking young men are waiting in every street corner. You can see they have daggers and clubs concealed under their clothes, and catch a mixture of fear, anticipation and pride in the quick looks they throw at you as you pass by. Praying that your enemies have not been alarmed by this all too obvious bunch of plotters, you check your weapons for one last time and prepare yourself for the action ahead."),
  ("town_fight_ended_you_and_citizens_cleaned_town_from_bandits", "The remaining few bandits scatter off to the town's narrow alleys, only to be hunted down one by one by the angry townsfolk. Making sure that your victory is complete and all the wounded have been taken care of, you and the merchant head to his house to review the day's events."),
  ("town_fight_ended_you_and_citizens_cleaned_town_from_bandits_you_wounded", "You fall down with that last blow, unable to move and trying hard not to pass out. Soon the sounds of fighting filling the street gives way to the cheers of the townsmen and you realize with relief that your side won the day. Soon, friendly arms pick you up from the ground and you let yourself drift off to a blissful sleep. Hours later, you wake up in the merchants house."),


  ("journey_to_reyvadin", "You have come through the Vaegir highlands, a plateau exposed to the bitter winds from the north. The land here is frozen for most of the year, but the forests are rich with fur-bearing game, and the rivers are teaming with fish. The riches of the land draw the traders, but the traders in turn draw bandits. You saw the occasional dark figure mounted on a shaggy pony, watching the passage of your caravan from a snowy ridge, and were glad when the spires of Reyvadin came into view across the wide valley of the Boluk river."),
  ("journey_to_praven", "You came by caravan through the heartland of Calradia. Green shoots of wheat, barley and oats are beginning to push through the dark soil of the rolling hills, and on the lower slopes of the snowcapped mountains, herds of cattle and sheep are grazing on the spring grass. Occasionally, too, you catch sight of one of the great warhorses that are the pride of the Swadian nobility. The land here is rich -- but also troubled, as the occasional burnt-out farm bears witness. You keep a wide berth of the forests, where desperate men have taken refuge, and it is some relief when you crest a ridge and catch sight of the great port of Praven, its rooftops made golden by the last rays of the setting sun."),
  ("journey_to_jelkala", "You came by ship, skirting the cliffs where the Rhodok highlands meet the sea. Much of the coastline was obscured by tendrils of fog that snaked down the river valleys, but occasionally you caught sight of a castle watchtower rising above the mists -- and on one occasion, a beacon fire burning to warn of an enemy warband. You knew that you were relatively safe at sea, as you were too far south to risk encountering the sea raiders who trouble the coasts of the Nordic lands, but it was still a relief to reach the Selver estuary, gateway to the port of Jelkala, and see a Rhodok galley riding at anchor, its pennants fluttering in the evening breeze."),
  ("journey_to_sargoth", "You took passage with a trading longship, carrying gyrfalcons from the furthest reaches of the north to be bartered for linen and wool. It sailed early in the season, but the master reckoned that the risks of drifting ice and later winter storms could be justified by arriving ahead of the Sea Raiders, who by April would be sailing forth from their island lairs to ravage Calradia's coasts. It was some relief when your ship came in sight of the delta of the Vyl and Boluk rivers, and a short while later, rowed past tidal flats and coastal marshes to the city of Sargoth, home to the Sea Raiders' distant kinsmen, the Nordic lords, who a few generations ago had carved themselves a kingdom in this rich but troubled land."),
  ("journey_to_tulga", "You came with a caravan, crossing the mountains that border Calradia on the north and east, bringing spices from faraway lands to trade for wool and salt. The passes were still choked with snow, and it was hard going, but at last you crested a ridge and saw before you the Calradian steppes. On some hillsides the thin grass of spring was already turning yellow, but the lower slopes of the mountains were still a vibrant green. Herds of sheep and tawny steppe ponies drifted across them like clouds, testifying to the wealth of the Khergit khans. From time to time small groups of horsemen would follow your caravan from a distance, perhaps sizing up how well you could defend the wealth you carried, so it was with some relief that you saw the towers of Tulga rising up from the plains."),
  ("journey_to_shariz", "You came with a caravan, crossing the great desert to the east of Calradia. The bedouin guides chose your route carefully, leapfrogging through treacherous dune fields and across empty gravel plains to low-lying oases rich with orchards and date palms. Your great fear was that the caravan might lose its way and perish of thirst. The small bands of raiders who hovered just out of bowshot, waiting to pick off stragglers, were oddly a comfort -- at least water could be no more than a day's ride away. It was a great relief when the mountains came into view, and on the evening of the following day you crested a rocky pass and in the distance could make out the sea, and the towers of Shariz silhouetted against the sunset."),

  ("lost_tavern_duel_ordinary", "You slump to the floor, stunned by the drunk's last blow. Your attacker's rage immediately seems to slacken. He drops into a chair and sits there watching you, muttering under his breath, almost regretfully. A few of the other patrons manage to coax him to his feet and bundle him out the door. One of the others attends to your wounds, and soon you too are back on your feet, unsteady but alive."),
  ("lost_tavern_duel_assassin", "You slump to the floor, stunned by your attacker's last blow. Slowly and deliberately, he kneels down by your side, pulling a long knife from under his clothes. But before he can finish you off, the tavernkeeper, who seems to have regained his courage, comes up from behind and gives your attacker a clout behind the head. He loses his balance, and then, seeing that his chance to kill you has been lost, makes a dash for the door. He gets away. Meanwhile, the other tavern patrons bind your wounds and haul you to a back room to rest and recover."),
  ("lost_startup_hideout_attack", "You recover consciousness a short while later, and see that the kidnappers have celebrated their victory by breaking open a cask of wine, and have forgotten to take a few elementary precautions -- like binding your hands and feet. You manage to slip away. Based on the boisterous sounds coming from the hideout, you suspect that you may yet have some time to gather a few more followers and launch another attack."),
  ("reg1_blank_s3", "{!}{reg1} {s3}"),

("as_you_no_longer_maintain_an_independent_kingdom_you_no_longer_maintain_a_court",  "As you no longer rule an independent  kingdom, you no longer maintain a court"),

("rents_from_s0",  "Rents from {s0}:"),
("tariffs_from_s0",  "Tariffs from {s0}:"),
("general_quarrel",  " We've found ourselves on the opposite side of many arguments over the years, and bad blood has built up between us."),

#these are for resetting old {!} party names for the spawnpoints
("the_steppes", "the steppe"),
("the_deserts", "the desert"),
("the_tundra", "the tundra"),
("the_forests", "the forests"),
("the_highlands", "the highlands"),
("the_coast", "the coast"),
  ##diplomacy start+ make gender-correct
  ("my_lady_not_sufficient_chemistry", "My {lord/lady}, there are other {suitors/maidens} who have captured my heart."),
  ("my_lady_engaged_to_another", "My {lord/lady}, as I understand it, you are engaged to another."),
  ##diplomacy end+
  ("attempting_to_rejoin_party", "Attempting to rejoin party,"),
  ("separated_from_party", "Separated from party,"),
  ("whereabouts_unknown", "whereabouts unknown"),

  ("none_yet_gathered", "{!}None yet gathered"),

  ("betrothed", " Betrothed "),
  ("leading_party", "leading a party"),
  ("court_disbanded", "As you no longer rule an independent kingdom, your court has been disbanded"),
  ("i_am_not_accompanying_the_marshal_because_will_be_reappointment", " I am not accompanying the marshal, because I suspect that our ruler will shortly appoint another to that post."),

  ("persuasion_opportunity", "Persuasion opportunity.^Relation required for automatic success: {reg4}^Current relationship: {reg5}^Chance of success: {reg7}^Chance of losing {reg9} relation point(s): {reg8}"),

  ("marshal_warning", "You are not following {s1}. However, you will not suffer any penalty."),

  ("follow_army_quest_brief_2", "Your mission is complete. You may continue to follow {s9}'s army, if you wish further assignments."),

  ("greetings_playername__it_is_good_to_see_you_i_hope_that_you_have_had_success_in_your_efforts_to_make_your_name_in_the_world", " I am glad to see you. I trust you are having some success out there, making your name in the world"),

  ("minister_advice_select_fief", " Might I suggest that you select {s4}, as the vassals have been speculating about how you might assign it."),
  ("minister_advice_select_fief_wait", " Might I suggest that you wait until after you have appointed a marshal, as that will give time to the vassals to decide whom they wish to support."),
  ("minister_advice_fief_leading_vassal", " {s4}, by the way, has already received the support of {reg4} of your vassals."),
  ("unassigned_center", " (unassigned)"),
  ("s43_also_you_should_know_that_an_unprovoked_assault_is_declaration_of_war", "{s43} Also, as you are the ruler of your realm, you should know that this assault constitutes a declaration of war."),
  ("missing_after_battle", "Missing after battle"),
  ("retrieve_garrison_warning", " (Troops might not be retrievable if fortress awarded to another)"),

  ("s12s15_declared_war_to_control_calradia", "{s12}{s15} may attack {s16} without pretext, as a bid to extend control over all of Calradia."),
  ("offer_gift_description", " improve my standing by offering a gift."),
  ("resolve_dispute_description", " improve my standing by resolving a dispute."),
#diplomacy start+ potential gender correction
  ("feast_wedding_opportunity", " If your betrothed and {her/his} family are present, then this may be an opportunity for you to celebrate the wedding."),
#diplomacy end+
  ("s21_the_s8_declared_war_as_part_of_a_bid_to_conquer_all_calradia", "{s21}. The {s8} declared war with very little pretext, as part of a bid to conquer all Calradia."),
  ("master_vinter", "Master vinter"),
  ("s54_has_left_the_realm", "{s54} has left the realm."),
  ("enterprise_s5_at_s0", "Net revenue from {s5} at {s0}"),

  ("bread_site", "mill"),
  ("ale_site", "brewery"),
  ("oil_site", "oil press"),
  ("wine_site", "wine press"),
  ("tool_site", "ironworks"),
  ("leather_site", "tannery"),
  ("linen_site", "linen weavery"),
  ("wool_cloth_site", "wool weavery"),
  ("velvet_site", "dyeworks"),

  ("under_sequestration", "Under sequestration"),
  ("describe_secondary_input", " In addition, you will also need to purchase {s11} worth {reg10} denars."),
  ("profit", "profit"),
  ("loss", "loss"),

  ("server_name_s0", "Server Name: {s0}"),
  ("map_name_s0", "Map Name: {s0}"),
  ("game_type_s0", "Game Type: {s0}"),
  ("remaining_time_s0reg0_s1reg1", "Remaining Time: {s0}{reg0}:{s1}{reg1}"),
  ("you_are_a_lord_lady_of_s8_s9", "You are a {lord/lady} of {s8}.^{s9}"),
  ("you_are_king_queen_of_s8_s9", "You are {king/queen} of {s8}.^{s9}"),
  ("for_s4", " for {s4}"),

  ("cancel_fiancee_quest", " Also, you should please consider that other matter I had asked of you to have been successfully completed. It is not fit for me to commission you with tasks."),
  ("a_duel_request_is_sent_to_s0", "A duel offer is sent to {s0}."),
  ("s0_offers_a_duel_with_you", "{s0} offers a duel with you."),
  ("your_duel_with_s0_is_cancelled", "Your duel with {s0} is cancelled."),
  ("a_duel_between_you_and_s0_will_start_in_3_seconds", "A duel between you and {s0} will start in 3 seconds."),
  ("you_have_lost_a_duel", "You have lost a duel."),
  ("you_have_won_a_duel", "You have won a duel!"),
  ("server_s0", "[!]: {s0}"),
  ("disallow_ranged_weapons", "Disallow ranged weapons"),
  ("ranged_weapons_are_disallowed", "Ranged weapons are disallowed."),
  ("ranged_weapons_are_allowed", "Ranged weapons are allowed."),
  ("duel_starts_in_reg0_seconds", "Duel starts in {reg0} seconds..."),
# Lav modifications start (custom lord notes)
  ("lcn_faction", "He is loyal to {s41}."),
  ("lcn_stats", "Renown: {reg60}. Controversy: {reg61}."),
  ("lcn_prompt", "Enter your personal notes on {s41}:"),
# Lav modifications end (custom lord notes)
  ##diplomacy begin
###################################################################################
# Autoloot
###################################################################################
	("dplmc_none", "none"),

	("dplmc_item_pool_no_items", "There are currently no items in the item pool."),
	("dplmc_item_pool_one_item", "There is one item left in the item pool."),
	("dplmc_item_pool_many_items", "There are {reg20} items left in the item pool."),
	("dplmc_item_pool_abandon", "Leave the items in the item pool and continue."),
	("dplmc_item_pool_leave", "Done."),

	("dplmc_hero_not_upgrading_armor","not upgrading my armor"),
	("dplmc_hero_upgrading_armor","upgrading my own armor"),
	("dplmc_hero_not_upgrading_horse","not upgrading my horses"),
	("dplmc_hero_upgrading_horse","upgrading my own horses"),

	("dplmc_hero_wpn_slot_none","Keep current ({s10})"), #0
	("dplmc_hero_wpn_slot_horse","Horse"), #1 to maintain compatibility with header_items (item type 1 is horse)
	("dplmc_hero_wpn_slot_one_handed","One-handed Weapon"), #2
	("dplmc_hero_wpn_slot_two_handed","Two-handed Weapon"),  #3
	("dplmc_hero_wpn_slot_polearm_all","Polearms"), #4
	("dplmc_hero_wpn_slot_arrows","Arrows"), #5
	("dplmc_hero_wpn_slot_bolts","Bolts"), #6
	("dplmc_hero_wpn_slot_shield","Shield"), #7
	("dplmc_hero_wpn_slot_bow","Bow"), #8
	("dplmc_hero_wpn_slot_crossbow","Crossbow"), #9
	("dplmc_hero_wpn_slot_throwing","Throwing Weapon"), #10
  ##diplomacy start+ importing latest CC autoloot
	("dplmc_hero_wpn_slot_goods", "Goods "), #11
	("dplmc_hero_wpn_slot_head_armor", "Head armor "), #12
	("dplmc_hero_wpn_slot_body_armor", "Body armor "), #13
	("dplmc_hero_wpn_slot_foot_armor", "Foot armor "), #14
	("dplmc_hero_wpn_slot_hand_armor", "Hand armor "), #15
	("dplmc_hero_wpn_slot_pistol", "Pistol "), #16
	("dplmc_hero_wpn_slot_musket", "Musket "), #17
	("dplmc_hero_wpn_slot_bullets", "Bullets "), #18
	("dplmc_hero_wpn_slot_animal", "Animal "), #19
	("dplmc_hero_wpn_slot_book", "Book "), #20
  ##diplomacy end+
  #### Autoloot improved by rubik begin
	("dplmc_hero_wpn_slot_two_handed_one_handed","Two-handed/One-handed"), #11
  #### Autoloot improved by rubik end
###################################################################################
# End Autoloot
###################################################################################

  ("dplmc_gather_information", "gather information"),
  ("dplmc_conclude_non_agression", "conclude a non-aggression treaty"),
  ("dplmc_nearly_no", "nearly no"),
  ("dplmc_less_than_one_hundred", "less than one hundred"),
  ("dplmc_more_than_one_hundred", "more than one hundred"),
  ("dplmc_more_than_two_hundred", "more than two hundred"),
  ("dplmc_more_than_five_hundred", "more than five hundred"),
  ("dplmc_bring_gift", "bring the gift"),
  ("dplmc_exchange_prisoner","to exchange {s10} against {s11}"),
  ("dplmc_has_been_set_free", "{s7} has been set free."),
  ("dplmc_tax_very_low", "very low"),
  ("dplmc_tax_low", "low"),
  ("dplmc_tax_normal", "normal"),
  ("dplmc_tax_high", "high"),
  ("dplmc_tax_very_high", "very high"),
  ("dplmc_place_is_occupied_by_insurgents","The place is held by insurgents."),
  #nested diplomacy start+
  #Alter prepositions for dplmc_relation_****_**_ns
  #   indifferent against -> indifferent towards
  #   resentful against   -> resentful towards
  #Also changed pronouns to be gender-correct: "He" to {reg4?She:He}
  ("dplmc_relation_mnus_100_ns", "{reg4?She:He} seems to be vengeful towards {s59}."), # -100..-94
  ("dplmc_relation_mnus_90_ns",  "{reg4?She:He} seems to be vengeful towards {s59}."),  # -95..-84
  ("dplmc_relation_mnus_80_ns",  "{reg4?She:He} seems to be vengeful towards {s59}."),
  ("dplmc_relation_mnus_70_ns",  "{reg4?She:He} seems to be hateful towards {s59}."),
  ("dplmc_relation_mnus_60_ns",  "{reg4?She:He} seems to be hateful towards {s59}."),
  ("dplmc_relation_mnus_50_ns",  "{reg4?She:He} seems to be hostile towards {s59}."),
  ("dplmc_relation_mnus_40_ns",  "{reg4?She:He} seems to be angry towards {s59}."),
  ("dplmc_relation_mnus_30_ns",  "{reg4?She:He} seems to be resentful towards {s59}."),
  ("dplmc_relation_mnus_20_ns",  "{reg4?She:He} seems to be grumbling against {s59}."),
  ("dplmc_relation_mnus_10_ns",  "{reg4?She:He} seems to be suspicious towards {s59}."),
  ("dplmc_relation_plus_0_ns",   "{reg4?She:He} seems to be indifferent towards {s59}."),# -5...4
  ("dplmc_relation_plus_10_ns",  "{reg4?She:He} seems to be cooperative towards {s59}."), # 5..14
  ("dplmc_relation_plus_20_ns",  "{reg4?She:He} seems to be welcoming towards {s59}."),
  ("dplmc_relation_plus_30_ns",  "{reg4?She:He} seems to be favorable to {s59}."),
  ("dplmc_relation_plus_40_ns",  "{reg4?She:He} seems to be supportive to {s59}."),
  ("dplmc_relation_plus_50_ns",  "{reg4?She:He} seems to be friendly to {s59}."),
  ("dplmc_relation_plus_60_ns",  "{reg4?She:He} seems to be gracious to {s59}."),
  ("dplmc_relation_plus_70_ns",  "{reg4?She:He} seems to be fond of {s59}."),
  ("dplmc_relation_plus_80_ns",  "{reg4?She:He} seems to be loyal to {s59}."),
  ("dplmc_relation_plus_90_ns",  "{reg4?She:He} seems to be devoted to {s59}."),
  ("dplmc_s39_rival", " {reg4?She:He} scents rivals in {s39}"),
  ##nested diplomacy end+
  ("dplmc_s41_s39_rival", "{s41}, {s39}"),
  ##nested diplomacy start+
  #Changed pronouns to be gender-correct: "He" to {reg4?She:He}, etc.
  ("dplmc_s40_love_interest_s39", "{s40}. Aside from that {reg4?her:his} love interest is {s39}."),
  ("dplmc_s40_betrothed_s39", "{s40}. Aside from that {reg4?she:he} is betrothed to {s39}."),
  ("dplmc_reputation_martial", "It is said that {s46} is a martial person."),
  ("dplmc_reputation_debauched", "It is said that {s46} is a debauched person."),
  ("dplmc_reputation_pitiless", "It is said that {s46} is a pitiless person."),
  ("dplmc_reputation_calculating", "It is said that {s46} is a calculating person."),
  ("dplmc_reputation_quarrelsome", "It is said that {s46} is a quarrelsome person."),
  ("dplmc_reputation_goodnatured", "It is said that {s46} is a good-natured person."),
  ("dplmc_reputation_upstanding", "It is said that {s46} is a upstanding person."),
  ("dplmc_reputation_conventional", "It is said that {s46} is a conventional person."),
  ("dplmc_reputation_adventurous", "It is said that {s46} is a adventurous person."),
  ("dplmc_reputation_romantic", "It is said that {s46} is a romantic person."),
  ("dplmc_reputation_moralist", "It is said that {s46} is a moralist."),#Moralist -> moralist
  ("dplmc_reputation_ambitious", "It is said that {s46} is a ambitious person."),
  ("dplmc_reputation_unknown", "{s46}'s motivations are a closed book."),#Rewrote
  ##nested diplomacy end+
  ("dplmc_s21__the_s5_is_bound_by_alliance_not_to_attack_the_s14s18_it_will_expire_in_reg1_days", "{s21}^* The {s5} has formed an alliance with the {s14}.{s18} It will degrade into a defensive pact in {reg1} days."),
  ("dplmc_s21__the_s5_is_bound_by_defensive_not_to_attack_the_s14s18_it_will_expire_in_reg1_days", "{s21}^* The {s5} has agreed to a defensive pact with the {s14}.{s18} It will degrade into a trade agreement in {reg1} days."),
  ("dplmc_s21__the_s5_is_bound_by_trade_not_to_attack_the_s14s18_it_will_expire_in_reg1_days", "{s21}^* The {s5} has agreed to a trade agreement with the {s14}.{s18} It will degrade into a non-aggression pact in {reg1} days."),
  ("dplmc_small","small"),
  ("dplmc_medium","medium"),
  ("dplmc_big","big"),
  ("dplmc_elite","elite"),
  ("dplmc_very_decentralized", "very decentralized"),
  ("dplmc_quite_decentralized", "quite decentralized"),
  ("dplmc_little_decentralized", "a little decentralized"),
  ("dplmc_neither_centralize_nor_decentralized","neither too centralized nor decentralized"),
  ("dplmc_little_centralized", "a little centralized"),
  ("dplmc_quite_centralized", "quite centralized"),
  ("dplmc_very_centralized", "very centralized"),
  ("dplmc_very_plutocratic", "very plutocratic"),
  ("dplmc_quite_plutocratic", "quite plutocratic"),
  ("dplmc_little_plutocratic", "a little plutocratic"),
  ("dplmc_neither_aristocratic_nor_plutocratic","neither too aristocratic nor plutocratic"),
  ("dplmc_little_aristocratic", "a little aristocratic"),
  ("dplmc_quite_aristocratic", "quite aristocratic"),
  ("dplmc_very_aristocratic", "very aristocratic"),
  ("dplmc_all_free", "almost all free"),
  ("dplmc_mostly_free", "mostly free"),
  ("dplmc_usually_free", "usually free"),
  ("dplmc_mixture_serfs", "a mixture of serfs and freeman"),
  ("dplmc_usually_serfs", "usually serfs"),
  ("dplmc_mostly_serfs", "mostly serfs"),
  ("dplmc_all_serfs", "almost all serfs"),
  ("dplmc_very_quantity", "a vast number of soldiers"),
  ("dplmc_great_quantity", "very many soldiers"),
  ("dplmc_good_quantity", "many soldiers"),
  ("dplmc_mediocre_quality", "a mediocre quality"),
  ("dplmc_good_quality", "a good quality"),
  ("dplmc_great_quality", "a great quality"),
  ("dplmc_very_quality", "a very high quality"),
  ("dplmc_s21_the_s8_declared_war_to_fulfil_pact", "{s21}. The {s8} declared war to fulfil a pact"),
 ##diplomacy end
 ##diplomacy start+
 ("dplmc_very_laissez_faire", "very laissez-faire"),
 ("dplmc_quite_laissez_faire", "quite laissez-faire"),
 ("dplmc_little_laissez_faire", "a little laissez-faire"),
 ("dplmc_neither_mercantilist_nor_laissez_faire","neither particularly mercantilist nor entirely laissez-faire"),
 ("dplmc_little_mercantilist", "a little mercantilist"),
 ("dplmc_quite_mercantilist", "quite mercantilist"),
 ("dplmc_very_mercantilist", "very mercantilist"),

  ("dplmc_how_will_your_male_vassals_be_known","How will your male vassals be known?"),
  ("dplmc_how_will_your_female_vassals_be_known","How will your female vassals be known?"),
  ("dplmc_s40_married_s39", "{s40}. Aside from that {reg4?she:he} is married to {s39}."),
 #For fief exachange
 #TODO: customize responses by relation and/or personality
  ("dplmc_fief_exchange_ask_interest", "Would you be interested in exchanging fiefs?"),
  ("dplmc_fief_exchange_not_interested","No, I would not be interested in that."),

  ("dplmc_fief_exchange_listen", "This is somewhat unusual but not unprecendented.  I will listen.  Which fief of mine did you have in mind?"),
  ("dplmc_fief_exchange_listen_player_approval", "This is somewhat unusual, but since you're the {king/queen} there is no one to object.  Which fief of mine did you have in mind?"),
  ("dplmc_fief_exchange_listen_s10_approval", "This is somewhat unusual, but unless {s10} objects there is no reason we could not.  Which fief of mine did you have in mind?"),

  ("dplmc_fief_exchange_listen_2", "What fief do you offer in exchange?"),

  ("dplmc_fief_exchange_refuse_home", "I have no intention of giving up {s14}."),
  ("dplmc_fief_exchange_refuse_town", "I don't want to exchange a town for a castle or village."),
  ("dplmc_fief_exchange_refuse_castle", "I don't want to exchange a castle for a mere village."),
  ("dplmc_fief_exchange_refuse_rich", "I don't want to exchange a richer fief for one that much poorer."),
  ("dplmc_fief_exchange_refuse_s14_attack", "Speak of this to me later when {s14} is not under attack."),

  ("dplmc_fief_exchange_accept", "That exchange is acceptable to me."),
  ("dplmc_fief_exchange_accept_reg3_denars", "That exchange is acceptable to me, if you are willing to provide {reg3} denars to cover my expenses from the relocation."),

  ("dplmc_fief_exchange_confirm","It is settled then."),
  ("dplmc_fief_exchange_confirm_reg3_denars","It is settled then.  Here are your {reg3} denars."),
  #Other dialog
  ("dplmc_your_s11_s10", "Your {s11}, {s10}"),
  ("dplmc_reg6my_reg7spouse", "{reg6?M:m}y {reg7?love:{husband/wife}}"),
  #For trying to convince someone to support another candidate
  ("dplmc_refuse_support_s43_named_s4", "Support a {s43} like {s4}?  I think not."),
  #for political comments
  ("dplmc_comment_you_enfiefed_a_commoner_supportive",  "I understand that you have given {s51} to {s54}.  Others may find this controversial, but I believe that {s54} will be an able governor, and that {reg4?she:he} will not let you down."),
  #forms of address
  ("dplmc_sirmadame", "{sir/madame}"),
  ("dplmc_sirmadam",  "{sir/madam}"),
  ("dplmc_my_lordlady", "my {lord/lady}"),
  ("dplmc_your_highness", "your highness"),
  #expanded relation terms
  ("dplmc_grandfather", "grandfather"),
  ("dplmc_grandmother", "grandmother"),
  ("dplmc_grandson", "grandson"),
  ("dplmc_granddaughter", "granddaughter"),
  ("dplmc_half_brother", "half-brother"),#sharing a father or a mother, but not both
  ("dplmc_half_sister", "half-sister"),#sharing a father or a mother, but not both
  ("dplmc_sister_wife", "sister-wife"),#two women married to the same person
  ("dplmc_co_husband", "co-husband"),#two men married to the same person
  ("dplmc_co_spouse", "co-spouse"),#two people of different genders married to the same third person
  #not used in the relation scripts, but used elsewhere
  ("dplmc_friend", "friend"),
  ("dplmc_ally", "ally"),
  #status notifier
  ("s54_is_deceased", "{s54} is deceased."),
  ("dplmc_political_explanation_original_lord", "In this case, the fortress should go its original owner."),
  ##Utility: use these to avoid use of high-numbered string registers
 ("dplmc_s0_comma_s1",   "{!}{s0}, {s1}"),
 ("dplmc_s0_and_s1",     "{s0} and {s1}"),
 ("dplmc_s0_newline_s1", "{!}{s0}^{s1}"),
 ##diplomacy end+

 #morality objections
 ("hire_deserters", "take those scoundrels under our banner"),
 ("rotten_food", "consume those foul foodstuffs and find insects with every bite we take"),
 ("repress_farmers", "repress those peasants and propagate the violence inherent in the system"),
 ("stop_cheating", "waste time playing around with 'consoles' when you can just change the damn thing under camp options"),

 #auxiliary item types
 ("dplmc_hero_wpn_slot_morningstar","Two-handed/One-handed"), #21
 ("dplmc_hero_wpn_slot_lance","Lances"), #22
 ("dplmc_hero_wpn_slot_pikes","Pikes"), #23
 ("dplmc_hero_wpn_slot_halberd","Bladed Polearms"), #23
 ("dplmc_hero_wpn_slot_no_metatype","No Preference"), #23

  ("camera_keyboard", "To watch the fight you can use direction keys to move horizontally, numpad +- to move vertically, and numpad keys to rotate."),
  ("camera_mouse", "Use the mouse or numpad to rotate the camera, direction keys to move (holding Zoom will move faster). Tilt to adjust sensitivity, numpad to rotate and move vertically."),
  ("camera_follow", "Use tilt keys or mouse wheel to follow friendly agents. Hold Ctrl while using numpad to change view angle."),

  #ai behaviour strings (probably correct)
  ("ai_bhvr_hold", "Holding"),
  ("ai_bhvr_travel_to_party", "Travelling to Party"),
  ("ai_bhvr_patrol_location", "Patrolling Point"),
  ("ai_bhvr_patrol_party", "Patrolling around Party"),
  ("ai_bhvr_track_party", "Tracking Party"),
  ("ai_bhvr_attack_party", "Attacking Party"),
  ("ai_bhvr_avoid_party", "Avoiding Party"),
  ("ai_bhvr_travel_to_point", "Travelling to Point"),
  ("ai_bhvr_negotiate_party", "Negotiate Party"),
  ("ai_bhvr_in_town", "In Town"),
  ("ai_bhvr_travel_to_ship", "Travelling to Ship"),
  ("ai_bhvr_escort_party", "Accompanying Party"),
  ("ai_bhvr_driven_by_party", "Being Driven"),

  #party template names
  ("s5_transfer", "Transfer to {s5}"),
  ("s5_reinf", "Reinforcements from {s5}"),
  ("s5_scout", "{s5} Scout"),
  ("s5_patrol", "{s5} Patrol"),

  #companion mission strings
  ("preparing_prison_break", "Preparing a prison break in {s9}"),
  ("on_loan", "On loan"),
  ("accompanying_s5", "Accompanying {s5}"),

  # ("damage_cut", "cut"),
  # ("damage_pierce", "pierce"),
  # ("damage_blunt", "blunt"),

 #utility for keys array

  ("key_0", "0"),
  ("key_1", "1"),
  ("key_2", "2"),
  ("key_3", "3"),
  ("key_4", "4"),
  ("key_5", "5"),
  ("key_6", "6"),
  ("key_7", "7"),
  ("key_8", "8"),
  ("key_9", "9"),
  ("key_a", "A"),
  ("key_b", "B"),
  ("key_c", "C"),
  ("key_d", "D"),
  ("key_e", "E"),
  ("key_f", "F"),
  ("key_g", "G"),
  ("key_h", "H"),
  ("key_i", "I"),
  ("key_j", "J"),
  ("key_k", "K"),
  ("key_l", "L"),
  ("key_m", "M"),
  ("key_n", "N"),
  ("key_o", "O"),
  ("key_p", "P"),
  ("key_q", "Q"),
  ("key_r", "R"),
  ("key_s", "S"),
  ("key_t", "T"),
  ("key_u", "U"),
  ("key_v", "V"),
  ("key_w", "W"),
  ("key_x", "X"),
  ("key_y", "Y"),
  ("key_z", "Z"),
  ("key_numpad_0", "Numpad 0"),
  ("key_numpad_1", "Numpad 1"),
  ("key_numpad_2", "Numpad 2"),
  ("key_numpad_3", "Numpad 3"),
  ("key_numpad_4", "Numpad 4"),
  ("key_numpad_5", "Numpad 5"),
  ("key_numpad_6", "Numpad 6"),
  ("key_numpad_7", "Numpad 7"),
  ("key_numpad_8", "Numpad 8"),
  ("key_numpad_9", "Numpad 9"),
  ("key_num_lock", "Num lock"),
  ("key_numpad_slash", "Numpad slash"),
  ("key_numpad_multiply", "Numpad multiply"),
  ("key_numpad_minus", "Numpad minus"),
  ("key_numpad_plus", "Numpad plus"),
  ("key_numpad_enter", "Numpad enter"),
  ("key_numpad_period", "Numpad period"),
  ("key_insert", "Insert"),
  ("key_delete", "Delete"),
  ("key_home", "Home"),
  ("key_end", "End"),
  ("key_page_up", "Page up"),
  ("key_page_down", "Page down"),
  ("key_up", "Up"),
  ("key_down", "Down"),
  ("key_left", "Left"),
  ("key_right", "Right"),
  ("key_f1", "F1"),
  ("key_f2", "F2"),
  ("key_f3", "F3"),
  ("key_f4", "F4"),
  ("key_f5", "F5"),
  ("key_f6", "F6"),
  ("key_f7", "F7"),
  ("key_f8", "F8"),
  ("key_f9", "F9"),
  ("key_f10", "F10"),
  ("key_f11", "F11"),
  ("key_f12", "F12"),
  ("key_space", "Space"),
  ("key_escape", "Escape"),
  ("key_enter", "Enter"),
  ("key_tab", "Tab"),
  ("key_back_space", "Back space"),
  ("key_open_braces", "Open braces"),
  ("key_close_braces", "Close braces"),
  ("key_comma", "Comma"),
  ("key_period", "Period"),
  ("key_slash", "Slash"),
  ("key_back_slash", "Back slash"),
  ("key_equals", "Equals"),
  ("key_minus", "Minus"),
  ("key_semicolon", "Semicolon"),
  ("key_apostrophe", "Apostrophe"),
  ("key_tilde", "Tilde"),
  ("key_caps_lock", "Caps lock"),
  ("key_left_shift", "Left shift"),
  ("key_right_shift", "Right shift"),
  ("key_left_control", "Left control"),
  ("key_right_control", "Right control"),
  ("key_left_alt", "Left alt"),
  ("key_right_alt", "Right alt"),


  ("story_parent_noble","You came into the world a {reg11?daughter:son} of declining nobility,\
 owning only the house in which they lived. However, despite your family's hardships,\
 they afforded you a good education and trained you from childhood for the rigors of aristocracy and life at court."),
  ("story_parent_merchant","You were born the {reg11?daughter:son} of travelling merchants,\
 always moving from place to place in search of a profit. Although your parents were wealthier than most\
 and educated you as well as they could, you found little opportunity to make friends on the road,\
 living mostly for the moments when you could sell something to somebody."),
  ("story_parent_guard","As a child, your family scrabbled out a meagre living from your father's wages\
 as a guardsman to the local lord. It was not an easy existence, and you were too poor to get much of an\
 education. You learned mainly how to defend yourself on the streets, with or without a weapon in hand."),
  ("story_parent_forester","You were the {reg11?daughter:son} of a family who lived off the woods,\
 doing whatever they needed to make ends meet. Hunting, woodcutting, making arrows,\
 even a spot of poaching whenever things got tight. Winter was never a good time for your family\
 as the cold took animals and people alike, but you always lived to see another dawn,\
 though your brothers and sisters might not be so fortunate."),
  ("story_parent_nomad","You were a child of the steppe, born to a tribe of wandering nomads who lived\
 in great camps throughout the arid grasslands.\
 Like the other tribesmen, your family revered horses above almost everything else, and they taught you\
 how to ride almost before you learned how to walk."),
  ("story_parent_thief","As the {reg11?daughter:son} of a thief, you had very little 'formal' education.\
 Instead you were out on the street, begging until you learned how to cut purses, cutting purses\
 until you learned how to pick locks, all the way through your childhood.\
 Still, these long years made you streetwise and sharp to the secrets of cities and shadowy backways."),
  ("story_parent_priest","A {reg11?daughter:son} that nobody wanted, you were left to the church as a baby,\
 a foundling raised by the priests and nuns to their own traditions.\
 You were only one of many other foundlings and orphans, but you nonetheless received a lot of attention\
 as well as many years of study in the church library and before the altar. They taught you many things.\
 Gradually, faith became such a part of your life that it was no different from the blood coursing through your veins."),

  ##   As a {reg11?girl:boy} growing out of childhood,\
  ("story_childhood_page","you were sent to live in the court of one of the nobles of the land.\
 There, your first lessons were in humility, as you waited upon the lords and ladies of the household.\
 But from their chess games, their gossip, even the poetry of great deeds and courtly love, you quickly began to learn about the adult world of conflict\
 and competition. You also learned from the rough games of the other children, who battered at each other with sticks in imitation of their elders' swords."),
  ("story_childhood_apprentice","you apprenticed with a local craftsman to learn a trade. After years of hard work and study under your\
 new master, he promoted you to journeyman and employed you as a fully paid craftsman for as long as\
 you wished to stay."),
  ("story_childhood_urchin","you took to the streets, doing whatever you must to survive.\
 Begging, thieving and working for gangs to earn your bread, you lived from day to day in this violent world,\
 always one step ahead of the law and those who wished you ill."),
 ("story_childhood_nomad","you rode the great steppes on a horse of your own, learning the ways of the grass and the desert.\
 Although you sometimes went hungry, you became a skillful hunter and pathfinder in this trackless country.\
 Your body too started to harden with muscle as you grew into the life of a nomad {reg11?woman:man}."),
  ("story_childhood_stockboy","you apprenticed to a wealthy merchant, picking up the trade over years of working shops and driving caravans.\
 You soon became adept at the art of buying low, selling high, and leaving the customer thinking they'd\
 got the better deal."),
  ("story_childhood_mummer","you attached yourself to a troupe of wandering entertainers, going from town to town setting up mummer's\
 shows. It was a life of hard work, selling, begging and stealing your living from the punters who flocked\
 to watch your antics. Over time you became a performer well capable of attracting a crowd."),
  ("story_childhood_courtier","you spent much of your life at court, inserting yourself into the tightly-knit circles of nobility.\
 With the years you became more and more involved with the politics and intrigue demanded of a high-born {reg11?woman:man}.\
 You could not afford to remain a stranger to backstabbing and political violence, even if you wanted to."),
  ("story_childhood_noble","{reg11?you were trained and educated to the duties of a noble woman. You learned much about the household arts,\
 but even more about diplomacy and decorum, and all the things that a future husband might choose to speak of.\
 Truly, you became every inch as shrewd as any lord, though it would be rude to admit it aloud:you were trained and educated to perform the duties and wield the rights of a noble landowner.\
 The managing of taxes and rents were equally important in your education as diplomacy and even\
 personal defence. You learned everything you needed to become a lord of your own hall}."),
  ("story_childhood_acolyte","you became an acolyte in the church, the lowest rank on the way to priesthood.\
 Years of rigorous learning and hard work followed. You were one of several acolytes,\
 performing most of the menial labour in the church in addition to being trained for more holy tasks.\
 On the night of your adulthood you were allowed to conduct your first service.\
 After that you were no longer an acolyte {reg11?girl:boy}, but a {reg11?girl:boy} waiting to take your vows into the service of God."),


##  Though the distinction felt sudden to you, somewhere along the way you had become a {reg11?woman:man}, and the whole world seemed to change around you.\
  ("story_job_bravo","You left your old life behind to travel the roads as a mercenary, a bravo, guarding caravans for coppers\
 or bashing in heads for silvers. You became a {reg11?daughter:man} of the open road, working with bandits as often as against.\
 Going from fight to fight, you grew experienced at battle, and you learned what it was to kill."),
  ("story_job_merc","You signed on with a mercenary company and travelled far from your home. The life you found was rough and\
 ready, marching to the beat of strange drums and learning unusual ways of fighting.\
 There were men who taught you how to wield any weapon you desired, and plenty of battles to hone your skills.\
 You were one of the charmed few who survived through every campaign in which you marched."),
("story_job_poacher","Dissatisfied with common men's desperate scrabble for coin, you took to your local lord's own forests\
 and decided to help yourself to its bounty, laws be damned. You hunted stags, boars and geese and sold\
 the precious meat under the table. You cut down trees right under the watchmen's noses and turned them into\
 firewood that warmed many freezing homes during winter. All for a few silvers, of course."),
("story_job_craftsman","You pursued a career as a smith, crafting items of function and beauty out of simple metal.\
 As time wore on you became a master of your trade, and fine work started to fetch fine prices.\
 With food in your belly and logs on your fire, you could take pride in your work and your growing reputation."),
  ("story_job_peddler","Heeding the call of the open road, you travelled from village to village buying and selling what you could.\
 It was not a rich existence, but you became a master at haggling even the most miserly elders into\
 giving you a good price. Soon, you knew, you would be well-placed to start your own trading empire..."),
  ("story_job_preacher","You packed your few belongings and went out into the world to spread the word of God. You preached to\
 anyone who would listen, and impressed many with the passion of your sermons. Though you had taken a vow\
 to remain in poverty through your itinerant years, you never lacked for food, drink or shelter; the\
 hospitality of the peasantry was always generous to a rising {reg11?woman:man} of God."),
("story_job_troubadour","You set out on your own with nothing except the instrument slung over your back and your own voice.\
 It was a poor existence, with many a hungry night when people failed to appreciate your play,\
 but you managed to survive on your music alone. As the years went by you became adept at playing the\
 drunken crowds in your taverns, and even better at talking anyone out of anything you wanted."),
  ("story_job_squire", "When you were named squire to a noble at court, you practiced long hours with weapons,\
 learning how to deal out hard knocks and how to take them, too.\
 You were instructed in your obligations to your lord, and of your duties to those who might one day be your vassals.\
 But in addition to learning the chivalric ideal, you also learned about the less uplifting side\
 -- old warriors' stories of ruthless power politics, of betrayals and usurpations,\
 of men who used guile as well as valor to achieve their aims."),
  ("story_job_lady","You joined the tightly-knit circle of women at court, ladies who all did proper ladylike things,\
 the wives and mistresses of noble men as well as maidens who had yet to find a husband.\
 However, even here you found politics at work as the ladies schemed for prominence and fought each other\
 bitterly to catch the eye of whatever unmarried man was in fashion at court.\
 You soon learned ways of turning these situations and goings-on to your advantage. With it came the\
 realisation that you yourself could wield great influence in the world, if only you applied yourself\
 with a little bit of subtlety."),
 ("story_job_student","You found yourself as a student in the university of one of the great cities,\
 where you studied theology, philosophy, and medicine.\
 But not all your lessons were learned in the lecture halls.\
 You may or may not have joined in with your fellows as they roamed the alleys in search of wine, women, and a good fight.\
 However, you certainly were able to observe how a broken jaw is set,\
 or how an angry townsman can be persuaded to set down his club and accept cash compensation for the destruction of his shop."),

   ##^Only you know exactly what caused you to give up your old life and become an adventurer.\
  ("story_reason_revenge","Still, it was not a difficult choice to leave, with the rage burning brightly in your heart.\
 You want vengeance. You want justice. What was done to you cannot be undone,\
 and these debts can only be paid in blood..."),
  ("story_reason_death","All you can say is that you couldn't bear to stay, not with the memories of those you loved so close and so\
 painful. Perhaps your new life will let you forget,\
 or honour the name that you can no longer bear to speak..."),
  ("story_reason_wanderlust","You're not even sure when your home became a prison, when the familiar became mundane, but your dreams of\
 wandering have taken over your life. Whether you yearn for some faraway place or merely for the open road and the\
 freedom to travel, you could no longer bear to stay in the same place. You simply went and never looked back..."),
  ("story_reason_fervor","Regardless, the intense faith burning in your soul would not let you find peace in any single place.\
 There were others in the world, souls to be washed in the light of God. Now you preach wherever you go,\
 seeking to bring salvation and revelation to the masses, be they faithful or pagan. They will all know the\
 glory of God by the time you're done..."),
  ("story_reason_disown","However, you know you cannot go back. There's nothing to go back to. Whatever home you may have had is gone\
 now, and you must face the fact that you're out in the wide wild world. Alone to sink or swim..."),
  ("story_reason_greed","To everyone else, it's clear that you're now motivated solely by personal gain.\
 You want to be rich, powerful, respected, feared.\
 You want to be the one whom others hurry to obey.\
 You want people to know your name, and tremble whenever it is spoken.\
 You want everything, and you won't let anyone stop you from having it..."),

  ("story_all", "{s10}^^You started to learn about the world almost as soon as you could walk and talk. As a {reg11?girl:boy} growing out of childhood, {s11}^^\
Though the distinction felt sudden to you, somewhere along the way you had become a {reg11?woman:man}, and the whole world seemed to change around you. {s12}^^\
Only you know exactly what caused you to give up your old life and become an adventurer. {s13}"),

  ("chest_info", "Go near the chest and hold down the right mouse button for a while, then you can deposit or withdraw money from the chest. If you also have a chamberlain, you can access your treasury."),
#keep these string order relatively the same, because we're storing randomly within the range
#mercenary hiring, reg65 = gender, s0 = sir/madam, reg1 = plural/singular
  ("mercenary_intro_1", "You chose well, {s0}. {reg1?My {reg65?companions:lads}:I} know how to keep {reg1?their:my} word and earn {reg1?their:my} pay."),
  ("mercenary_intro_2", "Well done, {s0}. Keep the money and wine coming {reg1?my:our} way, and there's no foe in Calradia you need fear."),
  ("mercenary_intro_3", "{reg1?We are:I am} at your service, {s0}. Point {reg1?us:me} in the direction of those who need hurting, and {reg1?we:I}'ll do the rest."),
  ("mercenary_intro_4", "You will not be disappointed {s0}. You will not find {reg1?better warriors:a better fighter} in all Calradia."),
#bandit
  ("bandit_intro_1", "I can smell a fat purse a mile away. Methinks yours could do with some lightening, eh?"),
  ("bandit_intro_2", "Why, it be another traveller, chance met upon the road! I should warn you, country here's a mite dangerous for a good {fellow/woman} like you. But for a small donation my boys and I'll make sure you get rightways to your destination, eh?"),
  ("bandit_intro_3", "Well well, look at this! You'd best start coughing up some silver, friend, or me and my boys'll have to break you."),
  ("bandit_intro_4", "There's a toll for passin' through this land, payable to us, so if you don't mind we'll just be collectin' our due from your purse..."),
  ("bandit_outro_1", "Another fool come to throw {him/her}self on my weapon, eh? Fine, let's fight!"),
  ("bandit_outro_2", "We're not afraid of you, {sirrah/wench}. Time to bust some heads!"),
  ("bandit_outro_3", "That was a mistake. Now I'm going to have to make your death long and painful."),
  ("bandit_outro_4", "Brave words. Let's see you back them up with deeds, cur!"),
  ("bandit_outro_5", "I hope you die in a hole."),

#presentation names
  ("name_presentation_text", "What will be the name of {s1}?"),
  ("default_kingdom", "your realm"),
  ("default_town", "the capital"),
  ("default_party", "the party"),
  ("default_troop", "this companion"),
#training opponent descriptions
  ("tier_reg", "Good for you {lad/lass}. With this victory, you have advanced to the next training level. From now on your opponents will be regular fighters, not the riff-raff off the street, so be on your toes."),
  ("tier_vet", "Way to go {lad/lass}. Welcome to the third training level. From now on your opponents will be veteran fighters; soldiers and arena regulars and the like. These guys know some dirty tricks, so keep your defense up."),
  ("tier_champ", "You've got the heart of a champion, {lad/lass}, and the sword arm to match. From now on your opponents will be champion fighters. These are the cream of the crop, the finest warriors I have trained. If you can best three of them in a row, you will join their ranks."), # and they might join yours in return
  #("tier_finish", "It does my heart good to see such a promising talent. You have passed all tiers of training. You can now tell everyone that you have been trained by the master of the training field. If you have any recruits that need a lesson, don't hesitate to see me."),
#training ground strings
  ("ctm_melee", "Your opponent{reg0?s are: is} ready for the fight."),
  ("ctm_ranged", "Stay behind the line on the ground and shoot the targets. Try not to waste any shots."),
  ("ctm_mounted", "Try to destroy as many targets as you can. You have two and a half minutes to clear the track."),
#utility from CC for item modifiers
  ("imod_plain", "{!}"),
  ("imod_cracked", "Cracked "),
  ("imod_rusty", "Rusty "),
  ("imod_bent", "Bent "),
  ("imod_chipped", "Chipped "),
  ("imod_battered", "Battered "),
  ("imod_poor", "Poor "),
  ("imod_crude", "Crude "),
  ("imod_old", "Old "),
  ("imod_cheap", "Cheap "),
  ("imod_fine", "Fine "),
  ("imod_well_made", "Well Made "),
  ("imod_sharp", "Sharp "),
  ("imod_balanced", "Balanced "),
  ("imod_tempered", "Tempered "),
  ("imod_deadly", "Deadly "),
  ("imod_exquisite", "Exquisite "),
  ("imod_masterwork", "Masterwork "),
  ("imod_heavy", "Heavy "),
  ("imod_strong", "Strong "),
  ("imod_powerful", "Powerful "),
  ("imod_tattered", "Tattered "),
  ("imod_ragged", "Ragged "),
  ("imod_rough", "Rough "),
  ("imod_sturdy", "Sturdy "),
  ("imod_thick", "Thick "),
  ("imod_hardened", "Hardened "),
  ("imod_reinforced", "Reinforced "),
  ("imod_superb", "Superb "),
  ("imod_lordly", "Lordly "),
  ("imod_lame", "Lame "),
  ("imod_swaybacked", "Swaybacked "),
  ("imod_stubborn", "Stubborn "),
  ("imod_timid", "Timid "),
  ("imod_meek", "Meek "),
  ("imod_spirited", "Spirited "),
  ("imod_champion", "Champion "),
  ("imod_fresh", "Fresh "),
  ("imod_day_old", "Day Old "),
  ("imod_two_day_old", "Two Day Old "),
  ("imod_smelling", "Smelling "),
  ("imod_rotten", "Rotten "),
  ("imod_large_bag", "Large Bag "),

  #lowercase descriptions for disguises
  ("pilgrim_disguise", "pilgrim"),
  ("farmer_disguise", "farmer"),
  ("hunter_disguise", "hunter"),
  ("merchant_disguise", "merchant"),
  ("guard_disguise", "guard"),
  ("bard_disguise", "bard"),

  #recolor presentation strings
  ("html", "HTML Code: {s0}"),
  ("html_color", "{!}#{reg11}{reg12}{reg13}{reg14}{reg15}{reg16}"),
  ("color_of", "Color of {s0}:"),
  ("color_banner", "the back of your banner"),
  ("color_group", "the {s0} group on the minimap"),

  ("tactical_controls", "Use the keyboard NUMBERS to select a division. Press 0 to select your entire force.^^\
Use F1-F4 to order selected divisions. Keep the F1 key down to place selected divisions. One may target an enemy division through this mechanism.^^\
Pressing the ENTER key often initiates an overhead Strategy Camera.^^\
Pressing the BACKSPACE key often initiates a Battle Command Display with 'radar.'"),
  ("division_placement", "When ONE division is selected, the center of its front rank is placed at the spot indicated.^^\
When MANY divisions are selected, they are separated and spread out as if the player were standing at the spot indicated.^^\
One may memorize the placement of selected divisions relative to the player by pressing F2, F7. Default is infantry to the left, cavalry right, and ranged forward."),
  ("formations", "The Complex Formations on the Battle Menu are:^^\
- RANKS with best troops up front^\
- SHIELD WALL, ranks with shields in front and longer weapons in back^\
- WEDGE with best troops up front^\
- SQUARE in no particular order^\
- NO FORMATION^^\
Even in the last case, the player can make formations up to four lines by ordering Stand Closer enough times."),

  ("january_reg1_reg2_v2", "January {reg1}, {reg2}"),
  ("february_reg1_reg2_v2", "February {reg1}, {reg2}"),
  ("march_reg1_reg2_v2", "March {reg1}, {reg2}"),
  ("april_reg1_reg2_v2", "April {reg1}, {reg2}"),
  ("may_reg1_reg2_v2", "May {reg1}, {reg2}"),
  ("june_reg1_reg2_v2", "June {reg1}, {reg2}"),
  ("july_reg1_reg2_v2", "July {reg1}, {reg2}"),
  ("august_reg1_reg2_v2", "August {reg1}, {reg2}"),
  ("september_reg1_reg2_v2", "September {reg1}, {reg2}"),
  ("october_reg1_reg2_v2", "October {reg1}, {reg2}"),
  ("november_reg1_reg2_v2", "November {reg1}, {reg2}"),
  ("december_reg1_reg2_v2", "December {reg1}, {reg2}"),

#DtheHun
 #custom item
  ("tutorial_custom_item", "You may have customizable item equipped. Press ""Wiew Outfit"" and ""Inventory Window"" keys to open the Customization Window in character view, or find it in the Camp Actions Menu."),
  ("dont_have_custom_item", "You don't have any customizable item equipped!"),
 #tattoos
  ("ca_skin", "No_tattoo"),
  ("ca_amazon", "Amazon_tattoo"),
  ("ca_risty", "Risty_tattoo"),
  ("ca_custom", "Custom_tattoo"),
 #response
 #censure
  ("censure_response_0", "It's not you, it's me."),
  ("censure_response_1", "No way!"),
  ("censure_response_2", "How about this one?"),
  ("censure_response_3", "You can't be serious!"),
  ("censure_response_4", "Not my style."),
  ("censure_response_5", "It's just too revealing."),
  ("censure_response_6", "I need more cover."),
  ("censure_response_7", "That would be inappropriate."),
  ("censure_response_8", "I have a better idea."),
  ("censure_response_9", "I have a better idea."),
  ("censure_response_10", "Are you kidding me?"),
  ("censure_response_end", "END"),

#utility for skill names
]+[
("skl_"+skills[x][0], skills[x][1]) for x in range(0, len(skills))]

# modmerger_start version=201 type=2
try:
    component_name = "strings"
    var_set = { "strings" : strings }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
