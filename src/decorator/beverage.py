from abc import ABC, abstractmethod


class Beverage(ABC):

    def __init__(self) -> None:
        """
        Initializes the description of the beverage
        """
        self.description = "Unknown Beverage"

    def __repr__(self) -> str:
        return f"{self.get_description()} ${self.cost()}"

    def get_description(self):
        """
        Returns the default description of the beverage
        """
        return self.description

    @abstractmethod
    def cost(self):
        """
        Returns the cost of the beverage
        """
        pass
