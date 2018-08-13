# Formations AI by Motomataru
# rel. 12/26/10

from formations_constants import formation_delay_for_spawn

#AI variables
AI_long_range	= 13000	#do not put over 130m if you want archers to always fire
AI_firing_distance	= AI_long_range / 2
AI_charge_distance	= 2000
AI_for_kingdoms_only	= 1
Percentage_Cav_For_New_Dest	= 40
Hold_Point	= 100	#archer hold if outnumbered
Advance_More_Point	= 100 - Hold_Point * 100 / (Hold_Point + 100)	#advance 'cause expect other side is holding
AI_Delay_For_Spawn	= formation_delay_for_spawn + .1	#fire AFTER formations init
AI_Max_Reinforcements	= 2	#maximum number of reinforcement stages in a battle
AI_Replace_Dead_Player	= 1

#Battle Phases
BP_Setup	= 1
BP_Jockey	= 2
BP_Fight	= 3

#positions used in a script, named for convenience
Nearest_Enemy_Troop_Pos	= 36	#pos36	used only by infantry AI
Nearest_Enemy_Battlegroup_Pos	= 37	#pos37	used only by ranged AI
Nearest_Threat_Pos	= Nearest_Enemy_Troop_Pos	#used only by cavalry AI
Nearest_Target_Pos	= Nearest_Enemy_Battlegroup_Pos	#used only by cavalry AI
Infantry_Pos	= 38	#pos38
Archers_Pos	= 39	#pos39
Cavalry_Pos	= 40	#pos40
Team_Starting_Point	= 50	#pos50

#positions used through battle
Team0_Cavalry_Destination	= 51	#pos51
Team1_Cavalry_Destination	= 53	#pos53
Team2_Cavalry_Destination	= 54	#pos54
Team3_Cavalry_Destination	= 55	#pos55
#Team_Starting_Point	= 56	#pos56