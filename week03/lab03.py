import random


def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""

    return("The " + adjective + " " + noun + " is " + verb)


def guessing_game():
    """Run an interactive number-guessing game."""
    secret = random.randint(1, 100)
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == secret:
            print("Correct!")
            break
        elif guess < secret:
            print("Too low")
        else:
            print("Too high")