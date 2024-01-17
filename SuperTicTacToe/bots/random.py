from variables import board
from scripts import is_playable
import random

class RandomBot():
    def __init__(self, player):
        self.player = player

    def select_move(self,next_move, board):
        if next_move == (None, None):
            potential_main=[]
            for i in range(3):
                for j in range(3):
                    if is_playable[i][j]:
                        potential_main.append((j, i))
            next_move = random.choice(potential_main)
        potential_sub=[]
        for i in range(3):
            for j in range(3):
                if board[next_move[1]][next_move[0]][i][j]!='X' and board[next_move[1]][next_move[0]][i][j]!='O':
                    potential_sub.append(board[next_move[1]][next_move[0]][i][j])
        return random.choice(potential_sub)