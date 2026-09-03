hyttiluokka = (input("Anna laivan hyttiluokka (LUX, A, B, C) "))

if hyttiluokka == "LUX":
  print("LUX on pevekkeellinen hytti yläkannella.")

elif hyttiluokka == "A":
  print("A on ikkunnallinen hytti autokannen yläpuolella.")

elif hyttiluokka == "B":
  print("B on ikkunaton hytti autokannen alapuolella.")

elif hyttiluokka == "C":
  print("C on ikkunaton hytti autokannen alapuolella.")



else:
  print("Virheellinen hyttiluokka.")