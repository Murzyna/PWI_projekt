import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Knight(Piece):
    w_image = pg.image.load('assets/pieces/wN.png')
    b_image = pg.image.load('assets/pieces/bN.png')

    def possible_moves_f(self, board):
        index = 0
        rows = [2, 2, -2, -2, 1, 1, -1, -1]
        cols = [1, -1, 1, -1, 2, -2, 2, -2]
        y = self.pos[1]
        x = self.pos[0]
        for i in range(8):
            if x + rows[i] < 0 or x + rows[i] > 7 or y + cols[i] < 0 or y + cols[i] > 7:
                continue
            else:
                if board[x + rows[i]][y + cols[i]] != 0:
                    if board[x + rows[i]][y + cols[i]].color == self.color:
                        continue
                    else:
                        self.possible_moves[index] = (x + rows[i], y + cols[i])
                        index += 1
