import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *
from PWI_projekt.szachy.game.pieces.rook import *


class King(Piece):
    w_image = pg.image.load('assets/pieces/wK.png')
    b_image = pg.image.load('assets/pieces/bK.png')

    def __init__(self, color, pos, size):
        super(King, self).__init__(color, pos, size)
        self.is_checked = False

    def possible_moves_f(self, board, w_attacked, b_attacked):
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
                    # Sprawdzenie, czy pole nie znajduje się na liście atakowanych pól
                    if self.color == "w":
                        if b_attacked[i][j] == -1:
                            possible_moves_array[count_moves] = [i, j]
                            count_moves += 1

                    if self.color == "b":
                        if w_attacked[i][j] == -1:
                            possible_moves_array[count_moves] = [i, j]
                            count_moves += 1

        # Obcięcie tablicy do rzeczywistej liczby możliwych ruchów
        self.possible_moves = possible_moves_array[:count_moves]
        self.possible_attacks = possible_moves_array[:count_moves]


    def check(self, w_attacked, b_attacked):
        if self.color == "w":
            if b_attacked[self.pos[0]][self.pos[1]] == 1:
                self.is_checked = True
                return True
        if self.color == "b":
            if w_attacked[self.pos[0]][self.pos[1]] == 1:
                self.is_checked = True
                return True
        self.is_checked = False
        return False


    def can_castling(self, board, w_attacked, b_attacked):
        if self.color == "w" and self.was_moved is False:
            if board[7][7] != 0 and board[7][7].was_moved is False and board[7][6] == board[7][5] == 0 and b_attacked[7][6] != 1 and b_attacked[7][5] != 1:
                return True
            elif board[7][0] != 0 and board[7][0].was_moved is False and board[7][2] == board[7][3] == 0 and b_attacked[7][2] != 1 and b_attacked[7][3] != 1:
                return True
        elif self.color == "b" and self.was_moved is False:
            if board[0][7] != 0 and board[0][7].was_moved is False and board[0][6] == board[0][5] == 0 and w_attacked[0][6] != 1 and w_attacked[0][5] != 1:
                return True
            elif board[0][0] != 0 and board[0][0].was_moved is False and board[0][2] == board[0][3] == 0 and w_attacked[0][2] != 1 and w_attacked[0][3] != 1:
                return True
        return False
