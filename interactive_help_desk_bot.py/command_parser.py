'''  
Command Parser, Issue Categorizer 3 Task 1 and 2

The aim of this assignment is to create an interactive help desk bot that processes
user queries and responds appropriately for a SaaS application.

Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.
If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. Print out the category of the issue for the support team.

As you enter each command it will walk you through the program.
'''

 
commands = {
  "help" : "How can I help you?",
  "issue" : "Please describe the issue you're experiencing? ",
  "resolved" : "Thank you for letting us resolve the issue. If you need further type 'contact support' and recieve and email for further assistance.",
  "contact support" : "You can reach support at support@support.com"
}

issue_keywords = {
  "login": "Login issue",
  "performance": "Performance Issue",
  "error": "Error Issue"
}
def command_parser():
  while True:
    user_input = input("Enter if you need: (help/issue/resolved/contact support) or type 'quit' to exit: ").lower()
    
    if user_input in commands:
      print(commands[user_input]) 
      if user_input == "issue":
        issue_description = input("Describe the issue: (login/performance/error): ").lower()
        
        categorized = False
        for keyword in issue_keywords:
          if keyword in issue_description:
            print(f"Issue categorized as: {issue_keywords[keyword]}")  
            categorized = True
            break
        if not categorized:
          print("Issue categorized as: General Issue")
    if user_input == 'quit':
      print("Thank you for using our help bot. Have a nice day, Goodbye!")
      break    
    else: 
      print("I am not sure how to help you. please type 'help' for assistance.")  
      
command_parser()        