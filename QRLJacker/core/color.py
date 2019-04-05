#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#Written by: Karim shoair - D4Vinci ( QrlJacker-Framework )
import os,sys
#green - yellow - blue - red - white - magenta - cyan - reset
G, Y, B, R, W, M, C, end, Bold, underline = '\033[32m', '\033[93m', '\033[94m', '\033[31m', '\x1b[37m', '\x1b[35m', '\x1b[36m', '\033[0m', "\033[1m", "\033[4m"

def status(text):
	print( end+C+"[+] "+end+G+text+end )

def error(text):
	print( end+M+"[!] "+end+R+text+end )

def warning(text):
	print( end+B+"[W] "+end+Y+text+end )

def goodbye():
	#print(G+" Thanks for playing with "+B+"QrlJacker-Framework! "+R+"<3"+end)
	#Never say goodbye :V
	exit(0)
