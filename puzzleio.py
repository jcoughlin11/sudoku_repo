"""
Title:   io.py
Author:  Jared Coughlin
Date:    12/21/19
Purpose: Functions for parsing command-line arguments, loading puzzles,
            and saving puzzles.
Notes:   
"""
import argparse
import sys

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
