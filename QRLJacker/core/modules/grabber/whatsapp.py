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
    image_xpath       = '/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]'
                        #"/html/body/div[1]/div/div/div[2]/div[1]/div[2]"
    img_reload_button = '/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div/span/div'
                        #'/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/span/div'
    change_identifier = '/html/body/div[1]/div/div/div[2]/div[1]/div/div[3]/label/input'
                        #"/html/body/div[1]/div/div/div[2]/div[1]/div[3]/label/input"
    session_type      = "localStorage"
