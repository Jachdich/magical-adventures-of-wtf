import pyglet, random, threading
from PIL import Image
import resource_loader

GREEN = (000, 000, 255)
WHITE = (255, 255, 255)
main_batch = pyglet.graphics.Batch()

class Character:
    def __init__(self, texture_file):
        self.FRICTION = 1
        self.GRAVITY  = 3
        self.MASS     = 10.0

        self.x, self.y = 0, 0

        self.accelY = 0
        self.accelX = 0

        self.forceX = 0
        self.forceY = 0

        self.speedX = 0
        self.speedY = 0
        self.image = pyglet.sprite.Sprite(img=resource_loader.player_image, x=self.x, y=self.y, batch=main_batch)

    def get_colide_y(self):
        if self.y > SCREENHEIGHT - (20 + 0): #uhh... height
            return True
        else:
            return False
        #add something that checks for other y colisions

    def get_colide_posx(self):
        if self.x > SCREENWIDTH - (50 + 0): #uh... width
            return True
        return False

    def get_colide_negx(self):
        if self.x < 50:
            return True
        return False

    def apply_forces(self):
        self.final_forceY = self.forceY + self.GRAVITY
        if self.speedX > 0:
            self.forceX -= self.FRICTION
        elif self.speedX < 0:
            self.forceX += self.FRICTION
            
        self.accelX = self.forceX / self.MASS
        self.accelY = self.final_forceY / self.MASS
        
        collide_negx = not self.get_colide_negx()
        collide_posx = not self.get_colide_posx()

        if collide_posx or self.speedX <= 0:
            self.speedX += self.accelX
        elif self.speedX >= 0:
            self.speedX = 0

        if collide_negx or self.speedX >= 0:

            self.speedX += self.accelX
        elif self.speedX <= 0:
            self.speedX = 0
        
        if not self.get_colide_y():
            self.speedY += self.accelY
        else:
            self.speedY = 0

        self.x += self.speedX
        self.y += self.speedY
        
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
