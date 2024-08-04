import random
def computer_choice():
    return random.choice(['rock','paper','scissor'])
    
    
def user_choice():
    choice=input("enter rock,paper or scissor :").lower()
    while choice not in ['rock','paper','scissor']:
        choice= input('invalid input, enter rock or scissor or paper').lower()
    return  choice
    
    

    
    
def winner(user_action,computer_action):
    if user_action==computer_action:
        return 'tie'
    elif (user_action == 'rock' and computer_action == 'scissors') or \
    (user_action == 'paper' and computer_action == 'rock') or \
    (user_action == 'scissors' and computer_action == 'paper'):
        
        return "You win!"
    else:
        return 'computer wins'

def play_game ():
    user_action=user_choice()
    computer_action=computer_choice()
    print(f"\nYou choose {user_action}, computer choose {computer_action}\n")
    print(winner(user_action,computer_action))
    
    
play_game()