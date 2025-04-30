import tkinter as tk


def click(row, column):
    print(f"Button clicked is: {row}, {column}")


root = tk.Tk()
root.title("Grid of Buttons")
root.geometry("400x300")

rows, cols = 5, 4

for row in range(rows):
    for col in range(cols):
        button = tk.Button(root, text=f"{row}, {col}", command=lambda r=row, c=col: click(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()