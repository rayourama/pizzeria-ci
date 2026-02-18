from pizzeria.pizza import Pizza


def test_create_pizza():
    pizza = Pizza(
        name="Margherita",
        ingredients=["tomate", "fromage"],
        price=8.5,
    )

    assert pizza.name == "Margherita"
    assert pizza.ingredients == ["tomate", "fromage"]
    assert pizza.price == 8.5


def test_add_ingredient():
    pizza = Pizza(
        name="Reine",
        ingredients=["tomate", "fromage"],
        price=9,
    )
    pizza.ingredients.append("champignons")
    assert "champignons" in pizza.ingredients
