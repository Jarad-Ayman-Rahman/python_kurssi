

import random

lukumäärä = int(input("Anna arpakuution lukumäärä: "))

summa = 0

for i in range(lukumäärä):
  silmäluku = random.randint(1, 6)
  summa += silmäluku


print(f"Silmälukujen summa on: {summa}")