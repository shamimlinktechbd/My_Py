import random

# Color Codes (ANSI)
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

best_score = float('inf')

def get_difficulty():
    print(f"\n{BOLD}{CYAN}--- Select Difficulty Level ---{RESET}")
    print("1. Easy   (15 attempts)")
    print("2. Medium (10 attempts)")
    print("3. Hard   (5 attempts)")
    
    while True:
        choice = input(f"{BOLD}Enter your choice (1, 2, or 3): {RESET}")
        if choice in ['1', '2', '3']:
            return {'1': 15, '2': 10, '3': 5}[choice]
        print(f"{RED}Invalid choice! Please select 1, 2, or 3.{RESET}")

def start_game():
    global best_score
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = get_difficulty()
    
    print(f"\n{YELLOW}Game Started! You have {max_attempts} attempts. (1-100){RESET}")
    print("I'm thinking of a number between 1 and 100. Now find it 😎!")
    if best_score != float('inf'):
        print(f"{CYAN}Current Best Score: {best_score} attempts.{RESET}")

    while attempts < max_attempts:
        try:
            guess_input = input(f"\nAttempt {attempts + 1}/{max_attempts}: ")
            guess = int(guess_input)
            attempts += 1

            if guess < secret_number:
                print(f"{YELLOW}Too low! ↑{RESET}")
            elif guess > secret_number:
                print(f"{YELLOW}Too high! ↓{RESET}")
            else:
                print(f"\n{GREEN}{BOLD}🎉 Correct! You guessed it in {attempts} attempts.{RESET}")
                
                if attempts < best_score:
                    print(f"{GREEN}New High Score! Previous best was {best_score if best_score != float('inf') else 'none'}.{RESET}")
                    best_score = attempts
                return
        except ValueError:
            print(f"{RED}Invalid input! Please enter a number.{RESET}")

    print(f"\n{RED}{BOLD}Out of attempts! The number was {secret_number}. Better luck next time!{RESET}")

if __name__ == "__main__":
    while True:
        start_game()
        play_again = input(f"\n{BOLD}Play again? (yes/no): {RESET}").lower()
        if play_again != 'yes':
            final_score = best_score if best_score != float('inf') else 'N/A'
            print(f"\n{CYAN}Final Best Score: {final_score}{RESET}")
            print(f"{BOLD}Thanks for playing! Goodbye.{RESET}")
            break