import random
import pygame as pg
from pygame import mixer
import numpy as np
from PWI_projekt.szachy.game.pieces.pawn import *
from PWI_projekt.szachy.game.pieces.rook import *
from PWI_projekt.szachy.game.pieces.king import *
from PWI_projekt.szachy.game.pieces.queen import *
from PWI_projekt.szachy.game.pieces.bishop import *
from PWI_projekt.szachy.game.pieces.knight import *
from PWI_projekt.szachy.game.base_piece import *
from PWI_projekt.szachy.game.game import *
import random


class DumbBot:
    def __init__(self, color, board):
        self.color = color

        self.w_attacked = board.w_attacked
        self.b_attacked = board.b_attacked

    def get_random_move(self, board):
        valid_moves = self.get_all_valid_moves(board)
        if not valid_moves:
            return None

        return random.choice(valid_moves)

    def get_all_valid_moves(self, board):
        valid_moves = []

        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece != 0 and piece.color == self.color:
                    if isinstance(piece, King):
                        piece.possible_moves_f(board, self.w_attacked, self.b_attacked)
                        possible_moves_db = piece.possible_moves

                    else:
                        piece.possible_moves_f(board)
                        possible_moves_db = piece.possible_moves

                    if possible_moves_db is not None and possible_moves_db is not []:
                        for move in possible_moves_db:
                            valid_moves.append(((i, j), move))   #old position, new position
        return valid_moves

