import random


def guess_number():
    number = random.randint(1, 100)
    attempt = 0

    print("Welcome to guess number game")
    print("Please guess number between 1 and 100")
    while True:
        guess = int(input("Enter your Guess Number:"))
        attempt += 1
        if guess < number:
            print("You Guess Number is very low. please try again")
        elif guess > number:
            print("Your Guess Number is very high. Please Try again")
        else:
            print(f"Congrulation!!! Your guess is right. you have guess in {attempt}")
            break


guess_number()
