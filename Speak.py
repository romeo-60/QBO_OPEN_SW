#!/usr/bin/env python3
# -*- coding: latin-1 -*-
#--- software modified by Romeo Ceccato ---

import sys
import yaml
import subprocess

# read config file
config = yaml.safe_load(open("/opt/qbo/config.yml"))


def SpeechText_2(text_english, text_spain, forceStandalone=False):
    global config

    lang_code = 'en-US'
    text = text_english
    if config['language'] == 'spanish':
        lang_code = 'es-ES'
        text = text_spain

    speak = 'pico2wave -l "{}" -w /opt/qbo/sounds/pico2wave.wav "<volume level=\'{}\'>{}" && aplay -D convertQBO /opt/qbo/sounds/pico2wave.wav'.format(lang_code, config['volume'], text)

    subprocess.call(speak, shell=True)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("argv_1") #test
        action = sys.argv[1]
    else:
        print("argv <1") #test
        action = "default"
       

    if action == "custom":
        custom = sys.argv[2]
        print("custom") #test
        SpeechText_2(custom, custom)

    elif action == "update":
        print("update") #test
        SpeechText_2("Update completed. Wait while I restart.",
                     "El sistema se ha actualizado correctamente. Espera mientras reinicio.")

    else:
        print("speekText2") #test
        #SpeechText_2("Hi. I am Cubo",
                     #"Hola. Soy Cubo")
        SpeechText_2("hello Romeo, how were you, I'm happy to see you, , , how is beatrice? , , , where are the cats?",
                     "Hola. Soy Cubo")

