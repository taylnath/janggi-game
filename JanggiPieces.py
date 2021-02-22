# pieces for the Janggi game


class JanggiBoard:
    "A class to represent the Janggi game board."

    def __init__(self):

        self._columns = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8}
        self._rev_columns = {val : key for key, val in self._columns.items()}
        self._rows = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9}
        self._rev_rows = {val : key for key, val in self._rows.items()}
        self._board = {column + row: None for column in self._columns for row in self._rows}
        self._palace = [col + str(row) for row in [1,2,3,8,9,10] for col in ['d', 'e', 'f']]

    def loc_to_tuple(self, pos):
        """
        Converts the position "b5", for example, to the position tuple 
        (1,4) (column, row).
        """

        return (self._columns[pos[0]], self._rows[pos[1:]])

    def tuple_to_loc(self, tup):
        """
        Converts the tuple (1,4), for example, to the position 
        string "b5".
        """

        return self._rev_columns[tup[0]] + self._rev_rows[tup[1]]

    def get_piece(self, loc):
        """
        Returns the piece at the given location (for 
        example "b5".) Returns None if there is no 
        piece at that location.
        """

        return self._board[loc]

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

    def get_moves(self):
        """
        If the piece is in the palace, returns the possible moves 
        for this piece in the palace. Otherwise returns the normal 
        possible moves for the piece. 
        """

        if self._board.in_palace(self._loc):
            return self._moves["palace"]
        return self._moves["normal"]


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