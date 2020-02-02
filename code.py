import board
import digitalio
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)
pixels[0] = (0, 0, 255)
pixels[1] = (255, 0, 127)
pixels[2] = (255, 255, 255)
pixels[3] = (255, 0, 127)
pixels[4] = (0, 0, 255)
pixels[5] = (0, 0, 255)
pixels[6] = (255, 0, 127)
pixels[7] = (255, 255, 127)
pixels[8] = (255, 0, 127)
pixels[9] = (0, 0, 255)
pixels.show()