import pygame as pg
import numpy as np


def highlight(screen):
    color = (3, 166, 60)

    if pg.mouse.get_pressed()[0]:
        cords = pg.mouse.get_pos()
        x = (cords[0] // 100) * 100
        y = (cords[1] // 100) * 100
        pg.draw.rect(screen, color, (x, y, 100, 100))
        clicked = True
        print("kutas", "chuj")