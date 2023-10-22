import pygame as pg
import world


pg.init()
root = pg.display.set_mode((1100, 600))
pg.display.set_caption('LiveGame')
clock = pg.time.Clock()


w = world.World((220, 120))


run = True
while run:
    clock.tick(30)
    w.make_a_move()
    w.drawing()
    root.blit(w.root, (0, 0))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False


