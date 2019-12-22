"""
Title:   validation.py
Author:  Jared Coughlin
Date:    12/21/19
Purpose: Functions for checking if a number can go in a given cell
Notes:   
"""
import numpy as np


#============================================
#                 valid_1d
#============================================
def valid_1d(numList, num):
    """
    Checks for the presence of the number num in the array of values
    row.

    Parameters:
    -----------
        numList : ndarray
            Values currently occupying the current row or columnof the
            puzzle.

        num : int
            The number we're checking for.

    Raises:
    -------
        pass

    Returns:
    --------
        pass
    """
    if num in numList:
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
    if valid_1d(board[curCell[0]], num):
        # Check the column
        if valid_1d(board[:, curCell[1]], num):
            # Check the subgrid
            if valid_subgrid(board, curCell, num):
                return True
    return False
