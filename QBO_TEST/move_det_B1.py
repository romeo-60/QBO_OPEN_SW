#!/usr/bin/env python3
# -*- coding: latin-1 -*-
# import the necessary packages
# -----------------------------
import numpy as np
from imutils.video import VideoStream
import datetime
import imutils
import time
import cv2
import QboCmd
import serial
# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'XVID')
video_reg = cv2.VideoWriter('video_reg'+ str(datetime.datetime.now())+'.avi',fourcc, 20.0, (640,480))
#-------------------
port = '/dev/serial0'
# Open serial port
ser = serial.Serial(port, baudrate=115200, bytesize = serial.EIGHTBITS, stopbits = serial.STOPBITS_ONE, parity = serial.PARITY_NONE, rtscts = False, dsrdtr =False, timeout = 0)
print "Open serial port sucessfully."
print(ser.name)
QBO = QboCmd.Controller(ser)
#----------------
print("Blue Nose")
QBO.SetNoseColor(1) 
time.sleep(1)
print("Center head")
QBO.SetServo(1,500, 100)#Axis,Angle,Speed
#Pause
time.sleep(1)
print("Down Position")
QBO.SetServo(2,530,100)#Axis,Angle,Speed
time.sleep(1)
#------------------
ir=0
detected = ''
no_move_tm = time.time()
reg_tm =time.time()
vs = VideoStream(src=0).start()
time.sleep(1.0)
# initialize the first frame in the video stream
firstFrame = None
#----------------
# loop over the frames of the video
while True:
	#global detected
	# grab the current frame and initialize the occupied/unoccupied
	# text
	frame = vs.read()
	rframe =vs.read()
        #----------------
	text = "Unoccupied"
	detected = False
	# if the frame could not be grabbed, then we have reached the end
	# of the video
	if frame is None:
		break
	# resize the frame, convert it to grayscale, and blur it
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue
	# compute the absolute difference between the current frame and
	# first frame
	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	#print("cnts",cnts)
	# loop over the contours
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < 2500 :        #args["min_area"]:
			continue
		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Occupied"
		detected = True		
	# draw the text and timestamp on the frame
	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)	
	
	if detected==True:		
		#print("Smile")
		QBO.SetMouth(0x110E00) #happy
		# write the frame	
	else:
		QBO.SetMouth(0) #no_Led
		
	if detected == True:
		ir+=1
		cv2.putText(rframe, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
			(10, rframe.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
		cv2.putText(rframe, "Cont: {}".format(ir), (10, 50),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)			
		cv2.putText(rframe, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, rframe.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)	
		video_reg.write(rframe)
		cv2.imshow("Security Registration", rframe) #test
		if (time.time() - reg_tm > 100):
			print("reset reg_time")	
			#video_reg.release() da attivare con modifica al titolo del video inserendo il data.time
			#cv2.destroyAllWindows() #test
			reg_tm = time.time()
			detected =False 
			QBO.SetMouth(0) #no_Led	
		
	if (time.time() - no_move_tm > 100):
		print("reset_fFrame ")
		no_move_tm = time.time()
		firstFrame = None
			
	# show the frame and record if the user presses a key
	
	cv2.imshow("Security Feed", frame)
	#cv2.imshow("Thresh", thresh)
	#cv2.imshow("Frame Delta", frameDelta)	
	#print("delta_t",time.time() - no_move_tm )
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key is pressed, break from the lop
	if key == ord("q"):
		break
# cleanup the camera and close any open windows
vs.stop()
cv2.destroyAllWindows()	
QBO.SetNoseColor(0)
time.sleep(1)
QBO.SetMouth(0)
video_reg.release() 	
		
