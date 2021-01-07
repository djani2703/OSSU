import sqlite3 
import time 
import zlib

how_many = int(input('How many to dump: '))

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Senders')

senders = dict()
for (id, sender) in cur:
    senders[id] = sender

cur.execute('SELECT id, subject FROM Subjects')

subjects = dict()
for (id, subject) in cur:
    subjects[id] = subject

cur.execute('SELECT id, guid, sender_id, subject_id, sent_at FROM Messages')

messages = dict()
for (id, guid, sender_id, subject_id, sent_at) in cur:
    messages[id] = (guid, sender_id, subject_id, sent_at)

print('Loaded messages =', len(messages), 'subjects =', len(subjects), 'senders =', len(senders))

send_counts = dict()
send_orgs = dict()

for (message_id, message) in list(messages.items()):
    sender = message[1]
    send_counts[sender] = send_counts.get(sender, 0) + 1
    pieces = senders[sender].split('@')
    
    if len(pieces) != 2:
        continue
    dns = pieces[1]
    send_orgs[dns] = send_orgs.get(dns, 0) + 1

print('Top', how_many, 'Email list participants:')

sorted_senders = sorted(send_counts, key=send_counts.get, reverse=True)

for sender in sorted_senders[:how_many]:
    print(senders[sender], send_counts[sender])
    if send_counts[sender] < 10:
        break

print('Top', how_many, 'Email list organizations:')

sorted_orgs = sorted(send_orgs, key=send_orgs.get, reverse=True)

for org in sorted_orgs[:how_many]:
    print(org, send_orgs[org])
    if send_orgs[org] < 10:
        break