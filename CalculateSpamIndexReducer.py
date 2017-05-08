#!/usr/bin/env python

import sys

def readFileandReturnAnArray(fileName, readMode, isLower):

    with open(fileName, readMode) as readHandle:
        for line in readHandle.readlines():
            lineRead = line
            if isLower:
                lineRead = lineRead.lower()
            count = (lineRead.strip().lstrip())
    readHandle.close()
    return count

totalTweetCount = readFileandReturnAnArray("tweetCount", "r", True)
totalTweetCount = float(totalTweetCount)

geo_score = {}

for line in sys.stdin:
    line = line.strip()
    if line!="" and line is not None:
        topicId, username = line.split('\t')
        if topicId in geo_score:
                existingValues = geo_score.get(topicId)
                if username is not "" and username != None and username not in existingValues:
                        geo_score[topicId].append(username)
        else:
                geo_score[topicId] = []
                if username is not "" and username != None:
                        geo_score[topicId].append(username)


for topic in geo_score.keys():
    list_of_values = geo_score[topic]
    length = len(list_of_values)
    spamIndex = 1.00/length
    final_score = float(spamIndex)/totalTweetCount
    print '%s\t%s'% (topic, final_score)
