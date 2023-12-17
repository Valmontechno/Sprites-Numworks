# Sprites by Valmontechno
# https://github.com/valmontechno/Sprites-Numworks

__name__ = 'sprites'
__version__ = '1.0'

from kandinsky import *

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 222

FACTOR_CODE = '0123456789'
COLOR_CODE = 'abcdefghijklmnopqrstuvwxyz'
BLANK_CODE = '.'
NEWLINE_CODE = ','

def drawSprite(sprite, pallet, x, y, scale=(1, 1)):
    if isinstance(scale, (int, float)):
        scale = [scale] * 2
    yPos = y
    for col in sprite.split(NEWLINE_CODE):
        xPos = x
        factorStr = '0'
        for letter in col:
            if letter in FACTOR_CODE:
                factorStr += letter
            else:
                factor = max(int(factorStr), 1)
                if letter != BLANK_CODE:
                    color = pallet[COLOR_CODE.index(letter)]
                    fill_rect(int(xPos), int(yPos), int(scale[0] * factor), int(scale[1]), color)
                xPos += scale[0] * factor
                factorStr = '0'
        yPos += scale[1]

def fillScreen(color='#ffffff'):
    fill_rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, color)