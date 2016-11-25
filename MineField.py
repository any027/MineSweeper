import random

#MineField.py contains the board or "minefield" of minesweeper.
#Here, we will generate the board and the mines.

class MineField():

    minefield = []
    
    #init function, does all the things a minefield needs to be initialized
    #properly
    def __init__(self, difficulty):
        makeBoard(difficulty)
        
    #makeBoard, given a difficulty(an int), it will create a board of 
    #appropriate size.
    def makeBoard(self, difficulty):
        #difficulty 1 = easy
        if difficulty == 1:
            mineField = [8][8]
        #difficulty 2 = intermdiate
        if difficulty == 2:
            mineField = [16][16]
        #difficulty 3 = hard
        if difficulty == 3:
            mineField = [16][30]

            
    def clearBoard(self):
        
        

