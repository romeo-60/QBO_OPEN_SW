#!/usr/bin/env python3
# -*- coding: latin-1 -*-
#--- software modified by Romeo Ceccato ---

import os
import errno
import time
from assistants.QboTalk import QBOtalk

FIFO_listen = '/opt/qbo/pipes/pipe_listen'
FIFO_cmd = '/opt/qbo/pipes/pipe_cmd'

talk = QBOtalk()
Listening = True
listen_thd = 0


def WaitForSpeech():

	global Listening, listen_thd, FIFO_listen, FIFO_cmd
	print("WaitForSpeech started") #mio test
	if Listening == False:
		return

	elif talk.GetAudio == True:

		fifo = os.open(FIFO_cmd, os.O_WRONLY)
		os.write(fifo, "-c nose -co red")
		os.close(fifo)

		listen_thd(wait_for_stop=True)
		print("Something has arrived at WaitForSpeech: " + talk.strAudio)
		print("???????") #mio test
		fifo = os.open(FIFO_listen, os.O_WRONLY)
		os.write(fifo, talk.strAudio)
		os.close(fifo)

	return


try:
	os.mkfifo(FIFO_listen)
except OSError as oe:
	if oe.errno != errno.EEXIST:
		print("exit1", oe.errno)
		raise

try:
	os.mkfifo(FIFO_cmd)
except OSError as oe:	
	if oe.errno != errno.EEXIST:
		print("exit2", oe.errno)
		raise

listen_thd = talk.StartBackListen()

fifo = os.open(FIFO_cmd, os.O_WRONLY)

os.write(fifo, "-c nose -co green")

os.close(fifo)

while True:

	WaitForSpeech()
	
	if talk.GetAudio == True:
		print("statrt_listen")
		fifo = os.open(FIFO_cmd, os.O_WRONLY)
		os.write(fifo, "-c nose -co red")
		os.close(fifo)

		time.sleep(1)

		print("StartBackListen")

		try:
			listen_thd = talk.StartBackListen()
			fifo = os.open(FIFO_cmd, os.O_WRONLY)
			os.write(fifo, "-c nose -co green")
			os.close(fifo)
			talk.GetAudio = False

		except:
			print("StartBackListen EXCEPTION")
