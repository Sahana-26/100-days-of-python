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

def is_sufficient(order_ingredients):
    for i in order_ingredients:
        print(i)
        if order_ingredients[i]>resources[i]:
            print(f'sorry there is not enough {i}')
            return False
    return True

def calculate_money():
    print('please insert coins.....')
    total= int(input('how many quarters?  '))*0.25
    total+=int(input('how many dimes?  '))*0.1
    total+=int(input('how many nickles?  '))*0.05
    total+=int(input('how many pennies?  '))*0.01
    return total

def is_transaction_success(money,cost):
    if money>cost:
        change = round(money-cost,2)
        print(f'here is your {change}rs in change.')
        global profit 
        profit+=money
        return True
    else:
        print("insufficient money")
        return False

def make_coffee(choice,order_ingredients):
    for i in order_ingredients:
        resources[i]-=order_ingredients[i]
    print(f'here is your {choice}....enjoy!!!!')


profit = 0
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee": 100
}

is_on = True

while is_on:
    choice = input('what do you choose? (espresso/cappuccino/latte/report)')
    if choice=='off':
        is_on=False
    elif choice=='report':
        print(f"water : {resources['water']}ml \nmilk : {resources['milk']}ml\ncoffee : {resources['coffee']}g ")
    else:
        drink = MENU[choice]
        if is_sufficient(drink['ingredients']) == True:
            money = calculate_money()
            if is_transaction_success(money,drink['cost']):
                make_coffee(choice,drink['ingredients'])