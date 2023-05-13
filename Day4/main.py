import random
choose=int(input("What do you choose?0-Rock, 1-Paper, 2-Scrissors"))
rand=random.randint(0,2)
print(f"Computer choice:{rand}")
if choose==0:
  if rand==0:
    print("Draw")
  elif rand==1:
    print("Computer wins")
  else:
    print("You win")

if choose==1:
  if rand==0:
    print("You win")
  elif rand==1:
    print("Draw")
  else:
    print("Computer wins")
    
if choose==2:
  if rand==0:
    print("Computer wins")
  elif rand==1:
    print("You win")
  else:
    print("Draw") 
