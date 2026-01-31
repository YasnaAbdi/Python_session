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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#order = input("What would you like? (espresso/latte/cappuccino):")
def call_order():
    order = input("What would you like? (espresso/latte/cappuccino):")
    return order


def check_resources(order):
    if order == "espresso":
        if resources["water"] < 50 or resources["coffee"] < 18:
            print("Sorry there is not enough water or coffee.")
            call_order()
        else:
            process_coin(order)
    if order == "latte":
        if resources["water"] < 200 or resources["milk"] < 150 or  resources["coffee"] < 24:
            print("Sorry there is not enough water or coffee or milk.")
            call_order()
        else:
            process_coin(order)
    if order == "cappuccino":
        if resources["water"] < 250 or resources["milk"] < 100 or  resources["coffee"] < 24:
            print("Sorry there is not enough water or coffee or milk.")
            call_order()
        else:
            process_coin(order)


def turn_off(order):
    if order == "off":
        print("Machine has turn off.")
    return 0

def report(order):
   if order == "report":
        resource_diff(process_coin(order), order)


def process_coin(order):
    coin = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    quarters_r = int(input("How many quarters would you pay?")) * coin["quarters"]
    dimes_r = int(input("How many dimes would you pay?")) * coin["dimes"]
    nickles_r = int(input("How many nickles would you pay?")) * coin["nickles"]
    pennies_r = int(input("How many pennies would you pay?")) * coin["pennies"]

    customer_pay = quarters_r + dimes_r + nickles_r + pennies_r

    if order == "espresso":
        total_coin = MENU["espresso"]["cost"]
        if customer_pay >= total_coin:
            in_change = customer_pay - total_coin
            print(f"Here is ${in_change} dollars in change. enjoy")
            resource_diff(in_change, order)
            call_order()
            return in_change
        else:

            print("Sorry that's not enough money. Money refunded.")
            call_order()
            return 0
    elif order == "latte":
        total_coin = MENU["latte"]["cost"]
        if customer_pay >= total_coin:
            in_change = customer_pay - total_coin

            print(f"Here is ${in_change} dollars in change. enjoy")
            resource_diff(in_change, order)
            call_order()
            return in_change
        else:

            print("Sorry that's not enough money. Money refunded.")
            call_order()
            return 0
    else:
        total_coin = MENU["cappuccino"]["cost"]
        if customer_pay >= total_coin:
            in_change = customer_pay - total_coin
            print(f"Here is ${in_change} dollars in change. enjoy")
            resource_diff(in_change, order)
            call_order()
            return in_change
        else:

            print("Sorry that's not enough money. Money refunded.")
            call_order()
            return 0




def resource_diff(in_change, order):
    if order == "report":
        resources["water"] = resources["water"]
        resources["coffee"] = resources["coffee"]
        resources["milk"] = resources["milk"]
    if order == "espresso":
        resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        print(f"Water: {resources["water"]}\n Coffee: {resources["coffee"]}\n Money: {in_change}\n ")
        call_order()
    if order == "latte":
        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        print(f"Water: {resources["water"]}\n Coffee: {resources["coffee"]}\n Money: {in_change}\n ")
        call_order()
    if order == "cappuccino":
        resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        print(f"Water: {resources["water"]}\n Coffee: {resources["coffee"]}\n Money: {in_change}\n ")
        call_order()







result = call_order()
report(result)
turn_off(result)
check_resources(result)
process_coin(result)


