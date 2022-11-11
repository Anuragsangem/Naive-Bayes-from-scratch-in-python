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

def conv_2D(board, N):
        
    board2D = []
    
    for i in range(N):
        board2D.append(list(board[i*N:N+N*i]))
        
    return board2D

def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))

def valid_index(pichu_loc, N):
        return 0 <= pichu_loc[0] < N  and 0 <= pichu_loc[1] < N
                    
def pichu_w(board2D, N ,player):
    pichu_loc=[(row_i, col_i) for col_i in range(len(board2D[0])) for row_i in range(len(board2D)) if board2D[row_i][col_i]=="w"]
    
    pichu_succ = []
    
    board_succ = []
    
    for r, c in pichu_loc:
        board_succ = copy.deepcopy(board2D)
        if valid_index((r + 1, c - 1), N):
            if board2D[r + 1][c - 1] == '.' and ((r + 1) == (N - 1)):
                board_succ[r + 1][c - 1] = '@'
                board_succ[r][c] = '.'
                pichu_succ.append(board_succ)
                
            elif board2D[r + 1][c - 1] == '.' and ((r + 1) != (N - 1)):
                board_succ[r + 1][c - 1] = 'w'
                board_succ[r][c] = '.'
                pichu_succ.append(board_succ)
                
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
        if valid_index((r + 1, c + 1), N):
            if board2D[r + 1][c + 1] == '.' and ((r + 1) == (N - 1)):
                board_succ[r + 1][c + 1] = '@'
                board_succ[r][c] = '.'                                               
                pichu_succ.append(board_succ)
                    
            elif board2D[r + 1][c + 1] == '.' and ((r + 1) != (N - 1)):
                board_succ[r + 1][c + 1] = 'w'
                board_succ[r][c] = '.'
                pichu_succ.append(board_succ)
            
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
    
    for i in pichu_succ:
        for j in range(len(i)):
            print(i[j])
        print('\n')
        print('\n')
    print('loop')
    
    return pichu_succ

def pichu_b(board2D, N ,player):
    pichu_loc=[(row_i, col_i) for col_i in range(len(board2D[0])) for row_i in range(len(board2D)) if board2D[row_i][col_i]=="b"]
    
    pichu_succ = []
    
    board_succ = []
    
    for r, c in pichu_loc:
        board_succ = copy.deepcopy(board2D)
        if valid_index((r - 1, c - 1), N):
            if board2D[r - 1][c - 1] == '.' and ((r - 1) == 0):
                board_succ[r - 1][c - 1] = '$'
                board_succ[r][c] = '.'
                pichu_succ.append(board_succ)
                
            elif board2D[r - 1][c - 1] == '.' and ((r - 1) != 0):
                board_succ[r - 1][c - 1] = 'b'
                board_succ[r][c] = '.'
                pichu_succ.append(board_succ)
            
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
        if valid_index((r - 1, c + 1), N):
            if board2D[r - 1][c + 1] == '.' and ((r - 1) == 0):
                board_succ[r - 1][c + 1] = '$'
                board_succ[r][c] = '.'                                               
                pichu_succ.append(board_succ)
                
            elif board2D[r - 1][c + 1] == '.' and ((r - 1) != 0):
                board_succ[r - 1][c + 1] = 'b'
                board_succ[r][c] = '.'                                               
                pichu_succ.append(board_succ)
            
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
                
    for i in pichu_succ:
        for j in range(len(i)):
            print(i[j])
        print('\n')
        print('\n')
    print('loop')
    
    return pichu_succ

def pikachu_W(board2D, N ,player):
    pikachu_loc=[(row_i, col_i) for col_i in range(len(board2D[0])) for row_i in range(len(board2D)) if board2D[row_i][col_i]=="W"]
    
    pikachu_succ = []
    
    board_succ = []
    
    # .............................................................................................................                
    # Left
    
    for r, c in pikachu_loc: 
        board_succ = copy.deepcopy(board2D)
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
                
            
                
    for i in pikachu_succ:
        for j in range(len(i)):
            print(i[j])
        print('\n')
        print('\n')
    print('loop')
    
    return pikachu_succ

def pikachu_B(board2D, N ,player):
    pikachu_loc=[(row_i, col_i) for col_i in range(len(board2D[0])) for row_i in range(len(board2D)) if board2D[row_i][col_i]=="B"]
    
    pikachu_succ = []
    
    board_succ = []
    
    # .............................................................................................................                
    # Left
    
    for r, c in pikachu_loc: 
        board_succ = copy.deepcopy(board2D)
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
                
            
                
    for i in pikachu_succ:
        for j in range(len(i)):
            print(i[j])
        print('\n')
        print('\n')
    print('loop')
    
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

    for i in raichu_succ:
        for j in range(len(i)):
            print(i[j])
        print('\n')
        print('\n')
    print('loop')
    
    return raichu_succ

'''def test():
    for i in range(5):
        for j in range(5):
            if i == 0 and j == 0:
                print('yes')
            elif i == 5 and j == 5:
                print('no')
            else:
                break
        for k in range(2):
            print('unagi')
            
    for i in range(2):
        print('yea')
        if i == 1:
            break
            
    return 1'''

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

    for i in raichu_succ:
        for j in range(len(i)):
            print(i[j])
        print('\n')
        print('\n')
    print('loop')
    
    #return raichu_succ


    

    # .............................................................................................................   

'''
def cost_calc():
    
    return reward
'''

'''
player = w
w, W, @

player = b
b, B, $
'''

def find_best_move(board, N, player, timelimit):
    # This sample code just returns the same board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!
    #
    
    fringe = []
    
    board2D = conv_2D(board, N)
    
    print('Initial')
    print(board2D)
    
    while True:
        time.sleep(1)
        
        #y = test()
        
        x = pikachu_B(board2D, N, player)
        
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
