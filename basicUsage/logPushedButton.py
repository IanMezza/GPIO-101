from datetime import datetime
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)

i = 0

log = open("log.txt", "w")
try:
	while i in range(5):
	        now = str(datetime.now())
	        inputValue = GPIO.input(16)
	        if (inputValue == True):
	        	print 'Button pressed'
		        log.write(now + " " + 'Button pressed' + "\n")
		        sleep(.3)
	        sleep(.9)
except KeyboardInterrupt:
    pass
log.flush()
log.close()
GPIO.cleanup()