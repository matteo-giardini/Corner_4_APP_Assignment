''' TO DO LIST:
Board Class:
- initialize board with row and column
- setup_board - ask user how many rows and columns to play with
- make_board (if we do graphics, if we dont, let's draw it on the terminal)
- update_board (maybe necessary (??), takes as input old board, new move and returns new board)

- make_move
- valid_location + place to first available row
- check_horizontal
- check_vertical
- check_pos_diag
- check_neg_diag
- is_game_over - check if check functions above return True


User Class:
- initialize user (name, last_name, age, color (if we do graphics))
- get_name
- ask_input - returns column number
- ...

'''

### Connect_4_VF.py
# MIT License
# 
# Copyright (c) 2022 Patrick Peled, Matteo Augenti, Matteo Giardini, Ben Levin Bauschke, Philipp Baumanns
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.




class Board:

    def __init__(self): #When the Board class is initialized the dictionary containing the moves is empty
        
        self.dict_moves = {1 : {1 : ' ', 2 : ' ', 3 : ' ', 4 : ' ', 5 : ' ', 6 : ' ', 7 : ' '}, #Dictionary that contains the value inside each one of the boxes
        2 : {1 : ' ', 2 : ' ', 3 : ' ', 4 : ' ', 5 : ' ', 6 : ' ', 7 : ' '}, #Inside the dictionary, every dictionary contains the values saved inside the line
        3 : {1 : ' ', 2 : ' ', 3 : ' ', 4 : ' ', 5 : ' ', 6 : ' ', 7 : ' '},
        4 : {1 : ' ', 2 : ' ', 3 : ' ', 4 : ' ', 5 : ' ', 6 : ' ', 7 : ' '},
        5: {1 : ' ', 2 : ' ', 3 : ' ', 4 : ' ', 5 : ' ', 6 : ' ', 7 : ' '},
        6: {1 : ' ', 2 : ' ', 3 : ' ', 4 : ' ', 5 : ' ', 6 : ' ', 7 : ' '},
        7: {1 : ' ', 2 : ' ', 3 : ' ', 4 : ' ', 5 : ' ', 6 : ' ', 7 : ' '}
        }

    def make_a_move(self, column, player): 
        '''This function places the move (i.e. symbol of a player) in a given column in the lowest available spot'''
        for line in sorted(list(range(8)), reverse=True): #This for loop checks the lines starting from the bottom one and places the player sign the the lowest  empty one
            if line > 0:
                if self.dict_moves[line][column] == ' ':
                    self.dict_moves[line][column] = player
                    break
            else:
                print('All the spaces in this column are full. Try another column') #If the loop reaches 8 it means the column is full
    
    def printBoard(self):
        self.dict_board = {'roof' : '_______________', #the dict board is updated with the new values
        1 : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(self.dict_moves[1].values())),
        2 : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(self.dict_moves[2].values())),
        3 : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(self.dict_moves[3].values())),
        4 : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(self.dict_moves[4].values())),
        5 : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(self.dict_moves[5].values())),
        6 : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(self.dict_moves[6].values())),
        7 : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(self.dict_moves[7].values())),
        'bottom' : '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯'}
        for line in self.dict_board.keys(): #This for loop prints the dict_board line by line
            print(self.dict_board[line])

g = Board()

g.make_a_move(2, 'O')
g.printBoard()