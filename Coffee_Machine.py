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
offerings=['espresso','latte','cappuccino']


def amount(a):
    if a=="ok":
        q=float(input("Enter quarters\t"))
        d = float(input("Enter dimes\t"))
        n = float(input("Enter nickel\t"))
        p = float(input("Enter pennies\t"))
        total_cost = 0.25 * q + 0.1 * d + 0.05 * n + 0.01 * p
        return total_cost
def resource_sufficient(requirement):
    want_water=requirement['water']
    storage_water=resources["water"]
    want_milk=requirement["milk"]
    storage_milk=resources["milk"]
    want_coffee=requirement["coffee"]
    storage_coffee=resources["coffee"]
    if(storage_water<want_water):
        return print("Sorry there is not enough water ")
    elif (storage_milk<want_milk ):

        return print("Sorry there is not enough milk ")
    elif (storage_coffee<want_coffee ):
        return print("Sorry there is not enough coffee")
    else:
        return "ok"

def process_coins(total_cost,cost):

    if (total_cost<cost):
        return print("Insufficient coins inserted money refunded")
    elif(total_cost>cost):
        print(f"Here is ${round((total_cost-cost),2)} dollars in change")
        return (total_cost-cost)
def report(choosen,resources,requirement,cost):
    print(f"report before purchasing {choosen} \n {resources}")
    report={}
    report=resources
    report["milk"]=resources["milk"]-requirement["milk"]
    report["water"] = resources["water"] - requirement["water"]
    report["coffee"] = resources["coffee"] - requirement["coffee"]
    report["Money"]=f"${cost}"
    resources=report
    print(f"report after purchasing {choosen} \n {resources}")

def start():
    print(offerings)
    choosen = input("Enter your choice\t")
    if (choosen == 'off'):
        exit()
    requirement = MENU[f"{choosen}"]
    cost = requirement["cost"]
    requirement.pop("cost")
    requirement=requirement["ingredients"]
    print(requirement)
    print(resources)
    proceed=resource_sufficient(requirement)
    process_coins(amount(proceed),cost)
    report(choosen,resources,requirement,cost)

start()


