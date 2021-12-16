import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Enter a word: ").upper()
nato_wordlist = [nato_dict[letter] for letter in input_word]

print(nato_wordlist)
