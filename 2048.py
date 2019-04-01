"""
Clone of 2048 game.
To play the game go to
http://www.codeskulptor.org
and clear the screen and copy and past this code 
"""

import poc_2048_gui
import random
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code from the previous mini-project
    new_list= []
    count =0
    for item in line:
        if item:
            new_list.append(item)
        else:
            count +=1
    for index in range(count):
        new_list.append(0)
    for index in range(0, len(new_list)-1):
        if new_list[index] == new_list[index+1]:
            new_list[index] += new_list[index+1]
            
            for index2 in range(index+1, len(line)-1):
                new_list[index2]= new_list[index2+1]
            new_list[-1] =0
    return new_list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # setting initial height and width
        self.height = grid_height
        self.width = grid_width
        self.board = [[0 for col in range(grid_width)]
                        for row in range(grid_height)]
        self.reset()
       
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.board = [[0 for col in range(self.width)]
                        for row in range(self.height)]
        self.new_tile()
        self.new_tile()
        
        
        

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        board = ""
        for row in range(self.height):
            board += str(self.board[row]) +"\n"
        return board

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        
        if direction == 1or direction == 2:
            
            for col in range(self.width):
                my_list = []
                for row in range(self.height):
                    my_list.append(self.board[row][col])
               
                if direction == 2:
                    my_list.reverse()
               
                my_list = merge(my_list)
                if direction == 2:
                    my_list.reverse()
                
                for row in range(self.height):
                     self.board[row][col] = my_list[row]
               
        if direction == 3 or direction == 4:
            
            for row in range(self.height):
                my_list = []
                for col in range(self.width):
                    my_list.append(self.board[row][col])
                
                if direction == 4:
                    my_list.reverse()
                
                my_list = merge(my_list)
                if direction == 4:
                    my_list.reverse()
                
                for col in range(self.width):
                     self.board[row][col] = my_list[col]
                
        self.new_tile()       
       
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        starter_list = [2,2,2,2,random.choice([2,4])]*2
        space = True
        while space:
            row = random.randint(0, self.height-1)
            col = random.randint(0, self.width-1)
            if self.board[row][col] == 0:
                self.board[row][col] = random.choice(starter_list)
                space = False
                

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self.board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.board[row][col]





       
    
    

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))