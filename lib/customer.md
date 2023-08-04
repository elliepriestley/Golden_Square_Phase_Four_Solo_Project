class Customer:

    def __init__(self, name):
        Parameters:
           - name: string
        Properties:
            - orders: a list of order_details properties from the order instances representing orders they have placed, i.e.: [{Dishoom : {Boiled Rice : 3.50, Mattar Paneer : 15.99}} , {Pizza Hut : {Margarita : 10.99, Diet Coke : 3.99}}]
        Side-effects:
           - Sets the name property

    def get_receipt(self, order)
        Parameters:
            - order: an instance of the Order class.
        Returns: 
            - a string with an itemised list of the respective order, and a Grand Total Price.
