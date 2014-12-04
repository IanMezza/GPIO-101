import RPi.GPIO as GPIO
from flask import Flask, render_template, request
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

app = Flask(__name__)


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pins = {
   23 : {'name' : 'Lampara', 'state' : GPIO.LOW}
   }

for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   templateData = {
      'pins' : pins
      }
   return render_template('index.html', **templateData)
   
@app.route("/<changePin>/<action>")
def action(changePin, action):
   changePin = int(changePin)
   deviceName = pins[changePin]['name']
   if action == "on":
      GPIO.output(changePin, GPIO.HIGH)
      message = deviceName + " encendida."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = deviceName + " apagada."
      
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   templateData = {
      'message' : message, 
      'pins' : pins
   }

   return render_template('index.html', **templateData)

@app.route("/adc")
def adc():
   a0 = GPIO.input(7)  ^ 1
   
   a1 = GPIO.input(11) ^ 1
   
   a2 = GPIO.input(12) ^ 1

   a3 = GPIO.input(13) ^ 1

   a4 = GPIO.input(15) ^ 1

   a5 = GPIO.input(16) ^ 1

   a6 = GPIO.input(18) ^ 1

   a7 = GPIO.input(22) ^ 1
   
   cadena_binaria = str(a7) + str(a6) + str(a5) + str(a4) + str(a3) +str(a2) + str(a1) + str(a0)

   lectura = int(cadena_binaria, 2) * 100 / 255

   templateData = {
   'adc' : str(lectura)
   }

   return str(lectura) #render_template('index.html', **templateData)



   
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)