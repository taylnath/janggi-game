# pieces for the Janggi game

from JanggiBoard import JanggiBoard
from JanggiPosition import JanggiPosition
from JanggiMechanic import JanggiMechanic

class Piece:
    """
    A class to represent a generic Janggi piece. 
    """

    def __init__(self, player:str, number:int, character:str, location:dict, board:JanggiBoard):
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
            self._pos = JanggiPosition(location[player][number], board)
        else:
            self._pos = JanggiPosition("invalid location", board)

        # place the piece on the board
        self._board = board
        mechanic = JanggiMechanic(self._board)
        mechanic.place_piece(self)

    def get_name(self) -> str:
        "Returns the piece's name."

        return self._name

    def get_player(self) -> str:
        "Returns the player that owns this piece."

        return self._name[0]
    
    def get_pos(self) -> JanggiPosition:
        "Returns the piece's current position."

        return self._pos

    def get_loc(self) -> str:
        "Returns the piece's current location."

        return self._pos.get_loc()
    
    def set_pos(self, loc:str):
        "Sets the current position of the piece."

        pos = JanggiPosition(loc, self._board)

        self._pos = pos

class Elephant(Piece):
    """
    A class to represent the Elephant piece.
    """

    def __init__(self, player, number, board):
        "Initialize the elephant."

        location = {"R": {1: "b1", 2: "g1"}, "B": {1: "b10", 2: "g10"}}

        paths = {}

        super().__init__(player, number, "E", location, board)

class General(Piece):
    " A class to represent the General piece."

    def __init__(self, player, board):
        "Initialize the general."

        location = {"R": {1: "e2"}, "B": {1: "e9"}}

        paths = {}

        super().__init__(player, 1, "G", location, board)

class Advisor(Piece):
    "A class to represent the Advisor piece."

    def __init__(self, player, number, board):
        "Initialize the advisor and place on board."

        location = {"R": {1: "d1", 2: "f1"}, "B": {1: "d10", 2: "f10"}}

        paths = {}

        super().__init__(player, number, "A", location, board)

class Chariot(Piece):
    "A class to represent a Chariot piece."

    def __init__(self, player, number, board):
        "Initialize the Chariot."

        location = {"R": {1: "a1", 2: "i1"}, "B": {1: "a10", 2: "i10"}}

        paths = {
            "normal": [[(i,j)] for i in range(-8,9) for j in range(-9,10)
                    if i*j == 0 and (i != 0 or j != 0)]
        }

        super().__init__(player, number, "C", location, board)

class Cannon(Piece):
    "A class to represent the Cannon piece."

    def __init__(self, player, number, board):
        "Initialize the Cannon."

        location = {"R": {1: "b3", 2: "h3"}, "B": {1: "b8", 2: "h8"}}

        paths = {
            "normal":
                [[(i,j)] for i in range(-8,9) for j in range(-9,10)
                    if i*j == 0 and (i != 0 or j != 0)]
        }

        super().__init__(player, number, "O", location, board)

class Horse(Piece):
    "A class to represent the Horse piece."

    def __init__(self, player, number, board):
        "Initialize the horse."

        location = {"R": {1: "c1", 2: "h1"}, "B": {1: "c10", 2: "h10"}}

        self._paths = {
            (0,1): [(1,1), (-1,1)], 
            (0,-1): [(1,-1), (-1,-1)], 
            (1,0): [(1,1), (1,-1)],
            (-1,0): [(-1,1), (-1,-1)]
        }

        super().__init__(player, number, "H", location, board)

    def get_moves(self) -> list:
        "Returns a list of valid moves for this Horse"

        valid_moves = []

        for first_move in self._paths:
            first_pos = self._pos.shift(first_move)
            first_player = self._board.get_player(first_pos.get_loc())
            if first_player is None:
                for second_move in self._paths[first_move]:
                    second_pos = first_pos.shift(second_move)
                    second_loc = second_pos.get_loc()
                    second_player = self._board.get_player(second_loc)
                    if second_player != self.get_player() and second_loc is not None:
                        valid_moves.append(second_loc)

        return valid_moves

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

        self._palace_moves = {
            "d8": ["e9", "d9", "e8"],
            "e8": ["d8", "f8", "e9"],
            "f8": ["e9", "f9", "e8"],
            "d9": ["e9", "d10"],
            "e9": ["d9", "f9", "d10", "e10", "f10"],
            "f9": ["e9", "f10"],
            "d10": ["e10"],
            "e10": ["d10", "f10"],
            "f10": ["e10"],
            "d3": ["e2", "d2", "e3"],
            "e3": ["d3", "f3", "e2"],
            "f3": ["e2", "f2", "e3"],
            "d2": ["e2", "d1"],
            "e2": ["d2", "f2", "d1", "e1", "f1"],
            "f2": ["e2", "f1"],
            "d1": ["e1"],
            "e1": ["d1", "f1"],
            "f1": ["e1"]
        }

        # normal movement
        self._movement = [(1, 0), (-1, 0), (0, direction)]

        super().__init__(player, number, "S", location, board)

    def get_moves(self):
        "Returns a list of valid moves for this Soldier."

        valid_moves = []

        for movement in self._movement:
            move = self._pos.shift(movement).get_loc()
            if self._board.get_player(move) == self.get_player():
                move = None
            if move is not None:
                valid_moves.append(move)
        
        if self.get_loc() in self._palace_moves:
            for palace_move in self._palace_moves[self.get_loc()]:
                if palace_move in valid_moves:
                    continue
                if self._board.get_player(palace_move) == self.get_player():
                    continue
                valid_moves.append(palace_move)

        return valid_moves
