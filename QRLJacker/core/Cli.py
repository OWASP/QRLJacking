#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Written by: Karim shoair - D4Vinci ( QrlJacker-Framework )
import os,sys,time,random,traceback,json,argparse,readline
from core import utils,db,module,Settings,browser
from core.color import *

global modules,all_keywords
modules = db.index_modules()
all_keywords = [
			"help","?","os","banner","exit","quit",
			"list","show","use","info","previous","search","sessions","jobs",
			"database","debug","dev","verbose","reload","refresh",
			"history","makerc","resource"
			]
help_msg = end+G+"""
General commands
=================
	Command               Description
	---------             -------------
	help/?                Show this help menu.
	os      <command>     Execute a system command without closing the framework
	banner                Display banner.
	exit/quit             Exit the framework.

Core commands
=============
	Command               Description
	---------             -------------
	database              Prints the core version, check if framework is up-to-date and update if you are not up-to-date.
	debug                 Drop into debug mode or disable it. (Making identifying problems easier)
	dev                   Drop into development mode or disable it. (Reload modules every use)
	verbose               Drop into verbose mode or disable it. (Make framework displays more details)
	reload/refresh        Reload the modules database.

Resources commands
==================
	Command               Description
	---------             -------------
	history               Display commandline most important history from the beginning.
	makerc                Save the most important commands entered since start to a file.
	resource  <file>      Run the commands stored in a file.

Sessions management commands
============================
	Command               Description
	---------             -------------
	sessions (-h)         Dump session listings and display information about sessions.
	jobs     (-h)         Displays and manages jobs."""+end

module_help = G+"""

Module commands
===============
	Command               Description
	---------             -------------
	list/show             List modules you can use.
	use      <module>     Use an available module.
	info     <module>     Get information about an available module.
	previous              Runs the previously loaded module.
	search   <text>       Search for a module by a specific text in its name or in its description.
"""+end

# To use with session command
sessions_parser = argparse.ArgumentParser(prog="sessions",add_help=False)
sessions_parser.add_argument('-h', action="store_true", help="Show this help message.") # I done that because print the normal help exits the framework
sessions_parser.add_argument('-l', action="store_true", help='List all captured sessions.')
sessions_parser.add_argument('-K', action="store_true", help='Remove all captured sessions.')
sessions_parser.add_argument('-s', metavar='', help='Search for sessions with a specifed type.')
sessions_parser.add_argument('-k', metavar='', help='Remove a specifed captured session by ID')
sessions_parser.add_argument('-i', metavar='', help='Interact with a captured session by ID.')
# Yeah, you must have noticed that I'm trying to make sessions arguments are the same as metasploit to not make you feel weird :D

def general_commands(command, args=None, full_help=module_help):

	if command=="banner":
		utils.banner(modules)
		return True

	elif command=="history":
		n = -1
		for i in range( len(Settings.history) ):
			print( Settings.history[n] )
			n -= 1
		return True

	elif command=="makerc":
		file_name = "history.txt"
		if args and len(args.split(" "))>0:
			file_name = args.split(" ")[0]
		f = open(file_name,"w")
		for line in Settings.history:
			f.write(line+"\n")
		f.close()
		status( "Command history saved to "+file_name )
		return True

	elif command in ["help","?"]:
		print(help_msg+full_help)
		return True

	elif command in ["exit","quit"]:
		if Settings.headless_browser:
			Settings.headless_browser.close_all()
			Settings.headless_browser = None
		exit(0)

	else:
		return False

chars_filter = { ";":"{{Semi-Colon}}" } # Here we add all the chars that may do some problems while processing
def start(rc=False):
	myinput  = utils.getinput()
	utils.Input_completer(all_keywords+modules )
	while True:
		if sys.stdin.closed or sys.stdout.closed:
			exit(0)
		try:
			name = Settings.name
			if rc:
				cmd = rc
				print("\n"+name+G+" > "+end+cmd)
			else:
				cmd = myinput("\n"+name+G+" > "+end)

			cmd = cmd.strip()
			special_char = False
			for q in ["'",'"']:
				if cmd.count(q) >=2:
					special_char = q

			if special_char:
				# Welcome to the new age of the quick shitty special characters filters..
				quoted = cmd.split(special_char)[1]     # Get the first thing between quotes
				for char in chars_filter:
					quoted = quoted.replace(char,chars_filter[char])
				cmd = cmd.replace(  cmd.split(special_char)[1].join([special_char]*2), quoted )
				# Not the filter this framework deserves but, the filter it needed..lol

			for c in cmd.split(";"):
				for char in chars_filter:
					c = c.replace(chars_filter[char],char) # Yeah reversing
				if len( cmd.split(";") ) > 1:
					print(G+" > "+end+ c)
				if Settings.running_module:
					module.handle(c)
					continue

				head = c.lower().split()[0]
				args = " ".join(c.split()[1:])

				if not general_commands(head, args=args):
					command_handler(c)
		except KeyboardInterrupt:
			print()
			error("KeyboardInterrupt use exit command!")
			continue
		except Exception as e:
			if Settings.debug:
				print("\nInput function error:")
				print("  Exception -> "+str(e))
				print("    Input -> "+str(cmd))
				print("  Trackback -> ")
				traceback.print_exc()
				break
		finally:
			if rc:
				time.sleep(0.3)
				break

#A function for every command (helpful in the future)
def command_handler(c):
	#parsing a command and pass to its function
	if c=="" or c[0]=="#":return
	command = c.lower().split()[0]
	args    = " ".join(c.split()[1:])
	try:
		handler = globals()["command_{}".format(command)]
		handler(args)
		Settings.update_history(c)  # Log the important commands and the ones that doesn't gave error :D
	except Exception as e:
		if command not in all_keywords:
			error( command + " is not recognized as an internal command !")
			#To check for the wanted command on typos
			wanted = utils.grab_wanted(command,all_keywords)
			if len(wanted)>0:
				status( "Maybe you meant : " + wanted )
		else:
			error( "Error in executing command "+ command )
		status( "Type help or ? to learn more..")

		if Settings.debug:
			print("Exception -> "+str(e))
			print("    Input -> "+str(c))
			print("  Modules -> "+"  ".join(modules))
			print("Trackback -> ")
			traceback.print_exc()

def command_list(text=False):
	cols = [G+Bold+"Name"+end,G+Bold+"Description"+end]
	Columns = []
	for p in modules:
		info = db.grab(p)
		Columns.append([p ,info.short_description])
	utils.create_table(cols,Columns)

def command_show(text=False):
	command_list(text)

def command_search(text=False):
	if not text:
		error("You must enter a text to search for !")
	else:
		cols = [G+Bold+"Name"+end,G+Bold+"Description"+end]
		Columns = []
		text = text.lower()
		for p in modules:
			info = db.grab(p)
			full_text = " ".join([info.author, info.short_description, info.full_description if info.full_description else ""]).lower()
			if text in full_text:
				Columns.append([p ,info.short_description])
		if not Columns:
			error("Didn't find a module have the entered text!")
		else:
			utils.create_table(cols,Columns)

def command_os(text=False):
	if text:
		os.system(text)
	else:
		error("You must enter a command to execute !")
		return

def command_use(p=False):
	p = p.lower()
	if not p:
		error("You must enter a module to use !")
		return
	else:
		if p in modules:
			if Settings.running_module:
				Settings.update_previous()
			Settings.running_module = p
			module.Exec(all_keywords)
			return
		else:
			if Settings.debug:
				print("Module -> "+p)
				print("Loaded modules ->"+"\t".join(modules))
			error(p+" module not found!")

def command_sessions(text=""):
	sessions_file = os.path.join("core","sessions.json")
	sessions = json.load(open( sessions_file ))
	try:
		cmd = sessions_parser.parse_args(text.split())
	except:
		cmd = sessions_parser.parse_args("") # Fuck you argparse, next time I will use more flexible module like getopt globally
		# I done this because any error argparse gives is printed and it exit the framework but now no

	if cmd.h:
		print(sessions_parser.format_help())
		return

	elif not text or cmd.l:
		if not sessions:
			error("No captured sessions.")
		else:
			cols = [G+Bold+"ID"+end, G+Bold+"Module name"+end,G+Bold+"Captured on"+end]
			Columns = []
			for session_id in list(sessions.keys()):
				line = sessions[session_id]
				date = line["session_path"].replace( os.path.join("sessions",""),"").replace(".session","")
				Columns.append([session_id, line["name"], date])
			utils.create_table(cols,Columns)

	elif cmd.i:
		if not sessions:
			error("No captured sessions.")
		else:
			if not cmd.i:
				error("Enter a session ID to interact with!")
			elif cmd.i not in list(sessions.keys()):
				error("Invalid session ID!")
			else:
				if not Settings.visible_browser:
					Settings.visible_browser = browser.visible_browsers()
				status(f"Starting interaction with ({cmd.i})...")
				if sessions[cmd.i]["session_type"] == "localStorage":
					Settings.visible_browser.load_localstorage(cmd.i)
				elif sessions[cmd.i]["session_type"] == "cookies":
					Settings.visible_browser.load_cookie(cmd.i)
				else:
					Settings.visible_browser.load_profile(cmd.i)

	elif cmd.k:
		if not sessions:
			error("No captured sessions.")
		else:
			if not cmd.k:
				error("Enter a session ID to interact with!")
			elif cmd.k not in list(sessions.keys()):
				error("Invalid session ID!")
			else:
				session_file = sessions[cmd.k]["session_path"]
				os.remove(session_file)
				sessions.pop(cmd.k)
				f = open( sessions_file,"w" )
				json.dump(sessions, f, indent=2)
				f.close()
				status(f"Session ({cmd.k}) removed!")

	elif cmd.s:
		if not sessions:
			error("No captured sessions.")
		else:
			if not cmd.s:
				error("Enter a session type to filter with!")
			elif cmd.s not in [ sessions[i]["name"] for i in list(sessions.keys()) ]:
				error("Invalid session type!")
			else:
				cols = [G+Bold+"ID"+end, G+Bold+"Captured on"+end]
				Columns = []
				for session_id in list(sessions.keys()):
					line = sessions[session_id]
					if cmd.s == line["name"]:
						date = line["session_path"].replace( os.path.join("sessions",""),"").replace(".session","")
						Columns.append([session_id, date])
				utils.create_table(cols,Columns)

	elif cmd.K:
		if not sessions:
			error("No captured sessions.")
		else:
			for sess in list(sessions.keys()):
				session_file = sessions[sess]["session_path"]
				os.remove(session_file)
			f = open( sessions_file,"w" )
			json.dump({}, f, indent=2)
			f.close()
			status(f"All captured sessions removed!")

def command_jobs(process=""):
	help_command = """
usage: jobs [-h] [-l] [-K] [-k]

optional arguments:
  -h   Show this help message.
  -l   List all running jobs.
  -K   Terminate all running jobs.
  -k   Terminate jobs by job ID or module name"""

	if process=="-h":
		print(help_command)
		return

	else:
		if not Settings.headless_browser or Settings.headless_browser.browsers=={}:
			error("No active jobs.")
			return

	option = process.split()[:1]
	args   = process.split()[1:]
	if not process or option[0] =="-l":
		cols = [G+Bold+"ID"+end, G+Bold+"Module name"+end,G+Bold+"Serving on"+end]
		Columns = []
		for module_name in list(Settings.headless_browser.browsers.keys()):
			line = Settings.headless_browser.browsers[module_name]
			if Settings.headless_browser.browsers[module_name]["Status"]:
				uri = line["host"]+":"+line["port"]
				Columns.append([line["Controller"].session_id, module_name, uri])
		if Columns:
			utils.create_table(cols,Columns)
		else:
			error("No active jobs.")

	elif option[0]=="-k":
		if not args:
			error("Enter a job ID/module name to terminate!")
		else:
			for module_name in list(Settings.headless_browser.browsers.keys()):
				if Settings.headless_browser.browsers[module_name]["Controller"].session_id == args[0]:
					Settings.headless_browser.close_job(module_name)
					status("Job terminated successfully!")
					return
			for module_name in list(Settings.headless_browser.browsers.keys()):
				if module_name == args[0]:
					Settings.headless_browser.close_job(module_name)
					status("Job terminated successfully!")
					return
			error("Job not found!")

	elif option[0] == "-K":
		Settings.headless_browser.close_all()
		Settings.headless_browser = None
		status("All jobs terminated successfully!")

	else:
		error("Invalid option!")

def command_previous(p=False):
	if len(Settings.previous)!=0:
		prev = Settings.previous.pop(-1)
		command_use(prev)
	else:
		error("You haven't used a modules yet !")

def command_resource(p=False):
	try:
		with open(p,"r") as f:
			cmds = f.readlines()
			for cmd in cmds:
				start(cmd.strip())
	except:
		if not p:
			error("Enter a resource file to read!")
		else:
			if Settings.debug:
				print("    Input -> "+str(p))
				print("      Dir -> "+str(os.getcwd()))
			error("Can't open the specifed resource file!")
		return

def command_info(p=False):
	if not p:
		error("You must enter a module to get it's information !")
		return
	p   = p.lower()
	if p in modules:
		info = db.grab(p)
		print( "      Module : " + utils.humanize(p) )
		print( " Provided by : " + info.author )
		if info.full_description:
			print( " Description : " + info.full_description )
		else:
			print( " Description : " + info.short_description )
	else:
		error(p+" module not found!")

def command_reload(text=False):
	global modules
	modules = db.index_modules()
	status("Database updated! ( {} module(s) loaded now )".format( len(modules) ) )
	utils.Input_completer(all_keywords+utils.my_map(lambda x: utils.pythonize(x).split(".")[-1],modules) )

def command_refresh(text=False):
	command_reload(text)

def command_database(text=False):
	status("Checking...")
	v = open(os.path.join(Settings.path, "core", "Data", "version.txt")).read().strip()
	status("Core database "+Y+v)
	lol = utils.check_version()
	if lol and lol==v:
		status("You are up-to-date!")
	elif not lol:
		error("Error in connection! Check your internet!")
	else:
		error("The latest core database is "+lol)
		status("Updating...")
		os.chdir("..")
		os.popen("git pull")
		os.chdir("QRLJacker")
		status("Framework updated successfully!")

def command_exec(text=False): # A hidden command to use in debugging :D
	if Settings.debug and text:
		exec(text)

def command_eval(text=False): # Aaaaaand another hidden one :D
	if Settings.debug and text:
		eval(text)

def command_report(text=False):
	if Settings.debug:
		if Settings.headless_browser:
			for key in Settings.headless_browser.browsers:
				print("Key: "+key)
				print("Data: ")
				print(Settings.headless_browser.browsers[key]["Controller"].capabilities)
				break

# if its value is False the result will be mode=(False==False) so the mode will be True and so on, yup it's magic :D
def command_debug(text=False):
	Settings.debug = (Settings.debug==False)
	status("Debug mode " + {True:"enabled!",False:"disabled!"}[Settings.debug] )

def command_dev(text=False):
	Settings.development = (Settings.development==False)
	status("Development mode " + {True:"enabled!",False:"disabled!"}[Settings.development] )

def command_verbose(text=False):
	Settings.verbose = (Settings.verbose==False)
	status("Verbose mode " + {True:"enabled!",False:"disabled!"}[Settings.verbose] )
