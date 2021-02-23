# Author: Nathan Taylor
# Date: 2/19/2021
# Description: A Python implementation of Janggi.
from JanggiPieces import *
from JanggiMechanic import JanggiMechanic

class JanggiGame:
    "A class to represent the Janggi game."

    def __init__(self):
        "Initialize the game with a populated board."

        self._board = JanggiBoard()
        self._player = "B"
        self._mechanic = JanggiMechanic(self._board)

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

        # get the pieces at the move_from and move_to locations
        piece = self._board.get_piece(move_from)
        to_piece = self._board.get_piece(move_to)


        # return False if there is no piece at move_from
        if piece is None:
            return False

        # if the piece is not owned by the current player, return False
        if piece.get_player() != self._player:
            return False

        # if the destination piece is owned by the current player, return False
        if to_piece is not None and to_piece.get_player() == self._player:
            return False

        # if the piece is cannot move to the given location, return False
        if move_to not in piece.get_moves():
            return False

        self._mechanic.move_piece(piece, move_to)
        
        return True


g = JanggiGame()
g.get_board().print_board()
input()
print(g.make_move("c7", "d6"))
print('here')
g.get_board().print_board()
input()
print(g.make_move("c7", "c6"))
g.get_board().print_board()
input()
print(g.make_move("c6", "c5"))
g.get_board().print_board()
input()
print(g.make_move("c5", "c4"))
g.get_board().print_board()
input()
print(g.make_move("c4", "c3"))
g.get_board().print_board()
input()
print(g.make_move("c3", "d3"))
g.get_board().print_board()
input()
print(g.make_move("d3", "e2"))
g.get_board().print_board()