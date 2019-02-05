import pyglet, resource_loader
from constants import *
import physics

collisions = resource_loader.collisions

class Character(physics.Engine):
    def __init__(self, texture_file, batch, group=None):
        self.FRICTION = 00.1
        self.GRAVITY  = 03.0
        self.MASS     = 10.0

        self.x, self.y = 0, 0

        self.accelY = 0
        self.accelX = 0

        self.forceX = 0
        self.forceY = 0

        self.speedX = 0
        self.speedY = 0
        self.image = pyglet.sprite.Sprite(img=resource_loader.player_image, x=self.x, y=self.y, batch=batch, group=group)

    def get_collide_posy(self):
        if collisions[self.x, self.y][0] <= 10:
            print("collisions!")
        if self.y < 100: #uhh... height
            return True
        else:
            return False
            
    def get_collide_negy(self):
        return False
    
    def get_collide_posx(self):
        if self.x > SCREENWIDTH - (PADDING + CHARACTER_WIDTH): #uh... width
            return True
        return False

    def get_collide_negx(self):
        if self.x < PADDING:
            return True
        return False

class Background(physics.Engine):
    def __init__(self, character, batch, group=None):
        self.FRICTION = 00.1
        self.GRAVITY  = 90.0
        self.MASS     = 10.0

        self.x, self.y = 0, 0

        self.accelY = 0
        self.accelX = 0

        self.forceX = 0
        self.forceY = 0

        self.speedX = 0
        self.speedY = 0
        self.character = character
        self.image = pyglet.sprite.Sprite(img=resource_loader.background_image, x=self.x, y=self.y, batch=batch, group=group)
        self.image.scale = SCREENHEIGHT / BACKGROUND_HEIGHT

    def get_collide_negx(self):
        return False

    def get_collide_posx(self):
        return False

    def get_collide_posy(self):
        return False

    def get_collide_negy(self):
        return False

    def update(self):
        if self.character.get_collide_posx() and self.character.forceX > 0:
                self.forceX = -10.8
        elif self.character.get_collide_negx() and self.character.forceX < 0:
                self.forceX = 10.8
        else:
            self.forceX = 0
        self.apply_forces()
