import random

rules = [['Draw','Player Wins','Computer Wins'],
         ['Computer Wins','Draw','Player Wins'],
         ['Player Wins','Computer Wins','Draw']]

print("Game Started !!!")
print("Rocks, Paper and Scissors !!!")
while(True):
    print("enter Rocks , Paper Or Scissors  !!!")
    player=input("Enter Your Choice ! : ").lower()
    Comp= random.randint(0,2)
    p=0 if player=='rocks' else 1 if player=='paper' else 2
    print(f" {rules[p][Comp]}")
        