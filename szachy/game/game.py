import pygame as pg
import numpy as np


def highlight(screen):
    color = (40, 200, 250)

    if pg.mouse.get_pressed()[0]:
        cords = pg.mouse.get_pos()
        x = np.floor(cords[0] / 100) * 100
        y = np.floor(cords[1] / 100) * 100
        pg.draw.rect(screen, color, (x, y, 100, 100))
        clicked = True
