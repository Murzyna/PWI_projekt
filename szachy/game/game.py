import pygame as pg
import numpy as np


def highlight(screen):
    color = (3, 166, 60)
    clicked = 0
    if pg.mouse.get_pressed()[0]:
        cords = pg.mouse.get_pos()
        if clicked == 0:
            x = np.floor(cords[0] / 100) * 100
            y = np.floor(cords[1] / 100) * 100
            target_rect = pg.draw.rect(screen, color, (x, y, 100, 100))
            print("kutas")
