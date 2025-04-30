import random


class QuestionAsker:

    question_type: int = 0
    question_text: str = ""
    answer_prompt: str = "" # Answer Prompt
    rows: int = 0
    cols: int = 0
    correct_answer: tuple = ()
    user_answer: tuple = ()
    foreign_language: str = ""
    word: str = ""


    def __init__(self):
        print("QuestionAsker initialized")

    def check_answer(self, correct_answer, user_answer):
        user_was_correct = False

        if self.question_type == 0: # Column Type Question
            if user_answer[1] == correct_answer[1]: # Check Column
                user_was_correct = True
                self.answer_prompt = "Correct!"
            else:
                self.answer_prompt = f"Incorrect! You clicked the {user_answer[1]} column."
        elif self.question_type == 1: # Row Type Question
            if user_answer[0] ==  correct_answer[0]: # Check Row
                user_was_correct = True
                self.answer_prompt = "Correct!"
            else:
                self.answer_prompt = f"Incorrect! You clicked the {user_answer[0]} row."
        else: # Position Question
            if user_answer == correct_answer: # Check Position
                user_was_correct = True
                self.answer_prompt = "Correct!"
            else:
                self.answer_prompt = "Incorrect!"
        return user_was_correct

    def ask_question(self, language, word):
        question_text = ""
        self.foreign_language = language
        self.word = word

        if self.question_type == 0: # Column Type Question
            question_text = f"Click in the {language} column"

        elif self.question_type == 1: # Row Type Question
            question_text = f"Click in the row for \"{word}\""

        else: # Position Type Question
            question_text = f"Click on the {language} word for \"{word}\""

        return question_text

    def update_question_type(self):
        self.question_type = random.randint(0, 2)

    def get_question_type(self):
        return self.question_type

    def get_foreign_language(self):
        return self.foreign_language

    def get_word(self):
        return self.word