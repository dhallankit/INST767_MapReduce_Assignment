#!/usr/bin/env python
import sys
import re

worddict = {}
for line in sys.stdin:
    line = line.strip()
    words, count = line.split("\t")
    words = words.replace("(('",'')
    words = words.replace("),",'')
    words = words.replace("'",'')
    if words in worddict:
        worddict[words]+= int(count)
    else:
        worddict[words]=int(count)

for k,v in worddict.items():
    print(k, v)
