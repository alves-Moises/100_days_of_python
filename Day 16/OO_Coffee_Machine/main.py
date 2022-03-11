from replit import clear
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    coffee = CoffeeMaker()
    money_machine = MoneyMachine()


    is_on = True
    while is_on:
        print("What your choice?", menu.get_items())
        answer = input()
        
        #turn off
        clear()
        if answer == "off":
            is_on = False
            break
        

        #show info
        if answer == "report":
            coffee.report()
            money_machine.report()


        # make answer
        if answer in menu.get_items():
            item = menu.find_drink(answer)
            money_machine.process_coins()

            
            if coffee.is_resource_sufficient(item):
                payment_acepted = False
                while not payment_acepted:
                    if money_machine.make_payment(item.cost):
                        payment_acepted = True
                    # else:
                    #     money_machine.process_coins()


                print("Payment succefull!")
                coffee.make_coffee(item)
          

        if not (answer in menu.get_items()) and (answer != "report"):
            print("Invalid choice.")
     

    print("End...")


main()