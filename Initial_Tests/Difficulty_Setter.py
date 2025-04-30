
class DifficultySetter:

    target_time = 60.0
    average_time = 30.0
    min_difficulty = 1
    max_difficulty = 10

    def __init__(self, difficulty):
        if self.min_difficulty <= difficulty <= self.max_difficulty:
            self.difficulty = difficulty # Within range of 1 to 10
        else:
            self.difficulty = 5



    def update_difficulty(self, elapsed_time):
        divisor = 2 * self.target_time / self.max_difficulty
        self.difficulty = int((self.target_time - elapsed_time) / divisor)

        if self.difficulty < self.min_difficulty:
            self.difficulty = self.min_difficulty
        if self.difficulty > self.max_difficulty:
            self.difficulty = self.max_difficulty
        print("Difficulty: " + str(self.difficulty))


    def max_grid_size(self, question_type):
        max_rows = 2
        max_cols = 2
        if question_type == 0: # Looking for Column
            max_rows = 12 - self.difficulty
            max_cols = self.difficulty + 1
        elif question_type == 1: # Looking for Row
            max_rows = self.difficulty + 1
            max_cols = 12 - self.difficulty
        else: # Looking for Word
            max_rows = self.difficulty + 1
            max_cols = self.difficulty + 1

        return max_rows, max_cols

