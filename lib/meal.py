
class Meal:

    def __init__(self, name, price):
        # Parameters:
        #    - name: string
        #    - price: float
        # Side-effects:
        #    - Sets the name and price properties and adds them to a dictionary property with the variable name 'info', i.e. {name: Curry, price : 16.99}
        self.name = name
        self.price = price
        self.info = {name:price}
        