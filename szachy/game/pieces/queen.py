import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Queen(Piece):
    w_image = pg.image.load('assets/pieces/wQ.png')
    b_image = pg.image.load('assets/pieces/bQ.png')

    def possible_moves_f(self, board):
        self.possible_moves = np.empty((0, 2), dtype=int)
        y, x = self.pos

        # Define the directions to check
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dy, dx in directions:
            i, j = y + dy, x + dx
            while 0 <= i < 8 and 0 <= j < 8:
                if board[i][j] == 0:
                    self.possible_moves = np.append(self.possible_moves, np.array([[i, j]]), axis=0)
                elif board[i][j].color == self.color:
                    break
                else:
                    self.possible_moves = np.append(self.possible_moves, np.array([[i, j]]), axis=0)
                    break
                i += dy
                j += dx
