import math

print("Det här programmet kollar vilket av dina tal som är minst")

number1 = float(input("skriv ett tal: "))
number2 = float(input("skriv ett annat tal: "))     

if number1 > number2:
    print(f"{number2} är minst")
else:
    print(f"{number1} är minst")
      