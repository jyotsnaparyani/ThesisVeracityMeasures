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
        splitLine = line.split()
        topicId = splitLine[0]
        location = splitLine[1]
        date = splitLine[2]
        dateTopicId = date + " " + topicId


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
    spamIndex = 1.00/length
    print '%s\t%s'% (topic, spamIndex)
