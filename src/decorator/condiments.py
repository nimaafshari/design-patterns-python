from condiment_decorator import CondimentDecorator


class Mocha(CondimentDecorator):
    def __init__(self, beverage: CondimentDecorator) -> None:
        """
        Initializes the description of the beverage
        """
        super().__init__(beverage)
        self.description: str = f"{self.beverage.get_description()}, Mocha"

    def cost(self) -> float:
        """
        Returns the cost of the beverage
        """
        return self.beverage.cost() + 0.20


class Whip(CondimentDecorator):
    def __init__(self, beverage: CondimentDecorator) -> None:
        """
        Initializes the description of the beverage
        """
        super().__init__(beverage)
        self.description: str = f"{self.beverage.get_description()}, Whip"

    def cost(self) -> float:
        """
        Returns the cost of the beverage
        """
        return self.beverage.cost() + 0.10


class Soy(CondimentDecorator):
    def __init__(self, beverage: CondimentDecorator) -> None:
        """
        Initializes the description of the beverage
        """
        super().__init__(beverage)
        self.description: str = f"{self.beverage.get_description()}, Soy"

    def cost(self) -> float:
        """
        Returns the cost of the beverage
        """
        return self.beverage.cost() + 0.15


class SteamMilk(CondimentDecorator):
    def __init__(self, beverage: CondimentDecorator) -> None:
        """
        Initializes the description of the beverage
        """
        super().__init__(beverage)
        self.description: str = f"{self.beverage.get_description()}, Stream Milk"

    def cost(self) -> float:
        """
        Returns the cost of the beverage
        """
        return self.beverage.cost() + 0.10
