import RPi.GPIO as GPIO 
import time

# blinking function 
def blink(pin): 
    GPIO.output(pin,GPIO.HIGH) 
    time.sleep(1) 
    GPIO.output(pin,GPIO.LOW) 
    time.sleep(1) 
    return

# to use Raspberry Pi board pin numbers 
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channel 
GPIO.setup(37, GPIO.OUT)
# blink 10 times 
for i in range(0,10):
    print i
    blink(37)

GPIO.cleanup()