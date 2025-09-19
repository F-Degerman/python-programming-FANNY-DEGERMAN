import math

print("6:ans multiplikationstabell från 0 till 10: ")
for i in range(0, 11):
    print(f"{6 * i}", end=" ")



print("\n\nVälj en egen tabell att skriva ut med ett start- och slutvärde: ")

tabell = int(input("Vilken tabell vill du skriva ut? "))
start = int(input("Start: "))  
slut = int(input("Slut: "))  
for i in range(start, slut + 1):
    print(f"{tabell * i}", end=" ")


