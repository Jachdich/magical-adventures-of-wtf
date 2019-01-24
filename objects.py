import pyglet, resource_loader
from constants import *

"""
Answers to that reading paper
"""

class Character:
    def __init__(self, texture_file, batch):
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
        self.image = pyglet.sprite.Sprite(img=resource_loader.player_image, x=self.x, y=self.y, batch=batch)

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

    def stop(self):
        self.forceX = 0
        self.accelX = 0
        self.speedX = 0

    def apply_forces(self):
        self.final_forceY = self.forceY - self.GRAVITY
            
        self.accelX = self.forceX / self.MASS
        self.accelY = self.final_forceY / self.MASS

        collide_negx = not self.get_colide_negx()
        collide_posx = not self.get_colide_posx()

        if collide_posx or self.speedX <= 0:
            self.speedX += self.accelX
        elif self.speedX >= 0:
            self.speedX = 0
            self.x = SCREENWIDTH - PADDING - CHARACTER_WIDTH

        if collide_negx or self.speedX >= 0:
            self.speedX += self.accelX
        elif self.speedX <= 0:
            self.speedX = 0
            self.x = PADDING
        
        if not self.get_colide_y():
            self.speedY += self.accelY
        else:
            self.speedY = 0

        if self.speedX > 0:
            if self.speedX > self.FRICTION:
                self.speedX -= self.FRICTION
            else:
                self.speedX = 0
                
        elif self.speedX < 0:
            if -self.speedX > self.FRICTION:
                self.speedX += self.FRICTION
            else:
                self.speedX = 0

        self.x += self.speedX
        self.y += self.speedY
        
        self.image.set_position(self.x, self.y)
    def draw(self):
        self.image.draw()
