import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Knight(Piece):
    w_image = pg.image.load('assets/pieces/wN.png')
    b_image = pg.image.load('assets/pieces/bN.png')

    def possible_moves_f(self, board):
        self.possible_moves = np.empty((0, 2), dtype=int)
        y, x = self.pos

        rows = [2, 2, -2, -2, 1, 1, -1, -1]
        cols = [1, -1, 1, -1, 2, -2, 2, -2]

        for i in range(8):
            new_x, new_y = x + rows[i], y + cols[i]
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board[new_x][new_y] == 0 or board[new_x][new_y].color != self.color:
                    self.possible_moves = np.append(self.possible_moves, np.array([[new_x, new_y]]), axis=0)
