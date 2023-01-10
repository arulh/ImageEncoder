from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random

class EncodedImage:
    text_ul = (50, 50)
    text_size = 75
    key = random.randint(0,500)

    def __init__(self, s, p) -> None:
        self.text = s
        self.path = p
        self.img_data = load_image(self.path)

        self.height = self.img_data.shape[0]
        self.width = self.img_data.shape[1]

    def create_text_image(self):
        # img = Image.open("/Users/arulh/Documents/Projects/ImageEncoder/resources/cat.jpg")
        img = Image.new(mode="RGB", size=(self.width, self.height))
        font = ImageFont.truetype("~/Library/Fonts/Arial Unicode.ttf", self.text_size)
        draw = ImageDraw.Draw(img)
        draw.text(self.text_ul, self.text, fill=(0, 255, 0), font=font)
        img.save("/Users/arulh/Documents/Projects/ImageEncoder/resources/text.jpg")

    def encode_image(self):
        text = Image.open("/Users/arulh/Documents/Projects/ImageEncoder/resources/text.jpg")
        text_data = np.asarray(text)

        for y in range(self.text_ul[1], self.text_ul[1]+self.text_size + 10): # range(self.text_ul[1], self.height)
            for x in range(self.text_ul[0], self.width): # range(self.text_ul[0], self.width)
                if (correct_colour(text_data[y][x])):
                    self.img_data[y][x] = set_lob(self.img_data[y][x], self.key)

    def create_image(self):
        data = Image.fromarray(self.img_data)
        data.save("encoded_cat.jpg")

    def decode_image(self):
        print("hello")


# Helper functions
def load_image(path):
    img = Image.open(path)
    data = np.asarray(img)

    return data

def set_lob(pixel, key):
    x = key%64

    # pixel->r = (pixel->r / 4)*4 + (d / 16);
    # pixel->g = (pixel->g / 4)*4 + ((d % 16) / 4);
    # pixel->b = (pixel->b / 4)*4 + (d % 4);

    # r = (pixel[0]/4)*4 + (x/16)
    # g = (pixel[1]/4)*4 + ((x%16)/4)
    # b = (pixel[2]/4)*4 + (x%4)

    r = 0
    g = 255
    b = 0

    return (r, g, b)

def correct_colour(pixel):
    return (pixel[0] < 30) and (pixel[1] > 220) and (pixel[2] < 30)

def black(pixel):
    return pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0