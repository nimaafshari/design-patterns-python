from pizza_store import PizzaStore
from chicago_pizza_store.pizzas import (
    ChicagoCheesePizza,
    ChicagoClamPizza,
    ChicagoPepperoniPizza,
    ChicagoVeggiePizza,
)


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, type: str) -> None:
        if type == "cheese":
            return ChicagoCheesePizza()
        elif type == "veggie":
            return ChicagoClamPizza()
        elif type == "clam":
            return ChicagoPepperoniPizza()
        elif type == "pepperoni":
            return ChicagoVeggiePizza()
        else:
            return None
