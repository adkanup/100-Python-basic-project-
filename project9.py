import random


def hangman():
    word_list = ["python", "hangman", "game", "openai", "programming"]
    word = random.choice(word_list).lower()
    guessed_letters = []
    tries = 6

    while tries > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        print("Guessed word: ", guessed_word)
        print("Tries left: ", tries)

        if guessed_word == word:
            print("Congratulations! You won!")
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
        elif guess in word:
            print("Correct guess!")
            guessed_letters.append(guess)
        else:
            print("Wrong guess!")
            tries -= 1
            guessed_letters.append(guess)

        print("--------------")

    if tries == 0:
        print("Sorry, you lost! The word was:", word)


hangman()
