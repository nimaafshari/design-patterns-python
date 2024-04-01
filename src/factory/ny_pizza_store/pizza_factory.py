from pizza_store import PizzaStore
from ny_pizza_store.pizzas import (
    NYCheesePizza,
    NYClamPizza,
    NYPepperoniPizza,
    NYVeggiePizza,
)


class NYPizzaStore(PizzaStore):
    def create_pizza(self, type: str) -> None:
        if type == "cheese":
            return NYCheesePizza()
        elif type == "veggie":
            return NYClamPizza()
        elif type == "clam":
            return NYPepperoniPizza()
        elif type == "pepperoni":
            return NYVeggiePizza()
        else:
            return None
