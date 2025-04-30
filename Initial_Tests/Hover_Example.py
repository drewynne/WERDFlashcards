import tkinter as tk

# Function to change the button color when hovered over
def on_enter(e):
    e.widget['background'] = 'cyan'  # Change to desired hover color
    e.widget['foreground'] = 'black'

# Function to revert the button color when the mouse leaves
def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'  # Revert to default color
    e.widget['foreground'] = 'black'

# Create the main window
root = tk.Tk()
root.title("Hover Example")

# Create a button
button = tk.Button(root, text="Hover over me!")
button.pack(pady=20)

# Bind hover events to the button
button.bind("<Enter>", on_enter)  # Mouse enters the button
button.bind("<Leave>", on_leave)  # Mouse leaves the button

# Run the application
root.mainloop()