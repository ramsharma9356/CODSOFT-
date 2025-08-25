#PASSWORD GENERATOR
#A password generator is a useful tool that generates strong and random passwords for users.Allowing users to specify the length and complexity of the password.

import random
import string

characters=string.ascii_letters+string.digits+string.punctuation
password=""

num=int(input("Enter your desired length of password :- "))

if (num<=4):
    print("Less complex")
    print("Use more than 4 characters for more complexity")

for i in range(num):
    password+=random.choice(characters)

print(f"Your password={password}")