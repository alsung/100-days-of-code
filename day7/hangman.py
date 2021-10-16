import random
import hangman_art
import hangman_words

# word_list = ["aardvark", "baboon", "camel"]
stages = hangman_art.stages
logo = hangman_art.logo
word_list = hangman_words.word_list
end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = len(stages) - 1

print(logo)

# display = ['_'] * len(chosen_word)
display = []
for letter in chosen_word:
    display += "_"

guessed_set = set()
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    
    # Check guessed letter
    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = guess
    print(f"{' '.join(display)}")  

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(chosen_word)

    if "_" not in display: 
        end_of_game = True
        print("You win!")
        print(chosen_word)

    print(stages[lives])