import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="pythonuser",
    password="python123",
    database="airports"
)

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")

sql = """
SELECT name, latitude_deg, longitude_deg
FROM airports
WHERE ident = %s
"""

cursor = yhteys.cursor()

cursor.execute(sql, (icao1,))
kentta1 = cursor.fetchone()

cursor.execute(sql, (icao2,))
kentta2 = cursor.fetchone()

if kentta1 and kentta2:
    koordinaatit1 = (kentta1[1], kentta1[2])
    koordinaatit2 = (kentta2[1], kentta2[2])

    etaisyys = geodesic(koordinaatit1, koordinaatit2).kilometers

    print(f"Lentokenttien välinen etäisyys on {etaisyys:.1f} km.")
else:
    print("Lentokenttää ei löytynyt.")

cursor.close()
yhteys.close()