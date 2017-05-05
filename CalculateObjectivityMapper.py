#!/usr/bin/env python



from textblob import TextBlob

import sys

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
    tweets_text = line
    topicfiles = ["foodtopic1", "foodtopic2", "foodtopic3"]
    for i in topicfiles:
        alphabet = readFileandReturnAnArray(i, "r", True)
        topicId = alphabet.pop(0)
        for symbol in alphabet:
            if symbol in tweets_text  :
                objectivityTruthful = TextBlob(tweets_text)
                print '%s\t%s' % (topicId, objectivityTruthful.subjectivity)
