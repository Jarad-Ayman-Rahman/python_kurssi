import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="pythonuser",
    password="",
    database="airports"
)

maakoodi = input("Anna maakoodi: ").upper()

sql = """
SELECT type, COUNT(*)
FROM airports
WHERE iso_country = %s
GROUP BY type
"""

cursor = yhteys.cursor()
cursor.execute(sql, (maakoodi,))

tulokset = cursor.fetchall()

for tyyppi, maara in tulokset:
    print(tyyppi, maara)

cursor.close()
yhteys.close()
