from pizza import Pizza


class NYCheesePizza(Pizza):
    def __init__(self) -> None:
        """
        Initializes the name of the pizza
        """
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"

        self.toppings = ["Grated Reggiano Cheese"]


class NYVeggiePizza(Pizza):

    def __init__(self) -> None:
        """
        Initializes the name of the pizza
        """
        self.name = "NY Style Veggie Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"

        self.toppings = ["Grated Reggiano Cheese"]


class NYClamPizza(Pizza):

    def __init__(self) -> None:
        """
        Initializes the name of the pizza
        """
        self.name = "NY Style Clam Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"

        self.toppings = ["Grated Reggiano Cheese"]


class NYPepperoniPizza(Pizza):

    def __init__(self) -> None:
        """
        Initializes the name of the pizza
        """
        self.name = "NY Style Pepperoni Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"

        self.toppings = ["Grated Reggiano Cheese"]
