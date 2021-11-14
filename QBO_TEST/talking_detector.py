#!/usr/bin/env python3
# -*- coding: latin-1 -*-
#it works even if it loses track sometimes (returns to Home)
import QboCmd
import serial
import cv2
import numpy as np
import subprocess
import time
import yaml
#--------------------
port = '/dev/serial0'
# Open serial port
ser = serial.Serial(port, baudrate=115200, bytesize = serial.EIGHTBITS, stopbits = serial.STOPBITS_ONE, parity = serial.PARITY_NONE, rtscts = False, dsrdtr =False, timeout = 0)
print ("Open serial port sucessfully.")
print(ser.name)
QBO = QboCmd.Controller(ser)
#---------------------------
# constant for the movement
Ksp = 100 #speed = 100
#frame dimension
fw = 320
fh = 280
fwc = fw/2
fhc =fh/2
center = fwc, fhc 
f_frameCenter = fwc, fhc
p_frameCenter = fwc, fhc
f_face = None
p_face = None
#logic flags
f_Facedet = None
p_Facedet = None
#initial frames
f_frame = None
p_frame = None
Face_detected = None
#settings time and counters
fr_time = 0
f_i = 0 # frame counter
p_i = 0 
f_counter = 0
p_counter = 0
## Head X and Y angle limits
Xmax = 725 #total LEFT
Xmin = 300 #total RIGHT
Ymax = 550 #total UP
Ymin = 400 #total DOWN
## Initial Head position
Home_x = 511
Home_y = 550
Xcoor = 511
Ycoor = 550
#-----touch control------
move_to = [0]
touch_str = ''
#no_move_tm = time.time()
#det_valid =time.time()
#----- speak session -----
# read config file
config = yaml.safe_load(open("configQbo.yml"))
print(str(config["volume"]))
phrases = (
    "ciao, ti ho visto!", 
    "buogiorno!", 
    "heilà", 
    "scusa, ero distratto! adesso ti ho visto",
    "ci sono!adesso ti vedo!",
    "ciao!",
    "guarda che ti vedo sai?",
    "eccoti quì!",
    "non è stato facile, ma ti ho visto!",
    "che piacere vederti"
)
 
# information on the page https://github.com/opencv/opencv/tree/master/data/haarcascades
f_faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
p_faceCascade = cv2.CascadeClassifier("haarcascade_profileface.xml")
#----------------------------------
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, fw)  
video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, fh)
#------test ---------
QBO.SetMouth(0)
time.sleep(0.1)
QBO.SetNoseColor(0) 
time.sleep(0.1)
print("Blue Nose")
QBO.SetNoseColor(1) 
print ("OK")
#---------------
def ServoHead():
    global Xcoor, Ycoor, Xmax, Xmin, Ymax, Ymin, Ksp
    if Xcoor < Xmin:
        Xcoor  = Xmin +1
    if Xcoor > Xmax:
        Xcoor = Xmax -1
    #------------------
    if Ycoor < Ymin: 
        Ycoor = Ymin + 1
    if Ycoor > Ymax:
        Ycoor = Ymax -1
    print("Cam_X =",Xcoor)
    time.sleep(0.1)
    QBO.SetServo(1, Xcoor, Ksp)
    time.sleep(1)
    print("Cam_Y =",Ycoor)
    QBO.SetServo(2, Ycoor, Ksp)
    time.sleep(1)
	
#testmove
ServoHead()
time.sleep (1)

def F_capture(video_capture):
    global f_frame, f_frameCenter, f_counter, f_i, f_Facedet
    f_i+=1
    # Capture frame-by-frame
    ret, f_frame = video_capture.read()
    gray = cv2.cvtColor(f_frame, cv2.COLOR_BGR2GRAY)
    f_face = f_faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.03,
        minNeighbors=1,
        minSize=(60, 60),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
	)
    
    # Draw a rectangle around the faces
    if len(f_face) > 0:
        f_counter+=1
        f_i = 0
        print("f_counter",f_counter)
        print ("F_FACE")
        f_Facedet = True
        # extract the bounding box coordinates of the face and
        # use the coordinates to determine the center of the
        # face
        (x, y, w, h) = f_face[0]
        f_faceX = int(x + (w / 2.0))
        f_faceY = int(y + (h / 2.0))
        f_frameCenter = (f_faceX, f_faceY)
        # return the center (x, y)-coordinates of the face
        # return (f_frameCenter, f_Facedet,)
    else:
        f_Facedet = False
    
    if f_Facedet == True:
           #print("Smile")
           QBO.SetMouth(0x110E00) #happy
           time.sleep(0.1)
    if f_i > 20:
        f_counter = 0
        print("F_reset")
        f_frameCenter = fwc, fhc
 
def P_capture(video_capture):
    global p_frame, p_frameCenter, p_counter, p_i, p_Facedet
    p_i+=1
    # Capture frame-by-frame
    ret, p_frame = video_capture.read()
    gray = cv2.cvtColor(p_frame, cv2.COLOR_BGR2GRAY)
    p_face = p_faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.03,
        minNeighbors=1,
        minSize=(60, 60),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
	)
    
    # Draw a rectangle around the faces
    if len(p_face) > 0:
        p_counter+=1
        p_i = 0
        print("p_counter",p_counter)
        print ("P_FACE")
        p_Facedet = True
        # extract the bounding box coordinates of the face and
        # use the coordinates to determine the center of the
        # face
        (x, y, w, h) = p_face[0]
        p_faceX = int(x + (w / 2.0))
        p_faceY = int(y + (h / 2.0))
        p_frameCenter = (p_faceX, p_faceY)
        # return the center (x, y)-coordinates of the face
        
    else:
        p_Facedet = False
    
    if p_Facedet == True:
           # print("Smile")
           time.sleep(0.1)
           QBO.SetMouth(0x110E00) #happy
           time.sleep(0.1)
    if p_i > 20:
        p_counter = 0
        print("reset PI")
        p_frameCenter = fwc, fhc
        
def FaceControl():
    global Home_x, Home_y, Xcoor, Ycoor, Face_detected
    if f_Facedet == True or p_Facedet == True:
        Face_detected = True
        print ("Face_detected = ", Face_detected)
        speaker_ok = False
        if Face_detected == True and speaker_ok == False:
            t_ini = time.time()
            print("sepaker", speaker_ok)
            Speech_it(phrases[int(np.random.rand()*10)])
            speaker_ok = True
            print ("t_ini",t_ini," ", "sepaker_ok=", speaker_ok)
            Face_detected = False
            print ("time", time.time())
            if time.time() - t_ini > 100:
                print ("°°°°°°°°°°°")
                print ("time:", time.time(), "t_ini", t_ini)
                t_ini = time.time()
                speaker_ok = False
        
    #----------
    print ("FI", f_i, ' ', "PI", p_i)
    print ("----")
    print ("f_Facedet", f_Facedet, " ", "p_Facedet", p_Facedet)
    #print ("f_frameCenter", f_frameCenter, " ", "p_frameCenter", p_frameCenter)
    F_Xcoor = f_frameCenter[0]
    F_Ycoor = f_frameCenter[1]
    P_Xcoor = p_frameCenter[0]
    P_Ycoor = p_frameCenter[1]
    print ("F_COOR",' ', F_Xcoor, " ", F_Ycoor)
    print ("----")
    print ("P_COOR",P_Xcoor, " ", P_Ycoor)
    if f_Facedet:
        print ("F_DETECTED")
        Xcoor = Home_x + (fwc - F_Xcoor)
        Ycoor = Home_y - (fhc - F_Ycoor)
        print("FRONTAL Xcoordinate", Xcoor, "Ycoordinate",Ycoor)
        ServoHead()

    if p_Facedet:
        print ("P_DETECTED")
        Xcoor = Home_x + (fwc - P_Xcoor)
        Ycoor = Home_y - (fhc - P_Ycoor)
        print("PROFILE Xcoordinate", Xcoor, "Ycoordinate",Ycoor)
        ServoHead()
            
    if p_i >20 and f_i > 20:
        QBO.SetMouth(0) # not faces detected
        Xcoor = Home_x
        Ycoor = Home_y
        time.sleep(0.1) 
        ServoHead()
        
def Speech_it(text_to_speech ):
    global config
    time.sleep (1)
    speak = 'pico2wave -l \"it-IT\" -w //home/pi/QBO/QBO_BETA_0/pico2wave.wav "<volume level=\'{}\'>{}" && aplay -D convertQBO /home/pi/QBO/QBO_BETA_0/pico2wave.wav'.format(config['volume'],text_to_speech)
    subprocess.call(speak, shell=True)
    print("**********")
    print("speak",speak)
#-----------------------  
def WaitForTouch():
    global touch
    touch = QBO.GetHeadCmd("GET_TOUCH", 0)

    if touch:
        if touch == [1]:
            touch_str = "Touch: left"
            print("Left Positon")
            QBO.SetServo(1,650, 100)#Axis,Angle,Speed
            time.sleep(1) 
             			
        elif touch == [2]:
            touch_str = "Touch: up"
            print("Center head")
            QBO.SetMouth(0x1B1F0E04) #love
            time.sleep(0.1)
            QBO.SetServo(1,511, 100)#Axis,Angle,Speed
            time.sleep(1)
            
        elif touch == [3]:
            touch_str = "Touch: right"
            print("Right position")
            QBO.SetServo(1,350, 100)#Axis,Angle,Speed
            time.sleep(1) 
            
        if touch == [1] or touch == [2] or touch == [3]:
			print("touch ",touch)
		
	time.sleep(1)
	#return touch_str





         
while True:
    fr_time = time.time()
    #print ("time: " + str(time.time() - fr_time))
    F_capture(video_capture)
    P_capture(video_capture)
    #cv2.circle(f_frame, f_frameCenter, radius=4, color=(255, 0, 0), thickness=-1)
    #cv2.imshow('FVideo', f_frame)
    #cv2.circle(p_frame, p_frameCenter, radius=4, color=(0, 255, 0), thickness=-1)
    #cv2.imshow('PVideo', p_frame)
    FaceControl()
    time.sleep(1)
    WaitForTouch()    
    if cv2.waitKey(1) & 0xFF == ord('q') : #== ord('q')
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
QBO.SetNoseColor(0)
time.sleep(0.5)
QBO.SetMouth(0)


