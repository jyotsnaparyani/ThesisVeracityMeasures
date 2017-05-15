#!/usr/bin/env python


import sys,json

def readFileandReturnAnArray(fileName, readMode, isLower):
    myArray=[]
    with open(fileName, readMode) as readHandle:
        for line in readHandle.readlines():
            lineRead = line
            if isLower:
                lineRead = lineRead.lower()
            myArray.append(lineRead.strip().lstrip())
    readHandle.close()
    return myArray


for line in sys.stdin:
    parsed_json_tweet = json.loads(line)
    tweets_text = parsed_json_tweet['text'].lstrip().strip()
    user_handle = parsed_json_tweet['user']['screen_name'].strip()
    user_handle = user_handle.encode('ascii', 'ignore')
    dateTime = parsed_json_tweet['created_at'].lstrip().strip()
    dateTime = dateTime.encode('ascii', 'ignore')
    dateTimeList=dateTime.split()
    exactDate = dateTimeList[0] + dateTimeList[1]+dateTimeList[2]+dateTimeList[5]
    if user_handle is not None:
        username = user_handle.strip().lstrip()
    topicfiles = ["foodtopic1", "foodtopic2", "foodtopic3"]
    for i in topicfiles:
        topics = readFileandReturnAnArray(i, "r", True)
        topicId = topics.pop(0)
        for keyword in topics:
                if keyword in tweets_text  :
                        print '%s\t%s\t%s' %(topicId,username,exactDate)
