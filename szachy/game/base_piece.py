import pygame as pg
import numpy as np


class Piece:

    def __init__(self, color, pos, size):
        self.color = color
        self.pos = pos
        self.size = size

    def draw_piece(self, screen, w_image, b_image):
        w_scaled_image = pg.transform.scale(w_image, (self.size, self.size))
        b_scaled_image = pg.transform.scale(b_image, (self.size, self.size))
        if self.color == "w":
            screen.blit(w_scaled_image, (self.pos[1]*100 + 13, self.pos[0]*100 + 13))
        else:
            screen.blit(b_scaled_image, (self.pos[1]*100 + 13, self.pos[0]*100 + 13))
