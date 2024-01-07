from PIL import Image
from tkinter import filedialog

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 222
COLOR_CHAR = 'abcdefghijkl'
BLANK_CHAR = '.'
NEWLINE_CHAR = ','
TRANSPARENCY_LIMIT = 127

img = Image.open(filedialog.askopenfilename())

if img.width > SCREEN_WIDTH or img.height > SCREEN_HEIGHT:
    img = img.resize((SCREEN_WIDTH, SCREEN_HEIGHT))

img = img.convert('RGBA')
imgP = img.convert('P')
imgP = imgP.quantize(len(COLOR_CHAR))
imgP = imgP.convert('RGB')

palette = set()
for row in range(img.height):
    for col in range(img.width):
        if img.getpixel((col, row))[3] > TRANSPARENCY_LIMIT:
            palette.add(imgP.getpixel((col, row)))
palette = list(palette)
print('(' + ','.join(["'#%02x%02x%02x'" % tuple(palette[i]) for i in range(len(palette))]) + ')')

sprite = ''
for row in range(img.height):
    factor = 0
    char = ''
    for col in range(img.width +1):
        if char != '' and (col == img.width and char != BLANK_CHAR) or (col < img.width and char != (BLANK_CHAR if img.getpixel((col, row))[3] <= TRANSPARENCY_LIMIT else COLOR_CHAR[palette.index(imgP.getpixel((col, row)))])):
            if factor > 1:
                sprite += str(factor)
            sprite += char
            factor = 0
        if col < img.width:
            char = BLANK_CHAR if img.getpixel((col, row))[3] <= TRANSPARENCY_LIMIT else COLOR_CHAR[palette.index(imgP.getpixel((col, row)))]
            factor += 1
    if row < img.height -1:
        sprite += ','

print(f"'{sprite}'")
input()