import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

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
   
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
