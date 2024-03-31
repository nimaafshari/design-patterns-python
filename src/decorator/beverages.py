from beverage import Beverage


class Espresso(Beverage):
    def __init__(self) -> None:
        """
        Initializes the description of the beverage
        """
        self.description: str = "Espresso Coffee"

    def cost(self) -> float:
        """
        Returns the cost of the beverage
        """
        return 1.99


class HouseBlend(Beverage):
    def __init__(self) -> None:
        """
        Initializes the description of the beverage
        """
        self.description: str = "House Blend Coffee"

    def cost(self) -> float:
        """
        Returns the cost of the beverage
        """
        return 0.89


class DarkRoast(Beverage):
    def __init__(self) -> None:
        """
        Initializes the description of the beverage
        """
        self.description: str = "Dark Roast Coffee"

    def cost(self) -> float:
        """
        Returns the cost of the beverage
        """
        return 0.99


class Decaf(Beverage):
    def __init__(self) -> None:
        """
        Initializes the description of the beverage
        """
        self.description: str = "Decaf Coffee"

    def cost(self) -> float:
        """
        Returns the cost of the beverage
        """
        return 1.05
