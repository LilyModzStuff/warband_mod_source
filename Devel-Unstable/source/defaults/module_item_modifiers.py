####################################################################################################################
#  Each item modifier record contains the following fields:
#  1) Modifier id: used for referencing modifiers in other files.
#  2) Modifier name: how this modifier will change item name, with %s being substituted by item's base name.
#  3) Price modifier: coefficient for item price when modifier is in effect.
#  4) Rarity modifier: how common are items with this modifier.
####################################################################################################################

item_modifiers = [

    ("plain", "Plain %s", 1.000000, 1.000000),
    ("cracked", "Cracked %s", 0.500000, 1.000000),
    ("rusty", "Rusty %s", 0.550000, 1.000000),
    ("bent", "Bent %s", 0.650000, 1.000000),
    ("chipped", "Chipped %s", 0.720000, 1.000000),
    ("battered", "Battered %s", 0.750000, 1.000000),
    ("poor", "Poor %s", 0.800000, 1.000000),
    ("crude", "Crude %s", 0.830000, 1.000000),
    ("old", "Old %s", 0.860000, 1.000000),
    ("cheap", "Cheap %s", 0.900000, 1.000000),
    ("fine", "Fine %s", 1.900000, 0.600000),
    ("well_made", "Well_Made %s", 2.500000, 0.500000),
    ("sharp", "Sharp %s", 1.600000, 0.600000),
    ("balanced", "Balanced %s", 3.500000, 0.500000),
    ("tempered", "Tempered %s", 6.700000, 0.400000),
    ("deadly", "Deadly %s", 8.500000, 0.300000),
    ("exquisite", "Exquisite %s", 14.500000, 0.300000),
    ("masterwork", "Masterwork %s", 17.500000, 0.300000),
    ("heavy", "Heavy %s", 1.900000, 0.700000),
    ("strong", "Strong %s", 4.900000, 0.400000),
    ("powerful", "Powerful %s", 3.200000, 0.400000),
    ("tattered", "Tattered %s", 0.500000, 1.000000),
    ("ragged", "Ragged %s", 0.700000, 1.000000),
    ("rough", "Rough %s", 0.600000, 1.000000),
    ("sturdy", "Sturdy %s", 1.700000, 0.500000),
    ("thick", "Thick %s", 2.600000, 0.350000),
    ("hardened", "Hardened %s", 3.900000, 0.300000),
    ("reinforced", "Reinforced %s", 6.500000, 0.250000),
    ("superb", "Superb %s", 2.500000, 0.250000),
    ("lordly", "Lordly %s", 11.500000, 0.250000),
    ("lame", "Lame %s", 0.400000, 1.000000),
    ("swaybacked", "Swaybacked %s", 0.600000, 1.000000),
    ("stubborn", "Stubborn %s", 0.900000, 1.000000),
    ("timid", "Timid %s", 1.800000, 1.000000),
    ("meek", "Meek %s", 1.800000, 1.000000),
    ("spirited", "Spirited %s", 6.500000, 0.600000),
    ("champion", "Champion %s", 14.500000, 0.200000),
    ("fresh", "Fresh %s", 1.000000, 1.000000),
    ("day_old", "Day-old %s", 1.000000, 1.000000),
    ("two_day_old", "Two Days-old %s", 0.900000, 1.000000),
    ("smelling", "Smelling %s", 0.400000, 1.000000),
    ("rotten", "Rotten %s", 0.050000, 1.000000),
    ("large_bag", "Large Bag of %s", 1.900000, 0.300000),

]