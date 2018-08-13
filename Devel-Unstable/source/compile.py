WRECK_VERSION = '1.0.0'

import sys
if (sys.version_info[0] != 2) or (sys.version_info[1] < 6):
	exit("\nYou're running Python version {0}.{1}.{2}.\nW.R.E.C.K. requires Python version 2.6.x or 2.7.x to run!\n".format(*sys.version_info[0:3]))
sys.dont_write_bytecode = True

from time import time as gettime
from os import makedirs

from traceback import extract_tb

# Color support
if 'bw' in sys.argv:
	COLORAMA = ('', '', '', '', '', '', '', '')
else:
	try:
		import colorama
		colorama.init()
		COLORAMA = ('\x1b[0m', '\x1b[31m', '\x1b[32m', '\x1b[33m', '\x1b[34m', '\x1b[35m', '\x1b[36m', '\x1b[37m')
	except:
		COLORAMA = ('', '', '', '', '', '', '', '')

from compiler import *



write_id_files = "ID_%s.py" # Where the compiler will write new iteration ID-files.
show_performance_data = False # Set to true to display compiler performance data by default.
export_filename = '%s.txt' # How to name export files (only used for some debugging purposes).

WRECK.time_started = gettime()


print
print '{2}*** Warband Refined & Enhanced Compiler Kit (W.R.E.C.K.) version {version!s} ***{0}'.format(*COLORAMA, version = WRECK_VERSION)
print 'Please report errors, problems and suggestions at {5}http://lav.lomskih.net/wreck/{0}'.format(*COLORAMA)
print

try:

#   +-----------------------------------------------------------------------------------------------
#  /
# +
# |

	print 'Loading module...',

	try:

		# Info module and plugins
		WRECK.current_module = 'info'
		from module_info import *
		WRECK.destination = export_dir.rstrip('/')
		globals().update(WRECK.syntax_extensions)
		globals().update(WRECK.plugin_globals)

		# Optional modules
		WRECK.current_module = 'item_modifiers'
		try:
			from module_item_modifiers import *
		except ImportError:
			#from defaults.module_item_modifiers import *
			item_modifiers = DEFAULT_ITEM_MODIFIERS
			WRECK.generate_item_modifiers = False
		generate_imod_constants_for_backwards_compatibility(item_modifiers)
		WRECK.current_module = 'ui_strings'
		try:
			from module_ui_strings import *
		except ImportError:
			ui_strings = []
			WRECK.generate_ui_strings = False
		WRECK.current_module = 'user_hints'
		try:
			from module_user_hints import *
		except ImportError:
			user_hints = []
			WRECK.generate_user_hints = False

		# Required modules
		WRECK.current_module = 'skills'
		from module_skills import *
		generate_skill_constants_for_backwards_compatibility(skills)
		WRECK.current_module = 'animations'
		from module_animations import *
		WRECK.current_module = 'factions'
		from module_factions import *
		WRECK.current_module = 'game_menus'
		from module_game_menus import *
		WRECK.current_module = 'info_pages'
		from module_info_pages import *
		WRECK.current_module = 'meshes'
		from module_meshes import *
		WRECK.current_module = 'mission_templates'
		from module_mission_templates import *
		WRECK.current_module = 'tracks'
		from module_music import *
		WRECK.current_module = 'particle_systems'
		from module_particle_systems import *
		WRECK.current_module = 'postfx_params'
		from module_postfx import *
		WRECK.current_module = 'quests'
		from module_quests import *
		WRECK.current_module = 'scene_props'
		from module_scene_props import *
		WRECK.current_module = 'scenes'
		from module_scenes import *
		WRECK.current_module = 'scripts'
		from module_scripts import *
		WRECK.current_module = 'simple_triggers'
		from module_simple_triggers import *
		WRECK.current_module = 'sounds'
		from module_sounds import *
		WRECK.current_module = 'strings'
		from module_strings import *
		WRECK.current_module = 'tableaus'
		from module_tableau_materials import *
		WRECK.current_module = 'triggers'
		from module_triggers import *
		WRECK.current_module = 'items'
		from module_items import *
		WRECK.current_module = 'map_icons'
		from module_map_icons import *
		WRECK.current_module = 'skins'
		from module_skins import *
		WRECK.current_module = 'presentations'
		from module_presentations import *
		WRECK.current_module = 'troops'
		from module_troops import *
		WRECK.current_module = 'party_templates'
		from module_party_templates import *
		WRECK.current_module = 'parties'
		from module_parties import *
		WRECK.current_module = 'dialogs'
		from module_dialogs import *
		WRECK.current_module = None

	except Exception, e:
		print '{1}FAILED.\nMODULE `{module!s}` ERROR:\n{error!s}{0}'.format(*COLORAMA, module = WRECK.current_module, error = (e.formatted() if isinstance(e, MSException) else formatted_exception()))
		if isinstance(e, TypeError) and (('object is not callable' in e.message) or ('indices must be integers' in e.message)):
			exc_type, exc_value, exc_traceback = sys.exc_info()
			error_info = extract_tb(exc_traceback)[-1]
			print '{6}  Compiler hint: this error is typically caused by a missing comma.\n  Please check that tuples are followed by commas in `{path!s}` above line {line}:\n\n    {5}{code!s}{0}'.format(*COLORAMA, path = path_split(error_info[0])[1], line = error_info[1], code = error_info[3])
		WRECK.time_loaded = gettime()
		raise MSException()
	print '{2}DONE.{0}'.format(*COLORAMA)
	WRECK.time_loaded = gettime()

# |
# +
#  \
#   +===============================================================================================
#  /
# +
# |

	print 'Loading plugins...',

	try:
		# Check plugin requirements
		prereq_errors = []
		for plugin, required_by in WRECK.requirements.iteritems():
			if plugin not in WRECK.plugins:
				prereq_errors.append('Plugin %s not imported but required by %s.' % (plugin, ', '.join(required_by)))
		if prereq_errors:
			raise MSException('\r\n'.join(prereq_errors))
		# Process data injections
		glob = get_globals()
		for plugin in WRECK.plugins:
			for parser in parsers.iterkeys():
				if hasattr(glob[plugin], parser):
					glob[parser].extend(getattr(glob[plugin], parser))
			injections = getattr(glob[plugin], 'injection', None)
			if injections:
				for inj_name, inj_elements in injections.iteritems():
					WRECK.injections.setdefault(inj_name, []).extend(inj_elements)
					#WRECK.warnings.append('Injection: %d elements for `%s` in `%s`' % (len(inj_elements), inj_name, plugin))
	except Exception, e:
		print '{1}FAILED.\nPLUGIN `{module!s}` ERROR:\n{error!s}{0}'.format(*COLORAMA, module = plugin, error = (e.formatted() if isinstance(e, MSException) else formatted_exception()))
		WRECK.time_plugins = gettime()
		raise MSException()
	print '{2}DONE.{0}'.format(*COLORAMA)
	WRECK.time_plugins = gettime()

# |
# +
#  \
#   +===============================================================================================
#  /
# +
# |

	print 'Checking module syntax...',

	try:
		for entity_name, entity_def in parsers.iteritems():
			WRECK.current_module = entity_name
			get_globals()[entity_name] = check_syntax(get_globals()[entity_name], [entity_def['parser']], entity_def.get('uid', 0))
		WRECK.current_module = None
	except Exception, e:
		print '{1}FAILED.\nMODULE `{module!s}` ERROR:\n{error!s}{0}'.format(*COLORAMA, module = entity_name, error = (e.formatted() if isinstance(e, MSException) else formatted_exception()))
		WRECK.time_syntax = gettime()
		raise MSException()
	print '{2}DONE.{0}'.format(*COLORAMA)
	WRECK.time_syntax = gettime()

	WRECK.anim[7] = animations
	WRECK.fac[7] = factions
	WRECK.ip[7] = info_pages
	WRECK.imod[7] = item_modifiers
	WRECK.itm[7] = items
	WRECK.icon[7] = map_icons
	WRECK.mnu[7] = game_menus
	WRECK.mesh[7] = meshes
	WRECK.mt[7] = mission_templates
	WRECK.track[7] = tracks
	WRECK.psys[7] = particle_systems
	WRECK.p[7] = parties
	WRECK.pt[7] = party_templates
	WRECK.pfx[7] = postfx_params
	WRECK.prsnt[7] = presentations
	WRECK.qst[7] = quests
	WRECK.spr[7] = scene_props
	WRECK.scn[7] = scenes
	WRECK.script[7] = scripts
	WRECK.skl[7] = skills
	WRECK.snd[7] = sounds
	WRECK.s[7] = strings
	WRECK.tableau[7] = tableaus
	WRECK.trp[7] = troops

# |
# +
#  \
#   +===============================================================================================
#  /
# +
# |

	print 'Allocating identifiers...',

	try:
		allocate_global_variables()
		allocate_quick_strings()
		calculate_identifiers(animations, anim)
		calculate_identifiers(factions, fac)
		calculate_identifiers(info_pages, ip)
		calculate_identifiers(item_modifiers, imod, imodbit)
		calculate_identifiers(items, itm)
		calculate_identifiers(map_icons, icon)
		calculate_identifiers(game_menus, mnu)
		calculate_identifiers(meshes, mesh)
		calculate_identifiers(mission_templates, mt)
		calculate_identifiers(tracks, track)
		calculate_identifiers(particle_systems, psys)
		calculate_identifiers(parties, p)
		calculate_identifiers(party_templates, pt)
		calculate_identifiers(postfx_params, pfx)
		calculate_identifiers(presentations, prsnt)
		calculate_identifiers(quests, qst)
		calculate_identifiers(scene_props, spr)
		calculate_identifiers(scenes, scn)
		calculate_identifiers(scripts, script)
		calculate_identifiers(skills, skl)
		calculate_identifiers(sounds, snd)
		calculate_identifiers(strings, s)
		calculate_identifiers(tableaus, tableau)
		calculate_identifiers(troops, trp)
		undefined = undefined_identifiers()
		if undefined: raise MSException('undeclared identifiers found in module source:\n * %s' % ('\n * '.join(['%s (referenced by \'%s\')' % (name, '\', \''.join(refs)) for name, refs in undefined])))
	except Exception, e:
		print '{1}FAILED.'.format(*COLORAMA)
		if isinstance(e, MSException):
			print 'MODULE ERROR:\n{error!s}{0}'.format(*COLORAMA, error = e.formatted())
		else:
			print 'COMPILER INTERNAL ERROR:\n{error!s}{0}'.format(*COLORAMA, error = formatted_exception())
		WRECK.time_identifiers = gettime()
		raise MSException()
	print '{2}DONE.{0}'.format(*COLORAMA)
	WRECK.time_identifiers = gettime()

# |
# +
#  \
#   +===============================================================================================
#  /
# +
# |

	print 'Compiling module...',

	try:
		stage = 0
		# Pre-processing (note that all entity-level injections are already done but script-level injections are not).
		glob = get_globals()
		preprocess_entities_internal(glob)
		stage = 1
		for plugin in WRECK.plugins:
			processor = getattr(glob[plugin], 'preprocess_entities', None)
			if processor:
				try: processor(glob)
				except Exception, e: raise MSException('Error in %r pre-processor script.' % plugin, formatted_exception())
		# Compiling...
		stage = 2
		for entity_name, entity_def in parsers.iteritems():
			stage = 3
			entities = get_globals()[entity_name]
			stage = 4
			for index in xrange(len(entities)):
				entities[index] = entity_def['processor'](entities[index], index)
			stage = 5
			setattr(WRECK, entity_name, entity_def['aggregator'](entities))
		# Post-processing (plugins are NOT allowed to do anything here as we are dealing with already compiled code)
		stage = 6
		postprocess_entities()
	except Exception, e:
		print '{1}FAILED.'.format(*COLORAMA)
		if isinstance(e, MSException):
			if stage == 0:
				print 'COMPILER PREPROCESSOR ERROR:\n{error!s}{0}'.format(*COLORAMA, error = e.formatted())
			if stage == 1:
				print 'PLUGIN {module!s} PREPROCESSOR ERROR:\n{error!s}{0}'.format(*COLORAMA, module = plugin, error = e.formatted())
			elif stage == 3:
				print 'MODULE {module!s} ENTITY #{index} COMPILATION ERROR:\n{error!s}{0}'.format(*COLORAMA, module = entity_name, index = index, error = e.formatted())
			elif stage == 4:
				print 'MODULE {module!s} AGGREGATOR ERROR:\n{error!s}{0}'.format(*COLORAMA, module = entity_name, error = e.formatted())
			elif stage == 5:
				print 'COMPILER POSTPROCESSOR ERROR:\n{error!s}{0}'.format(*COLORAMA, error = e.formatted())
		else:
			print 'COMPILER INTERNAL ERROR:\n{error!s}{0}'.format(*COLORAMA, error = formatted_exception())
		WRECK.time_compile = gettime()
		raise MSException()
	print '{2}DONE.{0}'.format(*COLORAMA)
	WRECK.time_compile = gettime()

# |
# +
#  \
#   +===============================================================================================
#  /
# +
# |

	print 'Exporting module...',

	export = {
		'animations': export_filename % 'actions',
		'dialogs': export_filename % 'conversation',
		'dialog_states': export_filename % 'dialog_states',
		'factions': export_filename % 'factions',
		'game_menus': export_filename % 'menus',
		'info_pages': export_filename % 'info_pages',
		'items': export_filename % 'item_kinds1',
		'map_icons': export_filename % 'map_icons',
		'meshes': export_filename % 'meshes',
		'mission_templates': export_filename % 'mission_templates',
		'tracks': export_filename % 'music',
		'particle_systems': export_filename % 'particle_systems',
		'parties': export_filename % 'parties',
		'party_templates': export_filename % 'party_templates',
		'postfx_params': export_filename % 'postfx',
		'presentations': export_filename % 'presentations',
		'quests': export_filename % 'quests',
		'scene_props': export_filename % 'scene_props',
		'scenes': export_filename % 'scenes',
		'scripts': export_filename % 'scripts',
		'simple_triggers': export_filename % 'simple_triggers',
		'skills': export_filename % 'skills',
		'skins': export_filename % 'skins',
		'sounds': export_filename % 'sounds',
		'strings': export_filename % 'strings',
		'tableaus': export_filename % 'tableau_materials',
		'triggers': export_filename % 'triggers',
		'troops': export_filename % 'troops',
		'variables': export_filename % 'variables',
		'quick_strings': export_filename % 'quick_strings',
	}
	if WRECK.generate_item_modifiers: export['item_modifiers'] = 'Data/item_modifiers.txt'
	if WRECK.generate_ui_strings: export['ui_strings'] = 'Languages/en/ui.csv'
	if WRECK.generate_user_hints: export['user_hints'] = 'Languages/en/hints.csv'

	try:
		for entity_name, filename in export.iteritems():
			contents = getattr(WRECK, entity_name)
			if contents is None:
				#print 'Module %s has no changes, skipping export.' % entity_name
				continue
			#print 'Exporting module %s...' % entity_name
			filename = path_split(filename.replace('\\', '/'))
			folder = ('%s/%s' % (WRECK.destination, filename[0])) if filename[0] else WRECK.destination
			if filename[0] and not(path_exists(folder)): makedirs(folder)
			with open('%s/%s' % (folder, filename[1]), 'w+b') as f: f.write(contents)
	except Exception, e:
		print '{1}FAILED.\nCOMPILER INTERNAL ERROR WHILE WRECKING {module!s}:\n{error!s}{0}'.format(*COLORAMA, module = entity_name, error = formatted_exception())
		WRECK.time_export = gettime()
		raise MSException()

	if write_id_files is not None:
		export = {
			'animations': (WRECK.anim, 'anim_'),
			'factions': (WRECK.fac, 'fac_'),
			'info_pages': (WRECK.ip, 'ip_'),
			'items': (WRECK.itm, 'itm_'),
			'map_icons': (WRECK.icon, 'icon_'),
			'menus': (WRECK.mnu, 'mnu_'),
			'meshes': (WRECK.mesh, 'mesh_'),
			'mission_templates': (WRECK.mt, 'mt_'),
			'music': (WRECK.track, 'track_'),
			'particle_systems': (WRECK.psys, 'psys_'),
			'parties': (WRECK.p, 'p_'),
			'party_templates': (WRECK.pt, 'pt_'),
			'postfx_params': (WRECK.pfx, 'pfx_'),
			'presentations': (WRECK.prsnt, 'prsnt_'),
			'quests': (WRECK.qst, 'qst_'),
			'scene_props': (WRECK.spr, 'spr_'),
			'scenes': (WRECK.scn, 'scn_'),
			'scripts': (WRECK.script, 'script_'),
			'skills': (WRECK.skl, 'skl_'),
			'sounds': (WRECK.snd, 'snd_'),
			'strings': (WRECK.s, 'str_'),
			'tableau_materials': (WRECK.tableau, 'tableau_'),
			'troops': (WRECK.trp, 'trp_'),
		}
		try:
			for entity_name, (entity, prefix) in export.iteritems():
				contents = '\n'.join(['%s%s = %d' % (prefix, ref, index) for ref, index in sorted(map(lambda i:(i[0],int(i[1]&0xFFFFFFFF)), entity[0].iteritems()), lambda x,y:cmp(x[1],y[1]))])
				with open(write_id_files % entity_name, 'w+b') as f:
					f.write(contents)
					f.write('\n')
		except Exception, e:
			print '{1}FAILED.\nCOMPILER INTERNAL ERROR WHILE WRECKING {module!s}:\n{error!s}{0}'.format(*COLORAMA, module = write_id_files % entity_name, error = formatted_exception())
			WRECK.time_export = gettime()
			raise MSException()

	print '{2}DONE.{0}'.format(*COLORAMA)
	WRECK.time_export = gettime()

# |
# +
#  \
#   +-----------------------------------------------------------------------------------------------


except MSException:
	WRECK.successful = False

print
if WRECK.successful:
	print '{2}COMPILATION SUCCESSFUL.{0}\n'.format(*COLORAMA)
else:
	print '{1}COMPILATION FAILED.{0}\n'.format(*COLORAMA)

error_reporting_level = 3
if 'silent' in sys.argv: error_reporting_level = 0
if ('error' in sys.argv) or ('errors' in sys.argv): error_reporting_level = 1
if ('error' in sys.argv) or ('warnings' in sys.argv): error_reporting_level = 2
if ('notice' in sys.argv) or ('notices' in sys.argv): error_reporting_level = 3

if WRECK.errors and (error_reporting_level > 0):
	print 'The following errors were generated during compilation:{1}\n '.format(*COLORAMA),
	print '\n  '.join(WRECK.errors)
	print '{0}'.format(*COLORAMA)
if WRECK.warnings and (error_reporting_level > 1):
	print 'The following warnings were generated during compilation:{3}\n '.format(*COLORAMA),
	print '\n  '.join(WRECK.warnings)
	print '{0}'.format(*COLORAMA)
if WRECK.notices and (error_reporting_level > 2):
	print 'The following notifications were generated during compilation:{6}\n '.format(*COLORAMA),
	print '\n  '.join(WRECK.notices)
	print '{0}'.format(*COLORAMA)
if show_performance_data and WRECK.time_loaded:
	print 'Displaying W.R.E.C.K. performance information.'
	print 'Use {5}show_performance_data = False{0} directive in {5}module_info.py{0} file to disable.'.format(*COLORAMA)
	print
	if WRECK.time_loaded:      print '    %.03f sec spent to load module data.' % (WRECK.time_loaded - WRECK.time_started)
	if WRECK.time_plugins:     print '    %.03f sec spent to load plugins.' % (WRECK.time_plugins - WRECK.time_loaded)
	if WRECK.time_syntax:      print '    %.03f sec spent to check module syntax.' % (WRECK.time_syntax - WRECK.time_plugins)
	if WRECK.time_identifiers: print '    %.03f sec spent to allocate identifiers.' % (WRECK.time_identifiers - WRECK.time_syntax)
	if WRECK.time_compile:     print '    %.03f sec spent to compile module.' % (WRECK.time_compile - WRECK.time_identifiers)
	if WRECK.time_export:      print '    %.03f sec spent to export module.' % (WRECK.time_export - WRECK.time_compile)
	print
	print '    >>> %.03f sec total time spent. <<<' % (gettime() - WRECK.time_started)
	print
if 'wait' in sys.argv: raw_input('Press Enter to finish>')
