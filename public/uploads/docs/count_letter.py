#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

'''

from string import ascii_lowercase     # ascii_lowercase =='abcdefghijklmnopqrstuvwxyz'
print "Nom du fichier"
with open('votrefichier.txt') as f:
    text = f.read().lower().strip()
    dic = {}
    for x in ascii_lowercase:
        dic[x] = text.count(x)
print dic