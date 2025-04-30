# Sample dictionary
my_dict = {
    "apple": [1, 2],
    "banana": [1, 2, 3],
    "cherry": [1]
}

# Sort dictionary by the size of its values
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: len(item[1])))

print(sorted_dict)