import math

print("Det här programmet kollar om dina tre tal kan bilda en rätvinklig triangel") 
tal_a = float(input("skriv tal A: "))
tal_b = float(input("skriv tal B: "))     
tal_c = float(input("skriv tal C: ")) 

if tal_a + tal_b + tal_c == 180:
    print("Dina tal kan bilda en triangel")
    if (tal_a == 90) or (tal_b == 90) or (tal_c == 90):
        print("Dina tal kan bilda en rätvinklig triangel")
    else:
        print("Dina tal kan inte bilda en rätvinklig triangel")
else:
    print("Dina tal kan inte bilda en triangel")

