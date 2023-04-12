#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Written by: Karim shoair - D4Vinci ( QrlJacker-Framework )
from core import utils,Settings,Cli,db,browser
from core.color import *
from core.module_utils import *
import importlib,traceback,os
global global_options, module_keywords, cli_keywords
module_help = end+G+"""

Module commands
===============
	Command               Description
	----------            --------------
	list/show             List modules you can use.
	options               Displays options for the current module.
	set                   Sets a context-specific variable to a value.
	run                   Launch the current module.
	use     <module>      Use an available module.
	info    <module>      Get information about an available module.
	search  <text>        Search for a module by a specific text in its name or in its description.
	previous              Sets the previously loaded module as the current module.
	back                  Move back from the current context.
"""+end

global_options = {}
modules = db.index_modules()
module_keywords = ["options","set","run","back","close"]
def Exec(all_keywords):
	global global_options, module_keywords, cli_keywords
	module_keywords += all_keywords
	cli_keywords = all_keywords
	mod            = importlib.import_module(utils.pythonize("core.modules."+Settings.running_module))
	if Settings.development:
		mod            = utils.reload(mod)
	global_options = getattr(mod, 'execution').module_type.options
	if os.name !="nt":
		utils.Input_completer(module_keywords+modules)
	Settings.add_module(Settings.running_module)

def handle(c):
	if c=="" or c[0]=="#":return
	c = c.strip()
	head = c.lower().split(" ")[0]
	args = " ".join(c.split(" ")[1:])
	try:
		# Yeah, we don't have switch case in python...
		if not Cli.general_commands(head, args, module_help):
			if head in ["database","debug","dev","verbose","reload","refresh","list","show","resource","os","use","exec",
							"search","info","previous","sessions","jobs","eval","report"]:
				exec("Cli.command_{}(args)".format(head))
				Settings.update_history(c)
			else:
				handler = globals()["command_{}".format(head)]
				handler(args)
				Settings.update_history(c)
	except Exception as e:
		if Settings.debug:
			print("Exception -> "+str(e))
			print("    Input -> "+str(c))
			print("Trackback -> ")
			traceback.print_exc()
		error( head + " is not recognized as an internal command !")
		#To check for the wanted command on typos
		wanted = utils.grab_wanted(head,module_keywords)
		if len(wanted)>0:
			status( "Maybe you meant : " + wanted )
		status( "Type help or ? to learn more..")

def command_options(text=False):
	try:
		options     = global_options
		headers     = [B+Bold+"Name","Current value","Required","Description"+end]
		names       = list( options.keys() )
		values      = utils.my_map(lambda x:str(options[x][2]),names)
		required    = utils.my_map(lambda x:["No","Yes"][options[x][0]],names)
		description = utils.my_map(lambda x:options[x][1],names)
		cols        = []
		for row in range(len(names)):
			cols.append([ names[row], values[row], required[row], description[row] ])
		utils.create_table(headers,cols)

	except Exception as e:
		if Settings.debug:
			error("Error in finding options! ")
			print("Exception -> "+str(e) )
			print("   Module -> "+str(m) )
			print("Trackback -> ")
			traceback.print_exc()
		else:
			error("Unknown error! enable debug mode to more details")

def is_option(option):
	try:
		blah = global_options[option.lower()][2]
		return [blah]
	except:
		return False

def change_value(option,new_value):
	global_options[option.lower()][2] = new_value

def command_set(opt=False):
	if not opt:
		error("You must type an option first !")
	elif len( opt.split(" ") ) < 2 and not "=" in opt:
		error("You must type a new value to the option !")
	else:
		split_char = " "
		if "=" in opt:split_char = "="
		splitted = opt.split(split_char)
		x = is_option(splitted[0].lower())
		if type(x) is list:
			if type(x[0]) is bool:
				change_value(splitted[0],x[0]==False)
				status( splitted[0] + " => " + str(x[0]==False) )
			else:
				change_value( splitted[0], " ".join(splitted[1:]) )
				status( splitted[0] + " => " + " ".join(splitted[1:]) )
		else:
			error("Invalid option!")

def command_run(text=False):
	# Options format : {"name":[ (0,1,2),description,value]}
	# Required     --> 1 # Means that it must have value
	# Not required --> 0 # Means that it could have value or not
	for key in global_options.keys():
		if global_options[key][0]==1 and not str(global_options[key][2]).strip(): # A required option but has empty value
			error("Error! the following option have not been set ("+ key + ")" )
			return
	module = importlib.import_module(utils.pythonize("core.modules."+Settings.running_module))
	if Settings.development: module = utils.reload(module)
	exec_info  = getattr(module, "execution")
	current_browser = {"Status":"Ok"}
	if not Settings.headless_browser:
		Settings.headless_browser = browser.headless_browsers()
		current_browser = Settings.headless_browser.new_session(exec_info.name, exec_info.url, global_options["useragent"][2])
	else:
		current_browser = Settings.headless_browser.new_session(exec_info.name, exec_info.url, global_options["useragent"][2])

	if current_browser["Status"]=="Duplicate":
		error("Module already running!")
	elif current_browser["Status"]=="NoBrowser":
		error("Couldn't find Firefox file path!")
	elif current_browser["Status"]=="Failed":
		error("Couldn't open Firefox! Check the installation instructions again!")
	elif current_browser["Status"]=="Invalid useragent":
		error("Can't use this useragent! See the possible useragent values in the wiki!")
	else:
		# RUN https://youtu.be/PTZ4L6cNNC4
		#current_browser = current_browser["Controller"]
		if exec_info.module_type == types.grabber:
			if Settings.development:
				status("Grabber module detected!")
			Settings.headless_browser.website_qr(exec_info.name, exec_info.image_xpath) # Keeps QR image always updated and it runs in a thread too
			Settings.headless_browser.create_listener(exec_info.name, exec_info.change_identifier, exec_info.session_type)
			if exec_info.img_reload_button:
				Settings.headless_browser.check_img(exec_info.name, exec_info.img_reload_button) # This line will run in a thread too
			Settings.headless_browser.serve_module(exec_info.name, global_options["host"][2], int(global_options["port"][2]))

		# TODO
		elif exec_info.module_type == types.post:
			if Settings.development:
				status("Post module detected!")

def command_close(text=False): # Another hidden command to use in debugging :D
	if Settings.headless_browser:
		Settings.headless_browser.close_all()
		Settings.headless_browser = None

def command_back(text=False):
	Settings.update_previous()
	Settings.running_module = False
	Settings.reset_name()
	if os.name!="nt":
		utils.Input_completer(cli_keywords+modules )
