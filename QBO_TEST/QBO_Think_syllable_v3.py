#!/usr/bin/python3
#QBO_think_syllable
#expression led mouth
import os
import errno
import serial
import sys
import time
import QboCmd_test_base_v3
#import QboCmd
port = '/dev/serial0'


syllable_led = {
'A': 0x40A1511, 'B': 0x80E0A0C, 'C': 0xC08080C, 'D': 0x20E0A06, 'E': 0xC0A0C0E,
'F': 0xE0C0808, 'G': 0xE080A0E, 'H': 0xA0A0E0A, 'I': 0x4000404, 'J': 0x404140C,
'K': 0xA0C0C0A, 'L': 0x808080C, 'M': 0x1B151111, 'N': 0x121A1612, 'O': 0x40A0A04,
'P': 0xE0A0C08, 'Q': 0xE0A0602, 'R': 0xE0A0C0A, 'S': 0x605140C, 'T': 0xE040404,
'U': 0xA0A0A0E, 'V': 0x11110A04, 'W': 0x11150A04, 'X': 0x110A0E11, 'Y': 0xA040404,
'Z': 0xF020C1F}
for k, v in syllable_led.items():
    print('syllable  ', k," ", 'dec_code_expression ', v)
#----
try:

    print(port)

    # Open serial port
    ser = serial.Serial(port, baudrate=115200, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE, rtscts=False, dsrdtr=False, timeout=0)

    print ("Open serial port sucessfully.")
    print(ser.name)

    #QBO = QboCmd.Controller(ser)
    QBO = QboCmd_test_base_v3.Controller(ser)
except:
    print ("Error opening serial port.")
    sys.exit()

def WaitForTouch():
    global syllable_led
    touch = QBO.GetHeadCmd("GET_TOUCH", 0)

    if touch:

        if touch == [2]:
            print("number_expression_led")
            print("Cyan Nose")
            QBO.SetNoseColor(5)
            time.sleep(1)
            matrix_led = 0
            
            for k, v in syllable_led.items():
                matrix_led = v
                print('syllable  ', k, ' ', 'matrix_led', matrix_led)
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

