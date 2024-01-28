import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}
word = input("Enter a word: ").upper()

output_code = [nato_dict[letter] for letter in word]
print(output_code)