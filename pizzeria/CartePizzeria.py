from .pizza import Pizza
from .CartePizzeriaException import CartePizzeriaException


class CartePizzeria:
    def __init__(self):
        self._pizzas = []

    def is_empty(self) -> bool:
        return len(self._pizzas) == 0

    def nb_pizzas(self) -> int:
        return len(self._pizzas)

    def add_pizza(self, pizza: Pizza):
        self._pizzas.append(pizza)

    def remove_pizza(self, name: str):
        for pizza in self._pizzas:
            if pizza.name == name:
                self._pizzas.remove(pizza)
                return
        raise CartePizzeriaException(f"Pizza {name} not found")
