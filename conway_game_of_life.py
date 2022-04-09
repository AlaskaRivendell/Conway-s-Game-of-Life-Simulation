import pygame as pg
import random as rnd

spielfeld = {(rnd.randrange(200),rnd.randrange(200)) for i in range(6000)}

pg.init()
sc_b= sc_h = 1000
screen = pg.display.set_mode([sc_b, sc_h])

while True:
    screen.fill((0,0,0))
    for x,y in spielfeld:
        pg.draw.rect(screen,(0,0,255), (x*5,y*5, 5, 5))
    pg.display.flip()

pg.quit()

//*17:11*//