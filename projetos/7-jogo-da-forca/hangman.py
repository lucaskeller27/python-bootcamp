# Day 7 Project - Hangman

import random, os, hangman_art
from hangman_words import word_list

os.system('cls' if os.name == 'nt' else 'clear')

lives_left = 6
print(hangman_art.logo)

# Selecting a word

chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for i in range(word_length):
    placeholder += "_"

print(placeholder, "\n")

game_over = False
guessed_letters = []
made_guesses = []


while not game_over:
    # Asking the user for a letter
    guess = input("Guess a letter:\n-> ").lower()
    
    # Checking if the guess is correct or not
    answer = ""
    for letter in chosen_word:
        if guess == letter:
            answer += letter
            guessed_letters.append(letter)
        elif letter in guessed_letters:
            answer += letter
        else:
            answer += "_"
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(hangman_art.logo, "\n")
    
    # Telling the user if their guess is correct or not
    
    if guess in made_guesses:
        print(f"You've already guessed the letter \"{guess}\". Try another one!")
    elif guess not in chosen_word:
        lives_left -= 1
        print(f"Your guess ({guess}) was incorrect. You lose a life! ({lives_left}/6 lives left)")
    elif guess in chosen_word:
        print(f"Your guess ({guess}) was correct!")

    made_guesses.append(guess)
    
    print("\n", answer, "\n")
    print(hangman_art.stages[lives_left])
    
    # Checking if the game should end
    
    if lives_left == 0:
        game_over = True
        print(f"You lose. The answer was \"{chosen_word}\". To the gallows!")
    
    if "_" not in answer:
        game_over = True
        print("Congratulations, you win!")
