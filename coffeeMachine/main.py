MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# starting from here.


def isResourceSufficient(orderIngredients):
    """Return TRUE when order get in process, False when ingredients are insufficient"""
    for item in orderIngredients:
        if orderIngredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def processCoins():
    """Return the total calculated from coins inserted"""
    print("Please insert coins. ")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total



def isTransactionSuccessful(moneyReceived,drinkCost):
    """Returns TRUE whwn the payment accepted ELSE, FALSE if money is insufficient"""
    if moneyReceived >= drinkCost:
        change = round(moneyReceived - drinkCost, 2)
        global profit
        profit += drinkCost
        return True
    else:
        print("Sorry, Thats' not enough money. Money Refunded")
        return False

def makeCoffee(drinkName, OrderIngredients):
    """Deduct the required ingredients form the resources"""
    for item in OrderIngredients:
        resources[item] -= OrderIngredients[item]
    print(f"Voila, Here is your {drinkName} ")




isOn = True;

while isOn:
    choice = input("What would you like? (espresso / latte / cappuccino ) : ")
    if (choice == "off"):
        isOn = False 
    elif (choice == "report"):
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if isResourceSufficient(drink["ingredients"]):
            payment = processCoins()
            if isTransactionSuccessful(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])





