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
    },

}

resources = {
    "water": 200,
    "milk": 150,
    "coffee": 24,
}


def continue_working(working):
    if user_ask == "off":
        working = False
        return


def report(resources):
    global profit
    if user_ask == "report":
        print(f"Water: {resources.get("water")}")
        print(f"Milk: {resources.get("milk")}")
        print(f"Coffee: {resources.get("coffee")}")
        print(f"Money: ${profit}")


def check_resources(resources, MENU):

        coffee = MENU[user_ask]
        coffee_ingredients = coffee.get("ingredients")
        for value in coffee_ingredients:
            if resources.get(value) >= coffee_ingredients.get(value):
                new_resources = resources.get(value) - coffee_ingredients.get(value)
                resources[value] = new_resources
            else:
                print("oops we dont have enough resources to make your coffee!")

def process(MENU):
    quarters = int(input("How many quarters?")) * 0.25
    dimes = int(input("How many dimes?")) * 0.10
    nickels = int(input("How many nickels?")) * 0.05
    pennies = int(input("How many pennies?")) * 0.01
    pay_money = quarters + dimes + nickels + pennies
    coffee = MENU[user_ask]
    profit = coffee.get("cost")
    if pay_money < profit:
        print("your money is not enough for our coffee")
    else:
        money = pay_money - coffee.get("cost")
        print(f"Here is {money} in change")
        print("Enjoy your coffee")
    return profit


working = True
while working:
   money = 0
   user_ask = input("What would you like? (espresso/latte/cappuccino):").lower()
   continue_working(working)
    if user_ask == "espresso" or user_ask == "latte" or user_ask == "cappuccino":
        check_resources(resources, MENU)
        process(MENU)
    else:
        report(resources)




