"""
Title:   sudoku.py
Author:  Jared Coughlin
Date:    12/21/19
Purpose: Solve a sudoku problem via backtracking.
Notes:   https://www.geeksforgeeks.org/sudoku-backtracking-7/
"""
import argparse

import numpy as np


#============================================
#              parse_cl_args
#============================================
def parse_cl_args():
    """
    Collects the passed in command-line args.

    Parameters:
    -----------
        None

    Raises:
    -------
        pass

    Returns:
    --------
        clArgs : argparse.Namespace
            Object containing the values of the command-line args.
    """
    # Instantiate the parser
    parser = argparse.ArgumentParser()
    # Set up the allowed arguments
    parser.add_argument(
        'boardFile',
        help="Name of the file containing the problem to solve."
    )
    # Parse
    clArgs = parser.parse_args()
    return clArgs


#============================================
#                load_board
#============================================
def load_board(boardFile):
    """
    Loads in a sudoku problem from the specified file.

    The problem should be formatted in a grid, with zeros used to
    represent empty cells.

    Parameters:
    -----------
        boardFile : str

    Raises:
    -------
        pass

    Returns:
    --------
        board : ndarray
            The loaded problem in matrix form.
    """
    try:
        board = np.loadtxt(boardFile, dtype=int)
    except OSError:
        print("Could not load {}".format(boardFile))
        sys.exit(1)
    # Validate shape
    if board.shape != (9, 9):
        print("Invalid board shape {}, must be (9, 9)".format(board.shape))
        sys.exit(1)
    return board


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
#               valid_row
#============================================
def valid_row(row, num):
    """
    Checks for the presence of the number num in the array of values
    row.

    Parameters:
    -----------
        row : ndarray
            Values currently occupying the current row of the puzzle.

        num : int
            The number we're checking for.

    Raises:
    -------
        pass

    Returns:
    --------
        pass
    """
    if num in row:
        return False 
    else:
        return True 


#============================================
#               valid_col
#============================================
def valid_col(col, num):
    """
    Checks for the presence of the number num in the array of values
    col.

    Parameters:
    -----------
        col : ndarray
            Values currently occupying the current col of the puzzle.

        num : int
            The number we're checking for.

    Raises:
    -------
        pass

    Returns:
    --------
        pass
    """
    if num in col:
        return False 
    else:
        return True 


#============================================
#               valid_subgrid
#============================================
def valid_subgrid(board, curCell, num):
    """
    Checks for the presence of the number num in the given 3x3 subgrid
    of the board.

    Parameters:
    -----------
        pass

    Raises:
    -------
        pass

    Returns:
    --------
        pass
    """
    # Figure out the bounds of the subgrid containing curCell
    start = (np.array(curCell, dtype=int) // 3) * 3
    end = start + 3
    # Check for num's presence in the subgrid
    if num in board[start[0]:end[0], start[1]:end[1]]:
        return False
    else:
        return True


#============================================
#                num_is_valid
#============================================
def num_is_valid(board, curCell, num):
    """
    Driver routine for making sure the given number doesn't already
    exist in the current row, column, or 3x3 subgrid.

    Parameters:
    -----------
        board : ndarray
            Current state of the puzzle.

        curCell : tuple
            The row-column index pair for the current cell under
            consideration.

        num : int
            The number we're trying to place into curCell.

    Raises:
    -------
        pass

    Returns:
    --------
        pass
    """
    # Check the row
    if valid_row(board[curCell[0]], num):
        # Check the column
        if valid_col(board[:, curCell[1]], num):
            # Check the subgrid
            if valid_subgrid(board, curCell, num):
                return True
    return False


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


#============================================
#                   main
#============================================
def main():
    """
    Driver function.

    Parameters:
    -----------
        None

    Raises:
    -------
        None

    Returns:
    --------
        None
    """
    # Parse the command-line arguments
    clArgs = parse_cl_args()
    # Load the board from the passed file
    board = load_board(clArgs.boardFile)
    # Solve the board
    solved, board = solve_board(board)
    if solved:
        print(board)
    else:
        print("Could not solve.")


if __name__ == '__main__':
    main()
