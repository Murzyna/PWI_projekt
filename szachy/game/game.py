import pygame as pg
import numpy as np

clicked = False
x = 0
y = 0

def highlight(screen):
    color = (3, 166, 60)
    global clicked
    global x
    global y
    if pg.mouse.get_pressed()[0]:
        cords = pg.mouse.get_pos()
<<<<<<< HEAD
        if clicked is False:
=======
        if clicked == False:
>>>>>>> origin/main
            x = np.floor(cords[0] / 100) * 100
            y = np.floor(cords[1] / 100) * 100
            target_rect = pg.draw.rect(screen, color, (x, y, 100, 100))
            clicked = True
            print("kutas")
<<<<<<< HEAD
        if clicked is True:

    if clicked is True:
        target_rect = pg.draw.rect(screen, color, (x, y, 100, 100))
=======
    if clicked == True:
        target_rect = pg.draw.rect(screen, color, (x, y, 100, 100))
>>>>>>> origin/main
