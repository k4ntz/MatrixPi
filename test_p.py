# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
from letters import letters_dict

def blackout(width=32, height=8):
	return [[[0, 0, 0] for i in range(width)] for l in range(height)]

def write_image(image):
	for l, line in enumerate(image):
		for c, pix in enumerate(line):
			if l % 2 == 0:
				pixels[l * width + c] = pix
			else:
				pixels[(l+1) * width - (c + 1)] = pix
	pixels.show()
	time.sleep(1)

def insert_letter(base_image, letter, color, x=0, y=0):
	for l, line in enumerate(letter):
		for c, col in enumerate(line):
			if letter[l][c]:
				base_image[y+l][x+c] = color

def write_word(word, x=0):
	image = blackout()
	for i, lett in enumerate(word):
		lett_matrix = letters_dict[lett]
		insert_letter(image, lett_matrix, (0, 0, 255), x, 2)
		x += len(lett_matrix[0]) + 1
	return image

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
width = 32
height = 8
num_pixels = width * height

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)



if __name__ == '__main__':
	image = write_word("QUENTIN", x=1)
	write_image(image)
