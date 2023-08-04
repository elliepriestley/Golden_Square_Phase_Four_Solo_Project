from lib.restaurant import Restaurant

"""
Test that when initialised, self. dishes is an empty dict
"""

def test_when_initialised_dishes_property_is_empty_dict():
    pizzahut = Restaurant()
    assert pizzahut.dishes == {}