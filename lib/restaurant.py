from lib.meal import Meal

class Restaurant:

    def __init__(self):
        self.dishes = {}

    def add_meal(self, meal):
        self.dishes[meal.name] = meal.price

    def get_menu(self):
        return list(self.dishes.items())

