import pandas

# Read CSV and create phonetic dict
df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# Function to generate phonetic code
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        code_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()  # Ask again
    else:
        print(code_list)

generate_phonetic()
