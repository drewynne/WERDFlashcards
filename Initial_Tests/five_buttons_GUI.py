import tkinter as tk

def click(button_id):
    print("Button clicked is: ", button_id)

root = tk.Tk()
root.title("Multiple Buttons")
root.geometry("400x300")

for i in range(5):
    button = tk.Button(root, text="Button " + str(i+1), command=lambda i=i: click(i+1))
    button.pack(pady=10)

root.mainloop()