from lib.meal import Meal

"""
Test that new instance of class Meal stores values in public properties: name, price and info
"""

def test_initializing_meal_class_sets_public_properties():
    meal1 = Meal("Spaghetti", "10.50")
    assert meal1.name == "Spaghetti"
    assert meal1.price == "10.50"
    assert meal1.info == {"Spaghetti":"10.50"}
