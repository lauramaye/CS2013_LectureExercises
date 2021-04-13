# --- create class here and then move to new file
from adafruit_circuitplayground import cp
import time

class NeoPixels:

    # set class variables
    pixels_off_state = [0, 0, 0]

    def __init__(self):
        # set instance variables here
        self.pixels_amount = len(cp.pixels)
        self.halfway_point = self.pixels_amount // 2
        cp.pixels.brightness = 0.1
        print(NeoPixels.pixels_off_state)

    def flash(self, colour):
        cp.pixels.fill(colour)
        time.sleep(0.5)
        cp.pixels.fill(NeoPixels.pixels_off_state)
        time.sleep(0.5)

    def alternate_colour(self, colour_1, colour_2):
        for pixel in range(self.halfway_point):
            if pixel % 2 == 0:
                cp.pixels[pixel] = colour_1
            else:
                cp.pixels[pixel] = colour_2
            time.sleep(0.5)
            cp.pixels[pixel] = NeoPixels.pixels_off_state
