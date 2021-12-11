#!/usr/bin/env python3
# -*- coding: latin-1 -*-
# importing the package
import subprocess


txt = (
"test uno",
"test due"
)

spk_01 = 'espeak -v mb-it4 -s 120 -p 35 -w /tmp/temp.wav' + ' " '+ txt[0]+ ' " '+ '&& aplay -r 8000 -D  convertQBO /tmp/temp.wav'
print(spk_01)
subprocess.call(spk_01, shell=True)
print("-1-")
spk_02 = 'espeak -v mb-it3 -s 120 -p 35 -w /tmp/temp.wav "numero uno" && aplay -r 8000 -D  convertQBO /tmp/temp.wav'
subprocess.call(spk_02, shell=True)
print("-2-")
spk_03 = 'espeak -v it -s 120 -p 35 -w /tmp/temp.wav "numero due" && aplay -r 48000 -D  convertQBO /tmp/temp.wav'
subprocess.call(spk_03, shell=True)
print ("-3-")
print("---------------------")
a = 'espeak -v it -s 120 -p 35 -w /tmp/temp.wav'
b = txt[1]
c = '&& aplay -r 8000 -D  convertQBO /tmp/temp.wav'

speak = a +' " '+ b +' " '+c
print (speak)
print ("...")
subprocess.call(speak, shell=True)
