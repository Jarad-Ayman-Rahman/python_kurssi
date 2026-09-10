import math

def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * sade ** 2
    pinta_ala_neliometreina = pinta_ala / 10000
    return hinta / pinta_ala_neliometreina


halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta: "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija: "))
hinta2 = float(input("Anna toisen pizzan hinta: "))

hinta1_m2 = yksikkohinta(halkaisija1, hinta1)
hinta2_m2 = yksikkohinta(halkaisija2, hinta2)

if hinta1_m2 < hinta2_m2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif hinta2_m2 < hinta1_m2:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat yhtä hyviä vastineeltaan.")