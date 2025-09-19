import math

print("Det här programmet kollar om ditt bagage har rätt storlek och vikt för att få tas med på flyget")

length = float(input("Skriv längden på ditt bagage i cm: "))
width = float(input("Skriv bredden på ditt bagage i cm: "))
height = float(input("Skriv höjden på ditt bagage i cm: "))
weight = float(input("Skriv vikten på ditt bagage i kg: ")) 

if length <= 55 and width <= 40 and height <= 25 and weight <= 8:
    print("Ditt bagage har rätt storlek och vikt för att få tas med på flyget")
else:
    print("Ditt bagage har inte rätt storlek och/eller vikt för att få tas med på flyget")
