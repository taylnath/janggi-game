from JanggiBoard import JanggiBoard

class JanggiMechanic:
    """
    A class to update the Janggi game board. 
    Used by the JanggiGame class to move pieces on the board,
    and to initially place pieces on the board.
    """

    def __init__(self, board:JanggiBoard):
        "Initialize the mechanic with a JanggiBoard object."

        self._board = board

    def place_piece(self, piece):
        """
        Used to initially place a piece on the board. 
        Attempts to place the given piece at the given position.
        Returns False and changes nothing if there is already a piece at the position, 
        otherwise returns True and places the piece.
        """

        loc = piece.get_loc()

        # the second if also checks this condition
        if not self._board.loc_on_board(loc):
            return False

        if self._board.get_piece(loc) is not None:
            return False

        self._board.set_piece(piece, loc)
        return True

    def move_piece(self, piece, loc:str, opponent_pieces:list):
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

        # if a piece was captured, remove it from the opponent's piece list
        if captured_piece in opponent_pieces:
            opponent_pieces.remove(captured_piece)

        return captured_piece

    def undo_move(self, captured_piece, capturers_loc:str, captured_loc:str,  piece_list:list):
        """
        Undoes the move from capturers_loc to captured_loc:
        Returns the captured_piece back to the board, at the captured_loc. 
        Does this by calling move_piece to move the capturer back to its previous position, 
        then again calling move_piece to move the captured_piece back on the board. 
        Finally, adds the captured_piece back to the appropriate team's list of pieces 
        (piece_list). If captured_piece is None, this method just returns the "capturer"
        to its previous location (capturers_loc). 
        """

        # get the capturer piece
        capturer = self._board.get_piece(captured_loc)

        # move the capturer back to its old position
        self.move_piece(capturer, capturers_loc, [])

        if captured_piece is not None:
            # move the captured piece back to its old location
            self.move_piece(captured_piece, captured_loc, [])

            # add the captured piece back to the piece_list
            piece_list.append(captured_piece)
