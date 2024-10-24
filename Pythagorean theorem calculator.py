import math

print("Here is a Python calculator for Pythagoras' theorem!")
response_choice = input("What do you want to know? (hypotenuse [h] or Cathetus [c])")
a = int(input("What is the length of the first Cathetus?"))
if response_choice.lower() == "h":
    b = int(input("What is the length of the second Cathetus?"))
    x = a**2 + b**2
    x = math.sqrt(x)
    print(f"The hypotenuse is: {x}")

if response_choice.lower() == "c":
    b = int(input("What is the length of the hypotenuse?"))
    x = b**2 - a**2
    x = math.sqrt(x)
    print(f"The second Cathetus is: {x}")

