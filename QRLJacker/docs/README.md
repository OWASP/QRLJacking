Well, I worked so hard to make the development as simple as possible and you will see that :smile:
> before starting make sure you turned the development mode on. If you done so, the framework will reload the module every time you run it with the new changes without needing to restart the framework

# Writing a grabber module for the Framework
- Grabber modules are the main modules in the framework and it lies in the directory `core/modules/grabber`
- Once you add any python file there, it gets loaded into the framework with three options automatically. The three options are (of course) host, port and useragent
- The code inside the module file should be as follows:

```
# -*- coding: utf-8 -*-
from core.module_utils import types

class info:
    author            = ""               # (1)
    short_description = ""               # (2)
    full_description  = None             # (3)

class execution:
    module_type       = types.grabber
    name              = ""               # (4)
    url               = ""               # (5)
    image_xpath       = ""               # (6)
    img_reload_button = None             # (7)
    change_identifier = ""               # (8)
    session_type      = "localStorage"   # (9)

```

The code variables is described below:
1. Here you add your name which will appear in the framework
2. Here you put a quick short description which will appear when listing the Modules
3. Here you put the full Description to your module if it's necessary and it will appear only when using the `info` command. If you won't add one, leave it as None and the short description will be used instead.
4. The name of the website which will be used inside the framework and also you should create a folder with the same name as the variable value in the path `core/www` example: `core/www/whatsapp`
5. The Url which have the QR code and used to load the session example: `https://web.whatsapp.com`
6. The exact xpath to the QR image position in the page because it will be used by the framework to screenshot the QR code image.
7. If this websites checks for idle and wants you to click refresh every few minutes like whatsapp for example then put the exact xpath for this button when it appears and the framework will run a thread to check every few seconds the reload button appearance then click it. If this technique isn't used, leave the variable as None.
8. The xpath of an element in the page disappears only when the session loads. For example the QR code img tag in whatsapp.
9. This variable takes one of two values `localStorage` or `Cookies`. The value should be the same used in the website to determine user session.

And voilaaa! You have created your first module. You can keep it for yourself or better make a PR to the framework so everyone can use your module with your name on it, do the math :smile:
