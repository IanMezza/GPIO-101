import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)

try:
	while True:
		GPIO.output(15, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(15, GPIO.LOW)
		time.sleep(1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()