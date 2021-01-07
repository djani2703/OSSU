import sqlite3, time, zlib

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('SELECT id, sender FROM Senders')

senders = dict()
for (id, sender) in cur:
    senders[id] = sender

cur.execute('SELECT id, guid, sender_id, subject_id, sent_at FROM Messages')

messages = dict()
for (id, guid, sender_id, subject_id, sent_at) in cur:
    messages[id] = (guid, sender_id, subject_id, sent_at)

print('Loaded messages =', len(messages), 'senders =', len(senders))

send_org = dict()
for (message_id, message) in list(messages.items()):
    sender = message[1]
    pieces = senders[sender].split('@')
    
    if len(pieces) != 2:
        continue

    dns = pieces[1]
    send_org[dns] = send_org.get(dns, 0) + 1

orgs = sorted(send_org, key=send_org.get, reverse=True)
orgs = orgs[:10]

print('Top 10 Organizations:', orgs)

counts, months = dict(), list()

for (message_id, message) in list(messages.items()):
    sender = message[1]
    pieces = senders[sender].split('@')
    if len(pieces) != 2:
        continue

    dns = pieces[1]
    if dns not in orgs:
        continue
    month = message[3][:7]

    if month not in months:
        months.append(month)

    key = (month, dns)
    counts[key] = counts.get(key, 0) + 1

months.sort()

fhand = open('gline.js','w')
fhand.write("gline = [ ['Month'")

for org in orgs:
    fhand.write(",'"+org+"'")
fhand.write("]")

for month in months:
    fhand.write(",\n['"+month+"'")
    for org in orgs:
        key = (month, org)
        val = counts.get(key, 0)
        fhand.write("," + str(val))
    fhand.write("]");

fhand.write("\n];\n")
fhand.close()

print("Output written to gline.js")
print("Open gline.htm to visualize the data.")