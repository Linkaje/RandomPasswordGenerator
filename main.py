# Imports the random library
import random

# Asks the user for the length of the password and transforms it to int type
passlen = int(input("Enter the length of the password: "))

# Stores the available characters for the random password
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%*()?"

# Creates the password joining random characters from the ones we stored before and the length of the password
p = "".join(random.sample(s, passlen))

# Prints the final password
print(p)