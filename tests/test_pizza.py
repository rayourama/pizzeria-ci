import pytest
from pizzeria.pizza import Pizza

def test_create_pizza():
    pizza = Pizza(name="Margherita", ingredients=["tomate", "fromage"], prix=8.5)

    assert pizza.name == "Margherita"
    assert pizza.ingredients == ["tomate", "fromage"]
    assert pizza.prix == 8.5

def test_add_ingredient():
    pizza = Pizza(name="Reine", ingredients=["tomate", "fromage"], prix=9)
    pizza.ingredients.append("champignons")
    assert "champignons" in pizza.ingredients
