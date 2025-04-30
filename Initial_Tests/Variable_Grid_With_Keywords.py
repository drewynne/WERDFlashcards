import tkinter as tk
from tkinter import messagebox
import random
from operator import index

from Data import *

# Define a common font to be used across the buttons and labels in the application
my_font = ("Arial", 12)


def update_grid(rows, cols):
    """
    Dynamically updates the GUI grid with a specified number of rows and columns.
    Each cell in the grid displays words in one of the foreign languages.
    The function also creates a new question for the user.
    """
    # Clear all existing widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Convert the language dictionary into a list of items and shuffle them randomly
    multi_language_items = list(multi_language_dict.items())
    random.shuffle(multi_language_items)

    foreign_languages = language_tuple_list.copy()
    foreign_languages.remove(("English", 0))
    random.shuffle(foreign_languages)

    for i in range(len(foreign_languages) - cols):
        foreign_languages.pop()

    #language_list = random.sample(language_tuple_list, cols)
    #language = language_list[0][0]
    language = foreign_languages[0][0]
    answer_language = random.choice(foreign_languages)
    answer_position = foreign_languages.index(answer_language)

    debugging_answer = True
    if debugging_answer:
        print(f"Answer language = {answer_language[0]}")
        print(f"Answer position = {answer_position}")

    ask_question(answer_language[0])

    button_frame = tk.Frame(root)
    button_frame.grid(row=rows, column=0, columnspan=cols, sticky="ew")

    sample = random.sample(multi_language_items, rows)
    english_words = [word[0] for word in sample]
    words = english_words.copy()
    prepare_hint(button_frame, foreign_languages, words)


    for row in range(rows):

        sample_row = sample[row][1]
        for col in range(cols):
            index = foreign_languages[col][1]
            word = sample_row[index - 1]
            # button_text = f"{language_list[col][0]} {row}"
            # button_text = sample[row][1][col]
            button_text = word
            button = tk.Button(button_frame, text=button_text, font=my_font,
                               command=lambda r=row, c=col, fl=foreign_languages, ac=answer_position: click(r, c, fl, ac))
            button.grid(row=row + 1, column=col + 1, ipadx=5, ipady=5, sticky="ew")
            button.bind("<Enter>", on_enter)
            button.bind("<Leave>", on_leave)


def ask_question(language):
    """
    Displays a question at the top of the GUI, asking the user to click a specific column.
    Args:
        language (str): Target language for the question.
    """
    # Construct the question text and display it in a label at the top of the GUI
    """
    Displays a question asking the user to click the correct column.

    Args:
        language (str): The language of the correct column.
    """
    # language = "French"
    question_text = f"Click in the {language} column"
    print("Question = ", question_text)
    question = tk.Label(root, text=question_text, font=my_font)
    question.grid(row=0, column=0, ipadx=5, ipady=5, sticky="ew")


def prepare_hint(button_frame, foreign_languages, words):
    """
    Adds a "Pass" button to the GUI, providing the user with hints for assistance.
    Args:
        button_frame (tk.Frame): Frame where hint labels are added.
        foreign_languages (list): List of languages available in the grid.
        words (list): List of English words corresponding to hints.
    """
    # Create a button labeled "Pass" that displays hints for the user
    """
    Adds a hint button to the GUI that provides additional information when clicked.

    Args:
        button_frame (tk.Frame): The frame containing the buttons.
        foreign_languages (list): List of foreign language tuples.
        words (list): List of English words for reference.
    """
    hint_button = tk.Button(root, text="Pass", font=my_font, bg="orange",
                            command=lambda bf=button_frame, fl=foreign_languages, w=words: hint_click(bf, fl, w))
    hint_button.grid(row=0, column=1, ipadx=5, ipady=5, sticky="ew")


def on_enter(event):
    """
    Changes the button background and text color when the mouse hovers over it.
    Args:
        event: Mouse hover event bound to the widget.
    """
    """
    Changes the background and foreground color of a widget when the mouse enters it.

    Args:
        event: The mouse enter event.
    """
    event.widget["background"] = "cyan"
    event.widget["foreground"] = "black"


def on_leave(event):
    """
    Resets the button background and text color to default when the mouse leaves it.
    Args:
        event: Mouse leave event bound to the widget.
    """
    """
    Resets the background and foreground color of a widget when the mouse leaves it.

    Args:
        event: The mouse leave event.
    """
    event.widget["background"] = "SystemButtonFace"
    event.widget["foreground"] = "black"


def click(row, column, foreign_languages, answer_position):
    """
    Handles clicks on individual buttons in the grid.
    Checks if the clicked button is in the correct column and provides feedback through a dialog.
    Args:
        row (int): Row index of the clicked button.
        column (int): Column index of the clicked button.
        foreign_languages (list): List of languages in the grid.
        answer_position (int): Column index of the correct language.
    """
    """
    Handles the event when a button in the grid is clicked.

    Args:
        row (int): The row index of the button.
        column (int): The column index of the button.
        foreign_languages (list): List of foreign language tuples for the grid.
        answer_position (int): The column index of the correct answer.

    This function checks whether the user's selection is correct, displays the result, 
    and updates the grid with a new question and layout.
    """
    print("----------")
    print(f"Button clicked is: {row}, {column}")

    print(f"Column clicked = {column + 1}")
    language = foreign_languages[column][0]
    language_index = foreign_languages.index(foreign_languages[column])
    print(f"Language clicked = {language}")
    user_answer = language_tuple_list[language_index + 1][0]

    if answer_position == column:
        print("\nCorrect!\n")
        result_messagebox("Result!", "Correct!", "green")
    else:
        print("Incorrect!")
        print(f"\tThe correct answer was: {language}")
        print(f"\tYour answer was: {user_answer}")
        result_messagebox("Result!",
                          f"Incorrect! You clicked the {foreign_languages[column][0]} column",
                          "red")

    print("----------")
    rows = random.randint(4, 6)
    cols = random.randint(3, 6)

    update_grid(rows, cols)


def hint_click(button_frame, foreign_languages, words):
    """
    Displays hints for the user with labels indicating the expected translations.
    Args:
        button_frame (tk.Frame): Frame where hint labels are added.
        foreign_languages (list): List of target foreign languages.
        words (list): Corresponding English words for reference.
    """
    print("Hint clicked")

    hint_row_text = foreign_languages
    hint_column_text = words

    for i in range(len(hint_row_text)):
        lang_text = hint_row_text[i][0]
        lang_txt_box = tk.Label(button_frame, height=1, width=len(lang_text), font=my_font, text=lang_text)
        lang_txt_box.grid(row=0, column=i + 1, ipadx=5, ipady=5, sticky="ew")

    for i in range(len(hint_column_text)):
        word_text = hint_column_text[i]
        word_txt_box = tk.Label(button_frame, height=1, width=len(word_text), font=my_font, text=word_text)
        word_txt_box.grid(row=i + 1, column=0, ipadx=5, ipady=5, sticky="ew")


def result_messagebox(title, message, bg_color):
    """
    Displays a custom result dialog with a message and a background color based on the result.
    Args:
        title (str): Title of the dialog box.
        message (str): Message to display in the dialog box.
        bg_color (str): Background color of the dialog box (e.g., green for correct, red for incorrect).
    """
    # Create a custom Toplevel dialog for a customizable messagebox
    dialog = tk.Toplevel(root)
    width = len(message) * 10
    dialog.geometry(f"{width}x50+300+300")
    dialog.resizable(False, False)

    dialog.title(title)
    dialog.configure(bg=bg_color)  # Use `bg_color` for the dialog's background

    # Add label with the message
    label = tk.Label(dialog, text=message, font=my_font, bg=bg_color, fg="white")
    label.pack(pady=10, padx=10)

    # Add OK button to close the dialog
    # ok_button = tk.Button(dialog, text="OK", command=dialog.destroy, font=my_font)
    # ok_button.pack(pady=10)

    # Center the dialog on the main window
    dialog.transient(root)
    dialog.grab_set()
    dialog.after(500, dialog.destroy)
    root.wait_window(dialog)


# Create the main application window
root = tk.Tk()

root.title("Variable Sized Grid")
# root.geometry("400x300")

# Initialize default values for grid dimensions
rows, cols = 5, 4

foreign_languages = language_tuple_list.copy()

click(rows, cols, foreign_languages, 2)

root.mainloop()
