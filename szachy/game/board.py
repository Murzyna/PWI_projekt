import pygame as pg
import numpy as np
from PWI_projekt.szachy.game.pieces.pawn import *
from PWI_projekt.szachy.game.pieces.rook import *
from PWI_projekt.szachy.game.pieces.king import *
from PWI_projekt.szachy.game.pieces.queen import *
from PWI_projekt.szachy.game.pieces.bishop import *
from PWI_projekt.szachy.game.pieces.knight import *
from PWI_projekt.szachy.game.base_piece import *
from PWI_projekt.szachy.game.game import *



class ChessBoard:

    piece_size = 65
    turn = "w"
    board = np.zeros((8,8), dtype=classmethod)

    def __init__(self, size, colors, screen):
        self.size = size
        self.color1 = colors[0]
        self.color2 = colors[1]
        self.screen = screen
        self.square_size = screen.get_width()//8
        self.piece_to_move = None
        self.w_pieces = np.zeros(16, dtype=classmethod)
        self.b_pieces = np.zeros(16, dtype=classmethod)
        self.w_attacked_pos = np.zeros((8, 8), dtype=int)
        self.b_attacked_pos = np.zeros((8, 8), dtype=int)



    def draw_board(self):
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0:
                    pg.draw.rect(self.screen, self.color1, (i*self.square_size, j*self.square_size, self.square_size, self.square_size))
                else:
                    pg.draw.rect(self.screen, self.color2, (i * self.square_size, j * self.square_size, self.square_size, self.square_size))

    def draw_pieces(self):
        for i in range(8):
            for j in range(8):
                piece = ChessBoard.board[i][j]
                if piece != 0:
                    piece.draw_piece(self.screen, piece.w_image, piece.b_image)


    def move_piece(self):
        if pg.mouse.get_pressed()[0] is False:
            ChessBoard.mouse_hold = False

        if pg.mouse.get_pressed()[0] and ChessBoard.mouse_hold is False:
            mouse_pos_i = pg.mouse.get_pos()[1] // 100
            mouse_pos_j = pg.mouse.get_pos()[0] // 100
            self.piece_to_move = (ChessBoard.board[mouse_pos_i][mouse_pos_j], mouse_pos_i, mouse_pos_j)
            ChessBoard.mouse_hold = True


        if self.piece_to_move is not None and self.piece_to_move[0] != 0 and ChessBoard.mouse_hold is False and self.piece_to_move[0].color == ChessBoard.turn:       # zmiana pozycji figur
            piece_to_move = self.piece_to_move[0]
            old_pos_i = self.piece_to_move[1]
            old_pos_j = self.piece_to_move[2]
            new_pos_i = pg.mouse.get_pos()[1]//100
            new_pos_j = pg.mouse.get_pos()[0]//100


            new_pos = np.array([new_pos_i, new_pos_j])
            piece_to_move.possible_moves_f(ChessBoard.board)
            a = 0
            for pos in piece_to_move.possible_moves:
                if pos[0] == new_pos[0] and pos[1] == new_pos[1]:       # sprawdzainie czy to dobry ruch
                    a = 1
                    break
            if a == 0:
                self.piece_to_move = None
                return 0


            if old_pos_i == new_pos_i and old_pos_j == new_pos_j:
                self.piece_to_move = None
                return 0


            piece_to_move.pos = (new_pos_i, new_pos_j)
            ChessBoard.board[old_pos_i][old_pos_j] = 0
            ChessBoard.board[new_pos_i][new_pos_j] = piece_to_move

            if isinstance(piece_to_move, King) and piece_to_move.color == "w":
                ChessBoard.w_king = piece_to_move
            elif isinstance(piece_to_move, King):
                ChessBoard.b_king = piece_to_move


            if ChessBoard.turn == "w":
                ChessBoard.turn = "b"
            else:
                ChessBoard.turn = "w"


            self.piece_to_move = None



    board[7, 4] = King("w", (7, 4), piece_size)
    board[7, 3] = Queen("w", (7, 3), piece_size)
    board[7, 7] = Rook("w", (7, 7), piece_size)
    board[7, 0] = Rook("w", (7, 0), piece_size)
    board[7, 2] = Bishop("w", (7, 2), piece_size)
    board[7, 5] = Bishop("w", (7, 5), piece_size)
    board[7, 6] = Knight("w", (7, 6), piece_size)
    board[7, 1] = Knight("w", (7, 1), piece_size)
    board[6, 1] = Pawn("w", (6, 1), piece_size)
    board[6, 2] = Pawn("w", (6, 2), piece_size)
    board[6, 3] = Pawn("w", (6, 3), piece_size)
    board[6, 4] = Pawn("w", (6, 4), piece_size)
    board[6, 5] = Pawn("w", (6, 5), piece_size)
    board[6, 6] = Pawn("w", (6, 6), piece_size)
    board[6, 7] = Pawn("w", (6, 7), piece_size)
    board[6, 0] = Pawn("w", (6, 0), piece_size)

    board[0, 4] = King("b", (0, 4), piece_size)
    board[0, 3] = Queen("b", (0, 3), piece_size)
    board[0, 0] = Rook("b", (0, 0), piece_size)
    board[0, 7] = Rook("b", (0, 7), piece_size)
    board[0, 2] = Bishop("b", (0, 2), piece_size)
    board[0, 5] = Bishop("b", (0, 5), piece_size)
    board[0, 6] = Knight("b", (0, 6), piece_size)
    board[0, 1] = Knight("b", (0, 1), piece_size)
    board[1, 1] = Pawn("b", (1, 1), piece_size)
    board[1, 2] = Pawn("b", (1, 2), piece_size)
    board[1, 3] = Pawn("b", (1, 3), piece_size)
    board[1, 4] = Pawn("b", (1, 4), piece_size)
    board[1, 5] = Pawn("b", (1, 5), piece_size)
    board[1, 6] = Pawn("b", (1, 6), piece_size)
    board[1, 7] = Pawn("b", (1, 7), piece_size)
    board[1, 0] = Pawn("b", (1, 0), piece_size)

    w_king = board[7][4]
    b_king = board[0][4]

    mouse_hold = False
