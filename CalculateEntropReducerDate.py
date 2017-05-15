#!/usr/bin/env python

from operator import itemgetter
import sys

en_score = {}

for line in sys.stdin:
    line = line.strip()
    if line!="" and line is not None:
        splitLine = line.split()
        topicId = splitLine[0]
        score = splitLine[1]
        date = splitLine[2]
        dateTopicId = date + " " + topicId

        if dateTopicId in en_score:
                en_score[dateTopicId].append(float(score))
        else:
                en_score[dateTopicId] = []
                en_score[dateTopicId].append(float(score))


for topic in en_score.keys():
    avg_score = sum(en_score[topic])/len(en_score[topic])
    print '%s\t%s'% (topic, avg_score)
