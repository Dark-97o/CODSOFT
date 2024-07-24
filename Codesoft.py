# # CALCULATOR
# def Main():
#     print("Calculator")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     c=int(input("Enter your choice: "))
#     a=float(input("Enter first number: "))
#     b=float(input("Enter second number: "))
#     if c==1:
#         print(a+b)
#     elif c==2:
#         print(a-b)
#     elif c==3:
#         print(a*b)
#     elif c==4:
#         print(a/b)
#     else:
#         print("Invalid Choice")
        
# Main()
   
   

# #ROCK PAPER SCISSORS GAME
# import random
# def Main():
#     print("==========================\nROCK , PAPER AND SCISSORS")
#     a=input("Press Y/y to Start: ").lower() 
#     print("==========================")
#     if a== 'y':
#         menu()
        
# def menu():
#     case=["rock","paper","scissors"]
#     comp=random.choice(case)
#     print("Rock \t Paper \t Scissors")
#     c=input("Enter your choice: ").lower()
#     print("==========================")
#     while c not in case:
#         c=input("Invalid choice. Enter your choice: ")
#     print("Computer chose",comp,"\t You chose",c)
#     if c==comp:
#         print("Its a tie")
#     if c=='rock':
#         if comp=='paper':
#             print("Computer wins")
#         else:
#             print("You win")
#     if c=='paper':
#         if comp=='scissors':
#             print("Computer wins")
#         else:
#             print("You win")
#     if c=='scissors':
#         if comp=='rock':
#             print("computer wins")
#         else:
#             print("You win")
            
# Main()




# #PASSWORD GENERATOR
# import random
# import string

# def pw(a):
#     char=string.ascii_letters + string.digits + string.punctuation
#     password=''.join(random.choice(char) for i in range(a))
#     print("Generated Password: ",password)
    
    
# a=int(input("Enter the length of Password: "))
# pw(a)
