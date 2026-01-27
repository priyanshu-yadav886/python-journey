prompt = "\nEnter your toppings."
prompt += "\n(Enter 'quit' to stop the program.)"

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(f"I'll add your {message} topping in your pizza")