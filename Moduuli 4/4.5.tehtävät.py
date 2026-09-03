kayttajatunnus = "python"
salasana = "rules"

yritykset = 0

while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana_syote = input("Salasana: ")

    if tunnus == kayttajatunnus and salasana_syote == salasana:
        print("Tervetuloa")
        break

    yritykset += 1

if yritykset == 5:
    print("Pääsy evätty")