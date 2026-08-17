import pygame as pg
import math
pg.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

clock = pg.time.Clock()



class Ball:

    density = 50
    LINE_COLOUR = (0,0,0)
    LINE_SCALAR = 10
    def __init__(self, x, y, x_v, y_v, colour, size, trail=False):

        self.pos = pg.math.Vector2(x,y)
        self.vel = pg.math.Vector2(x_v, y_v)
        self.acc = pg.math.Vector2(0,0)

        self.colour = colour
        self.size = size

        self.mass = math.pi * size**2 * self.density

        self.trail = trail
        self.trail_list = []
        

    def tick(self, obj_list, screen):

        
        self.vel = self.vel + (self.acc * dt)
        self.pos = self.pos + (self.vel * dt)

        self.create_trail_ball()

        for trail_ball in self.trail_list[:]:
            if trail_ball.draw_trail_ball(screen) is False:
                self.trail_list.remove(trail_ball)

    def draw_ball(self, screen):
        pg.draw.circle(screen, self.colour, self.pos, self.size)

    def draw_line(self,screen):
        pg.draw.line(screen, self.LINE_COLOUR, self.pos, self.pos + (self.LINE_SCALAR * self.acc), width=4)
    

    def create_trail_ball(self):

        if self.trail is True:
            trail_ball = TrailBall(self.pos, self.size)
            self.trail_list.append(trail_ball)

    def find_acc(self, obj_list):

        self.acc = pg.Vector2(0,0)

        for obj in obj_list:

            if obj is not self:

                distance = self.pos.distance_to(obj.pos)

                # if distance is less than size of target obj
                #   mass = ((actual distance / size) ** (1/2)) * mass

                if distance == 0:
                    continue

                acc_unit_vector = (obj.pos - self.pos).normalize()
                
                if distance >= obj.size:
                    self.acc += acc_unit_vector * (obj.mass / distance**2)

                elif distance < obj.size:
                    self.acc += acc_unit_vector * (obj.mass / obj.size**3) * distance

    def calculate_kinetic_energy(self):
        k_e = 0.5 * self.mass * self.vel.magnitude_squared()
        return k_e

class TrailBall:

    countdown = 20  # Number of frames where ball is visible
    trail_colour = (0,255,255)

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.colour = self.trail_colour
        self.countdown = TrailBall.countdown

    def draw_trail_ball(self, screen):
        pg.draw.circle(screen, self.colour, self.pos, self.size)
        self.countdown -= 1

        if self.countdown < 0:
            return False # Returns false when lifespan is exceeded


screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pg.display.set_caption("Simulation")

running = True

ball1 = Ball(480, 480, 0, 0, (255,0,0), 20, trail=True)
ball2 = Ball(640, 360, 0, 0, (0,255,0), 20, trail=True)
ball3 = Ball(320, 360, 0, 0, (255,255,0), 20, trail=True)

objects = [ball1, ball2, ball3][::-1]



while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # update code

    dt = clock.tick(120) / 1000

    total_k_e = 0
    
    for obj in objects:
        total_k_e += obj.calculate_kinetic_energy()
    
    print(total_k_e)

    screen.fill((255,255,255))

    for obj in objects:
        obj.find_acc(objects)

    for obj in objects:
        obj.tick(objects, screen)

    for obj in objects:
        obj.draw_ball(screen)
        obj.draw_line(screen)

 
    
    pg.display.flip()