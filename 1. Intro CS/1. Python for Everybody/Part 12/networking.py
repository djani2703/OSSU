# -*- coding: utf-8 -*-

# An HTTP request in Python:
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()

# Representing simple string:
char = 'H'
ascii_num_value = ord(char)
print(f'char is equal {ascii_num_value}')

# In Python 3, all the strings are unicode:
x = 'Привіт Світ'
type_str = type(x)
x =u'Привіт Світ'
type_unicode = type(x)
print('Type str is equal type unicode: {}\n'.format(type_str is type_unicode))

# Using urllib in Python:
import urllib.request, urllib.parse, urllib.error

url_hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in url_hand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

# Reading web pages:
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())

# Reading binary files using urllib:
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()

# Using BeautifulSoup:
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors:
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))