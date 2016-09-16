import pyodbc
import json
cnx = pyodbc.connect('DSN=hi')
cursor = cnx.cursor()


getcmd = "select tweet from dbo.twitter2"
cursor.execute(getcmd)
row = cursor.fetchall()

weather_data = []
for r in row:
    weather_data.append(json.loads(r[0]))

print weather_data