from random import sample

lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

my_ticket = [1, 6, 9, 'c']

attempts = 0

while True:
    attempts += 1

    drawn_ticket = sample(lottery_items, 4)
    if set(drawn_ticket) == set(my_ticket):
        print("Winning tickets found!")
        print(f"My ticket: {my_ticket}")
        print(f"Winning tickets: {drawn_ticket}")

        print(f"Attemptts needed: {attempts}")
        break