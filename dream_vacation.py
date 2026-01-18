responces = {}

active_user = True
while active_user:
    user = input("Plese enter you name: ")
    location = input("If you could visit one place in the world where would you go? Please enter: ")

    responces[user] = location

    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat.lower() == 'no':
        active_user = False


print("\n--Poll Result--")
for  user, location in responces.items():
    print(f"{user} would like to visit {location}")
