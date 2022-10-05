from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
drinkmenu = Menu()
drinkitem = MenuItem
money = MoneyMachine()
is_on = True

while(is_on):
    choice = input(f"What would you like to order? {drinkmenu.get_items()} ")

    if(choice == "report"):
        machine.report()
        money.report()
    elif(choice == "off"):
        print("Shutting down...  Printing final report...")
        machine.report()
        money.report()
        is_on = False
    else:
        drink = drinkmenu.find_drink(choice)
        if(machine.is_resource_sufficient(drink)):
            if(money.make_payment(drink.cost)):
                machine.make_coffee(drink)
