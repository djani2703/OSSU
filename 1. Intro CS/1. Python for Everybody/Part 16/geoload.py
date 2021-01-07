import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys


api_key = False

if api_key:
    service_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
else:
    service_url = 'http://py4e-data.dr-chuck.net/geojson?'


conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhand = open('where.data')
count = 0

for line in fhand:
    if count > 200:
        print('Retrieved 200 locations, restart to retrieve more')
        break
    address = line.strip()

    cur.execute('SELECT geodata FROM Locations WHERE address=?', (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print('Found in database ', address)
        continue
    except:
        pass

    params = dict()
    params['query'] = address
    
    if api_key is not False:
        params['key'] = api_key
    
    url = service_url + urllib.parse.urlencode(params)

    print('Retrieving..', url)
    uhand = urllib.request.urlopen(url)
    data = uhand.read().decode()
    print('Retrieved.', len(data), 'characters', data[:20].replace('\n', ' '))
    
    count += 1

    try:
        json_data = json.loads(data)
    except:
        print(data)
        continue

    if 'status' not in json_data or (json_data['status'] != 'OK' and json_data['status'] != 'ZERO_RESULTS'):
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('INSERT INTO Locations (address, geodata) VALUES (?, ?)', 
    (memoryview(address.encode()), memoryview(data.encode())))

    conn.commit()
    if count % 10 == 0:
        print('Pausing for a bit..')
        time.sleep(5)

print('Run geodump.py to read the data from the database so you can visualize it on a map.')