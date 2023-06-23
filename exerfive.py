# Scissor Paper Rock Game

import random

def check(comp,user):
    if comp == user:
        return 0
    
    if(comp == 0 and user == 1):
        return -1
    if(comp == 1 and user == 2):
        return -1
    if(comp == 2 and user == 0):
        return -1
    
    return 1
    
   

comp = random.randint(0, 2)
while(True):
    
    user = int(input("0 for scissor , 1 for paper , 2 for rock and 3 for exit:\n"))

    if user == 3:
        print("Exiting the game . Goodbye!")
        break

    if user not in [0, 1, 2]:
        print("Invalid input. Please enter 0, 1, 2, or 3.")
        continue

    user = int(user)
 
    score = check(comp,user)

    print("You: ",user)
    print("Computer: ",comp)

    if (score == 0):
        print("Its a Draw")
    elif (score == -1):
        print("You Lose")
    else :
        print("You won")

    comp = random.randint(0, 2)
    
    