import pygame
import math 
from variables import SCREEN, O_IMG, X_IMG

def check_small_win(board, small_board_coords):
    pass

def render_board(board, graphical_board, next_move):
    for m_y in range(3):
        for m_x in range(3):
            for s_y in range(3):
                for s_x in range(3):
                    if board[m_y][m_x][s_y][s_x]=="X":
                        graphical_board[m_y][m_x][s_y][s_x][0] = X_IMG
                        graphical_board[m_y][m_x][s_y][s_x][1] = X_IMG.get_rect(center = (m_x*200 + (s_x/3)*200 + (1/6)*200, m_y*200 + (s_y/3)*200 + (1/6)*200 + 200))
                    elif board[m_y][m_x][s_y][s_x]=="O":
                        graphical_board[m_y][m_x][s_y][s_x][0] = O_IMG
                        graphical_board[m_y][m_x][s_y][s_x][1] = O_IMG.get_rect(center = (m_x*200 + (s_x/3)*200 + (1/6)*200, m_y*200 + (s_y/3)*200 + (1/6)*200 + 200))
    if next_move!=None:
        #pygame.draw.rect(SCREEN, (0,255,0), pygame.Rect(next_move[0]*200 + 10, next_move[1]*200+200 + 10, 180,180))
        next_move_rect = pygame.Surface((180, 180))
        next_move_rect.set_alpha(80)
        next_move_rect.fill((0,255,0))
        SCREEN.blit(next_move_rect, (next_move[0]*200 + 10, next_move[1]*200+200 + 10))


def add_XO(board, graphical_board, to_move, next_move): #function that gets mouse input to place an X or O on the chosen spot
    current_pos = pygame.mouse.get_pos()
    main_board_x = math.floor(current_pos[0]/200)+1
    main_board_y = math.floor((current_pos[1]-200)/200)+1
    sub_board_x = math.floor((current_pos[0]%200)/(200/3))+1
    sub_board_y = math.floor(((current_pos[1]-200)%200)/(200/3))+1
    if main_board_x>0 and main_board_y>0:
        if board[main_board_y-1][main_board_x-1][sub_board_y-1][sub_board_x-1]!='X' and board[main_board_y-1][main_board_x-1][sub_board_y-1][sub_board_x-1]!='O':
            board[main_board_y-1][main_board_x-1][sub_board_y-1][sub_board_x-1]=to_move
            if to_move=="X": to_move="O"
            else: to_move="X"
            next_move = (sub_board_x-1, sub_board_y-1)
        #adding new X or O to the graphical_board
        render_board(board, graphical_board, next_move)
        #bliting the board to the screen
        for m_y in range(3):
            for m_x in range(3):
                for s_y in range(3):
                    for s_x in range(3):
                        if graphical_board[m_y][m_x][s_y][s_x][0]!=None:
                            SCREEN.blit(graphical_board[m_y][m_x][s_y][s_x][0], graphical_board[m_y][m_x][s_y][s_x][1])
        
    return board, to_move, next_move