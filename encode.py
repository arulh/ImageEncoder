from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random

class EncodedImage:
    text_ul = (50, 50)
    text_size = 75
    key = random.randint(0,1000)

    def __init__(self, s, p) -> None:
        self.text = s
        self.path = p
        self.img_data = load_image(f'{self.path}uploaded_image.png')

        self.height = self.img_data.shape[0]
        self.width = self.img_data.shape[1]

    def create_text_image(self):
        img = Image.new(mode="RGB", size=(self.width, self.height))
        font = ImageFont.truetype("~/Library/Fonts/Arial Unicode.ttf", self.text_size)
        draw = ImageDraw.Draw(img)
        draw.text(self.text_ul, self.text, fill=(0, 255, 0), font=font)
        img.save(f'{self.path}text.png')

    def encode_image(self):
        text = Image.open(f'{self.path}text.png')
        text_data = np.asarray(text)

        for y in range(self.text_ul[1], self.text_ul[1]+self.text_size + 10):
            for x in range(self.text_ul[0], self.width):
                if (correct_colour(text_data[y][x])):
                    self.img_data[y][x] = set_lob(self.img_data[y][x], self.key)

    def create_image(self, name):
        data = Image.fromarray(self.img_data)
        data.save(f'{self.path}{name}')

    def decode_image(self, key):
        for y in range(self.text_ul[1], self.text_ul[1]+self.text_size + 10):
            for x in range(self.text_ul[0], self.width):
                if (hidden_pixel(self.img_data[y][x], key)):
                    self.img_data[y][x] = (0, 255, 0, 255)


# Helper functions
def load_image(path):
    img = Image.open(path)
    data = np.asarray(img)

    return data

def set_lob(pixel, key):
    # Extract the RGB values of the pixel
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]

    # Convert the key to a binary string
    binary_key = bin(key)[2:].zfill(8)

    # Encode the least significant bits of the RGB values with the key
    r = (r & 0b11111100) | int(binary_key[0:2], 2)
    g = (g & 0b11111100) | int(binary_key[2:4], 2)
    b = (b & 0b11111100) | int(binary_key[4:6], 2)

    # Return the encoded pixel
    return (r, g, b, 255)

def correct_colour(pixel):
    return (pixel[0] == 0) and (pixel[1] == 255) and (pixel[2] == 0)

def hidden_pixel(pixel, key):
    # Extract the RGB values of the pixel
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]

    # Convert the key to a binary string
    binary_key = bin(key)[2:].zfill(8)

    # Extract the least significant bits of the RGB values
    r_lsb = r & 0b00000011
    g_lsb = g & 0b00000011
    b_lsb = b & 0b00000011

    # Extract the bits of the key used to encode the pixel
    key_bits = binary_key[0:2] + binary_key[2:4] + binary_key[4:6]

    # Decode the least significant bits of the RGB values using the key bits
    decoded_r = (r & 0b11111100) | int(key_bits[0:2], 2)
    decoded_g = (g & 0b11111100) | int(key_bits[2:4], 2)
    decoded_b = (b & 0b11111100) | int(key_bits[4:6], 2)

    # Check if the decoded pixel matches the original pixel
    if decoded_r == r and decoded_g == g and decoded_b == b:
        return True
    else:
        return False
