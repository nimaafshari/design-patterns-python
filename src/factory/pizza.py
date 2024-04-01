from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self, name, dough, sauce) -> None:
        """
        Initializes the description of the pizza
        """
        self.name: str = name
        self.dough: str = dough
        self.sauce: str = sauce
        self.toppings: list = []

    def prepare(self) -> None:
        """
        Prepares the pizza
        """
        print(
            f"""Preparing {self.name}\n
              Tossing dough {self.dough}\n
              Adding sauce {self.sauce}\n
              Adding toppings: {", ".join(self.toppings)}\n"""
        )

    def bake(self) -> None:
        """
        Bakes the pizza
        """
        print(f"Bake for 25 minutes at 350")

    def cut(self) -> None:
        """
        Cuts the pizza
        """
        print(f"Cutting the pizza into diagonal slices")

    def box(self) -> None:
        """
        Boxes the pizza
        """
        print(f"Place the pizza in official PizzaStore box")

    def get_name(self) -> str:
        """
        Returns the name of the pizza
        """
        return self.name
