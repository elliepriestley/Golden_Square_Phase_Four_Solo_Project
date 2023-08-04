from lib.customer_order import CustomerOrder
from unittest.mock import Mock

"""
Test that upon initializing, customer name can be found in public property
"""

def test_upon_initializing_creates_public_property_customer_name():
    order1 = CustomerOrder("Ellie Priestley")
    assert order1.customer_name == "Ellie Priestley"

# """
# Test that when passing through several instances of Meal Class, and an isntance of the restaurant class, the order_takeaway method sets the public properties of restaurant, and items as expected
# """

def test_order_takeaway_method_adds_public_properties():
    order1 = CustomerOrder("Ellie Priestley")
    mock_restaurant = Mock()
    mock_meal1 = Mock()
    mock_meal1.name = "Curry"
    mock_meal1.price = "10.99"
    mock_meal2 = Mock()
    mock_meal2.name = "Boiled Rice"
    mock_meal2.price = "3.99"
    order1.order_takeaway(mock_restaurant, mock_meal1, mock_meal2)
    assert order1.restaurant == mock_restaurant
    print(mock_restaurant.items)
    assert order1.items == {"Curry" : "10.99", "Boiled Rice": "3.99"}
    