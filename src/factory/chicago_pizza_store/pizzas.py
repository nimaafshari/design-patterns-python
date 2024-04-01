from pizza import Pizza


class ChicagoCheesePizza(Pizza):
    def __init__(self) -> None:
        """
        Initializes the name of the pizza
        """
        self.name = "Chicago Style Sauce and Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

        self.toppings = ["Shredded Mozzarella Cheese", "Black Olives", "Spinach"]

    def cut(self) -> None:
        """
        Cuts the pizza
        """
        print(f"Cutting the pizza into square slices")


class ChicagoVeggiePizza(Pizza):

    def __init__(self) -> None:
        """
        Initializes the name of the pizza
        """
        self.name = "Chicago Style Veggie Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

        self.toppings = ["Shredded Mozzarella Cheese"]


class ChicagoClamPizza(Pizza):

    def __init__(self) -> None:
        """
        Initializes the name of the pizza
        """
        self.name = "Chicago Style Clam Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

        self.toppings = ["Shredded Mozzarella Cheese"]


class ChicagoPepperoniPizza(Pizza):

    def __init__(self) -> None:
        """
        Initializes the name of the pizza
        """
        self.name = "Chicago Style Pepperoni Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

        self.toppings = ["Shredded Mozzarella Cheese"]
