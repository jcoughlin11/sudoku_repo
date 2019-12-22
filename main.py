"""
Title:   main.py
Author:  Jared Coughlin
Date:    12/21/19
Purpose: Solve a sudoku problem via backtracking.
Notes:   https://www.geeksforgeeks.org/sudoku-backtracking-7/
"""
import gui
import puzzleio as io 
import sudoku


#============================================
#                   main
#============================================
def main():
    """
    Driver function for playing sudoku.

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
    clArgs = io.parse_cl_args()
    # Load the board from the passed file
    board = io.load_board(clArgs.boardFile)
    # Solve the board
    solved, solvedBoard = sudoku.solve_board(board)
    # Play game
    if solved:
        game = gui.Game(board, solvedBoard)
        game.play()
    else:
        print("Puzzle has no solution.")


if __name__ == '__main__':
    main()
