import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Pawn(Piece):
    w_image = pg.image.load('assets/pieces/wP.png')
    b_image = pg.image.load('assets/pieces/bP.png')

    def __init__(self, color, pos, size):
        super().__init__(color, pos, size)
        self.first_move = True

    def possible_moves_f(self, board):
        self.possible_moves = np.empty((0, 2), dtype=int)
        y, x = self.pos

        # Define the direction based on the color of the pawn
        direction = 1 if self.color == 'w' else -1

        # Move one square forward
        new_y = y + direction
        if 0 <= new_y < 8 and board[new_y][x] == 0:
            self.possible_moves = np.append(self.possible_moves, np.array([[new_y, x]]), axis=0)

            # Move two squares forward on the first move
            if self.first_move and board[y + 2 * direction][x] == 0:
                self.possible_moves = np.append(self.possible_moves, np.array([[y + 2 * direction, x]]), axis=0)

        # Check diagonal moves for capturing
        for dx in [-1, 1]:
            new_x = x + dx
            if 0 <= new_x < 8 and 0 <= new_y < 8 and board[new_y][new_x] != 0 and board[new_y][new_x].color != self.color:
                self.possible_moves = np.append(self.possible_moves, np.array([[new_y, new_x]]), axis=0)