## Prebattle Orders & Deployment by Caba'drin
## v0.92
## 20 Jan 2012

strings = [
##PBOD
#-- Dunde's Key Config BEGIN
# KEY CHAR Label
("0x02", "1"), ("0x03", "2"), ("0x04", "3"), ("0x05", "4"), ("0x06", "5"), ("0x07", "6"), ("0x08", "7"), ("0x09", "8"), ("0x0a", "9"), ("0x0b", "0"), 
("0x1e", "A"), ("0x30", "B"), ("0x2e", "C"), ("0x20", "D"), ("0x12", "E"), ("0x21", "F"), ("0x22", "G"), ("0x23", "H"), ("0x17", "I"), ("0x24", "J"),
("0x25", "K"), ("0x26", "L"), ("0x32", "M"), ("0x31", "N"), ("0x18", "O"), ("0x19", "P"), ("0x10", "Q"), ("0x13", "R"), ("0x1f", "S"), ("0x14", "T"), 
("0x16", "U"), ("0x2f", "V"), ("0x11", "W"), ("0x2d", "X"), ("0x15", "Y"), ("0x2c", "Z"), 
("0x52", "Numpad 0"), ("0x4f", "Numpad 1"), ("0x50", "Numpad 2"), ("0x51", "Numpad 3"), ("0x4b", "Numpad 4"), 
("0x4c", "Numpad 5"), ("0x4d", "Numpad 6"), ("0x47", "Numpad 7"), ("0x48", "Numpad 8"), ("0x49", "Numpad 9"), 
("0x45", "Num Lock"), ("0xb5", "Numpad DIV"), ("0x37", "Numpad MUL"), ("0x4a", "Numpad MIN"), ("0x4e", "Numpad PLUS"), ("0x9c", "Numpad ENTER"), ("0x53", "Numpad DEL)"), 
("0xd2", "Insert"), ("0xd3", "Delete"), ("0xc7", "Home"), ("0xcf", "End"), ("0xc9", "Page Up"), ("0xd1", "Page Down"), 
("0xc8", "Up"), ("0xd0", "Down"), ("0xcb", "Left"), ("0xcd", "Right"),
("0x3b", "F1"), ("0x3c", "F2"), ("0x3d", "F3"), ("0x3e", "F4"),  ("0x3f", "F5"),  ("0x40", "F6"), 
("0x41", "F7"), ("0x42", "F8"), ("0x43", "F9"), ("0x44", "F10"), ("0x57", "F11"), ("0x58", "F12"),
("0x39", "Space Bar"), ("0x1c", "Enter"), ("0x0f", "Tab"), ("0x0e", "Backspace"), 
("0x1a", "[ "), ("0x1b", " ] "), ("0x33", " < "), ("0x34", " > "), ("0x35", " ? "), ("0x2b", "\\"), ("0x0d", " = "), ("0x0c", " -- "), 
("0x27", "Semicolon"), ("0x28", "Apostrophe"), ("0x29", "Tilde"), ("0x3a", "Caps Lock"),
("0x2a", "Left Shift"), ("0x36", "Right Shift"), ("0x1d", "Left Ctrl"), ("0x9d", "Right Ctrl"), ("0x38", "Left Alt"), ("0xb8", "Right Alt"),
("0xe0", "Left Click"), ("0xe1", "Right Click"),
("0xe2", "Mouse Button 3"), ("0xe3", "Mouse Button 4"), ("0xe4", "Mouse Button 5"), ("0xe5", "Mouse Button 6"), ("0xe6", "Mouse Button 7"), ("0xe7", "Mouse Button 8"),
("0xee", "Scroll Up"), ("0xef", "Scroll Down"), 

# KEY Function Assignment Label
#-- Parts to modify as your mod need --------------
("key_no1",  "Camera Forward"),
("key_no2",  "Camera Backward"),
("key_no3",  "Camera Turn Right"),
("key_no4",  "Camera Turn Left"),
("key_no5",  "Camera Up"),
("key_no6",  "Camera Down"),
("key_no7",  "Next BOT"),
("key_no8",  "Prev BOT"),
("key_no9",  "Toggle Camera Mode"),
("key_no10", "Select Order 7"),
("key_no11", "Select Order 8"),
("key_no12", "Select Order 9"),
("key_no13", "Select Order 10"),
("key_no14", "Spear Brace"),
("key_no15", "Call Horse"),
#("key_no16", "Deploy Pavise"), #Floris Only
("key_no17", "Shield Bash Attack"),
#--------------------------------------------------
#-- Dunde's Key Config END
##PBOD
]

from util_common import add_objects

# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "strings"
        orig_strings = var_set[var_name_1]
        add_objects(orig_strings, strings)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)