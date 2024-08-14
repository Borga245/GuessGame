import random

def display_heading():
    print("Welcome to the Number Guessing Game!")
    print("-----------------------------------")

def play_game(limit):
    random_number = random.randint(1, limit)
    print(f"\nI'm thinking of a number between 1 and {limit}. Can you guess what it is?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess > random_number:
                print("Too high! Try again.")
            elif guess < random_number:
                print("Too low! Try again.")
            else:
                print("Congratulations! You guessed the correct number!")
                break
        except ValueError:
            print("Please enter a valid number.")

def main():
    display_heading()

    while True:
        try:
            limit = int(input("\nEnter the limit for the random number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        play_game(limit)

        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
