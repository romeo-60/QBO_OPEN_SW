#!/usr/bin/env python3
#FACE DETECT


import cv2 as cv
import numpy
import time

#import sys
print("cv2 verison=",cv.__version__)
# versione 1
#faceCascade = cv.CascadeClassifier("/usr/local/lib/python3.7/dist-packages/cv2/data/haarcascade_frontalface_alt2.xml")
# versione 2
#faceCascade = cv.CascadeClassifier("/home/pi/.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
#versione 3 
#faceCascade = cv.CascadeClassifier("haarcascade_frontalface_alt2.xml")

i = 0
counter = 0
video_capture = cv.VideoCapture(0)

#set Frame resolution
video_capture.set(cv.CAP_PROP_FRAME_WIDTH, 320)
video_capture.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
print ("Frame resolution set to: (" + str(video_capture.get(cv.CAP_PROP_FRAME_WIDTH)) + "; ")

while True:
    i+=1
    print("i",i)
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame',gray)
    cv.imwrite('Initial_img_gray.jpg',gray)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.03,
        minNeighbors=1,
        minSize=(60, 60),
    #    #flags=cv2.cv.CV_HAAR_SCALE_IMAGE #da verificare
    )
    print ("FACES",faces)
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        xc=int(x+w/2)
        yc=int(y+h/2)
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #faces = () # solo per test    
    # Display the resulting frame
    if faces != ():
        counter+=1
        print ("center x", xc, " center y",yc)
        cv.putText(frame, "Cont: {}".format(counter), (10, 20),
            cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        #----------
        cv.circle(frame, (xc,yc), radius=1, color=(0, 0, 255), thickness=-1)
        cv.putText(frame, "x: {}".format(xc), (10, 40),
            cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv.putText(frame, "v: {}".format(yc), (10, 60),
            cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        #-------------
            
            
        cv.imwrite('img_gray.jpg',gray)
        cv.imwrite('FaceTest.jpg',frame)
        
        print("FACE counter",counter)
    else:
        print("no face")
    
    #print("contatore",counter)
    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv.destroyAllWindows()
