import random

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    print("Choose one: rock, paper, scissors")
    user_choice = input().lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print("You lose!")
        else:
            print("You win!")
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print("You lose!")
        else:
            print("You win!")
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print("You lose!")
        else:
            print("You win!")
    else:
        print("Invalid choice. Please try again.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

play_game()
