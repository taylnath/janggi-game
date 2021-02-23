import tkinter as tk
import JanggiGame

g = JanggiGame.JanggiGame()

window = tk.Tk()

cols = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i'}
rows = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8', 8: '9', 9: '10'}
rev_cols = {val:key for key, val in cols.items()}
rev_rows = {val:key for key, val in rows.items()}

board = {col + row: tk.StringVar() for col in rev_cols for row in rev_rows}
buttons = {col + row: None for col in rev_cols for row in rev_rows}

def update_board():
    b = g.get_board()

    for name in board:
        piece = b.get_piece(name)

        if piece is None:
            board[name].set("      ")
        else:
            board[name].set(piece.get_name())


def clear_colors():
    global buttons

    for name in buttons:
        buttons[name].configure(bg = "#F0F0F0")
        buttons[name].configure(activebackground = "#F0F0F0")

move_from = True
from_loc = ""

def select_move(selection):
    "Print out the button label."
    global move_from
    global from_loc
    if move_from:
        move_from = False
        from_loc = selection
        piece = g.get_board().get_piece(from_loc)
        if piece is not None:
            for move in piece.get_moves():
                buttons[move].configure(bg="red")
                buttons[move].configure(activebackground="red")
    else:
        move_from = True
        g.make_move(from_loc, selection)
        update_board()
        clear_colors()

# create the window

for col in cols:
        # column labels
        frame = tk.Frame(master = window)
        frame.grid(row=0, column=col+1)
        lbl = tk.Label(master=frame, text=" " + cols[col] + " ")
        lbl.pack()

for col in cols:
    for ro in rows:
        # row labels
        frame = tk.Frame(master = window)
        frame.grid(row=ro + 1, column=0)
        if ro < 9:
            lbl = tk.Label(master=frame, text=" " + rows[ro] + " ")
        else:
            lbl = tk.Label(master=frame, text=rows[ro])
        lbl.pack()

        # position buttons
        frame = tk.Frame(
                master = window,
                relief = tk.RAISED,
                borderwidth = 1
        )
        frame.grid(row=ro + 1, column=col + 1)
        name = cols[col] + rows[ro]
        if ro < 9:
            btn = tk.Button(master=frame, textvariable=board[name], command= lambda txt=name: select_move(txt))
        else:
            btn = tk.Button(master=frame, textvariable = board[name], command=lambda txt=name: select_move(txt))
        buttons[name] = btn
        btn.pack()

if __name__ == "__main__":
    update_board()
    clear_colors()
    window.mainloop()
