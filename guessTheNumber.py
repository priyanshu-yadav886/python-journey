import random

secret_number = random.randint(1, 20)

print("I am thinking of a number between 1 and 20.")

for guesse_taken in range(1, 7):
    print("Take a guess.")
    guess = int(input(">"))
    if guess < secret_number:
        print("You are too low!")

    elif guess > secret_number:
        print("You are too high!")

    else:
        break


if guess == secret_number:
    print(f"Good job! you got it {guesse_taken} in guesses!")

else:
    print("Nope. The number was" + str(secret_number))
