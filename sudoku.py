"""
Title:   sudoku.py
Author:  Jared Coughlin
Date:    12/21/19
Purpose: Solve a sudoku problem via backtracking.
Notes:   https://www.geeksforgeeks.org/sudoku-backtracking-7/
"""


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
    board = solve_board(board)
    # Print
    print_board(board)


if __name__ == '__main__':
    main()
