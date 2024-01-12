try:
    import os
    os.environ['KANDINSKY_OS_MODE'] = '0'
    os.environ['KANDINSKY_ZOOM_RATIO'] = '2'
except: pass

from sprites import *
import kandinsky as kd
import numpy as np

sprite = '9b8.9b,b7ab8.b7ab,baba5b8.5babab,b3a2b14.2b3ab,ba2bab14.ba2bab,ba4b14.4bab,bab20.bab,bab20.bab,3b20.3b9,3b20.3b,bab20.bab,bab20.bab,ba4b14.4bab,ba2bab14.ba2bab,b3a2b14.2b3ab,baba5b8.5babab,b7ab8.b7ab,9b8.9b'
pallet = ('#e3fbfb','#383028')

# for i in range(6):
#     for j in range(8):
#         drawSprite(sprite, pallet, 25*j, 25*i)
drawSprite(sprite, pallet, 0, 0, 2)