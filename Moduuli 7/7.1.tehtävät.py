
vuodenajat = ("talvi", "kevät", "kesä", "syksy")
kuukausi = int(input("Anna kuukauden numerot (1-12): "))

if kuukausi == 12:
  print(vuodenajat[0])
elif kuukausi <= 2:
  print(vuodenajat[0])
elif kuukausi <= 5:
  print(vuodenajat[1])
elif kuukausi <= 8:
  print(vuodenajat[2])
else:
  print(vuodenajat[3])
