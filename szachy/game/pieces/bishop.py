import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Bishop(Piece):
    w_image = pg.image.load('assets/pieces/wB.png')
    b_image = pg.image.load('assets/pieces/bB.png')

    def possible_moves_f(self, board):
        index = 0
        y = self.pos[0]
        x = self.pos[1]
        for i in range(y - 1, -1, -1):
            j = x + 1
            if j == 8:
                break
            if board[i][j] == 0:
                self.possible_moves[index] = [i, j]
                index += 1
            elif board[i][j] == self.color:
                break
            else:
                self.possible_moves[index] = [i, j]
                index += 1
                break
        for i in range(y - 1, -1, -1):
            j = x - 1
            if j == -1:
                break
            if board[i][j] == 0:
                self.possible_moves[index] = [i, j]
                index += 1
            elif board[i][j] == self.color:
                break
            else:
                self.possible_moves[index] = [i, j]
                index += 1
                break
        for i in range(y + 1, 8):
            j = x + 1
            if j == 8:
                break
            if board[i][j] == 0:
                self.possible_moves[index] = [i, j]
                index += 1
            elif board[i][j] == self.color:
                break
            else:
                self.possible_moves[index] = [i, j]
                index += 1
                break
        for i in range(y + 1, 8):
            j = x - 1
            if j == 0:
                break
            if board[i][j] == 0:
                self.possible_moves[index] = [i, j]
                index += 1
            elif board[i][j] == self.color:
                break
            else:
                self.possible_moves[index] = [i, j]
                index += 1
                break



