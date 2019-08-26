import pygame

class Board:
    
    #Constructor
    def __init__(self, row, col):
        """
            :param "row": number of rows in the board game.\n
            :param "col": number of columns in the board game.
        """
        pass

    #Statics Methods
    def prettyPrint(boardGame):
        """
            Prints a prettier board game in the console.\n  
            :param "board_game": A matrix of size (row, col).
        """
        pass

    #Methods
    def drawBoard(self):
        """
            Returns a board game.\n
        """
        pass

    def drawBoardPygame(self, screen): 
       """
            Displays the Puissance 4 board.\n
            :param "screen": The Puissance 4 screen.
        """
       
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(0, 100, 700, 700))
        for i in range(self.col):
            for j in range(self.row):
                pygame.draw.circle(screen, (0, 0, 0), 
                 (i*100 + 50, (j+1)*100 + 50), 40)
        

    def checkHorizontal(self, boardGame, playerCoin, col):
        """
            Returns True if there is a connect 4 horizontally.\n
            :param "boardGame": a matrix of size (row, col).\n
            :param "playerCoin": player coin, either 1 or 2.\n
            :param "col": position of the coin.
        """
        pass

    def checkVertical(self, boardGame, playerCoin, col):
        """
            Returns True if there is a connect 4 vertically.\n
            :param "boardGame": a matrix of size (row, col).\n
            :param "playerCoin": player coin, either 1 or 2.\n
            :param "col": position of the coin.
        """

        pass     
    
    def checkDiagonal(self, boardGame, playerCoin, col):
        """
            Returns True if there is a connect 4 diagonally.\n
            :param "boardGame": a matrix of size (row, col).\n
            :param "playerCoin": player coin, either 1 or 2.\n
            :param "col": position of the coin.
        """
        pass



        
        

