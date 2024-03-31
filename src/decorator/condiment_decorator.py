from abc import ABC, abstractmethod
from beverage import Beverage


class CondimentDecorator(Beverage):

    def __init__(self, beverage: Beverage) -> None:
        """
        Initializes the description of the beverage
        """
        self.beverage: Beverage = beverage
