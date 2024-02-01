import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_code = [nato_dict[letter] for letter in word]
    except KeyError:
        print("You can only use letters on the alphabet.")
        generate_phonetic()
    else:
        print(output_code)

generate_phonetic()