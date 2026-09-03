
import random

N = int(input("Anna arvottavien pisteiden määrä: "))

n = 0 


for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # Tarkistetaan, onko piste yksikköympyrän sisällä
    if x*x + y*y < 1:
        n = n + 1

pi_approksimaatio = 4.0 * n / N


print("Piin likiarvo on:", pi_approksimaatio)