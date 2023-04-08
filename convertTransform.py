from PIL import Image
import sys
import numpy

def image_to_ascii(image_path):
    img = Image.open(image_path)
    img = img.convert('L') # convert to grayscale
    width, height = img.size
    aspect_ratio = height/width
    new_width = 720
    new_height = aspect_ratio * new_width * 0.5
    img = img.resize((new_width, int(new_height)))
    pixels = img.getdata()
    ascii_chars = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    ascii_art = ''.join([ascii_chars[int(pixel/25)] for pixel in pixels])
    ascii_art = '\n'.join([ascii_art[i:i+new_width] for i in range(0, len(ascii_art), new_width)])
    return ascii_art

if __name__ == '__main__':
    image_path = sys.argv[1]
    ascii_art = image_to_ascii(image_path)
    f=open("outputAsciiArt.txt","w+")
    f.write(ascii_art)
    print(ascii_art)
