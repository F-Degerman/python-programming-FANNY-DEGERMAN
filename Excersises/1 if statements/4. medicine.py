import math

print("Det här programmet hjälper dig att avgöra hur många tabletter du kan ta")

age = int(input("Hur gammal är du? "))
weight = int(input("Hur mycket väger du i kg? "))

if age >= 12 and weight > 40:
    print("Du kan ta 1-2 tabletter")
elif age <= 12 and age >= 6 and weight <= 40 and weight >= 25:
    print("Du kan ta 1/2-1 tablett")
elif age <= 7 and age >= 2 and weight <= 26 and weight >= 14:
    print("Du kan ta 1/2 tablett")
else:
    print("Du kan inte ta några tabletter") 
