import pygame as pg

pg.init()

screen = pg.display.set_mode((1280,720))
pg.display.set_caption("Simulation")

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # update code

    pg.display.flip()