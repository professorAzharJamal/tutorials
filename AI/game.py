import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 6
    hint_threshold = 3

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number ({secret_number}) correctly!")
            break

        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"You have {remaining_attempts} attempts remaining.")

        # Provide a hint if the player exceeds the hint threshold
        if attempts == hint_threshold:
            hint = "even" if secret_number % 2 == 0 else "odd"
            print(f"Hint: The secret number is {hint}.")

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()
