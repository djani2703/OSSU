import sqlite3, time, zlib, string

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('SELECT id, subject FROM Subjects')

subjects = dict()

for (id, subject) in cur:
    subjects[id] = subject

cur.execute('SELECT subject_id FROM Messages')

counts = dict()

for (subject_id, ) in cur:
    text = subjects[subject_id]
    text = text.translate(str.maketrans('','', string.punctuation))
    text = text.translate(str.maketrans('','', '1234567890'))
    text = text.strip().lower()
    words = text.split()
    
    for word in words:
        if len(word) < 4:
            continue
        counts[word] = counts.get(word, 0) + 1

sorted_words = sorted(counts, key=counts.get, reverse=True)
highest, lowest = None, None

for word in sorted_words[:100]:
    if highest is None or highest < counts[word]:
        highest = counts[word]
    if lowest is None or lowest > counts[word]:
        lowest = counts[word]
print('Range of counts:', highest, lowest)

print('lowest:', lowest, 'highest:', highest)

big_size, small_size = 80, 20

fhand = open('gword.js', 'w')
fhand.write('gword = [')
first = True

for word in sorted_words[:100]:
    if not first:
        fhand.write(',\n')
    first = False
    size = counts[word]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * big_size) + small_size)
    fhand.write("{text: '" + word + "', size: " + str(size) + "}")
fhand.write('\n];\n') 

print('Output written to gword.js.')
print('Open gword.htm in a browser to see the visualization.')