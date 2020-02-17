#!/usr/bin/env python
import sys
# import StringIO

if __name__ == "__main__":
    count = 0
    sum = 0
    for line in sys.stdin:
        number = int(line.strip())
        sum += number
        count += 1
    print([sum, count], 1)
    