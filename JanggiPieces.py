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

        paths = {}

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

    # def get_move(self, start_loc, movement_tuple):
    #     """
    #     Simulates moving from 
    #     start_loc by the offset movement_tuple. Returns a tuple
    #     containing the end location and the owner of the piece at 
    #     the destination (or None if there is no destination piece),
    #     i.e. returns (loc, player).
    #     """

    #     start_tuple = self._board.loc_to_tuple(start_loc)
    #     end_tuple = self.add_tuples(start_tuple, movement_tuple)
    #     end_loc = self._board.tuple_to_loc(end_tuple)
    #     end_piece = self._board.get_piece(end_loc)
    #     if end_piece is None:
    #         end_player = None
    #     else:
    #         end_player = end_piece.get_player()

    #     return (end_loc, end_player)

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


    # def get_moves(self):
    #     "Returns a list of valid moves for this Horse."

    #     valid_moves = []

    #     for initial_move in self._paths:
    #         initial_loc, initial_player = self.get_move(self._loc, initial_move)
    #         if initial_player is None:
    #             for second_move in self._paths[initial_move]:
    #                 second_loc, second_player = self.get_move(initial_loc, second_move)
    #                 if second_player != self.get_player() and second_loc is not None:
    #                     valid_moves.append(second_loc)

    #     return valid_moves

        # for initial_move in self._paths:
        #     initial_tuple = self.add_tuples(loc_tuple, initial_move)
        #     initial_loc = self._board.tuple_to_loc(initial_tuple)
        #     initial_piece = self._board.get_piece(initial_loc)
        #     if initial_piece is None:
        #         for second_move in self._paths[initial_move]:
        #             second_tuple = self.add_tuples(initial_tuple, second_move)
        #             second_loc = self._board.tuple_to_loc(second_tuple)
        #             second_piece = self._board.get_piece(second_loc)
        #             if second_piece is None or second_piece.get_player() != self.get_player():
        #                 valid_moves.append(second_loc)


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

        self._moves = {
            "normal": [(1, 0), (-1, 0), (0, direction)],
            "palace": [(1, direction), (-1, direction)]
        }

        super().__init__(player, number, "S", location, board)

    def get_moves(self):
        "Returns a list of valid moves for this Soldier."

        # get the relative moves of the piece
        relative_moves = self._moves["normal"]
        if self._board.in_palace(self._pos.get_loc()):
            relative_moves += self._moves["palace"]

        valid_moves = []

        for movement in relative_moves:
            move = self._pos.shift(movement).get_loc()
            if self._board.get_player(move) == self.get_player():
                move = None
            if move is not None:
                valid_moves.append(move)

        return valid_moves