'''importing lib'''
import RPi.GPIO as GPIO
#making RPI as GPIO
import time
#allowing time to wait
import os
#importing operating system functions

'''setting up breadboard and button'''
GPIO.setmode(GPIO.BOARD)
#setting breadboard
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#button set as input
GPIO.setup(12, GPIO.OUT) #green
GPIO.setup(13, GPIO.OUT) #yellow
GPIO.setup(15, GPIO.OUT) #red

'''getting temp'''
os.system ("sudo modprobe w1-gpio")
os.system ("sudo modprobe w1-therm")
tfile = open("/sys/bus/w1/devices/idNumberFromTemp/w1_slave")
theNumber = 0
#var theNumber has value of 0

'''Defining functions and procedures'''
'''turnOnGreen'''
def turnOnGreen():
#defining var called turnOnGreen
	GPIO.output (12, True)
	#turn green light on

'''turnOfffGreen'''
def turnOffGreen():
#defining var called turnOffGreen
	GPIO.output (12, False)
	#turn green light off

'''turnOnYellow'''	
def turnOnYellow():
#defining var called turnOnYellow
	GPIO.output (13, True)
	#turn red light on

'''turnOffRed'''
def turnOffYellow():
#defining var called turnOffYellow
	GPIO.output (13, False)
	#turn red light off
	
'''turnOnRed'''	
def turnOnRed():
#defining var called turnOnRed
	GPIO.output (15, True)
	#turn red light on

'''turnOffRed'''
def turnOffRed():
#defining var called turnOffRed
	GPIO.output (15, False)
	#turn red light off

'''turnOnePicture'''
def takePicture ():
#defining var called takePicture
	os.system ("raspistill –o picture.jpg")
	#take one picture

'''TakeVideo'''
def takeVideo ():
#defining var called takeVideo
	os.system ("raspivid -o vid.h264 vid"+str(thenumber)+".mp4")
	#take video

'''setting up program'''
while True:
    time.sleep (0.5)
	#sleep
    print ("Program Ready")
	#printing to screen

    if (GPIO.input(11)==False):
	#if 11 light is false
        print ("Button Pressed")
		#print to screen
        break
		#end
time.sleep(2)
#sleep

'''Start of main program'''
while True:
    print ("Main Program Running")
	#print to screen
	turnOnGreen()
	#run proc
	
	'''Moved to top'''
	'''
	#getting temp
	os.system ("sudo modprobe w1-gpio")
	os.system ("sudo modprobe w1-therm")
	tfile = open("/sys/bus/w1/devices/ENTERIDNUMBER/w1_slave")
	theNumber = 0
	#var theNumber has value of 0
	'''
	
	'''printing temp'''
	datafile = open("tempdata.log","a")
	#datafile has value of tempdata.log
	text=tfile.read()
	#text has value of tfile
	tfile.close
	#close tfile
	secondline = text.split("\n") [1]
	#this line is being used to store the information from the second line of the temperature sensor. 
	temperaturedata = secondline.split (" ") [9]
	#this is picking out the 9th number on the second row from the temperaturedata file from the previous line 
	temperature = float(temperaturedata[2:])
	#this is telling the program to use the temperature variable as a float for a more accurate reading
	temperature = temperature / 1000
	# this is dividing the temperature data recorded by 1000
	
	'''printing temp, add theNumber and save temp log'''
	datafile.write(str(temperature) + “\n”)
	#this is making the program record the data 
	datafile.close
	#closing datafile
	print (temperature)
	#this is so the user will be able to physically see what the temperature is
	theNumber = theNumber + 1
	#the number has the value of itself add 1
	
	'''creating conditinal statements'''
		
		'''taking single pick'''
		if(temperature >= 22) and (temperature <23.99):
		#if temp is greater then 22 and less then 23.99
			#run proc
			turnOnGreen():
			turnOnYellow():
			turnOffRed():
			takePicture():
		
		'''taking multi pick'''
		elif(temperature >= 24):
		#if temp is equal or greater than 24
			#run proc
			turnOnGreen():
			turnOnRed():
			takeVideo():
			time.sleep(5):
		
		
		'''above fail'''
		else:
		#if above critiria is not meet
			turnOffGreen():
			turnOffRed():
			turnOffYellow():
			time.sleep(5):
	
	''' End program '''
    if (GPIO.input(11)==False):
	#if equal false
        print ("Button Pressed")
		#print
        print("Program Ended")
		#print
		turnOffGreen()
		#run proc
        break
	
'''end of program'''