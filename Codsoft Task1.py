# # CALCULATOR
def Main():
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    c=int(input("Enter your choice: "))
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    if c==1:
        print(a+b)
    elif c==2:
        print(a-b)
    elif c==3:
        print(a*b)
    elif c==4:
        print(a/b)
    else:
        print("Invalid Choice")
        
Main()

