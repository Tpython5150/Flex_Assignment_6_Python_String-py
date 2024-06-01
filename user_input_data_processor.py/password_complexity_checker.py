'''
Password Complexity Checker 2 Task 2:

Create a function that checks the complexity of a user's password. The password must be at
least 8 characters long, contain one uppercase letter, one lowercase letter and one number.
If the password does not meet these criteria, print a message explaining the complexity
requirements.

'''


def password_check(password):
  if len(password) < 8:
    print("The password must be characters long.")
    return 
    
  has_upper = False
  has_lower = False
  has_digit = False
  
  for char in password:
    if char.isupper():
      has_upper = True
    elif char.islower():
      has_lower = True
    elif char.isdigit():
      has_digit = True
      
  if not has_upper:
    print("The password must have 1 uppercase letter.")
  if not has_lower:
    print("The password must have 1 lowercase letter. ")
  if not has_digit:
    print("The passwword must have 1 digit.")
    
  return True
    
def main():
  while True:
    password = input("Enter you password. Must have 1 uppercase letter, 1 lowercase letter and a digit: ")
    if password.lower() == 'quit':
      break
    if password_check(password):
      print("Your password is valid.")
      break
    else:
      print("Please try again.")
    
main()   
   