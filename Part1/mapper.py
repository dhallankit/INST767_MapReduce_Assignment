#!/usr/bin/env python
import sys
import re
from collections import Counter
if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        words = re.findall('\w+', line)
        strng = str(Counter(zip(words,words[1:])))
        strng = strng[8:-1]
        dic = eval(strng)
        for k,v in dic.items():
            print("%s\t%d"%(k,v))