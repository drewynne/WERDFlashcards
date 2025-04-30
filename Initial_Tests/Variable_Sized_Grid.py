import tkinter as tk
import random


def update_grid(rows, cols):

    for widget in root.winfo_children():
        widget.destroy()
    
    for row in range(rows):
        for col in range(cols):
            button_text = f"{row}, {col}"
            button = tk.Button(root, text=button_text, command=lambda r=row, c=col: click(r, c))
            button.grid(row=row, column=col, ipadx=5, ipady=5)


def click(row, column):
    print(f"Button clicked is: {row}, {column}")

    rows = random.randint(4, 6)
    cols = random.randint(3, 4)

    update_grid(rows, cols)

root = tk.Tk()
root.title("Variable Sized Grid")
# root.geometry("400x300")

rows, cols = 5, 4

click(rows, cols)



root.mainloop()