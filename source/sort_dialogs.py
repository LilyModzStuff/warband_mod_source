from header_common import *
from header_dialogs import *
from header_operations import *
from module_constants import *

####################################################################################################################
# During a dialog, the dialog lines are scanned from top to bottom.
# If the dialog-line is spoken by the player, all the matching lines are displayed for the player to pick from.
# If the dialog-line is spoken by another, the first (top-most) matching line is selected.
#
#  Each dialog line contains the following fields:
# 1) Dialogue partner: This should match the person player is talking to.
#    Usually this is a troop-id.
#    You can also use a party-template-id by appending '|party_tpl' to this field.
#    Use the constant 'anyone' if you'd like the line to match anybody.
#    Appending '|plyr' to this field means that the actual line is spoken by the player
#    Appending '|other(troop_id)' means that this line is spoken by a third person on the scene.
#       (You must make sure that this third person is present on the scene)
#
# 2) Starting dialog-state:
#    During a dialog there's always an active Dialog-state.
#    A dialog-line's starting dialog state must be the same as the active dialog state, for the line to be a possible candidate.
#    If the dialog is started by meeting a party on the map, initially, the active dialog state is "start"
#    If the dialog is started by speaking to an NPC in a town, initially, the active dialog state is "start"
#    If the dialog is started by helping a party defeat another party, initially, the active dialog state is "party_relieved"
#    If the dialog is started by liberating a prisoner, initially, the active dialog state is "prisoner_liberated"
#    If the dialog is started by defeating a party led by a hero, initially, the active dialog state is "enemy_defeated"
#    If the dialog is started by a trigger, initially, the active dialog state is "event_triggered"
# 3) Conditions block (list): This must be a valid operation block. See header_operations.py for reference.  
# 4) Dialog Text (string):
# 5) Ending dialog-state:
#    If a dialog line is picked, the active dialog-state will become the picked line's ending dialog-state.
# 6) Consequences block (list): This must be a valid operation block. See header_operations.py for reference.
# 7) Voice-over (string): sound filename for the voice over. Leave here empty for no voice over
####################################################################################################################

dialogs = [

  [anyone|plyr,"member_talk", [
    (troop_get_slot, ":is_skill_companion", "$g_talk_troop", slot_troop_skill_companion),
    (eq, ":is_skill_companion", 0),
  ], "I'd like you to try to keep out of the fighting.", "member_keep_out_fighting",[]],
  
  [anyone,"member_keep_out_fighting", [], "Oh? Are you sure?", "member_keep_out_fighting_confirm",[]],
  
  [anyone|plyr,"member_keep_out_fighting_confirm", [], "Yes, you have other skills that are too valuable for me to risk losing you in battle.", "member_keep_out_fighting_yes",[
    (troop_set_slot, "$g_talk_troop", slot_troop_skill_companion, 1),
  ]],
  
  [anyone|plyr,"member_keep_out_fighting_confirm", [], "Actually, never mind.", "member_keep_out_fighting_no",[]],
  
  [anyone,"member_keep_out_fighting_yes", [
    (store_conversation_troop,"$g_talk_troop"),
    (troop_is_hero,"$g_talk_troop"),
    (troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
    (str_store_string, s5, ":honorific"),
  ], "As you say {s5}. Unless you order me otherwise, I will try to be the last to enter the battle. Anything else?", "member_talk",[]],
  
  [anyone,"member_keep_out_fighting_no", [], "Very well. Anything else?", "member_talk",[]],
  
  [anyone|plyr,"member_talk", [
    (troop_get_slot, ":is_skill_companion", "$g_talk_troop", slot_troop_skill_companion),
    (eq, ":is_skill_companion", 1),
  ], "I'd like you to take an active role in battles from now on.", "member_join_in_fighting",[]],
  
  [anyone,"member_join_in_fighting", [], "I see. Is this definitely what you want?", "member_join_in_fighting_confirm",[]],
  
  [anyone|plyr,"member_join_in_fighting_confirm", [], "Yes, your skill on the battlefield is what we need now.", "member_join_in_fighting_yes",[
    (troop_set_slot, "$g_talk_troop", slot_troop_skill_companion, 0),
  ]],
  
  [anyone|plyr,"member_join_in_fighting_confirm", [], "Actually, never mind.", "member_join_in_fighting_no",[]],

  [anyone,"member_join_in_fighting_yes", [
    (store_conversation_troop,"$g_talk_troop"),
    (troop_is_hero,"$g_talk_troop"),
    (troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
    (str_store_string, s5, ":honorific"),
  ], "As you command {s5}. I will take my position with the rest of the troops from now on. Anything else?", "member_talk",[]],
  
  [anyone,"member_join_in_fighting_no", [], "Very well. Anything else?", "member_talk",[]],
  
]

def add_dialog(dialogs, new_dialog, bottom_offset):
  if bottom_offset == 0:
    dialogs.append(new_dialog)
  else:
    state = new_dialog[1]
    indices = []
    for i in xrange(0, len(dialogs)):
      dialog = dialogs[i]
      if dialog[1] == state:
        indices.append(i)
    if len(indices) == 0:
      index = len(dialogs)
    elif len(indices) < bottom_offset:
      index = indices[0]
    else:
      index = indices[len(indices) - bottom_offset]
    dialogs.insert(index, new_dialog)

def modmerge(var_set):
  try:
      var_name_1 = "dialogs"
      orig_scripts = var_set[var_name_1]
      
  # START do your own stuff to do merging

      for dialog in dialogs:
        state = dialog[1]
        if state == "member_talk":
          add_dialog(orig_scripts, dialog, 1)
        else:
          add_dialog(orig_scripts, dialog, 0)

  # END do your own stuff
      
  except KeyError:
      errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
      raise ValueError(errstring)