''' TO DO LIST:
Board Class:
- initialize board with row and column # not necessary
- setup_board - ask user how many rows and columns to play with - Done
- make_board - Done
- print_board - Done


- make_move - Matteo
- valid_location + place to first available row
- check_horizontal - Patrick 
- check_vertical - Patrick 
- check_pos_diag - Patrick
- check_neg_diag - Patrick
- is_game_over - check if check functions above return True
- restart_game - TO DO


User Class: - Philipp
- initialize user (name, last_name, symbol) ### symbol either X or O
- get_name
- ask_input - returns column number
- ...

Score_Board Class: - Philipp
- 

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


#Imports
import pandas as pd


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




    def check_line_win(self):

        #Assumptions:
        ##The board is 7x7
        ##X and O are the only chip options

        df = pd.DataFrame(data = board.dict_moves).transpose()
        inv_dict = df.to_dict()

        for iteration in board.dict_moves.keys():
            #horizontal wins
            line = board.dict_moves[iteration].values()
            line_string = "".join(line)

            #vertical wins
            column = inv_dict[iteration].values()
            column_string = "".join(column)


            if (line_string.find("XXXX") >= 0 or column_string.find("XXXX") >= 0):
                return "X wins"
            if (line_string.find("OOOO") >= 0 or column_string.find("OOOO") >= 0):
                return "O wins"



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

#g = Board()

#g.make_a_move(2, 'O')
#g.printBoard()

class User:
    '''User class that defines the names and symbols of user and contains the user functionalities'''
    def __init__(self, first_name, last_name, symbol):
        self.first_name = first_name
        self.last_name = last_name
        self.symbol = symbol

    @classmethod
    def get_user_input(cls):
        '''User information method that gets the input from users'''
        
        return cls(str(input('Please enter your first name: ')),
        str(input('Please enter your last name: ')),
        str(input('Please enter your symbol (X or O): ')))
        # To add in game functionality:
        # -> if user1 picks "X" or "O" as their symbol, user2 automatically gets assigned the other symbol (can't add this in a class method)

    
    def ask_column(self):
        '''Column function that gets the played column of the users'''

        column = int(input("It's your turn {}. In which column do you want to place your stone? (1-7) ".format(self.first_name)))
        return column   

class Game:
    def __init__(self):
        self.board = Board()
        
        print("Player 1 Information:")
        first_name_1 = str(input('Please enter your first name: '))
        last_name_1 = str(input('Please enter your last name: '))
        symbol_1 = str(input('Please enter your symbol (X or O): '))
        self.user_1 = User(first_name_1, last_name_1, symbol_1)
        
        print("Player 2 Information:")
        first_name_2 = str(input('Please enter your first name: '))
        last_name_2 = str(input('Please enter your last name: '))
        
        if symbol_1 == "X":
            symbol_2 = "O"
        else: 
            symbol_2 = "X"
        
        self.user_2 = User(first_name_2, last_name_2, symbol_2)
        
    
    def lets_play(self):
        win = False
        player = 1

        while win == False:
            if player == 1:
                self.choose_move(self.user_1)
                win = self.check_result()
                if win == True:
                    self.end_game(self.user_1.first_name)
                else:
                    player += 1
            elif player == 2:
                self.choose_move(self.user_2)
                result = self.board.check_line_win()
                if win == True:
                    self.end_game(self.user_2.first_name)
                else:
                    player -= 1
    
    
    
    def choose_move(self, player):
        self.board.printBoard()
        print("_________________________________")
        print(player.first_name + ", it's your turn!")
        print("---------------------------------")
        column = int(input('Please enter column: '))
        print("---------------------------------")
        move = self.board.make_a_move(column, player.symbol)

        while move == 'All the spaces in this column are full. Try another column':
            print(move)
            column = int(input('Please enter column: '))
            move = self.board.make_a_move(column, player.symbol)
                      
            
    def check_result(self):
        result = self.board.check_line_win()
        if result == "X wins":
            return(True)
        elif result == "O wins":
            return(True)
        else:
            return(False)
        
            
    def end_game(self, player_name):
        print("Game over!")
        print(player_name + " has won the game!") 
        

if __name__ == "__main__": 
    # Matteo G. and Levin
    Game().lets_play()

    # Testing user class in other game and board classes
    user1 = User.get_user_input()
    print(user1.first_name)

    user2 = User.get_user_input()
    print(user2.first_name)

    column1 = user1.ask_column()
    print(column1)

    column2 = user2.ask_column()
    print(column2)

    board = Board()
    board.make_a_move(column1,user1.symbol)
    board.make_a_move(column2,user2.symbol)
    board.printBoard()

    #Testing for the checking_line_win function
    board = Board()
    board.make_a_move(1,"X")
    board.make_a_move(2,"O")
    board.make_a_move(2,"X")
    board.make_a_move(3,"O")
    board.make_a_move(3,"O")
    board.make_a_move(3,"X")
    board.make_a_move(4,"O")
    board.make_a_move(4,"O")
    board.make_a_move(4,"O")
    board.make_a_move(4,"X")
    board.make_a_move(5,"O")
    board.printBoard()

    board.check_line_win()


    is_game_over = False
    count_turns = 0
    while is_game_over == False:
        ### ask for user input
        count_turns +=1
        is_game_over = True
        


    while is_game_over == False:
        ### Game dynamics 
        count_turns +=1
        
        # remove below
        if count_turns == 5:
            is_game_over = True
