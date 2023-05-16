# def encrypt(string, nshift):
#   cipher_text = ""
#   for i in string:
#     index = alphabet.index(i)
#     if index + nshift > 25:
#       index = (index + nshift) % 26
#       cipher_text += alphabet[index]
#     else:
#       cipher_text += alphabet[index + nshift]
#   print(f"The encoded text is: {cipher_text}")

# def decrypt(string, nshift):
#   cipher_text = ""
#   for i in string:
#     index = alphabet.index(i)
#     if index - nshift < 0:
#       index = (index - nshift) % 26
#       cipher_text += alphabet[index]
#     else:
#       cipher_text += alphabet[index - nshift]
#   print(f"The encoded text is: {cipher_text}")


def caesar(string, nshift, fdirection):
  cipher_text = ""
  if fdirection == "decode":
    nshift = -nshift
  elif fdirection != "decode" and fdirection != "encode":
    print("No good function")
    exit(-1)
  for i in string:
    if i in alphabet:
      index = alphabet.index(i)
      if index + nshift > 25:
        index = (index + nshift) % 26
        cipher_text += alphabet[index]
      elif index - nshift < 0:
        index = (index - nshift) % 26
        cipher_text += alphabet[index]
      else:
        cipher_text += alphabet[index + nshift]

    else:
      cipher_text += i
  print(f"The encoded text is: {cipher_text}")


alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
answer = "YES"
while (answer == "YES"):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(text, shift, direction)
  answer = input("Do you want to try again? Y or N \n")
  if answer == "Y":
    answer = "YES"
  else:
    "NO"
