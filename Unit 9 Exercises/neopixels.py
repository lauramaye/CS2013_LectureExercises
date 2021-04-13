# import circuit playground express board
from adafruit_circuitplayground import cp
import time

class NeoPixels:

    def __init__(self):
        self.pixel_amount = 10
        self.pixels_off_state = [0, 0, 0]  # pixels are turned off if black.
        self.count = 0
        self.pixel_amount = len(cp.pixels)
        cp.pixels.brightness = 0.1
        cp.pixels.auto_write = False

    def every_second_pixel(self, color):
        for pixel in range(0, self.pixel_amount):
            if pixel % 2 == 0:
                cp.pixels[pixel] = color # pixels positions range from 0 - 9
            else:
                cp.pixels[pixel] = self.pixels_off_state
        cp.pixels.show()



# code to keep running forever
while True:
    pass
