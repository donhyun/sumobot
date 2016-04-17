import RPi.GPIO as GPIO
import time
#servo controller function

def move(pin):
    GPIO.output(pin, GPIO.HIGH) #Create a 5V pulse for 13ms
    time.sleep(.0013)
    GPIO.output(pin, GPIO.LOW) #Wait for 20ms at 0V
    time.sleep(.02)
    return

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channel
GPIO.setup(32, GPIO.OUT)

# move servo 100 times
for i in range(0,100):
    print i
    move(32)

GPIO.cleanup()