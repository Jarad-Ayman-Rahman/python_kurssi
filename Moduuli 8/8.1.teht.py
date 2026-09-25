import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="pythonuser",
    password="python123",
    database="airports"
)

icao = input("Anna lentoaseman ICAO-koodi: ")

sql = """
SELECT name, municipality
FROM airports
WHERE ident = %s
"""

cursor = yhteys.cursor()
cursor.execute(sql, (icao,))

tulos = cursor.fetchone()

if tulos:
    print("Lentoasema:", tulos[0])
    print("Sijaintikunta:", tulos[1])
else:
    print("Lentoasemaa ei löytynyt.")

cursor.close()
yhteys.close()