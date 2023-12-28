import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Knight(Piece):
    w_image = pg.image.load('assets/pieces/wN.png')
    b_image = pg.image.load('assets/pieces/bN.png')

    def possible_moves_f(self, board):
        y, x = self.pos

        rows = [2, 2, -2, -2, 1, 1, -1, -1]
        cols = [1, -1, 1, -1, 2, -2, 2, -2]

        max_possible_moves = 8  # Maksymalna liczba potencjalnych ruchów skoczka
        possible_moves_array = np.full((max_possible_moves, 2), -1, dtype=int)

        count_moves = 0

        for i in range(8):
            new_x, new_y = x + rows[i], y + cols[i]
            if 0 <= new_x < 8 and 0 <= new_y < 8 and (board[new_y][new_x] == 0 or board[new_y][new_x].color != self.color):
                possible_moves_array[count_moves] = [new_y, new_x]
                count_moves += 1

        self.possible_moves = possible_moves_array[:count_moves]

    def attacks(self, board):
        y, x = self.pos

        rows = [2, 2, -2, -2, 1, 1, -1, -1]
        cols = [1, -1, 1, -1, 2, -2, 2, -2]

        max_possible_moves = 8  # Maksymalna liczba potencjalnych ruchów skoczka
        possible_attacks_array = np.full((max_possible_moves, 2), -1, dtype=int)

        count_moves = 0

        for i in range(8):
            new_x, new_y = x + rows[i], y + cols[i]
            if 8 > new_x >= 0 == board[new_y][new_x] and 0 <= new_y < 8:
                possible_attacks_array[count_moves] = [new_y, new_x]
                count_moves += 1

        self.possible_moves = possible_attacks_array[:count_moves]
