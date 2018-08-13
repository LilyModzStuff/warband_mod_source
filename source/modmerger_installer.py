from modmerger_header import *





def get_unused_backup_filename(basic_filename):
    import os.path
    counter = 1  
    backup_filename = "%s.%d.bak" %(basic_filename,counter)
    
    while(os.path.isfile(backup_filename)):
        counter += 1  
        backup_filename = "%s.%d.bak" %(basic_filename,counter)
    
    return backup_filename
    
def backup_file(basic_filename):
    from shutil import copyfile
    backup_filename = get_unused_backup_filename(basic_filename)   
    
    copyfile(basic_filename, backup_filename)
        
    
def line_is_modmerger_start(line):
    import re
    m = re.match('^\s*#\s*modmerger_start.*', line)
    if( m ):
        return True
    return False
    
    
def line_is_modmerger_end(line):
    import re
    m = re.match('^\s*#\s*modmerger_end.*', line)
    if( m ):
        return True
    return False
    

def line_parse_nvp(dstdict, line):
    import re
    pattern = '\s*(\w*)=\s*(\w*)(.*)'
    matcher = re.compile(pattern)
    
    m=matcher.match(line)
    while m:
        dstdict[m.group(1)] = m.group(2)
        line = m.group(3)
        m=matcher.match(line)
        
def line_parse_modmerger_data(line):
    import re
    
    data={}
    m = re.match('^\s*#\s*modmerger_start\s+(.*)', line)
    if( m ):
        values = m.group(1)
        #print "values=",values
        line_parse_nvp(data, values)
        return data
    return None

def modmerger_data_to_string(data):
    line=""
    for k in data.keys():
        line += " %s=%s"%(k,str(data[k]))
	
    return line


def generate_branding100(component_name):
    lines=[]
    component_type = get_component_type(component_name)
    metadata = {
        "version" : modmerger_version,
        "type" : component_type,
    }    
    
    lines.append("# modmerger_start%s"% modmerger_data_to_string(metadata))
    
    if component_type > 0:
        if  component_type & 1:
            lines.append("try:")
            lines.append("    from util_common import logger")
            lines.append("    from modmerger_options import mods_active")
            lines.append("    modcomp_name = \"constants\"")
            lines.append("    for mod_name in mods_active:")
            lines.append("        try:")
            lines.append("            logger.info(\"Importing constants from mod \\\"%s\\\"...\"%(mod_name))")
            lines.append("            code = \"from %s_constants import *\" % mod_name")
            lines.append("            exec code")
            lines.append("        except ImportError:")
            lines.append("            errstring = \"Component \\\"%s\\\" not found for mod \\\"%s\\\".\" % (modcomp_name, mod_name)")
            lines.append("            logger.debug(errstring)")
            lines.append("except:")
            lines.append("    raise")
        if  component_type & 2:
            lines.append("try:")
            lines.append("    import inspect, os.path, re,sys")
            lines.append("    module_name = os.path.basename(inspect.stack()[0][1])")
            lines.append("    result = re.match(\"^(module_([^.]*)).py\", module_name)")
            lines.append("    if( result ):    ")
            lines.append("        from modmerger import modmerge")
            lines.append("        modmerge(eval(result.group(2)))")
            lines.append("except:")
            lines.append("    raise")
    else:
        return None
    # if

    lines.append("# modmerger_end")
    return lines

def generate_branding200(component_name):
    lines=[]
    component_type = get_component_type(component_name)
    metadata = {
        "version" : modmerger_version,
        "type" : component_type,
    }    
    
    lines.append("# modmerger_start%s"% modmerger_data_to_string(metadata))
    
    if component_type > 0:
        if  component_type & 1:
            lines.append("try:")
            lines.append("    from util_common import logger")
            lines.append("    from modmerger_options import mods_active")
            lines.append("    modcomp_name = \"constants\"")
            lines.append("    for mod_name in mods_active:")
            lines.append("        try:")
            lines.append("            logger.info(\"Importing constants from mod \\\"%s\\\"...\"%(mod_name))")
            lines.append("            code = \"from %s_constants import *\" % mod_name")
            lines.append("            exec code")
            lines.append("        except ImportError:")
            lines.append("            errstring = \"Component \\\"%s\\\" not found for mod \\\"%s\\\".\" % (modcomp_name, mod_name)")
            lines.append("            logger.debug(errstring)")
            lines.append("except:")
            lines.append("    raise")
        if  component_type & 2:
            lines.append("try:")
            lines.append("    import inspect, os.path, re,sys")
            lines.append("    module_name = os.path.basename(inspect.stack()[0][1])")
            lines.append("    result = re.match(\"^(module_([^.]*)).py\", module_name)")
            lines.append("    if( result ):    ")
            lines.append("        from modmerger import modmerge")
            lines.append("        var_set = { result.group(2) : eval(result.group(2)) }")
            lines.append("        modmerge(var_set)")
            lines.append("except:")
            lines.append("    raise")
    else:
        return None
    # if

    lines.append("# modmerger_end")
    return lines


def generate_branding201(component_name):
    lines=[]
    component_type = get_component_type(component_name)
    metadata = {
        "version" : modmerger_version,
        "type" : component_type,
    }    
    
    lines.append("# modmerger_start%s"% modmerger_data_to_string(metadata))
    
    if component_type > 0:
        if  component_type & 1:
            lines.append("try:")
            lines.append("    from util_common import logger")
            lines.append("    from modmerger_options import mods_active")
            lines.append("    modcomp_name = \"constants\"")
            lines.append("    for mod_name in mods_active:")
            lines.append("        try:")
            lines.append("            logger.info(\"Importing constants from mod \\\"%s\\\"...\"%(mod_name))")
            lines.append("            code = \"from %s_constants import *\" % mod_name")
            lines.append("            exec code")
            lines.append("        except ImportError:")
            lines.append("            errstring = \"Component \\\"%s\\\" not found for mod \\\"%s\\\".\" % (modcomp_name, mod_name)")
            lines.append("            logger.debug(errstring)")
            lines.append("except:")
            lines.append("    raise")
        if  component_type & 2: # for cases where the variable passed in is the same name as the component
            lines.append("try:")
            lines.append("    component_name = \"%s\"" % component_name)                        
            lines.append("    var_set = { \"%s\" : %s }" %(component_name,component_name))
            lines.append("    from modmerger import modmerge")
            lines.append("    modmerge(var_set)")
            lines.append("except:")
            lines.append("    raise")
        if  component_type & 4: # for cases where the variables to pass in is provided        
            varstr=""
            for var_i in mod_components3[component_name]:
                varstr+="\"%s\":%s," % (var_i,var_i)
            if varstr <> "":	 
                lines.append("try:")
                lines.append("    component_name = \"%s\"" % component_name)
                lines.append("    var_set = { %s }" % varstr)
                lines.append("    from modmerger import modmerge")
                lines.append("    modmerge(var_set, component_name)")
                lines.append("except:")
                lines.append("    raise")
    else:
        return None
    # if

    lines.append("# modmerger_end")
    return lines


def generate_branding(component_name, version=None):
    if version == None: version = modmerger_version
    
    if version == 200:
        return generate_branding200(component_name)
    elif version == 100:
        return generate_branding100(component_name)
    else:
        return generate_branding201(component_name)

 
        
    return None



# return True is successful, False if there is no need to brand        
def brand_component_source_file(component_name):
    source_filename = "module_%s.py" % component_name
    f = open(source_filename)
    lines = f.readlines()
    f.close()

    # first pass: tries to find previous modmerger file

    need_to_brand = True # assume we need to brand the file
    
    in_modmerger_chunk=False
    for line in lines:
        if line_is_modmerger_start(line):
            in_modmerger_chunk = True
            
            data = line_parse_modmerger_data(line)
            if data:
                try:
                    file_modmerger_version = data["version"]                    
                    if int(file_modmerger_version) >= int(modmerger_version):
                        need_to_brand = False # file modmerger version is up to date
                except KeyError:
                    # no version, will rebrand
                    pass	            
        #if  in_modmerger_chunk :
            #print line.rstrip()
        if line_is_modmerger_end(line):
            in_modmerger_chunk = False
            
    
    if not need_to_brand:
        return False
    else:
        branding = generate_branding(component_name)
        if branding is None:
            return False
	
        # now will backup and replace the file, avoiding older modmerger chunk and writing a new brand at the end
        backup_file(source_filename)
        
        f = open(source_filename, "w")
        
        in_modmerger_chunk=False
        for line in lines:
            if line_is_modmerger_start(line):
                in_modmerger_chunk = True
            if  in_modmerger_chunk :
                #print line.rstrip()
                continue
            else: # write to new file
                f.write(line)            
            if line_is_modmerger_end(line):
                in_modmerger_chunk = False        
        
        # write in new chunk
        
        for l in branding:
            f.write("%s\n"%l.rstrip())
        f.close()
    return True
 
# return True is successful, False if there is no need to brand        
def unbrand_component_source_file(component_name):
    source_filename = "module_%s.py" % component_name
    f = open(source_filename)
    lines = f.readlines()
    f.close()

    # first pass: tries to find previous modmerger file

    need_to_unbrand = False # assume we don't need to unbrand
    
    in_modmerger_chunk=False
    for line in lines:
        if line_is_modmerger_start(line):
            in_modmerger_chunk = True
        if line_is_modmerger_end(line):
            in_modmerger_chunk = False
            need_to_unbrand = True  # will only unbrand if there is a properly closed branding
            break
                
    if not need_to_unbrand:
        return False
    else:	
        # now will backup and replace the file, avoiding older modmerger chunk and writing a new brand at the end
        backup_file(source_filename)
        
        f = open(source_filename, "w")
        
        in_modmerger_chunk=False
        for line in lines:
            if line_is_modmerger_start(line):
                in_modmerger_chunk = True
            if  in_modmerger_chunk :
                #print line.rstrip()
                continue
            else: # write to new file
                f.write(line)            
            if line_is_modmerger_end(line):
                in_modmerger_chunk = False                
        f.close()
    return True
 
 
# brand all module files with modmerger code snippets
def install_modmerger():
    from util_common import logger
    for comp_name in mod_components:    
        if( brand_component_source_file(comp_name) ):
            print "Successfully branded: module_%s.py" % comp_name
        else:
            print "Branding not required: module_%s.py" % comp_name
        
	
# remove brands from all module files
def uninstall_modmerger():
    from util_common import logger
    for comp_name in mod_components:    
        if( unbrand_component_source_file(comp_name) ):
            print "Branding successfully removed from: module_%s.py" % comp_name
        else:
            print "No proper branding detected: module_%s.py" % comp_name
     
    
def remove_backup_files():    
    import os
    dirList=os.listdir(".")
    
    for f in dirList:
        if f[-4:] == ".bak":
            print "Deleting: %s" % f
            os.remove(f)
	
 
    



def confirm(prompt):
    legal_replies = set(["y","n"])
    reply = ""
    while not reply in legal_replies:
        reply = raw_input("%s (y/n) >" % prompt).lower()
        
    return reply

def print_main_menu():
    print "------------------------------------------------------------"
    print "Mount and Blade"
    print "ModMerger framework version %.2f:" %(modmerger_version/100.0)
    print "by sphere"
    print "for Mount and Blade Module System"
    print "------------------------------------------------------------"
    print "1) Installs ModMerger in the current directory"
    print "2) Uninstalls ModMerger from the current directory"
    print "3) Delete all backup files (*.bak) in the current directory"
    print "4) Meditate..."    
    print "5) About this installer"
    print "0) Exit"     

def main_menu():
    import os
    # installer menu    
    legal_replies = set(["0","1","2","3","4","5","9"])
    reply=""    
    print_main_menu()
    while reply <> "0":
        reply=""    
        while not reply in legal_replies:
            reply = raw_input("Make a choice (9 to display menu again) >").lower()
        #if reply == "9": print_main_menu()
        if reply =="1" and confirm("Are you sure you want to install ModMerger framework?") == "y":
            install_modmerger()
        elif reply =="2" and confirm("Are you sure you want to uninstall ModMerger framework?") == "y":
            uninstall_modmerger()
        elif reply == "3" and confirm("Are you sure you want to delete all files with extension .bak in this directory?") == "y":
            remove_backup_files()          
        elif reply == "4":
            print
            import this
            print
        elif reply == "5":
            print "\nsphere: I haven't made this kind of 'menu' since the days when I thought basica was a powerful language...\n"
        elif reply == "9":
            print_main_menu()
           
	
        
    


 
if __name__ == '__main__':
    main_menu()
 
    
    
    
