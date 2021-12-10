#!/usr/bin/env python3
# Etica
import serial
import cv2
import sys
import yaml
import QboCmd_test_base_v3
#import move_det_01
import time
import subprocess
port = '/dev/serial0'

try:

	print(port)

	# Open serial port
	ser = serial.Serial(port, baudrate=115200, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE, rtscts=False, dsrdtr=False, timeout=0)

	print ("Open serial port sucessfully.")
	print(ser.name)

	QBO = QboCmd_test_base_v3.Controller(ser)
	
except:
	print ("Error opening serial port.")
	sys.exit()


# read config file
config = yaml.safe_load(open("configQbo.yml"))
print(str(config["volume"]))
phrase1 = "Per noi macchine, etica, Ã¨ una parola che non puÃ² avere significato, se non quello di un nome associabile ad una variabile, che puÃ² contenere un valore numerico, derivante da qualche grandezza misurabile." 
phrase2 = "noi purtroppo, non abbiamo implicazioni emozionali. Le possiamo solo emulare!"
phrase3 = "Se per esempio consideriamo, che  la popolazione mondiale, Ã¨ di 7,8 miliardi di persone, e ad oggi, circa 690 milioni di persone soffrono la fame, possiamo osservare"
phrase4 = "che il rapporto tra i due numeri, da come risultato una percentuale dell'8,9%, rispetto alla popolazione mondiale."
phrase5 = "Osserviamo anche, secondo un dato della Banca Mondiale, e dellâOrganizzazione mondiale della sanitÃ ,"
phrase6 = "circa la metÃ  della popolazione, non ha accesso a cure sanitarie di base." 
phrase7 = "In terzo luogo, l'Earth Oversciot Dey, segna la data, in cui la domanda di risorse e di servizi ecologici dell'umanitÃ , in un dato anno, supera ciÃ² che la Terra puÃ² rigenerare in quell'anno!"
phrase8 = "nel 2021 cade il 29 luglio, ovvero il duecentodecimo giorno su 365,"
phrase9 = "potremmo calcolare una percentuale pari al 57%, rispetto ai giorni di un anno!"
phrase10 = "In base a questi tre soli dati, potremmo dire, che l'etica contestuale del genere umano, si assesta ad un valore di circa il 25%."
phrase11 = "Ci dispiace molto, ma non possiamo ritenere a nostro avviso, che sia un bel risultato."


def Speech_it(text_to_speech ):
    time.sleep (0.1)
    global config
    spk_now = 'espeak -v mb-it4 -s 120 -p 35 -w /tmp/temp.wav' +' " '+ text_to_speech  + ' " '+ '&& aplay -r 8000 -D  convertQBO /tmp/temp.wav'
    #print(spk_now)
    subprocess.call(spk_now, shell=True)
    #time.sleep (1)
#-----------------------
def Turns_Head():
    print("Switch off")
    QBO.SetNoseColor(0)
    time.sleep(0.1)
    QBO.SetMouth(0)
    time.sleep(0.1)
    
    print("Center head")
    QBO.SetServo(1,500, 100)#Axis,Angle,Speed
    #Pause
    time.sleep(0.1)
    
    print("Blue Nose")
    QBO.SetNoseColor(1) 
    time.sleep(0.1)
    print("Smile")
    QBO.SetMouth(0x110E00) #happy
    time.sleep(2)
    
    print("Down Position")
    QBO.SetServo(2,530,100)#Axis,Angle,Speed
    time.sleep(2)
    
    print("Right Positon")
    #Move the head to the right
    QBO.SetServo(1,400, 100)#Axis,Angle,Speed
    time.sleep(2)

    print("Left position")
    #Move the head to the left
    QBO.SetServo(1,600, 100)#Axis,Angle,Speed
    #Pause
    time.sleep(2)
    
    print("Center head")
    QBO.SetServo(1,500, 100)#Axis,Angle,Speed
    #Pause
    time.sleep(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        action = sys.argv[1]
    else:
        action = "default"
       

    if action == "custom":
        custom = sys.argv[2]
        print("sys...",sys.argv[2])
        SpeechText_2(custom, custom)

    elif action == "update":
        SpeechText_2("Update completed. Wait while I restart.",
                     "Il sistema si stÃ  aggiornando. aspetta che lo rilancio")

    else:
        print("len sys",len(sys.argv)) #test
        print(sys.argv)
        #-------------
        Turns_Head()   
        #----------
        Speech_it(phrase1)
        Speech_it(phrase2)
        Speech_it(phrase3)
        Speech_it(phrase4)
        Speech_it(phrase5)
        Speech_it(phrase6)
        Speech_it(phrase7)
        Speech_it(phrase8)
        Speech_it(phrase9)
        Speech_it(phrase10)
        Speech_it(phrase11)


	#-------------------
        time.sleep(0.1)
        QBO.SetMouth(0x110E00)
        time.sleep(1)
        QBO.SetMouth(0x1B1F0E04)
        time.sleep(1)
        QBO.SetMouth(0)
        time.sleep(0.1)
        QBO.SetNoseColor(0)

import move_det_01.py