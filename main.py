import pygame as pg

pg.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


clock = pg.time.Clock()

clock.tick(1)
dt = clock.tick(1) / 1000

class Ball:
    def __init__(self, x, y, x_v, y_v, colour, size):
        self.pos = pg.math.Vector2(x,y)
        self.vel = pg.math.Vector2(x_v, y_v)
        
        self.colour = colour
        self.size = size
    
    def tick(self):
        self.pos = self.pos + (self.vel * dt)

    def draw_ball(self, screen):
        pg.draw.circle(screen, self.colour, self.pos, self.size)

screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pg.display.set_caption("Simulation")

pg.draw.circle(screen, (255,0,0), (640,360), 5)

running = True

ball1 = Ball(720,360, 5,0,(255,0,0), 5)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # update code

    screen.fill((255,255,255))

    ball1.tick()
    ball1.draw_ball(screen)

    
    
    pg.display.flip()