import pyglet, random, threading
from PIL import Image
import resource_loader, pyglet
from objects import Character, Background
from constants import *

GREEN = (000, 000, 255)
WHITE = (255, 255, 255)
main_batch = pyglet.graphics.Batch()
foreground = pyglet.graphics.OrderedGroup(1)
background = pyglet.graphics.OrderedGroup(0)

class GameEngine:
    def __init__(self):
        self.player = Character("test", main_batch, foreground)
        self.background = Background(self.player, main_batch, background)
            
    def draw(self, fps=0):
        self.background.update()
        self.player.apply_forces()
        
g = GameEngine()

key = pyglet.window.key

screen = pyglet.window.Window(SCREENWIDTH, SCREENHEIGHT)
#pyglet.gl.glClearColor(1, 1, 1, 1)

@screen.event
def on_draw():
    screen.clear()
    g.draw()
    main_batch.draw()

@screen.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        g.player.forceX = -0.8

    if symbol == key.RIGHT:
        g.player.forceX = 0.8

    if symbol == key.SPACE:
        g.player.forceY = 15
        print("mmmMMMMMMMmmmmmm")
        
@screen.event
def on_key_release(symbol, modifiers):
    if symbol == key.LEFT or symbol == key.RIGHT:
        g.player.forceX = 0
        
pyglet.clock.schedule_interval(g.draw, 1.0 / 60.0)
pyglet.app.run()
