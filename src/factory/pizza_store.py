from abc import ABC, abstractmethod


class PizzaStore(ABC):
    def order_pizza(self, type: str) -> None:
        """
        Orders a specific type of pizza
        """
        pizza = self.create_pizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, type: str) -> None:
        """
        Abstract method to create a specific type of pizza
        """
        pass
