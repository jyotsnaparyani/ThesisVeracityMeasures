#!/usr/bin/env python

import sys,json


for line in sys.stdin:
    if len(line.strip()) > 1:
        parsed_json_tweet = json.loads(line)
        dateTime = parsed_json_tweet['created_at'].lstrip().strip()
        dateTime = dateTime.encode('ascii', 'ignore')
        dateTimeList=dateTime.split()
        exactDate = dateTimeList[0] + dateTimeList[1]+dateTimeList[2]+dateTimeList[5]
        print "%s\t%s" %(exactDate,1)
