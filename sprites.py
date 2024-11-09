import pygame as pg
vec = pg.math.Vector2
# Importing modules
class Player(pg.sprite.Sprite): # Creating player class
    def __init__(self, x, y): # Initializing position, image, and size of the object
        self.x = x
        self.y = y
        pg.sprite.Sprite.__init__(self)

        self.vel = vec(0, 0) # Velocity and acceleration
        self.acc = vec(0, 0)
        self.img = pg.image.load("assets/jungleman.png")
        self.img = pg.transform.scale(self.img, (50, 50))
        self.img_1 = pg.transform.scale(self.img, (50, 50))
        self.rect=self.img.get_rect()
        self.jumping = False


    def update(self): # Update method - this is called every tick
        self.acc = vec(0, 0.8) # Applying gravity
        self.acc.x += self.vel.x*-0.12
        self.vel += self.acc # Applying acceleration
        self.x += self.vel.x + 0.5*self.acc.x
        self.y += self.vel.y + 0.5*self.acc.x # Applying movement
        self.rect.midbottom = (self.x, self.y)
        self.img = self.img_1
        if self.vel.x > 0:
            self.img = pg.transform.flip(self.img_1, True, False)

    def draw(self, win): # Draws the image
        rect = self.img.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center) #Centers image
        win.blit(self.img, rect.topleft) # Draws image on screen


    def jump(self): # Jump function
        if not self.jumping:
            self.vel.y += -20
            self.jumping = True


# class Water(pg.sprite.Sprite): # I have started coding the platform class
#
#     def __init__(self, x, y, groups):
#         self.x = x
#         self.y = y
#         self.groups = groups
#         pg.sprite.Sprite.__init__(self, groups)
#         self.img = pg.image.load("water3.png")
#
#         self.img = pg.transform.scale(self.img, (220, 50))
#         self.rect=self.img.get_rect()
#     def draw(self,win):
#
#         win.blit(self.img, self.rect.bottomleft)  # Draws image on screen
#
#     def update(self):
#         self.rect.midbottom = (self.x, self.y) # Positions sprite



class Platform(pg.sprite.Sprite): # I have started coding the platform class
    def __init__(self, x, y, groups):
        self.x = x
        self.y = y
        self.groups = groups
        pg.sprite.Sprite.__init__(self, groups)
        self.img = pg.image.load("assets/platform.png")

        self.img = pg.transform.scale(self.img, (180, 50))
        self.rect=self.img.get_rect()
    def draw(self,win):

        win.blit(self.img, self.rect.bottomleft)  # Draws image on screen


    def update(self):
        self.rect.midbottom = (self.x, self.y) # Positions sprite


class Fruit(pg.sprite.Sprite):
    def __init__(self, x, y, groups):
        self.x = x
        self.y = y
        self.groups = groups
        pg.sprite.Sprite.__init__(self, groups)
        self.img=pg.transform.scale(pg.image.load("assets/banana.png"), (64, 32))
        self.img_1 = pg.transform.scale(pg.image.load("assets/banana.png"), (64, 32))
        self.vel = vec(0, 0)  # Velocity and acceleration
        self.acc = vec(0, 0)


        self.rect = self.img.get_rect() # Image rectangle

    def draw(self,win):
        #rect = self.img.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)  # Centers image
        win.blit(self.img, self.rect.bottomleft)  # Draws image on screen

    def update(self):
        self.rect.midbottom = (self.x, self.y)
        self.acc = vec(0, 0.8)  # Applying gravity
        self.acc.x += self.vel.x * -0.12
        self.vel += self.acc  # Applying acceleration
        self.x += self.vel.x + 0.5 * self.acc.x
        self.y += self.vel.y + 0.5 * self.acc.x  # Applying movement
        self.rect.midbottom = (self.x, self.y)

class Heart(pg.sprite.Sprite):
    def __init__(self, x, y, groups):
        self.game_is_on = True
        self.x = x
        self.y = y
        self.groups = groups
        pg.sprite.Sprite.__init__(self, groups)
        self.img=pg.transform.scale(pg.image.load("assets/heart1.png"), (64, 32))
        self.img_1 = pg.transform.scale(pg.image.load("assets/heart1.png"), (64, 32))
        self.vel = vec(0, 0)  # Velocity and acceleration
        self.acc = vec(0, 0)


        self.rect = self.img.get_rect() # Image rectangle

    def draw(self,win):
        #rect = self.img.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)  # Centers image
        win.blit(self.img, self.rect.bottomleft)  # Draws image on screen

    def update(self):
        self.rect.midbottom = (self.x, self.y)
        self.acc = vec(0, 0.8)  # Applying gravity
        self.acc.x += self.vel.x * -0.12
        self.vel += self.acc  # Applying acceleration
        self.x += self.vel.x + 0.5 * self.acc.x
        self.y += self.vel.y + 0.5 * self.acc.x  # Applying movement
        self.rect.midbottom = (self.x, self.y)
