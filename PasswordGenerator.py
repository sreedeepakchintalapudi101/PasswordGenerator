import random
import string

#defining length of the Password

length = int(input("Enter the Length of the Password: "))

#Initializing the all Lower_Case, Upper_Case, Digits, Punctuation to form Characters

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

#adding all the characters to form a Password

all_chars = lower_case + upper_case + digits + punctuation

#Initializing the Password

password = "".join(random.sample(all_chars,length))

#Returning the Passwords

print(password)
