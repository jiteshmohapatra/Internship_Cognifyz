#Write a Python program that generates arandom number between 1 and 100. Theuser should then try to guess the number.The program should provide hints such as"too high" or "too low" until the correct number is guessed.



import random
def game(check):
    if check == "easy":
        return 10
    elif check == "hard":
        return 5
    else:
        again = input("Invalid syntax. Please enter 'easy' or 'hard': ")
        return game(again)


num1 = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")
difficulty = input("Choose 'easy' or 'hard': Type Number ")
attempts = game(difficulty)
print(f"You have {attempts} attempts remaining to guess the number.")

while True:
    guess = int(input("Guess A number: "))
    attempts -= 1
    if attempts == 0:
        print(f"You've run out of guesses, you lose! The answer was {num1}.")
        break
    if guess > num1:
        print("Too high.")
    elif guess < num1:
        print("Too low.")
    elif guess == num1:
        print(f"You got it!. The answer was {num1}.")
        break
    else:
        print(f"You lose the game!. The answer was {num1}.")
        break
    print("Guess again.")
    print(f"You have {attempts} attempts remaining to guess the number.")