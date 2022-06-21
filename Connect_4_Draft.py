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


def main():
    count_turns = 0
    while is_game_over == False:
        ### ask for user input
        count_turns +=1


    while is_game_over == False:
        ### Game dynamics 
        count_turns +=1


if __name__ == __main__:
    main()
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
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns



class User:
    def __init__(self, fist_name, last_name, age, color):
        self.fist_name = fist_name
        self.last_name = last_name
        self.age = age
        self.color = color



if __name__ == "__main__":
    is_game_over = False
    count_turns = 0
    while is_game_over == False:
        ### ask for user input
        count_turns +=1
        


    while is_game_over == False:
        ### Game dynamics 
        count_turns +=1
        
        # remove below
        if count_turns == 5:
            is_game_over = True

        