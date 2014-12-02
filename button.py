import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)
count = 0
try:
	while True:
		inputValue = GPIO.input(16)
		if (inputValue == True):
			count = count + 1
			print("Button pressed " + str(count) + " times.")
			time.sleep(.3)
		time.sleep(0.25)
except KeyboardInterrupt:
	pass
GPIO.cleanup()