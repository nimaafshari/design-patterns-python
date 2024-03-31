from beverages import DarkRoast, Espresso, HouseBlend, Decaf
from condiments import Mocha, Whip, Soy, SteamMilk

if __name__ == "__main__":
    beverage = Espresso()
    print(beverage)

    beverage_2 = DarkRoast()
    beverage_2 = Mocha(beverage_2)
    beverage_2 = Mocha(beverage_2)
    beverage_2 = Whip(beverage_2)
    print(beverage_2)

    beverage_3 = HouseBlend()
    beverage_3 = Soy(beverage_3)
    beverage_3 = Mocha(beverage_3)
    beverage_3 = Whip(beverage_3)
    print(beverage_3)
