import sqlite3, time, re, zlib
from datetime import datetime, timedelta

try:
    import dateutil.parser as parser
except Exception as expt:
    print(f'Error: {expt}')

dns_mapping = dict()
mapping = dict()


def fix_sender(sender, all_senders=None):
    global dns_mapping
    global mapping

    if sender is None:
        return None
    sender = sender.strip().lower()    
    sender = sender.replace('<', '').replace('>', '')

    if all_senders is not None and sender.endswith('gmane.org'):
        pieces = sender.split('-')
        real_sender = None
        for curr_sender in all_senders:
            if curr_sender.startswith(pieces[0]):
                real_sender = sender
                sender = curr_sender
                break
        if real_sender is None:
            for curr_sender in mapping:
                if curr_sender.startswith(pieces[0]):
                    real_sender = sender
                    sender = mapping[curr_sender]
                    break
        if real_sender is None:
            sender = pieces[0]
    mpieces = sender.split('@')
    if len(mpieces) != 2:
        return sender
        
    dns = mpieces[1]
    pieces = dns.split('.')

    if dns[-4:] in ['.edu', '.com', '.org', '.net']:
        dns = '.'.join(pieces[-2:])
    else:
        dns = '.'.join(pieces[-3:])

    dns = dns_mapping.get(dns, dns)
    return mpieces[0] + '@' + dns

def parse_mail_date(mail_date):
    try:
        parse_date = parser.parse(tdate)
        test_at = parse_date.isoformat()
        return test_at
    except Exception as expt:
        pass
    
    pieces = mail_date.split()
    notz = " ".join(pieces[:4]).strip()

    dnotz = None
    for form in [ '%d %b %Y %H:%M:%S', '%d %b %Y %H:%M:%S',
        '%d %b %Y %H:%M', '%d %b %Y %H:%M', '%d %b %y %H:%M:%S',
        '%d %b %y %H:%M:%S', '%d %b %y %H:%M', '%d %b %y %H:%M' ] :
        try:
            dnotz = datetime.strptime(notz, form)
            break
        except:
            continue

    if dnotz is None:
        return None

    iso = dnotz.isoformat()

    tz = "+0000"
    try:
        tz = pieces[4]
        ival = int(tz) 
        if tz == '-0000' : tz = '+0000'
        tzh = tz[:3]
        tzm = tz[3:]
        tz = tzh + ":" + tzm
    except:
        pass
    return iso+tz

def parse_headers(header, all_senders=None):
    if header is None or len(header) < 1:
        return None
    
    sender = None

    tmp_headers = re.findall('\nFrom: .*<(\S+@\S+)>\n', header)
    if not tmp_headers:
        tmp_headers = re.findall('\nFrom: (\S+@\S+)\n', header)
    
    if tmp_headers:
        sender = tmp_headers[0]

    sender = fix_sender(sender, all_senders)

    tmp_date = re.findall('\nDate: .*, (.*)\n', header)

    sent_at = None

    if tmp_date:
        tdate = tmp_date[0]
        tdate = tdate[:26]
        
        try:
            sent_at = parse_mail_date(tdate)
        except Exception as expt:
            print(f'Date ignored: {expt}')
            return None

    subject = None

    tmp_subject = re.findall('\nSubject: (.*)\n', header)
    if tmp_subject:
        subject = tmp_subject[0].strip().lower()

    guid = None
    tmp_guid = re.findall('\nMessage-ID: (.*)\n', header)
    
    if tmp_guid:
        guid = tmp_guid[0].strip().lower()
    
    for entity in [sender, sent_at, subject, guid]:
        if entity is None:
            return None
    return (guid, sender, subject, sent_at)


conn_0 = sqlite3.connect('index.sqlite')
cur_0 = conn_0.cursor()

cur_0.execute('DROP TABLE IF EXISTS Messages')
cur_0.execute('DROP TABLE IF EXISTS Senders')
cur_0.execute('DROP TABLE IF EXISTS Subjects')
cur_0.execute('DROP TABLE IF EXISTS Replies')
    
cur_0.execute('''CREATE TABLE IF NOT EXISTS Messages(
    id INTEGER PRIMARY KEY,
    guid TEXT UNIQUE,
    sent_at INTEGER,
    sender_id INTEGER,
    subject_id INTEGER,
    headers BLOB,
    body BLOB)
''')

cur_0.execute('''CREATE TABLE IF NOT EXISTS Senders(
    id INTEGER PRIMARY KEY,
    sender TEXT UNIQUE)
''')

cur_0.execute('''CREATE TABLE IF NOT EXISTS Subjects(
    id INTEGER PRIMARY KEY,
    subject TEXT UNIQUE)
''')

cur_0.execute('''CREATE TABLE IF NOT EXISTS Replies(
    from_id INTEGER,
    to_id INTEGER)
''')

conn_1 = sqlite3.connect('mapping.sqlite')
cur_1 = conn_1.cursor()

cur_1.execute('SELECT old, new FROM DNSMapping')
for (old, new) in cur_1:
    old = old.strip().lower()
    new = new.strip().lower()
    dns_mapping[old] = new

print('DNS mapping:', dns_mapping) # -

cur_1.execute('SELECT old, new FROM Mapping')
for (old, new) in cur_1:
    old = fix_sender(old)
    new = fix_sender(new)
    mapping[old] = new

print('Mapping', mapping) 

conn_1.close()

conn_1 = sqlite3.connect('file:content.sqlite?mode=ro', uri=True)
cur_1 = conn_1.cursor()

all_senders = list()

cur_1.execute('SELECT email FROM Messages')
for (email, ) in cur_1:
    sender = fix_sender(email)
    if sender is None:
        continue
    if 'gmane.org' in sender:
        continue
    if sender in all_senders:
        continue
    all_senders.append(sender)
    
print('Loaded all senders', len(all_senders), 'mapping', len(mapping), 'and dns mapping', dns_mapping)

cur_1.execute('SELECT headers, body, sent_at FROM Messages ORDER BY sent_at')

senders, subjects, guids = dict(), dict(), dict()
count = 0

for (headers, body, sent_at) in cur_1:
    parsed_header = parse_headers(headers, all_senders)

    if not parse_headers:
        continue

    (guid, sender, subject, sent_at) = parsed_header

    sender = mapping.get(sender, sender)
    count += 1

    if count % 250 == 1:
        print(count, sent_at, sender)

    if 'gmane.org' in sender:
        print('Error in sender ===', sender)

    sender_id = senders.get(sender, None)
    subject_id = subjects.get(subject, None)
    guid_id = guids.get(guid, None)

    if sender_id is None:
        cur_0.execute('INSERT OR IGNORE INTO Senders(sender) VALUES (?)', (sender, ))
        conn_0.commit()
        cur_0.execute('SELECT id FROM Senders WHERE sender=?', (sender, ))
        
        try:
            (sender_id, ) = cur_0.fetchone()
            senders[sender] = sender_id
        except:
            print('Could not retrieve sender id', sender)
            break
    
    if subject_id is None:
        cur_0.execute('INSERT OR IGNORE INTO Subjects(subject) VALUES (?)', (subject, ))
        conn_0.commit()
        cur_0.execute('SELECT id FROM Subjects WHERE subject=? LIMIT 1', (subject, ))
    
        try:
            (subject_id, ) = cur_0.fetchone()
            subjects[subject] = subject_id
        except:
            print('Could not retrieve subject id', subject)
            break

    cur_0.execute('INSERT OR IGNORE INTO Messages(guid, sender_id, subject_id, sent_at, headers, body) VALUES (?, ?, ?, datetime(?), ?, ?)',
        (guid, sender_id, subject_id, sent_at, zlib.compress(headers.encode()), zlib.compress(body.encode())) )

    conn_0.commit()
    cur_0.execute('SELECT id FROM Messages WHERE guid=? LIMIT 1', (guid, ))
    
    try:
        (guid_id, ) = cur_0.fetchone()
        guids[guid] = guid_id
    except:
        print('Could not retrieve guid id..', guid)
        break

cur_0.close()
cur_1.close() 