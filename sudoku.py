"""
Title:   sudoku.py
Author:  Jared Coughlin
Date:    12/21/19
Purpose: Solve a sudoku problem via backtracking.
Notes:   https://www.geeksforgeeks.org/sudoku-backtracking-7/
"""
import numpy as np


#============================================
#           find_next_empty_cell
#============================================
def find_next_empty_cell(board):
    """
    Loops over the board row-by-row until the first empty cell is
    found. An empty cell is denoted with a 0.

    Parameters:
    -----------
        board : ndarray

    Raises:
    -------
        pass

    Returns:
    --------
        pass
    """
    # Get the indices of every empty cell
    emptyInds = np.where(board == 0)
    # np.where returns a tuple of ndarrays (ndarray0, ndarray1, ...),
    # where each ndarray corresponds to the value of the index along
    # that dimension. E.g., if a = np.array([[1,2,3], [4, 3, 6]]) and
    # you do inds = np.where(a == 3), inds = ([0, 1], [2, 1])
    # corresponding to the pairs (0, 2) and (1, 1)
    emptyInds = list(zip(emptyInds[0], emptyInds[1]))
    # If no empty cells were found, return None
    if len(emptyInds) == 0:
        return None
    else:
        return emptyInds[0]


#============================================
#               solve_board
#============================================
def solve_board(board):
    """
    Driver routine for solving the given puzzle via backtracking.

    Parameters:
    -----------
        board : ndarray
            The puzzle to be solved.

    Raises:
    -------
        pass

    Returns:
    --------
        pass
    """
    # Find empty cell. It's possible that there aren't any, in which
    # case, there's nothing left to do
    curCell = find_next_empty_cell(board)
    if curCell is None:
        return True, board
    # Loop over every possible number
    for num in range(1, 10):
        # Check to see if the current number is allowed in the current
        # cell
        if num_is_valid(board, curCell, num):
            # Make the assignment
            board[curCell] = num
            # Repeat the process
            solved, board = solve_board(board)
            if solved:
                return True, board
            # If solving fails, then num must not be the right number
            # for the current cell, so we reset that cell and try the
            # next number
            else:
                board[curCell] = 0
    # If we're here, then it means we looped over every number and did
    # not get a valid solution. This triggers the backtracking
    return False, board
