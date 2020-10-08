#!/usr/bin/env python3
import os

text = ''
path = "/media/alex/Data/Code/CodeSource/Code/PyProj/byteOfPython/files/"

os.mkdir(path)

for i in range(0, 5):

    crea = open('files/text.py{0}'.format(i), 'w')

    crea.write(text)
    crea.close()

crea = open('text.txt')

while True:
    line = crea.readline()
    if len(line) == 0:
        break
    print(line, end='')

