from Data import Data
import numpy as np
import pandas as pd

# Headers for first 30 Words
data = Data()
word_index = data.word_list

class TimeData:
    time_data = None
    num_rows = 1000
    num_cols = 11
    file_path = "time_data2.csv"
    def __init__(self):
        pass

    def import_data(self):
        try:
            self.time_data = pd.read_csv(self.file_path, index_col=0)
            self.time_data.columns = self.time_data.columns.astype(int)

            if (self.time_data.shape[0] != self.num_rows) or (self.time_data.shape[1] != self.num_cols):
                self.time_data = None
                raise Exception("Data shape does not match")
        except (FileNotFoundError, Exception):
            print("Data file not found or invalid. Creating new data file.")
            self.time_data = pd.DataFrame(np.zeros((self.num_rows, self.num_cols)), index=word_index)

    def save_data(self):
        if self.time_data is not None:
            self.time_data.to_csv(self.file_path)


    def get_data(self):
        return self.time_data

    def update_entry(self, word, lang_index, time):
        if word in word_index:
            if lang_index in self.time_data.columns:
                row_index = word
                old_time = self.time_data.at[row_index, int(lang_index)]
                samples = 8
                old_time = (samples  - 1) * old_time / samples
                new_time = old_time + time / samples
                self.time_data.at[row_index, int(lang_index)] = new_time
            else:
                print(f"Invalid language index: {lang_index}. Skipping update")

    @staticmethod
    def rolling_average(elapsed_time):
        samples = 8
        av_time = 0

        return av_time

if __name__ == "__main__":
    #time_data = np.loadtxt("time_data.csv", delimiter=",")
    total_rows = 1000
    total_cols = 11
    time_data = 5 * np.ones((total_rows, total_cols))
    df = pd.DataFrame(time_data, index=word_index)

    rewriting = False
    if rewriting:
        df.to_csv("time_data.csv")
    #
    print()
    time_data = TimeData()
    time_data.import_data()
    print(time_data.get_data())
    time_data.update_entry("what", 5, 10)
    time_data.save_data()
