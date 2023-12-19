# Sprites-Numworks
This module allowing to display images on Numworks calculator. You can draw sprites on a computer with the [sprites editor](sprites_editor.py) then display it on the calculator with the [sprites module](sprites.py).

![Screenshot_20231219-192649](https://github.com/valmontechno/Sprites-Numworks/assets/108832011/e073f07e-b6fb-4a14-846e-5081d074c07e)

### Installation
You can **[upload on calculator](https://my.numworks.com/python/valmontechno/sprites)** the sprites module from the Numworks website. And upload a [sprites demo](https://my.numworks.com/python/valmontechno/sprites_demo) or a [sprites animation demo](https://my.numworks.com/python/valmontechno/sprites_animation_demo).

### More
I recommend using the [Kandinsky module of Numworks](https://github.com/ZetaMap/Kandinsky-Numworks) for test the program without putting it on the calculator.<br>
If you have a suggestion or your question is not answered, open an [Issue](https://github.com/valmontechno/Sprites-Numworks/issues/new).

### Usable content

**drawSprite(`sprite`, `pallet`, `x`, `y`, `scale`):**<br>
Draw a sprite on the screen.
* `sprite` **(string)** The description of the sprite obtained from the editor.
* `pallet` **(list of color)** The colors to use to draw the sprite. For example `('#1ab803','#620000','#e67e22')` or `((26,184,3),(98,0,0),(230,126,34))`.
* `x`, `y` **(numbers)** The coordinates of the upper left point of the sprite.
* `scale` **(number or list of two numbers)** **(default: `(1, 1)`)** The sprite scale or respectively the horizontal and vertical scale.
<br>

**fillScreen(`color`):**<br>
Fill the screen with a solid color.
* `color` **(color)** **(default: `'#ffffff'`)** The color to fill the screen with.

#### Constants
* **SCREEN_WIDTH** = `320`
* **SCREEN_HEIGHT** = `222`

### Sprites Editor

![image](https://github.com/valmontechno/Sprites-Numworks/assets/108832011/766ecfc1-a97e-4079-8d78-028d52361985)

This software allows you to draw sprites. Access the `File > Export` menu to obtain the string and the color palette to enter in the `drawSprite()` function.

