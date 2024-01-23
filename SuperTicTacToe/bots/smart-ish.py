from variables import board
from scripts import is_playable
import random

class OtherBot():
    def __init__(self, player):
        self.player = player

    def select_move(self,next_move, board, to_move):
        if to_move == 'X':
            other = 'O'
        else:
            other = 'X'
        if next_move == (None, None):
            potential_main=[]
            for i in range(3):
                for j in range(3):
                    if is_playable[i][j]:
                        potential_main.append((j, i))
            next_move = random.choice(potential_main)
        potential_sub=[]

        #poziomo
        for i in range(3):
            wyn = 0
            for j in range(3):
                if board[next_move[1]][next_move[0]][i][j] == to_move and board[next_move[1]][next_move[0]][i][j] != other:
                    wyn+=1
                else:
                    maybe = (next_move[0], next_move[1], j, i)
            if wyn == 2:
                return maybe
        
        #pionowo
        for i in range(3):
            wyn = 0
            for j in range(3):
                if board[next_move[1]][next_move[0]][j][i] == to_move and board[next_move[1]][next_move[0]][j][i] != other:
                    wyn+=1
                else:
                    maybe = (next_move[0], next_move[1], i, j)
            if wyn == 2:
                return maybe
        
        #na skos
        wyn=0
        for i in range(3):
            for j in range(3):
                if i == j:
                    if board[next_move[1]][next_move[0]][i][j] == to_move and board[next_move[1]][next_move[0]][i][j] != other:
                        wyn+=1
                    else:
                        maybe = (next_move[0], next_move[1], j, i)
        if wyn == 2:
            return maybe
                
        wyn=0
        for i in range(3):
            for j in range(3):
                if i + j == 2:
                    if board[next_move[1]][next_move[0]][i][j] == to_move and board[next_move[1]][next_move[0]][i][j] != other:
                        wyn+=1
                    else:
                        maybe = (next_move[0], next_move[1], j, i)
        if wyn == 2:
            return maybe
        
        #losowo
        for i in range(3):
            for j in range(3):
                if board[next_move[1]][next_move[0]][i][j]!='X' and board[next_move[1]][next_move[0]][i][j]!='O':
                    potential_sub.append((next_move[0], next_move[1], j, i))
        return random.choice(potential_sub)
