"""
Sprite encoding:
    pyxel.blt(x, y, img, u, v, w, h, [colkey])
- x, y: where to draw the sprite in screen
- img: image bank index (0-2)
- u, v: x and y position of the sprite in the image bank
- w, h: width and height of the sprite
- colkey: (optional) color to be treated as transparent
"""

SUN_SPRITES = {"static_sun": (0, 0, 0, 0, 0, 0, 0, 0)}