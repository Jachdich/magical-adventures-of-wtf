import pyglet, random, threading
from PIL import Image
import resource_loader
from objects import Character

GREEN = (000, 000, 255)
WHITE = (255, 255, 255)
main_batch = pyglet.graphics.Batch()
        
class GameEngine:
    def __init__(self):
        self._parse_background_image("background.png")
        
        self.player = Character("test")
        self.offset = 0

    def _parse_background_image(self, image_name):
        im = Image.open("resources/bg.png")
        image_data = im.getdata()
        image_x, image_y = im.size
        
        self.data = [] 
        x = 0
        y = 0
        pos = 0
        pixel_scaler = SCREENHEIGHT / image_y
        while True:
            self.data.append([[x * pixel_scaler, y * pixel_scaler, pixel_scaler, pixel_scaler], image_data[pos]])
            pos += 1
            x += 1
            if x >= image_x:
                x = 0
                y += 1
            if y >= image_y:
                break
            
    def draw(self):
            self.player.apply_forces()
            self.player.draw()
                             
            for point in self.data:
                size_xy, colour = point
                x_, y_, sx, sy= size_xy

                #pygame.draw.rect(self.screen, colour, [x_ + self.offset, y_, sx, sy])

SCREENWIDTH = 640
SCREENHEIGHT = 480
g = GameEngine()

key = pyglet.window.key
#keys = key.KeyStateHandler()

screen = pyglet.window.Window(SCREENWIDTH, SCREENHEIGHT)

@screen.event
def on_draw():
    screen.clear()
    main_batch.draw()

@screen.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        print("yes")

pyglet.app.run()
