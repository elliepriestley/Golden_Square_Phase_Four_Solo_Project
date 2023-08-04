from lib.restaurant import Restaurant
from lib.meal import Meal

"""
Test that the Restaurant class add method adds instance of a meal class and appends it to the self property 'dishes'
"""

def test_restaurant_add_method_appends_dict_to_public_property():
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