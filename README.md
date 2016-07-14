*QRLJacking* - A new Social Engineering Attack Vector
====================

Find documentation in our [Wiki](https://github.com/OWASP/QRLJacking/wiki).
## What is QRLJacking?
QRLJacking or Quick Response Code Login Jacking is a simple-but-nasty attack vector affecting all applications that relay on “Login with QR code” feature as a secure way to login into accounts. In a simple way, It’s all about convincing the victim to scan the attacker’s QR code.


## What are the requirements to achieve a successful QRLJacking attack?
QRLJacking attack consists of two sides:

1. Server Side: A server side script is needed to serve and shape the final look to the victim.
2. Client Side: Cloning the QR and pushing it to the phishing page.

### Our example will be: WhatsApp Web Application!

## Server Setup (Attacker's hosting):
1. Upload "qrHandler.php" to your server, this php file is used to convert the base64 qr code string into a valid .JPG file

	Now we have a valid generated QR image named "tmp.jpg" residing in the same root folder of your files and will be updated whenever that php file will be called, So we can put it anywhere "for example a fake WhatsApp page, a scam page with an offer related to WhatsApp, etc... depending on your creativity"

2. Now update the "phishing.html" file your prefered phishing page source code.


## Client Side Setup (Attacker's browser):

1. Open your Firefox browser!
2. Write "about:config" in the url area, click the "i'll be careful, i promise" confirmation button.
3. Search for a preference named "security.csp.enable" and change it's value to "false" by double clicking it to allow performing an XHR Request over a different domain (We're not supporting leaving this preference disabled, you may do that while testing, but after that you should set the preference to its original state).
4. Instal Greasemonkey addon (https://addons.mozilla.org/en-US/firefox/addon/greasemonkey) and be sure that the module file "WhatsAppQRJackingModule.js" is loaded and already running!
5. Now We're Ready, Browse to our example "https://web.whatsapp.com" on your side, Wait for a WhatsApp session to be loaded, Greasemonkey should now inject our WhatsApp module file to catch and  .
6. Send the direct link of the final phishing page to a victim "Once the QR scanned, Victim's session is yours now"


## Demo Video:
Attacking WhatsApp Web Application and performing MiTM attack to inject a bogus ad including WhatsApp QR Code
<a href="https://goo.gl/NLRdtZ">Demo Video</a>

## Technical Paper
The technical paper clarifying  everything about QRLJacking attack vector can be found [here](https://github.com/OWASP/QRLJacking/blob/master/blob/QRLJacking%20Technical%20Paper.pdf) or directly visit our [Wiki](https://github.com/OWASP/QRLJacking/wiki).
