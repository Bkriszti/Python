from art import logo
from replit import clear
import random

LEVEL_EASY_TURNS = 10
LEVEL_HARD_TURNS = 5


def choose_level():
  ans = input("Type 'easy' for 10 attempts or 'hard' for 5\n")
  if ans == "easy":
    return LEVEL_EASY_TURNS
  else:
    return LEVEL_HARD_TURNS


def check_answer(answer, guess, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")


print(logo)
print("Number guessing")
number = random.randint(1, 100)
turns = choose_level()
guess = 0
while guess != number:
  if turns == 0:
    print("You loose!")
    break
  print(f"You have {turns} attempts remaining!")
  guess = int(input("Introduce your number: "))
  turns = check_answer(number, guess, turns)
