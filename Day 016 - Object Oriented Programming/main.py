from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
drinkmenu = Menu()
drinkitem = MenuItem
money = MoneyMachine()

choice = input(f"What would you like to order? {drinkmenu.get_items()} ")
choice = "latte"

if(choice == "report"):
    print(machine.report())
    print(money.report())
else:
    drink = drinkmenu.find_drink(choice)
    if(machine.is_resource_sufficient(drink)):
        if(money.make_payment(drink.cost)):
            print(machine.make_coffee(drink))
