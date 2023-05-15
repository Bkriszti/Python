import random

word_list = ["hangman", "mouse", "art", "camel"]
word = random.choice(word_list)
print(word)
string = []

for i in range(len(word)):
  print("_", end='')
  string.append("_")

print("")
count = 0
#while count<6:
# letter=input("What is your letter?")
# if(word.find(letter)!=-1):
#  print("You have choose a good  letter!")
#else:
#  print("Bad")
# count+=1

ok = 0
count = 0
while count < 6 and string.count("_") != 0:
  chletter = input("What is your letter?").lower()
  ok = 0
  for i in range(0, len(word)):
    if word[i] == chletter:
      string[i] = chletter
      ok = 1

  if ok == 1:
    print(string)
  if ok == 0:
    count += 1
    print("Bad ch")

if count == 6:
  print("Loose!")
else:
  print("Win!")
