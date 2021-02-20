# Author: Nathan Taylor
# Date: 2/19/2021
# Description: A Python implementation of Janggi.

columns = { 
    'a': 0, 
    'b': 1, 
    'c': 2, 
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8
}
rows = {
    '1': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    '10': 9
}
board = {column + row: None for column in columns for row in rows}
def get_pos_tuple(pos):
    """
    Converts the position "b5", for example, to the position tuple 
    (1,4) (column, row).
    """

    return (columns[pos[0]], rows[pos[1:]])

def print_board():
    "Prints a representation of the board."

    for row in rows:
        for col in columns:
            if col + row == "b5":
                print("BE1  ", end="")
            elif col + row == "i8":
                print("BG   ", end="")
            else:
                print(" .   ", end="")
        print()

print(len(board))
print(board)
print(get_pos_tuple("b5"))
print_board()