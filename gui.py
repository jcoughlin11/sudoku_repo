"""
Title:   gui.py
Author:  Jared Coughlin
Date:    12/21/19
Purpose: Contains the main game and gui logic for sudoku.
Notes:
"""
import pygame


#============================================
#                   Game
#============================================
class Game:
    """
    Sudoku game manager class.

    Attributes:
    -----------
        pass

    Methods:
    --------
        pass
    """
    #-----
    # constructor
    #-----
    def __init__(self, board, solvedBoard):
        """
        Sets up the display.

        Parameters:
        -----------
            board : ndarray
                The input puzzle. Zeros represent empty cells.

            solvedBoard : ndarray
                The solved puzzle. Used for checking player's input.

        Raises:
        -------
            pass

        Returns:
        --------
            None
        """
        pygame.init()
        self.board = board
        self.solvedBoard = solvedBoard
        self.done = False
        self.screenSize = [640, 480]
        self.screen = pygame.display.set_mode(self.screenSize)
        self.clock = pygame.time.Clock()
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.grey = pygame.Color(121, 121, 121)

    #-----
    # play
    #-----
    def play(self):
        """
        Contains the main game loop.

        Parameters:
        -----------
            None

        Raises:
        -------
            pass

        Returns:
        --------
            None
        """
        while not self.done:
            # Get player input
            event = pygame.event.poll()
            # Handle player input
            self.handle_event(event)
            # Display current game state to the screen
            self.display()

    #-----
    # handle_event
    #-----
    def handle_event(self, event):
        """
        Doc string.

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
        # Quitting event
        if event.type == pygame.QUIT:
            self.done = True

    #-----
    # display
    #-----
    def display(self):
        """
        Doc string.

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
        # Background
        self.screen.fill(self.white)
