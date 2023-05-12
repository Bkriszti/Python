size = input("What size? S,M,L")
extra_p = input("Do you want extra pepperoni?Y or N")
extra_ch = input("Do you want extra cheese?Y or N")
if size == "S":
  bill = 15

elif size == "M":
  bill = 20

else:
  bill = 20

if extra_p == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_ch == "Y":
  bill += 1

print(f"Your pizza price is {bill}")
