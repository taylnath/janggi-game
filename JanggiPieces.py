# pieces for the Janggi game

from JanggiBoard import JanggiBoard

class Piece:
    """
    A class to represent a generic Janggi piece. 
    """

    def __init__(self, player:str, number:int, character:str, location:dict, moves:dict, board:JanggiBoard):
        """
        Place the piece on the board, and keep track of this piece's location. 
        """
        # construct the piece's name
        if character == "G":
            self._name = player + character
        else:
            self._name = player + character + str(number)

        # get the piece's starting location
        if player in location and number in location[player]:
            self._loc = location[player][number]
        else:
            self._loc = "invalid location"

        # place the piece on the board
        self._board = board
        self._board.place_piece(self._loc, self)

        self._moves = moves

    def get_name(self):
        "Returns the piece's name."

        return self._name

    def get_player(self):
        "Returns the player that owns this piece."

        return self._name[0]

    def get_loc(self):
        "Returns the piece's current location."

        return self._loc
    
    def set_loc(self, loc):
        "Sets the current location of the piece."

        self._loc = loc

    def get_moves(self):
        """
        If the piece is in the palace, returns the possible moves 
        for this piece in the palace. Otherwise returns the normal 
        possible moves for the piece. 
        """

        # get the relative moves of the piece
        if self._board.in_palace(self._loc):
            relative_moves = self._moves["palace"]
        else:
            relative_moves = self._moves["normal"]

        loc_tuple = self._board.loc_to_tuple(self._loc)

        tuple_moves = [(loc_tuple[0] + move[0], loc_tuple[1] + move[1]) for move in relative_moves]
        moves = [self._board.tuple_to_loc(tuple_move) for tuple_move in tuple_moves]
        valid_moves = [move for move in moves if move is not None]

        return valid_moves


class Elephant(Piece):
    """
    A class to represent the Elephant piece.
    """

    def __init__(self, player, number, board):
        "Initialize the elephant."

        location = {"R": {1: "b1", 2: "g1"}, "B": {1: "b10", 2: "g10"}}

        moves = {}

        super().__init__(player, number, "E", location, moves, board)


class General(Piece):
    " A class to represent the General piece."

    def __init__(self, player, board):
        "Initialize the general."

        location = {"R": {1: "e2"}, "B": {1: "e9"}}

        moves = {}

        super().__init__(player, 1, "G", location, moves, board)

class Advisor(Piece):
    "A class to represent the Advisor piece."

    def __init__(self, player, number, board):
        "Initialize the advisor and place on board."

        location = {"R": {1: "d1", 2: "f1"}, "B": {1: "d10", 2: "f10"}}

        moves = {}

        super().__init__(player, number, "A", location, moves, board)

class Chariot(Piece):
    "A class to represent a Chariot piece."

    def __init__(self, player, number, board):
        "Initialize the Chariot."

        location = {"R": {1: "a1", 2: "i1"}, "B": {1: "a10", 2: "i10"}}

        moves = {}

        super().__init__(player, number, "C", location, moves, board)

class Cannon(Piece):
    "A class to represent the Cannon piece."

    def __init__(self, player, number, board):
        "Initialize the Cannon."

        location = {"R": {1: "b3", 2: "h3"}, "B": {1: "b8", 2: "h8"}}

        moves = {}

        super().__init__(player, number, "O", location, moves, board)

class Horse(Piece):
    "A class to represent the Horse piece."

    def __init__(self, player, number, board):
        "Initialize the horse."

        location = {"R": {1: "c1", 2: "h1"}, "B": {1: "c10", 2: "h10"}}

        moves = {}

        super().__init__(player, number, "H", location, moves, board)

class Soldier(Piece):
    "A class to represent the Soldier piece."

    def __init__(self, player, number, board):
        "Initialize the soldier."

        location = {
            "R": {1: "a4", 2: "c4", 3: "e4", 4: "g4", 5: "i4"},
            "B": {1: "a7", 2: "c7", 3: "e7", 4: "g7", 5: "i7"}
        }

        if player == "R":
            direction = 1
        else:
            direction = -1

        moves = {
            "normal": [(1, 0), (-1, 0), (0, direction)],
            "palace": [(1, 0), (-1, 0), (1, direction), (-1, direction)]
        }

        super().__init__(player, number, "S", location, moves, board)