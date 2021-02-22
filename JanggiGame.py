# Author: Nathan Taylor
# Date: 2/19/2021
# Description: A Python implementation of Janggi.
from JanggiPieces import *

class JanggiGame:
    "A class to represent the Janggi game."

    def __init__(self):
        "Initialize the game with a populated board."

        self._board = JanggiBoard()
        self._player = "B"

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

    def make_move(self, move_from, move_to):
        """
        Attempts to move a piece located at move_from location to 
        the move_to location.
        """

        # get the piece at the move_from location
        piece = self._board.get_piece(move_from)

        # return False if there is no piece at move_from
        if piece is None:
            return False

        # if the piece is not owned by the current player, return False
        if piece.get_player() != self._player:
            return False

        print(self._board.loc_to_tuple("b5"))
        print(self._board.tuple_to_loc((1,4)))

g = JanggiGame()
g.get_board().print_board()
g.make_move("c7", "c6")

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