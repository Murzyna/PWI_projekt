import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class King(Piece):
    w_image = pg.image.load('assets/pieces/wK.png')
    b_image = pg.image.load('assets/pieces/bK.png')

    def possible_moves_f(self, board):
        y, x = self.pos

        # Define the directions to check (vertical, horizontal, and diagonal)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        max_possible_moves = 8  # Maksymalna liczba potencjalnych ruchów króla
        possible_moves_array = np.full((max_possible_moves, 2), -1, dtype=int)

        count_moves = 0

        for dy, dx in directions:
            i, j = y + dy, x + dx
            if 0 <= i < 8 and 0 <= j < 8:
                if board[i][j] == 0 or board[i][j].color != self.color:
                    possible_moves_array[count_moves] = [i, j]
                    count_moves += 1

        # Obcięcie tablicy do rzeczywistej liczby możliwych ruchów
        self.possible_moves = possible_moves_array[:count_moves]
