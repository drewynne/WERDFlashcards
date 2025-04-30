# Word Selector Class
import random

import pandas as pd

from Initial_Tests.Data import multi_language_dict, language_tuple_list
from Initial_Tests.TimeData import TimeData


class WordSelector:
    """
    Represents a word selection and management system with functionalities
    for grid generation, sorting, and manipulation based on different
    parameters such as difficulty, time, and languages.

    This class is responsible for handling word grid structures and
    foreign language selections, leveraging underlying data like
    starting word grids, language tuples, and time-based information.

    :ivar word_grid: Represents a grid of words filtered and organized based
        on various rules and selection criteria.
    :ivar foreign_languages: List of foreign languages available for
        selection, excluding English by default.
    :ivar start_data: Stores the initial word grid data for configuration
        and manipulation during different difficulty settings.
    :ivar time_data: A pandas DataFrame storing time-based statistics for
        words and languages, used for sorting and selection.
    :ivar language_tuple_list: A list of language tuples used for operations
        like filtering and grid configuration.
    """
    word_grid: dict
    foreign_languages: list

    start_data: dict
    time_data: pd.DataFrame
    language_tuple_list: list




    def __init__(self, start_data: dict, time_data: pd.DataFrame, language_tuple_list: list):
        self.time_data = time_data
        self.start_data = start_data
        self.word_grid = self.easy_grid(start_data, time_data)
        self.language_tuple_list = language_tuple_list

    def get_word(self):
        pass

    def update_word(self):
        pass

    def select_words(self):
        words = None
        return words

    def update_grid(self, difficulty: int):
        """
        Updates the grid for the application based on the specified difficulty level.

        This method modifies the grid of words and associated data by filtering and
        selecting specific entries according to the given difficulty. The function
        adjusts the range of words and languages used in the grid, ensuring that only
        words meeting the proficiency and time criteria are included. The method
        utilizes predefined data structures such as `self.start_data`, `self.time_data`,
        and `self.language_tuple_list` while updating the grid.

        :param difficulty: An integer representing the difficulty level. It must be
            within the range 1 to 10, inclusive.
        :type difficulty: int
        :return: None
        """


        big_grid = self.start_data.copy()
        keys = list(big_grid.keys())
        all_cols = list(range(11))

        dead_zone = False

        print(f"Updating grid with difficulty: {difficulty}")
        assert 1 <= difficulty <= 10
        if difficulty < 4: # Easy Difficulty
            start_row, end_row, start_col, end_col, target_time_per_word = 0, 30, 0, 5, 5.0 # Zone 1
            words = list(self.sort_words_by_time(self.time_data, keys))
            col_list = list(range(start_col, end_col + 1))
            languages = self.sort_language_by_time(self.time_data, col_list)

        elif difficulty < 7: # Medium Difficulty
            start_row, end_row, start_col, end_col, target_time_per_word = 25, 300, 0, 7, 15.0 # Zone 2
            if random.random() < 0.5:
                dead_zone = True

            if dead_zone:
                print("Dead_zone = True")
                start_row, end_row, start_col, end_col, target_time_per_word = 0, 30, 4, 10, 15.0 # Dead Zone

            # words = list(self.time_data.iloc[start_row:end_row].loc[:, start_col:end_col])
            words = list(self.time_data.index[start_row:end_row])
            random.shuffle(words)
            print(words)
            languages = list(range(start_col, end_col + 1))

        else: # Hard Difficulty
            start_row, end_row, start_col, end_col, target_time_per_word = 250, 1000, 0, 10, 25.0 # Zone 3
            words = list(reversed(self.sort_words_by_time(self.time_data, keys)))
            col_list = list(range(start_col, end_col + 1))
            languages = list(reversed(self.sort_language_by_time(self.time_data, col_list)))

        #avg_words = self.sort_words_by_time(self.time_data, keys)
        #avg_languages = self.sort_language_by_time(self.time_data, all_cols)
        #avg_languages = {key: avg_languages[key] for key in avg_languages if key in range(start_col, end_col + 1)}

        selected_keys = words[0:30]

        # Add words that are over time. ie the user is not fluent in them yet
        time_multiplier = len(languages) / len(all_cols)
        self.add_over_time_words(selected_keys, target_time_per_word, time_multiplier, words)

        selected_keys = [key for key in selected_keys if key in big_grid]
        # selected_keys = [key for key in selected_keys if key in avg_languages]
        if len(selected_keys) == 0:
            print("len(selected_keys) == 0")
        # selected_keys += [key for key in languages if languages[key] > target_time_per_word]

        selected_keys = [key for key in selected_keys if key in keys]

        print("Selected keys = ", selected_keys)
        if len(selected_keys) < 2:
            selected_keys = big_grid.keys()
            print("Increasing difficulty to 10 because of low time per word. New length of selected keys = ",
                  len(selected_keys))


        for key in list(big_grid.keys()):
            if key not in selected_keys:
                big_grid.pop(key)

        grid = {key: big_grid[key] for key in selected_keys}

        # Update Local Data
        self.word_grid = grid

        self.foreign_languages = [("English", 0)]
        for i in languages:
            if i + 1 < len(self.language_tuple_list):
                self.foreign_languages.append(self.language_tuple_list[i + 1])

    def add_over_time_words(self, selected_keys, target_time_per_word, time_multiplier, words):

        for word in words:
            if word not in selected_keys:
                if self.time_data.loc[word].sum() > target_time_per_word * time_multiplier:
                    selected_keys.append(word)
                    if len(selected_keys) == 10:
                        break

    def easy_grid(self, word_grid: dict, time_data: pd.DataFrame):
        keys = list(word_grid.keys())

        avg_words = self.sort_words_by_time(time_data, keys)

        selected_keys = list(avg_words.keys())[0:10]
        grid = {key: word_grid[key] for key in selected_keys}

        return grid

    def get_grid(self):
        return self.word_grid

    def sort_words_by_time(self, time_data: pd.DataFrame, words: list):
        avg_word_dict = dict()
        for word in words:
            avg_time = sum(time_data.loc[word]) / len(time_data.loc[word])
            avg_word_dict[word] = avg_time

        avg_word_dict = dict(sorted(avg_word_dict.items(), key=lambda item: item[1]))
        return avg_word_dict

    def sort_language_by_time(self, time_data: pd.DataFrame, language_index: list):
        avg_lang_dict = dict()
        for lang_num in language_index:
            if lang_num in time_data.columns:
                avg_time = sum(time_data.loc[:, lang_num]) / len(time_data.loc[:, lang_num])
                avg_lang_dict[lang_num] = avg_time
            else:
                print(f"Invalid language index: {lang_num}. Skipping update")

        avg_lang_dict = dict(sorted(avg_lang_dict.items(), key=lambda item: item[1]))
        return avg_lang_dict

    def foreign_language_selector(self, cols: int) -> list:
        foreign_languages = self.foreign_languages.copy()
        if ("English", 0) in foreign_languages:
            foreign_languages.remove(("English", 0))
        random.shuffle(foreign_languages)
        for _ in range(len(foreign_languages) - cols):
            foreign_languages.pop()
        return foreign_languages



    def sample_selector(self, rows: int) -> list:
        items_list = list(self.word_grid.items())[:rows]
        random.shuffle(items_list)
        return items_list


if __name__ == "__main__":
    start_data = multi_language_dict
    start_languages = language_tuple_list
    time_data = TimeData()
    time_data.import_data()
    word_selector = WordSelector(start_data, time_data.get_data(), language_tuple_list)

    words = ["as", "I", "his", "that", "he", "was", "for", "on", "are", "with"]
    sorted_words = word_selector.sort_words_by_time(time_data.get_data(), words)
    print(sorted_words)

    languages = [x for x in range(5)]
    sorted_languages = word_selector.sort_language_by_time(time_data.get_data(), languages)
    print(sorted_languages)

    simple_grid = word_selector.get_grid()

    foreign_languages = word_selector.foreign_language_selector(4)
    print("Foreign Languages:")
    print(foreign_languages)

    print(simple_grid.keys())

    for i in range(10):
        difficulty = random.randint(1, 10)
        word_selector.update_grid(difficulty)
        new_grid = word_selector.get_grid()
        print("Words: ")
        print(new_grid.keys())
        print()



