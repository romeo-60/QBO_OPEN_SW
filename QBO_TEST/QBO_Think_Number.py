#!/usr/bin/python3
#QBO_think_numbers
#expression led mouth
import os
import errno
import serial
import sys
import time
import QboCmd

port = '/dev/serial0'


number_led = {0:0xE0A0A0E, 1: 0xC040404, 2: 0x602040F, 3: 0xE02041C, 4: 0x40C1E04, 5: 0x704020C, 
6: 0x3040A0E, 7: 0xE020408, 8: 0x40A040A, 9: 0xE0A0418}
for k, v in number_led.items():
    print('number  ', k," ", 'dec_code_expression ', v)
#----
try:

	print(port)

	# Open serial port
	ser = serial.Serial(port, baudrate=115200, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE, rtscts=False, dsrdtr=False, timeout=0)

	print ("Open serial port sucessfully.")
	print(ser.name)

	QBO = QboCmd.Controller(ser)
	
except:
	print ("Error opening serial port.")
	sys.exit()

def WaitForTouch():
	global number_led	
	touch = QBO.GetHeadCmd("GET_TOUCH", 0)

	if touch:
			
		if touch == [2]:
			print("number_expression_led")
			print("Cyan Nose")
			QBO.SetNoseColor(5)
			time.sleep(1)
			matrix_led = 0
            
			for k, v in number_led.items():
				matrix_led = v
				print('number  ', k, ' ', 'matrix_led', matrix_led)
				QBO.SetMouth(matrix_led) #
				#Pause
				time.sleep(0.5)
			print("Switch off")
			QBO.SetNoseColor(0)
			time.sleep(1)
			QBO.SetMouth(0)
			matrix_led = 0
			
		
	
	touch = 0
	matrix_led = 0

while True:
    WaitForTouch()
