import RPi.GPIO as GPIO
import time

# This function is to blink the LED.
def blink(pin):  
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(.2)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(.2)  


# ---------------   MAIN PROGRAM     ----------------------
# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BOARD)  

# LED
led = 37
GPIO.setup(led, GPIO.OUT) 

# set up GPIO switch channel 
sw = 33
GPIO.setup(sw, GPIO.IN)

go = False

while True:
	print go
	if GPIO.input(sw)==1:
		if go==False:
			go = True
		else:
			go = False	
		
		time.sleep(1)

	if go == False:
        # If the sumobot is in standby mode, then blink the LED.
		blink(led)
	else:
        # If it is go time, then keep the LED lit up.
		GPIO.output(led,GPIO.HIGH)
        # If the line detectors detects white, then backup left or backup right.
        # Check the proximity sensor to see if the opponent is in front.
		 