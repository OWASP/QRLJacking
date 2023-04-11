#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#Written by: Karim shoair - D4Vinci ( QrlJacker-Framework )
from sys import version_info as py_ver
import argparse,os
if ( py_ver.major==3 and py_ver.minor<7 ):
    # The second condition is for the future releases of python
    error("The framework is designed to work only on python 3.7 or above!")
    error("You are using version "+".".join( map( str,[py_ver.major, py_ver.minor, py_ver.micro] )) )
    exit(0)

elif os.name=="nt":
    error("The framework is designed to work on Linux or MacOS only! Sorry for that :)")
    exit(0)

from core import Cli,utils,Settings,db
from core.color import *

parser = argparse.ArgumentParser(prog='QrlJacker.py')
parser.add_argument("-r", metavar='', help="Execute a resource file (history file).")
parser.add_argument("-x", metavar='', help="Execute a specific command (use ; for multiples).")
parser.add_argument("--debug",action="store_true", help="Enables debug mode (Identifying problems easier).")
parser.add_argument("--dev",action="store_true", help="Enables development mode (Reloading modules every use).")
parser.add_argument("--verbose",action="store_true", help="Enables verbose mode (Display more details).")
parser.add_argument("-q",action="store_true", help="Quit mode (no banner).")
args    = parser.parse_args()

def main():
    Settings.path = os.getcwd()
    if args.debug:
        Settings.debug = True
    if args.dev:
        Settings.development = True
    if args.verbose:
        Settings.verbose = True
    if not args.q:
        utils.banner(db.index_modules())

    if args.x:
        for c in args.x.split(";"):
            Cli.start(c)
        Cli.start()
    elif args.r:
        try:
            with open(args.r,"r") as f:
                cmds = f.readlines()
                for cmd in cmds:
                    Cli.start(cmd.strip())
            Cli.start()
        except:
            error("Can't open the specifed resource file!")
            exit(0)
    else:
        Cli.start()
    #You think it's simple when you look here huh :"D
    sys.exit()

if __name__ == '__main__':
    main()
