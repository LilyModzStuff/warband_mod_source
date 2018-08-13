from module_info import *
from process_operations import *
import os

print "Initializing..."

try:
  os.remove(export_dir + 'tag_uses.txt')
except:
  a = []
try:
  os.remove(export_dir + 'quick_strings.txt')
except:
  a = []
try:
  os.remove(export_dir + 'variables.txt')
except:
  a = []
try:
  os.remove(export_dir + 'variable_uses.txt')
except:
  a = []

variables = []
variable_uses = []
try:
  file = open("variables.txt","r")
  var_list = file.readlines()
  file.close()
  for v in var_list:
    vv = string.strip(v)
    if vv:
      variables.append(vv)
      variable_uses.append(int(1))
  save_variables(export_dir, variables, variable_uses)
except:
  print "variables.txt not found. Creating new variables.txt file"
