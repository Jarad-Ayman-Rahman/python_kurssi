
while True:
    valinta = input("Haluatko syöttää uuden lentoaseman (u), hakea lentoaseman (h) vai lopettaa (l): ")

    if valinta == "u":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif valinta == "h":
        icao = input("Anna ICAO-koodi: ")
        print(lentoasemat[icao])

    elif valinta == "l":
        break