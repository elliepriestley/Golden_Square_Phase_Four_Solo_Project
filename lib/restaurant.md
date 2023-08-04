class Restaurant

    def __init__(self):
        Parameters:
            - None
        Properties:
            - self.dishes: an empty dict representing dish, and corresponding price 
        Side effects:
            - None

    def add_meal(self, meal):
        Parameters:
           - meal: an instance of Meal Class
        Side-effects:
           - Adds the meal to the dishes dictionary property of the self object
      

    def get_menu(self):
        Parameters:
           - None
        Side effects:
            - None
        Returns:
           - A list, with nested dictionary inside, representing the meals from the self.dishes dictionary, with corresponding prices

