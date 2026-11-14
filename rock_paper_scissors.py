import random

def get_choices():
    player_choice = input("Enter your choice (Rock, Paper, Scissors): ")
    comp_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    choice={'player_choice': player_choice, 'comp_choice': comp_choice}
    return choice

def check_winner(player_choice, comp_choice):
    print('you chose:', player_choice, 'computer chose:', comp_choice)
    if player_choice == comp_choice:
        return "It's a tie!"
    elif player_choice=='Rock':
        if comp_choice=='Scissors':
            return 'you win!'
        else:
            return 'you lose!'
    elif player_choice=='Paper':
        if comp_choice=='Rock':
            return 'you win!'
        else:
            return 'you lose!'
    elif player_choice=='Scissors':
        if comp_choice=='Paper':
            return 'you win!'
        else:
            return 'you lose!'
    
    

choices = get_choices()
winner=check_winner(choices['player_choice'], choices['comp_choice'])
print(winner)
