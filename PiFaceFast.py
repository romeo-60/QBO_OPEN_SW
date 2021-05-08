##!/usr/bin/env python3
# -*- coding: latin-1 -*-
#--- software modified by Romeo Ceccato ---

import os
import subprocess
import cv2
import serial
import sys
import time
import Speak
import thread
import yaml
import imp
#from assistants.QboGAssistant import GAssistant
#from assistants.QboWatson import QBOWatson
from assistants.QboTalk import QBOtalk
from assistants.QboTalkMycroft import QBOtalkMycroft
from controller.QboController import Controller
#from snowboy.snowboythreaded import ThreadedDetector
from VisualRecognition import VisualRecognition
from assistants.QboDialogFlowV2 import QboDialogFlowV2


config = yaml.safe_load(open("/opt/qbo/config.yml"))

if config["startWith"] == "interactive-mycroft":
		print ("Mode: MyCroft"
		subprocess.call('sudo bash /opt/qbo/mycroft-core/start-mycroft.sh audio && sudo bash /opt/qbo/mycroft-core/start-mycroft.sh bus && sudo bash /opt/qbo/mycroft-core/start-mycroft.sh skills', shell=True))

		talk = QBOtalkMycroft()

	else:
		print ( "fatal error")

## Global Hotword defector

threaded_detector = 0

##

Kpx = 1
Kpy = 1
Ksp = 40

## Head X and Y angle limits

Xmax = 725
Xmin = 290
Ymax = 550
Ymin = 420

## Initial Head position

Xcoor = 511
Ycoor = 450
Facedet = 0

## Time head wait turned
touch_wait = 2

no_face_tm = time.time()
face_det_tm = time.time()
last_face_det_tm = time.time()
touch_tm = 0
touch_samp = time.time()
qbo_touch = 0
touch_det = False
Listening = False
WaitingSpeech = False
listen_thd = 0
face_not_found_idx = 0
mutex_wait_touch = False
faceFound = False
HotwordListened = False

if len(sys.argv) > 1:
	port = sys.argv[1]
else:
	port = '/dev/serial0'

try:
	# Open serial port
	ser = serial.Serial(port, baudrate=115200, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE, rtscts=False, dsrdtr=False, timeout=0)
	print ("Open serial port sucessfully.")
	print (ser.name)

except:
	print ("Error opening serial port.")
	sys.exit()

controller = Controller(ser)
vc = VisualRecognition()

try:
	controller.SetMicrophoneGain(config['microphoneGain'])
except KeyError:
	controller.SetMicrophoneGain(100)

controller.SetServo(1, Xcoor, int(config["servoSpeed"]))
controller.SetServo(2, Ycoor, int(config["servoSpeed"]))
time.sleep(1)
#controller.SetPid(1, 26, 12, 16)
controller.SetPid(1, 26, 2, 16)
time.sleep(1)
#controller.SetPid(2, 26, 12, 16)
controller.SetPid(2, 26, 2, 16)
time.sleep(1)
controller.SetNoseColor(0)  # Off QBO nose brigth

webcam = cv2.VideoCapture(int(config['camera']))  # Get ready to start getting images from the webcam
webcam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320)  # I have found this to be about the highest-
webcam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)  # resolution you'll want to attempt on the pi
#webcam.set(cv2.CV_CAP_PROP_BUFFERSIZE, 2)		# frame buffer storage

if not webcam:
	print ("Error opening WebCAM")
	sys.exit(1)


##get webcam properties
# for i in range(0,24):
#   print webcam.get(i)

frontalface = cv2.CascadeClassifier("/opt/qbo/haarcascades/haarcascade_frontalface_alt2.xml")  # frontal face pattern detection
profileface = cv2.CascadeClassifier("/opt/qbo/haarcascades/haarcascade_profileface.xml")  # side face pattern detection

face = [0, 0, 0, 0]  # This will hold the array that OpenCV returns when it finds a face: (makes a rectangle)
Cface = [0, 0]  # Center of the face: a point calculated from the above variable
lastface = 0  # int 1-3 used to speed up detection. The script is looking for a right profile face,-
# a left profile face, or a frontal face; rather than searching for all three every time,-
# it uses this variable to remember which is last saw: and looks for that again. If it-
# doesn't find it, it's set back to zero and on the next loop it will search for all three.-
# This basically tripples the detect time so long as the face hasn't moved much.

time.sleep(1)  # Wait for them to start


def ServoHome():
	global Xcoor, Ycoor, touch_tm

	Xcoor = 511
	Ycoor = 450

	controller.SetServo(1, Xcoor, int(config["servoSpeed"]))
	time.sleep(0.1)
	controller.SetServo(2, Ycoor, int(config["servoSpeed"]))
	touch_tm = time.time()

	return


def WaitForSpeech():
	global WaitingSpeech, Listening, listen_thd
	#print ("WaitingSpeech " + str(WaitingSpeech))

	if config["distro"] == "ibmwatson":
		if talk.onListeningChanged:
			talk.onListeningChanged = False
			if talk.onListening:
				controller.SetNoseColor(1)
			else:
				controller.SetNoseColor(0)

	if WaitingSpeech == False and interactiveTypeGAssistant == False:  # mutex zone
		WaitingSpeech = True

		if Listening == False:
			WaitingSpeech = False
			return

		elif config["distro"] != "ibmwatson" and vc.askAboutMe(talk.strAudio):
			talk.GetResponse = False

			print ("Started visual recognition")
			subprocess.call("aplay /opt/qbo/sounds/blip_0.wav", shell=True)
			
			vc.captureAndRecognizeImage(webcam)

			if vc.resultsAvailable:
				print (vc.results)
				talk.SpeechText(vc.results[0])
				vc.resultsAvailable = False

			talk.strAudio = " "
			talk.GetAudio = False
			talk.GetResponse = False

		elif talk.GetResponse == True:

			if config["distro"] != "ibmwatson":
				listen_thd(wait_for_stop=True)

			if len(talk.Response) > 0:
				talk.SpeechText(talk.Response)

			if config["distro"] != "ibmwatson":
				controller.SetNoseColor(0)

			talk.GetResponse = False
			Listening = False

			StartHotwordListener()

		WaitingSpeech = False

	return


def WaitTouchMove():
	global Xcoor, Ycoor, touch_tm, mutex_wait_touch, faceFound

	if (mutex_wait_touch):
		return

	mutex_wait_touch = True
	time.sleep(3)

	if faceFound:
		return

	controller.SetServo(1, Xcoor, int(config["servoSpeed"]))
	time.sleep(0.1)
	controller.SetServo(2, Ycoor, int(config["servoSpeed"]))
	time.sleep(1)
	touch_tm = time.time()
	mutex_wait_touch = False

	return

def StartHotwordListener():
	global threaded_detector
	if interactiveTypeGAssistant == False:
		threaded_detector = ThreadedDetector("/opt/qbo/voicemodels/Hi_QBO.pmdl", sensitivity=0.4, audio_gain=1)
		threaded_detector.start()
		threaded_detector.start_recog(detected_callback=HotwordListenedEvent)

def StopHotwordListener():
	global threaded_detector
	if interactiveTypeGAssistant == False:
		threaded_detector.terminate()

def DialogflowV2SeeFace():
	talk.record_wav()
	talk.detect_intent_stream()

def HotwordListenedEvent():
	global HotwordListened
	HotwordListened = True


StartHotwordListener()

print (" Face tracking running.")
print (" QBO nose bright green when see your face")

Speak.SpeechText_2("I am ready.", "Estoy preparado.")

touch_tm = time.time()

fr_time = 0

while True:
	# print ("frame time: " + str(time.time() - fr_time))
	fr_time = time.time()

	faceFound = False  # This variable is set to true if, on THIS loop a face has already been found
	# We search for a face three diffrent ways, and if we have found one already-
	# there is no reason to keep looking.
	thread.start_new_thread(WaitForSpeech, ())
	#	WaitForSpeech()

	if HotwordListened:

		if Listening == False:

			if config["distro"] != "ibmwatson":
				controller.SetNoseColor(1)

			StopHotwordListener()

			if interactiveTypeGAssistant == True:
				gassistant.start_conversation_from_face()
			else:
				listen_thd = talk.StartBack()
				Listening = True

		HotwordListened = False

	if not faceFound:
		if lastface == 0 or lastface == 1:
			t_ini = time.time()

			while time.time() - t_ini < 0.01:  # wait for present frame
				t_ini = time.time()
				aframe = webcam.read()[1]

			# print ("t: " + str(time.time()-t_ini))
			fface = frontalface.detectMultiScale(aframe, 1.03, 4, (cv2.cv.CV_HAAR_DO_CANNY_PRUNING + cv2.cv.CV_HAAR_FIND_BIGGEST_OBJECT + cv2.cv.CV_HAAR_DO_ROUGH_SEARCH), (60, 60))

			if fface != ():  # if we found a frontal face...
				face_not_found_idx = 0
				lastface = 1  # set lastface 1 (so next loop we will only look for a frontface)
				for f in fface:  # f in fface is an array with a rectangle representing a face
					faceFound = True
					face = f

	if not faceFound:  # if we didnt find a face yet...
		if lastface == 0 or lastface == 2:  # only attempt it if we didn't find a face last loop or if-
			t_ini = time.time()

			while time.time() - t_ini < 0.01:  # wait for present frame
				t_ini = time.time()
				aframe = webcam.read()[1]

			# print ("tp: " + str(time.time()-t_ini))
			pfacer = profileface.detectMultiScale(aframe, 1.03, 4, (cv2.cv.CV_HAAR_DO_CANNY_PRUNING + cv2.cv.CV_HAAR_FIND_BIGGEST_OBJECT + cv2.cv.CV_HAAR_DO_ROUGH_SEARCH), (80, 80))

			if pfacer != ():  # if we found a profile face...
				face_not_found_idx = 0
				lastface = 2
				for f in pfacer:
					faceFound = True
					face = f

	if not faceFound:  # if no face was found...-

		face_not_found_idx += 1
		print ("No face " + str(face_not_found_idx))

		if face_not_found_idx > 5:
			face_not_found_idx = 0
			lastface = 0  # the next loop needs to know
			face = [0, 0, 0, 0]  # so that it doesn't think the face is still where it was last loop

			if Facedet != 0:
				Facedet = 0
				no_face_tm = time.time()
				print ("No face, 5 times!")

			elif time.time() - no_face_tm > 10:
				ServoHome()
				Cface[0] = [0, 0]
				print ("No face, > 10 times!......")
				no_face_tm = time.time()

	else:

		last_face_det_tm = time.time()
		x, y, w, h = face

		Cface = [(w / 2 + x), (h / 2 + y)]  # we are given an x,y corner point and a width and height, we need the center
		#print ("face ccord: " + str(Cface[0]) + "," + str(Cface[1]))

		if Facedet == 0:
			if Listening == False:
			Facedet = 1
			face_det_tm = time.time()

		elif Listening == False & WaitingSpeech == False & (time.time() - face_det_tm > 2):
			face_det_tm = time.time()
			print ("face detected") # mio test

			if Listening == False:
				controller.SetNoseColor(1)

				listen_thd = talk.StartBack()
				print (" control refresh") # test mio
				Listening = True

		else:
			print ("control test") #test mio
			controller.SetNoseColor(4)

		if touch_det == False:

			faceOffset_X = 160 - Cface[0]

			if (faceOffset_X > 20) | (faceOffset_X < -20):

				time.sleep(0.002)
				controller.SetAngleRelative(1, faceOffset_X >> 1)
				# wait for move
				time.sleep(0.05)

			# print ("MOVE REL X: " + str(faceOffset_X >> 1))
			faceOffset_Y = Cface[1] - 120

			if (faceOffset_Y > 20) | (faceOffset_Y < -20):
				time.sleep(0.002)
				controller.SetAngleRelative(2, faceOffset_Y >> 1)
				# wait for move
				time.sleep(0.05)

				#print ("MOVE REL Y: " + str(faceOffset_Y >> 1))

	if (time.time() - touch_samp > 0.5):  # & (time.time() - last_face_det_tm > 3):
		touch_samp = time.time()
		last_face_det_tm = time.time()
		#print ("getHeadCmd()")
		qbo_touch = controller.GetHeadCmd("GET_TOUCH", 0)
		time.sleep(0.002)

		if touch_tm == 0 and qbo_touch:

			if qbo_touch == [1]:
				controller.SetServo(1, Xmax - 25, int(config["servoSpeed"]))
				time.sleep(0.002)
				controller.SetServo(2, Ymin - 5, int(config["servoSpeed"]))
				thread.start_new_thread(WaitTouchMove, ())
				# wait for begin touch move.
				time.sleep(1)

			elif qbo_touch == [2]:
				time.sleep(0.002)
				controller.SetServo(2, Ymin - 5, int(config["servoSpeed"]))
				thread.start_new_thread(WaitTouchMove, ())
				# wait for begin touch move.
				time.sleep(1)

			elif qbo_touch == [3]:
				controller.SetServo(1, Xmin + 25, int(config["servoSpeed"]))
				time.sleep(0.002)
				controller.SetServo(2, Ymin - 5, int(config["servoSpeed"]))
				thread.start_new_thread(WaitTouchMove, ())
				# wait for begin touch move.
				time.sleep(1)

	if touch_tm != 0 and time.time() - touch_tm > touch_wait:
		print ("touch ready")
		touch_tm = 0


StopHotwordListener()
