#import files and modules
import hangman_words
import random
import hangman_art

#declare variables
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#import the logo from hangman_art.py
print(hangman_art.logo)

#display blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #check whether the letter is in the word, if duplicate, let user know 
    if guess in display:
        print(f"You've already guessed {guess}. Try again")

    #check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #check whether user is wrong
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. Try again.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #join elements and turn it into strings
    print(f"{' '.join(display)}")

    #check if the user got all the answer
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])