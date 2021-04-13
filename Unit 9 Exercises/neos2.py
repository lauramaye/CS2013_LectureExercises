# import circuit playground express board
from adafruit_circuitplayground import cp
import time, random, math

class NeoPixels:

    def __init__(self):
        self.pixels_off_state = [0, 0, 0]  # pixels are turned off if black.
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


    # lights up half of the board in a pattern
    def half_pattern(self, colour):
        cp.pixels.fill(self.pixels_off_state)
        cp.pixels.show()
        for pixel in range(0, self.pixel_amount//2):
            cp.pixels[pixel] = colour
            cp.pixels[(self.pixel_amount - 1) - pixel] = colour
            cp.pixels.show()
            time.sleep(0.5)
            print("hello")
        cp.pixels.fill([0, 0, 0])
        cp.pixels.show()
        time.sleep(0.5)


    def half_light(self, side, colour):
        #cp.pixels.fill(self.pixels_off_state)
        #cp.pixels.show()
        if side == 1:
            cp.pixels[0:5] = [colour] * 5
            cp.pixels[5:] = [self.pixels_off_state] * 5
        elif side == 0:
            cp.pixels[0:5] = [self.pixels_off_state] * 5
            cp.pixels[5:] = [colour] * 5
        cp.pixels.show()

    # random light - OK if one from same position appears
    def random_light(self, colour):
        cp.pixels.fill(self.pixels_off_state)
        cp.pixels.show()
        cp.pixels[random.randint(0, self.pixel_amount -1)] = colour
        cp.pixels.show()
        time.sleep(0.5)

    def loading_light(self, background_colour, loading_colour):
        cp.pixels.fill(self.pixels_off_state)
        cp.pixels.show()
        cp.pixels.fill(background_colour)
        for i in range(self.pixel_amount):
            cp.pixels[i] = loading_colour
            cp.pixels.show()
            time.sleep(0.3)
            cp.pixels.fill(background_colour)



class SensorControlledPixels(NeoPixels):

        def half_light(self, x_acc, colour):
           # cp.pixels.fill(self.pixels_off_state)
          #  cp.pixels.show()
            if not (x_acc > 9.81 or x_acc < -9.81):
                if x_acc < -3:
                    super().half_light(0, colour)
                elif x_acc > 3:
                    super().half_light(1, colour)
                else:
                    print("test")
                    cp.pixels.fill([0, 0, 0])
                    cp.pixels.show()


        def displaylights_x(self, acceleration_x, colour):
            #cp.pixels.fill(self.pixels_off_state)
            #cp.pixels.show()
            if math.fabs(acceleration_x) > 9.81:
                return

            pixel_peak = 0

            highest_acceleration_value = 9.81


            if acceleration_x > 2:
                pixel_peak = int(acceleration_x * 5 / highest_acceleration_value)
                highest_pixel_location = 5
                for i in range(self.pixel_amount):
                    if i <= pixel_peak:
                        cp.pixels[(highest_pixel_location - 1) - i] = colour
                    else:
                        cp.pixels[(highest_pixel_location - 1) - i] = self.pixels_off_state
            elif acceleration_x < - 2:
                flipped_acceleration_x = acceleration_x * -1

                pixel_start = self.pixel_amount // 2
                pixel_peak = pixel_start + (int(flipped_acceleration_x * 5 / highest_acceleration_value))
                print(pixel_start, pixel_peak)
                for i in range(pixel_start, self.pixel_amount):
                    if i <= pixel_peak:
                        cp.pixels[i] = colour
                    else:
                        cp.pixels[i] = self.pixels_off_state
            else:
                cp.pixels.fill(self.pixels_off_state)


            cp.pixels.show()


        def tiltcolour_y(self, acceleration_y):
          #  cp.pixels.fill(self.pixels_off_state)
          #  cp.pixels.show()
            blue = 0
            green = 0
            red = 0
            highest_acceleration_value = 9.81
            absolute_acceleration = math.fabs(acceleration_y) # converting the input to a positive number
            if math.fabs(acceleration_y) < highest_acceleration_value:
                blue = int((absolute_acceleration * 255) / highest_acceleration_value)
                print(blue)
            color = [red, green, blue]
            print(color)
            cp.pixels.fill(color)
            cp.pixels.show()



# code to keep running forever
neopixel_1 = NeoPixels()
sens_neopix = SensorControlledPixels()
while True:
    x,y = cp.acceleration[0:2]
    sens_neopix.displaylights_x(x, [0, 255, 255])
'''
    if cp.switch:
        neopixel_1.half_pattern()
        neopixel_1.half_light(0, [255, 0, 100])
        time.sleep(0.3)
        neopixel_1.random_light([255, 100, 0])
        sens_neopix.loading_light([0, 255, 255], [255, 0, 255])
    else:
        sens_neopix.half_light(x, [255, 255, 0])
        time.sleep(0.5)
        sens_neopix.tiltcolour_y(y)
        time.sleep(0.5)
        sens_neopix.displaylights_x(x, [0, 255, 255])
    #sens_neopix.tilt_feedback_x(x, [0, 255, 255])
    #sens_neopix.loading_light([0, 255, 255], [0, 0, 255])
    #sens_neopix.tiltcolour_y(y)
    time.sleep(0.1)
'''