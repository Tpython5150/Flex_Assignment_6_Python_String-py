'''
Email Formatter 2 Task 3:

Implement a script that ensures all user email addresses are in a standard format.

'''

import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
email = input("Please enter your email to validate: ")

# alphanumeric characters, dots, underscores, perecentages, and plus signs
# The @ symbol.
# A domain name consisisting of alphanumeric characters and dots.
# A top-level domain with a length of 2 to 7 alphabetic characters.

  
def check(email):
  if re.fullmatch(regex, email):
    print("Valid Email")
  else:
    print("Invalid Email.") 
    
check(email)