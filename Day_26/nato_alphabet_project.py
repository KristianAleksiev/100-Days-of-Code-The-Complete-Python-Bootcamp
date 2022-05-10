import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Enter a name: ").upper()
result_list = [phonetic_dictionary[letter] for letter in name]
print(result_list)
