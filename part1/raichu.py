#
# raichu.py : Play the game of Raichu
#
# Hrithik Prativadi Bhayankara, Anurag Sangem, and Diwakar Reddy.
#
# Based on skeleton code by D. Crandall, Oct 2021
#
import sys
import time
import copy
import heapq

def conv_2D(board, N):
        
    board2D = []
    # Converting to a 2D matrix, that is a list of lists.
    for i in range(N):
        board2D.append(list(board[i*N:N+N*i]))
        
    return board2D

def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))

def valid_index(pichu_loc, N):
        return 0 <= pichu_loc[0] < N  and 0 <= pichu_loc[1] < N
                    
def pichu_w(board2D, N ,player):
    # To store all the indices where the condition holds true.
    pichu_loc=[(row_i, col_i) for col_i in range(len(board2D[0])) for row_i in range(len(board2D)) if board2D[row_i][col_i]=="w"]
    
    pichu_succ = []
    
    board_succ = []
    
    for r, c in pichu_loc:
        board_succ = copy.deepcopy(board2D)
        # To check whether or not the next to go index is valid or not.
        if valid_index((r + 1, c - 1), N):
            # To promote if it reaches the maximum row from it's respective side.
            if board2D[r + 1][c - 1] == '.' and ((r + 1) == (N - 1)):
                board_succ[r + 1][c - 1] = '@'
                board_succ[r][c] = '.'
                pichu_succ.append(board_succ)
                
            elif board2D[r + 1][c - 1] == '.' and ((r + 1) != (N - 1)):
                board_succ[r + 1][c - 1] = 'w'
                board_succ[r][c] = '.'
                pichu_succ.append(board_succ)
                
            # To jump over the opponent piece and remove it if the move is legal! :)
            elif valid_index((r + 2, c - 2), N) and ((r + 2) == (N - 1)) and board2D[r + 2][c - 2] == '.' and board2D[r + 1][c - 1] == 'b':
                board_succ[r + 2][c - 2] = '@'
                board_succ[r + 1][c - 1] = '.'
                board_succ[r][c] = '.'                                              
                pichu_succ.append(board_succ)
            
            elif valid_index((r + 2, c - 2), N) and (r + 2 != N - 1) and board2D[r + 2][c - 2] == '.' and board2D[r + 1][c - 1] == 'b':
                board_succ[r + 2][c - 2] = 'w'
                board_succ[r + 1][c - 1] = '.'
                board_succ[r][c] = '.'                                              
                pichu_succ.append(board_succ)
        
    for r, c in pichu_loc:
        board_succ = copy.deepcopy(board2D)
        # To check whether or not the next to go index is valid or not.
        if valid_index((r + 1, c + 1), N):
            # To promote if it reaches the maximum row from it's respective side.
            if board2D[r + 1][c + 1] == '.' and ((r + 1) == (N - 1)):
                board_succ[r + 1][c + 1] = '@'
                board_succ[r][c] = '.'                                               
                pichu_succ.append(board_succ)
                    
            elif board2D[r + 1][c + 1] == '.' and ((r + 1) != (N - 1)):
                board_succ[r + 1][c + 1] = 'w'
                board_succ[r][c] = '.'
                pichu_succ.append(board_succ)
            
            # To jump over the opponent piece and remove it if the move is legal! :)
            elif valid_index((r + 2, c + 2), N) and (r + 2 == N - 1) and board2D[r + 2][c + 2] == '.' and board2D[r + 1][c + 1] == 'b':
                board_succ[r + 2][c + 2] = '@'
                board_succ[r + 1][c + 1] = '.'
                board_succ[r][c] = '.'                                              
                pichu_succ.append(board_succ)
                
            elif valid_index((r + 2, c + 2), N) and (r + 2 != N - 1) and board2D[r + 2][c + 2] == '.' and board2D[r + 1][c + 1] == 'b':
                board_succ[r + 2][c + 2] = 'w'
                board_succ[r + 1][c + 1] = '.'
                board_succ[r][c] = '.'                                              
                pichu_succ.append(board_succ)
    
#     for i in pichu_succ:
#         for j in range(len(i)):
#             print(i[j])
#         print('\n')
#         print('\n')
#     print('loop')
    
    return pichu_succ

def pichu_b(board2D, N ,player):
    pichu_loc=[(row_i, col_i) for col_i in range(len(board2D[0])) for row_i in range(len(board2D)) if board2D[row_i][col_i]=="b"]
    
    pichu_succ = []
    
    board_succ = []
    
    for r, c in pichu_loc:
        board_succ = copy.deepcopy(board2D)
        # To check whether or not the next to go index is valid or not.
        if valid_index((r - 1, c - 1), N):
            # To promote if it reaches the maximum row from it's respective side.
            if board2D[r - 1][c - 1] == '.' and ((r - 1) == 0):
                board_succ[r - 1][c - 1] = '$'
                board_succ[r][c] = '.'
                pichu_succ.append(board_succ)
                
            elif board2D[r - 1][c - 1] == '.' and ((r - 1) != 0):
                board_succ[r - 1][c - 1] = 'b'
                board_succ[r][c] = '.'
                pichu_succ.append(board_succ)
            
            # To jump over the opponent piece and remove it if the move is legal! :)
            elif valid_index((r - 2, c - 2), N) and ((r - 2) == 0) and board2D[r - 2][c - 2] == '.' and board2D[r - 1][c - 1] == 'w':
                board_succ[r - 2][c - 2] = '$'
                board_succ[r - 1][c - 1] = '.'
                board_succ[r][c] = '.'                                              
                pichu_succ.append(board_succ)
                
            elif valid_index((r - 2, c - 2), N) and ((r - 2) != 0) and board2D[r - 2][c - 2] == '.' and board2D[r - 1][c - 1] == 'w':
                board_succ[r - 2][c - 2] = 'b'
                board_succ[r - 1][c - 1] = '.'
                board_succ[r][c] = '.'                                              
                pichu_succ.append(board_succ)
        
    for r, c in pichu_loc:
        board_succ = copy.deepcopy(board2D)
        # To check whether or not the next to go index is valid or not.
        if valid_index((r - 1, c + 1), N):
            # To promote if it reaches the maximum row from it's respective side.
            if board2D[r - 1][c + 1] == '.' and ((r - 1) == 0):
                board_succ[r - 1][c + 1] = '$'
                board_succ[r][c] = '.'                                               
                pichu_succ.append(board_succ)
                
            elif board2D[r - 1][c + 1] == '.' and ((r - 1) != 0):
                board_succ[r - 1][c + 1] = 'b'
                board_succ[r][c] = '.'                                               
                pichu_succ.append(board_succ)
            
            # To jump over the opponent piece and remove it if the move is legal! :)
            elif valid_index((r - 2, c + 2), N) and ((r - 2) == 0) and board2D[r - 2][c + 2] == '.' and board2D[r - 1][c + 1] == 'w':
                board_succ[r - 2][c + 2] = '$'
                board_succ[r - 1][c + 1] = '.'
                board_succ[r][c] = '.'                                              
                pichu_succ.append(board_succ)
                
            elif valid_index((r - 2, c + 2), N) and ((r - 2) != 0) and board2D[r - 2][c + 2] == '.' and board2D[r - 1][c + 1] == 'w':
                board_succ[r - 2][c + 2] = 'b'
                board_succ[r - 1][c + 1] = '.'
                board_succ[r][c] = '.'                                              
                pichu_succ.append(board_succ)
                
#     for i in pichu_succ:
#         for j in range(len(i)):
#             print(i[j])
#         print('\n')
#         print('\n')
#     print('loop')
    
    return pichu_succ

def pikachu_W(board2D, N ,player):
    pikachu_loc=[(row_i, col_i) for col_i in range(len(board2D[0])) for row_i in range(len(board2D)) if board2D[row_i][col_i]=="W"]
    
    pikachu_succ = []
    
    board_succ = []
    
    # .............................................................................................................                
    # Left
    
    for r, c in pikachu_loc: 
        board_succ = copy.deepcopy(board2D)
        # To check whether or not the next to go index is valid or not.
        if valid_index((r, c - 1), N):
            if board2D[r][c - 1] == '.':
                board_succ[r][c - 1] = 'W'
                board_succ[r][c] = '.'
                pikachu_succ.append(board_succ)
                
                board_succ = copy.deepcopy(board2D)
                if valid_index((r, c - 2), N) and board2D[r][c - 2] == '.':
                    board_succ[r][c - 2] = 'W'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
        if valid_index((r, c - 1), N) and (board2D[r][c - 1] == 'b' or board2D[r][c - 1] == 'B'):
                if valid_index((r, c - 2), N) and board2D[r][c - 2] == '.':
                    board_succ[r][c - 2] = 'W'
                    board_succ[r][c - 1] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
                board_succ = copy.deepcopy(board2D)
                if valid_index((r, c - 2), N) and board2D[r][c - 2] == '.' and (valid_index((r, c - 3), N) and board2D[r][c - 3] == '.'):
                    board_succ[r][c - 3] = 'W'
                    board_succ[r][c - 2] = '.'
                    board_succ[r][c - 1] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
    for r, c in pikachu_loc:
        board_succ = copy.deepcopy(board2D)
        if valid_index((r, c - 2), N) and (board2D[r][c - 2] == 'b' or board2D[r][c - 2] == 'B'):
                if valid_index((r, c - 1), N) and board2D[r][c - 1] == '.':
                    if valid_index((r, c - 3), N) and board2D[r][c - 3] == '.':
                        board_succ[r][c - 3] = 'W'
                        board_succ[r][c - 2] = '.'
                        board_succ[r][c - 1] = '.'
                        board_succ[r][c] = '.'
                        pikachu_succ.append(board_succ)
    # .............................................................................................................                
    # Right               
    for r, c in pikachu_loc:
        board_succ = copy.deepcopy(board2D)
        if valid_index((r, c + 1), N):
            # To check whether or not the next to go index is valid or not.
            if board2D[r][c + 1] == '.':
                board_succ[r][c + 1] = 'W'
                board_succ[r][c] = '.'
                pikachu_succ.append(board_succ)
                
                board_succ = copy.deepcopy(board2D)
                if valid_index((r, c + 2), N) and board2D[r][c + 2] == '.':
                    board_succ[r][c + 2] = 'W'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
        if valid_index((r, c + 1), N) and (board2D[r][c + 1] == 'b' or board2D[r][c + 1] == 'B'):
                if valid_index((r, c + 2), N) and board2D[r][c + 2] == '.':
                    board_succ[r][c + 2] = 'W'
                    board_succ[r][c + 1] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
                board_succ = copy.deepcopy(board2D)
                if valid_index((r, c + 2), N) and board2D[r][c + 2] == '.' and (valid_index((r, c + 3), N) and board2D[r][c + 3] == '.'):
                    board_succ[r][c + 3] = 'W'
                    board_succ[r][c + 2] = '.'
                    board_succ[r][c + 1] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                  
    for r, c in pikachu_loc:
        board_succ = copy.deepcopy(board2D)
        if valid_index((r, c + 2), N) and (board2D[r][c + 2] == 'b' or board2D[r][c + 2] == 'B'):
                if valid_index((r, c + 1), N) and board2D[r][c + 1] == '.':
                    if valid_index((r, c + 3), N) and board2D[r][c + 3] == '.':
                        board_succ[r][c + 3] = 'W'
                        board_succ[r][c + 2] = '.'
                        board_succ[r][c + 1] = '.'
                        board_succ[r][c] = '.'
                        pikachu_succ.append(board_succ)
                        
                        
                        
                        
                        
    # .............................................................................................................                
    # Forward
                    
    for r, c in pikachu_loc:
        board_succ = copy.deepcopy(board2D)
        if valid_index((r + 1, c), N):
            # To check whether or not the next to go index is valid or not.
            if board2D[r + 1][c] == '.' and ((r + 1) == (N - 1)):
                board_succ[r + 1][c] = '@'
                board_succ[r][c] = '.'
                pikachu_succ.append(board_succ)
                
                board_succ = copy.deepcopy(board2D)
                
            elif board2D[r + 1][c] == '.' and ((r + 1) != (N - 1)):
                board_succ[r + 1][c] = 'W'
                board_succ[r][c] = '.'
                pikachu_succ.append(board_succ)
                
                board_succ = copy.deepcopy(board2D)
                if valid_index((r + 2, c), N) and ((r + 2) == (N - 1)) and board2D[r + 2][c] == '.':
                    board_succ[r + 2][c] = '@'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    board_succ = copy.deepcopy(board2D)
                    
                elif valid_index((r + 2, c), N) and ((r + 2) != (N - 1)) and board2D[r + 2][c] == '.':
                    board_succ[r + 2][c] = 'W'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    board_succ = copy.deepcopy(board2D)
        
            
        if valid_index((r + 1, c), N) and (board2D[r + 1][c] == 'b' or board2D[r + 1][c] == 'B'):
                if valid_index((r + 2, c), N) and ((r + 2) == (N - 1)) and board2D[r + 2][c] == '.':
                    board_succ[r + 2][c] = '@'
                    board_succ[r + 1][c] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
                    board_succ = copy.deepcopy(board2D)
                
                elif valid_index((r + 2, c), N) and ((r + 2) != (N - 1)) and board2D[r + 2][c] == '.':
                    board_succ[r + 2][c] = 'W'
                    board_succ[r + 1][c] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
                    board_succ = copy.deepcopy(board2D)
                if valid_index((r + 2, c), N) and board2D[r + 2][c] == '.' and (valid_index((r + 3, c), N) and ((r + 3) == (N - 1)) and board2D[r + 3][c] == '.'):
                    board_succ[r + 3][c] = '@'
                    board_succ[r + 2][c] = '.'
                    board_succ[r + 1][c] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
                elif valid_index((r + 2, c), N) and board2D[r + 2][c] == '.' and (valid_index((r + 3, c), N) and ((r + 3) != (N - 1)) and board2D[r + 3][c] == '.'):
                    board_succ[r + 3][c] = 'W'
                    board_succ[r + 2][c] = '.'
                    board_succ[r + 1][c] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                  
    for r, c in pikachu_loc:
        board_succ = copy.deepcopy(board2D)
        if valid_index((r + 2, c), N) and (board2D[r + 2][c] == 'b' or board2D[r + 2][c] == 'B'):
                if valid_index((r + 1, c), N) and board2D[r + 1][c] == '.':
                    if valid_index((r + 3, c), N) and ((r + 3) == (N - 1)) and board2D[r + 3][c] == '.':
                        board_succ[r + 3][c] = '@'
                        board_succ[r + 2][c] = '.'
                        board_succ[r + 1][c] = '.'
                        board_succ[r][c] = '.'
                        pikachu_succ.append(board_succ)
                        
                    elif valid_index((r + 3, c), N) and ((r + 3) != (N - 1)) and board2D[r + 3][c] == '.':
                        board_succ[r + 3][c] = 'W'
                        board_succ[r + 2][c] = '.'
                        board_succ[r + 1][c] = '.'
                        board_succ[r][c] = '.'
                        pikachu_succ.append(board_succ)
                
            
                
#     for i in pikachu_succ:
#         for j in range(len(i)):
#             print(i[j])
#         print('\n')
#         print('\n')
#     print('loop')
    
    return pikachu_succ

def pikachu_B(board2D, N ,player):
    pikachu_loc=[(row_i, col_i) for col_i in range(len(board2D[0])) for row_i in range(len(board2D)) if board2D[row_i][col_i]=="B"]
    
    pikachu_succ = []
    
    board_succ = []
    
    # .............................................................................................................                
    # Left
    
    for r, c in pikachu_loc: 
        board_succ = copy.deepcopy(board2D)
        # To check whether or not the next to go index is valid or not.
        if valid_index((r, c - 1), N):
            if board2D[r][c - 1] == '.':
                board_succ[r][c - 1] = 'B'
                board_succ[r][c] = '.'
                pikachu_succ.append(board_succ)
                
                board_succ = copy.deepcopy(board2D)
                if valid_index((r, c - 2), N) and board2D[r][c - 2] == '.':
                    board_succ[r][c - 2] = 'B'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
        if valid_index((r, c - 1), N) and (board2D[r][c - 1] == 'w' or board2D[r][c - 1] == 'W'):
                if valid_index((r, c - 2), N) and board2D[r][c - 2] == '.':
                    board_succ[r][c - 2] = 'B'
                    board_succ[r][c - 1] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
                board_succ = copy.deepcopy(board2D)
                if valid_index((r, c - 2), N) and board2D[r][c - 2] == '.' and (valid_index((r, c - 3), N) and board2D[r][c - 3] == '.'):
                    board_succ[r][c - 3] = 'B'
                    board_succ[r][c - 2] = '.'
                    board_succ[r][c - 1] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
    for r, c in pikachu_loc:
        board_succ = copy.deepcopy(board2D)
        if valid_index((r, c - 2), N) and (board2D[r][c - 2] == 'w' or board2D[r][c - 2] == 'W'):
                if valid_index((r, c - 1), N) and board2D[r][c - 1] == '.':
                    if valid_index((r, c - 3), N) and board2D[r][c - 3] == '.':
                        board_succ[r][c - 3] = 'B'
                        board_succ[r][c - 2] = '.'
                        board_succ[r][c - 1] = '.'
                        board_succ[r][c] = '.'
                        pikachu_succ.append(board_succ)
    # .............................................................................................................                
    # Right               
    for r, c in pikachu_loc:
        board_succ = copy.deepcopy(board2D)
        if valid_index((r, c + 1), N):
            # To check whether or not the next to go index is valid or not.
            if board2D[r][c + 1] == '.':
                board_succ[r][c + 1] = 'B'
                board_succ[r][c] = '.'
                pikachu_succ.append(board_succ)
                
                board_succ = copy.deepcopy(board2D)
                if valid_index((r, c + 2), N) and board2D[r][c + 2] == '.':
                    board_succ[r][c + 2] = 'B'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
        if valid_index((r, c + 1), N) and (board2D[r][c + 1] == 'W' or board2D[r][c + 1] == 'W'):
                if valid_index((r, c + 2), N) and board2D[r][c + 2] == '.':
                    board_succ[r][c + 2] = 'B'
                    board_succ[r][c + 1] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
                board_succ = copy.deepcopy(board2D)
                if valid_index((r, c + 2), N) and board2D[r][c + 2] == '.' and (valid_index((r, c + 3), N) and board2D[r][c + 3] == '.'):
                    board_succ[r][c + 3] = 'B'
                    board_succ[r][c + 2] = '.'
                    board_succ[r][c + 1] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                  
    for r, c in pikachu_loc:
        board_succ = copy.deepcopy(board2D)
        if valid_index((r, c + 2), N) and (board2D[r][c + 2] == 'w' or board2D[r][c + 2] == 'W'):
                if valid_index((r, c + 1), N) and board2D[r][c + 1] == '.':
                    if valid_index((r, c + 3), N) and board2D[r][c + 3] == '.':
                        board_succ[r][c + 3] = 'B'
                        board_succ[r][c + 2] = '.'
                        board_succ[r][c + 1] = '.'
                        board_succ[r][c] = '.'
                        pikachu_succ.append(board_succ)
                        
                        
                        
                        
                        
    # .............................................................................................................                
    # Forward
                    
    for r, c in pikachu_loc:
        board_succ = copy.deepcopy(board2D)
        if valid_index((r - 1, c), N):
            # To check whether or not the next to go index is valid or not.
            if board2D[r - 1][c] == '.' and ((r - 1) == 0):
                board_succ[r - 1][c] = '$'
                board_succ[r][c] = '.'
                pikachu_succ.append(board_succ)
                
                board_succ = copy.deepcopy(board2D)
                
            elif board2D[r - 1][c] == '.' and ((r - 1) != 0):
                board_succ[r - 1][c] = 'B'
                board_succ[r][c] = '.'
                pikachu_succ.append(board_succ)
                
                board_succ = copy.deepcopy(board2D)
                
                if valid_index((r - 2, c), N) and ((r - 2) == 0) and board2D[r - 2][c] == '.':
                    board_succ[r - 2][c] = '$'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    board_succ = copy.deepcopy(board2D)
                    
                elif valid_index((r - 2, c), N) and ((r - 2) != 0) and board2D[r - 2][c] == '.':
                    board_succ[r - 2][c] = 'B'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    board_succ = copy.deepcopy(board2D)
                    
        if valid_index((r - 1, c), N) and (board2D[r - 1][c] == 'w' or board2D[r - 1][c] == 'W'):
                if valid_index((r - 2, c), N) and ((r - 2) == 0) and board2D[r - 2][c] == '.':
                    board_succ[r - 2][c] = '$'
                    board_succ[r - 1][c] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
                    board_succ = copy.deepcopy(board2D)
                    
                elif valid_index((r - 2, c), N) and ((r - 2) != 0) and board2D[r - 2][c] == '.':
                    board_succ[r - 2][c] = 'B'
                    board_succ[r - 1][c] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
                    board_succ = copy.deepcopy(board2D)
                    
                if valid_index((r - 2, c), N) and board2D[r - 2][c] == '.' and (valid_index((r - 3, c), N) and ((r - 3) == 0) and board2D[r - 3][c] == '.'):
                    board_succ[r - 3][c] = '$'
                    board_succ[r - 2][c] = '.'
                    board_succ[r - 1][c] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                    
                elif valid_index((r - 2, c), N) and board2D[r - 2][c] == '.' and (valid_index((r - 3, c), N) and ((r - 3) != 0) and board2D[r - 3][c] == '.'):
                    board_succ[r - 3][c] = 'B'
                    board_succ[r - 2][c] = '.'
                    board_succ[r - 1][c] = '.'
                    board_succ[r][c] = '.'
                    pikachu_succ.append(board_succ)
                  
    for r, c in pikachu_loc:
        board_succ = copy.deepcopy(board2D)
        if valid_index((r - 2, c), N) and (board2D[r - 2][c] == 'w' or board2D[r - 2][c] == 'W'):
                if valid_index((r - 1, c), N) and board2D[r - 1][c] == '.':
                    if valid_index((r - 3, c), N) and ((r - 3) == 0) and board2D[r - 3][c] == '.':
                        board_succ[r - 3][c] = '$'
                        board_succ[r - 2][c] = '.'
                        board_succ[r - 1][c] = '.'
                        board_succ[r][c] = '.'
                        pikachu_succ.append(board_succ)
                        
                    elif valid_index((r - 3, c), N) and ((r - 3) != 0) and board2D[r - 3][c] == '.':
                        board_succ[r - 3][c] = 'B'
                        board_succ[r - 2][c] = '.'
                        board_succ[r - 1][c] = '.'
                        board_succ[r][c] = '.'
                        pikachu_succ.append(board_succ)
                
            
                
#     for i in pikachu_succ:
#         for j in range(len(i)):
#             print(i[j])
#         print('\n')
#         print('\n')
#     print('loop')
    
    return pikachu_succ

def raichu_W(board2D, N ,player):
    raichu_loc=[(row_i, col_i) for col_i in range(len(board2D[0])) for row_i in range(len(board2D)) if board2D[row_i][col_i]=="@"]
    
    raichu_succ = []
    
    board_succ = []
    
    # .............................................................................................................                
    # Left
    
    
    for r, c in raichu_loc:
        counter = 0 
        board_succ = copy.deepcopy(board2D)
        for i in range(c-1, -1, -1):
            # To check whether or not the next to go index is valid or not.
            if valid_index((r, i), N) and board2D[r][i] == '.':
                board_succ[r][i] = '@'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((r, i), N) and (board2D[r][i] == 'b' or board2D[r][i] == 'B' or board2D[r][i] == '$'):
                for k in range(i-1, -1, -1):
                    if valid_index((r, k), N) and board2D[r][k] == '.':
                        board_succ[r][c] = '.'
                        board_succ[r][i] = '.'
                        board_succ[r][k] = '@'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((r, i), N) and (board2D[r][i] == 'w' or board2D[r][i] == 'W' or board2D[r][i] == '@'):
                counter = 1
                        
            if counter == 1:
                break
                
    # .............................................................................................................                
    # Right
    
    
    for r, c in raichu_loc:
        counter = 0 
        board_succ = copy.deepcopy(board2D)
        for i in range(c+1, N):
            # To check whether or not the next to go index is valid or not.
            if valid_index((r, i), N) and board2D[r][i] == '.':
                board_succ[r][i] = '@'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((r, i), N) and (board2D[r][i] == 'b' or board2D[r][i] == 'B' or board2D[r][i] == '$'):
                for k in range(i+1, N):
                    if valid_index((r, k), N) and board2D[r][k] == '.':
                        board_succ[r][c] = '.'
                        board_succ[r][i] = '.'
                        board_succ[r][k] = '@'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((r, i), N) and (board2D[r][i] == 'w' or board2D[r][i] == 'W' or board2D[r][i] == '@'):
                counter = 1
                        
            if counter == 1:
                break
    
    # .............................................................................................................                
    # Top
    
    
    for r, c in raichu_loc:
        counter = 0 
        board_succ = copy.deepcopy(board2D)
        for i in range(r-1, -1, -1):
            # To check whether or not the next to go index is valid or not.
            if valid_index((i, c), N) and board2D[i][c] == '.':
                board_succ[i][c] = '@'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((i, c), N) and (board2D[i][c] == 'b' or board2D[i][c] == 'B' or board2D[i][c] == '$'):
                for k in range(i-1, -1, -1):
                    if valid_index((k, c), N) and board2D[k][c] == '.':
                        board_succ[r][c] = '.'
                        board_succ[i][c] = '.'
                        board_succ[k][c] = '@'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((i, c), N) and (board2D[i][c] == 'w' or board2D[i][c] == 'W' or board2D[i][c] == '@'):
                counter = 1
                        
            if counter == 1:
                break
                
    # .............................................................................................................                
    # Bottom
    
    
    for r, c in raichu_loc:
        counter = 0
        board_succ = copy.deepcopy(board2D)
        for i in range(r+1, N):
            # To check whether or not the next to go index is valid or not.
            if valid_index((i, c), N) and board2D[i][c] == '.':
                board_succ[i][c] = '@'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((i, c), N) and (board2D[i][c] == 'b' or board2D[i][c] == 'B' or board2D[i][c] == '$'):
                for k in range(i+1, N):
                    if valid_index((k, c), N) and board2D[k][c] == '.':
                        board_succ[r][c] = '.'
                        board_succ[i][c] = '.'
                        board_succ[k][c] = '@'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((i, c), N) and (board2D[i][c] == 'w' or board2D[i][c] == 'W' or board2D[i][c] == '@'):
                counter = 1
                        
            if counter == 1:
                break

    # .............................................................................................................                
    # Left - Up
    
    
    for r, c in raichu_loc:
        counter = 0 
        board_succ = copy.deepcopy(board2D)
        for i,j in zip(range(r-1, -1, -1),range(c-1,-1,-1)):
            # To check whether or not the next to go index is valid or not.
            if valid_index((i, j), N) and board2D[i][j] == '.':
                board_succ[i][j] = '@'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((i, j), N) and (board2D[i][j] == 'b' or board2D[i][j] == 'B' or board2D[i][j] == '$'):
                for k,l in zip(range(i-1, -1, -1),range(j-1,-1,-1)):
                    if valid_index((k, l), N) and board2D[k][l] == '.':
                        board_succ[r][c] = '.'
                        board_succ[i][j] = '.'
                        board_succ[k][l] = '@'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((i, j), N) and (board2D[i][j] == 'w' or board2D[i][j] == 'W' or board2D[i][j] == '@'):
                counter = 1
                        
            if counter == 1:
                break
                
    # ............................................................................................................. 

    # .............................................................................................................                
    # Left - Down
    
    
    for r, c in raichu_loc:
        counter = 0 
        board_succ = copy.deepcopy(board2D)
        for i,j in zip(range(r+1, N),range(c-1,-1,-1)):
            # To check whether or not the next to go index is valid or not.
            if valid_index((i, j), N) and board2D[i][j] == '.':
                board_succ[i][j] = '@'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((i, j), N) and (board2D[i][j] == 'b' or board2D[i][j] == 'B' or board2D[i][j] == '$'):
                for k,l in zip(range(i+1, N),range(j-1,-1,-1)):
                    if valid_index((k, l), N) and board2D[k][l] == '.':
                        board_succ[r][c] = '.'
                        board_succ[i][j] = '.'
                        board_succ[k][l] = '@'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((i, j), N) and (board2D[i][j] == 'w' or board2D[i][j] == 'W' or board2D[i][j] == '@'):
                counter = 1
                        
            if counter == 1:
                break
                
    # ............................................................................................................. 
    # .............................................................................................................                
    # Right - Up
    
    
    for r, c in raichu_loc:
        counter = 0 
        board_succ = copy.deepcopy(board2D)
        for i,j in zip(range(r-1,-1,-1),range(c+1,N)):
            # To check whether or not the next to go index is valid or not.
            if valid_index((i, j), N) and board2D[i][j] == '.':
                board_succ[i][j] = '@'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((i, j), N) and (board2D[i][j] == 'b' or board2D[i][j] == 'B' or board2D[i][j] == '$'):
                for k,l in zip(range(i-1, -1, -1),range(j+1,N)):
                    if valid_index((k, l), N) and board2D[k][l] == '.':
                        board_succ[r][c] = '.'
                        board_succ[i][j] = '.'
                        board_succ[k][l] = '@'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((i, j), N) and (board2D[i][j] == 'w' or board2D[i][j] == 'W' or board2D[i][j] == '@'):
                counter = 1
                        
            if counter == 1:
                break
                
    # ............................................................................................................. 

    # .............................................................................................................                
    # Right - Down
    
    
    for r, c in raichu_loc:
        counter = 0 
        board_succ = copy.deepcopy(board2D)
        for i,j in zip(range(r+1, N),range(c+1,N)):
            # To check whether or not the next to go index is valid or not.
            if valid_index((i, j), N) and board2D[i][j] == '.':
                board_succ[i][j] = '@'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((i, j), N) and (board2D[i][j] == 'b' or board2D[i][j] == 'B' or board2D[i][j] == '$'):
                for k,l in zip(range(i+1, N),range(j+1,N)):
                    if valid_index((k, l), N) and board2D[k][l] == '.':
                        board_succ[r][c] = '.'
                        board_succ[i][j] = '.'
                        board_succ[k][l] = '@'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((i, j), N) and (board2D[i][j] == 'w' or board2D[i][j] == 'W' or board2D[i][j] == '@'):
                counter = 1
                        
            if counter == 1:
                break
                
    # ............................................................................................................. 

    '''for i in raichu_succ:
        for j in range(len(i)):
            print(i[j])
        print('\n')
        print('\n')
    print('loop')'''
    
    return raichu_succ

def raichu_B(board2D, N ,player):
    raichu_loc=[(row_i, col_i) for col_i in range(len(board2D[0])) for row_i in range(len(board2D)) if board2D[row_i][col_i]=="$"]
    
    raichu_succ = []
    
    board_succ = []
    
    # .............................................................................................................                
    # Left
    
    
    for r, c in raichu_loc:
        counter = 0 
        board_succ = copy.deepcopy(board2D)
        for i in range(c-1, -1, -1):
            # To check whether or not the next to go index is valid or not.
            if valid_index((r, i), N) and board2D[r][i] == '.':
                board_succ[r][i] = '$'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((r, i), N) and (board2D[r][i] == 'w' or board2D[r][i] == 'W' or board2D[r][i] == '@'):
                for k in range(i-1, -1, -1):
                    if valid_index((r, k), N) and board2D[r][k] == '.':
                        board_succ[r][c] = '.'
                        board_succ[r][i] = '.'
                        board_succ[r][k] = '$'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((r, i), N) and (board2D[r][i] == 'b' or board2D[r][i] == 'B' or board2D[r][i] == '$'):
                counter = 1
                        
            if counter == 1:
                break
                
    # .............................................................................................................                
    # Right
    
    
    for r, c in raichu_loc:
        counter = 0 
        board_succ = copy.deepcopy(board2D)
        for i in range(c+1, N):
            # To check whether or not the next to go index is valid or not.
            if valid_index((r, i), N) and board2D[r][i] == '.':
                board_succ[r][i] = '$'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((r, i), N) and (board2D[r][i] == 'w' or board2D[r][i] == 'W' or board2D[r][i] == '@'):
                for k in range(i+1, N):
                    if valid_index((r, k), N) and board2D[r][k] == '.':
                        board_succ[r][c] = '.'
                        board_succ[r][i] = '.'
                        board_succ[r][k] = '$'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((r, i), N) and (board2D[r][i] == 'b' or board2D[r][i] == 'B' or board2D[r][i] == '$'):
                counter = 1
                        
            if counter == 1:
                break
    
    # .............................................................................................................                
    # Top
    
    
    for r, c in raichu_loc:
        counter = 0
        board_succ = copy.deepcopy(board2D)
        for i in range(r-1, -1, -1):
            # To check whether or not the next to go index is valid or not.
            if valid_index((i, c), N) and board2D[i][c] == '.':
                board_succ[i][c] = '$'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((i, c), N) and (board2D[i][c] == 'w' or board2D[i][c] == 'W' or board2D[i][c] == '@'):
                for k in range(i-1, -1, -1):
                    if valid_index((k, c), N) and board2D[k][c] == '.':
                        board_succ[r][c] = '.'
                        board_succ[i][c] = '.'
                        board_succ[k][c] = '$'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((i, c), N) and (board2D[i][c] == 'b' or board2D[i][c] == 'B' or board2D[i][c] == '$'):
                counter = 1
                        
            if counter == 1:
                break
                
    # .............................................................................................................                
    #Bottom
    
    
    for r, c in raichu_loc:
        counter = 0 
        board_succ = copy.deepcopy(board2D)
        for i in range(r+1, N):
            # To check whether or not the next to go index is valid or not.
            if valid_index((i, c), N) and board2D[i][c] == '.':
                board_succ[i][c] = '$'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((i, c), N) and (board2D[i][c] == 'w' or board2D[i][c] == 'W' or board2D[i][c] == '@'):
                for k in range(i+1, N):
                    if valid_index((k, c), N) and board2D[k][c] == '.':
                        board_succ[r][c] = '.'
                        board_succ[i][c] = '.'
                        board_succ[k][c] = '$'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((i, c), N) and (board2D[i][c] == 'b' or board2D[i][c] == 'B' or board2D[i][c] == '$'):
                counter = 1
                        
            if counter == 1:
                break

    # .............................................................................................................                
    # Left - Up
    
    
    for r, c in raichu_loc:
        counter = 0 
        board_succ = copy.deepcopy(board2D)
        for i,j in zip(range(r-1, -1, -1),range(c-1,-1,-1)):
            # To check whether or not the next to go index is valid or not.
            if valid_index((i, j), N) and board2D[i][j] == '.':
                board_succ[i][j] = '$'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((i, j), N) and (board2D[i][j] == 'w' or board2D[i][j] == 'W' or board2D[i][j] == '@'):
                for k,l in zip(range(i-1, -1, -1),range(j-1,-1,-1)):
                    if valid_index((k, l), N) and board2D[k][l] == '.':
                        board_succ[r][c] = '.'
                        board_succ[i][j] = '.'
                        board_succ[k][l] = '$'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((i, j), N) and (board2D[i][j] == 'b' or board2D[i][j] == 'B' or board2D[i][j] == '$'):
                counter = 1
                        
            if counter == 1:
                break
                
    # ............................................................................................................. 

    # .............................................................................................................                
    # Left - Down
    
    
    for r, c in raichu_loc: 
        counter = 0
        board_succ = copy.deepcopy(board2D)
        for i,j in zip(range(r+1, N),range(c-1,-1,-1)):
            # To check whether or not the next to go index is valid or not.
            if valid_index((i, j), N) and board2D[i][j] == '.':
                board_succ[i][j] = '$'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((i, j), N) and (board2D[i][j] == 'w' or board2D[i][j] == 'W' or board2D[i][j] == '@'):
                for k,l in zip(range(i+1, N),range(j-1,-1,-1)):
                    if valid_index((k, l), N) and board2D[k][l] == '.':
                        board_succ[r][c] = '.'
                        board_succ[i][j] = '.'
                        board_succ[k][l] = '$'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((i, j), N) and (board2D[i][j] == 'b' or board2D[i][j] == 'B' or board2D[i][j] == '$'):
                counter = 1
                        
            if counter == 1:
                break
                
    # ............................................................................................................. 
    # .............................................................................................................                
    # Right - Up
    
    
    for r, c in raichu_loc:
        counter = 0 
        board_succ = copy.deepcopy(board2D)
        for i,j in zip(range(r-1,-1,-1),range(c+1,N)):
            # To check whether or not the next to go index is valid or not.
            if valid_index((i, j), N) and board2D[i][j] == '.':
                board_succ[i][j] = '$'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((i, j), N) and (board2D[i][j] == 'w' or board2D[i][j] == 'W' or board2D[i][j] == '@'):
                for k,l in zip(range(i-1, -1, -1),range(j+1,N)):
                    if valid_index((k, l), N) and board2D[k][l] == '.':
                        board_succ[r][c] = '.'
                        board_succ[i][j] = '.'
                        board_succ[k][l] = '$'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((i, j), N) and (board2D[i][j] == 'b' or board2D[i][j] == 'B' or board2D[i][j] == '$'):
                counter = 1
                        
            if counter == 1:
                break
                
    # ............................................................................................................. 

    # .............................................................................................................                
    # Right - Down
    
    
    for r, c in raichu_loc:
        counter = 0 
        board_succ = copy.deepcopy(board2D)
        for i,j in zip(range(r+1, N),range(c+1,N)):
            # To check whether or not the next to go index is valid or not.
            if valid_index((i, j), N) and board2D[i][j] == '.':
                board_succ[i][j] = '$'
                board_succ[r][c] = '.'
                raichu_succ.append(board_succ)
                board_succ = copy.deepcopy(board2D)
                
            elif valid_index((i, j), N) and (board2D[i][j] == 'w' or board2D[i][j] == 'W' or board2D[i][j] == '@'):
                for k,l in zip(range(i+1, N),range(j+1,N)):
                    if valid_index((k, l), N) and board2D[k][l] == '.':
                        board_succ[r][c] = '.'
                        board_succ[i][j] = '.'
                        board_succ[k][l] = '$'
                        raichu_succ.append(board_succ)
                        board_succ = copy.deepcopy(board2D)
                        
                    else:
                        counter = 1
                        break
                counter = 1
                        
            elif valid_index((i, j), N) and (board2D[i][j] == 'b' or board2D[i][j] == 'B' or board2D[i][j] == '$'):
                counter = 1
                        
            if counter == 1:
                break
                
    # ............................................................................................................. 

    '''for i in raichu_succ:
        for j in range(len(i)):
            print(i[j])
        print('\n')
        print('\n')
    print('loop')'''
    
    return raichu_succ


    

    # .............................................................................................................   

# A function that calculates the total points that can be earned depending on the player that has to win.
def cost_calc(board_succ, player):
    result = if_game_end(board_succ)
    
    reward_white = 0
    reward_black = 0
    
    if result == 'w' or result == 'b':
        if player == 'w':
            if result == 'w':
                return +99999
            
            elif result == 'b':
                return -99999
                
        elif player == 'b':
            if result == 'w':
                return -99999
                
            elif result == 'b':
                return +99999
        
    else:
        if player == 'w':
            for i in board_succ:
                for j in range(len(i)):
                    if(j == 'w'):
                        reward_white += 1
                    elif(j == 'W'):
                        reward_white += 2
                    elif(j == '@'):
                        reward_white += 3
                    elif(j == 'b'):
                        reward_white -= 1
                    elif(j == 'B'):
                        reward_white -= 2
                    elif(j == '$'):
                        reward_white -= 3
                        
        elif player == 'b':
            for i in board_succ:
                for j in range(len(i)):
                    if(j == 'w'):
                        reward_black -= 1
                    elif(j == 'W'):
                        reward_black -= 2
                    elif(j == '@'):
                        reward_black -= 3
                    elif(j == 'b'):
                        reward_black += 1
                    elif(j == 'B'):
                        reward_black += 2
                    elif(j == '$'):
                        reward_black += 3
                        
    if player == 'w':
        return reward_white
    
    else:
        return reward_black
    
def get_succ(board, N, player):
    succ = []
    
    if player == 'w':
        succ1 = pichu_w(board, N, player)
        succ2 = pikachu_W(board, N, player)
        succ3 = raichu_W(board, N, player)
        
    elif player == 'b':
        succ1 = pichu_b(board, N, player)
        succ2 = pikachu_B(board, N, player)
        succ3 = raichu_B(board, N, player)
    
    for i in succ1:
        succ.append(i)
        
    for i in succ2:
        succ.append(i)
        
    for i in succ3:
        succ.append(i)
        
    return succ

# To check if the game has ended or not.
def if_game_end(board_succ):
    black_counter = 0
    white_counter = 0
    
    for i in board_succ:
        for j in range(len(i)):
            if i[j] == 'b' or i[j] == 'B' or i[j] == '$':
                black_counter += 1
            
            elif i[j] == 'w' or i[j] == 'W' or i[j] == '@':
                white_counter += 1
    
    victor = 'x'
    # Since, we don't yet know the victor here we gave it 'x' :) as unknown.
    if black_counter == 0:
        victor = 'w'
       
    elif white_counter == 0:
        victor = 'b'
    
    else:
        return None
    
    return victor

# Uses min logic for alpha-beta pruning
def min_cost(curr_level, alpha, beta, player, num_levels, N, succ):
    curr_level += 1
    
    victor = if_game_end(succ)
    
    # Terminal states
    if victor == 'w' or victor == 'b' or curr_level == num_levels:
        reward =  cost_calc(succ, player)
        return reward
    
    else:
        if player == 'w':
            max_succ = get_succ(succ, N, 'b')
            
        elif player == 'b':
            max_succ = get_succ(succ, N, 'w')
        
        for x in max_succ:
            beta = min(beta, max_cost(curr_level, alpha, beta, player, num_levels, N, x))
            
            if alpha >= beta:
                return beta
            
        return beta

# Uses max logic for alpha-beta pruning
def max_cost(curr_level, alpha, beta, player, num_levels, N, succ):
    curr_level += 1
    
    victor = if_game_end(succ)
    
    # Terminal states, but current number of levels can be greater than or equal to number of total levels. :)
    if victor == 'w' or victor == 'b' or curr_level >= num_levels:
        reward =  cost_calc(succ, player)
        return reward
    
    else:
        min_succ = get_succ(succ, N, player)
        
        for x in min_succ:
            alpha = max(alpha, min_cost(curr_level, alpha, beta, player, num_levels, N, x))
            
            if alpha >= beta:
                return alpha
            
        return alpha

# The main min-max function.
def min_max(num_levels, board, N, player):
    curr_level = 0
    
    curr_succ = get_succ(board, N, player)
    
    # Initializing alpha and beta values
    alpha = float('-inf')
    beta = float('inf')
    
    # Although the name says max heap, we will be using min heap but with negative values. Which means that it is actually max heap when traversed :)
    max_heap = []
    
    for x in curr_succ:
        # Here, we multiply the values by -1, in order to convert the generated successors to a max heap like structure from a default min heap formation.
        heapq.heappush(max_heap, ((-1) * (min_cost(curr_level, alpha, beta, player, num_levels, N, x)), x))
        
    return heapq.heappop(max_heap)[1]

# Convert any given 2D matrix to a string.
def matrix_to_string(board):
    board_str = ''
    for i in board:
        for j in range(len(i)):
            board_str += i[j]
            
    return board_str
    
def find_best_move(board, N, player, timelimit):
    # This sample code just returns the same board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!
    #
    
    num_levels = 0
    
    board2D = conv_2D(board, N)
    
    #print('Initial')
    #print(board2D)
    
#     start_time = time.time()
#     print(start_time)
    
    while True:
        #time.sleep(1)
        
#         if((int(time.time()) - int(start_time)) > timelimit):
#             print(time.time())
#             sys.exit(0)
            
        result = min_max(num_levels, board2D, N, player)
        
        # To convert back to string in order to display result
        result_string = matrix_to_string(result)
        
        num_levels += 1
        
        yield result_string
        
        #yield board


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")
        
    (_, N, player, board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    for new_board in find_best_move(board, N, player, timelimit):
        print(new_board)
