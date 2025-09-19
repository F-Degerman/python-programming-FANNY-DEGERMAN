import math

#i = första talet i talföljden (1-100)
i = 1
#n = summan av talen i talföljden (1-100)
n = 1
# Räknar upp alla tal från 1 till 100 och lägger ihop dem i varje steg av talföljden
while i < 100:
    n += i + 1
    i += 1
print(n)

# udda tal
i = 1
n = 1
while i < 99:
    n += i + 2
    i += 2
print(n)