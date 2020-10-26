*QRLJacking* - A New Social Engineering Attack Vector
====================
![](https://github.com/OWASP/QRLJacking/blob/master/blob/images/QRLJacking.JPG?raw=true)






Find documentation in our [Wiki](https://github.com/OWASP/QRLJacking/wiki).
## What is QRLJacking?
QRLJacking or Quick Response Code Login Jacking is a simple social engineering attack vector capable of session hijacking affecting all applications that rely on the “Login with QR code” feature as a secure way to login into accounts. In a nutshell, the victim scans the attacker’s QR code which results in session hijacking.


## Exploitation, Client Side Setup (Attacker's browser):

Using QRLJacker - [QRLJacking Exploitation Framework](https://github.com/OWASP/QRLJacking/tree/master/QRLJacker)

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

Mohamed.Baset@OWASP.org

# Acknowledgements
(List in no particular order)

- [Mohamed Abdel Aty (@M_Aty)](https://github.com/mohamedaty)
- [Mostafa Kassem (@Zanzofily)](https://github.com/Zanzofily)
- [Karim Shoair (@D4Vinci)](https://github.com/D4Vinci)
- [Abdelrahman Shawky (@ShawkyZ)](https://github.com/ShawkyZ)
- [Ahmed Elsobky (@0xSobky)](https://github.com/0xSobky)
- [Ahmed Abbas (@Fiberghost)](https://github.com/fiberghost)
- [Hiram Camarillo (@Hiramcoop)](https://github.com/hiramcoop)
- [Juan Carlos Mejia (@Th3kr45h)](https://github.com/th3kr45h)

