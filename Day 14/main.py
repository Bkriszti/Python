from game_data import data
from art import logo
from art import vs
import random
from replit import clear

print(logo)
score = [0]


def funct(rand, rand2):
  if score[0] == 0:
    rand = random.randint(0, 49)
  print(
    f"Compare A: {data[rand]['name']}, a {data[rand]['description']}, from{data[rand]['country']}."
  )
  rand2 = random.randint(0, 49)
  while rand == rand2:
    rand2 = random.randint(0, 49)
  print(vs)
  print(
    f"Against B: {data[rand2]['name']}, a {data[rand2]['description']}, from {data[rand2]['country']}."
  )
  ans = input("Who has more followers?A or B\n")
  if ans == "A" and (data[rand]['follower_count'] >
                     data[rand2]['follower_count']):
    score[0] = score[0] + 1
    print(f"Your score is:{score[0]}")
    rand = rand2
    funct(rand, rand2)
    clear()
  elif ans == "B" and (data[rand]['follower_count'] <
                       data[rand2]['follower_count']):
    score[0] = score[0] + 1
    print(f"Your score is:{score[0]}")
    rand = rand2
    funct(rand, rand2)
    clear()


a = 0
b = 0
funct(a, b)
print("Game over!")
print(f"Your final score:{score[0]}")
