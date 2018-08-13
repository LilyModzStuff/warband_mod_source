reserved_variables = []
# modmerger_start version=201 type=4
try:
    component_name = "variables"
    var_set = { "reserved_variables":reserved_variables, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
