#!/usr/bin/python3.7
#Written by: Karim shoair - D4Vinci ( QrlJacker-Framework )
import sys, os, time, random, importlib, readline, atexit
from .color import *
from terminaltables import AsciiTable as table
from urllib.request import urlopen

def banner(m):
    #Choose a random banner and prints it
    os.system("clear")
    #m = db.index_modules()
    banners = open(os.path.join("core","Data","banners.txt")).read().split("$$$$$AnyShIt$$$$$$")
    banner  = random.choice(banners)
    v = open(os.path.join("core","Data","version.txt")).read().strip()
    grabbers = len([ i for i in m if "grabber" in i])
    post = len([ i for i in m if "post" in i])
    banner_to_print  = Bold+G + banner.format(Name=f"{end+R}QrlJacker-Framework {end+B}By {Bold}@D4Vinci -{M} V{v+end+Bold+G}",
                                      Description=f"{end+C}Attack vector By Mohamed Abdelbasset Elnouby {end+Bold+B}(@SymbianSyMoh){end+Bold+G}",
                                       Loaded=f"{end+B}Loaded {end+R}{grabbers}{end+B} grabber(s), {end+R}{post}{end+B} post module(s).{G+Bold}") + end
    print(banner_to_print)
    return

def getinput():
    # Return the suitable input type according to python version
    ver = sys.version[0]
    if ver=="3":
        return input
    else:
        return raw_input

def reload(module):
    # Reload an imported module and return the imported of course
    return importlib.reload(module)

def create_table(headers,rows):
    # Prints a table with the given parameters
    #print(table([["Header1","Header2"],["Row"]],"name").table)
    Main = []
    Main.append(headers)
    for row in rows:Main.append(row)
    t = table(Main)
    t.inner_column_border = False
    t.outer_border    = False
    t.inner_heading_row_border = False
    t.inner_footing_row_border = False
    print("\n"+t.table)

def pythonize(path):
    # Normal path to python importable path
    return path.lower().replace('/', '.').replace("\\","")

def humanize(path):
    # Python importable path to normal path
    return path.lower().replace('.', '/')

def grab_wanted(cmd,keywords):
    #To check for the wanted command on typos
    wanted = ""
    for i in reversed(range(1,5)): # Danger! Magic,don't touch :"D
        oo = [s for s in keywords if (s[:i]==cmd[:i] and s not in wanted) ]
        if len(oo)>1:
            wanted += ", ".join(oo)
        elif len(oo)==1:
            wanted += ", "+oo[0]
    return wanted

def check_version():
    #check for core version online
    u = "https://raw.githubusercontent.com/OWASP/QRLJacking/master/QRLJacker/core/Data/version.txt"
    try:
        res = urlopen(u).read().decode('utf-8').strip()
        return res
    except:
        return None

def my_map(func,values):
    # Because map behaves differently in python 2 and 3, I decided to write my own fuckin version :3
    result = []
    for value in values:
        result.append( func(value) )
    return result

"""
def slow_print(text):
    for s in text:
        if sys.version_info[0]==2:
            sys.stdout.write(s)
        else:
            print(s, end='')
    time.sleep(0.1)
"""
# TODO: make autocomplete fix typos                                               (Done)
# TODO: make autocomplete with parts like whatsapp replaced with grabber/whatsapp (DONE)
# Say hi to my own autocomplete implementation :)
class MyCompleter(object):
    def __init__(self, options):
        self.options = sorted(options)
        self.module_options = sorted(["host","port","useragent"])
    def complete(self, text, state):
        if state == 0:
            if text:
                text = text.lower()
                line = readline.get_line_buffer() # This one gets the whole line typed
                if line.startswith("use") or line.startswith("info"): # This works if the word isn't use/info command but use/info command is typed before so we only return modules
                    self.matches = [m for m in self.options if "/" in m and m.startswith(text)]
                    if len(self.matches)==0: # This returns modules that have any word of the current written ones
                        self.matches = [m for m in self.options if "/" in m and text in m]

                elif line.startswith("set") and "set" in self.options: # This returns options for set command but only when it's available :D
                    self.matches = [m for m in self.module_options if m.startswith(text)]
                    if len(self.matches)==0: # This returns all options if no thing is written after the set command
                        self.matches = self.module_options
                else:
                    self.matches = [s for s in self.options if s.startswith(text) and not "/" in s]
                    if len(self.matches)==0:
                        possible_matches = [s for s in self.options if not "/" in s]
                        wanted = []
                        for i in reversed(range(1,5)): # Fixing typos to return matches if there's no matches :D
                            wanted.extend( [ s for s in possible_matches if (s[:i]==text[:i] and s not in wanted) ])
                            if len(wanted)>0:
                                self.matches = sorted(wanted)
                                break
                        self.matches = sorted(wanted)
            else:
                line = readline.get_line_buffer()
                if line.startswith("use "): # This works if there's no word typed but use command was typed before
                    self.matches = [m for m in self.options if "/" in m]
                elif line.startswith("set") and "set" in self.options:
                    self.matches = self.module_options
                else:
                    self.matches = [m for m in self.options if not "/" in m ]
        try:
            return self.matches[state]
        except IndexError:
            return None

history_file = os.path.join(".autocomplete_history")
def save_history(history_file=history_file): # So you can use the up key to access the previous session commands
    readline.write_history_file(history_file)

def Input_completer(keywords):
    completer = MyCompleter(keywords)
    readline.set_completer(completer.complete)
    if "libedit" in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind('tab: complete')
        #readline.parse_and_bind('"\\e[A": complete') # Up arrow
    readline.parse_and_bind("set colored-completion-prefix on")
    readline.parse_and_bind("set show-all-if-unmodified on")
    readline.parse_and_bind("set horizontal-scroll-mode on")
    if os.path.exists(history_file):
        readline.read_history_file(history_file)
        readline.set_history_length(20)
    readline.set_completer_delims(' ')
    atexit.register(save_history)
