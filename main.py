
import random

secret = random.randint(1,30)
guess = None


while True:
    guess = int(input("What is your guess? "))

    if guess == secret:
        print(f"yes, it is {secret}")
        break

    hint = None
    if guess > secret:
        hint = "smaller"
    else:
        hint = "bigger"

    print(f"try something {hint}")





