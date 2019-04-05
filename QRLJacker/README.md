# QRLJacker - QRLJacking Exploitation Framework
### A customizable framework to demonstrate "QRLJacking Attack Vector" and to show how easy it is to hijack services that rely on QR Code Authentication!

## Screenshot
![alt img](Screenshots/Screenshot1.png)

## Prerequisites before installing:
1. Linux or MacOS. (Not working on windows)
2. Python 3.7+

## Installing instructions:
1. Update Firefox browser to the latest version
2. Install the latest geckodriver from https://github.com/mozilla/geckodriver/releases and extract the file then do :
	* `chmod +x geckodriver`
	* `sudo mv -f geckodriver /usr/local/share/geckodriver`
	* `sudo ln -s /usr/local/share/geckodriver /usr/local/bin/geckodriver`
	* `sudo ln -s /usr/local/share/geckodriver /usr/bin/geckodriver`
3. Clone the repo with `git clone https://github.com/OWASP/QRLJacking` then do `cd QRLJacking/QRLJacker`
4. Install all the requirements with `pip install -r requirements.txt`
5. Now you can run the framework with `python3 QrlJacker.py --help`

## Tested on
- Ubuntu 18.04 Bionic Beaver
- Kali Linux 2018.x and up

## Usage
### Commandline arguments
```
usage: QrlJacker.py [-h] [-r ] [-x ] [--debug] [--dev] [--verbose] [-q]

optional arguments:
  -h, --help  show this help message and exit
  -r          Execute a resource file (history file).
  -x          Execute a specific command (use ; for multiples).
  --debug     Enables debug mode (Identifying problems easier).
  --dev       Enables development mode (Reloading modules every use).
  --verbose   Enables verbose mode (Display more details).
  -q          Quit mode (no banner).
```
### Main menu help
```
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
	database              Prints the core version and then check if it's up-to-date.
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
	jobs     (-h)         Displays and manages jobs.

Module commands
===============
	Command               Description
	---------             -------------
	list/show             List modules you can use.
	use      <module>     Use an available module.
	info     <module>     Get information about an available module.
	previous              Runs the previously loaded module.
	search   <text>       Search for a module by a specific text in its name or in its description.
```
### Module menu help
```
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
	database              Prints the core version and then check if it's up-to-date.
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
	jobs     (-h)         Displays and manages jobs.

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
```

## Taking advantage of the core
### Commands autocomplete
The autocomplete done in this framework is not the usual one you always see :smile:
	1. It's designed to fix typos in typed commands to the most similar command with just one tab click so `saerch` becomes `search` and so on, even if you typed any random word similar to an command in this framework.
	2. For the lazy ones like me, it can predict what module you are trying to use by typing any part of it. For example if you typed `use wh` and clicked tab, it would be replaced with `use grabber/whatsapp` and so on. You are welcome :smile:
	3. If you typed some command wrong and pressed enter, the framework tells you what's the nearest command to what you wrote which could be what you wanted.
	4. Some less impressive things like autocomplete for options of the current module after `set` command, autocomplete for modules after `use` and `info` commands and finally it converts all uppercase to lowercase automatically just-in-case you switched cases by mistake while typing :3
	5. Finally you find the normal things you expect in autocomplete like commands autocompletion and persistent history :smile:

### Searching for modules
- In QrlJacker you can search for a module by its name, something written in its description or even the author name!

### Automation
	- As you must noticed you can use a resource file from command-line arguments or send commands directly
	- Inside the framework you can use `makerc` command like in Metasploit but this time it only saves the important commands which doesn't gave error also.
	- There are `history` and `resource` commands so you don't need to exit the framework.
	- You can execute many commands at the same time by splitting them with semi-colon and more

**Reporting an issue**
	- Before reporting an issue you found, activate the debug mode by using the `debug` command or the debug command-line argument and once the error happens again, the framework will print the error trace-back. Also debug mode activates some hidden commands which will help us in debugging the error with you :smile:
	- And now make sure when you are reporting an issue to provide the basic info like your system, python version and the output from the debug mode.

## Development
If you want to write your own module, read [the development docs from here](docs/README.md)

## ToDo:
1. Write modules for other websites
2. Write post modules for the framework
