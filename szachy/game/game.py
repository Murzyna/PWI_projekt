import pygame as pg
import numpy as np
import math

def draw(surface, rect):
    kolor = (3, 166, 60)
    alpha_value = 128

    green_surface = pg.Surface((rect.width, rect.height), pg.SRCALPHA)
    green_surface.fill((kolor[0], kolor[1], kolor[2], 128))
    surface.blit(green_surface, (rect.x, rect.y))

def highlight(surface):
    kolor = (3, 166, 60)
    clicked = 0
    cords = [0, 0]
    if pg.mouse.get_pressed()[0]:
        cords = pg.mouse.get_pos()
        if clicked == 0:
            starting_x = math.floor(cords[0] / 100) * 100
            starting_y = math.floor(cords[1] / 100) * 100
            target_rect = pg.Rect(starting_x, starting_y, starting_x + 100, starting_y + 100)
            draw(surface, target_rect)
