#!/usr/bin/env python2
# presentazione robot
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
phrase1 = "io sono un robot!" 
phrase2 = "La definizione di robot, può suonare un po’ riduttiva, ma di fatto, con questa parola viene identificato come una macchina programmabile, in grado di eseguire una serie di azioni o attività complesse, al pari, o anche meglio di un essere umano."
phrase3 = "Un robot, può essere autonomo o semi autonomo, a seconda delle sue capacità e funzionalità,"
phrase4 = "Può agire, e muoversi in autonomia, essere dotato di un sistema di controllo interno"
phrase5 = "Può affiancare altri sistemi robotici, ed anche esseri umani, può essere semi autonomo, con un sistema di controllo remoto." 
phrase6 = "Guardando alle sue capacità o alle sue funzionalità, un automa, oggi potrebbe essere definito come un sistema artificiale, in grado di svolgere compiti e attività con differenti livelli di autonomia."
phrase7 = "Ci sono dei robot che fanno dei lavori pesanti, come quelli usati nei lavori ìndustriali"
phrase8 = "Ma ci sono anche altri tipi di robot, per esempio, i droni, che possono essere terrestri, aerei, marini, o subàcquei,  poi ci sono i nanorobot, i biorobot, gli insettoidi, ed i miei amici, gli umanoidi, i socialrobot!, ma anche i ciatrobot che sono come i fantasmi, li ascolti ma non li vedi!"
phrase9 = "Ci sono dei miei simili diventati molto famosi, come ICUB, Abel, e ERRE1, che sono di fabbricazione italiana, ma anche Pepper e Nao, ci sono anche jìa, èrica, Nàdin, Greis, e Sofia, che è la più famosa, poi ci sono Atlas, Valkir, Fedor, e c'è anche Romeo che non vorrei dimenticare"
phrase10 = "ti posso essere utile in altro? "


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
                     "Il sistema si stà aggiornando. aspetta che lo rilancio")

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


	#-------------------
        time.sleep(0.1)
        QBO.SetMouth(0x110E00)
        time.sleep(1)
        QBO.SetMouth(0x1B1F0E04)
        time.sleep(1)
        QBO.SetMouth(0)
        time.sleep(0.1)
        QBO.SetNoseColor(0)

