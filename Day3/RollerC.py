height = int(input("Height: "))
age = int(input("Age: "))
if height >= 120:
  if age < 12:
    print("Can, 7$")
  elif age <= 18:
    print("Can. 12$")
  else:
    print("Can, 20$")
else:
  print("Can't")
