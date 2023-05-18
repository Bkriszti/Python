def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  if n2 == 0:
    return "Division by 0!!!"
  return n1 / n2


operations = {"*": multiply, "+": add, "/": divide, "-": subtract}


def calc():
  num1 = float(input("What's the first number?"))
  for op in operations:
    print(op)
  cont = "y"
  result = 0
  while (cont == "y"):
    oper_symbol = input("Choose a symbol:")
    num2 = float(input("What's the second number?"))
    oper = operations[oper_symbol]
    result = oper(num1, num2)
    num1 = result
    print(num1)
    cont = input("Do you want to contiune?y or n to start again")
    if cont == "n":
      calc()


calc()
