### Author: Robert Kaye
### Description: On board LED test 
### Category: Other
### License: MIT
### Appname: LED test
### Built-in: hide
import machine

# open the PB13 pin. The NeoPixel is not on X2 as shown on the diagrams.
pin = machine.Pin("PB13", machine.Pin.OUT)

# create a NeoPixel driver object
neo = pyb.Neopix(pin)

# Set up two colors
colors = [0xFF7700, 0xFF00FF]

# Loop over both colors for 500ms each
while True:
    for color in colors:
        neo.display(color)
        pyb.delay(500)
