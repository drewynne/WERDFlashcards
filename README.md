# WERD Flashcards

A dynamic language learning application that helps users practice vocabulary across multiple languages through an interactive grid-based interface.

## Description

WERD Flashcards is an educational application designed to improve language learning through interactive exercises. The application presents users with a grid of words in different languages and asks questions that require users to identify words in specific languages or positions. The difficulty automatically adjusts based on user performance, making it suitable for learners at all levels.

## Features

- **Multiple Question Types**: 
  - Column-based questions (click in a specific language column)
  - Row-based questions (click in a row for a specific word)
  - Position-based questions (click on a specific language word for a given word)

- **Adaptive Difficulty**: The application automatically adjusts difficulty based on user performance, increasing or decreasing the grid size and complexity.

- **Performance Tracking**: Tracks user response times and accuracy to focus on words and languages that need more practice.

- **Time-Based Feedback**: Provides immediate feedback on answers with time penalties for incorrect responses.

- **Multi-Language Support**: Supports multiple languages for vocabulary practice.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/PythonProject3.git
   cd PythonProject3
   ```

2. Create and activate a virtual environment (recommended):
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install pandas
   ```

## Usage

1. Run the main application:
   ```
   python Initial_Tests\Multiple_Question_Types_Timed.py
   ```

2. The application will display a grid of words in different languages and ask you questions.

3. Click on the appropriate cell in the grid to answer the question.

4. The application will provide feedback on your answer and automatically adjust the difficulty based on your performance.

5. Use the "Pass" button if you need a hint, which will display the English words and language labels.

6. Your performance data is automatically saved when you exit the application.

## Project Structure

- **Multiple_Question_Types_Timed.py**: Main application file that creates the GUI and coordinates the different components.
- **Answer_Timer.py**: Handles timing functionality for tracking user response times.
- **Difficulty_Setter.py**: Adjusts difficulty based on user performance.
- **Question_Asker.py**: Generates questions and validates user answers.
- **Word_Selector.py**: Selects words and languages for the grid based on difficulty and user performance.
- **TimeData.py**: Manages and persists user performance data.
- **Data.py**: Provides access to the language and word data.

## Dependencies

- Python 3.6+
- tkinter (included in standard Python installation)
- pandas

## Data Files

- **multi_language_dict.csv**: Contains vocabulary words in multiple languages.
- **time_data.csv**: Stores user performance data for different words and languages.

## Contributing

Contributions to improve the application are welcome. Please feel free to submit a pull request or open an issue to discuss potential changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.