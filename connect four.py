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