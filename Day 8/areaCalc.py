import math


def CanCalc(width, height, cover):
  total = (float(width) * float(height)) / cover
  print(f"You need {math.ceil(total)} cans")


CanCalc(width=7, height=13, cover=5)
