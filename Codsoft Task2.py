# #ROCK PAPER SCISSORS GAME
import random
def Main():
    print("==========================\nROCK , PAPER AND SCISSORS")
    a=input("Press Y/y to Start: ").lower() 
    print("==========================")
    if a== 'y':
        menu()
        
def menu():
    case=["rock","paper","scissors"]
    comp=random.choice(case)
    print("Rock \t Paper \t Scissors")
    c=input("Enter your choice: ").lower()
    print("==========================")
    while c not in case:
        c=input("Invalid choice. Enter your choice: ")
    print("Computer chose",comp,"\t You chose",c)
    if c==comp:
        print("Its a tie")
    if c=='rock':
        if comp=='paper':
            print("Computer wins")
        else:
            print("You win")
    if c=='paper':
        if comp=='scissors':
            print("Computer wins")
        else:
            print("You win")
    if c=='scissors':
        if comp=='rock':
            print("computer wins")
        else:
            print("You win")
            
Main()