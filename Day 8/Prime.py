import math


def prime_checker(number):
  ok = True
  if number == 0 or number == 1:
    ok = False
  if number == 2:
    ok = True
  if number % 2 == 0:
    ok = False
  for i in range(3, number // 2, 2):
    if number % i == 0:
      ok = False
  if number == 3:
    ok = True
  if ok == True:
    print("Number is prime!")
  else:
    print("Number is not prime!")


n = int(input("The number you want to check"))
prime_checker(number=n)
