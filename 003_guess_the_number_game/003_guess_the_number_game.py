import random

def guess_the_number():
    number = random.randint(1, 100)
    guess = 0
    tries = 0

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != number:
        tries += 1
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("That's not a valid number!")
            continue

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")

    print(f"Congratulations! You guessed the number in {tries} tries!")

if __name__ == "__main__":
    guess_the_number()
