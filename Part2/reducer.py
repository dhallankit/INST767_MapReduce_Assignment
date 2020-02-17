#!/usr/bin/env python
import sys
import re

if __name__ == "__main__":
    avg = 0.00
    sumval = 0
    fcount = 0
    for line in sys.stdin:
        word, key = line.split("], ")
        sum, count = word.replace('([', "").split(", ")
        sumval += int(sum)
        fcount += int(count)
    avg = float(sumval)/fcount
    print(round(avg,2), fcount)