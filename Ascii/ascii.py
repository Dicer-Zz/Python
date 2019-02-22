# -*- coding: utf-8 -*-
# @Author: Dicer
# @Date:   2019-01-23 09:47:10
# @Last Modified by:   Dicer
# @Last Modified time: 2019-01-23 10:46:06

from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--height', default = '128', type = int)
parser.add_argument('--width', default = '70', type = int)


args = parser.parse_args()

IMG = args.file
WIDTH = args.height
HEIGHT =  args.height
OUTPUT = args.output

ascii_char = list("!\"#$%&'()*+,-./0123456789:;<=>?`abcdefghijklmnopqrstuvwxyz|~@ABCDEFGHIJKLMNOPQRSTUVWXYZ\\^_	")

def get_char(r, g, b, alpha = 256):

	if alpha == 0:
		return ' '

	length = len(ascii_char)

	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

	unit = (256.0 + 1)/length

	return ascii_char[int(gray/unit)]

if __name__ == '__main__':

	im = Image.open(IMG)
	im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

	txt = ""

	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*im.getpixel((j, i)))
		txt += '\n'

	print(txt)

	if OUTPUT:
		with open(OUTPUT, 'w') as f:
			f.write(txt)
	else:
		with open("output.txt", 'w') as f:
			f.write(txt)


