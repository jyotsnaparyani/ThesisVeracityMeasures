#!/usr/bin/env python


import sys,json

def readFileandReturnAnArray(fileName, readMode, isLower):
    with open(fileName, readMode) as readHandle:
        for line in readHandle.readlines():
            lineRead = line
            if isLower:
                lineRead = lineRead.lower()
            count = (lineRead.strip().lstrip())
    readHandle.close()
    return count


geo_score = {}

for line in sys.stdin:
    line = line.strip()
    if line!="" and line is not None:
        cols = line.split()
        topicId = cols[0]
        location=cols[1]
        date=cols[2]
        dateTopicId=date + " " + topicId


        if dateTopicId in geo_score:
                existingValues = geo_score.get(dateTopicId)
                if location is not "" and location != None and location not in existingValues:
                        geo_score[dateTopicId].append(location)
        else:
                geo_score[dateTopicId] = []
                if location is not "" and location != None:
                        geo_score[dateTopicId].append(location)


for topic in geo_score.keys():
    list_of_values = geo_score[topic]
    length = len(list_of_values)
    print '%s\t%s'% (topic, length)
