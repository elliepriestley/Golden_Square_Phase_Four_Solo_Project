from lib.restaurant import Restaurant
from lib.customer_order import CustomerOrder
from lib.meal import Meal

"""
Test that the Restaurant class add method adds instance of a meal class and appends it to the self property 'dishes'
"""

def test_restaurant_add_meal_method_appends_dict_to_public_property():
    meal1 = Meal("Mattar Paneer", "16.99")
    dishoom = Restaurant()
    dishoom.add_meal(meal1)
    assert dishoom.dishes == {"Mattar Paneer":"16.99"}


"""
Test that the Restaurant class get_menu method returns expected list
"""

def test_restaurant_get_menu_method_returns_expected_list():
    meal1 = Meal("Mattar Paneer", "16.99")
    meal2 = Meal("Chicken Korma", "10.00")
    meal3 = Meal("Boiled Rice", "3.99")
    dishoom = Restaurant()
    dishoom.add_meal(meal1)
    dishoom.add_meal(meal2)
    dishoom.add_meal(meal3)
    assert dishoom.get_menu() == [('Mattar Paneer', '16.99'), ('Chicken Korma', '10.00'), ('Boiled Rice', '3.99')]


"""
Test that when passing through several instances of Meal Class, and an isntance of the restaurant class, the order_takeaway method sets the public properties of restaurant, and items as expected
"""

def test_customer_order_takeaway_method_adds_public_properties():
    order1 = CustomerOrder("Ellie Priestley")
    dishoom = Restaurant()
    meal1 = Meal("Curry", "10.99")
    meal2 = Meal("Boiled Rice","3.99")
    order1.order_takeaway(dishoom, meal1, meal2)
    assert order1.restaurant == dishoom
    assert order1.items == {"Curry" : "10.99", "Boiled Rice": "3.99"}


"""
Test that get_receipt method of Customer Order calss prints a string all items listed, and a grand total price.
"""

def test_Customer_Order_get_receipt_method_returns_all_items_listed_and_grand_total():
    order1 = CustomerOrder("Ellie P")
    dishoom = Restaurant()
    meal1 = Meal("Curry", "10.99")
    meal2 = Meal("Boiled Rice","3.99")
    order1.order_takeaway(dishoom, meal1, meal2)
    assert order1.get_receipt() == "Your order items were: \n{'Curry': '10.99', 'Boiled Rice': '3.99'}. \nYour total is 14.98"