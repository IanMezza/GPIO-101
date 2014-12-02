GPIO-101
========

Código básico para comenzar a trabajar con el GPIO del Raspberry Pi y Python.

## Librería utilizada

* RPi.GPIO

### Nota
Para todos los códigos, se utiliza la numeración de los pines del GPIO tal como vienen dispuestos en el Raspberry Pi y no la definición del Broadcom

## blink.py y button.py
El diagrama de conexión correspondiente a éstos programas, es el siguiente.

<img src="https://github.com/IanMezza/GPIO-101/blob/master/assets/blink_button_bb.png">

Hay que tener en cuenta que para conectar un botón a cualquiera de los puertos, éste debe estar conectado a 3.3V pues el GPIO no es tolerante a entradas de voltaje superior.

