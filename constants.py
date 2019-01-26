import pyglet
SCREENHEIGHT = 480
SCREENWIDTH  = 640
CHARACTER_WIDTH  = 52
CHARACTER_HEIGHT = 158
BACKGROUND_WIDTH  = 6000
BACKGROUND_HEIGHT = 300
PADDING = 30
GREEN = (000, 000, 255)
WHITE = (255, 255, 255)

main_batch = pyglet.graphics.Batch()
foreground = pyglet.graphics.OrderedGroup(1)
background = pyglet.graphics.OrderedGroup(0)
