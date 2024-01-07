# Upload here: https://my.numworks.com/python/valmontechno/sprites_animation_demo

from sprites import *
from ion import *
from time import sleep

sprites = [
    '5d5a6d,4d9a3d,4d3b2cbc5d,3dbcb3cb3c3d,3dbc2b3cb3c2d,3d2b4c4b3d,5d7c4d,4d2ba3b6d,3d4b2a2b5d,3d3b2ac2ac4d,3d4b5a4d,3da2b3c3a4d,4dab2c3a5d,5d3a3b5d,5d7b4d,5d4b7d',
    '5d5a6d,4d9a3d,4d3b2cbc5d,3dbcb3cb3c3d,3dbc2b3cb3c2d,3d2b4c4b3d,5d7c4d,2d4b2a2b6d,2c4b3a3b3cd,3cd2bac3a2b2cd,2c2d7a2db2d,3d9a2b2d,2d10a2b2d,d2b3a3d3a2b2d,d3b12d,2d3b11d',
    '16d,6d5a5d,5d9a2d,5d3b2cbc4d,4dbcb3cb3c2d,4dbc2b3cb3cd,4d2b4c4b2d,5d8c3d,5d4babdc3d,4dc6b3c2d,3d2ca5b2c3d,3d2b7a4d,3db8a4d,2d2b3ad3a5d,2db4d3b6d,7d4b5d'
]
bgColor = '#7892ff'
textColor = '#000000'
pallets = [
    ('#d82800','#887000','#fc9838',bgColor),
    ('#fcd8a8','#d82800','#fc9838',bgColor)
]

palletIndex = 0
keyPressed = True

fillScreen(bgColor)
draw_string('Sprites animation demo', 10, 5, textColor, bgColor)
draw_string('Press OK', 10, 25, textColor, bgColor)

while True:
    for i in range(3):
        if keydown(KEY_OK):
            if not keyPressed:
                palletIndex += 1
                if palletIndex >= len(pallets):
                    palletIndex = 0
                keyPressed = True
        else:
            keyPressed = False
        drawSprite(sprites[i], pallets[palletIndex], 70, 65, 10)
        sleep(0.1)