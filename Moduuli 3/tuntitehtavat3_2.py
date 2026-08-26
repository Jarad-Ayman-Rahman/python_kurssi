#Ohjelma, joka kysyy käyttäjän pituuden, ja kertoo sitte mihin huvipuiston laitteisiin hän saa mennä.

if pituus >= 140:
  print("Pääset kaikkiin laitteisiin")

  ika = int(input("Mikä on ikäsi? "))
  if ika >= 8:
    print("Pääset kaikkiin laitteisiin")
  else:
    print("Pääset kaikkiin paitsi Tulirekeen")

elif pituus >= 100:
  print("Pääset lasten laitteisiin")
else:
  print("Et pääse vielä mihinkään.")