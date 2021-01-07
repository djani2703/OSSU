import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Pages') # Delete it later
cur.execute('DROP TABLE IF EXISTS Webs')
cur.execute('DROP TABLE IF EXISTS Links')


cur.execute('''
CREATE TABLE IF NOT EXISTS Pages(
    id INTEGER PRIMARY KEY,
    url TEXT UNIQUE, 
    html TEXT,
    error iNTEGER,
    old_rank REAL,
    new_rank REAL)
''')

cur.execute('''CREATE TABLE IF NOT EXISTS Links(
    from_id INTEGER,
    to_id INTEGER)
''')

cur.execute('''CREATE TABLE IF NOT EXISTS Webs(
    url TEXT UNIQUE)
''')

cur.execute('SELECT id, url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')
row = cur.fetchone()

if row is not None:
    print('Restarting existing crawl. Remove spider.sqlite to start a fresh crawl.')
else:
    start_url = input('Enter web url or enter: ')
    if len(start_url) < 1:
        start_url = 'https://docs.python.org/3/howto/urllib2.html'    
    
    if start_url.endswith('/'):
        start_url = start_url[:-1]
    
    web = start_url

    if start_url.endswith('.htm') or start_url.endswith('.html'):
        pos = start_url.rfind('/')
        web = start_url[:pos]

    if len(web) > 1:
        cur.execute('INSERT OR IGNORE INTO Webs(url) VALUES (?)', (web, ))
        cur.execute('INSERT OR IGNORE INTO Pages(url, html, new_rank) VALUES (?, NULL, 1.0)', (start_url, ))
        conn.commit()

cur.execute('SELECT url FROM Webs')
webs = list()
for row in cur:
    webs.append(str(row[0]))

print(webs)

many = 0
while True:
    if many < 1:
        try:
            str_val = input('How many pages: ')
            if len(str_val) < 1:
                break
            many = int(str_val)
        except KeyboardInterrupt as expt:
            print('\nProgram interrupted by user..')
            break
    many -= 1
    
    try:
        cur.execute('SELECT id, url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')
        from_id, url = cur.fetchone()
    except:
        print('No unretrieved HTML pages found..')
        many = 0
        break
    
    print(from_id, url)

    cur.execute('DELETE from Links WHERE from_id=?', (from_id, ))
    
    try:
        document = urlopen(url, context=ctx)
        html = document.read()
                
        if document.getcode() != 200:
            print('Error on page:', document.getcode())
            cur.execute('UPDATE Pages SET error=? WHERE url=?', (document.getcode(), url))
        
        if document.info().get_content_type() != 'text/html':
            print('Ignore non text/html page')
            cur.execute('DELETE FROM Pages WHERE url=?', (url, ))
            cur.execute('UPDATE Pages SET error=0 WHERE url=?', (url, ))
            conn.commit()
            continue
        
        print('Length: (' + str(len(html)) + ')')

        soup = BeautifulSoup(html, 'html.parser')
    except:
        print('Unable to retrieve or parse page')
        cur.execute('UPDATE Pages SET error=-1 WHERE url=?', (url, ))
        conn.commit()
        continue

    cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES (?, NULL, 1.0)', (url, ))
    cur.execute('UPDATE Pages SET html=? WHERE url=?', (memoryview(html), url))
    conn.commit()

    tags = soup('a')
    count = 0

    for tag in tags:
        href = tag.get('href', None)
        
        if href is None:
            continue

        url_parse = urlparse(href)

        if len(url_parse.scheme) < 1:
            href = urljoin(url, href)
        
        ipos = href.find('#')
        if ipos > 1:
            href = href[:ipos]
        
        if href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif'):
            continue

        if href.endswith('/'):
            href = href[:-1]

        if len(href) < 1:
            continue

        found = False
        for web in webs:
            if href.startswith(web):
                found = True
                break
        if not found:
            continue 

        cur.execute('INSERT OR IGNORE INTO Pages(url, html, new_rank) VALUES (?, NULL, 1.0)', (href, ))
        count += 1
        conn.commit()
        print(f'{count}: {href}: {from_id}')

        cur.execute('SELECT id FROM Pages WHERE url=? LIMIT 1', (href, ))
        try:
            row = cur.fetchone()
            to_id = row[0]
            print(f'{count}: {href}: {from_id} - {to_id}')
        except:
            print('Could not retrieve id')
            continue
        
        cur.execute('INSERT OR IGNORE INTO Links (from_id, to_id) VALUES (?, ?)', (from_id, to_id))

    print(count)

cur.close()        