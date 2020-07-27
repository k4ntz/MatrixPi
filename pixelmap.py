import numpy as np
import time
import board
import neopixel
from letters import letters_dict
from colors import colors_dict
from icons import make_icon
from copy import deepcopy

class PixelScreen():
    def __init__(self, width=32, height=8):
        pixel_pin = board.D18

        # The number of NeoPixels
        self.width = width
        self.height = height
        self.num_pixels = width * height

        # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
        # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
        ORDER = neopixel.GRB

        self.pixels = neopixel.NeoPixel(
            pixel_pin, self.num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
        )

    def _show(self):
        self.pixels.show()

    def _load(self, image):
        if type(image) == Piximage:
            image = image.pixel_map
        for l, line in enumerate(image):
            for c, pix in enumerate(line):
                if l % 2 == 0:
                    self.pixels[l * self.width + c] = pix
                else:
                    self.pixels[(l+1) * self.width - (c + 1)] = pix

    def blackout(self):
        for i in range(self.num_pixels):
            self.pixels[i] = (0, 0, 0)
        self._show()

    def display_message(self, image, loop=False):
        if image.w <= self.width:
            self._load(image.pixel_map)
            self._show()
            time.sleep(3)
        else:
            new_im = Piximage() + image + Piximage()
            for epoch in range(10):
                for i in range(new_im.w):
                    self._load(new_im.pixel_map[:,i:i+32,:])
                    self._show()
                    time.sleep(0.02)
                time.sleep(1)

    def _anim(self, image_list, speed):
        for image in image_list:
            assert image.w <= self.width
            self._load(image.pixel_map)
            self._show()
            time.sleep(1./speed)

    def annimate(self, image_list, speed=5, loop=True):
        if loop:
            for _ in range(20):
                self._anim(image_list, speed)
        else:
            self._anim(image_list, speed)


class Piximage():
    def __init__(self, **kwargs):
        if "width" in kwargs.keys():
            self.w = kwargs["width"]
        else:
            self.w = 32
        if "height" in kwargs.keys():
            self.h = kwargs["height"]
        else:
            self.h = 8
        if "pixel_map" in kwargs.keys():
            if type(kwargs["pixel_map"]) == np.array:
                self.pixel_map = kwargs["pixel_map"]
            else:
                self.pixel_map = np.array(kwargs["pixel_map"])
            self.w = len(self.pixel_map[0])
            self.h = len(self.pixel_map)
        else:
            self.pixel_map = np.array([[[0, 0, 0] for i in range(self.w)] for l in range(self.h)])
        if "icon" in kwargs.keys():
            self.insert_icon(kwargs["icon"])


    def expand(self, w=None, h=None, inplace=True):
        assert w is not None or h is not None
        if w == None:
            w = self.w
        elif h == None:
            h = self.h
        assert not(w < self.w or h < self.h) # assert bigger image
        newpix_map = deepcopy(self.pixel_map)
        if w > self.w:
            newpix_map = np.concatenate((newpix_map, np.zeros((self.h, w - self.w, 3), dtype=np.int8)), axis = 1)
        if h > self.h:
            newpix_map = np.concatenate((newpix_map, np.zeros((h - self.h, h, 3), dtype=np.int8)), axis = 0)
        if inplace:
            self.pixel_map = newpix_map
            self.h = h
            self.w = w
        else:
            return Piximage(pixel_map=newpix_map)

    def empty(self, array):
        return not np.any(array)

    def insert_letter(self, letter, color, x=0, y=0):
        lett_matrix = letters_dict[letter]
        w, h = np.array(lett_matrix).shape
        if not self.empty(self.pixel_map[x:x+w, y:y+h]):
            print("You are writing on a non empty part")
        for l, line in enumerate(lett_matrix):
            for c, col in enumerate(line):
                if lett_matrix[l][c]:
                    self.pixel_map[y+l][x+c] = colors_dict[color]
        return x + len(lett_matrix[0])

    def insert_icon(self, icon_name, x=0, y=0):
        icon_matrix = make_icon(icon_name)
        w, h, d = np.array(icon_matrix).shape
        if not self.empty(self.pixel_map[x:x+w, y:y+h]):
            print("You are writing on a non empty part")
        for l, line in enumerate(icon_matrix):
            for c, col in enumerate(line):
                self.pixel_map[y+l][x+c] = col
        return x + len(icon_matrix[0])

    def _erase_end(self):
        """
        delete the last column if empty
        """
        for i in reversed(range(self.w)):
            if not self.pixel_map[:,i].any(): # only 0s.
                self.pixel_map = self.pixel_map[:,:i]
                self.w -= 1
            else:
                break

    def insert_letters(self, letters, color, x=0, y=0):
        for letter in letters:
            if x > self.w - 8:
                self.expand(w=self.w + 32)
            x = self.insert_letter(letter, color, x, y) + 1
        self._erase_end()


    def __add__(self, pixim2):
        if len(self.pixel_map) < len(pixim2.pixel_map):
            missing_lines = len(pixim2.pixel_map) - len(self.pixel_map)
            z = np.zeros((missing_lines, self.pixel_map.shape[1], 3))
            n_pixel_map = np.concatenate((np.concatenate((z, self.pixel_map), axis=0),
                                         pixim2.pixel_map),  axis=1)
        elif len(self.pixel_map) > len(pixim2.pixel_map):
            missing_lines = len(self.pixel_map) - len(pixim2.pixel_map)
            z = np.zeros((missing_lines, self.pixel_map.shape[1], 3))
            n_pixel_map = np.concatenate((self.pixel_map,
                                          np.concatenate((z, pixim2.pixel_map), axis=0)),
                                         axis=1)
        else: # equal height
            n_pixel_map = np.concatenate((self.pixel_map, pixim2.pixel_map), axis=1)
        return Piximage(pixel_map=n_pixel_map)

    def __repr__(self):
        repr = ""
        for line in self.pixel_map:
            repr += "|"
            for el in line:
                if el[0] == 0 and el[1] == 0 and el[2] == 0:
                    repr += " "
                else:
                    repr += "#"
            repr += "|\n"
        return repr


if __name__ == '__main__':
    # import ipdb; ipdb.set_trace()
    # pim.insert_letters("COUCOU PROUTI < !!!", "white")
    screen = PixelScreen()
    for icon in ["bulb"]:
    # for icon in ["bulb", "gmail", "heart", "cloud", "sun", "checked"]:
        pim = Piximage()
        # pim.insert_letters("HELLO YOU <", "darkred")
        # pim.insert_icon(icon)
        screen.annimate([Piximage(icon="bulb1"), Piximage(icon="bulb0"), Piximage(icon="bulb2"), Piximage(icon="bulb0")])
        screen.display_message(pim)
    screen.blackout()
