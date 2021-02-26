# Author: Nathan Taylor
# Date: 2/25/2021
# Description: A Halfway Progress report on my Python implementation of Janggi.

########################################################################
########################################################################
# Contents: 
#   (1). DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
#   (2). Docstrings and methods for classes.
########################################################################
########################################################################


########################################################################
########################################################################
# DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
########################################################################
########################################################################

########################################################################
# 1. Initializing the board.
########################################################################

#    The JanggiGame class begins by initializing an instance of the 
#    JanggiBoard class. This creates a board as an empty dictionary, 
#    with keys the location strings ("b5") and values None.
#
#    Next, the Pieces for each player are initialized. Each piece 
#    knows where it should be placed on the board, depending on which player
#    owns the piece and which number piece it is. The pieces place 
#    themselves on the board with the help of the JanggiMechanic method 
#    place_piece (the method basically just sets the board dictionary value 
#    for the specified location to be that piece).
#
#    After initialization, the board is a dictionary with keys the location 
#    strings, and values either Pieces, or None.

########################################################################
# 2. Determining how to represent pieces  at a given location on the board
########################################################################

#    The board represents pieces located at a given position via a dictionary 
#    with keys the location strings ("b5") and values the Pieces themselves.
#    
#    The pieces remember their location via their own JanggiPosition object.
#    The JanggiPosition object is basically a location string that knows how 
#    to convert itself to a tuple, and how to do vector addition.

########################################################################
# 3. Determining how to validate a given move according to the rules for each piece, turn taking and other game rules.
########################################################################

#    The make_move method first checks whether the game is finished already. 
#    If so, no moves are valid. 
#    
#    Next, the make_move method asks the board if there are pieces at 
#    the starting location and ending location. If there is no piece at 
#    the starting location, no move can be made. 
#    
#    Next, it checks if the owner of the piece in the starting location is 
#    owned by the current player. If not, no move can be made.
#    
#    Next, if the starting and ending locations are the same (and the 
#    current player is not in check), the move is skipped. 
#    
#    Next, make_move asks the piece at the starting location what moves 
#    it can make:
#       Each piece has a method called get_moves. The get_moves method returns 
#       a list of all valid moves for that piece from its current location. 
#       (without taking into account an in-check situation). The get_moves 
#       method does make sure a piece does not try to move into a location
#       where one of its own player is located.
#    If the move is not in that piece's valid moves, then the move cannot be made.
#    
#    Next, a trial move is performed: 
#       The board saves itself (creating a copy of the board dictionary).
#       Then we make the move, saving the captured piece (if a piece is captured). 
#       Next, we check to see if the move put the current player's general in check.
#       (the captured piece is used in the is_in_check method).
#           If the move does put the current general in check, we call the 
#           board's recover_board method, which restores the saved board and updates
#           Pieces' locations. Then we stop here, since the move cannot be made.
#           
#           If the move doesn't put the current player's general in check, 
#           we leave the move as-is.
#    
#    If the trial move is ok, we remove any captured pieces from the opponent's 
#    list of captured pieces.
#    
#    Next, we check if the current player has won the game, i.e. if the other 
#    player is now in checkmate (more on this below).
#    
#    Finally, update the current turn (alternating "R" to "B").

########################################################################
# 4. Modifying the board state after each move.
########################################################################

#    
#    
#    
#    
#    
#    
#    
#    

########################################################################
# 5. Determining how to track which player's turn it is to play right now.
########################################################################

########################################################################
# 6. Determining how to detect the checkmate scenario.
########################################################################

########################################################################
# 7. Determining which player has won and also figuring out when to check that.
########################################################################


########################################################################
########################################################################
# Docstrings and methods for classes.
########################################################################
########################################################################

########################################################################
# The JanggiBoard Class -- Representing the physical board
########################################################################

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
        pass

    def get_pieces(self):
        """
        Returns a list containing all pieces on the board.
        """
        pass

    def get_palace_pieces(self):
        """
        Returns a list containing all pieces in both palaces.
        """
        pass

    def save_board(self):
        """
        Saves the current state of the board. 
        Can be recovered with the recover_board method.
        Only one state is saved.
        """
        pass

    def recover_board(self):
        """
        Recovers the previous state of the board, as 
        stored in _saved_board. Updates the position of 
        each piece accordingly.
        """
        pass

    def loc_on_board(self, loc:str) -> bool:
        """
        Returns True if the location is on the board. Returns False 
        otherwise.
        """
        pass

    def tuple_on_board(self, tup:tuple) -> bool:
        """
        Returns True if the tuple is on the board. Returns False otherwise.
        """
        pass

    def loc_to_tuple(self, loc:str):
        """
        Converts the string location "b5", for example, to the position tuple 
        (1,4) (column, row). Returns None if the location is invalid.
        """
        pass


    def tuple_to_loc(self, tup:tuple):
        """
        Converts the tuple (1,4), for example, to the position 
        string "b5". If the tuple is not on the board, returns None.
        """
        pass

    def get_piece(self, loc:str):
        """
        Returns the piece at the given location (for 
        example "b5".) Returns None if there is no 
        piece at that location, or if the location is invalid.
        """
        pass

    def clear_loc(self, loc:str):
        """
        Clears the location (loc) on the board (sets its value to None).
        Does nothing if (loc) is not on the board.
        """
        pass

    def set_piece(self, piece, loc:str):
        """
        Moves (piece) to (loc) on the board. Does nothing if loc 
        is not on the board. Does not check legality of the move.
        Does not clear the piece's old location.
        """
        pass

    def get_player(self, loc:str):
        """
        Returns the player who owns the piece at the given location.
        Returns None if there is no piece there.
        """
        pass

    def in_palace(self, loc:str) -> bool:
        """
        Returns True if the given location (for example "e3") 
        is in the palace. Returns False otherwise.
        """
        pass

    def print_piece(self, location:str):
        """
        Prints a piece on the board at the given location. 
        To be used with print_board.
        """
        pass

    def print_board(self):
        "Prints a representation of the board."
        pass

########################################################################
# The JanggiPosition Class -- Representing a position on the board
########################################################################

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
        pass

    def __repr__(self):
        "Return the position's location string."
        pass


    def set_pos(self, pos):
        """
        Set the position. pos can be either a tuple or a 
        location string. If the position is not 
        on the board, both _loc and _tuple are set to None.
        """
        pass

    def get_tuple(self) -> tuple:
        "Returns the position's tuple representation."
        pass

    def get_loc(self) -> str:
        "Returns the position's location string representation."
        pass

    def add_tuples(self, tup1:tuple, tup2:tuple) -> tuple:
        """
        Performs vector addition on the two tuples, and 
        returns the sum.
        For example, (1,2) + (0,1) = (1,3).
        """
        pass

    def shift(self, movement:tuple):
        """
        Shifts the position by the movement tuple (using vector 
        addition). Returns a new JanggiPosition with the shifted coordinates.
        """
        pass

########################################################################
# The JanggiPieces Classes -- Representing the Pieces on the board
########################################################################

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
        pass

    def get_name(self) -> str:
        "Returns the piece's name."
        pass

    def get_player(self) -> str:
        "Returns the player that owns this piece."
        pass
    
    def get_pos(self) -> JanggiPosition:
        "Returns the piece's current position."
        pass

    def get_loc(self) -> str:
        "Returns the piece's current location string."
        pass
    
    def set_pos(self, loc:str):
        "Sets the current position of the piece."
        pass

    def pos_on_board(self, pos:JanggiPosition) -> bool:
        """
        Returns True if the position pos is on the board. 
        Returns False otherwise. 
        """
        pass

    def get_pos_player(self, pos:JanggiPosition):
        """
        If there is a piece at the given position, returns
        the player who owns that piece. If there is no piece 
        at the position or the position is invalid, returns None.
        """
        pass

    def loc_from_pos(self, pos):
        """
        Takes either a JanggiPosition object or a location string (i.e. "b5")
        as input. If given a JanggiPosition object, loc_from_pos converts it 
        to a location string, and returns that string. If given a location 
        string, loc_from_pos returns that string. Does not check if the 
        location or position is on the board.
        """
        pass

    def is_open(self, pos):
        """
        Takes either a JanggiPosition object or a location string (i.e. "b5")
        as input. Returns True if the position is valid and doesn't contain a piece.
        Returns False otherwise. 
        """
        pass

    def is_us(self, pos):
        """
        Takes either a JanggiPosition object or a location string (i.e. "b5") 
        as input. Returns True if the position contains a piece owned by 
        the current player. Returns False otherwise. 
        """
        pass

    def is_not_us(self, pos):
        """
        Takes either a JanggiPosition object or a location string (i.e. "b5") 
        as input. Returns True if the position does not contain a piece owned by 
        the current player. Returns False otherwise. 
        """
        pass

    def is_opponent(self, pos):
        """
        Takes either a JanggiPosition object or a location string (i.e. "b5") 
        as input. Returns True if the position contains a piece owned by 
        the opposite player. Returns False otherwise. 
        """
        pass

    def is_piece(self, pos):
        """
        Takes either a JanggiPosition object or a location string (i.e. "b5")
        as input. Returns True if the position contains a piece owned by 
        either player. Returns False otherwise. 
        """
        pass

    def ok_to_move_here(self, pos):
        """
        Takes either a JanggiPosition object or a location string (i.e. "b5") 
        as input. Returns True if the position is on the board and 
        does not contain a piece owned by the current player. 
        Returns False otherwise. 
        """
        pass

class Elephant(Piece):
    """
    A class to represent the Elephant piece.
    """

    def __init__(self, player, number, board):
        "Initialize the elephant."
        pass

    def get_moves(self) -> list:
        "Returns a list of valid moves for this Elephant."
        pass

class General(Piece):
    " A class to represent the General piece."

    def __init__(self, player, board):
        "Initialize the general."
        pass

    def get_moves(self):
        "Returns a list of valid moves for the General."
        pass

class Advisor(Piece):
    "A class to represent the Advisor piece."

    def __init__(self, player, number, board):
        "Initialize the advisor."
        pass

    def get_moves(self):
        "Returns a list of valid moves for the Advisor."
        pass

class Chariot(Piece):
    "A class to represent a Chariot piece."

    def __init__(self, player, number, board):
        "Initialize the Chariot."
        pass

    def get_step(self, start:JanggiPosition, direction:tuple) -> JanggiPosition:
        """
        Generator function that finds the next position
        on the board in the given direction. Starts at the 
        start position. Returns the next position 
        while the next position is on the board.
        """
        pass

    def get_move(self, direction:tuple) -> str:
        """
        Generator function that finds the next valid move 
        in the given direction. 
        """
        pass

    def get_moves(self) -> list:
        "Returns a list of valid moves for this Cannon."
        pass

class Cannon(Piece):
    "A class to represent the Cannon piece."

    def __init__(self, player, number, board):
        "Initialize the Cannon."
        pass

    def is_cannon(self, pos:JanggiPosition) -> bool:
        """
        Returns True if there is a Cannon at the given 
        position. Returns False otherwise.
        """
        pass

    def get_step(self, start:JanggiPosition, direction:tuple) -> JanggiPosition:
        """
        Generator function that finds the next position
        on the board in the given direction. Starts at the 
        start position. Returns the next position 
        while the next position is on the board.
        """
        pass

    def get_jump_pos(self, direction:tuple):
        """
        Returns the position of the next piece in the given direction 
        (starting at the Cannon's current position). This is the position
        the Cannon will jump over.
        Returns False if no piece is found.
        """
        pass

    def get_move(self, direction:tuple) -> str:
        """
        Generator function that finds the next valid move 
        in the given direction. 
        """
        pass

    def get_moves(self) -> list:
        "Returns a list of valid moves for this Cannon."
        pass

class Horse(Piece):
    "A class to represent the Horse piece."

    def __init__(self, player, number, board):
        "Initialize the horse."
        pass

    def get_moves(self) -> list:
        "Returns a list of valid moves for this Horse"
        pass

class Soldier(Piece):
    "A class to represent the Soldier piece."

    def __init__(self, player, number, board):
        "Initialize the soldier."
        pass

    def get_moves(self):
        "Returns a list of valid moves for this Soldier."
        pass

########################################################################
# The JanggiMechanic Class -- Moving Pieces on the board
########################################################################

class JanggiMechanic:
    """
    A class to update the Janggi game board. 
    Used by the JanggiGame class to move pieces on the board,
    and to initially place pieces on the board.
    """

    def __init__(self, board:JanggiBoard):
        "Initialize the mechanic with a JanggiBoard object."
        pass

    def place_piece(self, piece):
        """
        Used to initially place a piece on the board. 
        Attempts to place the given piece at the given position.
        Returns False and changes nothing if there is already a piece at the position, 
        otherwise returns True and places the piece.
        """
        pass

    def move_piece(self, piece, loc:str):
        """
        Moves the (piece) to the given location (loc).
        Returns the piece which was captured, or None 
        if no piece was captured.
        """
        pass

########################################################################
# The JanggiGame Class -- Representing a game of Janggi
########################################################################

class JanggiGame:
    "A class to represent the Janggi game."

    def __init__(self):
        """
        Initialize the game with a populated board, starting 
        player "B"lue, and starting _state "UNFINISHED".
        """
        pass

    def get_player(self) -> str:
        "Returns the current player."
        pass

    def get_in_check(self, player:str) -> str:
        "Returns the string 'Yes' if the player is in check."
        pass

    def get_game_state(self) -> str:
        """
        Returns 'UNFINISHED', 'RED_WON', or 'BLUE_WON', 
        depending on the state of the game.
        """
        pass

    def get_general(self, player:str) -> General:
        """
        Returns the general belonging to the given player.
        """
        pass

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
        pass

    def get_opponent(self, player:str) -> str:
        """
        Returns the player opposing the given player.
        I.e. returns "R" if the given player is "B".
        """
        pass

    def update_turn(self):
        """
        Changes the current turn from 'B' to 'R' or 
        from 'R' to 'B'. (should this be called brb?)
        """
        pass

    def get_board(self) -> JanggiBoard:
        """
        Returns the game board.
        """
        pass

    def try_move(self, piece, move_to):
        """
        Saves the board, then makes the given move (if valid).
        If the move puts the current player in check, try_move 
        restores the board and returns False.
        """
        pass

    def check_if_player_won(self, player:str) -> bool:
        """
        Checks if the opponent to the given player is in check and 
        has no moves to get out of check.
        """
        pass

    def declare_winner(self, player:str):
        """
        Declares the (player) to be the winner.
        """
        pass

    def make_move(self, move_from, move_to):
        """
        Attempts to move a piece located at move_from location to 
        the move_to location.
        """
        pass
