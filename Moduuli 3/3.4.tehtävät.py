Vuosi = int(input("Anna vuosiluku: "))

if Vuosi % 400 == 0:
  print("Vuosi on karkausvuosi")

elif Vuosi % 100 == 0:
  print("Vuosi ei ole karkausvuosi.")
elif Vuosi % 4 == 0:
  print("Vuosi on karkausvuosi.")


else:
  print("Vuosi ei ole karkausvuosi.")