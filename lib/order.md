class Order:
    
    def __init__(self, meals, restaurant, customer):
        Parameters:
            - unlimited instance(s) of the Meal Class
            - instance of the Customer Class
            - instance of the restaurant class
        Side-effects:
           - Sets the meals, restaurant and customer property of the self object
           - Creates a new instance of the order Class, then used by customer to get receipt
           - creates a public variable called order_details, which is a nested dictionary of relevant info, i.e.:
            {customer: Ellie Priestley, restaurant : Pho, meals :{Noodle Soup : 13.99, Prawn-less Crackers : 4.99}}

