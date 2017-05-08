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

totalTweetCount = readFileandReturnAnArray("foodTweetCount1", "r", True)
totalTweetCount = float(totalTweetCount)

geo_score = {}

for line in sys.stdin:
    line = line.strip()
    if line!="" and line is not None:
        cols = line.split('\t')
        topicId = line[0]
        if line[1:] is not None:
            location = line[1:]
        else:
            location = None

        if topicId in geo_score:
                existingValues = geo_score.get(topicId)
                if location is not "" and location != None and location not in existingValues and location!="noLocation":
                        geo_score[topicId].append(location)
        else:
                geo_score[topicId] = []
                if location is not "" and location != None and location!="noLocation":
                         geo_score[topicId].append(location)


for topic in geo_score.keys():
    list_of_values = geo_score[topic]
    length = len(list_of_values)
    final_score = float(length)/totalTweetCount
    print '%s\t%s'% (topic, final_score)
