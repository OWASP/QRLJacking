#!/usr/bin/python3.7
# Written by: Karim shoair - D4Vinci ( QrlJacker-Framework )
import os,importlib
from . import utils

def index_modules():
    # Return list of all modules
    modules = []
    for path,_, files in os.walk( os.path.join("core","modules") ):
        for name in [f for f in files if f.endswith(".py")]:
            modules.append( os.path.join(path, name) )
    modules = [x for x in modules if ("__" not in x and "Data"+os.sep not in x and x.endswith('.py'))]
    modules = utils.my_map( (lambda x:x.replace(".py","").replace("\\","/")),modules)
    modules = utils.my_map(lambda x:x.replace(os.path.join("core","modules",""),""),modules)
    return modules

def grab(module):
    # Return info from module
    module = importlib.import_module(utils.pythonize( "/".join(["core","modules",module])))
    return getattr(module, 'info')
