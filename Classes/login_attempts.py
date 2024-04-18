""" 
This Program greets a user, then displays 
the number of times that they have logged in
"""

class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def define_user(self):
        """Summerizes the User's Information"""
        print(f"\nName: {self.first_name} {self.last_name}")
        print(f"\nAge: {self.age} years old")
        print(f"\nLocation: {self.location}")

    def greet_user(self):
        """Prints a Personalized Greeting to the User"""
        print(f"Hello {self.first_name}!")

    def increment_login_attempts(self):
        """ Increases Login Attempt number"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_0 = User('lily', 'white', 32, 'london')
User.define_user(user_0)
User.greet_user(user_0)


# Login attempt number increases for each function call
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()

print(f"\n{user_0.first_name} has attempted to login in {user_0.login_attempts} times")

user_0.reset_login_attempts()

# Resets the number of login attempt
# print(f"\n{user_0.first_name} has attempted to login in {user_0.login_attempts} times")