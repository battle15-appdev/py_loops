""" This Program displays the flavors of ice cream that a parlor serves"""
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        print(f"\nThe restarant, {self. restaurant_name}, serves {self.cuisine_type} flavors: ")

    def open_restaurant(self):
        """Display a message that the restaurant is open"""
        print(f"\n{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, customers_served):
        """Allow user to increment the number of customer served."""
        self.number_served += customers_served


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def read_flavors(self):
        for flavor in self.flavors:
            print(f"-{flavor.title()}")


icy_ice_cream = IceCreamStand('Icy Ice cream')
icy_ice_cream.flavors = ['vanilla', 'chocolate', 'strawberry']

icy_ice_cream.describe_restaurant()
icy_ice_cream.read_flavors()