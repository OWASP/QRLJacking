*QRLJacking* - A New Social Engineering Attack Vector
====================
![](https://github.com/OWASP/QRLJacking/blob/master/blob/images/QRLJacking.JPG?raw=true)






Find documentation in our [Wiki](https://github.com/OWASP/QRLJacking/wiki).
## What is QRLJacking?
QRLJacking or Quick Response Code Login Jacking is a simple social engineering attack vector capable of session hijacking affecting all applications that rely on the “Login with QR code” feature as a secure way to login into accounts. In a nutshell, the victim scans the attacker’s QR code which results in session hijacking.


## What are the requirements to achieve a successful QRLJacking attack?
The QRLJacking attack consists of two sides:

1. Server Side: A server side script is needed to serve and shape the final look to the victim.
2. Client Side: Cloning the QR Code and pushing it to the phishing page.

### Our example will be: The WhatsApp Web Application!

## Server Setup (Attacker's hosting):
1. Upload "qrHandler.php" to your server. This php file is used to convert the base64 QR Code string into a valid .JPG file.

	Now you have a valid, generated, QR image named "tmp.jpg" residing in the same root folder as your files which will be updated whenever that php file is called, so we can put it anywhere. For example: a fake WhatsApp page, a scam page with an offer related to WhatsApp, etc. Depending on your creativity.

2. Now update the "phishing.html" file with your prefered phishing page source code.


## Client Side Setup (Attacker's browser):

1. Open your Firefox browser.
2. Write "about:config" in the url area, click the "I'll be careful, I promise" confirmation button.
3. Search for a preference named "security.csp.enable" and change its value to "false" by double clicking it to allow performing an XHR Request from a different domain (we're not supporting leaving this preference disabled, you may do that while testing, but after that you should set the preference to its original state).
4. Install the Greasemonkey add-on (https://addons.mozilla.org/en-US/firefox/addon/greasemonkey) and be sure that the module file "WhatsAppQRJackingModule.js" is loaded and already running.
5. Now we're ready. Browse to our example "https://web.whatsapp.com" on your side and wait for a WhatsApp session to be loaded. Greasemonkey should now inject our WhatsApp module file to catch.
6. Send the direct link of the final phishing page to a victim.

Once the QR Code is scanned, the victim's session is yours.


## Demo Video:
Attacking WhatsApp Web Application and performing a MITM attack to inject a bogus ad including WhatsApp QR Code.
[Demo Video](https://goo.gl/NLRdtZ)


## Technical Paper
The technical paper clarifying everything about the QRLJacking attack vector can be found directly via our [Wiki](https://github.com/OWASP/QRLJacking/wiki).

# Vulnerable Web Applications and Services
There are a lot of well-known web applications and services which were vulnerable to this attack until the date we wrote this paper. Here are some examples (that we have reported) including, but not limited to:

### Chat Applications:

WhatsApp, WeChat, Line, Weibo, QQ Instant Messaging


### Mailing Services:

QQ Mail (Personal and Business Corporate), Yandex Mail

### eCommerce:

Alibaba, Aliexpress, Taobao, Tmall, 1688.com, Alimama, Taobao Trips


### Online Banking:

AliPay, Yandex Money, TenPay


### Passport Services “Critical”:

Yandex Passport (Yandex Mail, Yandex Money, Yandex Maps, Yandex Videos, etc...)

### Mobile Management Software:

AirDroid

### Other Services:

MyDigiPass, Zapper & Zapper WordPress Login by QR Code plugin, Trustly App, Yelophone, Alibaba Yunos

# Author


[Mohamed Abdelbasset Elnouby (@SymbianSyMoh)](https://github.com/SymbianSyMoh)

Information Security Researcher

Seekurity Labs

MaeBaset@Seekurity.com

# Acknowledgements
I would like to personally thank the talented people who helped shape the QRLJacking attack and got it out into the light. (List in no particular order)

Thanks to:

- [Mohamed Abdel Aty (@M_Aty)](https://github.com/mohamedaty)
- [Mostafa Kassem (@Zanzofily)](https://github.com/Zanzofily)
- [Karim Shoair (@D4Vinci)](https://github.com/D4Vinci)
- [Abdelrahman Shawky (@ShawkyZ)](https://github.com/ShawkyZ)
- [Ahmed Elsobky (@0xSobky)](https://github.com/0xSobky)
- [Ahmed Abbas (@Fiberghost)](https://github.com/fiberghost)
- [Hiram Camarillo (@Hiramcoop)](https://github.com/hiramcoop)
- [Juan Carlos Mejia (@Th3kr45h)](https://github.com/th3kr45h)
- Mohamed Elfateh (OWASP Egypt)
