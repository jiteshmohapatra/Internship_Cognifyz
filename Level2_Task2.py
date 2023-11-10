#Create a number guessing game where theprogram generates a random numberbetween a specified range, and the user triesto guess it. Provide feedback to the user if their guess is too high or too low.




import random

# Set the range for the random number
num1 = 1
num2 = 100
random_number = random.randint(num1, num2)

# Initialize the number of attempts
attempts = 0

print(f"Welcome to the Number Guessing Game! Guess a number between {num1} and {num2}.")

# Main game loop
while True:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < num1 or user_guess > num2:
            print("Your guess is out of the specified range.")
        elif user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Game over. Thank you for playing!")
