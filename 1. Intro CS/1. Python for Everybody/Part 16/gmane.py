    
import sqlite3, time, ssl, re
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse
from datetime import datetime, timedelta

try:
    import dateutil.parser as parser
except Exception as expt:
    print(f'Dateutil import error: {expt}')


def parse_mail_date(mail_date):
    try:
        pdate = parser.parse(tdate)
        test_at = test_at = pdate.isoformat()
        return test_at
    except Exception as expt:
        print('Error:', {expt})


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

base_url = 'http://mbox.dr-chuck.net/sakai.devel/'

cur.execute('''CREATE TABLE IF NOT EXISTS Messages(
    id INTEGER UNIQUE,
    email TEXT,
    sent_at TEXT,
    subject TEXT,
    headers TEXT,
    body TEXT)
''')

start = None
cur.execute('SELECT max(id) FROM Messages')

try:
    row = cur.fetchone()
    if row == (None, ):
        start = 0
    else:
        start = row[0]
except:
    start = 0

many, count, fail = 0, 0, 0

while True:
    if (many < 1):
        try:
            str_val = input('How many messages: ')
            if len(str_val) < 1:
                break
            many = int(str_val)
        except KeyboardInterrupt as ki_expt:
            print(f'Error: {ki_expt}')
            break
        except Exception as expt:
            print(f'Error: {expt}')
            break
    
    start += 1
    cur.execute('SELECT id FROM Messages WHERE id=?', (start, ))

    try:
        row = cur.fetchone()
        if row is not None:
            continue
    except:
        row = None
            
    many -= 1
    url = base_url + str(start) + '/' + str(start + 1)
    
    text = 'None'
    try:
        document = urlopen(url, None, timeout=30, context=ctx)
        text = document.read().decode()
        
        if document.getcode() != 200:
            print('Error code =', document.getcode(), url)
            break
    except Exception as expt:
        print('Unable to retrieve or parse page:', url)
        print('Error:', expt)
        fail = fail + 1
        if fail > 5: 
            break
        continue

    print(f'Length of {url}: {len(text)}')
    
    count += 1
    
    if not text.startswith('From '):
        print(text, '\nDidn\'t find \'From..\' in text..')
        fail += 1
        if fail > 5:
            break
        continue

    pos = text.find('\n\n')
    if pos > 0:
        headers = text[:pos]
        body = text[pos+2:]
    else:
        print(text, '\nCouldn\'t find break between headers and body..')
        fail += 1
        if fail > 5:
            break
        continue
    
    email = None

    pos_email = re.findall('\nFrom: .*<(\S+@\S+)>\n', headers)
    
    if not pos_email:
        pos_email = re.findall('\nFrom: (\S+@\S+)\n', headers)

    email = pos_email[0].strip().lower()
    email = email.replace('<', '')
    
    date = None

    pos_date = re.findall('\nDate: .*, (.*)\n', headers)
    if pos_date:
        tdate = pos_date[0]
        tdate = tdate[:26]

        try:
            sent_at = parse_mail_date(tdate)
        except:
            print(text, '\nParse fail..', tdate)
            fail += 1
            if fail > 5:
                break
            continue
    
    subject = None
    pos_subject = re.findall('\nSubject: (.*)\n', headers)

    if pos_subject:
        subject = pos_subject[0].strip().lower()

    fail = 0
    print(' ', email, sent_at, subject)

    cur.execute('''INSERT OR IGNORE INTO Messages(id, email, sent_at, subject, headers, body)
        VALUES (?, ?, ?, ?, ?, ?)''', (start, email, sent_at, subject, headers, body))

    if count % 5 == 0:
        conn.commit()
    
    if count % 100 == 0:
        time.sleep()

conn.commit()
cur.close()