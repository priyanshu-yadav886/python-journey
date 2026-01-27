from random import sample
lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = sample(lottery_items, 4)

print("Any ticket matching these following 4 numbers or letters wins a prize:")
for winner in winning_ticket:
    print(f"- {winner}")