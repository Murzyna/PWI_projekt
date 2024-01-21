import pygame as pg
import numpy as np


class Piece:

    draw_adjust = 17

    def __init__(self, color, pos, size):
        self.color = color
        self.pos = pos
        self.size = size
        self.possible_moves = None
        self.possible_attacks = None
        self.was_moved = False


    def draw_piece(self, screen, w_image, b_image):
        w_scaled_image = pg.transform.scale(w_image, (self.size, self.size))
        b_scaled_image = pg.transform.scale(b_image, (self.size, self.size))
        if self.color == "w":
            screen.blit(w_scaled_image, (self.pos[1]*100 + Piece.draw_adjust, self.pos[0]*100 + Piece.draw_adjust))
        else:
            screen.blit(b_scaled_image, (self.pos[1]*100 + Piece.draw_adjust, self.pos[0]*100 + Piece.draw_adjust))


    def is_clicked(self):
        if pg.mouse.get_pressed()[0]:
            if self.pos[1]*100 < pg.mouse.get_pos()[0] < self.pos[1]*100 + 100:
                if self.pos[0]*100 < pg.mouse.get_pos()[1] < self.pos[0]*100 + 100:
                    return True
        return False
