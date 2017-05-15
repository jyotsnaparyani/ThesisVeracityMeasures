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
    user_location = parsed_json_tweet['user']['location']
    dateTime = parsed_json_tweet['created_at'].lstrip().strip()
    dateTime = dateTime.encode('ascii', 'ignore')
    dateTimeList=dateTime.split()
    exactDate = dateTimeList[0] + dateTimeList[1]+dateTimeList[2]+dateTimeList[5]
    if user_location is not None:
        user_location = user_location.encode('ascii', 'ignore')
        location = user_location.strip().lstrip()
        topicfiles = ["foodtopic1", "foodtopic2", "foodtopic3"]
        for i in topicfiles:
                topics = readFileandReturnAnArray(i, "r", True)
                topicId = topics.pop(0)
                for keyword in topics:
                        if keyword in tweets_text  :
                                if location is not None and location is not '' and location is not "  " and location!="":
                                        print '%s\t%s\t%s' %(topicId,location,exactDate)
