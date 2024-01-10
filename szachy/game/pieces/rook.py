import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *
from PWI_projekt.szachy.game.pieces.king import *


class Rook(Piece):
    w_image = pg.image.load('assets/pieces/wR.png')
    b_image = pg.image.load('assets/pieces/bR.png')

    def possible_moves_f(self, board):
        y, x = self.pos

        # Define the directions to check (vertical and horizontal)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        max_possible_moves = 14  # Maksymalna liczba potencjalnych ruchów wieży
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

    def attacks(self, board):
        y, x = self.pos

        # Define the directions to check (vertical and horizontal)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        max_possible_moves = 14  # Maksymalna liczba potencjalnych ruchów wieży
        possible_attacks_array = np.full((max_possible_moves, 2), -1, dtype=int)

        count_moves = 0
        for dy, dx in directions:
            i, j = y + dy, x + dx
            while 0 <= i < 8 and 0 <= j < 8:
                if board[i][j] == 0:
                    possible_attacks_array[count_moves] = [i, j]
                    count_moves += 1
                else:
                    if isinstance(board[i][j], King) and board[i][j].color != self.color:
                        possible_attacks_array[count_moves] = [i, j]
                        count_moves += 1
                    else:
                        possible_attacks_array[count_moves] = [i, j]
                        count_moves += 1
                        break
                i += dy
                j += dx

        # Obcięcie tablicy do rzeczywistej liczby możliwych ruchów
        self.possible_attacks = possible_attacks_array[:count_moves]

