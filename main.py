from pathlib import Path
import random
import sys
import time
import ast

import scipy.ndimage
import numpy

def random_board_generator(x, y):
    """Generate random board of two number inputs"""
    random_board = [[random.randint(0, 1) for j in range(int(y))] 
    for i in range(int(x))]
    return random_board

def cell_status(cell, neighbors_sum):
    """Changing status of cell depending on neighbors around"""
    if cell == 1:
        if neighbors_sum < 2 or neighbors_sum > 3:
            cell = 0
        else:
            pass
    else:
        if neighbors_sum == 3:
            cell = 1
    return cell
    
def neighbors(board, xy):
    """Return a sum of cell neighbors"""
    matrix = numpy.array(board)
    indices = tuple(numpy.transpose(numpy.atleast_2d(xy)))
    arr_shape = numpy.shape(matrix)
    dist = numpy.ones(arr_shape)
    dist[indices] = 0
    dist = scipy.ndimage.distance_transform_cdt(dist, 
    metric='chessboard')
    nb_indices = numpy.transpose(numpy.nonzero(dist == 1))
    return sum([matrix[tuple(ind)] for ind in nb_indices])
            
def turns(board):
    """New status of cell in board"""
    new_board = []
    for i in range(len(board)):
        row = board[i]
        new_row = []
        for j in range(len(row)):
            cell = row[j]
            cell_n = neighbors(board, [i, j])
            new_cell = cell_status(cell, cell_n)
            new_row.append(new_cell)
        new_board.append(new_row)
    return new_board
   

if __name__ == '__main__':
    while True:
        # Loop to choose board input or generate random
        user_input = input("Do you have prepared board in file (Y/N)? ")
        if user_input in ["Y", "y"]:
            print("Board should be a nested 2D matrix list, like this:")
            print("[[0, 0, 0], [1, 1, 1], [0, 0, 0]]")
            while True:
                file_input = input("Well, enter the file destination and name: ")
                
                # Checking valid file path and name
                if Path(file_input).exists() == True:
                    try:
                        # Open and check file for syntax errors
                        with open(file_input, 'r') as f:
                            board = ast.literal_eval(f.read())
                            # Check if board a list
                            if isinstance(board, list):
                                break
                            else:
                                print("Wrong board format. Try another")
                    except SyntaxError:
                        print("Wrong board format. Try another")
                        pass
                else:
                    print("This file doesn't exist. Try again")
            break
        elif user_input in ["N", "n"]:
            M = random.randint(0, 42)
            N = random.randint(0, 42)
            board = random_board_generator(M, N)
            break
        else:
            print("Wrong answer, try again")
    while True:
        # Updating board until the end of time
        time.sleep(1)
        board = turns(board)
        # Pretty representation of board
        print("\n")
        for r in board:
            print(*r, sep=' ')
