import math

print("Det här programmet kollar om:\n1. ditt tal är jämt eller udda \n2.Ditt tal är delbart med 5 \n3.Ditt tal är delbart med 5 och udda")

number = int(input("Skriv ett tal: "))  
if number % 2 == 0:
    print(f"{number} är ett jämt tal")
else:
    print(f"{number} är ett udda tal")  
if number % 5 == 0:
    print(f"{number} är delbart med 5")    
else:
    print(f"{number} är inte delbart med 5")
       
