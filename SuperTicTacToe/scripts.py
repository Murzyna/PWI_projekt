import pygame
import math 
from variables import SCREEN, O_IMG, X_IMG

#list that specifies whether you can put any more X's or O's to the specific sub_board, it states False if there is a winner there or a draw
is_playable = [[True, True, True], [True, True, True], [True, True, True]]

is_draw = [[False, False, False], [False, False, False], [False, False, False]]

small_board_wins = [[None, None, None], [None, None, None], [None, None, None]]

def check_small_win(board, small_board_coords): #w przypadku wygranej kogos w malej tablicy zmieniamy small_board_wins konkretne na 'X' albo 'O'
    pass

def check_major_win(small_board_wins):
    pass

def check_draw(board, small_board_coords):
    for i in range(3):
        for j in range(3):
            if board[small_board_coords[1]][small_board_coords[0]][i][j]!="X" and board[small_board_coords[1]][small_board_coords[0]][i][j]!="O":
                return False
    return True

def mark_draws(board):
    for i in range(3):
        for j in range(3):
            if is_draw[j][i]:
                draw_rect = pygame.Surface((180, 180))
                draw_rect.set_alpha(80)
                draw_rect.fill((255,0,0))
                SCREEN.blit(draw_rect, ((i)*200 + 10, (j)*200+200 + 10))
                is_playable[j][i]=False

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
    if next_move[0]!=None:
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

        if board[main_board_y-1][main_board_x-1][sub_board_y-1][sub_board_x-1]!='X' \
            and board[main_board_y-1][main_board_x-1][sub_board_y-1][sub_board_x-1]!='O'\
            and is_playable[main_board_y-1][main_board_x-1] and ((main_board_x-1 == next_move[0] and main_board_y-1 == next_move[1]) or next_move[0]==None):

            board[main_board_y-1][main_board_x-1][sub_board_y-1][sub_board_x-1]=to_move

            if to_move=="X": to_move="O"
            else: to_move="X"

            if is_playable[sub_board_y-1][sub_board_x-1]:
                next_move = (sub_board_x-1, sub_board_y-1)
            else:
                next_move = (None, None)

            #if check_small_win() - tutaj wlasnie powinno to sprawdzenie isc, koniecznie przed sprawdzeniem remisu, \
            #w razie wygranej koniecznie trzeba zmienic is_playable dla tego indeksu na False, next_move=None i wstawic duzy X albo O na miejsce tej planszy
            if check_draw(board, (main_board_x-1, main_board_y-1)):
                is_draw[main_board_y-1][main_board_x-1] = True
                next_move = (None, None)

        #adding new X or O to the graphical_board
        render_board(board, graphical_board, next_move)
        #bliting the board to the screen:
        for m_y in range(3):
            for m_x in range(3):
                for s_y in range(3):
                    for s_x in range(3):
                        if graphical_board[m_y][m_x][s_y][s_x][0]!=None:
                            SCREEN.blit(graphical_board[m_y][m_x][s_y][s_x][0], graphical_board[m_y][m_x][s_y][s_x][1])
        
    return board, to_move, next_move