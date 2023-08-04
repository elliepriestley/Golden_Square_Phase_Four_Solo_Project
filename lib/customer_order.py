from lib.meal import Meal

class CustomerOrder:

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.restaurant = None
        self.items = {}

    def order_takeaway(self, restaurant, *meals):
        self.restaurant = restaurant
        for meal in meals:
            self.items[meal.name] = meal.price

    def get_receipt(self):
        prices = []
        for key, value in self.items.items():
            prices.append(float(value))
        total = sum(prices)
        return f"Your order items were: \n{self.items}. \nYour total is {total}"
