# -*- coding: utf-8 -*-

import socket, re

# INTERNAL API's:
def get_socket_document():
    url = input('Input url: ').strip()

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        regex_patt = '^http[s]*://[w.]*(\S+)/'
        host = re.findall(regex_patt, url)[0]
        
        mysock.connect((host, 80))
    except Exception as expt:
        print('Socket error:', expt)

    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    
    return mysock

def get_ulrlib_document():
    url = input('Input url: ').strip()
    url_hand = urllib.request.urlopen(url)
    
    return url_hand


# Exercise 1:
mysock = get_socket_document() 

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()

# Exercise 2:
mysock = get_socket_document()
lim, all_doc = 3000, ''

while True:
    data = mysock.recv(1)
    if len(data) < 1:
        break
    all_doc += data.decode()

visible = lim if len(all_doc) > lim else len(all_doc) 
print(f'{all_doc[0:lim:1]}...[{visible} symbols of {len(all_doc)}]')

# Exercise 3:
import urllib.request

all_doc, counts, lim = '', 0, 3000
url_hand = get_ulrlib_document()
for line in url_hand:
    line = line.decode()
    if counts + len(line) < lim:
        all_doc += line
        counts += len(line)
    else:
        all_doc += line[0:lim-counts]
        counts = lim
print(all_doc)

# Exercise 4:
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Input url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0
tags = soup('p')
for tag in tags:
    count += 1
print(f'Count of <p> tag = {count}')

# Exercise 5:
mysock = get_socket_document()
all_doc = ''

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    all_doc += data.decode()

content = all_doc.split('\r\n\r\n')[1]
print(content)