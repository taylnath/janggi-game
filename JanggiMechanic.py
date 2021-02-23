from JanggiBoard import JanggiBoard
from JanggiPieces import Piece

class JanggiMechanic:
    "A class to update the Janggi game board."

    def __init__(self, board:JanggiBoard):

        self._board = board

    def move_piece(self, piece:Piece, loc:str):
        """
        Moves the (piece) to the given location (loc).
        Returns the piece which was captured, or None 
        if no piece was captured.
        """

        # save the captured piece
        captured_piece = self._board.get_piece(loc)

        # clear the old location
        self._board.clear_loc(piece.get_loc())

        # move to new location
        self._board.set_piece(piece, loc)

        # update new location
        piece.set_pos(loc)

        return captured_piece
