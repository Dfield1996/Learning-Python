import random

def play():
    user = input("Pick your choice ('r' rock, 'p' paper, 's' scissors): ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'Draw!\n Computer chose: ' + str(computer)


    if win(user, computer):
        return 'You win!\n Computer chose: ' + str(computer)

    return 'You lost!\n Computer chose: ' + str(computer)

def win(player, pc):
    if (player == 'r' and pc == 's') or (player == 'p' and pc == 'r') or (player == 's' and pc == 'p'):
        return True

print (play())