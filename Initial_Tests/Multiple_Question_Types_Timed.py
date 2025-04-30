# Multiple_Question_Types_Timed.py
"""
Main application file for the WERD Flashcards language learning application.

This module creates a GUI application that presents users with a grid of words
in different languages and asks questions that require users to identify words
in specific languages or positions. The difficulty automatically adjusts based
on user performance.
"""
import logging
import random
import tkinter as tk

from Initial_Tests.Answer_Timer import AnswerTimer
from Initial_Tests.Data import language_tuple_list, Data
from Initial_Tests.Difficulty_Setter import DifficultySetter
from Initial_Tests.Question_Asker import QuestionAsker
from Initial_Tests.Time_Averager import TimeAverager
from Initial_Tests.TimeData import TimeData
from Initial_Tests.Word_Selector import WordSelector

# Define a common font to be used across the buttons and labels in the application
my_font = ("Arial", 12)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def update_grid(rows, cols):
    """
    Dynamically updates the GUI grid with a specified number of rows and columns.

    This function rebuilds the entire grid UI with new words and languages based on
    the current difficulty level. It handles the creation of buttons for each cell
    in the grid and sets up a new question for the user.

    Args:
        rows (int): Number of rows for the grid
        cols (int): Number of columns for the grid

    Raises:
        ValueError: If there aren't enough foreign languages or if the language data is invalid
    """
    # Clear all existing widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    global outer_frame
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    outer_frame = tk.Frame(root)
    outer_frame.grid(row=0, column=0, sticky="nsew")
    outer_frame.place(relx=0.5, rely=0.5, anchor="center")
    outer_frame.pack_propagate(False)

    word_selector.update_grid(difficulty_setter.difficulty)

    # Get foreign languages for the grid
    foreign_languages = word_selector.foreign_language_selector(cols)
    logger.debug(f"Foreign languages returned: {foreign_languages}")

    # Validate returned data to avoid runtime errors
    if not all(isinstance(lang, tuple) and len(lang) >= 2 for lang in foreign_languages):
        logger.error(f"Invalid foreign languages returned: {foreign_languages}")
        raise ValueError("Invalid foreign languages data structure from foreign_language_selector!")

    cols = len(foreign_languages)
    if len(foreign_languages) < 2:
        logger.error(f"Not enough foreign languages for grid: {len(foreign_languages)}")
        raise ValueError(f"Not enough foreign languages for grid: {len(foreign_languages)}")

    for lang in foreign_languages:
        if not isinstance(lang, tuple) or len(lang) < 2:
            logger.error(f"Invalid language tuple: {lang}")
            raise ValueError(
                f"Invalid language tuple: {lang}. Expected a tuple with at least two elements."
            )


    # Select a random language and word for the question
    language = foreign_languages[0][0]
    answer_language = random.choice(foreign_languages)
    answer_column = foreign_languages.index(answer_language)

    logger.debug(f"Answer language = {answer_language[0]}, Answer position = {answer_column}")



    # Create frame for buttons
    button_frame = tk.Frame(outer_frame)
    button_frame.grid(row=rows, column=0, columnspan=cols, sticky="ew")

    # Get sample words for the grid
    sample = word_selector.sample_selector(rows)

    # Validate sample
    rows = len(sample)
    if len(sample) < 2:
        logger.error(f"Not enough words for grid: {len(sample)}")
        raise ValueError(f"Not enough words for grid: {len(sample)}")

    # Select a random word for the question
    word = random.choice(sample)
    word_index = sample.index(word)

    # Update question type and ask a new question
    question_asker.update_question_type()
    ask_question(answer_language[0], word[0])

    # Extract English words for hints
    english_words = [word[0] for word in sample]
    words = english_words.copy()

    # Prepare hint button and labels
    prepare_hint(button_frame, foreign_languages, words)

    # Create grid of buttons
    answer_position = (word_index, answer_column)
    for row in range(rows):
        sample_row = sample[row][1]

        for col in range(cols):
            index = foreign_languages[col][1]

            # Validate index
            if not isinstance(index, int):
                logger.error(f"Expected an integer for index, but got {type(index)}: {index}")
                raise ValueError(f"Expected an integer for `index`, but got {type(index)}: {index}")

            if index <= 0 or index > len(sample_row):
                logger.warning(f"Index {index} out of range for sample row {sample_row}")
                continue

            # Create button with word in appropriate language
            word = sample_row[index - 1]
            button_text = word
            button = tk.Button(
                button_frame, 
                text=button_text, 
                font=my_font,
                command=lambda r=row, c=col, fl=foreign_languages, ap=answer_position: click(r, c, fl, ap)
            )
            button.grid(row=row + 1, column=col + 1, ipadx=5, ipady=5, sticky="ew")
            button.bind("<Enter>", on_enter)
            button.bind("<Leave>", on_leave)



def ask_question(language, word):
    """
    Displays a question at the top of the GUI and starts the answer timer.

    This function generates a question based on the current question type and
    displays it in a label at the top of the GUI. It also starts the answer timer.

    Args:
        language (str): Target language for the question
        word (str): Target word for the question
    """
    question_text = question_asker.ask_question(language, word)
    logger.debug(f"Question = {question_text}")

    question = tk.Label(outer_frame, text=question_text, font=my_font)
    question.grid(row=0, column=0, ipadx=5, ipady=5, sticky="ew")

    # Start timing the user's response
    answer_timer.start()


def prepare_hint(button_frame, foreign_languages, words):
    """
    Adds a "Pass" button to the GUI that provides hints when clicked.

    This function creates a button that, when clicked, displays labels showing
    the language names and English words to help the user answer the question.

    Args:
        button_frame (tk.Frame): Frame where hint labels will be added
        foreign_languages (list): List of language tuples (name, index) available in the grid
        words (list): List of English words corresponding to rows in the grid
    """
    hint_button = tk.Button(
        outer_frame, 
        text="Pass", 
        font=my_font, 
        bg="orange",
        command=lambda bf=button_frame, fl=foreign_languages, w=words: hint_click(bf, fl, w)
    )
    hint_button.grid(row=0, column=1, ipadx=5, ipady=5, sticky="ew")


def on_enter(event):
    """
    Changes the button background and text color when the mouse hovers over it.

    Args:
        event: Mouse hover event bound to the widget
    """
    event.widget["background"] = "cyan"
    event.widget["foreground"] = "black"


def on_leave(event):
    """
    Resets the button background and text color to default when the mouse leaves it.

    Args:
        event: Mouse leave event bound to the widget
    """
    event.widget["background"] = "SystemButtonFace"
    event.widget["foreground"] = "black"


def click(row, column, foreign_languages, answer_position):
    """
    Handles clicks on individual buttons in the grid.

    This function processes the user's click on a grid button, checks if it's correct,
    updates the performance data, adjusts difficulty, and generates a new grid.

    Args:
        row (int): Row index of the clicked button
        column (int): Column index of the clicked button
        foreign_languages (list): List of language tuples (name, index) in the grid
        answer_position (tuple): (row, column) of the correct answer
    """
    logger.debug(f"Button clicked at position: {row}, {column}")

    # Get the language of the clicked button
    language = foreign_languages[column][0]

    # Check if the answer is correct
    user_answer_pos = (row, column)
    correct_answer_pos = answer_position
    user_was_correct = question_asker.check_answer(correct_answer_pos, user_answer_pos)

    # Stop the timer and get elapsed time
    answer_timer.stop(user_was_correct)
    time_elapsed = answer_timer.get_time_elapsed()

    # Update time statistics
    time_averager.update(time_elapsed)
    average_time = time_averager.get_average()
    logger.info(f"Time elapsed: {time_elapsed:.2f}s, Average time: {average_time:.2f}s, Correct: {user_was_correct}")

    # Update time data entry for the word and language
    word = question_asker.get_word()
    foreign_language = question_asker.get_foreign_language()

    # Find the language index
    language_index = -1
    for lang, index in foreign_languages:
        if lang == foreign_language:
            language_index = index - 1
            break

    if language_index == -1:
        logger.warning(f"Language '{foreign_language}' not found in foreign languages")

    # Calculate adjusted time based on grid size and question type
    rows = len(words)
    cols = len(foreign_languages)
    adjusted_time = answer_timer.divide_time(time_elapsed, question_asker.get_question_type(), rows, cols)

    # Update performance data
    time_data.update_entry(word, language_index, adjusted_time)
    save_data()

    # Adjust difficulty based on performance
    difficulty_setter.update_difficulty(time_elapsed)

    # Show result to user
    result_color = "green" if user_was_correct else "red"
    result_messagebox("Result", question_asker.answer_prompt, result_color)

    # Generate new grid with appropriate dimensions
    max_rows, max_cols = difficulty_setter.max_grid_size(question_asker.get_question_type())
    rows = random.randint(2, max_rows)
    cols = random.randint(2, max_cols)
    update_grid(rows, cols)


def hint_click(button_frame, foreign_languages, words):
    """
    Displays hints for the user when the "Pass" button is clicked.

    This function adds labels to the grid showing the language names at the top
    and English words on the left side to help the user identify the correct cell.

    Args:
        button_frame (tk.Frame): Frame where hint labels are added
        foreign_languages (list): List of language tuples (name, index) in the grid
        words (list): List of English words corresponding to rows in the grid
    """
    logger.debug("Hint button clicked - displaying language and word labels")

    # Add language labels at the top of the grid
    for i, lang_tuple in enumerate(foreign_languages):
        lang_text = lang_tuple[0]
        lang_txt_box = tk.Label(
            button_frame, 
            height=1, 
            width=len(lang_text), 
            font=my_font, 
            text=lang_text
        )
        lang_txt_box.grid(row=0, column=i + 1, ipadx=5, ipady=5, sticky="ew")

    # Add word labels on the left side of the grid
    for i, word_text in enumerate(words):
        word_txt_box = tk.Label(
            button_frame, 
            height=1, 
            width=len(word_text), 
            font=my_font, 
            text=word_text
        )
        word_txt_box.grid(row=i + 1, column=0, ipadx=5, ipady=5, sticky="ew")


def result_messagebox(title, message, bg_color):
    """
    Displays a custom result dialog with feedback on the user's answer.

    This function creates a temporary dialog window that shows whether the user's
    answer was correct or incorrect. The dialog automatically closes after a short delay.

    Args:
        title (str): Title of the dialog box
        message (str): Message to display in the dialog box
        bg_color (str): Background color of the dialog box (green for correct, red for incorrect)
    """
    # Create a custom dialog window
    dialog = tk.Toplevel(root)

    # Size the dialog based on message length
    width = len(message) * 10
    dialog.geometry(f"{width}x50+300+300")
    dialog.resizable(False, False)

    # Set title and background color
    dialog.title(title)
    dialog.configure(bg=bg_color)

    # Add message label
    label = tk.Label(dialog, text=message, font=my_font, bg=bg_color, fg="white")
    label.pack(pady=10, padx=10)

    # Make dialog modal and auto-close after delay
    dialog.transient(root)
    dialog.grab_set()
    dialog.after(1000, dialog.destroy)
    root.wait_window(dialog)

def save_data():
    """
    Saves the user performance data to a CSV file.

    This function is called after each answer and when the application exits
    to ensure that user progress is not lost.
    """
    logger.info("Saving performance data")
    time_data.save_data()


def on_exit():
    """
    Handles the application exit event.

    This function is called when the user closes the application window.
    It saves any unsaved data before destroying the main window.
    """
    save_data()
    logger.info("Application closing")
    root.destroy()


def main():
    """
    Main function that initializes and runs the application.

    This function creates the main window, initializes all components,
    sets up the initial grid, and starts the main event loop.
    """
    global root, outer_frame, question_asker, answer_timer, time_averager
    global time_data, difficulty_setter, word_selector, words

    # Create and configure the main window
    root = tk.Tk()
    root.title("WERD Flashcards")
    root.protocol("WM_DELETE_WINDOW", on_exit)
    root.geometry("800x600+300+300")
    root.resizable(False, False)

    # Configure grid layout
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create main frame
    outer_frame = tk.Frame(root)
    outer_frame.grid(row=0, column=0, sticky="nsew")
    outer_frame.pack_propagate(False)

    # Initialize components
    logger.info("Initializing application components")

    # Question generation
    question_asker = QuestionAsker()
    question_asker.update_question_type()

    # Timing and performance tracking
    answer_timer = AnswerTimer()
    time_averager = TimeAverager()

    # Data management
    time_data = TimeData()
    time_data.import_data()

    # Difficulty management
    difficulty_setter = DifficultySetter(5)

    # Word and language selection
    data = Data()
    start_data = data.get_data()
    foreign_languages = language_tuple_list.copy()
    word_selector = WordSelector(start_data, time_data.get_data(), foreign_languages)

    # Initialize default values for grid
    words = ["as", "I", "his", "that", "he", "was", "for", "on", "are", "with"]
    rows, cols = 5, 4

    # Create initial grid
    logger.info("Creating initial grid")
    click(rows, cols, foreign_languages, (0, 0))

    # Start the main event loop
    logger.info("Application started")
    root.mainloop()


# Entry point of the application
if __name__ == "__main__":
    main()
