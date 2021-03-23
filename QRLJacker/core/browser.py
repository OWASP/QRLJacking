#!/usr/bin/python3.7
from selenium.webdriver import Firefox,FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from user_agent import generate_user_agent
from core.color import *
from core.module_utils import *
from core import Settings
from pathlib2 import Path
import os, pickle, json, time, threading, functools, traceback, subprocess

# In Sessions folder we have a json file contains all data about sessions like ids and cookie file path that saved with pickle
def generate_profile(useragent="(default)"):
    profile = FirefoxProfile()
    if useragent.strip().lower()=="(default)":
        status("Using the default useragent")
        return profile
    elif useragent.strip().lower()=="(random)":
        random_useragent = generate_user_agent(os=('mac', 'linux'))
        profile.set_preference("general.useragent.override", random_useragent) # To make our useragent random
        status("Using random useragent "+random_useragent)
        return profile
    else:
        profile.set_preference("general.useragent.override", useragent)
        status("Using useragent "+useragent)
        return profile

def Run_inside_thread(thread_name):
    def hook(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=func, name=thread_name, args=args, kwargs=kwargs)
            thread.daemon = True
            thread.start()
        return wrapper
    return hook

class headless_browsers:
    # Here we create invisble browsers, fast and in an organized way without repeating browsers for the same module
    def __init__(self):
        self.opts = Options()
        self.opts.add_argument("--headless") # To make firefox invisible of course (Headless)
        self.browsers = {} # Here we save all the browsers we create so we can control and use later
        self.useragent = ""
        self.browser_path = ""
        self.sessions_file = os.path.join("core","sessions.json")
        p = subprocess.Popen(["which","firefox"], stdout= subprocess.PIPE, stderr= subprocess.PIPE)
        out, err = p.communicate()
        if err or not out.decode():
            return {"Status":"NoBrowser"}
        else:
            self.browser_path = out.decode().strip()

    def new_session(self, module_name, url, useragent="(random)", force=False):
        if self.browsers!={} and module_name in list(self.browsers.keys()) and self.browsers[module_name]["Status"] and force:
            return {"Status":"Duplicate"}
        else:
            new_headless = {module_name:{"host":"","port":""}}

        new_headless[module_name]["url"] = url
        if not useragent.strip(): # This if condition is useless because module won't let the useragent to be empty but I will leave it just in case...
            return {"Status":"Invalid useragent"}
        else:
            profile = generate_profile(useragent)
        try:
            new_headless[module_name]["Controller"] = None
            caps = DesiredCapabilities.FIREFOX.copy()
            # Disabling the new Firefox driver called marionette so it won't override geckodriver
            # caps['marionette'] = False
            caps['binary_location'] = self.browser_path
            if Settings.debug:
                new_headless[module_name]["Controller"] = Firefox(profile, executable_path="/usr/local/share/geckodriver", capabilities=caps)#options=self.opts) # Inserting the browser object
            else:
                new_headless[module_name]["Controller"] = Firefox(profile, executable_path="/usr/local/share/geckodriver", capabilities=caps, options=self.opts) # Inserting the browser object
        except Exception as e:
            if Settings.debug:
                print(" Exception: "+str(e))
                print(" Trackback: ")
                traceback.print_exc()
            return {"Status":"Failed"}
        else:
            new_headless[module_name]["Status"] = "Success"
            self.browsers.update(new_headless)
            new_headless[module_name]["Controller"].get(url)
            self.useragent = new_headless[module_name]["Controller"].execute_script("return navigator.userAgent;")
            return new_headless[module_name]

    @Run_inside_thread("Sessions catcher thread")
    def create_listener(self, module_name, change_identifier, session_type):
        # If I used another function to run this one as thread, python would be upset :D
        # So I'm using a decorator and also it looks cooler :D
        try:
            status(f"Waiting for sessions on {module_name}")
            controller = self.browsers[module_name]["Controller"]
            if controller:
                while self.browsers[module_name]["Status"] == "Success":
                    null = controller.find_elements_by_xpath(change_identifier)
                    if not null:
                        # If we got here then that means we got session
                        print()
                        status(f"Got session on {module_name} module")
                        if session_type.lower() == "localstorage":
                            self.save_localstorage(module_name)
                        elif session_type.lower() == "cookies":
                            self.save_cookie(module_name)
                        else:
                            self.save_profile(module_name)

                        if Settings.verbose:
                            status("Reseting browser cookies and localStorage to start over..")
                        
                        if not session_type.lower() == "profile":
                            controller.delete_all_cookies()
                            controller.execute_script("window.localStorage.clear()")
                            controller.refresh()
                            if Settings.verbose:
                                status("Session reset successfully")
                            time.sleep(5)
                        else:
                            self.close_job()
                            self.close_all()
                    else:
                        time.sleep(5)
            else:
                error(f"Browser controller hasn't been created [{module_name}]")
        except:
            return

    @Run_inside_thread("QR updater thread")
    def website_qr(self, module_name, img_xpath):
        # Always download the QR image from the site to use it in the webserver
        status(f"Running a thread to keep the QR image  [{module_name}]")
        controller = self.browsers[module_name]["Controller"]
        if controller:
            while self.browsers[module_name]["Status"] == "Success":
                try:
                    misc.Screenshot(controller, img_xpath, module_name)
                    #if Settings.verbose: status(f"QR code image updated! [{module_name}]")
                    time.sleep(3)
                except:
                    time.sleep(1)
        else:
            error(f"Browser controller hasn't been created [{module_name}]")

    @Run_inside_thread("Idle detector thread")
    def check_img(self, module_name, button_xpath):
        # Checks if QR image got blocked by a reloading button and click it
        status(f"Running a thread to detect Idle once it happens then click the QR reload button [{module_name}]")
        controller = self.browsers[module_name]["Controller"]
        if controller:
            while self.browsers[module_name]["Status"] == "Success":
                try:
                    btn = controller.find_element_by_xpath(button_xpath) # now it should work
                    # If we got here then that means we got the button
                    if Settings.verbose: status(f"Idle detected, Reloading QR code image [{module_name}]")
                    btn.click()
                    time.sleep(5)
                except:
                    time.sleep(1) # Yeah we need to be fast
        else:
            error(f"Browser controller hasn't been created [{module_name}]")

    @Run_inside_thread("Webserver manager thread")
    def serve_module(self, module_name, host, port):
        # Start a webserver for module and automatically close it when module closed
        status(f"Initializing webserver... [{module_name}]")
        self.browsers[module_name]["host"] = "http://"+host
        self.browsers[module_name]["port"] = str(port)
        webserver = server(name=module_name,port=port)
        webserver.start_serving(host)
        while self.browsers[module_name]["Status"] == "Success":
            time.sleep(1)
        # Well, the module got stopped
        webserver.stop_web_server()

    def save_localstorage(self,module_name):
        browser = self.browsers[module_name]["Controller"]
        session_file_name = os.path.join( "sessions",time.ctime().replace(" ","-") )+".session"
        session_file = open(session_file_name,"wb")
        pickle.dump( browser.execute_script("return localStorage"), session_file)
        session_file.close()
        if Settings.debug:
            status("localStorage data saved in "+session_file_name)
        # Now let's save session details into sessions file
        with open( self.sessions_file ) as f:
            try:
                sessions = json.load(f)
            except:
                sessions = {}

        for i in range(0,1000):
            if str(i) not in list(sessions.keys()):
                session_id = str(i)
                break

        session = {
            session_id:{
                "name":module_name,
                "web_url":self.browsers[module_name]["url"],
                "session_type":"localStorage",
                "useragent":self.useragent,
                "session_path":session_file_name
            }
        }
        sessions.update(session)
        f = open( self.sessions_file,"w" )
        json.dump(sessions, f, indent=2)
        f.close()
        status("Session saved successfully")

    def save_cookie(self,module_name):
        # First let's save the browser cookies before anything
        browser = self.browsers[module_name]["Controller"]
        session_file_name = os.path.join( "sessions",time.ctime().replace(" ","-") )+".session"
        session_file = open(session_file_name,"wb")
        pickle.dump( browser.get_cookies(), session_file)
        session_file.close()
        if Settings.debug:
            status("Cookies saved in "+session_file_name)
        # Now let's save session details into sessions file
        with open( self.sessions_file ) as f:
            try:
                sessions = json.load(f)
            except:
                sessions = {}

        for i in range(0,1000):
            if str(i) not in list(sessions.keys()):
                session_id = str(i)
                break

        session = {
            session_id:{
                "name":module_name,
                "web_url":self.browsers[module_name]["url"],
                "session_type":"cookie",
                "useragent":self.useragent,
                "session_path":session_file_name
            }
        }
        sessions.update(session)
        f = open( self.sessions_file,"w" )
        json.dump(sessions, f, indent=2)
        f.close()
        status("Session saved successfully")

    def save_profile(self, module_name):
        browser = self.browsers[module_name]["Controller"]
        profile_file_name = os.path.join( "profiles",time.ctime().replace(" ","-")) + ".pf"
        profile_file = open(profile_file_name,"w")
        profile_file.write(browser.capabilities['moz:profile'])
        profile_file.close()

        if Settings.debug:
            status("Profile location saved in " + profile_file_name)
        
        with open( self.sessions_file ) as f:
            try:
                sessions = json.load(f)
            except:
                sessions = {}
            
            for i in range(0,1000):
                if str(i) not in list(sessions.keys()):
                    session_id = str(i)
                    break

        session = {
            session_id:{
                "name":module_name,
                "web_url":self.browsers[module_name]["url"],
                "session_type":"profile",
                "useragent":self.useragent,
                "session_path":profile_file_name
            }
        }
        sessions.update(session)
        f = open( self.sessions_file,"w" )
        json.dump(sessions, f, indent=2)
        f.close()
        status("Session saved successfully")

    def close_all(self):
        if self.browsers!={}: # I'm using this comparsion because it's is faster than comparsion with keys length btw
            for module_name in list(self.browsers.keys()):
                try:
                    self.browsers[module_name]["Controller"].close()     # To close the browser
                except: # Some one played with the browser so it lost control lol
                    pass
                self.browsers[module_name]["Controller"] = None      # Reseting the browser controller
                self.browsers[module_name]["Status"]     = None      # To close any listener working on this browser

    def close_job(self, module_name):
        if self.browsers!={}:
            if module_name in list(self.browsers.keys()):
                try:
                    self.browsers[module_name]["Controller"].close()     # To close the browser
                except: # Some one played with the browser so it lost control lol
                    pass
                self.browsers[module_name]["Controller"] = None      # Reseting the browser controller
                self.browsers[module_name]["Status"]     = None      # To close any listener working on this browser

class visible_browsers:
    # Here we open sessions for user with cookies we already have from sessions
    def __init__(self):
        self.browsers = []
        self.sessions_file = os.path.join("core","sessions.json")

    def load_localstorage(self, session_id):
        sessions = json.load(open( self.sessions_file ))
        storage_path = sessions[str(session_id)]["session_path"]
        url = sessions[str(session_id)]["web_url"]
        # Setting useragent to the same one the session saved with
        useragent = sessions[str(session_id)]["useragent"]
        profile = FirefoxProfile()
        profile.set_preference("general.useragent.override", useragent )
        localStorage = pickle.load(open(storage_path, "rb"))
        try:
            browser = Firefox(profile)
        except:
            error("Couldn't open browser to view session!")
            return
        browser.get(url)
        browser.delete_all_cookies()
        browser.execute_script("window.localStorage.clear()") # clear the current localStorage
        for key,value in localStorage.items():
            browser.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)
        status(f"Session {session_id} loaded")
        browser.refresh()
        self.browsers.append(browser)

    def load_cookie(self, session_id):
        sessions = json.load(open( self.sessions_file ))
        cookie_path = sessions[str(session_id)]["session_path"]
        url = sessions[str(session_id)]["web_url"]
        # Setting useragent to the same one the session saved with
        useragent = sessions[str(session_id)]["useragent"]
        profile = FirefoxProfile()
        profile.set_preference("general.useragent.override", useragent )
        cookies = pickle.load(open(cookie_path, "rb"))
        try:
            browser = Firefox(profile)
        except:
            error("Couldn't open browser to view session!")
            return
        browser.get(url)
        browser.delete_all_cookies()
        browser.execute_script("window.localStorage.clear()") # clear the current localStorage
        for cookie in cookies:
            browser.add_cookie(cookie)
        status(f"Session {session_id} loaded")
        browser.refresh()
        self.browsers.append(browser)
    
    def load_profile(self, session_id):
        sessions = json.load(open( self.sessions_file ))
        profile_path = sessions[str(session_id)]["session_path"]
        url = sessions[str(session_id)]["web_url"]
        useragent = sessions[str(session_id)]["useragent"]
        with open(profile_path, "r") as ff:
            pro_path = Path(ff.read())
        profile = FirefoxProfile(str(pro_path))
        try:
            browser = Firefox(profile)
        except:
            error("Couldn't open browser to view session!")
            return
        browser.get(url)
        self.browsers.append(browser)
