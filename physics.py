from constants import *

class Engine:
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

        if self.speedX > 4:
            self.speedX = 4
        if self.speedX < -4:
            self.speedX = -4

        self.x += self.speedX
        self.y += self.speedY
        
        self.image.x = self.x
        self.image.y = self.y
