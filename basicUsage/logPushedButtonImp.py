from datetime import datetime
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)

def button_pushed(arg):
	now = str(datetime.now())
	if GPIO.input(arg) == 1:
		print 'Boton presionado'
		log.write('Button pressed at ' + now + "\n")
	else:
		print 'Boton liberado'
		log.write('Button released at ' + now + "\n")

log = open("logPushedButtonImp.txt", "w")
try:
	GPIO.add_event_detect(16, GPIO.BOTH, callback=button_pushed, bouncetime=200)
	while True:
		#ME HAGO WHILE
		pass
except KeyboardInterrupt:
    pass
GPIO.cleanup()
log.flush()
log.close()