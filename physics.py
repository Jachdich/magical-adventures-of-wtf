from constants import *

class Engine:
    def apply_forces(self):
        self.final_forceY = self.forceY - self.GRAVITY
            
        self.accelX = self.forceX / self.MASS
        self.accelY = self.final_forceY / self.MASS

        collide_negx = not self.get_collide_negx()
        collide_posx = not self.get_collide_posx()

        if collide_posx or self.speedX < 0:
            self.speedX += self.accelX
        elif self.speedX >= 0:
            self.speedX = 0
            self.x = SCREENWIDTH - PADDING - CHARACTER_WIDTH

        if collide_negx or self.speedX > 0:
            self.speedX += self.accelX
        elif self.speedX <= 0:
            self.speedX = 0
            self.x = PADDING
        
        if not self.get_collide_posy() and self.speedY + self.accelY > 0:
            self.speedY += self.accelY
        else:
            self.speedY = 0
            self.y = 0

        if not self.get_collide_negy() and self.speedY + self.accelY < 0:
            self.speedY += self.accelY
        else:
            self.speedY = 0

        if self.get_collide_negy() and self.speedY + self.accelY > 0:
            self.y = SCREENHEIGHT
            self.speedY = 0
            
        if self.get_collide_posy() and self.speedY + self.accelY < 0:
            self.y = 0
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
