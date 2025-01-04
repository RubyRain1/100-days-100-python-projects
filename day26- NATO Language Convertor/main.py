student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_data_frame)

nato_dict = {
    row["letter"]: row["code"]
    for _, row in nato_data_frame.iterrows()
}

print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("enter a word to convert: ")
nato_conversions = [nato_dict[letter.upper()] for letter in word if letter.upper() in nato_dict]
print(" ".join(nato_conversions))







