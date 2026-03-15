import random

# গ্লোবাল ভেরিয়েবল দিয়ে বেস্ট স্কোর ট্র্যাক করা হচ্ছে
best_score = float('inf') 

def get_difficulty():
    print("\n--- Select Difficulty Level ---")
    print("1. Easy   (15 attempts)")
    print("2. Medium (10 attempts)")
    print("3. Hard   (5 attempts)")
    
    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice in ['1', '2', '3']:
            return {'1': 15, '2': 10, '3': 5}[choice]
        print("Invalid choice! Please select 1, 2, or 3.")

def start_game():
    global best_score
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = get_difficulty()
    
    print(f"\nGame Started! You have {max_attempts} attempts. (1-100)")
    print("I'm thinking of a number between 1 and 100. Now find it!")
    if best_score != float('inf'):
        print(f"Current Best Score: {best_score} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! ↑")
            elif guess > secret_number:
                print("Too high! ↓")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                
                # হাই স্কোর আপডেট করা হচ্ছে
                if attempts < best_score:
                    print(f"New High Score! Previous best was {best_score if best_score != float('inf') else 'none'}.")
                    best_score = attempts
                return
        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"\nOut of attempts! The number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    while True:
        start_game()
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"\nFinal Best Score: {best_score if best_score != float('inf') else 'N/A'}")
            print("Thanks for playing! Goodbye.")
            break