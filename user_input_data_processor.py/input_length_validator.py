'''
User Input Data Processor 2 Task 1

The aim of this asignment is rto process and format user input data.

Input length Validator

Write a script that checks the length of the user's first name and last name.
Both should be at least 2 characters long. If not, print an error message.


'''
first_name = input("Enter your first name: ")
last_name= input("Enter your last name: ") 

def length_validate():
  if len(first_name ) > 2 and len(last_name):
    print("First name is valid!")
  else:
    print("Try again. The first, and last name must be 2 characters long.")
       
length_validate()  