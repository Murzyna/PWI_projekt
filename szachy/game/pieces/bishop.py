import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Bishop(Piece):
    w_image = pg.image.load('assets/pieces/wB.png')
    b_image = pg.image.load('assets/pieces/bB.png')

    def possible_moves_f(self, board):
        y, x = self.pos

        # Define the directions to check (diagonal)
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        max_possible_moves = 13  # Maksymalna liczba potencjalnych ruchów gońca
        possible_moves_array = np.full((max_possible_moves, 2), -1, dtype=int)

        count_moves = 0

        for dy, dx in directions:
            i, j = y + dy, x + dx
            while 0 <= i < 8 and 0 <= j < 8:
                if board[i][j] == 0:
                    possible_moves_array[count_moves] = [i, j]
                    count_moves += 1
                elif board[i][j].color == self.color:
                    break
                else:
                    possible_moves_array[count_moves] = [i, j]
                    count_moves += 1
                    break
                i += dy
                j += dx

        # Obcięcie tablicy do rzeczywistej liczby możliwych ruchów
        self.possible_moves = possible_moves_array[:count_moves]
