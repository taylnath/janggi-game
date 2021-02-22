# the Janggi Board

class JanggiPosition:
    """
    A class to represent a position on the Janggi game board.
    """

    def __init__(self, pos, board:JanggiBoard):
        """
        Initialize the position. pos can be either a tuple or a 
        string representing the position. If the position is not 
        on the board, both _loc and _tuple are set to None.
        """

        self._board = board

        self.set_pos(pos)

    def __repr__(self):
        "Return the position's string location."

        return self._loc

    def set_pos(self, pos):
        """
        Set the position. pos can be either a tuple or a 
        string representing the position. If the position is not 
        on the board, both _loc and _tuple are set to None.
        """

        if type(pos) == str:
            self._loc = self.tuple_to_loc(self.loc_to_tuple(pos))
            self._tuple = self.loc_to_tuple(pos)
        else:
            self._loc = self.tuple_to_loc(pos)
            self._tuple = self.loc_to_tuple(self.tuple_to_loc(pos))


    def tuple_to_loc(self, tup:tuple):
        """
        Convert the tuple to a location on the board.
        Returns None if the location is not valid.
        """

        return self._board.tuple_to_loc(tup)

    def loc_to_tuple(self, loc:str):
        """
        Converts the location string to a tuple on the board.
        Returns None if the location is not valid.
        """

        return self._board.loc_to_tuple(loc)


    def get_tuple(self) -> tuple:
        "Returns the position's tuple representation."

        return self._tuple

    def get_loc(self) -> str:
        "Returns the position's string representation."

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
        addition.)
        """

        new_tuple = self.add_tuples(self._tuple, movement)

        self.set_pos(new_tuple)

class JanggiBoard:
    "A class to represent the Janggi game board."

    def __init__(self):

        self._columns = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8}
        self._rev_columns = {val : key for key, val in self._columns.items()}
        self._rows = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9}
        self._rev_rows = {val : key for key, val in self._rows.items()}
        self._board = {column + row: None for column in self._columns for row in self._rows}
        self._palace = [col + str(row) for row in [1,2,3,8,9,10] for col in ['d', 'e', 'f']]

    def move_piece(self, piece, loc:JanggiPosition):
        """
        Moves the (piece) to the given location (loc).
        Returns the piece which was captured, or None 
        if no piece was captured.
        """

        # save the captured piece
        captured_piece = self._board[loc]

        # clear the old location
        self._board[piece.get_loc()] = None

        # move to new location
        self._board[loc] = piece

        # update new location
        piece.set_loc(loc)

        return captured_piece

    def loc_to_tuple(self, pos):
        """
        Converts the position "b5", for example, to the position tuple 
        (1,4) (column, row).
        """
        if pos is None:
            return None
        if pos[0] not in self._columns or pos[1:] not in self._rows:
            return None

        return (self._columns[pos[0]], self._rows[pos[1:]])

    def tuple_to_loc(self, tup):
        """
        Converts the tuple (1,4), for example, to the position 
        string "b5". If the tuple is not on the board, returns None.
        """
        if tup is None:
            return None

        if tup[0] not in self._rev_columns:
            return None
        if tup[1] not in self._rev_rows:
            return None

        loc = self._rev_columns[tup[0]] + self._rev_rows[tup[1]]

        return loc

    def get_piece(self, loc):
        """
        Returns the piece at the given location (for 
        example "b5".) Returns None if there is no 
        piece at that location, or if the location is invalid.
        """

        if loc not in self._board:
            return None

        return self._board[loc]

    def get_player(self, loc):
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

    def place_piece(self, loc, piece):
        """
        Attempts to place the given piece at the given location.
        Returns False and changes nothing if there is already a piece at the location, 
        otherwise returns True and places the piece.
        """
        if loc not in self._board:
            return False

        if self._board[loc] is not None:
            return False

        self._board[loc] = piece
        return True

    def in_palace(self, location):
        """
        Returns True if the given location (for example "e3") 
        is in the palace. Returns False otherwise.
        """

        if location in self._palace:
            return True
        return False

    def print_piece(self, location):
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
