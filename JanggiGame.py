# Author: Nathan Taylor
# Date: 2/19/2021
# Description: A Python implementation of Janggi.
from JanggiPieces import *

class JanggiGame:
    "A class to represent the Janggi game."

    def __init__(self):
        "Initialize the game with a populated board."

        self._board = JanggiBoard()

        for player in ["R", "B"]:
            General(player, self._board)
            for number in [1, 2]:
                for piece_type in [Elephant, Advisor, Chariot, Cannon, Horse]:
                    piece_type(player, number, self._board)
            for number in [1,2,3,4,5]:
                Soldier(player, number, self._board)


    def get_board(self):
        """
        Returns the game board.
        """

        return self._board

g = JanggiGame()
g.get_board().print_board()

# b = JanggiBoard()
# e = Elephant("R", 1, b)
# b.print_board()

# columns = { 
#     'a': 0, 
#     'b': 1, 
#     'c': 2, 
#     'd': 3,
#     'e': 4,
#     'f': 5,
#     'g': 6,
#     'h': 7,
#     'i': 8
# }
# rows = {
#     '1': 0,
#     '2': 1,
#     '3': 2,
#     '4': 3,
#     '5': 4,
#     '6': 5,
#     '7': 6,
#     '8': 7,
#     '9': 8,
#     '10': 9
# }
# board = {column + row: None for column in columns for row in rows}
# def get_pos_tuple(pos):
#     """
#     Converts the position "b5", for example, to the position tuple 
#     (1,4) (column, row).
#     """

#     return (columns[pos[0]], rows[pos[1:]])

# e = Elephant('B', 1)
# e2 = Elephant('B', 2)
# g = General('R')
# h = General('B')
# board["b5"] = e
# board["i8"] = e2
# board["d3"] = g
# board["e9"] = h

# def print_piece(location):
#     """
#     Prints a piece on the board at the given location. 
#     To be used with print_board.
#     """
#     num_spaces = 2

#     space_type = {loc:" " for loc in board}
#     pre_space_type = {loc:" " for loc in board}
#     dot_type = {loc:"." for loc in board}
#     palace_border_right_upper = ["d1", "e1", "d8", "e8"]
#     palace_border_right_lower = ["d3", "e3", "d10", "e10"]
#     palace_border_left_upper = ["e1", "f1", "e8", "f8"]
#     palace_border_left_lower = ["e3", "f3", "e10", "f10"]
#     palace_border_vert = ["d2", "d3", "d9", "d10", "f2", "f3", "f9", "f10"]
#     for border_piece in palace_border_right_upper:
#         space_type[border_piece] = "-"
#     for border_piece in palace_border_right_lower:
#         space_type[border_piece] = "_"
#     for border_piece in palace_border_left_upper:
#         pre_space_type[border_piece] = "-"
#     for border_piece in palace_border_left_lower:
#         pre_space_type[border_piece] = "_"
#     for border_piece in palace_border_vert:
#         dot_type[border_piece] = "!"

#     piece = board[location]
#     space = space_type[location]
#     pre_space = pre_space_type[location]
#     dot = dot_type[location]

#     if piece is None:
#         print(pre_space + dot + space * num_spaces, end="")
#         return
#     name = piece.get_name()
#     if len(name) == 3:
#         print(name + space * (num_spaces - 1), end="")
#         return
#     print(pre_space + name + space * (num_spaces - 1), end="")

# def print_board():
#     "Prints a representation of the board."

#     for row in rows:
#         for col in columns:
#             print_piece(col + row)
#         print()

# print(len(board))
# print(board)
# print(get_pos_tuple("b5"))
# print_board()