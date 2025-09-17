# Sprites-Numworks
This module allows you to display images on the Numworks calculator. You can convert any image with the [sprite converter](sprite_converter.py) and then display it on the calculator with the [sprites module](sprites.py).

![Screenshot_20231219-192649](https://github.com/valmontechno/Sprites-Numworks/assets/108832011/e073f07e-b6fb-4a14-846e-5081d074c07e)

### Installation
You can [upload to the calculator](https://my.numworks.com/python/valmontechno/sprites) the sprites module from the Numworks website.

### More
I recommend using the [Kandinsky module for Numworks](https://github.com/ZetaMap/Kandinsky-Numworks) to test the program without putting it on the calculator.<br>
If you have a suggestion or if your question is not answered, open an [Issue](https://github.com/valmontechno/Sprites-Numworks/issues/new).

### Usable content

#### drawSprite(`sprite`, `palette`, `x`, `y`, `scale`) :
Draw a sprite on the screen.
* `sprite` **(string)** The description of the sprite obtained from the editor.
* `palette` **(list of colors)** The colors to be used for drawing the sprite. For example `('#1ab803','#620000','#e67e22')` or `((26,184,3),(98,0,0),(230,126,34))`.
* `x`, `y` **(numbers)** The coordinates of the upper left point of the sprite.
* `scale` **(number or list of two numbers)** **(default: `(1, 1)`)** The sprite scale or respectively the horizontal and vertical scale.

#### fillScreen(`color`) :
Fill the screen with a solid color.
* `color` **(color)** **(default: `'#ffffff'`)** The color used to fill the screen.

#### Constants :
* **SCREEN_WIDTH** = `320`
* **SCREEN_HEIGHT** = `222`

### Sprite converter
The [sprite converter](sprite_converter.py) allows you to convert any image into a string that can be displayed by the module.
