import random
import numpy as np
i = random.randint(1,100)
# Antal gissningar
n = 1

guess = 50

d = guess // 2
while True: 
    if guess == i:
        print(f"Congratulations, you guessed correct after {n} guesses!")
        break
    else:
        if guess < i:
            guess += d
            # Runda uppåt för att undvika att d blir 0 vid division med 2
            d = np.ceil(d / 2)
            n += 1
        elif guess > i:
            guess -= d
            d = np.ceil(d/2)
            n += 1