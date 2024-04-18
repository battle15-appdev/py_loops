
""" This program goes through different ways to stop a while loop"""

# Use a conditional test in a while statment to stop the loop
prompt = ("\nPlease enter the pizza topping that you will like.")
prompt += ("\n Please type 'quit' when you are finished. ")
message = ""

while (message) != 'quit':
    message = input(prompt)
    print(f"\n{message} will be added to your pizza")


# Use an active variable to control how long the loop run

prompt = ("\nPlease enter the pizza topping that you will like.")
prompt += ("\n Please type 'stop' when you are finished. ")
message = ""
active = True

while active:
    message = input(prompt)

    if message == 'stop':
        active = False
    else:
        print(f"\n{message} will be added to your pizza")


# Use a break statement to exit the loop when the user enters a 'quit' value

prompt = ("\nPlease enter the pizza topping that you will like.")
prompt += ("\n Please type 'exit' when you are finished. ")
message = ""

while True:
    message = input(prompt)
    if (message) == 'exit':
        break
    else:
        print(f"\n{message} will be added to your pizza")