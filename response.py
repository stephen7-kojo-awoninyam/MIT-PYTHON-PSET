from validators import email
from sys import exception

email = input("What's your email address? ")

if val := email(email):
    print("Valid")
else:
    print("Invalid")    



 
