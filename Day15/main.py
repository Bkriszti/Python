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


def verify(rw,rm,rc,ans):
    if ans!="espresso":
        if rw<MENU[ans]["ingredients"]["water"]:
            return 0
        if rm<MENU[ans]["ingredients"]["milk"]:
            return 0
        if rc<MENU[ans]["ingredients"]["coffee"]:
            return 0
        return 1
    else:
        if rw<MENU[ans]["ingredients"]["water"]:
            return 0
        if rc<MENU[ans]["ingredients"]["coffee"]:
            return 0
        return 1

def machine(money):
    ans=input("What do you want to buy?espresso/latte/cappucino?")
    rw = resources["water"]
    rm = resources["milk"]
    rc = resources["coffee"]
    if ans == "report":
        print(f"Water left: {rw}" )
        print(f"Milk left: {rm}")
        print(f"Coffee  left: {rc}")
        print(f"Money:${money}")
        machine(money)
    else:
        if verify(rw,rm,rc,ans)==1:
            print("Please insert coins!")
            quar=float(input("How many quarters?"))
            dim = float(input("How many dimes?"))
            nick = float(input("How many nickles?"))
            pen = float(input("How many pennies?"))
            total=0.25*quar+0.10*dim+0.05*nick+0.01*pen
            if total>=float(MENU[ans]["cost"]):
                cost= float(MENU[ans]["cost"])
                money += cost
                if ans=="espresso":
                    rw=rw-int(MENU[ans]["ingredients"]["water"])
                    rc=rc-int(MENU[ans]["ingredients"]["coffee"])
                    resources["water"]=rw
                    resources["coffee"]=rc
                else:
                    rw = rw - int(MENU[ans]["ingredients"]["water"])
                    rc = rc - int(MENU[ans]["ingredients"]["coffee"])
                    rm=rm-int(MENU[ans]["ingredients"]["milk"])
                    resources["water"] = rw
                    resources["coffee"] = rc
                    resources["milk"]=rm
                change=format(total-cost,".2f")
                print(f"Here is ${change} in change!")
                print(f"Here is your {ans}!")
                machine(money)
        else:
            print("You don't have enough resources!")
            machine(money)
machine(0)
