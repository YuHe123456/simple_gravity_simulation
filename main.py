import pygame as pg

pg.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


clock = pg.time.Clock()
clock.tick(60)

dt = clock.tick(60) / 1000

class Ball:
    def __init__(self, x, y, x_v, y_v, colour, size):
        self.pos = pg.math.Vector2(x,y)
        self.vel = pg.math.Vector2(x_v, y_v)
        
        self.colour = colour
        self.size = size

    def tick(self):
        self.pos = self.pos + (self.vel * dt)


screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pg.display.set_caption("Simulation")

pg.draw.circle(screen, (255,0,0), (640,360), 5)

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    # update code


    

    pg.display.flip()