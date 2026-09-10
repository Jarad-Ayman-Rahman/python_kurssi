

def bensiini_maara(gallona):
  return gallona * 3.785

while True:
    gallona = float(input("Anna gallonamäärä: "))

    if gallona < 0:
        break

    litrat = bensiini_maara(gallona)
    print(litrat)