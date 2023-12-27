import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Queen(Piece):
    w_image = pg.image.load('assets/pieces/wQ.png')
    b_image = pg.image.load('assets/pieces/bQ.png')

    def possible_moves_f(self, board):
        index = 0
        y = self.pos[0]
        x = self.pos[1]
        for i in range(x + 1, 8):
            if board[y][i] == 0:
                self.possible_moves[index] = [y, i]
                index += 1
            elif board[y][i].color == self.color:
                break
            else:
                self.possible_moves[index] = [y, i]
                index += 1
                break
        for i in range(x - 1, -1, -1):
            if board[y][i] == 0:
                self.possible_moves[index] = [y, i]
                index += 1
            elif board[y][i].color == self.color:
                break
            else:
                self.possible_moves[index] = [y, i]
                index += 1
                break
        for i in range(y + 1, 8):
            if board[i][x] == 0:
                self.possible_moves[index] = [i, x]
                index += 1
            elif board[i][x].color == self.color:
                break
            else:
                self.possible_moves[index] = [i, x]
                index += 1
                break
        for i in range(y - 1, -1, -1):
            if board[i][x] == 0:
                self.possible_moves[index] = [i, x]
                index += 1
            elif board[i][x].color == self.color:
                break
            else:
                self.possible_moves[index] = [i, x]
                index += 1
                break
        for i in range(y - 1, -1, -1):
            j = x + 1
            if j == 8:
                break
            if board[i][j] == 0:
                self.possible_moves[index] = [i, j]
                index += 1
            elif board[i][j].color == self.color:
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
            elif board[i][j].color == self.color:
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
            elif board[i][j].color == self.color:
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
            elif board[i][j].color == self.color:
                break
            else:
                self.possible_moves[index] = [i, j]
                index += 1
                break