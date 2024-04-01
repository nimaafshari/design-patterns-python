from chicago_pizza_store.pizza_factory import ChicagoPizzaStore
from ny_pizza_store.pizza_factory import NYPizzaStore


if __name__ == "__main__":
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.get_name()} \n\n")
    pizza = chicago_store.order_pizza("cheese")
    print(f"Joel ordered a {pizza.get_name()} \n\n")
