# Sprites by Valmontechno
# https://github.com/valmontechno/Sprites-Numworks

__name__ = 'sprites'
__version__ = '1.1'

from kandinsky import *

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 222

COLOR_CHAR = 'abcdefghijklmnopqrstuvwxyz'
BLANK_CHAR = '.'
NEWLINE_CHAR = ','

def drawSprite(sprite, pallet, x, y, scale=(1, 1)):
    if isinstance(scale, (int, float)):
        scale = [scale] * 2
    yPos = y
    for col in sprite.split(NEWLINE_CHAR):
        xPos = x
        factorStr = '0'
        for char in col:
            if char in '0123456789':
                factorStr += char
            else:
                factor = max(int(factorStr), 1)
                if char != BLANK_CHAR:
                    color = pallet[COLOR_CHAR.index(char)]
                    fill_rect(int(xPos), int(yPos), int(scale[0] * factor), int(scale[1]), color)
                xPos += scale[0] * factor
                factorStr = '0'
        yPos += scale[1]

def fillScreen(color='#ffffff'):
    fill_rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, color)