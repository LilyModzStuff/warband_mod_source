------------------------------------------------------------------------------
ModMerger version 0.2.5 for
Mount and Blade
by sphere
------------------------------------------------------------------------------
This is STILL a sorry excuse for a read me file.
There, I've said it myself, again ;)
I will not take responsibility for any damage directly or indirectly caused, including breaking your current mod.  
This is a prototype, bugs are expected.  You can help by providing feedback.
Patience is a required trait not just in learning to use this thing, but also modding in general.

To "install" modmerger, use the modmerger_installer.py script which will have an "interactive TEXT menu".  Due to the increased complexity of the hooks being inserted, manual installation is no longer recommended.


Just before any more misunderstanding, ModMerger will NOT breakdown your existing mods into parts that can be fitted into newer game versions.  If just ALLOWS you to keep your mod content/scripts which started out separated from the original source away from the source files.  IOW, if you are using a set of original source files which are heavily modded, somebody will have to separate out the mess manually first (e.g. porting manually), and then you can decide whether you want to put the stuff back into updated module system source files or do you want to keep them separate...

I know that this thing could be hard to understand and use for some people.  There are plans or tutorials, but I am hanging on a little to see if I can simplify the process of using this for new mods / rewrap existing mods, just a little more.  The whole idea is to try to let modders do as little manual work as possible.


------------------------------------------------------------------------------
Installation by installer script (automated)
------------------------------------------------------------------------------
Step 1) BACKUP all your source files in your module system directory, then put the files in modmerger archive here
Step 2) Execute "modmerger_installer.py".  If you did not mess up python installation, .py files are automatically associated with python so you just have to double click on "modmerger_installer.py" to execute the installer.
Step 3) From the interactive menu, 
	a) enter "1" to install (needs confirmation), which will backup your existing files to *.bak in case things got messed up.  Installation just adds the small modmerger code block required for module files to work with modmerger
	b) enter "2" to uninstall, which removes all the code blocks previously inserted by installation process.  If you did not mess up the inserted code block, which has signature lines that uninstallation requires, all the inserted code should THEORETICALLY be removed.
   c) enter "3" to delete all the *.bak files in the current directory.  It could get messy after a few rounds of installation and uninstallation.


Step 4) After installation, run build_module.bat to ensure that things are still working (assuming build_module worked before you started the installation).


------------------------------------------------------------------------------
How to add / remove a ModMergerized mod
------------------------------------------------------------------------------
Mods which are wrapped using ModMerger conventions will be using their own set of files, which should be different from the orignal source files and thus will not overwrite anything.
There will be a mod-id, which is a (short) string used as a prefix for all the files belonging to the mod.
The mod files will have the naming convention "{mod-id}_{component}.py", which corresponds to each "module_{component}.py" of the original source files.
For example, if I had a mod with mod-id "mymod", any changes I wish to make to "module_scripts.py" will be stored in "mymod_scripts.py".  Any new items I am adding to "module_items.py" will be in "mymod_items.py" etc.

To "install" a MM-mod,

Step 1) Copy all the mod files into the same module system directory (assuming that ModMerger is already installed.  If not, re-read previous section).

Step 2) Edit "modmerger_options.py" and look for the list definition "mods_active".  Add the mod-id to the list.

Example, inside modmerger_options.py:

mods_active = [
	# some existing entries
]

Insert the mod-id, let's assume it is "mymod" in this case:

mods_active = [
	# some existing entries
	"mymod",
]

Note that the order of mod-ids specified in mods_active will be the default order in which the modded content is merged.  For some stuff like items/troops/strings, ORDER is IMPORTANT, so you should not change this order cos it will probably mess up any save games that you previously had when the order was different.

Step 3) That's all.  go build module!


------------------------------------------------------------------------------
(WIP) Attempt to describe how to create a new mod under ModMerger system
------------------------------------------------------------------------------
Firstly, decide on a mod-id.  Try to choose a short string which nobody else is using, and yet can identify your mod's name/function.
The general rule in using ModMerger system is that when you want to make changes to some source file "module_{component}.py", you should instead create a new file (if none exists) "{mod-id}_{component}.py", put your changes in there, then put down instructions on how to merge it back in.

Tutorial By Example: Adding a new script to module_scripts.py
Let's assume that I am working on a new mod with id "mymod" and I want to add my own script "mymod_do_something" to module_scripts.py.
Instead of editing module_scripts.py, This is what I will do:

Step 1) Firstly, I create a copy of "module_scripts.py" to "mymod_scripts.py".  (This is to copy over the necessary headers and constants) 

Step 2) Then editing "mymod_scripts.py", I'll delete all the existing scripts (those are already in module_scripts.py), and put in a new script.  The script constant should look like the following:

scripts=[
]


Step 3) I create a new script tuple and start doing what I'll normally do in module_scripts.py

scripts=[
	# This is a script function of mymod
	# Arguments:
	# Return:
	("mymod_do_something", [
		# do your scripting, blah blah blah
	]),
]



Step 4) Now at this point, the new scripts is sitting in "mymod_scripts.py" and not "module_scripts.py".  We have to tell modmerger to merge in this when we build the module.  To do this, edit "modmerger_options.py" and look for the list "mods_active".  If the mod-id ("mymod") is not in the list, add it to the list.

From now on, when "module_scripts.py" is being processed by build_module, the modmerger code inserted into module_scripts.py will start to look or the "{mod-id}_scripts.py" for all the mods listed in "mods_active".  It first checks whether there is a "modmerge()" function defined in "{mod-id}_scripts.py", which is supposed to be a function with specialized instructions for merging (e.g. code splicing).  If it is not found (like in our example above), it will try to use a generic approach, which defaults to adding the tuples defined in "scripts" to module_scripts.py 's scripts if the script name is not previously found, or to replace the original script tuple in "module_scripts.py" if any scripts in "mymod_scripts.py" has the same name.  Using this approach, we can add new scripts or replace existing scripts of the same name at build time without needing to touch the original source files.


Beyond Step 4) For more advanced stuff like code splicing (inserting/removing operations into existing scripts' op-block), it is necessary to define a localized modmerge function in your mod's source files, but my head feels too thick to try to explain it clearly now.  I'm using some sort of pseudo instruction I've created myself to handle such splicing, which can be seen in some examples (like xgm_item_powers).  For those adventurous ones, you may want to explore it yourself.  As or the rest, you'll probably have to wait until I'm free and clear-headed enough to write more detail tutorials.  Sorry about that :|




------------------------------------------------------------------------------
Changelog
------------------------------------------------------------------------------
0.2.5: hotfix
+ Fixed more bugs with process_script_directives which was passing the wrong directives to OpBlockWrapper.FindLine, causing remove and replace operations to fail.

0.2.4: hotfix
+ Fixed bug in util_scripts:process_script_directives which was calling OpBlockWrapper.RemoveRange instead of OpBlockWrapper.RemoveAt for removal or replacement directives.  This has previously caused problems with  script directives SD_OP_BLOCK_REMOVE and SD_OP_BLOCK_REPLACE to fail when removing lines in op blocks.

0.2.3:
+ Fixed bug with mission_templates's variable list for vanilla versions.
+ Fixed error with vanilla for missing info_pages and postfx modules.
+ Fixed use of map without assignment in header file.

0.2.2:
+ Added GameMenuWrapper to util_wrappers.
+ Added MissionTemplateWrapper to util_wrappers.
+ Fixed bug with PresentationWrapper.FindTrigger always returning first trigger.

0.2.1
+ First release.

