"""
This progam uses a function that accepts a size and displays
the message that will printed on the shirt 

"""

# Large Shirts:
# large shirts with a
# default message = " I love python"
# large and medium sizes shirts with default message
# shirt of any size with different message

def make_shirt(size, message = 'I love Python'):
        print(f"T-Shirt size: {size.title()} ")
        print(f"Message: {message}")
make_shirt('large')
make_shirt('medium')

# Changing the message value
make_shirt('small', message = 'push through!')