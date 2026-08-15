import pygame as pg
import math
pg.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

clock = pg.time.Clock()

clock.tick(60)
dt = clock.tick(25) / 1000

class Ball:

    density = 30

    def __init__(self, x, y, x_v, y_v, colour, size, trail=False):

        self.pos = pg.math.Vector2(x,y)
        self.vel = pg.math.Vector2(x_v, y_v)
        self.acc = pg.math.Vector2(0,0)

        self.colour = colour
        self.size = size

        self.mass = math.pi * size**2 * self.density

        self.trail = trail

    def tick(self, obj_list, trail_list):

        self.find_acc(obj_list)
        self.vel = self.vel + (self.acc * dt)
        self.pos = self.pos + (self.vel * dt)

        self.create_trail_ball(trail_list)

    def draw_ball(self, screen):
        pg.draw.circle(screen, self.colour, self.pos, self.size)

    def create_trail_ball(self, trail_list):

        if self.trail is True:
            trail_ball = TrailBall(self.pos, self.size)
            trail_list.append(trail_ball)

    def find_acc(self, obj_list):
        for obj in obj_list:
            if obj is not self:
                distance = self.pos.distance_to(obj.pos)
                acc_unit_vector = (obj.pos - self.pos).normalize()

                # if distance is less than size of target obj
                #   mass = ((actual distance / size) ** (1/2)) * mass

                if distance == 0:
                    acc_vector = pg.Vector2(0,0)
                    
                elif distance > obj.size:
                    effective_mass = obj.mass
                    acc_vector = acc_unit_vector * (effective_mass / distance**2)

                elif distance < obj.size:
                    effective_mass = obj.mass
                    acc_vector = acc_unit_vector * (effective_mass / obj.size**3) * distance

                    

                # acc_vector = (effective_mass * acc_unit_vector) / (distance**2)
                self.acc = acc_vector

        print(acc_unit_vector)

class TrailBall:

    countdown = 10  # Number of frames where ball is visible
    trail_colour = (0,255,255)

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.colour = self.trail_colour
        self.countdown = self.countdown

    def draw_trail_ball(self, screen):
        pg.draw.circle(screen, self.colour, self.pos, self.size)
        self.countdown -= 1

        if self.countdown < 0:
            return False # Returns false when lifespan is exceeded


screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pg.display.set_caption("Simulation")

pg.draw.circle(screen, (255,0,0), (640,360), 5)

running = True

ball1 = Ball(720, 180, 0, 0, (255,0,0), 5, trail=True)
ball2 = Ball(720, 360, 0, 0, (0,255,0), 100)

objects = [ball1, ball2][::-1]
trails = []

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # update code

    screen.fill((255,255,255))

    for obj in objects:
        obj.tick(objects, trails)

    for trail_ball in trails:

        if trail_ball.draw_trail_ball(screen) is False:
            trails.remove(trail_ball)

    for obj in objects:
        obj.draw_ball(screen)



        
    
    pg.display.flip()