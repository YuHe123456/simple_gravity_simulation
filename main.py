import pygame as pg
import math
pg.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

clock = pg.time.Clock()

clock.tick(60)
dt = clock.tick(25) / 1000

class Ball:

    density = 1

    def __init__(self, x, y, x_v, y_v, colour, size):

        self.pos = pg.math.Vector2(x,y)
        self.vel = pg.math.Vector2(x_v, y_v)
        self.acc = pg.math.Vector2(0,0)

        self.colour = colour
        self.size = size

        self.mass = math.pi * size**2 * self.density

    def tick(self):
        self.pos = self.pos + (self.vel * dt)
        self.vel = self.vel + (self.acc * dt)

    def draw_ball(self, screen):
        pg.draw.circle(screen, self.colour, self.pos, self.size)

    def find_acc(self, obj_list):
        for obj in obj_list:
            if obj is not self:
                distance = self.pos.distance_to(obj.pos)
                acc_unit_vector = (obj.pos - self.pos).normalize()

                # if distance is less than size of target obj
                #   mass = ((actual distance / size) ** (1/2)) * mass

                if distance < obj.size:
                    effective_mass = ((distance / obj.size) ** (1/2)) * obj.mass
                else:
                    effective_mass = obj.mass

                acc_vector = (effective_mass * acc_unit_vector) / (distance**2)
                self.acc = acc_vector
                print(self.acc)

        print(acc_unit_vector)

screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pg.display.set_caption("Simulation")

pg.draw.circle(screen, (255,0,0), (640,360), 5)

running = True

ball1 = Ball(720, 360, 5, 0, (255,0,0), 5)
ball2 = Ball(720, 180, 5, 0, (0,255,0), 100)

objects = [ball1, ball2]

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # update code

    screen.fill((255,255,255))

    for obj in objects:
        obj.find_acc(objects)
        obj.tick()
    for obj in objects:
        obj.draw_ball(screen)
        
    
    pg.display.flip()