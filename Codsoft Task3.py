# #PASSWORD GENERATOR
import random
import string

def pw(a):
    char=string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choice(char) for i in range(a))
    print("Generated Password: ",password)
    
    
a=int(input("Enter the length of Password: "))
pw(a)