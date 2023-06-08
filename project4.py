import random
def play_game():
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        player_choice = input("Enter your choice (1-4): ")

        if player_choice == '4':
            print("Thanks for playing!")
            break

        if player_choice not in ['1', '2', '3']:
            print("Invalid choice. Please try again.")
            continue

        player_choice = int(player_choice)
        moves = ['Rock', 'Paper', 'Scissors']
        player_move = moves[player_choice - 1]
        computer_move = random.choice(moves)

        print("\nYour move:", player_move)
        print("Computer's move:", computer_move)

        if player_move == computer_move:
            print("It's a tie!")
        elif (player_move == 'Rock' and computer_move == 'Scissors') or \
             (player_move == 'Paper' and computer_move == 'Rock') or \
             (player_move == 'Scissors' and computer_move == 'Paper'):
            print("You win!")
        else:
            print("Computer wins!")

play_game()