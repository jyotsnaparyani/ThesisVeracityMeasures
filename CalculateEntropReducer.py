#!/usr/bin/env python

from operator import itemgetter
import sys

en_score = {}

for line in sys.stdin:
    line = line.strip()
    topicId, score = line.split('\t')

    if topicId in en_score:
        en_score[topicId].append(float(score))
    else:
        en_score[topicId] = []
        en_score[topicId].append(float(score))


for topic in en_score.keys():
    avg_score = sum(en_score[topic])/len(en_score[topic])
    print '%s\t%s'% (topic, avg_score)
