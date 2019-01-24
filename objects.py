import pyglet, resource_loader
from constants import *
import physics

"""
Answers to that reading paper
"""

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

    def get_colide_y(self):
        if self.y < 100: #uhh... height
            return True
        else:
            return False
        #add something that checks for other y colisions

    def get_colide_posx(self):
        if self.x > SCREENWIDTH - (PADDING + CHARACTER_WIDTH): #uh... width
            return True
        return False

    def get_colide_negx(self):
        if self.x < PADDING:
            return True
        return False

class Background(physics.Engine):
    def __init__(self, character, batch, group=None):
        self.FRICTION = 00.1
        self.GRAVITY  = 00.0
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
        self.image.scale = SCREENHEIGHT // BACKGROUND_HEIGHT

    def get_colide_negx(self):
        return False

    def get_colide_posx(self):
        return False

    def get_colide_y(self):
        return False

    def update(self):
        if self.character.get_colide_posx() and self.character.forceX > 0:
                self.forceX = -10.8
        elif self.character.get_colide_negx() and self.character.forceX < 0:
                self.forceX = 10.8
        else:
            self.forceX = 0
        self.apply_forces()
