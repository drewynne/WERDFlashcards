import time


class AnswerTimer:

    max_time = 120

    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.time_elapsed = 0
        self.is_running = False
        self.is_correct = False

    def start(self):
        self.start_time = time.time()
        self.is_running = True

    def stop(self, is_correct):
        self.end_time = time.time()
        self.time_elapsed = self.end_time - self.start_time
        self.is_running = False
        self.is_correct = is_correct

    def get_time_elapsed(self):
        if not self.is_correct:
            self.time_elapsed += 10
            self.time_elapsed *= 2.0 # Time Penalty for incorrect Answers
            if self.time_elapsed > self.max_time:
                self.time_elapsed = self.max_time
        return self.time_elapsed

    @staticmethod
    def divide_time(time_elapsed, question_type, rows, cols):
        divided_time = 5
        if question_type == 0:
            divided_time = time_elapsed / cols
        elif question_type == 1:
            divided_time = time_elapsed / rows
        else:
            divided_time = time_elapsed / (rows * cols)
        return divided_time