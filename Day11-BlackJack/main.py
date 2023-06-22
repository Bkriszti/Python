from replit import clear
from art import logo
import random


def caddcard():
  card = cards[random.randint(0, 12)]
  clist.append(card)


def paddcard():
  card = cards[random.randint(0, 12)]
  plist.append(card)


def cscore():
  sum = 0
  for i in clist:
    sum += i
  return sum


def pscore():
  sum = 0
  for i in plist:
    sum += i
  return sum


def funct():
  answ = input("Type 'y' to get another card or 'n' to pass\n")
  if answ == "y":
    paddcard()
    print(f"Your cards are {plist}, total score {pscore()}")
    funct()


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ans = input("Do you wanna play blackjack? Y or N\n")
if ans == "N":
  clear()
  print("Bye")

clear()
print(logo)
plist = []
clist = []
card1 = cards[random.randint(0, 12)]
card2 = cards[random.randint(0, 12)]
plist.append(card1)
plist.append(card2)
print(f"Your cards are {plist}, total score:{pscore()}")
ccard1 = cards[random.randint(0, 12)]
ccard2 = cards[random.randint(0, 12)]
clist.append(ccard1)
print(f"Computer's first card:{clist}")
clist.append(ccard2)
while cscore() < 17:
  caddcard()
funct()
fps = pscore()
fcs = cscore()
if (fps > 21):
  print("Dealer wins!")
elif (fcs > 21):
  print("Player wins!")
elif (fps > fcs):
  print("Player wins!")
elif (fcs > fps):
  print("Dealer wins!")
else:
  print("Draw!")

print(f"Computer's cards: {clist}, toltal score:{cscore()}")
