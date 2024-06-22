water = 300
milk = 200
coffee = 100

def get_change():
    quarters = int(input("Please insert coins.\nHow many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = ((quarters * 25) + (dimes * 10) + (nickels * 5) + pennies)
    dollars = total // 100
    cents = total % 100
    return round(dollars + cents / 100.00, 2)

choice = ""
while choice != "quit":
    choice = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if choice == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}mg")
    else:
        if choice == "espresso":  # Requires 50ml water and 18g coffee
            total = get_change()
            if total >= 1.50:
                change = round(total - 1.50, 2)
                print(f"Here's your change: ${change}, enjoy your espresso!")
                water -= 50
                coffee -= 18
            else:
                print(f"You don't have enough money. You need ${round(1.50 - total, 2)} more.")

        elif choice == "latte":  # Requires 200ml water, 150ml milk, and 24g coffee
            total = get_change()
            if total >= 2.00:
                change = round(total - 2.00, 2)
                print(f"Here's your change: ${change}, enjoy your latte!")
                water -= 200
                milk -= 150
                coffee -= 24
            else:
                print(f"You don't have enough money. You need ${round(2.00 - total, 2)} more.")

        elif choice == "cappuccino":  # Requires 250ml water, 100ml milk, and 24g coffee
            total = get_change()
            if total >= 2.50:
                change = round(total - 2.50, 2)
                print(f"Here's your change: ${change}, enjoy your cappuccino!")
                water -= 250
                milk -= 100
                coffee -= 24
            else:
                print(f"You don't have enough money. You need ${round(2.50 - total, 2)} more.")
        
        elif choice == "quit":
            print("Goodbye!")
        
        else:
            print("Unexpected input for drink")
