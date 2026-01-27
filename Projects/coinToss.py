import random

while True:
    guess = input("Guess the coin: ")

    while guess not in ('heads', 'tails'):
        print('Guess only in heads and tails.')
        break

    else:
        toss = random.randint(0, 1)

        if toss == 0:
            print('Result = heads')
            result = 'heads'

        elif toss == 1:
            print('tails')
            result = 'result = tails'

            
        if result == guess:
            print('You won')
            break

        else:
            print('You lost')
                