# import circuit playground express board
from adafruit_circuitplayground import cp
import time
from neopixels import NeoPixels


# ---------------------------------- -----

blue = [0, 0, 255]
red = [255, 0, 0]
magenta = [255, 0, 255]

neopixels_1 = NeoPixels()

# ----- loop forever
while True:

    print(cp.switch)

    # ---- pattern 1: flash
    if cp.switch == True:
        neopixels_1.flash(blue)

    # ---- pattern 2: alternate_colour
    else:
        neopixels_1.alternate_colour(red, magenta)
