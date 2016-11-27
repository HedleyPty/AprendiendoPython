﻿# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       english.rpy [English Soft Keyboard]
#                                                                                                       Author   :  Andrea Rubenstein
#                                                                                                       Created : 2011/10/14
#                                                                                                       Updated: 2011/10/16
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
   
init -1 python:
 
##############################################################################
#       KEYS
##############################################################################     
    if persistent.lang == "en":
        INPUT_VALUE_DEFAULT = ""
        INPUT_LABEL_DEFAULT = "¿Cuál es el año de tu fecha de nacimiento?\nIngresa un dato incorrecto y aprenderás algo nuevo"
    
        softkey_type = [{"alphabet" : "en"}, {"symbols" : "en"}]
        
        #main_buttons["default"] = "Default"
        main_buttons["clear"] = "Limpiar"
        main_buttons["confirm"] = "OK"
        
        input_nav_buttons["alphabet"] = "ABC"
        input_nav_buttons["symbols"] = "123"
        
    softkey["en"] = {}
    softkey["en"]["alphabet"] = []
    softkey["en"]["alphabet"].append(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","x","z"])
    softkey["en"]["alphabet"].append(["à","á","â","ã","ä","å","æ","ç","è","é","ê","ë","ì","í","î","ï","ð","ñ","ò","ó","ô","õ","ö","ø","ù","ú","û","ü","ý","þ","ÿ"])

    softkey["en"]["symbols"] = []
    softkey["en"]["symbols"].append(["1","2","3","4","5","6","7","8","9","0","#","$","%","&","(",")",":",";",".",",","?","!","•",">","<","|","=","…","¡","¿","„","§","†","‡","±"])
    softkey["en"]["symbols"].append(["\'","\"","-","_","~","^","\\","/","★","☆","♀","♂","♥","♠","♣","♦","♪","♫","♭","♯","∞","™","©","®"])

##############################################################################
#       SCREENS
##############################################################################   
if persistent.lang == "en":
    screen input_special_type:
        $col = key_col-2
        grid 1 col:
            if input_keyboard == "alphabet":
                textbutton input_special["caps"] action [ToggleVariable("input_caps"),SetVariable("input_alphabet", SwitchCaps(input_alphabet,not input_caps))] style "keyboard_button_special"
                textbutton input_special["shift"] action [ToggleVariable("input_shift"),SetVariable("input_alphabet", SwitchCaps(input_alphabet,not input_shift))] style "keyboard_button_special"
                for i in range(2,col):
                    null   
            else:
                for i in range(0,col):
                    null   
        
#EOF
