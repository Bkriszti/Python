# firstchar = "Hello"[4]
# print(firstchar)
# #INT
# print(123_456_789)
# #float
# print(123_245.56)
# #boolean
# ok = True
# ok = False
# print(type(ok))

# num_char = input("What is your number?")
# firstd = int(num_char[0])
# secondd = int(num_char[1])
# print(firstd + secondd)

#PRINT CAN'T CONCATENATE STRING TO INT
# print("Your name has " + str(num_char) + " characters")
#MATHEMATICAL OPERATION 2**2=2^2

#round(2.5, 3)-> 3 digits after .
# print(8//3)->int division

print(round(8 / 3, 2))
# f-String->letter f before ""-> print(f"Hello World {variable_name}")
# score = 0
# print(f"Hello {score}")
bill = input("What was the total bill?")
tip = input("Tips percentage: ")
persons = input("Numbers of persons: ")
total = float(bill) + float(bill) * int(tip) / 100
final = total / int(persons)
final = round(final, 2)  # =    final="{:.2f}".format(final)

print(f"Each person should pay: ${total_divided}")
