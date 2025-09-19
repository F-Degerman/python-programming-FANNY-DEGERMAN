import math
print("Räknar ihop varje tal i intervallet 1-100: ")

for i in range(1, 101):
    n = 0
    n += i  
n = sum(range(1, 101))
print(n)

print("Räknar ihop varje udda tal i intervallet 1-100: ")   
for i in range(1, 100, 2):
    # n= håller koll på summan av talen 
    n = 0
    # lägger till varje udda tal i summan
    n += i  
n = sum(range(1, 100, 2))
print(n)    
