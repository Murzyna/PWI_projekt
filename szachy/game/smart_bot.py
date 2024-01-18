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

class SmartBot:
    def __init__(self, color, board):
        self.color = color

        self.w_attacked = board.w_attacked  # Initialize w_attacked
        self.b_attacked = board.b_attacked  # Initialize b_attacked

    def get_smart_move(self, board):
        attack_moves = self.all_attack_moves(board)

        if attack_moves != None and attack_moves != []:     #The smart bot attacks if he can
            return random.choice(attack_moves)


        valid_moves = self.get_all_valid_moves(board)
        if valid_moves:
            return random.choice(valid_moves)

        return None


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



                    # Check if possible_moves is None
                    if possible_moves_db is not None and possible_moves_db is not []:
                        for move in possible_moves_db:
                            valid_moves.append(((i, j), move))   #old position, new position
        return valid_moves





    def all_attack_moves(self, board):
        valid_moves = []

        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece != 0 and piece.color == self.color:
                    if isinstance(piece, King):
                        possible_attacks_sb = None
                        pass        #The King does not have attacks

                    else:
                        piece.attacks(board)
                        possible_attacks_sb = piece.possible_attacks



                    if possible_attacks_sb is not None and possible_attacks_sb is not []:
                        for move in possible_attacks_sb:
                            target_piece = board[move[0]][move[1]]
                            if target_piece != 0 and target_piece.color != self.color:      #check if there is a piece of the other color
                                valid_moves.append(((i, j), move))   #old position, new position
        return valid_moves
