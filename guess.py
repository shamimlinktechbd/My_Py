import random

def start_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("\n--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            # Taking user input
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            # Checking the logic
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")
                break
        except ValueError:
            # Handling non-integer inputs
            print("Invalid input! Please enter a valid number (e.g., 10, 50, 99).")

if __name__ == "__main__":
    start_game()