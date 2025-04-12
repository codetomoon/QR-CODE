def ai_guess():
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    print("You can respond with 'higher', 'lower', or 'correct'.")

    low = 1
    high = 100
    guesses = 0

    while True:
        # AI makes a guess by selecting the middle number
        guess = (low + high) // 2
        guesses += 1

        # Ask for the user's response
        response = input(f"Is your number {guess}? (higher/lower/correct): ").lower()

        if response == 'higher':
            # The number is higher than the guess
            low = guess + 1
        elif response == 'lower':
            # The number is lower than the guess
            high = guess - 1
        elif response == 'correct':
            print(f"Yay! I guessed your number {guess} in {guesses} tries.")
            break
        else:
            print("Please respond with 'higher', 'lower', or 'correct'.")

if __name__ == "__main__":
    ai_guess()
print("aritra is great and you should saluter him")
import random

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Please enter a valid number.")

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        # Ask the user for a guess
        guess = get_user_guess()
        attempts += 1
        
        # Check if the guess is correct
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
print("thanks for playing")

# Main function to start the game
def main():
    welcome_message()
    number_guessing_game()

if __name__ == "__main__":    main()
