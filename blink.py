import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

try:
	while True:
		GPIO.output(18, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(18, GPIO.LOW)
		time.sleep(1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()