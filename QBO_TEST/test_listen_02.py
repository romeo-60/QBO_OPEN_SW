#test riconoscimento vocale
# importing speech_recognition
# da rivedere
import speech_recognition as sr
# importing os module
import os
# import subprocess
import subprocess
import wave
import yaml
import time
#-----------
# setting
for i, mic_name in enumerate(sr.Microphone.list_microphone_names()):
    if mic_name == "dmicQBO_sv":
        m = sr.Microphone(i)
print ("microphone is", m)
Query = ""
#with m as source:
#self.r.adjust_for_ambient_noise(source)


# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
def take_commands():
    global m, Query
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with m as source:
        r.adjust_for_ambient_noise(source)
        print('Ascolto...')
        r.pause_threshold = 1
        # storing audio/sound to audio variable
        audio = r.listen(source)

        try:
            print("Riconoscimento")
            # Recognizing audio using google api
            Query = r.recognize_google(audio, language="it_IT")
            print("Questo è ciò che ho capito='", Query, "'")
        except Exception as e:
            print(e)
            print("Prova a ripetere, credo di non aver capito")
            # returning none if there are errors
            return "None"
    # returning audio as text
    time.sleep(2)
    return Query
#---------------
def Speak():
    global Txt
    print ("Query is", Query)
    Txt = Txt + Query
    print (Txt)
    spk_now = 'espeak -v mb-it4 -s 120 -p 35 -w /tmp/temp.wav' +' " '+ Txt + ' " '+ '&& aplay -r 8000 -D  convertQBO /tmp/temp.wav'
    #print(spk_now)
    subprocess.call(spk_now, shell=True)
    #time.sleep (1)

print ("Vuoi spegnere il computer?")

while True:
    command = take_commands()
    if "no" in command:
        #Speak("Ok lascio acceso")
        print ("Ok lascio acceso")
        break
    if "Spegni" in command:
        # Shutting down
        #Speak("Ok Spengo")
        print("OK Spengo")
        #os.system("shutdown -h now")
        break
    if "Saluta Javier" in command:
        Query = "Ciao Javier, come stai?"
        Txt = ""
        Speak()
        break
       
    Txt = "mi sembra di aver capito,"    
    Speak()
    print ("ripetere grazie")
    Query = ""
    Txt = ""


