dict_moves = {'line1': {'a' : ' ','b' : ' ','c' : ' ','d' : ' ','e' : ' ','f' : ' ','g' : ' '}, #Dictionary that contains the value inside each one of the boxes
'line2': {'a' : ' ','b' : ' ','c' : ' ','d' : ' ','e' : ' ','f' : ' ','g' : ' '}, #Inside the dictionary, every dictionary contains the values saved inside the line
'line3': {'a' : ' ','b' : ' ','c' : ' ','d' : ' ','e' : ' ','f' : ' ','g' : ' '},
'line4': {'a' : ' ','b' : ' ','c' : ' ','d' : ' ','e' : ' ','f' : ' ','g' : ' '},
'line5': {'a' : ' ','b' : ' ','c' : ' ','d' : ' ','e' : ' ','f' : ' ','g' : ' '},
'line6': {'a' : ' ','b' : ' ','c' : ' ','d' : ' ','e' : ' ','f' : ' ','g' : ' '},
'line7': {'a' : ' ','b' : ' ','c' : ' ','d' : ' ','e' : ' ','f' : ' ','g' : ' '}
}

dict_board ={'roof' : '_______________', #Dicionary that contains the graphical output of the moves
'line1' : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(dict_moves['line1'].values())), #Each line is formatted with the values contained in the dict_moves dictionary
'line2' : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(dict_moves['line2'].values())),
'line3' : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(dict_moves['line3'].values())),
'line4' : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(dict_moves['line4'].values())),
'line5' : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(dict_moves['line5'].values())),
'line6' : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(dict_moves['line6'].values())),
'line7' : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(dict_moves['line7'].values())),
'bottom' : '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯'}

for line in dict_board.keys(): #This for loop prints the dict_board line by line
    print(dict_board[line])

lines_list = [ 'line7', 'line6', 'line5', 'line4', 'line3', 'line2', 'line1'] #List containing the lines of the dict_moves in order to check them from lower to higher

player = 'O' #Placeholer, until we develop the 'makeMove' function
column = 'e'

for line in lines_list: #This for loop checks the lines starting from the bottom one and places the player sign the the lowest  empty one
    if dict_moves[line][column] == ' ':
        dict_moves[line][column] = player
        break
    

dict_board ={'roof' : '_______________', #the dict board is updated with the new values
'line1' : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(dict_moves['line1'].values())),
'line2' : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(dict_moves['line2'].values())),
'line3' : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(dict_moves['line3'].values())),
'line4' : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(dict_moves['line4'].values())),
'line5' : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(dict_moves['line5'].values())),
'line6' : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(dict_moves['line6'].values())),
'line7' : '|{}|{}|{}|{}|{}|{}|{}|'.format(*list(dict_moves['line7'].values())),
'bottom' : '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯'}

for line in dict_board.keys(): #This for loop prints the dict_board line by line
                print(dict_board[line])