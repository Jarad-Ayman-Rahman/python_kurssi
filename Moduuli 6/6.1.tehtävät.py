import random

def heita_noppaa():
  return random.randint(1, 6)

while True:
  luku = heita_noppaa()
  print(luku)
  if luku == 6:
    break



  