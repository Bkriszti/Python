from replit import clear
from art import logo
print(logo)
print("Welcome to Auction!")
answer="Y"
dict={}
while(answer=="Y"):
  name=input("What is your name?: ")
  bid=int(input("What's your bid?$:  "))
  dict[name]=bid
  answer=input("Are there any other bidder?Y or N")
  if answer=="Y":
    clear()

maxim=0
name_best=""
for names in dict:
  if dict[names] > maxim:
    maxim=dict[names]
    name_best=names

print(f"The winner is {name_best} with {maxim}$ auction")
    
  