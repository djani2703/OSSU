import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w', 'utf-8')
fhand.write('myData = [\n')
count = 0

for row in cur:
    data = str(row[1].decode())

    try:
        json_data = json.loads(str(data))
    except:
        continue
    
    if not ('status' in json_data and json_data['status'] == 'OK'):
        continue

    lat = json_data['results'][0]['geometry']['location']['lat']
    lng = json_data['results'][0]['geometry']['location']['lng']

    if lat == 0 or lng == 0:
        continue
    
    where = json_data['results'][0]['formatted_address']
    where = where.replace("'", "")

    try:
        print(where, lat, lng)

        count += 1
        if count > 1:
            fhand.write(',\n')
        
        output = '[' + str(lat) + ', ' + str(lng) + ', \'' + where + '\']'
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser.")