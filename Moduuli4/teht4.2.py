
tuuma = float(input("Tuumat senttimetreiksi: "))

while tuuma >= 0:
    senttimetrit = tuuma * 2.54
    print(tuuma, "tuumaa =", senttimetrit, "cm")
    tuuma = float(input("Tuumat senttimetreiksi: "))

print("Annettiin negatiivinen tuumamäärä.")
print("Ohjelma lopettaa. 1 tuuma = 2,54 cm")