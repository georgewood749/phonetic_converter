import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)

user_input = input("Please enter a word to break down:\n").upper()
nato_letters = [nato_dict[letter] for letter in user_input]
print(nato_letters)
