import tkinter as tk

window = tk.Tk()

def handle_click(event):
    print(event)
    print("click!")

cols = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i'}
rows = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8', 8: '9', 9: '10'}
rev_cols = {val:key for key, val in cols.items()}
rev_rows = {val:key for key, val in rows.items()}

board = {col + row: None for col in rev_cols for row in rev_rows}

def what_button(x):
    "Print out the button label."

    print(x)

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
            btn = tk.Button(master=frame, text=" " + name + " ", command= lambda: what_button(btn["text"]))
        else:
            btn = tk.Button(master=frame, text=name, command=lambda: what_button(btn["text"]))
        board[col + ro] = btn
        btn.pack()

window.mainloop()
