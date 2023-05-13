import random

names_string = input("Give persons name like this: Aurel, Gabriel, ...")
name = names_string.split(", ")
number = random.randint(0, len(name) - 1)
print(f"{name[number]} is gonna pay!")
person_who_pay = random.choice(name)
print(f"{person_who_pay} is gonna pay!")
