# Author: Nathan Taylor
# Date: 2/28/2021
# Description: A Python implementation of Janggi.

class JanggiBoard:
    """
    A class to represent the Janggi game board. The board is 
    designed to store information about which pieces are where 
    (via a dictionary). The board also contains methods which 
    report information about which pieces are where on the board.
    Each JanggiGame, Piece, and JanggiMechanic object has a 
    reference to a JanggiBoard object.
    """

    def __init__(self):
        """
        Initialize the board as a blank dictionary. Also initialize 
        dictionaries to convert from location notation (i.e. "b5") 
        to tuple notation, and a list of locations in the palace.
        """

        self._columns = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8}
        self._rev_columns = {val : key for key, val in self._columns.items()}
        self._rows = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9}
        self._rev_rows = {val : key for key, val in self._rows.items()}
        self._board = {column + row: None for column in self._columns for row in self._rows}
        self._palace = [col + str(row) for row in [1,2,3,8,9,10] for col in ['d', 'e', 'f']]
        self._saved_board = None

    def get_pieces(self):
        """
        Returns a list containing all pieces on the board.
        """

        return [piece for piece in self._board if piece is not None]

    def get_palace_pieces(self):
        """
        Returns a list containing all pieces in both palaces.
        """

        palace_spots = [self._board[i] for i in self._palace]
        palace_pieces = [piece for piece in palace_spots if piece is not None]

        return palace_pieces

    def save_board(self):
        """
        Saves the current state of the board. 
        Can be recovered with the recover_board method.
        Only one state is saved.
        """
        
        self._saved_board = dict(self._board)

    def recover_board(self):
        """
        Recovers the previous state of the board, as 
        stored in _saved_board. Updates the position of 
        each piece accordingly.
        """

        self._board = dict(self._saved_board)
        for loc in self._board:
            piece = self._board[loc]
            if piece is not None:
                piece.set_pos(loc)

    def loc_on_board(self, loc:str) -> bool:
        """
        Returns True if the location is on the board. Returns False 
        otherwise.
        """

        if loc in self._board:
            return True

        return False

    def tuple_on_board(self, tup:tuple) -> bool:
        """
        Returns True if the tuple is on the board. Returns False otherwise.
        """

        loc = self.tuple_to_loc(tup)

        return self.loc_on_board(loc)

    def loc_to_tuple(self, loc:str):
        """
        Converts the string location "b5", for example, to the position tuple 
        (1,4) (column, row). Returns None if the location is invalid.
        """

        if loc is None or len(loc) < 2:
            return None
        if loc[0] not in self._columns or loc[1:] not in self._rows:
            return None

        return (self._columns[loc[0]], self._rows[loc[1:]])

    def tuple_to_loc(self, tup:tuple):
        """
        Converts the tuple (1,4), for example, to the position 
        string "b5". If the tuple is not on the board, returns None.
        """

        if tup is None or len(tup) < 2:
            return None

        if tup[0] not in self._rev_columns:
            return None
        if tup[1] not in self._rev_rows:
            return None

        loc = self._rev_columns[tup[0]] + self._rev_rows[tup[1]]

        return loc

    def get_piece(self, loc:str):
        """
        Returns the piece at the given location (for 
        example "b5".) Returns None if there is no 
        piece at that location, or if the location is invalid.
        """

        if loc not in self._board:
            return None

        return self._board[loc]

    def clear_loc(self, loc:str):
        """
        Clears the location (loc) on the board (sets its value to None).
        Does nothing if (loc) is not on the board.
        """

        self.set_piece(None, loc)

    def set_piece(self, piece, loc:str):
        """
        Moves (piece) to (loc) on the board. Does nothing if loc 
        is not on the board. Does not check legality of the move.
        Does not clear the piece's old location.
        """

        if loc not in self._board:
            return None

        self._board[loc] = piece

    def get_player(self, loc:str):
        """
        Returns the player who owns the piece at the given location.
        Returns None if there is no piece there.
        """

        if loc is None:
            return None

        piece = self.get_piece(loc)

        if piece is None:
            return None

        return piece.get_player()

    def in_palace(self, loc:str) -> bool:
        """
        Returns True if the given location (for example "e3") 
        is in the palace. Returns False otherwise.
        """

        if loc in self._palace:
            return True
        return False

    def print_piece(self, location:str):
        """
        Prints a piece on the board at the given location. 
        To be used with print_board.
        """
        num_spaces = 2

        # print "." when there is no piece in a position.
        # also, print a border around the palace
        space_type = {loc:" " for loc in self._board}
        pre_space_type = {loc:" " for loc in self._board}
        dot_type = {loc:"." for loc in self._board}
        palace_border_right_upper = ["d1", "e1", "d8", "e8"]
        palace_border_right_lower = ["d3", "e3", "d10", "e10"]
        palace_border_left_upper = ["e1", "f1", "e8", "f8"]
        palace_border_left_lower = ["e3", "f3", "e10", "f10"]
        palace_border_vert = ["d2", "d3", "d9", "d10", "f2", "f3", "f9", "f10"]
        for border_piece in palace_border_right_upper:
            space_type[border_piece] = "-"
        for border_piece in palace_border_right_lower:
            space_type[border_piece] = "_"
        for border_piece in palace_border_left_upper:
            pre_space_type[border_piece] = "-"
        for border_piece in palace_border_left_lower:
            pre_space_type[border_piece] = "_"
        for border_piece in palace_border_vert:
            dot_type[border_piece] = "!"

        # define the display components for the location
        piece = self._board[location]
        space = space_type[location]
        pre_space = pre_space_type[location]
        dot = dot_type[location]

        # print the location
        if piece is None:
            print(pre_space + dot + space * num_spaces, end="")
            return
        name = piece.get_name()
        if len(name) == 3:
            print(name + space * (num_spaces - 1), end="")
            return
        print(pre_space + name + space * (num_spaces - 1), end="")

    def print_board(self):
        "Prints a representation of the board."

        print("     ", end="")
        for col in self._columns:
            print(col + "   ", end="")
        print()
        print("   ------------------------------------")
        for row in self._rows:
            print(row + " | " if int(row) < 10 else row + "| ", end="")
            for col in self._columns:
                self.print_piece(col + row)
            print()

class JanggiPosition:
    """
    A class to represent a position on the Janggi game board. 
    A JanggiPosition can be initialized using a location string ("b5") 
    or a tuple ((1,4)). The purpose of this class is to have clean 
    syntax for adding vectors (represented by tuples) to positions on the 
    board (represented usually as location strings). The most important 
    method is the shift method, which does this vector addition.

    The JanggiPosition class uses the JanggiBoard class to do conversions 
    between tuple and location string, and to check whether a given tuple 
    is actually on the board. 

    The Pieces store their location information as a JanggiPosition, 
    so that they can use the shift method to calculate potential moves. 
    """

    def __init__(self, pos, board:JanggiBoard):
        """
        Initialize the position, setting _loc to be the 
        current location string, and setting _tuple to be the 
        current location tuple. pos can be either a tuple or a 
        location string. If the position is not 
        on the board, both _loc and _tuple are set to None.
        """

        self._board = board
        self.set_pos(pos)

    def __repr__(self):
        "Return the position's location string."

        return self._loc

    def set_pos(self, pos):
        """
        Set the position. pos can be either a tuple or a 
        location string. If the position is not 
        on the board, both _loc and _tuple are set to None.
        """

        if type(pos) == str and self._board.loc_on_board(pos):
            self._loc = pos
            self._tuple = self._board.loc_to_tuple(pos)
        elif type(pos) == tuple and self._board.tuple_on_board(pos):
            self._loc = self._board.tuple_to_loc(pos)
            self._tuple = pos
        else:
            self._loc = None
            self._tuple = None


    # def tuple_to_loc(self, tup:tuple):
    #     """
    #     Convert the tuple to a location on the board.
    #     Returns None if the location is not valid.
    #     """

    #     return self._board.tuple_to_loc(tup)

    # def loc_to_tuple(self, loc:str):
    #     """
    #     Converts the location string to a tuple on the board.
    #     Returns None if the location is not valid.
    #     """

    #     return self._board.loc_to_tuple(loc)

    def get_tuple(self) -> tuple:
        "Returns the position's tuple representation."

        return self._tuple

    def get_loc(self) -> str:
        "Returns the position's location string representation."

        return self._loc

    def add_tuples(self, tup1:tuple, tup2:tuple) -> tuple:
        """
        Performs vector addition on the two tuples, and 
        returns the sum.
        For example, (1,2) + (0,1) = (1,3).
        """

        if tup1 is None or tup2 is None:
            return None

        return (tup1[0] + tup2[0], tup1[1] + tup2[1])


    def shift(self, movement:tuple):
        """
        Shifts the position by the movement tuple (using vector 
        addition). Returns a new JanggiPosition with the shifted coordinates.
        """

        new_tuple = self.add_tuples(self._tuple, movement)
        new_pos = JanggiPosition(new_tuple, self._board)

        return new_pos

class Piece:
    """
    A class to represent a generic Janggi Piece. The generic Janggi 
    Piece has attributes for its current position (a JanggiPosition object), 
    name, and the JanggiBoard it belongs to. The JanggiBoard _board dictionary
    contains the locations of each Piece as well.

    Methods for the generic Janggi Piece are for reporting information about 
    the Piece (i.e. name, owner of the piece), or for helping the Pieces themselves
    calculate potential moves.
    """

    def __init__(self, player:str, number:int, character:str, location:dict, board:JanggiBoard):
        """
        Place the piece on the board, and keep track of this piece's location. 

        Each child class of Piece will give the superclass a location dictionary 
        which contains information about where to initially place the piece.
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
        "Returns the piece's current location string."

        return self._pos.get_loc()
    
    def set_pos(self, loc:str):
        "Sets the current position of the piece."

        pos = JanggiPosition(loc, self._board)

        self._pos = pos

    def pos_on_board(self, pos:JanggiPosition) -> bool:
        """
        Returns True if the position pos is on the board. 
        Returns False otherwise. 
        """

        return self._board.loc_on_board(pos.get_loc())

    def get_pos_player(self, pos:JanggiPosition):
        """
        If there is a piece at the given position, returns
        the player who owns that piece. If there is no piece 
        at the position or the position is invalid, returns None.
        """

        return self._board.get_player(pos.get_loc())

    def loc_from_pos(self, pos):
        """
        Takes either a JanggiPosition object or a location string (i.e. "b5")
        as input. If given a JanggiPosition object, loc_from_pos converts it 
        to a location string, and returns that string. If given a location 
        string, loc_from_pos returns that string. Does not check if the 
        location or position is on the board.
        """

        if type(pos) == JanggiPosition:
            return pos.get_loc()
        return pos

    def is_open(self, pos):
        """
        Takes either a JanggiPosition object or a location string (i.e. "b5")
        as input. Returns True if the position is valid and doesn't contain a piece.
        Returns False otherwise. 
        """

        # convert the location/position to a location string
        loc = self.loc_from_pos(pos)

        if not self._board.loc_on_board(loc):
            return False

        return self._board.get_piece(loc) is None

    def is_us(self, pos):
        """
        Takes either a JanggiPosition object or a location string (i.e. "b5") 
        as input. Returns True if the position contains a piece owned by 
        the current player. Returns False otherwise. 
        """

        # convert the location/position to a location string
        loc = self.loc_from_pos(pos)

        return self._board.get_player(loc) == self.get_player()

    def is_not_us(self, pos):
        """
        Takes either a JanggiPosition object or a location string (i.e. "b5") 
        as input. Returns True if the position does not contain a piece owned by 
        the current player. Returns False otherwise. 
        """

        # convert the location/position to a location string
        loc = self.loc_from_pos(pos)

        return self._board.get_player(loc) != self.get_player()

    def is_opponent(self, pos):
        """
        Takes either a JanggiPosition object or a location string (i.e. "b5") 
        as input. Returns True if the position contains a piece owned by 
        the opposite player. Returns False otherwise. 
        """

        return self.is_not_us(pos) and (not self.is_open(pos))

    def is_piece(self, pos):
        """
        Takes either a JanggiPosition object or a location string (i.e. "b5")
        as input. Returns True if the position contains a piece owned by 
        either player. Returns False otherwise. 
        """

        return self.is_us(pos) or self.is_opponent(pos)

    def ok_to_move_here(self, pos):
        """
        Takes either a JanggiPosition object or a location string (i.e. "b5") 
        as input. Returns True if the position is on the board and 
        does not contain a piece owned by the current player. 
        Returns False otherwise. 
        """

        if type(pos) == str:
            pos = JanggiPosition(pos, self._board)

        return self.pos_on_board(pos) and self.is_not_us(pos)

class Elephant(Piece):
    """
    A class to represent the Elephant piece.
    """

    def __init__(self, player, number, board):
        "Initialize the elephant."

        location = {"R": {1: "b1", 2: "g1"}, "B": {1: "b10", 2: "g10"}}

        self._movement = {
            (0,1): [(1,1), (-1,1)], 
            (0,-1): [(1,-1), (-1,-1)], 
            (1,0): [(1,1), (1,-1)],
            (-1,0): [(-1,1), (-1,-1)]
        }

        super().__init__(player, number, "E", location, board)

    def get_moves(self) -> list:
        "Returns a list of valid moves for this Elephant."

        valid_moves = []

        # try the first move in each direction
        for first_move in self._movement:
            first_pos = self._pos.shift(first_move)
            # if the first position is open, check the next moves
            if self.is_open(first_pos):
                # there are two options for second move: diagonal right or diagonal left
                for second_move in self._movement[first_move]:
                    second_pos = first_pos.shift(second_move)
                    # if the second position is open, repeat the second move
                    if self.is_open(second_pos):
                        third_pos = second_pos.shift(second_move)
                        # add the move if it is valid
                        if self.ok_to_move_here(third_pos):
                            valid_moves.append(third_pos.get_loc())

        return valid_moves

class General(Piece):
    " A class to represent the General piece."

    def __init__(self, player, board):
        "Initialize the general."

        location = {"R": {1: "e2"}, "B": {1: "e9"}}

        self._moves = {
            "d8": ["e8", "d9", "e9"],
            "e8": ["d8", "f8", "e9"],
            "f8": ["e8", "e9", "f9"],
            "d9": ["d8", "e9", "d10"],
            "e9": ["d8", "e8", "f8", "d9", "f9", "d10", "e10", "f10"],
            "f9": ["f8", "e9", "f10"],
            "d10": ["d9", "e9", "e10"],
            "e10": ["e9", "d10", "f10"],
            "f10": ["e9", "f9", "e10"],
            "d3": ["e3", "d2", "e2"],
            "e3": ["d3", "f3", "e2"],
            "f3": ["e3", "e2", "f2"],
            "d2": ["d3", "e2", "d1"],
            "e2": ["d3", "e3", "f3", "d2", "f2", "d1", "e1", "f1"],
            "f2": ["f3", "e2", "f1"],
            "d1": ["d2", "e2", "e1"],
            "e1": ["e2", "d1", "f1"],
            "f1": ["e2", "f2", "e1"],
        }

        super().__init__(player, 1, "G", location, board)

    def get_moves(self):
        "Returns a list of valid moves for the General."

        valid_moves = []

        if self.get_loc() in self._moves:
            for move in self._moves[self.get_loc()]:
                # add the move if valid
                if self.ok_to_move_here(move):
                    valid_moves.append(move)
        
        return valid_moves

class Advisor(Piece):
    "A class to represent the Advisor piece."

    def __init__(self, player, number, board):
        "Initialize the advisor."

        location = {"R": {1: "d1", 2: "f1"}, "B": {1: "d10", 2: "f10"}}

        self._moves = {
            "d8": ["e8", "d9", "e9"],
            "e8": ["d8", "f8", "e9"],
            "f8": ["e8", "e9", "f9"],
            "d9": ["d8", "e9", "d10"],
            "e9": ["d8", "e8", "f8", "d9", "f9", "d10", "e10", "f10"],
            "f9": ["f8", "e9", "f10"],
            "d10": ["d9", "e9", "e10"],
            "e10": ["e9", "d10", "f10"],
            "f10": ["e9", "f9", "e10"],
            "d3": ["e3", "d2", "e2"],
            "e3": ["d3", "f3", "e2"],
            "f3": ["e3", "e2", "f2"],
            "d2": ["d3", "e2", "d1"],
            "e2": ["d3", "e3", "f3", "d2", "f2", "d1", "e1", "f1"],
            "f2": ["f3", "e2", "f1"],
            "d1": ["d2", "e2", "e1"],
            "e1": ["e2", "d1", "f1"],
            "f1": ["e2", "f2", "e1"],
        }

        super().__init__(player, number, "A", location, board)

    def get_moves(self):
        "Returns a list of valid moves for the Advisor."

        valid_moves = []

        if self.get_loc() in self._moves:
            for move in self._moves[self.get_loc()]:
                # add the move if valid
                if self.ok_to_move_here(move):
                    valid_moves.append(move)
        
        return valid_moves

class Chariot(Piece):
    "A class to represent a Chariot piece."

    def __init__(self, player, number, board):
        "Initialize the Chariot."

        location = {"R": {1: "a1", 2: "i1"}, "B": {1: "a10", 2: "i10"}}

        # movement direction vectors
        self._directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # palace movement dictionary
        # format: 
        # start: (jump, dest)
        self._palace_corner_moves = {
            "d1": ("e2", "f3"),
            "f1": ("e2", "d3"),
            "d3": ("e2", "f1"),
            "f3": ("e2", "d1"),
            "d10": ("e9", "f8"),
            "f10": ("e9", "d8"),
            "d8": ("e9", "f10"),
            "f8": ("e9", "d10")
        }

        self._palace_center_moves = {
            "e2": ["d3", "f3", "d1", "f1"],
            "e9": ["d8", "f8", "d10", "f10"]
        }

        super().__init__(player, number, "C", location, board)

    def get_step(self, start:JanggiPosition, direction:tuple) -> JanggiPosition:
        """
        Generator function that finds the next position
        on the board in the given direction. Starts at the 
        start position. Returns the next position 
        while the next position is on the board.
        """

        step = start.shift(direction)

        while self.pos_on_board(step):
            yield step
            step = step.shift(direction)

    def get_move(self, direction:tuple) -> str:
        """
        Generator function that finds the next valid move 
        in the given direction. 
        """

        start = self._pos

        for step in self.get_step(start, direction):
            # if we reach our own piece, stop here
            if self.is_us(step):
                return

            # if we reach the opponents piece, return the location
            # then stop here
            if self.is_opponent(step):
                yield step.get_loc()
                return

            yield step.get_loc()

    def get_moves(self) -> list:
        "Returns a list of valid moves for this Cannon."

        valid_moves = []

        for direction in self._directions:
            for move in self.get_move(direction):
                valid_moves.append(move)

        # add diagonal moves if appropriate
        if self.get_loc() in self._palace_corner_moves:
            move1, move2 = self._palace_corner_moves[self.get_loc()]
            if self.ok_to_move_here(move1):
                valid_moves.append(move1)
            if self.is_open(move1) and self.ok_to_move_here(move2):
                valid_moves.append(move2)
        
        # add moves from center of palace if appropriate
        if self.get_loc() in self._palace_center_moves:
            moves = self._palace_center_moves[self.get_loc()]
            for move in moves:
                if self.ok_to_move_here(move):
                    valid_moves.append(move)

        return valid_moves

class Cannon(Piece):
    "A class to represent the Cannon piece."

    def __init__(self, player, number, board):
        "Initialize the Cannon."

        location = {"R": {1: "b3", 2: "h3"}, "B": {1: "b8", 2: "h8"}}

        # movement direction vectors
        self._directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # palace movement dictionary
        # format: 
        # start: (jump, dest)
        self._palace_moves = {
            "d1": ("e2", "f3"),
            "f1": ("e2", "d3"),
            "d3": ("e2", "f1"),
            "f3": ("e2", "d1"),
            "d10": ("e9", "f8"),
            "f10": ("e9", "d8"),
            "d8": ("e9", "f10"),
            "f8": ("e9", "d10")
        }

        super().__init__(player, number, "O", location, board)

    def is_cannon(self, pos:JanggiPosition) -> bool:
        """
        Returns True if there is a Cannon at the given 
        position. Returns False otherwise.
        """
        
        piece = self._board.get_piece(pos.get_loc())

        if piece is None:
            return False

        if piece.get_name()[1] == 'O':
            return True
        
        return False

    def get_step(self, start:JanggiPosition, direction:tuple) -> JanggiPosition:
        """
        Generator function that finds the next position
        on the board in the given direction. Starts at the 
        start position. Returns the next position 
        while the next position is on the board.
        """

        step = start.shift(direction)

        while self.pos_on_board(step):
            yield step
            step = step.shift(direction)

    def get_jump_pos(self, direction:tuple):
        """
        Returns the position of the next piece in the given direction 
        (starting at the Cannon's current position). This is the position
        the Cannon will jump over.
        Returns False if no piece is found.
        """

        for step in self.get_step(self._pos, direction):
            # if there is a cannon here, stop
            if self.is_cannon(step):
                return False

            # if we find a non-cannon piece, return the position
            if self.is_piece(step):
                return step
        # no pieces found
        return False

    def get_move(self, direction:tuple) -> str:
        """
        Generator function that finds the next valid move 
        in the given direction. 
        """

        start = self.get_jump_pos(direction)

        # if there is no jump position, do nothing
        if not start:
            return

        for step in self.get_step(start, direction):
            # if we reach a cannon, stop here
            if self.is_cannon(step):
                return

            # if we reach our own piece, stop here
            if self.is_us(step):
                return

            # if we reach the opponents piece, return the location
            # then stop here
            if self.is_opponent(step):
                yield step.get_loc()
                return

            yield step.get_loc()

    def get_moves(self) -> list:
        "Returns a list of valid moves for this Cannon."

        valid_moves = []

        for direction in self._directions:
            for move in self.get_move(direction):
                valid_moves.append(move)

        # add diagonal moves if appropriate
        if self.get_loc() in self._palace_moves:
            jump, dest = self._palace_moves[self.get_loc()]
            if self.is_piece(jump) and self.ok_to_move_here(dest):
                valid_moves.append(dest)

        return valid_moves

class Horse(Piece):
    "A class to represent the Horse piece."

    def __init__(self, player, number, board):
        "Initialize the horse."

        location = {"R": {1: "c1", 2: "h1"}, "B": {1: "c10", 2: "h10"}}

        self._movement = {
            (0,1): [(1,1), (-1,1)], 
            (0,-1): [(1,-1), (-1,-1)], 
            (1,0): [(1,1), (1,-1)],
            (-1,0): [(-1,1), (-1,-1)]
        }

        super().__init__(player, number, "H", location, board)

    def get_moves(self) -> list:
        "Returns a list of valid moves for this Horse"

        valid_moves = []

        # try moving in each direction
        for first_move in self._movement:
            first_pos = self._pos.shift(first_move)
            # if the first move is clear, move on to second move
            if self.is_open(first_pos):
                # there are two possible second moves: diagonal right or diagonal left
                for second_move in self._movement[first_move]:
                    second_pos = first_pos.shift(second_move)
                    # add the move if it is valid
                    if self.ok_to_move_here(second_pos):
                        valid_moves.append(second_pos.get_loc())

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

        # normal movement
        self._movement = [(1, 0), (-1, 0), (0, direction)]

        # extra moves when in the palace
        self._palace_moves = {
            "d8": ["e9"],
            "f8": ["e9"],
            "e9": ["d10", "f10"],
            "d3": ["e2"],
            "f3": ["e2"],
            "e2": ["d1", "f1"]
        }

        super().__init__(player, number, "S", location, board)

    def get_moves(self):
        "Returns a list of valid moves for this Soldier."

        valid_moves = []

        for movement in self._movement:
            move = self._pos.shift(movement)
            # add the move if valid
            if self.ok_to_move_here(move):
                valid_moves.append(move.get_loc())

        if self.get_loc() in self._palace_moves:
            for palace_move in self._palace_moves[self.get_loc()]:
                # add the move if valid
                if self.ok_to_move_here(palace_move):
                    valid_moves.append(palace_move)

        return valid_moves

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

    def move_piece(self, piece, loc:str):
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

class JanggiGame:
    "A class to represent the Janggi game."

    def __init__(self):
        """
        Initialize the game with a populated board, starting 
        player "B"lue, and starting _state "UNFINISHED".
        """

        self._board = JanggiBoard()
        self._player = "B"
        self._mechanic = JanggiMechanic(self._board)
        self._state = "UNFINISHED"
        self._pieces = {"R": [], "B": []}
        self._in_check = {"R": "", "B": ""}

        # place pieces on the board
        for player in ["R", "B"]:
            general = General(player, self._board)
            self._pieces[player].append(general)
            for number in [1, 2]:
                for piece_type in [Elephant, Advisor, Chariot, Cannon, Horse]:
                    piece = piece_type(player, number, self._board)
                    self._pieces[player].append(piece)
            for number in [1,2,3,4,5]:
                soldier = Soldier(player, number, self._board)
                self._pieces[player].append(soldier)

    def get_player(self) -> str:
        "Returns the current player."

        return self._player

    def get_in_check(self, player:str) -> str:
        "Returns the string 'Yes' if the player is in check."

        return self._in_check[player]

    def get_game_state(self) -> str:
        """
        Returns 'UNFINISHED', 'RED_WON', or 'BLUE_WON', 
        depending on the state of the game.
        """

        return self._state

    def get_general(self, player:str) -> General:
        """
        Returns the general belonging to the given player.
        """

        return self._pieces[player][0]

        # for piece in self._board.get_palace_pieces():
        #     if type(piece) == General and piece.get_player() == player:
        #         return piece

    # the exclude excludes the piece that was optionally captured
    def is_in_check(self, player:str, exclude=None) -> bool:
        """
        Returns True if the player is in check. 
        Returns False otherwise. Only looks at the 
        first letter of the given string (player) to identify the player 
        (i.e. "B", "b", and "Blue" are all interpreted as the blue player.)

        The optional exclude parameter is for a piece that was captured when 
        trying out a move. If this parameter is passed, the given piece will 
        be ignored. The try_move method does not remove the captured 
        piece, in case the move will put the player's general in check.
        """

        player = player[0].upper()

        general_loc = self.get_general(player).get_loc()

        opponent = self.get_opponent(player)

        opponent_pieces = [piece for piece in self._pieces[opponent] if piece is not exclude]

        # for piece in self._pieces[opponent]:
        for piece in opponent_pieces:
            if general_loc in piece.get_moves():
                return True

        return False

    def get_opponent(self, player:str) -> str:
        """
        Returns the player opposing the given player.
        I.e. returns "R" if the given player is "B".
        """

        if player == 'B':
            return 'R'
        else:
            return 'B'

    def update_turn(self):
        """
        Changes the current turn from 'B' to 'R' or 
        from 'R' to 'B'. (should this be called brb?)
        """

        self._player = self.get_opponent(self._player)

    def get_board(self) -> JanggiBoard:
        """
        Returns the game board.
        """

        return self._board

    def try_move(self, piece, move_to):
        """
        Saves the board, then makes the given move (if valid).
        If the move puts the current player in check, try_move 
        restores the board and returns False.
        """

        self._board.save_board()
        captured_piece = self._mechanic.move_piece(piece, move_to)
        if self.is_in_check(self._player, exclude=captured_piece):
            self._board.recover_board()
            return False
        return True

    def check_if_player_won(self, player:str) -> bool:
        """
        Checks if the opponent to the given player is in check and 
        has no moves to get out of check.
        """

        opponent = self.get_opponent(player)

        if not self.is_in_check(opponent):
            return False

        for piece in self._pieces[opponent]:
            for move in piece.get_moves():
                # old_loc = piece.get_loc() # debug
                self._board.save_board()
                self._mechanic.move_piece(piece, move)
                if not self.is_in_check(opponent):
                    # print("check win: found move " + old_loc + " to " + move) # debug
                    self._board.recover_board()
                    return False
                self._board.recover_board()

        return True

    def declare_winner(self, player:str):
        """
        Declares the (player) to be the winner.
        """

        if player == "R":
            self._state = "RED_WON"
        elif player == "B":
            self._state = "BLUE_WON"

    def make_move(self, move_from, move_to):
        """
        Attempts to move a piece located at move_from location to 
        the move_to location.
        """

        # check the game state
        if self._state != 'UNFINISHED':
            return False

        # get the pieces at the move_from and move_to locations
        piece = self._board.get_piece(move_from)
        to_piece = self._board.get_piece(move_to)

        # return False if there is no piece at move_from
        if piece is None:
            return False

        # if the piece is not owned by the current player, return False
        if piece.get_player() != self._player:
            return False

        # # if the destination piece is owned by the current player, return False
        # if to_piece is not None and to_piece.get_player() == self._player:
        #     return False

        # if the current player wants to skip a turn, 
        # update the turn and do nothing else
        if move_to == move_from:
            if self.is_in_check(self._player):
                return False
            self.update_turn()
            return True

        # if the piece cannot move to the given location, return False
        if move_to not in piece.get_moves():
            return False

        # make the move, then undo if it puts the current player in check
        if not self.try_move(piece, move_to):
            return False

        # if a piece was captured, remove it from the opponent's piece list
        opponent = self.get_opponent(self._player)
        if to_piece in self._pieces[opponent]:
            self._pieces[opponent].remove(to_piece)

        # check if the current player won
        if self.check_if_player_won(self._player):
            self.declare_winner(self._player)

        # update whether each player is in check or not
        for player in [self._player, opponent]:
            if self.is_in_check(player):
                self._in_check[player] = "Yes"
            else:
                self._in_check[player] = "No"

        self.update_turn()
        
        return True
