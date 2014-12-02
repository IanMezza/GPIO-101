import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(22, GPIO.IN)

bin = "0b"
cadena_binaria = "0"
decimal = "0"
try:
	while True:
		a0 = GPIO.input(7) ^ 1
		
		a1 = GPIO.input(11) ^ 1
		
		a2 = GPIO.input(12) ^ 1

		a3 = GPIO.input(13) ^ 1

		a4 = GPIO.input(15) ^ 1

		a5 = GPIO.input(16) ^ 1

		a6 = GPIO.input(18) ^ 1

		a7 = GPIO.input(22) ^ 1
		
		time.sleep(.1) 

		cadena_binaria = str(a7) + str(a6) + str(a5) + str(a4) + str(a3) +str(a2) + str(a1) + str(a0)

		print "La combinacion binara es " + cadena_binaria

		print "El valor decimal de la cadena binaria es " + str(int(cadena_binaria, 2))


except KeyboardInterrupt:
	pass
GPIO.cleanup()