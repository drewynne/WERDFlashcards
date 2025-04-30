import tkinter as tk

def click():
    print("Button clicked")

window = tk.Tk()
window.title("GUI")
window.geometry("400x300")

button = tk.Button(window, text="Click Me", command=click)
button.pack()



window.mainloop()