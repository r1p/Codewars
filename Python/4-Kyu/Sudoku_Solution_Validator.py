'''
Description:
Sudoku Background

Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)
Sudoku Solution Validator

Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
Examples

validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true

validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); // => false

Categories:
#DataStructures #Algorithms

Solve date:
16 Jul 2022
'''

import numpy as np

def valid_solution(board):
    # Checking for zeros on the board
    for x in range(0, 9):
        if 0 in board[x]: return False

    # Checking for repetition in rows
    for x in range(0, 9):
        if len(set(board[x])) < 9: return False
    
    # Moving rows to columns
    reversedList = np.array(board).T.tolist()
    
    # Checking for repetition in columns
    for x in range(0, 9):
        if len(set(np.array(board).T.tolist()[x])) < 9: return False
    
    # Splitting board in 9 3x3 squares (or blocks)
    squares = []
    
    # Getting the squares of the 3 top rows
    top_squares = []
    for x in range(0, 9, 3):
        for y in board[0:3]:
            for z in y[x:x+3]:
                top_squares.append(z)
     
    # Getting the squares of the 3 mid rows
    mid_squares = []
    for x in range(0, 9, 3):
        for y in board[3:6]:
            for z in y[x:x+3]:
                mid_squares.append(z)
    
    # Getting the squares of the 3 low rows
    
    low_squares = []
    for x in range(0, 9, 3):
        for y in board[6:9]:
            for z in y[x:x+3]:
                low_squares.append(z)
    
    for i in range(0, 27, 9):
        x = i
        squares.append(top_squares[x:x+9])
        squares.append(mid_squares[x:x+9])
        squares.append(low_squares[x:x+9])
    
    for x in range(0, 9):
        if len(set(squares[x])) < 9: return False
    

    return True
