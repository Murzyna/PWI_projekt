import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Pawn(Piece):
    w_image = pg.image.load('assets/pieces/wP.png')
    b_image = pg.image.load('assets/pieces/bP.png')
    
    def __init__(self, color, pos, size):
        super().__init__(color, pos, size)
        self.first_move = True
        self.en_passant_pos = None
        self.en_passant_attack = None
        self.starting_pos = pos

    def possible_moves_f(self, board):
        y, x = self.pos

        max_possible_moves = 6  # Maksymalna liczba potencjalnych ruchów pionka
        possible_moves_array = np.full((max_possible_moves, 2), -1, dtype=int)

        count_moves = 0

        if self.starting_pos != self.pos:
            self.first_move = False

        self.en_passant_pos = None
        self.en_passant_attack = None

        if self.color == "w":
            if self.first_move and board[y-2][x] == 0:
                possible_moves_array[count_moves] = [y-2, x]
                count_moves += 1

            if board[y-1][x] == 0:              # ruch do przodu
                possible_moves_array[count_moves] = [y-1, x]
                count_moves += 1

            if 0<y<8 and 0<=x<7 and board[y-1][x+1] != 0 and board[y-1][x+1].color != self.color:       # bicie na ukos
                possible_moves_array[count_moves] = [y-1, x+1]
                count_moves += 1

            if 0<y<8 and 0<x<8 and board[y-1][x-1] != 0 and board[y-1][x-1].color != self.color:       # bicie na ukos
                possible_moves_array[count_moves] = [y-1, x-1]
                count_moves += 1

            if y==3 and 0<=x<7 and board[y][x+1] != 0 and board[y][x+1].color != self.color and isinstance(board[y][x+1], Pawn) and board[y][x+1].first_move is True:       # bicie w przelocie
                possible_moves_array[count_moves] = [y-1, x+1]
                self.en_passant_pos = [y - 1, x + 1]
                self.en_passant_attack = [y, x + 1]
                count_moves += 1

            if y==3 and 0<x<=7 and board[y][x-1] != 0 and board[y][x-1].color != self.color and isinstance(board[y][x-1], Pawn) and board[y][x-1].first_move is True:     # bicie w przelocie
                possible_moves_array[count_moves] = [y-1, x-1]
                self.en_passant_pos = [y-1, x-1]
                self.en_passant_attack = [y, x-1]
                count_moves += 1


        if self.color == "b":
            if self.first_move and board[y+2][x] == 0:
                possible_moves_array[count_moves] = [y+2, x]
                count_moves += 1

            if board[y+1][x] == 0:              # ruch do przodu
                possible_moves_array[count_moves] = [y+1, x]
                count_moves += 1

            if 0<y<8 and 0<=x<7 and board[y+1][x+1] != 0 and board[y+1][x+1].color != self.color:       # bicie na ukos
                possible_moves_array[count_moves] = [y+1, x+1]
                count_moves += 1

            if 0<y<8 and 0<x<8 and board[y+1][x-1] != 0 and board[y+1][x-1].color != self.color:       # bicie na ukos
                possible_moves_array[count_moves] = [y+1, x-1]
                count_moves += 1

            if y==4 and 0<=x<7 and board[y][x+1] != 0 and board[y][x+1].color != self.color and isinstance(board[y][x+1], Pawn) and board[y][x+1].first_move is True:       # bicie w przelocie
                possible_moves_array[count_moves] = [y-1, x+1]
                self.en_passant_pos = [y - 1, x + 1]
                self.en_passant_attack = [y, x + 1]
                count_moves += 1

            if y==4 and 0<x<=7 and board[y][x-1] != 0 and board[y][x-1].color != self.color and isinstance(board[y][x-1], Pawn) and board[y][x-1].first_move is True:     # bicie w przelocie
                possible_moves_array[count_moves] = [y-1, x-1]
                self.en_passant_pos = [y - 1, x - 1]
                self.en_passant_attack = [y, x - 1]
                count_moves += 1

        # Obcięcie tablicy do rzeczywistej liczby możliwych ruchów
        self.possible_moves = possible_moves_array[:count_moves]


    def attacks(self, board):
        y, x = self.pos

        max_possible_moves = 6  # Maksymalna liczba potencjalnych ruchów pionka
        possible_moves_array = np.full((max_possible_moves, 2), -1, dtype=int)

        count_moves = 0

        if self.color == "w":
            if 0<y<8 and 0<=x<7:       # bicie na ukos
                possible_moves_array[count_moves] = [y-1, x+1]
                count_moves += 1

            if 0<y<8 and 1<x<=8:       # bicie na ukos
                possible_moves_array[count_moves] = [y-1, x-1]
                count_moves += 1


        if self.color == "b":
            if 0<y<8 and 0<=x<7:       # bicie na ukos
                possible_moves_array[count_moves] = [y+1, x+1]
                count_moves += 1

            if 0<y<8 and 1<x<=8:       # bicie na ukos
                possible_moves_array[count_moves] = [y+1, x-1]
                count_moves += 1

        # Obcięcie tablicy do rzeczywistej liczby możliwych ruchów
        self.possible_attacks = possible_moves_array[:count_moves]