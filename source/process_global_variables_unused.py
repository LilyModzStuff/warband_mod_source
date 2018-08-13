from module_info import *
from process_common import *
from process_operations import *
##diplomacy start+
import re

imported_variables = []
try:
  file = open("variables.txt","r")
  var_list = file.readlines()
  file.close()
  for v in var_list:
    vv = string.strip(v)
    if vv:
      imported_variables.append(vv)
except:
	imported_variables = []

suppressed_imported_variables = []
##diplomacy end+

print "Checking global variable usages..."
variable_uses = []
variables = load_variables(export_dir,variable_uses)
i = 0
while (i < len(variables)):
  if (variable_uses[i] == 0):
	##diplomacy start+
	##OLD:
	#print "WARNING: Global variable never used: " + variables[i]
	#
	##NEW:
	#For "reserved" names
	if i > 100 or (re.match(r"^reserved_\d\d\d?$", variables[i]) is None):
		if (i < len(imported_variables)) and (not "dplmc" in variables[i].lower()) and ("_" in variables[i]):
			assert variables[i] == imported_variables[i]
			suppressed_imported_variables.append(variables[i])
		else:
			print "WARNING: Global variable never used: " + variables[i]
	##diplomacy end+
  i = i + 1
##diplomacy start+
if len(suppressed_imported_variables) > 0:
	print "Imported %d global variables for saved-game compatability that are not used." % (len(suppressed_imported_variables),)
##diplomacy end+