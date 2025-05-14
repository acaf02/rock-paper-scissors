import random

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

def play(user_choice):
    user = user_choice.lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)
    elif is_win(user, computer):
        return (1, user, computer)
    else:
        return (-1, user, computer)
