import random

words = ["python", "hangman", "developer", "challenge", "music", "computer", "kpop"]

word = random.choice(words)

word_letters = set(word)

guessed_letters = set()

tries = 6 

print(" Welcome to Hangman Game ^^ ")
print(" You need to guess the word to fill up the blanks below!! ")
print("_ " * len(word))
print()

while len(word_letters) > 0 and tries > 0:

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)

    print(f"Tries left: {tries}")

    print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")


    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.add(guess)

    if guess in word_letters:
        word_letters.remove(guess)
        print("Good guess!\n")
    else:
        tries -= 1
        print("Wrong guess!\n")


if tries == 0:
    print(f"Game Over! The word was '{word}'")
else:
    print(f"Congratulations! You guessed the word '{word}'")
