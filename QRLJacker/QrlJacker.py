#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#Written by: Karim shoair - D4Vinci ( QrlJacker-Framework )
from core import Cli,utils,Settings,db
from core.color import *
import argparse

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
            with open(p,"r") as f:
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
