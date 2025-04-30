
import pandas as pd
import numpy as np

file_path = "Eleven_Languages.xlsx"

df = pd.read_excel(file_path)

word_list = df['Var1'].tolist()
word_list = word_list[2:]

new_file = "time_data2.csv"

data_matrix = 100.0 * np.ones((len(word_list), 11))

data2 = pd.DataFrame(data_matrix, index=word_list)

rewriting = False
if rewriting:
    data2.to_csv(new_file)

print(word_list)