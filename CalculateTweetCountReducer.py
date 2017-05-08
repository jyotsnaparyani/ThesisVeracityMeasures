#!/usr/bin/env python

from operator import itemgetter
import sys

current_count = 0

for line in sys.stdin:
    line = line.strip()
    tweetcount, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    current_count += count
print '%s' % (current_count)
