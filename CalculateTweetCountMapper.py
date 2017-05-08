#!/usr/bin/env python

import sys,json


for line in sys.stdin:
    if len(line.strip()) > 1:
        print "%s\t%s" %("Tweet Count:",1)
