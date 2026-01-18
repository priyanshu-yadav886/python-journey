active = True

while True:
    age = input("\nEnter your age: ")
    age = int(age)

    if age < 3:
        print("Your ticket is free.")

    elif age <= 12:
        print("You have to pay 10$ for a ticket.")

    else:
        print("You have to pay 15$ for a ticket.")
