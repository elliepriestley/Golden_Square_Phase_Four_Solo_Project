from lib.restaurant import Restaurant
from unittest.mock import Mock

"""
Test that when initialised, self. dishes is an empty dict
"""

def test_when_initialised_dishes_property_is_empty_dict():
    pizzahut = Restaurant()
    assert pizzahut.dishes == {}

"""
Test using Mock test that add_meal method updates dishes public property
"""
def test_add_meal_method_updates_public_dishes_property():
    dishoom = Restaurant()
    mock_meal = Mock()
    mock_meal.name = "Mock name"
    mock_meal.price = "3.99"
    dishoom.add_meal(mock_meal)
    assert dishoom.dishes == {"Mock name": "3.99"}

"""
Tets using Mock test that get_menu method lists all dishes 
"""

def test_get_menu_method_lists_all_dishes():
    dishoom = Restaurant()
    mock_meal1 = Mock()
    mock_meal1.name = "Mock name"
    mock_meal1.price = "3.99"
    mock_meal2 = Mock()
    mock_meal2.name = "Mock name2"
    mock_meal2.price = "4.99"
    mock_meal3 = Mock()
    mock_meal3.name = "Mock name3"
    mock_meal3.price = "5.99"
    dishoom.add_meal(mock_meal1)
    dishoom.add_meal(mock_meal2)
    dishoom.add_meal(mock_meal3)
    assert dishoom.get_menu() == [('Mock name', '3.99'), ('Mock name2', '4.99'), ('Mock name3', '5.99')]