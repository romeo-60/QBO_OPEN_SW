import serial
import time
import sys
#import QboCmd
import QboCmd_test_base_v3

port = '/dev/serial0'

# Open serial port


print(port)

# Open serial port
ser = serial.Serial(port, baudrate=115200, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE, rtscts=False, dsrdtr=False, timeout=0)

print ("Open serial port sucessfully.")
print(ser.name)

#QBO = QboCmd.Controller(ser)
QBO = QboCmd_test_base_v3.Controller(ser)   


print("Blue Nose")
QBO.SetNoseColor(1) 
time.sleep(1)

print("Right Positon")
#Move the head to the right
QBO.SetServo(1,290, 100)#Axis,Angle,Speed
#pause
time.sleep(1)

print("Left position fast")
#Move the head to the left
QBO.SetServo(1,725, 100)#Axis,Angle,Speed
#Pause
time.sleep(1)

print("Up Positon")
#Set a start position 
QBO.SetServo(2,400, 100)#Axis,Angle,Speed
#Pause
time.sleep(5)

print("Down Position")
QBO.SetServo(2,550,100)#Axis,Angle,Speed
time.sleep(1)

print("Smile")
QBO.SetMouth(0x110E00) #happy
time.sleep(1)

print("Center head")
QBO.SetServo(1,511, 100)#Axis,Angle,Speed
#Pause
time.sleep(2)

print("Switch off")
QBO.SetNoseColor(0)
time.sleep(1)
QBO.SetMouth(0)
time.sleep(1)