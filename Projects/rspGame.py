import random, sys

print("ROCK, PAPER, SCISSORS")

wins = 0
losses = 0
ties = 0

while True:
    print("Enter your move: (r)ock (p)aper  (s)cissors or (q)uit")
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    players_move = input(">")
    while True:
        if players_move == "r" or players_move == "p" or players_move == "s":
            break
        elif players_move == "q":
            sys.exit()

    if players_move == "r":
        print("ROCK v/s...")

    elif players_move == "p":
        print("PAPER V/S...")

    elif players_move == "s":
        print("SCISSORS V/S...")

    number_move = random.randint(1, 3)

    if number_move == 1:
        computer_move = "r"
        print("ROCK")

    elif number_move == 2:
        computer_move = "p"
        print("PAPER")

    elif number_move == 3:
        computer_move = "s"
        print("SCISSORS")

    if players_move == computer_move:
        print("It is a tie!")
        ties += 1

    if players_move == "r" and computer_move == "p":
        print("You lost!")
        losses += 1

    if players_move == "p" and computer_move == "r":
        print("You Win!")
        wins += 1

    if players_move == "s" and computer_move == "p":
        print("You Win!")
        wins += 1

    if players_move == "s" and computer_move == "r":
        print("You Lost!")
        losses += 1

    if players_move == "r" and computer_move == "s":
        print("You Win!")
        wins += 1

    if players_move == "p" and computer_move == "s":
        print("You Lost!")
        losses += 1
