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
        y, x = self.pos

        max_possible_moves = 4  # Maksymalna liczba potencjalnych ruchów pionka
        possible_moves_array = np.full((max_possible_moves, 2), -1, dtype=int)

        count_moves = 0

        if self.color == "w":
            if board[y-1][x] == 0:              # ruch do przodu
                self.first_move = False
                possible_moves_array[count_moves] = [y-1, x]
                count_moves += 1
            if 0<y<8 and 0<=x<8 and board[y-1][x+1] != 0 and board[y-1][x+1].color != self.color:       # bicie na ukos
                self.first_move = False
                possible_moves_array[count_moves] = [y-1, x+1]
                count_moves += 1
            if 0<y<8 and 0<x<=8 and board[y-1][x-1] != 0 and board[y-1][x-1].color != self.color:       # bicie na ukos
                self.first_move = False
                possible_moves_array[count_moves] = [y-1, x-1]
                count_moves += 1
            if self.first_move and board[y-2][x] == 0:
                self.first_move = False
                possible_moves_array[count_moves] = [y-2, x]
                count_moves += 1

        if self.color == "b":
            if board[y+1][x] == 0:              # ruch do przodu
                self.first_move = False
                possible_moves_array[count_moves] = [y+1, x]
                count_moves += 1

            if 0<y<8 and 0<=x<8 and board[y+1][x+1] != 0 and board[y+1][x+1].color != self.color:       # bicie na ukos
                self.first_move = False
                possible_moves_array[count_moves] = [y+1, x+1]
                count_moves += 1

            if 0<y<8 and 0<x<=8 and board[y+1][x-1] != 0 and board[y+1][x-1].color != self.color:       # bicie na ukos
                self.first_move = False
                possible_moves_array[count_moves] = [y+1, x-1]
                count_moves += 1

            if self.first_move and board[y+2][x] == 0:
                self.first_move = False
                possible_moves_array[count_moves] = [y+2, x]
                count_moves += 1

        # Obcięcie tablicy do rzeczywistej liczby możliwych ruchów
        self.possible_moves = possible_moves_array[:count_moves]