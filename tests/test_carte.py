import pytest
from unittest.mock import MagicMock
from pizzeria.carte import CartePizzeria
from pizzeria.exceptions import CartePizzeriaException


def test_is_empty_initially():
    carte = CartePizzeria()
    assert carte.is_empty() is True


def test_add_pizza():
    carte = CartePizzeria()
    pizza_mock = MagicMock()
    pizza_mock.name = "Margherita"

    carte.add_pizza(pizza_mock)

    assert carte.nb_pizzas() == 1
    assert carte.is_empty() is False


def test_remove_existing_pizza():
    carte = CartePizzeria()
    pizza_mock = MagicMock()
    pizza_mock.name = "Reine"

    carte.add_pizza(pizza_mock)
    carte.remove_pizza("Reine")

    assert carte.nb_pizzas() == 0


def test_remove_unknown_pizza_raises_exception():
    carte = CartePizzeria()

    with pytest.raises(CartePizzeriaException):
        carte.remove_pizza("Inconnue")
