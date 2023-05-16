def greet():
  print("Hello")
  print("World")
  print("!")


greet()


def greet_name(name):
  print(f"Hello {name}")
  print("Goodbye")


greet_name("Kriszti")


def greet_2(name, location):
  print(f"{name} is in {location}")
  print("Bye")


greet_2("Maria", "Beclean")  #POSITIONAL ARGUMENT
greet_2(location="Beclean", name="Maria")  #KEYWORD ARGUMENT
