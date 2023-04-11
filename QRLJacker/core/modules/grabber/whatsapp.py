# -*- coding: utf-8 -*-
# Written by: Karim shoair - D4Vinci ( QrlJacker-Framework )
from core.module_utils import types

class info:
    author            = "Karim Shoair (D4Vinci)"
    short_description = "Whatsapp QR-sessions grabber and controller"
    full_description  = None

class execution:
    module_type       = types.grabber
    name              = "whatsapp"
    url               = "https://web.whatsapp.com"
    image_xpath       = '/html/body/div[1]/div/div/div[3]/div[1]/div/div/div[2]/div/canvas'
    img_reload_button = '/html/body/div[1]/div/div/div[3]/div[1]/div/div/div[2]/div/span/button'
    change_identifier = '/html/body/div[1]/div/div/div[4]/header/div[1]/div/img'
    session_type      = "profile"
