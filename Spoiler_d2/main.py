bill=float(input("How much is your bill?"))
persons=float(input("How many persons to split the bill?"))
tips=float(input("How many tips?10,12,15?"))
total=bill+bill*tips/100.
total=total/persons/1.00
print(total)