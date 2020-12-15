# -*- coding: utf-8 -*-

# Agreed on a 'wired format': xml:
# XML example:
'''
<person>
    <name>Chuck</name>
    <phone type="intl">+1 734 303 4456</phone>
    <emali hide="yes" />
</person>
'''

# JSON example:
'''
{
    "name": "Chuk",
    "phone': "303-4456"
}
'''

# XML elements (or Nodes):
'''
<people>
    <person>
        <name>Chuck</name>
        <phone>303 4456</phone>
    </person>
    <person>
        <name>Noah</name>
        <phone>622 7421</phone>
    </person>
</people>
'''

# Worked example - XML:
import xml.etree.ElementTree as et

data_0 = '''
<person>
    <name>Chuck</name>
    <phone type='intl'>
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = et.fromstring(data_0)

print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = et.fromstring(data)
users = stuff.findall('users/user')

for user in users:
    print('[attr:', user.get('x'), '] Name: ', user.find('name').text, ' and id: ', user.find('id').text, sep='')

# JSON:
import json

data = '''{
    "name": "Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
    },
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data)
print('Name:', info['name'])
print('Phone number:', info['phone']['number'])
print('Hide:', info['email']['hide'])

# JSON represents data as nested lists and dictionaries:
data = '''[
    {
        "id": "001",
        "x": "2",
        "name": "Chuck"
    },
    {
        "id": "009",
        "x": "7",
        "name": "Joseph"
    }
]'''

info = json.loads(data)
for item in info:
    print('[', item['id'], '] name: ', item['name'], ' and x: ', item['x'], sep='')

# GeoJSON example:
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    
    if len(address) < 1: 
        break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving:', url)
    url_handler = urllib.request.urlopen(url)
    data = url_handler.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure Retrieve ====')
        print(data)
        continue
    
    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

# Using Twitter API's:
import twurl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    acct = input('Enter twitter account: ')
    if (len(acct) < 1):
        break
    url = twurl.argument(TWITTER_URL, {'screen_name': acct, 'count': 5})

    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)

    print(json.dumps(js, indent=4))

    for u in js['user']:
        print(u['screen_name'])
        s = u['status']['text']
        print('  ', s[:50])

# Twitter test:
from twurl import argument
import ssl

print('*Calling Twitter...')

ulr = argument('https://api.twitter.com/1.1/statuses/user_timeline.json',
                {'screen_name': 'drchuck', 'count': '2'})

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=context)
data = connection.read().decode()

headers = dict(connection.getheaders())
