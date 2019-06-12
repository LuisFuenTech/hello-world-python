from random import randint

while True:
    player = input('rock (r), paper (p) or scissor (s)? ')
    print(player, 'vs', end=' ')

    computer = randint(1,3)

    if computer == 1:
        computer = 'r'
    elif computer == 2:
        computer = 'p'
    else:
        computer = 's'

    print(computer)

    if player == computer:
        print('Draw!')
    if player == 'r' and computer == 's':
        print('Player wins')
    if player == 'r' and computer == 'p':
        print('Computer wins')
    if player == 'p' and computer == 's':
        print('Computer wins')
    if player == 'p' and computer == 'r':
        print('Player wins')
    if player == 's' and computer == 'p':
        print('Player wins')
    if player == 's' and computer == 'r':
        print('Computer wins')
