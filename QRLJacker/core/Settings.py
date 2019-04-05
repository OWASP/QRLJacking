#!/usr/bin/python3.7
# Here I put all the constant things between the scripts so I don't forget them
# Also give myself another reason to start refactoring the whole code in OOP :D

from core.color import *
global debug,development,verbose
global path,history,running_module,name,headless_browser,visible_browser
global previous
path             = None            # The core directory we started in
debug            = False           # Framework mode
development      = False           # Framework mode
verbose          = False           # Framework mode
running_module   = False           # The current running module and used to decide which cli to use
headless_browser = False           # The current instance of my headless browser class
visible_browser  = False           # The current instance of my visible browser class
previous   = []                    # All modules used before, using this in previous command
history    = []                    # Used in commands history ofc!

# I know I could use simply use `list.append(element)` but this way looks cooler :"D
update_history  = lambda h:history.append(h)
update_previous = lambda:previous.append(running_module)

name = W+underline+"QrlJacker"+end
def add_module(p): global name;name = W+underline+"QrlJacker"+end+ W+" Module("+R+p+W+")"+end # Fuck lambda
def reset_name() : global name;name = W+underline+"QrlJacker"+end
