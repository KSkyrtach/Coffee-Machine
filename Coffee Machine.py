Coffee = {
    "Espresso":{
        "Ml Water": 50,
        "G Coffee": 18,
        "Price": 1.5
    },
    "Latte":{
        "Ml water": 200,
        "G Coffee": 24,
        "Ml Milk": 150,
        "Price": 2.5
    },
    "Cappuccino":{
    "Ml Water": 250,
    "G Coffee": 24,
    "Ml Milk": 100,
    "Price": 3
    }
}


Machine_Resources = {
    "Ml Water": 400,
    "Ml Milk": 300,
    "G Coffee": 100,
    "Money $": 0

}

Coin_Operated = {
    "Penny": 0.01,
    "Nickel": 0.05,
    "Dime": 0.1,
    "Quarter": 0.25
}

Input = input("What would you like? (espresso/latte/cappuccino): ")
money_after_shop = 0
while Input != "Stop":
    if Input == "report":
        for key, value in Machine_Resources.items():
            print(f"{key}: {value}")

    if Input == "latte":
        Machine_Resources["Money $"] += 2.5
        Machine_Resources["G Coffee"] -= 24
        Machine_Resources["Ml Milk"] -= 150
        Machine_Resources["Ml Water"] -= 200
        if Machine_Resources["G Coffee"] < 0 or Machine_Resources["Ml Milk"] < 0 or Machine_Resources["Ml Water"] < 0:
            print("We have not enough resources.")
            Machine_Resources["Money $"] -= 2.5
            Machine_Resources["G Coffee"] += 24
            Machine_Resources["Ml Milk"] += 150
            Machine_Resources["Ml Water"] += 200
        else:
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            Sum = Coin_Operated["Quarter"] * quarters + Coin_Operated["Dime"] * dimes + Coin_Operated["Nickel"] * nickles + Coin_Operated["Penny"] * pennies
            Sum_after_change = Sum - Coffee["Latte"]["Price"]
            money_after_shop += Sum_after_change
            if money_after_shop < 0:
                print("Sorry that's not enough money. Money refunded.")
                Machine_Resources["Money $"] -= 2.5
                Machine_Resources["G Coffee"] += 24
                Machine_Resources["Ml Milk"] += 150
                Machine_Resources["Ml Water"] += 200
            else:
                print("Here is ${:.2f} in change.".format(money_after_shop))
                print("Here is your Latte! Enjoy!")

    elif Input == "espresso":
        Machine_Resources["Money $"] += 1.5
        Machine_Resources["G Coffee"] -= 18
        Machine_Resources["Ml Water"] -= 50
        if Machine_Resources["G Coffee"] < 0 or Machine_Resources["Ml Milk"] < 0 or Machine_Resources["Ml Water"] < 0:
            print("We have not enough resources.")
            Machine_Resources["Money $"] -= 1.5
            Machine_Resources["G Coffee"] += 18
            Machine_Resources["Ml Water"] += 50
        else:
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            Sum = Coin_Operated["Quarter"] * quarters + Coin_Operated["Dime"] * dimes + Coin_Operated["Nickel"] * nickles + Coin_Operated["Penny"] * pennies
            Sum_after_change = Sum - Coffee["Espresso"]["Price"]
            money_after_shop += Sum_after_change
            if money_after_shop < 0:
                print("Sorry that's not enough money. Money refunded.")
                Machine_Resources["Money $"] -= 1.5
                Machine_Resources["G Coffee"] += 18
                Machine_Resources["Ml Water"] += 50
            else:
                print(f"Here is ${money_after_shop:.2f} in change.")
                print("Here is your Espresso! Enjoy!")

    elif Input == "cappuccino":
        Machine_Resources["Money $"] += 3
        Machine_Resources["G Coffee"] -= 24
        Machine_Resources["Ml Milk"] -= 100
        Machine_Resources["Ml Water"] -= 250
        if Machine_Resources["G Coffee"] < 0 or Machine_Resources["Ml Milk"] < 0 or Machine_Resources["Ml Water"] < 0:
            print("We have not enough resources.")
            Machine_Resources["Money $"] -= 3
            Machine_Resources["G Coffee"] += 24
            Machine_Resources["Ml Milk"] += 100
            Machine_Resources["Ml Water"] += 250
        else:
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            Sum = Coin_Operated["Quarter"] * quarters + Coin_Operated["Dime"] * dimes + Coin_Operated["Nickel"] * nickles + Coin_Operated["Penny"] * pennies
            Sum_after_change = Sum - Coffee["Cappuccino"]["Price"]
            money_after_shop += Sum_after_change
            if money_after_shop < 0:
                print("Sorry that's not enough money. Money refunded.")
                Machine_Resources["Money $"] -= 3
                Machine_Resources["G Coffee"] += 24
                Machine_Resources["Ml Milk"] += 100
                Machine_Resources["Ml Water"] += 250
            else:
                print(f"Here is ${money_after_shop:.2f} in change.")
                print("Here is your Cappuccino! Enjoy!")

    if Input == "stop":
        break
    Input = input("What would you like? (espresso/latte/cappuccino) \nif you want to stop write 'stop': ")